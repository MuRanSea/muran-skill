<!-- Official source: https://klingai.com/document-api/api/ecommerce-replication/apparel.md -->
<!-- Source SHA-256: 38d470a30a67fff2b9e462454ba0eed0142d032262ad93cb3b49652a1f6acedf -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://klingai.com/document-api/llms.txt
> Use this file to discover all available pages before exploring further.

# 一键换装

> 来源: https://klingai.com/document-api/api/ecommerce-replication/apparel
> 语言: zh
> 当前 Tab: 一键换装
> 此内容为面向 LLM 优化的 Markdown，已展开页面内 Tab，并省略页面目录、复制按钮等 UI 控件。

---

## 功能简介

一键换装（clothing_dupe）是面向服装品类电商商家和平台运营团队的 AI 视频生成服务。用户只需提供一段服装商品的参考视频和商品图，系统即可自动生成展示用户商品的新视频，有效降低内容生产成本与交付周期。

系统会将参考视频中的服装替换为用户上传的服装，并尽量复刻参考视频中的展示节奏、镜头语言、动作姿态、场景氛围和商品呈现方式。

生成产物为一段基于参考视频的 5～180 秒商品展示视频。

## 接入与使用建议

### 商品图素材质量建议

- 商品图建议使用高分辨率素材（长边 ≥ 1000px），背景干净、主体居中、光线均匀。
- 上传多张图时，建议涵盖不同角度（正面、侧面、细节），有助于系统生成更丰富的展示视角。
- 避免上传已有大量文字水印或强烈滤镜的素材。

### 适用场景

- 新品上市快速出片：从素材到完整视频物料，分钟级交付。
- 大促活动批量备片：支持批量调用，快速产出多 SKU 视频内容。
- 内容营销素材生产：展示视频可直接用于信息流广告、短视频平台投放。

## 创建任务

### 接口概览

- Method: `POST`
- Path: `/solutions/e-commerce/clothing_dupe`
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
| `contents` | array | 是 | - | - | 参考素材合集，如商品描述、参考视频、商品图、模特图、音频素材（BGM、配音音色）等。 |
| `contents[].type` | string | 是 | - | `product_info`, `source_video`, `product_image`, `model_image`, `bgm`, `voice` | 素材类型。支持：商品描述、参考视频、商品图、模特图、背景音乐、TTS 音色。 |
| `settings` | object | 否 | - | - | 输出视频配置相关参数。 |
| `settings.resolution` | string | 否 | `720p` | `720p`, `1080p` | 生成视频的清晰度。 |
| `settings.aspect_ratio` | string | 否 | - | `9:16`, `2:3`, `3:4`, `1:1`, `4:3`, `3:2`, `16:9`, `21:9` | 生成视频的画面纵横比（宽:高）。 |
| `options` | object | 否 | - | - | 通用配置，如回调地址、是否含水印等。 |
| `options.callback_url` | string | 否 | - | - | 本次任务结果回调通知地址。如果配置，服务端会在任务状态发生变更时主动通知。 |
| `options.external_task_id` | string | 否 | - | - | 自定义任务 ID。 |
| `options.watermark_info` | object | 否 | - | - | 是否同时生成含水印的结果。通过 enabled 参数定义，具体 object 格式如下： |

#### Request Body 字段补充说明

- `contents`: 参考格式如下，参数说明详见下文：
  ```json
  "contents": [
    {
      "type": "product_info",
      "text": ""
    },
    {
      "type": "source_video",
      "url": "https://your-cdn.com/ref_video.mp4"
    },
    {
      "type": "product_image",
      "url": "https://your-cdn.com/product.jpg"
    },
    {
      "type": "model_image",
      "url": "https://your-cdn.com/model.jpg"
    },
    {
      "type": "bgm",
      "url": "https://cdn.example.com/b.mp3"
    },
    {
      "type": "voice",
      "voice_id": "calm_sales_woman"
    }
  ]
  ```
- `contents[].type`: `product_info`：商品描述标识。
  - `source_video`：参考视频素材标识。
  - `product_image`：商品图素材标识。
  - `model_image`：模特图素材标识（选填）。
  - `bgm`：最终输出视频背景音乐素材（选填）。
  - `voice`：最终输出视频 TTS 音色素材（选填）。
- `contents[].type.product_info`: 通过 JSON 的格式定义，具体如下：
  ```json
  {
    "type": "product_info", // 素材类型，固定参数值：product_info；必填
    "text": "string" // 文本提示词内容，内容长度不能超过2500个字符；必填
  }
  ```
- `contents[].type.source_video`: 通过 JSON 的格式定义，具体如下：
  ```json
  {
    "type": "source_video", // 参考视频素材标识；必填
    "url": "string" // 素材内容，支持通过url方式提供，暂不支持base64；直接将相关信息填入即可；必填
  }
  ```
- `contents[].type.source_video`: 视频文件大小不能超过 100MB。
- `contents[].type.source_video`: 视频时长需介于 5 秒（含）和 180 秒（含）之间。
- `contents[].type.source_video`: 视频格式支持 .mp4 / .mov。
- `contents[].type.source_video`: 视频宽高尺寸需介于 576px（含）和 4553px（含）之间，像素总面积不超过 8294400。其中：视频的宽高比需在 0.4~2 之间。
- `contents[].type.source_video`: 视频帧率支持 24fps（含）～60fps（含）（生成视频的帧率为 24fps）。
- `contents[].type.product_image`: 通过 JSON 的格式定义，具体如下：
  ```json
  {
    "type": "product_image", // 商品图素材标识；必填
    "url": "https://cdn.example.com/1.jpg" // 素材内容，支持通过url或base64的方式提供；直接将相关信息填入即可；必填
  },
  {
    "type": "product_image",
    "url": "https://cdn.example.com/2.jpg"
  }
  ```
- `contents[].type.product_image`: 图片格式支持 .jpg / .jpeg / .png / .webp。
- `contents[].type.product_image`: 图片文件大小不能超过 50MB。
- `contents[].type.product_image`: 图片宽高尺寸不小于 300px，图片宽高比要在 1:2.5 ~ 2.5:1 之间。
- `contents[].type.product_image`: 最多支持同时上传 5 张商品图。
- `contents[].type.model_image`: 通过 JSON 的格式定义，具体如下：
  ```json
  {
    "type": "model_image", // 模特图素材标识；选填
    "url": "https://cdn.example.com/a.jpg" // 素材内容，支持通过url或base64的方式提供；直接将相关信息填入即可；选填
  },
  {
    "type": "model_image",
    "url": "https://cdn.example.com/b.jpg"
  }
  ```
- `contents[].type.model_image`: 图片格式支持 .jpg / .jpeg / .png / .webp。
- `contents[].type.model_image`: 图片文件大小不能超过 50MB。
- `contents[].type.model_image`: 图片宽高尺寸不小于 300px，图片宽高比要在 1:2.5 ~ 2.5:1 之间。
- `contents[].type.model_image`: 最多支持同时上传 5 张模特图。
- `contents[].type.model_image`: 此项为选填，不传则默认使用参考视频中的人物形象。
- `contents[].type.bgm`: 通过 JSON 的格式定义，具体如下：
  ```json
  {
    "type": "bgm", // 输出视频背景音乐；选填
    "url": "https://cdn.example.com/b.mp3" // 素材内容，支持通过url方式提供，暂不支持base64；直接将相关信息填入即可；选填
  }
  ```
- `contents[].type.bgm`: 音频格式支持 .mp3 / .m4a / .wav / .wave。
- `contents[].type.bgm`: 音频文件大小不能超过 50MB。
- `contents[].type.bgm`: 音频文件时长建议在 5s~10min。若音频时长短于视频：循环播放至视频结束；若音频时长长于视频：从开头对齐截取，仅保留与视频等长的部分。
- `contents[].type.bgm`: 最多支持上传 1 条音频文件。
- `contents[].type.bgm`: 此项为选填，未传则从 bgm 库自动匹配推荐。
- `contents[].type.voice`: 通过 JSON 的格式定义，具体如下：
  ```json
  {
    "type": "voice", // 输出视频配音；选填
    "voice_id": "calm_sales_woman" // TTS音色ID字符串，暂不支持传入自定义音色，可从官方音色库选填音色ID；传入则走指定TTS配音，不传则默认音画同出；选填
  }
  ```
- `contents[].type.voice`: 此项为选填，传入则走 TTS 音色，未传则默认音画同出。
- `contents[].type.voice`: 当 type=voice 时，voice_id 字段填入以下枚举值之一。本解决方案使用独立音色库，所有音色均通过 voice_id 字符串标识，系统自动匹配对应配置。
  
  | voice_id | 中文名称 |
  | --- | --- |
  | energetic_sales_girl | 活力带货女 |
  | gentle_sales_woman | 温柔带货女 |
  | crisp_sales_girl | 清脆带货女 |
  | mature_sales_woman | 知性带货女 |
  | calm_sales_woman | 平静带货女 |
  | soft_sales_woman | 柔和带货女 |
  | energetic_sales_boy | 活力带货男 |
  | enthusiastic_sales_man | 热情带货男 |
  | steady_sales_man | 沉稳带货男 |
  | calm_sales_man | 平静带货男 |
- `settings.resolution`: 720p：输出清晰度为 720P 的视频。
  - 1080p：输出清晰度为 1080P 的视频。
- `settings.aspect_ratio`: 可选；传入则校验。
- `options`: ```json
  "options": {
    "callback_url": "https://example.com/cb", // 本次任务结果回调通知地址。如果配置，服务端会在任务状态发生变更时主动通知
    "external_task_id": "string", // 自定义任务ID，可用于查询，需在账号范围内保证唯一性
    "watermark_info": {
      "enabled": false // 是否生成含水印结果，true为生成，false为不生成；默认为false
    }
  }
  ```
- `options.callback_url`: 具体通知的消息 schema 见 [Callback 协议](https://klingai.com/document-api/api/get-started/callbacks)。
- `options.external_task_id`: 用户自定义任务 ID，传入不会覆盖系统生成的任务 ID，但支持通过该 ID 进行任务查询。
- `options.external_task_id`: 请注意，单用户下需要保证唯一性。
- `options.watermark_info`: ```json
  "watermark_info": {
    "enabled": boolean // 是否生成含水印结果，true为生成，false为不生成；默认为false
  }
  ```
- `options.watermark_info`: 暂不支持自定义水印。

### Request Example

```bash
curl --location --request POST 'https://api-beijing.klingai.com/solutions/e-commerce/clothing_dupe' \
--header 'Authorization: Bearer {apikey}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "contents": [
    {
      "type": "product_info",
      "text": "轻盈透气短袖衬衫，商务休闲百搭"
    },
    {
      "type": "source_video",
      "url": "https://your-cdn.com/ref_video.mp4"
    },
    {
      "type": "product_image",
      "url": "https://your-cdn.com/product_shirt.jpg"
    },
    {
      "type": "model_image",
      "url": "https://your-cdn.com/model.jpg"
    }
  ],
  "settings": {
    "resolution": "720p",
    "aspect_ratio": "16:9"
  },
  "options": {
    "callback_url": "https://example.com/callback",
    "external_task_id": "my_task_123",
    "watermark_info": {
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
          "type": "product_image", // 产物类型，枚举值：product_image（商品图）、model_images（模特图）、product_video（商品视频）。不同生成内容类型返回值及相关字段会有区别
          "url": "string", // 生成结果的 URL，防盗链格式（请注意，为保障信息安全，生成的图片/视频会在 30 天后被清理，请及时转存）
          "watermark_url": "string" // 含水印下载 URL，防盗链格式
        },
        {
          "type": "model_images", // 生成结果为「模特图」时返回
          "url": "string", // 生成结果的 URL，防盗链格式（请注意，为保障信息安全，生成的图片/视频会在 30 天后被清理，请及时转存）
          "watermark_url": "string" // 含水印下载 URL，防盗链格式
        },
        {
          "type": "product_video", // 生成结果为「商品视频」时返回
          "url": "string", // 生成结果的 URL，防盗链格式（请注意，为保障信息安全，生成的图片/视频会在 30 天后被清理，请及时转存）
          "watermark_url": "string" // 含水印下载 URL，防盗链格式
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

### 一键换装专属错误信息

参数校验错误统一返回 `code: 1201`，具体场景和 message 如下：

| 场景                                 | message                                                                                                      | 中文提示映射                                             |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------- |
| 缺参考视频                           | Reference video is missing. Please upload a reference video.                                                 | 请上传参考视频                                           |
| 缺商品图                             | Product image is missing. Please upload a product image.                                                     | 请上传商品图                                             |
| 缺商品描述                           | Product description is missing. Please provide a product description.                                        | 请上传商品描述                                           |
| 多个 `contents.type=bgm`             | Only one bgm item is allowed in contents.                                                                    | 背景音乐最多上传 1 条，请移除多余的 bgm                  |
| 有 `type=bgm` 但 `url` 为空          | bgm is provided but url is empty. Please provide a BGM file URL or remove bgm to use the system default BGM. | 背景音乐地址为空，请填写 URL 或移除 bgm 使用系统默认配乐 |
| `type=voice` 但 `voice_id` 为空/非法 | Invalid voice_id. Please select a valid voice from the voice library.                                        | 音色 ID 无效，请从音色库中选择有效的 voice_id            |
| 有多个 `type=voice`                  | Only one voice item is allowed in contents.                                                                  | 最多指定 1 个音色，请移除多余的 voice                    |
| `resolution` 非法                    | Unsupported resolution. Only 720P and 1080P are supported.                                                   | 分辨率仅支持 720P 和 1080P                               |
| `aspect_ratio` 非法                  | aspect_ratio only supports 9:16, 2:3, 3:4, 1:1, 4:3, 3:2, 16:9 and 21:9.                                     | 画面比例仅支持 9:16、2:3、3:4、1:1、4:3、3:2、16:9、21:9 |
