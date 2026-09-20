"""Build in isolation, validate, then publish a complete local document snapshot."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

from products import PRODUCTS, SKILL_ROOT

SCRIPTS = Path(__file__).resolve().parent
CACHE = SKILL_ROOT / '.cache'
LIVE = SKILL_ROOT / 'generated'


def run(script, *args, work):
    env = {**os.environ, 'MURAN_VOLC_WORK_ROOT': str(work), 'PYTHONUTF8': '1', 'PYTHONDONTWRITEBYTECODE': '1'}
    subprocess.run([sys.executable, '-B', '-X', 'utf8', str(SCRIPTS / script), *map(str, args)], env=env, check=True)


def write_snapshot(folder, origin):
    files = {p.relative_to(folder).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
             for p in sorted(folder.rglob('*')) if p.is_file() and p.name != 'snapshot.json'}
    if 'INDEX.md' not in files or not any(name.startswith('chapters/') for name in files):
        raise ValueError('Incomplete generated documentation')
    metadata = {'schema_version': 1, 'built_at': datetime.now(timezone.utc).isoformat(), 'origin': origin, 'files': files}
    (folder / 'snapshot.json').write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def publish_generated(candidate, destination, backup):
    """Rollback the previous snapshot if the final rename fails."""
    if backup.exists():
        raise ValueError('Backup path already exists')
    had_previous = destination.exists()
    if had_previous:
        os.replace(destination, backup)
    try:
        os.replace(candidate, destination)
    except BaseException:
        if had_previous:
            os.replace(backup, destination)
        raise
    if had_previous:
        shutil.rmtree(backup)


def import_snapshot(source, work):
    source = source.resolve()
    original = source / 'skills' / 'volcengine-docs'
    if not original.is_dir():
        raise ValueError('Expected original volcengine_doc_skill repository directory')
    shutil.copytree(original / 'chapters', work / 'generated' / 'chapters')
    for index in original.glob('INDEX*.md'):
        shutil.copy2(index, work / 'generated' / index.name)
    for product in PRODUCTS:
        shutil.copy2(source / 'build' / (product['key'] + '.json'), work / 'build' / (product['key'] + '.json'))
        shutil.copy2(source / 'doc' / (product['source'] + '.md'), work / 'doc' / (product['source'] + '.md'))


def verify_pdf_extraction(pdf, md):
    import pypdfium2 as pdfium
    chinese = re.compile(r'[一-鿿]')
    with pdfium.PdfDocument(str(pdf)) as doc:
        samples = range(0, len(doc), max(1, len(doc) // 100))
        found = sum(len(chinese.findall(doc[i].get_textpage().get_text_range())) for i in samples)
        estimate = found * len(doc) / len(samples)
    ratio = len(chinese.findall(md.read_text(encoding='utf-8'))) / estimate if estimate else 0
    if ratio < 0.8:
        raise ValueError(f'Extraction lost text for {pdf.name}: {ratio:.1%}')


def build(args):
    CACHE.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='build-', dir=CACHE) as temporary:
        work = Path(temporary).resolve()
        if not work.is_relative_to(CACHE.resolve()):
            raise ValueError('Build workspace escaped cache')
        previous = CACHE / 'work'
        for directory in ('doc', 'build'):
            (work / directory).mkdir()
            if previous.exists() and not args.import_from:
                shutil.copytree(previous / directory, work / directory, dirs_exist_ok=True)
        (work / 'generated').mkdir()
        if args.import_from:
            import_snapshot(args.import_from, work)
            run('check_build.py', work=work)
            origin = 'Imported local document snapshot; source text coverage validated'
        else:
            if args.only and LIVE.exists():
                shutil.copytree(LIVE, work / 'generated', dirs_exist_ok=True)
            if args.fetch:
                run('fetch_docs.py', '--clean-old', work=work)
            for product in PRODUCTS:
                if args.only and product['key'] != args.only:
                    continue
                md = work / 'doc' / (product['source'] + '.md')
                if args.fetch or args.convert:
                    pdfs = sorted((work / 'doc').glob(product['source'] + '_*.pdf'))
                    if not pdfs:
                        raise ValueError(f"No PDF for {product['key']}; use --fetch")
                    run('pdf_to_md.py', '--pdf', pdfs[-1], '--out', md, work=work)
                    verify_pdf_extraction(pdfs[-1], md)
                if not md.is_file():
                    raise ValueError('No cached source text; use --fetch or --import-from')
                run('build_volc_doc_skill.py', '--md', md, '--product', product['key'],
                    '--out-dir', work / 'generated' / 'chapters' / product['key'],
                    '--manifest', work / 'build' / (product['key'] + '.json'), '--oversize', args.oversize, work=work)
            run('gen_index.py', work=work)
            run('check_build.py', work=work)
            origin = 'Official Volcengine PDFs' if args.fetch else 'Rebuilt from cached document sources'
        write_snapshot(work / 'generated', origin)
        # Prepare both source caches before publishing. A failed publish rolls
        # the cache back together with the generated snapshot.
        next_work = work / 'next-work'
        next_work.mkdir()
        for directory in ('doc', 'build'):
            os.replace(work / directory, next_work / directory)
        backup_work = work / 'previous-work'
        had_work = previous.exists()
        if had_work:
            if previous.is_junction() or previous.is_symlink() or not previous.resolve().is_relative_to(CACHE.resolve()):
                raise ValueError('Unexpected cache target')
            os.replace(previous, backup_work)
        try:
            os.replace(next_work, previous)
            publish_generated(work / 'generated', LIVE, work / 'previous-generated')
        except BaseException:
            if previous.exists():
                shutil.rmtree(previous)
            if had_work:
                os.replace(backup_work, previous)
            raise
    print('Document snapshot ready: ' + str(LIVE))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--import-from', type=Path)
    parser.add_argument('--fetch', action='store_true')
    parser.add_argument('--convert', action='store_true')
    parser.add_argument('--only', choices=[p['key'] for p in PRODUCTS])
    parser.add_argument('--oversize', type=int, default=1500)
    args = parser.parse_args()
    if args.import_from and (args.fetch or args.convert or args.only):
        parser.error('--import-from cannot be combined with rebuild options')
    CACHE.mkdir(parents=True, exist_ok=True)
    import msvcrt
    with (CACHE / 'build.lock').open('a+b') as lock:
        if lock.tell() == 0:
            lock.write(b'0')
            lock.flush()
        lock.seek(0)
        try:
            msvcrt.locking(lock.fileno(), msvcrt.LK_NBLCK, 1)
        except OSError:
            parser.exit(1, 'Another document build is running\n')
        try:
            build(args)
        finally:
            lock.seek(0)
            msvcrt.locking(lock.fileno(), msvcrt.LK_UNLCK, 1)


if __name__ == '__main__':
    main()
