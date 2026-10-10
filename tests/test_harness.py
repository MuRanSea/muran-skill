"""Adapters, single-attempt runner and Git baselines against a fake CLI, real subprocesses and Git."""
from concurrent.futures import ThreadPoolExecutor
import json
import os
from pathlib import Path
import sys
import threading
import time
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))
from multi_harness_fixture import Fixture  # noqa: E402

import adapters  # noqa: E402
import runner  # noqa: E402
import worktrees  # noqa: E402


class HarnessTests(Fixture):
    def task(self, name='agy', mode='advisor', objective='hello', **extra):
        value = {'harness': name, 'mode': mode, 'model': 'fixture-model', 'objective': objective,
                 'acceptance': ['Parent checks the output'], 'timeout_seconds': 10, **extra}
        if mode == 'worker':
            value.setdefault('allowed_paths', ['calc.py', 'new.txt'])
        return runner.validate_task(value)

    def attempt(self, task, cancel_check=None, session_id=None, folder=None):
        """Run like the group service does: isolated modes get a snapshot worktree."""
        folder = folder or self.base / 'runs' / os.urandom(4).hex()
        if adapters.get(task['harness']).isolated(task['mode']):
            base = worktrees.snapshot(self.repo)
            workspace = folder.parent / (folder.name + '-ws')
            worktrees.add_worktree(self.repo, workspace, base, self.base / 'hooks')
        else:
            base, workspace = None, self.repo
        return runner.run_attempt(task, folder=folder, workspace=workspace, base=base,
                                  prompt=runner.build_prompt(task, workspace), session_id=session_id,
                                  cancel_check=cancel_check)

    def test_stdin_preserves_unicode_quotes_and_shell_metacharacters_for_both_adapters(self):
        text = '中文 "quotes"\n$(whoami) & echo injected > pwned.txt; `literal` %PATH%'
        for name in ('agy', 'claude'):
            with self.subTest(name=name):
                result = self.attempt(self.task(name, objective='echo ' + text))
                self.assertEqual(result['status'], 'completed')
                self.assertEqual(result['response'], text)
                self.assertEqual(result['tool_calls'], 1)
                self.assertEqual(result['model'], 'fixture-model')
                self.assertEqual(result['model_verification'], 'matching')
                self.assertFalse((self.repo / 'pwned.txt').exists())
                self.assertEqual(runner.read_json(result['result_path']), result)

    def test_exit_zero_cannot_hide_provider_errors_or_missing_terminal_events(self):
        for name in ('agy', 'claude'):
            for objective, expected in [('error-zero', 'failed'), ('truncate', 'protocol_error'),
                                        ('malformed', 'protocol_error')]:
                with self.subTest(name=name, objective=objective):
                    result = self.attempt(self.task(name, objective=objective))
                    self.assertEqual(result['status'], expected)
                    self.assertEqual(result['exit_code'], 0)

    def test_worker_patch_contains_tracked_new_and_binary_files_without_changing_parent(self):
        task = self.task(mode='worker', objective='ignored', allowed_paths=['calc.py', 'new.txt', 'ignored.bin'])
        result = self.attempt(task)
        self.assertEqual(result['status'], 'completed')
        self.assertEqual(result['changed_files'], ['calc.py', 'ignored.bin', 'new.txt'])
        self.assertEqual(result['scope_violations'], [])
        self.assertIn('a - b', (self.repo / 'calc.py').read_text())
        self.assertFalse((self.repo / 'new.txt').exists())
        patch_file = Path(result['result_path']).parent / 'changes.patch'
        self.git('apply', '--check', str(patch_file))
        self.assertEqual(self.git('status', '--porcelain'), '')

    def test_worker_retains_but_rejects_out_of_scope_changes(self):
        result = self.attempt(self.task(mode='worker', objective='violate'))
        self.assertEqual(result['status'], 'scope_violation')
        self.assertEqual(result['scope_violations'], ['outside.txt'])
        self.assertTrue((Path(result['workspace']) / 'outside.txt').exists())
        self.assertFalse((self.repo / 'outside.txt').exists())

    def test_snapshot_includes_uncommitted_work_without_touching_the_repository(self):
        (self.repo / 'calc.py').write_text('user work in progress\n')
        (self.repo / 'draft.md').write_text('untracked note\n', encoding='utf-8')
        (self.repo / 'ignored.bin').write_bytes(b'ignored')
        self.git('add', 'calc.py')
        before = (self.git('status', '--porcelain'), self.git('rev-parse', 'HEAD'), self.git('diff', '--cached'))
        result = self.attempt(self.task(objective='read calc.py draft.md ignored.bin'))
        self.assertEqual(result['status'], 'completed')
        seen = json.loads(result['response'])['seen']
        self.assertEqual(seen, {'calc.py': 'user work in progress\n', 'draft.md': 'untracked note\n', 'ignored.bin': None})
        self.assertEqual((self.git('status', '--porcelain'), self.git('rev-parse', 'HEAD'), self.git('diff', '--cached')), before)

    def test_clean_snapshot_is_head(self):
        self.assertEqual(worktrees.snapshot(self.repo), self.git('rev-parse', 'HEAD'))

    def test_dependency_patches_apply_skip_when_present_and_report_conflicts(self):
        first = self.attempt(self.task(mode='worker', objective='edit'))
        patch_file = Path(first['result_path']).parent / 'changes.patch'
        hooks = self.base / 'hooks'
        workspace = self.base / 'dependent'
        worktrees.add_worktree(self.repo, workspace, worktrees.snapshot(self.repo), hooks)
        base, applied, skipped = worktrees.apply_patches(workspace, [('edit', patch_file)], hooks)
        self.assertEqual((applied, skipped), (['edit'], []))
        self.assertIn('a + b', (workspace / 'calc.py').read_text())
        self.assertEqual(worktrees.changed_names(workspace, base)[0], [])
        self.assertEqual(worktrees.integrate(self.repo, patch_file), 'applied')
        self.assertEqual(worktrees.integrate(self.repo, patch_file), 'already_present')
        integrated = self.base / 'integrated'
        worktrees.add_worktree(self.repo, integrated, worktrees.snapshot(self.repo), hooks)
        self.assertEqual(worktrees.apply_patches(integrated, [('edit', patch_file)], hooks)[1:], ([], ['edit']))
        (self.repo / 'calc.py').write_text('conflicting user change\n')
        conflicted = self.base / 'conflicted'
        worktrees.add_worktree(self.repo, conflicted, worktrees.snapshot(self.repo), hooks)
        with self.assertRaisesRegex(ValueError, 'conflict'):
            worktrees.apply_patches(conflicted, [('edit', patch_file)], hooks)

    def test_invalid_task_configuration_fails_before_any_cli_call(self):
        with patch.object(adapters, '_cached_probe') as probe:
            for bad in ('../escape.py', 'C:/escape.py', '.git/config', '/tmp/a', 'src/*.py', 'a\\b', './a'):
                with self.subTest(bad=bad), self.assertRaises(ValueError):
                    self.task(mode='worker', allowed_paths=[bad])
            for name in ('agy', 'claude'):
                for model in (None, '', '  ', 'auto', 'default', '<model-id>', '--flag', 'model\nname'):
                    value = {'harness': name, 'mode': 'advisor', 'objective': 'x', 'acceptance': ['y']}
                    if model is not None:
                        value['model'] = model
                    with self.subTest(name=name, model=model), self.assertRaisesRegex(ValueError, 'explicit CLI model'):
                        runner.validate_task(value)
            with self.assertRaisesRegex(ValueError, 'Unknown task fields'):
                self.task(extra_args=['--dangerously-skip-permissions'])
            with self.assertRaisesRegex(ValueError, 'no supported'):
                self.task(max_budget_usd=1)
            with self.assertRaisesRegex(ValueError, 'researcher mode is not supported by agy'):
                self.task('agy', 'researcher')
            with self.assertRaisesRegex(ValueError, 'Only worker'):
                self.task('claude', 'researcher', allowed_paths=['report.md'])
            with self.assertRaisesRegex(ValueError, 'Unsupported harness'):
                self.task('codex')
            for check in ({'type': 'shell', 'path': 'new.txt'}, {'type': 'cjk_count', 'path': '../escape', 'max': 10},
                          {'type': 'cjk_count', 'path': 'new.txt', 'min': 100, 'max': 10}):
                with self.assertRaises(ValueError):
                    self.task(mode='worker', checks=[check])
            with self.assertRaisesRegex(ValueError, 'Unsupported effort'):
                self.task(mode='worker', effort='max')
            with self.assertRaisesRegex(ValueError, 'conflicts with effort'):
                runner.validate_task({**self.task(mode='worker'), 'model': 'gemini-3.8-flash-high', 'effort': 'low'})
            probe.assert_not_called()
        with patch.dict(os.environ, {runner.CHILD_MARKER: '1'}), self.assertRaisesRegex(ValueError, 'Recursive'):
            self.attempt(self.task())

    def test_tool_policy_never_enables_shell_agents_or_permission_bypass(self):
        claude, agy = adapters.get('claude'), adapters.get('agy')
        for mode in ('advisor', 'worker'):
            args = claude.args(self.task('claude', mode))
            tools = args[args.index('--tools') + 1].lower().split(',')
            self.assertEqual('write' in tools, mode == 'worker')
            allowed = agy.allowed_tools(mode)
            self.assertEqual('write_to_file' in allowed, mode == 'worker')
            for selected, arguments in ((tools, args), (allowed, agy.args(self.task('agy', mode)))):
                self.assertFalse({'bash', 'agent', 'run_command'} & set(selected))
                self.assertNotIn('--dangerously-skip-permissions', arguments)
        task = self.task(mode='worker', profile='writer', effort='low')
        args = agy.args(task, 'saved-session')
        self.assertEqual(args[args.index('--effort') + 1], 'low')
        self.assertEqual(args[args.index('--conversation') + 1], 'saved-session')
        prompt = runner.build_prompt(task, self.repo)
        self.assertNotIn('Return a concise report', prompt)
        self.assertIn('only the changed relative file paths', prompt)
        self.assertEqual(prompt.count('\n\n'), 1)

    def test_agy_unexpected_tool_or_advisor_write_fails_audit_in_isolation(self):
        result = self.attempt(self.task(objective='tool run_command'))
        self.assertEqual(result['status'], 'scope_violation')
        self.assertEqual(result['observed_tools'], ['run_command'])
        self.assertEqual(result['tool_scope_control'], 'prompt_and_audit')
        self.assertNotEqual(Path(result['workspace']), self.repo)
        written = self.attempt(self.task(objective='edit'))
        self.assertEqual(written['status'], 'scope_violation')
        self.assertEqual(written['scope_violations'], ['calc.py', 'new.txt'])
        self.assertIn('a - b', (self.repo / 'calc.py').read_text())

    def test_research_mode_exposes_web_tools_and_records_actual_tool_use(self):
        result = self.attempt(self.task('claude', 'researcher', 'research-scope'))
        self.assertEqual(result['status'], 'completed')
        self.assertEqual(result['observed_tools'], ['WebFetch'])
        self.assertEqual(self.git('status', '--porcelain'), '')

    def test_timeout_terminates_descendants_and_output_limit_never_completes(self):
        result = self.attempt(self.task(objective=f'timeout-child {self.base.as_posix()}', timeout_seconds=1))
        self.assertEqual(result['status'], 'timed_out')
        time.sleep(3)
        self.assertFalse((self.base / 'orphan.txt').exists())
        self.assertTrue(Path(result['result_path']).exists())
        with patch.object(runner, 'LOG_LIMIT', 1024):
            self.assertEqual(self.attempt(self.task(objective='large'))['status'], 'output_limit')

    def test_live_events_and_cancel_are_visible_before_completion(self):
        stop = threading.Event()
        folder = self.base / 'runs' / 'live'
        with ThreadPoolExecutor(max_workers=1) as pool:
            future = pool.submit(self.attempt, self.task(objective='slow'), stop.is_set, None, folder)
            deadline = time.monotonic() + 10
            progress = None
            while time.monotonic() < deadline:
                path = folder / 'progress.json'
                if path.exists():
                    progress = runner.read_json(path)
                    if progress.get('session_id'):
                        break
                time.sleep(0.05)
            self.assertTrue(progress and progress['session_id'])
            self.assertFalse(future.done())
            stop.set()
            result = future.result(timeout=10)
        self.assertEqual(result['status'], 'cancelled')
        self.assertEqual(result['session_id'], progress['session_id'])

    def test_resume_must_confirm_the_same_session(self):
        for name in ('claude', 'agy'):
            with self.subTest(name=name):
                first = self.attempt(self.task(name, objective='hello'))
                resumed = self.attempt(self.task(name, objective='hello again'), session_id=first['session_id'])
                self.assertEqual(resumed['status'], 'completed')
                self.assertTrue(json.loads(resumed['response'])['continued'])
                mismatch = self.attempt(self.task(name, objective='session-mismatch'), session_id=first['session_id'])
                self.assertEqual(mismatch['status'], 'protocol_error')

    def test_selected_doctor_probes_only_that_cli(self):
        import groups
        with patch.object(adapters.Adapter, 'probe', autospec=True, return_value={'available': True}) as probe:
            self.assertEqual(groups.doctor('claude')['adapters'], [{'available': True}])
        self.assertEqual([call.args[0].name for call in probe.call_args_list], ['claude'])


if __name__ == '__main__':
    unittest.main()
