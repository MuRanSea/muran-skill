#!/usr/bin/env python3
"""Sanity-check a ai-platform-docs build.

Verifies, per product: every manifest row has a file on disk and vice versa; the
row line-ranges cover the source MD from its first heading to the end without
gaps; and no chapter file is empty. Also re-checks CJK extraction against the
PDF, which is how the 火山方舟_文档指南 markitdown failure (13% of the Chinese
text) was caught.

From the repository: uv run --locked skills/ai-platform-docs/scripts/check_build.py [--pdf]
(--pdf adds the slow PDF re-check)
"""

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from products import BUILD, DOC, SKILL, PRODUCTS, pdf_path  # noqa: E402

CJK = re.compile(r"[一-鿿]")
GAP_TOLERANCE = 5


def check_lossless(meta, src_lines, chapters, rows):
    """The normaliser rejoins wrapped lines and drops page furniture; this proves the
    rejoining never drops characters. Furniture is stripped here with an independent
    rule, then each chapter's text must still contain its whole source slice.
    """
    prefix = meta.get("header_prefix")
    hdr = re.compile(rf"^{re.escape(prefix)} \d+\. ") if prefix else None
    marker = re.compile(r"^\s*(?:[•·▪]|\d{1,2}\.|[a-z]\.|[（(]\d{1,2}[）)])\s*$")

    def content(lines):
        keep = [ln for ln in lines
                if "版权所有©北京火山引擎科技有限公司" not in ln
                and not marker.match(ln) and not (hdr and hdr.match(ln))]
        return "".join("".join(ln.split()) for ln in keep)

    problems = []
    for r in rows:
        want = content(src_lines[r["start"] - 1:r["end"]])
        got = "".join((chapters / r["file"]).read_text(encoding="utf-8").split())
        if want and want not in got:
            problems.append(f"content lost in {r['file']} "
                            f"(source lines {r['start']}-{r['end']})")
            if len(problems) > 3:
                break
    return problems


def check_product(key, pdf_check):
    meta = json.loads((BUILD / f"{key}.json").read_text(encoding="utf-8"))
    rows, problems = meta["rows"], []
    chapters = SKILL / "chapters" / "volcengine" / key

    on_disk = {p.name for p in chapters.iterdir()}
    in_index = {r["file"] for r in rows}
    for name in sorted(in_index - on_disk):
        problems.append(f"indexed but missing on disk: {name}")
    for name in sorted(on_disk - in_index):
        problems.append(f"on disk but not indexed: {name}")
    if len(in_index) != len(rows):
        problems.append(f"duplicate filenames: {len(rows)} rows -> {len(in_index)} names")

    for r in rows:
        f = chapters / r["file"]
        if f.exists() and not f.read_text(encoding="utf-8").strip():
            problems.append(f"empty chapter file: {r['file']}")

    src = DOC / meta["source"]
    src_lines = src.read_text(encoding="utf-8").splitlines()
    total = len(src_lines)
    problems += check_lossless(meta, src_lines, chapters, rows)
    ordered = sorted(rows, key=lambda r: r["start"])
    cursor = ordered[0]["start"]
    front = cursor - 1  # cover page + TOC, intentionally not part of any chapter
    for r in ordered:
        if r["start"] > cursor + GAP_TOLERANCE:
            problems.append(f"gap in source coverage: lines {cursor}-{r['start'] - 1}")
        cursor = max(cursor, r["end"] + 1)
    if total - cursor > GAP_TOLERANCE:
        problems.append(f"tail not covered: lines {cursor}-{total}")

    md_cjk = len(CJK.findall(src.read_text(encoding="utf-8")))
    note = ""
    if pdf_check:
        import pypdfium2 as pdfium
        pdf = pdf_path(next(p for p in PRODUCTS if p['key'] == key))
        if pdf is None:
            raise FileNotFoundError(f'No PDF for {key}; rebuild with --fetch')
        d = pdfium.PdfDocument(str(pdf))
        n = len(d)
        sampled = c = 0
        step = max(1, n // 100)
        for i in range(0, n, step):
            c += len(CJK.findall(d[i].get_textpage().get_text_range()))
            sampled += 1
        est = c * n / sampled
        ratio = md_cjk / est if est else 0
        note = f" | PDF CJK ratio {ratio:.2f}"
        if ratio < 0.8:
            problems.append(f"extraction lost text: MD has {ratio:.0%} of the PDF's Chinese "
                            f"characters - re-extract with tools/pdf_to_md.py")

    status = "OK " if not problems else "FAIL"
    print(f"[{status}] {key}: {len(rows)} files, {meta['pages']} pages, "
          f"source {total} lines (front matter {front} lines){note}")
    for p in problems:
        print(f"       - {p}")
    return not problems


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", action="store_true", help="also re-check CJK against the PDFs")
    args = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    keys = sorted(p.stem for p in BUILD.glob("*.json"))
    ok = all([check_product(k, args.pdf) for k in keys])
    print("\nall good" if ok else "\nproblems found")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
