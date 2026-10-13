<!-- Official source: https://cloud.tencent.com/document/product/1823/135738 -->
<!-- Source SHA-256: c5032616fb260e69c0483f5781010faa1cca881bcae0f2241612e3e00f484f42 -->

# 视频生成模型调用概览

官方来源：https://cloud.tencent.com/document/product/1823/135738
最近更新时间：2026-09-18 22:00:30

## 概述

TokenHub 视频生成模型提供**文生视频、图生视频、首尾帧生视频、参考生视频、全能视频生成、视频特效、人像驱动**等能力，覆盖 PixVerse、Kling、Vidu、MiniMax、Hy、优图等系列模型。本文为各模型的快速导航与选型指引。

**说明：**

各接口的详细参数、请求示例与返回字段请跳转对应文档查阅。计费说明请参见 [TokenHub 模型价格说明](https://cloud.tencent.com/document/product/1823/130055)。

## 模型列表

### WAND 系列

详情请参见 [WAND 生视频调用指南](https://cloud.tencent.com/document/product/1823/138195)。

<table><colgroup><col/><col/><col/><col/><col/></colgroup><tbody><tr><td colspan="1" rowspan="1"><div><b>模型名称</b></div></td><td colspan="1" rowspan="1"><div><b>model 参数值</b></div></td><td colspan="1" rowspan="1"><div><b>支持能力</b></div></td><td colspan="1" rowspan="1"><div><b>视频时长（秒）</b></div></td><td colspan="1" rowspan="1"><div><b>清晰度档位</b></div></td></tr><tr><td colspan="1" rowspan="1"><div>WAND-Vega-Video-1.0-Lite</div></td><td colspan="1" rowspan="1"><div>wand-vega-video-1.0-lite</div></td><td colspan="1" rowspan="1"><div>文生 / 首尾帧生 / 参考生</div></td><td colspan="1" rowspan="1"><div>4 ~ 15</div></td><td colspan="1" rowspan="1"><div>768P、1080P、2K、4K</div></td></tr></tbody></table>

### PixVerse 系列

详情请参见 [PixVerse 调用指南](https://cloud.tencent.com/document/product/1823/135325)。

| 模型名称 | model 参数值 | 支持能力 | 简要说明 |
| --- | --- | --- | --- |
| PixVerse-Video-v6 | `pixverse-video-v6.0` | 文生 / 图生 / 首尾帧 / 参考生 | 通用场景推荐，支持多镜头智能分镜。 |
| PixVerse-Video-c1 | `pixverse-video-c1` | 文生 / 图生 / 首尾帧 / 参考生 | 打斗、法术特效、高速运动等动态场景推荐。 |
| PixVerse-Video-v5.6 | `pixverse-video-v5.6` | 文生 / 图生 / 首尾帧 / 参考生 | 历史版本，新接入建议直接使用 V6.0。 |

### Kling 系列

详情请参见 [Kling 生视频调用指南](https://cloud.tencent.com/document/product/1823/135742)。

<table><colgroup><col/><col/><col/><col/></colgroup><tbody><tr><td><div>模型名称</div></td><td><div>model 参数值</div></td><td><div>支持能力</div></td><td><div>简要说明</div></td></tr><tr><td><div>Kling-Video-V3</div></td><td><div><code>kling-video-v3</code></div></td><td><div>文生 / 图生（含首尾帧、元素）</div></td><td><div>旗舰款：原生音频、多镜头、元素引用与 4K，能力最全。</div></td></tr><tr><td><div>Kling-Video-V3-omni</div></td><td><div><code>kling-video-v3-omni</code></div></td><td><div>全能视频生成（多模态输入、视频编辑）</div></td><td><div>参考视频、视频编辑等多模态混合输入场景。</div></td></tr><tr><td><div>Kling-Video-V3-turbo</div></td><td><div><code>kling-video-v3-turbo</code></div></td><td><div>文生 / 图生</div></td><td><div>V3 快速版，批量生成、成本优先；无音频与多镜头。</div></td></tr><tr><td><div>Kling-Video-O1</div></td><td><div><code>kling-video-o1</code></div></td><td><div>全能视频生成（多模态统一入口）</div></td><td><div>O1 系列多模态统一生成入口，时长上限 10 秒。</div></td></tr><tr><td><div>Kling-Video-V2.6</div></td><td><div><code>kling-video-v2.6</code></div></td><td><div>文生 / 图生（含首尾帧）</div></td><td><div>支持原生音频的成熟方案。</div></td></tr><tr><td><div>Kling-Video-V2.5-turbo</div></td><td><div><code>kling-video-v2.5-turbo</code></div></td><td><div>文生 / 图生（含首尾帧）</div></td><td><div>参数最精简的入门款，成本敏感场景。</div></td></tr><tr><td colspan="1" rowspan="1"><div>Kling-Video-Motion-Control-V3.0</div></td><td colspan="1" rowspan="1"><div><code>kling-video-motion-control-v3.0</code></div></td><td colspan="1" rowspan="1"><div>动作控制（形象参考图 + 动作参考视频，支持引用主体）</div></td><td><div>让形象参考图中的人物<b>复刻参考视频的动作</b>；支持引用 1 个主体</div></td></tr><tr><td colspan="1" rowspan="1"><div>Kling-Video-Motion-Control-V2.6</div></td><td colspan="1" rowspan="1"><div><code>kling-video-motion-control-v2.6</code></div></td><td colspan="1" rowspan="1"><div>动作控制（形象参考图 + 动作参考视频）</div></td><td><div>动作控制上一代版本，不支持引用主体</div></td></tr></tbody></table>

### Vidu 系列

详情请参见 [Vidu 调用指南](https://cloud.tencent.com/document/product/1823/135756)。

| 模型名称 | model 参数值 | 支持能力 | 简要说明 |
| --- | --- | --- | --- |
| Vidu-Video-q3.0-turbo | `vidu-video-q3-turbo` | 文生 / 图生 / 参考生 / 首尾帧 / 智能切镜 / 音画同出 | 生成速度最快、性价比最高。 |
| Vidu-Video-q3.0-pro | `vidu-video-q3-pro` | 文生 / 图生 / 首尾帧 / 智能切镜 / 音画同出 | Q3 高画质版。 |
| Vidu-Video-q3.0 | `vidu-video-q3` | 参考生 / 智能切镜 / 音画同出 | 多机位一致性更出色。 |
| Vidu-Video-q2.0 | `vidu-video-q2` | 文生 / 参考生 | 动态效果好、细节丰富。 |
| Vidu-Video-q2.0-pro | `vidu-video-q2-pro` | 图生 / 参考生 / 首尾帧 | 参考生支持视频参考，唯一支持视频输入的 Vidu 模型。 |
| Vidu-Video-q2.0-turbo | `vidu-video-q2-turbo` | 图生 / 首尾帧 | Q2 快速版。 |

### MiniMax 视频

详情请参见 [MiniMax 调用指南](https://cloud.tencent.com/document/product/1823/135737)。

<table><colgroup><col/><col/><col/><col/></colgroup><tbody><tr><td><div>模型名称</div></td><td><div>model 参数值</div></td><td><div>支持能力</div></td><td><div>简要说明</div></td></tr><tr><td><div>MiniMax-Video-v2.3</div></td><td><div><code>minimax-video-v2.3</code></div></td><td><div>文生 / 图生 / 首尾帧</div></td><td><div>旗舰款：物理表现与指令遵循强，支持运镜指令。</div></td></tr><tr><td><div>MiniMax-Video-v2.3-fast</div></td><td><div><code>minimax-video-v2.3-fast</code></div></td><td><div>图生（首帧）</div></td><td><div>v2.3 快速版，批量创作成本更低；仅支持图生。</div></td></tr><tr><td><div>MiniMax-Video-H3</div></td><td><div><code>minimax-video-h3</code></div></td><td><div>文生 / 图生（首尾帧）/ 多模态参考生</div></td><td><div>最新旗舰：2K 直出、多模态参考、原生立体声、最长15秒。</div></td></tr><tr><td colspan="1" rowspan="1"><div>MiniMax-Video-H3-Max</div></td><td colspan="1" rowspan="1"><div><code>minimax-video-h3-max</code></div></td><td><div>文生 / 图生（首帧 / 尾帧），不支持中间帧</div></td><td><div>H3 极速版：出片更快、成本更低；<b>不支持中间帧与多模态参考生视频</b>。</div></td></tr></tbody></table>

### Hy 视频

详情请参见 [Hy 调用指南](https://cloud.tencent.com/document/product/1823/137202)。

| 模型名称 | model 参数值 | 支持能力 | 简要说明 |
| --- | --- | --- | --- |
| Hy-Video-v1.5 | `hy-video-v1.5` | 文生 / 图生 | 混元生视频，基于混元大模型智能生成视频。 |

### YT（优图）视频

详情请参见 [YT 调用指南](https://cloud.tencent.com/document/product/1823/135716)。

| 模型名称 | model 参数值 | 支持能力 | 简要说明 |
| --- | --- | --- | --- |
| YT-Video-HumanActor | `yt-video-humanactor` | 人像驱动 | 单张参考照片驱动生成动态人像视频。 |
