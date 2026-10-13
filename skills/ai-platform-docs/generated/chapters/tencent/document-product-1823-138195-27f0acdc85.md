<!-- Official source: https://cloud.tencent.com/document/product/1823/138195 -->
<!-- Source SHA-256: 5d2b4851dfee511713cf8e99a54b52cdb52caf86209e5d3e16ad9533ef2b2de8 -->

# WAND 生视频调用指南

官方来源：https://cloud.tencent.com/document/product/1823/138195
最近更新时间：2026-09-17 16:47:00

## 概述

[Tencent Cloud WAND（腾讯云音视频 AI）](https://cloud.tencent.com/product/wand)是腾讯云面向音视频场景打造的 AI 能力品牌。音视频场景复杂多样，通用 AI 难以直接发挥效果；WAND 依托腾讯云多年音视频技术积累与海量业务实践，将多模态大模型与音视频工程经验深度结合，提供经真实场景验证的 AI 原子能力。**WAND-Vega-Video** 是**高性价比多模态视频生成**模型，支持文生视频、首尾帧生视频、参考生视频，兼顾成本与质量。

### 前提条件

已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号并开通 TokenHub 服务。

已在 [TokenHub 控制台](https://console.cloud.tencent.com/tokenhub/apikey) 获取 API Key。

**说明：**

下文所有示例中的 YOUR\_API\_KEY 均需替换为您自己的 API Key，鉴权方式为请求头 Authorization: Bearer YOUR\_API\_KEY。

### **调用流程**

视频生成为耗时任务（通常 1~3 分钟），接口采用**异步调用**模式，统一分两步：

1. **提交任务**：调用 `POST /v1/wand/vega-videos/tasks`，成功返回 `id` 与 `status=queued`。

2. **轮询结果**：携带 `id` 调用 `GET /v1/wand/vega-videos/tasks/{id}`，直至 `status` 为 `succeeded` 或 `failed`，成功后从 `content.video_url` 获取视频地址。

### 模型列表

| **模型名称** | **model 参数值** | **支持能力** | **视频时长（秒）** | **清晰度档位** |
| --- | --- | --- | --- | --- |
| WAND-Vega-Video-1.0-Lite | wand-vega-video-1.0-lite | 文生 / 首尾帧生 / 参考生 | 4 ~ 15 | 768P、1080P、2K、4K |

## 视频生成

### 1. 接口描述

提交一个视频生成任务。三种生成形态（文生、首尾帧生、参考生）共用本接口，通过 `content` 数组中元素的 `type` 与 `role` 组合区分。

**接口：**`POST https://tokenhub.tencentmaas.com/v1/wand/vega-videos/tasks`

### 2. 输入参数

| **参数名** | **必选** | **类型** | **描述** |
| --- | --- | --- | --- |
| model | 是 | string | 模型名称。取值：  wand-vega-video-1.0-lite |
| content | 是 | array[object] | 多模态输入数组。必须包含至少 1 个 type=text 元素（生成需要文本提示词）。详细见下方 **content 数组元素参数**。 |
| resolution | 否 | string | 视频分辨率。  Lite 取值：768P、1080P、2K、4K |
| ratio | 否 | string | 画面宽高比。  取值：21:9、16:9、4:3、1:1、3:4、9:16、adaptive（默认）。  其中 adaptive 表示由模型或输入素材自动决定。 |
| duration | 否 | integer | 视频时长（秒）。  取值：4 ~ 15 的整数，默认 5。 |
| options | 否 | object | 高级 / 扩展参数集合。整体可缺省；未传或空对象等价于全部字段缺省，各字段单独也可缺省。 |

#### **options 对象字段**

options 用于承载“高级 / 扩展”档位类参数。

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| options.return\_last\_frame | 否 | boolean | 是否返回生成视频的尾帧图片。取值：true / false，默认 false。传 true 时，若模型确实产出了尾帧，查询接口会在 content.last\_frame\_url 返回其临时下载地址；未产出则该字段缺省。 |

#### **content 数组元素参数**

`content` 是一个按 `type` 区分的联合类型数组，各元素字段互斥：

| **参数名** | **必选** | **类型** | **描述** |
| --- | --- | --- | --- |
| type | 是 | string | 元素类型。取值：text、image\_url、video\_url、audio\_url。 |
| text | 条件必选 | string | 文本提示词。type=text 时必填且不可为空串。存在多个 text 元素时按数组顺序拼接为完整提示词。 |
| image\_url | 条件必选 | object | 图片素材。type=image\_url 时必填，结构 {"url": "..."}，其中 url 不可为空串。 |
| video\_url | 条件必选 | object | 视频素材。type=video\_url 时必填，结构 {"url": "..."}，其中 url 不可为空串。 |
| audio\_url | 条件必选 | object | 音频素材。type=audio\_url 时必填，结构 {"url": "..."}，其中 url 不可为空串。 |
| role | 条件必选 | string | 素材用途，type 为 image\_url / video\_url / audio\_url 时必填（type=text 不使用该字段）。  取值：first\_frame、last\_frame、reference\_image、reference\_video、reference\_audio。  type=image\_url：首帧取 first\_frame，尾帧取 last\_frame，参考图片取 reference\_image；  type=video\_url：固定 reference\_video；  type=audio\_url：固定 reference\_audio。 |

`type` 与 `role` 的组合：

| **type** | **role** | **实际用途** |
| --- | --- | --- |
| image\_url | first\_frame | 首帧图片 |
| image\_url | last\_frame | 尾帧图片 |
| image\_url | reference\_image | 参考图片 |
| video\_url | reference\_video（固定） | 参考视频 |
| audio\_url | reference\_audio（固定） | 参考音频 |
| text | 不使用 | - |

### 3. 文生视频请求示例

仅凭文本提示词生成视频。`content` 数组只包含一个 `type=text` 元素，resolution、ratio、duration 均可显式指定。

```json
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/vega-videos/tasks' \\
  -H 'Content-Type: application/json' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -d '{
  "model": "wand-vega-video-1.0-lite",
  "content": [
    {
      "type": "text",
      "text": "一只橙色小猫在窗台上看向镜头，阳光从侧面洒入，镜头缓缓推进"
    }
  ],
  "resolution": "768P",
  "ratio": "16:9",
  "duration": 6
}'
```

### 4. 首尾帧生视频请求示例

以 1~2 张图片作为首帧 / 尾帧，结合文本提示词生成视频。在 `content` 中传入 `type=image_url` 且 `role` 为 first\_frame / last\_frame 的元素。

**说明：**

首帧（role=first\_frame）最多 1 张，尾帧（role=last\_frame）最多 1 张。

必须同时包含至少 1 个 type=text 元素。

不指定 ratio 时由输入图片决定画幅；也可显式指定 21:9 / 16:9 / 4:3 / 1:1 / 3:4 / 9:16 / adaptive。

```json
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/vega-videos/tasks' \\
  -H 'Content-Type: application/json' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -d '{
  "model": "wand-vega-video-1.0-lite",
  "content": [
    {
      "type": "text",
      "text": "镜头从首帧自然过渡到尾帧，保持光影连续"
    },
    {
      "type": "image_url",
      "image_url": { "url": "https://example.com/start.jpg" },
      "role": "first_frame"
    },
    {
      "type": "image_url",
      "image_url": { "url": "https://example.com/end.jpg" },
      "role": "last_frame"
    }
  ],
  "resolution": "1080P",
  "duration": 8
}'
```

### 5. 参考生视频请求示例

以文本 + 参考图片 / 参考视频 / 参考音频的组合生成视频。在 content 中传入 type=image\_url / type=video\_url / type=audio\_url 元素：

type=image\_url：role 传 reference\_image。

type=video\_url：role 固定为 reference\_video。

type=audio\_url：role 固定为 reference\_audio。

role 对以上三种 type 均为必填，省略或留空会被拒绝。

**说明：**

必须包含至少 1 个 type=text 元素。

建议至少包含 1 个参考图片或参考视频，不要仅输入音频。

建议参考图不超过 9 张、参考视频不超过 3 段、参考音频不超过 3 段，素材合计不超过 12 个。

文件 URL 暂时不支持 Base64 内联，功能支持中。

```json
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/vega-videos/tasks' \\
  -H 'Content-Type: application/json' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -d '{
  "model": "wand-vega-video-1.0-lite",
  "content": [
    {
      "type": "text",
      "text": "参考图中的角色在参考视频的场景里自然运动，背景音乐与画面节奏一致"
    },
    {
      "type": "image_url",
      "image_url": { "url": "https://example.com/character.jpg" },
      "role": "reference_image"
    },
    {
      "type": "video_url",
      "video_url": { "url": "https://example.com/scene.mp4" },
      "role": "reference_video"
    },
    {
      "type": "audio_url",
      "audio_url": { "url": "https://example.com/bgm.mp3" },
      "role": "reference_audio"
    }
  ],
  "resolution": "768P",
  "ratio": "16:9",
  "duration": 10
}'
```

### 6. 输出参数

**说明：**

提交成功以 HTTP 状态码 201 + 返回 id 为准，响应体中不含错误信息块。

提交接口不做请求级幂等：每次提交均生成新的任务 ID。请以业务侧请求标识自行管理重试，避免重复出片计费。

| **参数名** | **类型** | **说明** |
| --- | --- | --- |
| id | string | 任务 ID，用于轮询查询任务状态。 |
| model | string | 回显提交时的 model 取值。 |
| status | string | 任务状态。提交成功恒为 queued。 |

### 7. 响应示例

```json
HTTP/1.1 201 Created
Content-Type: application/json

{
  "id": "1300000000-video-68b7c1d4a1f2e3d4c5b6a79808192a3b4c5d6e7f8-0000",
  "model": "wand-vega-video-1.0-lite",
  "status": "queued"
}
```

## 查询任务结果

### 1. 接口描述

各生成形态共用的任务查询端点：提交任务返回 id 后，通过本接口轮询任务状态，成功后从 content.video\_url 获取视频地址。

接口：`GET https://tokenhub.tencentmaas.com/v1/wand/vega-videos/tasks/{id}`

### 2. 输入参数

| **参数名** | **必选** | **类型** | **描述** |
| --- | --- | --- | --- |
| id | 是 | string | 任务 ID（路径参数），即提交任务时返回的 id。 |

### 3. 请求示例

```java
curl -X GET 'https://tokenhub.tencentmaas.com/v1/wand/vega-videos/tasks/<Fid>' \\
  -H 'Content-Type: application/json' \\
  -H 'Authorization: Bearer YOUR_API_KEY'
```

### 4. 输出参数

| **参数名** | **类型** | **说明** |
| --- | --- | --- |
| id | string | 任务 ID。 |
| model | string | 回显提交时的 model 取值，不是实际出片模型。 |
| status | string | 任务状态。取值：queued（排队中）、running（生成中）、succeeded（生成成功）、failed（生成失败）。 |
| content | object | 任务生成结果内容，仅在 status=succeeded 时返回。 |
| content.video\_url | string | 生成视频的下载地址。临时地址，有效期 12 小时，请及时下载转存。 |
| content.last\_frame\_url | string | 生成视频的尾帧图片地址。仅在 options.return\_last\_frame=true 时返回。 |
| error | object | 任务失败信息，仅在 status=failed 时返回。 |
| error.code | string | 任务级错误码。取值：InternalError、TaskTimeout 等。 |
| error.message | string | 失败原因描述，便于定位问题。 |

### 5. 响应示例

```json
{
  "id": "1300000000-video-68b7c1d4a1f2e3d4c5b6a79808192a3b4c5d6e7f8-0000",
  "model": "wand-vega-video-1.0-lite",
  "status": "succeeded",
  "content": {
    "video_url": "https://aigc-video.example.com/xxx/result.mp4"
  }
}
```

## 附录

### 统一错误码

| **HTTP 状态码** | **error.code** | **含义** | **处理建议** |
| --- | --- | --- | --- |
| 401 | 由网关定义 | 鉴权失败：Authorization 头缺失或 API Key 无效/已过期。该错误在网关层返回，错误码以网关为准。 | 检查 Authorization: Bearer <API Key> 是否正确、是否在有效期内。 |
| 400 | invalid\_request\_error | 请求参数非法（缺失必选项、类型错误、枚举越界、JSON 解析失败等）。 | 对照本文档各参数的取值范围检查后重试。 |
| 404 | not\_found | 资源不存在（任务 ID 不存在、路径错误等）。 | 确认路径与任务 ID 是否正确。 |
| 500 | internal\_error | 服务内部错误或处理超时。 | 重试；持续失败请联系技术支持。 |
| 503 | service\_unavailable | 服务过载，暂不可用。 | 退避重试。 |

## 常见问题

### 1. 传入不支持的 resolution 会降级吗？

不会。超出当前模型档位的 resolution 会在提交阶段直接返回 400 invalid\_request\_error（如 Lite 传 720P）。

### 2. 生成结果视频链接会过期吗？

会过期。生成结果为临时地址，有效期 12 小时，请在任务成功后及时下载并转存到自有存储。

### 3. 提交成功但一直处于 queued 怎么办？

排队超时的任务会被置为 failed 并返回 error.code = TaskTimeout。若长时间停留在 queued，请稍后重试并提交 id 联系技术支持。
