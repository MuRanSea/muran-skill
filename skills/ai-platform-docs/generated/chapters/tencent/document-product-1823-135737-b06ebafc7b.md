<!-- Official source: https://cloud.tencent.com/document/product/1823/135737 -->
<!-- Source SHA-256: cb97367e1fc3f8912deffb9ac636b1645b6246bfd84e259974c791275be148c3 -->

# MiniMax 生视频调用指南

官方来源：https://cloud.tencent.com/document/product/1823/135737
最近更新时间：2026-10-13 15:50:31

## 概述

MiniMax 视频（海螺视频）是 MiniMax 推出的视频生成模型系列，支持**文生视频、图生视频（首帧 / 首尾帧）、多模态参考生视频**等能力，具备运镜指令控制、2K 直出、原生立体声等特性。

本文介绍如何通过 TokenHub 调用 MiniMax 的四款视频模型：`minimax-video-v2.3`、`minimax-video-v2.3-fast`、`minimax-video-h3`、`minimax-video-h3-max`。

**说明：**

MiniMax 视频在 TokenHub 上有**两套提交端点**，分别对应两种传参风格，提交与查询的响应结构也不同，请按模型选择对应端点：

V1（扁平参数）：`POST /v1/wand/minimax-video/generation` 及其查询 `GET /v1/wand/minimax-video/tasks/{task_id}`，适用于 `minimax-video-v2.3`、`minimax-video-v2.3-fast`。

V2（content 数组）：`POST /v1/wand/minimax-video-v2/generation` 及其查询 `GET /v1/wand/minimax-video-v2/tasks/{task_id}`，适用于 `minimax-video-h3`、`minimax-video-h3-max`。

其中 v2.3 / v2.3-fast 使用扁平参数（`prompt`、`first_frame_image` 等）；h3 / h3-max 使用 `content` 多模态数组传参，详见各接口章节。提交与查询必须使用同一端点组。

### 前提条件

已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号并开通 TokenHub 服务。

已在 [TokenHub 控制台](https://console.cloud.tencent.com/tokenhub/apikey) 获取 API Key。

在[控制台-在线推理-视觉模型](https://console.cloud.tencent.com/tokenhub/inference?regionId=1&serviceType=VISION) 处开启对应模型的后付费。

**说明：**

下文所有示例中的 YOUR\_API\_KEY 均需替换为您自己的 API Key，鉴权方式为请求头 Authorization: Bearer YOUR\_API\_KEY。

### 调用流程

视频生成为耗时任务（通常 1~3 分钟），接口采用**异步调用**模式，统一分两步：

1. **提交任务**：调用 `POST /v1/wand/minimax-video/generation`，成功返回 `task_id`。

2. **轮询结果**：携带 `task_id` 调用 [查询任务结果](https://cloud.tencent.com/document/product/1823/135737#.E6.9F.A5.E8.AF.A2.E4.BB.BB.E5.8A.A1.E7.BB.93.E6.9E.9C) 接口，直至任务状态为成功，从结果中获取视频地址。

**注意：**

所有接口响应均包含 `request_id`（顶层，用于排查问题）；查询接口额外返回 tokenhub\_usage（用量消耗，含 tokenhub\_usage.total\_tokens）。任务状态枚举以实际返回为准：v2.3 / v2.3-fast 参照官方为 Preparing / Queueing / Processing / Success / Fail；h3 参照官方为 queued / running / succeeded / failed / cancelled。

### 模型列表

| 模型名称 | model 参数值 | 支持能力 | 视频时长（秒） | 清晰度档位 | 传参方式 | 选型建议 |
| --- | --- | --- | --- | --- | --- | --- |
| MiniMax-Video-v2.3 | `minimax-video-v2.3` | 文生 / 图生 | 6 / 10（768P）；6（1080P） | 768P / 1080P | 扁平参数 | **旗舰款**：物理表现与指令遵循强，支持运镜指令。 |
| MiniMax-Video-v2.3-fast | `minimax-video-v2.3-fast` | 图生 | 6 / 10（768P）；6（1080P） | 768P / 1080P | 扁平参数 | v2.3 快速版，生成更快、批量创作成本更低；**仅支持图生。** |
| MiniMax-Video-H3 | `minimax-video-h3` | 文生 / 图生（首尾帧）/ 多模态参考生 | 4 ~ 15 | 768P / 2K（传入 1080P 降级为 768P，4K 降级为 2K） | content 数组 | 最新旗舰：2K 直出、多模态参考（图/视频/音频）、原生立体声。 |
| MiniMax-Video-H3-Max | `minimax-video-h3-max` | 文生 / 图生（首帧 / 尾帧）/ 多模态参考生 | 5 ~ 15（不支持 4 秒） | 480P / 768P（不支持 2K；传入 1080P / 2K / 4K 会静默降级为 768P） | content 数组 | H3 极速版：出片更快、成本更低；不支持 2K，支持 `extra.prompt_expansion_mode` 提示词扩写。 |

**说明：**

`minimax-video-v2.3-fast` **仅支持图生视频（首帧）**，不支持文生视频与尾帧。

v2.3 系列时长与分辨率联动：768P 可选 6 或 10 秒，1080P 仅支持 6 秒。

h3 / h3-max 的 ratio（画幅）：文生必填且不能为 adaptive（传 adaptive 会按 16:9 处理）；图生由输入图片决定（恒 adaptive，显式传值会被忽略）；多模态参考生可选，默认 adaptive。

`extra.prompt_expansion_mode` 仅 `minimax-video-h3-max` 生效，`minimax-video-h3` 传入会被忽略。

h3 / h3-max 的请求体总大小 ≤ 64MB，大文件请使用公网 URL，勿用 Base64。

## 文生视频

### 1. 接口描述

仅凭文本提示词生成视频。支持模型：`minimax-video-v2.3`（扁平参数）、`minimax-video-h3`、`minimax-video-h3-max`（content 数组）。v2.3 支持 `[指令]` 运镜语法，请参见 [附录：运镜指令语法](https://cloud.tencent.com/document/product/1823/135737#.E8.BF.90.E9.95.9C.E6.8C.87.E4.BB.A4.E8.AF.AD.E6.B3.95)。

**接口：** `POST https://tokenhub.tencentmaas.com/v1/wand/minimax-video/generation`

**接口：** `POST https://tokenhub.tencentmaas.com/v1/wand/minimax-video-v2/generation`

### 2. 输入参数

#### **v2.3（扁平参数）：**

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| model | 是 | string | 模型名称。取值：`minimax-video-v2.3` |
| prompt | 是 | string | 文本提示词，≤ 2000 字符。支持 `[指令]` 运镜语法（如 [推进]、[左摇]）。 |
| prompt\_optimizer | 否 | boolean | 是否自动优化 prompt。默认值：true；设为 false 可进行更精确的控制。 |
| fast\_pretreatment | 否 | boolean | 是否缩短 prompt\_optimizer 的优化耗时。默认值：false。 |
| duration | 否 | integer | 视频时长（秒）。768P：6 或 10；1080P：仅 6。默认值：6。 |
| resolution | 否 | string | 视频分辨率。可选：768P（默认）/ 1080P。 |
| aigc\_watermark | 否 | boolean | 是否在生成视频中添加 AIGC 标识水印。默认值：false。 |

#### **h3 / h3-max（content 数组）：**

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| model | 是 | string | 模型名称。取值：`minimax-video-h3`、`minimax-video-h3-max` |
| content | 是 | array[object] | 多模态输入数组，文生视频仅含一个 `text` 元素。子字段：`type`（text）、`text`（提示词）。`text` 必须非空，最多 7000 个字符。 |
| resolution | 是 | string | 视频分辨率。  h3：768P / 2K（传入 1080P 降级为 768P，4K 降级为 2K）。  h3-max：**仅 480P / 768P，不支持 2K**（传入 1080P / 2K / 4K 会静默降级为 768P）。 |
| duration | 是 | integer | 视频时长（秒）。  h3：4 ~ 15 的整数。  h3-max：5 ~ 15 的整数（不支持 4 秒）。传入区间外的值不会报错，会静默回落为 5 秒。 |
| ratio | 是 | string | 画面宽高比。**文生视频必填且不能为 adaptive**（传 adaptive 会按 16:9 处理）。可选：21:9 / 16:9 / 4:3 / 1:1 / 3:4 / 9:16。 |
| aigc\_watermark | 否 | boolean | 是否添加 AIGC 标识水印。默认值：false。 |
| extra.prompt\_expansion\_mode | 否 | string | **仅** `minimax-video-h3-max` **生效**，`minimax-video-h3` 传入会被忽略。提示词扩写模式。disabled 表示关闭提示词扩写；balanced 表示均衡扩写且为默认值；quality 表示质量优先扩写。  可用选项：disabled, balanced, quality  不传 extra 或不传此属性时，使用 balanced。不要传 balance、空字符串、布尔值或其他未声明字段。 |

### 3. 请求示例

#### **模型：minimax-video-v2.3**

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/minimax-video/generation' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "minimax-video-v2.3",
  "prompt": "一只橙色小猫在窗台上看向镜头"
}'
```

#### **模型：minimax-video-h3**

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/minimax-video-v2/generation' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "minimax-video-h3",
  "content": [
    {
      "type": "text",
      "text": "一只橙色小猫在窗台上看向镜头"
    }
  ],
  "resolution": "2K",
  "duration": 6,
  "ratio": "16:9"
}'
```

### 4. 输出参数

**V1（minimax-video-v2.3 / v2.3-fast）：**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| task\_id | string | 生成任务的任务 ID，用于轮询查询任务状态。 |
| base\_resp | object | 请求状态对象。 |
| base\_resp.status\_code | integer | 请求状态码，0 表示提交成功。 |
| base\_resp.status\_msg | string | 请求状态描述，成功为 success。 |
| request\_id | string | 唯一请求标识，用于排查问题。 |

**V2（minimax-video-h3 / h3-max）：**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| task\_id | string | 生成任务的任务 ID，用于轮询查询任务状态。 |
| request\_id | string | 唯一请求标识，用于排查问题。 |

**说明：**

V2 提交响应**不含** `base_resp`（与 V1 不同），提交是否成功以 HTTP 状态码与是否返回 `task_id` 为准。

### 5. 响应示例

**V1（minimax-video-v2.3）：**

```json
{
  "task_id": "4-WandVideo-a786becfdc80433b8cff4aa344c8fd3d",
  "base_resp": {
    "status_code": 0,
    "status_msg": "success"
  },
  "request_id": "3aec3299-06ad-4654-8b45-c57b823a15d2"
}
```

**V2（minimax-video-h3 / h3-max）：**

```json
{
  "task_id": "4-WandVideo-a786becfdc80433b8cff4aa344c8fd3d",
  "request_id": "3aec3299-06ad-4654-8b45-c57b823a15d2"
}
```

### 6. 错误码

请求失败时返回错误码，具体错误码及处理建议请参见 [附录：统一错误码](https://cloud.tencent.com/document/product/1823/135737#.E7.BB.9F.E4.B8.80.E9.94.99.E8.AF.AF.E7.A0.81)。任务提交成功后，生成阶段的任务状态通过 [查询任务结果](https://cloud.tencent.com/document/product/1823/135737#.E6.9F.A5.E8.AF.A2.E4.BB.BB.E5.8A.A1.E7.BB.93.E6.9E.9C) 接口获取。

## 图生视频（首帧 / 首尾帧）

### 1. 接口描述

以图片为首帧（v2.3 可选尾帧）结合文本提示词生成视频。支持模型：`minimax-video-v2.3`、`minimax-video-v2.3-fast`（扁平参数）、`minimax-video-h3`、`minimax-video-h3-max`（content 数组）。输出画幅跟随输入图片。

**接口：** `POST https://tokenhub.tencentmaas.com/v1/wand/minimax-video/generation`

**接口：** `POST https://tokenhub.tencentmaas.com/v1/wand/minimax-video-v2/generation`

### 2. 输入参数

**v2.3 / v2.3-fast（扁平参数）：**

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| model | 是 | string | 模型名称。取值：`minimax-video-v2.3`、`minimax-video-v2.3-fast` |
| first\_frame\_image | 是 | string | 图片 first\_frame\_image：首帧图片，支持 URL 和 Base64格式，图片格式：jpg/jpeg/png/webp，短边>300px，宽高比 2：5~5：2；单张图片大小≤20MB；  1. Base64：所有图片大小和<=48MB，转为 Base64大小和<=64MB；格式要求：`data:image/<图片格式>;base64,`。注：图片为 jpg 时图片格式填 jpeg。  2. URL：需要公网可访问（http/https） |
| prompt | 否 | string | 文本提示词，≤ 2000 字符。支持 `[指令]` 运镜语法。 |
| prompt\_optimizer | 否 | boolean | 是否自动优化 prompt。默认值：true。 |
| fast\_pretreatment | 否 | boolean | 是否缩短优化耗时。默认值：false。 |
| duration | 否 | integer | 视频时长（秒）。768P：6 或 10；1080P：仅 6。默认值：6。 |
| resolution | 否 | string | 视频分辨率。可选：768P（默认）/ 1080P。 |
| aigc\_watermark | 否 | boolean | 是否添加 AIGC 标识水印。默认值：false。 |

**h3 / h3-max（content 数组）：**

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| model | 是 | string | 模型名称。取值：`minimax-video-h3`、`minimax-video-h3-max` |
| content | 是 | array[object] | 多模态输入数组：1 个 `text` + 1~2 张 `image_url`（`role` 为 `first_frame` / `last_frame`。  图片 content[].image\_url：支持首帧/尾帧图片（role=first\_frame/last\_frame），支持 URL 或 Base64格式，图片格式：jpg/jpeg/png/webp/heic/heif，宽高[256，5760]px，宽高比[0.4，2.5]，首帧 ≤ 1 张、尾帧 ≤ 1 张；单张图片大小 <=30MB；  1. Base64：图片转为 Base64 后计入请求体，请求体总大小 <=64MB（Base64 会放大约 33%，大图请用公网 URL）；格式要求：`data:image/<图片格式>;base64,` 。注：图片为 jpg 时图片格式填 jpeg。  2. URL：需要公网可访问（http/https）。 |
| resolution | 是 | string | 视频分辨率。h3：768P / 2K（传入 1080P 降级为 768P，4K 降级为 2K）；h3-max：**仅 480P / 768P，不支持 2K**（传入 1080P / 2K / 4K 会静默降级为 768P）。 |
| duration | 是 | integer | 视频时长（秒）。h3：4 ~ 15 的整数；h3-max：5 ~ 15 的整数（不支持 4 秒）。传入区间外的值不会报错，会静默回落为 5 秒。 |
| ratio | 否 | string | 画面宽高比。**图生视频恒为 adaptive（宽高比由输入图片决定）**；显式传入 21:9 / 16:9 / 4:3 / 1:1 / 3:4 / 9:16 不会报错，但会被忽略并按 adaptive 处理。 |
| aigc\_watermark | 否 | boolean | 是否添加 AIGC 标识水印。默认值：false。 |
| extra.prompt\_expansion\_mode | 否 | string | **仅** `minimax-video-h3-max` **生效**，`minimax-video-h3` 传入会被忽略。提示词扩写模式。disabled 表示关闭提示词扩写；balanced 表示均衡扩写且为默认值；quality 表示质量优先扩写。  可用选项: disabled, balanced, quality  不传 extra 或不传此属性时，使用 balanced。不要传 balance、空字符串、布尔值或其他未声明字段。 |

### 3. 请求示例

**模型：minimax-video-v2.3-fast（首帧）**

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/minimax-video/generation' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "minimax-video-v2.3-fast",
  "first_frame_image": "https://example.com/input.jpg"
}'
```

**模型：minimax-video-h3（首尾帧）**

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/minimax-video-v2/generation' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "minimax-video-h3",
  "content": [
    {
      "type": "text",
      "text": "从首帧自然过渡到尾帧"
    },
    {
      "type": "image_url",
      "image_url": { "url": "https://example.com/start.jpg" },
      "role": "first_frame"
    },
    {
      "type": "image_url",
      "image_url": { "url": "https://example.com/end.jpg" },
      "role": "last_frame"
    }
  ],
  "resolution": "768P",
  "duration": 6
}'
```

### 4. 输出参数

同 [文生视频](https://cloud.tencent.com/document/product/1823/135737#4.-.E8.BE.93.E5.87.BA.E5.8F.82.E6.95.B0) 输出参数。

### 5. 响应示例

```json
{
  "task_id": "4-WandVideo-a786becfdc80433b8cff4aa344c8fd3d",
  "request_id": "3aec3299-06ad-4654-8b45-c57b823a15d2"
}
```

### 6. 错误码

请求失败时返回错误码，具体错误码及处理建议见 [附录：统一错误码](https://cloud.tencent.com/document/product/1823/135737#.E7.BB.9F.E4.B8.80.E9.94.99.E8.AF.AF.E7.A0.81)。任务状态说明同 [文生视频](https://cloud.tencent.com/document/product/1823/135737#6.-.E9.94.99.E8.AF.AF.E7.A0.81)。

## 多模态参考生视频（H3 / H3-Max）

### 1. 接口描述

以文本 + 参考图片 / 参考视频 / 参考音频的组合为参考生成视频，`minimax-video-h3` 与 `minimax-video-h3-max` 均支持。不可仅输入音频，须至少包含 1 个参考视频或图片。

**接口：** `POST https://tokenhub.tencentmaas.com/v1/wand/minimax-video-v2/generation`

### 2. 输入参数

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| model | 是 | string | 模型名称。取值：`minimax-video-h3`、`minimax-video-h3-max` |
| content | 是 | array[object] | 多模态输入数组：1 个 `text` + 参考素材（`role` 为 `reference_image` / `reference_video` / `reference_audio`）。参考图 ≤ 9 张、参考视频 ≤ 3 段、参考音频 ≤ 3 段，素材合计 ≤ 12 个。子字段与素材约束见下表。    图片 content[].image\_url：支持0张-9张参考图输入（role=reference\_image），支持 URL 或 Base64格式，JPG/JPEG/PNG/WEBP/HEIC/HEIF；宽高[256，5760]px，宽高比[0.4，2.5]；单个文件大小<=30MB；  1. Base64：图片转为 Base64 后计入请求体，请求体总大小 <=64MB（Base64 会放大约 33%，大图请用公网 URL）；格式要求：`data:image/<图片格式>;base64,`。  2. URL：需要公网可访问（http/https）。    视频 content[].video\_url：支持0个-3个参考视频（role=reference\_video），视频格式：mp4/mov，支持 URL 或 Base64格式，单段参考视频时长2~15 秒，所有参考视频时长总和≤15 秒；单个视频大小 <=50MB  1. Base64：所有参考视频的 Base64大小和<=64MB；格式要求：`data:video/<视频格式>;base64,`。 注：视频为 mov 时视频格式填 quicktime。  2. URL：需要公网可访问（http/https）。    音频 content[].audio\_url：支持0段-3段参考音频（role=reference\_audio），支持 URL 或 Base64格式，音频格式：wav/mp3，单段 2~15 秒，所有参考音频时长总和 ≤15 秒；单个音频大小 <=15MB  1. Base64：音频转为 Base64 后计入请求体，请求体总大小 <=64MB；格式要求：`data:audio/<音频格式>;base64,`。 注：音频为 mp3 时音频格式填 mpeg。  2. URL：需要公网可访问（http/https）。 |
| resolution | 是 | string | 视频分辨率。h3：768P / 2K；h3-max：仅 480P / 768P（不支持 2K，传入 1080P / 2K / 4K 会静默降级为 768P）。 |
| duration | 是 | integer | 视频时长（秒）。h3：4 ~ 15 的整数；h3-max：5 ~ 15 的整数（不支持 4 秒）。传入区间外的值不会报错，会静默回落为 5 秒。 |
| ratio | 否 | string | 画面宽高比。默认 adaptive（自动）；可显式指定 21:9 / 16:9 / 4:3 / 1:1 / 3:4 / 9:16。 |
| aigc\_watermark | 否 | boolean | 是否添加 AIGC 标识水印。默认值：false。 |
| extra.prompt\_expansion\_mode | 否 | string | **仅** `minimax-video-h3-max` **生效**，`minimax-video-h3` 传入会被忽略。提示词扩写模式。disabled 表示关闭提示词扩写；balanced 表示均衡扩写且为默认值；quality 表示质量优先扩写。  可用选项: disabled, balanced, quality  不传 extra 或不传此属性时，使用 balanced。不要传 balance、空字符串、布尔值或其他未声明字段。 |

**content 数组元素子字段：**

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| type | 是 | string | 素材类型。枚举：text / image\_url / video\_url / audio\_url。 |
| text | 条件必选 | string | 文本提示词，type=text 时必选（每次请求必须包含一个非空 text 项），最多 7000 个字符。 |
| image\_url | 条件必选 | object | 图片素材，type=image\_url 时必选。结构 `{ "url": "..." }` |
| video\_url | 条件必选 | object | 视频素材，type=video\_url 时必选。结构 `{ "url": "..." }` |
| audio\_url | 条件必选 | object | 音频素材，type=audio\_url 时必选。结构 `{ "url": "..." }` |
| role | 否 | string | 素材用途。枚举：first\_frame / last\_frame / reference\_image / reference\_video / reference\_audio。 |

**注意：**

图生视频与多模态参考生**互斥**：content 中出现 `reference_image` / `reference_video` / `reference_audio` 任一 role，就不能再出现 `first_frame` / `last_frame`，反之亦然。

参考视频：MP4 / MOV（H.264 / H.265），≤ 50MB，≤ 3 段，单段 2~15 秒、总时长 ≤ 15 秒，宽高 [256, 5760]px，帧率 [23.976, 60]。

参考音频：WAV / MP3，≤ 15MB，≤ 3 段，单段 2~15 秒、总时长 ≤ 15 秒；不可仅输入音频。

请求体总大小 ≤ 64MB，大文件请使用公网 URL，勿用 Base64。

### 3. 请求示例

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/minimax-video-v2/generation' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "minimax-video-h3",
  "content": [
    {
      "type": "text",
      "text": "参考图中的角色在参考视频的场景中自然运动"
    },
    {
      "type": "image_url",
      "image_url": { "url": "https://example.com/character.jpg" },
      "role": "reference_image"
    },
    {
      "type": "video_url",
      "video_url": { "url": "https://example.com/scene.mp4" },
      "role": "reference_video"
    }
  ],
  "resolution": "768P",
  "duration": 6,
  "ratio": "16:9"
}'
```

### 4. 输出参数

同 [文生视频](https://cloud.tencent.com/document/product/1823/135737#4.-.E8.BE.93.E5.87.BA.E5.8F.82.E6.95.B0) 输出参数。

### 5. 响应示例

```json
{
  "task_id": "4-WandVideo-a786becfdc80433b8cff4aa344c8fd3d",
  "request_id": "3aec3299-06ad-4654-8b45-c57b823a15d2"
}
```

### 6. 错误码

请求失败时返回错误码，具体错误码及处理建议见 [附录：统一错误码](https://cloud.tencent.com/document/product/1823/135737#.E7.BB.9F.E4.B8.80.E9.94.99.E8.AF.AF.E7.A0.81)。任务状态说明同 [文生视频](https://cloud.tencent.com/document/product/1823/135737#6.-.E9.94.99.E8.AF.AF.E7.A0.81)。

## 查询任务结果

### 1. 接口描述

各生成接口共用的任务查询方式：提交任务返回 `task_id` 后，通过统一的任务查询端点轮询任务状态，成功后从结果中获取视频地址。

**接口：** `GET https://tokenhub.tencentmaas.com/v1/wand/minimax-video/tasks/{task_id}`

**接口：** `GET https://tokenhub.tencentmaas.com/v1/wand/minimax-video-v2/tasks/{task_id}`

**说明：**

路径中的 `{task_id}` 即提交任务时返回的 `task_id`（示例中以 `YOUR_TASK_ID` 占位）。视频生成约需 1~3 分钟，建议每 3~5 秒轮询一次。

### 2. 输入参数

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| task\_id | 是 | string | 任务 ID（路径参数），即提交任务时返回的 `task_id`。 |

### 3. 请求示例

**模型：minimax-video-v2.3**

```bash
curl -X GET 'https://tokenhub.tencentmaas.com/v1/wand/minimax-video/tasks/YOUR_TASK_ID' \\
  -H 'Authorization: Bearer YOUR_API_KEY'
```

**模型：minimax-video-h3**

```bash
curl -X GET 'https://tokenhub.tencentmaas.com/v1/wand/minimax-video-v2/tasks/YOUR_TASK_ID' \\
  -H 'Authorization: Bearer YOUR_API_KEY'
```

### 4. 输出参数

**V1（minimax-video-v2.3 / v2.3-fast）：**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| task\_id | string | 任务 ID。 |
| status | string | 任务状态：Processing / Success / Fail。 |
| content | object | 任务生成结果内容，任务成功后返回。 |
| content.url | string | 生成视频的下载地址，为临时地址，有效期 12 小时，请及时下载转存。 |
| video\_width | integer | 生成视频宽度（像素），任务成功后返回。 |
| video\_height | integer | 生成视频高度（像素），任务成功后返回。 |
| base\_resp | object | 本次查询请求的状态对象（与任务成败无关）。 |
| base\_resp.status\_code | integer | 查询请求状态码，恒为 0。 |
| base\_resp.status\_msg | string | 查询请求状态描述；`status=Fail` 时该字段承载任务失败原因。 |
| tokenhub\_usage | object | 用量消耗。 |
| tokenhub\_usage.total\_tokens | integer | 本次任务消耗的 token 数，用于计费/对账。 |
| request\_id | string | 唯一请求标识，用于排查问题。 |

**注意：**

V1 查询的视频地址在 `content.url`（非顶层 `url`）；`base_resp.status_code` 恒为 0，任务成败以 `status` 为准，失败原因读 `base_resp.status_msg`。

**V2（minimax-video-h3 / h3-max）：**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| task | object | 任务对象。 |
| task.id | string | 任务 ID。 |
| task.model | string | 使用的模型名称，例如 MiniMax-H3、MiniMax-H3-Max。 |
| task.status | string | 任务状态：queued / running / succeeded / failed / cancelled。 |
| task.task\_type | string | 任务类型，例如 generation（视频生成）。 |
| task.modality | string | 任务产出模态，例如 video。 |
| task.created\_at | integer | 任务创建时间，Unix 时间戳（秒）。 |
| task.updated\_at | integer | 任务更新时间，Unix 时间戳（秒）。 |
| task.content | object | 任务生成结果内容，成功后返回。 |
| task.content.url | string | 生成视频下载地址，临时 URL，有效期 12 小时，请及时下载保存。 |
| task.error | object | 任务失败信息，status=failed 时返回。 |
| task.error.code | string | 失败错误码。 |
| task.error.message | string | 失败原因描述。 |
| task.duration | integer | 视频时长，单位：秒。 |
| task.resolution | string | 视频分辨率，例如 768P。 |
| task.ratio | string | 视频宽高比例，例如 16:9。 |
| task.usage | object | 任务视频用量信息。 |
| task.usage.input\_image\_count | integer | 输入图片数量。 |
| task.usage.input\_seconds | integer | 输入视频时长，单位：秒。 |
| task.usage.output\_seconds | integer | 输出视频时长，单位：秒。 |
| task.usage.total\_seconds | integer | 总计视频时长，单位：秒。 |
| tokenhub\_usage | object | 本次请求用量消耗。 |
| tokenhub\_usage.total\_tokens | integer | 本次任务消耗的 token 数，用于计费和对账。 |
| request\_id | string | 请求唯一标识，用于问题定位和排查。 |

**注意：**

V2 查询响应为 `task` 对象，无 `base_resp`、无顶层 `status`；任务标识与状态在 `task.id` / `task.status`。

### 5. 响应示例

**V1（minimax-video-v2.3）生成成功：**

```json
{
  "task_id": "4-WandVideo-a786becfdc80433b8cff4aa344c8fd3d",
  "status": "Success",
  "content": {
    "url": "https://aigc-video.cos.myqcloud.com/xxx/result.mp4"
  },
  "video_width": 1366,
  "video_height": 768,
  "base_resp": {
    "status_code": 0,
    "status_msg": "success"
  },
  "tokenhub_usage": {
    "total_tokens": 102655
  },
  "request_id": "3aec3299-06ad-4654-8b45-c57b823a15d2"
}
```

**V2（minimax-video-h3 / h3-max）生成成功：**

```json
{
  "task": {
    "id": "4-WandVideo-a786becfdc80433b8cff4aa344c8fd3d",
    "model": "MiniMax-H3-Max",
    "task_type": "generation",
    "modality": "video",
    "status": "succeeded",
    "created_at": 1772345678,
    "updated_at": 1772345810,
    "resolution": "768P",
    "duration": 5,
    "ratio": "16:9",
    "content": {
      "url": "https://aigc-video.cos.myqcloud.com/xxx/result.mp4"
    },
    "usage": {
      "total_seconds": 5,
      "input_seconds": 0,
      "output_seconds": 5,
      "input_image_count": 0
    }
  },
  "tokenhub_usage": {
    "total_tokens": 102655
  },
  "request_id": "3aec3299-06ad-4654-8b45-c57b823a15d2"
}
```

### 6. 错误码

| status | 含义 | 处理建议 |
| --- | --- | --- |
| Success（V1）/ succeeded（V2） | 生成成功 | 从结果中获取视频地址。 |
| Processing / queued / running | 准备中 / 排队中 / 生成中 | 每 3~5 秒轮询一次，直至成功。 |
| Fail（V1）/ failed（V2） | 生成失败 | 查看失败原因（V1 见 `base_resp.status_msg`，V2 见 `task.error.message`），修改后重试；持续失败请联系技术支持并附 request\_id。 |
| cancelled（V2） | 任务已取消 | 任务已终止且不会再更新，如需结果请重新提交任务。 |

请求级错误码见 [附录：统一错误码](https://cloud.tencent.com/document/product/1823/135737#.E7.BB.9F.E4.B8.80.E9.94.99.E8.AF.AF.E7.A0.81)。

## 附录

### 统一错误码

| HTTP 状态码 | 业务码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 200 | 0 | success | 请求成功。 |
| 401 | 1000 | Authentication failed | Authorization 缺失或 apikey 非法。 |
| 401 | 1001 | Authorization is empty | 未携带 Authorization 头。 |
| 401 | 1002 | Authorization is invalid | apikey 无效或已失效。 |
| 401 | 1003 | Authorization is not yet valid | apikey 尚未生效。 |
| 401 | 1004 | Authorization has expired | apikey 已过期。 |
| 429 | 1100 | Account exception | 账号异常（可能欠费、被封禁或被暂停）。 |
| 429 | 1101 | Account in arrears (postpaid) | 后付费账号欠费。 |
| 429 | 1102 | Resource pack depleted or expired | 资源包已用完或已过期。 |
| 403 | 1103 | Access denied for the requested resource | 请求资源无访问权限（未订阅对应模型/能力）。 |
| 400 | 1200 | Invalid request parameters | 请求参数非法（缺失必选项、类型错误、枚举越界等）。 |
| 400 | 1201 | Invalid parameters | 参数值不合法，请对照文档参数取值范围检查。 |
| 404 | 1202 | The requested method is invalid | HTTP 方法错误。 |
| 404 | 1203 | The requested resource does not exist | 端点路径错误或资源不存在。 |
| 400 | 1300 | Trigger the platform strategy | 触发平台策略（如内容审核不通过、违规输入）。 |
| 400 | 1301 | Trigger platform sensitive word list | 命中敏感词或违规提示词。 |
| 429 | 1302 | Too frequent API calls | 调用过于频繁，触发限流。 |
| 429 | 1303 | Concurrency or QPS exceeds the limit | 并发或 QPS 超过预设配额。 |
| 400 | 1304 | Trigger IP strategy | 触发 IP 策略拦截。 |
| 500 | 5000 | Internal server error | 服务器内部错误。 |
| 503 | 5001 | Server is temporarily unavailable | 服务暂不可用（多为忙碌或维护中）。 |
| 504 | 5002 | Server internal timeout | 服务内部超时。 |

### 运镜指令语法

v2.3 / v2.3-fast 支持在 prompt 中通过 `[指令]` 格式添加运镜指令（h3 使用自然语言描述即可）：

左右移：[左移]、[右移]；左右摇：[左摇]、[右摇]；推拉：[推进]、[拉远]

升降：[上升]、[下降]；上下摇：[上摇]、[下摇]；变焦：[变焦推近]、[变焦拉远]

其他：[晃动]、[跟随]、[固定]

使用规则：

**组合运镜**：同一组 `[]` 内的多个指令同时生效，如 `[左摇,上升]`，建议组合不超过 3 个。

**顺序运镜**：prompt 中前后出现的指令依次生效，如 “...[推进]，然后...[拉远]”。

**自然语言**：也支持自然语言描述运镜，但使用标准指令能获得更准确的响应。

### 素材通用约束

**图片（v2.3 / v2.3-fast）**：JPG / JPEG / PNG / WebP；< 20MB；短边 > 300px；宽高比 2:5 ~ 5:2；支持公网 URL 或 Base64 图片数据（Data URL 形式，如 `data:image/jpeg;base64,...`）。

**图片（h3）**：JPG / JPEG / PNG / WEBP / HEIC / HEIF；≤ 30MB；宽高 [256, 5760]px；宽高比 [0.4, 2.5]；首帧 ≤ 1、尾帧 ≤ 1、参考图 ≤ 9。

**视频（h3 参考视频）**：MP4 / MOV（H.264 / H.265，音频 AAC / MP3）；≤ 50MB；≤ 3 段；单段 2~15 秒、总时长 ≤ 15 秒；宽高 [256, 5760]px；宽高比 [0.4, 2.5]；帧率 [23.976, 60]。

**音频（h3 参考音频）**：WAV / MP3；≤ 15MB；≤ 3 段；单段 2~15 秒、总时长 ≤ 15 秒。

**注意：**

h3 请求体总大小 ≤ 64MB，大文件请使用公网 URL，勿用 Base64。

## 常见问题

#### **1. 四款模型如何选择？**

通用场景、要强物理表现与指令遵循：`minimax-video-v2.3`（文生图生均可）。

图生场景、速度与成本优先（批量创作最高可降 50% 成本）：`minimax-video-v2.3-fast`（仅图生）。

要 2K 直出、多模态参考（参考图/视频/音频）、最长 15 秒：`minimax-video-h3`。

要更快出片、成本更低，且不要求 2K（h3-max 最高仅 768P，不支持 2K）：`minimax-video-h3-max`。另支持 `extra.prompt_expansion_mode` 提示词扩写，h3 不支持该参数。

#### **2. minimax-video-v2.3-fast 能用于文生视频吗？**

不能。v2.3-fast 仅支持图生视频（首帧），文生视频请使用 `minimax-video-v2.3` 或 `minimax-video-h3`。

#### **3. 时长和分辨率的组合有什么限制？**

v2.3 / v2.3-fast：768P 可选 6 或 10 秒，1080P 仅支持 6 秒。

h3：时长 4~15 秒，768P / 2K 均可。

h3-max：时长 5~15 秒（不支持 4 秒），仅 480P / 768P，不支持 2K。

#### **4. 生成结果视频链接会过期吗？**

会过期。生成结果为临时地址，有效期 12 小时，请在任务成功后及时下载视频文件并转存到自有存储，不要长期依赖该链接。
