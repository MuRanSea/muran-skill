<!-- Official source: https://klingai.com/document-api/api/image/2-1/image-generation.md -->
<!-- Source SHA-256: bdbeac437c09d49f507dfa9af7b6fc01e6de6366c257124079de05ee55824c70 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://klingai.com/document-api/llms.txt
> Use this file to discover all available pages before exploring further.

# 文生图/单图生图

> 来源: https://klingai.com/document-api/api/image/2-1/image-generation
> 语言: zh
> 当前 Tab: 文生图/单图生图
> 同组 Tab: 文生图/单图生图 / 多图参考生图
> 此内容为面向 LLM 优化的 Markdown，已展开页面内 Tab，并省略页面目录、复制按钮等 UI 控件。

---

## 创建任务

### 接口概览

- Method: `POST`
- Path: `/v1/images/generations`
- Auth: `Authorization: Bearer <API_KEY>`
- Content-Type: `application/json`

### 说明

> 请您注意，为了保持命名统一，原 model 字段变更为 model_name字段，未来请您使用该字段来指定需要调用的模型版本。
>
> 同时，我们保持了行为上的向前兼容，如您继续使用原 model字段，不会对接口调用有任何影响、不会有任何异常，等价于 model_name为空时的默认行为（即调用V1模型）

### Headers

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `Content-Type` | string | 是 | `application/json` | - | 数据交换格式 |
| `Authorization` | string | 是 | - | - | 鉴权信息，参考接口鉴权 |

### Request Body

| 字段路径 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `model_name` | string | 否 | `kling-v3` | `kling-v2-1`, `kling-v3` | 模型名称 |
| `prompt` | string | 是 | - | - | 正向文本提示词 |
| `negative_prompt` | string | 否 | - | - | 负向文本提示词 |
| `image` | string | 否 | - | - | 参考图像 |
| `image_reference` | string | 否 | - | `subject`, `face` | 图片参考类型 |
| `image_fidelity` | float | 否 | `0.5` | - | 生成过程中对用户上传图片的参考强度 |
| `human_fidelity` | float | 否 | `0.45` | - | 面部参考强度，即参考图中人物五官相似度 |
| `element_list` | array | 否 | - | - | 主体参考列表，基于主体库中主体的ID配置 |
| `element_list[].element_id` | long | 是 | - | - | 主体ID |
| `resolution` | string | 否 | `1k` | `1k`, `2k` | 生成图片的清晰度 |
| `n` | int | 否 | `1` | - | 生成图片数量 |
| `aspect_ratio` | string | 否 | `16:9` | `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `3:2`, `2:3`, `21:9` | 生成图片的画面纵横比（宽:高） |
| `watermark_info` | object | 否 | - | - | 是否同时生成含水印的结果 |
| `callback_url` | string | 否 | - | - | 本次任务结果回调通知地址，如果配置，服务端会在任务状态发生变更时主动通知。 |
| `external_task_id` | string | 否 | - | - | 自定义任务 ID |

#### Request Body 字段补充说明

- `prompt`: 不能超过 2500 个字符
- `negative_prompt`: 不能超过 2500 个字符
- `negative_prompt`: 注：图生图（即 image 字段不为空时）场景下，不支持负向提示词
- `image`: 支持传入图片 Base64 编码或图片 URL（确保可访问）
- `image`: Base64 编码说明：
  请注意，若您使用base64的方式，请确保您传递的所有图像数据参数均采用Base64编码格式。使用 Base64 时，请不要添加任何前缀如 `data:image/png;base64,`，只需提供 Base64 编码字符串本身。
  
  正确示例：
  ```plaintext
  iVBORw0KGgoAAAANSUhEUgAAAAUA...
  ```
  
  错误示例：
  ```plaintext
  data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA...
  ```
- `image`: 图片格式支持 .jpg / .jpeg / .png
- `image`: 图片文件大小不能超过 10MB，图片宽高尺寸不小于 300px，图片宽高比介于 1:2.5 ~ 2.5:1 之间
- `image`: image_reference 参数不为空时，当前参数必填
- `image_reference`: `subject`（角色特征参考）, `face`（人物长相参考）
- `image_reference`: 使用 `face`（人物长相参考）时，上传图片需仅含 1 张人脸
- `image_fidelity`: 取值范围：[0, 1]，数值越大参考强度越大
- `image_fidelity`: > 仅 kling-v2-1 支持当前参数
- `human_fidelity`: 仅 image_reference 参数为 subject 时生效
- `human_fidelity`: 取值范围：[0, 1]，数值越大参考强度越大
- `human_fidelity`: > 仅 kling-v2-1 支持当前参数
- `element_list`: 用 key:value 承载，格式如上：
  ```json
  "element_list":[
    { "element_id": long },
    { "element_id": long }
  ]
  ```
- `element_list`: 参考主体数量与参考图片数量有关，参考主体数量和参考图片数量之和不得超过 10
- `resolution`: `1k`：1K 标清, `2k`：2K 高清
- `resolution`: > 不同模型版本支持范围不同，详见 [能力地图](https://klingai.com/document-api/guides/capability-map/image)
- `n`: 取值范围：[1, 9]
- `aspect_ratio`: > 不同模型版本支持的范围不同，详见 [能力地图](https://klingai.com/document-api/guides/capability-map/image)
- `watermark_info`: 通过enabled参数定义，具体格式如下：
  ```json
   "watermark_info": { "enabled": boolean } 
  ```
- `watermark_info`: true 为生成，false 为不生成
- `watermark_info`: 暂不支持自定义水印
- `callback_url`: 具体通知的消息 schema 见 [Callback 协议](https://klingai.com/document-api/api/get-started/callbacks)
- `external_task_id`: 传入不会覆盖系统生成的任务 ID，但支持通过该 ID 进行任务查询
- `external_task_id`: 请注意，单用户下需要保证唯一性

### Request Example

```bash
curl --request POST \
  --url https://api-beijing.klingai.com/v1/images/generations \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
    "model_name": "kling-v2-1",
    "prompt": "生成皮克斯风格的小狗",
    "negative_prompt": "",
    "image": "https://p1-kling.klingai.com/kcdn/cdn-kcdn112452/kling-qa-test/dog.png",
    "n": 2,
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
    "task_info": { // 任务创建时的参数信息
      "external_task_id": "string" // 客户自定义任务ID
    },
    "created_at": 1722769557708, // 任务创建时间，Unix时间戳、单位ms
    "updated_at": 1722769557708 // 任务更新时间，Unix时间戳、单位ms
  }
}
```

---

## 查询任务（单个）

### 接口概览

- Method: `GET`
- Path: `/v1/images/generations/{id}`
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
  --url https://api-beijing.klingai.com/v1/images/generations/{id} \
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
    "final_unit_deduction": "string", // 任务最终扣减积分数值
    "final_balance_deduction": { // 额度扣减信息
      "quota": "string", // 额度扣减折扣价
      "list_price": "string" // 额度扣减刊例价
    },
    "watermark_info": {
      "enabled": boolean
    },
    "task_info": { // 任务创建时的参数信息
      "external_task_id": "string" // 客户自定义任务ID
    },
    "created_at": 1722769557708, // 任务创建时间，Unix时间戳、单位ms
    "updated_at": 1722769557708, // 任务更新时间，Unix时间戳、单位ms
    "task_result": {
      "images": [
        {
          "index": 0, // 图片编号，0-9
          "url": "string", // 生成图片的URL（请注意，为保障信息安全，生成的图片/视频会在30天后被清理，请及时转存）
          "watermark_url": "string" // 含水印图片下载URL，防盗链格式
        }
      ]
    }
  }
}
```

---

## 查询任务（列表）

### 接口概览

- Method: `GET`
- Path: `/v1/images/generations`
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
  --url 'https://api-beijing.klingai.com/v1/images/generations?pageNum=1&pageSize=30' \
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
      "final_unit_deduction": "string", // 任务最终扣减积分数值
      "final_balance_deduction": { // 额度扣减信息
        "quota": "string", // 额度扣减折扣价
        "list_price": "string" // 额度扣减刊例价
      },
      "watermark_info": {
        "enabled": boolean
      },
      "task_info": { // 任务创建时的参数信息
        "external_task_id": "string" // 客户自定义任务ID
      },
      "created_at": 1722769557708, // 任务创建时间，Unix时间戳、单位ms
      "updated_at": 1722769557708, // 任务更新时间，Unix时间戳、单位ms
      "task_result": {
        "images": [
          {
            "index": 0, // 图片编号，0-9
            "url": "string", // 生成图片的URL（请注意，为保障信息安全，生成的图片/视频会在30天后被清理，请及时转存）
            "watermark_url": "string" // 含水印图片下载URL，防盗链格式
          }
        ]
      }
    }
  ]
}
```
