import json
import io
import os
from pathlib import Path
import sys
import tarfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
import upstream
from muran import git
import test_manager


class MergeTests(unittest.TestCase):
    def test_archive_ignores_root_alias_but_rejects_linked_skill_resources(self):
        for name, rejected in (('AGENTS.md', False), ('skills/example/file.md', True)):
            buffer = io.BytesIO()
            with tarfile.open(fileobj=buffer, mode='w:gz') as archive:
                entry = tarfile.TarInfo('repo/' + name)
                entry.type, entry.linkname = tarfile.SYMTYPE, 'CLAUDE.md'
                archive.addfile(entry)
            with patch.object(upstream.urllib.request, 'urlopen', return_value=io.BytesIO(buffer.getvalue())):
                if rejected:
                    with self.assertRaisesRegex(ValueError, 'Linked upstream'):
                        upstream.download('a' * 40)
                else:
                    self.assertEqual(upstream.download('a' * 40), {})

    def test_preserves_local_adaptation_and_applies_independent_upstream_change(self):
        base = b'header\n' + b'context\n' * 8 + b'tail\n'
        local = base.replace(b'header', b'local header')
        incoming = base.replace(b'tail', b'new tail')
        self.assertEqual(upstream.merge_file('skill', base, local, incoming),
                         incoming.replace(b'header', b'local header'))

    def test_conflicts_stop_including_delete_and_binary_changes(self):
        for values in ((b'old', b'local', b'new'), (b'old', b'local', None),
                       (None, b'local', b'new'), (b'a\0', b'b\0', b'c\0')):
            with self.subTest(values=values), self.assertRaisesRegex(ValueError, 'conflict'):
                upstream.merge_file('skill', *values)


@unittest.skipUnless(os.name == 'nt', 'Windows integration')
class UpstreamTests(unittest.TestCase):
    setUp = test_manager.ManagerTests.setUp
    tearDown = test_manager.ManagerTests.tearDown
    git_fixture = test_manager.ManagerTests.git_fixture

    def prepare(self):
        self.git_fixture()
        self.old, self.new = 'a' * 40, 'b' * 40
        def catalog(description):
            return {'.claude-plugin/plugin.json': json.dumps({'version': '1', 'skills': ['./skills/example']}).encode(),
                    'LICENSE': b'Fixture license\n',
                    'skills/example/SKILL.md': ('---\nname: example\ndescription: ' + description + '\n---\n\nCall the Skill tool with "example".\n').encode()}
        self.upstream_base, self.incoming = catalog('Original description'), catalog('Updated description')
        tree, metadata = upstream.adapted_tree(self.upstream_base)
        for name, data in tree.items():
            path = self.repo / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        source = {'mattpocock': {'repository': upstream.UPSTREAM, 'commit': self.old, **metadata}}
        (self.repo / 'sources.json').write_text(json.dumps(source), encoding='utf-8')
        git(self.repo, 'add', '.')
        git(self.repo, 'commit', '-m', 'import fixture')
        git(self.repo, 'push', 'origin', 'main')
        self.before = git(self.repo, 'rev-parse', 'HEAD').strip()

    def invoke(self, before_push=None):
        real_git = upstream.git
        def fake_git(root, *args, **kwargs):
            if args[0] == 'ls-remote':
                return self.new + '\tHEAD\n'
            if args[0] == 'push' and before_push:
                before_push()
            return real_git(root, *args, **kwargs)
        with patch.object(upstream, 'git', side_effect=fake_git), patch.object(
                upstream, 'download', side_effect=lambda ref: self.upstream_base if ref == self.old else self.incoming):
            return upstream.sync_upstream(self.manager)

    def test_valid_update_is_committed_pushed_and_installed_with_compatibility(self):
        self.prepare()
        result = self.invoke()
        self.assertEqual(result['status'], 'published')
        self.assertTrue(result['ok'])
        self.assertEqual(git(self.repo, 'rev-parse', 'HEAD').strip(), result['commit'])
        self.assertEqual(git(self.repo, 'status', '--porcelain'), '')
        body = (self.repo / 'skills/example/SKILL.md').read_text(encoding='utf-8')
        self.assertIn('Updated description', body)
        self.assertEqual(body.count('## Harness compatibility'), 1)
        self.assertEqual(json.loads((self.repo / 'sources.json').read_text())['mattpocock']['commit'], self.new)

    def test_dirty_checkout_never_commits_user_edits(self):
        self.prepare()
        file = self.repo / 'skills/example/SKILL.md'
        file.write_text('uncommitted user work')
        self.assertEqual(self.invoke()['status'], 'skipped_dirty')
        self.assertEqual(file.read_text(), 'uncommitted user work')
        self.assertEqual(git(self.repo, 'rev-parse', 'HEAD').strip(), self.before)

    def test_unchanged_upstream_does_not_create_commit(self):
        self.prepare()
        self.new = self.old
        self.assertEqual(self.invoke()['status'], 'unchanged')
        self.assertEqual(git(self.repo, 'rev-parse', 'HEAD').strip(), self.before)

    def test_doctor_reports_upstream_failure_and_ignores_uninstalled_docs(self):
        self.prepare()
        state = self.manager.load_state()
        state['last_docs_update'] = {'ok': False, 'status': 'failed'}
        state['last_upstream_update'] = {'status': 'failed', 'error': 'fixture conflict'}
        self.manager.save(state)
        report = self.manager.doctor()
        self.assertFalse(report['ok'])
        self.assertFalse(any('Last document rebuild failed' in error for error in report['errors']))
        self.assertTrue(any('Last Matt upstream update failed' in error for error in report['errors']))

    def test_grouped_matt_update_stays_inside_its_package(self):
        self.prepare()
        parent = self.repo / 'skills/matt'
        parent.mkdir()
        (parent / 'pack.json').write_text(json.dumps({'schema_version': 1, 'name': 'matt', 'skills': ['*'], 'updater': 'matt'}))
        source, destination = self.repo / 'skills/example', parent / 'example'
        self.assertTrue(source.resolve().is_relative_to(self.repo.resolve()))
        self.assertTrue(destination.resolve().is_relative_to(self.repo.resolve()))
        source.rename(destination)
        git(self.repo, 'add', '-A')
        git(self.repo, 'commit', '-m', 'group package')
        git(self.repo, 'push', 'origin', 'main')
        result = self.invoke()
        self.assertEqual(result['status'], 'published')
        self.assertIn('Updated description', (destination / 'SKILL.md').read_text(encoding='utf-8'))
        self.assertFalse(source.exists())
        self.assertEqual((self.manager.shared / 'example').resolve(), destination.resolve())

    def test_remote_advance_rejects_push_without_overwriting_either_checkout(self):
        self.prepare()
        def advance():
            git(self.publisher, 'pull', '--ff-only', 'origin', 'main')
            (self.publisher / 'remote-note.txt').write_text('concurrent remote change')
            git(self.publisher, 'add', '.')
            git(self.publisher, 'commit', '-m', 'remote update')
            git(self.publisher, 'push', 'origin', 'main')
        with self.assertRaises(RuntimeError):
            self.invoke(before_push=advance)
        self.assertEqual(git(self.repo, 'rev-parse', 'HEAD').strip(), self.before)
        remote = git(self.repo, 'remote', 'get-url', 'origin').strip()
        self.assertEqual(git(self.repo, 'ls-remote', remote, 'refs/heads/main').split()[0],
                         git(self.publisher, 'rev-parse', 'HEAD').strip())

    def test_conflict_preserves_local_and_remote(self):
        self.prepare()
        file = self.repo / 'skills/example/SKILL.md'
        file.write_text(file.read_text(encoding='utf-8').replace('Original description', 'Local description'), encoding='utf-8')
        git(self.repo, 'add', '.')
        git(self.repo, 'commit', '-m', 'local customization')
        git(self.repo, 'push', 'origin', 'main')
        before = git(self.repo, 'rev-parse', 'HEAD')
        with self.assertRaisesRegex(ValueError, 'conflict'):
            self.invoke()
        self.assertEqual(git(self.repo, 'rev-parse', 'HEAD'), before)
        self.assertEqual(git(self.repo, 'rev-parse', 'origin/main'), before)

    def test_invalid_candidate_is_not_pushed(self):
        self.prepare()
        self.incoming['skills/example/SKILL.md'] = b'invalid skill\n'
        with self.assertRaisesRegex(ValueError, 'validation failed'):
            self.invoke()
        self.assertEqual(git(self.repo, 'rev-parse', 'origin/main').strip(), self.before)
        self.assertEqual(git(self.repo, 'rev-parse', 'HEAD').strip(), self.before)

    def test_push_rejection_preserves_installed_checkout(self):
        self.prepare()
        with self.assertRaisesRegex(RuntimeError, 'fixture network failure'):
            self.invoke(before_push=lambda: (_ for _ in ()).throw(RuntimeError('fixture network failure')))
        self.assertEqual(git(self.repo, 'rev-parse', 'HEAD').strip(), self.before)
        self.assertEqual(git(self.repo, 'status', '--porcelain'), '')

    def test_new_upstream_skill_cannot_replace_separately_managed_skill(self):
        self.prepare()
        self.incoming['.claude-plugin/plugin.json'] = json.dumps({'version': '2', 'skills': ['./skills/example', './skills/custom']}).encode()
        self.incoming['skills/custom/SKILL.md'] = b'---\nname: custom\ndescription: upstream\n---\n'
        folder = self.repo / 'skills/custom'
        folder.mkdir()
        (folder / 'SKILL.md').write_text('---\nname: custom\ndescription: mine\n---\n')
        git(self.repo, 'add', '.')
        git(self.repo, 'commit', '-m', 'custom skill')
        git(self.repo, 'push', 'origin', 'main')
        with self.assertRaisesRegex(ValueError, 'conflicts with local skill'):
            self.invoke()


if __name__ == '__main__':
    unittest.main()
