#!/usr/bin/env python3
"""Fetch the latest official PDF documentation from Volcengine Doc Center.

Queries Volcengine's getLibList API to find the newest PDF export URLs for
all configured products in tools/products.py (or any Library ID), compares
timestamps against local doc/ files, and downloads updated PDFs.
"""

import argparse
import json
import re
import ssl
import sys
import time
import urllib.request
from pathlib import Path
from urllib.parse import unquote, urlparse

from products import DOC as DOC_DIR

# Use the platform certificate store; never silently disable TLS verification.
SSL_CTX = ssl.create_default_context()

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept": "application/json, text/plain, */*",
}


def get_lib_list(lib_id: int | str) -> list[dict]:
    """Query Volcengine Doc API for a given Library ID."""
    url = f"https://docs.volcengine.com/api/doc/getLibList?LibraryID={lib_id}&type=online"
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, context=SSL_CTX, timeout=15) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        return data.get("Result", [])


def extract_lib_ids_from_readme(readme_path: Path = DOC_DIR / "readme.md") -> list[int]:
    """Parse doc/readme.md to extract all doc Library IDs."""
    if not readme_path.exists():
        return [6349, 6448, 82379]
    content = readme_path.read_text(encoding="utf-8")
    ids = set()
    for m in re.finditer(r"/docs/(\d+)", content):
        ids.add(int(m.group(1)))
    return sorted(ids)


def get_local_pdf(source_name: str) -> tuple[Path | None, int]:
    """Find the newest local PDF for a given source name and its timestamp."""
    pdfs = sorted(DOC_DIR.glob(f"{source_name}_*.pdf"))
    if not pdfs:
        return None, 0
    latest = pdfs[-1]
    m = re.search(r"_(\d+)\.pdf$", latest.name)
    ts = int(m.group(1)) if m else 0
    return latest, ts


def discover_available_pdfs(lib_ids: list[int]) -> list[dict]:
    """Discover all PDF exports available in the given Library IDs."""
    results = []
    for lib_id in lib_ids:
        libs = get_lib_list(lib_id)
        for lib in libs:
            lib_name = lib.get("Name", "").strip()
            for nav in lib.get("SecondNav", []):
                pdf_url = nav.get("PDFURL", "")
                if not pdf_url:
                    continue
                nav_name = nav.get("Name", "").strip()
                # Extract last path segment before unquoting to avoid %2F splitting filename
                raw_name = urlparse(pdf_url).path.split("/")[-1]
                filename = unquote(raw_name)
                # Replace invalid windows filename characters if any (like /)
                filename = re.sub(r'[<>:"/\\|?*\x00-\x1f]', '_', filename)
                if not filename.lower().endswith('.pdf'):
                    continue
                m = re.match(r"^(.+)_(\d+)\.pdf$", filename)
                if m:
                    source_name = m.group(1)
                    remote_ts = int(m.group(2))
                else:
                    source_name = f"{lib_name}_{nav_name}"
                    remote_ts = 0

                local_path, local_ts = get_local_pdf(source_name)

                results.append({
                    "lib_id": lib_id,
                    "lib_name": lib_name,
                    "nav_name": nav_name,
                    "source_name": source_name,
                    "remote_ts": remote_ts,
                    "local_ts": local_ts,
                    "local_path": local_path,
                    "pdf_url": pdf_url,
                    "filename": filename,
                    "updated_time": nav.get("UpdatedTime", ""),
                    "has_update": remote_ts > local_ts,
                })
    return results


def download_file(url: str, dest_path: Path):
    """Download a file with atomic write."""
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    temp_path = dest_path.with_suffix(".tmp")
    req = urllib.request.Request(url, headers=HEADERS)

    t0 = time.time()
    with urllib.request.urlopen(req, context=SSL_CTX, timeout=60) as resp:
        total_size = int(resp.headers.get("Content-Length", 0))
        downloaded = 0
        chunk_size = 1024 * 1024  # 1MB chunk

        with open(temp_path, "wb") as f:
            while True:
                chunk = resp.read(chunk_size)
                if not chunk:
                    break
                f.write(chunk)
                downloaded += len(chunk)

    if total_size and downloaded != total_size:
        raise ValueError(f'Incomplete download: {dest_path.name}')
    with temp_path.open('rb') as check:
        if not check.read(5).startswith(b'%PDF-'):
            raise ValueError(f'Not a PDF: {dest_path.name}')

    temp_path.replace(dest_path)
    dur = max(0.001, time.time() - t0)
    size_mb = dest_path.stat().st_size / (1024 * 1024)
    speed = size_mb / dur
    print(f"  -> Downloaded: {dest_path.name} ({size_mb:.1f} MB in {dur:.1f}s, {speed:.1f} MB/s)")


def main():
    parser = argparse.ArgumentParser(description="Fetch latest PDF docs from Volcengine")
    parser.add_argument("--check", action="store_true", help="Only check for updates, do not download")
    parser.add_argument("--all", action="store_true", help="Download all available PDFs, not just configured products")
    parser.add_argument("--force", action="store_true", help="Force re-download even if timestamp matches")
    parser.add_argument("--clean-old", action="store_true", help="Remove older versions of downloaded PDFs")
    args = parser.parse_args()

    # Try to import configured product sources
    try:
        from products import PRODUCTS
        target_sources = {p["source"] for p in PRODUCTS}
    except ImportError:
        target_sources = {
            "对象存储_文档指南",
            "火山方舟_API参考",
            "火山方舟_文档指南",
            "AI MediaKit_API 参考",
            "AI MediaKit_文档指南",
        }

    lib_ids = extract_lib_ids_from_readme()
    print(f"Checking Volcengine doc libraries: {lib_ids} ...\n")

    items = discover_available_pdfs(lib_ids)

    # Filter target items
    if not args.all:
        matched_items = [it for it in items if it["source_name"] in target_sources]
    else:
        matched_items = items

    if not args.all:
        missing = target_sources - {it['source_name'] for it in matched_items}
        if missing:
            raise ValueError('Official source did not return required documents: ' + ', '.join(sorted(missing)))

    print(f"{'Source':<28} {'Local TS':<12} {'Remote TS':<12} {'Status':<10}")
    print("-" * 65)

    for it in matched_items:
        status = "UPDATE" if it["has_update"] else ("EXISTS" if it["local_ts"] else "NEW")
        print(f"{it['source_name']:<28} {str(it['local_ts'] or '-'):<12} {str(it['remote_ts']):<12} {status:<10}")

    print()

    if args.check:
        return

    to_download = [it for it in matched_items if it["has_update"] or args.force or not it["local_ts"]]

    if not to_download:
        print("All documents are already up to date.")
        return

    print(f"Found {len(to_download)} document(s) to download:\n")

    from concurrent.futures import ThreadPoolExecutor

    def _download_task(it):
        dest = DOC_DIR / it["filename"]
        print(f"Starting download: {it['source_name']} -> {it['filename']}")
        download_file(it["pdf_url"], dest)
        if args.clean_old and it["local_path"] and it["local_path"] != dest:
            print(f"  Removing old version: {it['local_path'].name}")
            it["local_path"].unlink(missing_ok=True)

    with ThreadPoolExecutor(max_workers=min(4, len(to_download))) as pool:
        list(pool.map(_download_task, to_download))

    if args.clean_old:
        valid_filenames = {it["filename"] for it in matched_items}
        for p in DOC_DIR.glob("*.pdf"):
            # Check if pdf belongs to a tracked source but is an outdated version or orphan
            for src in target_sources:
                if p.name.startswith(src) and p.name not in valid_filenames:
                    print(f"  Removing outdated/orphaned PDF: {p.name}")
                    p.unlink(missing_ok=True)
        valid_md_names = {f"{src}.md" for src in target_sources}
        for p in DOC_DIR.glob("*.md"):
            if p.name != "readme.md" and p.name not in valid_md_names:
                print(f"  Removing outdated/orphaned MD: {p.name}")
                p.unlink(missing_ok=True)

    print("\nDownload finished! You can now run:")
    print("  python tools/build_all.py --convert")


if __name__ == "__main__":
    main()
