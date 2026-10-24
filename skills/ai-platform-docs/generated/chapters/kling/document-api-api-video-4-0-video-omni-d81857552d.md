<!-- Official source: https://klingai.com/document-api/api/video/4-0/video-omni.md -->
<!-- Source SHA-256: 8306e7d9f59387c764d08b8a84018a72391b9c851be6e0288fd636a9059cfcda -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://klingai.com/document-api/llms.txt
> Use this file to discover all available pages before exploring further.

# 全能参考生视频

> 来源: https://klingai.com/document-api/api/video/4-0/video-omni
> 语言: zh
> 当前 Tab: 全能参考生视频
> 同组 Tab: 文生视频 / 图生视频 / 全能参考生视频 / 主体管理 / 音色管理
> 此内容为面向 LLM 优化的 Markdown，已展开页面内 Tab，并省略页面目录、复制按钮等 UI 控件。

---

## 创建任务

### 接口概览

- Method: `POST`
- Path: `/omni-video/kling-4.0`
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
| `contents` | array | 是 | - | - | 参考素材合集，如提示词、图片、视频、主体、音色等 |
| `contents[].type` | string | 是 | - | `prompt`, `first_frame`, `middle_frame`, `last_frame`, `refer_image`, `feature_video`, `base_video`, `element`, `voice` | 素材类型，支持：提示词、图片、视频、主体、音色 |
| `settings` | object | 否 | - | - | 输出配置相关参数，如清晰度、时长等 |
| `settings.resolution` | string | 否 | `1080p` | `720p`, `1080p` | 生成视频的清晰度 |
| `settings.aspect_ratio` | string | 否 | `adaptive` | `21:9`, `16:9`, `9:16`, `1:1`, `adaptive` | 生成视频的画面纵横比（宽:高） |
| `settings.duration` | int | 否 | `10` | `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`, `16`, `17`, `18`, `19`, `20`, `21`, `22`, `23`, `24`, `25`, `26`, `27`, `28`, `29`, `30` | 生成视频时长，单位 s |
| `options` | object | 否 | - | - | 通用配置，如回调地址、是否含水印等 |
| `options.callback_url` | string | 否 | - | - | 本次任务结果回调通知地址 |
| `options.external_task_id` | string | 否 | - | - | 自定义任务ID |
| `options.watermark_info` | object | 否 | - | - | 是否同时生成含水印的结果 |
| `options.watermark_info.enabled` | boolean | 否 | `false` | - | true 为生成，false 为不生成 |

#### Request Body 字段补充说明

- `contents`: 参考格式如下，参数说明详见下文：
- `contents`: ```json
  "contents": [
    {
      "type": "prompt",
      "text": "string"
    },
    {
      "type": "first_frame",
      "url": "string",
      "id": "string"
    },
    {
      "type": "middle_frame",
      "url": "string",
      "id": "string"
    },
    {
      "type": "last_frame",
      "url": "string",
      "id": "string"
    },
    {
      "type": "refer_image",
      "url": "string",
      "id": "string"
    },
    {
      "type": "feature_video",
      "url": "string",
      "id": "string"
    },
    {
      "type": "base_video",
      "url": "string",
      "id": "string"
    },
    {
      "type": "element",
      "element_id": "string",
      "id": "string"
    },
    {
      "type": "voice",
      "voice_id": "string",
      "id": "string"
    }
  ]
  ```
- `contents[].type.prompt`: 文本提示词内容长度与字符类型有关。如为纯英文，内容长度不超过26,000个字符；如为纯非英文，内容长度不能超过11,000个字符；如为英文&非英文混合输入，需保持英文字符数 ÷ 26,000 + 非英文字符数 ÷ 11,000 ≤ 1。
- `contents[].type.prompt`: 通过JSON的格式定义，具体如下：
- `contents[].type.prompt`: ```json
  {
    "type": "prompt", // 素材类型，固定参数值：prompt；必填
    "text": "string" // 文本提示词内容；必填
  }
  ```
- `contents[].type.prompt`: > **可灵视频 4.0 可通过 Prompt 描述素材用途、画面内容、事件顺序及声音要求，实现多素材参考生成与视频编辑。**
  >
  > 
  > 1. **通过自定义素材 ID 引用素材。** 在 `contents` 中定义图片、视频或主体等素材对象时，为其设置 `id`，并在 Prompt 中使用 `@id` 引用。例如，为 `refer_image` 对象设置 `"id": "image_1"` 后，通过 `@image_1` 引用该图片。同一任务内的素材 ID 不得重复。
  >
  > 
  > 2. **明确每份素材的用途与作用范围。** 例如，“保持 `@image_1` 中人物的面孔、发型与服装”“参考 `@video_1` 的动作节奏，不使用其中的背景”。仅引用素材而不说明用途时，模型会自行推断，可能影响结果与预期的一致性。
  >
  > 
  > 3. **建议按“素材用途＋整体设定＋分段事件＋声音要求”组织提示词。** 根据需要描述场景、视觉风格、镜头运动、动作顺序、台词、环境声、配乐与音效；视频编辑场景还应明确需要修改和保留的内容。详细信息见 [可灵4.0使用指南](https://docs.qingque.cn/d/home/eZQBwtYbPcQQkDUf3zQ56oqeW?identityId=1zDWrpFHUKR)。
- `contents[].type.first_frame / middle_frame / last_frame / refer_image`: 图片可作为场景、风格等参考图，也可作为关键帧生成视频。
- `contents[].type.first_frame / middle_frame / last_frame / refer_image`: 通过JSON的格式定义，具体如下：
- `contents[].type.first_frame / middle_frame / last_frame / refer_image`: ```json
  {
    "type": "string", // 图片素材标识，依次对应枚举值：first_frame、middle_frame、last_frame、refer_image；必填
    "url": "string", // 素材内容，支持通过url或base64的方式提供；必填
    "id": "string" // 素材索引ID，用于在prompt中指定，同任务中当前参数不得重复
  }
  ```
- `contents[].type.first_frame / middle_frame / last_frame / refer_image`: 图片格式支持.jpg / .jpeg / .png。
- `contents[].type.first_frame / middle_frame / last_frame / refer_image`: 图片文件大小不能超过30MB。
- `contents[].type.first_frame / middle_frame / last_frame / refer_image`: 图片宽高尺寸不小于300px，图片宽高比要在2:5 ~ 5:2之间。
- `contents[].type.first_frame / middle_frame / last_frame / refer_image`: 如果有多张middle_frame、多张refer_image，id 参数必填。
- `contents[].type.first_frame / middle_frame / last_frame / refer_image`: 图片数量不得超过10。
- `contents[].type.first_frame / middle_frame / last_frame / refer_image`: 图片数量 + 视频数量 + 主体数量 + 音色数量之和不得超过15。
- `contents[].type.feature_video / base_video`: 视频可作为特征参考视频 feature_video，也可作为待编辑视频 base_video。
- `contents[].type.feature_video / base_video`: 通过JSON的格式定义，具体如下：
- `contents[].type.feature_video / base_video`: ```json
  {
    "type": "string", // 视频素材标识，依次对应枚举值：feature_video、base_video；必填
    "url": "string", // 素材内容，支持通过url的方式提供；必填
    "id": "string" // 素材索引ID，用于在prompt中指定，同任务中当前参数不得重复；选填
  }
  ```
- `contents[].type.feature_video / base_video`: 视频格式支持.mp4 / .mov。
- `contents[].type.feature_video / base_video`: 视频文件大小不能超过300MB。
- `contents[].type.feature_video / base_video`: 单个视频时长与视频总时长均需介于3秒（含）和30秒（含）之间，视频总时长包含特征参考视频、待编辑视频和视频角色主体的时长。
- `contents[].type.feature_video / base_video`: 视频宽高尺寸需介于700px（含）和4553px（含）之间，像素总面积不超过8294400，视频的宽高比需在2:5~5:2之间。
- `contents[].type.feature_video / base_video`: 支持 24～60 fps 的输入视频；生成视频帧率为 24 fps。
- `contents[].type.feature_video / base_video`: 参考视频数量与是否有视频角色主体有关：
    - 当无视频角色主体时，最多支持5个参考视频输入。
    - 当有视频角色主体时，视频角色主体数量和参考视频数量总计不超过5个。
    - 其中最多添加1段待编辑视频base_video。
- `contents[].type.feature_video / base_video`: 图片数量 + 视频数量 + 主体数量 + 音色数量之和不得超过15。
- `contents[].type.element`: 通过JSON的格式定义，具体如下：
- `contents[].type.element`: ```json
  {
    "type": "element", // 素材类型，固定参数值：element；必填
    "element_id": "string", // 主体ID，由系统生成，通过查询主体相关API返回；必填
    "id": "string" // 素材索引ID，用于在prompt中指定，同任务中当前参数不得重复；必填
  }
  ```
- `contents[].type.element`: 主体分为通过视频定制的主体（简称：视频角色主体）和通过图片定制的主体（简称：多图主体），适用范围不同，请注意区分。
- `contents[].type.element`: 主体数量上限：
    - 最多支持7个主体，其中视频角色主体不得超过3个。
    - 如果有视频角色主体，视频角色主体和参考视频总数量不得超过5个。
- `contents[].type.element`: 图片数量 + 视频数量 + 主体数量 + 音色数量之和不得超过15。
- `contents[].type.element`: 更多官方主体信息详见：[可灵「主体库 3.0」使用指南](https://docs.qingque.cn/d/home/eZQCXlb985uYAZ-c8NgyTv11X?identityId=2Cn18n4EIHT#section=h.ihbooeem1vo)。
- `contents[].type.voice`: 通过JSON的格式定义，具体如下：
- `contents[].type.voice`: ```json
  {
    "type": "voice", // 素材类型，固定参数值：voice；必填
    "voice_id": "string", // 音色ID，由系统生成，通过音色定制相关API返回；必填
    "id": "string" // 素材索引ID，用于在prompt中指定，同任务中当前参数不得重复；必填
  }
  ```
- `contents[].type.voice`: 至多引用3个音色。
- `contents[].type.voice`: voice_id参数值通过音色定制接口返回，也可使用系统预置音色，详见 [音色定制](https://klingai.com/document-api/api/video/3-0-omni/voice-customization)。
- `settings.resolution`: 720p：输出清晰度为 720P 的视频
- `settings.resolution`: 1080p：输出清晰度为 1080P 的视频
- `settings.aspect_ratio`: 传入明确的比例值时，以参数指定的比例为准。
- `settings.aspect_ratio`: 未传入该参数，或用户传入 adaptive 时，模型会识别并遵循 Prompt 中的画面比例意图，例如“生成一段 9:16 的竖屏视频”。
- `settings.aspect_ratio`: 如若 Prompt 中未识别到明确的比例意图，则依次根据待编辑视频 base_video、关键帧图片、其他输入视频的比例确定输出比例；均不适用时，使用默认比例 16:9。存在多张关键帧时，优先采用首帧比例；未提供首帧时，采用第一张关键帧图片的比例。
- `settings.duration`: 传入该参数时，以参数指定的时长为准。
- `settings.duration`: 未传入该参数时，模型会识别并遵循 Prompt 中的时长意图，例如“生成一段 15 秒的视频”。
- `settings.duration`: 如若 Prompt 中未识别到明确的时长意图，则优先采用待编辑视频 base_video 的时长；未提供 base_video 时，使用默认时长 10 秒。
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
curl --location 'https://api-beijing.klingai.com/omni-video/kling-4.0' \
  --header 'Content-Type: application/json' \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --data '{
    "contents": [
      {
        "type": "prompt",
        "text": "Change the color of the parrot’s feathers to match the reference image. Keep all other elements of the video unchanged."
      },
      {
        "type": "first_frame",
        "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release_note/image_7.1.png",
        "id": "image_1"
      },
      {
        "type": "refer_image",
        "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release_note/image_7.1.png",
        "id": "image_2"
      }
    ],
    "settings": {
      "resolution": "1080p",
      "duration": 10,
      "aspect_ratio": "adaptive"
    },
    "options": {
      "callback_url": "https://xxx/callback",
      "external_task_id": ""
    }
  }'
```

### Response Example

```json
{
  "code": 0, // 错误码；具体定义见错误码
  "message": "string", // 错误信息
  "request_id": "string", // 请求ID，系统生成，用于跟踪请求、排查问题
  "data": {
    "id": "string", // 系统生成的任务ID
    "status": "string", // 任务状态，枚举值：submitted（已提交）、processing（处理中）、succeeded（成功）、failed（失败）
    "create_time": 1781080778802, // 任务创建时间，Unix时间戳、单位ms
    "update_time": 1781080794151, // 任务更新时间，Unix时间戳、单位ms
    "external_id": "string" // 该任务的自定义任务ID（如有）
  }
}
```

## 更多场景调用示例

### 特征参考视频

```cURL
curl --location --request POST \
  'https://api-beijing.klingai.com/omni-video/kling-4.0' \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data-raw '{
    "contents": [
      {
        "type": "prompt",
        "text": "参考 @video_1 的打斗动作与出招节奏，角色造型来自 @image_1 @image_2。"
      },
      {
        "type": "feature_video",
        "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch12_2_fight_motion_source.mp4",
        "id": "video_1"
      },
      {
        "type": "refer_image",
        "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch12_2_dark_hair_fighter_ref.png",
        "id": "image_1"
      },
      {
        "type": "refer_image",
        "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch12_2_silver_hair_fighter_ref.png",
        "id": "image_2"
      }
    ],
    "settings": {
      "duration": 15,
      "resolution": "1080p",
      "aspect_ratio": "adaptive"
    }
  }'
```

### 视频编辑

```cURL
curl --location --request POST \
  'https://api-beijing.klingai.com/omni-video/kling-4.0' \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data-raw '{
    "contents": [
      {
        "type": "prompt",
        "text": "编辑 @video_1，在视频最后箱子再次被打开时，@element_1 正躺在里面睡觉。最后一句台词“Ah, it'\''s all old stuff.”改为“Why is there a pig here?”。"
      },
      {
        "type": "base_video",
        "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch12_6_box_source.mp4",
        "id": "video_1"
      },
      {
        "type": "element",
        "element_id": "173",
        "id": "element_1"
      }
    ],
    "settings": {
      "duration": 10,
      "resolution": "1080p",
      "aspect_ratio": "adaptive"
    }
  }'
```

### 音色参考

```cURL
curl --location 'https://api-beijing.klingai.com/omni-video/kling-4.0' \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data-raw '{
    "contents": [
      {
        "type": "prompt",
        "text": "Use @image_1 as the character reference. A girl sits by the window on a moving train, quietly gazing outside with a melancholic expression. After a few moments, the camera slowly pulls back, revealing more of the train carriage and other passengers. The girl stands up from her seat and carefully walks down the aisle. As she passes another passenger, she turns slightly and politely says in English using @1: \"Excuse me.\" Natural body movements, realistic facial expressions, accurate lip synchronization, cinematic lighting, continuous camera movement."
      },
      {
        "type": "refer_image",
        "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release_note/image_25.png",
        "id": "image_1"
      },
      {
        "type": "voice",
        "voice_id": "829826751244537879",
        "id": "1"
      }
    ],
    "settings": {
      "resolution": "1080p",
      "duration": 5,
      "aspect_ratio": "9:16"
    },
    "options": {
      "watermark_info": {
        "enabled": false
      }
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
      "usage": { // 计费用量：仅任务结束且存在用量时返回，否则省略
        "input_duration": "8.03" // 输入视频总时长（包括视频主体），单位秒、两位小数字符串；仅 4.0 有视频输入时有值
      },
      "billing": [
        {
          "charge_type": "string", // 消耗账户类型，如果消耗的是额度则参数值为cash，如果是消耗资源包则参数值为unit
          "cash_type": "string", // 额度类型，仅存在于消耗额度场景（charge_type=cash）；如果消耗的是正式额度则参数值为balance，如果是消耗的是测试金则参数值为test_balance
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
      "values": ["video"]
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
        "values": ["video"]
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
        "usage": { // 计费用量：仅任务结束且存在用量时返回，否则省略
          "input_duration": "8.03" // 输入视频总时长（包括视频主体），单位秒、两位小数字符串；仅 4.0 有视频输入时有值
        },
        "billing": [
          {
            "charge_type": "string", // 消耗账户类型，如果消耗的是额度则参数值为 cash，如果消耗资源包则参数值为 unit
            "cash_type": "string", // 额度类型，仅存在于消耗额度场景（charge_type=cash）；如果消耗的是正式额度则参数值为balance，如果是消耗的是测试金则参数值为test_balance
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
