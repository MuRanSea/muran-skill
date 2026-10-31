<!-- Official source: https://platform.minimax.cn/docs/faq/models.md -->
<!-- Source SHA-256: 1f2b437460f88635da1ff94bdaefce997a8d7da65c00f3beed7289788c99098d -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.minimaxi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 模型列表

> 查看 MiniMax 开放平台当前支持的模型，以及已下线的历史模型。

模型定价信息请参阅[产品定价](https://platform.minimaxi.com/docs/pricing/overview.md)。

> [accordion] MiniMax M2.5、M2.7 系列模型下线通知
>
> 随着新版本模型的推出，我们将逐步停止提供 MiniMax M2.5、M2.7 系列模型服务，并为现有用户预留迁移时间。具体安排如下：
>
> * **停止向新用户开放调用：**【2026年10月19日】
> * **正式下线：**【2026年11月18日】
>
> **按量付费 API 用户**
>
> 存量用户可继续调用至正式下线日，正式下线后相关 API 调用将不再可用。请提前核查调用情况，并在下线前完成模型迁移。
>
> **M Plan 和 Token Plan 用户**
>
> M2.5、M2.7 系列模型请求将于【2026年10月19日】统一路由至 **M3.1 Flash**。
>
> 原模型名称保留作为兼容入口，用户无需修改模型名称，原有套餐用量权益不受影响。
>
> 为避免影响业务，**请尽快核查调用情况并提前做好模型迁移准备。**
>
> 感谢您一直以来对MiniMax的支持与信任。

## 可用模型

### 语言模型

| 模型名称 | 描述 |
| :- | :- |
| [MiniMax-M3.1-Flash](https://platform.minimaxi.com/docs/guides/text-generation.md) | 原生多模态、1M 上下文的 Frontier Coding 模型，思考深度可调 |
| [MiniMax-M3](https://platform.minimaxi.com/docs/guides/text-generation.md) | 原生多模态、1M 上下文的 Frontier Coding 模型 |

### 视频模型

| 模型名称 | 描述 |
| :- | :- |
| [MiniMax-H3](https://platform.minimaxi.com/docs/guides/video-generation.md) | 新一代开放通用多模态视频模型，支持文生 / 图生 / 首尾帧 / 多模态参考，768P / 2K 分辨率，4–15s 时长 |
| [MiniMax-H3-Max](https://platform.minimaxi.com/docs/guides/video-generation.md) | 基于 MiniMax H3 后训练的极速视频生成模型，专为高速视频生成而优化。仅支持文生 / 图生（首帧、尾帧），480P / 768P 分辨率，5–15s 时长 |
| [MiniMax-Hailuo-2.3](https://platform.minimaxi.com/docs/guides/video-generation.md) | 全新视频生成模型，肢体动作、面部表情、物理表现与指令遵循再度突破 |
| [MiniMax-Hailuo-2.3-Fast](https://platform.minimaxi.com/docs/guides/video-generation.md) | 全新图生视频模型，物理表现与指令遵循具佳，更快更优惠 |
| [MiniMax-Hailuo-02](https://platform.minimaxi.com/docs/guides/video-generation.md) | 新一代视频生成模型，1080p 原生，SOTA 指令遵循，极致物理表现 |

### 语音模型

| 模型名称 | 描述 |
| :- | :- |
| [speech-2.8-hd](https://platform.minimaxi.com/docs/guides/speech-t2a-websocket.md) | 新一代语音 HD 模型，情绪渲染融合语气词，重塑自然听感 |
| [speech-2.8-turbo](https://platform.minimaxi.com/docs/guides/speech-t2a-websocket.md) | 新一代语音 Turbo 模型，极致生成速度，更自然逼真的音频效果 |
| [speech-2.6-hd](https://platform.minimaxi.com/docs/guides/speech-t2a-websocket.md) | 极致音质与韵律表现，生成更快更自然 |
| [speech-2.6-turbo](https://platform.minimaxi.com/docs/guides/speech-t2a-websocket.md) | 音质优异，超低时延，响应更灵敏 |
| [speech-02-hd](https://platform.minimaxi.com/docs/guides/speech-t2a-websocket.md) | 语音 HD 模型，拥有出色的韵律和稳定性，复刻相似度和音质表现突出 |
| [speech-02-turbo](https://platform.minimaxi.com/docs/guides/speech-t2a-websocket.md) | 语音 Turbo 模型，小语种能力增强，性能表现出色 |

### 图像模型

| 模型名称 | 描述 |
| :- | :- |
| [image-01](https://platform.minimaxi.com/docs/guides/image-generation.md) | 图像生成模型，画面表现细腻，支持文生图、图生图 |
| [image-01-live](https://platform.minimaxi.com/docs/guides/image-generation.md) | 图像生成模型，手绘、卡通等画风增强，支持文生图并进行画风设置 |

## 历史模型

以下模型均已下线。

| 模型名称 | 类型 | 状态 |
| :- | :- | :- |
| MiniMax-M2.7 | 语言模型 | 已下线 |
| MiniMax-M2.7-highspeed | 语言模型 | 已下线 |
| MiniMax-M2.5 | 语言模型 | 已下线 |
| MiniMax-M2.5-highspeed | 语言模型 | 已下线 |
| MiniMax-M2.1 | 语言模型 | 已下线 |
| MiniMax-M2.1-highspeed | 语言模型 | 已下线 |
| MiniMax-M2 | 语言模型 | 已下线 |
| M2-her | 语言模型 | 已下线 |
| music-3.0 | 音乐 | 已下线 |
| music-2.6 | 音乐 | 已下线 |
| music-cover | 音乐 | 已下线 |
| music-3.0-free | 音乐 | 已下线 |
| music-2.6-free | 音乐 | 已下线 |
| music-cover-free | 音乐 | 已下线 |
| Music-2.5+ | 音乐 | 已下线 |
| Music-2.5 | 音乐 | 已下线 |
| Music-2.0 | 音乐 | 已下线 |
