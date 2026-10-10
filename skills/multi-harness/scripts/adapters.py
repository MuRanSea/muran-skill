"""CLI adapters: everything that differs between supported local CLIs lives here.

Adding a CLI means adding one Adapter subclass and registering it in ADAPTERS.
"""
from __future__ import annotations

from functools import lru_cache
import json
import os
from pathlib import Path
import re
import shutil
import subprocess

SESSION = re.compile(r'[a-zA-Z0-9_-]{1,200}')


def process_options():
    return {'creationflags': subprocess.CREATE_NO_WINDOW} if os.name == 'nt' else {}


def resolve_launcher(name):
    """Resolve Windows npm shims without passing task data through cmd.exe.

    MURAN_HARNESS_<NAME>_LAUNCHER may hold a JSON argv prefix for installs outside PATH.
    """
    override = os.environ.get(f'MURAN_HARNESS_{name.upper()}_LAUNCHER')
    if override:
        launcher = json.loads(override)
        if not isinstance(launcher, list) or not launcher or any(not isinstance(x, str) or not x for x in launcher):
            raise ValueError('Launcher override must be a JSON list of strings')
        return launcher
    found = shutil.which(name)
    if not found:
        raise ValueError(f'{name} is not on PATH')
    path = Path(found).resolve()
    if os.name != 'nt' or path.suffix.lower() == '.exe':
        return [str(path)]
    if path.suffix.lower() not in ('.cmd', '.bat', '.ps1'):
        raise ValueError(f'Unsupported launcher: {path}')
    # Standard npm shims contain a literal relative JS or EXE entrypoint.
    shim = path.read_text(encoding='utf-8-sig')
    matches = re.findall(r'"(?:%dp0%|\$basedir)[\\/]([^"\r\n]+\.(?:exe|[cm]?js))"', shim)
    targets = [(path.parent / match.replace('\\', '/')).resolve() for match in matches]
    targets = [target for target in targets if 'node_modules' in target.parts and target.is_file()]
    if not targets or any(target != targets[0] for target in targets):
        raise ValueError(f'Unsupported npm shim: {path}; install a standard native/npm CLI')
    if targets[0].suffix.lower() == '.exe':
        return [str(targets[0])]
    node = path.parent / 'node.exe'
    runtime = str(node) if node.is_file() else shutil.which('node')
    if not runtime:
        raise ValueError('Node.js is required for this CLI')
    return [runtime, str(targets[0])]


class Adapter:
    name = ''
    required_flags: tuple[str, ...] = ()
    tool_control = ''
    efforts: tuple[str, ...] = ()
    modes: tuple[str, ...] = ('advisor', 'worker')
    has_budget = False

    def isolated(self, mode):
        """Whether this mode must run in a separate worktree."""
        return mode == 'worker'

    def validate(self, task):
        """Harness-specific task rules; the generic shape is checked by runner.validate_task."""
        if task['mode'] not in self.modes:
            raise ValueError(f'{task["mode"]} mode is not supported by {self.name}')
        if 'effort' in task and task['effort'] not in self.efforts:
            raise ValueError('Unsupported effort for the selected harness')
        if self.has_budget:
            budget = task.get('max_budget_usd', 1)
            if type(budget) not in (int, float) or budget != budget or not 0 < budget < float('inf'):
                raise ValueError('max_budget_usd must be positive')
            task['max_budget_usd'] = budget
        elif 'max_budget_usd' in task:
            raise ValueError(f'{self.name} has no supported per-run USD limit')

    def args(self, task, session_id=None):
        raise NotImplementedError

    def encode(self, prompt):
        return prompt.encode('utf-8')

    def summarize(self, event):
        """A small progress envelope: never copy prompts, tool inputs or model reasoning."""
        raise NotImplementedError

    def read(self, event, acc):
        raise NotImplementedError

    def finish(self, acc):
        raise NotImplementedError

    def audit(self, observed_tools, mode):
        """Tools that were used but fall outside the mode; only for audit-controlled CLIs."""
        return []

    def parse(self, path):
        acc = {'status': 'protocol_error', 'response': '', 'model': None, 'usage': None,
               'cost_usd': None, 'tool_calls': 0, 'errors': [], 'session_id': None,
               'tools': set(), 'steps': set(), 'terminal': None}
        try:
            with Path(path).open(encoding='utf-8-sig') as stream:
                for line in stream:
                    if not line.strip():
                        continue
                    event = json.loads(line)
                    if not isinstance(event, dict):
                        raise ValueError('Event is not an object')
                    session = self.summarize(event).get('session_id')
                    if session:
                        if not isinstance(session, str) or not SESSION.fullmatch(session):
                            raise ValueError('Invalid session identifier')
                        if acc['session_id'] and acc['session_id'] != session:
                            raise ValueError('Session identifier changed within one attempt')
                        acc['session_id'] = session
                    self.read(event, acc)
            if acc['terminal'] is not None:
                self.finish(acc)
            if not isinstance(acc['response'], str) or not isinstance(acc['errors'], list):
                raise ValueError('Invalid response/error shape')
            if acc['status'] == 'protocol_error':
                acc['errors'] = ['Missing recognized final response / terminal event']
        except (ValueError, UnicodeError, KeyError, TypeError, AttributeError):
            acc['status'] = 'protocol_error'
            acc['errors'] = ['Malformed or unsupported CLI event stream; inspect stdout.jsonl']
        acc['observed_tools'] = sorted(acc.pop('tools'))
        for key in ('steps', 'terminal'):
            acc.pop(key)
        return acc

    def probe(self):
        return _probe(self.name, self.required_flags)


@lru_cache(maxsize=None)
def _cached_probe(name, required, launcher):
    launcher = list(launcher)
    options = {'stdin': subprocess.DEVNULL, 'capture_output': True, 'timeout': 30, **process_options()}
    version = subprocess.run([*launcher, '--version'], **options)
    if version.returncode != 0:
        raise ValueError(f'{name} --version exited {version.returncode}')
    help_result = subprocess.run([*launcher, '--help'], **options)
    if help_result.returncode != 0:
        raise ValueError(f'{name} --help failed')
    text = (help_result.stdout + help_result.stderr).decode('utf-8', errors='replace')
    missing = [flag for flag in required if flag not in text]
    if missing:
        raise ValueError(f'{name} lacks required flags: {", ".join(missing)}')
    return {'harness': name, 'version': version.stdout.decode('utf-8', errors='replace').strip(),
            'launcher': launcher, 'available': True}


def _probe(name, required):
    # Cached per launcher within one controller process; parallel tasks reuse one probe.
    return dict(_cached_probe(name, tuple(required), tuple(resolve_launcher(name))))


class Claude(Adapter):
    name = 'claude'
    required_flags = ('--output-format', '--tools', '--allowedTools', '--safe-mode',
                      '--strict-mcp-config', '--disable-slash-commands', '--permission-mode',
                      '--permission-prompts', '--resume', '--max-budget-usd', '--model', '--effort')
    tool_control = 'cli_allowlist'
    efforts = ('low', 'medium', 'high', 'xhigh', 'max')
    modes = ('advisor', 'researcher', 'worker')
    has_budget = True

    @staticmethod
    def tools(mode):
        tools = ['Read', 'Glob', 'Grep']
        if mode == 'worker':
            tools += ['Edit', 'Write']
        if mode == 'researcher':
            tools += ['WebSearch', 'WebFetch']
        return tools

    def args(self, task, session_id=None):
        tools = ','.join(self.tools(task['mode']))
        args = ['-p', '--output-format', 'stream-json', '--verbose', '--safe-mode',
                '--strict-mcp-config', '--disable-slash-commands',
                '--tools', tools, '--allowedTools', tools,
                '--permission-mode', 'acceptEdits' if task['mode'] == 'worker' else 'dontAsk',
                '--permission-prompts', 'none', '--max-budget-usd', str(task['max_budget_usd']),
                '--model', task['model']]
        if 'effort' in task:
            args += ['--effort', task['effort']]
        if session_id:
            args += ['--resume', session_id]
        return args

    def summarize(self, event):
        kind = event.get('type', 'unknown')
        summary = {'kind': kind}
        if event.get('subtype'):
            summary['subtype'] = event['subtype']
        if kind == 'assistant':
            summary['tools'] = [item.get('name') for item in event.get('message', {}).get('content', [])
                                if item.get('type') == 'tool_use']
        if event.get('session_id'):
            summary['session_id'] = event['session_id']
        return summary

    def read(self, event, acc):
        kind = event.get('type')
        if kind == 'assistant':
            message = event.get('message', {})
            acc['model'] = message.get('model', acc['model'])
            uses = [item for item in message.get('content', []) if item.get('type') == 'tool_use']
            acc['tool_calls'] += len(uses)
            acc['tools'].update(item.get('name', 'unknown') for item in uses)
        elif kind == 'result':
            acc['terminal'] = event

    def finish(self, acc):
        terminal = acc['terminal']
        acc['response'] = terminal.get('result', '')
        acc['usage'] = terminal.get('usage')
        acc['cost_usd'] = terminal.get('total_cost_usd')
        acc['errors'] = terminal.get('errors', [])
        success = terminal.get('subtype') == 'success' and terminal.get('is_error') is False
        acc['status'] = 'completed' if success and acc['response'] else 'failed'
        if acc['status'] == 'failed' and acc['response']:
            # Claude reports auth and quota failures in the result text.
            acc['errors'] = [*acc['errors'], acc['response'][:2000]]


class Antigravity(Adapter):
    name = 'agy'
    required_flags = ('--mode', '--input-format', '--output-format',
                      '--disable-slash-commands', '--print-timeout', '--model', '--conversation', '--effort')
    tool_control = 'prompt_and_audit'
    efforts = ('low', 'medium', 'high')
    modes = ('advisor', 'worker')
    read_tools = ('view_file', 'grep_search', 'find_by_name', 'list_dir', 'finish')
    write_tools = ('replace_file_content', 'multi_replace_file_content', 'write_to_file')

    def isolated(self, mode):
        # Native permissions are not narrowed, so every mode runs in a worktree.
        return True

    def validate(self, task):
        super().validate(task)
        tier = re.search(r'-(low|medium|high)$', task['model'])
        if tier and task.get('effort', tier[1]) != tier[1]:
            raise ValueError('Antigravity model tier conflicts with effort; choose a matching explicit model')

    def allowed_tools(self, mode):
        return [*self.read_tools, *(self.write_tools if mode == 'worker' else ())]

    def args(self, task, session_id=None):
        args = ['--input-format', 'stream-json', '--output-format', 'stream-json',
                '--disable-slash-commands', '--print-timeout', '0']
        if task['mode'] == 'worker':
            args += ['--mode', 'accept-edits']
        args += ['--model', task['model']]
        if 'effort' in task:
            args += ['--effort', task['effort']]
        if session_id:
            args += ['--conversation', session_id]
        return args

    def encode(self, prompt):
        event = {'event': 'user', 'message': {'content': prompt}}
        return (json.dumps(event, ensure_ascii=False) + '\n').encode('utf-8')

    def summarize(self, event):
        kind = event.get('event', 'unknown')
        summary = {'kind': kind}
        session = event.get('conversation_id')
        payload = event.get(kind, {})
        if isinstance(payload, dict):
            session = session or payload.get('conversation_id')
            if kind == 'step_update':
                summary.update(step_index=payload.get('step_index'), state=payload.get('state'),
                               tool=payload.get('tool_name') or payload.get('tool_info', {}).get('name'))
            if kind == 'result':
                summary['state'] = payload.get('status')
        if session:
            summary['session_id'] = session
        return summary

    def read(self, event, acc):
        kind = event.get('event')
        if kind == 'init':
            acc['model'] = event['init'].get('model')
            acc['available_tools'] = event['init'].get('tools')
        elif kind == 'step_update':
            step = event['step_update']
            if step.get('step_type') == 'tool':
                acc['steps'].add(step['step_index'])
                acc['tools'].add(step.get('tool_name') or step.get('tool_info', {}).get('name') or 'unknown')
            if step.get('subagent_info'):
                acc['tools'].add('invoke_subagent')
            acc['tool_calls'] = len(acc['steps'])
        elif kind == 'result':
            acc['terminal'] = event['result']

    def finish(self, acc):
        terminal = acc['terminal']
        acc['response'] = terminal.get('response', '')
        acc['usage'] = terminal.get('usage')
        acc['status'] = 'completed' if terminal.get('status') == 'SUCCESS' and acc['response'] else 'failed'
        if acc['status'] != 'completed':
            acc['errors'] = [terminal.get('error') or f'Antigravity status: {terminal.get("status")}']

    def audit(self, observed_tools, mode):
        return sorted(set(observed_tools) - set(self.allowed_tools(mode)))


ADAPTERS = {adapter.name: adapter for adapter in (Claude(), Antigravity())}


def get(name):
    if name not in ADAPTERS:
        raise ValueError('Unsupported harness; choose one of: ' + ', '.join(ADAPTERS))
    return ADAPTERS[name]
