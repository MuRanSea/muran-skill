<!-- Official source: https://cloud.tencent.com/document/product/1823/136957 -->
<!-- Source SHA-256: ba8e3c163d507903c03e40ab981ff6f27e681092117bf924803fb1df387999de -->

# 视频理解

官方来源：https://cloud.tencent.com/document/product/1823/136957
最近更新时间：2026-08-27 11:35:31

## **概述**

视频理解能力，支持对视频内容进行分析，可用于视频结构解析、视频内容审核、动作分析等场景。

## 模型与 API

### 支持的模型

TokenHub 提供多款支持视频理解能力的模型，涵盖专用多模态模型与具备多模态能力的语言模型。完整模型列表及能力说明，请参见 [模型列表](https://cloud.tencent.com/document/product/1823/130051)。

### 支持的 API

平台兼容 **OpenAI Chat Completions 协议**（`/v1/chat/completions`），视频以 `video_url` 类型块传入。详细参数与调用示例，请参见 [OpenAI Chat Completions 协议字段说明](https://cloud.tencent.com/document/product/1823/135872)。

## **视频传入方式（URL / Base64）**

视频支持通过 **URL** 或 **Base64** 两种方式传入，视频数据填入 `video_url` 的 `url` 字段。建议优先使用 URL 方式；各模型对 Base64 的支持情况见下方注意。

**注意：**

建议优先使用 **URL** 方式传入视频。Base64 编码会使视频体积膨胀约 33%，大文件易超出请求体大小上限（请求体大小不得超过 100 MB）。仅在视频无法公网访问时再考虑使用 Base64。

已知**不支持 Base64 传入视频**的模型：HY-Vision-Video（混元）、YT-VITA、GLM-5V-Turbo，请仅使用 URL 方式；其余视觉模型实测支持 Base64，具体以实际调用为准。

视频 URL 必须为公网可直接访问的地址，私有存储请使用预签名 URL。封装 / 编码格式、时长、文件大小、数量等具体限制，详情请参见 [使用说明](https://cloud.tencent.com/document/product/1823/136957#c924d8e4-c3af-473f-8933-ca0c1adf33ff)。

请求结构（URL 方式）：

```json
{
  "type": "video_url",
  "video_url": {
    "url": "https://example.com/video.mp4"
  }
}
```

Base64 方式示例（将视频读取为二进制后做 Base64 编码，以 `data:video/mp4;base64,<编码>` 形式填入 `url`）：

```json
{
  "type": "video_url",
  "video_url": {
    "url": "data:video/mp4;base64,AAAAIGZ0eXB...（省略大量编码内容）"
  }
}
```

## **调用示例**

下面示例均使用 **OpenAI Chat Completions 协议**（`POST /v1/chat/completions`），视频通过 `content` 中的 `video_url` 类型块传入，支持单视频与多视频两种输入。

**说明：**

单视频示例以视频专用模型 **HY-Vision-Video** 演示 URL 传入；由于混元视频模型不支持 Base64，单视频 Base64 与多视频示例改用实测支持 Base64 的 **Kimi K3** 演示。不同模型对 Base64、多视频的支持情况不同，详情请参见 [视频传入方式](https://cloud.tencent.com/document/product/1823/136957#b66501a5-8283-4e16-9587-2351dd49f4e2) 与 [使用说明](https://cloud.tencent.com/document/product/1823/136957#c924d8e4-c3af-473f-8933-ca0c1adf33ff)。

### 单视频输入

#### URL 传入（HY-Vision-Video）

cURL

Python

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/chat/completions' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
    "model": "hunyuan-turbos-vision-video-20250728",
    "messages": [{"role": "user", "content": [
      {"type": "video_url", "video_url": {"url": "https://example.com/video.mp4"}},
      {"type": "text", "text": "请描述视频的内容"}
    ]}],
    "stream": false
  }'
```

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

response = client.chat.completions.create(
    model="hunyuan-turbos-vision-video-20250728",
    messages=[{
        "role": "user",
        "content": [
            {"type": "video_url", "video_url": {"url": "https://example.com/video.mp4"}},
            {"type": "text", "text": "请描述视频的内容"},
        ],
    }],
)

print(response.choices[0].message.content)
```

**响应示例：**

```json
{
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "视频以一个黑暗的、抽象的图像开始，逐渐过渡到一个雪景，一个孤独的身影在雾蒙蒙的山地地形中穿行。场景转移到一个昏暗的室内环境，一个留着胡须的老人和一个红发年轻女子正在进行对话。然后焦点转移到户外，年轻女子在一个破败的城市景观中穿行，遇到了一只巨大的飞行生物。她与这只生物互动，最终骑上它飞越广阔的沙漠景观。视频以一个标题卡结束，上面写着“SINTEL”，接着是另一个标题卡，宣布“即将上映”，"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 3077,
    "completion_tokens": 120,
    "total_tokens": 3197
  }
}
```

#### Base64 传入（Kimi K3）

混元视频模型不支持 Base64，以下改用实测支持 Base64 的 **Kimi K3** 演示。将视频读取为二进制后做 Base64 编码，以 `data:video/mp4;base64,<编码>` 形式填入 `video_url` 的 `url` 字段。

Python

```python
import base64
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

with open("example.mp4", "rb") as f:
    base64_video = base64.b64encode(f.read()).decode("utf-8")

response = client.chat.completions.create(
    model="kimi-k3",
    messages=[{
        "role": "user",
        "content": [
            {"type": "video_url", "video_url": {"url": f"data:video/mp4;base64,{base64_video}"}},
            {"type": "text", "text": "请描述视频的内容"},
        ],
    }],
)

print(response.choices[0].message.content)
```

**响应示例：**

```json
{
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "视频展示了一段动画短片的预告，画面从一个黑暗的抽象场景开始，逐渐过渡到雪景，一个孤独的身影在雾蒙蒙的山地中穿行，随后进入室内对话场景，最终骑乘飞行生物飞越沙漠，并以“SINTEL”标题卡结束。"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 2735,
    "completion_tokens": 80,
    "total_tokens": 2815
  }
}
```

### 多视频输入

在 `content` 数组中并列多个 `video_url` 块即可实现多视频输入，可用于视频对比、多段联合理解等场景。以下以 **Kimi K3** 为例（实测支持多视频）。

**说明：**

已实测支持多视频输入的模型：**Kimi K3**、**Kimi K2.6**、**Kimi K2.7 系列**（Code / Code HighSpeed）、**Qwen3.5-Flash**。

模型解析视频时会将视频采样为若干帧参与推理，多视频会按视频数量**线性叠加 Token 消耗**（约单视频的整数倍），且受模型**上下文窗口**约束。除非有视频对比、多段联合理解等特定需求，**建议优先使用单视频输入**，以节省 Token 并降低超出上下文窗口的风险。

cURL（多视频 URL）

Python（多视频 URL）

Python（多视频 Base64）

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/chat/completions' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
    "model": "kimi-k3",
    "messages": [{"role": "user", "content": [
      {"type": "video_url", "video_url": {"url": "https://example.com/video_a.mp4"}},
      {"type": "video_url", "video_url": {"url": "https://example.com/video_b.mp4"}},
      {"type": "text", "text": "这两个视频内容一样吗？用一句话回答。"}
    ]}],
    "stream": false
  }'
```

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

response = client.chat.completions.create(
    model="kimi-k3",
    messages=[{
        "role": "user",
        "content": [
            {"type": "video_url", "video_url": {"url": "https://example.com/video_a.mp4"}},
            {"type": "video_url", "video_url": {"url": "https://example.com/video_b.mp4"}},
            {"type": "text", "text": "这两个视频内容一样吗？用一句话回答。"},
        ],
    }],
)

print(response.choices[0].message.content)
```

```python
import base64
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

def load_b64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

video_a = load_b64("example_a.mp4")
video_b = load_b64("example_b.mp4")

response = client.chat.completions.create(
    model="kimi-k3",
    messages=[{
        "role": "user",
        "content": [
            {"type": "video_url", "video_url": {"url": f"data:video/mp4;base64,{video_a}"}},
            {"type": "video_url", "video_url": {"url": f"data:video/mp4;base64,{video_b}"}},
            {"type": "text", "text": "这两个视频内容一样吗？用一句话回答。"},
        ],
    }],
)

print(response.choices[0].message.content)
```

**响应示例（多视频 URL）：**

```json
{
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "是的，这两个视频内容完全一样，都是Blender Foundation出品的动画短片《Sintel》的预告片，画面、场景和时间戳均相同。"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 87121,
    "completion_tokens": 95,
    "total_tokens": 87216
  }
}
```

**说明：**

已实测：上述单视频与多视频示例在 TokenHub 均可正常返回视频理解结果。多视频 URL 与 Base64 两种传入方式返回结构一致，差异仅在视频传入形式。

示例中真实返回均已脱敏；多视频示例使用两个相同视频验证“内容是否一致”的判断能力，实际应用中可替换为需对比的不同视频。

## **使用说明**

### 支持的视频格式

已验证兼容性最佳、推荐优先使用的格式为 **MP4（H.264 / H.265 编码）、MOV、AVI** 等主流封装；部分厂商视觉模型同时支持 MKV、WebM 等更多常见封装，具体支持的格式范围因模型而异。

如需使用上述常见格式以外的视频，建议在接入前自行实测验证，确认模型可正常解析后再正式使用。

### 视频数量说明

单次请求可传入的视频数量受限于所选模型的**上下文窗口（Context Window）**。视频会被采样为若干帧参与推理，当输入总 Token（视频帧 + 文本 + 输出）超过模型上下文窗口时，信息会被截断或请求被拒绝。

模型上下文窗口请参见 [模型列表](https://cloud.tencent.com/document/product/1823/130051)。

**数量说明：**

当前视觉模型普遍为**单次请求传入 1 个视频**；已实测支持多视频输入的模型：**Kimi K3、Kimi K2.6、Kimi K2.7 系列、Qwen3.5-Flash**，可用于视频对比、多段联合理解等场景。

**说明**

模型对视频的理解质量受输入视频信息量影响，过多的视频会导致理解质量下降，请合理控制单次请求传入视频的数量。视频理解对上下文的占用与视频时长、分辨率、采样帧数等相关，不同模型算法差异较大。

第三方视觉模型可能采用不同的视频 Token 算法，并设有各自的视频数量 / 时长上限，实际可传入数量请以对应模型实测为准。

不同模型对视频数量、大小、格式、时长的具体限制可能随版本更新而变化，接入前建议先进行实测验证。

### 视频文件大小

**TokenHub 平台侧限制**：无论是通过 URL 方式还是 Base64 方式传入视频，TokenHub 对单个视频文件的大小均限制不超过 **100 MB**，单次请求的请求体总大小同样不超过 **100 MB**。使用 Base64 编码时，数据体积会膨胀约 33%，多视频场景下需注意累加后不超过请求体上限。TokenHub 对图片上传不施加特殊限制；对视频仅限制单个文件大小不超过 **100 MB**。因此，视频的尺寸、数量、格式、时长等上限普遍来自**模型侧**（模型的上下文窗口及其自身约束）。实际可用范围请以所选模型的官方说明及调用返回为准。

**三方模型限制**：三方视觉模型（Kimi / DeepSeek / MiniMax / GLM / Qwen 等）对视频大小、时长的具体限制各不相同：多数模型对单视频大小设有明确上限（常见为数十 MB 量级，部分通过文件上传接口可放宽至数百 MB）；对视频时长也常有限制（从数十秒到数十分钟、乃至更长不等）。Base64 方式通常受单条数据大小约束，可用上限一般低于 URL / 文件上传方式。请参见对应模型调用指南或其官方文档，并以实际调用返回为准。
