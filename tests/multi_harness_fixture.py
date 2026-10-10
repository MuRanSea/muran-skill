"""Shared fixture for multi-harness tests: a real Git repository and a scripted fake CLI.

The fake CLI speaks both the Claude and Antigravity stream protocols, keeps its own
session memory on disk and acts on the first word of the message it receives.
It is selected through the documented MURAN_HARNESS_<NAME>_LAUNCHER override, so
controller subprocesses use it too. These are executor tests, not model acceptance.
"""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / 'skills/multi-harness/scripts'
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import adapters  # noqa: E402

FAKE = r'''
import json, os, pathlib, signal, subprocess, sys, time, uuid
if '--version' in sys.argv:
    print('fixture 1.0'); raise SystemExit()
if '--help' in sys.argv:
    print('--output-format --tools --allowedTools --safe-mode --strict-mcp-config --disable-slash-commands '
          '--permission-mode --permission-prompts --resume --conversation --effort --max-budget-usd --mode '
          '--input-format --print-timeout --model')
    raise SystemExit()
agy = '--input-format' in sys.argv
raw = sys.stdin.read()
if agy:
    raw = json.loads(raw)['message']['content']
packet = json.loads(raw.split('\n\n', 1)[1])
os.chdir(packet['project_root'])
if 'feedback' in packet:
    body = packet['feedback']
elif 'discussion' in packet:
    body = packet['discussion']['message']['body']
else:
    body = packet['objective']
words = body.split()
command = words[0] if words else ''
flag = '--conversation' if agy else '--resume'
resumed = flag in sys.argv
session = sys.argv[sys.argv.index(flag) + 1] if resumed else 'fixture-' + uuid.uuid4().hex
statefile = pathlib.Path(os.environ['FAKE_STATE']) / (session + '.json')
memory = json.loads(statefile.read_text()) if resumed else {'first': body}
if not resumed:
    statefile.write_text(json.dumps(memory))
model = sys.argv[sys.argv.index('--model') + 1]
if command == 'slow-init':
    time.sleep(2)
if agy:
    print(json.dumps({'event': 'init', 'conversation_id': session, 'init': {'model': model, 'tools': ['view_file']}}), flush=True)
else:
    print(json.dumps({'type': 'system', 'subtype': 'init', 'session_id': session}), flush=True)
if command in ('slow', 'slow-init'):
    time.sleep(8)
if command == 'nap':
    time.sleep(3)
if command == 'kill-controller':
    os.kill(int(os.environ['MURAN_HARNESS_CONTROLLER_PID']), signal.SIGTERM)
    raise SystemExit()
if command == 'timeout-child':
    marker = str(pathlib.Path(words[1]) / 'orphan.txt')
    subprocess.Popen([sys.executable, '-c', 'import pathlib,time; time.sleep(3); pathlib.Path(' + repr(marker) + ').write_text("orphan")'])
    time.sleep(30)
if command == 'malformed':
    print('not json'); raise SystemExit()
if command == 'large':
    print('x' * 8192); raise SystemExit()
if command == 'auth-error':
    print(json.dumps({'type': 'assistant', 'message': {'model': '<synthetic>', 'content': []}}))
    print(json.dumps({'type': 'result', 'session_id': session, 'subtype': 'success', 'is_error': True,
                      'result': 'Failed to authenticate: OAuth session expired and could not be refreshed', 'errors': []}))
    raise SystemExit(1)
if command in ('edit', 'violate', 'ignored'):
    pathlib.Path('calc.py').write_text('def add(a, b):\n    return a + b\n')
    pathlib.Path('new.txt').write_text('中文 new file\n', encoding='utf-8')
if command == 'violate':
    pathlib.Path('outside.txt').write_text('unexpected')
if command == 'ignored':
    pathlib.Path('ignored.bin').write_bytes(bytes(range(256)))
if command == 'write':
    pathlib.Path(words[1]).write_text(' '.join(words[2:]) + '\n', encoding='utf-8')
if command == 'revise-edit':
    pathlib.Path('new.txt').write_text('修订完成\n', encoding='utf-8')
if command == 'session-mismatch':
    session = 'different-session'
if command == 'wrong-model':
    model = 'unplanned-model'
seen = {}
if command == 'read':
    for name in words[1:]:
        path = pathlib.Path(name)
        seen[name] = path.read_text(encoding='utf-8') if path.exists() else None
tool = words[1] if command == 'tool' else ('WebFetch' if command == 'research-scope' else ('view_file' if agy else 'Read'))
if command == 'research-scope':
    available = sys.argv[sys.argv.index('--tools') + 1].split(',')
    assert 'WebSearch' in available and 'WebFetch' in available
    assert not set(available) & {'Write', 'Edit', 'Bash', 'Agent'}
error = command == 'error-zero'
answer = json.dumps({'body': body, 'first': memory['first'], 'continued': resumed, 'seen': seen, 'packet': packet},
                    ensure_ascii=False) if not error else 'fixture failure'
if command == 'echo':
    answer = body[5:]
if agy:
    for state in ('ACTIVE', 'DONE'):
        print(json.dumps({'event': 'step_update', 'step_update': {'step_type': 'tool', 'step_index': 2, 'state': state, 'tool_name': tool}}))
    if command != 'truncate':
        print(json.dumps({'event': 'result', 'conversation_id': session, 'result': {
            'status': 'ERROR' if error else 'SUCCESS', 'response': answer, 'error': 'fixture error' if error else '',
            'usage': {'input_tokens': 3, 'output_tokens': 4}}}))
else:
    print(json.dumps({'type': 'assistant', 'message': {'model': model, 'content': [{'type': 'tool_use', 'name': tool, 'id': 'x', 'input': {}}]}}))
    if command != 'truncate':
        print(json.dumps({'type': 'result', 'session_id': session, 'subtype': 'error_during_execution' if error else 'success',
                          'is_error': error, 'result': answer, 'usage': {'input_tokens': 3, 'output_tokens': 4},
                          'total_cost_usd': 0.01, 'errors': ['fixture error'] if error else []}))
'''

IDENTITY = ['-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.invalid', '-c', 'commit.gpgsign=false']


class Fixture(unittest.TestCase):
    def setUp(self):
        parent = ROOT / '.cache/tests'
        parent.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(prefix='mh-', dir=parent)
        self.base = Path(self.temporary.name).resolve()
        self.repo = self.base / 'project 中文 with spaces'
        self.repo.mkdir()
        self.fake = self.base / 'fake cli.py'
        self.fake.write_text(FAKE, encoding='utf-8')
        sessions = self.base / 'fake-sessions'
        sessions.mkdir()
        self.sessions = sessions
        launcher = json.dumps([sys.executable, str(self.fake)])
        self.env = patch.dict(os.environ, {'PYTHONUTF8': '1', 'FAKE_STATE': str(sessions),
                                           'MURAN_HARNESS_CLAUDE_LAUNCHER': launcher,
                                           'MURAN_HARNESS_AGY_LAUNCHER': launcher})
        self.env.start()
        adapters._cached_probe.cache_clear()
        (self.repo / 'calc.py').write_text('def add(a, b):\n    return a - b\n')
        (self.repo / '.gitignore').write_text('.cache/\nignored.bin\n')
        self.git('init', '-q')
        self.commit('fixture')

    def tearDown(self):
        self.env.stop()
        self.assertTrue(self.base.is_relative_to((ROOT / '.cache/tests').resolve()))
        self.temporary.cleanup()

    def git(self, *args):
        return subprocess.run(['git', '-c', 'core.hooksPath=' + str(self.base / 'no-hooks'), *args], cwd=self.repo,
                              check=True, capture_output=True, text=True, encoding='utf-8').stdout.strip()

    def commit(self, message):
        self.git('add', '-A')
        self.git(*IDENTITY, 'commit', '-q', '--allow-empty', '-m', message)

    def sessions_started(self):
        return len(list(self.sessions.iterdir()))
