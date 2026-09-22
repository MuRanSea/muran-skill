<!-- Official source: https://platform.minimax.cn/docs/guides/models-intro.md -->
<!-- Source SHA-256: 314382e2b4fb622889a147756d498abd58eed3bc3735c2aaa2b75701b6e92ec4 -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.minimaxi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 概览

> MiniMax 模型体系涵盖语言、视频、语音、图像与音乐五大方向，助力开发者高效构建智能应用。

### 语言模型

| **模型名称**                                                    | **介绍**                                                         |
| :---------------------------------------------------------- | :------------------------------------------------------------- |
| [MiniMax-M3](/docs/api-reference/text-anthropic-api)             | 原生多模态、1M 上下文的 Frontier Coding 模型                               |
| [MiniMax-M2.7](/docs/api-reference/text-anthropic-api)           | 开启模型的自我迭代                                                      |
| [MiniMax-M2.7-highspeed](/docs/api-reference/text-anthropic-api) | 与 M2.7 效果不变，速度大幅提升                                             |

<Accordion title="历史模型">
  | **模型名称**                                                    | **介绍**                                                         |
  | :---------------------------------------------------------- | :------------------------------------------------------------- |
  | [MiniMax-M2.5](/docs/api-reference/text-anthropic-api)           | 顶尖性能与极致性价比，轻松驾驭复杂任务                                            |
  | [MiniMax-M2.5-highspeed](/docs/api-reference/text-anthropic-api) | 与 M2.5 效果不变，速度大幅提升                                             |
  | [MiniMax-M2.1](/docs/api-reference/text-anthropic-api)           | 强大多语言编程能力，全面升级代码工程体验                                           |
  | [MiniMax-M2.1-highspeed](/docs/api-reference/text-anthropic-api) | 与 M2.1 效果不变，速度大幅提升                                             |
  | [MiniMax-M2](/docs/api-reference/text-anthropic-api)             | 专为高效编码与Agent工作流而生                                              |
</Accordion>

### 视频模型

| **模型名称**                                                    | **介绍**                                                                                                        |
| :---------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------ |
| [MiniMax H3](/docs/api-reference/video-generation-v2-create)     | 新一代开放通用多模态视频模型，支持文生 / 图生 / 首尾帧 / 多模态参考，768P / 2K 分辨率，4–15s 时长                                                 |
| [MiniMax H3 Max](/docs/api-reference/video-generation-v2-create) | 由 [fal.ai](https://fal.ai/) 基于 MiniMax H3 后训练的极速视频生成模型，专为高速视频生成而优化。仅支持文生 / 图生（首帧、尾帧），480P / 768P 分辨率，5–15s 时长 |

<Accordion title="历史模型">
  | **模型名称**                                                       | **介绍**                              |
  | :------------------------------------------------------------- | :---------------------------------- |
  | [MiniMax Hailuo 2.3](/docs/api-reference/video-generation-t2v)      | 全新视频生成模型，肢体动作、面部表情、物理表现与指令遵循再度突破    |
  | [MiniMax Hailuo 2.3 Fast](/docs/api-reference/video-generation-i2v) | 全新图生视频模型，物理表现与指令遵循具佳，更快更优惠          |
  | [MiniMax Hailuo 02](/docs/api-reference/video-generation-t2v)       | 新一代视频生成模型，1080p 原生，SOTA 指令遵循，极致物理表现 |
</Accordion>

### 语音模型

| **模型名称**                                           | **介绍**                                                         |
| :------------------------------------------------- | :------------------------------------------------------------- |
| [Speech-2.8-HD](/docs/api-reference/speech-t2a-http)    | 新一代语音 HD 模型，情绪渲染融合语气词，重塑自然听感                                   |
| [Speech-2.8-Turbo](/docs/api-reference/speech-t2a-http) | 新一代语音 Turbo 模型，极致生成速度，更自然逼真的音频效果                               |

<Accordion title="历史模型">
  | **模型名称**                                           | **介绍**                                                         |
  | :------------------------------------------------- | :------------------------------------------------------------- |
  | [Speech-2.6-HD](/docs/api-reference/speech-t2a-http)    | 极致音质与韵律表现，生成更快更自然                                              |
  | [Speech-2.6-Turbo](/docs/api-reference/speech-t2a-http) | 音质优异，超低时延，响应更灵敏                                                |
  | [Speech-02-HD](/docs/api-reference/speech-t2a-http)     | 语音 HD 模型，拥有出色的韵律和稳定性，复刻相似度和音质表现突出                              |
  | [Speech-02-Turbo](/docs/api-reference/speech-t2a-http)  | 语音 Turbo 模型，小语种能力增强，性能表现出色                                     |
</Accordion>

### 图片模型

| **模型名称**                                             | **介绍**                                                         |
| :--------------------------------------------------- | :------------------------------------------------------------- |
| [image-01](/docs/api-reference/image-generation-t2i)      | 图像生成模型，画面表现细腻，支持文生图、图生图                                        |
| [image-01-live](/docs/api-reference/image-generation-t2i) | 图像生成模型，手绘、卡通等画风增强，支持文生图并进行画风设置                                 |

### 音乐模型

<Note title="Music API 服务调整通知">
  自 2026 年 8 月 20 日起，付费接口（音乐生成、歌词生成）不再面向新用户提供服务，历史付费用户可继续使用现有 API 服务；免费音乐生成接口（Music-3.0-free、Music-2.6-free、music-cover-free）停止服务。

  如需体验或使用音乐生成能力，可前往 [MiniMax Audio](https://www.minimax.cn/audio)，或使用已发布在 [Hugging Face](https://huggingface.co/MiniMaxAI/MiniMax-Music3) 和 [魔搭 ModelScope](https://modelscope.cn/models/MiniMax/MiniMax-Music3) 的 MiniMax Music 3 开源模型。
</Note>

| **模型名称**                                       | **介绍**                                                          |
| :--------------------------------------------- | :-------------------------------------------------------------- |
| [music-3.0](/docs/api-reference/music-generation)   | 更懂创作意图，音质全面跃升，人声合成更自然                                           |
| [music-2.6](/docs/api-reference/music-generation)   | 以声传情：翻唱入心，器乐入魂                                                  |
| [music-cover](/docs/api-reference/music-generation) | 基于参考音频生成翻唱版本，支持一步翻唱和两步翻唱（可修改歌词），支持风格迁移和自动歌词提取                   |
