<!-- Official source: https://cloud.tencent.com/document/product/1823/136609 -->
<!-- Source SHA-256: 89a9732fcdafa28b759d8aff5ed73d92ae857dfd0281c7fdf623586c61a790a8 -->

# Seedream 生图调用指南

官方来源：https://cloud.tencent.com/document/product/1823/136609
最近更新时间：2026-09-15 18:00:59

## 概述

Seedream 是火山引擎推出的图片生成模型系列。本文介绍如何通过 TokenHub 调用 Seedream 图片生成模型 Seedream-Image-v5.0-pro（`seedream-image-v5.0-pro`）、Seedream-Image-v5.0-lite（`seedream-image-v5.0-lite`），支持**文生图、参考生图**，以参考图结合文本提示词生成图片，也可仅凭文本进行文生图。

### 前提条件

已在 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 注册账号并开通 TokenHub 服务。

已在 [TokenHub 控制台](https://console.cloud.tencent.com/tokenhub/apikey) 获取 API Key。

**说明：**

下文所有示例中的 YOUR\_API\_KEY 均需替换为您自己的 API Key，鉴权方式为请求头 Authorization: Bearer YOUR\_API\_KEY。

### 模型列表

<table><colgroup><col/><col/><col/><col/><col/></colgroup><tbody><tr><td><div>模型名称</div></td><td><div>model 参数值</div></td><td><div>支持能力</div></td><td><div>提示词上限</div></td><td><div>分辨率</div></td></tr><tr><td><div>Seedream-Image-v5.0-pro</div></td><td><div><code>seedream-image-v5.0-pro</code></div></td><td><div>参考生图 / 文生图</div></td><td><div>600字符</div></td><td><div>1K / 1.5K / 2K</div></td></tr><tr><td><div>Seedream-Image-v5.0-lite</div></td><td><div><code>seedream-image-v5.0-lite</code></div></td><td><div>参考生图 / 文生图</div></td><td><div>600字符</div></td><td colspan="1" rowspan="1"><div>2K / 3K / 4K</div></td></tr></tbody></table>

## 图片生成

### 1. 接口描述

Seedream 图片生成（参考生图 / reference-to-image）接口。支持参考生图、文生图与图片编辑：以参考图 + 文本提示词生成图片，未传图片时按文本进行文生图。

**接口：** `POST https://tokenhub.tencentmaas.com/v1/wand/si-image/generation`

### 2. 输入参数

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| model | 是 | string | 模型 ID。取值：`seedream-image-v5.0-pro、seedream-image-v5.0-lite` |
| prompt | 是 | string | 文本提示词，长度 ≤ 600 字符。未传 images 时按此文本进行文生图。  提示词字数建议：中文提示词不超过 300 字，英文提示词不超过 600 词。字数过多信息容易分散，模型可能因此忽略细节，只关注重点，造成图片缺失部分元素。 |
| images | 否 | array[string] | 参考图片 `seedream-image-v5.0-pro` 支持最多10张，`seedream-image-v5.0-lite` 支持最多14张。  输入的图片信息，支持 URL 或 Base64 编码，单张图片最大30MB。  图片 URL：请确保图片 URL 可被访问。  Base64 编码：请遵循此格式 data:image/<图片格式>;base64,<Base64 编码>。注意 <图片格式> 需小写，如 data:image/png;base64,<base64\_image>。 |
| layer\_decomposition | 否 | boolean | 图层拆分开关，控制是否开启图层拆分功能。  图层拆分会将单张图片的主体、背景、文字等内容自动拆解为1张底图和最多16个可独立编辑的图层。每个图层为带透明通道的 PNG 图片。  模型支持 ：  `seedream-image-v5.0-pro` |
| size | 否 | string | 图像尺寸。  `seedream-image-v5.0-pro`（图片生成场景）  支持以下两种方式，不可混用：  **方式 1（推荐）**：指定分辨率档位，并在 prompt 中用自然语言描述图片宽高比、图片形状或图片用途，最终由模型判断生成图片的大小。  默认值：2K  可选值：1K、1.5K、2K  **方式 2**：指定宽高像素值（宽 x 高）。  总像素取值范围：[1280x720（921600）, 2048x2048x1.1025（4624220）]  宽高比取值范围：[1/16, 16]    `seedream-image-v5.0-pro`（图层拆分场景）  仅支持通过指定分辨率档位的方式设置。输出图的分辨率规则如下：  底图 ：输出底图的分辨率和 size 指定的分辨率一致；输出底图和原待拆分图的宽高比一致。  各图层 ：输出图层的分辨率和 size 指定的分辨率接近；每个输出图层和其在原图中的宽高比一致。  size 的默认值与可选值：  默认值：auto  可选值：1K、1.5K、2K、auto（根据输入图的尺寸和宽高比进行输出）    `seedream-image-v5.0-lite`  支持以下两种方式，不可混用：  方式1：指定分辨率，并在 prompt 中用自然语言描述图片宽高比、图片形状或图片用途，最终由模型判断生成图片的大小。  可选值：2K、3K、4K  方式2：指定生成图像的宽高像素值。  默认值：2048x2048  总像素取值范围：[2560x1440（3686400）, 4096x4096（16777216）]  宽高比取值范围：[1/16, 16] |
| optimize\_prompt\_options | 否 | object | 提示词优化配置。 |
| optimize\_prompt\_options.mode | 否 | string | 优化模式。  standard：标准模式，生成内容的质量更高，耗时较长。  fast：快速模式，生成内容的耗时更短，效果略低于标准模式；`seedream-image-v5.0-lite` 当前不支持。 |
| output\_format | 否 | string | 图像格式。  指定生成图像的文件格式。可选值：  png  jpeg |
| background | 否 | string | 图片透明通道。  用于控制是否生成带透明通道的图片。可选值：  transparent：透明背景模式，输出带有透明背景的图。  opaque：不透明背景模式，生成常规的实体背景图。  模型支持 ：  `seedream-image-v5.0-pro` |
| response\_format | 否 | string | 返回格式。  指定生成图像的返回格式。支持以下两种返回方式：  url：返回图片下载链接，链接在图片生成后12小时内有效，请及时下载图片。  b64\_json：以 Base64 编码字符串的 JSON 格式返回图像数据。 |
| sequential\_image\_generation | 否 | string | 组图模式。  控制是否关闭组图功能（组图：基于您输入的内容，生成的一组内容关联的图片）。  auto：自动判断模式，模型会根据用户提供的提示词自主判断是否返回组图以及组图包含的图片数量。  disabled：关闭组图功能，模型只会生成一张图。  模型支持：  `seedream-image-v5.0-lite` |
| sequential\_image\_generation\_options | 否 | object | 组图配置。  组图功能的配置。仅当 sequential\_image\_generation 为 auto 时生效。  模型支持：  `seedream-image-v5.0-lite` |
| sequential\_image\_generation\_options.max\_images | 否 | integer | 最大生成数量。  指定本次请求，最多可生成的图片数量。取值范围：[1, 15] |
| tools | 否 | object | 工具配置。  模型支持：  `seedream-image-v5.0-lite` |
| tools.type | 否 | string | 工具类型。指定使用的工具类型。  web\_search：联网搜索功能。 |
| watermark | 否 | boolean | 水印开关。  是否在生成的图片中添加水印。  false：不添加水印。  true：在图片右下角添加“AI 生成”字样的水印标识。 |

### 3. 请求示例

**参考生图**

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/si-image/generation' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "seedream-image-v5.0-pro",
  "images": ["https://example.com/reference.jpg"],
  "prompt": "a cat sitting on a windowsill at sunset",
  "size": "2048x2048"
}'
```

**文生图（不传 images）**

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/si-image/generation' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "seedream-image-v5.0-pro",
  "prompt": "a cat sitting on a windowsill at sunset",
  "size": "2048x2048"
}'
```

### 4. 输出参数

<table><colgroup><col/><col/><col/></colgroup><tbody><tr><td><div>字段</div></td><td><div>类型</div></td><td><div>说明</div></td></tr><tr><td><div>created_at</div></td><td><div>string</div></td><td><div>任务创建时间。</div></td></tr><tr><td><div>data</div></td><td><div>object</div></td><td><div>返回图片内容。</div></td></tr><tr><td><div>data[].output_format</div></td><td><div>string</div></td><td><div>输出格式。</div></td></tr><tr><td><div>data[].size</div></td><td><div>string</div></td><td><div>图像尺寸。</div></td></tr><tr><td><div>data[].url</div></td><td><div>string</div></td><td><div>图片 URL。</div></td></tr><tr><td><div>data[].b64_json</div></td><td><div>string</div></td><td><div>图片 Base64 数据。</div></td></tr><tr><td><div>request_id</div></td><td><div>string</div></td><td><div>唯一请求标识，用于排查问题。</div></td></tr><tr><td><div>model</div></td><td><div>string</div></td><td><div>使用的生图模型。</div></td></tr><tr><td colspan="1" rowspan="1"><div>tokenhub_usage</div></td><td colspan="1" rowspan="1"><div>object</div></td><td colspan="1" rowspan="1"><div>用量消耗。</div></td></tr><tr><td colspan="1" rowspan="1"><div>tokenhub_usage.total_tokens</div></td><td colspan="1" rowspan="1"><div>integer</div></td><td colspan="1" rowspan="1"><div>本次任务消耗的 token 数，用于计费/对账。</div></td></tr></tbody></table>

### 5. 响应示例

```json
{
    "created": 1787309367,
    "data": [
        {
            "output_format": "jpeg",
            "size": "2048x2048",
            "url": "https://xxxxxxx.jpg"
        }
    ],
    "model": "doubao-seedream-5-0-pro-260628",
    "tokenhub_usage": {
        "total_tokens": 60000
    },
    "request_id": "f781d9dc-9792-43d8-82f3-90de51a1ff44"
}
```

## 附录

### 统一错误码

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| BadRequest | bad request | 不合法的请求 |
| FieldLacking | field is missing or empty | 缺少必填字段 |
| FieldUnwanted | unwanted field | 传入了不需要的字段 |
| FieldInvalid | invalid field | 传入参数未通过合法性校验 |
| FieldItemCountOutOfRange | field item count out of range | 字段项数超限（如图片数量超限） |
| PageSizeOutOfRange | page size out of range | 图像尺寸/参数超限 |
| ImageFormatInvalid | invalid image format | 图像格式不符合要求 |
| ImageSizeInvalid | image size invalid | 图片尺寸过大或过小 |
| ImageDownloadFailure | image download failure | 下载图片 URL 失败，请检查链接 |
| TaskPromptPolicyViolation | prompt policy violation | Prompt 触发安审风控 |
| CreationPolicyViolation | creation policy violation | 生成物触发风控 |
| AuditSubmitIllegal | submit is illegal | 输入未通过安全审核 |
| CreditInsufficient | insufficient credits | 积分不足 |
| ModelUnavailable | model unavailable | 模型不可用 |
| Unauthorized | unauthorized | 未鉴权（检查 Authorization） |
| Forbidden | forbidden | 请求没有权限 |
| TaskNotFound | task not found | task\_id 未找到 |
| QuotaExceeded | quota exceeded | 超过并发限制 |
| TooManyRequests | too many requests | 请求太频繁 |
| InternalServiceFailure | internal service failure | 服务器内部错误 |

### 图片素材通用约束

参考图片 `seedream-image-v5.0-pro` 支持最多10 张，`seedream-image-v5.0-lite` 支持最多14 张；支持图片 URL 或 Base64（须带 `data:image/png;base64,` 前缀）；格式支持 jpeg/png/webp/bmp/tiff/gif/heic/heif，像素最小 14 x 14，总像素不大于3600万，比例须小于 1:16 或 16:1，单图 ≤ 30MB，POST body ≤ 20MB。

## 常见问题

#### **1. 文生图和参考生图怎么区分？**

同一接口：传 `image` 即为参考生图（以图中主体为参考）；不传 `images` 即为文生图（仅凭 prompt 生成）。`seedream-image-v5.0-pro` 两种模式都支持。

#### **2. 生成结果图片链接会过期吗？**

会过期。生成结果为临时地址，有效期 12 小时，请在任务成功后及时下载。
