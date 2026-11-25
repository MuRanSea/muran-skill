<!-- Official source: https://klingai.com/document-api/api/image/4-0/long-image-generation.md -->
<!-- Source SHA-256: 92069f900b20d5d51a08264d8d9daa015611cccff71d6884b4e1d6df8fff0718 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://klingai.com/document-api/llms.txt
> Use this file to discover all available pages before exploring further.

# 长图生成

> 来源: https://klingai.com/document-api/api/image/4-0/long-image-generation
> 语言: zh
> 当前 Tab: 长图生成
> 同组 Tab: 图片生成 / 长图生成 / 主体管理
> 此内容为面向 LLM 优化的 Markdown，已展开页面内 Tab，并省略页面目录、复制按钮等 UI 控件。

---

## 创建任务

### 接口概览

- Method: `POST`
- Path: `/long-image-generation/kling-4.0`
- Auth: `Authorization: Bearer <API_KEY>`
- Content-Type: `application/json`

### 说明

生成电商详情页或网页设计长图，最终返回一张完整图片。

### Headers

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `Content-Type` | string | 是 | `application/json` | - | 数据交换格式 |
| `Authorization` | string | 是 | - | - | 鉴权信息，参考接口鉴权 |

### Request Body

| 字段路径 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `contents` | array | 是 | - | - | 参考素材合集，如：提示词、图片。 |
| `contents[].type` | string | 是 | - | `prompt`, `refer_image`, `style_refer_image`, `subject_refer_image` | 素材类型，支持：提示词、参考图片、风格参考图、主体参考图。不支持主体库素材（type=element）参考。 |
| `settings` | object | 是 | - | - | 输出设置，例如：生成长图的技能、清晰度；每次只能生成一张完整的长图，不支持设置输出张数。 |
| `settings.skill` | string | 是 | - | `ecommerce`, `webpage` | 生成长图所使用的技能。 |
| `settings.length` | string | 否 | `medium` | `short`, `medium`, `long` | 生成页面长度，支持：长/中/短，仅生成电商详情页（skill=ecommerce）时有效。 |
| `settings.resolution` | string | 否 | `1k` | `1k`, `2k` | 生成图片的清晰度，电商详情页与网页设计均适用。 |
| `options` | object | 否 | - | - | 通用配置，如回调地址、是否含水印等 |
| `options.callback_url` | string | 否 | - | - | 本次任务结果回调通知地址 |
| `options.external_task_id` | string | 否 | - | - | 自定义任务ID |
| `options.watermark_info` | object | 否 | - | - | 是否同时生成含水印的结果 |
| `options.watermark_info.enabled` | boolean | 否 | `false` | - | true 为生成，false 为不生成，默认 false。 |

#### Request Body 字段补充说明

- `contents`: 必填，非空
- `contents`: 参考格式如下，参数说明详见下文：
- `contents`: ```json
  "contents": [
    {
      "type": "prompt", //提示词素材，必填非空
      "text": "string"
    },
    {
      "type": "refer_image", //参考图片素材，生成网页设计时不支持。
      "url": "string",
      "id": "string"
    },
    {
      "type": "style_refer_image", //风格参考图素材，用于参考图片的视觉风格与排版风格。生成电商详情页时不支持。
      "url": "string",
      "id": "string"
    },
    {
      "type": "subject_refer_image", //主体参考图素材，用于保留图片中的主体元素，并围绕该主体进行设计。生成电商详情页时不支持。
      "url": "string",
      "id": "string"
    }
  ]
  ```
- `contents[].type`: prompt：提示词素材类型。
  - refer_image：参考图片素材类型
  - style_refer_image：风格参考图素材类型，用于参考图片的视觉风格与排版风格。
  - subject_refer_image：主体参考图素材类型，用于保留图片中的主体元素，并围绕该主体进行设计。
- `contents[].type`: 素材必须包含提示词，prompt必填且非空。
- `contents[].type`: 生成电商详情页（settings.skill=ecommerce），refer_image 必填，必须提供 1–3 张参考图；
- `contents[].type.prompt`: 文本提示词，必填非空，可包含正向与负向描述。
- `contents[].type.prompt`: 可将提示词模板化来满足不同的图像生成需求。
- `contents[].type.prompt`: 提示词长度，纯英文不超过166,000字符，纯非英文不超过 71,000 字符；混合输入需满足：英文字符数/166,000 + 非英文字符数/71,000 ≤ 1。
- `contents[].type.prompt`: 通过JSON的格式定义，具体如下：
- `contents[].type.prompt`: ```json
  {
    "type": "prompt", // 素材类型，固定参数值：prompt；必填
    "text": "string" // 文本提示词内容；必填
  }
  ```
- `contents[].type.refer_image`: 参考图片素材，生成电商详情页（settings.skill=ecommerce）时必填，必须提供 1–3 张图片。
- `contents[].type.refer_image`: 生成网页设计（settings.skill=webpage）时请勿使用该参数，网页设计参考图设置请通过type=style_refer_image、subject_refer_image指定。
- `contents[].type.refer_image`: 通过JSON的格式定义，具体如下：
- `contents[].type.refer_image`: ```json
  {
    "type": "refer_image", // 参考图片素材标识
    "url": "string", // 素材内容，支持通过url或base64的方式提供；必填
    "id": "string" // 素材索引ID，用于在prompt中指定，同任务中当前参数不得重复
  }
  ```
- `contents[].type.refer_image`: 支持传入图片 URL 或Base64编码，URL 必须可访问，值不得为空。
- `contents[].type.refer_image`: 图片格式支持 .jpg/.jpeg/.png。
- `contents[].type.refer_image`: 单张图片文件不超过 30 MB，宽、高均不小于 300 px，宽高比为 2:5–5:2。
- `contents[].type.style_refer_image`: 风格参考图素材，参考所给图片的视觉风格与排版风格进行设计。最多支持1张图片素材。
- `contents[].type.style_refer_image`: 生成网页设计时（settings.skill=webpage）选填，生成电商详情页（settings.skill=ecommerce）时请勿使用该参数，电商详情页参考图设置请通过type=refer_image指定。
- `contents[].type.style_refer_image`: 通过JSON的格式定义，具体如下：
- `contents[].type.style_refer_image`: ```json
  {
    "type": "style_refer_image", // 风格参考图片素材标识
    "url": "string", // 素材内容，支持通过url或base64的方式提供；必填
    "id": "string" // 素材索引ID，用于在prompt中指定，同任务中当前参数不得重复
  }
  ```
- `contents[].type.style_refer_image`: 支持传入图片 URL 或Base64编码，URL 必须可访问，值不得为空。
- `contents[].type.style_refer_image`: 图片格式支持 .jpg/.jpeg/.png。
- `contents[].type.style_refer_image`: 单张图片文件不超过 30 MB，宽、高均不小于 300 px，宽高比为 2:5–5:2。
- `contents[].type.subject_refer_image`: 主体参考图素材，保留所给图片中的主体元素，围绕该主体进行设计。支持最多1张图片素材。
- `contents[].type.subject_refer_image`: 生成网页设计时（settings.skill=webpage）选填，生成电商详情页（settings.skill=ecommerce）时请勿使用该参数，电商详情页参考图设置请通过type=refer_image指定。
- `contents[].type.subject_refer_image`: 通过JSON的格式定义，具体如下：
- `contents[].type.subject_refer_image`: ```json
  {
    "type": "subject_refer_image", // 主体参考图片素材标识
    "url": "string", // 素材内容，支持通过url或base64的方式提供；必填
    "id": "string" // 素材索引ID，用于在prompt中指定，同任务中当前参数不得重复
  }
  ```
- `contents[].type.subject_refer_image`: 支持传入图片 URL 或Base64编码，URL 必须可访问，值不得为空。
- `contents[].type.subject_refer_image`: 图片格式支持 .jpg/.jpeg/.png。
- `contents[].type.subject_refer_image`: 单张图片文件不超过 30 MB，宽、高均不小于 300 px，宽高比为 2:5–5:2。
- `settings.skill`: ecommerce：电商详情页。
  - webpage：网页设计。
- `settings.length`: short：表示短，约2~5功能页；（注：功能页指最终长图中的内容模块或分段，不代表输出图片张数，最终仍返回一张完整长图。）
  - medium：表示中，约6~10功能页；
  - long：表示长，约11~18功能页；
- `settings.length`: 网页设计（skill=webpage）不支持该参数，设置无效。
- `settings.resolution`: 1k：1K 标清；
  - 2k：2K 高清；
- `options.callback_url`: 如果配置，服务端会在任务状态发生变更时主动通知
- `options.callback_url`: 具体通知的消息 schema 见 [Callback 协议](https://klingai.com/document-api/api/get-started/callbacks)
- `options.external_task_id`: 传入不会覆盖系统生成的任务ID，但支持通过该ID进行任务查询
- `options.external_task_id`: 请注意，单用户下需要保证唯一性
- `options.watermark_info`: 通过 enabled 参数定义：
  ```json
  "watermark_info": {
    "enabled": false // 是否生成含水印结果，true 为生成，false 为不生成；默认为 false
  }
  ```
- `options.watermark_info`: 暂不支持自定义水印

### Request Example

```bash
curl --request POST \
  --url "https://api-beijing.klingai.com/long-image-generation/kling-4.0" \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header "Content-Type: application/json" \
  --data '{
  "contents": [
    {
      "type": "prompt",
      "text": "为 @product 中的咖啡机设计完整电商详情页长图，包含主视觉、核心卖点和使用场景；仅使用提供的商品事实，不编造参数"
    },
    {
      "type": "refer_image",
      "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/Coffee_machine.png",
      "id": "product"
    }
  ],
  "settings": {
    "skill": "ecommerce",
    "length": "medium",
    "resolution": "2k"
  },
  "options": {
    "external_task_id": ""
  }
}'
```

### Response Example

```json
{
  "code": 0, // 错误码，0 为成功，具体定义见错误码文档
  "message": "SUCCEED", // 接口消息
  "request_id": "example-long-request-id", // 请求跟踪 ID，由系统生成
  "data": {
    "id": "example-long-task-id", // 系统任务 ID，由平台生成
    "status": "submitted", // 任务状态：submitted/processing/succeeded/failed
    "create_time": 1790000000000, // 任务创建时间，Unix 毫秒时间戳
    "update_time": 1790000000000, // 任务更新时间，Unix 毫秒时间戳
    "external_id": "string" // 创建时指定的自定义任务 ID（如有）
  }
}
```

## 更多场景调用示例

### 网页设计（纯文本，2K；不支持 length）

```cURL
curl --request POST \
  --url "https://api-beijing.klingai.com/long-image-generation/kling-4.0" \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header "Content-Type: application/json" \
  --data '{
  "contents": [
    {
      "type": "prompt",
      "text": "设计精品咖啡品牌官网视觉长图，包含品牌首屏、产品展示、烘焙理念、门店信息和页尾；输出一张完整设计图片"
    }
  ],
  "settings": {
    "skill": "webpage",
    "resolution": "2k"
  },
  "options": {
    "external_task_id": ""
  }
}'
```

---

## 查询任务（按任务ID）

### 接口概览

- Method: `GET`
- Path: `/tasks`
- Auth: `Authorization: Bearer <API_KEY>`
- Content-Type: `application/json`

### 说明

> 注意：当前API仅支持查询非实时/异步任务

### Headers

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `Content-Type` | string | 是 | `application/json` | - | 数据交换格式 |
| `Authorization` | string | 是 | - | - | 鉴权信息，参考接口鉴权 |

### Query Params

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `task_ids` | string | 否 | - | - | 需要查询的系统定义的任务ID |
| `external_task_ids` | string | 否 | - | - | 需要查询的自定义任务ID |

#### Query Params 字段补充说明

- `task_ids`: 查询参数，请将值填写在 URL query string 中
- `task_ids`: 查询任务时，task_ids 与 external_task_ids 两种 ID 至少且只能选择一种，不可同时使用
- `task_ids`: 支持批量查询，用 "," 分隔
- `external_task_ids`: 查询参数，请将值填写在 URL query string 中
- `external_task_ids`: 查询任务时，task_ids 与 external_task_ids 两种 ID 至少且只能选择一种，不可同时使用
- `external_task_ids`: 支持批量查询，用 "," 分隔

### Request Example

```bash
curl --location 'https://api-beijing.klingai.com/tasks?task_ids=123' \
  --header 'Content-Type: application/json' \
  --header "Authorization: Bearer ${KLING_API_KEY}"
```

```bash
curl --location 'https://api-beijing.klingai.com/tasks?external_task_ids=123' \
  --header 'Content-Type: application/json' \
  --header "Authorization: Bearer ${KLING_API_KEY}"
```

### Response Example

```json
{
  "code": 0, // 错误码；具体定义见错误码
  "message": "string", // 错误信息
  "request_id": "string", // 请求ID，系统生成，用于跟踪请求、排查问题
  "data": [
    {
      "id": "893605946402811985", // 被查询的任务ID
      "status": "string", // 任务状态，枚举值：submitted（已提交）、processing（处理中）、succeeded（成功）、failed（失败）
      "message": "string", // 任务状态信息，当任务失败时展示失败原因（如触发平台的内容风控等）
      "create_time": 1781080778802, // 任务创建时间，Unix 时间戳，单位 ms
      "update_time": 1781080794151, // 任务更新时间，Unix 时间戳，单位 ms
      "external_id": "string", // 该任务的自定义任务ID（如有）
      "outputs": [
        {
          "type": "video", // 生成结果为“视频”时返回，不同生成内容类型返回值及相关字段会有区别；各内容类型枚举值：image, video, audio, element, voice
          "id": "string", // 视频ID，由系统生成
          "url": "string", // 生成结果的URL，防盗链格式（请注意，为保障信息安全，生成的图片/视频会在30天后被清理，请及时转存）
          "watermark_url": "string", // 含水印视频下载URL，防盗链格式
          "duration": "string" // 生成的视频的时长，单位：秒
        },
        {
          "type": "image", // 生成结果为“图片”时返回，不同生成内容类型返回值及相关字段会有区别；各内容类型枚举值：image, video, audio, element, voice
          "url": "string", // 生成结果的URL，防盗链格式（请注意，为保障信息安全，生成的图片/视频会在30天后被清理，请及时转存）
          "watermark_url": "string", // 含水印图片下载URL，防盗链格式
          "group_id": "string" // 仅在生成组图时出现，用于标记分组关系
        },
        {
          "type": "audio", // 生成结果为“音频”时返回，不同生成内容类型返回值及相关字段会有区别；各内容类型枚举值：image, video, audio, element, voice
          "id": "string", // 音频ID，由系统生成
          "mp3_url": "string", // 生成结果的URL，mp3+防盗链格式（请注意，为保障信息安全，生成的图片/视频会在30天后被清理，请及时转存）
          "wav_url": "string", // 生成结果的URL，wav+防盗链格式（请注意，为保障信息安全，生成的图片/视频会在30天后被清理，请及时转存）
          "mp3_duration": "string", // 生成的mp3格式的音频的时长，单位：秒
          "wav_duration": "string" // 生成的wav格式的音频的时长，单位：秒
        },
        {
          "type": "voice", // 生成结果为“音色”时返回，不同生成内容类型返回值及相关字段会有区别；各内容类型枚举值：image, video, audio, element, voice
          "id": "string", // 音色ID，由系统生成
          "name": "string", // 音频名称
          "url": "string", // 试听音频下载链接
          "owned_by": "string", // 音色来源，kling为官方音色库，数字为创作者ID
          "status": "succeeded" // 音色状态，分为正常和已被删除，枚举值分别为：succeeded, deleted
        },
        {
          "type": "element", // 生成结果为“主体”时返回，不同生成内容类型返回值及相关字段会有区别；各内容类型枚举值：image, video, audio, element, voice
          "id": "string", // 主体ID，由系统生成
          "name": "string", // 主体名称
          "description": "string", // 主体描述
          "element_type": "string", // 主体类型，分为视频角色主体和多图主体，枚举值分别为：video_character_elements和multi_image_elements
          "references": [ // 主体相关素材
            {
              "type": "image", // “图片”素材时返回，各内容类型枚举值：image, video, voice
              "role": "string", // 图片参考素材属性，分为正面参考图和其他参考图，枚举值分别为：frontal, refer
              "url": "string" // 素材下载链接
            },
            {
              "type": "video", // “视频”素材时返回，各内容类型枚举值：image, video, voice
              "role": "refer", // 视频参考素材属性，固定值：refer
              "url": "string" // 素材下载链接
            },
            {
              "type": "voice", // “音色”素材时返回，各内容类型枚举值：image, video, voice
              "role": "refer", // 音色参考素材属性，固定值：refer
              "url": "string", // 素材下载链接
              "id": "string", // 音色ID
              "name": "string", // 音色名称
              "owned_by": "string" // 音色来源，kling为官方音色库，数字为创作者ID
            }
          ],
          "owned_by": "string", // 主体来源，kling为官方主体库，数字为创作者ID
          "status": "string", // 主体状态，分为正常和已被删除，枚举值分别为：succeeded, deleted
          "tags": [ // 主体标签相关信息
            {
              "id": 1, // 标签ID
              "name": "string", // 标签名称
              "description": "string" // 标签描述
            }
          ]
        }
      ],
      "billing": [ // 当任务产生多账户类型的余额消耗时，系统将返回多条数据。
        {
          "charge_type": "string", // 消耗账户类型，如果消耗的是额度则参数值为cash，如果是消耗资源包则参数值为unit
          "cash_type": "string", // 额度类型，仅存在于消耗额度场景（charge_type=cash）；如果消耗的是正式额度则参数值为balance，如果是消耗的是测试金则参数值为test_balance，如果消耗的是奖励金则参数值为reward_balance
          "amount": "string", // 扣减数额；消耗额度场景（charge_type=cash）时代表额度扣减折扣价，消耗资源包场景（charge_type=unit）时代表积分扣减量；十进制
          "currency": "string", // 消耗单位，仅存在于消耗余额场景（charge_type=cash），固定枚举值：CNY, USD
          "package_type": "string", // 消耗资源包类型，仅存在于消耗资源包场景（charge_type=unit），固定枚举值：video, image, audio
          "list_price": "string" // 额度扣减刊例价，仅存在于消耗额度场景（charge_type=cash）
        }
      ]
    }
  ]
}
```

---

## 查询任务（按游标查询）

### 接口概览

- Method: `POST`
- Path: `/tasks`
- Auth: `Authorization: Bearer <API_KEY>`
- Content-Type: `application/json`

### 说明

> 注意：当前API仅支持查询非实时/异步任务

### Headers

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `Content-Type` | string | 是 | `application/json` | - | 数据交换格式 |
| `Authorization` | string | 是 | - | - | 鉴权信息，参考接口鉴权 |

### Request Body

| 字段路径 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `start_time` | string | 否 | `end_time - 30 天` | - | 任务创建筛选的开始时间 |
| `end_time` | string | 否 | `当前时间` | - | 任务创建筛选的结束时间 |
| `cursor` | string | 否 | - | - | 续页游标，即查询起点 |
| `limit` | int | 否 | `100` | - | 查询任务数量 |
| `filters` | array | 否 | - | - | 查询任务筛选条件，如任务状态、功能类型 |
| `filters[].key` | string | 否 | - | `status`, `product_type` | 筛选维度 |
| `filters[].values` | array | 否 | - | - | 筛选维度对应条件 |

#### Request Body 字段补充说明

- `start_time`: Unix 时间戳，单位 ms
- `start_time`: 默认值为 end_time - 30 天
- `start_time`: 开始时间需早于结束时间
- `end_time`: 默认值为当前时间
- `end_time`: Unix 时间戳，单位 ms
- `end_time`: 结束时间需晚于开始时间
- `cursor`: 参数值来自上次查询时返回的 next_cursor 参数
- `cursor`: 当前参数不为空时，优先基于当前参数值查询，此时开始时间和结束时间参数将失效
- `limit`: 最大值 500；当数量不足 500 时有多少展示多少
- `filters`: 通过 key/value 的方式设置查询条件：
  ```json
  "filters": [
    {
      "key": "status", // 筛选维度，按任务状态筛选，固定参数值：status
      "values": ["succeeded"]
    },
    {
      "key": "product_type", // 筛选维度，按功能类型筛选，固定参数值：product_type
      "values": ["image"]
    }
  ]
  ```
- `filters[].key`: status：按任务状态筛选
  - product_type：按功能类型筛选
- `filters[].values`: status：submitted、processing、succeeded、failed，依次为已提交、生成中、生成成功、生成失败
- `filters[].values`: product_type：video、image、try_on，依次为视频、图像、虚拟试穿

### Request Example

```bash
curl --location 'https://api-beijing.klingai.com/tasks' \
  --header 'Content-Type: application/json' \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --data '{
    "start_time": "1781193600000",
    "end_time": "1781516352968",
    "cursor": "",
    "limit": 500,
    "filters": [
      {
        "key": "status",
        "values": ["succeeded"]
      },
      {
        "key": "product_type",
        "values": ["image"]
      }
    ]
  }'
```

### Response Example

```json
{
  "code": 0, // 错误码；具体定义见错误码
  "message": "string", // 错误信息
  "request_id": "string", // 请求ID，系统生成，用于跟踪请求、排查问题
  "data": {
    "result": [
      {
        "id": "string", // 被查询的任务ID
        "status": "string", // 任务状态，枚举值：submitted（已提交）、processing（处理中）、succeeded（成功）、failed（失败）
        "message": "string", // 任务状态信息，当任务失败时展示失败原因
        "create_time": 1781080778802, // 任务创建时间，Unix 时间戳，单位 ms
        "update_time": 1781080794151, // 任务更新时间，Unix 时间戳，单位 ms
        "external_id": "string", // 该任务的自定义任务ID（如有）
        "outputs": [
        {
          "type": "video", // 生成结果为“视频”时返回，不同生成内容类型返回值及相关字段会有区别；各内容类型枚举值：image, video, audio, element, voice
          "id": "string", // 视频ID，由系统生成
          "url": "string", // 生成结果的URL，防盗链格式（请注意，为保障信息安全，生成的图片/视频会在30天后被清理，请及时转存）
          "watermark_url": "string", // 含水印视频下载URL，防盗链格式
          "duration": "string" // 生成的视频的时长，单位：秒
        },
        {
          "type": "image", // 生成结果为“图片”时返回，不同生成内容类型返回值及相关字段会有区别；各内容类型枚举值：image, video, audio, element, voice
          "url": "string", // 生成结果的URL，防盗链格式（请注意，为保障信息安全，生成的图片/视频会在30天后被清理，请及时转存）
          "watermark_url": "string", // 含水印图片下载URL，防盗链格式
          "group_id": "string" // 仅在生成组图时出现，用于标记分组关系
        },
        {
          "type": "audio", // 生成结果为“音频”时返回，不同生成内容类型返回值及相关字段会有区别；各内容类型枚举值：image, video, audio, element, voice
          "id": "string", // 音频ID，由系统生成
          "mp3_url": "string", // 生成结果的URL，mp3+防盗链格式（请注意，为保障信息安全，生成的图片/视频会在30天后被清理，请及时转存）
          "wav_url": "string", // 生成结果的URL，wav+防盗链格式（请注意，为保障信息安全，生成的图片/视频会在30天后被清理，请及时转存）
          "mp3_duration": "string", // 生成的mp3格式的音频的时长，单位：秒
          "wav_duration": "string" // 生成的wav格式的音频的时长，单位：秒
        },
        {
          "type": "voice", // 生成结果为“音色”时返回，不同生成内容类型返回值及相关字段会有区别；各内容类型枚举值：image, video, audio, element, voice
          "id": "string", // 音色ID，由系统生成
          "name": "string", // 音频名称
          "url": "string", // 试听音频下载链接
          "owned_by": "string", // 音色来源，kling为官方音色库，数字为创作者ID
          "status": "succeeded" // 音色状态，分为正常和已被删除，枚举值分别为：succeeded, deleted
        },
        {
          "type": "element", // 生成结果为“主体”时返回，不同生成内容类型返回值及相关字段会有区别；各内容类型枚举值：image, video, audio, element, voice
          "id": "string", // 主体ID，由系统生成
          "name": "string", // 主体名称
          "description": "string", // 主体描述
          "element_type": "string", // 主体类型，分为视频角色主体和多图主体，枚举值分别为：video_character_elements和multi_image_elements
          "references": [ // 主体相关素材
            {
              "type": "image", // “图片”素材时返回，各内容类型枚举值：image, video, voice
              "role": "string", // 图片参考素材属性，分为正面参考图和其他参考图，枚举值分别为：frontal, refer
              "url": "string" // 素材下载链接
            },
            {
              "type": "video", // “视频”素材时返回，各内容类型枚举值：image, video, voice
              "role": "refer", // 视频参考素材属性，固定值：refer
              "url": "string" // 素材下载链接
            },
            {
              "type": "voice", // “音色”素材时返回，各内容类型枚举值：image, video, voice
              "role": "refer", // 音色参考素材属性，固定值：refer
              "url": "string", // 素材下载链接
              "id": "string", // 音色ID
              "name": "string", // 音色名称
              "owned_by": "string" // 音色来源，kling为官方音色库，数字为创作者ID
            }
          ],
          "owned_by": "string", // 主体来源，kling为官方主体库，数字为创作者ID
          "status": "string", // 主体状态，分为正常和已被删除，枚举值分别为：succeeded, deleted
          "tags": [ // 主体标签相关信息
            {
              "id": 1, // 标签ID
              "name": "string", // 标签名称
              "description": "string" // 标签描述
            }
          ]
        }
      ],
        "billing": [ // 当任务产生多账户类型的余额消耗时，系统将返回多条数据。
          {
            "charge_type": "string", // 消耗账户类型，如果消耗的是额度则参数值为 cash，如果消耗资源包则参数值为 unit
            "cash_type": "string", // 额度类型，仅存在于消耗额度场景（charge_type=cash）；如果消耗的是正式额度则参数值为balance，如果是消耗的是测试金则参数值为test_balance，如果消耗的是奖励金则参数值为reward_balance
            "amount": "string", // 扣减数额；消耗额度场景（charge_type=cash）时代表额度扣减折扣价，消耗资源包场景（charge_type=unit）时代表积分扣减量；十进制
            "currency": "string", // 消耗单位，仅存在于消耗余额场景（charge_type=cash），固定枚举值：CNY, USD
            "package_type": "string", // 消耗资源包类型，仅存在于消耗资源包场景（charge_type=unit），固定枚举值：video, image, audio
            "list_price": "string" // 额度扣减刊例价，仅存在于消耗额度场景（charge_type=cash）
          }
        ]
      }
    ],
    "count": 1, // 查询结果数量
    "next_cursor": "string", // 游标信息，可用于继续查询后续
    "has_more": true // 基于游标信息，是否还有未查询到的数据
  }
}
```
