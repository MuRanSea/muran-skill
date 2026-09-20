#!/usr/bin/env python3
"""Compatibility accessors for Volcengine zones configured in providers.json."""

import json
import os
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
ROOT = Path(os.environ.get('MURAN_VOLC_WORK_ROOT', str(SKILL_ROOT / '.cache' / 'work')))
DOC = ROOT / "doc"
BUILD = ROOT / "build"
SKILL = ROOT / "generated"

REGISTRY = json.loads((SKILL_ROOT / 'providers.json').read_text(encoding='utf-8'))
VOLCENGINE = next(p for p in REGISTRY['providers'] if p['key'] == 'volcengine')
if VOLCENGINE['type'] != 'volcengine-pdf':
    raise ValueError('Volcengine requires the volcengine-pdf adapter')
PRODUCTS = VOLCENGINE['products']
LIBRARY_IDS = VOLCENGINE['library_ids']


def md_path(p):
    return DOC / f"{p['source']}.md"


def pdf_path(p):
    """The newest doc/<source>_<timestamp>.pdf - exports are timestamp-suffixed."""
    pdfs = sorted(DOC.glob(f"{p['source']}_*.pdf"))
    return pdfs[-1] if pdfs else None
