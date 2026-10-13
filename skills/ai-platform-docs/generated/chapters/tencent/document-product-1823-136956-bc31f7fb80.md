<!-- Official source: https://cloud.tencent.com/document/product/1823/136956 -->
<!-- Source SHA-256: 4b9394d165a1fa9b97da95c8da679b37a0eb6fcb917ae8e3ab1f148ae79daa1d -->

# 图片理解

官方来源：https://cloud.tencent.com/document/product/1823/136956
最近更新时间：2026-08-27 11:35:31

## **概述**

图片理解能力，支持对图片内容进行分析，可用于图像描述、目标检测、图文问答、图表数据解读等场景。

## 模型与 API

### 支持的模型

TokenHub 提供多款支持图片理解能力的模型，涵盖专用多模态模型与具备多模态能力的语言模型。完整模型列表及能力说明，请参见 [模型列表](https://cloud.tencent.com/document/product/1823/130051)。

### 支持的 API

平台兼容 OpenAI 的以下两种协议，图片均通过 `image_url` 字段传入（支持公网 URL 或 Base64 编码）：

**OpenAI Chat Completions 协议**（`/v1/chat/completions`）：图片以 `image_url` 类型块传入。详细参数与调用示例，请参见 [OpenAI Chat Completions 协议字段说明](https://cloud.tencent.com/document/product/1823/135872)。

**OpenAI Responses 协议**（`/v1/responses`，OpenAI 原生格式）：图片以 `input_image` 类型块传入，其中图片数据通过 `image_url` 字段指定（支持公网 URL 或 Base64 编码）。仅部分模型支持。详细字段与调用示例，请参见 [OpenAI Response 协议字段说明](https://cloud.tencent.com/document/product/1823/135873)。

## **图片传入方式（URL / Base64）**

图片支持通过 **URL** 或 **Base64** 两种方式传入。在 Chat Completions 协议中，图片数据填入 `image_url` 的 `url` 字段；在 Responses 协议中，图片数据填入 `input_image` 的 `image_url` 字段。两种方式的核心差异如下：

| 维度 | URL 方式 | Base64 方式 |
| --- | --- | --- |
| 适用场景 | 图片已存储于公网可访问位置（如 COS、CDN） | 图片位于本地、内网，或由程序临时生成 |
| 请求体大小 | 极小（仅包含图片 URL） | 约为原文件大小的 1.33 倍 |
| 公网可达要求 | 必须公网可访问 | 无要求 |
| 传输耗时 | 较快（仅发送短 URL），但 TokenHub 需额外下载图片，受图片服务器响应速度影响 | 较慢（请求体约为原图片的 1.33 倍），但无需外部网络访问，适合内网/本地环境 |

### **方式一：图片 URL 传入**

适用于图片已存储在公网可访问位置的场景。

**注意：**

图片 URL 必须为公网可直接访问的地址，私有存储请使用预签名 URL 或改用 Base64 方式。

单张图片大小上限、单次请求图片数量等限制，详见下方 [使用说明](https://cloud.tencent.com/document/product/1823/136956#823eda39-6f9e-45a7-9ab0-b68484c8f750)。

请求结构（Chat Completions 协议）：

```json
{
  "type": "image_url",
  "image_url": {
    "url": "https://example.com/photo.jpg"
  }
}
```

请求结构（Responses 协议）：

```json
{
  "type": "input_image",
  "image_url": "https://example.com/photo.jpg"
}
```

### **方式二：图片 Base64 传入**

适用于图片无法公网访问的场景。将图片读取为二进制后做 Base64 编码，并以 `data:<mime>;base64,<编码>` 的形式填入 `image_url.url`。常见图片 MIME：`image/jpeg`、`image/png`、`image/webp`。

**注意：**

Base64 会使请求体膨胀约 33%，大图建议使用 URL 方式。

单次请求图片数量等限制，详见下方 [使用说明](https://cloud.tencent.com/document/product/1823/136956#823eda39-6f9e-45a7-9ab0-b68484c8f750)。

请求结构（Chat Completions 协议）：

```json
{
  "type": "image_url",
  "image_url": {
    "url": "data:image/jpeg;base64,/9j/4AAQSkZJRgABA..."
  }
}
```

请求结构（Responses 协议）：

```json
{
  "type": "input_image",
  "image_url": "data:image/jpeg;base64,/9j/4AAQSkZJRgABA..."
}
```

## **调用示例**

下面示例均使用 **OpenAI Chat Completions 协议**（`POST /v1/chat/completions`），以 `hy-vision-2.0-instruct` 模型为例。图片通过 `content` 中的 `image_url` 类型块传入，支持单图与多图两种输入。

### 单图输入

cURL（单图 URL）

Python（单图 URL）

Python（单图 Base64）

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/chat/completions' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
    "model": "hy-vision-2.0-instruct",
    "messages": [{"role": "user", "content": [
      {"type": "image_url", "image_url": {"url": "YOUR_IMAGE_URL"}},
      {"type": "text", "text": "请描述这张图片的内容"}
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
    model="hy-vision-2.0-instruct",
    messages=[{
        "role": "user",
        "content": [
            {"type": "image_url", "image_url": {"url": "YOUR_IMAGE_URL"}},
            {"type": "text", "text": "请描述这张图片的内容"},
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

# 请将 example.jpg 替换为您本地图片的路径
with open("example.jpg", "rb") as f:
    base64_image = base64.b64encode(f.read()).decode("utf-8")

response = client.chat.completions.create(
    model="hy-vision-2.0-instruct",
    messages=[{
        "role": "user",
        "content": [
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}},
            {"type": "text", "text": "请描述这张图片的内容"},
        ],
    }],
)

print(response.choices[0].message.content)
```

**响应示例（单图）：**

```json
{
  "id": "57f096ed-219c-487a-8f1c-4f387faa81ca",
  "object": "chat.completion",
  "model": "hy-vision-2.0-instruct",
  "created": 1787628534,
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "这张图片以深邃的蓝绿色为主色调，采用仰视构图，聚焦于水下一个人的后脑与肩背轮廓，上方散布着细密气泡，营造出静谧而沉浸的水下氛围。"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 289,
    "completion_tokens": 51,
    "total_tokens": 340
  }
}
```

### 多图输入

在 `content` 数组中并列多个 `image_url` 块即可实现多图输入。HY-Vision 系列图片数量受上下文窗口约束，无硬性张数上限。

cURL（多图 URL）

Python（多图 URL）

Python（多图 Base64）

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/chat/completions' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
    "model": "hy-vision-2.0-instruct",
    "messages": [{"role": "user", "content": [
      {"type": "image_url", "image_url": {"url": "YOUR_IMAGE_URL"}},
      {"type": "image_url", "image_url": {"url": "YOUR_IMAGE_URL_2"}},
      {"type": "text", "text": "请分别描述这两张图片的内容"}
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
    model="hy-vision-2.0-instruct",
    messages=[{
        "role": "user",
        "content": [
            {"type": "image_url", "image_url": {"url": "YOUR_IMAGE_URL"}},
            {"type": "image_url", "image_url": {"url": "YOUR_IMAGE_URL_2"}},
            {"type": "text", "text": "请分别描述这两张图片的内容"},
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
    # 请将路径替换为您本地图片
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

# 请将 example_a.jpg / example_b.jpg 替换为您本地图片的路径
image_a = load_b64("example_a.jpg")
image_b = load_b64("example_b.jpg")

response = client.chat.completions.create(
    model="hy-vision-2.0-instruct",
    messages=[{
        "role": "user",
        "content": [
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_a}"}},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_b}"}},
            {"type": "text", "text": "请分别描述这两张图片的内容"},
        ],
    }],
)

print(response.choices[0].message.content)
```

**响应示例（多图）：**

```json
{
  "id": "5593d937-3243-4aa3-82bb-ad142dfdb338",
  "object": "chat.completion",
  "model": "hy-vision-2.0-instruct",
  "created": 1787628932,
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "### 第一张图片\\n- 颜色：这张图片由两种纯色组成，上半部分是蓝色（饱和度和亮度较高的正蓝色或艳蓝色），下半部分是红色（饱和度和亮度较高的正红色或艳红色）。\\n- 构图：采用了水平二分构图（上下分割），整个画面被一条水平直线（大致在图像垂直方向的中点位置）分成上下两个相等的矩形区域，上方区域填充蓝色，下方区域填充红色，两种颜色区域的面积大致相等，视觉上呈现出简洁的上下分色效果。\\n\\n\\n### 第二张图片\\n- 颜色：这张图片同样由两种纯色组成，左半部分是绿色（饱和度较高的鲜绿色或草绿色），右半部分是黄色（饱和度较高的亮黄色或柠檬黄）。\\n- 构图：采用了垂直二分构图（左右分割），整个画面被一条垂直直线（大致在图像水平方向的中点位置）分成左右两个相等的矩形区域，左侧区域填充绿色，右侧区域填充黄色，两种颜色区域的面积大致相等，视觉上呈现出简洁的左右分色效果。\\n"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 569,
    "completion_tokens": 231,
    "total_tokens": 800
  }
}
```

**说明：**

调用前请先安装 OpenAI Python SDK：`pip install openai`。

文本与图片可混合：`content` 数组中 `text` 与 `image_url` 的顺序即为模型接收的顺序。

上述单图与多图示例，在 TokenHub 使用 `hy-vision-2.0-instruct` 均可正常返回图片理解结果（单图 `total_tokens` 约 340、多图约 800，详见上方响应示例）。多图 URL 与多图 Base64 两种传入方式返回结构一致，差异仅在图片传入形式。

## **使用说明**

### 支持的图片格式

已验证支持的格式为 **JPEG、PNG、GIF、WEBP** 四种常见图片格式。

如需使用上述四种以外的图片格式，建议在接入前自行实测验证，确认模型可正常解析后再正式使用。

**注意：**

已知 **GLM-5V-Turbo 不支持 GIF** 格式（实测返回 `400 图片输入格式/解析错误`），请勿向该模型传入 GIF 图片。

### 图片数量说明

单次请求可传入的图片数量受限于所选模型的**上下文窗口（Context Window）**。当输入总 Token（文本 + 所有图片 + 输出）超过模型上下文窗口时，信息会被截断或请求被拒绝。

模型上下文窗口请参见 [模型列表](https://cloud.tencent.com/document/product/1823/130051)。

**举例说明（以 16k 上下文窗口为例）：**

当图片分辨率较大（如 1024×1024），每张图片约消耗 **1,058 token**，单次请求可传入的图片数量约为：
`16000 ÷ 1058 ≈ 15 张`

当图片分辨率中等（如 768×768），每张图片约消耗 **602 token**，单次请求可传入的数量约为：
`16000 ÷ 602 ≈ 26 张`

**说明：**

模型回复的质量受输入图片信息量影响。过多的图片会导致模型回复质量下降，请合理控制单次请求传入图片的数量。

以上数量估算以 **HY-Vision（混元视觉）系列模型** 的图片 Token 占用逻辑为参考；第三方视觉模型可能采用不同的图片 Token 算法，并设有各自的图片数量上限，实际可传入数量请以对应模型实测为准。

不同模型对图片数量、大小、格式的具体限制可能随版本更新而变化，接入前建议先进行实测验证。

### 图片文件大小

| 传入方式 | 单张图片大小建议 | 请求体大小限制 |
| --- | --- | --- |
| URL 方式 | 建议不超过 **10 MB** | 不超过 **100 MB** |
| Base64 方式 | 建议不超过 **10 MB** | 不超过 **100 MB**（Base64 编码会使数据体积膨胀约 1.33 倍，多图场景需注意累加） |

**说明：**

TokenHub 对图片上传不施加特殊限制；对视频仅限制单个文件大小不超过 100 MB。因此，图片的尺寸、数量、格式等上限普遍来自模型侧（模型的上下文窗口及其自身约束）。实际可用范围请以所选模型的官方说明及调用返回为准。

第三方视觉模型（Kimi / DeepSeek / MiniMax / GLM / Qwen 等）的具体限制，请参见对应模型调用指南或其官方文档。
