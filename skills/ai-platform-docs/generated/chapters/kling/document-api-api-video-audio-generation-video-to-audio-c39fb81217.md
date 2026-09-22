<!-- Official source: https://klingai.com/document-api/api/video/audio-generation/video-to-audio.md -->
<!-- Source SHA-256: e9ffad2c0daefb4f173ab43f2e75992316c6968873d707575ca3444ad9b05d3a -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://klingai.com/document-api/llms.txt
> Use this file to discover all available pages before exploring further.

# 视频生音效

> 来源: https://klingai.com/document-api/api/video/audio-generation/video-to-audio
> 语言: zh
> 当前 Tab: 视频生音效
> 同组 Tab: 文生音效 / 视频生音效
> 此内容为面向 LLM 优化的 Markdown，已展开页面内 Tab，并省略页面目录、复制按钮等 UI 控件。

---

## 创建任务

### 接口概览

- Method: `POST`
- Path: `/v1/audio/video-to-audio`
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
| `video_id` | string | 否 | - | - | 通过可灵 AI 生成的视频的 ID |
| `video_url` | string | 否 | - | - | 所上传视频的获取链接 |
| `sound_effect_prompt` | string | 否 | - | - | 音效生成提示词 |
| `bgm_prompt` | string | 否 | - | - | 配乐生成提示词 |
| `asmr_mode` | boolean | 否 | `false` | - | 是否开启 ASMR 模式；该模式会增强细节音效，适合高沉浸内容场景 |
| `external_task_id` | string | 否 | - | - | 自定义任务 ID |
| `callback_url` | string | 否 | - | - | 本次任务结果回调通知地址，如果配置，服务端会在任务状态发生变更时主动通知 |

#### Request Body 字段补充说明

- `video_id`: 与 video_url 参数二选一填写，不能同时为空，也不能同时有值
- `video_id`: 仅支持 30 天内生成并且长度在 3.0 秒-20.0 秒的视频
- `video_url`: 与 video_id 参数二选一填写，不能同时为空，也不能同时有值
- `video_url`: 视频格式仅支持 MP4/MOV，文件大小≤100M，视频长度在 3.0 秒-20.0 秒
- `sound_effect_prompt`: 不能超过 200 个字符
- `bgm_prompt`: 不能超过 200 个字符
- `asmr_mode`: true 表示开启，false 表示关闭（默认值）
- `external_task_id`: 用户自定义任务 ID，传入不会覆盖系统生成的任务 ID，但支持通过该 ID 进行任务查询
- `external_task_id`: 请注意，单用户下需要保证唯一性
- `callback_url`: 具体通知的消息 schema 见 [Callback 协议](https://klingai.com/document-api/api/get-started/callbacks)

### Request Example

```bash
curl --request POST \
  --url https://api-beijing.klingai.com/v1/audio/video-to-audio \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
    "video_url": "https://p1-kling.klingai.com/kcdn/cdn-kcdn112452/kling-qa-test/20fps-7s.mov",
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

## 查询任务（单个）

### 接口概览

- Method: `GET`
- Path: `/v1/audio/video-to-audio/{id}`
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
| `task_id` | string | 否 | - | - | 视频生音频的任务 ID |
| `external_task_id` | string | 否 | - | - | 用户自定义任务 ID |

#### Path Params 字段补充说明

- `task_id`: 请求路径参数，直接将值填写在请求路径中
- `task_id`: 与 external_task_id 两种查询方式二选一
- `external_task_id`: 创建任务时填写的 external_task_id，与 task_id 两种查询方式二选一

### Request Example

```bash
curl --request GET \
  --url https://api-beijing.klingai.com/v1/audio/video-to-audio/{task_id} \
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
      "external_task_id": "string", // 客户自定义任务ID
      "parent_video": { // 原始视频信息
        "id": "string", // 原始视频ID
        "url": "string", // 原始视频URL
        "duration": "string" // 原始视频时长，单位s（秒）
      }
    },
    "task_result": {
      "videos": [
        {
          "id": "string", // 生成的视频ID；全局唯一
          "url": "string", // 生成视频的URL（请注意，为保障信息安全，生成的图片/视频会在30天后被清理，请及时转存）
          "duration": "string" // 视频总时长，单位s（秒）
        }
      ],
      "audios": [
        {
          "id": "string", // 生成的音频ID；全局唯一，将在30天后被清理
          "url_mp3": "string", // 生成音频的MP3格式URL（请注意，为保障信息安全，生成的音频会在30天后被清理，请及时转存）
          "url_wav": "string", // 生成音频的WAV格式URL（请注意，为保障信息安全，生成的音频会在30天后被清理，请及时转存）
          "duration_mp3": "string", // MP3格式音频总时长，单位s（秒）
          "duration_wav": "string" // WAV格式音频总时长，单位s（秒）
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

## 查询任务（列表）

### 接口概览

- Method: `GET`
- Path: `/v1/audio/video-to-audio`
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
  --url 'https://api-beijing.klingai.com/v1/audio/video-to-audio?pageNum=1&pageSize=30' \
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
        "external_task_id": "string", // 客户自定义任务ID
        "parent_video": { // 原始视频信息
          "id": "string", // 原始视频ID
          "url": "string", // 原始视频URL
          "duration": "string" // 原始视频时长，单位s（秒）
        }
      },
      "task_result": {
        "videos": [
          {
            "id": "string", // 生成的视频ID；全局唯一
            "url": "string", // 生成视频的URL（请注意，为保障信息安全，生成的图片/视频会在30天后被清理，请及时转存）
            "duration": "string" // 视频总时长，单位s（秒）
          }
        ],
        "audios": [
          {
            "id": "string", // 生成的音频ID；全局唯一，将在30天后被清理
            "url_mp3": "string", // 生成音频的MP3格式URL（请注意，为保障信息安全，生成的音频会在30天后被清理，请及时转存）
            "url_wav": "string", // 生成音频的WAV格式URL（请注意，为保障信息安全，生成的音频会在30天后被清理，请及时转存）
            "duration_mp3": "string", // MP3格式音频总时长，单位s（秒）
            "duration_wav": "string" // WAV格式音频总时长，单位s（秒）
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
