"""Publish only validated generated Markdown and its hash manifest."""
import json

from muran import git, now
from validation import documentation_status

PREFIX = 'skills/ai-platform-docs/generated/'


def prepare(manager):
    root = manager.root
    if git(root, 'symbolic-ref', '--short', 'HEAD').strip() != 'main':
        raise ValueError('Document publication requires main')
    if git(root, 'status', '--porcelain', '--untracked-files=all').strip():
        raise ValueError('Uncommitted changes: document publication skipped; commit or resolve them first')
    state = manager.load_state()
    pending = state.get('last_docs_publish', {}).get('pending_commit')
    if pending:
        if git(root, 'rev-parse', 'HEAD').strip() != pending:
            raise ValueError('Pending document commit differs from HEAD; reconcile before publishing')
        git(root, 'push', 'origin', 'HEAD:refs/heads/main', timeout=120)
        state['last_docs_publish'] = {'time': now(), 'status': 'published', 'commit': pending}
        manager.save(state)
    update = manager.update()
    if not update['ok'] or update['status'] not in ('updated', 'unchanged'):
        raise ValueError('Repository not ready for document publication: ' + update['status'])
    return git(root, 'rev-parse', 'HEAD').strip()


def publish(manager, before):
    root = manager.root
    if (git(root, 'rev-parse', 'HEAD').strip() != before
            or git(root, 'symbolic-ref', '--short', 'HEAD').strip() != 'main'):
        raise ValueError('Repository changed during document rebuild')
    if git(root, 'diff', '--cached', '--name-only').strip():
        raise ValueError('Staged user changes appeared during document rebuild')
    changed = set(filter(None, git(root, 'diff', '--name-only', '-z').split('\0')))
    changed.update(filter(None, git(root, 'ls-files', '--others', '--exclude-standard', '-z').split('\0')))
    if any(not name.startswith(PREFIX) for name in changed):
        raise ValueError('User changes appeared outside generated documentation; publication stopped')
    if not changed:
        return {'status': 'unchanged'}
    docs = documentation_status(root)
    if not docs['ready']:
        raise ValueError('Cannot publish incomplete documentation: ' + docs['reason'])
    manifest = json.loads((root / PREFIX / 'snapshot.json').read_text(encoding='utf-8'))
    if any(not name.endswith('.md') for name in manifest['files']):
        raise ValueError('Only Markdown and snapshot.json may be published')
    git(root, 'add', '-A', '--', PREFIX)
    # Validate exact Git bytes, catching checkout line-ending or missing-file issues.
    tree = git(root, 'write-tree').strip()
    manager.validate_candidate(tree)
    git(root, 'commit', '-m', 'docs: 自动更新火山、可灵和 MiniMax 文档快照')
    commit = git(root, 'rev-parse', 'HEAD').strip()
    state = manager.load_state()
    state['last_docs_publish'] = {'time': now(), 'status': 'pending_push', 'pending_commit': commit}
    manager.save(state)
    git(root, 'push', 'origin', 'HEAD:refs/heads/main', timeout=120)
    result = {'time': now(), 'status': 'published', 'commit': commit, 'files': docs['files']}
    state['last_docs_publish'] = result
    manager.save(state)
    return result
