"""Protocol/process/Git integration with fake CLIs. Live checks are opt-in/manual."""
import importlib.util
import copy
from contextlib import redirect_stdout
from concurrent.futures import ThreadPoolExecutor
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / 'skills/multi-harness/scripts/harness.py'
spec = importlib.util.spec_from_file_location('multi_harness', SCRIPT)
harness = importlib.util.module_from_spec(spec)
spec.loader.exec_module(harness)

FAKE = r'''
import json, os, pathlib, subprocess, sys, time
if '--version' in sys.argv:
    print('fixture 1.0'); raise SystemExit()
if '--help' in sys.argv:
    print('--output-format --tools --allowedTools --safe-mode --strict-mcp-config '
          '--disable-slash-commands --permission-mode --permission-prompts '
          '--resume --conversation --effort --max-budget-usd --mode --agent --add-dir --input-format --print-timeout --model')
    raise SystemExit()
model = sys.argv[sys.argv.index('--model') + 1]
raw = sys.stdin.read()
is_agy = '--input-format' in sys.argv
session = 'fixture-session'
for flag in ('--conversation', '--resume'):
    if flag in sys.argv:
        assert sys.argv[sys.argv.index(flag) + 1] == session
if is_agy:
    print(json.dumps({'event':'init','conversation_id':session,'init':{'tools':['view_file','run_command'],'model':model}}), flush=True)
    if not raw:
        raise SystemExit()
    raw = json.loads(raw)['message']['content']
task = json.loads(raw.split('\n\n', 1)[1])
os.chdir(task['project_root'])
objective = task['objective']
if 'feedback' in task:
    objective = task['feedback']
if objective == 'session-mismatch':
    session = 'different-session'
if objective == 'slow-events':
    print(json.dumps({'event':'step_update','conversation_id':session,
        'step_update':{'step_index':0,'step_type':'tool','state':'ACTIVE','tool_name':'view_file'}}), flush=True)
    time.sleep(4)
if objective == 'research-scope':
    available = sys.argv[sys.argv.index('--tools') + 1].split(',')
    assert 'WebSearch' in available and 'WebFetch' in available
    assert not set(available) & {'Write', 'Edit', 'Bash', 'Agent'}
if objective == 'timeout-child':
    marker = str(pathlib.Path(task['context']) / 'orphan.txt')
    subprocess.Popen([sys.executable, '-c',
        'import pathlib,time; time.sleep(3); pathlib.Path(' + repr(marker) + ').write_text("orphan")'])
    time.sleep(30)
if objective in ('edit', 'violate', 'ignored'):
    pathlib.Path('calc.py').write_text('def add(a, b):\n    return a + b\n')
    pathlib.Path('new.txt').write_text('中文 new file\n', encoding='utf-8')
if objective == 'revise-edit':
    pathlib.Path('new.txt').write_text('修订完成\n', encoding='utf-8')
if objective == 'violate':
    pathlib.Path('outside.txt').write_text('unexpected')
if objective == 'ignored':
    pathlib.Path('ignored.bin').write_bytes(bytes(range(256)))
if objective == 'malformed':
    print('not json'); raise SystemExit()
if objective == 'large':
    print('x' * 8192); raise SystemExit()
error = objective == 'error-zero'
answer = objective if not error else 'fixture failure'
if is_agy:
    for state in ('ACTIVE', 'DONE'):
        print(json.dumps({'event':'step_update','step_update':{'step_type':'tool', 'step_index':2,'state':state,
            'tool_name':'run_command' if objective == 'unexpected-tool' else 'view_file'}}))
    if objective != 'truncate':
        print(json.dumps({'event':'result','conversation_id':session,'result':{'status':'ERROR' if error else 'SUCCESS',
            'response':answer, 'error':'fixture error' if error else '', 'usage':{'input_tokens':3,'output_tokens':4}}}))
else:
    print(json.dumps({'type':'assistant','message':{'model':model,
        'content':[{'type':'tool_use','name':'WebFetch' if objective == 'research-scope' else 'Read','id':'x','input':{}}]}}))
    if objective != 'truncate':
        print(json.dumps({'type':'result','session_id':session,'subtype':'error_during_execution' if error else 'success',
            'is_error':error, 'result':answer, 'usage':{'input_tokens':3,'output_tokens':4},
            'total_cost_usd':0.01, 'errors':['fixture error'] if error else []}))
'''


class HarnessTests(unittest.TestCase):
    def setUp(self):
        parent = ROOT / '.cache/tests'
        parent.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(prefix='harness-', dir=parent)
        self.base = Path(self.temporary.name).resolve()
        self.repo = self.base / 'repo 中文 with spaces'
        self.repo.mkdir()
        self.fake = self.base / 'fake cli.py'
        self.fake.write_text(FAKE, encoding='utf-8')
        self.output = self.base / 'runs'
        self.env = patch.dict(os.environ, {'PYTHONUTF8': '1'})
        self.env.start()
        self.launcher = patch.object(harness, 'resolve_launcher', return_value=[sys.executable, str(self.fake)])
        self.launcher.start()
        self.init_repo()

    def tearDown(self):
        self.launcher.stop()
        self.env.stop()
        self.assertTrue(self.base.is_relative_to((ROOT / '.cache/tests').resolve()))
        # All fixture repositories and their worktrees live under this checked path.
        self.temporary.cleanup()

    def task(self, name='agy', mode='advisor', objective='hello'):
        result = {'schema_version': 1, 'harness': name, 'mode': mode, 'cwd': str(self.repo),
                  'model': 'fixture-model', 'objective': objective,
                  'acceptance': ['Parent checks the output'], 'timeout_seconds': 10}
        if mode == 'worker':
            result['allowed_paths'] = ['calc.py', 'new.txt']
        return result

    def plan(self):
        tasks = []
        for task_id, name, mode, dependencies, objective in (
                ('inspect', 'agy', 'advisor', [], 'inspect input handling'),
                ('fix', 'claude', 'worker', ['inspect'], 'edit')):
            task = self.task(name, mode, objective)
            task['model'] = name + '-explicit-model'
            del task['cwd'], task['schema_version']
            tasks.append({'id': task_id, 'depends_on': dependencies,
                          'rationale': 'Independent analysis followed by scoped implementation', 'task': task})
        return {'schema_version': 1, 'plan_id': 'fixture-plan', 'state': 'ready',
                'goal': 'Fix arithmetic', 'strategy': 'Inspect first, implement after acceptance',
                'cwd': str(self.repo), 'acceptance': ['Parent verifies correct addition'], 'tasks': tasks}

    def save_plan(self, plan=None):
        path = self.base / 'plan.json'
        harness.write_json(path, plan or self.plan())
        return path

    def accept(self, plan_path, task_id, result):
        evidence = self.base / 'verified.md'
        evidence.write_text('Parent inspected fixture output and verified expected behavior.', encoding='utf-8')
        return harness.accept_result(plan_path, task_id, result['result_path'], evidence)

    def init_repo(self):
        harness.git(self.repo, 'init', '-q')
        (self.repo / 'calc.py').write_text('def add(a, b):\n    return a - b\n')
        (self.repo / '.gitignore').write_text('.cache/\nignored.bin\n')
        harness.git(self.repo, 'add', '.')
        harness.git(self.repo, '-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.invalid',
                    '-c', 'core.hooksPath=' + str(self.base / 'no-hooks'), 'commit', '-qm', 'fixture')

    def test_stdin_preserves_unicode_quotes_and_shell_metacharacters_for_both_adapters(self):
        text = '中文 "quotes"\n$(whoami) & echo injected > pwned.txt; `literal` %PATH%'
        for name in ('agy', 'claude'):
            with self.subTest(name=name):
                result = harness.run_task(self.task(name, objective=text), self.output)
                self.assertEqual(result['status'], 'completed')
                self.assertEqual(result['response'], text)
                self.assertEqual(result['tool_calls'], 1)
                self.assertEqual(result['acceptance'], 'pending')
                self.assertEqual(result['model'], 'fixture-model')
                self.assertFalse((self.repo / 'pwned.txt').exists())
                saved = json.loads(Path(result['result_path']).read_text(encoding='utf-8'))
                self.assertEqual(saved, result)

    def test_exit_zero_cannot_hide_provider_errors_or_missing_terminal_events(self):
        for name in ('agy', 'claude'):
            for objective, expected in [('error-zero', 'failed'), ('truncate', 'protocol_error'),
                                        ('malformed', 'protocol_error')]:
                with self.subTest(name=name, objective=objective):
                    result = harness.run_task(self.task(name, objective=objective), self.output)
                    self.assertEqual(result['status'], expected)
                    self.assertEqual(result['exit_code'], 0)

    def test_worker_patch_contains_tracked_new_and_binary_files_without_changing_parent(self):
        task = self.task(mode='worker', objective='ignored')
        task['allowed_paths'].append('ignored.bin')
        result = harness.run_task(task, self.output)
        self.assertEqual(result['status'], 'completed')
        self.assertEqual(result['changed_files'], ['calc.py', 'ignored.bin', 'new.txt'])
        self.assertEqual(result['scope_violations'], [])
        self.assertIn('a - b', (self.repo / 'calc.py').read_text())
        self.assertFalse((self.repo / 'new.txt').exists())
        patch_file = Path(result['result_path']).parent / 'changes.patch'
        harness.git(self.repo, 'apply', '--check', str(patch_file))
        self.assertEqual(harness.git(self.repo, 'status', '--porcelain'), '')

    def test_worker_retains_but_rejects_out_of_scope_changes(self):
        result = harness.run_task(self.task(mode='worker', objective='violate'), self.output)
        self.assertEqual(result['status'], 'scope_violation')
        self.assertEqual(result['scope_violations'], ['outside.txt'])
        self.assertTrue((Path(result['workspace']) / 'outside.txt').exists())
        self.assertFalse((self.repo / 'outside.txt').exists())

    def test_dirty_baseline_is_rejected_before_creating_a_run(self):
        (self.repo / 'calc.py').write_text('user work')
        with self.assertRaisesRegex(ValueError, 'clean repository'):
            harness.run_task(self.task(mode='worker'), self.output)
        self.assertFalse(self.output.exists())

    def test_invalid_scope_and_recursive_delegation_fail_before_spawn(self):
        for bad in ('../escape.py', 'C:/escape.py', '.git/config', '/tmp/a', 'src/*.py', 'a\\b', './a'):
            task = self.task(mode='worker')
            task['allowed_paths'] = [bad]
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                harness.run_task(task, self.output)
        with patch.dict(os.environ, {harness.CHILD_MARKER: '1'}), self.assertRaisesRegex(ValueError, 'Recursive'):
            harness.run_task(self.task(), self.output)
        self.assertFalse(self.output.exists())

    def test_tool_scope_policy_does_not_enable_permission_bypass(self):
        for name in ('agy', 'claude'):
            for mode in ('advisor', 'worker'):
                task = harness.validate_task(self.task(name, mode))
                args = harness.adapter_args(task)
                selected = (args[args.index('--tools') + 1].lower().split(',')
                            if name == 'claude' else harness.agy_tools(mode))
                self.assertNotIn('bash', selected)
                self.assertNotIn('agent', selected)
                self.assertEqual(('write' if name == 'claude' else 'write_to_file') in selected, mode == 'worker')
                self.assertNotIn('--dangerously-skip-permissions', args)

    def test_agy_advisor_is_isolated_and_unexpected_tool_use_fails_audit(self):
        result = harness.run_task(self.task(objective='unexpected-tool'), self.output)
        self.assertEqual(result['status'], 'scope_violation')
        self.assertEqual(result['observed_tools'], ['run_command'])
        self.assertEqual(result['tool_scope_control'], 'prompt_and_audit')
        self.assertNotEqual(Path(result['workspace']), self.repo)

    def test_agy_advisor_writes_are_retained_and_flagged(self):
        result = harness.run_task(self.task(objective='edit'), self.output)
        self.assertEqual(result['status'], 'scope_violation')
        self.assertEqual(result['scope_violations'], ['calc.py', 'new.txt'])
        self.assertIn('a - b', (self.repo / 'calc.py').read_text())

    def test_timeout_terminates_descendants_and_records_failure(self):
        task = self.task(objective='timeout-child')
        task.update(timeout_seconds=1, context=str(self.base))
        result = harness.run_task(task, self.output)
        self.assertEqual(result['status'], 'timed_out')
        time.sleep(3)
        self.assertFalse((self.base / 'orphan.txt').exists())
        self.assertTrue(Path(result['result_path']).exists())

    def test_output_limit_never_counts_as_a_completed_run(self):
        with patch.object(harness, 'LOG_LIMIT', 1024):
            result = harness.run_task(self.task(objective='large'), self.output)
        self.assertEqual(result['status'], 'output_limit')

    def test_unknown_flags_and_unsupported_budget_are_rejected(self):
        task = self.task()
        task['extra_args'] = ['--dangerously-skip-permissions']
        with self.assertRaisesRegex(ValueError, 'Unknown task fields'):
            harness.validate_task(task)
        task = self.task()
        task['max_budget_usd'] = 1
        with self.assertRaisesRegex(ValueError, 'no supported'):
            harness.validate_task(task)

    def test_selected_doctor_does_not_invoke_other_harnesses(self):
        with patch.object(sys, 'argv', ['harness.py', 'doctor', '--harness', 'claude']), \
                patch.object(harness, 'probe', return_value={'available': True}) as probe, \
                redirect_stdout(io.StringIO()):
            self.assertEqual(harness.main(), 0)
        probe.assert_called_once_with('claude')

    def test_research_mode_exposes_web_tools_and_records_actual_tool_use(self):
        result = harness.run_task(self.task('claude', 'researcher', 'research-scope'), self.output)
        self.assertEqual(result['status'], 'completed')
        self.assertEqual(result['observed_tools'], ['WebFetch'])
        self.assertEqual(harness.git(self.repo, 'status', '--porcelain'), '')
        with self.assertRaisesRegex(ValueError, 'currently requires Claude'):
            harness.validate_task(self.task('agy', 'researcher'))
        task = self.task('claude', 'researcher')
        task['allowed_paths'] = ['report.md']
        with self.assertRaisesRegex(ValueError, 'Only worker'):
            harness.validate_task(task)

    def test_missing_or_implicit_model_fails_before_any_cli_call(self):
        for name in ('agy', 'claude'):
            for model in (None, '', '  ', 'auto', 'default', '<model-id>', '--flag', 'model\nname'):
                task = self.task(name)
                if model is None:
                    del task['model']
                else:
                    task['model'] = model
                with self.subTest(name=name, model=model), patch.object(harness, 'probe') as probe:
                    with self.assertRaisesRegex(ValueError, 'explicit CLI model'):
                        harness.run_task(task, self.output)
                    probe.assert_not_called()

    def test_plan_rejects_cycles_unknown_dependencies_and_duplicate_ids(self):
        cases = []
        plan = self.plan()
        plan['tasks'][0]['depends_on'] = ['fix']
        cases.append((plan, 'cycle'))
        plan = self.plan()
        plan['tasks'][1]['depends_on'] = ['missing']
        cases.append((plan, 'Unknown'))
        plan = self.plan()
        plan['tasks'][1]['id'] = 'inspect'
        cases.append((plan, 'Duplicate'))
        for plan, error in cases:
            with self.subTest(error=error), self.assertRaisesRegex(ValueError, error):
                harness.validate_plan(plan)

    def test_plan_check_has_no_cli_side_effect_and_draft_cannot_dispatch(self):
        plan = self.plan()
        plan['state'] = 'draft'
        path = self.save_plan(plan)
        with patch.object(harness, 'probe') as probe, redirect_stdout(io.StringIO()) as output:
            with patch.object(sys, 'argv', ['harness.py', 'check-plan', '--plan', str(path)]):
                self.assertEqual(harness.main(), 0)
            self.assertEqual(json.loads(output.getvalue())['execution_order'], ['inspect', 'fix'])
            with self.assertRaisesRegex(ValueError, 'ready'):
                harness.run_planned(path, 'inspect', output_root=self.output)
            probe.assert_not_called()

    def test_plan_dispatch_passes_each_model_and_requires_parent_acceptance(self):
        path = self.save_plan()
        with self.assertRaisesRegex(ValueError, 'All dependencies'):
            harness.run_planned(path, 'fix', output_root=self.output)
        first = harness.run_planned(path, 'inspect', output_root=self.output)
        self.assertEqual(first['requested_model'], 'agy-explicit-model')
        self.assertEqual(first['model'], 'agy-explicit-model')
        with self.assertRaises(FileNotFoundError):
            harness.run_planned(path, 'fix', [first['result_path']], self.output)
        self.accept(path, 'inspect', first)
        second = harness.run_planned(path, 'fix', [first['result_path']], self.output)
        self.assertEqual(second['status'], 'completed')
        self.assertEqual(second['requested_model'], 'claude-explicit-model')
        self.assertEqual(second['model'], 'claude-explicit-model')
        self.assertEqual(second['model_verification'], 'matching')
        saved_task = harness.read_json(Path(second['result_path']).parent / 'task.json')
        self.assertNotIn(first['response'], saved_task['context'])
        self.assertIn('Parent inspected fixture', saved_task['context'])
        self.assertTrue((Path(second['result_path']).parent / 'plan.json').exists())
        self.assertEqual(harness.git(self.repo, 'status', '--porcelain'), '')

    def test_changed_plan_or_result_invalidates_prior_acceptance(self):
        path = self.save_plan()
        first = harness.run_planned(path, 'inspect', output_root=self.output)
        self.accept(path, 'inspect', first)
        plan = self.plan()
        plan['tasks'][1]['task']['model'] = 'changed-model'
        self.save_plan(plan)
        with self.assertRaisesRegex(ValueError, 'exact plan/task/model'):
            harness.run_planned(path, 'fix', [first['result_path']], self.output)
        self.save_plan()
        altered = {**first, 'response': 'changed after acceptance'}
        harness.write_json(Path(first['result_path']), altered)
        with self.assertRaisesRegex(ValueError, 'valid parent acceptance'):
            harness.run_planned(path, 'fix', [first['result_path']], self.output)

    def test_failed_result_empty_evidence_or_child_cannot_accept(self):
        plan = self.plan()
        plan['tasks'][0]['task']['objective'] = 'error-zero'
        path = self.save_plan(plan)
        failed = harness.run_planned(path, 'inspect', output_root=self.output)
        with self.assertRaisesRegex(ValueError, 'completed'):
            self.accept(path, 'inspect', failed)
        path = self.save_plan()
        result = harness.run_planned(path, 'inspect', output_root=self.output)
        blank = self.base / 'blank.txt'
        blank.write_text(' \n')
        with self.assertRaisesRegex(ValueError, 'nonempty'):
            harness.accept_result(path, 'inspect', result['result_path'], blank)
        with patch.dict(os.environ, {harness.CHILD_MARKER: '1'}), self.assertRaisesRegex(ValueError, 'cannot accept'):
            self.accept(path, 'inspect', result)

    def test_worker_dependency_requires_integrated_files_and_unchanged_accepted_output(self):
        plan = self.plan()
        plan['tasks'][0]['task'] = copy.deepcopy(plan['tasks'][1]['task'])
        plan['tasks'][1]['task']['objective'] = 'review applied changes'
        path = self.save_plan(plan)
        first = harness.run_planned(path, 'inspect', output_root=self.output)
        self.accept(path, 'inspect', first)
        with self.assertRaisesRegex(ValueError, 'Integrate accepted worker'):
            harness.run_planned(path, 'fix', [first['result_path']], self.output)
        workspace = Path(first['workspace'])
        (workspace / 'calc.py').write_text('different after acceptance')
        with self.assertRaisesRegex(ValueError, 'changed after acceptance'):
            harness.run_planned(path, 'fix', [first['result_path']], self.output)

    def single_worker_plan(self, name='agy', checks=None):
        plan = self.plan()
        plan['tasks'] = [plan['tasks'][1]]
        item = plan['tasks'][0]
        item['depends_on'] = []
        item['task'].update(harness=name, model='fixture-model', profile='writer',
                            effort='low', checks=checks or [])
        return self.save_plan(plan)

    def test_revision_keeps_task_session_workspace_and_preserves_original_artifacts(self):
        for name in ('agy', 'claude'):
            with self.subTest(name=name):
                path = self.single_worker_plan(name)
                first = harness.run_planned(path, 'fix', output_root=self.output)
                first_bytes = Path(first['result_path']).read_bytes()
                original = Path(first['result_path']).parent / 'artifacts/new.txt'
                self.assertEqual(harness.run_status(first['run_dir'])['status'], 'awaiting_review')
                feedback = self.base / 'feedback.md'
                feedback.write_text('revise-edit', encoding='utf-8')
                harness.reject_result(path, 'fix', first['result_path'], feedback)
                with self.assertRaisesRegex(ValueError, 'needs revision'):
                    self.accept(path, 'fix', first)
                second = harness.revise_result(path, 'fix', first['result_path'], feedback)
                self.assertEqual(second['status'], 'completed')
                self.assertEqual(second['run_id'], first['run_id'])
                self.assertEqual(second['session_id'], first['session_id'])
                self.assertEqual(second['workspace'], first['workspace'])
                self.assertEqual(second['attempt'], 2)
                self.assertEqual(second['dispatch'], first['dispatch'])
                self.assertEqual(second['usage_scope'], 'cli_reported_aggregation_unverified')
                self.assertIsNone(second['usage_delta'])
                self.assertIsNone(second['cost_delta_usd'])
                self.assertEqual(Path(first['result_path']).read_bytes(), first_bytes)
                self.assertEqual(original.read_text(encoding='utf-8'), '中文 new file\n')
                self.assertEqual((Path(second['result_path']).parent / 'artifacts/new.txt').read_text(encoding='utf-8'), '修订完成\n')
                with self.assertRaisesRegex(ValueError, 'superseded'):
                    self.accept(path, 'fix', first)
                self.accept(path, 'fix', second)
                with self.assertRaisesRegex(ValueError, 'unaccepted'):
                    harness.revise_result(path, 'fix', second['result_path'], feedback)
                self.assertEqual(harness.run_status(first['run_dir'])['status'], 'accepted')

    def test_automatic_checks_gate_acceptance_until_revision_passes(self):
        path = self.single_worker_plan(checks=[{'type': 'cjk_count', 'path': 'new.txt', 'min': 4, 'max': 4},
                                             {'type': 'contains', 'path': 'new.txt', 'text': '修订完成'},
                                             {'type': 'excludes', 'path': 'new.txt', 'text': 'unsupported'}])
        first = harness.run_planned(path, 'fix', output_root=self.output)
        self.assertEqual(first['status'], 'completed')
        self.assertFalse(first['checks']['passed'])
        self.assertEqual(first['checks']['items'][0]['actual'], 2)
        self.assertEqual(harness.run_status(first['run_dir'])['status'], 'needs_revision')
        with self.assertRaisesRegex(ValueError, 'needs revision'):
            self.accept(path, 'fix', first)
        feedback = self.base / 'feedback.md'
        feedback.write_text('revise-edit', encoding='utf-8')
        second = harness.revise_result(path, 'fix', first['result_path'], feedback)
        self.assertTrue(second['checks']['passed'])
        self.accept(path, 'fix', second)

    def test_live_events_and_cancel_are_visible_before_completion(self):
        task = self.task(objective='slow-events')
        with ThreadPoolExecutor(max_workers=1) as pool:
            future = pool.submit(harness.run_task, task, self.output)
            deadline = time.monotonic() + 10
            state = None
            while time.monotonic() < deadline:
                paths = list(self.output.glob('*/progress.json'))
                if paths:
                    state = harness.run_status(paths[0].parent)
                    if state['progress']['events'] >= 2:
                        break
                time.sleep(0.05)
            self.assertIsNotNone(state)
            self.assertGreaterEqual(state['progress']['events'], 2)
            self.assertFalse(future.done())
            self.assertEqual(state['progress']['last_event']['tool'], 'view_file')
            with self.assertRaisesRegex(ValueError, 'busy'), harness.operation_lock(Path(state['run_dir'])):
                pass
            harness.cancel_run(state['run_dir'])
            result = future.result(timeout=10)
            self.assertEqual(result['status'], 'cancelled')

    def test_snapshot_and_manual_edits_cannot_be_accepted_as_child_output(self):
        path = self.single_worker_plan()
        first = harness.run_planned(path, 'fix', output_root=self.output)
        artifact = Path(first['result_path']).parent / 'artifacts/new.txt'
        original = artifact.read_bytes()
        artifact.write_text('tampered')
        with self.assertRaisesRegex(ValueError, 'snapshot changed'):
            self.accept(path, 'fix', first)
        artifact.write_bytes(original)
        extra = Path(first['workspace']) / 'unexpected.txt'
        extra.write_text('parent addition')
        with self.assertRaisesRegex(ValueError, 'changed file set'):
            self.accept(path, 'fix', first)
        extra.unlink()
        (Path(first['workspace']) / 'new.txt').write_text('parent edit')
        with self.assertRaisesRegex(ValueError, 'keep parent edits separate'):
            self.accept(path, 'fix', first)

    def test_handoff_is_curated_and_hash_bound_without_raw_draft(self):
        path = self.save_plan()
        first = harness.run_planned(path, 'inspect', output_root=self.output)
        evidence = self.base / 'verified.md'
        evidence.write_text('Verified against source.', encoding='utf-8')
        handoff = self.base / 'handoff.json'
        packet = {'summary': 'Only these verified statements should inform writing.',
                  'claims': [{'claim': 'Example statement', 'source_url': 'https://example.com/primary',
                              'evidence_level': 'vendor_reported', 'limitations': 'Not independently tested'}],
                  'limitations': ['No runtime test']}
        harness.write_json(handoff, packet)
        harness.accept_result(path, 'inspect', first['result_path'], evidence, handoff)
        second = harness.run_planned(path, 'fix', [first['result_path']], self.output)
        prompt = (Path(second['result_path']).parent / 'prompt.txt').read_text(encoding='utf-8')
        self.assertIn(packet['summary'], prompt)
        self.assertIn('vendor_reported', prompt)
        self.assertNotIn(first['response'], prompt)
        harness.write_json(Path(first['result_path']).parent / 'handoff.json', {**packet, 'summary': 'altered'})
        with self.assertRaisesRegex(ValueError, 'handoff changed'):
            harness.run_planned(path, 'fix', [first['result_path']], self.output)

    def test_revision_rejects_missing_session_and_model_change_without_spawn(self):
        path = self.single_worker_plan()
        first = harness.run_planned(path, 'fix', output_root=self.output)
        feedback = self.base / 'feedback.md'
        feedback.write_text('revise-edit')
        harness.write_json(Path(first['result_path']), {**first, 'session_id': None})
        with patch.object(harness, 'probe') as probe, self.assertRaisesRegex(ValueError, 'session ID'):
            harness.revise_result(path, 'fix', first['result_path'], feedback)
        probe.assert_not_called()
        harness.write_json(Path(first['result_path']), first)
        saved_path = Path(first['run_dir']) / 'task.json'
        original_task = harness.read_json(saved_path)
        harness.write_json(saved_path, {**original_task, 'model': 'unplanned-model'})
        with patch.object(harness, 'probe') as probe, self.assertRaisesRegex(ValueError, 'Saved task changed'):
            harness.revise_result(path, 'fix', first['result_path'], feedback)
        probe.assert_not_called()
        harness.write_json(saved_path, original_task)
        plan = harness.read_json(path)
        plan['tasks'][0]['task']['model'] = 'different-model'
        harness.write_json(path, plan)
        with patch.object(harness, 'probe') as probe, self.assertRaisesRegex(ValueError, 'exact plan/task/model'):
            harness.revise_result(path, 'fix', first['result_path'], feedback)
        probe.assert_not_called()

    def test_resume_must_confirm_the_same_session(self):
        for name in ('claude', 'agy'):
            with self.subTest(name=name):
                path = self.single_worker_plan(name)
                first = harness.run_planned(path, 'fix', output_root=self.output)
                feedback = self.base / 'feedback.md'
                feedback.write_text('session-mismatch')
                second = harness.revise_result(path, 'fix', first['result_path'], feedback)
                self.assertEqual(second['status'], 'protocol_error')
                self.assertEqual(harness.run_status(first['run_dir'])['status'], 'failed')
                with self.assertRaisesRegex(ValueError, 'completed'):
                    self.accept(path, 'fix', second)
                with patch.object(harness, 'probe') as probe, self.assertRaisesRegex(ValueError, 'protocol violations'):
                    harness.revise_result(path, 'fix', second['result_path'], feedback)
                probe.assert_not_called()

    def test_check_configuration_and_effort_rejected_before_model_calls(self):
        task = self.task(mode='worker')
        for check in ({'type': 'shell', 'path': 'new.txt'},
                      {'type': 'cjk_count', 'path': '../escape', 'max': 10},
                      {'type': 'cjk_count', 'path': 'new.txt', 'min': 100, 'max': 10}):
            with self.assertRaises(ValueError):
                harness.validate_task({**task, 'checks': [check]})
        with self.assertRaisesRegex(ValueError, 'Unsupported effort'):
            harness.validate_task({**task, 'effort': 'max'})
        with patch.object(harness, 'probe') as probe, self.assertRaisesRegex(ValueError, 'conflicts with effort'):
            harness.run_task({**task, 'model': 'gemini-3.8-flash-high', 'effort': 'low'}, self.output)
        probe.assert_not_called()
        normalized = harness.validate_task({**task, 'profile': 'writer', 'effort': 'low'})
        args = harness.adapter_args(normalized, 'saved-session')
        self.assertEqual(args[args.index('--effort') + 1], 'low')
        self.assertEqual(args[args.index('--conversation') + 1], 'saved-session')
        prompt = harness.make_prompt(normalized, self.repo)
        self.assertNotIn('Return a concise report', prompt)
        self.assertIn('only the changed relative file paths', prompt)


if __name__ == '__main__':
    unittest.main()
