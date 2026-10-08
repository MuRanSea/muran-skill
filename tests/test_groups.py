"""Public group commands with durable storage and subprocess CLI fixtures."""
from contextlib import redirect_stdout
from concurrent.futures import ThreadPoolExecutor
import importlib.util
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

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / 'skills/multi-harness/scripts'
sys.path.insert(0, str(SCRIPTS))
spec = importlib.util.spec_from_file_location('groups', SCRIPTS / 'groups.py')
groups = importlib.util.module_from_spec(spec)
spec.loader.exec_module(groups)

FAKE = r'''
import json, os, pathlib, signal, sys, time, uuid
if '--version' in sys.argv:
    print('group-fixture 1.0'); raise SystemExit()
if '--help' in sys.argv:
    print('--output-format --tools --allowedTools --safe-mode --strict-mcp-config --disable-slash-commands --permission-mode --permission-prompts --resume --conversation --effort --max-budget-usd --mode --input-format --print-timeout --model'); raise SystemExit()
agy = '--input-format' in sys.argv
raw = sys.stdin.read()
if agy: raw = json.loads(raw)['message']['content']
packet = json.loads(raw.split('\n\n', 1)[1])
discussion = packet.get('discussion', {'message': {'body': packet['objective']}})
body = packet.get('feedback', discussion['message']['body'])
flag = '--conversation' if agy else '--resume'
session = sys.argv[sys.argv.index(flag) + 1] if flag in sys.argv else 'fixture-' + uuid.uuid4().hex
statefile = pathlib.Path(os.environ['GROUP_FAKE_STATE']) / (session + '.json')
if flag in sys.argv:
    memory = json.loads(statefile.read_text())
else:
    memory = {'first': body}
    statefile.write_text(json.dumps(memory))
model = sys.argv[sys.argv.index('--model') + 1]
if agy:
    print(json.dumps({'event':'init','conversation_id':session,'init':{'model':model}}), flush=True)
else:
    print(json.dumps({'type':'system','subtype':'init','session_id':session}), flush=True)
if body == 'slow': time.sleep(8)
if body == 'kill-controller':
    os.kill(int(os.environ['GROUP_TEST_CONTROLLER_PID']), signal.SIGTERM)
    raise SystemExit()
if body == 'broken':
    print('invalid-stream'); raise SystemExit()
if body == 'auth-error':
    print(json.dumps({'type':'assistant','message':{'model':'<synthetic>','content':[]}}))
    print(json.dumps({'type':'result','session_id':session,'subtype':'success','is_error':True,
        'result':'Failed to authenticate: OAuth session expired and could not be refreshed','errors':[]}))
    raise SystemExit(1)
if body == 'mismatch': session = 'unexpected-session'
if body == 'wrong-model': model = 'unplanned-model'
if body == 'violate': pathlib.Path('outside.txt').write_text('unexpected')
answer = json.dumps({'body':body, 'first':memory['first'], 'continued':flag in sys.argv, 'discussion':discussion}, ensure_ascii=False)
if agy:
    print(json.dumps({'event':'result','conversation_id':session,'result':{'status':'SUCCESS','response':answer}}))
else:
    print(json.dumps({'type':'assistant','message':{'model':model,'content':[]}}))
    print(json.dumps({'type':'result','session_id':session,'subtype':'success','is_error':False,'result':answer,'errors':[]}))
'''


class GroupTests(unittest.TestCase):
    def setUp(self):
        parent = ROOT / '.cache/tests'
        parent.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix='groups-', dir=parent)
        self.base = Path(self.temp.name).resolve()
        self.repo = self.base / 'project 中文'
        self.repo.mkdir()
        self.store = self.base / 'groups.sqlite3'
        self.fake = self.base / 'fake cli.py'
        self.fake.write_text(FAKE, encoding='utf-8')
        session_dir = self.base / 'fake-sessions'
        session_dir.mkdir()
        self.env = patch.dict(os.environ, {'PYTHONUTF8': '1', 'GROUP_FAKE_STATE': str(session_dir)})
        self.env.start()
        self.launcher = patch.object(groups.harness, 'resolve_launcher', return_value=[sys.executable, str(self.fake)])
        self.launcher.start()
        for args in [('init', '-q'), ('-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.invalid',
                                     '-c', 'commit.gpgsign=false', 'commit', '--allow-empty', '-qm', 'fixture')]:
            subprocess.run(['git', *args], cwd=self.repo, check=True, capture_output=True)

    def tearDown(self):
        self.launcher.stop()
        self.env.stop()
        self.assertTrue(self.base.is_relative_to((ROOT / '.cache/tests').resolve()))
        self.temp.cleanup()

    def file(self, name, value):
        path = self.base / name
        path.write_text(json.dumps(value, ensure_ascii=False), encoding='utf-8')
        return str(path)

    def invoke(self, *args, ok=True):
        out = io.StringIO()
        with redirect_stdout(out):
            code = groups.main(['--store', str(self.store), *map(str, args)])
        value = json.loads(out.getvalue())
        self.assertEqual(code, 0 if ok else 1, value)
        return value

    def team(self, **limits):
        return self.invoke('team', '--name', '研究组', '--config', self.file('team.json', {
            'members': [
                {'id': 'researcher', 'role': '研究员', 'harness': 'claude', 'model': 'fixture-claude', 'mode': 'advisor', **limits},
                {'id': 'editor', 'role': '编辑', 'harness': 'agy', 'model': 'fixture-gemini', 'mode': 'advisor', **limits},
            ]}))

    def open_group(self, name='Jev', context='thread-one', **extra):
        return self.invoke('open', '--config', self.file('group.json', {
            'name': name, 'goal': '研究请求内容审查', 'strategy': '先调研，后写作，负责人验收',
            'acceptance': ['来源可核对'], 'cwd': str(self.repo), 'team': '研究组', 'context': context, **extra}))

    def test_open_find_and_reuse_explicit_team_across_processes(self):
        self.team()
        first = self.open_group()
        cmd = [sys.executable, str(SCRIPTS / 'groups.py'), '--store', str(self.store),
               'status', '--cwd', str(self.repo), '--context', 'thread-one']
        result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
        self.assertEqual(result.returncode, 0, result.stderr)
        status = json.loads(result.stdout)
        self.assertEqual(status['id'], first['id'])
        self.assertEqual(status['members'][0]['model'], 'fixture-claude')
        self.assertEqual(status['state'], 'active')
        self.open_group('Second', 'thread-two')
        ambiguous = self.invoke('status', '--cwd', self.repo, ok=False)
        self.assertIn('ambiguous', ambiguous['error'])
        self.assertEqual(self.invoke('status', '--cwd', self.repo, '--context', 'thread-one')['id'], first['id'])
        elsewhere = self.base / 'elsewhere'
        elsewhere.mkdir()
        self.invoke('status', '--cwd', elsewhere, '--context', 'thread-one', ok=False)

    def send(self, group, body, to='researcher', **options):
        path = self.base / 'message.txt'
        path.write_text(body, encoding='utf-8')
        args = ['send', '--cwd', self.repo, '--group', group['id'], '--to', to, '--text-file', path]
        for key, value in options.items():
            args.extend(['--' + key.replace('_', '-'), str(value)])
        return self.invoke(*args)

    def test_addressed_messages_are_durable_and_idempotent_without_waking_members(self):
        self.team()
        group = self.open_group()
        first = self.send(group, '请核对官方接口', to='研究员', request_id='request-one')
        same = self.send(group, '请核对官方接口', to='研究员', request_id='request-one')
        self.assertEqual(first['id'], same['id'])
        self.send(group, '只讨论，不改文件', to='codex', kind='decision')
        messages = self.invoke('history', '--cwd', self.repo, '--group', group['id'])['messages']
        self.assertEqual([(m['recipient'], m['status']) for m in messages], [('researcher', 'queued'), ('codex', 'recorded')])
        self.assertTrue(all(m['sender'] == 'codex' for m in messages))
        status = self.invoke('status', '--cwd', self.repo, '--group', group['id'])
        self.assertEqual(status['queue'], {'researcher': 1, 'editor': 0})
        self.assertEqual(status['turns_used'], 0)
        self.assertFalse((self.base / 'groups-runs').exists())

    def test_dispatch_only_recipient_and_resume_its_real_cli_session(self):
        self.team()
        group = self.open_group()
        self.send(group, 'alpha')
        self.invoke('dispatch', '--cwd', self.repo, '--group', group['id'])
        messages = self.invoke('history', '--cwd', self.repo, '--group', group['id'])['messages']
        reply = messages[-1]
        self.assertEqual(reply['sender'], 'researcher')
        self.assertEqual(reply['kind'], 'reply')
        self.assertFalse(json.loads(reply['body'])['continued'])
        first_session = reply['provenance']['session_id']
        self.send(group, 'beta', reference=reply['id'])
        self.invoke('dispatch', '--cwd', self.repo, '--group', group['id'])
        second = self.invoke('history', '--cwd', self.repo, '--group', group['id'])['messages'][-1]
        self.assertTrue(json.loads(second['body'])['continued'])
        self.assertEqual(json.loads(second['body'])['first'], 'alpha')
        self.assertEqual(second['provenance']['session_id'], first_session)
        self.send(group, 'editor-only', to='editor')
        self.invoke('dispatch', '--cwd', self.repo, '--group', group['id'])
        third = self.invoke('history', '--cwd', self.repo, '--group', group['id'])['messages'][-1]
        self.assertEqual(third['sender'], 'editor')
        self.assertEqual(json.loads(third['body'])['first'], 'editor-only')
        self.assertNotEqual(third['provenance']['session_id'], first_session)
        self.assertNotIn('alpha', json.dumps(json.loads(third['body'])['discussion']))
        self.send(group, 'editor-followup', to='editor')
        self.invoke('dispatch', '--cwd', self.repo, '--group', group['id'])
        fourth = self.invoke('history', '--cwd', self.repo, '--group', group['id'])['messages'][-1]
        self.assertTrue(json.loads(fourth['body'])['continued'])
        self.assertEqual(json.loads(fourth['body'])['first'], 'editor-only')
        self.assertEqual(fourth['provenance']['session_id'], third['provenance']['session_id'])
        self.assertEqual(self.invoke('status', '--cwd', self.repo, '--group', group['id'])['turns_used'], 4)

    def test_timeout_preserves_queue_and_blocks_automatic_continuation(self):
        self.team(timeout_seconds=1)
        group = self.open_group()
        self.send(group, 'slow')
        self.send(group, 'later', to='editor')
        result = self.invoke('dispatch', '--cwd', self.repo, '--group', group['id'], '--limit', 2, ok=False)
        self.assertEqual(result['turns'][0]['status'], 'unknown')
        terminal = json.loads(Path(result['turns'][0]['result_path']).read_text(encoding='utf-8'))
        self.assertEqual(terminal['status'], 'timed_out')
        status = self.invoke('status', '--cwd', self.repo, '--group', group['id'])
        self.assertEqual(status['state'], 'needs_attention')
        self.assertEqual(status['queue']['editor'], 1)
        self.assertEqual(status['turns_used'], 1)
        self.invoke('resume', '--cwd', self.repo, '--group', group['id'], ok=False)
        self.invoke('dispatch', '--cwd', self.repo, '--group', group['id'], ok=False)
        self.assertEqual(len(list((self.base / 'fake-sessions').iterdir())), 1)

    def test_agy_scope_violation_cannot_resume_or_modify_source(self):
        self.team()
        group = self.open_group()
        self.send(group, 'violate', to='editor')
        result = self.invoke('dispatch', '--cwd', self.repo, '--group', group['id'], ok=False)
        terminal = json.loads(Path(result['turns'][0]['result_path']).read_text(encoding='utf-8'))
        self.assertEqual(terminal['status'], 'scope_violation')
        self.assertFalse((self.repo / 'outside.txt').exists())
        self.send(group, 'do not continue', to='editor')
        self.invoke('dispatch', '--cwd', self.repo, '--group', group['id'], ok=False)
        self.assertEqual(len(list((self.base / 'fake-sessions').iterdir())), 1)

    def test_agy_source_baseline_change_requires_new_group(self):
        self.team()
        group = self.open_group()
        self.send(group, 'first', to='editor')
        self.invoke('dispatch', '--cwd', self.repo, '--group', group['id'])
        subprocess.run(['git', '-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.invalid',
                        '-c', 'commit.gpgsign=false', 'commit', '--allow-empty', '-qm', 'new baseline'],
                       cwd=self.repo, check=True, capture_output=True)
        self.send(group, 'second', to='editor')
        result = self.invoke('dispatch', '--cwd', self.repo, '--group', group['id'], ok=False)
        self.assertIn('baseline', result['turns'][0]['error'])
        self.assertEqual(len(list((self.base / 'fake-sessions').iterdir())), 1)

    def test_pause_cancels_active_turn_preserves_queue_and_resume_does_not_retry_it(self):
        self.team()
        group = self.open_group()
        self.send(group, 'slow')
        service = groups.Groups(self.store)
        with ThreadPoolExecutor(max_workers=1) as pool:
            running = pool.submit(service.dispatch, group['id'])
            deadline = time.monotonic() + 5
            while time.monotonic() < deadline:
                status = self.invoke('status', '--cwd', self.repo, '--group', group['id'])
                if (status.get('active_turn') or {}).get('progress'):
                    break
                time.sleep(.05)
            else:
                self.fail('CLI never reached a visible running state')
            self.send(group, 'later', to='researcher')
            self.invoke('dispatch', '--cwd', self.repo, '--group', group['id'], ok=False)
            paused = self.invoke('pause', '--cwd', self.repo, '--group', group['id'])
            self.assertIn(paused['state'], ('pausing', 'paused'))
            running.result(timeout=6)
        status = self.invoke('status', '--cwd', self.repo, '--group', group['id'])
        self.assertEqual(status['state'], 'paused')
        self.assertEqual(status['queue']['researcher'], 1)
        self.invoke('dispatch', '--cwd', self.repo, '--group', group['id'], ok=False)
        self.invoke('resume', '--cwd', self.repo, '--group', group['id'])
        self.invoke('dispatch', '--cwd', self.repo, '--group', group['id'])
        messages = self.invoke('history', '--cwd', self.repo, '--group', group['id'])['messages']
        self.assertEqual(messages[0]['status'], 'cancelled')
        self.assertEqual(messages[-1]['sender'], 'researcher')
        self.assertEqual(len([m for m in messages if m['kind'] == 'reply']), 1)

    def test_controller_crash_is_unknown_and_never_implicitly_replayed(self):
        self.team()
        group = self.open_group()
        self.send(group, 'kill-controller')
        driver = self.base / 'driver.py'
        driver.write_text('import os, sys\nos.environ["GROUP_TEST_CONTROLLER_PID"] = str(os.getpid())\nsys.path.insert(0, ' + repr(str(SCRIPTS)) + ')\nimport groups\n'
                          'groups.harness.resolve_launcher = lambda name: [sys.executable, ' + repr(str(self.fake)) + ']\n'
                          'raise SystemExit(groups.main(sys.argv[1:]))\n', encoding='utf-8')
        result = subprocess.run([sys.executable, str(driver), '--store', str(self.store), 'dispatch',
                                 '--cwd', str(self.repo), '--group', group['id']], capture_output=True, timeout=8)
        self.assertNotEqual(result.returncode, 0, result.stdout.decode('utf-8', errors='replace'))
        status = self.invoke('status', '--cwd', self.repo, '--group', group['id'])
        self.assertEqual(status['turns_used'], 1)
        recovered = self.invoke('reconcile', '--cwd', self.repo, '--group', group['id'])
        self.assertEqual(recovered['turns'][0]['status'], 'unknown')
        self.invoke('resume', '--cwd', self.repo, '--group', group['id'], ok=False)
        self.invoke('dispatch', '--cwd', self.repo, '--group', group['id'], ok=False)
        self.assertEqual(self.invoke('status', '--cwd', self.repo, '--group', group['id'])['turns_used'], 1)

    def test_followup_keeps_linked_task_acceptance_and_results_unchanged(self):
        self.team()
        group = self.open_group()
        plan = self.file('plan.json', {
            'schema_version': 1, 'plan_id': 'original-task', 'state': 'ready', 'goal': 'Read source',
            'strategy': 'One scoped read', 'cwd': str(self.repo), 'acceptance': ['Evidence checked'],
            'tasks': [{'id': 'inspect', 'depends_on': [], 'rationale': 'User assignment', 'task': {
                'harness': 'claude', 'model': 'fixture-claude', 'mode': 'advisor', 'objective': 'original-task',
                'acceptance': ['Parent verifies result'], 'timeout_seconds': 10}}]})
        original = groups.harness.run_planned(plan, 'inspect', output_root=self.base / 'tasks')
        evidence = self.base / 'evidence.md'
        evidence.write_text('Verified fixture response and no source modifications.', encoding='utf-8')
        groups.harness.accept_result(plan, 'inspect', original['result_path'], evidence)
        root = Path(original['run_dir'])
        before = {name: (root / name).read_bytes() for name in ('run.json', 'result.json', 'acceptance.json')}
        self.invoke('link', '--cwd', self.repo, '--group', group['id'], '--member', 'researcher', '--result', original['result_path'])
        self.send(group, '解释已完成任务的依据')
        self.invoke('dispatch', '--cwd', self.repo, '--group', group['id'])
        status = self.invoke('status', '--cwd', self.repo, '--group', group['id'])
        self.assertEqual(status['tasks'][0]['status'], 'accepted')
        self.assertEqual(before, {name: (root / name).read_bytes() for name in before})

    def test_linked_task_reports_running_during_revision_before_result_exists(self):
        self.team()
        group = self.open_group()
        plan = self.file('plan.json', {
            'schema_version': 1, 'plan_id': 'linked-running', 'state': 'ready', 'goal': 'Read source',
            'strategy': 'One scoped read', 'cwd': str(self.repo), 'acceptance': ['Evidence checked'],
            'tasks': [{'id': 'inspect', 'depends_on': [], 'rationale': 'User assignment', 'task': {
                'harness': 'claude', 'model': 'fixture-claude', 'mode': 'advisor', 'objective': 'original-task',
                'acceptance': ['Parent verifies result'], 'timeout_seconds': 10}}]})
        original = groups.harness.run_planned(plan, 'inspect', output_root=self.base / 'tasks')
        self.invoke('link', '--cwd', self.repo, '--group', group['id'], '--member', 'researcher', '--result', original['result_path'])
        feedback = self.base / 'feedback.txt'
        feedback.write_text('slow', encoding='utf-8')
        root = Path(original['run_dir'])
        with ThreadPoolExecutor(max_workers=1) as pool:
            running = pool.submit(groups.harness.revise_result, plan, 'inspect', original['result_path'], feedback)
            try:
                deadline = time.monotonic() + 5
                while time.monotonic() < deadline:
                    state = groups.harness.read_json(root / 'run.json')
                    if state['status'] == 'running':
                        break
                    time.sleep(.05)
                else:
                    self.fail('Revision did not start')
                status = self.invoke('status', '--cwd', self.repo, '--group', group['id'])
                self.assertEqual(status['tasks'][0]['status'], 'running')
                self.assertFalse(Path(status['tasks'][0]['result_path']).exists())
            finally:
                groups.harness.cancel_run(root)
                running.result(timeout=6)

    def test_group_list_and_team_updates_do_not_change_existing_member_models(self):
        self.team()
        group = self.open_group()
        listed = self.invoke('list', '--cwd', self.repo)
        self.assertEqual(listed['groups'][0]['id'], group['id'])
        self.assertEqual(listed['teams'][0]['name'], '研究组')
        self.invoke('team', '--name', '研究组', '--config', self.file('changed-team.json', {
            'members': [{'id': 'researcher', 'role': '研究员', 'harness': 'claude', 'model': 'changed-model'}]}))
        original = self.invoke('status', '--cwd', self.repo, '--group', group['id'])
        self.assertEqual(original['members'][0]['model'], 'fixture-claude')

    def test_budget_stops_new_dispatch_until_explicit_extension(self):
        self.team()
        group = self.open_group(max_turns=1)
        self.send(group, 'one')
        self.invoke('dispatch', '--cwd', self.repo, '--group', group['id'])
        self.send(group, 'two')
        self.invoke('dispatch', '--cwd', self.repo, '--group', group['id'], ok=False)
        self.assertEqual(self.invoke('status', '--cwd', self.repo, '--group', group['id'])['queue']['researcher'], 1)
        self.invoke('resume', '--cwd', self.repo, '--group', group['id'], '--additional-turns', '1')
        self.invoke('dispatch', '--cwd', self.repo, '--group', group['id'])
        self.assertEqual(self.invoke('status', '--cwd', self.repo, '--group', group['id'])['turns_used'], 2)

    def test_invalid_stream_or_session_does_not_silently_start_a_new_conversation(self):
        self.team()
        for body in ('broken', 'mismatch'):
            with self.subTest(body=body):
                group = self.open_group(body, body)
                self.send(group, body)
                failure = self.invoke('dispatch', '--cwd', self.repo, '--group', group['id'], ok=False)
                self.assertEqual(failure['turns'][0]['status'], 'unknown')
                self.send(group, 'do not replay')
                self.invoke('resume', '--cwd', self.repo, '--group', group['id'], ok=False)
                self.invoke('dispatch', '--cwd', self.repo, '--group', group['id'], ok=False)
                self.assertEqual(self.invoke('status', '--cwd', self.repo, '--group', group['id'])['turns_used'], 1)

    def test_reported_model_mismatch_requires_review_before_continuing(self):
        self.team()
        group = self.open_group()
        self.send(group, 'wrong-model')
        result = self.invoke('dispatch', '--cwd', self.repo, '--group', group['id'], ok=False)
        self.assertEqual(result['turns'][0]['status'], 'failed')
        self.send(group, 'do not resume silently')
        result = self.invoke('dispatch', '--cwd', self.repo, '--group', group['id'], ok=False)
        self.assertIn('model', result['turns'][0]['error'].lower())

    def test_cli_authentication_error_is_not_hidden_by_a_synthetic_model_label(self):
        self.team()
        group = self.open_group()
        self.send(group, 'auth-error')
        result = self.invoke('dispatch', '--cwd', self.repo, '--group', group['id'], ok=False)
        self.assertEqual(result['turns'][0]['status'], 'failed')
        self.assertIn('OAuth session expired', result['turns'][0]['error'])
        self.assertNotIn('Reported model differs', result['turns'][0]['error'])


if __name__ == '__main__':
    unittest.main()
