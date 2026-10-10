"""CI selection against real Git history and snapshot validation through its CLI."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'scripts/ci_validate.py'
GENERATED = 'skills/ai-platform-docs/generated/'


class CiTests(unittest.TestCase):
    def setUp(self):
        parent = ROOT / '.cache/tests'
        parent.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix='ci-', dir=parent)
        self.base = Path(self.temp.name).resolve()
        self.repo = self.base / 'repo with space'
        self.repo.mkdir()
        self.event_path = self.base / 'event.json'
        self.output = self.base / 'output.txt'
        self.git('init', '-b', 'main')
        self.git('config', 'user.name', 'Fixture')
        self.git('config', 'user.email', 'fixture@example.invalid')
        self.git('config', 'commit.gpgsign', 'false')
        self.write('scripts/runtime.py', 'print("original")\n')
        self.write(GENERATED + 'INDEX.md', '# Index\n')
        self.write(GENERATED + 'chapters/example/page.md', '# Original\n')
        self.snapshot()
        self.initial = self.commit()

    def tearDown(self):
        self.assertTrue(self.base.is_relative_to((ROOT / '.cache/tests').resolve()))
        self.temp.cleanup()

    def git(self, *args):
        return subprocess.run(['git', *args], cwd=self.repo, check=True, capture_output=True,
                              text=True, encoding='utf-8').stdout.strip()

    def write(self, name, text):
        path = self.repo / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding='utf-8')

    def snapshot(self):
        folder = self.repo / GENERATED
        files = {p.relative_to(folder).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                 for p in folder.rglob('*.md')}
        self.write(GENERATED + 'snapshot.json', json.dumps({
            'files': files, 'built_at': 'fixture', 'origin': 'fixture'}))

    def commit(self):
        self.git('add', '-A')
        self.git('commit', '-qm', 'fixture')
        return self.git('rev-parse', 'HEAD')

    def invoke(self, command, event_name='push', event=None, code=0):
        self.event_path.write_text(json.dumps(event), encoding='utf-8')
        self.output.unlink(missing_ok=True)
        env = {**os.environ, 'GITHUB_EVENT_NAME': event_name, 'GITHUB_EVENT_PATH': str(self.event_path),
               'GITHUB_OUTPUT': str(self.output), 'PYTHONUTF8': '1', 'PYTHONDONTWRITEBYTECODE': '1'}
        result = subprocess.run([sys.executable, str(SCRIPT), '--root', str(self.repo), command],
                                capture_output=True, text=True, encoding='utf-8', env=env, timeout=40)
        self.assertEqual(result.returncode, code, result.stderr + result.stdout)
        value = json.loads(result.stdout)
        if command == 'select':
            self.assertEqual(self.output.read_text(encoding='utf-8').strip(),
                             'full_tests=' + str(value['full_tests']).lower())
        return value

    def test_generated_markdown_add_delete_and_manifest_update_use_light_checks(self):
        (self.repo / GENERATED / 'chapters/example/page.md').unlink()
        self.write(GENERATED + 'chapters/example/新文档 空格.md', '# Updated\n')
        self.snapshot()
        self.commit()
        result = self.invoke('select', event={'before': self.initial})
        self.assertFalse(result['full_tests'])
        self.assertEqual(result['changed_files'], 3)

    def test_other_paths_always_run_full_suite(self):
        names = ['scripts/runtime.py', 'tests/test_groups.py', 'pyproject.toml', 'uv.lock',
                 '.github/workflows/validate.yml', 'skills/ai-platform-docs/providers.json',
                 'skills/matt/example/SKILL.md', 'README.md', GENERATED + 'unexpected.py',
                 GENERATED + 'metadata.json']
        for name in names:
            with self.subTest(path=name):
                before = self.git('rev-parse', 'HEAD')
                self.write(name, 'changed\n')
                self.commit()
                self.assertTrue(self.invoke('select', event={'before': before})['full_tests'])

    def test_push_includes_code_changed_before_the_latest_document_commit(self):
        self.write('scripts/runtime.py', 'print("changed")\n')
        self.commit()
        self.write(GENERATED + 'INDEX.md', '# Updated\n')
        self.commit()
        self.assertTrue(self.invoke('select', event={'before': self.initial})['full_tests'])

    def test_pull_request_includes_all_commits(self):
        self.write('scripts/runtime.py', 'print("changed")\n')
        self.commit()
        self.write(GENERATED + 'INDEX.md', '# Updated\n')
        self.commit()
        event = {'pull_request': {'base': {'sha': self.initial}}}
        self.assertTrue(self.invoke('select', 'pull_request', event)['full_tests'])

    def test_pull_request_excludes_changes_only_on_base_and_handles_merge_checkout(self):
        self.git('switch', '-c', 'feature')
        self.write(GENERATED + 'INDEX.md', '# Updated\n')
        self.commit()
        self.git('switch', 'main')
        self.write('scripts/runtime.py', 'print("base changed")\n')
        base = self.commit()
        self.git('switch', 'feature')
        event = {'pull_request': {'base': {'sha': base}}}
        self.assertFalse(self.invoke('select', 'pull_request', event)['full_tests'])
        self.git('merge', '--no-edit', 'main')
        self.assertFalse(self.invoke('select', 'pull_request', event)['full_tests'])

    def test_rename_from_code_into_generated_still_runs_full_suite(self):
        (self.repo / 'scripts/runtime.py').rename(self.repo / GENERATED / 'moved.md')
        self.commit()
        self.assertTrue(self.invoke('select', event={'before': self.initial})['full_tests'])

    def test_unavailable_or_empty_change_ranges_run_full_suite(self):
        cases = [('push', {'before': '0' * 40}), ('push', {'before': '1' * 40}),
                 ('push', {'before': 'HEAD~1'}), ('push', {'before': self.initial}),
                 ('push', {}), ('push', None), ('pull_request', {'pull_request': None}),
                 ('workflow_dispatch', {})]
        for event_name, event in cases:
            with self.subTest(event_name=event_name, event=event):
                self.assertTrue(self.invoke('select', event_name, event)['full_tests'])

    def test_complete_document_snapshot_passes(self):
        self.assertTrue(self.invoke('documents')['ready'])

    def test_modified_or_unlisted_documents_fail(self):
        self.write(GENERATED + 'chapters/example/page.md', '# Modified\n')
        self.assertFalse(self.invoke('documents', code=1)['ready'])
        self.snapshot()
        self.write(GENERATED + 'unlisted.md', '# Unlisted\n')
        self.assertFalse(self.invoke('documents', code=1)['ready'])

    def test_missing_manifest_fails(self):
        (self.repo / GENERATED / 'snapshot.json').unlink()
        self.assertFalse(self.invoke('documents', code=1)['ready'])


if __name__ == '__main__':
    unittest.main()
