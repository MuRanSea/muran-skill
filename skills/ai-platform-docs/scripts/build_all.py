# /// script
# requires-python = ">=3.12,<3.13"
# dependencies = ["pypdfium2>=4.30,<6"]
# [tool.uv]
# python-preference = "only-managed"
# ///
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
from markdown_sources import providers, fetch_provider, load_provider, fingerprint_rows, build_provider

SCRIPTS = Path(__file__).resolve().parent
CACHE = SKILL_ROOT / '.cache'
LIVE = SKILL_ROOT / 'generated'


def run(script, *args, work):
    env = {**os.environ, 'MURAN_VOLC_WORK_ROOT': str(work), 'PYTHONUTF8': '1', 'PYTHONDONTWRITEBYTECODE': '1'}
    subprocess.run([sys.executable, '-B', '-X', 'utf8', str(SCRIPTS / script), *map(str, args)], env=env, check=True)


def write_snapshot(folder, origin, source_fingerprint=None, sources=None):
    files = {p.relative_to(folder).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
             for p in sorted(folder.rglob('*')) if p.is_file() and p.name != 'snapshot.json'}
    if 'INDEX.md' not in files or not any(name.startswith('chapters/') for name in files):
        raise ValueError('Incomplete generated documentation')
    metadata = {'schema_version': 1, 'built_at': datetime.now(timezone.utc).isoformat(), 'origin': origin, 'files': files}
    metadata['layout_version'] = 2 if (folder / 'chapters/volcengine').is_dir() else 1
    if source_fingerprint:
        metadata['source_fingerprint'] = source_fingerprint
    if sources:
        metadata['sources'] = sources
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
    shutil.copytree(original / 'chapters', work / 'generated' / 'chapters' / 'volcengine')
    for index in original.glob('INDEX*.md'):
        shutil.copy2(index, work / 'generated' / index.name)
    for product in PRODUCTS:
        shutil.copy2(source / 'build' / (product['key'] + '.json'), work / 'build' / (product['key'] + '.json'))
        shutil.copy2(source / 'doc' / (product['source'] + '.md'), work / 'doc' / (product['source'] + '.md'))
    (work / 'doc/pdf-versions.json').unlink(missing_ok=True)


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


def copy_cache_file(source, destination):
    # PDFs are immutable inputs; a same-volume hardlink avoids copying hundreds
    # of megabytes at each daily check. Mutable text and manifests stay isolated.
    if Path(source).suffix.lower() == '.pdf':
        try:
            os.link(source, destination)
            return destination
        except OSError:
            pass
    return shutil.copy2(source, destination)


def snapshot_matches(fingerprint):
    try:
        manifest = json.loads((LIVE / 'snapshot.json').read_text(encoding='utf-8'))
        if manifest.get('source_fingerprint') != fingerprint:
            return False
        files = manifest['files']
        actual = {p.relative_to(LIVE).as_posix() for p in LIVE.rglob('*') if p.is_file() and p.name != 'snapshot.json'}
        return set(files) == actual and all(
            (LIVE / name).resolve().is_relative_to(LIVE.resolve())
            and hashlib.sha256((LIVE / name).read_bytes()).hexdigest() == digest for name, digest in files.items())
    except (OSError, KeyError, ValueError, TypeError):
        return False


def source_fingerprint(work, catalog, oversize=1500):
    inputs = {p['key']: hashlib.sha256((work / 'doc' / (p['source'] + '.md')).read_bytes()).hexdigest() for p in PRODUCTS}
    inputs.update({p['key']: fingerprint_rows(load_provider(p, work / 'markdown')) for p in catalog})
    inputs['builder'] = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(SCRIPTS.glob('*.py'))}
    inputs['configuration'] = (SKILL_ROOT / 'providers.json').read_text(encoding='utf-8')
    inputs['pdf_versions'] = (work / 'doc/pdf-versions.json').read_text(encoding='utf-8')
    inputs['oversize'] = oversize
    return hashlib.sha256(json.dumps(inputs, sort_keys=True).encode()).hexdigest()


def build(args):
    CACHE.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='build-', dir=CACHE) as temporary:
        work = Path(temporary).resolve()
        if not work.is_relative_to(CACHE.resolve()):
            raise ValueError('Build workspace escaped cache')
        previous = CACHE / 'work'
        for directory in ('doc', 'build', 'markdown'):
            (work / directory).mkdir()
            if (previous / directory).exists():
                shutil.copytree(previous / directory, work / directory, dirs_exist_ok=True, copy_function=copy_cache_file)
        (work / 'generated').mkdir()
        catalog = providers()
        if args.only and not LIVE.exists():
            raise ValueError('--only requires an existing complete snapshot')
        if args.import_from:
            import_snapshot(args.import_from, work)
            run('check_build.py', work=work)
        if args.fetch:
            run('fetch_docs.py', '--clean-old', work=work)
        for provider in catalog:
            if args.fetch or (args.import_from and not (work / 'markdown' / provider['key'] / 'manifest.json').exists()):
                fetch_provider(provider, work / 'markdown')
        versions_file = work / 'doc' / 'pdf-versions.json'
        versions = json.loads(versions_file.read_text(encoding='utf-8')) if versions_file.exists() else {}
        for product in PRODUCTS:
            md = work / 'doc' / (product['source'] + '.md')
            if args.only and product['key'] != args.only:
                continue
            if args.fetch or args.convert:
                pdfs = sorted((work / 'doc').glob(product['source'] + '_*.pdf'))
                if not pdfs:
                    raise ValueError(f"No PDF for {product['key']}; use --fetch")
                pdf = pdfs[-1]
                if args.convert or not md.exists() or versions.get(product['key']) != pdf.name:
                    run('pdf_to_md.py', '--pdf', pdf, '--out', md, work=work)
                    verify_pdf_extraction(pdf, md)
                versions[product['key']] = pdf.name
            if not md.is_file():
                raise ValueError('No cached source text; use --fetch or --import-from')
        versions_file.write_text(json.dumps(versions, ensure_ascii=False, indent=2), encoding='utf-8')
        fingerprint = source_fingerprint(work, catalog, args.oversize)
        if args.if_changed and snapshot_matches(fingerprint):
            return {'status': 'unchanged', 'rebuilt': False}
        if not args.import_from:
            for product in PRODUCTS:
                if args.only and product['key'] != args.only:
                    source = LIVE / 'chapters' / 'volcengine' / product['key']
                    if not source.exists():  # Upgrade a snapshot built before platform grouping.
                        source = LIVE / 'chapters' / product['key']
                    shutil.copytree(source, work / 'generated' / 'chapters' / 'volcengine' / product['key'])
                    continue
                md = work / 'doc' / (product['source'] + '.md')
                run('build_volc_doc_skill.py', '--md', md, '--product', product['key'],
                    '--out-dir', work / 'generated' / 'chapters' / 'volcengine' / product['key'],
                    '--manifest', work / 'build' / (product['key'] + '.json'), '--oversize', args.oversize, work=work)
        run('gen_index.py', work=work)
        run('check_build.py', work=work)
        sources = {'volcengine': {'format': 'official-pdf', 'zones': len(PRODUCTS), 'pdf_versions': versions}}
        for provider in catalog:
            sources[provider['key']] = build_provider(provider, work / 'markdown', work / 'generated')
        index = work / 'generated' / 'INDEX.md'
        lines = ['# AI 平台文档 - 总索引', '', '先选择平台，再在平台索引中选择产品或接口。', '',
                 f"- [火山引擎](INDEX-volcengine.md)：{len(PRODUCTS)} 个产品文档分区。"]
        for provider in catalog:
            lines.append(f"- [{provider['label']}](INDEX-{provider['key']}.md)：{sources[provider['key']]['pages']} 页。")
        index.write_text('\n'.join(lines) + '\n', encoding='utf-8')
        origin = 'Official Volcengine PDF and Kling/MiniMax Markdown exports'
        write_snapshot(work / 'generated', origin, fingerprint, sources)
        # Prepare both source caches before publishing. A failed publish rolls
        # the cache back together with the generated snapshot.
        next_work = work / 'next-work'
        next_work.mkdir()
        for directory in ('doc', 'build', 'markdown'):
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
    return {'status': 'updated', 'rebuilt': True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--import-from', type=Path)
    parser.add_argument('--fetch', action='store_true')
    parser.add_argument('--convert', action='store_true')
    parser.add_argument('--if-changed', action='store_true', help='Keep the current snapshot when all sources and builder inputs are unchanged')
    parser.add_argument('--only', choices=[p['key'] for p in PRODUCTS], help='Rebuild one Volcengine zone while retaining other zones')
    parser.add_argument('--oversize', type=int, default=1500)
    args = parser.parse_args()
    if args.import_from and (args.convert or args.only):
        parser.error('--import-from cannot be combined with --convert or --only')
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
            print(json.dumps(build(args), ensure_ascii=False))
        finally:
            lock.seek(0)
            msvcrt.locking(lock.fileno(), msvcrt.LK_UNLCK, 1)


if __name__ == '__main__':
    main()
