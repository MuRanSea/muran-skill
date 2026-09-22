<!-- Official source: https://klingai.com/document-api/api/video/2-6/voice-customization.md -->
<!-- Source SHA-256: c94234012dfef02dd50a1e0562570927d046089e9ab9e59d34c37393c02d9e5f -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://klingai.com/document-api/llms.txt
> Use this file to discover all available pages before exploring further.

# 音色管理

> 来源: https://klingai.com/document-api/api/video/2-6/voice-customization
> 语言: zh
> 当前 Tab: 音色管理
> 同组 Tab: 文生视频 / 图生视频 / 动作控制 / 音色管理
> 此内容为面向 LLM 优化的 Markdown，已展开页面内 Tab，并省略页面目录、复制按钮等 UI 控件。

---

## 创建自定义音色

### 接口概览

- Method: `POST`
- Path: `/v1/general/custom-voices`
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
| `voice_name` | string | 是 | - | - | 音色名称 |
| `voice_url` | string | 否 | - | - | 音色数据文件获取链接 |
| `video_id` | string | 否 | - | - | 历史作品 ID，可通过引用历史作品提供音频素材 |
| `callback_url` | string | 否 | - | - | 本次任务结果回调通知地址，如果配置，服务端会在任务状态发生变更时主动通知。 |
| `external_task_id` | string | 否 | - | - | 自定义任务 ID |

#### Request Body 字段补充说明

- `voice_name`: 文本内容最大长度 20 个字符
- `voice_name`: 创建后不再使用的音色可通过 API 删除
- `voice_url`: 支持 .mp3 / .wav / .mp4 / .mov 格式的音视频文件
- `voice_url`: 音频中人声需干净无杂音，有且只能有一种人声，时长不短于 5 秒且不长于 30 秒
- `video_id`: 仅满足以下条件的视频可以用于定制音色：
    - 使用 V2.6 版本模型生成且开启 sound 参数值为 on 的视频
    - 通过数字人 API 生成的视频
    - 通过对口型 API 生成的视频
- `video_id`: 音频中人声需干净无杂音，有且只能有一种人声，时长不短于 5 秒且不长于 30 秒
- `callback_url`: 具体通知的消息 schema 见 [Callback 协议](https://klingai.com/document-api/api/get-started/callbacks)
- `external_task_id`: 传入不会覆盖系统生成的任务 ID，但支持通过该 ID 进行任务查询
- `external_task_id`: 请注意，单用户下需要保证唯一性

### Request Example

```bash
curl --request POST \
  --url https://api-beijing.klingai.com/v1/general/custom-voices \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
    "video_id": "",
    "voice_url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-qa-test/out.mp3",
    "voice_name": "定制人声",
    "callback_url": ""
  }'
```

### Response Example

```json
{
  "code": 0, // 错误码；具体定义见错误码
  "message": "string", // 错误信息
  "request_id": "string", // 请求ID，系统生成，用于跟踪请求、排查问题
  "data": {
    "task_id": "string", // 任务ID，系统生成
    "task_info": { // 任务创建时的参数信息
      "external_task_id": "string" // 客户自定义任务ID
    },
    "task_status": "string", // 任务状态，枚举值：submitted（已提交）、processing（处理中）、succeed（成功）、failed（失败）
    "created_at": 1722769557708, // 任务创建时间，Unix时间戳、单位ms
    "updated_at": 1722769557708 // 任务更新时间，Unix时间戳、单位ms
  }
}
```

---

## 查询自定义音色（单个）

### 接口概览

- Method: `GET`
- Path: `/v1/general/custom-voices/{id}`
- Auth: `Authorization: Bearer <API_KEY>`
- Content-Type: `application/json`

### Headers

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `Content-Type` | string | 是 | `application/json` | - | 数据交换格式 |
| `Authorization` | string | 是 | - | - | 鉴权信息，参考接口鉴权 |

### Path Params

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `task_id` | string | 是 | - | - | 图片生成的任务ID。请求路径参数，直接将值填写在请求路径中 |
| `external_task_id` | string | 否 | - | - | 用户自定义任务 ID |

#### Path Params 字段补充说明

- `external_task_id`: 创建任务时填写的 external_task_id，与 task_id 两种查询方式二选一
  - 请注意，单用户下需要保证唯一性

### Request Example

```bash
curl --request GET \
  --url 'https://api-beijing.klingai.com/v1/general/custom-voices/{id}' \
  --header 'Authorization: Bearer <token>'
```

### Response Example

```json
{
  "code": 0, // 错误码；具体定义见错误码
  "message": "string", // 错误信息
  "request_id": "string", // 请求ID，系统生成，用于跟踪请求、排查问题
  "data": {
    "task_id": "string", // 任务ID，系统生成
    "task_status": "string", // 任务状态，枚举值：submitted（已提交）、processing（处理中）、succeed（成功）、failed（失败）
    "task_status_msg": "string", // 任务状态信息，当任务失败时展示失败原因（如触发平台的内容风控等）
    "task_info": { // 任务创建时的参数信息
      "external_task_id": "string" // 客户自定义任务ID
    },
    "task_result": {
      "voices": [
        {
          "voice_id": "string", // 定制的音色的ID；全局唯一
          "voice_name": "string", // 定制的音色的名称
          "trial_url": "string", // 定制的音色的试听音频下载URL
          "owned_by": "kling" // 音色来源，kling为官方音色库，数字为创作者ID
        }
      ]
    },
    "final_unit_deduction": "string", // 任务最终扣减积分数值
    "final_balance_deduction": { // 额度扣减信息
      "quota": "string", // 额度扣减折扣价
      "list_price": "string" // 额度扣减刊例价
    },
    "created_at": 1722769557708, // 任务创建时间，Unix时间戳、单位ms
    "updated_at": 1722769557708 // 任务更新时间，Unix时间戳、单位ms
  }
}
```

---

## 查询自定义音色（列表）

### 接口概览

- Method: `GET`
- Path: `/v1/general/custom-voices`
- Auth: `Authorization: Bearer <API_KEY>`
- Content-Type: `application/json`

### Headers

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `Content-Type` | string | 是 | `application/json` | - | 数据交换格式 |
| `Authorization` | string | 是 | - | - | 鉴权信息，参考接口鉴权 |

### Query Params

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `pageNum` | int | 否 | `1` | - | 页码 |
| `pageSize` | int | 否 | `30` | - | 每页数据量 |

#### Query Params 字段补充说明

- `pageNum`: 取值范围：[1, 1000]
- `pageSize`: 取值范围：[1,1000]

### Request Example

```bash
curl --request GET \
  --url 'https://api-beijing.klingai.com/v1/general/custom-voices?pageNum=1&pageSize=30' \
  --header 'Authorization: Bearer <token>'
```

### Response Example

```json
{
  "code": 0, // 错误码；具体定义见错误码
  "message": "string", // 错误信息
  "request_id": "string", // 请求ID，系统生成，用于跟踪请求、排查问题
  "data": [
    {
      "task_id": "string", // 任务ID，系统生成
      "task_status": "string", // 任务状态，枚举值：submitted（已提交）、processing（处理中）、succeed（成功）、failed（失败）
      "task_status_msg": "string", // 任务状态信息，当任务失败时展示失败原因（如触发平台的内容风控等）
      "task_info": { // 任务创建时的参数信息
        "external_task_id": "string" // 客户自定义任务ID
      },
      "task_result": {
        "voices": [
          {
            "voice_id": "string", // 定制的声音的ID；全局唯一
            "voice_name": "string", // 定制的音色的名称
            "trial_url": "string", // 定制的音色的试听音频下载URL
            "owned_by": "kling" // 音色来源，kling为官方音色库，数字为创作者ID
          }
        ]
      },
      "final_unit_deduction": "string", // 任务最终扣减积分数值
      "final_balance_deduction": { // 额度扣减信息
        "quota": "string", // 额度扣减折扣价
        "list_price": "string" // 额度扣减刊例价
      },
      "created_at": 1722769557708, // 任务创建时间，Unix时间戳、单位ms
      "updated_at": 1722769557708 // 任务更新时间，Unix时间戳、单位ms
    }
  ]
}
```

---

## 查询官方音色（列表）

### 接口概览

- Method: `GET`
- Path: `/v1/general/presets-voices`
- Auth: `Authorization: Bearer <API_KEY>`
- Content-Type: `application/json`

### Headers

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `Content-Type` | string | 是 | `application/json` | - | 数据交换格式 |
| `Authorization` | string | 是 | - | - | 鉴权信息，参考接口鉴权 |

### Query Params

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `pageNum` | int | 否 | `1` | - | 页码 |
| `pageSize` | int | 否 | `30` | - | 每页数据量 |

#### Query Params 字段补充说明

- `pageNum`: 取值范围：[1, 1000]
- `pageSize`: 取值范围：[1,1000]

### Request Example

```bash
curl --request GET \
  --url 'https://api-beijing.klingai.com/v1/general/presets-voices?pageNum=1&pageSize=30' \
  --header 'Authorization: Bearer <token>'
```

### Response Example

```json
{
  "code": 0, // 错误码；具体定义见错误码
  "message": "string", // 错误信息
  "request_id": "string", // 请求ID，系统生成，用于跟踪请求、排查问题
  "data": [
    {
      "task_id": "string", // 任务ID，系统生成
      "task_status": "string", // 任务状态，枚举值：submitted（已提交）、processing（处理中）、succeed（成功）、failed（失败）
      "task_status_msg": "string", // 任务状态信息，当任务失败时展示失败原因（如触发平台的内容风控等）
      "task_result": {
        "voices": [
          {
            "voice_id": "string", // 系统预置的音色的ID；全局唯一
            "voice_name": "string", // 系统预置的音色的名称
            "trial_url": "string", // 系统预置的音色的试听音频下载URL
            "owned_by": "kling" // 音色来源，kling为官方音色库，数字为创作者ID
          }
        ]
      },
      "created_at": 1722769557708, // 任务创建时间，Unix时间戳、单位ms
      "updated_at": 1722769557708 // 任务更新时间，Unix时间戳、单位ms
    }
  ]
}
```

---

## 删除自定义音色

### 接口概览

- Method: `POST`
- Path: `/v1/general/delete-voices`
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
| `voice_id` | string | 是 | - | - | 待删除的音色的 ID，仅支持删除自定义音色 |

### Request Example

```bash
curl --request POST \
  --url https://api-beijing.klingai.com/v1/general/delete-voices \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
    "voice_id": "850087542757535834"
  }'
```

### Response Example

```json
{
  "code": 0, // 错误码；具体定义见错误码
  "message": "string", // 错误信息
  "request_id": "string", // 请求ID，系统生成，用于跟踪请求、排查问题
  "data": {
    "task_id": "string", // 任务ID，系统生成
    "task_status": "string" // 任务状态，枚举值：submitted（已提交）、processing（处理中）、succeed（成功）、failed（失败）
  }
}
```
