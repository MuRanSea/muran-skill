<!-- Official source: https://klingai.com/document-api/api/image/3-0-omni/image-omni.md -->
<!-- Source SHA-256: 6cdba6fdcc8bfcc27cf3938d29a6e26c8d4f1c78513dd983b2b5be46eee53d73 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://klingai.com/document-api/llms.txt
> Use this file to discover all available pages before exploring further.

# Omni 图片生成

> 来源: https://klingai.com/document-api/api/image/3-0-omni/image-omni
> 语言: zh
> 当前 Tab: Omni 图片生成
> 同组 Tab: 图片生成 / Omni 图片生成 / 主体管理
> 此内容为面向 LLM 优化的 Markdown，已展开页面内 Tab，并省略页面目录、复制按钮等 UI 控件。

---

## 创建任务

### 接口概览

- Method: `POST`
- Path: `/v1/images/omni-image`
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
| `model_name` | string | 否 | `kling-image-o1` | `kling-image-o1`, `kling-v3-omni` | 模型名称 |
| `prompt` | string | 是 | - | - | 文本提示词，可包含正向描述和负向描述 |
| `image_list` | array | 否 | - | - | 参考图列表 |
| `image_list[].image` | string | 是 | - | - | 图片 URL 或 Base64 字符串 |
| `element_list` | array | 否 | - | - | 主体参考列表，基于主体库中主体的 ID 配置 |
| `element_list[].element_id` | long | 是 | - | - | 主体库中主体的 ID |
| `resolution` | string | 否 | `1k` | `1k`, `2k`, `4k` | 生成图片的清晰度 |
| `result_type` | string | 否 | `single` | `single`, `series` | 生成结果单图/组图切换开关 |
| `n` | int | 否 | `1` | - | 生成图片数量 |
| `series_amount` | int | 否 | `4` | `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `auto` | 生成组图的图片数量 |
| `aspect_ratio` | string | 否 | `auto` | `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `3:2`, `2:3`, `21:9`, `auto` | 生成图片的画面纵横比（宽:高） |
| `watermark_info` | object | 否 | - | - | 是否同时生成含水印的结果 |
| `callback_url` | string | 否 | - | - | 本次任务结果回调通知地址，如果配置，服务端会在任务状态发生变更时主动通知 |
| `external_task_id` | string | 否 | - | - | 自定义任务 ID |

#### Request Body 字段补充说明

- `prompt`: 可将提示词模板化来满足不同的图像生成需求
- `prompt`: 不能超过 2500 个字符
- `prompt`: 通过 <<<>>> 的格式来指定某个图片，如：<<<image_1>>>
- `prompt`: 能力范围详见使用手册：[可灵 Omni 模型使用指南](https://docs.qingque.cn/d/home/eZQAOaXS_vSJtC2ykMjNfYSaa?identityId=2Cn18n4EIHT)
- `image_list`: 用 key:value 承载，如下：
  ```json
  "image_list":[
    { "image":"image_url" }
  ]
  ```
- `image_list`: 支持传入图片 Base64 编码或图片 URL（确保可访问）
- `image_list`: 图片格式支持 .jpg / .jpeg / .png
- `image_list`: 图片文件大小不能超过 10MB，图片宽高尺寸不小于 300px，图片宽高比要在 1:2.5 ~ 2.5:1 之间
- `image_list`: 参考主体数量与参考图片数量有关，参考主体数量和参考图片数量之和不得超过 10
- `image_list`: image_url 参数值不得为空
- `element_list`: 用 key:value 承载，如下：
  ```json
  "element_list":[
    { "element_id": 829836802793406551 }
  ]
  ```
- `element_list`: 参考主体数量与参考图片数量有关，参考主体数量和参考图片数量之和不得超过 10
- `element_list`: > 不同模型版本支持范围不同，详见 [能力地图](https://klingai.com/document-api/guides/capability-map/image)
- `resolution`: 1k：1K 标清
- `resolution`: 2k：2K 高清
- `resolution`: 4k：4K 高清
- `resolution`: > 不同模型版本支持范围不同，详见 [能力地图](https://klingai.com/document-api/guides/capability-map/image)
- `result_type`: > 不同模型版本支持范围不同，详见 [能力地图](https://klingai.com/document-api/guides/capability-map/image)
- `n`: 取值范围：[1, 9]
- `n`: 当 result_type 值为 series 时，当前参数无效
- `series_amount`: 其中：`auto` 为根据传入内容智能选择生成图片的数量
- `series_amount`: 使用 `auto` 时，会占用与实际生成数量对应的并发量
- `series_amount`: 当 result_type 值为 `single` 时，当前参数无效
- `series_amount`: > 不同模型版本支持范围不同，详见当前文档 [2-0 能力地图](https://klingai.com/document-api/guides/capability-map/image)
- `aspect_ratio`: 其中：`auto`为根据传入内容智能生成图片宽高比
- `aspect_ratio`: > 不同模型版本支持范围不同，详见 [能力地图](https://klingai.com/document-api/guides/capability-map/image)
- `watermark_info`: 通过enabled参数定义，具体格式如下：
  ```json
   "watermark_info": { "enabled": boolean } 
  ```
- `watermark_info`: true 为生成，false 为不生成
- `watermark_info`: 暂不支持自定义水印
- `callback_url`: 具体通知的消息schema见 [Callback协议](https://klingai.com/document-api/api/get-started/callbacks)
- `external_task_id`: 用户自定义任务 ID，传入不会覆盖系统生成的任务 ID，但支持通过该 ID 进行任务查询
- `external_task_id`: 请注意，单用户下需要保证唯一性

### Request Example

```bash
curl --request POST \
  --url https://api-beijing.klingai.com/v1/images/omni-image \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
    "model_name": "kling-image-o1",
    "prompt": "将所有图片中的人物融合到<<<object_1>>>图中",
    "element_list": [
        {
            "element_id": 829836802793406551
        }
    ],
    "image_list": [
        {
            "image": "https://v1-kling.klingai.com/kcdn/cdn-kcdn112452/kling-qa-test/multi-4.png"
        },
        {
            "image": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-qa-test/video_effects/1.png"
        },
        {
            "image": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-qa-test/video_effects/4.png"
        }
    ],
    "resolution": "2k",
    "n": 1,
    "aspect_ratio": "3:2"
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

## 调用示例

### 引入主体生成图像

```Bash
curl --location 'https://xxx/v1/images/generations' \
--header 'Authorization: Bearer xxx' \
--header 'Content-Type: application/json' \
--data '{
    "model_name": "kling-v3-omni",
    "prompt": "Generate a recommended cover for each subject <<element_1>> based on the style of the reference image <<image_1>>",
    "element_list": [
      {
        "element_id": 160
      },
      {
        "element_id": 161
      }
    ],
    "image_list": [
      {
        "image": "xxx"
      },
      {
        "image": "xxx"
      }
    ],
    "resolution": "2k",
    "result_type": "series",
    "series_amount": 2,
    "aspect_ratio": "auto",
    "external_task_id": "",
    "callback_url": ""
  }'
```

---

## 查询任务（单个）

### 接口概览

- Method: `GET`
- Path: `/v1/images/omni-image/{id}`
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
  --url https://api-beijing.klingai.com/v1/images/omni-image/{id} \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json'
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
      "external_task_id": "string" //客户自定义任务ID
    },
    "task_result": {
      "result_type": "single",
      "images": [
        {
          "index": 0, // 图片编号
          "url": "string", // 生成图片的URL，防盗链格式（请注意，为保障信息安全，生成的图片/视频会在30天后被清理，请及时转存）
          "watermark_url": "string" // 含水印图片下载URL，防盗链格式
        }
      ],
      "series_images": [
        {
          "index": 0, // 组图序号
          "url": "string", // 生成图片的URL，防盗链格式（请注意，为保障信息安全，生成的图片/视频会在30天后被清理，请及时转存）
          "watermark_url": "string" // 含水印图片下载URL，防盗链格式
        }
      ]
    },
    "watermark_info": { "enabled": boolean }, // 是否含水印
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
- Path: `/v1/images/omni-image`
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
  --url 'https://api-beijing.klingai.com/v1/images/omni-image?pageNum=1&pageSize=30' \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json'
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
      "created_at": 1722769557708, // 任务创建时间，Unix时间戳、单位ms
      "updated_at": 1722769557708, // 任务更新时间，Unix时间戳、单位ms
      "task_info": { //任务创建时的参数信息
        "external_task_id": "string" //客户自定义任务ID
      },
      "watermark_info": { "enabled": boolean },
      "task_result": {
        "result_type": "single",
        "images": [
          {
            "index": 0, // 图片编号
            "url": "string", // 生成图片的URL，防盗链格式（请注意，为保障信息安全，生成的图片/视频会在30天后被清理，请及时转存）
            "watermark_url": "string" // 含水印图片下载URL，防盗链格式
          }
        ],
        "series_images": [
          {
            "index": 0, // 组图序号
            "url": "string", // 生成图片的URL，防盗链格式（请注意，为保障信息安全，生成的图片/视频会在30天后被清理，请及时转存）
            "watermark_url": "string" // 含水印图片下载URL，防盗链格式
          }
        ]
      }
    }
  ]
}
```
