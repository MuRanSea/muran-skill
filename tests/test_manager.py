import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
from muran import Manager, atomic_json, check_uv_locks, git, normalized, repository_lock, run, uv_executable
from validation import documentation_status, forbidden_public_paths, validate


def skill(root, name='example', body='A test skill.'):
    folder = root / 'skills' / name
    folder.mkdir(parents=True, exist_ok=True)
    (folder / 'SKILL.md').write_text(f'---\nname: {name}\ndescription: A fixture skill for testing.\n---\n\n{body}\n', encoding='utf-8')
    return folder


def copy_manager(root):
    shutil.copytree(ROOT / 'scripts', root / 'scripts', ignore=shutil.ignore_patterns('__pycache__'))
    for name in ('muran.ps1', 'pyproject.toml', 'uv.lock', '.python-version', '.gitignore'):
        shutil.copy2(ROOT / name, root / name)


@unittest.skipUnless(os.name == 'nt', 'Windows junction semantics required')
class ManagerTests(unittest.TestCase):
    def setUp(self):
        self.base = ROOT / '.cache' / 'tests'
        self.base.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(prefix='manager-', dir=self.base)
        self.temp = Path(self.temporary.name).resolve()
        self.assertTrue(self.temp.is_relative_to(self.base.resolve()))
        self.repo, self.home = self.temp / 'repo with space', self.temp / 'home with space'
        self.repo.mkdir()
        self.home.mkdir()
        self.manager = Manager(self.repo, self.home, self.temp / 'state')
        self.manager.detect = lambda: ['codex', 'claude-code', 'pi', 'opencode', 'grok']
        self.manager.task = lambda *args, **kwargs: {'ok': True}
        skill(self.repo)

    def tearDown(self):
        # shutil on Python 3.12 never recurses into Windows junctions. Unlink
        # explicitly as well so fixtures cannot affect another test's source.
        for folder in (self.manager.shared, self.manager.claude, self.manager.grok):
            if folder.exists():
                for path in folder.iterdir():
                    if path.is_junction() or path.is_symlink():
                        os.rmdir(path)
        self.assertTrue(self.temp.is_relative_to(self.base.resolve()))
        self.temporary.cleanup()

    def test_links_are_shared_and_install_is_idempotent(self):
        first = self.manager.sync()
        self.assertTrue(first['ok'])
        self.assertEqual(first['created'], 3)
        modified = self.repo / 'skills/example/shared.txt'
        modified.write_text('new content', encoding='utf-8')
        for root in (self.manager.shared, self.manager.claude, self.manager.grok):
            self.assertTrue((root / 'example').is_junction())
            self.assertEqual((root / 'example/shared.txt').read_text(), 'new content')
        again = self.manager.sync()
        self.assertEqual(again['created'], 0)
        self.assertEqual(again['reused'], 3)

    def test_add_delete_and_missing_link_repair(self):
        self.manager.sync()
        os.rmdir(self.manager.shared / 'example')
        self.assertEqual(self.manager.sync()['created'], 1)
        skill(self.repo, 'second')
        self.assertEqual(self.manager.sync()['created'], 3)
        shutil.rmtree(self.repo / 'skills/example')
        self.assertEqual(self.manager.sync()['removed'], 3)
        self.assertFalse(os.path.lexists(self.manager.shared / 'example'))

    def test_conflicting_directory_is_not_overwritten(self):
        conflict = self.manager.shared / 'example'
        conflict.mkdir(parents=True)
        (conflict / 'keep.txt').write_text('mine')
        result = self.manager.sync()
        self.assertFalse(result['ok'])
        self.assertEqual((conflict / 'keep.txt').read_text(), 'mine')

    def test_adopts_existing_alias_without_owning_it(self):
        self.manager.shared.mkdir(parents=True)
        self.manager.claude.mkdir(parents=True)
        self.manager.make_link(self.repo / 'skills/example', self.manager.shared / 'example')
        self.manager.make_link(self.manager.shared / 'example', self.manager.claude / 'example')
        self.manager.sync()
        self.manager.uninstall()
        self.assertTrue((self.manager.claude / 'example').is_junction())
        self.assertTrue((self.manager.shared / 'example').is_junction())

    def test_changed_owned_link_is_not_removed(self):
        self.manager.sync()
        path = self.manager.shared / 'example'
        os.rmdir(path)
        unrelated = self.home / 'unrelated'
        unrelated.mkdir()
        (unrelated / 'keep.txt').write_text('keep')
        self.manager.make_link(unrelated, path)
        result = self.manager.uninstall()
        self.assertFalse(result['ok'])
        self.assertEqual((unrelated / 'keep.txt').read_text(), 'keep')
        self.assertTrue(path.is_junction())

    def test_uninstall_does_not_remove_source(self):
        self.manager.sync()
        self.assertTrue(self.manager.uninstall()['ok'])
        self.assertTrue((self.repo / 'skills/example/SKILL.md').is_file())
        self.assertFalse(os.path.lexists(self.manager.shared / 'example'))

    def test_uninstall_stops_repository_and_document_schedules(self):
        self.manager.sync()
        with patch.object(self.manager, 'task', return_value={'ok': True}) as task:
            self.assertTrue(self.manager.uninstall()['ok'])
        task.assert_any_call('disable')
        task.assert_any_call('disable', documents=True)

    def test_document_rename_migrates_ignored_snapshot_and_adopted_alias(self):
        legacy = skill(self.repo, 'volcengine-docs')
        (legacy / 'generated').mkdir()
        (legacy / 'generated/retained.txt').write_text('local snapshot')
        self.manager.sync()
        adopted = self.manager.claude / 'volcengine-docs'
        os.rmdir(adopted)
        self.manager.make_link(self.manager.shared / 'volcengine-docs', adopted)
        self.manager.sync()
        current = skill(self.repo, 'ai-platform-docs')
        shutil.copy2(ROOT / 'skills/ai-platform-docs/providers.json', current / 'providers.json')
        (legacy / 'SKILL.md').unlink()
        result = self.manager.sync()
        self.assertTrue(result['ok'], result)
        self.assertFalse(legacy.exists())
        self.assertEqual((current / 'generated/retained.txt').read_text(), 'local snapshot')
        for parent in (self.manager.shared, self.manager.claude, self.manager.grok):
            self.assertFalse(os.path.lexists(parent / 'volcengine-docs'))
            self.assertEqual((parent / 'ai-platform-docs').resolve(), current.resolve())

    def test_corrupt_state_cannot_remove_arbitrary_links(self):
        outside = self.home / 'not-a-skill'
        self.manager.make_link(self.repo / 'skills/example', outside)
        record = {'name': 'example', 'owned': True, 'path': str(outside), 'source': str(self.repo / 'skills/example')}
        self.assertFalse(self.manager.remove_owned_link(record))
        self.assertTrue(outside.is_junction())
        os.rmdir(outside)

    def test_operation_lock_prevents_overlap(self):
        with repository_lock(self.manager.state_dir):
            with self.assertRaisesRegex(RuntimeError, 'Another'):
                with repository_lock(self.manager.state_dir):
                    self.fail('Second lock acquired')

    def git_fixture(self):
        copy_manager(self.repo)
        git(self.repo, 'init', '-b', 'main')
        git(self.repo, 'config', 'user.name', 'Fixture')
        git(self.repo, 'config', 'user.email', 'fixture@example.invalid')
        git(self.repo, 'add', '.')
        git(self.repo, 'commit', '-m', 'initial')
        remote = self.temp / 'remote.git'
        git(self.temp, 'init', '--bare', str(remote))
        git(self.repo, 'remote', 'add', 'origin', str(remote))
        git(self.repo, 'push', '-u', 'origin', 'main')
        self.publisher = self.temp / 'publisher'
        git(self.temp, 'clone', '--branch', 'main', str(remote), str(self.publisher))
        git(self.publisher, 'config', 'user.name', 'Fixture')
        git(self.publisher, 'config', 'user.email', 'fixture@example.invalid')
        self.manager.sync()
        return git(self.repo, 'rev-parse', 'HEAD').strip()

    def publish(self, body='Updated remote content.'):
        skill(self.publisher, body=body)
        git(self.publisher, 'add', '.')
        git(self.publisher, 'commit', '-m', 'update')
        git(self.publisher, 'push', 'origin', 'main')

    def test_valid_remote_update_and_new_skill(self):
        before = self.git_fixture()
        skill(self.publisher, 'new-skill')
        self.publish()
        result = self.manager.update()
        self.assertEqual(result['status'], 'updated')
        self.assertNotEqual(git(self.repo, 'rev-parse', 'HEAD').strip(), before)
        self.assertTrue((self.manager.grok / 'new-skill').is_junction())
        self.assertEqual(self.manager.update()['status'], 'unchanged')

    def test_dirty_tree_is_preserved_and_links_still_sync(self):
        before = self.git_fixture()
        self.publish()
        file = self.repo / 'skills/example/SKILL.md'
        file.write_text(file.read_text() + '\nLocal edit.\n')
        skill(self.repo, 'local-skill')
        result = self.manager.update()
        self.assertEqual(result['status'], 'skipped_dirty')
        self.assertEqual(git(self.repo, 'rev-parse', 'HEAD').strip(), before)
        self.assertIn('Local edit.', file.read_text())
        self.assertTrue((self.manager.shared / 'local-skill').is_junction())

    def test_divergence_is_not_merged(self):
        self.git_fixture()
        self.publish()
        (self.repo / 'local.txt').write_text('local')
        git(self.repo, 'add', '.')
        git(self.repo, 'commit', '-m', 'local')
        before = git(self.repo, 'rev-parse', 'HEAD')
        self.assertEqual(self.manager.update()['status'], 'skipped_diverged')
        self.assertEqual(git(self.repo, 'rev-parse', 'HEAD'), before)

    def test_network_failure_preserves_checkout(self):
        before = self.git_fixture()
        git(self.repo, 'remote', 'set-url', 'origin', str(self.temp / 'unavailable.git'))
        result = self.manager.update()
        self.assertEqual(result['status'], 'failed')
        self.assertFalse(result['ok'])
        self.assertEqual(git(self.repo, 'rev-parse', 'HEAD').strip(), before)
        self.assertTrue((self.manager.shared / 'example').is_junction())

    def test_invalid_candidate_does_not_change_checkout(self):
        before = self.git_fixture()
        (self.publisher / 'skills/example/SKILL.md').write_text('invalid frontmatter')
        git(self.publisher, 'add', '.')
        git(self.publisher, 'commit', '-m', 'invalid')
        git(self.publisher, 'push', 'origin', 'main')
        result = self.manager.update()
        self.assertEqual(result['status'], 'failed')
        self.assertIn('validation failed', result['error'])
        self.assertEqual(git(self.repo, 'rev-parse', 'HEAD').strip(), before)

    def test_excluded_public_content_rejects_candidate(self):
        before = self.git_fixture()
        generated = self.publisher / 'skills/ai-platform-docs/generated'
        generated.mkdir(parents=True)
        (generated / 'document.md').write_text('must stay local')
        git(self.publisher, 'add', '--force', 'skills/ai-platform-docs/generated/document.md')
        self.publish()
        result = self.manager.update()
        self.assertFalse(result['ok'])
        self.assertIn('excluded public', result['error'])
        self.assertEqual(git(self.repo, 'rev-parse', 'HEAD').strip(), before)

    def test_feature_branch_is_not_switched(self):
        self.git_fixture()
        git(self.repo, 'switch', '-c', 'feature')
        self.assertEqual(self.manager.update()['status'], 'skipped_branch')
        self.assertEqual(git(self.repo, 'branch', '--show-current').strip(), 'feature')

    def test_stale_dependency_lock_rejects_remote_update(self):
        before = self.git_fixture()
        project = self.publisher / 'pyproject.toml'
        project.write_text(project.read_text().replace('PyYAML>=6.0.2', 'PyYAML>=6.0.3'))
        self.publish()
        result = self.manager.update()
        self.assertFalse(result['ok'])
        # With a cold registry cache, offline uv can reject stale metadata while
        # resolving dependencies, before emitting its more specific lock message.
        self.assertRegex(result['error'], r'lockfile|No solution found when resolving dependencies')
        self.assertEqual(git(self.repo, 'rev-parse', 'HEAD').strip(), before)
        self.assertTrue((self.manager.shared / 'example').is_junction())

    def test_missing_lock_rejects_remote_update(self):
        before = self.git_fixture()
        (self.publisher / 'uv.lock').unlink()
        self.publish()
        result = self.manager.update()
        self.assertIn('Missing uv project file: uv.lock', result['error'])
        self.assertEqual(git(self.repo, 'rev-parse', 'HEAD').strip(), before)


@unittest.skipUnless(os.name == 'nt', 'Windows launcher and scheduled tasks required')
class UvRuntimeTests(unittest.TestCase):
    def setUp(self):
        self.base = ROOT / '.cache/tests'
        self.base.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(prefix='uv-', dir=self.base)
        self.temp = Path(self.temporary.name).resolve()
        self.repo = self.temp / 'repo with space'
        self.repo.mkdir()
        copy_manager(self.repo)
        self.state = self.temp / 'state with space'
        self.shell = str(Path(os.environ['SystemRoot']) / 'System32/WindowsPowerShell/v1.0/powershell.exe')

    def tearDown(self):
        self.assertTrue(self.temp.is_relative_to(self.base.resolve()))
        self.temporary.cleanup()

    def launcher(self, **overrides):
        # Exercise the real entrypoint with no uv or Python in PATH. A foreign
        # current project must not affect the explicit checkout passed to uv.
        foreign = self.temp / 'pyproject.toml'
        foreign.write_text('invalid TOML from another project')
        env = {**os.environ, 'MURAN_UV': uv_executable(), 'MURAN_PYTHON': 'not-used.exe',
               'PATH': str(Path(self.shell).parent) + os.pathsep + str(Path(os.environ['SystemRoot']) / 'System32'),
               'UV_OFFLINE': '1', **overrides}
        return subprocess.run([self.shell, '-NoProfile', '-NonInteractive', '-ExecutionPolicy', 'Bypass',
                               '-File', str(self.repo / 'muran.ps1'), 'auto-update', 'status',
                               '--state-dir', str(self.state), '--task-name', 'MuranSkill-Absent-' + self.temp.name],
                              cwd=self.temp, env=env, text=True, encoding='utf-8', errors='replace',
                              capture_output=True, timeout=60)

    def test_launcher_bootstraps_without_system_python_or_active_environment(self):
        result = self.launcher()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)['status'], 'absent')
        self.assertTrue((self.repo / '.venv/pyvenv.cfg').is_file())
        second = self.launcher()
        self.assertEqual(second.returncode, 0, second.stderr)
        self.assertNotIn('Creating virtual environment', second.stderr)

    def test_missing_uv_reports_install_command(self):
        result = self.launcher(MURAN_UV=str(self.temp / 'missing/uv.exe'))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('winget install --id astral-sh.uv', result.stderr)
        self.assertFalse(self.state.exists())

    def test_stale_lock_fails_before_manager_runs(self):
        lock = self.repo / 'uv.lock'
        before = lock.read_bytes()
        project = self.repo / 'pyproject.toml'
        project.write_text(project.read_text().replace('PyYAML>=6.0.2', 'PyYAML>=6.0.3'))
        result = self.launcher()
        self.assertNotEqual(result.returncode, 0)
        self.assertRegex(result.stderr, r'lockfile|No solution found when resolving dependencies')
        self.assertFalse(self.state.exists())
        self.assertEqual(lock.read_bytes(), before)

    def test_script_is_standalone_outside_repository(self):
        destination = self.temp / 'standalone skill/scripts'
        shutil.copytree(ROOT / 'skills/ai-platform-docs/scripts', destination, ignore=shutil.ignore_patterns('__pycache__'))
        shutil.copy2(ROOT / 'skills/ai-platform-docs/providers.json', destination.parent / 'providers.json')
        output = run([uv_executable(), 'run', '--locked', '--script', str(destination / 'build_all.py'), '--help'],
                     cwd=self.temp, env={'UV_OFFLINE': '1'})
        self.assertIn('--fetch', output)

    def test_task_ownership_allows_runtime_migration_only_for_same_checkout(self):
        prefix = subprocess.list2cmdline(['-NoProfile', '-NonInteractive', '-WindowStyle', 'Hidden',
                                         '-ExecutionPolicy', 'Bypass', '-File', str(self.repo / 'scripts/run-update.ps1')])
        suffix = subprocess.list2cmdline(['-Repo', str(self.repo), '-StateDir', str(self.state)])
        legacy = prefix + ' -Python "C:\\old runtime\\python.exe" ' + suffix
        current = prefix + ' -Uv "C:\\new runtime\\uv.exe" ' + suffix
        def task(args, exe=None):
            return {'Actions': [{'Execute': exe or self.shell, 'Arguments': args}]}
        cases = [task(legacy), task(current), task(current.replace('new runtime', 'relocated')),
                 task(current.replace(str(self.repo), str(self.temp / 'another repo'))),
                 task(current + ' -Extra unrelated'), task(current.replace('uv.exe', 'other.exe')),
                 task(current, 'cmd.exe'), task(current.replace('state with space', 'different state')),
                 {'Actions': [task(current)['Actions'][0], task(legacy)['Actions'][0]]}]
        script = (". $env:MURAN_ACTION_HELPER; $cases = ConvertFrom-Json $env:MURAN_TASK_CASES; "
                  "@($cases | ForEach-Object { Test-MuranTaskAction $_ $env:MURAN_TEST_EXE "
                  "$env:MURAN_TEST_PREFIX $env:MURAN_TEST_SUFFIX }) | ConvertTo-Json -Compress")
        results = json.loads(run([self.shell, '-NoProfile', '-NonInteractive', '-Command', script],
                                 env={'MURAN_ACTION_HELPER': str(ROOT / 'scripts/task-action.ps1'),
                                      'MURAN_TASK_CASES': json.dumps(cases), 'MURAN_TEST_EXE': self.shell,
                                      'MURAN_TEST_PREFIX': prefix, 'MURAN_TEST_SUFFIX': suffix}))
        self.assertEqual(results, [True, True, True, False, False, False, False, False, False])


class ValidationTests(unittest.TestCase):
    def test_uv_locks_are_current_without_network_or_cache(self):
        with tempfile.TemporaryDirectory() as cache:
            with patch.dict(os.environ, {'UV_CACHE_DIR': cache}):
                check_uv_locks(ROOT)

    def test_imported_catalog(self):
        skills, errors = validate(ROOT)
        self.assertEqual(errors, [])
        imported = json.loads((ROOT / 'sources.json').read_text(encoding='utf-8'))['mattpocock']['skills']
        names = {s['name'] for s in skills}
        self.assertTrue({s['name'] for s in imported}.issubset(names))
        self.assertIn('ai-platform-docs', names)

    def test_public_exclusions(self):
        forbidden = ['skills/ai-platform-docs/generated/INDEX.md', 'skills/ai-platform-docs/.cache/doc/x.md', '.env', 'source.pdf']
        self.assertEqual(forbidden_public_paths(forbidden + ['skills/ai-platform-docs/SKILL.md', '.env.example']), forbidden)

    def test_frontmatter_delimiter_inside_a_string(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            folder = skill(root)
            (folder / 'SKILL.md').write_text('---\nname: example\ndescription: "A --- separator example"\n---\n\nBody.\n', encoding='utf-8')
            self.assertEqual(validate(root)[1], [])

    def test_broken_resource_and_dependency(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            skill(root, body='[Reference](missing.md)\nCall the Skill tool with "missing-skill".')
            _, errors = validate(root)
            self.assertTrue(any('missing resource' in e for e in errors))
            self.assertTrue(any('missing skill dependency' in e for e in errors))


class DocumentationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sys.path.insert(0, str(ROOT / 'skills/ai-platform-docs/scripts'))
        spec = importlib.util.spec_from_file_location('volc_builder', ROOT / 'skills/ai-platform-docs/scripts/build_all.py')
        cls.builder = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.builder)

    def test_snapshot_hash_detects_modified_documents(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            generated = root / 'skills/ai-platform-docs/generated'
            (generated / 'chapters/tos').mkdir(parents=True)
            (generated / 'INDEX.md').write_text('index')
            chapter = generated / 'chapters/tos/example.md'
            chapter.write_text('original')
            self.builder.write_snapshot(generated, 'fixture')
            self.assertTrue(documentation_status(root)['ready'])
            chapter.write_text('modified')
            self.assertFalse(documentation_status(root)['ready'])

    def test_failed_publish_restores_original(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            old, candidate, backup = root / 'old', root / 'candidate', root / 'backup'
            old.mkdir()
            candidate.mkdir()
            (old / 'sentinel.txt').write_text('old')
            real_replace = os.replace
            def fail_candidate(source, destination):
                if Path(source) == candidate:
                    raise OSError('injected rename failure')
                return real_replace(source, destination)
            with patch.object(self.builder.os, 'replace', side_effect=fail_candidate):
                with self.assertRaises(OSError):
                    self.builder.publish_generated(candidate, old, backup)
            self.assertEqual((old / 'sentinel.txt').read_text(), 'old')


if __name__ == '__main__':
    unittest.main()
