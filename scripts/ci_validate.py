"""Select CI checks from Git changes and validate the published document snapshot."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import subprocess

from validation import documentation_status

ROOT = Path(__file__).resolve().parents[1]
GENERATED = 'skills/ai-platform-docs/generated/'


def select_checks(root, event_name, event):
    full = {'full_tests': True, 'reason': 'Change range unavailable; run the full suite'}
    if not isinstance(event, dict):
        return full
    if event_name == 'push':
        base, separator = event.get('before'), '..'
    elif event_name == 'pull_request':
        try:
            base = event['pull_request']['base']['sha']
        except (KeyError, TypeError):
            return full
        separator = '...'
    else:
        return full
    if not isinstance(base, str) or not re.fullmatch(r'[0-9a-fA-F]{40}', base) or set(base) == {'0'}:
        return full
    try:
        # Keep both paths of a rename so moving code into generated/ cannot skip tests.
        result = subprocess.run(['git', 'diff', '--name-only', '--no-renames', '-z',
                                 f'{base}{separator}HEAD', '--'], cwd=root,
                                capture_output=True, check=True, timeout=30)
        paths = [name for name in result.stdout.decode('utf-8').split('\0') if name]
    except (OSError, subprocess.SubprocessError, UnicodeError):
        return full
    docs_only = bool(paths) and all(name.startswith(GENERATED) and
                                   (name.endswith('.md') or name == GENERATED + 'snapshot.json')
                                   for name in paths)
    return {'full_tests': not docs_only, 'changed_files': len(paths),
            'reason': 'Only generated documentation changed' if docs_only else
                      'Changes are not limited to generated documentation; run the full suite'}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('command', choices=('select', 'documents'))
    args = parser.parse_args(argv)
    if args.command == 'documents':
        result = documentation_status(args.root)
        print(json.dumps(result, ensure_ascii=False))
        return 0 if result['ready'] else 1
    try:
        event = json.loads(Path(os.environ['GITHUB_EVENT_PATH']).read_text(encoding='utf-8'))
    except (KeyError, OSError, ValueError):
        event = None
    result = select_checks(args.root, os.environ.get('GITHUB_EVENT_NAME'), event)
    output = os.environ.get('GITHUB_OUTPUT')
    if output:
        with Path(output).open('a', encoding='utf-8') as stream:
            stream.write('full_tests=' + str(result['full_tests']).lower() + '\n')
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
