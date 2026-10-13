<!-- Official source: https://cloud.tencent.com/document/product/1823/135745 -->
<!-- Source SHA-256: 0cf4374ca35e10c26b3fde2cf7538ab16914b3a22dd43ae8dfc1af273929f19d -->

# Hy 生图调用指南

官方来源：https://cloud.tencent.com/document/product/1823/135745
最近更新时间：2026-09-24 21:20:30

## 概述

混元生图是腾讯混元推出的图像生成模型系列。本文介绍如何通过 TokenHub 调用混元图片生成模型 Hy-Image-3.0（`hy-image-v3`）与 Hy-Image-3.5-preview（`hy-image-v3.5-preview`）：

**Hy-Image-3.0**：凭文本提示词同步生成图片，支持参考生图、自定义尺寸、生成种子、prompt 自动改写与图片水印脚注。

**Hy-Image-3.5-preview**：以 OpenAI Chat 风格的 messages 协议提交单轮或多轮生图/编辑请求，同步返回图片结果，支持多模态输入（文本 + 参考图）、多轮编辑、思维链改写、外部搜索增强、自定义尺寸/面积/种子、图片水印脚注等能力，最高支持 4096×4096（4K）输出。

**说明：**

两个模型均为**同步调用**：一次请求直接返回生成结果，无需提交任务与轮询。Hy-Image-3.5-preview 的服务端会在内部完成 SSE 流式推理并等到终态，最后把原厂最终图像帧原样返回给调用方。

### 前提条件

已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号并开通 TokenHub 服务。

已在 [TokenHub 控制台](https://console.cloud.tencent.com/tokenhub/apikey) 获取 API Key。

在 [控制台-在线推理-视觉模型](https://console.cloud.tencent.com/tokenhub/inference?regionId=1&serviceType=VISION) 处开启对应模型的后付费。

**说明：**

下文所有示例中的 YOUR\_API\_KEY 均需替换为您自己的 API Key，鉴权方式为请求头 Authorization: Bearer YOUR\_API\_KEY。

### 模型列表

<table><colgroup><col/><col/><col/><col/><col/><col/></colgroup><tbody><tr><td><div>模型名称</div></td><td><div>model 参数值</div></td><td><div>支持能力</div></td><td><div>输入上限</div></td><td><div>尺寸约束</div></td><td><div>简要说明</div></td></tr><tr><td><div>Hy-Image-3.5-preview</div></td><td><div><code>hy-image-v3.5-preview</code></div></td><td><div>文生图 / 参考生图 / 多轮编辑（同步）</div></td><td><div>100k tokens</div></td><td><div>宽高 ∈ [256, 8192]，面积 ≤ 16777216（4K，4096×4096）</div></td><td><div>Chat/Messages 协议，支持多模态输入、多轮编辑上下文、外部搜索增强、按面积档位自动决定尺寸，最高支持 4K 输出。</div></td></tr><tr><td colspan="1" rowspan="1"><div>Hy-Image-3.0</div></td><td colspan="1" rowspan="1"><div><code>hy-image-v3</code></div></td><td colspan="1" rowspan="1"><div>文生图 / 参考生图（同步）</div></td><td colspan="1" rowspan="1"><div>8192 字符</div></td><td colspan="1" rowspan="1"><div>宽高 ∈ [512, 2048]，面积 ≤ 1024×1024</div></td><td colspan="1" rowspan="1"><div>支持 prompt 自动改写、37 组预设尺寸、自定义水印脚注。</div></td></tr></tbody></table>

## Hy-Image-3.5-preview 图片生成（文生图 / 图生图 / 多轮编辑）

### 1. 接口描述

以 Chat/Messages 协议输入一轮或多轮上下文（文本 + 可选参考图），同步生成图片。未传 `size` 时，模型会结合 prompt 语义与 `generate_max_pixels` 面积档位自主决定最终宽高；传入 `size` 时强制按指定尺寸出图，最高支持 4096×4096（4K）。

**接口：** `POST https://tokenhub.tencentmaas.com/v1/wand/hunyuan-image/v35-generation`

### 2. 输入参数

#### 2.1 顶层参数

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| model | 是 | string | 模型 ID。取值：`hy-image-v3.5-preview` |
| messages | 是 | array[object] | 多轮会话内容，时间从旧到新排列。  服务端会取数组中最后一个 `role=user` 的消息作为本轮生图指令，其余对象作为历史上下文一并透传（用于多轮编辑）。元素结构见 2.2 messages 元素结构。 |
| size | 否 | string | 生成尺寸，格式 `${宽}x${高}`。  约束：  1. 宽、高均为正整数，取值范围 [256, 8192]。  2. 宽 × 高（面积）不超过 16777216，即最高支持 4096×4096（4K）。  不传或传空串时由模型基于 prompt 语义与 `generate_max_pixels` 自主决定尺寸；传入具体值时强制按指定尺寸出图。需要 4K 输出时，直接传 `"size": "4096x4096"` 即可。 |
| seed | 否 | integer | 生成种子，int64 类型，范围 [0, 2^63-1]；为 0 或不传时服务端随机分配。负值将被拒绝。 |
| generate\_max\_pixels | 否 | integer | 指定生成图片的目标面积（像素数），仅在未传 `size` 时生效。  支持 3 个枚举档位：`1048576`（1K，1024×1024）、`2359296`（1.5K，默认）、`4194304`（2K）；传入非枚举中间值时按最近面积归档。  注：该参数最高档位为 2K，需要更高分辨率请改用 `size` 指定。 |
| resize\_max\_pixels | 否 | integer | 输入参考图面积上限（像素数）。原图面积 ≤ 阈值时原样透传；> 阈值时按比例等比缩放到 ≈ 阈值后再送入模型，用于控制大图（4K/6K）带来的上下文 token 消耗。  不传默认 `1048576`（1024×1024）。 |
| session | 否 | string | 会话 ID，用于推理服务一致性哈希调度（同 session 的多轮请求会落到同一推理实例，提升 KV-cache 命中率）。多轮对话建议整条会话保持同一 session 值。 |
| footnote | 否 | string | 业务自定义水印内容，最长 16 字符（按 utf8.RuneCount 计算，不区分中英文），生成在图片右下角。 |
| use\_search\_tool | 否 | object | 外部搜索增强开关，结构固定为 `{"value": true}` 或 `{"value": false}`。当前默认关闭。 |

#### 2.2 messages 元素结构

`messages[n]` 每个元素结构如下：

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| role | 是 | string | 角色，支持 `user` / `assistant` / `tool`。  `tool` 角色仅在「把上一轮生图结果回灌作为下一轮上下文」时出现。 |
| content | 否 | array[object] | 该轮的具体内容，元素结构见 2.3 content 元素结构。  `assistant` 仅触发工具调用、不发文本时可省略。 |
| reasoning | 否 | string | 仅 `role=assistant` 多轮回灌时使用，透传上一轮响应中的思维链原文。 |
| tool\_calls | 否 | array | 仅 `role=assistant` 多轮回灌时使用；元素结构为标准 OpenAI tool\_call：`{id, type:"function", function:{name, arguments}}`，其中 `arguments` 为 JSON 字符串。 |
| tool\_call\_id | 否 | string | 仅 `role=tool` 多轮回灌时使用；须与上一条 `assistant.tool_calls[i].id` 字符级一致。 |

#### 2.3 content 元素结构

`messages[n].content[m]` 每个元素结构如下：

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| type | 是 | string | 内容类型，`text` 或 `image_url`。 |
| text | 否 | string | 当 `type=text` 时使用，表示具体文本。 |
| image\_url | 否 | object | 当 `type=image_url` 时使用，结构为 `{"url": "..."}`。  支持 http(s) 公网 URL 或 `data:image/...;base64,...` 形态；单图大小 ≤ 20MB，图片总数量 ≤ 20 张（超过时服务端按轮次由远到近自动截断）。 |
| is\_generate | 否 | bool | 仅 `role=tool` 回灌生图 content 时填 `true`，标记「这是上一轮 generate 工具产出的图」。其它场景不传。 |

### 3. 请求示例

**单轮文生图（4K 输出）**

```bash
# 文生图
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/hunyuan-image/v35-generation' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "hy-image-v3.5-preview",
  "size": "4096x4096",
  "messages": [
    {
      "role": "user",
      "content": [
        { "type": "text", "text": "画一只在沙滩上奔跑的金毛犬，傍晚的暖色光" }
      ]
    }
  ]
}'
```

**单轮参考生图（文本 + 参考图）**

```bash
# 参考生图
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/hunyuan-image/v35-generation' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "hy-image-v3.5-preview",
  "session": "demo-session-001",
  "messages": [
    {
      "role": "user",
      "content": [
        { "type": "text", "text": "参考这张图的风格，画一只猫" },
        { "type": "image_url", "image_url": { "url": "https://your-domain/dog.png" } }
      ]
    }
  ]
}'
```

**多轮编辑**（把上一轮响应中的 `assembled_history` 三条消息原样拼入）

```json
{
  "model": "hy-image-v3.5-preview",
  "session": "demo-session-001",
  "messages": [
    { "role": "user", "content": [
        { "type": "text", "text": "参考这张图的风格，画一只猫" },
        { "type": "image_url", "image_url": { "url": "https://your-domain/dog.png" } }
    ]},
    {
      "role": "assistant",
      "content":   [{ "type": "text", "text": "为了按要求创建图片，我将使用生成工具。" }],
      "reasoning": "用户希望参考狗的风格画一只猫...",
      "tool_calls": [{
        "id": "generate@call_0",
        "type": "function",
        "function": { "name": "generate", "arguments": "{\\"recaption\\":\\"a cat in similar style...\\"}" }
      }]
    },
    {
      "role": "tool",
      "tool_call_id": "generate@call_0",
      "content": [
        { "type": "image_url", "image_url": { "url": "http://hunyuan-image-result-tob-1258344703.cos.ap-guangzhou.myqcloud.com/xxx/cat.png" } }
      ]
    },
    {
      "role": "assistant",
      "content": [{ "type": "text", "text": "你请求的图片已完成。" }]
    },
    { "role": "user", "content": [
        { "type": "text", "text": "把猫换成布偶猫品种，背景换成壁炉旁" }
    ]}
  ]
}
```

### 4. 输出参数

| 参数名 | 类型 | 描述 |
| --- | --- | --- |
| id | string | 此次请求的 traceID，整流唯一。 |
| object | string | 固定 `image.chat.completion.chunk`。 |
| created | integer | Unix 秒级时间戳。 |
| model | string | 原厂实际服务返回的内部版本标识（形如 `HY-Image-3.5-preview-4090-Tob-vX.Y`），会随上游发布变化，不等同于请求体中传入的 `hy-image-v3.5-preview`，仅供参考，不建议客户端取此字段做业务分支判断。 |
| round | integer | 本帧所属 LLM 轮次，从 0 起算。 |
| choices | list | 固定长度 1。 |
| choices[0].delta | object | 主图载体，结构为 `{"type":"image", "image":{"url":"...", "width":..., "height":..., "source":"generate", "tool_call_id":"generate@call_0"}}`。  `choices[0].delta.image.url` **即为本次生图的最终交付 URL，客户端应优先读取此字段。** |
| choices[0].finish\_reason | string | null | 成功终态帧下往往为 `null`（原厂将图片作为最后一帧 delta 下发后直接关流，不额外发送完结帧）；仅在内容安全拦截 / 业务错误时会为 `error` 等非空值。  业务侧判断是否成功建议依据 `choices[0].delta.image.url` 是否存在，而非 `finish_reason`。 |
| usage.total\_tokens | integer | 本次任务消耗的 token 总量（原厂依据，v3.5 目前不拆分 prompt / completion）。 |
| tokenhub\_usage.total\_tokens | integer | TokenHub 网关侧计费/对账使用的 token 消耗，一般与 `usage.total_tokens` 保持一致。 |
| request\_id | string | 唯一请求标识，用于排查问题。 |
| assembled\_history | list | 服务端拼好的「下一轮回灌消息序列」，结构与请求体 `messages` 元素完全一致，典型为 3 条对象：  ① `role=assistant`（含 `reasoning` + `tool_calls`，描述本轮思考与工具调用）  ② `role=tool`（含工具产出图的中间 URL，`tool_call_id` 与 ① 一致）  ③ `role=assistant`（只含收尾文本，例如「你请求的图片已完成。」）  **多轮编辑时直接把该数组原样追加到下一轮** `messages` **即可。** |
| error | object | 仅失败终态帧才带，OpenAI 风格 `{type, code, message, request_id}`。 |

**说明：**

**两个图片 URL 的区别：**

`choices[0].delta.image.url`：**最终交付图 URL**（位于 `aigc-output-image-file-*.cos.ap-guangzhou.myqcloud.com`），已含水印/后处理，推荐业务优先读取此字段作为最终图片。

`assembled_history[].content[].image_url.url`（role=tool）：**中间产物 URL**（位于 `hunyuan-image-result-tob-*.cos.ap-guangzhou.myqcloud.com`），其作用是为下一轮多轮编辑提供可回灌的历史上下文。多轮编辑时必须拼入。

两者均为临时签名 URL，默认有效期 12 小时，请及时下载转存。

### 5. 响应示例

成功响应：

```json
{
  "id": "1374200352-WandImage-085edfe2367d4a688f68e813af3665a5",
  "object": "image.chat.completion.chunk",
  "created": 1789720599,
  "model": "HY-Image-3.5-preview-4090-Tob-v1.2",
  "round": 0,
  "choices": [
    {
      "index": 0,
      "delta": {
        "type": "image",
        "image": {
          "url": "https://aigc-output-image-file-1326893053.cos.ap-guangzhou.myqcloud.com/xxx/main.png?...",
          "width": 4096,
          "height": 4096,
          "source": "generate",
          "tool_call_id": "generate@call_0"
        }
      },
      "finish_reason": null
    }
  ],
  "usage": { "total_tokens": 20000 },
  "tokenhub_usage": { "total_tokens": 20000 },
  "request_id": "a1c00d07-041b-4daa-bae0-b7eabf2bc33a",
  "assembled_history": [
    {
      "role": "assistant",
      "content": [{ "type": "text", "text": "为了按要求创建图片，我将使用生成工具。" }],
      "reasoning": "用户指令是\\"跳舞\\"，需要将其具象化为具体的视觉表现...",
      "tool_calls": [
        {
          "id": "generate@call_0",
          "type": "function",
          "function": {
            "name": "generate",
            "arguments": "{\\"recaption\\":\\"...\\",\\"image_width\\":\\"855\\",\\"image_height\\":\\"1226\\",\\"source_image_indices_list\\":\\"[\\\\\\"rdnd\\\\\\"]\\"}"
          }
        }
      ]
    },
    {
      "role": "tool",
      "tool_call_id": "generate@call_0",
      "content": [
        {
          "type": "image_url",
          "image_url": {
            "url": "http://hunyuan-image-result-tob-1258344703.cos.ap-guangzhou.myqcloud.com/text2image2/strategy/upload/xxx.png?..."
          }
        }
      ]
    },
    {
      "role": "assistant",
      "content": [{ "type": "text", "text": "你请求的图片已完成。" }]
    }
  ]
}
```

失败响应（例如内容审核拦截）：

```json
{
  "id": "abc123",
  "object": "image.chat.completion.chunk",
  "created": 1785125530,
  "model": "HY-Image-3.5-preview-4090-Tob-v1.2",
  "round": 0,
  "choices": [
    { "index": 0, "delta": {}, "finish_reason": "error" }
  ],
  "error": {
    "type": "invalid_request_error",
    "code": "content_filter",
    "message": "input moderation rejected",
    "request_id": "xxxxxxxx"
  }
}
```

返回的 url 为临时地址，有效期 12 小时。由于该地址带有鉴权校验，直接通过浏览器地址栏访问可能被拒绝。建议通过以下方式下载：

```bash
curl -o generated_image.png 'https://aigc-output-image-file-1326893053.cos.ap-guangzhou.myqcloud.com/xxx/main.png?...'
```

或在代码中使用 HTTP 客户端下载保存到本地存储。

### 6. 错误码

| HTTP 状态码 | 说明 | 处理建议 |
| --- | --- | --- |
| 400 | 请求格式有误 | 检查请求体字段类型/取值（如 size 约束、messages 结构、模型名）。 |
| 401 | 鉴权不通过 | 检查 API\_KEY 是否有效、Authorization 是否为 Bearer 格式。 |
| 422 | 输入、输出审核不通过（内容安全拦截） | 输入或输出触发内容安全审核，需调整 prompt 或业务策略。 |
| 429 | 请求并发数超过限额 | 触发并发上限，建议退避重试并控制调用并发。 |
| 500 | 内部错误 | 服务端异常，可重试；持续失败请联系技术支持并附 request\_id。 |

## Hy-Image-3.0 图片生成

### 1. 接口描述

输入文本提示词，同步生成图片。未传 `size` 时，若 prompt 中指定了尺寸或比例，模型从 37 个预设组合中选择最接近的一个；若未指定则自动预测，详情请参见 [附录：Hy-Image-3.0 预设尺寸列表](https://cloud.tencent.com/document/product/1823/135745#hy-image-3.0-.E9.A2.84.E8.AE.BE.E5.B0.BA.E5.AF.B8.E5.88.97.E8.A1.A8)。

**接口：** `POST https://tokenhub.tencentmaas.com/v1/wand/hunyuan-image/v3-generation`

### 2. 输入参数

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| model | 是 | string | 模型 ID。取值：`hy-image-v3` |
| prompt | 是 | string | 生成图片使用的文本，长度 ≤ 8192 字符。 |
| images | 否 | array[string] | 参考图片，0~3 张。支持图片 URL 或 Base64。  格式 png / jpeg / jpg，单图大小 ≤ 10MB。 |
| size | 否 | string | 生成尺寸，格式 `${宽}x${高}`。  约束：  1. 宽、高均在 [512, 2048] 像素范围内；  2. 宽高乘积（图像面积）不超过 1024×1024 像素。  不传时模型从 37 个预设组合中选择/预测，详情请参见 [附录：Hy-Image-3.0 预设尺寸列表](https://cloud.tencent.com/document/product/1823/135745#hy-image-3.0-.E9.A2.84.E8.AE.BE.E5.B0.BA.E5.AF.B8.E5.88.97.E8.A1.A8)。 |
| seed | 否 | integer | 生成种子，范围 [1, 4294967295]，仅当生成图片数为 1 时生效；不传或为 0 时默认随机。 |
| footnote | 否 | string | 业务自定义水印内容，限制 16 个字符长度（不区分中英文），生成在图片右下角。 |
| revise | 否 | boolean | 是否对 prompt 改写。 |

### 3. 请求示例

```bash
# 文生图
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/hunyuan-image/v3-generation' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "hy-image-v3",
  "prompt": "一只橙色小猫在窗台上看向镜头",
  "size": "1024x1024"
}'
```

### 4. 输出参数

| 参数名 | 类型 | 描述 |
| --- | --- | --- |
| id | string | 此次请求的 id。 |
| created | integer | Unix 时间戳。 |
| data | list | 返回的图片生成内容数组。 |
| data[n].url | string | 生成的图片地址，为临时地址，有效期 12 小时，请及时下载转存。 |
| data[n].revised\_prompt | string | 改写后的 prompt（开启 revise 时返回）。 |
| request\_id | string | 唯一请求标识，用于排查问题。 |
| tokenhub\_usage | object | 用量消耗。 |
| tokenhub\_usage.total\_tokens | integer | 本次任务消耗的 token 数，用于计费/对账。 |

### 5. 响应示例

```json
{
  "id": "4-WandImage-a786becfdc80433b8cff4aa344c8fd3d",
  "created": 1785125529,
  "data": [
    {
      "url": "https://aigc-image.cos.myqcloud.com/xxx/result.png",
      "revised_prompt": "一只橙色小猫坐在洒满阳光的窗台上，转身看向镜头，毛发细节清晰，背景虚化"
    }
  ],
  "request_id": "3aec3299-06ad-4654-8b45-c57b823a15d2",
  "tokenhub_usage": {
    "total_tokens": 1024
  }
}
```

返回的 url 为临时地址，有效期 12 小时。由于该地址带有鉴权校验，直接通过浏览器地址栏访问可能被拒绝。建议通过以下方式下载：

```bash
curl -o generated_image.png 'https://aigc-image.cos.myqcloud.com/xxx/result.png'
```

或在代码中使用 HTTP 客户端下载保存到本地存储。

### 6. 错误码

| HTTP 状态码 | 说明 | 处理建议 |
| --- | --- | --- |
| 400 | 请求格式有误 | 检查请求体字段类型/取值（如 size 约束、prompt 长度、模型名）。 |
| 401 | 鉴权不通过 | 检查 API\_KEY 是否有效、Authorization 是否为 Bearer 格式。 |
| 422 | 输入、输出审核不通过（内容安全拦截） | 输入或输出触发内容安全审核，需调整 prompt 或业务策略。 |
| 429 | 请求并发数超过限额 | 触发并发上限，建议退避重试并控制调用并发。 |
| 500 | 内部错误 | 服务端异常，可重试；持续失败请联系技术支持并附 request\_id。 |

## 附录

### Hy-Image-3.0 预设尺寸列表

`size` 不传时模型从以下 37 个组合中选择/预测；传入 `size` 时需满足约束（宽高 ∈ [512, 2048]，乘积 ≤ 1024×1024）。格式均为「宽 x 高」：

| 2048 x 512 | 1984 x 512 | 1920 x 512 | 1856 x 512 |
| --- | --- | --- | --- |
| 1792 x 512 | 1728 x 512 | 1664 x 512 | 1600 x 512 |
| 1536 x 512 | 1472 x 576 | 1408 x 640 | 1344 x 704 |
| 1280 x 768 | 1216 x 832 | 1152 x 896 | 1088 x 960 |
| 1024 x 1024 | 960 x 1088 | 896 x 1152 | 832 x 1216 |
| 768 x 1280 | 704 x 1344 | 640 x 1408 | 576 x 1472 |
| 512 x 1536 | 512 x 1600 | 512 x 1664 | 512 x 1728 |
| 512 x 1792 | 512 x 1856 | 512 x 1920 | 512 x 1984 |
| 512 x 2048 | 768 x 1024 | 720 x 1280 | 1024 x 768 |
| 1280 x 720 | - | - | - |

### 参考图输入约束

| 模型 | 支持格式 | 单图大小 | 数量 |
| --- | --- | --- | --- |
| Hy-Image-3.0 | png / jpeg / jpg，支持图片 URL 或 Base64 | ≤ 10MB | 0~3 张 |
| Hy-Image-3.5-preview | png / jpeg / jpg，支持图片 URL 或 Base64 | ≤ 20MB | ≤ 20 张 |

建议使用 CDN 直链且不带鉴权，若为内网/带鉴权域名，需联系 TokenHub 侧加入白名单。

## 常见问题

#### **1. 两个模型怎么选？**

Hy-Image-3.0 为经典文生图接口，请求体简单（prompt + size），适合单轮批量出图、对接成本敏感的场景；Hy-Image-3.5-preview 采用 Chat/Messages 协议，支持多图输入、多轮编辑上下文与思维链改写，文字渲染、真实感与编辑一致性更强，最高支持 4K 输出，适合海报、UI 设计、商品图编辑等专业视觉生产场景。

#### **2. 怎么生成 4K 图片？**

仅 Hy-Image-3.5-preview 支持。直接传 `"size": "4096x4096"` 即可，宽高取值范围 [256, 8192]、面积上限 16777216，其它 4K 级比例（如 `"5461x3072"`）只要满足面积约束同样支持。注意 `generate_max_pixels` 最高档位为 2K（`4194304`），要出 4K 必须走 `size` 参数。

#### **3. size / generate\_max\_pixels 怎么组合使用？（Hy-Image-3.5-preview）**

**只传** `size`：强制按精确宽高出图，覆盖模型自主决定，4K 场景用这种方式。

`size` **+** `generate_max_pixels`：最终宽高由内部逻辑综合计算，尽量贴近 `size` 的宽高比例与 `generate_max_pixels` 的面积档位，取模型效果最佳的宽高值。

**只传** `generate_max_pixels`：默认 1:1 比例，面积按档位归档到 1K / 1.5K / 2K 之一。

**都不传**：由模型基于 prompt 语义自主决定（默认走 1.5K 档）。

#### **4. Hy-Image-3.0 的 size 参数怎么传？**

格式为 `${宽}x${高}`（例如 `1024x1024`），宽高均需在 [512, 2048] 范围内且面积不超过 1024×1024。建议直接使用 附录：Hy-Image-3.0 预设尺寸列表 中的组合；不传时可在 prompt 中描述比例（例如「横版 16:9」），模型会自动选择最接近的预设尺寸。

#### **5. seed 什么时候生效？如何复现？**

Hy-Image-3.0：范围 [1, 4294967295]，仅在生成图片数为 1 时生效，不传或传 0 时使用随机种子。

Hy-Image-3.5-preview：范围 [0, 2^63-1]，为 0 或不传时服务端随机分配，负值将被拒绝。需要复现同一结果时，请固定 seed + prompt + size。

#### **6. revise（prompt 改写）要关闭吗？（Hy-Image-3.0）**

开启改写时，模型会自动改写优化 prompt 以提升生图效果，改写约耗时 11 秒。仅当您已自行实现 prompt 改写逻辑时才建议关闭，否则对生图效果影响较大。

#### **7. 多轮编辑要怎么拼上下文？（Hy-Image-3.5-preview）**

第 N+1 轮请求的 `messages` = 第 N 轮的 `messages`（含首条 user） + 第 N 轮响应中的 `assembled_history`（典型为 assistant + tool + assistant 三条） + 本轮新的 user 消息。无需自己聚合 SSE 增量、无需组装多层嵌套 JSON，服务端已经在 `assembled_history` 里拼好了直接可用的对象。可参考前文「多轮编辑」请求示例中 assistant / tool / assistant 三条消息的拼接形态。

#### **8. 生成结果图片链接会过期吗？**

会过期。两个模型的生成结果均为临时地址，有效期 12 小时，请在生成成功后及时下载转存：Hy-Image-3.0 取 `data[n].url`；Hy-Image-3.5-preview 取 `choices[0].delta.image.url`（最终交付图，业务侧使用），如需保留历史上下文用于下一轮编辑，可同时保存 `assembled_history[].content[].image_url.url`（中间产物）。所有 URL 均为临时签名，切勿长期依赖。
