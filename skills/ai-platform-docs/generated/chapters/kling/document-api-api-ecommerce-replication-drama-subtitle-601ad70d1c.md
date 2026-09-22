<!-- Official source: https://klingai.com/document-api/api/ecommerce-replication/drama-subtitle.md -->
<!-- Source SHA-256: 533210b2c4ac8dd9cc1b5166fa993293407634a4adcd424de81748efe66fb81b -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://klingai.com/document-api/llms.txt
> Use this file to discover all available pages before exploring further.

# 字幕译制

> 来源: https://klingai.com/document-api/api/ecommerce-replication/drama-subtitle
> 语言: zh
> 当前 Tab: 字幕译制
> 此内容为面向 LLM 优化的 Markdown，已展开页面内 Tab，并省略页面目录、复制按钮等 UI 控件。

---

## 功能简介

字幕译制（drama_subtitle）是面向短剧出海内容方与译制团队的 AI 字幕生成服务。用户只需提供一段中文短剧原片视频，系统即可自动完成语音识别、逐句定界、中译英翻译、字幕排版与硬字幕烧录，生成可直接投放的英文硬字幕成片，有效降低译制成本与交付周期。

系统会保留原视频的画面和音轨，仅在画面上增加英文硬字幕；同时交付 SRT / ASS 字幕文件，便于二次加工。

生成产物为一段与原片等长（最长 300 秒）的英文硬字幕成片，以及配套 SRT / ASS 字幕文件。

## 接入与使用建议

### 源视频素材质量建议

- 源视频需包含清晰可识别的人声对白，建议背景音乐不过分压制台词；音频质量直接影响识别与翻译效果。
- 推荐使用 MP4 容器（视频编码 H.264、音频编码 AAC）；FFmpeg 能解码的其他格式均会尝试处理。
- 分辨率与帧率无硬限制，建议 240p～4K、不超过 60 FPS。
- 本能力不提供字幕擦除，原片已烧录的字幕不会去除、英文字幕会叠加显示，建议优先使用无字幕原片。

### 术语表使用建议

- 对连续剧集建议使用统一的术语表（glossary），保证人名、地名、组织名在多集之间译法一致。
- 人名默认使用汉语拼音（姓在前，如 Song Tang），不做西化改名；如需固定专名译法，请通过术语表传入。

### 适用场景

- 短剧出海批量译制：支持批量提交多集任务，单集自动完成翻译与烧录。
- 存量剧库快速英化：对已有中文短剧批量生成英文硬字幕版本。
- 成片直接投放：输出硬字幕成片可直接用于海外短剧平台与信息流投放；SRT / ASS 可用于人工精修。

## 创建任务

### 接口概览

- Method: `POST`
- Path: `/solutions/drama_subtitle`
- Auth: `Authorization: Bearer <API_KEY>`
- Content-Type: `application/json`

### Headers

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `Content-Type` | string | 是 | `application/json` | - | 数据交换格式 |
| `Authorization` | string | 是 | - | - | 鉴权信息，参考接口鉴权 |

### Request Body

| 字段路径 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `contents` | array | 是 | - | - | 输入的素材合集。首版必须且只能传一个源视频素材，可选传入术语表。 |
| `contents[].type` | string | 是 | - | `source_video`, `glossary` | 素材类型。支持：源视频素材、术语表。 |
| `settings` | object | 否 | - | - | 输出字幕配置相关参数。 |
| `settings.target_cps` | int | 否 | `17` | - | 目标阅读速度（字符/秒，CPS），控制英文字幕的压缩程度。 |
| `settings.target_language` | string | 否 | `en` | - | 目标语言。 |
| `settings.margin_v` | int | 否 | `自动` | - | 字幕距画面底部的像素距离。 |
| `settings.font_size` | int | 否 | `自动` | - | 字幕字号，正整数。 |
| `options` | object | 否 | - | - | 通用配置，如回调地址、自定义任务 ID 等。 |
| `options.callback_url` | string | 否 | - | - | 本次任务结果回调通知地址。如果配置，任务到达终态（succeeded / failed）后服务端主动通知，处理中的中间状态不触发回调。 |
| `options.external_task_id` | string | 否 | - | - | 自定义任务 ID。 |

#### Request Body 字段补充说明

- `contents`: 参考格式如下，参数说明详见下文：
  ```json
  "contents": [
    {
      "type": "source_video",
      "url": "https://your-cdn.com/drama_ep01.mp4"
    },
    {
      "type": "glossary",
      "source": "宋棠",
      "target": "Song Tang"
    }
  ]
  ```
- `contents[].type`: `source_video`：源视频素材标识。
  - `glossary`：术语表标识。
- `contents[].type.source_video`: 通过 JSON 的格式定义，具体如下：
  ```json
  {
    "type": "source_video", // 源视频素材标识；必填
    "url": "string" // 素材内容，支持通过 url 方式提供，暂不支持 base64；必须为服务端可访问的 HTTP/HTTPS 地址；必填
  }
  ```
- `contents[].type.source_video`: 视频文件大小不能超过 500MB。
- `contents[].type.source_video`: 视频时长不能超过 300 秒（5 分钟）。
- `contents[].type.source_video`: 必须至少包含一条视频轨和一条音频轨。
- `contents[].type.source_video`: 推荐 .mp4（H.264 + AAC）；FFmpeg 能解码的格式均会尝试处理。
- `contents[].type.source_video`: 分辨率、帧率无硬限制，建议 240p～4K、不超过 60 FPS。
- `contents[].type.source_video`: 最多支持 1 条源视频。
- `contents[].type.glossary`: 通过 JSON 的格式定义，`source` 为中文原词，`target` 为期望英文译法：
  ```json
  {
    "type": "glossary", // 术语表标识；选填
    "source": "苏芷", // 中文原词；必填
    "target": "Su Zhi" // 期望英文译法；必填
  }
  ```
- `contents[].type.glossary`: 最多 200 项；去除首尾空格后不能为空，单项最长 100 个字符。
- `contents[].type.glossary`: 只约束翻译结果；未传入的专名由系统自动翻译，人名默认使用汉语拼音。
- `settings.target_cps`: 取值范围：10～20 的整数。
- `settings.target_cps`: 值越小字幕越精简、越易读；值越大保留的台词信息越多。
- `settings.target_language`: 首版固定值：en（英文）。
- `settings.margin_v`: 省略或传 null 时自动选择：竖屏 340，横屏 80。
- `settings.margin_v`: 取值范围：1～4096 的整数。
- `settings.margin_v`: 原片自带硬字幕时可用于避开原字幕位置。
- `settings.font_size`: 省略或传 null 时自动选择：竖屏 60，横屏 56。
- `settings.font_size`: 取值范围：1～512 的整数。
- `options`: ```json
  "options": {
    "callback_url": "https://example.com/cb", // 本次任务结果回调通知地址。如果配置，任务到达终态（succeeded / failed）后服务端主动通知
    "external_task_id": "string" // 自定义任务 ID，可用于查询，需在账号范围内保证唯一性
  }
  ```
- `options.callback_url`: 具体通知的消息 schema 见 [Callback 协议](https://klingai.com/document-api/api/get-started/callbacks)。
- `options.external_task_id`: 传入不会覆盖系统生成的任务 ID，但支持通过该 ID 进行任务查询。
- `options.external_task_id`: 请注意，单用户下需要保证唯一性。

### Request Example

```bash
curl --location --request POST 'https://api-beijing.klingai.com/solutions/drama_subtitle' \
--header 'Authorization: Bearer {apikey}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "contents": [
    {
      "type": "source_video",
      "url": "https://your-cdn.com/drama_ep01.mp4"
    },
    {
      "type": "glossary",
      "source": "宋棠",
      "target": "Song Tang"
    },
    {
      "type": "glossary",
      "source": "顾氏集团",
      "target": "Gu Group"
    }
  ],
  "settings": {
    "target_cps": 17
  },
  "options": {
    "callback_url": "https://example.com/callback",
    "external_task_id": "my_task_123"
  }
}'
```

### Response Example

```json
{
  "code": 0, // 错误码；具体定义见错误码
  "message": "string", // 错误信息
  "request_id": "string", // 请求 ID，系统生成，用于跟踪请求、排查问题
  "data": {
    "id": "string", // 系统生成的任务 ID
    "status": "string", // 任务状态，枚举值：submitted（已提交）、processing（处理中）、succeeded（成功）、failed（失败）
    "create_time": 1781080778802, // 任务创建时间，Unix 时间戳，单位 ms
    "update_time": 1781080794151, // 任务更新时间，Unix 时间戳，单位 ms
    "external_id": "string" // 该任务的自定义任务 ID（如有）
  }
}
```

## 查询任务（指定任务ID）

### 接口概览

- Method: `GET`
- Path: `/solutions`
- Auth: `Authorization: Bearer <API_KEY>`
- Content-Type: `application/json`

### 说明

- 任务查询为平台级通用接口，适用于所有可灵解决方案API。

### Headers

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `Content-Type` | string | 是 | `application/json` | - | 数据交换格式 |
| `Authorization` | string | 是 | - | - | 鉴权信息，参考接口鉴权 |

### Query Params

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `task_ids` | string | 否 | - | - | 需要查询的系统定义的任务 ID。 |
| `external_task_ids` | string | 否 | - | - | 需要查询的自定义任务 ID。 |

#### Query Params 字段补充说明

- `task_ids`: 请求查询参数，将值拼接在请求 URL 的 `?` 之后。
- `task_ids`: task_ids 与 external_task_ids 两种 ID 至少且只能选择一种，不可同时使用。
- `task_ids`: 支持批量查询，最多可同时查询 20 个任务。
- `external_task_ids`: 请求查询参数，将值拼接在请求 URL 的 `?` 之后。
- `external_task_ids`: task_ids 与 external_task_ids 两种 ID 至少且只能选择一种，不可同时使用。
- `external_task_ids`: 支持批量查询，最多可同时查询 20 个任务。

### Request Example

```bash
curl -X GET "https://api-beijing.klingai.com/solutions?task_ids=id1,id2" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer {apikey}"
```

### Response Example

```json
{
  "code": 0, // 错误码；具体定义见错误码
  "message": "string", // 错误信息
  "request_id": "string", // 请求 ID，系统生成，用于跟踪请求、排查问题
  "data": [ // 任务列表
    {
      "id": "string", // 被查询的任务 ID
      "status": "string", // 任务状态，枚举值：submitted（已提交）、processing（处理中）、succeeded（成功）、failed（失败）
      "message": "string", // 任务状态信息，当任务失败时展示失败原因
      "create_time": 1787625163493, // 任务创建时间，Unix 时间戳，单位 ms
      "update_time": 1787626307663, // 任务更新时间，Unix 时间戳，单位 ms
      "external_id": "string", // 该任务的自定义任务 ID（如有）
      "outputs": [ // 生成产物列表
        {
          "type": "subbed_video", // 生成结果为「英文硬字幕成片」时返回
          "url": "string", // 生成结果的 URL，防盗链格式（请注意，为保障信息安全，生成的视频/文件会在 30 天后被清理，请及时转存）
          "duration": "string" // 视频时长，单位秒
        },
        {
          "type": "srt", // 生成结果为「SRT 字幕文件」时返回
          "url": "string" // 生成结果的 URL，防盗链格式
        },
        {
          "type": "ass", // 生成结果为「ASS 字幕文件」时返回
          "url": "string" // 生成结果的 URL，防盗链格式
        }
      ],
      "billing": [ // 任务消耗信息
        {
          "charge_type": "unit", // 消耗账户类型：资源包
          "amount": "string", // 扣减数额；unit 时代表积分扣减量；十进制
          "package_type": "string" // 消耗资源包类型，仅 charge_type=unit 时存在；固定枚举值：video
        },
        {
          "charge_type": "cash", // 消耗账户类型：余额
          "amount": "string", // 扣减数额；cash 时代表额度扣减折扣价；十进制
          "cash_type": "balance", // 额度类型，仅 charge_type=cash 时存在；枚举值：balance（正式额度）、test_balance（测试金）
          "list_price": "string", // 额度扣减刊例价，仅 charge_type=cash 时存在
          "currency": "CNY" // 货币类型，仅 charge_type=cash 时存在；枚举值：CNY（人民币）、USD（美元）
        }
      ]
    }
  ]
}
```

## 查询任务（游标）

### 接口概览

- Method: `POST`
- Path: `/solutions`
- Auth: `Authorization: Bearer <API_KEY>`
- Content-Type: `application/json`

### 说明

- 任务查询为平台级通用接口，适用于所有可灵解决方案API。

### Headers

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `Content-Type` | string | 是 | `application/json` | - | 数据交换格式 |
| `Authorization` | string | 是 | - | - | 鉴权信息，参考接口鉴权 |

### Request Body

| 字段路径 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `start_time` | long | 否 | `end_time - 30天` | - | 任务创建筛选的开始时间。 |
| `end_time` | long | 否 | `当前时间` | - | 任务创建筛选的结束时间。 |
| `cursor` | string | 否 | - | - | 续页游标，即查询起点。 |
| `limit` | int | 否 | `500` | - | 查询任务数量。 |
| `filters` | array | 否 | - | - | 查询任务筛选条件，如：任务状态。 |
| `filters[].key` | string | 否 | - | `status` | 筛选维度，目前支持按任务状态等条件筛选。 |

#### Request Body 字段补充说明

- `start_time`: Unix 时间戳、单位 ms。
- `start_time`: 默认值为 end_time - 30 天。
- `start_time`: 开始时间需早于结束时间。
- `end_time`: 默认值为当前时间。
- `end_time`: Unix 时间戳、单位 ms。
- `end_time`: 结束时间需晚于开始时间。
- `cursor`: 参数值来自上次查询时返回的 next_cursor 参数。
- `cursor`: 当前参数不为空时，优先基于当前参数值查询，此时开始时间和结束时间参数将失效。
- `limit`: 传入 0 或负数时，按 1 处理。
- `limit`: 最大值 500；当查询结果数量不足 500 时展示所有查询结果。
- `filters`: 通过 key & value 的方式设置查询条件，如：查询状态为 succeeded 的任务。
  - 参考格式如下，参数说明详见下文：
  ```json
  "filters": [
    {
      "key": "status",
      "values": ["succeeded"]
    }
  ]
  ```
- `filters[].key`: `status`：任务状态
- `filters[].key.status`: 通过 JSON 的格式定义，具体如下：
  ```json
  {
    "key": "status", // 筛选维度，按任务状态筛选，固定参数值：status；必填
    "values": ["succeeded"] // 筛选维度对应条件，枚举值：submitted、processing、succeeded、failed，依次为：已提交、生成中、生成成功、生成失败；必填
  }
  ```

### Response Example

```json
{
  "code": 0,
  "message": "string",
  "request_id": "string",
  "data": {
    "result": [ "... 结构与「查询任务（指定任务ID）」响应体一致 ..." ], // 任务列表，结构与查询任务（指定任务ID）响应体一致
    "count": 1, // 查询结果数量
    "next_cursor": "string", // 游标信息，可用于继续查询后续
    "has_more": true // 基于游标信息，是否还有未查询到的数据
  }
}
```

## 错误码 / 回调协议

参考平台通用文档：[接口鉴权](https://klingai.com/document-api/api/get-started/authentication)、[错误码](https://klingai.com/document-api/api/get-started/error-codes)、[回调协议](https://klingai.com/document-api/api/get-started/callbacks)。

### 字幕译制专属错误信息

参数校验错误统一返回 `code: 1201`，具体场景和 message 如下：

| 场景                                                 | message                                                                  | 中文提示映射                                   |
| ---------------------------------------------------- | ------------------------------------------------------------------------ | ---------------------------------------------- |
| 缺源视频                                             | Source video is missing. Please provide a source video URL.              | 请提供源视频                                   |
| 多个 `contents.type=source_video`                    | Only one source_video item is allowed in contents.                       | 源视频最多上传 1 条，请移除多余的 source_video |
| `source_video` 的 url 为空 / 非法                    | source_video is missing. Please provide exactly one source_video.        | 源视频地址无效，请提供有效的 HTTP/HTTPS 地址   |
| `glossary` 超过 200 项                               | Glossary exceeds the limit of 200 entries.                               | 术语表最多 200 项                              |
| `glossary` 单项为空或超过 100 字符                   | Each glossary entry must be non-empty and no longer than 100 characters. | 术语表单项不能为空且不超过 100 字符            |
| `margin_v` / `font_size` / `target_cps` 非正整数     | margin_v, font_size and target_cps must be positive integers.            | 底边距、字号、目标阅读速度需为正整数           |
| `margin_v` / `font_size` / `target_cps` 超出取值范围 | {param} out of range. Please provide a value between {min} and {max}.    | {参数} 超出取值范围，需在 {min}～{max} 之间    |

### 任务失败信息（查询接口 `data[].message`）

任务处理失败时，失败原因通过查询接口 / 回调的 `message` 字段返回：

| 场景                     | message                                                                                            | 中文提示映射                                             |
| ------------------------ | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| 源视频格式无法解码       | The source video format is not supported. Please provide a decodable video file (MP4 recommended). | 源视频格式不支持，请提供可正常解码的视频文件（推荐 MP4） |
| 源视频超过大小限制       | The source video exceeds the 500MB size limit.                                                     | 源视频超过 500MB 大小限制                                |
| 源视频超过时长限制       | The source video exceeds the 300-second duration limit.                                            | 源视频超过 300 秒时长限制                                |
| 源视频缺少音频轨或视频轨 | No valid audio or video track detected in the source video.                                        | 源视频缺少可识别的音频轨或视频轨                         |
| 系统内部错误             | Internal error, please contact Kling customer service.                                             | 系统内部错误                                             |
