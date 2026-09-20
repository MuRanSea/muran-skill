"""Read-only validation shared by installation, doctor and candidate updates."""
from __future__ import annotations

import ast
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml

NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def validate(root: Path) -> tuple[list[dict], list[str]]:
    skills, errors = [], []
    skills_root = root / "skills"
    if not skills_root.is_dir():
        return [], ["Missing skills directory"]
    for folder in sorted(skills_root.iterdir()):
        if folder.name.startswith('.') or not folder.is_dir():
            continue
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
            skills.append({'name': name, 'path': str(folder), 'dependencies': sorted(dependencies)})
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
                    if name == 'volcengine-docs' and destination.is_relative_to(folder.resolve() / 'generated'):
                        continue
                    if not destination.is_relative_to(root.resolve()):
                        errors.append(f'{name}: resource escapes repository: {target}')
                    elif not destination.exists():
                        errors.append(f'{name}/{rel}: missing resource {target}')
        except (OSError, ValueError, TypeError, AttributeError, yaml.YAMLError) as exc:
            errors.append(f'{folder.name}: {exc}')
    names = {s['name'] for s in skills}
    if not names:
        errors.append('No valid skills found')
    for skill in skills:
        for dependency in skill['dependencies']:
            if dependency not in names:
                errors.append(f"{skill['name']}: missing skill dependency {dependency}")
    for source in list((root / 'scripts').glob('*.py')) + list((skills_root / 'volcengine-docs' / 'scripts').glob('*.py')):
        try:
            ast.parse(source.read_text(encoding='utf-8'), filename=str(source))
        except (SyntaxError, UnicodeError) as exc:
            errors.append(f'{source.relative_to(root)}: {exc}')
    return skills, errors


def documentation_status(root: Path) -> dict:
    folder = root / 'skills' / 'volcengine-docs' / 'generated'
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
        return {'ready': True, 'files': len(files), 'built_at': manifest['built_at'], 'origin': manifest['origin']}
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
