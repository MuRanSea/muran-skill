<!-- Official source: https://cloud.tencent.com/document/product/1823/140911 -->
<!-- Source SHA-256: 161ce74f7ef95a6fa28b8fdced4d1b09f3191d508d7b79f75902ee29153c7cc3 -->

# Minimax 生图调用指南

官方来源：https://cloud.tencent.com/document/product/1823/140911
最近更新时间：2026-11-13 20:08:30

## 概述

MiniMax H3-Image 是 MiniMax 推出的图像生成模型系列。本文介绍如何通过 TokenHub 调用 MiniMax 图像生成模型（`minimax-image-h3` / `minimax-image-h3-highspeed`）：以 OpenAI Images 风格的协议提交文生图或图片编辑请求，同步返回图片结果，支持文本描述生图、多图参考编辑、自定义尺寸/宽高比、输出格式控制等能力。

**说明：**

本接口为**同步调用**：一次请求直接返回生成结果，无需提交任务与轮询。服务端会在内部完成异步推理并等到终态，最后把原厂最终图像原样返回给调用方。

### 前提条件

已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号并开通 TokenHub 服务。

已在 [TokenHub 控制台](https://console.cloud.tencent.com/tokenhub/apikey) 获取 API Key。

在 [控制台-在线推理-视觉模型](https://console.cloud.tencent.com/tokenhub/inference?regionId=1&serviceType=VISION) 处开启对应模型的后付费。

**说明：**

下文所有示例中的 YOUR\_API\_KEY 均需替换为您自己的 API Key，鉴权方式为请求头 Authorization: Bearer YOUR\_API\_KEY。

### 模型列表

| 模型名称 | model 参数值 | 支持能力 | 简要说明 |
| --- | --- | --- | --- |
| MiniMax H3-Image | `minimax-image-h3` | 文生图 / 图片编辑（同步） | 标准质量，支持文本生图与多图参考编辑，综合效果均衡。 |
| MiniMax H3-Image Highspeed | `minimax-image-h3-highspeed` | 文生图 / 图片编辑（同步） | 高速版本，生成速度更快，适合对延迟敏感的场景。 |

## 文生图

### 1. 接口描述

以文本 prompt 描述目标图像，同步生成图片。支持指定输出尺寸、宽高比、输出格式等参数。

**接口：** `POST https://tokenhub.tencentmaas.com/v1/wand/minimax-image/generation`

### 2. 输入参数

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| `model` | 是 | string | 模型 ID，取值 `minimax-image-h3` 或 `minimax-image-h3-highspeed`，**不可为空**。 |
| `prompt` | 否 | string | 图片的文本描述，最长 32000 个字符（按 Unicode 字符计，不含首尾空白），为空或只含空白时返回 400。关闭 Prompt 增强（disable\_prompt\_enhanced 为 true）时，模型只读取约前 4096 个 token，超出部分不生效。 |
| `n` | 否 | integer | 生成图片数量，取值范围 [1,10]，默认 1。 |
| `size` | 否 | string | 生成尺寸，格式 `${宽}x${高}`（如 `2720x1536`）。宽、高为正整数。面积（宽 × 高）在 655,360 ~ 20,000,000 像素之间，宽高比在 1:3 ~ 3:1 之间，均含边界；不满足时返回 400，不会自动缩放或取整。此时不能再传 aspect\_ratio 或 area，不传时由模型自主决定尺寸。也可传 `"auto"` 让模型根据 prompt 语义自动选择最优尺寸。 |
| `aspect_ratio` | 否 | string | 输出宽高比，默认 auto。只能在 size 不传或为 auto 时传入。auto：由 Prompt 增强结合参考图与内容决定 X:Y：X、Y 为 1 ~ 300 的整数，宽高比在 1:3 ~ 3:1 之间（含边界），如 16:9、3:4、21:9、3:1. |
| `area` | 否 | string | 输出面积档位，支持1K, 2K, 4K ,默认 4K。只能在 size 不传或为 auto 时传入，size 为 宽 x 高 时传入返回 400。1K、2K、4K 的目标面积分别为 1024 × 1024、2048 × 2048、4096 × 4096 像素，宽高由服务端按宽高比计算，如 2K 搭配 16:9 输出 2720 × 1536。每张的实际宽高见 data[].size。 |
| `output_format` | 否 | string | 输出图片格式，支持 `"jpeg"`、`"png"`、`"webp"`，默认 `"jpeg"`。 |
| `response_format` | 否 | string | 图片返回形式，支持 `"url"`（返回图片 URL，默认）和 `"b64_json"`（返回 base64 编码）。 |
| `output_compression` | 否 | integer | 输出图片压缩质量，范围 `[0, 100]`，默认95，值越大质量越高，仅对 `jpeg`/`webp` 格式有效。 |
| `aigc_watermark` | 否 | boolean | 是否为生成图叠加 AIGC 可见水印。`false`：不加水印（默认）；`true`：加水印。 |
| `disable_prompt_enhanced` | 否 | boolean | 是否关闭 Prompt 增强（模型侧自动优化 prompt）。`false`：开启增强（默认）；`true`：关闭增强，严格按原始 prompt 生图。 |

### 3. 请求示例

**文生图（基础）：**

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/minimax-image/generation' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "minimax-image-h3",
  "prompt": "一只橘猫趴在窗台上晒太阳，背景是模糊的城市街景，暖色调，写实风格"
}'
```

**文生图（指定尺寸与格式）：**

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/minimax-image/generation' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "minimax-image-h3",
  "prompt": "赛博朋克风格的城市夜景，霓虹灯倒映在雨后的街道上",
  "size": "2720x1536",
  "output_format": "jpeg",
  "response_format": "url"
}'
```

**文生图（高速版，指定宽高比）：**

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/minimax-image/generation' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "minimax-image-h3-highspeed",
  "prompt": "极简风格的产品海报，白色背景，中央放置一瓶香水",
  "aspect_ratio": "9:16",
  "output_format": "png"
}'
```

## 图片编辑

### 1. 接口描述

以文本 prompt 描述编辑意图，并提供一张或多张参考图，同步生成编辑后的图片。支持换背景、换风格、局部修改、多图融合等场景。

**接口：** `POST https://tokenhub.tencentmaas.com/v1/wand/minimax-image/edits`

### 2. 输入参数

在文生图参数基础上，额外支持以下参数：

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| `images` | 否 | array[object] | 参考图列表，1～16张，每个元素结构为 `{"image_url": "..."}` 或 `{"url": "..."}`（两种字段名均兼容）。支持 http(s) 公网 URL 或 `data:image/...;base64,...` 形态。多图场景下模型会综合所有参考图进行编辑。 |

其余参数（`model`、`prompt`、`n`、`size`、`aspect_ratio`、`output_format` 等）与文生图接口完全一致，请参考上方参数表。

### 3. 请求示例

**单图参考编辑：**

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/minimax-image/edits' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "minimax-image-h3",
  "prompt": "保持人物不变，将背景替换为日落时分的海滩",
  "images": [
    {"image_url": "https://your-domain/portrait.jpg"}
  ],
  "response_format": "url"
}'
```

## 输出参数

文生图与图片编辑接口的响应结构相同，均为原厂 MiniMax 原始回包直接透传。

| 参数名 | 类型 | 描述 |
| --- | --- | --- |
| `created` | integer | Unix 秒级时间戳。 |
| `data` | array | 生成结果列表，每个元素包含 `url`（图片 URL，当 `response_format=url` 时）或 `b64_json`（base64 编码，当 `response_format=b64_json` 时）。 |
| `tokenhub_usage` | object | 本次任务消耗的 token 数，用于计费/对账。 |
| `request_id` | string | 请求 id, 排查问题时请携带 request\_id。 |

## 响应示例

**成功响应：**

```json
{
    "created": 1794385455,
    "data": [
        {
            "revised_prompt": "The image is a realistic ......",
            "size": "3552x4736",
            "url": "https://xxx.png"
        }
    ],
    "output_format": "jpeg",
    "request_id": "6e44b701-e024-426a-bb00-839553cb58c9",
    "tokenhub_usage": {
        "total_tokens": 44547
    }
}
```

## 常见问题

#### **生成结果图片链接会过期吗？**

会过期。生成结果为临时地址，请在生成成功后及时下载保存。
