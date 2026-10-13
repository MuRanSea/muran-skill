<!-- Official source: https://cloud.tencent.com/document/product/1823/135756 -->
<!-- Source SHA-256: a95ecf011842442379852bd5edb208fe22dabcc8a46ec7a76dca91885f228707 -->

# Vidu 生视频调用指南

官方来源：https://cloud.tencent.com/document/product/1823/135756
最近更新时间：2026-10-09 10:22:50

## 概述

Vidu 是生数科技推出的视频生成模型系列，支持**文生视频、图生视频、多图参考生视频、首尾帧生视频**等能力，具备智能切镜、音画同出等特性。本文介绍如何通过 TokenHub 调用 Vidu 的六款视频模型：`vidu-video-q2`、`vidu-video-q2-pro`、`vidu-video-q2-turbo`、`vidu-video-q3`、`vidu-video-q3-pro`、`vidu-video-q3-turbo`。

### 前提条件

已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号并开通 TokenHub 服务。

已在 [TokenHub 控制台](https://console.cloud.tencent.com/tokenhub/apikey) 获取 API Key。

在 [控制台-在线推理-视觉模型](https://console.cloud.tencent.com/tokenhub/inference?regionId=1&serviceType=VISION) 处开启对应模型的后付费。

**说明：**

下文所有示例中的 YOUR\_API\_KEY 均需替换为您自己的 API Key，鉴权方式为请求头 Authorization: Bearer YOUR\_API\_KEY。

### 调用流程

视频生成为耗时任务，接口采用**异步调用**模式，统一分两步：

1. **提交任务**：调用生成接口，成功返回 `task_id` 与初始状态 `created`。

2. **轮询结果**：携带 `task_id` 调用「查询任务结果」接口，直至 `state = success`，从结果中获取视频地址。

**注意：**

任务状态：created（创建成功）/ queueing（排队中）/ processing（处理中）/ success（成功）/ failed（失败）。

所有接口响应均包含 `request_id`（顶层，用于排查问题）；查询接口额外返回 tokenhub\_usage（用量消耗）。

### 模型列表

| 模型名称 | model 参数值 | 支持能力 | 视频时长（秒） | 清晰度档位 | 选型建议 |
| --- | --- | --- | --- | --- | --- |
| Vidu-Video-q3.0 | `vidu-video-q3` | 参考生 / 智能切镜 / 音画同出 | 参考生 3~16 | 540p / 720p / 1080p | 多机位一致性更出色 |
| Vidu-Video-q3.0-pro | `vidu-video-q3-pro` | 文生 / 图生 / 首尾帧 / 智能切镜 / 音画同出 | 文生、图生、首尾帧 1~16 | 540p / 720p / 1080p | Q3 高画质版 |
| Vidu-Video-q3.0-turbo | `vidu-video-q3-turbo` | 文生 / 图生 / 参考生 / 首尾帧 / 智能切镜 / 音画同出 | 文生、图生、首尾帧 1~16；参考生 3~16 | 540p / 720p / 1080p | 生成速度最快、性价比最高 |
| Vidu-Video-q2.0 | `vidu-video-q2` | 文生 / 参考生 | 1 ~ 10 | 540p / 720p / 1080p | 动态效果好、细节丰富 |
| Vidu-Video-q2.0-pro | `vidu-video-q2-pro` | 图生 / 参考生 / 首尾帧 | 图生 1~10；参考生 0~10；首尾帧 1~8 | 540p / 720p / 1080p | 参考生支持视频参考，唯一支持视频输入 |
| Vidu-Video-q2.0-turbo | `vidu-video-q2-turbo` | 图生 / 首尾帧 | 图生 1~10；首尾帧 1~8 | 540p / 720p / 1080p | Q2 快速版 |

**说明：**

各接口实际支持的 model 取值与 `duration` 取值范围以各接口「输入参数」中的说明为准，不同能力的时长范围存在差异，请参见 [附录：各接口时长取值速查](https://cloud.tencent.com/document/product/1823/135756#.E5.90.84.E6.8E.A5.E5.8F.A3.E6.97.B6.E9.95.BF.E5.8F.96.E5.80.BC.E9.80.9F.E6.9F.A5)。

`q3` 系列支持智能切镜与音画同出（`audio`）；`q2` 系列支持 `bgm`、`movement_amplitude` 等。

参考生视频的 `videos` 视频参考与视频主体仅 `vidu-video-q2-pro` 支持。

## 文生视频

### 1. 接口描述

通过纯文本提示词创建文生视频任务，可指定时长、比例、分辨率、运动幅度、音视频直出与 BGM 等参数。

**接口：** `POST https://tokenhub.tencentmaas.com/v1/wand/vidu/text-to-video`

### 2. 输入参数

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| model | 是 | string | 模型名称。取值：`vidu-video-q3-turbo`、`vidu-video-q3-pro`、`vidu-video-q2` |
| prompt | 是 | string | 文本提示词。≤ 5000 字符。 |
| style | 否 | string | 风格。默认 general；可选 general（通用）/ anime（动漫）。**q2、q3 系列不生效。** |
| duration | 否 | integer | 视频时长（秒）。q3 系列可选 1~16；q2 系列可选 1~10。默认值：5。 |
| aspect\_ratio | 否 | string | 画面宽高比。默认 16:9；可选 16:9 / 9:16 / 3:4 / 4:3 / 1:1（部分比例仅特定模型支持）。 |
| resolution | 否 | string | 分辨率。默认值依模型与时长而定；常见可选 540p / 720p / 1080p。 |
| movement\_amplitude | 否 | string | 运动幅度。默认 auto；可选 auto / small / medium / large。**q2、q3 系列不生效。** |
| bgm | 否 | boolean | 是否添加背景音乐。默认 false。**q3 系列不生效。** |
| audio | 否 | boolean | 是否音视频直出（输出带台词/音效的有声视频）。**仅 q3 系列支持**；默认视模型而定。 |
| audio\_type | 否 | string | 音频类型（audio=true 时必填）。默认 all；可选 all / speech\_only / sound\_effect\_only。 |
| seed | 否 | integer | 随机种子。不传或传 0 时使用随机数。 |
| payload | 否 | string | 透传参数。≤ 1,048,576 字符。 |
| watermark | 否 | boolean | 是否添加水印。默认 false。 |
| wm\_position | 否 | integer | 水印位置。TokenHub 不支持该参数。开启 watermark 默认添加腾讯水印在左上角。 |
| wm\_url | 否 | string | 自定义水印图片 URL；不传使用默认水印。 |

### 3. 请求示例

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/vidu/text-to-video' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "vidu-video-q2",
  "prompt": "一只橙色小猫在窗台上看向镜头"
}'
```

**说明：**

将示例中的 `model` 替换为 `vidu-video-q3-turbo` 或 `vidu-video-q3-pro`，即可调用对应模型；duration / aspect\_ratio / resolution / audio 等参数详见 [输入参数](https://cloud.tencent.com/document/product/1823/135756#2.-.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0)。

### 4. 输出参数

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| task\_id | string | Vidu 生成的任务 ID |
| state | string | 处理状态：created / queueing / processing / success / failed |
| model | string | 本次调用的模型名称 |
| prompt | string | 本次调用的提示词参数 |
| duration | integer | 本次调用的视频时长参数 |
| aspect\_ratio | string | 本次调用的比例参数 |
| resolution | string | 本次调用的分辨率参数 |
| audio | boolean | 本次调用是否开启音视频直出 |
| seed | integer | 本次调用的随机种子参数 |
| credits | integer | 本次调用消耗的积分数 |
| created\_at | string | 任务创建时间（ISO 8601） |
| request\_id | string | 唯一请求标识，用于排查问题。 |

### 5. 响应示例

```json
{
  "task_id": "4-WandVideo-a786becfdc80433b8cff4aa344c8fd3d",
  "state": "created",
  "model": "vidu-video-q3-turbo",
  "prompt": "一只小猫在月光下奔跑，镜头跟随",
  "duration": 5,
  "aspect_ratio": "16:9",
  "resolution": "720p",
  "audio": true,
  "seed": 0,
  "credits": 100,
  "created_at": "2026-07-31T15:41:31.968Z",
  "request_id": "3aec3299-06ad-4654-8b45-c57b823a15d2"
}
```

### 6. 错误码

请求失败时返回错误码，具体见错误信息。常见错误码见 [附录：统一错误码](https://cloud.tencent.com/document/product/1823/135756#.E7.BB.9F.E4.B8.80.E9.94.99.E8.AF.AF.E7.A0.81)。

## 图生视频

### 1. 接口描述

以一张首帧图像为起点生成视频，可选文本提示词、音视频直出、指定音色与推荐提示词等。输出画幅跟随输入图片比例（无 `aspect_ratio` 参数）。

**接口：** `POST https://tokenhub.tencentmaas.com/v1/wand/vidu/image-to-video`

### 2. 输入参数

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| model | 是 | string | 模型名称。取值：`vidu-video-q3-turbo`、`vidu-video-q3-pro`、`vidu-video-q2-pro`、`vidu-video-q2-turbo` |
| images | 是 | array[string] | 首帧图像（仅 1 张）。支持图片 URL 或 Base64；png/jpeg/jpg/webp；比例 < 1:4 或 4:1；≤ 50MB；POST body ≤ 20MB |
| prompt | 否 | string | 文本提示词。≤ 5000 字符。使用 is\_rec 时本参数被忽略 |
| audio | 否 | boolean | 是否音视频直出。默认 false（q3-pro/turbo 默认 true） |
| audio\_type | 否 | string | 音频类型（audio=true 时必填）。默认 all；可选 all / speech\_only / sound\_effect\_only |
| voice\_id | 否 | string | 音色 ID（**q3 系列不生效**）。为空时系统自动推荐 |
| is\_rec | 否 | boolean | 是否使用推荐提示词。true 时系统自动推荐并生成（每任务多消耗 10 积分） |
| bgm | 否 | boolean | 是否添加背景音乐。默认 false（**q3 系列不生效**） |
| duration | 否 | integer | 视频时长（秒）。q3 系列默认 5、可选 1~16；q2-pro / q2-turbo 默认 5、可选 1~10。默认值：5 |
| resolution | 否 | string | 分辨率。默认值依模型与时长而定；常见可选 540p / 720p / 1080p |
| movement\_amplitude | 否 | string | 运动幅度。默认 auto；可选 auto / small / medium / large（**q2、q3 不生效**） |
| seed | 否 | integer | 随机种子。不传或传 0 时使用随机数 |
| payload / watermark / wm\_position / wm\_url | 否 | - | 通用配置，同「文生视频」 |

### 3. 请求示例

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/vidu/image-to-video' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "vidu-video-q3-turbo",
  "images": ["https://example.com/start.jpg"],
  "prompt": "让画面中的主体自然运动，镜头缓慢推近",
  "duration": 5,
  "resolution": "720p",
  "audio": true
}'
```

### 4. 输出参数

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| task\_id | string | Vidu 生成的任务 ID |
| state | string | 处理状态：created / queueing / processing / success / failed |
| model | string | 本次调用的模型名称 |
| prompt | string | 本次调用的提示词参数 |
| images | array[string] | 本次调用的图像参数 |
| duration | integer | 本次调用的视频时长参数 |
| audio | boolean | 本次调用是否音画同出 |
| seed | integer | 本次调用的随机种子参数 |
| resolution | string | 本次调用的分辨率参数 |
| credits | integer | 本次调用消耗的积分数 |
| created\_at | string | 任务创建时间（ISO 8601） |
| request\_id | string | 唯一请求标识，用于排查问题 |

### 5. 响应示例

```json
{
  "task_id": "4-WandVideo-a786becfdc80433b8cff4aa344c8fd3d",
  "state": "created",
  "model": "vidu-video-q3-turbo",
  "prompt": "让画面中的主体自然运动，镜头缓慢推近",
  "images": ["https://example.com/start.jpg"],
  "duration": 5,
  "audio": true,
  "seed": 0,
  "resolution": "720p",
  "credits": 100,
  "created_at": "2026-07-31T15:41:31.968Z",
  "request_id": "3aec3299-06ad-4654-8b45-c57b823a15d2"
}
```

### 6. 错误码

请求失败时返回错误码，具体见错误信息。常见错误码见 [附录：统一错误码](https://cloud.tencent.com/document/product/1823/135756#.E7.BB.9F.E4.B8.80.E9.94.99.E8.AF.AF.E7.A0.81)。

## 多图参考生视频

### 1. 接口描述

以参考素材（图片/视频/主体）保持主体一致性生成视频，支持两种调用方式：**方式一**使用 `subjects` 主体（可在 prompt 中以 `@主体名` 引用）；**方式二**直接使用顶层 `images`/`videos` 参考。两者必选其一。

**接口：** `POST https://tokenhub.tencentmaas.com/v1/wand/vidu/reference-to-video`

### 2. 输入参数

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| model | 是 | string | 模型名称。取值：`vidu-video-q3-turbo`、`vidu-video-q3`、`vidu-video-q2-pro`、`vidu-video-q2` |
| subjects | 条件必选 | array[object] | 主体集合（方式一，与 images/videos 二选一）。子字段见下表 |
| images | 条件必选 | array[string] | 图像参考（方式二，1~7 张）。支持图片 URL 或 Base64；png/jpeg/jpg/webp；像素 ≥ 128×128；比例 < 1:4 或 4:1；≤ 50MB |
| videos | 条件必选 | array[string] | 视频参考（方式二，1~2 个，**仅 q2-pro 支持**）。1 个 8 秒或 2 个 5 秒；mp4/avi/mov；≤ 100MB |
| prompt | 是 | string | 文本提示词。主体方式 ≤ 5000 字符（可用 `@主体名` 引用）；直接参考方式 ≤ 2000 字符 |
| auto\_subjects | 否 | boolean | 是否使用智能主体库能力。默认 false |
| audio | 否 | boolean | 是否音视频直出。q3/q3-turbo 默认 true，其他默认 false；非主体调用时仅 q3 支持 |
| audio\_type | 否 | string | 音频类型（audio=true 时必填）。默认 all；可选 all / speech\_only / sound\_effect\_only |
| duration | 否 | integer | 视频时长（秒）。q3 系列可选 3~16；q2-pro 可选 0~10（**0 表示由模型自动判断时长**）；q2 可选 1~10。默认值：5 |
| aspect\_ratio | 否 | string | 画面宽高比。默认 16:9；可选 16:9 / 9:16 / 3:4 / 4:3 / 1:1 |
| resolution | 否 | string | 分辨率。默认值依模型而定；常见可选 540p / 720p / 1080p |
| movement\_amplitude | 否 | string | 运动幅度。默认 auto；可选 auto / small / medium / large（**q2、q3 不生效**） |
| bgm | 否 | boolean | 是否添加背景音乐。默认 false（**q3 系列不生效**） |
| seed / payload / watermark / wm\_position / wm\_url | 否 | - | 通用配置，同「文生视频」 |

**subjects 数组元素子字段：**

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| name | 是 | string | 主体 ID/名称，后续在 prompt 中以 `@name` 引用。 |
| images | 条件必选 | array[string] | 主体图片（与 videos 必填其一）。最多 3 张；URL 或 Base64；png/jpeg/jpg/webp；比例 < 1:4 或 4:1；Base64 解码 < 20MB。 |
| videos | 条件必选 | array[string] | 主体视频（与 images 必填其一，**仅 q2-pro 支持**）。1 个 5 秒视频；mp4/avi/mov；像素 ≥ 128×128。 |
| voice\_id | 否 | string | 主体音色 ID（**q3 参考生不生效**）。为空时自动推荐。 |

**说明：**

**主体数量限制：**

q3/q2：图片/文字主体最多 7 个，不支持视频主体。

q2-pro：图片/文字主体最多 4 个，视频主体最多 1 个。

### 3. 请求示例

**方式一：subjects 主体**

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/vidu/reference-to-video' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "vidu-video-q3-turbo",
  "subjects": [
    { "name": "girl", "images": ["https://example.com/girl1.jpg"] },
    { "name": "boy", "images": ["https://example.com/boy1.jpg"] }
  ],
  "prompt": "@girl 和 @boy 在一起吃火锅",
  "duration": 8,
  "audio": true
}'
```

**方式二：直接 images 参考**

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/vidu/reference-to-video' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "vidu-video-q2",
  "images": [
    "https://example.com/input.jpg"
  ],
  "prompt": "保持参考图主体外观并自然移动"
}'
```

### 4. 输出参数

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| task\_id | string | Vidu 生成的任务 ID |
| state | string | 处理状态：created / queueing / processing / success / failed |
| model | string | 本次调用的模型名称 |
| prompt | string | 本次调用的提示词参数 |
| images | array[string] | 本次调用的图像参数 |
| videos | array[string] | 本次调用的视频参数（方式二/视频主体） |
| duration | integer | 本次调用的视频时长参数 |
| audio | boolean | 本次调用是否开启音视频直出 |
| seed | integer | 本次调用的随机种子参数 |
| credits | integer | 本次调用消耗的积分数 |
| created\_at | string | 任务创建时间（ISO 8601） |
| request\_id | string | 唯一请求标识，用于排查问题 |

### 5. 响应示例

```json
{
  "task_id": "4-WandVideo-a786becfdc80433b8cff4aa344c8fd3d",
  "state": "created",
  "model": "vidu-video-q3-turbo",
  "prompt": "@girl 和 @boy 在一起吃火锅",
  "images": ["https://example.com/girl1.jpg", "https://example.com/boy1.jpg"],
  "duration": 8,
  "audio": true,
  "seed": 0,
  "credits": 100,
  "created_at": "2026-07-31T15:41:31.968Z",
  "request_id": "3aec3299-06ad-4654-8b45-c57b823a15d2"
}
```

### 6. 错误码

请求失败时返回错误码，具体见错误信息。常见错误码见 [附录：统一错误码](https://cloud.tencent.com/document/product/1823/135756#.E7.BB.9F.E4.B8.80.E9.94.99.E8.AF.AF.E7.A0.81)。

## 首尾帧生视频

### 1. 接口描述

以两张图片（首帧 + 尾帧）为端点生成过渡视频，可选文本提示词、推荐提示词、音视频直出与 BGM。

**接口：** `POST https://tokenhub.tencentmaas.com/v1/wand/vidu/start-end-to-video`

### 2. 输入参数

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| model | 是 | string | 模型名称。取值：`vidu-video-q3-turbo`、`vidu-video-q3-pro`、`vidu-video-q2-pro`、`vidu-video-q2-turbo` |
| images | 是 | array[string] | 首尾帧图像：第 1 张为首帧、第 2 张为尾帧。支持图片 URL 或 Base64；首尾帧分辨率需相近（比值 0.8~1.25）；png/jpeg/jpg/webp；比例 < 1:4 或 4:1；≤ 50MB。 |
| prompt | 否 | string | 文本提示词。≤ 5000 字符。使用 is\_rec 时本参数被忽略。 |
| is\_rec | 否 | boolean | 是否使用推荐提示词。true 时系统自动推荐并生成（每任务多消耗 10 积分）。 |
| duration | 否 | integer | 视频时长（秒）。q3 系列默认 5、可选 1~16；q2-pro / q2-turbo 默认 5、可选 1~8。默认值：5。 |
| resolution | 否 | string | 分辨率。默认值依模型而定；常见可选 540p / 720p / 1080p。 |
| movement\_amplitude | 否 | string | 运动幅度。默认 auto；可选 auto / small / medium / large（**q2、q3 不生效**）。 |
| audio | 否 | boolean | 是否音视频直出。默认 true；**仅 q3 系列支持。** |
| bgm | 否 | boolean | 是否添加背景音乐。默认 false（**q3 系列不生效**）。 |
| seed / payload / watermark / wm\_position / wm\_url | 否 | - | 通用配置，同「文生视频」 |

**说明：**

建议首帧与尾帧图片保持相近的分辨率与比例，以获得最佳过渡效果。

### 3. 请求示例

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/vidu/start-end-to-video' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "vidu-video-q3-turbo",
  "images": ["https://example.com/start.jpg", "https://example.com/end.jpg"],
  "prompt": "从首帧自然过渡到尾帧",
  "duration": 5,
  "resolution": "720p"
}'
```

### 4. 输出参数

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| task\_id | string | Vidu 生成的任务 ID |
| state | string | 处理状态：created / queueing / processing / success / failed |
| model | string | 本次调用的模型名称 |
| prompt | string | 本次调用的提示词参数 |
| images | array[string] | 本次调用的图像参数（首帧、尾帧） |
| duration | integer | 本次调用的视频时长参数 |
| seed | integer | 本次调用的随机种子参数 |
| resolution | string | 本次调用的分辨率参数 |
| credits | integer | 本次调用消耗的积分数 |
| created\_at | string | 任务创建时间（ISO 8601） |
| request\_id | string | 唯一请求标识，用于排查问题 |

### 5. 响应示例

```json
{
  "task_id": "4-WandVideo-a786becfdc80433b8cff4aa344c8fd3d",
  "state": "created",
  "model": "vidu-video-q3-turbo",
  "prompt": "从首帧自然过渡到尾帧",
  "images": ["https://example.com/start.jpg", "https://example.com/end.jpg"],
  "duration": 5,
  "seed": 0,
  "resolution": "720p",
  "credits": 100,
  "created_at": "2026-07-31T15:41:31.968Z",
  "request_id": "3aec3299-06ad-4654-8b45-c57b823a15d2"
}
```

### 6. 错误码

请求失败时返回错误码，具体见错误信息。常见错误码见 [附录：统一错误码](https://cloud.tencent.com/document/product/1823/135756#.E7.BB.9F.E4.B8.80.E9.94.99.E8.AF.AF.E7.A0.81)。

## 查询任务结果

### 1. 接口描述

各生成接口共用的任务查询方式：提交任务返回 `task_id` 后，通过本接口轮询任务状态，成功后从结果中获取视频地址。

**接口：** `GET https://tokenhub.tencentmaas.com/v1/wand/vidu/tasks/{task_id}`

**说明：**

路径中的 `{task_id}` 即提交任务时返回的 `task_id`（示例中以 `YOUR_TASK_ID` 占位）。视频生成约需 1~5 分钟，建议每 5~10 秒轮询一次。

### 2. 输入参数

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| task\_id | 是 | string | 任务 ID（路径参数），即提交任务时返回的 `task_id` |

### 3. 请求示例

```bash
curl -X GET 'https://tokenhub.tencentmaas.com/v1/wand/vidu/tasks/YOUR_TASK_ID' \\
  -H 'Authorization: Bearer YOUR_API_KEY'
```

### 4. 输出参数

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| task\_id | string | 任务 ID |
| state | string | 处理状态：created / queueing / processing / success / failed |
| model | string | 本次调用的模型名称 |
| prompt | string | 本次调用的提示词参数 |
| duration | integer | 本次调用的视频时长参数 |
| seed | integer | 本次调用的随机种子参数 |
| resolution | string | 本次调用的分辨率参数 |
| creations | array[object] | 生成结果列表（成功时返回） |
| creations[].url | string | 生成视频的下载地址，为临时地址，有效期 12 小时，请及时下载转存 |
| creations[].cover\_url | string | 生成视频的封面图地址 |
| credits | integer | 本次调用消耗的积分数 |
| created\_at | string | 任务创建时间（ISO 8601） |
| request\_id | string | 唯一请求标识，用于排查问题 |
| tokenhub\_usage | object | 用量消耗 |
| tokenhub\_usage.total\_tokens | integer | 本次任务消耗的 token 数，用于计费/对账 |

### 5. 响应示例

**生成成功：**

```json
{
  "task_id": "4-WandVideo-a786becfdc80433b8cff4aa344c8fd3d",
  "state": "success",
  "model": "vidu-video-q3-turbo",
  "prompt": "一只小猫在月光下奔跑，镜头跟随",
  "duration": 5,
  "seed": 0,
  "resolution": "720p",
  "creations": [
    {
      "url": "https://aigc-video.cos.myqcloud.com/xxx/result.mp4",
      "cover_url": "https://aigc-video.cos.myqcloud.com/xxx/cover.jpg"
    }
  ],
  "credits": 100,
  "created_at": "2026-07-31T15:41:31.968Z",
  "request_id": "3aec3299-06ad-4654-8b45-c57b823a15d2",
  "tokenhub_usage": { "total_tokens": 102655 }
}
```

### 6. 错误码

| state | 含义 | 处理建议 |
| --- | --- | --- |
| success | 生成成功 | 从 `creations[].url` 获取结果视频。 |
| processing / queueing | 处理中 / 排队中 | 每 5~10 秒轮询一次，直至 success。 |
| failed | 生成失败 | 查看失败原因，修改后重试；持续失败请联系技术支持并附 request\_id。 |

请求级错误码见 [附录：统一错误码](https://cloud.tencent.com/document/product/1823/135756#.E7.BB.9F.E4.B8.80.E9.94.99.E8.AF.AF.E7.A0.81)。

## 附录

### 统一错误码

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| BadRequest | bad request | 不合法的请求 |
| FieldLacking | field is missing or empty | 缺少必填字段 |
| FieldUnwanted | unwanted field | 传入了不需要的字段 |
| FieldInvalid | invalid field | 传入参数未通过合法性校验 |
| FieldItemCountOutOfRange | field item count out of range | 字段项数超限（如图片数量超限） |
| PageSizeOutOfRange | page size out of range | 图像尺寸/参数超限 |
| ImageFormatInvalid / VideoFormatInvalid | invalid image/video format | 图像/视频格式不符合要求 |
| ImageSizeInvalid | image size invalid | 图片尺寸过大或过小 |
| ImageDownloadFailure / VideoDownloadFailure | image/video download failure | 下载图片/视频 URL 失败 |
| ImageCheckFaceFailed | Image Check Face Failed | 输入图人脸检测失败 |
| ImageCheckBodyJointsFailed | Image Check Body Joints Failed | 输入图人体检测失败 |
| NoFaceDetected / MultiFaceDetected | no / multi face detected | 未检测到人脸 / 多张人脸 |
| TaskPromptPolicyViolation | prompt policy violation | Prompt 触发安审风控 |
| CreationPolicyViolation | creation policy violation | 生成物触发风控 |
| AuditSubmitIllegal / AuditFailed | submit is illegal / audit failed | 输入未通过安全审核 / 审核失败 |
| CreditInsufficient | insufficient credits | 积分不足 |
| ModelUnavailable | model unavailable | 模型不可用 |
| Unauthorized | unauthorized | 未鉴权（检查 Authorization） |
| Forbidden | forbidden | 请求没有权限 |
| TaskNotFound / CreationNotFound / NotFound | not found | 任务/生成物/资源不存在 |
| QuotaExceeded | quota exceeded | 超过并发限制 |
| TooManyRequests | too many requests | 请求太频繁 |
| SystemThrottling | system is throttling | 资源超过限制（限流） |
| UserCancelled / Canceled | user cancelled / request canceled | 用户手动终止 / 请求被取消 |
| InternalServiceFailure | internal service failure | 服务器内部错误 |
| Unknown | unknown | 未知原因 |

### 各接口时长取值速查

| 接口 | q3 系列（q3 / q3-pro / q3-turbo） | q2 系列（q2 / q2-pro / q2-turbo） |
| --- | --- | --- |
| 文生视频 | 1 ~ 16，默认 5 | 1 ~ 10，默认 5 |
| 图生视频 | 1 ~ 16，默认 5 | 1 ~ 10，默认 5 |
| 多图参考生视频 | 3 ~ 16，默认 5 | q2-pro：0 ~ 10（0 = 自动判断时长）；q2：1 ~ 10，默认 5 |
| 首尾帧生视频 | 1 ~ 16，默认 5 | 1 ~ 8，默认 5 |

**注意：**

`duration` 取值范围随**接口能力**变化，不是仅由模型决定。例如同为 q3-turbo，文生视频可传 1~16 秒，但参考生视频最小为 3 秒。

### 素材通用约束

**图片**：格式 png / jpeg / jpg / webp；像素 ≥ 128×128；比例须小于 1:4 或 4:1；单图 ≤ 50MB；POST body ≤ 20MB；支持 URL 或 Base64（Base64 须带 `data:image/png;base64,` 前缀）。

**视频（仅 q2-pro 参考生支持）**：格式 mp4 / avi / mov；像素 ≥ 128×128；比例 < 1:4 或 4:1；参考视频 ≤ 100MB；主体视频 5 秒以内、Base64 解码 < 20MB。

### 主体引用语法

在参考生视频的 `subjects` 方式中，通过 `subjects[].name` 定义主体名，在 `prompt` 中以 `@主体名` 引用（如 `@girl 和 @boy 在一起吃火锅`）。主体名避免互为子串。

## 常见问题

#### **1. 六款视频模型如何选择？**

速度成本优先、要智能切镜/音画同出：`vidu-video-q3-turbo`；

多机位一致性更出色：`vidu-video-q3`；

高画质：`vidu-video-q3-pro`；

参考生需要视频参考/视频主体：`vidu-video-q2-pro`（唯一支持视频输入）；

动态效果好、细节丰富：`vidu-video-q2`；

Q2 快速版：`vidu-video-q2-turbo`。

#### **2. subjects 主体方式和 images 直接参考方式有什么区别？**

subjects 方式：可定义多个命名主体，在 prompt 中用 `@主体名` 灵活引用，适合多主体交互场景；prompt 上限 5000 字符；

images/videos 直接方式：直接传参考素材，不支持命名引用；prompt 上限 2000 字符。

#### **3. audio 和 bgm 有什么区别？**

`audio` 是音视频直出（输出带台词/音效的有声视频），仅 q3 系列支持；`bgm` 是添加背景音乐，q3 系列不生效，q2 系列 duration 为 9/10 秒时不生效。

#### **4. 哪些接口可以指定画面宽高比？**

仅**文生视频、多图参考生视频**支持 `aspect_ratio` 参数；**图生视频、首尾帧生视频**无此参数，输出画幅跟随输入图片比例。

#### **5. 生成结果视频链接会过期吗？**

会过期。生成结果为临时地址，有效期 12 小时，请在任务成功后及时下载 `creations[].url` 中的视频并转存到自有存储，不要长期依赖该链接。
