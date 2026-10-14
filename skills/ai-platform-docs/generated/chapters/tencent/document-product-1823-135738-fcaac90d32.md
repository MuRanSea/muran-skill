<!-- Official source: https://cloud.tencent.com/document/product/1823/135738 -->
<!-- Source SHA-256: 745fa11608e82c75c249713735c80e65ae6e4227cd89bc7d2d657dac5cc2475d -->

# 视频生成模型调用概览

官方来源：https://cloud.tencent.com/document/product/1823/135738
最近更新时间：2026-10-13 15:50:31

## 概述

TokenHub 视频生成模型提供**文生视频、图生视频、首尾帧生视频、参考生视频、全能视频生成、视频特效、人像驱动**等能力，覆盖 PixVerse、Kling、Vidu、MiniMax、Hy、优图等系列模型。本文为各模型的快速导航与选型指引。

**说明：**

各接口的详细参数、请求示例与返回字段请跳转对应文档查阅。计费说明请参见 [TokenHub 模型价格说明](https://cloud.tencent.com/document/product/1823/130055)。

## 模型列表

### WAND 系列

详情请参见 [WAND 生视频调用指南](https://cloud.tencent.com/document/product/1823/138195)。

| 模型名称 | model 参数值 | 支持能力 | 视频时长（秒） | 清晰度档位 |
| --- | --- | --- | --- | --- |
| WAND-Vega-Video-1.0-Lite | wand-vega-video-1.0-lite | 文生 / 首尾帧生 / 参考生 | 4 ~ 15 | 768P、1080P、2K、4K |

### PixVerse 系列

详情请参见 [PixVerse 生视频调用指南](https://cloud.tencent.com/document/product/1823/135325)。

| 模型名称 | model 参数值 | 支持能力 | 简要说明 |
| --- | --- | --- | --- |
| PixVerse-Video-v6 | `pixverse-video-v6.0` | 文生 / 图生 / 首尾帧 / 参考生 | 通用场景推荐，支持多镜头智能分镜。 |
| PixVerse-Video-c1 | `pixverse-video-c1` | 文生 / 图生 / 首尾帧 / 参考生 | 打斗、法术特效、高速运动等动态场景推荐。 |
| PixVerse-Video-v5.6 | `pixverse-video-v5.6` | 文生 / 图生 / 首尾帧 / 参考生 | 历史版本，新接入建议直接使用 V6.0。 |

### Kling 系列

详情请参见 [Kling 生视频调用指南](https://cloud.tencent.com/document/product/1823/135742)。

| 模型名称 | model 参数值 | 支持能力 | 简要说明 |
| --- | --- | --- | --- |
| Kling-Video-V3 | `kling-video-v3` | 文生 / 图生（含首尾帧、元素） | 旗舰款：原生音频、多镜头、元素引用与 4K，能力最全。 |
| Kling-Video-V3-omni | `kling-video-v3-omni` | 全能视频生成（多模态输入、视频编辑） | 参考视频、视频编辑等多模态混合输入场景。 |
| Kling-Video-V3-turbo | `kling-video-v3-turbo` | 文生 / 图生 | V3 快速版，批量生成、成本优先；无音频与多镜头。 |
| Kling-Video-O1 | `kling-video-o1` | 全能视频生成（多模态统一入口） | O1 系列多模态统一生成入口，时长上限 10 秒。 |
| Kling-Video-V2.6 | `kling-video-v2.6` | 文生 / 图生（含首尾帧） | 支持原生音频的成熟方案。 |
| Kling-Video-V2.5-turbo | `kling-video-v2.5-turbo` | 文生 / 图生（含首尾帧） | 参数最精简的入门款，成本敏感场景。 |
| Kling-Video-Motion-Control-V3.0 | `kling-video-motion-control-v3.0` | 动作控制（形象参考图 + 动作参考视频，支持引用主体） | 让形象参考图中的人物**复刻参考视频的动作**；支持引用 1 个主体 |
| Kling-Video-Motion-Control-V2.6 | `kling-video-motion-control-v2.6` | 动作控制（形象参考图 + 动作参考视频） | 动作控制上一代版本，不支持引用主体 |

### Vidu 系列

详情请参见 [Vidu 生视频调用指南](https://cloud.tencent.com/document/product/1823/135756)。

| 模型名称 | model 参数值 | 支持能力 | 简要说明 |
| --- | --- | --- | --- |
| Vidu-Video-q4-preview | `vidu-video-q4-preview` | 图生 / 参考生 / 音画同出 | 最新旗舰预览版：支持 2K / 4K 输出，参考生最多 15 张参考图 + 3 段参考音频。 |
| Vidu-Video-q3.0-turbo | `vidu-video-q3-turbo` | 文生 / 图生 / 参考生 / 首尾帧 / 智能切镜 / 音画同出 | 生成速度最快、性价比最高。 |
| Vidu-Video-q3.0-pro | `vidu-video-q3-pro` | 文生 / 图生 / 首尾帧 / 智能切镜 / 音画同出 | Q3 高画质版。 |
| Vidu-Video-q3.0 | `vidu-video-q3` | 参考生 / 智能切镜 / 音画同出 | 多机位一致性更出色。 |
| Vidu-Video-q2.0 | `vidu-video-q2` | 文生 / 参考生 | 动态效果好、细节丰富。 |
| Vidu-Video-q2.0-pro | `vidu-video-q2-pro` | 图生 / 参考生 / 首尾帧 | 参考生支持视频参考，唯一支持视频输入的 Vidu 模型。 |
| Vidu-Video-q2.0-turbo | `vidu-video-q2-turbo` | 图生 / 首尾帧 | Q2 快速版。 |

### MiniMax 视频

详情请参见 [MiniMax 调用指南](https://cloud.tencent.com/document/product/1823/135737)。

| 模型名称 | model 参数值 | 支持能力 | 简要说明 |
| --- | --- | --- | --- |
| MiniMax-Video-v2.3 | `minimax-video-v2.3` | 文生 / 图生 / 首尾帧 | 旗舰款：物理表现与指令遵循强，支持运镜指令。 |
| MiniMax-Video-v2.3-fast | `minimax-video-v2.3-fast` | 图生（首帧） | v2.3 快速版，批量创作成本更低；仅支持图生。 |
| MiniMax-Video-H3 | `minimax-video-h3` | 文生 / 图生（首尾帧）/ 多模态参考生 | 最新旗舰：2K 直出、多模态参考、原生立体声、最长15秒。 |
| MiniMax-Video-H3-Max | `minimax-video-h3-max` | 文生 / 图生（首帧 / 尾帧），不支持中间帧 | H3 极速版：出片更快、成本更低；**不支持中间帧与多模态参考生视频**。 |

### Hy 视频

详情请参见 [Hy 生视频调用指南](https://cloud.tencent.com/document/product/1823/137202)。

| 模型名称 | model 参数值 | 支持能力 | 简要说明 |
| --- | --- | --- | --- |
| Hy-Video-v1.5 | `hy-video-v1.5` | 文生 / 图生 | 混元生视频，基于混元大模型智能生成视频。 |

### YT（优图）视频

详情请参见 [YT 调用指南](https://cloud.tencent.com/document/product/1823/135716)。

| 模型名称 | model 参数值 | 支持能力 | 简要说明 |
| --- | --- | --- | --- |
| YT-Video-HumanActor | `yt-video-humanactor` | 人像驱动 | 单张参考照片驱动生成动态人像视频。 |
