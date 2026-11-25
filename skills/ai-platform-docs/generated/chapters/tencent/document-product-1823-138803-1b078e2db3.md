<!-- Official source: https://cloud.tencent.com/document/product/1823/138803 -->
<!-- Source SHA-256: 8f6e9a222535302c33e311743888d3bf6dc983fe04abaa96a54177e418283150 -->

# Kling 生图调用指南

官方来源：https://cloud.tencent.com/document/product/1823/138803
最近更新时间：2026-11-24 16:41:24

## 概述

可灵（Kling）是快手推出的视觉生成模型系列。本文介绍如何通过 TokenHub 调用可灵图片生成模型 `kling-image-v3`、`kling-image-o1`、`kling-image-v3-omni`、`kling-image-v4`、`kling-image-v4-long`。

### 前提条件

已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号并开通 TokenHub 服务。

已在 [TokenHub 控制台](https://console.cloud.tencent.com/tokenhub/apikey) 获取 API Key。

在 [控制台-在线推理-视觉模型](https://console.cloud.tencent.com/tokenhub/inference?regionId=1&serviceType=VISION) 处开启对应模型的后付费。

**说明：**

下文所有示例中的 YOUR\_API\_KEY 均需替换为您自己的 API Key，鉴权方式为请求头 Authorization: Bearer YOUR\_API\_KEY。

### 调用流程

图片生成为耗时任务，接口采用**异步调用**模式，统一分两步：

1. **提交任务**：调用图片生成接口，成功返回任务 ID（v3 / o1 / v3-omni 为 `data.task_id`，v4 / v4-long 为 `data.id`）。

2. **轮询结果**：携带任务 ID 调用 [查询任务](https://cloud.tencent.com/document/product/1823/138803#.E6.9F.A5.E8.AF.A2.E4.BB.BB.E5.8A.A1) 接口（建议每 3~5 秒一次），直至任务成功：v3 / o1 / v3-omni 为 `task_status = succeed`，从 `task_result.images` 获取图片地址；v4 / v4-long 为 `status = succeeded`，从 `outputs[]` 获取图片地址。

**说明：**

Kling-Image-v4 / v4-long 与 v3 系列的提交接口路径、请求结构不同（v4 系列以 `contents` + `settings` 组织参数），但共用同一个查询接口。

### 模型列表

| 模型名称 | model 参数值 | 支持能力 | 提示词上限 | 分辨率 |
| --- | --- | --- | --- | --- |
| Kling-Image-v3 | `kling-image-v3` | 文生图 / 图生图（单图参考） | 2500 字符 | 1K / 2K |
| Kling-Image-o1 | `kling-image-o1` | 文生图 / 图生图（多图参考） | 2500 字符 | 1K / 2K |
| Kling-Image-v3-omni | `kling-image-v3-omni` | 文生图 / 图生图（多图参考）/ 系列组图 | 2500 字符 | 1K / 2K / 4K |
| Kling-Image-v4 | `kling-image-v4` | 文生图 / 图生图（多图参考）/ 主体参考 / 系列组图 | 英文 50000 / 非英文 21000 字符 | 2K / 4K / 8K |
| Kling-Image-v4-long | `kling-image-v4-long` | 长图生成：电商详情页 / 网页设计 | 英文 166000 / 非英文 71000 字符 | 1K / 2K |

**说明：**

Kling-Image-v3 / o1 / v3-omni 均支持 16:9、9:16、1:1、4:3、3:4、3:2、2:3、21:9 共 8 种画面纵横比；`kling-image-o1` 与 `kling-image-v3-omni` 额外支持 auto（根据传入内容智能判断画面比例）。

`kling-image-v4` 支持上述 8 种画面纵横比及 auto，默认 auto。

`kling-image-v4-long` 输出一张完整长图，不设置画面纵横比，通过 `settings.skill` 选择电商详情页或网页设计场景。

## 图片生成（Kling-Image-v3）

### 1. 接口描述

Kling-Image-v3 图片生成接口。支持文生图与图生图（单图参考）：传入 `image` 即为图生图，未传时按文本提示词进行文生图，支持正负向提示词。

**接口：** `POST https://tokenhub.tencentmaas.com/v1/wand/kling-image/generation`

### 2. 输入参数

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| model | 是 | string | 模型 ID。取值：`kling-image-v3` |
| prompt | 是 | string | 正向文本提示词，长度 ≤ 2500 字符。未传 `image` 时按此文本进行文生图。 |
| negative\_prompt | 否 | string | 负向文本提示词，长度 ≤ 2500 字符。仅文生图支持；图生图（`image` 不为空）场景下不支持负向提示词。 |
| image | 否 | string | 参考图片（单图）。传入后即为图生图。  支持图片 URL（请确保可被访问）或 Base64 编码；Base64 方式无须添加 `data:image/png;base64,` 前缀，直接传 Base64 字符串本身。 |
| element\_list | 否 | array | 主体参考列表，基于主体库中主体的 ID 配置，格式：`"element_list": [{"element_id": 主体 ID}]`。  参考主体数量与参考图片数量之和不得超过 10。 |
| aspect\_ratio | 否 | string | 生成图片的画面纵横比（宽:高）。  可选值：16:9、9:16、1:1、4:3、3:4、3:2、2:3、21:9。默认值 16:9。 |
| resolution | 否 | string | 生成图片的清晰度。  可选值：1k（1K 标清）、2k（2K 高清）。默认值 1k。 |
| n | 否 | integer | 生成图片数量。取值范围 [1, 9]，默认 1。 |
| watermark\_info | 否 | object | 是否同时生成含水印的结果，格式：`"watermark_info": {"enabled": boolean}`。  true 为生成含水印结果，false 为不生成；暂不支持自定义水印。 |

### 3. 请求示例

```bash
# 文生图 / 图生图
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/kling-image/generation' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "kling-image-v3",
  "prompt": "a small orange kitten sitting on a sunny windowsill",
  "image": "https://example.com/input.jpg",
  "aspect_ratio": "1:1",
  "resolution": "2k",
  "n": 3
}'
```

文生图时删去 `image` 字段即可，此时可另传 `negative_prompt`（图生图不支持负向提示词）。

### 4. 输出参数

<table><colgroup><col/><col/><col/></colgroup><tbody><tr><td><div>参数名</div></td><td><div>类型</div></td><td><div>描述</div></td></tr><tr><td colspan="1" rowspan="1"><div>code</div></td><td colspan="1" rowspan="1"><div>string</div></td><td colspan="1" rowspan="1"><div>错误码。</div></td></tr><tr><td colspan="1" rowspan="1"><div>message</div></td><td colspan="1" rowspan="1"><div>string</div></td><td colspan="1" rowspan="1"><div>错误信息。</div></td></tr><tr><td colspan="1" rowspan="1"><div>request_id</div></td><td colspan="1" rowspan="1"><div>string</div></td><td colspan="1" rowspan="1"><div>请求 ID，系统生成，用于跟踪请求、排查问题。</div></td></tr><tr><td><div>data.task_id</div></td><td><div>string</div></td><td><div>任务 ID。</div></td></tr><tr><td><div>data.task_status</div></td><td><div>string</div></td><td><div>任务状态，枚举值：submitted（已提交）、processing（处理中）、succeed（成功）、failed（失败）。</div></td></tr><tr><td><div>data.created_at</div></td><td><div>integer</div></td><td><div>任务创建时间，Unix 时间戳，单位 ms。</div></td></tr><tr><td><div>data.updated_at</div></td><td><div>integer</div></td><td><div>任务更新时间，Unix 时间戳，单位 ms。</div></td></tr></tbody></table>

### 5. 响应示例

```json
{
    "code": 0,
    "message": "SUCCEED",
    "request_id": "58b5fba6-b418-4cfa-9ecb-fa5e0406bc6d",
    "data": {
        "task_id": "251435731-WandImage-d59f0494e75a47d791135b1294892545",
        "task_status": "submitted",
        "created_at": 1790237643425,
        "updated_at": 1790237643425,
        "task_info": {}
    }
}
```

## Omni 图片生成（Kling-Image-o1 / Kling-Image-v3-omni）

### 1. 接口描述

Kling-Image-o1 与 Kling-Image-v3-omni 的图片生成接口。支持文生图、多图参考图生图与系列组图：传入 `image_list`（最多 10 张）即为多图参考，可在提示词中通过 `<<<image_N>>>` 引用具体参考图；`kling-image-v3-omni` 可通过 `result_type` 开启系列组图生成，并支持 4K 超高清直出。

**接口：** `POST https://tokenhub.tencentmaas.com/v1/wand/kling-image/generation`

### 2. 输入参数

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| model | 是 | string | 模型 ID。取值：`kling-image-o1`、`kling-image-v3-omni` |
| prompt | 是 | string | 文本提示词，可包含正向描述与负向描述，长度 ≤ 2500 字符。  多图参考场景下，可通过 `<<<image_1>>>` 的格式在提示词中引用某张参考图，如：`将<<<image_1>>>中的人物融合到<<<image_2>>>的场景中`。未传 `image_list` 时按此文本进行文生图。 |
| image\_list | 否 | array[string] | 参考图片列表（多图），最多 10 张。传入后即为多图参考图生图。  支持图片 URL（请确保可被访问）或 Base64 编码；Base64 方式无须添加 `data:image/png;base64,` 前缀，直接传 Base64 字符串本身。 |
| element\_list | 否 | array | 主体参考列表，基于主体库中主体的 ID 配置，格式：`"element_list": [{"element_id": 主体 ID}]`。  参考主体数量与参考图片数量之和不得超过 10。 |
| aspect\_ratio | 否 | string | 生成图片的画面纵横比（宽:高）。  可选值：16:9、9:16、1:1、4:3、3:4、3:2、2:3、21:9、auto（根据传入内容智能判断画面比例）。默认值 auto。  注：文生图场景（未传 `image_list`）不支持 auto。 |
| resolution | 否 | string | 生成图片的清晰度。  可选值：1k（1K 标清）、2k（2K 高清）、4k（4K 超高清）。默认值 1k。  4K 仅 `kling-image-v3-omni` 支持；`kling-image-o1` 支持 1K / 2K。 |
| n | 否 | integer | 生成图片数量。取值范围 [1, 9]，默认 1。  `result_type` 为 series 时本参数无效。 |
| result\_type | 否 | string | 生成结果单图 / 组图切换开关。  可选值：single（单图，默认）、series（组图）。系列组图仅 `kling-image-v3-omni` 支持。 |
| series\_amount | 否 | integer | 组图模式的图片数量，仅 `result_type` 为 series 时生效。  可选值：2 ~ 9、auto（根据传入内容智能选择数量）。默认值 4。 |
| watermark\_info | 否 | object | 是否同时生成含水印的结果，格式：`"watermark_info": {"enabled": boolean}`。  true 为生成含水印结果，false 为不生成；暂不支持自定义水印。 |

### 3. 请求示例

**多图参考（Kling-Image-o1）**

```bash
# 文生图 / 多图参考图生图
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/kling-image/generation' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "kling-image-o1",
  "prompt": "put the character in <<<image_1>>> into the scene of <<<image_2>>>",
  "image_list": [
    "https://example.com/character.jpg",
    "https://example.com/scene.jpg"
  ],
  "resolution": "2k",
  "n": 1
}'
```

**多图参考 + 系列组图（Kling-Image-v3-omni）**

```bash
# 文生图 / 多图参考图生图 / 系列组图
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/kling-image/generation' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "kling-image-v3-omni",
  "prompt": "a small orange kitten sitting on a sunny windowsill",
  "image_list": ["https://example.com/input.jpg"],
  "result_type": "series",
  "series_amount": 3
}'
```

提交任务的输出参数与响应示例同 图片生成（Kling-Image-v3）。

## 图片生成（Kling-Image-v4）

### 1. 接口描述

以 `contents` 数组组织提示词与参考素材（支持提示词、参考图、主体），结合 `settings` 控制输出清晰度、宽高比、单图 / 组图数量，异步生成图片。

**接口：** `POST https://tokenhub.tencentmaas.com/v1/wand/kling/image-generation`

### 2. 输入参数

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| model | 是 | string | 模型 ID。取值：`kling-image-v4` |
| contents | 是 | array | 参考素材合集，详见下方字段说明。必须至少包含一个 `type=prompt` 元素。 |
| contents[].type | 是 | string | 素材类型，可选值：`prompt`（提示词）、`refer_image`（参考图）、`element`（主体库主体）。图片与主体合计最多 10 个，提示词不占参考名额。 |
| contents[].text | 否 | string | 仅 `type=prompt` 使用，文本提示词内容，非空。纯英文 ≤ 50000 字符，纯非英文 ≤ 21000 字符；混合输入须满足 `英文/50000 + 非英文/21000 ≤ 1`。 |
| contents[].url | 否 | string | 仅 `type=refer_image` 使用，参考图 URL 或 Base64 编码。支持 .jpg / .jpeg / .png，单张 ≤ 30MB，宽高均 ≥ 300px，宽高比 2:5 ~ 5:2。 |
| contents[].element\_id | 否 | string | 仅 `type=element` 使用，主体库中的主体 ID（仅支持多图主体）。 |
| contents[].id | 否 | string | 素材索引 ID，用于在提示词中通过 `@id` 引用该素材；同一任务内不得重复。 |
| settings | 否 | object | 输出设置，详见下方字段。 |
| settings.result\_type | 否 | string | 生成结果类型，可选值：`single`（单图，默认）、`series`（系列组图，同组图片共享 `group_id`）。 |
| settings.n | 否 | integer | 单图模式生成张数，取值范围 [1, 9]，默认 1；`result_type=series` 时无效。 |
| settings.series\_amount | 否 | integer / string | 组图模式张数，取值 [2, 10] 或字符串 `auto`，默认 4；仅 `result_type=series` 时生效。 |
| settings.resolution | 否 | string | 输出清晰度，可选值：`2k`（默认）、`4k`、`8k`。 |
| settings.aspect\_ratio | 否 | string | 输出宽高比，可选值：`16:9`、`9:16`、`1:1`、`4:3`、`3:4`、`3:2`、`2:3`、`21:9`、`auto`。默认值 `auto`。 |
| options | 否 | object | 通用配置。 |
| options.watermark\_info | 否 | object | 是否同时生成含水印的结果，格式：`{"enabled": boolean}`，默认 `false`；暂不支持自定义水印。 |

**说明：**

`options.callback_url` 与 `options.external_task_id` 暂不支持，请勿传入。

### 3. 请求示例

```bash
# 图生图（单图）
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/kling/image-generation' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "kling-image-v4",
  "contents": [
    {
      "type": "prompt",
      "text": "以 @dog 中的小狗为参考，生成一张三维动画风格的角色海报，保留毛色和外观特征，暖色灯光，背景简洁。"
    },
    {
      "type": "refer_image",
      "url": "https://example.com/dog.png",
      "id": "dog"
    }
  ],
  "settings": {
    "result_type": "single",
    "n": 1,
    "resolution": "2k",
    "aspect_ratio": "1:1"
  }
}'

# 系列组图
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/kling/image-generation' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "kling-image-v4",
  "contents": [
    {
      "type": "prompt",
      "text": "以 @dog 中的小狗为主角，生成四张连贯的三维动画风格故事图片，依次表现：走进咖啡馆、在窗边落座、闻咖啡香、在门口告别"
    },
    {
      "type": "refer_image",
      "url": "https://example.com/dog.png",
      "id": "dog"
    }
  ],
  "settings": {
    "result_type": "series",
    "series_amount": 4,
    "resolution": "2k",
    "aspect_ratio": "3:4"
  },
  "options": {
    "watermark_info": {"enabled": false}
  }
}'
```

文生图时删去 `refer_image` 项即可；使用主体参考时，在 `contents` 中加入 `type` 为 `element` 的项（传 `element_id` 与 `id`），并在提示词中以 `@id` 引用。

### 4. 输出参数

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| code | integer | 错误码，0 为成功；非 0 时参见 `message` 排查。 |
| message | string | 接口消息。 |
| request\_id | string | 请求 ID，系统生成，用于跟踪请求、排查问题。 |
| data.id | string | 任务 ID，用于查询任务结果。 |
| data.status | string | 任务状态，提交成功为 `submitted`。 |
| data.message | string | 任务状态信息。 |
| data.create\_time | integer | 任务创建时间，Unix 时间戳，单位 ms。 |
| data.update\_time | integer | 任务更新时间，Unix 时间戳，单位 ms。 |

### 5. 响应示例

```json
{
  "code": 0,
  "message": "SUCCEED",
  "request_id": "271d2cf5-1309-4af9-a890-604fa73048d6",
  "data": {
    "id": "251435731-kling_image_v4-30bfc3211f66479e8b14135fd1ed5bdc",
    "status": "submitted",
    "message": "",
    "create_time": 1794984991920,
    "update_time": 1794984991920
  }
}
```

拿到 `data.id` 后，参考 [查询任务](https://cloud.tencent.com/document/product/1823/138803#.E6.9F.A5.E8.AF.A2.E4.BB.BB.E5.8A.A1) 一节轮询获取终态结果。

## 长图生成（Kling-Image-v4-long）

### 1. 接口描述

用于生成电商详情页或网页设计长图，最终返回一张完整图片。通过 `settings.skill` 切换场景：`ecommerce` 为电商详情页（搭配 `refer_image` 商品参考图），`webpage` 为网页设计（支持 `style_refer_image` 风格参考图与 `subject_refer_image` 主体参考图）。

**接口：** `POST https://tokenhub.tencentmaas.com/v1/wand/kling/long-image-generation`

### 2. 输入参数

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| model | 是 | string | 模型 ID。取值：`kling-image-v4-long` |
| contents | 是 | array | 参考素材合集，必填非空，必须至少包含一个 `type=prompt` 元素。 |
| contents[].type | 是 | string | 素材类型，可选值：`prompt`、`refer_image`、`style_refer_image`、`subject_refer_image`。**不支持 `element`**。 |
| contents[].text | 否 | string | 仅 `type=prompt` 使用，文本提示词内容，非空。纯英文 ≤ 166000 字符，纯非英文 ≤ 71000 字符；混合输入须满足 `英文/166000 + 非英文/71000 ≤ 1`。 |
| contents[].url | 否 | string | 仅 `refer_image` / `style_refer_image` / `subject_refer_image` 使用，参考图 URL 或 Base64 编码。支持 .jpg / .jpeg / .png，单张 ≤ 30MB，宽高均 ≥ 300px，宽高比 2:5 ~ 5:2。 |
| contents[].id | 否 | string | 素材索引 ID，用于在提示词中通过 `@id` 引用；同一任务内不得重复。 |
| settings | 是 | object | 输出设置，必填。 |
| settings.skill | 是 | string | 生成长图所使用的技能：`ecommerce`（电商详情页）、`webpage`（网页设计）。 |
| settings.length | 否 | string | 页面长度，可选值：`short`（约 2~5 功能页）、`medium`（约 6~10 功能页，默认）、`long`（约 11~18 功能页）；**仅 `skill=ecommerce` 生效**，`webpage` 下设置无效。 |
| settings.resolution | 否 | string | 输出清晰度，可选值：`1k`（默认）、`2k`。 |
| options | 否 | object | 通用配置。 |
| options.watermark\_info | 否 | object | 是否同时生成含水印的结果，格式：`{"enabled": boolean}`，默认 `false`；暂不支持自定义水印。 |

**说明：**

`skill=ecommerce` 时，`refer_image` 必填，必须提供 1~3 张商品参考图；请勿使用 `style_refer_image` / `subject_refer_image`。

`skill=webpage` 时，参考图请通过 `style_refer_image`（风格参考）/ `subject_refer_image`（主体参考）传入；请勿使用 `refer_image`。

`options.callback_url` 与 `options.external_task_id` 暂不支持，请勿传入。

### 3. 请求示例

```bash
# 电商详情页
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/kling/long-image-generation' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "kling-image-v4-long",
  "contents": [
    {
      "type": "prompt",
      "text": "为 @product 中的咖啡机设计完整电商详情页长图，包含主视觉、核心卖点和使用场景；仅使用提供的商品事实，不编造参数"
    },
    {
      "type": "refer_image",
      "url": "https://example.com/coffee_machine.png",
      "id": "product"
    }
  ],
  "settings": {
    "skill": "ecommerce",
    "length": "medium",
    "resolution": "1k"
  }
}'

# 网页设计
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/kling/long-image-generation' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "kling-image-v4-long",
  "contents": [
    {
      "type": "prompt",
      "text": "设计精品咖啡品牌官网视觉长图，包含品牌首屏、产品展示、烘焙理念、门店信息和页尾；输出一张完整设计图片"
    }
  ],
  "settings": {
    "skill": "webpage",
    "resolution": "2k"
  }
}'
```

### 4. 响应示例

```json
{
  "code": 0,
  "message": "SUCCEED",
  "request_id": "17f2c8b0-e050-4b6c-8adc-9b4a5b9760c6",
  "data": {
    "id": "251435731-kling_image_v4_long-f965a34379a0448881077763957514f9",
    "status": "submitted",
    "message": "",
    "create_time": 1794986040492,
    "update_time": 1794986040492
  }
}
```

输出参数说明同 图片生成（Kling-Image-v4）。拿到 `data.id` 后，参考 [查询任务](https://cloud.tencent.com/document/product/1823/138803#.E6.9F.A5.E8.AF.A2.E4.BB.BB.E5.8A.A1) 一节轮询获取终态结果。

## 查询任务

### 1. 接口描述

查询图片生成任务的状态与结果。五款模型共用本接口，提交任务后携带返回的任务 ID 轮询（建议每 3~5 秒一次）。返回结构按模型分为两类：

Kling-Image-v3 / o1 / v3-omni：直至 `task_status = succeed`，单图结果从 `task_result.images` 获取；`result_type` 为 series 的组图任务从 `task_result.series_images` 获取。

Kling-Image-v4 / v4-long：直至 `status = succeeded` 或 `status = failed`，结果从 `data[].outputs[]` 获取；长图生成最终只返回一张完整图片，Kling-Image-v4 按实际生成张数返回多条。

**接口：** `GET https://tokenhub.tencentmaas.com/v1/wand/kling-image/tasks/{task_id}`

### 2. 输入参数

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| task\_id | 是 | string | 任务 ID（路径参数），即提交任务时返回的 `task_id`（v3 / o1 / v3-omni）或 `data.id`（v4 / v4-long）。 |

### 3. 请求示例

```bash
curl -X GET 'https://tokenhub.tencentmaas.com/v1/wand/kling-image/tasks/YOUR_TASK_ID' \\
  -H 'Authorization: Bearer YOUR_API_KEY'
```

### 4. 输出参数

**Kling-Image-v3 / Kling-Image-o1 / Kling-Image-v3-omni：**

<table><colgroup><col/><col/><col/></colgroup><tbody><tr><td><div>字段</div></td><td><div>类型</div></td><td><div>说明</div></td></tr><tr><td><div>code</div></td><td><div>integer</div></td><td><div>错误码。</div></td></tr><tr><td><div>message</div></td><td><div>string</div></td><td><div>错误信息。</div></td></tr><tr><td><div>request_id</div></td><td><div>string</div></td><td><div>请求 ID，系统生成，用于跟踪请求、排查问题。</div></td></tr><tr><td colspan="1" rowspan="1"><div>tokenhub_usage</div></td><td colspan="1" rowspan="1"><div>object</div></td><td colspan="1" rowspan="1"><div>用量消耗。</div></td></tr><tr><td colspan="1" rowspan="1"><div>tokenhub_usage.total_tokens</div></td><td colspan="1" rowspan="1"><div>integer</div></td><td colspan="1" rowspan="1"><div>本次任务消耗的 token 数，用于计费/对账。</div></td></tr><tr><td><div>data.task_id</div></td><td><div>string</div></td><td><div>任务 ID。</div></td></tr><tr><td><div>data.task_status</div></td><td><div>string</div></td><td><div>任务状态，枚举值：submitted（已提交）、processing（处理中）、succeed（成功）、failed（失败）。</div></td></tr><tr><td><div>data.task_status_msg</div></td><td><div>string</div></td><td><div>任务状态信息，任务失败时展示失败原因。</div></td></tr><tr><td colspan="1" rowspan="1"><div>data.created_at</div></td><td colspan="1" rowspan="1"><div>integer</div></td><td colspan="1" rowspan="1"><div>任务创建时间，Unix 时间戳，单位 ms。</div></td></tr><tr><td colspan="1" rowspan="1"><div>data.updated_at</div></td><td colspan="1" rowspan="1"><div>integer</div></td><td colspan="1" rowspan="1"><div>任务更新时间，Unix 时间戳，单位 ms。</div></td></tr><tr><td><div>data.task_result.images[].index</div></td><td><div>integer</div></td><td><div>图片编号，0 ~ 9。</div></td></tr><tr><td><div>data.task_result.images[].url</div></td><td><div>string</div></td><td><div>生成图片的 URL。</div></td></tr><tr><td><div>data.task_result.images[].watermark_url</div></td><td><div>string</div></td><td><div>含水印图片的下载 URL（<code>watermark_info.enabled</code> 为 true 时返回）。</div></td></tr><tr><td><div>data.task_result.series_images[].index</div></td><td><div>integer</div></td><td><div>组图序号（组图任务返回）。</div></td></tr><tr><td><div>data.task_result.series_images[].url</div></td><td><div>string</div></td><td><div>组图图片的 URL（组图任务返回）。</div></td></tr></tbody></table>

**Kling-Image-v4 / Kling-Image-v4-long：**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| code | integer | 错误码，0 为成功；非 0 时参见 `message` 排查。 |
| message | string | 接口消息。 |
| request\_id | string | 请求 ID，排查问题时请携带。 |
| tokenhub\_usage.total\_tokens | integer | 本次任务消耗的 token 数，用于计费/对账。 |
| data[].id | string | 被查询的任务 ID。 |
| data[].status | string | 任务状态：`submitted`（已提交）、`processing`（处理中）、`succeeded`（成功）、`failed`（失败）。 |
| data[].message | string | 任务状态信息，任务失败时展示失败原因（如触发平台的内容风控等）。 |
| data[].create\_time | integer | 任务创建时间，Unix 时间戳，单位 ms。 |
| data[].update\_time | integer | 任务更新时间，Unix 时间戳，单位 ms。 |
| data[].outputs[].type | string | 生成结果类型，图片任务为 `image`。 |
| data[].outputs[].url | string | 生成图片的 URL（防盗链，有效期约 12 小时，请及时下载转存）。 |
| data[].outputs[].watermark\_url | string | 含水印图片的下载 URL（仅在 `options.watermark_info.enabled=true` 时返回）。 |
| data[].outputs[].group\_id | string | 组图分组 ID（仅 `kling-image-v4` 且 `result_type=series` 时返回，用于标记同组图片）。 |

### 5. 响应示例

**成功（Kling-Image-v3 / o1 / v3-omni）：**

```json
{
    "code": 0,
    "data": {
        "created_at": 1790158890000,
        "task_status_msg": "",
        "updated_at": 1790158935886,
        "task_id": "1256342408-WandImage-7f7d37d4db5d4d308b5a0d9a8374d7fb",
        "task_info": {

        },
        "task_result": {
            "images": [
                {
                    "index": 0,
                    "url": "https://xxxxx.png"
                },
                {
                    "index": 1,
                    "url": "https://xxxxx.png"
                }
            ]
        },
        "task_status": "succeed"
    },
    "message": "SUCCEED",
    "request_id": "6efe9620-b3c6-472d-ac36-0322d3041e87",
    "tokenhub_usage": {
        "total_tokens": 40000
    }
}
```

**处理中（Kling-Image-v4 / v4-long）：**

```json
{
  "code": 0,
  "message": "SUCCEED",
  "request_id": "f2046163-ba72-460b-8cd0-5c4231619cb1",
  "data": [
    {
      "id": "251435731-kling_image_v4-30bfc3211f66479e8b14135fd1ed5bdc",
      "status": "processing",
      "message": "",
      "create_time": 1794984992000,
      "update_time": 1794985029408
    }
  ]
}
```

**成功（Kling-Image-v4，单图）：**

```json
{
  "code": 0,
  "message": "SUCCEED",
  "request_id": "b7416b83-b664-4e11-b572-7d237bc68438",
  "data": [
    {
      "id": "251435731-kling_image_v4-30bfc3211f66479e8b14135fd1ed5bdc",
      "status": "succeeded",
      "message": "",
      "create_time": 1794984992000,
      "update_time": 1794985136996,
      "outputs": [
        {
          "type": "image",
          "url": "https://aigc-output-image-file-xxx.cos.ap-guangzhou.myqcloud.com/xxx.png?q-sign-algorithm=sha1&..."
        }
      ]
    }
  ],
  "tokenhub_usage": {
    "total_tokens": 42000
  }
}
```

**成功（Kling-Image-v4-long，电商详情页长图）：**

```json
{
  "code": 0,
  "message": "SUCCEED",
  "request_id": "45f2d4e8-7773-48ee-ad19-c97510f0d9b7",
  "data": [
    {
      "id": "251435731-kling_image_v4_long-f965a34379a0448881077763957514f9",
      "status": "succeeded",
      "message": "",
      "create_time": 1794986041000,
      "update_time": 1794986350684,
      "outputs": [
        {
          "type": "image",
          "url": "https://aigc-output-image-file-xxx.cos.ap-guangzhou.myqcloud.com/xxx.png?q-sign-algorithm=sha1&..."
        }
      ]
    }
  ],
  "tokenhub_usage": {
    "total_tokens": 352000
  }
}
```

## 附录

### 错误码说明

| HTTP 状态码 | 业务码 | 业务码定义 | 业务码解释 | 建议解决方案 |
| --- | --- | --- | --- | --- |
| 200 | 0 | 请求成功 | - | - |
| 401 | 1000 | 身份验证失败 | 身份验证失败 | 检查 Authorization 是否正确 |
| 401 | 1001 | 身份验证失败 | Authorization 为空 | 在 Request Header 中填写正确的 Authorization |
| 401 | 1002 | 身份验证失败 | Authorization 值非法 | 在 Request Header 中填写正确的 Authorization |
| 401 | 1003 | 身份验证失败 | Authorization 未到有效时间 | 检查 token 的开始生效时间，等待生效或重新签发 |
| 401 | 1004 | 身份验证失败 | Authorization 已失效 | 检查 token 的有效期，重新签发 |
| 429 | 1100 | 账户异常 | 账户异常 | 检查账户配置信息 |
| 429 | 1101 | 账户异常 | 账户欠费 (后付费场景) | 进行账户充值，确保余额充足 |
| 429 | 1102 | 账户异常 | 资源包已用完/已过期（预付费场景） | 购买额外的资源包，或开通后付费服务（如有） |
| 403 | 1103 | 账户异常 | 请求的资源无权限，如接口/模型 | 检查账户权限 |
| 400 | 1200 | 请求参数非法 | 请求参数非法 | 检查请求参数是否正确 |
| 400 | 1201 | 请求参数非法 | 参数非法，如 key 写错或 value 非法 | 参考返回体中 message 字段的具体信息，修改请求参数 |
| 404 | 1202 | 请求参数非法 | 请求的 method 无效 | 查看接口文档，使用正确的 request method |
| 404 | 1203 | 请求参数非法 | 请求的资源不存在，如模型 | 参考返回体中 message 字段的具体信息，修改请求参数 |
| 400 | 1300 | 触发策略 | 触发平台策略 | 检查是否触发平台策略 |
| 400 | 1301 | 触发策略 | 触发平台的内容安全策略 | 检查输入内容，修改后重新发起请求 |
| 429 | 1302 | 触发策略 | API 请求过快，超过平台速率限制 | 降低请求频率、稍后重试，或联系客服增加限额 |
| 429 | 1303 | 触发策略 | 并发或 QPS 超出预付费资源包限制 | 降低请求频率、稍后重试，或联系客服增加限额 |
| 429 | 1304 | 触发策略 | 触发平台的 IP 白名单策略 | 联系客服 |
| 500 | 5000 | 内部错误 | 服务器内部错误 | 稍后重试，或联系客服 |
| 503 | 5001 | 内部错误 | 服务器暂时不可用，通常是在维护 | 稍后重试，或联系客服 |
| 504 | 5002 | 内部错误 | 服务器内部超时，通常是发生积压 | 稍后重试，或联系客服 |

### 图片素材通用约束

**Kling-Image-v3 / o1 / v3-omni**：参考图支持 .jpg / .jpeg / .png 格式，单张大小 ≤ 10MB，图片宽高尺寸不小于 300px，宽高比须在 1:2.5 ~ 2.5:1 之间。图片 URL 需确保可被访问；Base64 编码方式无须添加 `data:image/png;base64,` 前缀，直接传 Base64 字符串本身。多图参考（`image_list`）最多 10 张；参考主体数量与参考图片数量之和不得超过 10。

**Kling-Image-v4 / v4-long**：参考图支持 .jpg / .jpeg / .png 格式，单张大小 ≤ 30MB，宽高均不小于 300px，宽高比须在 2:5 ~ 5:2 之间；支持图片 URL 或 Base64 编码。`kling-image-v4` 图片与主体合计最多 10 个；`kling-image-v4-long` 电商详情页场景需 1~3 张商品参考图。

## 常见问题

#### **1. 文生图和图生图怎么区分？**

同一接口：`kling-image-v3` 传 `image`、`kling-image-o1` / `kling-image-v3-omni` 传 `image_list` 即为图生图，以图中内容为参考；都不传即为文生图（仅凭 prompt 生成）。以上三款模型均支持两种模式；`kling-image-v4` 在 `contents` 中加入 `refer_image` 即为图生图，仅含 `prompt` 即为文生图。

#### **2. 怎么生成组图？**

`kling-image-v3-omni` 与 `kling-image-v4` 支持组图：

`kling-image-v3-omni`：`result_type` 传 `series`，并用 `series_amount` 指定数量（2~9 或 auto，默认 4），此时 `n` 无效；结果从查询任务返回的 `task_result.series_images` 中获取。

`kling-image-v4`：`settings.result_type` 传 `series`，并用 `settings.series_amount` 指定数量（2~10 或 auto，默认 4），此时 `settings.n` 无效；结果从 `outputs[]` 中获取，同组图片共享 `group_id`。

`kling-image-v4-long` 不支持组图，固定输出一张完整长图。

#### **3. 负向提示词什么时候能用？**

仅 Kling-Image-v3 支持 `negative_prompt`，且只在文生图场景生效；图生图（传 `image`）时不支持。Kling-Image-o1 / Kling-Image-v3-omni 可将负向描述直接写在 `prompt` 中。

#### **4. 如何在提示词中引用参考图或主体？**

`kling-image-o1` / `kling-image-v3-omni`：在提示词中用 `<<<image_N>>>` 引用 `image_list` 中的第 N 张参考图。

`kling-image-v4` / `kling-image-v4-long`：在 `contents[]` 中给参考图 / 主体设置 `id`（同任务内唯一），在提示词中以 `@id` 引用。例如参考图 `id` 为 `dog` 时，提示词写「以 @dog 中的小狗为参考，……」。

#### **5. 电商详情页与网页设计的参考图要怎么传？**

电商详情页（`skill=ecommerce`）：必须通过 `refer_image` 传 1~3 张商品参考图，请勿使用 `style_refer_image` / `subject_refer_image`。

网页设计（`skill=webpage`）：通过 `style_refer_image`（参考视觉风格与排版）或 `subject_refer_image`（保留主体元素）传入，请勿使用 `refer_image`。

#### **6. length 参数什么时候生效？**

仅 `kling-image-v4-long` 且 `settings.skill=ecommerce` 时生效，控制电商详情页的功能页数量（short / medium / long）。网页设计场景（`skill=webpage`）设置无效。

#### **7. 生成结果图片链接会过期吗？**

会过期。生成结果为临时地址，有效期 12 小时，请在任务成功后及时下载转存。
