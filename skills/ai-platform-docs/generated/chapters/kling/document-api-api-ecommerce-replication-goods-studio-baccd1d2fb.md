<!-- Official source: https://klingai.com/document-api/api/ecommerce-replication/goods-studio.md -->
<!-- Source SHA-256: 9bd687e05773071abb0c5c62c5e1a83376f7e39111238e134cd774207d95e355 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://klingai.com/document-api/llms.txt
> Use this file to discover all available pages before exploring further.

# 商品成片

> 来源: https://klingai.com/document-api/api/ecommerce-replication/goods-studio
> 语言: zh
> 当前 Tab: 商品成片
> 此内容为面向 LLM 优化的 Markdown，已展开页面内 Tab，并省略页面目录、复制按钮等 UI 控件。

---

## 功能简介

商品成片（goods_studio）是专为电商商家与平台运营团队打造的 AI 视频生成服务。用户仅需输入商品信息，系统即可一键生成高质量的商品广告视频，降低营销内容的制作成本与交付周期。

系统会自动解析商品图片与核心卖点，合成富有叙事逻辑与营销吸引力的动态画面。

生成产物为一段基于商品信息自动创作的 15～60 秒高质量商品展示视频。

## 接入与使用建议

### 商品图素材质量建议

- 商品图建议使用高分辨率素材（长边 ≥ 1000px），背景干净、主体居中、光线均匀。
- 上传多张图时，建议涵盖不同角度（正面、侧面、细节），有助于系统生成更丰富的展示视角。

### 适用场景

- 新品快速出片：仅需商品信息，分钟级产出可用展示视频。
- 投放素材一键直出：支持多 SKU 批量调用，一键直出投放素材。
- 低成本视频化：无需拍摄团队与场地，零片场成本完成冷启动。

## 创建任务

### 接口概览

- Method: `POST`
- Path: `/solutions/e-commerce/goods_studio`
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
| `contents` | array | 是 | - | - | 输入的素材合集，包括商品图片、商品标题、商品描述。 |
| `contents[].type` | string | 是 | - | `ref_image`, `goods_title`, `goods_description` | 素材类型。支持：商品图片、商品标题、商品描述。 |
| `settings` | object | 是 | - | - | 输出视频配置相关参数。 |
| `settings.resolution` | string | 是 | - | `720p`, `1080p` | 生成视频的清晰度。 |
| `settings.aspect_ratio` | string | 是 | - | `9:16`, `1:1`, `16:9` | 生成视频的画面纵横比（宽:高）。 |
| `settings.duration` | int | 是 | - | `15`, `30`, `60` | 生成视频的时长范围，单位秒。 |
| `options` | object | 否 | - | - | 通用配置，如回调地址、是否含水印等。 |
| `options.callback_url` | string | 否 | - | - | 本次任务结果回调通知地址。如果配置，服务端会在任务状态发生变更时主动通知。 |
| `options.external_task_id` | string | 否 | - | - | 自定义任务 ID。 |
| `options.watermark` | object | 否 | - | - | 是否同时生成含水印的结果。通过 enabled 参数定义，具体 object 格式如下： |

#### Request Body 字段补充说明

- `contents`: 参考格式如下，参数说明详见下文：
  ```json
  "contents": [
    {
      "type": "ref_image",
      "url": "https://cdn.example.com/1.jpg"
    },
    {
      "type": "ref_image",
      "url": "https://cdn.example.com/2.jpg"
    },
    {
      "type": "goods_title",
      "text": "雨伞"
    },
    {
      "type": "goods_description",
      "text": "一把精美的雨伞"
    }
  ]
  ```
- `contents[].type`: `ref_image`：商品图片标识。
  - `goods_title`：商品标题标识。
  - `goods_description`：商品描述标识。
- `contents[].type.ref_image`: 通过 JSON 的格式定义，具体如下：
  ```json
  {
    "type": "ref_image", // 商品图片标识；必填
    "url": "https://cdn.example.com/1.jpg" // 素材内容，支持通过url或base64的方式提供；直接将相关信息填入即可；必填
  },
  {
    "type": "ref_image",
    "url": "https://cdn.example.com/2.jpg"
  }
  ```
- `contents[].type.ref_image`: 图片格式支持 .jpg / .jpeg / .png / .webp。
- `contents[].type.ref_image`: 图片文件大小不能超过 50MB。
- `contents[].type.ref_image`: 图片宽高尺寸不小于 300px，图片宽高比要在 1:2.5 ~ 2.5:1 之间。
- `contents[].type.ref_image`: 最多支持同时上传 5 张商品图片。
- `contents[].type.goods_title`: 通过 JSON 的格式定义，具体如下：
  ```json
  {
    "type": "goods_title", // 商品标题；必填
    "text": "string" // 文本提示词内容，内容长度不能超过200个字符；必填
  }
  ```
- `contents[].type.goods_description`: 通过 JSON 的格式定义，具体如下：
  ```json
  {
    "type": "goods_description", // 商品描述；选填
    "text": "string" // 文本提示词内容，内容长度不能超过2000个字符
  }
  ```
- `settings.resolution`: 720p：输出清晰度为 720P 的视频。
  - 1080p：输出清晰度为 1080P 的视频。
- `options`: ```json
  "options": {
    "callback_url": "https://example.com/cb", // 本次任务结果回调通知地址。如果配置，服务端会在任务状态发生变更时主动通知
    "external_task_id": "string", // 自定义任务ID，可用于查询，需在账号范围内保证唯一性
    "watermark": {
      "enabled": false // 是否生成含水印结果，true为生成，false为不生成；默认为false
    }
  }
  ```
- `options.callback_url`: 具体通知的消息 schema 见 [Callback 协议](https://klingai.com/document-api/api/get-started/callbacks)。
- `options.external_task_id`: 用户自定义任务 ID，传入不会覆盖系统生成的任务 ID，但支持通过该 ID 进行任务查询。
- `options.external_task_id`: 请注意，单用户下需要保证唯一性。
- `options.watermark`: ```json
  "watermark": {
    "enabled": boolean // 是否生成含水印结果，true为生成，false为不生成；默认为false
  }
  ```
- `options.watermark`: 暂不支持自定义水印。

### Request Example

```bash
curl --location --request POST 'https://api-beijing.klingai.com/solutions/e-commerce/goods_studio' \
--header 'Authorization: Bearer {apikey}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "contents": [
    {
      "type": "ref_image",
      "url": "https://cdn.example.com/1.jpg"
    },
    {
      "type": "ref_image",
      "url": "https://cdn.example.com/2.jpg"
    },
    {
      "type": "goods_title",
      "text": "雨伞"
    },
    {
      "type": "goods_description",
      "text": "一把精美的雨伞"
    }
  ],
  "settings": {
    "resolution": "1080p",
    "aspect_ratio": "16:9",
    "duration": 15
  },
  "options": {
    "callback_url": "https://example.com/cb",
    "external_task_id": "my_task_123",
    "watermark": {
      "enabled": false
    }
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
      "message": "string", // 任务状态信息，当任务失败时展示失败原因（如触发平台的内容风控等）
      "create_time": 1781080778802, // 任务创建时间，Unix 时间戳，单位 ms
      "update_time": 1781080794151, // 任务更新时间，Unix 时间戳，单位 ms
      "external_id": "string", // 该任务的自定义任务 ID（如有）
      "outputs": [ // 生成产物列表
        {
          "type": "video", // 产物类型：video（商品视频）
          "url": "string", // 生成结果的 URL，防盗链格式（请注意，为保障信息安全，生成的图片/视频会在 30 天后被清理，请及时转存）
          "watermark_url": "string", // 含水印下载 URL，防盗链格式
          "duration": "string" // 生成视频的时长，单位秒
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

### 商品成片专属错误信息

参数校验错误统一返回 `code: 1201`，具体场景和 message 如下：

| 场景                     | message                                                                        | 中文提示映射                                          |
| ------------------------ | ------------------------------------------------------------------------------ | ----------------------------------------------------- |
| 缺商品图                 | Product image is missing. Please upload a product image.                       | 请上传商品图                                          |
| 缺商品标题               | Product title is missing. Please provide a product title.                      | 请填写商品标题                                        |
| 商品图超过 5 张          | At most 5 ref_image items are allowed in contents.                             | 商品图最多上传 5 张，请移除多余图片                   |
| 图片格式/规格不符合要求  | Unsupported product image. Please check the image format, size and dimensions. | 商品图不符合要求，请检查图片格式、大小与尺寸          |
| 多个 `goods_title`       | Only one goods_title item is allowed in contents.                              | 商品标题最多上传 1 条，请移除多余的 goods_title       |
| `goods_title` 超长       | goods_title exceeds the 200-character limit.                                   | 商品标题不能超过 200 个字符                           |
| 多个 `goods_description` | Only one goods_description item is allowed in contents.                        | 商品描述最多上传 1 条，请移除多余的 goods_description |
| `goods_description` 超长 | goods_description exceeds the 2000-character limit.                            | 商品描述不能超过 2000 个字符                          |
| `resolution` 非法        | Unsupported resolution. Only 720p and 1080p are supported.                     | 分辨率仅支持 720p 和 1080p                            |
| `aspect_ratio` 非法      | aspect_ratio only supports 9:16, 1:1 and 16:9.                                 | 画面比例仅支持 9:16、1:1、16:9                        |
| `duration` 非法          | Unsupported duration. Only 15, 30 and 60 seconds are supported.                | 视频时长仅支持 15、30、60 秒                          |
