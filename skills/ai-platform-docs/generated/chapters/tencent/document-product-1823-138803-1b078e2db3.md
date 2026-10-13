<!-- Official source: https://cloud.tencent.com/document/product/1823/138803 -->
<!-- Source SHA-256: 8de23939a6281a4665345902d7e11174ca6d7b95f96676b7c5dc2f11a4c43b77 -->

# Kling 生图调用指南

官方来源：https://cloud.tencent.com/document/product/1823/138803
最近更新时间：2026-09-24 21:20:30

## 概述

可灵（Kling）是快手推出的视觉生成模型系列。本文介绍如何通过 TokenHub 调用可灵图片生成模型 Kling-Image-v3（`kling-image-v3`）、Kling-Image-o1（`kling-image-o1`）、Kling-Image-v3-omni（`kling-image-v3-omni`），支持**文生图、图生图**：以参考图结合文本提示词生成图片，也可仅凭文本进行文生图；o1 与 Omni 支持多图参考，Omni 支持系列组图生成与 4K 超高清直出。

### 前提条件

已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号并开通 TokenHub 服务。

已在 [TokenHub 控制台](https://console.cloud.tencent.com/tokenhub/apikey) 获取 API Key。

在 [控制台-在线推理-视觉模型](https://console.cloud.tencent.com/tokenhub/inference?regionId=1&serviceType=VISION) 处开启对应模型的后付费。

**说明：**

下文所有示例中的 YOUR\_API\_KEY 均需替换为您自己的 API Key，鉴权方式为请求头 Authorization: Bearer YOUR\_API\_KEY。

### 调用流程

图片生成为耗时任务，接口采用**异步调用**模式，统一分两步：

1. **提交任务**：调用图片生成接口，成功返回任务 `task_id`。

2. **轮询结果**：携带任务 `task_id` 调用 查询任务 接口（建议每 3~5 秒一次），直至 `task_status = succeed`，从 `task_result.images` 中获取图片地址。

### 模型列表

| 模型名称 | model 参数值 | 支持能力 | 提示词上限 | 分辨率 |
| --- | --- | --- | --- | --- |
| Kling-Image-v3 | `kling-image-v3` | 文生图 / 图生图（单图参考） | 2500 字符 | 1K / 2K |
| Kling-Image-o1 | `kling-image-o1` | 文生图 / 图生图（多图参考） | 2500 字符 | 1K / 2K |
| Kling-Image-v3-omni | `kling-image-v3-omni` | 文生图 / 图生图（多图参考）/ 系列组图 | 2500 字符 | 1K / 2K / 4K |

**说明：**

三款模型均支持 16:9、9:16、1:1、4:3、3:4、3:2、2:3、21:9 共 8 种画面纵横比；`kling-image-o1` 与 `kling-image-v3-omni` 额外支持 auto（根据传入内容智能判断画面比例）。

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

## 查询任务

### 1. 接口描述

查询图片生成任务的状态与结果。提交任务返回 `task_id` 后，通过本接口轮询获取结果（建议每 3~5 秒一次），任务成功后从 `task_result.images` 获取单图结果；`result_type` 为 series 的组图任务从 `task_result.series_images` 获取。

**接口：** `GET https://tokenhub.tencentmaas.com/v1/wand/kling-image/tasks/{task_id}`

### 2. 输入参数

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| task\_id | 是 | string | 任务 ID（路径参数），即提交任务时返回的 `task_id`。 |

### 3. 请求示例

```bash
curl -X GET 'https://tokenhub.tencentmaas.com/v1/wand/kling-image/tasks/YOUR_TASK_ID' \\
  -H 'Authorization: Bearer YOUR_API_KEY'
```

### 4. 输出参数

<table><colgroup><col/><col/><col/></colgroup><tbody><tr><td><div>字段</div></td><td><div>类型</div></td><td><div>说明</div></td></tr><tr><td><div>code</div></td><td><div>integer</div></td><td><div>错误码。</div></td></tr><tr><td><div>message</div></td><td><div>string</div></td><td><div>错误信息。</div></td></tr><tr><td><div>request_id</div></td><td><div>string</div></td><td><div>请求 ID，系统生成，用于跟踪请求、排查问题。</div></td></tr><tr><td colspan="1" rowspan="1"><div>tokenhub_usage</div></td><td colspan="1" rowspan="1"><div>object</div></td><td colspan="1" rowspan="1"><div>用量消耗。</div></td></tr><tr><td colspan="1" rowspan="1"><div>tokenhub_usage.total_tokens</div></td><td colspan="1" rowspan="1"><div>integer</div></td><td colspan="1" rowspan="1"><div>本次任务消耗的 token 数，用于计费/对账。</div></td></tr><tr><td><div>data.task_id</div></td><td><div>string</div></td><td><div>任务 ID。</div></td></tr><tr><td><div>data.task_status</div></td><td><div>string</div></td><td><div>任务状态，枚举值：submitted（已提交）、processing（处理中）、succeed（成功）、failed（失败）。</div></td></tr><tr><td><div>data.task_status_msg</div></td><td><div>string</div></td><td><div>任务状态信息，任务失败时展示失败原因。</div></td></tr><tr><td colspan="1" rowspan="1"><div>data.created_at</div></td><td colspan="1" rowspan="1"><div>integer</div></td><td colspan="1" rowspan="1"><div>任务创建时间，Unix 时间戳，单位 ms。</div></td></tr><tr><td colspan="1" rowspan="1"><div>data.updated_at</div></td><td colspan="1" rowspan="1"><div>integer</div></td><td colspan="1" rowspan="1"><div>任务更新时间，Unix 时间戳，单位 ms。</div></td></tr><tr><td><div>data.task_result.images[].index</div></td><td><div>integer</div></td><td><div>图片编号，0 ~ 9。</div></td></tr><tr><td><div>data.task_result.images[].url</div></td><td><div>string</div></td><td><div>生成图片的 URL。</div></td></tr><tr><td><div>data.task_result.images[].watermark_url</div></td><td><div>string</div></td><td><div>含水印图片的下载 URL（<code>watermark_info.enabled</code> 为 true 时返回）。</div></td></tr><tr><td><div>data.task_result.series_images[].index</div></td><td><div>integer</div></td><td><div>组图序号（组图任务返回）。</div></td></tr><tr><td><div>data.task_result.series_images[].url</div></td><td><div>string</div></td><td><div>组图图片的 URL（组图任务返回）。</div></td></tr></tbody></table>

### 5. 响应示例

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

参考图支持 .jpg / .jpeg / .png 格式，单张大小 ≤ 10MB，图片宽高尺寸不小于 300px，宽高比须在 1:2.5 ~ 2.5:1 之间。图片 URL 需确保可被访问；Base64 编码方式无须添加 `data:image/png;base64,` 前缀，直接传 Base64 字符串本身。多图参考（`image_list`）最多 10 张；参考主体数量与参考图片数量之和不得超过 10。

## 常见问题

#### **1. 文生图和图生图怎么区分？**

同一接口：`kling-image-v3` 传 `image`、`kling-image-o1` / `kling-image-v3-omni` 传 `image_list` 即为图生图，以图中内容为参考；都不传即为文生图（仅凭 prompt 生成）。三款模型均支持两种模式。

#### **2. 怎么生成组图？**

仅 `kling-image-v3-omni` 支持：`result_type` 传 `series`，并用 `series_amount` 指定数量（2~9 或 auto，默认 4）。此时 `n` 参数无效，结果从查询任务返回的 `task_result.series_images` 中获取。

#### **3. 负向提示词什么时候能用？**

仅 Kling-Image-v3 支持 `negative_prompt`，且只在文生图场景生效；图生图（传 `image`）时不支持。Kling-Image-o1 / Kling-Image-v3-omni 可将负向描述直接写在 `prompt` 中。

#### **4. 生成结果图片链接会过期吗？**

会过期。生成结果为临时地址，有效期 12 小时，请在任务成功后及时下载转存。
