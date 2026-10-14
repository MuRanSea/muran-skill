<!-- Official source: https://cloud.tencent.com/document/product/1823/135746 -->
<!-- Source SHA-256: 18de3381d74e0e6e2e102646e3d8782bebb0d6a15c162c2f51679996de5c0a48 -->

# Vidu 生图调用指南

官方来源：https://cloud.tencent.com/document/product/1823/135746
最近更新时间：2026-10-12 12:50:00

## 概述

Vidu 是生数科技推出的多模态生成模型系列。本文介绍如何通过 TokenHub 调用 Vidu 图片生成模型 Vidu-Image-q2（`vidu-image-q2`），支持**参考生图、文生图与图片编辑**：以 0~7 张参考图结合文本提示词生成图片，也可仅凭文本进行文生图。

### 前提条件

已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号并开通 TokenHub 服务。

已在 [TokenHub 控制台](https://console.cloud.tencent.com/tokenhub/apikey) 获取 API Key。

**说明：**

下文所有示例中的 YOUR\_API\_KEY 均需替换为您自己的 API Key，鉴权方式为请求头 Authorization: Bearer YOUR\_API\_KEY。

### 调用流程

图片生成为耗时任务，接口采用**异步调用**模式，统一分两步：

1. **提交任务**：调用图片生成接口，成功返回 `task_id` 与初始状态 `created`。

2. **轮询结果**：携带 `task_id` 调用「查询任务结果」接口，直至 `state = success`，从结果中获取图片地址。也可通过 `callback_url` 配置回调，任务状态变更时由服务端主动推送。

**注意：**

任务状态：created（创建成功）/ queueing（排队中）/ processing（处理中）/ success（成功）/ failed（失败）。

所有接口响应均包含 `request_id`（顶层，用于排查问题）；查询接口额外返回 `usage`（用量消耗）。

### 模型列表

| 模型名称 | model 参数值 | 支持能力 | 提示词上限 | 分辨率 | 画面宽高比 |
| --- | --- | --- | --- | --- | --- |
| Vidu-Image-q2 | `vidu-image-q2` | 参考生图 / 文生图 / 图片编辑 | 2000 字符 | 1080p / 2K / 4K | 16:9、9:16、1:1、3:4、4:3、21:9、2:3、3:2、auto |

## 图片生成

### 1. 接口描述

Vidu 图片生成（参考生图 / reference-to-image）接口。支持参考生图、文生图与图片编辑：以 0~7 张参考图 + 文本提示词生成图片，未传图片时按文本进行文生图。

**接口：** `POST https://tokenhub.tencentmaas.com/v1/wand/vidu-image/generation`

### 2. 输入参数

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| model | 是 | string | 模型 ID。取值：`vidu-image-q2` |
| prompt | 是 | string | 文本提示词，长度 ≤ 2000 字符。未传 images 时按此文本进行文生图。 |
| images | 否 | array[string] | 图片 images：支持 0张-7张图片输入， 支持 URL 和Base64格式。  图片格式：png/jpeg/jpg/webp，像素≥128×128，比例<1：4或4：1；  1. Base64：所有图片大小和<=15MB，转为 Base64大小和<=20MB; 格式要求：data:image/<图片格式>;base64,<Base64 编码>；注：图片为 jpg 时图片格式填 jpeg。  2. URL：单个文件大小<=50MB；需要公网可访问（http/https）。 |
| aspect\_ratio | 否 | string | 画面宽高比。可选：16:9 / 9:16 / 1:1 / 3:4 / 4:3 / 21:9 / 2:3 / 3:2 / auto（与首张输入图比例一致）。默认值：16:9。 |
| resolution | 否 | string | 分辨率。可选：1080p / 2K / 4K。默认值：1080p。 |
| seed | 否 | integer | 随机种子。不传或传 0 时使用随机数。 |
| callback\_url | 否 | string | 任务状态变化回调地址（POST）。回调体与查询任务返回体一致，采用回调签名算法认证。 |

### 3. 请求示例

**参考生图**

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/vidu-image/generation' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "vidu-image-q2",
  "images": ["https://example.com/reference.jpg"],
  "prompt": "a cat sitting on a windowsill at sunset",
  "aspect_ratio": "16:9",
  "resolution": "2K"
}'
```

**文生图（不传 images）**

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/vidu-image/generation' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "vidu-image-q2",
  "prompt": "a cat sitting on a windowsill at sunset",
  "aspect_ratio": "16:9",
  "resolution": "1080p"
}'
```

### 4. 输出参数

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| task\_id | string | Vidu 生成的任务 ID，用于后续查询任务与回调匹配。 |
| state | string | 处理状态：created / queueing / processing / success / failed。 |
| prompt | string | 本次调用的提示词参数。 |
| created\_at | string | 任务创建时间（ISO 8601）。 |
| request\_id | string | 唯一请求标识，用于排查问题。 |

### 5. 响应示例

```json
{
    "task_id": "1374200352-WandImage-a457a7b042694f8aad4deeff8c7f7ef3",
    "state": "created",
    "prompt": "a cat sitting on a windowsill at sunset",
    "created_at": "2026-08-20T07:31:07.277Z",
    "request_id": "26eb0d62-1c52-4f3a-9b5e-7e8fb2524d8f"
}
```

### 6. 错误码

请求失败时返回错误码，具体见 `ErrMsg`/错误信息。常见错误码请参见 [附录：统一错误码](https://cloud.tencent.com/document/product/1823/135746#.E7.BB.9F.E4.B8.80.E9.94.99.E8.AF.AF.E7.A0.81)。

## 查询任务结果

### 1. 接口描述

查询图片生成任务的状态与结果。提交任务返回 `task_id` 后，通过本接口轮询获取结果。

**接口：** `GET https://tokenhub.tencentmaas.com/v1/wand/vidu-image/tasks/{task_id}`

**说明：**

路径中的 `{task_id}` 即提交任务时返回的 `task_id`（示例中以 `YOUR_TASK_ID` 占位）。图片生成约需数秒至数十秒，建议每 3~5 秒轮询一次。

### 2. 输入参数

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| task\_id | 是 | string | 任务 ID（路径参数），即提交任务时返回的 `task_id`。 |

### 3. 请求示例

```bash
curl -X GET 'https://tokenhub.tencentmaas.com/v1/wand/vidu-image/tasks/YOUR_TASK_ID' \\
  -H 'Authorization: Bearer YOUR_API_KEY'
```

### 4. 输出参数

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| state | string | 处理状态：created / queueing / processing / success / failed。 |
| model | string | 本次调用的模型名称。 |
| aspect\_ratio | string | 本次调用的比例参数。 |
| resolution | string | 本次调用的分辨率参数。 |
| creations | array[object] | 生成结果列表（成功时返回）。 |
| creations[].url | string | 生成图片的下载地址，为临时地址，有效期 12 小时，请及时下载转存。 |
| request\_id | string | 唯一请求标识，用于排查问题。 |
| tokenhub\_usage | object | 用量消耗。 |
| tokenhub\_usage.total\_tokens | integer | 本次任务消耗的 token 数，用于计费/对账。 |

### 5. 响应示例

**生成成功：**

```json
{
  "state": "success",
  "model": "vidu-image-q2",
  "prompt": "a cat sitting on a windowsill at sunset",
  "creations": [
    { "url": "https://aigc-image.cos.myqcloud.com/xxx/result.png" }
  ],
  "aspect_ratio": "16:9",
  "resolution": "2K",
  "request_id": "3aec3299-06ad-4654-8b45-c57b823a15d2",
  "tokenhub_usage": { "total_tokens": 1024 }
}
```

### 6. 错误码

| state | 含义 | 处理建议 |
| --- | --- | --- |
| success | 生成成功 | 从 `creations[].url` 获取结果图片。 |
| processing / queueing | 处理中 / 排队中 | 每 3~5 秒轮询一次，直至 success。 |
| failed | 生成失败 | 查看失败原因，修改后重试；持续失败请联系技术支持并附 request\_id。 |

请求级错误码请参见 [附录：统一错误码](https://cloud.tencent.com/document/product/1823/135746#.E7.BB.9F.E4.B8.80.E9.94.99.E8.AF.AF.E7.A0.81)。

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

格式 png / jpeg / jpg / webp；像素 ≥ 128×128；比例须小于 1:4 或 4:1；单图 ≤ 50MB；POST body ≤ 20MB；支持图片 URL 或 Base64（Base64 须带 `data:image/png;base64,` 前缀）。

## 常见问题

#### **1. 文生图和参考生图怎么区分？**

同一接口：传 `images` 即为参考生图（以图中主体为参考）；不传 `images` 即为文生图（仅凭 prompt 生成）。`vidu-image-q2` 两种模式都支持。

#### **2. 生成结果图片链接会过期吗？**

会过期。生成结果为临时地址，有效期 12 小时，请在任务成功后及时下载 `creations[].url` 中的图片并转存到自有存储，不要长期依赖该链接。

#### **3. auto 宽高比是什么？**

`aspect_ratio: auto` 表示输出比例与首张输入图保持一致，仅在参考生图模式下有意义。
