<!-- Official source: https://klingai.com/document-api/api/video/avatar.md -->
<!-- Source SHA-256: 2dfa05345dfdc6d2d2f8325b52810f8117a4cba119b5ff39cba7b09ee2fc3f30 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://klingai.com/document-api/llms.txt
> Use this file to discover all available pages before exploring further.

# 数字人

> 来源: https://klingai.com/document-api/api/video/avatar
> 语言: zh
> 当前 Tab: 数字人
> 同组 Tab: 数字人 / 语音合成
> 此内容为面向 LLM 优化的 Markdown，已展开页面内 Tab，并省略页面目录、复制按钮等 UI 控件。

---

## 创建任务

### 接口概览

- Method: `POST`
- Path: `/v1/videos/avatar/image2video`
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
| `image` | string | 是 | - | - | 数字人参考图 |
| `audio_id` | string | 否 | - | - | 通过试听接口生成的音频的 ID |
| `sound_file` | string | 否 | - | - | 音频文件 |
| `prompt` | string | 否 | - | - | 正向文本提示词 |
| `mode` | string | 否 | `std` | `std`, `pro` | 生成视频的模式 |
| `watermark_info` | object | 否 | - | - | 是否同时生成含水印的结果 |
| `callback_url` | string | 否 | - | - | 本次任务结果回调通知地址，如果配置，服务端会在任务状态发生变更时主动通知 |
| `external_task_id` | string | 否 | - | - | 自定义任务 ID |

#### Request Body 字段补充说明

- `image`: 支持传入图片 Base64 编码或图片 URL（确保可访问）
- `image`: **Base64 编码说明：**
  请注意，若您使用base64的方式，请确保您传递的所有图像数据参数均采用Base64编码格式。使用 Base64 时，请不要添加任何前缀如 `data:image/png;base64,`，只需提供 Base64 编码字符串本身。
  
  **正确示例：**
  ```plaintext
  iVBORw0KGgoAAAANSUhEUgAAAAUA...
  ```
  
  **错误示例：**
  ```plaintext
  data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA...
  ```
- `image`: 图片格式支持 .jpg / .jpeg / .png
- `image`: 图片文件大小不能超过 10MB，图片宽高尺寸不小于 300px，图片宽高比介于 1:2.5 ~ 2.5:1 之间
- `audio_id`: 仅支持使用 30 天内生成的、时长不短于 2 秒且不超过 300 秒的音频
- `audio_id`: `audio_id`、`sound_file` 参数二选一，不能同时为空，也不能同时有值
- `sound_file`: 支持传入音频 Base64 编码或音频 URL（确保可访问）
- `sound_file`: 音频文件支持 .mp3/.wav/.m4a/.aac，文件大小不超过 5MB，格式不匹配或文件过大会返回错误码等信息
- `sound_file`: 仅支持使用时长不短于 2 秒且不长于 300 秒的音频
- `sound_file`: `audio_id`、`sound_file` 参数二选一，不能同时为空，也不能同时有值
- `sound_file`: 系统会校验音频内容，如有问题会返回错误码等信息
- `prompt`: 可定义数字人动作、情绪及运镜等
- `prompt`: 不能超过 2500 个字符
- `mode`: `std`：标准模式，基础模式，性价比高
- `mode`: `pro`：专家模式（高品质），高表现模式，生成视频质量更佳
- `mode`: > 不同模型版本、视频模式支持范围不同，详见 [能力地图](https://klingai.com/document-api/guides/capability-map/video)
- `watermark_info`: 通过enabled参数定义，具体格式如下：
  ```json
   "watermark_info": { "enabled": boolean } 
  ```
- `watermark_info`: true 为生成，false 为不生成
- `watermark_info`: 暂不支持自定义水印
- `callback_url`: 具体通知的消息 schema 见 [Callback 协议](https://klingai.com/document-api/api/get-started/callbacks)
- `external_task_id`: 用户自定义任务 ID，传入不会覆盖系统生成的任务 ID，但支持通过该 ID 进行任务查询
- `external_task_id`: 请注意，单用户下需要保证唯一性

### Request Example

```bash
curl --request POST \
  --url https://api-beijing.klingai.com/v1/videos/avatar/image2video \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
    "image": "https://p1-kling.klingai.com/kcdn/cdn-kcdn112452/kling-qa-test/pink_boy.png",
    "sound_file": "https://p1-kling.klingai.com/kcdn/cdn-kcdn112452/kling-qa-test/go-to-world.mp3",
    "prompt": "一边说话，一边兴奋的摇头晃脑，最后伸手握拳，决定出发，蹦蹦跳跳很开心",
    "mode": "std",
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
- Path: `/v1/videos/avatar/image2video/{id}`
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
| `task_id` | string | 否 | - | - | 数字人的任务 ID，直接将值填写在请求路径中 |
| `external_task_id` | string | 否 | - | - | 数字人的自定义任务ID。直接在请求路径中填写值，与task_id两种查询方式二选一 |

### Request Example

```bash
curl --request GET \
  --url https://api-beijing.klingai.com/v1/videos/avatar/image2video/{task_id} \
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
      "videos": [
        {
          "id": "string", // 生成的视频ID；全局唯一
          "url": "string", // 生成视频的URL（请注意，为保障信息安全，生成的图片/视频会在30天后被清理，请及时转存）
          "watermark_url": "string", // 含水印视频下载URL，防盗链格式
          "duration": "string" // 视频总时长，单位s
        }
      ]
    },
    "watermark_info": {
      "enabled": boolean
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
- Path: `/v1/videos/avatar/image2video`
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
  --url 'https://api-beijing.klingai.com/v1/videos/avatar/image2video?pageNum=1&pageSize=30' \
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
        "videos": [
          {
            "id": "string", // 生成的视频ID；全局唯一
            "url": "string", // 生成视频的URL（请注意，为保障信息安全，生成的图片/视频会在30天后被清理，请及时转存）
            "watermark_url": "string", // 含水印视频下载URL，防盗链格式
            "duration": "string" // 视频总时长，单位s
          }
        ]
      },
      "watermark_info": {
        "enabled": boolean
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
