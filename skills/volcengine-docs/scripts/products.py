#!/usr/bin/env python3
"""Single source of truth for the doc zones of the volcengine-docs skill.

Adding a product means adding one entry here plus dropping its PDF in doc/ named
`<source>_<timestamp>.pdf` - build_all.py and gen_index.py both read this list.
"""

import os
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
ROOT = Path(os.environ.get('MURAN_VOLC_WORK_ROOT', str(SKILL_ROOT / '.cache' / 'work')))
DOC = ROOT / "doc"
BUILD = ROOT / "build"
SKILL = ROOT / "generated"

PRODUCTS = [
    dict(
        key="tos",
        label="TOS 区",
        source="对象存储_文档指南",
        doc_title="《对象存储 文档指南》",
        blurb="对象存储：存储桶/对象操作、生命周期、回源、镜像、事件通知、tosutil、SDK、API 签名、错误码、计费",
    ),
    dict(
        key="ark",
        label="方舟 API 区",
        source="火山方舟_API参考",
        doc_title="《火山方舟 API 参考》",
        blurb="方舟接口契约：Chat/Responses/Files、视频·图片·3D 生成、向量化、上下文缓存、批量推理、"
              "Managed Agents、接入点与 API Key 管理、分词",
    ),
    dict(
        key="ark-guide",
        label="方舟指南区",
        source="火山方舟_文档指南",
        doc_title="《火山方舟 文档指南》",
        blurb="方舟使用指南：模型列表与价格、多模态理解、视频·图片生成教程、Function Calling、深度思考、"
              "模型精调与评测、Agent 开发、订阅与配额",
    ),
    dict(
        key="mediakit",
        label="AI MediaKit API 区",
        source="AI MediaKit_API 参考",
        doc_title="《AI MediaKit API 参考》",
        blurb="智能处理接口契约：视频/图像/剪辑/音频/大模型工具提交任务 API、查询任务、获取媒体上传地址、事件回调、错误码",
    ),
    dict(
        key="mediakit-guide",
        label="AI MediaKit 指南区",
        source="AI MediaKit_文档指南",
        doc_title="《AI MediaKit 文档指南》",
        blurb="智能处理使用指南：画质增强、字幕擦除、转码、极智超清、暗水印、场景切分、高光智剪、剧本还原、解说视频、"
              "OCR·翻译、智能剪辑、音频工具、CLI/Skill/MCP、计费说明",
    ),
]


def md_path(p):
    return DOC / f"{p['source']}.md"


def pdf_path(p):
    """The newest doc/<source>_<timestamp>.pdf - exports are timestamp-suffixed."""
    pdfs = sorted(DOC.glob(f"{p['source']}_*.pdf"))
    return pdfs[-1] if pdfs else None
