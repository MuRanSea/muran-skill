"""Read-only validation shared by installation, doctor and candidate updates."""
from __future__ import annotations

import ast
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml
from skill_packages import catalog

NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def validate(root: Path) -> tuple[list[dict], list[str]]:
    skills, errors = [], []
    skills_root = root / "skills"
    if not skills_root.is_dir():
        return [], ["Missing skills directory"]
    try:
        packs = catalog(root)
    except (ValueError, OSError, KeyError, TypeError) as exc:
        return [], [str(exc)]
    for package, folder in [(name, folder) for name, pack in packs.items() for folder in pack['folders']]:
        file = folder / "SKILL.md"
        try:
            if folder.is_symlink() or folder.is_junction():
                raise ValueError("Source skill must be an ordinary directory")
            text = file.read_text(encoding="utf-8-sig")
            frontmatter = re.match(r'\A---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|$)', text, flags=re.S)
            if frontmatter is None:
                raise ValueError("SKILL.md must start with YAML frontmatter")
            meta = yaml.safe_load(frontmatter.group(1))
            if not isinstance(meta, dict):
                raise ValueError("Invalid frontmatter")
            name, description = meta.get('name'), meta.get('description')
            if not isinstance(name, str) or not NAME.fullmatch(name) or len(name) > 64 or name != folder.name:
                raise ValueError("Invalid name or name differs from directory")
            if not isinstance(description, str) or not 1 <= len(description.strip()) <= 1024:
                raise ValueError("description must contain 1-1024 characters")
            dependencies = set()
            for line in text[frontmatter.end():].splitlines():
                if 'Skill tool' in line:
                    dependencies.update(re.findall(r'"([a-z][a-z0-9-]+)"', line))
            skills.append({'name': name, 'path': str(folder), 'package': package, 'dependencies': sorted(dependencies)})
            if name == 'ai-platform-docs':
                config = json.loads((folder / 'providers.json').read_text(encoding='utf-8'))
                keys = [p['key'] for p in config['providers']]
                if not keys or len(keys) != len(set(keys)) or not all(NAME.fullmatch(k) for k in keys):
                    raise ValueError('Invalid document provider registry')
                zone_keys = []
                for provider in config['providers']:
                    if provider['type'] == 'volcengine-pdf':
                        if provider['key'] != 'volcengine' or not provider['library_ids'] or not all(type(i) is int and i > 0 for i in provider['library_ids']):
                            raise ValueError('Invalid Volcengine library IDs')
                        if not provider['products']:
                            raise ValueError('Missing Volcengine products')
                        for product in provider['products']:
                            if not all(isinstance(product[f], str) and product[f].strip() for f in ('key', 'label', 'source', 'doc_title', 'blurb')):
                                raise ValueError('Invalid Volcengine product')
                            if any(c in product['source'] for c in '/\\:') or product['source'] in ('.', '..'):
                                raise ValueError('Unsafe Volcengine source filename')
                            zone_keys.append(product['key'])
                    elif provider['type'] == 'markdown':
                        zone_keys.append(provider['key'])
                    else:
                        raise ValueError('Unsupported document provider type')
                if len(zone_keys) != len(set(zone_keys)) or not all(NAME.fullmatch(k) for k in zone_keys):
                    raise ValueError('Invalid or duplicate document zones')
            policy_file = folder / 'agents' / 'openai.yaml'
            if meta.get('disable-model-invocation') is True:
                if not policy_file.is_file() or yaml.safe_load(policy_file.read_text(encoding='utf-8')).get('policy', {}).get('allow_implicit_invocation') is not False:
                    errors.append(f'{name}: missing equivalent explicit-invocation policy for Codex')
            for resource in folder.rglob('*'):
                rel = resource.relative_to(folder)
                if any(p in ('generated', '.cache', '__pycache__') for p in rel.parts):
                    continue
                if resource.is_symlink() or resource.is_junction():
                    errors.append(f'{name}: source resource is a link: {rel}')
                if not resource.is_file() or resource.suffix != '.md':
                    continue
                body = re.sub(r'```.*?```', '', resource.read_text(encoding='utf-8-sig'), flags=re.S)
                for target in re.findall(r'(?<!!)\[[^\]\n]*\]\(([^)\n]+)\)', body):
                    target = target.strip().strip('<>')
                    if urlsplit(target).scheme or target.startswith('#') or any(p in target for p in ('{{', '${', '<')):
                        continue
                    path = unquote(target.split('#', 1)[0])
                    if not path:
                        continue
                    destination = (resource.parent / path).resolve()
                    if name == 'ai-platform-docs' and destination.is_relative_to(folder.resolve() / 'generated'):
                        continue
                    if not destination.is_relative_to(root.resolve()):
                        errors.append(f'{name}: resource escapes repository: {target}')
                    elif not destination.exists():
                        errors.append(f'{name}/{rel}: missing resource {target}')
        except (OSError, ValueError, KeyError, TypeError, AttributeError, yaml.YAMLError) as exc:
            errors.append(f'{folder.name}: {exc}')
    names = {s['name'] for s in skills}
    if len(names) != len(skills):
        errors.append('Skill names must be unique across packages')
    if not names:
        errors.append('No valid skills found')
    for skill in skills:
        for dependency in skill['dependencies']:
            if dependency not in names:
                errors.append(f"{skill['name']}: missing skill dependency {dependency}")
    for source in list((root / 'scripts').glob('*.py')) + list((skills_root / 'ai-platform-docs' / 'scripts').glob('*.py')):
        try:
            ast.parse(source.read_text(encoding='utf-8'), filename=str(source))
        except (SyntaxError, UnicodeError) as exc:
            errors.append(f'{source.relative_to(root)}: {exc}')
    return skills, errors


def documentation_status(root: Path) -> dict:
    folder = root / 'skills' / 'ai-platform-docs' / 'generated'
    try:
        manifest = json.loads((folder / 'snapshot.json').read_text(encoding='utf-8'))
        files = manifest['files']
        if not isinstance(files, dict) or not files or 'INDEX.md' not in files:
            raise ValueError('Incomplete document manifest')
        actual = {p.relative_to(folder).as_posix() for p in folder.rglob('*') if p.is_file() and p.name != 'snapshot.json'}
        if set(files) != actual:
            raise ValueError('Document files differ from manifest')
        for name, expected in files.items():
            path = (folder / name).resolve()
            if not path.is_relative_to(folder.resolve()) or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
                raise ValueError(f'Document missing or modified: {name}')
        config_path = folder.parent / 'providers.json'
        sources = manifest.get('sources', {})
        if config_path.exists():
            for provider in json.loads(config_path.read_text(encoding='utf-8'))['providers']:
                key = provider['key']
                if provider['type'] == 'volcengine-pdf':
                    zones = provider['products']
                    if sources.get(key, {}).get('zones') != len(zones):
                        raise ValueError(f'Missing or incomplete documentation provider: {key}')
                    for zone in zones:
                        zone_key = zone['key']
                        prefix = f'chapters/volcengine/{zone_key}/' if manifest.get('layout_version', 1) >= 2 else f'chapters/{zone_key}/'
                        if f'INDEX-{zone_key}.md' not in files or not any(name.startswith(prefix) for name in files):
                            raise ValueError(f'Missing documentation zone: {key}/{zone_key}')
                    continue
                pages = sum(name.startswith(f'chapters/{key}/') for name in files)
                if not pages or sources.get(key, {}).get('pages') != pages or f'INDEX-{key}.md' not in files:
                    raise ValueError(f'Missing or incomplete documentation provider: {key}')
        return {'ready': True, 'files': len(files), 'built_at': manifest['built_at'], 'origin': manifest['origin'], 'sources': sources}
    except (OSError, KeyError, ValueError, TypeError) as exc:
        return {'ready': False, 'reason': str(exc), 'command': '.\\muran.ps1 docs build --fetch'}


def forbidden_public_paths(paths: list[str]) -> list[str]:
    """Names only: never read or report credential contents."""
    bad = []
    for path in paths:
        parts = Path(path).parts
        base = Path(path).name.lower()
        if (any(p in ('.cache', '.venv', '__pycache__') for p in parts)
                or path.startswith('skills/volcengine-docs/generated/')
                or base.endswith(('.pdf', '.zip', '.pyc'))
                or base == '.env' or (base.startswith('.env.') and base != '.env.example')):
            bad.append(path)
    return bad
