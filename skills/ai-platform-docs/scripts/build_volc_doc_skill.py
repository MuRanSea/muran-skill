#!/usr/bin/env python3
"""Build ai-platform-docs skill chapter files from an intermediate Markdown.

Usage:
  uv run --locked skills/ai-platform-docs/scripts/build_volc_doc_skill.py --md <intermediate.md> --product <name> \
      --out-dir <skill>/chapters/<product> [--oversize N] [--manifest out.json]

Pipeline (see CONTEXT.md): 原始文档(PDF) -> 中间 MD -> 接口级切分章节文件.

Splitting strategy (endpoint-level split):
- The document's own TOC (lines of the form "N.N Title <page>") is parsed to get the
  authoritative set of heading numbers, so prose lines that look like headings
  (e.g. "0.1 节点温度...", "2.0 支持") are ignored.
- A body heading is a chunk boundary unless it has a deeper child heading directly
  after it (group headers like "13.1 管理推理接入点" become preamble of their
  first child chunk).
- Chunks over --oversize lines are sub-split automatically (see subsplit): cuts land
  on a semantic anchor (请求参数/响应参数/示例/错误码/...) when one falls in range,
  otherwise on a PDF page boundary, so a part never starts mid-sentence.

The JSON manifest written with --manifest is what tools/gen_index.py turns into
INDEX files, so the index never has to re-derive the chunking.
"""

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

NUMBER = r"\d+(?:\.\d+)*\.?"
TOC_ENTRY_RE = re.compile(rf"^({NUMBER}) (.+?) (\d+)$")
# The title may start with a digit ("2.5.1 3D 生成"); collect_headings' TOC-title
# match is what keeps numeric list items out, so no [^\d] guard here.
HEADING_RE = re.compile(rf"^({NUMBER}) (.+)$")
FOOTER_RE = re.compile(r"版权所有©北京火山引擎科技有限公司 (\d+)/\d+")
FOOTER_ANY_RE = re.compile(r"版权所有©北京火山引擎科技有限公司")
INVALID_FN_CHARS = re.compile(r'[\\/:*?"<>|\r\n\t]')
SPACE_RUN = re.compile(r" {2,}")

# Section labels the Volcengine docs use inside a single endpoint. A cut here keeps
# a sub-part self-contained and gives it a meaningful name.
ANCHORS = (
    "请求参数", "响应参数", "返回参数", "请求体", "响应体", "请求示例", "响应示例",
    "示例代码", "调用示例", "使用示例", "代码示例", "错误码", "错误处理", "参数说明",
    "接口说明", "使用限制", "注意事项", "前提条件", "快速开始", "操作步骤", "常见问题",
    "计费说明", "最佳实践", "SDK 示例", "返回示例", "功能说明",
)
ANCHOR_RE = re.compile(rf"^\s*({'|'.join(ANCHORS)})\s*[:：]?\s*$")


BARE_MARKER_RE = re.compile(r"^\s*(?:[•·▪]|\d{1,2}\.|[a-z]\.|[（(]\d{1,2}[）)])\s*$")
# A line that starts one of these cannot be the tail of a wrapped sentence.
BLOCK_START_RE = re.compile(r"^(?:\s|[{}\[\]<>\"'#$|]|//|--|\*|•|·|▪|\d{1,2}\.\s|[a-z]\.\s)")
# Text column width the PDF wraps prose at; measured peak is 88-93 across all four
# docs, so a line at least this wide was broken by the layout, not by the author.
WRAP_WIDTH = 80


def display_width(s: str) -> int:
    return sum(2 if ord(c) > 0x2E80 else 1 for c in s)


def header_prefix(lines):
    """The running header ('文档指南 8. API 参考') is always the line before the page
    footer, and its prefix is the document's own title. Derive it from the data
    rather than hard-coding one title per product."""
    counts = Counter()
    for i, ln in enumerate(lines):
        if i and FOOTER_ANY_RE.search(ln):
            m = re.match(r"^(.{1,20}?) \d+\. ", lines[i - 1])
            if m:
                counts[m.group(1)] += 1
    return counts.most_common(1)[0][0] if counts else None


def normalize(body, prefix, is_heading):
    """Strip page furniture and rejoin lines the PDF layout wrapped mid-sentence.

    26% of raw lines end mid-sentence, which is why grepping a whole phrase like
    '文件在一定时间后过期删除' found nothing before this ran. Page headers/footers are
    dropped first so a sentence spanning a page boundary can rejoin.
    """
    hdr = re.compile(rf"^{re.escape(prefix)} \d+\. ") if prefix else None
    kept = []
    for ln in body:
        if FOOTER_ANY_RE.search(ln) or BARE_MARKER_RE.match(ln):
            continue
        if hdr and hdr.match(ln):
            continue
        kept.append(ln)

    out = []
    prev_wrapped = False  # did the previous *source* line fill the text column?
    for ln in kept:
        if prev_wrapped and out and not is_heading(ln) and not BLOCK_START_RE.match(ln):
            out[-1] += ln
        elif ln.strip() or (out and out[-1].strip()):
            out.append(ln)
        prev_wrapped = display_width(ln) >= WRAP_WIDTH and not is_heading(ln)
    while out and not out[-1].strip():
        out.pop()
    return out


def sanitize_filename(text: str, max_len: int = 100) -> str:
    name = INVALID_FN_CHARS.sub("-", text)
    name = SPACE_RUN.sub(" ", name).strip(" .")
    if len(name) > max_len:
        name = name[:max_len].rstrip(" .-")
    return name


def plausible_section(num):
    """Reject date fragments that match the entry pattern: '2023 年 03 月 59' and
    '05 月 20 日 ~ 06 月 30 日 87' both parse as TOC entries otherwise. A real
    top-level section is 1..99 with no leading zero."""
    head = num.split(".")[0]
    return not head.startswith("0") and head.isdigit() and 1 <= int(head) <= 99


def parse_toc(lines):
    """File-wide scan of TOC entries ('N.N Title <page>'). The TOC may span pages
    with page footers/headers in between, so a contiguous-run scan is not safe."""
    nums = {}
    for ln in lines:
        m = TOC_ENTRY_RE.match(ln)
        if not m:
            continue
        num = m.group(1).rstrip(".")
        if not plausible_section(num):
            continue
        # First match wins: the real TOC sits at the front of the document, so a
        # later prose line that happens to look like an entry ("1 项，最多 100")
        # must not overwrite the genuine title.
        nums.setdefault(num, m.group(2))
    return nums


def collect_headings(lines, toc_nums):
    """Body headings: lines matching the heading pattern whose number is a real
    TOC number AND whose title matches the TOC title (the PDF body truncates long
    headings, so the body title is usually a prefix of the TOC title). This keeps
    ordered-list items ('2. （可选）单击...') and prose references out."""
    seen = set()
    headings = []
    for i, ln in enumerate(lines):
        if TOC_ENTRY_RE.match(ln):
            continue
        m = HEADING_RE.match(ln)
        if not m:
            continue
        num = m.group(1).rstrip(".")
        title = m.group(2)
        toc_title = toc_nums.get(num)
        if not toc_title or len(title) < 2:
            continue
        if not (toc_title.startswith(title) or title.startswith(toc_title)):
            continue
        if num not in seen:
            seen.add(num)
            headings.append((i, num, title))
    return headings


def is_child(heading, next_heading):
    num, next_num = heading[1], next_heading[1]
    return len(next_num.split(".")) > len(num.split(".")) and next_num.startswith(num + ".")


def split_chunks(lines, headings):
    """One pass over headings: group headers (with their trailing intro lines)
    accumulate as preamble for the next boundary; a boundary heading starts a
    chunk that ends at the next heading line (group or boundary).
    Each chunk carries `pre`, the length of that preamble. Since the group headers
    chain contiguously up to the chunk's own heading, body[j] is always
    lines[start - pre + j] - which is how sub-split parts map back to source lines.
    """
    chunks = []
    pending = []
    for idx, h in enumerate(headings):
        nxt = headings[idx + 1] if idx + 1 < len(headings) else None
        if nxt is not None and is_child(h, nxt):
            pending.extend(lines[h[0] : nxt[0]])
            continue
        end = nxt[0] if nxt is not None else len(lines)
        title = " ".join(lines[h[0]].split())
        chunks.append((title, h[0], end, pending + lines[h[0] : end], len(pending)))
        pending = []
    return chunks


def first_footer_page(chunk_lines, fallback=None):
    for line in chunk_lines[:80]:
        m = FOOTER_RE.search(line)
        if m:
            return m.group(1)
    return fallback


def last_footer_page(chunk_lines, fallback=None):
    for line in reversed(chunk_lines):
        m = FOOTER_RE.search(line)
        if m:
            return m.group(1)
    return fallback


def page_at(body, upto):
    """PDF page that body[upto] sits on. A footer ends its page, so the line after
    the last footer before `upto` is already on the next page."""
    page = None
    for line in body[:upto]:
        m = FOOTER_RE.search(line)
        if m:
            page = m.group(1)
    return str(int(page) + 1) if page else None


def subsplit(body, limit):
    """Cut an oversized chunk into parts of roughly `limit` lines.

    Prefer the last semantic anchor in the part's tail window; fall back to the
    last page boundary; hard-cut only if neither exists. Anchors may overshoot
    `limit` by `slack` lines - keeping 请求参数/响应参数 whole is worth a longer
    file than cutting a parameter table in half.
    Returns [(start, end, anchor_label_or_None), ...] over body indices.
    """
    anchors, pages = set(), set()
    for i, line in enumerate(body):
        if ANCHOR_RE.match(line):
            anchors.add(i)
        elif FOOTER_ANY_RE.search(line):
            pages.add(i + 1)  # part starts on the line after the footer

    slack = int(limit * 0.3)
    parts = []
    start, label = 0, None
    n = len(body)
    while n - start > limit + slack:
        lo, hi = start + limit // 2, start + limit
        window_anchors = [i for i in anchors if lo < i <= hi + slack]
        window_pages = [i for i in pages if lo < i <= hi]
        if window_anchors:
            cut = max(window_anchors)
            next_label = body[cut].strip().rstrip(":：")
        elif window_pages:
            cut = max(window_pages)
            next_label = None
        else:
            cut, next_label = hi, None
        parts.append((start, cut, label))
        start, label = cut, next_label
    parts.append((start, n, label))
    return parts


def part_title(title, idx, label):
    return f"{title} - 第{idx}部分" + (f"·{label}" if label else "")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--md", required=True, help="intermediate markdown")
    ap.add_argument("--product", required=True, help="product key, e.g. ark / tos")
    ap.add_argument("--out-dir", required=True, help="chapter output dir")
    ap.add_argument("--oversize", type=int, default=1500, help="max lines per chapter file")
    ap.add_argument("--manifest", help="write chapter metadata as JSON here")
    args = ap.parse_args()

    sys.stdout.reconfigure(encoding="utf-8")
    src = Path(args.md)
    lines = src.read_text(encoding="utf-8").splitlines()
    toc_nums = parse_toc(lines)
    headings = collect_headings(lines, toc_nums)
    chunks = split_chunks(lines, headings)

    out = Path(args.out_dir)
    if out.exists():
        for old in out.iterdir():
            old.unlink()
    out.mkdir(parents=True, exist_ok=True)

    prefix = header_prefix(lines)
    heading_lines = {lines[i] for i, _, _ in headings}
    is_heading = heading_lines.__contains__

    rows = []
    prev_page = None
    n_split = 0
    for title, start, end, body, pre in chunks:
        page = first_footer_page(body, prev_page)
        if page:
            prev_page = page
        norm = normalize(body, prefix, is_heading)
        last = last_footer_page(body, page)
        if len(norm) <= args.oversize:
            fname = sanitize_filename(title) + ".md"
            (out / fname).write_text("\n".join(norm), encoding="utf-8")
            rows.append(dict(title=title, page=page or "-", page_end=last or page or "-",
                             start=start + 1, end=end, lines=len(norm), file=fname))
            continue
        n_split += 1
        # subsplit needs the raw body (page footers are its cut points), so scale the
        # limit by how much normalisation shrinks this chunk to land near --oversize.
        raw_limit = max(1, round(args.oversize * len(body) / len(norm)))
        for i, (ps, pe, label) in enumerate(subsplit(body, raw_limit), 1):
            ptitle = part_title(title, i, label)
            fname = sanitize_filename(ptitle) + ".md"
            part = normalize(body[ps:pe], prefix, is_heading)
            (out / fname).write_text("\n".join(part), encoding="utf-8")
            ppage = page_at(body, ps) or page or "-"
            rows.append(dict(title=ptitle, page=ppage,
                             page_end=last_footer_page(body[ps:pe], ppage) or ppage,
                             start=start - pre + ps + 1, end=start - pre + pe,
                             lines=len(part), file=fname))

    # The footer's own denominator ("… 194/924") is the document's page count; counting
    # footer lines drifts because a few pages repeat or lose theirs.
    denoms = Counter(m.group(1) for ln in lines
                     for m in [re.search(r"版权所有©北京火山引擎科技有限公司 \d+/(\d+)", ln)] if m)
    pages = (int(denoms.most_common(1)[0][0]) if denoms
             else sum(1 for ln in lines if FOOTER_ANY_RE.search(ln)))
    tops = {n: t for n, t in sorted(toc_nums.items(), key=lambda kv: int(kv[0].split(".")[0]))
            if "." not in n}
    meta = dict(product=args.product, source=src.name, pages=pages,
                src_lines=len(lines), chunks=len(chunks), files=len(rows),
                oversize=args.oversize, subsplit_chunks=n_split,
                header_prefix=prefix, top_sections=tops, rows=rows)
    if args.manifest:
        Path(args.manifest).parent.mkdir(parents=True, exist_ok=True)
        Path(args.manifest).write_text(json.dumps(meta, ensure_ascii=False, indent=1),
                                       encoding="utf-8")

    biggest = max(rows, key=lambda r: r["lines"])
    print(f"{args.product}: {pages} pages | {len(chunks)} chunks -> {len(rows)} files "
          f"({n_split} sub-split) | largest {biggest['lines']} lines: {biggest['file']}")


if __name__ == "__main__":
    sys.exit(main())
