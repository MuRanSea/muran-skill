<!-- Official source: https://cloud.tencent.com/document/product/1823/137202 -->
<!-- Source SHA-256: 79c5a3cee68dfcbefed57ca1d6f6f0c7a0a2f9f8a110c6e77923555ba1bb220d -->

# Hy 生视频调用指南

官方来源：https://cloud.tencent.com/document/product/1823/137202
最近更新时间：2026-09-24 21:20:30

## 概述

腾讯混元生视频是一款提供视频生成和视频处理能力的 API 技术服务。 该服务基于腾讯视频生成大模型等一系列领先的音视频 AI 技术，支持高质量地生成或处理视频内容。既能帮助专业视频创作者降低制作成本、发现视频创意，又能提升视频社交娱乐的趣味性。可广泛应用于短视频平台、影视制作、广告营销、社交媒体、游戏等领域。

### 前提条件

已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号并开通 TokenHub 服务。

已在 [TokenHub 控制台](https://console.cloud.tencent.com/tokenhub/apikey) 获取 API Key。

在[控制台-在线推理-视觉模型](https://console.cloud.tencent.com/tokenhub/inference?regionId=1&serviceType=VISION) 处开启对应模型的后付费。

**说明：**

下文所有示例中的 YOUR\_API\_KEY 均需替换为您自己的 API Key，鉴权方式为请求头 Authorization: Bearer YOUR\_API\_KEY。

### **调用流程**

视频生成为耗时任务，接口采用**异步调用**模式，统一分两步：

1. **提交任务**：调用视频生成接口，成功返回 `task_id`（任务 ID）和 `request_id`；

2. **轮询结果**：携带任务 ID 调用 [查询任务结果](https://cloud.tencent.com/document/product/1823/137202#.E6.9F.A5.E8.AF.A2.E4.BB.BB.E5.8A.A1.E7.BB.93.E6.9E.9C) 接口，直至 `status = succeeded`，从 `videos[].url` 获取视频地址。

**注意：**

本系列接口响应**不使用 code / message / data 统一信封**：提交成功返回 `{"task_id": "...", "created": ..., "request_id": "..."}`，查询返回任务对象（含 task\_id / status / videos / usage 等字段）。任务状态统一为：queued（等待调度）/ running（生成中）/ succeeded（成功）/ failed（失败）。

### 模型列表

| 模型名称 | model 参数值（模型 ID） | 支持能力 | 视频时长（秒） | 清晰度档位 | 画面宽高比 | 选型建议 |
| --- | --- | --- | --- | --- | --- | --- |
| hy-video-v1.5 | `hy-video-v1.5` | 文生 / 图生 | 5 | 720p | 16:9、9:16、1:1、4:3、3:4（仅文生可指定） | 混元视频通用款，文生 / 图生一体化 |

**说明：**

文生 / 图生由是否携带图片入参自动区分：携带 `image` 或 `image_url` 即图生视频，否则为文生视频；

图生视频的画面比例由输入图片决定，不支持 `aspect_ratio` 参数。

## 视频生成

### 1. 接口描述

提交文生视频或图生视频任务：不携带图片即为文生视频；携带 `image`（Base64）或 `image_url`（图片 URL）即为图生视频。

**接口：** `POST https://tokenhub.tencentmaas.com/v1/wand/hunyuan-video/generation`

### 2. 输入参数

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| model | 是 | string | 模型版本。取值：`hy-video-v1.5` |
| prompt | 条件必选 | string | 文本提示词。文生视频必选；图生视频可选（用于描述图片中主体的运动）。 |
| negative\_prompt | 否 | string | 负向提示词，描述不希望出现的内容。 |
| image | 否 | string | 输入图片 Base64 编码，大小不超过10M，支持 jpg/jpeg/png 格式，携带即为图生视频。与 `image_url` 二选一；同时传入时以 `image` 为准。 |
| image\_url | 否 | string | 输入图片公网可访问 URL，大小不超过10M，支持 jpg/jpeg/png 格式，生成视频长宽比与传入图片保持一致，携带即为图生视频。与 `image` 二选一。 |
| n | 否 | int | 输出视频数量。 |
| duration | 否 | number | 视频时长（秒），小数将截断为整数。当前版本固定生成 5 秒。 |
| aspect\_ratio | 否 | string | 画面宽高比，**仅文生视频有效**。枚举：16:9 / 9:16 / 1:1 / 4:3 / 3:4。 |
| resolution | 否 | string | 清晰度。当前版本固定输出 720p。 |
| revise | 否 | bool | 是否开启提示词智能改写（扩展参数，原样透传至模型服务）。 |
| moderation | 否 | bool | 内容审核开关（扩展参数，原样透传至模型服务）。 |
| seed | 否 | int | 随机种子（扩展参数，原样透传至模型服务，是否生效以模型侧为准）。 |
| footnote | 否 | string | 业务自定义水印内容，限制 16 个字符长度（不区分中英文,会去换行与空格字符），生成在视频右下角。 |

**注意：**

除上表字段外，其余未识别字段将原样透传至模型服务；

### 3. 请求示例

**文生视频：**

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/hunyuan-video/generation' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "hy-video-v1.5",
  "prompt": "一只小狗在草地上奔跑，阳光明媚",
  "negative_prompt": "模糊、变形",
  "aspect_ratio": "16:9"
}'
```

**图生视频（图片 URL）：**

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/hunyuan-video/generation' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "hy-video-v1.5",
  "prompt": "让图片中的主体自然转头，微风吹动头发",
  "image_url": "https://example.com/start.jpg"
}'
```

**图生视频（图片 Base64）：**

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/hunyuan-video/generation' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "hy-video-v1.5",
  "prompt": "镜头缓慢推进",
  "image": "<BASE64_ENCODED_IMAGE>"
}'
```

### 4. 输出参数

提交成功返回：

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| task\_id | string | 系统生成的任务 ID，用于后续任务查询。 |
| created | integer | 任务创建时间，Unix 秒级时间戳。 |
| request\_id | string | 本次请求的唯一 ID，用于问题排查与技术支持定位。 |

提交失败返回统一错误信封：

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| task\_id | string | 任务 ID（未能创建时为空字符串）。 |
| status | string | 固定 `failed`。 |
| error.code | string | 错误码，请参见 [附录：统一错误码](https://cloud.tencent.com/document/product/1823/137202#.E7.BB.9F.E4.B8.80.E9.94.99.E8.AF.AF.E7.A0.81)。 |
| error.message | string | 错误描述信息。 |

### 5. 响应示例

**提交成功：**

```json
{
  "task_id": "251435731-WandVideo-05c42d57d3a74c1fa39d56ff59b31e20",
  "created": 1787108411,
  "request_id": "835a268e-af02-4615-a30b-7e4b815e8839"
}
```

**提交失败：**

```json
{
  "task_id": "",
  "status": "failed",
  "error": {
    "code": "1300",
    "message": "Trigger the platform strategy"
  }
}
```

### 6. 错误码

请求失败时返回 `{"task_id":"","status":"failed","error":{...}}` 信封，具体错误码及处理建议请参见 [附录：统一错误码](https://cloud.tencent.com/document/product/1823/137202#.E7.BB.9F.E4.B8.80.E9.94.99.E8.AF.AF.E7.A0.81)。任务提交成功后，生成阶段的任务状态通过 [查询任务结果](https://cloud.tencent.com/document/product/1823/137202#.E6.9F.A5.E8.AF.A2.E4.BB.BB.E5.8A.A1.E7.BB.93.E6.9E.9C) 接口获取：

| status | 含义 | 处理建议 |
| --- | --- | --- |
| queued | 已提交等待调度 | 继续轮询 |
| running | 生成中 | 继续轮询 |
| succeeded | 生成成功 | 从查询结果 `videos[].url` 获取视频地址 |
| failed | 生成失败 | 查看 `error.message` 失败原因，修改后重试；持续失败请联系技术支持 |

## 查询任务结果

### 1. 接口描述

提交任务返回任务 ID 后，通过任务查询端点轮询任务状态，成功后从结果中获取视频地址。

**接口：** `GET https://tokenhub.tencentmaas.com/v1/wand/hunyuan-video/tasks/{task_id}`

**说明：**

路径中的 `{task_id}` 即提交任务时返回的 `task_id`（示例中以 `YOUR_TASK_ID` 占位）。视频生成约需数分钟，建议每 3~5 秒轮询一次。响应为模型侧回包透传并叠加平台归一化字段，**可能包含下表之外的原厂字段，以实际返回为准**。

### 2. 输入参数

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| task\_id | 是 | string | 任务 ID（路径参数），即提交任务时返回的 `task_id`。 |

### 3. 请求示例

```bash
curl -X GET 'https://tokenhub.tencentmaas.com/v1/wand/hunyuan-video/tasks/YOUR_TASK_ID' \\
  -H 'Authorization: Bearer YOUR_API_KEY'
```

### 4. 输出参数

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| task\_id | string | 任务 ID。 |
| status | string | 任务状态：queued（等待调度）/ running（生成中）/ succeeded（成功）/ failed（失败） |
| created | integer | 任务创建时间，Unix 秒级时间戳。 |
| videos | array | 视频结果数组（成功时返回）。 |
| videos[].url | string | 视频文件地址，为临时地址，请及时下载转存。 |
| videos[].audio\_url | string | 音频文件地址（无音频时为空字符串）。 |
| videos[].generate\_info | string | 模型侧生成附加信息（无则空字符串）。 |
| tokenhub\_usage | object | 用量消耗（任务到达终态并完成计费后返回）。 |
| tokenhub\_usage.total\_tokens | integer | 本次任务消耗的 token 数，用于计费 / 对账。 |
| error | object | 失败信息（status=failed 时返回），含 code / message；未失败为 null。 |
| error.code | string | 错误码。 |
| error.message | string | 错误描述信息。 |
| request\_id | string | 本次请求的唯一 ID，用于问题排查与技术支持定位。 |

### 5. 响应示例

**生成中（running）：**

```json
{
  "created": 1787108411,
  "error": null,
  "task_id": "251435731-WandVideo-05c42d57d3a74c1fa39d56ff59b31e20",
  "status": "running",
  "request_id": "252e94a8-dbce-4440-8747-e36f52e0fc29"
}
```

**生成成功（succeeded）：**

```json
{
  "created": 1787108411,
  "error": null,
  "task_id": "251435731-WandVideo-05c42d57d3a74c1fa39d56ff59b31e20",
  "status": "succeeded",
  "videos": [
    {
      "audio_url": "",
      "generate_info": "",
      "url": "https://aigc-output-video-1326893053.cos.ap-guangzhou.myqcloud.com/251435731/251435731-WandVideo-05c42d57d3a74c1fa39d56ff59b31e20_0.mp4?q-sign-algorithm=sha1&..."
    }
  ],
  "tokenhub_usage": {
    "total_tokens": 150000
  },
  "request_id": "252e94a8-dbce-4440-8747-e36f52e0fc29"
}
```

**生成失败（failed）：**

```json
{
  "created": 1787108411,
  "task_id": "251435731-WandVideo-05c42d57d3a74c1fa39d56ff59b31e20",
  "status": "failed",
  "error": {
    "code": "InternalServiceError",
    "message": "generate video failed"
  },
  "request_id": "252e94a8-dbce-4440-8747-e36f52e0fc29"
}
```

### 6. 错误码

请求失败时返回统一错误信封，具体错误码及处理建议请参见 [附录：统一错误码](https://cloud.tencent.com/document/product/1823/137202#.E7.BB.9F.E4.B8.80.E9.94.99.E8.AF.AF.E7.A0.81)。任务状态说明同「视频生成」。

## 附录

### 统一错误码

| HTTP 状态码 | 业务码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 200 | 0 | success | 请求成功。 |
| 401 | 1000 | Authentication failed | Authorization 缺失或 apikey 非法。 |
| 401 | 1001 | Authorization is empty | 未携带 Authorization 头。 |
| 401 | 1002 | Authorization is invalid | apikey 无效或已失效。 |
| 401 | 1003 | Authorization is not yet valid | apikey 尚未生效。 |
| 401 | 1004 | Authorization has expired | apikey 已过期。 |
| 429 | 1100 | Account exception | 账号异常（可能欠费、被封禁或被暂停）。 |
| 429 | 1101 | Account in arrears (postpaid) | 后付费账号欠费。 |
| 429 | 1102 | Resource pack depleted or expired | 资源包已用完或已过期。 |
| 403 | 1103 | Access denied for the requested resource | 请求资源无访问权限（未订阅对应模型/能力）。 |
| 400 | 1200 | Invalid request parameters | 请求参数非法（缺失必选项、类型错误、枚举越界等）。 |
| 400 | 1201 | Invalid parameters | 参数值不合法，请对照文档参数取值范围检查。 |
| 404 | 1202 | The requested method is invalid | HTTP 方法错误。 |
| 404 | 1203 | The requested resource does not exist | 端点路径错误或资源不存在。 |
| 400 | 1300 | Trigger the platform strategy | 触发平台策略（如内容审核不通过、违规输入）。 |
| 400 | 1301 | Trigger platform sensitive word list | 命中敏感词或违规提示词。 |
| 429 | 1302 | Too frequent API calls | 调用过于频繁，触发限流。 |
| 429 | 1303 | Concurrency or QPS exceeds the limit | 并发或 QPS 超过预设配额。 |
| 400 | 1304 | Trigger IP strategy | 触发 IP 策略拦截。 |
| 500 | 5000 | Internal server error | 服务器内部错误。 |
| 503 | 5001 | Server is temporarily unavailable | 服务暂不可用（多为忙碌或维护中）。 |
| 504 | 5002 | Server internal timeout | 服务内部超时。 |

## 常见问题

**1. 文生视频和图生视频如何切换？**

由入参自动区分：不携带 `image` / `image_url` 即为文生视频；携带任一图片参数即为图生视频。`image` 与 `image_url` 同时传入时以 `image`（Base64）为准。

**2. 视频时长、清晰度、宽高比支持哪些取值？**

当前版本视频时长固定 5 秒、清晰度固定 720p；宽高比 `aspect_ratio` 仅文生视频可指定（16:9 / 9:16 / 1:1 / 4:3 / 3:4），图生视频的画面比例由输入图片决定。

**3. 查询接口返回的 status 有哪些？**

`queued`（等待调度）/ `running`（生成中）/ `succeeded`（成功）/ `failed`（失败）。仅 `succeeded` 时 `videos[].url` 有值；`failed` 时查看 `error` 字段获取失败原因。

**4. 查询响应里出现了文档未列出的字段？**

查询响应为模型侧回包透传并叠加平台归一化字段（如 `usage.total_tokens`、`request_id`），可能包含其他原厂字段，均属正常，以实际返回为准。
