import hashlib
import json
import os
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'scripts'))
import document_publish as publisher
from muran import git
import test_manager


@unittest.skipUnless(os.name == 'nt', 'Windows integration')
class DocumentPublishTests(unittest.TestCase):
    setUp = test_manager.ManagerTests.setUp
    tearDown = test_manager.ManagerTests.tearDown
    git_fixture = test_manager.ManagerTests.git_fixture

    def setup_snapshot(self):
        self.git_fixture()
        skill = test_manager.skill(self.repo, 'ai-platform-docs')
        (skill / 'providers.json').write_text(json.dumps({'providers': [{'key': 'example', 'type': 'markdown'}]}))
        self.generated = skill / 'generated'
        (self.generated / 'chapters/example').mkdir(parents=True)
        for name in ('INDEX.md', 'INDEX-example.md', 'chapters/example/page.md'):
            (self.generated / name).write_bytes(b'# Original\r\n')
        self.snapshot()
        git(self.repo, 'add', '.')
        git(self.repo, 'commit', '-m', 'initial docs')
        git(self.repo, 'push', 'origin', 'main')

    def snapshot(self):
        files = {p.relative_to(self.generated).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                 for p in self.generated.rglob('*') if p.is_file() and p.name != 'snapshot.json'}
        manifest = {'files': files, 'built_at': 'fixture', 'origin': 'fixture', 'sources': {'example': {'pages': 1}}}
        (self.generated / 'snapshot.json').write_text(json.dumps(manifest), encoding='utf-8')

    def test_publishes_snapshot_and_preserves_exact_git_bytes(self):
        self.setup_snapshot()
        before = publisher.prepare(self.manager)
        (self.generated / 'chapters/example/page.md').write_bytes(b'# Updated\r\n')
        self.snapshot()
        result = publisher.publish(self.manager, before)
        self.assertEqual(result['status'], 'published')
        self.assertEqual(git(self.repo, 'show', 'HEAD:skills/ai-platform-docs/generated/chapters/example/page.md', binary=True), b'# Updated\r\n')
        self.assertEqual(git(self.repo, 'status', '--porcelain'), '')
        self.assertEqual(publisher.publish(self.manager, result['commit'])['status'], 'unchanged')

    def test_manual_changes_block_update(self):
        self.setup_snapshot()
        (self.repo / 'manual.txt').write_text('user work')
        with self.assertRaisesRegex(ValueError, 'Uncommitted'):
            publisher.prepare(self.manager)

    def test_push_failure_is_retried_without_rebuilding(self):
        self.setup_snapshot()
        before = publisher.prepare(self.manager)
        (self.generated / 'chapters/example/page.md').write_text('updated')
        self.snapshot()
        real_git = publisher.git
        def fail_push(root, *args, **kwargs):
            if args[0] == 'push':
                raise RuntimeError('fixture network failure')
            return real_git(root, *args, **kwargs)
        with patch.object(publisher, 'git', side_effect=fail_push), self.assertRaisesRegex(RuntimeError, 'network failure'):
            publisher.publish(self.manager, before)
        pending = self.manager.load_state()['last_docs_publish']['pending_commit']
        self.assertEqual(publisher.prepare(self.manager), pending)
        self.assertEqual(git(self.repo, 'rev-parse', 'origin/main').strip(), pending)
        self.assertEqual(self.manager.load_state()['last_docs_publish']['status'], 'published')

    def test_concurrent_manual_changes_are_not_committed(self):
        self.setup_snapshot()
        before = publisher.prepare(self.manager)
        (self.generated / 'chapters/example/page.md').write_text('updated')
        self.snapshot()
        (self.repo / 'manual.txt').write_text('user work')
        with self.assertRaisesRegex(ValueError, 'outside generated'):
            publisher.publish(self.manager, before)
        self.assertEqual(git(self.repo, 'rev-parse', 'HEAD').strip(), before)
