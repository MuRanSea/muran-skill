"""Git baselines and isolated worktrees.

A baseline is a snapshot commit of the user's working tree (HEAD plus uncommitted
and untracked, non-ignored files). It is built with a temporary index, so the
user's branch, index and files are never touched.
"""
from __future__ import annotations

import hashlib
import os
from pathlib import Path, PurePosixPath
import shutil
import subprocess
import tempfile

from adapters import process_options

IDENTITY = {'GIT_AUTHOR_NAME': 'multi-harness', 'GIT_AUTHOR_EMAIL': 'multi-harness@localhost',
            'GIT_COMMITTER_NAME': 'multi-harness', 'GIT_COMMITTER_EMAIL': 'multi-harness@localhost'}


def command(args, cwd, accepted=(0,), env=None):
    result = subprocess.run(args, cwd=cwd, stdin=subprocess.DEVNULL, capture_output=True, timeout=120,
                            env=env, **process_options())
    if result.returncode not in accepted:
        # Never inline Git diagnostics wholesale: keep the first line for context only.
        detail = result.stderr.decode('utf-8', errors='replace').strip().splitlines()[:1]
        raise ValueError(f'{Path(args[0]).name} {args[1] if len(args) > 1 else ""} exited {result.returncode}'
                         + (f': {detail[0]}' if detail else ''))
    return result.stdout


def git(cwd, *args, env=None, accepted=(0,)):
    return command(['git', '-c', 'core.quotepath=false', *args], cwd, accepted, env).decode('utf-8').strip()


def relative_file(value):
    if not isinstance(value, str) or not value or '\\' in value:
        raise ValueError('File paths must be nonempty relative paths using /')
    path = PurePosixPath(value)
    if (path.is_absolute() or any(part in ('..', '.git') for part in path.parts)
            or any(char in value for char in ':*?\x00\r\n') or path.as_posix() != value
            or value == '.' or value.endswith('/') or value.startswith('-')):
        raise ValueError(f'Unsafe or non-exact file path: {value!r}')
    return value


def repository_root(cwd):
    cwd = Path(cwd).resolve()
    try:
        top = Path(git(cwd, 'rev-parse', '--show-toplevel')).resolve()
    except ValueError:
        raise ValueError('Isolated runs require cwd to be a Git repository') from None
    if top != cwd:
        raise ValueError('Isolated runs require cwd to be the Git repository root')
    return cwd


def snapshot(cwd):
    """Commit the current working tree state without changing the user's repository."""
    cwd = repository_root(cwd)
    head = git(cwd, 'rev-parse', '--verify', '-q', 'HEAD', accepted=(0, 1)) or None
    with tempfile.TemporaryDirectory(prefix='mh-index-') as folder:
        index = Path(folder) / 'index'
        real = Path(git(cwd, 'rev-parse', '--git-path', 'index'))
        real = real if real.is_absolute() else cwd / real
        if real.exists():
            shutil.copyfile(real, index)  # Reuse the stat cache; contents are rebuilt below.
        env = {**os.environ, 'GIT_INDEX_FILE': str(index), **IDENTITY}
        if head:
            git(cwd, 'read-tree', head, env=env)
        else:
            git(cwd, 'read-tree', '--empty', env=env)
        git(cwd, 'add', '-A', '--', '.', env=env)
        tree = git(cwd, 'write-tree', env=env)
        if head and tree == git(cwd, 'rev-parse', head + '^{tree}'):
            base = head
        else:
            base = git(cwd, 'commit-tree', tree, *(['-p', head] if head else []),
                       '-m', 'multi-harness working tree snapshot', env=env)
    entries = command(['git', 'ls-tree', '-r', '-z', base], cwd).split(b'\0')
    if any(entry.startswith((b'120000 ', b'160000 ')) for entry in entries):
        raise ValueError('Isolated runs do not support symlinks or submodules in their baseline')
    return base


def add_worktree(cwd, path, base, hooks):
    Path(hooks).mkdir(parents=True, exist_ok=True)
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    git(Path(cwd), '-c', f'core.hooksPath={hooks}', 'worktree', 'add', '--detach', str(path), base)


def checkout(workspace, base, hooks):
    """Move a clean member worktree to a newer baseline; the session path stays the same."""
    files, _ = changed_names(workspace, current_head(workspace))
    if files:
        raise ValueError('Member worktree has changes; investigate before syncing the baseline')
    git(Path(workspace), '-c', f'core.hooksPath={hooks}', 'checkout', '-q', '--detach', base)


def current_head(workspace):
    return git(Path(workspace), 'rev-parse', 'HEAD')


def apply_patches(workspace, patches, hooks):
    """Apply accepted dependency patches and commit them as the new base.

    A patch that is already present (the user integrated it) is skipped.
    Returns (base, applied, skipped).
    """
    workspace = Path(workspace)
    applied, skipped = [], []
    for name, patch in patches:
        patch = str(Path(patch).resolve())
        if not Path(patch).read_bytes().strip():
            skipped.append(name)
            continue
        if _applies(workspace, patch):
            git(workspace, 'apply', '--index', '--binary', patch)
            applied.append(name)
        elif _applies(workspace, patch, reverse=True):
            skipped.append(name)
        else:
            raise ValueError(f'Accepted changes from {name} conflict with the current baseline; integrate them manually')
    if applied:
        env = {**os.environ, **IDENTITY}
        git(workspace, '-c', 'commit.gpgsign=false', '-c', f'core.hooksPath={hooks}', 'commit', '-q',
            '--no-verify', '-m', 'multi-harness accepted dependencies: ' + ', '.join(applied), env=env)
    return current_head(workspace), applied, skipped


def _applies(workspace, patch, reverse=False):
    args = ['git', 'apply', '--check', '--binary', *(['--reverse'] if reverse else []), patch]
    return subprocess.run(args, cwd=workspace, stdin=subprocess.DEVNULL, capture_output=True,
                          timeout=120, **process_options()).returncode == 0


def integrate(cwd, patch):
    """Apply an accepted patch to the user's working tree (not the index)."""
    cwd = repository_root(cwd)
    patch = str(Path(patch).resolve())
    if not Path(patch).read_bytes().strip():
        return 'empty'
    if _applies(cwd, patch):
        git(cwd, 'apply', '--binary', patch)
        return 'applied'
    if _applies(cwd, patch, reverse=True):
        return 'already_present'
    raise ValueError('Patch does not apply to the current working tree; resolve the conflict manually')


def changed_names(workspace, base):
    workspace = Path(workspace)
    if current_head(workspace) != base:
        raise ValueError('Agent changed HEAD; inspect the preserved worktree')
    tracked = command(['git', 'diff', '--no-renames', '--name-only', '-z', base], workspace)
    # Include ignored new files, too: scope checks must not hide generated changes.
    untracked = command(['git', 'ls-files', '--others', '-z'], workspace)
    new_files = [name.decode('utf-8') for name in untracked.split(b'\0') if name]
    files = sorted({name.decode('utf-8') for name in tracked.split(b'\0') if name} | set(new_files))
    for name in files:
        relative_file(name)
        path = workspace / name
        if not path.resolve().is_relative_to(workspace.resolve()) or path.is_symlink() or path.is_junction():
            raise ValueError('Agent created a linked or escaping path; inspect the preserved worktree')
    return files, new_files


def collect_changes(workspace, folder, base, allowed_paths):
    """Write changes.patch (tracked, new and binary files) and return (files, violations)."""
    workspace = Path(workspace)
    files, new_files = changed_names(workspace, base)
    with (Path(folder) / 'changes.patch').open('wb') as patch:
        patch.write(command(['git', 'diff', '--no-ext-diff', '--no-textconv', '--no-renames', '--binary', base], workspace))
        for name in new_files:
            patch.write(command(['git', 'diff', '--no-ext-diff', '--no-textconv', '--no-index', '--binary',
                                 '--', '/dev/null', name], workspace, accepted=(0, 1)))
    return files, sorted(set(files) - set(allowed_paths))


def file_hashes(workspace, names):
    workspace = Path(workspace).resolve()
    hashes = {}
    for name in names:
        path = workspace / relative_file(name)
        if not path.resolve().is_relative_to(workspace):
            raise ValueError('Changed file escapes workspace')
        hashes[name] = hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else None
    return hashes
