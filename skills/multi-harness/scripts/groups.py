"""Persistent, on-demand collaboration groups hosted by the current Codex chat."""
from __future__ import annotations

import argparse
from contextlib import contextmanager
import json
import os
from pathlib import Path
import re
import sqlite3
import sys
import uuid

import harness
import conversation


class GroupSelectionError(ValueError):
    def __init__(self, message, candidates):
        super().__init__(message)
        self.candidates = candidates


def text_value(value, label, limit=20000):
    if not isinstance(value, str) or not value.strip() or '\x00' in value or len(value) > limit:
        raise ValueError(f'{label} must be nonempty text, at most {limit} characters')
    return value.strip()


def validate_team(value):
    if not isinstance(value, dict) or set(value) != {'members'} or not isinstance(value['members'], list):
        raise ValueError('Team requires members')
    if not 1 <= len(value['members']) <= 8:
        raise ValueError('Team requires 1-8 members')
    members, aliases = [], {'codex', 'user'}
    fields = {'id', 'role', 'harness', 'model', 'mode', 'effort', 'timeout_seconds', 'max_budget_usd'}
    for member in value['members']:
        if not isinstance(member, dict) or set(member) - fields:
            raise ValueError('Unknown member fields')
        identity = member.get('id')
        if not isinstance(identity, str) or not re.fullmatch(r'[a-z][a-z0-9_-]{0,39}', identity):
            raise ValueError('Member id must be a short lowercase identifier')
        role = text_value(member.get('role'), 'role', 100)
        names = {identity.casefold(), role.casefold()}
        if names & aliases:
            raise ValueError('Member id/role aliases must be unique and cannot be codex/user')
        aliases.update(names)
        if member.get('mode', 'advisor') not in ('advisor', 'researcher'):
            raise ValueError('Discussion members use advisor/researcher; workers use task plans')
        normalized = harness.validate_task({
            **{k: v for k, v in member.items() if k not in ('id', 'role')},
            'schema_version': 1, 'cwd': str(Path.cwd()), 'objective': 'Validate member configuration',
            'mode': member.get('mode', 'advisor'), 'acceptance': ['Parent checks evidence'],
        })
        members.append({'id': identity, 'role': role, **{k: normalized[k] for k in fields - {'id', 'role'} if k in normalized}})
    return {'members': members}


@contextmanager
def dispatch_lock(path):
    """An OS lock is released on controller death; timestamps/PIDs are not proof."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('a+b') as stream:
        if stream.tell() == 0:
            stream.write(b'0')
            stream.flush()
        stream.seek(0)
        try:
            if os.name == 'nt':
                import msvcrt
                msvcrt.locking(stream.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                import fcntl
                fcntl.flock(stream.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:
            raise ValueError('Group dispatcher is busy; messages may still be queued or paused') from None
        try:
            yield
        finally:
            stream.seek(0)
            if os.name == 'nt':
                msvcrt.locking(stream.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                fcntl.flock(stream.fileno(), fcntl.LOCK_UN)


class Groups:
    """Durable public operations; the host decides when to enqueue and dispatch."""

    def __init__(self, store):
        if os.environ.get(harness.CHILD_MARKER):
            raise ValueError('Child agents cannot control collaboration groups')
        self.store = Path(store).resolve()
        self.store.parent.mkdir(parents=True, exist_ok=True)
        self.artifacts = self.store.parent / (self.store.stem + '-runs')
        with self.connect() as db:
            db.executescript('''
                CREATE TABLE IF NOT EXISTS teams(name TEXT PRIMARY KEY, config TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS groups(
                    id TEXT PRIMARY KEY, name TEXT NOT NULL, cwd TEXT NOT NULL,
                    config TEXT NOT NULL, state TEXT NOT NULL, created_at TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS bindings(
                    context TEXT NOT NULL, cwd TEXT NOT NULL, group_id TEXT NOT NULL,
                    PRIMARY KEY(context, cwd));
                CREATE TABLE IF NOT EXISTS messages(
                    id INTEGER PRIMARY KEY AUTOINCREMENT, group_id TEXT NOT NULL,
                    request_id TEXT NOT NULL, sender TEXT NOT NULL, recipient TEXT NOT NULL,
                    kind TEXT NOT NULL, body TEXT NOT NULL, status TEXT NOT NULL,
                    reference_id INTEGER, provenance TEXT, created_at TEXT NOT NULL,
                    UNIQUE(group_id, request_id));
                CREATE TABLE IF NOT EXISTS turns(
                    id TEXT PRIMARY KEY, group_id TEXT NOT NULL, message_id INTEGER UNIQUE NOT NULL,
                    member TEXT NOT NULL, status TEXT NOT NULL, result_path TEXT NOT NULL,
                    started_at TEXT NOT NULL, finished_at TEXT, error TEXT);
                CREATE TABLE IF NOT EXISTS task_links(
                    group_id TEXT NOT NULL, run_id TEXT NOT NULL, member TEXT NOT NULL,
                    root TEXT NOT NULL, dispatch TEXT NOT NULL, task_sha256 TEXT NOT NULL,
                    PRIMARY KEY(group_id, run_id));
            ''')

    @contextmanager
    def connect(self, write=False):
        db = sqlite3.connect(self.store, timeout=10, isolation_level=None)
        db.row_factory = sqlite3.Row
        try:
            if write:
                db.execute('BEGIN IMMEDIATE')
            yield db
            if write:
                db.commit()
        except BaseException:
            if write:
                db.rollback()
            raise
        finally:
            db.close()

    def save_team(self, name, config):
        name = text_value(name, 'team name', 100)
        config = validate_team(config)
        with self.connect(True) as db:
            db.execute('INSERT OR REPLACE INTO teams VALUES(?, ?)', (name, json.dumps(config, ensure_ascii=False)))
        return {'name': name, **config}

    def list(self, cwd=None):
        workspace = os.path.normcase(str(Path(cwd or Path.cwd()).resolve()))
        with self.connect() as db:
            rows = db.execute('SELECT id,name,cwd,state FROM groups WHERE cwd=? ORDER BY created_at', (workspace,)).fetchall()
            teams = db.execute('SELECT name,config FROM teams ORDER BY name').fetchall()
        return {'groups': [dict(row) for row in rows],
                'teams': [{'name': t['name'], **json.loads(t['config'])} for t in teams]}

    def open(self, config):
        fields = {'name', 'goal', 'strategy', 'cwd', 'team', 'acceptance', 'context', 'max_turns'}
        if not isinstance(config, dict) or set(config) - fields:
            raise ValueError('Unknown group configuration fields')
        config = dict(config)
        for field in ('name', 'goal', 'strategy', 'team'):
            config[field] = text_value(config.get(field), field, 4000 if field in ('goal', 'strategy') else 100)
        cwd = Path(text_value(config.get('cwd'), 'cwd'))
        if not cwd.is_absolute() or not cwd.is_dir():
            raise ValueError('cwd must be an existing absolute directory')
        config['cwd'] = str(cwd.resolve())
        criteria = config.get('acceptance')
        if not isinstance(criteria, list) or not criteria or len(criteria) > 20:
            raise ValueError('Group needs acceptance criteria')
        config['acceptance'] = [text_value(x, 'acceptance', 1000) for x in criteria]
        config['max_turns'] = config.get('max_turns', 12)
        if type(config['max_turns']) is not int or not 1 <= config['max_turns'] <= 100:
            raise ValueError('max_turns must be 1-100')
        context = config.get('context')
        if context is not None:
            text_value(context, 'context', 200)
        group_id = uuid.uuid4().hex[:12]
        with self.connect(True) as db:
            team = db.execute('SELECT config FROM teams WHERE name=?', (config['team'],)).fetchone()
            if not team:
                raise ValueError('Team not configured; save explicit CLI/model assignments first')
            config['members'] = json.loads(team['config'])['members']
            db.execute('INSERT INTO groups VALUES(?,?,?,?,?,?)',
                       (group_id, config['name'], os.path.normcase(config['cwd']), json.dumps(config, ensure_ascii=False), 'active', harness.now()))
            if context:
                db.execute('INSERT OR REPLACE INTO bindings VALUES(?,?,?)', (context, os.path.normcase(config['cwd']), group_id))
        return self.status(group_id)

    def resolve(self, group=None, cwd=None, context=None):
        workspace = os.path.normcase(str(Path(cwd or Path.cwd()).resolve()))
        with self.connect() as db:
            if group:
                rows = db.execute('SELECT id FROM groups WHERE (id=? OR name=?) AND cwd=?', (group, group, workspace)).fetchall()
            elif context:
                rows = db.execute('SELECT group_id AS id FROM bindings WHERE context=? AND cwd=?', (context, workspace)).fetchall()
                if not rows:
                    rows = db.execute('SELECT id FROM groups WHERE cwd=?', (workspace,)).fetchall()
            else:
                rows = db.execute('SELECT id FROM groups WHERE cwd=?', (workspace,)).fetchall()
        if len(rows) != 1:
            with self.connect() as db:
                candidates = db.execute('SELECT id,name,cwd,state FROM groups WHERE cwd=? OR id=? OR name=? ORDER BY created_at',
                                        (workspace, group, group)).fetchall()
            raise GroupSelectionError('Group not found in this project' if not rows else
                                      'Group selection is ambiguous; use an explicit group ID/name',
                                      [dict(row) for row in candidates])
        return rows[0]['id']

    def status(self, group_id):
        with self.connect() as db:
            row = db.execute('SELECT * FROM groups WHERE id=?', (group_id,)).fetchone()
            if not row:
                raise ValueError('Group not found')
            config = json.loads(row['config'])
            queue = {m['id']: 0 for m in config['members']}
            for item in db.execute("SELECT recipient, count(*) AS n FROM messages WHERE group_id=? AND status='queued' GROUP BY recipient", (group_id,)):
                queue[item['recipient']] = item['n']
            turns = [dict(t) for t in db.execute('SELECT * FROM turns WHERE group_id=? ORDER BY started_at', (group_id,))]
            active = next((t for t in turns if t['status'] == 'dispatched'), None)
            if active:
                progress = Path(active['result_path']).parent / 'progress.json'
                active['progress'] = harness.read_json(progress) if progress.exists() else None
                active['note'] = 'Last recorded dispatch; reconcile if the controller has exited. No message-level read receipt.'
            return {**config, 'id': row['id'], 'state': row['state'], 'queue': queue,
                    'turns_used': len(turns), 'turns_remaining': max(0, config['max_turns'] - len(turns)),
                    'active_turn': active, 'recent_turns': turns[-10:], 'tasks': self.task_status(group_id)}

    def send(self, group_id, recipient, body, *, kind='question', request_id=None, reference_id=None):
        group = self.status(group_id)
        target = next((m['id'] for m in group['members'] if recipient.casefold() in (m['id'].casefold(), m['role'].casefold())), None)
        target = 'codex' if recipient == 'codex' else target
        if not target:
            raise ValueError('Unknown recipient; use a configured member id/role or codex')
        if kind not in ('question', 'update', 'decision') or (kind == 'decision' and target != 'codex'):
            raise ValueError('Decisions are recorded by Codex; use question/update for members')
        body = text_value(body, 'message')
        key = text_value(request_id or uuid.uuid4().hex, 'request id', 200)
        if key.startswith('reply:'):
            raise ValueError('reply: request IDs are reserved for actual CLI responses')
        with self.connect(True) as db:
            if reference_id is not None and not db.execute('SELECT 1 FROM messages WHERE group_id=? AND id=?', (group_id, reference_id)).fetchone():
                raise ValueError('Referenced message must belong to the same group')
            prior = db.execute('SELECT * FROM messages WHERE group_id=? AND request_id=?', (group_id, key)).fetchone()
            if prior:
                if (prior['recipient'], prior['body'], prior['kind'], prior['reference_id']) != (target, body, kind, reference_id):
                    raise ValueError('Request id already belongs to a different message')
                return self.message(prior)
            cursor = db.execute('INSERT INTO messages(group_id,request_id,sender,recipient,kind,body,status,reference_id,created_at) VALUES(?,?,?,?,?,?,?,?,?)',
                                (group_id, key, 'codex', target, kind, body, 'recorded' if target == 'codex' else 'queued', reference_id, harness.now()))
            return self.message(db.execute('SELECT * FROM messages WHERE id=?', (cursor.lastrowid,)).fetchone())

    @staticmethod
    def message(row):
        value = dict(row)
        value['provenance'] = json.loads(value['provenance']) if value['provenance'] else None
        return value

    def history(self, group_id, after=0, limit=50):
        if after < 0 or not 1 <= limit <= 200:
            raise ValueError('Use after >= 0 and limit 1-200')
        with self.connect() as db:
            rows = db.execute('SELECT * FROM messages WHERE group_id=? AND id>? ORDER BY id LIMIT ?', (group_id, after, limit)).fetchall()
        return {'messages': [self.message(row) for row in rows], 'next_after': rows[-1]['id'] if rows else after}

    def dispatch(self, group_id, limit=1):
        with dispatch_lock(self.artifacts / group_id / 'dispatcher.lock'):
            return self._dispatch(group_id, limit)

    def _dispatch(self, group_id, limit):
        if type(limit) is not int or not 1 <= limit <= 4:
            raise ValueError('Dispatch limit must be 1-4 turns')
        completed = []
        for _ in range(limit):
            group = self.status(group_id)
            with self.connect(True) as db:
                state = db.execute('SELECT state FROM groups WHERE id=?', (group_id,)).fetchone()['state']
                if state != 'active':
                    raise ValueError(f'Group state is {state}; resolve pending attention or resume a paused group before dispatching')
                if db.execute("SELECT 1 FROM turns WHERE group_id=? AND status='dispatched'", (group_id,)).fetchone():
                    raise ValueError('Group has an active or unreconciled turn; do not duplicate dispatch')
                count = db.execute('SELECT count(*) FROM turns WHERE group_id=?', (group_id,)).fetchone()[0]
                message = db.execute("SELECT * FROM messages WHERE group_id=? AND status='queued' ORDER BY id LIMIT 1", (group_id,)).fetchone()
                if not message:
                    break
                if count >= group['max_turns']:
                    raise ValueError('Group turn budget exhausted; explicitly extend it before continuing')
                member = next(m for m in group['members'] if m['id'] == message['recipient'])
                decision = db.execute("SELECT * FROM messages WHERE group_id=? AND kind='decision' ORDER BY id DESC LIMIT 1", (group_id,)).fetchone()
                reference = db.execute('SELECT * FROM messages WHERE id=? AND group_id=?', (message['reference_id'], group_id)).fetchone()
                discussion = {'group': group['name'], 'message': self.message(message),
                              'current_decision': self.message(decision) if decision else None,
                              'quoted_reference': self.message(reference) if reference else None,
                              'task_status_only': group['tasks']}
                if len(json.dumps(discussion, ensure_ascii=False)) > 50000:
                    raise ValueError('Discussion context too large; provide a curated shorter reference')
                turn_id = uuid.uuid4().hex
                root = self.artifacts / group_id / member['id']
                result_path = root / 'turns' / turn_id / 'result.json'
                db.execute('INSERT INTO turns VALUES(?,?,?,?,?,?,?,?,?)',
                           (turn_id, group_id, message['id'], member['id'], 'dispatched', str(result_path), harness.now(), None, None))
                db.execute("UPDATE messages SET status='dispatched' WHERE id=?", (message['id'],))
            try:
                result = conversation.ask(root, conversation.member_task(group, member), discussion, turn_id,
                                          lambda: self.is_paused(group_id))
                completed.append(self.finish(group_id, turn_id, result))
            except (ValueError, OSError) as exc:
                completed.append(self.finish(group_id, turn_id, None, str(exc)))
            if completed[-1]['status'] != 'replied':
                break
        return {'group_id': group_id, 'turns': completed, 'status': self.status(group_id)}

    def finish(self, group_id, turn_id, result, error=None, outcome=None):
        state = ('replied' if result['status'] == 'completed' else
                 'cancelled' if result['status'] == 'cancelled' else
                 'unknown' if result['status'] in ('protocol_error', 'output_limit', 'timed_out') else 'failed') if result else 'failed'
        state = outcome or state
        if result and result['status'] == 'completed' and result.get('model_verification') == 'different_identifier':
            state, error = 'failed', 'Reported model differs from the explicitly assigned model; inspect original evidence'
        with self.connect(True) as db:
            turn = db.execute('SELECT * FROM turns WHERE id=? AND group_id=?', (turn_id, group_id)).fetchone()
            if turn['status'] != 'dispatched':
                return dict(turn)
            if not error and result:
                details = list(result.get('errors', []))
                if state == 'failed' and result.get('response'):
                    details.append(result['response'][:2000])
                error = '; '.join(details)
            db.execute('UPDATE turns SET status=?,finished_at=?,error=? WHERE id=?', (state, harness.now(), error, turn_id))
            db.execute('UPDATE messages SET status=? WHERE id=?', (state, turn['message_id']))
            if state == 'replied':
                provenance = {key: result.get(key) for key in ('harness', 'requested_model', 'model', 'model_verification', 'session_id', 'result_path', 'base_commit')}
                provenance['result_sha256'] = harness.digest(result)
                db.execute('INSERT INTO messages(group_id,request_id,sender,recipient,kind,body,status,reference_id,provenance,created_at) VALUES(?,?,?,?,?,?,?,?,?,?)',
                           (group_id, 'reply:' + turn_id, turn['member'], 'codex', 'reply', result['response'], 'recorded', turn['message_id'], json.dumps(provenance), harness.now()))
            db.execute("UPDATE groups SET state='paused' WHERE id=? AND state='pausing'", (group_id,))
            if state == 'unknown':
                db.execute("UPDATE groups SET state='needs_attention' WHERE id=?", (group_id,))
            return dict(db.execute('SELECT * FROM turns WHERE id=?', (turn_id,)).fetchone())

    def is_paused(self, group_id):
        with self.connect() as db:
            return db.execute('SELECT state FROM groups WHERE id=?', (group_id,)).fetchone()['state'] != 'active'

    def pause(self, group_id):
        with self.connect(True) as db:
            unknown = db.execute("SELECT 1 FROM turns WHERE group_id=? AND status='unknown'", (group_id,)).fetchone()
            active = db.execute("SELECT 1 FROM turns WHERE group_id=? AND status='dispatched'", (group_id,)).fetchone()
            state = 'needs_attention' if unknown else 'pausing' if active else 'paused'
            db.execute('UPDATE groups SET state=? WHERE id=?', (state, group_id))
        return self.status(group_id)

    def resume(self, group_id, additional_turns=0):
        if type(additional_turns) is not int or not 0 <= additional_turns <= 100:
            raise ValueError('additional_turns must be 0-100')
        with self.connect(True) as db:
            if db.execute("SELECT 1 FROM turns WHERE group_id=? AND status IN ('dispatched','unknown')", (group_id,)).fetchone():
                raise ValueError('An active/unreconciled turn must finish before resume')
            row = db.execute('SELECT config FROM groups WHERE id=?', (group_id,)).fetchone()
            config = json.loads(row['config'])
            if config['max_turns'] + additional_turns > 100:
                raise ValueError('A group is limited to 100 turns; open a new scoped group')
            config['max_turns'] += additional_turns
            db.execute("UPDATE groups SET state='active',config=? WHERE id=?", (json.dumps(config, ensure_ascii=False), group_id))
        return self.status(group_id)

    def reconcile(self, group_id):
        outcomes = []
        with dispatch_lock(self.artifacts / group_id / 'dispatcher.lock'):
            group = self.status(group_id)
            with self.connect() as db:
                turns = [dict(t) for t in db.execute("SELECT * FROM turns WHERE group_id=? AND status='dispatched'", (group_id,))]
            for turn in turns:
                root = self.artifacts / group_id / turn['member']
                member = next(m for m in group['members'] if m['id'] == turn['member'])
                result = conversation.recover_terminal(root, conversation.member_task(group, member), turn['id'])
                if result is None:
                    outcomes.append(self.finish(group_id, turn['id'], None,
                                    'Controller exited without terminal evidence. Check any remaining CLI process; do not resend. Open a new group only after investigation.', outcome='unknown'))
                    continue
                outcomes.append(self.finish(group_id, turn['id'], result))
        return {'turns': outcomes, 'status': self.status(group_id)}

    def link_task(self, group_id, member_id, result_path):
        group = self.status(group_id)
        member = next((m for m in group['members'] if m['id'] == member_id), None)
        result = harness.read_json(result_path)
        if not member or not result.get('dispatch') or result.get('discussion_only'):
            raise ValueError('Link a planned execution task to a configured member')
        root, _ = harness.current_run(result_path, result)
        plan, assignment = harness.load_assignment(root / 'plan.json', result['dispatch']['task_id'])
        harness.check_result(plan, assignment, {**result, 'status': 'completed'})
        if (Path(result['source_cwd']).resolve() != Path(group['cwd']).resolve() or
                (member['harness'], member['model']) != (result['harness'], result['requested_model'])):
            raise ValueError('Task workspace/CLI/model must match the group member')
        with self.connect(True) as db:
            db.execute('INSERT OR REPLACE INTO task_links VALUES(?,?,?,?,?,?)',
                       (group_id, result['run_id'], member_id, str(root), json.dumps(result['dispatch']), result['task_sha256']))
        return {'tasks': self.task_status(group_id)}

    def task_status(self, group_id):
        with self.connect() as db:
            links = db.execute('SELECT * FROM task_links WHERE group_id=? ORDER BY run_id', (group_id,)).fetchall()
        statuses = []
        for link in links:
            item = {'run_id': link['run_id'], 'member': link['member'], 'root': link['root']}
            try:
                root = Path(link['root'])
                state = harness.read_json(root / 'run.json')
                result_path = Path(state['latest_result']).resolve()
                if not result_path.is_relative_to(root.resolve()):
                    raise ValueError('Result escaped its task root')
                if (state['run_id'] != link['run_id'] or state['dispatch'] != json.loads(link['dispatch']) or
                        state['task_sha256'] != link['task_sha256']):
                    raise ValueError('Linked task identity changed')
                if state['status'] == 'running':
                    item.update(status='running', execution_status='running', task_id=state['dispatch']['task_id'],
                                requested_model=state['requested_model'], result_path=str(result_path))
                    statuses.append(item)
                    continue
                result = harness.read_json(result_path)
                if result['dispatch'] != json.loads(link['dispatch']) or result['task_sha256'] != link['task_sha256']:
                    raise ValueError('Linked task identity changed')
                if state['status'] == 'accepted':
                    accepted = harness.read_json(result_path.parent / 'acceptance.json')
                    if accepted['status'] != 'accepted' or accepted['result_sha256'] != harness.digest(result):
                        raise ValueError('Task acceptance no longer matches the result')
                item.update(status=state['status'], execution_status=result['status'], task_id=result['dispatch']['task_id'],
                            requested_model=result['requested_model'], model=result.get('model'), result_path=str(result_path))
            except (ValueError, OSError, KeyError, TypeError) as exc:
                item.update(status='evidence_changed', error=str(exc))
            statuses.append(item)
        return statuses


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    default = Path(os.environ.get('LOCALAPPDATA', Path.home() / '.local/share')) / 'muran-skill/groups.sqlite3'
    parser.add_argument('--store', type=Path, default=default)
    subs = parser.add_subparsers(dest='command', required=True)
    team = subs.add_parser('team', help='Save an explicit reusable team without calling models')
    team.add_argument('--name', required=True)
    team.add_argument('--config', type=Path, required=True)
    opening = subs.add_parser('open', help='Open a group from a complete plan/configuration')
    opening.add_argument('--config', type=Path, required=True)
    for name in ('status', 'history', 'send', 'dispatch', 'pause', 'resume', 'reconcile', 'link', 'list'):
        action = subs.add_parser(name)
        action.add_argument('--group')
        action.add_argument('--cwd', type=Path)
        action.add_argument('--context')
        if name == 'history':
            action.add_argument('--after', type=int, default=0)
            action.add_argument('--limit', type=int, default=50)
        if name == 'dispatch':
            action.add_argument('--limit', type=int, default=1)
        if name == 'resume':
            action.add_argument('--additional-turns', type=int, default=0)
        if name == 'link':
            action.add_argument('--member', required=True)
            action.add_argument('--result', type=Path, required=True)
        if name == 'send':
            action.add_argument('--to', required=True)
            action.add_argument('--text-file', type=Path, required=True)
            action.add_argument('--kind', default='question', choices=['question', 'update', 'decision'])
            action.add_argument('--request-id')
            action.add_argument('--reference', type=int)
    args = parser.parse_args(argv)
    try:
        if os.environ.get(harness.CHILD_MARKER):
            raise ValueError('Child agents cannot control collaboration groups')
        service = Groups(args.store)
        if args.command == 'team':
            result = service.save_team(args.name, harness.read_json(args.config))
        elif args.command == 'open':
            result = service.open(harness.read_json(args.config))
        elif args.command == 'list':
            result = service.list(args.cwd)
        else:
            group = service.resolve(args.group, args.cwd, args.context)
            if args.command == 'history':
                result = service.history(group, args.after, args.limit)
            elif args.command == 'send':
                result = service.send(group, args.to, args.text_file.read_text(encoding='utf-8-sig'), kind=args.kind,
                                      request_id=args.request_id, reference_id=args.reference)
            elif args.command == 'dispatch':
                result = service.dispatch(group, args.limit)
            elif args.command == 'pause':
                result = service.pause(group)
            elif args.command == 'resume':
                result = service.resume(group, args.additional_turns)
            elif args.command == 'reconcile':
                result = service.reconcile(group)
            elif args.command == 'link':
                result = service.link_task(group, args.member, args.result)
            else:
                result = service.status(group)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 1 if args.command == 'dispatch' and any(t['status'] != 'replied' for t in result['turns']) else 0
    except GroupSelectionError as exc:
        print(json.dumps({'status': 'rejected', 'error': str(exc), 'candidates': exc.candidates}, ensure_ascii=False))
        return 1
    except (ValueError, OSError, sqlite3.Error, KeyError, TypeError) as exc:
        print(json.dumps({'status': 'rejected', 'error': str(exc)}, ensure_ascii=False))
        return 1


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    raise SystemExit(main())
