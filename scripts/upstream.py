"""Import Matt's formal catalog in isolation, preserving local adaptations."""
from __future__ import annotations

import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import tarfile
import tempfile
import urllib.request

from muran import Manager, git, now
from validation import NAME, forbidden_public_paths

UPSTREAM = 'https://github.com/mattpocock/skills'
COMPATIBILITY = ('\n\n## Harness compatibility\n\n'
    'When these instructions say to call the Skill tool, use your agent’s native skill loader. '
    'If it has no such tool, read the named skill’s `SKILL.md` from the sibling skill directory '
    '(resolve paths from this skill directory, not the project working directory). '
    'Use available native tools with equivalent behavior. '
    'If subagents are unavailable, perform the passes sequentially and disclose that they were not independent.\n')
EXPLICIT = ('\nThis skill is intended for explicit user invocation. Harnesses that ignore '
    '`disable-model-invocation` should follow this intent; this text is not a runtime permission control.\n')


def download(commit):
    if not re.fullmatch(r'[0-9a-f]{40}', commit):
        raise ValueError('Invalid upstream commit')
    url = f'https://codeload.github.com/mattpocock/skills/tar.gz/{commit}'
    with urllib.request.urlopen(url, timeout=60) as response:
        data = response.read(64 * 1024 * 1024 + 1)
    if len(data) > 64 * 1024 * 1024:
        raise ValueError('Upstream archive exceeds size limit')
    files = {}
    with tarfile.open(fileobj=io.BytesIO(data), mode='r:gz') as archive:
        total = 0
        for entry in archive:
            if entry.isdir():
                continue
            path = PurePosixPath(entry.name)
            if path.is_absolute() or '..' in path.parts or '\\' in entry.name or ':' in entry.name:
                raise ValueError('Unsafe upstream archive entry')
            name = PurePosixPath(*path.parts[1:]).as_posix()
            if not entry.isfile():
                if name.startswith(('skills/', '.claude-plugin/')) or name == 'LICENSE':
                    raise ValueError('Linked upstream skill resources are unsupported')
                continue  # For example the upstream root AGENTS.md -> CLAUDE.md alias.
            total += entry.size
            if total > 128 * 1024 * 1024:
                raise ValueError('Expanded upstream archive exceeds size limit')
            if name in files:
                raise ValueError('Duplicate upstream archive entry')
            files[name] = archive.extractfile(entry).read()
    return files


def adapted_tree(files):
    plugin = json.loads(files['.claude-plugin/plugin.json'])
    result, records, seen = {}, [], set()
    for raw in plugin['skills']:
        path = PurePosixPath(raw.removeprefix('./'))
        name = path.name
        if path.is_absolute() or '..' in path.parts or not NAME.fullmatch(name) or name in seen:
            raise ValueError('Invalid or duplicate upstream skill')
        seen.add(name)
        prefix = path.as_posix() + '/'
        for source, body in files.items():
            if source.startswith(prefix):
                result[f'skills/{name}/' + source[len(prefix):]] = body
        skill = f'skills/{name}/SKILL.md'
        original = result[skill]
        body = original.decode('utf-8').replace('\r\n', '\n')
        if any(word in body for word in ('Skill tool', 'subagent', 'sub-agent')):
            body += COMPATIBILITY
        if 'disable-model-invocation: true' in body:
            result[f'skills/{name}/agents/openai.yaml'] = b'policy:\n  allow_implicit_invocation: false\n'
            body += EXPLICIT
        result[skill] = body.encode('utf-8')
        records.append({'name': name, 'upstream_path': path.as_posix(),
                        'original_skill_sha256': hashlib.sha256(original).hexdigest()})
    if not seen:
        raise ValueError('Empty upstream catalog')
    result['licenses/mattpocock-MIT.txt'] = files['LICENSE']
    if forbidden_public_paths(list(result)):
        raise ValueError('Upstream contains excluded public files')
    return result, {'version': plugin['version'], 'skills': records}


def merge_file(path, base, local, incoming):
    if local == base:
        return incoming
    if incoming == base or local == incoming:
        return local
    if None in (base, local, incoming) or any(b'\x00' in b for b in (base, local, incoming)):
        raise ValueError(f'Upstream conflict: {path}')
    with tempfile.TemporaryDirectory(prefix='muran-merge-') as temp:
        paths = [Path(temp) / name for name in ('local', 'base', 'incoming')]
        for file, data in zip(paths, (local, base, incoming)):
            file.write_bytes(data)
        process = subprocess.run(['git', 'merge-file', '-p', *map(str, paths)], capture_output=True)
        if process.returncode:
            raise ValueError(f'Upstream conflict: {path}')
        return process.stdout


def local_blob(root, revision, path):
    # Read only committed content. Ignored snapshots and local files never enter the import.
    names = git(root, 'ls-tree', '-r', '--name-only', revision, '--', path).splitlines()
    if path not in names:
        return None
    mode = git(root, 'ls-tree', revision, '--', path).split()[0]
    if mode not in ('100644', '100755'):
        raise ValueError(f'Unsupported local file mode: {path}')
    return git(root, 'show', f'{revision}:{path}', binary=True)


def sync_upstream(manager):
    """A rejected push or merge conflict never edits the installed checkout."""
    root = manager.root
    if git(root, 'symbolic-ref', '--short', 'HEAD').strip() != 'main':
        return {'ok': True, 'status': 'skipped_branch'}
    if git(root, 'status', '--porcelain', '--untracked-files=all').strip():
        return {'ok': True, 'status': 'skipped_dirty'}
    before = git(root, 'rev-parse', 'HEAD').strip()
    if before != git(root, 'rev-parse', 'origin/main').strip():
        return {'ok': True, 'status': 'skipped_diverged'}
    provenance = json.loads(git(root, 'show', 'HEAD:sources.json'))
    record = provenance['mattpocock']
    if record['repository'] != UPSTREAM:
        raise ValueError('Unexpected Matt upstream repository')
    latest = git(root, 'ls-remote', UPSTREAM + '.git', 'HEAD').split()[0]
    if latest == record['commit']:
        return {'ok': True, 'status': 'unchanged', 'upstream_commit': latest}
    base, _ = adapted_tree(download(record['commit']))
    incoming, metadata = adapted_tree(download(latest))
    # Disallow a newly imported skill from taking over a separately maintained skill.
    old_names = {entry['name'] for entry in record['skills']}
    for entry in metadata['skills']:
        if entry['name'] not in old_names and git(root, 'ls-tree', 'HEAD', '--', f"skills/{entry['name']}").strip():
            raise ValueError(f"New upstream skill conflicts with local skill: {entry['name']}")
    merged = {path: merge_file(path, base.get(path), local_blob(root, before, path), incoming.get(path))
              for path in sorted(base.keys() | incoming.keys())}
    # Deleting a catalog entry must not silently discard locally added resources.
    retired = old_names - {entry['name'] for entry in metadata['skills']}
    for name in retired:
        local_paths = git(root, 'ls-tree', '-r', '--name-only', before, '--', f'skills/{name}').splitlines()
        if any(path not in base or merged.get(path) is not None for path in local_paths):
            raise ValueError(f'Retired upstream skill has local adaptations: {name}')
    provenance['mattpocock'] = {**record, **metadata, 'commit': latest}
    merged['sources.json'] = (json.dumps(provenance, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
    remote = git(root, 'remote', 'get-url', '--push', 'origin').strip()
    with tempfile.TemporaryDirectory(prefix='upstream-', dir=manager.state_dir) as temp:
        checkout = Path(temp) / 'repo'
        git(root, 'clone', '--no-local', '--quiet', str(root), str(checkout))
        git(checkout, 'checkout', '--detach', before)
        for key in ('user.name', 'user.email'):
            git(checkout, 'config', key, git(root, 'config', '--get', key).strip())
        for name, data in merged.items():
            path = checkout / name
            if not path.resolve().is_relative_to(checkout.resolve()):
                raise ValueError('Upstream destination escapes checkout')
            if data is None:
                path.unlink(missing_ok=True)
                # Remove empty retired directories so skill validation sees the new catalog.
                parent = path.parent
                while parent != checkout and parent.exists() and not any(parent.iterdir()):
                    parent.rmdir()
                    parent = parent.parent
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(data)
        git(checkout, 'add', '-A')
        changed = git(checkout, 'diff', '--cached', '--name-only').splitlines()
        if forbidden_public_paths(changed) or not set(changed).issubset(merged):
            raise ValueError('Unexpected files in automatic commit')
        git(checkout, 'diff', '--cached', '--check')
        git(checkout, 'commit', '-m', f'chore(skills): 同步 Matt 技能 {latest[:12]}')
        candidate = git(checkout, 'rev-parse', 'HEAD').strip()
        Manager(checkout, manager.home, manager.state_dir).validate_candidate(candidate)
        # Catch user edits during network calls before publishing any automatic commit.
        if (git(root, 'status', '--porcelain', '--untracked-files=all').strip()
                or git(root, 'rev-parse', 'HEAD').strip() != before
                or git(root, 'symbolic-ref', '--short', 'HEAD').strip() != 'main'):
            return {'ok': True, 'status': 'skipped_changed_during_update'}
        # Regular fast-forward push; a concurrent remote update rejects this push.
        git(checkout, 'push', remote, 'HEAD:refs/heads/main', timeout=120)
        updated = manager.update()
        return {'ok': updated['ok'], 'status': 'published', 'commit': candidate,
                'upstream_commit': latest, 'changed_files': len(changed), 'local_update': updated}


def daily(manager):
    initial = manager.update()
    result = {'command': 'daily-update', 'ok': initial['ok'], 'repository': initial}
    if initial['ok'] and initial['status'] in ('updated', 'unchanged'):
        try:
            result['upstream'] = sync_upstream(manager)
            result['ok'] = result['upstream']['ok']
        except (RuntimeError, ValueError, OSError, KeyError, tarfile.TarError, subprocess.SubprocessError) as exc:
            result.update(ok=False, upstream={'status': 'failed', 'error': str(exc)})
    else:
        result['upstream'] = {'status': 'skipped_repository_not_ready'}
    state = manager.load_state()
    state['last_upstream_update'] = {'time': now(), **result['upstream']}
    manager.save(state)
    return result
