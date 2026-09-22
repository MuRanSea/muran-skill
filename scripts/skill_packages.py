"""Discover independently maintained skill packs without executing their code."""
import json
from pathlib import Path
import re

NAME = re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')


def catalog(root):
    parent = Path(root) / 'skills'
    if not parent.is_dir():
        raise ValueError('Missing skills directory')
    result = {}
    for folder in sorted(parent.iterdir()):
        if folder.name.startswith('.') or not folder.is_dir():
            continue
        if folder.is_symlink() or folder.is_junction():
            raise ValueError('Source package must be an ordinary directory')
        manifest = folder / 'pack.json'
        if manifest.exists():
            spec = json.loads(manifest.read_text(encoding='utf-8'))
            if spec.get('schema_version') != 1 or spec.get('name') != folder.name or not NAME.fullmatch(folder.name):
                raise ValueError(f'Invalid package manifest: {folder.name}')
            if spec.get('updater', 'git') not in ('git', 'matt', 'documents'):
                raise ValueError(f'Unsupported package updater: {folder.name}')
            owner = {'matt': 'matt', 'documents': 'ai-platform-docs'}.get(spec.get('updater'))
            if owner and folder.name != owner:
                raise ValueError(f'Updater {spec["updater"]} belongs to package {owner}')
            if spec.get('skills') == ['.']:
                folders = [folder]
            elif spec.get('skills') == ['*']:
                folders = [p for p in sorted(folder.iterdir()) if p.is_dir() and not p.name.startswith('.')]
            else:
                raise ValueError(f'Package skills must be ["."] or ["*"]: {folder.name}')
            if not folders:
                raise ValueError(f'Empty package: {folder.name}')
            explicit = True
        else:
            # Compatibility with old installations and isolated manager fixtures.
            folders = [folder]
            spec = {'name': folder.name, 'description': folder.name, 'updater': 'git'}
            explicit = False
        result[folder.name] = {**spec, 'path': str(folder), 'folders': folders, 'explicit': explicit}
    return result


def selected_packages(root, state):
    packs = catalog(root)
    if 'packages' in state:
        selected = [name for name in state['packages'] if name in packs]
        legacy = set(state['packages']) - packs.keys()
        return selected + [name for name, pack in packs.items() if name not in selected and any(folder.name in legacy for folder in pack['folders'])]
    installed = {record['name'] for record in state.get('links', [])}
    return [name for name, pack in packs.items() if any(folder.name in installed for folder in pack['folders'])]
