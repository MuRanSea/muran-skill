<!-- Official source: https://cloud.tencent.com/document/product/1823/135325 -->
<!-- Source SHA-256: 3698940348d057c3108e5db7aba88e77d5339ddc8b09ea641fb7eb4055c15ffb -->

# PixVerse 生视频调用指南

官方来源：https://cloud.tencent.com/document/product/1823/135325
最近更新时间：2026-09-24 21:20:30

## 概述

PixVerse（爱诗科技）是面向短视频创作场景的视频生成模型系列，支持文生视频、图生视频、首尾帧生视频、参考生视频四种能力，具备多分辨率、多画幅、运镜控制、音频生成与多镜头分镜等特性。

本文介绍如何通过 TokenHub 调用 PixVerse 的三款模型：pixverse-video-v5.6、pixverse-video-v6.0、pixverse-video-c1。

### 前提条件

已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号并开通 TokenHub 服务。

已在 [TokenHub 控制台](https://console.cloud.tencent.com/tokenhub/apikey) 获取 API Key。

在 [控制台-在线推理-视觉模型](https://console.cloud.tencent.com/tokenhub/inference?regionId=1&serviceType=VISION) 处开启对应模型的后付费。

**说明：**

下文所有示例中的 YOUR\_API\_KEY 均需替换为您自己的 API Key，鉴权方式为请求头 Authorization: Bearer YOUR\_API\_KEY。

### **调用流程**

视频生成为耗时任务（通常 1~5 分钟），接口采用**异步调用**模式，统一分两步：

1. **提交任务**：调用能力接口（文生/图生/首尾帧/参考生），成功返回 `Resp.video_id`（任务 ID）。

2. **轮询结果**：携带 `video_id` 调用 [查询任务结果](https://cloud.tencent.com/document/product/1823/135325#b6289ab1-c148-43a0-a544-9bf97e2d4879) 接口，建议**每 3~5 秒轮询一次**，直至 `Resp.status = 1`（生成成功），从 `Resp.url` 获取结果视频。

**说明：**

任务创建成功后请勿重复提交，通过轮询获取结果即可。

通用响应制式：`ErrCode`（0 表示成功）、`ErrMsg`（提示信息）、`Resp`（数据对象）。

### 模型列表

| 模型名称 | model 参数值 | 支持能力 | 视频时长（秒） | 清晰度档位 | 画面宽高比（文生/参考生） | 选型建议 |
| --- | --- | --- | --- | --- | --- | --- |
| PixVerse V6.0 | `pixverse-video-v6.0` | 文生 / 图生 / 首尾帧 / 参考生 | 1 ~ 15 | 360p / 540p / 720p / 1080p | 16:9、4:3、1:1、3:4、9:16、2:3、3:2、21:9 | **通用场景推荐**，支持多镜头（智能分镜）。 |
| PixVerse C1 | `pixverse-video-c1` | 文生 / 图生 / 首尾帧 / 参考生 | 1 ~ 15 | 360p / 540p / 720p / 1080p | 16:9、4:3、1:1、3:4、9:16、2:3、3:2、21:9 | 打斗、法术特效、高速运动等**动态场景**推荐；支持由提示词自动生成结构化分镜。 |
| PixVerse V5.6 | `pixverse-video-v5.6` | 文生 / 图生 / 首尾帧 / 参考生 | 5 / 8 / 10（1080p 不支持 10） | 360p / 540p / 720p / 1080p | 16:9、4:3、1:1、3:4、9:16 | 历史版本，新接入建议直接使用 V6.0。 |

**说明：**

「画面宽高比」列为**文生视频、参考生视频**支持的取值范围；**图生视频、首尾帧生视频**的输出画幅默认跟随输入图片比例。

## 文生视频

### 1. 接口描述

仅凭文本提示词生成视频，支持运镜、音频与多镜头开关。

**接口：**`POST https://tokenhub.tencentmaas.com/v1/wand/pixverse/text-to-video`

### 2. 输入参数

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| prompt | 是 | string | 文本提示词，描述期望生成的视频内容。取值范围：≤ 5000 字符。 |
| model | 是 | string | 模型版本。取值范围：`pixverse-video-v5.6`、`pixverse-video-v6.0`、`pixverse-video-c1` |
| duration | 是 | integer | 视频时长（秒）。v5.6：5/8/10（1080p 不支持 10）；v6.0/c1：1~15。默认值：5。 |
| quality | 是 | string | 视频清晰度。取值范围：360p / 540p / 720p / 1080p。 |
| aspect\_ratio | 否 | string | 画面宽高比。v5.6：16:9 / 4:3 / 1:1 / 3:4 / 9:16；v6.0/c1 额外支持 2:3 / 3:2 / 21:9。默认值：16:9。 |
| camera\_movement | 否 | string | 运镜方式，如 zoom\_in 等（按需使用）。 |
| seed | 否 | integer | 随机种子。取值范围：0 ~ 2147483647；不传或传 0 时使用随机数。 |
| generate\_audio\_switch | 否 | boolean | 音频开关。true=有声（自动生成匹配的背景音乐或音效），false=静音。默认值：false。 |
| generate\_multi\_clip\_switch | 否 | boolean | 多镜头开关，**仅** `pixverse-video-v6.0` **支持**。true=多镜头（系统智能分镜），false=单镜头。默认值：false。 |

### 3. 请求示例

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/pixverse/text-to-video' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "pixverse-video-v5.6",
  "prompt": "一只橙色小猫在窗台上看向镜头",
  "duration": 5,
  "quality": "360p",
  "aspect_ratio": "16:9"
}'
```

**说明：**

将示例中的 `model` 替换为 `pixverse-video-v5.6` 或 `pixverse-video-c1`，即可调用对应模型。

### 4. 输出参数

<table><colgroup><col/><col/><col/></colgroup><tbody><tr><td><div>字段</div></td><td><div>类型</div></td><td><div>说明</div></td></tr><tr><td><div>ErrCode</div></td><td><div>integer</div></td><td><div>错误码；0 表示成功。</div></td></tr><tr><td><div>ErrMsg</div></td><td><div>string</div></td><td><div>错误或提示信息。</div></td></tr><tr><td><div>Resp</div></td><td><div>object</div></td><td><div>返回数据对象。</div></td></tr><tr><td><div>Resp.video_id</div></td><td><div>string</div></td><td><div>任务 ID，用于轮询查询任务状态。</div></td></tr><tr><td colspan="1" rowspan="1"><div>request_id</div></td><td colspan="1" rowspan="1"><div>string</div></td><td colspan="1" rowspan="1"><div>唯一请求标识，用于排查问题。</div></td></tr></tbody></table>

### 5. 响应示例

```json
{
  "ErrCode": 0,
  "ErrMsg": "Success",
  "Resp": {
    "video_id": "4-WandVideo-4ba31a7d508249b787fa0b0c62a6a399"
  }
,
  "request_id": "4d384c85-2177-4bae-adf9-364ed917509b" 
}
```

### 6. 错误码

请求失败时 `ErrCode` 不为 0，具体原因见 `ErrMsg`。任务提交成功后，生成阶段的任务状态通过 [查询任务结果](https://cloud.tencent.com/document/product/1823/135325#b6289ab1-c148-43a0-a544-9bf97e2d4879) 接口获取：

| status | 含义 | 处理建议 |
| --- | --- | --- |
| 1 | 生成成功 | 从 `Resp.url` 获取结果视频。 |
| 5 | 生成中 | 每 3~5 秒轮询一次，直至 status=1。 |
| 6 | 已删除 | 任务结果已删除，需重新发起。 |
| 7 | 内容审核失败 | 检查提示词/图片是否含违规内容，修改后重试。 |
| 8 | 生成失败 | 服务端生成出错，请重试；持续失败请联系技术支持并附任务 ID。 |

## 图生视频

### 1. 接口描述

以一张图片为首帧生成动态视频，图片直接传入公网可访问的 URL，输出视频画幅跟随输入图片比例。支持负向提示词、运镜、音频与多镜头开关。

**接口：**`POST https://tokenhub.tencentmaas.com/v1/wand/pixverse/image-to-video`

### 2. 输入参数

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| img\_id | 是 | string | 图片地址，传入公网可访问的图片 URL，或者 base64图片数据。单张图片小于20MB。 |
| img\_ids | 否 | array[string] | 多图模板专用图片 URL 数组，如 ["url1", "url2"]。 |
| prompt | 是 | string | 文本提示词。取值范围：≤ 5000 字符。 |
| model | 是 | string | 模型版本。取值范围：`pixverse-video-v5.6`、`pixverse-video-v6.0`、`pixverse-video-c1` |
| duration | 是 | integer | 视频时长（秒）。v5.6：5/8/10（1080p 不支持 10）；v6.0/c1：1~15。默认值：5。 |
| quality | 是 | string | 视频清晰度。取值范围：360p / 540p / 720p / 1080p。 |
| camera\_movement | 否 | string | 运镜方式，如 zoom\_in 等（按需使用）。 |
| seed | 否 | integer | 随机种子。取值范围：0 ~ 2147483647；不传或传 0 时使用随机数。 |
| generate\_audio\_switch | 否 | boolean | 音频开关。true=有声，false=静音。默认值：false。 |
| generate\_multi\_clip\_switch | 否 | boolean | 多镜头开关，**仅** `pixverse-video-v6.0` **支持**。true=多镜头，false=单镜头。默认值：false。 |

### 3. 请求示例

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/pixverse/image-to-video' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "pixverse-video-v6.0",
  "prompt": "让图片中的主体自然转头",
  "img_id": "https://example.com/input.jpg",
  "duration": 5,
  "quality": "360p"
}'
```

**说明：**

将示例中的 `model` 替换为 `pixverse-video-v5.6` 或 `pixverse-video-c1`，即可调用对应模型。

### 4. 输出参数

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| ErrCode | integer | 错误码；0 表示成功。 |
| ErrMsg | string | 错误或提示信息。 |
| Resp | object | 返回数据对象。 |
| Resp.video\_id | string | 生成任务的视频 ID，用于轮询查询任务状态。 |
| request\_id | string | 唯一请求标识，用于排查问题。 |

### 5. 响应示例

```json
{
	"ErrCode": 0,
	"ErrMsg": "success",
	"Resp": {
		"video_id": "4-WandVideo-a786becfdc80433b8cff4aa344c8fd3d"
	},
	"request_id": "4d384c85-2177-4bae-adf9-364ed917509b"
}
```

### 6. 错误码

请求失败时 `ErrCode` 不为 0，具体原因见 `ErrMsg`。任务提交成功后，生成阶段的任务状态通过 [查询任务结果](https://cloud.tencent.com/document/product/1823/135325#b6289ab1-c148-43a0-a544-9bf97e2d4879) 接口获取：

| status | 含义 | 处理建议 |
| --- | --- | --- |
| 1 | 生成成功 | 从 `Resp.url` 获取结果视频。 |
| 5 | 生成中 | 每 3~5 秒轮询一次，直至 status=1。 |
| 6 | 已删除 | 任务结果已删除，需重新发起。 |
| 7 | 内容审核失败 | 检查提示词/图片是否含违规内容，修改后重试。 |
| 8 | 生成失败 | 服务端生成出错，请重试；持续失败请联系技术支持并附任务 ID。 |

## 首尾帧生视频

### 1. 接口描述

给定首帧与尾帧两张图片（公网可访问的 URL），生成在两者之间平滑过渡的视频。输出视频画幅跟随输入图片比例。

**接口：** `POST https://tokenhub.tencentmaas.com/v1/wand/pixverse/start-end-to-video`

**说明：**

建议首帧与尾帧图片保持相同的宽高比例，以获得最佳过渡效果。

### 2. 输入参数

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| prompt | 是 | string | 文本提示词，描述过渡内容。取值范围：≤ 5000 字符。示例：“从首帧自然过渡到尾帧” |
| first\_frame\_img | 是 | string | 首帧图片地址，传入公网可访问的图片 URL，或者 base64图片数据。单张图片小于20MB。 |
| last\_frame\_img | 是 | string | 尾帧图片地址，传入公网可访问的图片 URL，或者 base64图片数据。单张图片小于20MB。 |
| model | 是 | string | 模型版本。取值范围：`pixverse-video-v5.6`、`pixverse-video-v6.0`、`pixverse-video-c1` |
| duration | 是 | integer | 视频时长（秒）。v5.6：5/8/10（1080p 不支持 10）；v6.0/c1：1~15。默认值：5。 |
| quality | 是 | string | 视频清晰度。取值范围：360p / 540p / 720p / 1080p。 |
| seed | 否 | integer | 随机种子。取值范围：0 ~ 2147483647；不传或传 0 时使用随机数。 |
| generate\_audio\_switch | 否 | boolean | 音频开关。true=有声，false=静音。默认值：false。 |

### 3. 请求示例

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/pixverse/start-end-to-video' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "pixverse-video-v6.0",
  "prompt": "从首帧自然过渡到尾帧",
  "first_frame_img": "https://example.com/start.jpg",
  "last_frame_img": "https://example.com/end.jpg",
  "duration": 5,
  "quality": "360p"
}'
```

**说明：**

将示例中的 `model` 替换为 `pixverse-video-v5.6` 或 `pixverse-video-c1`，即可调用对应模型。

### 4. 输出参数

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| ErrCode | integer | 错误码；0 表示成功。 |
| ErrMsg | string | 错误或提示信息。 |
| Resp | object | 返回数据对象。 |
| Resp.video\_id | string | 任务 ID，用于轮询查询任务状态。 |
| request\_id | string | 唯一请求标识，用于排查问题。 |

### 5. 响应示例

```json
{
	"ErrCode": 0,
	"ErrMsg": "success",
	"Resp": {
		"video_id": "1374200019-WandVideo-a786becfdc80433b8cff4aa344c8fd3d"
	},
	"request_id": "4d384c85-2177-4bae-adf9-364ed917509b"
}
```

### 6. 错误码

请求失败时 `ErrCode` 不为 0，具体原因见 `ErrMsg`。任务提交成功后，生成阶段的任务状态通过 [查询任务结果](https://cloud.tencent.com/document/product/1823/135325#b6289ab1-c148-43a0-a544-9bf97e2d4879) 接口获取：

| status | 含义 | 处理建议 |
| --- | --- | --- |
| 1 | 生成成功 | 从 `Resp.url` 获取结果视频。 |
| 5 | 生成中 | 每 3~5 秒轮询一次，直至 status=1。 |
| 6 | 已删除 | 任务结果已删除，需重新发起。 |
| 7 | 内容审核失败 | 检查提示词/图片是否含违规内容，修改后重试。 |
| 8 | 生成失败 | 服务端生成出错，请重试；持续失败请联系技术支持并附任务 ID。 |

## 参考生视频

### 1. 接口描述

通过一组参考图（主体/背景）结合提示词生成主体一致的视频，参考图直接传入公网可访问的 URL，prompt 中可用 `@ref_name` 指代具体参考图。

**接口：**`POST https://tokenhub.tencentmaas.com/v1/wand/pixverse/reference-to-video`

### 2. 输入参数

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| image\_references | 是 | array[object] | 参考图数组，v5.6/v6.0/c1 最多支持 7 项。子字段见下表。 |
| prompt | 是 | string | 文本提示词。取值范围：≤ 5000 字符。可用 `@ref_name` 指代参考图（@ 后接空格），如 "@dog plays at @room"。 |
| model | 是 | string | 模型版本。取值范围：`pixverse-video-v5.6`、`pixverse-video-v6.0`、`pixverse-video-c1` |
| duration | 是 | integer | 视频时长（秒）。v5.6：5/8/10（1080p 不支持 10）；v6.0/c1：1~15。默认值：5。 |
| quality | 是 | string | 视频清晰度。取值范围：360p / 540p / 720p / 1080p。 |
| aspect\_ratio | 否 | string | 画面宽高比。v5.6：16:9 / 4:3 / 1:1 / 3:4 / 9:16；v6.0/c1 额外支持 2:3 / 3:2 / 21:9。默认值：16:9。 |
| generate\_audio\_switch | 否 | boolean | 音频开关。true=有声，false=静音。默认值：false。 |
| seed | 否 | integer | 随机种子。取值范围：0 ~ 2147483647。 |

**image\_references 数组元素子字段：**

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| img\_id | 是 | string | 参考图地址，传入公网可访问的图片 URL，或者 base64图片数据。 |
| type | 否 | string | 参考图类型。取值：subject（主体）/ background（背景）。 |
| ref\_name | 否 | string | 参考图名称，≤ 30 字符；用于在 prompt 中以 `@ref_name` 引用。 |

### 3. 请求示例

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/pixverse/reference-to-video' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "pixverse-video-v6.0",
  "prompt": "参考图主体自然挥手",
  "image_references": [
    {
      "img_id": "https://example.com/input.png",
      "type": "subject"
    }
  ],
  "duration": 5,
  "quality": "360p",
  "aspect_ratio": "16:9"
}'
```

**说明：**

将示例中的 `model` 替换为 `pixverse-video-v5.6` 或 `pixverse-video-c1`，即可调用对应模型。

### 4. 输出参数

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| ErrCode | integer | 错误码；0 表示成功。 |
| ErrMsg | string | 错误或提示信息。 |
| Resp | object | 返回数据对象。 |
| Resp.video\_id | string | 任务 ID，用于轮询查询任务状态。 |
| request\_id | string | 唯一请求标识，用于排查问题。 |

### 5. 响应示例

```json
{
	"ErrCode": 0,
	"ErrMsg": "success",
	"Resp": {
		"video_id": "1374200019-WandVideo-a786becfdc80433b8cff4aa344c8fd3d"
	},
	"request_id": "4d384c85-2177-4bae-adf9-364ed917509b"
}
```

### 6. 错误码

请求失败时 `ErrCode` 不为 0，具体原因见 `ErrMsg`。任务提交成功后，生成阶段的任务状态通过 [查询任务结果](https://cloud.tencent.com/document/product/1823/135325#b6289ab1-c148-43a0-a544-9bf97e2d4879) 接口获取：

| status | 含义 | 处理建议 |
| --- | --- | --- |
| 1 | 生成成功 | 从 `Resp.url` 获取结果视频。 |
| 5 | 生成中 | 每 3~5 秒轮询一次，直至 status=1。 |
| 6 | 已删除 | 任务结果已删除，需重新发起。 |
| 7 | 内容审核失败 | 检查提示词/图片是否含违规内容，修改后重试。 |
| 8 | 生成失败 | 服务端生成出错，请重试；持续失败请联系技术支持并附任务 ID。 |

## 查询任务结果

### 1. 接口描述

四个能力接口共用的任务查询接口，用于轮询获取生成结果。

**接口：**`GET https://tokenhub.tencentmaas.com/v1/wand/pixverse/tasks/{task_id}`

**说明：**

路径中的 `{task_id}` 即提交任务时返回的 `Resp.video_id`（示例中以 `YOUR_TASK_ID` 占位）。视频生成约需数分钟，建议每 3~5 秒轮询一次。

### 2. 输入参数

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| task\_id | 是 | string | 任务 ID（路径参数），即提交任务时返回的 `Resp.video_id`。 |

### 3. 请求示例

```bash
curl -X GET 'https://tokenhub.tencentmaas.com/v1/wand/pixverse/tasks/YOUR_TASK_ID' \\
  -H 'Authorization: Bearer YOUR_API_KEY'
```

### 4. 输出参数

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| ErrCode | integer | 错误码；0 表示成功 |
| ErrMsg | string | 错误或提示信息 |
| Resp | object | 返回数据对象（任务详情） |
| Resp.id | string | 视频 ID（即 video\_id） |
| Resp.status | integer | 视频状态：1 成功 / 5 生成中 / 6 已删除 / 7 审核失败 / 8 生成失败 |
| Resp.url | string | 生成成功后的视频结果 URL |
| Resp.prompt | string | 本次生成的提示词 |
| Resp.negative\_prompt | string | 负向提示词 |
| Resp.seed | integer | 随机种子 |
| Resp.style | string | 风格 |
| Resp.resolution\_ratio | integer | 视频清晰度 |
| Resp.outputWidth | integer | 视频宽度 |
| Resp.outputHeight | integer | 视频高度 |
| Resp.size | integer | 视频文件大小 |
| Resp.create\_time | string | 任务创建时间 |
| Resp.modify\_time | string | 任务更新时间 |
| tokenhub\_usage | object | 用量消耗 |
| tokenhub\_usage.total\_tokens | integer | 消耗的 token 数 |
| request\_id | string | 唯一请求标识，用于排查问题 |

### 5. 响应示例

**生成成功：**

```json
{
	"ErrCode": 0,
	"ErrMsg": "Success",
	"Resp": {
		"id": "4-WandVideo-a786becfdc80433b8cff4aa344c8fd3d",
		"status": 1,
		"url": "https://aigc-video.cos.myqcloud.com/12245233/4-WandVideo-33b8cff4aa344c8fd3d_0.mp4?q-sign=keLrAG",
		"prompt": "一只橙色小猫在窗台上看向镜头",
		"negative_prompt": "",
		"seed": 0,
		"style": "",
		"resolution_ratio": 720,
		"outputWidth": 1280,
		"outputHeight": 720,
		"size": 0,
		"create_time": "2026-07-29 15:41:31",
		"modify_time": "2026-07-29 15:42:10"
	},
	"tokenhub_usage": {
		"total_tokens": 102655
	},
	"request_id": "2524bc44-5c6f-4114-9b94-6c57eb85f54a-query-1785393236"
}
```

### 6. 状态码

| status | 含义 | 处理建议 |
| --- | --- | --- |
| 1 | 生成成功 | 从 `Resp.url` 获取结果视频。 |
| 5 | 生成中 | 每 3~5 秒轮询一次，直至 status=1。 |
| 6 | 已删除 | 任务结果已删除，需重新发起。 |
| 7 | 内容审核失败 | 检查提示词/图片是否含违规内容，修改后重试。 |
| 8 | 生成失败 | 服务端生成出错，请重试；持续失败请联系技术支持并附任务 ID。 |

## 附录：通用参数限制速查

| 参数 | 限制说明 |
| --- | --- |
| duration | v5.6：5/8/10（1080p 不支持 10 秒）；v6.0/c1：1~15 整数（1080p 同样支持至 15 秒）。 |
| aspect\_ratio | 仅文生视频、参考生视频支持。v5.6：16:9 / 4:3 / 1:1 / 3:4 / 9:16；v6.0/c1 额外支持 2:3 / 3:2 / 21:9；默认值 16:9。图生视频、首尾帧生视频不支持该参数，输出画幅跟随输入图片比例。 |
| generate\_multi\_clip\_switch | 仅 `pixverse-video-v6.0` 的**文生视频、图生视频**支持；首尾帧、参考生不支持。 |

## 常见问题

#### **1. 三款模型如何选择？**

通用场景、或需要多镜头智能分镜：`pixverse-video-v6.0`。

打斗、法术特效、高速运动等动态场景：`pixverse-video-c1`。

`pixverse-video-v5.6` 为历史版本，新接入建议直接使用 V6.0。

#### **2. 为什么 v5.6 在 1080p 下无法生成 10 秒视频？**

`pixverse-video-v5.6` 在 1080p 清晰度下仅支持 5 / 8 秒。如需 10 秒，请降低清晰度至 720p 及以下，或切换至 v6.0 / c1（均支持 1~15 秒）。

#### **3. 图生/首尾帧/参考生接口中的图片如何传入？**

直接传入公网可访问的图片 URL 即可：`img_id`（图生）、`first_frame_img` / `last_frame_img`（首尾帧）、`image_references[].url`（参考生）均接收图片 URL 字符串，无需先调用上传接口。

#### **4. 生成结果视频链接会过期吗？**

建议任务成功后及时下载 `Resp.url` 中的视频文件，有效期不超过12小时，建议尽快下载使用。
