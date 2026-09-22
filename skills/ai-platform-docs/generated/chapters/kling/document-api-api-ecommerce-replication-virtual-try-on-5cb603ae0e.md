<!-- Official source: https://klingai.com/document-api/api/ecommerce-replication/virtual-try-on.md -->
<!-- Source SHA-256: 2492de5dd3f834325b363a1c1b870057939c15ecb3fd0f6e71b98cfdb7f7b970 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://klingai.com/document-api/llms.txt
> Use this file to discover all available pages before exploring further.

# 虚拟试穿

> 来源: https://klingai.com/document-api/api/ecommerce-replication/virtual-try-on
> 语言: zh
> 当前 Tab: 虚拟试穿
> 此内容为面向 LLM 优化的 Markdown，已展开页面内 Tab，并省略页面目录、复制按钮等 UI 控件。

---

## 功能简介

虚拟试穿（virtual_try_on）是面向服饰电商场景的图像生成 API。开发者输入一张服饰参考图与一张模特参考图后，系统将参考服饰的款式、颜色和纹理，在目标人物图上生成试穿结果图。

该能力适用于商品详情页素材制作、上新测款、广告素材扩展和买家秀批量生成等场景。

虚拟试穿通过 `POST /solutions/virtual_try_on` 提交试穿任务，异步返回结果图片。任务提交后，可通过查询接口按任务 ID 轮询状态，也可在创建任务时传入 `callback_url` 接收异步回调，无需主动轮询。

API 支持三个独立的图像控制维度：

| 控制维度                    | 说明                                             |
| --------------------------- | ------------------------------------------------ |
| 人脸保持（keep_face）       | 保留人物面部特征、五官、表情与发型               |
| 姿态保持（keep_pose）       | 保留人物原始姿势、身体朝向与位置                 |
| 背景保持（keep_background） | 保留人物图原始背景，或生成与服饰风格协调的新背景 |

三个维度默认全部开启，可按场景需求单独调整。

## 接入与使用建议

### 图片质量要求

**服饰图（product_image）**

- 服饰图支持真人上身图、人台商品图、平铺服装图、白底或简洁背景商品图。
- 不建议使用主体多件服饰不清晰、服装被道具大面积遮挡、带明显水印 / 促销文字 / 拼图边框、低清强反光过曝、严重褶皱或服装轮廓不完整的图片。
- 支持 jpg、jpeg、png、webp；图片最长边不超过 2048px，短边大于 300px，体积不超过 10MB。

**人物图（person_image）**

- 人物图建议为单人图，正面或四分之三侧身，人物主体清晰且试穿区域完整可见，避免多人画面、半身过窄裁切、夸张姿势以及手臂大面积遮挡服装区域。
- 启用 `keep_pose: true` 时，人物图中的姿势将被保留；建议使用身体自然舒展的站姿图，避免遮挡手部区域。
- 图片格式与尺寸建议同服饰图。

## 创建任务

### 接口概览

- Method: `POST`
- Path: `/solutions/virtual_try_on`
- Auth: `Authorization: Bearer <API_KEY>`
- Content-Type: `application/json`

### 说明

提交一个虚拟试穿任务，返回任务 ID 用于后续状态查询。

### Headers

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `Content-Type` | string | 是 | `application/json` | - | 请求体数据格式 |
| `Authorization` | string | 是 | - | - | 鉴权凭证，获取方式参见接口鉴权文档 |

### Request Body

| 字段路径 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `contents` | array | 是 | - | - | 输入图片资产列表，必须包含且仅包含 1 项 product_image 和 1 项 person_image，共 2 项。 |
| `contents[].type` | string | 是 | - | `product_image`, `person_image` | 图片类型枚举值，指定当前条目的图片用途。 |
| `contents[].url` | string | 是 | - | - | 公网可访问的图片 URL。 |
| `settings` | object | 否 | - | - | 控制人物面部、姿态与背景的保留方式，各字段独立生效。 |
| `settings.keep_face` | boolean | 否 | `true` | `true`, `false` | 控制是否保留人物的面部特征。 |
| `settings.keep_pose` | boolean | 否 | `true` | `true`, `false` | 控制是否保留人物的姿势。 |
| `settings.keep_background` | boolean | 否 | `true` | `true`, `false` | 控制是否保留人物图背景。 |
| `options` | object | 否 | - | - | 任务自定义选项，支持配置回调地址与业务方任务 ID。 |
| `options.callback_url` | string | 否 | - | - | 任务完成后的结果回调地址。 |
| `options.external_task_id` | string | 否 | - | - | 业务方自定义任务 ID，用于与业务系统关联。 |
| `options.watermark` | object | 否 | - | - | 是否同时生成含水印的结果。通过 enabled 参数定义，具体 object 格式如下： |

#### Request Body 字段补充说明

- `contents`: 参考格式如下，参数说明详见下文：
  ```json
  "contents": [
    {
      "type": "product_image",
      "url": "https://cdn.example.com/product.jpg"
    },
    {
      "type": "person_image",
      "url": "https://cdn.example.com/person.jpg"
    }
  ]
  ```
- `contents`: 两种类型各提供 1 项，顺序不限；缺少任意一种类型将导致请求失败。
- `contents[].type.product_image`: 通过 JSON 的格式定义，具体如下：
  ```json
  {
    "type": "product_image", // 商品图标识；必填
    "url": "https://cdn.example.com/product.jpg" // 公网可访问的图片 URL；必填
  }
  ```
- `contents[].type.product_image`: 建议使用清晰、完整、无遮挡的图片，避免过多文字、水印或明显合成痕迹。
- `contents[].type.product_image`: 图片格式支持 jpg、jpeg、png、webp；图片最长边不超过 2048px，短边大于 300px，体积不超过 10MB。
- `contents[].type.person_image`: 通过 JSON 的格式定义，具体如下：
  ```json
  {
    "type": "person_image", // 人物图标识；必填
    "url": "https://cdn.example.com/person.jpg" // 公网可访问的图片 URL；必填
  }
  ```
- `contents[].type.person_image`: 建议使用单人、清晰、正面或四分之三侧身图片，确保试穿区域完整可见。
- `contents[].type.person_image`: 启用 `keep_pose: true` 时，人物图中的姿势将被保留；建议使用身体自然舒展的站姿图，避免遮挡手部区域。
- `contents[].type.person_image`: 图片格式支持 jpg、jpeg、png、webp；图片最长边不超过 2048px，短边大于 300px，体积不超过 10MB。
- `contents[].url`: 图片格式支持 jpg、jpeg、png、webp；图片最长边不超过 2048px，短边大于 300px，体积不超过 10MB。
- `settings`: 省略整个 `settings` 对象时，所有控制维度均使用默认值（全部保留原始状态）：
  ```json
  "settings": {
    "keep_face": true,
    "keep_pose": true,
    "keep_background": true
  }
  ```
- `settings.keep_face`: true（默认）：保留面部特征、五官、表情与发型。
  - false：允许面部随服饰风格自然变化，仍保持肤色与体型比例。
- `settings.keep_pose`: true（默认）：保留原始姿势、身体朝向与位置。
  - false：允许模型为更好地展示服饰效果而自然调整姿态。
- `settings.keep_background`: true（默认）：保留人物图的原始背景。
  - false：允许生成与服饰风格协调的新背景。
- `options`: 省略整个 `options` 对象时，任务结果需通过查询接口主动轮询获取：
  ```json
  "options": {
    "callback_url": "https://example.com/callback",
    "external_task_id": "virtual-tryon-001",
    "watermark": {
      "enabled": false
    }
  }
  ```
- `options.callback_url`: 未填写时，可通过查询接口主动轮询任务状态与结果。
- `options.callback_url`: 具体通知的消息 schema 见 [Callback 协议](https://klingai.com/document-api/api/get-started/callbacks)。
- `options.external_task_id`: 创建后可在查询接口中通过 `external_task_ids` 检索对应任务。
- `options.external_task_id`: 请注意，单用户下需要保证唯一性。
- `options.watermark`: ```json
  "watermark": {
    "enabled": boolean // 是否生成含水印结果，true为生成，false为不生成；默认为false
  }
  ```
- `options.watermark`: 暂不支持自定义水印。

### Request Example

```bash
curl --location --request POST 'https://api-beijing.klingai.com/solutions/virtual_try_on' \
--header 'Authorization: Bearer {apikey}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "contents": [
    {
      "type": "product_image",
      "url": "https://cdn.example.com/product.jpg"
    },
    {
      "type": "person_image",
      "url": "https://cdn.example.com/person.jpg"
    }
  ],
  "settings": {
    "keep_face": true,
    "keep_pose": true,
    "keep_background": true
  },
  "options": {
    "callback_url": "https://example.com/callback",
    "external_task_id": "virtual-tryon-001",
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
    "task_id": "string", // 系统生成的任务 ID，用于后续查询
    "status": "string", // 任务状态，枚举值：submitted（已提交）、processing（处理中）、succeed（成功）、failed（失败）
    "create_time": 1788595200000, // 任务创建时间，Unix 时间戳，单位 ms
    "update_time": 1788595200000, // 任务更新时间，Unix 时间戳，单位 ms
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

按任务 ID 或业务方任务 ID 查询试穿任务的状态与结果。

任务成功后，通过 `outputs` 数组中 `type` 为 `image` 的条目的 `url` 字段获取成品图片；任务失败时，`message` 字段返回可供调用方处理的失败说明。

- 任务查询为平台级通用接口，适用于所有可灵解决方案API。

### Headers

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `Content-Type` | string | 是 | `application/json` | - | 请求体数据格式 |
| `Authorization` | string | 是 | - | - | 鉴权凭证，获取方式参见接口鉴权文档 |

### Query Params

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `task_ids` | string | 否 | - | - | 需要查询的系统定义的任务 ID，传入创建接口返回的 data.task_id。 |
| `external_task_ids` | string | 否 | - | - | 需要查询的自定义任务 ID，传入创建时指定的 options.external_task_id。 |

#### Query Params 字段补充说明

- `task_ids`: 请求查询参数，将值拼接在请求 URL 的 `?` 之后。
- `task_ids`: 多个 ID 用英文逗号分隔，最多 20 个。
- `task_ids`: task_ids 与 external_task_ids 两种 ID 至少且只能选择一种，不可同时使用。
- `external_task_ids`: 请求查询参数，将值拼接在请求 URL 的 `?` 之后。
- `external_task_ids`: 多个 ID 用英文逗号分隔，最多 20 个。
- `external_task_ids`: task_ids 与 external_task_ids 两种 ID 至少且只能选择一种，不可同时使用。

### Request Example

```bash
# 按 task_id 查询
curl --location --request GET 'https://api-beijing.klingai.com/solutions?task_ids=882836916432285766' \
--header 'Authorization: Bearer {apikey}' \
--header 'Content-Type: application/json'

# 按 external_task_id 查询
curl --location --request GET 'https://api-beijing.klingai.com/solutions?external_task_ids=virtual-tryon-001' \
--header 'Authorization: Bearer {apikey}' \
--header 'Content-Type: application/json'
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
      "status": "string", // 任务状态，枚举值：submitted（已提交）、processing（处理中）、succeed（成功）、failed（失败）
      "message": "string", // 任务状态信息，当任务失败时返回可供调用方处理的失败说明
      "create_time": 1788870967898, // 任务创建时间，Unix 时间戳，单位 ms
      "update_time": 1788870971958, // 任务更新时间，Unix 时间戳，单位 ms
      "external_id": "string", // 该任务的自定义任务 ID（如有）
      "outputs": [ // 生成产物列表
        {
          "type": "image", // 产物类型：image（试穿成品图）
          "url": "string", // 生成结果的 URL，防盗链格式（请注意，为保障信息安全，生成的图片会在 30 天后被清理，请及时转存）
          "watermark_url": "string" // 含水印下载 URL，防盗链格式
        }
      ],
      "billing": [ // 任务消耗信息；实际按本次扣费方式只返回其中一种
        {
          "charge_type": "unit", // 消耗账户类型：资源包
          "amount": "string", // 扣减数额；unit 时代表积分扣减量；十进制
          "package_type": "string" // 消耗资源包类型，仅 charge_type=unit 时存在；固定枚举值：image
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

按时间范围或任务状态批量查询试穿任务，支持游标翻页，适用于数据对账、批量状态同步等场景。

- 任务查询为平台级通用接口，适用于所有可灵解决方案API。

### Headers

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `Content-Type` | string | 是 | `application/json` | - | 请求体数据格式 |
| `Authorization` | string | 是 | - | - | 鉴权凭证，获取方式参见接口鉴权文档 |

### Request Body

| 字段路径 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `start_time` | long | 否 | `end_time 前 30 天` | - | 查询起始时间，Unix 毫秒时间戳，包含该时刻。 |
| `end_time` | long | 否 | `当前时间` | - | 查询结束时间，Unix 毫秒时间戳，不包含该时刻。 |
| `cursor` | string | 否 | - | - | 续页游标，取上一次响应中的 next_cursor 值。 |
| `limit` | int | 否 | `500` | - | 每页返回条数，取值范围 1–500。 |
| `filters` | array | 否 | - | - | 查询任务筛选条件，如：任务状态。 |
| `filters[].key` | string | 否 | - | `status` | 筛选维度，目前支持按任务状态等条件筛选。 |

#### Request Body 字段补充说明

- `start_time`: 省略时默认取 end_time 往前推 30 天。
- `end_time`: 须大于 start_time；省略时默认取当前时间。
- `cursor`: 传入后 start_time 和 end_time 将被忽略；其他筛选条件须与上次请求保持一致。
- `filters`: 通过 key & values 的方式设置查询条件，如：查询状态为 succeed 的任务。
  - 参考格式如下，参数说明详见下文：
  ```json
  "filters": [
    {
      "key": "status",
      "values": ["succeed"]
    }
  ]
  ```
- `filters[].key`: `status`：任务状态
- `filters[].key.status`: 通过 JSON 的格式定义，具体如下：
  ```json
  {
    "key": "status", // 筛选维度，按任务状态筛选，固定参数值：status；必填
    "values": ["succeed"] // 筛选维度对应条件，枚举值：submitted、processing、succeed、failed，依次为：已提交、生成中、生成成功、生成失败；必填
  }
  ```

### Request Example

```bash
# 首次请求：按时间范围 + 状态筛选
curl --location --request POST 'https://api-beijing.klingai.com/solutions' \
--header 'Authorization: Bearer {apikey}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "start_time": 1788134400000,
  "end_time": 1788739200000,
  "limit": 20,
  "filters": [
    {
      "key": "status",
      "values": ["succeed"]
    }
  ]
}'

# 翻页请求：传入 cursor 后，start_time / end_time 将被忽略
curl --location --request POST 'https://api-beijing.klingai.com/solutions' \
--header 'Authorization: Bearer {apikey}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "cursor": "882836916432285766",
  "limit": 20,
  "filters": [
    {
      "key": "status",
      "values": ["succeed"]
    }
  ]
}'
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
    "next_cursor": "string", // 游标信息，has_more 为 true 时作为下次请求的 cursor 继续翻页
    "has_more": true // 基于游标信息，是否还有未查询到的数据；为 false 时表示已到达最后一页
  }
}
```

## 错误码 / 回调协议

参考平台通用文档：[接口鉴权](https://klingai.com/document-api/api/get-started/authentication)、[错误码](https://klingai.com/document-api/api/get-started/error-codes)、[回调协议](https://klingai.com/document-api/api/get-started/callbacks)。
