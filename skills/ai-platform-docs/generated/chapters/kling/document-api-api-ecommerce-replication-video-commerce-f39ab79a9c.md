<!-- Official source: https://klingai.com/document-api/api/ecommerce-replication/video-commerce.md -->
<!-- Source SHA-256: b2dc3abf724ef2e23543be2a4ce8c364f0c9db6415ffa4e70b645e47a7c67701 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://klingai.com/document-api/llms.txt
> Use this file to discover all available pages before exploring further.

# 口播带货

> 来源: https://klingai.com/document-api/api/ecommerce-replication/video-commerce
> 语言: zh
> 当前 Tab: 口播带货
> 此内容为面向 LLM 优化的 Markdown，已展开页面内 Tab，并省略页面目录、复制按钮等 UI 控件。

---

## 功能简介

口播带货（talking_agent）是面向电商商家、品牌方与内容运营团队的 AI 口播视频生成服务。用户提供人物形象、商品素材与口播文案后，系统自动完成文案润色、配音与口型对齐，一键产出可直接投放的口播视频。

本方案采用「生成侧自由生成 + 口型专家模型后处理」链路：视频画面侧不受短时长口型窗口限制，口型一致性由后处理模型兜底修复，适合 15 秒以上的营销口播、多语种口播和批量电商素材生产。

系统会根据 `contents` 中是否包含商品内容自动分流为两类模式：

- **达人口播**：不传商品内容，全程人物出镜讲解，不生成商品画面，支持通过 `settings.speech_rate` 调节语速。
- **口播带货**：传入商品内容，人物讲解镜、人货同框镜与货品特写镜自动编排，暂不支持语速调节。

## 接入与使用建议

### 人物形象建议

- 建议使用单人、正脸清晰、嘴部无遮挡的人物素材。
- 图片建议高分辨率、光线均匀、面部区域清晰，避免多人合影、侧脸、强遮挡、墨镜或强滤镜。
- 口播带货场景下系统需生成人物与商品同框的画面，建议人物双手自然放松，避免双手被遮挡或插袋。

### 商品素材建议

- 商品图建议主体居中、背景干净、光线均匀。
- 建议上传 1～5 张不同角度商品参考图，如正面、侧面、细节图等。
- 避免上传已有大量文字、水印或复杂合成痕迹的商品图，避免生成画面复刻无关信息。

### 口播内容建议

- `speech_script` 为必填项，应为适合直接朗读的口语化表达。
- 传入商品内容时，建议至少提供 `ref_image` 与 `goods_title`，其余商品信息可按需补充。
- 如文案已经定稿不可改写，可将 `settings.allow_polish` 设为 `false`，系统将逐字使用传入的文案。
- 成片时长由系统根据口播稿自动决定，不支持通过请求指定；口播稿长度是影响成片时长与费用的主要因素。

### 适用场景

- 达人口播批量出片：一个形象加一段文案，分钟级产出多条口播视频。
- 电商带货素材生产：多 SKU 批量调用，直出可投放的带货口播视频。
- 多语种营销素材：同一商品信息生成不同语种口播，覆盖多地区投放。

## 创建任务

### 接口概览

- Method: `POST`
- Path: `/solutions/talking_agent`
- Auth: `Authorization: Bearer <API_KEY>`
- Content-Type: `application/json`

### 说明

- 模式由 `contents` 中是否包含商品内容自动分流：带商品内容走口播带货，不带商品内容走达人口播。

### Headers

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `Content-Type` | string | 是 | `application/json` | - | 数据交换格式 |
| `Authorization` | string | 是 | - | - | 鉴权信息，参考接口鉴权 |

### Request Body

| 字段路径 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `contents` | array | 是 | - | - | 输入的素材合集，包括人物形象、商品图片、商品文案与口播稿。 |
| `contents[].type` | string | 是 | - | `avatar_image`, `avatar_id`, `ref_image`, `goods_title`, `goods_price`, `goods_target_audience`, `goods_selling_point`, `speech_script` | 素材类型。支持：人物形象、商品图片、商品文案、口播稿。 |
| `settings` | object | 否 | - | - | 输出视频配置相关参数，如分辨率、画幅、音色、语速等。 |
| `settings.resolution` | string | 否 | `720p` | `720p`, `1080p` | 生成视频的清晰度。 |
| `settings.aspect_ratio` | string | 否 | `9:16` | `9:16`, `16:9` | 生成视频的画面纵横比（宽:高）。 |
| `settings.allow_polish` | boolean | 否 | `false` | - | 是否允许系统润色口播文案。 |
| `settings.voice_id` | string | 否 | - | - | TTS 音色 ID。 |
| `settings.speech_rate` | float | 否 | `1.0` | `0.8`, `1.0`, `1.2` | 口播配音的语速。 |
| `settings.action_prompt` | string | 否 | - | - | 人物的动作表现提示。 |
| `settings.bgm_enabled` | boolean | 否 | `false` | - | 是否为生成视频添加背景音乐。 |
| `options` | object | 否 | - | - | 通用配置，如回调地址、是否含水印等。 |
| `options.callback_url` | string | 否 | - | - | 本次任务结果回调通知地址。如果配置，服务端会在任务状态发生变更时主动通知。 |
| `options.external_task_id` | string | 否 | - | - | 自定义任务 ID。 |
| `options.watermark` | object | 否 | - | - | 是否同时生成含水印的结果。通过 enabled 参数定义，具体 object 格式如下： |

#### Request Body 字段补充说明

- `contents`: 参考格式如下，参数说明详见下文：
  ```json
  "contents": [
    {
      "type": "avatar_image",
      "url": "https://cdn.example.com/person.jpg"
    },
    {
      "type": "ref_image",
      "url": "https://cdn.example.com/1.jpg"
    },
    {
      "type": "goods_title",
      "text": "JBL GO 4 便携蓝牙音箱"
    },
    {
      "type": "speech_script",
      "text": "周末出门，我不太想带一堆复杂设备。"
    }
  ]
  ```
- `contents`: 图片类条目通过 `url` 传素材，文本类条目通过 `text` 传内容。
- `contents`: 人物来源二选一：上传人物用 `avatar_image`（恰好 1 条，`settings.voice_id` 必填），或使用形象库人物用 `avatar_id`（恰好 1 条，禁止传 `settings.voice_id`）。
- `contents`: 商品内容包括 `ref_image` / `goods_title` / `goods_price` / `goods_target_audience` / `goods_selling_point`。一旦出现任意一项即走口播带货模式，此时 `ref_image` 至少 1 张、`goods_title` 恰好 1 条且非空。
- `contents`: `speech_script` 为必填项：两种模式下均需恰好 1 条且非空。
- `contents`: 口播带货模式暂不支持语速调节：该模式下请勿传入 `settings.speech_rate`，传入将返回参数校验错误。
- `contents[].type.avatar_image`: 通过 JSON 的格式定义，具体如下：
  ```json
  {
    "type": "avatar_image", // 上传的人物图标识；与 avatar_id 二选一
    "url": "https://cdn.example.com/person.jpg" // 素材内容，支持通过 url 或 base64 的方式提供；必填
  }
  ```
- `contents[].type.avatar_image`: 图片格式支持 .jpg / .jpeg / .png / .webp。
- `contents[].type.avatar_image`: 图片文件大小不能超过 50MB。
- `contents[].type.avatar_image`: 图片宽高尺寸不小于 300px，图片宽高比要在 1:2.5 ~ 2.5:1 之间。
- `contents[].type.avatar_image`: 任务级输入：恰好 1 条，且每次任务都需重新提交素材。
- `contents[].type.avatar_image`: 上传人物图时，`settings.voice_id` 必填。
- `contents[].type.avatar_image`: 建议使用单人、正脸清晰、嘴部无遮挡的素材，避免多人合影、侧脸、强遮挡、墨镜或强滤镜。
- `contents[].type.avatar_id`: 通过 JSON 的格式定义，具体如下：
  ```json
  {
    "type": "avatar_id", // 形象库人物标识；与 avatar_image 二选一
    "text": "string" // 平台预先导入的形象库人物 ID，长度不能超过 128 个字符；必填
  }
  ```
- `contents[].type.avatar_id`: 只接受平台预先导入的固定形象列表中的 ID；恰好 1 条，暂不支持自定义形象库人物。
- `contents[].type.avatar_id`: 形象库人物自带音色，因此禁止传 `settings.voice_id`。
- `contents[].type.avatar_id`: text 字段填入以下形象 ID 之一，清单会随平台上架情况更新。
  
  | avatar_id | 姓名 | 性别 | 年龄 |
  | --- | --- | --- | --- |
  | avatar_vivian_female | Vivian（佳佳） | 女 | 23 |
  | avatar_lee_male | Lee（李阳） | 男 | 28 |
  | avatar_chenjing_female | 陈静 | 女 | 30 |
  | avatar_zhaochen_male | 赵晨 | 男 | 25 |
  | avatar_wanglei_male | 王磊 | 男 | 45 |
  | avatar_eva_female | Eva | 女 | 18 |
  | avatar_oliver_male | Oliver | 男 | 30 |
  | avatar_elena_female | Elena | 女 | 30 |
  | avatar_adam_male | Adam | 男 | 25 |
  | avatar_anna_female | Anna | 女 | 25 |
  | avatar_rajput_male | Rajput | 男 | 40 |
  | avatar_mia_female | Mia | 女 | 28 |
  | avatar_river_male | River | 男 | 27 |
  | avatar_marcus_male | Marcus | 男 | 35 |
  | avatar_toto_cartoon | Toto（卡通） | 男 | 15 |
- `contents[].type.ref_image`: 通过 JSON 的格式定义，具体如下：
  ```json
  {
    "type": "ref_image", // 商品图片标识；传入商品内容时必填
    "url": "https://cdn.example.com/1.jpg" // 素材内容，支持通过 url 或 base64 的方式提供；必填
  },
  {
    "type": "ref_image",
    "url": "https://cdn.example.com/2.jpg"
  }
  ```
- `contents[].type.ref_image`: 图片格式支持 .jpg / .jpeg / .png / .webp。
- `contents[].type.ref_image`: 图片文件大小不能超过 50MB。
- `contents[].type.ref_image`: 图片宽高尺寸不小于 300px，图片宽高比要在 1:2.5 ~ 2.5:1 之间。
- `contents[].type.ref_image`: 最多支持同时上传 5 张商品图片。口播带货模式下至少需要 1 张。
- `contents[].type.ref_image`: 商品图建议主体居中、背景干净、光线均匀。提供正面、侧面、细节等多个角度，有助于系统生成更丰富的货品镜头。
- `contents[].type.goods_title`: 通过 JSON 的格式定义，具体如下：
  ```json
  {
    "type": "goods_title", // 商品标题标识；传入商品内容时必填，且恰好 1 条
    "text": "string" // 文本提示词内容，内容长度不能超过 500 个字符；必填
  }
  ```
- `contents[].type.goods_price`: 通过 JSON 的格式定义，具体如下：
  ```json
  {
    "type": "goods_price", // 商品价格标识；选填，最多 1 条
    "text": "399元" // 文本提示词内容，内容长度不能超过 256 个字符
  }
  ```
- `contents[].type.goods_target_audience`: 通过 JSON 的格式定义，具体如下：
  ```json
  {
    "type": "goods_target_audience", // 商品目标人群标识；选填，最多 20 条
    "text": "露营人群" // 文本提示词内容，单条内容长度不能超过 200 个字符
  }
  ```
- `contents[].type.goods_selling_point`: 通过 JSON 的格式定义，具体如下：
  ```json
  {
    "type": "goods_selling_point", // 商品卖点标识；选填，最多 20 条
    "text": "IP67级防尘防水" // 文本提示词内容，单条内容长度不能超过 500 个字符
  }
  ```
- `contents[].type.speech_script`: 通过 JSON 的格式定义，具体如下：
  ```json
  {
    "type": "speech_script", // 完整口播稿标识；必填，且恰好 1 条
    "text": "string" // 文本提示词内容，内容长度不能超过 2000 个字符；必填
  }
  ```
- `contents[].type.speech_script`: 应为适合直接朗读的口语化表达。如文案已定稿不可改写，可将 `settings.allow_polish` 设为 false。
- `contents[].type.speech_script`: 成片时长由系统根据口播稿自动决定，不支持通过请求指定，因此口播稿长度是影响成片时长与费用的主要因素。
- `settings`: 字段名采用 snake_case，同时兼容 camelCase 别名（`aspectRatio`、`allowPolish`、`voiceId`、`speechRate`、`actionPrompt`、`bgmEnabled`）。
- `settings.resolution`: 720p：输出清晰度为 720P 的视频。
  - 1080p：输出清晰度为 1080P 的视频。
- `settings.aspect_ratio`: camelCase 别名：`aspectRatio`。
- `settings.allow_polish`: camelCase 别名：`allowPolish`。
- `settings.allow_polish`: 设为 false 时系统会逐字使用传入的 `speech_script`，只做配音与画面生成，不改写文案。
- `settings.voice_id`: camelCase 别名：`voiceId`。
- `settings.voice_id`: `contents` 中传 `avatar_image` 时必填；传 `avatar_id` 时禁止传入，形象库人物自带音色。
- `settings.voice_id`: 暂不支持传入自定义音色，本字段填入以下音色 ID 之一，清单会随平台上架情况更新。
  
  | voice_id | 音色 |
  | --- | --- |
  | male_calm_informative | 男声·沉稳科普 |
  | female_clear_rational | 女声·理性讲解 |
  | female_gentle_soothing | 女声·温柔治愈 |
  | female_bright_engaging | 女声·明亮带货 |
  | male_crisp_persuasive | 男声·利落种草 |
  | female_intelligent_narrative | 女声·知性叙事 |
  | male_clear_professional | 男声·清朗主持 |
  | male_energetic_sporty | 男声·清爽竞技 |
  | female_warm_rich | 女声·醇厚分享 |
- `settings.speech_rate`: 0.8：比默认语速慢。
  - 1.0：默认语速。
  - 1.2：比默认语速快。
- `settings.speech_rate`: camelCase 别名：`speechRate`。
- `settings.speech_rate`: 仅达人口播模式可用。口播带货模式暂不支持语速调节，该模式下请勿传入本字段，传入将返回参数校验错误。
- `settings.action_prompt`: 内容长度不能超过 2500 个字符。
- `settings.action_prompt`: camelCase 别名：`actionPrompt`。
- `settings.bgm_enabled`: camelCase 别名：`bgmEnabled`。
- `settings.bgm_enabled`: 开启后由系统自动配乐，不支持指定具体背景音乐。
- `options`: ```json
  "options": {
    "callback_url": "https://example.com/cb", // 本次任务结果回调通知地址。如果配置，服务端会在任务状态发生变更时主动通知
    "external_task_id": "string", // 自定义任务ID，可用于查询，需在账号范围内保证唯一性
    "watermark": {
      "enabled": false // 是否生成含水印结果，true为生成，false为不生成；默认为false
    }
  }
  ```
- `options.callback_url`: 长度不能超过 1024 个字符。
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
# 口播带货：传入商品内容
curl --location --request POST 'https://api-beijing.klingai.com/solutions/talking_agent' \
--header 'Authorization: Bearer {apikey}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "contents": [
    {
      "type": "avatar_image",
      "url": "https://cdn.example.com/person.jpg"
    },
    {
      "type": "ref_image",
      "url": "https://cdn.example.com/jbl-front.jpg"
    },
    {
      "type": "ref_image",
      "url": "https://cdn.example.com/jbl-side.jpg"
    },
    {
      "type": "goods_title",
      "text": "JBL GO 4 便携蓝牙音箱"
    },
    {
      "type": "goods_price",
      "text": "399元"
    },
    {
      "type": "goods_target_audience",
      "text": "露营人群"
    },
    {
      "type": "goods_selling_point",
      "text": "IP67级防尘防水"
    },
    {
      "type": "speech_script",
      "text": "周末出门，我不太想带一堆复杂设备。一只 JBL GO 4 便携蓝牙音箱，挂在包上就能带走。"
    }
  ],
  "settings": {
    "resolution": "1080p",
    "aspect_ratio": "9:16",
    "allow_polish": true,
    "voice_id": "male_calm_informative",
    "action_prompt": "说到便携挂环时抬手展示挂环，语气轻松自然。",
    "bgm_enabled": true
  },
  "options": {
    "callback_url": "https://example.com/cb",
    "external_task_id": "my_task_123",
    "watermark": {
      "enabled": false
    }
  }
}'

# 达人口播：不传商品内容
curl --location --request POST 'https://api-beijing.klingai.com/solutions/talking_agent' \
--header 'Authorization: Bearer {apikey}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "contents": [
    {
      "type": "avatar_id",
      "text": "avatar_anna_female"
    },
    {
      "type": "speech_script",
      "text": "人有时候走得太快，就会忘记看看身边。慢一点并不代表停下来。"
    }
  ],
  "settings": {
    "resolution": "720p",
    "aspect_ratio": "16:9",
    "allow_polish": false,
    "bgm_enabled": false
  },
  "options": {
    "callback_url": "https://example.com/cb",
    "external_task_id": "my_task_124"
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
          "type": "video", // 产物类型：video（口播视频）
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

### 口播带货专属错误信息

参数校验错误统一返回 `code: 1201`，具体场景和 message 如下：

| 场景                 | message                                                                                            | 中文提示映射                                                 |
| -------------------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| 人物来源缺失或冲突   | Exactly one avatar source is required: provide avatar_image (with voiceId) or avatar_id, not both. | 人物来源只能二选一：上传人物图（并指定音色）或选择形象库人物 |
| 上传人物图未指定音色 | voiceId is required when uploading an avatar_image.                                                | 上传人物图需指定音色                                         |
| 缺口播内容           | speech_script is required for single-person videos.                                                | 请填写口播文案                                               |
| 有商品信息但无商品图 | Product image is missing. Please upload at least one product image.                                | 请上传商品图（至少 1 张）                                    |
| 有商品图但无标题     | goods_title is required when product content is provided.                                          | 请填写商品标题                                               |
| `speech_rate` 非法   | speechRate only supports 0.8, 1.0 and 1.2.                                                         | 语速仅支持 0.8、1.0 和 1.2                                   |
| 口播带货模式传了语速 | Speech rate adjustment not supported in Video Commerce.                                            | 口播带货模式下不支持语速调节                                 |
| `resolution` 非法    | Unsupported resolution. Only 720p and 1080p are supported.                                         | 分辨率仅支持 720p 和 1080p                                   |
| `aspect_ratio` 非法  | aspect_ratio only supports 9:16 and 16:9.                                                          | 画面比例仅支持 9:16 和 16:9                                  |
| 素材规格不符         | Unsupported image. Please check the image format, size and dimensions.                             | 图片不符合要求，请检查格式、大小和尺寸                       |
| 风控不通过           | Failure to pass the risk control system                                                            | 内容未通过安全审核，请修改后重试                             |
