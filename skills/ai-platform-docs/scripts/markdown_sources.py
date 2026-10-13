"""Cache official page sources as Markdown without executing document content."""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import gzip
import io
import json
from pathlib import Path
import re
import time
import urllib.error
import urllib.parse
import urllib.request

CONFIG = Path(__file__).resolve().parent.parent / 'providers.json'
MAX_BYTES = 16 * 1024 * 1024


def providers():
    return [p for p in json.loads(CONFIG.read_text(encoding='utf-8'))['providers']
            if p['type'] in ('markdown', 'tencent-cloud')]


def allowed_url(url, provider):
    parts = urllib.parse.urlsplit(url)
    if parts.scheme != 'https' or parts.hostname not in provider['hosts'] or parts.username or parts.password:
        raise ValueError(f"Unexpected document URL for {provider['key']}: {url}")
    return url


def fetch_text(url, provider, *, data=None):
    class OfficialRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, req, fp, code, msg, headers, newurl):
            allowed_url(newurl, provider)
            return super().redirect_request(req, fp, code, msg, headers, newurl)

    opener = urllib.request.build_opener(OfficialRedirect())
    for attempt in range(3):
        try:
            headers = {'User-Agent': 'muran-skill/0.1 documentation-sync'}
            if data is not None:
                headers['Content-Type'] = 'application/json'
                headers['Referer'] = provider['index_url']
                origin = urllib.parse.urlsplit(provider['index_url'])
                headers['Origin'] = f'{origin.scheme}://{origin.netloc}'
            req = urllib.request.Request(allowed_url(url, provider), headers=headers,
                                         data=json.dumps(data).encode() if data is not None else None)
            with opener.open(req, timeout=30) as response:
                raw = response.read(MAX_BYTES + 1)
            if len(raw) > MAX_BYTES:
                raise ValueError(f'Document too large: {url}')
            if raw.startswith(b'\x1f\x8b'):
                with gzip.GzipFile(fileobj=io.BytesIO(raw)) as compressed:
                    raw = compressed.read(MAX_BYTES + 1)
                if len(raw) > MAX_BYTES:
                    raise ValueError(f'Document too large: {url}')
            text = raw.decode('utf-8-sig').replace('\r\n', '\n')
            if re.search(r'<(?:!doctype\s+html|html)[\s>]', text[:1000], re.I) or (data is None and len(text.strip()) < 80):
                raise ValueError(f'Expected a complete Markdown document: {url}')
            return text
        except (urllib.error.URLError, TimeoutError, OSError):
            if attempt == 2:
                raise
            time.sleep(attempt + 1)


def catalog(text, provider):
    pages = {}
    for title, url in re.findall(r'^\s*-\s+\[([^\]\n]+)\]\((https://[^\s)]+)\)', text, re.M):
        parts = urllib.parse.urlsplit(url)
        if not parts.path.endswith('.md') or not any(parts.path.startswith(p) for p in provider['include_paths']):
            continue
        allowed_url(url, provider)
        if provider.get('canonical_host'):
            url = urllib.parse.urlunsplit(parts._replace(netloc=provider['canonical_host']))
        pages[parts.path] = {'title': title, 'url': url}
    if not pages or not set(provider['required_paths']).issubset(pages):
        raise ValueError(f"Incomplete official catalog: {provider['key']}")
    return [pages[key] for key in sorted(pages)]


def page_filename(url):
    path = urllib.parse.urlsplit(url).path.removesuffix('.md')
    slug = re.sub(r'[^a-zA-Z0-9-]+', '-', path).strip('-')[-100:]
    return slug + '-' + hashlib.sha256(url.encode()).hexdigest()[:10] + '.md'


def fetch_provider(provider, cache):
    def fetch_tencent(action, payload):
        # Public read endpoints used by Tencent's document viewer.
        endpoint = urllib.parse.urljoin(provider['index_url'], '/document/cgi/document/' + action)
        return fetch_text(endpoint, provider, data={'action': action, 'payload': payload})

    tencent = provider.get('type') == 'tencent-cloud'
    if tencent:
        from tencent_sources import catalog as tencent_catalog, extract_article
        index = fetch_tencent('getDocProductMenuByDocType', {
            'categoryId': str(provider['product_id']), 'lang': 'zh', 'isPreview': False})
        pages = tencent_catalog(index, provider)
    else:
        index = fetch_text(provider['index_url'], provider)
        pages = catalog(index, provider)
    folder = cache / provider['key']
    folder.mkdir(parents=True, exist_ok=True)

    def download(page):
        try:
            if tencent:
                response = fetch_tencent('getDocPageDetail', {
                    'id': urllib.parse.urlsplit(page['url']).path.rsplit('/', 1)[-1],
                    'lang': 'zh', 'isPreview': False, 'isFromClient': True})
                body = extract_article(response, page['url'], provider, fetch_glossary=lambda: fetch_tencent(
                    'getGlossary', {'catId': str(provider['product_id']), 'isPreview': False}))
            else:
                body = fetch_text(page['url'], provider)
        except Exception as exc:
            raise ValueError(f"Failed official page {page['url']}: {exc}") from exc
        finally:
            if tencent:
                time.sleep(0.5)
        filename = page_filename(page['url'])
        (folder / filename).write_text(body, encoding='utf-8', newline='\n')
        return {**page, 'file': filename, 'sha256': hashlib.sha256(body.encode()).hexdigest()}

    with ThreadPoolExecutor(max_workers=1 if tencent else 4) as pool:
        rows = []
        for row in pool.map(download, pages):
            rows.append(row)
            if tencent and len(rows) % 25 == 0:
                print(f"{provider['key']}: fetched {len(rows)}/{len(pages)} pages", flush=True)
    metadata = {'key': provider['key'], 'label': provider['label'], 'region': provider['region'],
                'index_url': provider['index_url'], 'checked_at': datetime.now(timezone.utc).isoformat(), 'pages': rows}
    if tencent:
        metadata['format'] = 'official-document-api-to-markdown'
    (folder / 'manifest.json').write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    # The catalog is authoritative for removals. Only cached Markdown files are removed.
    desired = {row['file'] for row in rows}
    for file in folder.glob('*.md'):
        if file.name not in desired:
            file.unlink()
    print(f"{provider['key']}: fetched {len(rows)} official pages", flush=True)
    return metadata


def load_provider(provider, cache):
    folder = cache / provider['key']
    if not (folder / 'manifest.json').is_file():
        raise ValueError(f"Missing cached documentation for {provider['key']}; run docs update")
    metadata = json.loads((folder / 'manifest.json').read_text(encoding='utf-8'))
    rows = metadata['pages']
    if not rows or not set(provider['required_paths']).issubset({urllib.parse.urlsplit(r['url']).path for r in rows}):
        raise ValueError(f"Incomplete cached catalog: {provider['key']}; run docs update")
    for row in rows:
        allowed_url(row['url'], provider)
        file = (folder / row['file']).resolve()
        if file.parent != folder.resolve() or hashlib.sha256(file.read_bytes()).hexdigest() != row['sha256']:
            raise ValueError(f"Missing or modified source: {provider['key']}/{row['file']}")
    return metadata


def fingerprint_rows(metadata):
    return [{key: row[key] for key in ('url', 'title', 'sha256')} for row in metadata['pages']]


def build_provider(provider, cache, generated):
    metadata = load_provider(provider, cache)
    destination = generated / 'chapters' / provider['key']
    destination.mkdir(parents=True, exist_ok=True)
    index = [f"# {provider['label']}", '', f"官方目录：{provider['index_url']}",
             f"地区：{provider['region']}", '', '| 文档 | 本地文件 | 官方来源 |', '|---|---|---|']
    for row in metadata['pages']:
        source = cache / provider['key'] / row['file']
        body = source.read_text(encoding='utf-8')
        header = f"<!-- Official source: {row['url']} -->\n<!-- Source SHA-256: {row['sha256']} -->\n\n"
        target = destination / row['file']
        target.write_text(header + body, encoding='utf-8')
        if target.read_text(encoding='utf-8')[len(header):] != body:
            raise ValueError(f'Markdown content changed during build: {target.name}')
        title = row['title'].replace('|', '\\|')
        index.append(f"| {title} | `chapters/{provider['key']}/{row['file']}` | {row['url']} |")
    (generated / f"INDEX-{provider['key']}.md").write_text('\n'.join(index) + '\n', encoding='utf-8')
    return {key: value for key, value in metadata.items() if key != 'pages'} | {'pages': len(metadata['pages'])}
