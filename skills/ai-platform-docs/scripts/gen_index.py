#!/usr/bin/env python3
"""Write the ai-platform-docs skill index files from the build manifests.

Reads build/<product>.json (written by build_volc_doc_skill.py --manifest) and
writes, into the skill root:

  INDEX.md          router - one summary table per zone, top-level sections only.
                    Small enough to read whole; that is its job.
  INDEX-<zone>.md   every chapter file of that zone with page + source line range.
                    Meant to be grepped, not read whole (TOS alone is ~1350 rows).

From the repository: uv run --locked skills/ai-platform-docs/scripts/gen_index.py
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from products import BUILD, PRODUCTS, SKILL  # noqa: E402

HEADER_NOTE = (
    "「页码」是原 PDF 页码范围；「行范围」是中间 MD（`doc/<源文档>.md`）的 1 起始行号，"
    "可据此回查原文。章节文件本身已去掉页眉页脚，回查 PDF 时用这两列。"
    "文件名即章节标题，日常定位直接 Glob 文件名即可，用不到这两列。"
)
TABLE_HEAD = ["| 编号 | 标题 | 页码 | 行范围(源文件) | 行数 | 文件 |",
              "|------|------|------|---------------|------|------|"]


def load(key):
    path = BUILD / f"{key}.json"
    if not path.exists():
        sys.exit(f"missing manifest {path} - run build_volc_doc_skill.py --manifest first")
    return json.loads(path.read_text(encoding="utf-8"))


def split_num(title):
    num, _, rest = title.partition(" ")
    return num, (rest or title).replace("|", "\\|")


def top_of(title):
    return split_num(title)[0].split(".")[0]


def zone_summary(meta):
    """Per top-level section: page range, file count, first file - the routing table."""
    groups = {}
    for r in meta["rows"]:
        groups.setdefault(top_of(r["title"]), []).append(r)
    out = ["| 章节 | 标题 | 页码范围 | 文件数 |", "|------|------|---------|-------|"]
    for num, title in meta["top_sections"].items():
        rows = groups.get(num)
        if not rows:
            continue
        pages = [int(r["page"]) for r in rows if r["page"].isdigit()]
        span = f"{min(pages)}-{max(pages)}" if pages else "-"
        out.append(f"| {num} | {title.replace('|', chr(92) + '|')} | {span} | {len(rows)} |")
    return out


def write_zone_index(p, meta):
    key = p["key"]
    lines = [f"# {p['label']}章节表（{key}）", "",
             f"来源：{p['doc_title']}（{meta['pages']} 页）。{meta['files']} 个章节文件，"
             f"接口级切分：一个接口/任务一个文件；超过 {meta['oversize']} 行的按语义块自动再拆为"
             f"`… - 第N部分`（{meta['subsplit_chunks']} 个章节被拆分）。", "",
             HEADER_NOTE, "",
             "**这张表用来 grep，不要整读。**", "", *TABLE_HEAD]
    for r in meta["rows"]:
        num, rest = split_num(r["title"])
        end = r.get("page_end", r["page"])
        pages = r["page"] if end == r["page"] else f"{r['page']}-{end}"
        lines.append(f"| {num} | {rest} | {pages} | {r['start']}-{r['end']} | "
                     f"{r['lines']} | `chapters/volcengine/{key}/{r['file'].replace('|', chr(92) + '|')}` |")
    out = SKILL / f"INDEX-{key}.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    metas = [(p, load(p["key"])) for p in PRODUCTS]

    lines = [f"# 火山引擎 - 产品文档索引", "",
             f"{len(metas)} 个产品区，每区一张章节表。本文件只列各区的一级章节用于选区；"
             "选定区后到 `INDEX-<区>.md` 里 grep 具体章节。", "",
             "| 区 | 目录 | 源文档 | 页数 | 章节文件 | 章节表 |",
             "|----|------|-------|------|---------|-------|"]
    for p, m in metas:
        lines.append(f"| {p['label']} | `chapters/volcengine/{p['key']}/` | {p['doc_title']} | "
                     f"{m['pages']} | {m['files']} | `INDEX-{p['key']}.md` |")
    lines += ["", HEADER_NOTE, ""]

    for p, m in metas:
        lines += [f"## {p['label']}（{p['key']}）", "", p["blurb"], "",
                  f"全部 {m['files']} 个章节文件见 `INDEX-{p['key']}.md`。", "",
                  *zone_summary(m), ""]

    (SKILL / "INDEX-volcengine.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"INDEX-volcengine.md: {len(lines)} lines")
    for p, m in metas:
        out = write_zone_index(p, m)
        print(f"{out.name}: {m['files']} rows")


if __name__ == "__main__":
    main()
