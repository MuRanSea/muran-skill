<!-- Official source: https://klingai.com/document-api/api/video/lip-sync.md -->
<!-- Source SHA-256: c81c058b6825440d96d97b737c13ddfb5882f4456851bc40cf42f6c32c362bc0 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://klingai.com/document-api/llms.txt
> Use this file to discover all available pages before exploring further.

# 对口型

> 来源: https://klingai.com/document-api/api/video/lip-sync
> 语言: zh
> 当前 Tab: 对口型
> 同组 Tab: 对口型 / 人脸识别
> 此内容为面向 LLM 优化的 Markdown，已展开页面内 Tab，并省略页面目录、复制按钮等 UI 控件。

---

## 创建任务

### 接口概览

- Method: `POST`
- Path: `/v1/videos/advanced-lip-sync`
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
| `session_id` | string | 是 | - | - | 会话 ID，会基于对口型人脸识别接口生成 |
| `face_choose` | array | 是 | - | - | 指定人脸对口型 |
| `face_choose[].face_id` | string | 是 | - | - | 人脸 ID |
| `face_choose[].audio_id` | string | 否 | - | - | 通过试听接口生成的音频的 ID |
| `face_choose[].sound_file` | string | 否 | - | - | 音频文件 |
| `face_choose[].sound_start_time` | long | 是 | - | - | 音频裁剪起点时间 |
| `face_choose[].sound_end_time` | long | 是 | - | - | 音频裁剪终点时间 |
| `face_choose[].sound_insert_time` | long | 是 | - | - | 裁剪后音频插入时间 |
| `face_choose[].sound_volume` | float | 否 | `1` | - | 音频音量大小；值越大，音量越大 |
| `face_choose[].original_audio_volume` | float | 否 | `1` | - | 原始视频音量大小；值越大，音量越大 |
| `watermark_info` | object | 否 | - | - | 是否同时生成含水印的结果 |
| `external_task_id` | string | 否 | - | - | 自定义任务 ID |
| `callback_url` | string | 否 | - | - | 本次任务结果回调通知地址，如果配置，服务端会在任务状态发生变更时主动通知 |

#### Request Body 字段补充说明

- `session_id`: 由[人脸识别](https://klingai.com/document-api/api/video/lip-sync/face-detection)接口生成
- `face_choose`: 包括人脸 ID、口型参考等内容等
- `face_choose`: 暂时仅支持指定单人对口型
- `face_choose[].face_id`: 由人脸识别接口返回
- `face_choose[].audio_id`: 仅支持使用 30 天内生成的、时长不短于 2 秒且不超过 60 秒的音频
- `face_choose[].audio_id`: audio_id、sound_file 参数二选一，不能同时为空，也不能同时有值
- `face_choose[].sound_file`: 支持传入音频 Base64 编码或图音频 URL（确保可访问）
- `face_choose[].sound_file`: 音频文件支持 .mp3/.wav/.m4a/.aac，文件大小不超过 5MB，格式不匹配或文件过大会返回错误码等信息
- `face_choose[].sound_file`: 仅支持使用时长不短于 2 秒且不长于 60 秒的音频
- `face_choose[].sound_file`: audio_id、sound_file 参数二选一，不能同时为空，也不能同时有值
- `face_choose[].sound_file`: 系统会校验音频内容，如有问题会返回错误码等信息
- `face_choose[].sound_start_time`: 以原始音频开始时间为准，开始时间为 0 分 0 秒，单位 ms
- `face_choose[].sound_start_time`: 起点之前的音频会被裁剪，裁剪后音频不得短于 2 秒
- `face_choose[].sound_end_time`: 以原始音频开始时间为准，开始时间为 0 分 0 秒，单位 ms
- `face_choose[].sound_end_time`: 终点之后的音频会被裁剪，裁剪后音频不得短于 2 秒
- `face_choose[].sound_end_time`: 终点时间不得晚于原始音频总时长
- `face_choose[].sound_insert_time`: 以视频开始时间为准，视频开始时间为 0 分 0 秒，单位 ms
- `face_choose[].sound_insert_time`: 插入音频的时间范围与该人脸可对口型时间区间至少重合 2 秒时长
- `face_choose[].sound_insert_time`: 插入音频的开始时间不得早于视频开始时间，插入音频的结束时间不得晚于视频结束时间
- `face_choose[].sound_volume`: 取值范围：[0, 2]
- `face_choose[].original_audio_volume`: 取值范围：[0, 2]
- `face_choose[].original_audio_volume`: 原视频无声时，当前参数无效果
- `watermark_info`: 通过enabled参数定义，具体格式如下：
  ```json
   "watermark_info": { "enabled": boolean } 
  ```
- `watermark_info`: true 为生成，false 为不生成
- `watermark_info`: 暂不支持自定义水印
- `external_task_id`: 用户自定义任务 ID，传入不会覆盖系统生成的任务 ID，但支持通过该 ID 进行任务查询
- `external_task_id`: 请注意，单用户下需要保证唯一性
- `callback_url`: 具体通知的消息 schema 见 [Callback 协议](https://klingai.com/document-api/api/get-started/callbacks)

### Request Example

```bash
curl --request POST \
  --url https://api-beijing.klingai.com/v1/videos/advanced-lip-sync \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
    "session_id": "850508686686064678",
    "face_choose": [
      {
        "face_id": "0",
        "sound_file": "https://p1-kling.klingai.com/kcdn/cdn-kcdn112452/kling-qa-test/go-to-world.mp3",
        "sound_insert_time": 1000,
        "sound_start_time": 0,
        "sound_end_time": 3000,
        "sound_volume": 2,
        "original_audio_volume": 2
      }
    ],
    "external_task_id": "",
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
    "task_info": { //任务创建时的参数信息
      "external_task_id": "string" //客户自定义任务ID
    },
    "task_status": "string", // 任务状态，枚举值：submitted（已提交）、processing（处理中）、succeed（成功）、failed（失败）
    "created_at": 1722769557708, // 任务创建时间，Unix时间戳、单位ms
    "updated_at": 1722769557708 //任务更新时间，Unix时间戳、单位ms
  }
}
```

---

## 查询任务（单个）

### 接口概览

- Method: `GET`
- Path: `/v1/videos/advanced-lip-sync/{id}`
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
| `task_id` | string | 否 | - | - | 对口型的任务ID。直接在请求路径中填写值。 |

### Request Example

```bash
curl --request GET \
  --url https://api-beijing.klingai.com/v1/videos/advanced-lip-sync/{task_id} \
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
    "task_info": { //任务创建时的参数信息
      "parent_video": { //原始视频信息
        "id": "string", // 原始视频ID
        "url": "string", // 原始视频URL
        "duration": "string" //原始视频时长，单位s
      }
    },
    "task_result": { //任务结果
      "videos": [ //生成的视频列表
        {
          "id": "string", // 生成的视频ID；全局唯一
          "url": "string", // 生成视频的URL（请注意，为保障信息安全，生成的图片/视频会在30天后被清理，请及时转存）
          "watermark_url": "string", // 含水印视频下载URL，防盗链格式
          "duration": "string" //视频总时长，单位s
        }
      ]
    },
    "watermark_info": {
      "enabled": boolean //是否启用水印
    },
    "final_unit_deduction": "string", // 任务最终扣减积分数值
    "final_balance_deduction": { // 额度扣减信息
      "quota": "string", // 额度扣减折扣价
      "list_price": "string" // 额度扣减刊例价
    },
    "created_at": 1722769557708, // 任务创建时间，Unix时间戳、单位ms
    "updated_at": 1722769557708 //任务更新时间，Unix时间戳、单位ms
  }
}
```

---

## 查询任务（列表）

### 接口概览

- Method: `GET`
- Path: `/v1/videos/advanced-lip-sync`
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
- `pageSize`: 取值范围：[1, 500]

### Request Example

```bash
curl --request GET \
  --url 'https://api-beijing.klingai.com/v1/videos/advanced-lip-sync?pageNum=1&pageSize=30' \
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
      "task_info": { //任务创建时的参数信息
        "parent_video": { //原始视频信息
          "id": "string", // 原始视频ID
          "url": "string", // 原始视频URL
          "duration": "string" //原始视频时长，单位s
        }
      },
      "task_result": { //任务结果
        "videos": [ //生成的视频列表
          {
            "id": "string", // 生成的视频ID；全局唯一
            "url": "string", // 生成视频的URL（请注意，为保障信息安全，生成的图片/视频会在30天后被清理，请及时转存）
            "watermark_url": "string", // 含水印视频下载URL，防盗链格式
            "duration": "string" //视频总时长，单位s
          }
        ]
      },
      "watermark_info": {
        "enabled": boolean //是否启用水印
      },
      "final_unit_deduction": "string", // 任务最终扣减积分数值
      "final_balance_deduction": { // 额度扣减信息
        "quota": "string", // 额度扣减折扣价
        "list_price": "string" // 额度扣减刊例价
      },
      "created_at": 1722769557708, // 任务创建时间，Unix时间戳、单位ms
      "updated_at": 1722769557708 //任务更新时间，Unix时间戳、单位ms
    }
  ]
}
```
