import json
import os
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'scripts'))
from muran import choose_packages
from validation import validate
import test_manager
import upstream


@unittest.skipUnless(os.name == 'nt', 'Windows integration')
class PackageTests(unittest.TestCase):
    setUp = test_manager.ManagerTests.setUp
    tearDown = test_manager.ManagerTests.tearDown

    def pack(self, name, skills):
        parent = self.repo / 'skills' / name
        parent.mkdir(exist_ok=True)
        (parent / 'pack.json').write_text(json.dumps({'schema_version': 1, 'name': name, 'description': name, 'skills': ['*'], 'updater': 'git'}))
        for skill in skills:
            folder = parent / skill
            folder.mkdir()
            (folder / 'SKILL.md').write_text(f'---\nname: {skill}\ndescription: fixture\n---\n')
        return parent

    def test_new_install_requires_choice_and_new_packages_are_not_auto_installed(self):
        self.pack('matt', ['alpha'])
        self.assertFalse(self.manager.sync()['ok'])
        result = self.manager.sync(packages=['matt'])
        self.assertTrue(result['ok'])
        self.assertEqual(result['skills'], 1)
        self.pack('later', ['beta'])
        self.assertEqual(self.manager.sync()['skills'], 1)
        self.assertFalse((self.manager.shared / 'beta').exists())
        self.assertTrue((self.manager.shared / 'alpha').is_junction())

    def test_additive_install_and_single_package_uninstall(self):
        self.pack('first', ['alpha'])
        self.pack('second', ['beta'])
        self.manager.sync(packages=['first'])
        self.assertEqual(self.manager.sync(packages=['second'])['skills'], 2)
        result = self.manager.uninstall_packages(['first'])
        self.assertTrue(result['ok'])
        self.assertFalse((self.manager.shared / 'alpha').exists())
        self.assertTrue((self.manager.shared / 'beta').is_junction())
        self.assertTrue((self.repo / 'skills/first/alpha/SKILL.md').exists())
        self.assertEqual(self.manager.uninstall_packages(['second'])['skills'], 0)
        self.assertEqual(self.manager.sync()['skills'], 0)

    def test_legacy_links_are_retargeted_after_grouping(self):
        self.manager.sync()
        parent = self.pack('matt', [])
        source, destination = self.repo / 'skills/example', parent / 'example'
        self.assertTrue(source.resolve().is_relative_to(self.repo.resolve()))
        self.assertTrue(destination.resolve().is_relative_to(self.repo.resolve()))
        source.rename(destination)
        result = self.manager.sync()
        self.assertTrue(result['ok'])
        self.assertEqual(result['packages'], ['matt'])
        self.assertEqual((self.manager.shared / 'example').resolve(), destination.resolve())

    def test_duplicate_names_and_missing_selected_dependencies_are_rejected(self):
        first = self.pack('first', ['alpha'])
        self.pack('second', ['beta'])
        (first / 'alpha/SKILL.md').write_text('---\nname: alpha\ndescription: fixture\n---\nCall the Skill tool with "beta".\n')
        self.assertFalse(self.manager.sync(packages=['first'])['ok'])
        self.assertTrue(self.manager.sync(packages=['first', 'second'])['ok'])
        with self.assertRaisesRegex(ValueError, 'missing dependencies'):
            self.manager.uninstall_packages(['second'])
        self.pack('third', ['alpha'])
        self.assertTrue(any('unique' in error for error in validate(self.repo)[1]))

    def test_terminal_selection_and_cancel(self):
        self.pack('matt', ['alpha'])
        with patch('sys.stdin.isatty', return_value=True), patch('builtins.input', return_value='matt'):
            self.assertEqual(choose_packages(self.manager), ['matt'])
        with patch('sys.stdin.isatty', return_value=True), patch('builtins.input', return_value=''):
            self.assertEqual(choose_packages(self.manager), [])
        with patch('sys.stdin.isatty', return_value=False), self.assertRaisesRegex(ValueError, '--packages'):
            choose_packages(self.manager)

    def test_daily_task_does_not_check_uninstalled_matt(self):
        self.pack('matt', ['alpha'])
        self.pack('other', ['beta'])
        self.manager.sync(packages=['other'])
        with patch.object(self.manager, 'update', return_value={'ok': True, 'status': 'unchanged'}), patch.object(upstream, 'sync_upstream') as sync:
            result = upstream.daily(self.manager)
        sync.assert_not_called()
        self.assertEqual(result['upstream']['status'], 'skipped_not_installed')
