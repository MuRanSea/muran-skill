"""Public group commands: durable state, parallel advance, review gates and recovery."""
from contextlib import redirect_stdout
from concurrent.futures import ThreadPoolExecutor
import io
import json
from pathlib import Path
import subprocess
import sys
import time
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from multi_harness_fixture import SCRIPTS, Fixture  # noqa: E402

import groups  # noqa: E402
import runner  # noqa: E402

MEMBERS = [
    {'id': 'researcher', 'role': '研究员', 'harness': 'claude', 'model': 'fixture-claude', 'mode': 'advisor', 'timeout_seconds': 20},
    {'id': 'editor', 'role': '编辑', 'harness': 'agy', 'model': 'fixture-gemini', 'mode': 'advisor', 'timeout_seconds': 20},
]


class GroupTests(Fixture):
    def setUp(self):
        super().setUp()
        self.store = self.base / 'state' / 'collab.sqlite3'

    def file(self, name, value):
        path = self.base / name
        path.write_text(json.dumps(value, ensure_ascii=False), encoding='utf-8')
        return path

    def invoke(self, *args, ok=True):
        out = io.StringIO()
        with redirect_stdout(out):
            code = groups.main(['--store', str(self.store), *map(str, args)])
        value = json.loads(out.getvalue())
        self.assertEqual(code, 0 if ok else 1, value)
        return value

    def scoped(self, command, group, *args, ok=True):
        return self.invoke(command, '--cwd', self.repo, '--group', group['id'], *args, ok=ok)

    def open_group(self, name='Jev', context='thread-one', members=None, **extra):
        config = {'name': name, 'goal': '研究请求内容审查', 'strategy': '先调研，后写作，负责人验收',
                  'acceptance': ['来源可核对'], 'cwd': str(self.repo), 'context': context, **extra}
        if 'team' not in config:
            config['members'] = members or MEMBERS
        return self.invoke('open', '--config', self.file('group.json', config))

    def send(self, group, body, to='researcher', *extra):
        return self.scoped('send', group, '--to', to, '--text', body, *extra)['messages']

    def last_reply(self, group, sender=None):
        messages = self.scoped('history', group)['messages']
        replies = [m for m in messages if m['kind'] == 'reply' and (sender is None or m['sender'] == sender)]
        return replies[-1], json.loads(replies[-1]['body'])

    def plan(self, group, tasks, state='ready'):
        return self.scoped('plan', group, '--config', self.file('plan.json', {'state': state, 'tasks': tasks}))

    def task(self, task_id, member, objective, **extra):
        return {'id': task_id, 'member': member, 'objective': objective, 'acceptance': ['Parent verifies'], **extra}

    def accept(self, group, task_id, note='Parent checked the fixture output.', *extra):
        return self.scoped('accept', group, '--task', task_id, '--note', note, *extra)

    def tasks(self, group):
        return {t['id']: t for t in self.scoped('status', group)['tasks']}

    # ---- groups and discussion ----------------------------------------------

    def test_open_find_and_reuse_saved_team_across_processes(self):
        self.invoke('team', '--name', '研究组', '--config', self.file('team.json', {'members': MEMBERS}))
        first = self.open_group(team='研究组')
        result = subprocess.run([sys.executable, str(SCRIPTS / 'groups.py'), '--store', str(self.store), 'status',
                                 '--cwd', str(self.repo), '--context', 'thread-one'], capture_output=True, text=True, encoding='utf-8')
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        status = json.loads(result.stdout)
        self.assertEqual(status['id'], first['id'])
        self.assertEqual(status['members'][0]['model'], 'fixture-claude')
        self.open_group('Second', 'thread-two')
        self.assertIn('ambiguous', self.invoke('status', '--cwd', self.repo, ok=False)['error'])
        self.assertEqual(self.invoke('status', '--cwd', self.repo, '--context', 'thread-one')['id'], first['id'])
        elsewhere = self.base / 'elsewhere'
        elsewhere.mkdir()
        self.invoke('status', '--cwd', elsewhere, '--context', 'thread-one', ok=False)
        self.invoke('team', '--name', '研究组', '--config', self.file('changed.json', {'members': [
            {'id': 'researcher', 'role': '研究员', 'harness': 'claude', 'model': 'changed-model'}]}))
        self.assertEqual(self.scoped('status', first)['members'][0]['model'], 'fixture-claude')
        self.assertEqual(len(self.invoke('list', '--cwd', self.repo)['groups']), 2)

    def test_messages_are_durable_idempotent_and_do_not_wake_members(self):
        group = self.open_group()
        first = self.send(group, '请核对官方接口', '研究员', '--request-id', 'request-one')
        same = self.send(group, '请核对官方接口', '研究员', '--request-id', 'request-one')
        self.assertEqual(first[0]['id'], same[0]['id'])
        self.scoped('send', group, '--to', 'researcher', '--text', 'different', '--request-id', 'request-one', ok=False)
        both = self.send(group, '大家评审方案', 'all', '--request-id', 'review')
        self.assertEqual([m['recipient'] for m in both], ['researcher', 'editor'])
        self.scoped('send', group, '--to', 'codex', '--kind', 'decision', '--text', '只讨论，不改文件')
        self.scoped('send', group, '--to', 'editor', '--kind', 'decision', '--text', 'nope', ok=False)
        status = self.scoped('status', group)
        self.assertEqual(status['queue'], {'researcher': 2, 'editor': 1})
        self.assertEqual(status['turns_used'], 0)
        self.assertTrue(any(hint.startswith('advance') for hint in status['next']))
        self.assertEqual(self.sessions_started(), 0)

    def test_advance_runs_members_in_parallel_and_resumes_each_session(self):
        group = self.open_group()
        self.send(group, 'nap alpha')
        self.send(group, 'nap beta', 'editor')
        started = time.monotonic()
        result = self.scoped('advance', group)
        self.assertLess(time.monotonic() - started, 5.5, 'members should run concurrently')
        self.assertEqual(sorted((r['member'], r['status']) for r in result['results']),
                         [('editor', 'replied'), ('researcher', 'replied')])
        reply, body = self.last_reply(group, 'researcher')
        self.assertFalse(body['continued'])
        self.send(group, 'gamma', 'researcher', '--reference', reply['id'])
        self.scoped('advance', group)
        second, body = self.last_reply(group, 'researcher')
        self.assertTrue(body['continued'])
        self.assertEqual(body['first'], 'nap alpha')
        self.assertEqual(second['provenance']['session_id'], reply['provenance']['session_id'])
        self.assertEqual(body['packet']['discussion']['quoted_references'][0]['id'], reply['id'])
        _, editor = self.last_reply(group, 'editor')
        self.assertNotIn('alpha', json.dumps(editor['packet']))
        self.assertEqual(self.scoped('status', group)['turns_used'], 3)

    def test_failed_turn_blocks_only_that_member_and_fork_restarts_with_carryover(self):
        group = self.open_group(members=[{**MEMBERS[0], 'timeout_seconds': 4}, MEMBERS[1]])
        self.send(group, 'remember RIVER-42')
        self.scoped('advance', group)
        self.send(group, 'slow')
        self.send(group, 'editor still works', 'editor')
        result = self.scoped('advance', group, ok=False)
        outcome = {r['member']: r for r in result['results']}
        self.assertEqual(outcome['researcher']['status'], 'failed')
        self.assertIn('timed_out', outcome['researcher']['error'])
        self.assertEqual(outcome['editor']['status'], 'replied')
        status = self.scoped('status', group)
        self.assertEqual(status['state'], 'active')
        self.assertTrue(status['members'][0]['blocked'])
        self.send(group, 'queued while blocked')
        blocked = self.scoped('advance', group, ok=False)
        self.assertIn('fork --member', blocked['results'][0]['error'])
        sessions = self.sessions_started()
        self.scoped('fork', group, '--member', 'researcher')
        self.scoped('advance', group)
        _, body = self.last_reply(group, 'researcher')
        self.assertFalse(body['continued'])
        self.assertEqual(self.sessions_started(), sessions + 1)
        self.assertIn('RIVER-42', json.dumps(body['packet']['discussion']['carryover'], ensure_ascii=False))

    def test_pause_cancels_active_turn_preserves_queue_and_resume_continues_the_session(self):
        group = self.open_group()
        self.send(group, 'slow-init')
        service = groups.Groups(self.store)
        with ThreadPoolExecutor(max_workers=1) as pool:
            running = pool.submit(service.advance, group['id'])
            deadline = time.monotonic() + 15
            while time.monotonic() < deadline and not running.done():
                turns = self.scoped('status', group)['running_turns']
                progress = (turns[0].get('progress') or {}) if turns else {}
                if progress.get('session_id'):
                    break
                time.sleep(.05)
            else:
                self.fail('CLI never reported a session ID before pause: '
                          + (json.dumps(running.result(), ensure_ascii=False)[:2000] if running.done() else 'timeout'))
            session_id = progress['session_id']
            self.send(group, 'later')
            self.assertEqual(self.scoped('advance', group)['results'], [])
            self.assertIn(self.scoped('pause', group)['state'], ('pausing', 'paused'))
            running.result(timeout=10)
        status = self.scoped('status', group)
        self.assertEqual(status['state'], 'paused')
        self.assertEqual(status['queue']['researcher'], 1)
        self.scoped('advance', group, ok=False)
        self.scoped('resume', group)
        self.scoped('advance', group)
        messages = self.scoped('history', group)['messages']
        self.assertEqual(messages[0]['status'], 'cancelled')
        reply, body = self.last_reply(group)
        self.assertEqual(reply['provenance']['session_id'], session_id)
        self.assertEqual((body['continued'], body['first'], body['body']), (True, 'slow-init', 'later'))
        self.assertEqual(len([m for m in messages if m['kind'] == 'reply']), 1)

    def test_controller_crash_is_unknown_never_replayed_and_recoverable_by_fork(self):
        group = self.open_group()
        self.send(group, 'kill-controller')
        result = subprocess.run([sys.executable, '-X', 'utf8', str(SCRIPTS / 'groups.py'), '--store', str(self.store),
                                 'advance', '--cwd', str(self.repo), '--group', group['id']], capture_output=True, timeout=30)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(len(self.scoped('status', group)['running_turns']), 1)
        recovered = self.scoped('reconcile', group)
        self.assertEqual(recovered['recovered'][0]['status'], 'unknown')
        self.assertTrue(self.scoped('status', group)['members'][0]['blocked'])
        self.send(group, 'after crash')
        self.scoped('advance', group, ok=False)
        self.scoped('fork', group, '--member', 'researcher', '--note', 'Earlier turn lost; continue from the brief.')
        self.scoped('advance', group)
        _, body = self.last_reply(group)
        self.assertEqual(body['packet']['discussion']['carryover'], {'summary': 'Earlier turn lost; continue from the brief.'})
        statuses = [m['status'] for m in self.scoped('history', group)['messages'] if m['kind'] == 'question']
        self.assertEqual(statuses, ['abandoned', 'replied'])

    def test_model_mismatch_and_auth_errors_are_explicit(self):
        group = self.open_group()
        self.send(group, 'wrong-model')
        result = self.scoped('advance', group, ok=False)
        self.assertEqual(result['results'][0]['status'], 'failed')
        self.assertIn('model', result['results'][0]['error'].lower())
        self.send(group, 'auth-error', 'researcher')
        self.scoped('fork', group, '--member', 'researcher')
        result = self.scoped('advance', group, ok=False)
        self.assertIn('OAuth session expired', result['results'][0]['error'])
        self.assertNotIn('Reported model differs', result['results'][0]['error'])

    def test_agy_member_follows_new_commits_and_uncommitted_work_in_the_same_session(self):
        group = self.open_group()
        self.send(group, 'read calc.py', 'editor')
        self.scoped('advance', group)
        first, _ = self.last_reply(group, 'editor')
        (self.repo / 'calc.py').write_text('committed change\n')
        self.commit('new baseline')
        (self.repo / 'notes.md').write_text('uncommitted\n')
        self.send(group, 'read calc.py notes.md', 'editor')
        self.scoped('advance', group)
        second, body = self.last_reply(group, 'editor')
        self.assertTrue(body['continued'])
        self.assertEqual(body['seen'], {'calc.py': 'committed change\n', 'notes.md': 'uncommitted\n'})
        self.assertEqual(first['provenance']['session_id'], second['provenance']['session_id'])

    def test_agy_discussion_scope_violation_blocks_member_and_leaves_source_alone(self):
        group = self.open_group()
        self.send(group, 'violate', 'editor')
        result = self.scoped('advance', group, ok=False)
        self.assertEqual(runner.read_json(result['results'][0]['result_path'])['status'], 'scope_violation')
        self.assertFalse((self.repo / 'outside.txt').exists())
        self.send(group, 'do not continue', 'editor')
        self.scoped('advance', group, ok=False)
        self.assertEqual(self.sessions_started(), 1)

    def test_turn_budget_stops_until_explicit_extension(self):
        group = self.open_group(max_turns=1)
        self.send(group, 'one')
        self.scoped('advance', group)
        self.send(group, 'two')
        self.assertIn('budget', self.scoped('advance', group, ok=False)['results'][0]['error'])
        self.scoped('resume', group, '--additional-turns', 1)
        self.scoped('advance', group)
        self.assertEqual(self.scoped('status', group)['turns_used'], 2)

    # ---- planned tasks ----------------------------------------------------

    def test_plan_dispatch_review_gate_and_handoff_flow(self):
        group = self.open_group()
        self.send(group, 'Explain where subtraction happens')
        self.scoped('advance', group)
        self.plan(group, [self.task('inspect', 'editor', 'inspect input handling'),
                          self.task('fix', '研究员', 'edit', mode='worker', allowed_paths=['calc.py', 'new.txt'],
                                    depends_on=['inspect'])], state='draft')
        self.assertTrue(any(h.startswith('approve') for h in self.scoped('status', group)['next']))
        self.assertEqual(self.scoped('advance', group)['results'], [])
        self.scoped('approve', group)
        wave = self.scoped('advance', group)
        self.assertEqual([(r['id'], r['state']) for r in wave['results']], [('inspect', 'awaiting_review')])
        self.assertEqual(self.tasks(group)['fix']['waiting_on'], ['inspect'])
        inspect = self.scoped('show', group, '--task', 'inspect')
        handoff = self.file('handoff.json', {'summary': 'Verified: add() subtracts.', 'claims': [], 'limitations': ['fixture']})
        self.accept(group, 'inspect', 'Checked calc.py myself.', '--handoff', handoff)
        wave = self.scoped('advance', group)
        fix = wave['results'][0]
        self.assertEqual((fix['id'], fix['state'], fix['changed_files']), ('fix', 'awaiting_review', ['calc.py', 'new.txt']))
        prompt = (Path(fix['result_path']).parent / 'prompt.txt').read_text(encoding='utf-8')
        self.assertIn('Verified: add() subtracts.', prompt)
        self.assertNotIn(inspect['response'], prompt)
        self.assertIn('member_discussion', prompt)
        self.assertIn('Explain where subtraction happens', prompt)
        self.assertEqual(runner.read_json(fix['result_path'])['requested_model'], 'fixture-claude')
        self.accept(group, 'fix')
        self.assertEqual(self.git('status', '--porcelain'), '')
        integrated = self.scoped('integrate', group, '--task', 'fix')
        self.assertEqual(integrated['integration'], 'applied')
        self.assertIn('a + b', (self.repo / 'calc.py').read_text())
        self.assertEqual(self.scoped('integrate', group, '--task', 'fix')['integration'], 'already_present')
        self.assertTrue(any('all tasks accepted' in h for h in self.scoped('status', group)['next']))

    def test_chained_workers_receive_accepted_changes_without_any_commit(self):
        (self.repo / 'wip.txt').write_text('user work in progress\n')
        group = self.open_group()
        self.plan(group, [
            self.task('first', 'researcher', 'write step.txt one', mode='worker', allowed_paths=['step.txt']),
            self.task('second', 'editor', 'write next.txt two', mode='worker', allowed_paths=['next.txt'], depends_on=['first']),
            self.task('review', 'researcher', 'read step.txt next.txt wip.txt', depends_on=['first', 'second'])])
        self.scoped('advance', group)
        self.accept(group, 'first')
        second = self.scoped('advance', group)['results'][0]
        self.assertEqual(second['changed_files'], ['next.txt'])
        self.assertTrue((Path(second['workspace']) / 'step.txt').exists())
        self.accept(group, 'second')
        review = self.scoped('advance', group)['results'][0]
        seen = json.loads(self.scoped('show', group, '--task', 'review')['response'])['seen']
        self.assertEqual(seen, {'step.txt': 'one\n', 'next.txt': 'two\n', 'wip.txt': 'user work in progress\n'})
        self.assertNotEqual(Path(review['workspace']), self.repo)
        self.assertEqual(self.git('status', '--porcelain'), '?? wip.txt')
        self.scoped('integrate', group, '--task', 'first')
        self.scoped('integrate', group, '--task', 'second')
        self.assertEqual((self.repo / 'next.txt').read_text(), 'two\n')

    def test_independent_tasks_run_in_parallel(self):
        group = self.open_group()
        self.plan(group, [self.task('a', 'researcher', 'nap a'), self.task('b', 'editor', 'nap b'),
                          self.task('c', 'researcher', 'nap c')])
        started = time.monotonic()
        wave = self.scoped('advance', group)
        self.assertLess(time.monotonic() - started, 8, 'three 3-second tasks should overlap')
        self.assertEqual(sorted(r['id'] for r in wave['results']), ['a', 'b', 'c'])
        self.assertTrue(all(r['state'] == 'awaiting_review' for r in wave['results']))

    def test_revision_resumes_session_and_checks_gate_acceptance(self):
        group = self.open_group()
        self.plan(group, [self.task('write', 'editor', 'edit', mode='worker', profile='writer', effort='low',
                                    allowed_paths=['calc.py', 'new.txt'],
                                    checks=[{'type': 'contains', 'path': 'new.txt', 'text': '修订完成'}])])
        first = self.scoped('advance', group)['results'][0]
        self.assertEqual(first['state'], 'needs_revision')
        self.assertFalse(first['checks_passed'])
        self.scoped('accept', group, '--task', 'write', '--note', 'no', ok=False)
        self.scoped('revise', group, '--task', 'write', '--feedback', 'revise-edit')
        second = self.scoped('advance', group)['results'][0]
        self.assertEqual((second['state'], second['attempt'], second['checks_passed']), ('awaiting_review', 2, True))
        self.assertEqual(second['workspace'], first['workspace'])
        self.assertTrue(json.loads(self.scoped('show', group, '--task', 'write')['response'])['continued'])
        self.assertEqual((Path(first['result_path']).parent / 'artifacts/new.txt').read_text(encoding='utf-8'), '中文 new file\n')
        self.accept(group, 'write')
        self.scoped('revise', group, '--task', 'write', '--feedback', 'again', ok=False)

    def test_protocol_error_requires_fork_which_starts_fresh_with_guidance(self):
        group = self.open_group()
        self.plan(group, [self.task('fix', 'researcher', 'edit', mode='worker', allowed_paths=['calc.py', 'new.txt'])])
        first = self.scoped('advance', group)['results'][0]
        self.scoped('revise', group, '--task', 'fix', '--feedback', 'session-mismatch')
        failed = self.scoped('advance', group, ok=False)['results'][0]
        self.assertEqual((failed['state'], failed['execution_status']), ('failed', 'protocol_error'))
        self.assertIn('fork', self.scoped('revise', group, '--task', 'fix', '--feedback', 'x', ok=False)['error'])
        self.scoped('fork', group, '--task', 'fix', '--note', 'Only change calc.py this time.')
        fresh = self.scoped('advance', group)['results'][0]
        self.assertEqual(fresh['state'], 'awaiting_review')
        self.assertNotEqual(fresh['workspace'], first['workspace'])
        shown = self.scoped('show', group, '--task', 'fix')
        packet = json.loads(shown['response'])['packet']
        self.assertEqual(packet['previous_attempt']['guidance'], 'Only change calc.py this time.')
        self.assertFalse(json.loads(shown['response'])['continued'])
        self.assertNotEqual(shown['session_id'], runner.read_json(first['result_path'])['session_id'])

    def test_tampered_evidence_cannot_be_accepted_or_handed_off(self):
        group = self.open_group()
        self.plan(group, [self.task('fix', 'researcher', 'edit', mode='worker', allowed_paths=['calc.py', 'new.txt']),
                          self.task('next', 'researcher', 'hello', depends_on=['fix'])])
        first = self.scoped('advance', group)['results'][0]
        artifact = Path(first['result_path']).parent / 'artifacts/new.txt'
        original = artifact.read_bytes()
        artifact.write_text('tampered')
        self.assertIn('snapshot changed', self.scoped('accept', group, '--task', 'fix', '--note', 'x', ok=False)['error'])
        artifact.write_bytes(original)
        extra = Path(first['workspace']) / 'unexpected.txt'
        extra.write_text('parent addition')
        self.assertIn('changed file set', self.scoped('accept', group, '--task', 'fix', '--note', 'x', ok=False)['error'])
        extra.unlink()
        (Path(first['workspace']) / 'new.txt').write_text('parent edit')
        self.assertIn('keep parent edits separate', self.scoped('accept', group, '--task', 'fix', '--note', 'x', ok=False)['error'])
        (Path(first['workspace']) / 'new.txt').write_text('中文 new file\n', encoding='utf-8')
        self.accept(group, 'fix')
        runner.write_json(Path(first['result_path']).parent / 'handoff.json', {'summary': 'altered', 'claims': [], 'limitations': []})
        result = self.scoped('advance', group, ok=False)['results'][0]
        self.assertIn('handoff', result['error'])

    def test_pause_cancels_running_tasks_and_cancel_targets_one(self):
        group = self.open_group()
        self.plan(group, [self.task('slow', 'researcher', 'slow'), self.task('other', 'editor', 'slow')])
        service = groups.Groups(self.store)
        with ThreadPoolExecutor(max_workers=1) as pool:
            running = pool.submit(service.advance, group['id'])
            deadline = time.monotonic() + 8
            while time.monotonic() < deadline and sum(t['state'] == 'running' for t in self.tasks(group).values()) < 2:
                time.sleep(.05)
            self.scoped('cancel', group, '--task', 'other')
            time.sleep(1)
            self.assertEqual(self.tasks(group)['other']['state'], 'cancelled')
            self.assertEqual(self.tasks(group)['slow']['state'], 'running')
            self.scoped('pause', group)
            running.result(timeout=10)
        self.assertEqual(self.scoped('status', group)['state'], 'paused')
        self.assertEqual({t['state'] for t in self.tasks(group).values()}, {'cancelled'})
        self.scoped('resume', group)
        self.scoped('revise', group, '--task', 'slow', '--feedback', 'finish now')
        self.assertEqual(self.scoped('advance', group)['results'][0]['state'], 'awaiting_review')

    def test_plan_validation_and_attempt_cap(self):
        group = self.open_group(max_task_attempts=1)
        bad = [
            ([self.task('a', 'nobody', 'x')], 'Unknown member'),
            ([self.task('a', 'researcher', 'x', depends_on=['b']), self.task('b', 'researcher', 'x', depends_on=['a'])], 'cycle'),
            ([self.task('a', 'researcher', 'x', depends_on=['missing'])], 'Unknown or self'),
            ([self.task('a', 'researcher', 'x', model='other')], 'Unknown plan task fields'),
            ([self.task('a', 'editor', 'x', mode='researcher')], 'not supported by agy'),
        ]
        for tasks, error in bad:
            with self.subTest(error=error):
                self.assertIn(error, self.scoped('plan', group, '--config', self.file('bad.json', {'tasks': tasks}), ok=False)['error'])
        self.plan(group, [self.task('a', 'researcher', 'error-zero')])
        self.scoped('advance', group, ok=False)
        self.assertIn('already started', self.scoped('plan', group, '--config', self.file('again.json', {
            'tasks': [self.task('a', 'researcher', 'x')]}), ok=False)['error'])
        self.scoped('fork', group, '--task', 'a')
        self.assertIn('max_task_attempts', self.scoped('advance', group, ok=False)['results'][0]['error'])

    def test_detached_advance_runs_in_background_and_wait_collects_it(self):
        group = self.open_group()
        self.plan(group, [self.task('bg', 'researcher', 'nap background')])
        started = self.scoped('advance', group, '--detach')
        self.assertEqual(started['status'], 'started')
        self.assertTrue(Path(started['log']).exists())
        done = self.scoped('wait', group, '--timeout', 30)
        self.assertFalse(done['waiting'])
        self.assertEqual({t['id']: t['state'] for t in done['status']['tasks']}, {'bg': 'awaiting_review'})


if __name__ == '__main__':
    unittest.main()
