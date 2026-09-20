#!/usr/bin/env python3
"""Fallback PDF -> intermediate MD extractor using pypdfium2.

markitdown (pdfminer) silently drops most CJK text on some Volcengine PDFs
(e.g. 火山方舟_文档指南 came out at 13% of its actual Chinese characters).
pypdfium2 reads those fonts correctly, so use this script whenever
`tools/check_extraction.py` reports a low ratio for a markitdown output.

Usage:
  uv run --locked skills/ai-platform-docs/scripts/pdf_to_md.py --pdf <source.pdf> --out <text.md>
"""

import argparse
import sys
from pathlib import Path

import pypdfium2 as pdfium


def extract(pdf_path: Path, out_path: Path) -> None:
    doc = pdfium.PdfDocument(str(pdf_path))
    total = len(doc)
    parts = []
    for i in range(total):
        text = doc[i].get_textpage().get_text_range()
        # Normalise to \n and drop the soft hyphen / replacement chars pdfium
        # emits where the PDF uses a private-use glyph as a word joiner.
        text = text.replace("\r\n", "\n").replace("\r", "\n").replace("￾", "")
        parts.append(text)
        if (i + 1) % 500 == 0 or (i + 1) == total:
            print(f"  [{pdf_path.stem}] {i + 1}/{total} pages", flush=True)
    out_path.write_text("\n".join(parts), encoding="utf-8")
    print(f"  [{pdf_path.stem}] done: {total} pages -> {out_path.stat().st_size / 1024 / 1024:.2f} MB", flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    extract(Path(args.pdf), Path(args.out))


if __name__ == "__main__":
    main()
