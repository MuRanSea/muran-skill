<!-- Official source: https://platform.minimax.cn/docs/guides/models-intro.md -->
<!-- Source SHA-256: 3cdfbd0339bfe98ed187bb211905df82521faee08971d9606ae6155881f3cebe -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.minimaxi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 概览

> MiniMax 模型体系涵盖语言、视频、语音、图像与音乐五大方向，助力开发者高效构建智能应用。

### 语言模型

| **模型名称**             | **介绍**                                                         |
| :- | :- |
| [MiniMax-M3.1-Flash](https://platform.minimaxi.com/docs/api-reference/text-anthropic-api.md) | 原生多模态、1M 上下文的 Frontier Coding 模型，思考深度可调 |
| [MiniMax-M3](https://platform.minimaxi.com/docs/api-reference/text-anthropic-api.md) | 原生多模态、1M 上下文的 Frontier Coding 模型 |

### 视频模型

| **模型名称**             | **介绍** |
| :- | :- |
| [MiniMax H3](https://platform.minimaxi.com/docs/api-reference/video-generation-v2-create.md) | 新一代开放通用多模态视频模型，支持文生 / 图生 / 首尾帧 / 多模态参考，768P / 2K 分辨率，4–15s 时长 |
| [MiniMax H3 Max](https://platform.minimaxi.com/docs/api-reference/video-generation-v2-create.md) | 由 [fal.ai](https://fal.ai/) 基于 MiniMax H3 后训练的极速视频生成模型，专为高速视频生成而优化。仅支持文生 / 图生（首帧、尾帧），480P / 768P 分辨率，5–15s 时长 |

> **历史模型**
>
> | **模型名称**             | **介绍** |
> | :- | :- |
> | [MiniMax Hailuo 2.3](https://platform.minimaxi.com/docs/api-reference/video-generation-t2v.md) | 全新视频生成模型，肢体动作、面部表情、物理表现与指令遵循再度突破 |
> | [MiniMax Hailuo 2.3 Fast](https://platform.minimaxi.com/docs/api-reference/video-generation-i2v.md) | 全新图生视频模型，物理表现与指令遵循具佳，更快更优惠 |
> | [MiniMax Hailuo 02](https://platform.minimaxi.com/docs/api-reference/video-generation-t2v.md) | 新一代视频生成模型，1080p 原生，SOTA 指令遵循，极致物理表现 |

### 语音模型

| **模型名称**             | **介绍**                                                         |
| :- | :- |
| [Speech-2.8-HD](https://platform.minimaxi.com/docs/api-reference/speech-t2a-http.md) | 新一代语音 HD 模型，情绪渲染融合语气词，重塑自然听感 |
| [Speech-2.8-Turbo](https://platform.minimaxi.com/docs/api-reference/speech-t2a-http.md) | 新一代语音 Turbo 模型，极致生成速度，更自然逼真的音频效果 |

> **历史模型**
>
> | **模型名称**             | **介绍**                                                         |
> | :- | :- |
> | [Speech-2.6-HD](https://platform.minimaxi.com/docs/api-reference/speech-t2a-http.md) | 极致音质与韵律表现，生成更快更自然 |
> | [Speech-2.6-Turbo](https://platform.minimaxi.com/docs/api-reference/speech-t2a-http.md) | 音质优异，超低时延，响应更灵敏 |
> | [Speech-02-HD](https://platform.minimaxi.com/docs/api-reference/speech-t2a-http.md) | 语音 HD 模型，拥有出色的韵律和稳定性，复刻相似度和音质表现突出 |
> | [Speech-02-Turbo](https://platform.minimaxi.com/docs/api-reference/speech-t2a-http.md) | 语音 Turbo 模型，小语种能力增强，性能表现出色 |

### 图片模型

| **模型名称**            | **介绍**                                                         |
| :- | :- |
| [image-01](https://platform.minimaxi.com/docs/api-reference/image-generation-t2i.md) | 图像生成模型，画面表现细腻，支持文生图、图生图 |
| [image-01-live](https://platform.minimaxi.com/docs/api-reference/image-generation-t2i.md) | 图像生成模型，手绘、卡通等画风增强，支持文生图并进行画风设置 |

### 音乐模型

> [!NOTE]
>
> 自 2026 年 8 月 20 日起，付费接口（音乐生成、歌词生成）不再面向新用户提供服务，历史付费用户可继续使用现有 API 服务；免费音乐生成接口（Music-3.0-free、Music-2.6-free、music-cover-free）停止服务。
>
> 如需体验或使用音乐生成能力，可前往 [MiniMax Audio](https://www.minimax.cn/audio)，或使用已发布在 [Hugging Face](https://huggingface.co/MiniMaxAI/MiniMax-Music3) 和 [魔搭 ModelScope](https://modelscope.cn/models/MiniMax/MiniMax-Music3) 的 MiniMax Music 3 开源模型。

| **模型名称**            | **介绍**                                                          |
| :- | :- |
| [music-3.0](https://platform.minimaxi.com/docs/api-reference/music-generation.md) | 更懂创作意图，音质全面跃升，人声合成更自然 |
| [music-2.6](https://platform.minimaxi.com/docs/api-reference/music-generation.md) | 以声传情：翻唱入心，器乐入魂 |
| [music-cover](https://platform.minimaxi.com/docs/api-reference/music-generation.md) | 基于参考音频生成翻唱版本，支持一步翻唱和两步翻唱（可修改歌词），支持风格迁移和自动歌词提取 |
