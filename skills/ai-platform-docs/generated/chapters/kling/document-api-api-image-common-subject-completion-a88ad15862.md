<!-- Official source: https://klingai.com/document-api/api/image/common/subject-completion.md -->
<!-- Source SHA-256: 480db2d63c82939ebef713751fb891ed2a350ba5ec31f601b19ca1bad99851d9 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://klingai.com/document-api/llms.txt
> Use this file to discover all available pages before exploring further.

# 智能补全主体图

> 来源: https://klingai.com/document-api/api/image/common/subject-completion
> 语言: zh
> 当前 Tab: 智能补全主体图
> 同组 Tab: 智能补全主体图 / 扩图
> 此内容为面向 LLM 优化的 Markdown，已展开页面内 Tab，并省略页面目录、复制按钮等 UI 控件。

---

## 创建任务

### 接口概览

- Method: `POST`
- Path: `/v1/general/ai-multi-shot`
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
| `element_frontal_image` | string | 是 | - | - | 主体正面参考图 |
| `callback_url` | string | 否 | - | - | 本次任务结果回调通知地址，如果配置，服务端会在任务状态发生变更时主动通知 |
| `external_task_id` | string | 否 | - | - | 自定义任务ID |

#### Request Body 字段补充说明

- `element_frontal_image`: 支持传入图片Base64编码或图片URL（确保可访问）
- `element_frontal_image`: 图片格式支持.jpg / .jpeg / .png
- `element_frontal_image`: 图片文件大小不能超过10MB，图片宽高尺寸不小于300px，图片宽高比要在1:2.5 ~ 2.5:1之间
- `callback_url`: 具体通知的消息schema见 [Callback协议](https://klingai.com/document-api/api/get-started/callbacks)
- `external_task_id`: 用户自定义任务ID，传入不会覆盖系统生成的任务ID，但支持通过该ID进行任务查询
- `external_task_id`: 请注意，单用户下需要保证唯一性

### Request Example

```bash
curl --request POST \
  --url https://api-beijing.klingai.com/v1/general/ai-multi-shot \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
    "element_frontal_image": "https://v1-kling.klingai.com/kcdn/cdn-kcdn112452/kling-qa-test/multi-1.png",
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
    "task_status": "string", // 任务状态，枚举值：submitted（已提交）、processing（处理中）、succeed（成功）、failed（失败）
    "task_info": { //任务创建时的参数信息
      "external_task_id": "string" //客户自定义任务ID
    },
    "created_at": 1722769557708, // 任务创建时间，Unix时间戳、单位ms
    "updated_at": 1722769557708 //任务更新时间，Unix时间戳、单位ms
  }
}
```

---

## 查询任务（单个）

### 接口概览

- Method: `GET`
- Path: `/v1/general/ai-multi-shot/{id}`
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
| `task_id` | string | 是 | - | - | 任务ID，请求路径参数，直接将值填写在请求路径中 |

### Request Example

```bash
curl --request GET \
  --url https://api-beijing.klingai.com/v1/general/ai-multi-shot/{task_id} \
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
      "images": [
        {
          "index": 0, // 图片结果编号，0-2
          "url_1": "string", // 生成图片的URL，防盗链格式（请注意，为保障信息安全，生成的图片/视频会在30天后被清理，请及时转存）
          "url_2": "string", // 生成图片的URL，防盗链格式（请注意，为保障信息安全，生成的图片/视频会在30天后被清理，请及时转存）
          "url_3": "string" // 生成图片的URL，防盗链格式（请注意，为保障信息安全，生成的图片/视频会在30天后被清理，请及时转存）
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
- Path: `/v1/general/ai-multi-shot`
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
  --url 'https://api-beijing.klingai.com/v1/general/ai-multi-shot?pageNum=1&pageSize=30' \
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
        "external_task_id": "string" //客户自定义任务ID
      },
      "task_result": {
        "images": [
          {
            "index": 0, // 图片结果编号，0-2
            "url_1": "string", // 生成图片的URL，防盗链格式（请注意，为保障信息安全，生成的图片/视频会在30天后被清理，请及时转存）
            "url_2": "string", // 生成图片的URL，防盗链格式（请注意，为保障信息安全，生成的图片/视频会在30天后被清理，请及时转存）
            "url_3": "string" //生成图片的URL，防盗链格式（请注意，为保障信息安全，生成的图片/视频会在30天后被清理，请及时转存）
          }
        ]
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
