"""Windows skill repository manager. PowerShell is the user-facing entrypoint."""
from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import io
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tarfile
import tempfile

from validation import NAME, documentation_status, forbidden_public_paths, validate

ROOT = Path(__file__).resolve().parent.parent
AGENTS = {'codex': 'codex', 'claude-code': 'claude', 'pi': 'pi', 'opencode': 'opencode', 'grok': 'grok'}
TASK_NAME = 'MuranSkill-DailyUpdate'
DOCS_TASK_NAME = 'MuranSkill-DocsUpdate'


def now():
    return datetime.now(timezone.utc).isoformat()


def normalized(path):
    return os.path.normcase(os.path.abspath(str(path).removeprefix('\\\\?\\')))


def link_target(path):
    try:
        return normalized(os.readlink(path)) if path.is_junction() or path.is_symlink() else None
    except OSError:
        return None


def atomic_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix('.tmp')
    temp.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    os.replace(temp, path)


def run(command, *, cwd=None, timeout=60, env=None, binary=False):
    merged = os.environ.copy()
    merged.update({'GIT_TERMINAL_PROMPT': '0', 'GCM_INTERACTIVE': 'Never', 'PYTHONUTF8': '1'})
    if env:
        merged.update(env)
    result = subprocess.run(command, cwd=cwd, env=merged, capture_output=True,
                            text=not binary, encoding=None if binary else 'utf-8',
                            errors=None if binary else 'replace', timeout=timeout,
                            creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0)
    if result.returncode:
        detail = result.stderr if not binary else result.stderr.decode('utf-8', 'replace')
        raise RuntimeError(detail.strip() or f'{Path(command[0]).name} exited with {result.returncode}')
    return result.stdout


def git(root, *args, **kwargs):
    return run(['git', '-c', 'credential.interactive=false', '-C', str(root), *args], **kwargs)


def uv_executable():
    executable = shutil.which(os.environ.get('MURAN_UV') or 'uv')
    if not executable:
        raise RuntimeError('uv is required; install uv and reopen PowerShell')
    return str(Path(executable).resolve())


def check_uv_locks(root):
    """Check metadata without executing candidate code or changing its locks."""
    for required in ('pyproject.toml', 'uv.lock', '.python-version'):
        if not (root / required).is_file():
            raise ValueError(f'Missing uv project file: {required}')
    command = [uv_executable(), 'lock', '--check', '--offline', '--no-build',
               '--no-python-downloads', '--python', sys.executable, '--directory', str(root)]
    run(command)
    builder = root / 'skills/ai-platform-docs/scripts/build_all.py'
    if builder.exists():
        run([*command, '--script', str(builder)])


@contextmanager
def repository_lock(state_dir):
    import msvcrt
    state_dir.mkdir(parents=True, exist_ok=True)
    with (state_dir / 'manager.lock').open('a+b') as handle:
        if handle.tell() == 0:
            handle.write(b'0')
            handle.flush()
        handle.seek(0)
        try:
            msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
        except OSError as exc:
            raise RuntimeError('Another muran-skill operation is running') from exc
        try:
            yield
        finally:
            handle.seek(0)
            msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)


class Manager:
    def __init__(self, root=ROOT, home=None, state_dir=None):
        self.root = Path(root).resolve()
        self.home = Path(home or Path.home()).resolve()
        self.state_dir = Path(state_dir or Path(os.environ.get('LOCALAPPDATA', self.home / 'AppData/Local')) / 'muran-skill').resolve()
        self.state_path = self.state_dir / 'state.json'
        self.shared = self.home / '.agents' / 'skills'
        self.claude = Path(os.environ.get('CLAUDE_CONFIG_DIR', self.home / '.claude')) / 'skills'
        self.grok = self.home / '.grok' / 'skills'

    def load_state(self):
        if not self.state_path.exists():
            return {'schema_version': 1, 'repository': str(self.root), 'agents': [], 'links': []}
        data = json.loads(self.state_path.read_text(encoding='utf-8'))
        if data.get('schema_version') != 1 or normalized(data.get('repository', '')) != normalized(self.root):
            raise RuntimeError('State belongs to a different repository or unsupported version; use its uninstall command first')
        return data

    def save(self, state):
        atomic_json(self.state_path, state)

    def log(self, result):
        self.state_dir.mkdir(parents=True, exist_ok=True)
        log = self.state_dir / 'operations.jsonl'
        if log.exists() and log.stat().st_size > 1024 * 1024:
            os.replace(log, log.with_suffix('.previous.jsonl'))
        with log.open('a', encoding='utf-8') as stream:
            stream.write(json.dumps({'time': now(), **result}, ensure_ascii=False) + '\n')

    def detect(self):
        return [name for name, executable in AGENTS.items()
                if any(shutil.which(executable + suffix) for suffix in ('', '.cmd', '.ps1', '.exe'))]

    def destinations(self, agents):
        result = []
        for agent in agents:
            path = self.claude if agent == 'claude-code' else self.grok if agent == 'grok' else self.shared
            if path not in result:
                result.append(path)
        return result

    def safe_record(self, record):
        name = record.get('name', '')
        if not isinstance(name, str) or not NAME.fullmatch(name):
            return False
        path = Path(record.get('path', ''))
        return (normalized(path) in {normalized(p / name) for p in (self.shared, self.claude, self.grok)}
                and normalized(record.get('source', '')) == normalized(self.root / 'skills' / name))

    def remove_owned_link(self, record):
        if not record.get('owned') or not self.safe_record(record):
            return False
        path = Path(record['path'])
        if link_target(path) != normalized(record['source']):
            return False
        # rmdir on a junction removes the reparse point, never its contents.
        os.rmdir(path)
        return True

    def make_link(self, source, destination):
        destination.parent.mkdir(parents=True, exist_ok=True)
        run(['powershell.exe', '-NoProfile', '-NonInteractive', '-Command',
             "$ErrorActionPreference='Stop'; New-Item -ItemType Junction -Path $env:MURAN_LINK_PATH -Target $env:MURAN_SOURCE_PATH | Out-Null"],
            env={'MURAN_LINK_PATH': str(destination), 'MURAN_SOURCE_PATH': str(source)})
        if normalized(destination.resolve()) != normalized(source.resolve()):
            raise RuntimeError(f'Junction verification failed: {destination}')

    def sync(self, agents=None):
        self.migrate_document_skill()
        skills, errors = validate(self.root)
        if errors:
            return {'command': 'sync', 'ok': False, 'errors': errors}
        state = self.load_state()
        selected = list(dict.fromkeys(agents if agents is not None else state['agents'] + self.detect()))
        if not selected:
            return {'command': 'sync', 'ok': False, 'errors': ['No installed agent found; select --agents explicitly']}
        unknown = set(selected) - AGENTS.keys()
        if unknown:
            raise ValueError(f'Unknown agents: {sorted(unknown)}')
        state['agents'] = selected
        previous = {normalized(r['path']): r for r in state['links'] if self.safe_record(r)}
        desired, new_links, conflicts = set(), [], []
        created, removed, reused = 0, 0, 0
        for skill in skills:
            source = Path(skill['path']).resolve()
            for folder in self.destinations(selected):
                dest = folder / skill['name']
                key = normalized(dest)
                desired.add(key)
                old = previous.get(key)
                target = link_target(dest)
                exists = os.path.lexists(dest)
                if target and normalized(dest.resolve()) == normalized(source):
                    record = {'name': skill['name'], 'path': str(dest), 'source': str(source), 'owned': bool(old and old.get('owned') and target == normalized(source))}
                    new_links.append(record)
                    reused += 1
                elif not exists:
                    self.make_link(source, dest)
                    record = {'name': skill['name'], 'path': str(dest), 'source': str(source), 'owned': True}
                    new_links.append(record)
                    created += 1
                else:
                    conflicts.append(str(dest))
                    if old:
                        new_links.append(old)
                # Persist each successful ownership change; interrupted installations can resume.
                state['links'] = new_links + [r for k, r in previous.items() if k not in desired]
                self.save(state)
        for key, record in previous.items():
            if key in desired:
                continue
            path = Path(record['path'])
            if self.remove_owned_link(record):
                removed += 1
            elif record.get('owned') and os.path.lexists(path):
                conflicts.append(str(path))
                new_links.append(record)
        state['links'] = new_links
        self.save(state)
        return {'command': 'sync', 'ok': not conflicts, 'skills': len(skills), 'agents': selected,
                'created': created, 'reused': reused, 'removed': removed, 'conflicts': conflicts}

    def migrate_document_skill(self):
        """Retain ignored snapshots when Git replaces the old skill entrypoint."""
        current = self.root / 'skills/ai-platform-docs'
        legacy = self.root / 'skills/volcengine-docs'
        if not (current / 'SKILL.md').is_file() or (legacy / 'SKILL.md').exists():
            return
        if legacy.exists():
            if legacy.is_junction() or legacy.is_symlink():
                raise ValueError('Legacy source directory is a link; migration stopped')
            for name in ('generated', '.cache'):
                source, destination = legacy / name, current / name
                if source.exists():
                    if source.is_junction() or source.is_symlink() or source.resolve().parent != legacy.resolve():
                        raise ValueError('Unexpected legacy documentation target')
                    if destination.exists():
                        raise ValueError(f'Both old and new documentation caches exist: {name}; reconcile them before sync')
                    os.replace(source, destination)
            if not any(legacy.iterdir()):
                legacy.rmdir()
        state = self.load_state()
        aliases = {normalized(legacy)} | {normalized(p / 'volcengine-docs') for p in (self.shared, self.claude, self.grok)}
        for record in state['links']:
            # The explicit rename also retires adopted aliases that still point
            # into this old skill. Unrelated or retargeted links are preserved.
            if record.get('name') == 'volcengine-docs' and not record.get('owned') and self.safe_record(record):
                path = Path(record['path'])
                if link_target(path) in aliases:
                    os.rmdir(path)

    def validate_candidate(self, ref):
        names = git(self.root, 'ls-tree', '-r', '--name-only', ref).splitlines()
        forbidden = forbidden_public_paths(names)
        if forbidden:
            raise ValueError(f'Candidate contains excluded public files: {forbidden[:5]}')
        archive = git(self.root, 'archive', '--format=tar', ref, binary=True)
        with tempfile.TemporaryDirectory(prefix='candidate-', dir=self.state_dir) as temp:
            target = Path(temp)
            with tarfile.open(fileobj=io.BytesIO(archive)) as bundle:
                for member in bundle.getmembers():
                    destination = (target / member.name).resolve()
                    if not destination.is_relative_to(target.resolve()) or not (member.isfile() or member.isdir()):
                        raise ValueError('Candidate contains unsafe archive entry')
                bundle.extractall(target, filter='data')
            _, errors = validate(target)
            for required in ('muran.ps1', 'scripts/muran.py', 'scripts/upstream.py', 'scripts/validation.py', 'scripts/scheduled-task.ps1', 'scripts/run-update.ps1', 'scripts/run-docs-update.ps1', 'scripts/task-action.ps1'):
                if not (target / required).is_file():
                    errors.append(f'Missing manager file: {required}')
            if errors:
                raise ValueError('Candidate validation failed: ' + '; '.join(errors[:10]))
            check_uv_locks(target)
            run(['powershell.exe', '-NoProfile', '-NonInteractive', '-Command',
                 "$ErrorActionPreference='Stop'; Get-ChildItem -LiteralPath $env:MURAN_CANDIDATE -Filter *.ps1 -Recurse | ForEach-Object { $tokens=$null; $parseErrors=$null; [void][System.Management.Automation.Language.Parser]::ParseFile($_.FullName,[ref]$tokens,[ref]$parseErrors); if ($parseErrors) { throw ($parseErrors | Out-String) } }"],
                env={'MURAN_CANDIDATE': str(target)})

    def update(self):
        before = None
        status, error = 'unchanged', None
        try:
            branch = git(self.root, 'symbolic-ref', '--short', 'HEAD').strip()
            before = git(self.root, 'rev-parse', 'HEAD').strip()
            if branch != 'main':
                status = 'skipped_branch'
            elif git(self.root, 'status', '--porcelain', '--untracked-files=all').strip():
                status = 'skipped_dirty'
            else:
                git(self.root, 'fetch', '--no-tags', 'origin', '+refs/heads/main:refs/remotes/origin/main')
                candidate = git(self.root, 'rev-parse', 'origin/main').strip()
                if before != candidate:
                    try:
                        git(self.root, 'merge-base', '--is-ancestor', before, candidate)
                    except RuntimeError:
                        status = 'skipped_diverged'
                    else:
                        self.validate_candidate(candidate)
                        # Another tool may have edited the working tree during the fetch or validation.
                        if (git(self.root, 'status', '--porcelain', '--untracked-files=all').strip()
                                or git(self.root, 'rev-parse', 'HEAD').strip() != before
                                or git(self.root, 'symbolic-ref', '--short', 'HEAD').strip() != 'main'):
                            status = 'skipped_changed_during_update'
                        else:
                            git(self.root, 'merge', '--ff-only', '--no-edit', candidate)
                            status = 'updated'
        except (RuntimeError, ValueError, OSError, subprocess.TimeoutExpired) as exc:
            status, error = 'failed', str(exc)
        synchronization = self.sync()
        result = {'command': 'update', 'ok': error is None and synchronization['ok'], 'status': status,
                  'previous_commit': before, 'sync': synchronization}
        if error:
            result['error'] = error
        state = self.load_state()
        state['last_update'] = {'time': now(), 'status': status, 'ok': result['ok'], 'error': error}
        self.save(state)
        return result

    def task(self, action, task_name=TASK_NAME, *, documents=False):
        if documents and task_name == TASK_NAME:
            task_name = DOCS_TASK_NAME
        runner = self.root / 'scripts' / ('run-docs-update.ps1' if documents else 'run-update.ps1')
        prefix = ['-NoProfile', '-NonInteractive', '-WindowStyle', 'Hidden', '-ExecutionPolicy', 'Bypass', '-File', str(runner)]
        suffix = ['-Repo', str(self.root), '-StateDir', str(self.state_dir)]
        arguments = subprocess.list2cmdline([*prefix, '-Uv', uv_executable(), *suffix])
        env = {'MURAN_TASK_ACTION': action, 'MURAN_TASK_NAME': task_name, 'MURAN_TASK_ARGUMENTS': arguments,
               'MURAN_TASK_PREFIX': subprocess.list2cmdline(prefix), 'MURAN_TASK_SUFFIX': subprocess.list2cmdline(suffix),
               'MURAN_TASK_TIME': '09:30' if documents else '09:00',
               'MURAN_TASK_TIMEOUT': '120' if documents else '10',
               'MURAN_TASK_EXECUTABLE': str(Path(os.environ['SystemRoot']) / 'System32/WindowsPowerShell/v1.0/powershell.exe')}
        raw = run(['powershell.exe', '-NoProfile', '-NonInteractive', '-ExecutionPolicy', 'Bypass', '-File', str(self.root / 'scripts' / 'scheduled-task.ps1')], env=env)
        return json.loads(raw)

    def uninstall(self):
        state = self.load_state()
        removed, retained, remaining = [], [], []
        # Only remove the default task if the action still belongs to this checkout.
        task = self.task('disable')
        docs_task = self.task('disable', documents=True)
        for record in state['links']:
            if self.remove_owned_link(record):
                removed.append(record['path'])
            elif record.get('owned') and os.path.lexists(record['path']):
                retained.append(record['path'])
                remaining.append(record)
        state['links'], state['agents'] = remaining, []
        self.save(state)
        return {'command': 'uninstall', 'ok': not retained, 'removed': removed, 'retained': retained, 'task': task, 'docs_task': docs_task}

    def build_docs(self, action, source=None, fetch=False):
        self.migrate_document_skill()
        builder = self.root / 'skills/ai-platform-docs/scripts/build_all.py'
        command = [sys.executable, '-B', '-X', 'utf8', str(builder)]
        if action == 'import':
            if not source:
                raise ValueError('docs import requires a source directory')
            command += ['--import-from', str(source)]
        if fetch or action == 'update':
            command += ['--fetch']
        if action == 'update':
            command += ['--if-changed']
        try:
            output = run(command, timeout=7100)
            (self.state_dir / 'docs-build.log').write_text(output[-64000:], encoding='utf-8')
            build_result = json.loads(output.strip().splitlines()[-1])
            docs = documentation_status(self.root)
            result = {'command': 'docs', 'action': action, 'ok': docs['ready'], **build_result, **docs}
        except (RuntimeError, OSError, ValueError, subprocess.TimeoutExpired) as exc:
            result = {'command': 'docs', 'action': action, 'ok': False, 'status': 'failed', 'error': str(exc)[-8000:]}
        state = self.load_state()
        state['last_docs_update'] = {'time': now(), **result}
        self.save(state)
        return result

    def doctor(self):
        skills, errors = validate(self.root)
        state = self.load_state()
        links = []
        for skill in skills:
            for parent in self.destinations(state['agents']):
                path = parent / skill['name']
                good = bool(link_target(path)) and normalized(path.resolve()) == normalized(skill['path'])
                links.append({'path': str(path), 'valid': good})
                if not good:
                    errors.append(f'Missing or conflicting link: {path}')
        if not state['agents']:
            errors.append('No agents registered; run install')
        docs = documentation_status(self.root) if any(s['name'] == 'ai-platform-docs' for s in skills) else None
        if docs and not docs['ready']:
            errors.append('AI platform documentation missing or invalid; run docs update')
        if state.get('last_docs_update', {}).get('ok') is False:
            errors.append('Last document rebuild failed; the previous snapshot may still be usable')
        if state.get('last_upstream_update', {}).get('status') == 'failed':
            errors.append('Last Matt upstream update failed; inspect last_upstream_update')
        dependencies = {name: bool(shutil.which(name)) for name in ('git', 'powershell.exe')}
        dependencies['uv'] = bool(shutil.which(os.environ.get('MURAN_UV') or 'uv'))
        dependencies['runtime_3_12'] = sys.version_info[:2] == (3, 12)
        dependencies['pypdfium2'] = importlib.util.find_spec('pypdfium2') is not None
        if not all(dependencies.values()):
            errors.append('A required executable or uv runtime dependency is missing')
        try:
            check_uv_locks(self.root)
            dependencies['uv_locks_current'] = True
        except (RuntimeError, ValueError, OSError, subprocess.TimeoutExpired) as exc:
            dependencies['uv_locks_current'] = False
            errors.append(f'uv lock validation failed: {exc}')
        return {'command': 'doctor', 'ok': not errors, 'skills': len(skills), 'agents': state['agents'], 'links': links,
                'documentation': docs, 'dependencies': dependencies, 'last_update': state.get('last_update'),
                'last_docs_update': state.get('last_docs_update'),
                'last_upstream_update': state.get('last_upstream_update'), 'errors': errors}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['install', 'sync', 'update', 'daily-update', 'doctor', 'auto-update', 'uninstall', 'docs'])
    parser.add_argument('action', nargs='?')
    parser.add_argument('source', nargs='?')
    parser.add_argument('--agents', nargs='+', choices=list(AGENTS))
    parser.add_argument('--home', type=Path)
    parser.add_argument('--state-dir', type=Path)
    parser.add_argument('--task-name', default=TASK_NAME)
    parser.add_argument('--fetch', action='store_true')
    parser.add_argument('--json', action='store_true')
    parser.add_argument('--quiet', action='store_true')
    args = parser.parse_args()
    if os.name != 'nt':
        parser.error('This release supports native Windows only')
    manager = Manager(home=args.home, state_dir=args.state_dir)
    try:
        with repository_lock(manager.state_dir):
            if args.command in ('install', 'sync'):
                result = manager.sync(args.agents)
                result['command'] = args.command
            elif args.command == 'update':
                result = manager.update()
            elif args.command == 'daily-update':
                from upstream import daily
                result = daily(manager)
            elif args.command == 'doctor':
                result = manager.doctor()
                try:
                    result['task'] = manager.task('status')
                    result['docs_task'] = manager.task('status', documents=True)
                    if not result['docs_task'].get('ok', True):
                        result['ok'] = False
                        result['errors'].append('Documentation scheduled task action does not belong to this checkout')
                    if not result['task'].get('ok', True):
                        result['ok'] = False
                        result['errors'].append('Scheduled task action does not belong to this checkout')
                except RuntimeError as exc:
                    result['task'] = {'status': 'unavailable', 'reason': str(exc)}
                    result['ok'] = False
                    result['errors'].append('Could not inspect the scheduled task')
            elif args.command == 'uninstall':
                result = manager.uninstall()
            elif args.command == 'auto-update':
                if args.action not in ('enable', 'disable', 'status'):
                    parser.error('auto-update requires enable, disable or status')
                result = manager.task(args.action, args.task_name)
            else:
                if args.action == 'status':
                    result = documentation_status(ROOT)
                    result['ok'] = result['ready']
                elif args.action in ('build', 'import', 'update'):
                    result = manager.build_docs(args.action, args.source, args.fetch)
                elif args.action == 'auto-update':
                    if args.source not in ('enable', 'disable', 'status'):
                        parser.error('docs auto-update requires enable, disable or status')
                    result = manager.task(args.source, args.task_name, documents=True)
                else:
                    parser.error('docs requires update, build [--fetch], import PATH [--fetch], status or auto-update enable/disable/status')
            manager.log(result)
    except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as exc:
        result = {'command': args.command, 'ok': False, 'error': str(exc)}
        manager.log(result)
    if not args.quiet or not result.get('ok', True):
        print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result.get('ok', True) else 1


if __name__ == '__main__':
    sys.exit(main())
