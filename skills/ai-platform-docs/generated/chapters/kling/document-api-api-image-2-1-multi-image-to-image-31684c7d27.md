<!-- Official source: https://klingai.com/document-api/api/image/2-1/multi-image-to-image.md -->
<!-- Source SHA-256: 5bcfa897ad2e81bad8f689837a17d6a2f30d0899794c0c2282678ea86416f9b6 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://klingai.com/document-api/llms.txt
> Use this file to discover all available pages before exploring further.

# 多图参考生图

> 来源: https://klingai.com/document-api/api/image/2-1/multi-image-to-image
> 语言: zh
> 当前 Tab: 多图参考生图
> 同组 Tab: 文生图/单图生图 / 多图参考生图
> 此内容为面向 LLM 优化的 Markdown，已展开页面内 Tab，并省略页面目录、复制按钮等 UI 控件。

---

## 创建任务

### 接口概览

- Method: `POST`
- Path: `/v1/images/multi-image2image`
- Auth: `Authorization: Bearer <API_KEY>`
- Content-Type: `application/json`

### 说明

基于多张参考图片（主体、场景、风格）生成图像。

### Headers

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `Content-Type` | string | 是 | `application/json` | - | 数据交换格式 |
| `Authorization` | string | 是 | - | - | 鉴权信息，参考接口鉴权 |

### Request Body

| 字段路径 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `model_name` | string | 否 | `kling-v2-1` | `kling-v2-1` | 模型名称 |
| `prompt` | string | 否 | - | - | 正向文本提示词 |
| `subject_image_list` | array | 是 | - | - | 主体参考图片列表 |
| `subject_image_list[].subject_image` | string | 是 | - | - | 主体图片 URL 或 Base64 字符串 |
| `scene_image` | string | 否 | - | - | 场景参考图 |
| `style_image` | string | 否 | - | - | 风格参考图 |
| `n` | int | 否 | `1` | - | 生成图片数量 |
| `aspect_ratio` | string | 否 | `16:9` | `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `3:2`, `2:3`, `21:9` | 生成图片的画面纵横比（宽:高） |
| `watermark_info` | object | 否 | - | - | 是否同时生成含水印的结果 |
| `callback_url` | string | 否 | - | - | 本次任务结果回调通知地址，如果配置，服务端会在任务状态发生变更时主动通知 |
| `external_task_id` | string | 否 | - | - | 自定义任务 ID |

#### Request Body 字段补充说明

- `prompt`: 不能超过 2500 个字符
- `subject_image_list`: 最多支持 4 张图片，最少支持 1 张图片，用 key:value 承载，如下：
  ```json
  "subject_image_list":[
    { "subject_image":"image_url" },
    { "subject_image":"image_url" },
    { "subject_image":"image_url" },
    { "subject_image":"image_url" }
  ]
  ```
- `subject_image_list`: API 端无裁剪逻辑，请直接上传已选主体后的图片
- `subject_image_list`: 支持传入图片 Base64 编码或图片 URL（确保可访问）
- `subject_image_list`: 注意：若您使用 Base64 方式，请不要在 Base64 编码字符串前添加任何前缀（如 `data:image/png;base64,`），直接传递 Base64 编码后的字符串即可。
- `subject_image_list`: **正确的 Base64 编码参数：**
  ```plaintext
  iVBORw0KGgoAAAANSUhEUgAAAAUA...
  ```
- `subject_image_list`: 错误的 Base64 编码参数（包含 data: 前缀）：
  ```plaintext
  data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA...
  ```
- `subject_image_list`: 图片格式支持 .jpg / .jpeg / .png
- `subject_image_list`: 图片文件大小不能超过 10MB，图片宽高尺寸不小于 300px，图片宽高比要在 1:2.5 ~ 2.5:1 之间
- `scene_image`: 支持传入图片 Base64 编码或图片 URL（确保可访问）
- `scene_image`: 注意：若您使用 Base64 方式，请不要在 Base64 编码字符串前添加任何前缀（如 `data:image/png;base64,`），直接传递 Base64 编码后的字符串即可。
- `scene_image`: 正确的 Base64 编码参数：
  ```plaintext
  iVBORw0KGgoAAAANSUhEUgAAAAUA...
  ```
- `scene_image`: 错误的 Base64 编码参数（包含 data: 前缀）：
  ```plaintext
  data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA...
  ```
- `scene_image`: 图片格式支持 .jpg / .jpeg / .png
- `scene_image`: 图片文件大小不能超过 10MB，图片宽高尺寸不小于 300px，图片宽高比要在 1:2.5 ~ 2.5:1 之间
- `style_image`: 支持传入图片 Base64 编码或图片 URL（确保可访问）
- `style_image`: 注意：若您使用 Base64 方式，请不要在 Base64 编码字符串前添加任何前缀（如 `data:image/png;base64,`），直接传递 Base64 编码后的字符串即可。
- `style_image`: 正确的 Base64 编码参数：
  ```plaintext
  iVBORw0KGgoAAAANSUhEUgAAAAUA...
  ```
- `style_image`: 错误的 Base64 编码参数（包含 data: 前缀）：
  ```plaintext
  data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA...
  ```
- `style_image`: 图片格式支持 .jpg / .jpeg / .png
- `style_image`: 图片文件大小不能超过 10MB，图片宽高尺寸不小于 300px，图片宽高比要在 1:2.5 ~ 2.5:1 之间
- `n`: 取值范围：[1, 9]
- `aspect_ratio`: > 不同模型版本支持范围不同，详见 [能力地图](https://klingai.com/document-api/guides/capability-map/image)
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
  --url https://api-beijing.klingai.com/v1/images/multi-image2image \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
    "model_name": "kling-v2-1",
    "prompt": "身着飘逸红色连衣裙,在草原上，吉卜力风格。",
    "negative_prompt": "",
    "subject_image_list": [
      { "subject_image": "https://v1-kling.klingai.com/kcdn/cdn-kcdn112452/kling-qa-test/multi-1.png" },
      { "subject_image": "https://v1-kling.klingai.com/kcdn/cdn-kcdn112452/kling-qa-test/multi-2.png" }
    ],
    "scene_image": "https://v1-kling.klingai.com/kcdn/cdn-kcdn112452/kling-qa-test/background.jpeg",
    "style_image": "https://v1-kling.klingai.com/kcdn/cdn-kcdn112452/kling-qa-test/16x9_jipuli.png",
    "n": 2,
    "aspect_ratio": "9:16"
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
- Path: `/v1/images/multi-image2image/{id}`
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
| `task_id` | string | 是 | - | - | 图片生成的任务ID。请求路径参数，直接将值填写在请求路径中。与 external_task_id 两种查询方式二选一 |
| `external_task_id` | string | 否 | - | - | 用户自定义任务 ID |

#### Path Params 字段补充说明

- `external_task_id`: 创建任务时填写的 external_task_id，与 task_id 两种查询方式二选一
  - 请注意，单用户下需要保证唯一性

### Request Example

```bash
curl --request GET \
  --url https://api-beijing.klingai.com/v1/images/multi-image2image/{id} \
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
    "task_info": { //任务创建时的参数信息
      "external_task_id": "string" //客户自定义任务ID
    },
    "task_status": "string", // 任务状态，枚举值：submitted（已提交）、processing（处理中）、succeed（成功）、failed（失败）
    "task_status_msg": "string", // 任务状态信息，当任务失败时展示失败原因（如触发平台的内容风控等）
    "final_unit_deduction": "string", // 任务最终扣减积分数值
    "final_balance_deduction": { // 额度扣减信息
      "quota": "string", // 额度扣减折扣价
      "list_price": "string" // 额度扣减刊例价
    },
    "watermark_info": { "enabled": boolean },
    "created_at": 1722769557708, // 任务创建时间，Unix时间戳、单位ms
    "updated_at": 1722769557708, // 任务更新时间，Unix时间戳、单位ms
    "task_result": {
      "images": [
        {
          "index": 0, // 图片编号，0-9
          "url": "string", // 生成图片的URL，例如：...（请注意，为保障信息安全，生成的图片/视频会在30天后被清理，请及时转存）
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
- Path: `/v1/images/multi-image2image`
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
  --url 'https://api-beijing.klingai.com/v1/images/multi-image2image?pageNum=1&pageSize=30' \
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
      "task_info": { //任务创建时的参数信息
        "external_task_id": "string" //客户自定义任务ID
      },
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
      "created_at": 1722769557708, // 任务创建时间，Unix时间戳、单位ms
      "updated_at": 1722769557708, // 任务更新时间，Unix时间戳、单位ms
      "task_result": {
        "images": [
          {
            "index": 0, // 图片编号，0-9
            "url": "string", // 生成图片的URL，例如：...（请注意，为保障信息安全，生成的图片/视频会在30天后被清理，请及时转存）
            "watermark_url": "string" // 含水印图片下载URL，防盗链格式
          }
        ]
      }
    }
  ]
}
```
