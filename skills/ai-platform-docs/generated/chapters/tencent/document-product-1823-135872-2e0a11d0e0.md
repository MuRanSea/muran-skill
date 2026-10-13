<!-- Official source: https://cloud.tencent.com/document/product/1823/135872 -->
<!-- Source SHA-256: 3c80c6f9e441378c90b92442ab28876c17525cac7b21c5f6b0952c7675fed85f -->

# OpenAI Chat Completions 协议字段说明

官方来源：https://cloud.tencent.com/document/product/1823/135872
最近更新时间：2026-09-15 10:55:40

## OpenAI Chat Completions API 使用

### 请求参数

**说明：**

本文为语言模型的公共调用指南，不同模型支持的参数范围可能存在差异，具体以对应模型的能力为准。完整字段定义与最新更新请参见 [OpenAI API 官方文档](https://developers.openai.com/api/reference/overview)。

#### 核心参数

| 参数 | 类型 | 必选 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `model` | string | 是 | - | 模型标识。平台默认服务 ID 与模型名称一致（如 `hy3`、`deepseek-v4-flash`）；自定义服务格式为 `ep-xxxxxxxx`。 |
| `messages` | array | 是 | - | 聊天上下文消息数组，详见 [Messages 参数](https://cloud.tencent.com/document/product/1823/135872#821d03e3-f2ee-4f69-b301-6a82b1d4e8e9)。 |
| `stream` | boolean | 否 | `false` | 是否启用流式输出（SSE）。 |
| `stream_options` | object | 否 | - | 流式选项，仅 `stream=true` 时生效。 |
| `stream_options.include_usage` | boolean | 否 | `false` | 流式最后一个 chunk 是否携带 `usage` 统计。平台始终请求 usage，此字段仅控制是否向客户端下发。 |

#### Messages 参数

`messages` 为对象数组，每个对象代表一条消息。消息顺序规则：`[system（可选）→ user → assistant → user → ...]`。

**System Message：**

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `role` | string | 是 | 固定为 `"system"` |
| `content` | string | 是 | 系统指令，用于设定模型行为和上下文。 |

**User Message：**

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `role` | string | 是 | 固定为 `"user"` |
| `content` | string 或 array | 是 | 纯文本为 string；多模态内容为 array（见下方 Content Part）。 |

**Content Part（** `content` **为 array 时）：**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `type` | string | 内容类型：`"text"` / `"image_url"` / `"video_url"` / `"file_url"` |
| `text` | string | `type="text"` 时的文本内容。 |
| `image_url` | object | `type="image_url"` 时的图片信息。 |
| `image_url.url` | string | 图片 HTTP(S) URL 或 `data:image/...;base64,...` 格式的 Data URL。 |
| `image_url.detail` | string | 图片分辨率策略：`"auto"` / `"low"` / `"high"`，默认 `"auto"`。 |
| `video_url` | object | `type="video_url"` 时的视频信息。 |
| `video_url.url` | string | 视频 HTTP(S) URL。 |
| `file_url` | object | `type="file_url"` 时的文件信息。 |
| `file_url.url` | string | 文件 HTTP URL（仅支持 HTTP 直链，不支持 Base64）。 |

**注意：**

部分模型不允许在同一条消息中混用 `file_url` 与 `image_url` / `video_url`，具体请参见对应模型的能力说明。

**Assistant Message：**

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `role` | string | 是 | 固定为 `"assistant"` |
| `content` | string | 否 | 模型回复文本（无 `tool_calls` 时必选）。 |
| `reasoning_content` | string | 否 | 思维链内容。思考模型响应中回传，多轮对话时需原样回填以保持上下文连续。 |
| `reasoning_details` | array | 否 | 思维链块数组，含签名，多轮对话时需原样回传以保持上下文连续。 |
| `tool_calls` | array | 否 | 工具调用列表，请参见 [工具调用参数](https://cloud.tencent.com/document/product/1823/135872#64364552-0fb7-45ab-8393-fe24761e1228)。 |
| `prefix` | boolean | 否 | 部分 DeepSeek 模型支持：`true` 时以本消息内容作为前缀续写，需配合对应的 Beta 端点使用。标准端点下该字段会被忽略，不影响请求结果。 |

**Tool Message：**

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `role` | string | 是 | 固定为 `"tool"` |
| `content` | string | 是 | 工具函数返回的结果内容（建议 JSON 字符串格式）。 |
| `tool_call_id` | string | 是 | 对应 `assistant.tool_calls[].id` 的值。 |
| `name` | string | 否 | 工具函数名称。 |

#### 生成控制参数

| 参数 | 类型 | 必选 | 默认值 | 取值范围 | 说明 |
| --- | --- | --- | --- | --- | --- |
| `temperature` | float | 否 | 1.0 | [0.0, 2.0] | 采样温度。值越高输出越随机，值越低越确定。一般只调此参数或 `top_p` 之一。 |
| `top_p` | float | 否 | 1.0 | (0.0, 1.0] | 核采样概率阈值。`top_p=0` 会被平台归一化为 `null`（等效默认值）。 |
| `max_tokens` | integer | 否 | 模型最大值 | ≥ 1 | 单次响应最大输出 Token 数。超出后 `finish_reason` 为 `"length"`。 |
| `max_completion_tokens` | integer | 否 | 模型最大值 | ≥ 1 | 最大输出 Token 数（OpenAI 新版字段，语义同 `max_tokens`）。两者传其一即可，平台优先使用 `max_completion_tokens`。 |
| `n` | integer | 否 | 1 | ≥ 1 | 候选回复数量。`n > 1` 时按总 Token 量计费。部分模型不支持；思考模式开启时 `n` 必须为 `1`，否则返回 400。 |
| `stop` | string 或 array | 否 | - | 最多 4 个 | 停止序列。遇到匹配序列立即停止生成。超过 4 个会被校验拒绝。 |
| `seed` | integer | 否 | - | 任意整数 | 随机种子，相同 seed 尽最大努力保证输出一致。 |
| `frequency_penalty` | float | 否 | 0 | [-2.0, 2.0] | 频率惩罚。正值降低已出现 Token 的重复概率。`0` 被归一化为 `null`。 |
| `presence_penalty` | float | 否 | 0 | [-2.0, 2.0] | 存在惩罚。正值鼓励生成新话题。`0` 被归一化为 `null`。 |
| `logprobs` | boolean | 否 | false | - | 是否返回输出 Token 的对数概率。 |
| `top_logprobs` | integer | 否 | 0 | [0, 20] | 每个位置返回概率最高的 N 个 Token，需 `logprobs=true`，否则校验失败。 |
| `reasoning_effort` | string | 否 | - | `"low"` / `"medium"` / `"high"` | 推理深度，适用于思考类模型。混元模型有内部映射转换。 |

**说明：**

**不支持的客户端参数**：`top_k`、`repetition_penalty`、`modalities`、`audio` 等字段在客户端请求中传入会被静默忽略。这些参数仅可通过平台配置注入。

#### 响应格式参数

| 参数 | 类型 | 必选 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `response_format` | object | 否 | `{"type":"text"}` | 响应格式控制。 |
| `response_format.type` | string | 是 | `"text"` | 格式类型：`"text"` / `"json_object"` / `"json_schema"`。 |
| `response_format.json_schema` | object | 条件 | - | `type="json_schema"` 时必选，定义输出 JSON 结构。 |
| `response_format.json_schema.name` | string | 是 | - | Schema 名称。 |
| `response_format.json_schema.schema` | object | 是 | - | JSON Schema 定义（遵循 JSON Schema 规范）。 |
| `response_format.json_schema.strict` | boolean | 否 | false | 是否强制严格匹配 Schema。 |

**注意：**

使用 `json_object` 时需在 `messages` 中明确要求模型输出 JSON 格式，否则部分模型行为不确定。

#### 工具调用参数

| 参数 | 类型 | 必选 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `tools` | array | 否 | - | 工具定义列表。 |
| `tools[].type` | string | 是 | - | 固定为 `"function"`。 |
| `tools[].function` | object | 是 | - | 函数定义。 |
| `tools[].function.name` | string | 是 | - | 工具函数名称（仅含字母、数字、下划线和短横线）。 |
| `tools[].function.description` | string | 否 | - | 工具函数描述，帮助模型判断何时调用。 |
| `tools[].function.parameters` | object | 否 | `{}` | 入参定义（JSON Schema object 格式）。 |
| `tool_choice` | string 或 object | 否 | `"auto"` | 工具调用策略，详见下方枚举。 |
| `parallel_tool_calls` | boolean | 否 | true | 是否允许并行调用多个工具。 |

`tool_choice` **取值：**

| 值 | 说明 |
| --- | --- |
| `"none"` | 不调用任何工具（混元下会同时清除 `tools` 字段）。 |
| `"auto"` | 模型自行决定是否调用工具（默认）。 |
| `"required"` | 强制模型调用至少一个工具。**注意**：思考模式开启时（`deepseek-v4-*` 等模型默认开启），该取值及指定函数对象会返回 400，需显式传入 `thinking: {"type": "disabled"}` 后使用。 |
| `{"type":"function","function":{"name":"xxx"}}` | 指定调用某个工具。 |

#### 思考模式参数

不同模型的默认思考开关不同，请参考各模型调用指南。

| 参数 | 类型 | 必选 | 默认值 | 说明 | 适用模型 |
| --- | --- | --- | --- | --- | --- |
| `thinking` | object | 否 | - | 思考模式控制（标准方式） | 思考类模型（如 混元、DeepSeek 等） |
| `thinking.type` | string | 是 | - | `"enabled"` 开启 / `"disabled"` 关闭 / `"adaptive"` 自适应。传入 `thinking` 对象时该字段必填，仅给出 `budget_tokens` 而缺少 `type` 会返回 400。 | 思考类模型（与 `thinking` 一致；具体可用取值因模型而异） |
| `thinking.budget_tokens` | integer | 否 | 8192（自动补） | 思考过程最大 Token 数。`type=enabled` 且未指定时自动补 8192。该值为期望上限而非硬性截断，部分模型的实际思考 Token 数可能超出设定值，请以响应 `usage.completion_tokens_details.reasoning_tokens` 为准。 | 思考类模型（部分模型仅作参考，不严格截断） |
| `enable_thinking` | boolean | 否 | - | 是否开启思考模式（简化开关）。作为 `thinking.type` 的替代写法，部分模型（如 Qwen、DeepSeek 系列）可用；推荐统一使用 `thinking.type`。 | 混元、DeepSeek 等部分模型 |
| `thinking_budget` | integer | 否 | - | 思考过程最大 Token 数（简化字段），需配合 `enable_thinking` 使用；推荐统一使用 `thinking.budget_tokens`。 | 混元、DeepSeek 等部分模型 |
| `interleaved_thinking` | boolean | 否 | - | 交错思维链模式：边推理边输出，适合流式展示。该字段为扩展能力，各模型的实际支持程度不同，不支持的模型会忽略该字段而不报错。 | 部分模型（具体以模型能力说明为准） |
| `reasoning_split` | boolean | 否 | - | 将推理内容与最终回复分段输出。该字段为扩展能力，不支持的模型会忽略该字段而不报错。 | 部分模型 |

**说明：**

思考模式下推理 Token 会计入 `completion_tokens`，建议适当调大 `max_tokens`。

`thinking.type` 的三个取值并非所有模型都支持。例如 `minimax-m3` 仅接受 `"adaptive"` 与 `"disabled"`，传入 `"enabled"` 会返回 400；另有部分模型即使传入 `"disabled"` 仍可能返回思维链内容。接入前建议针对所用模型实测确认。

#### 搜索增强参数

Chat Completions 接口通过 `web_search_options` 字段开启联网搜索（需先在控制台开通联网搜索资源包）。完整参数说明、支持模型与请求/响应示例，请参见 [联网搜索使用文档](https://cloud.tencent.com/document/product/1823/132358)。

#### 缓存参数

| 参数 | 类型 | 必选 | 默认值 | 说明 | 适用模型 |
| --- | --- | --- | --- | --- | --- |
| `prompt_cache_key` | string | 否 | - | 手动指定 Prompt 缓存 Key。相同 key 的请求可复用缓存，命中后按缓存价格计费，可通过响应 `usage.prompt_tokens_details.cached_tokens` 查看命中的 Token 数。 | 支持 Prompt Cache 的模型 |

#### 其他参数

| 参数 | 类型 | 必选 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `user` | string | 否 | - | 终端用户标识符，透传给模型服务，用于滥用检测和用量追踪。 |
| `user_id` | string 或 number | 否 | - | 平台业务层用户 ID（兼容数字类型，平台自动转为字符串）。仅用于平台内部用户标识，不会透传给模型服务；如需透传给模型服务，请使用 `user` 字段。 |
| `safety_identifier` | string | 否 | - | 安全标识符，供风控系统做用户级别的内容审核追踪。 |
| `extra_body` | object | 否 | - | 透传给模型服务的额外参数，平台不做解析。部分模型会将此字段合并到请求体顶层，其他模型服务忽略此字段。 |

### 返回参数

#### 顶层结构

```json
{
  "id": "chatcmpl-xxxxxxxxxxxxxxxxxxxxxxxx",
  "object": "chat.completion",
  "created": 1750924800,
  "model": "<your-model-name>",
  "choices": [...],
  "usage": {...},
  "search_info": null
}
```

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `id` | string | 请求唯一标识，格式 `chatcmpl-{uuid}`（平台生成，与模型服务返回的 ID 无关）。 |
| `object` | string | 对象类型，固定为 `"chat.completion"`。 |
| `created` | integer | 创建时间（Unix 时间戳，秒）。 |
| `model` | string | 用户请求时传入的原始模型名称（非模型服务实际模型名）。 |
| `choices` | array | 候选结果列表，元素数量等于请求中的 `n`。 |
| `usage` | object | Token 消耗统计，见「usage 对象」 |
| `search_info` | object 或 null | 联网搜索信息（混元/AISearch 路径时携带，其他场景为 `null`）。 |

#### choices 数组元素

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `index` | integer | 选项在 `choices` 数组中的索引，从 0 开始。 |
| `message` | object | 回复消息对象，见 [message 对象](https://cloud.tencent.com/document/product/1823/135872#message)。 |
| `finish_reason` | string | 生成结束原因，见下方枚举。 |
| `logprobs` | object 或 null | Token 概率信息（需请求时设置 `logprobs=true`）。 |

`finish_reason` **取值：**

| 值 | 说明 | 处理建议 |
| --- | --- | --- |
| `"stop"` | 正常结束（模型主动停止或匹配到 `stop` 序列）。 | 正常处理。 |
| `"length"` | 达到 `max_tokens` / `max_completion_tokens` 上限，输出被截断。 | 考虑增大 `max_tokens` 或分段生成。 |
| `"tool_calls"` | 模型需要调用工具。 | 执行工具，将结果作为 `tool` 消息继续请求。 |
| `"content_filter"` | 内容被安全策略过滤。 | 检查输入内容是否触发安全规则。 |

**message 对象**

**：**

| 字段 | 类型 | 说明 | 适用场景 |
| --- | --- | --- | --- |
| `role` | string | 固定为 `"assistant"` | 全部 |
| `content` | string 或 null | 回复文本内容。当存在 `tool_calls` 时可能为 `null` | 全部 |
| `reasoning_content` | string | 思维链/推理过程内容 | 思考类模型 |
| `reasoning_details` | array | 思维链块数组（含 `signature`） | 思考类模型 |
| `tool_calls` | array | 工具调用列表 | Function Calling |
| `refusal` | string 或 null | 拒绝回复的原因说明 | 内容安全过滤 |

`tool_calls` **数组元素：**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `id` | string | 工具调用唯一 ID，格式 `call_{uuid}`。 |
| `type` | string | 固定为 `"function"`。 |
| `function.name` | string | 被调用的函数名称。 |
| `function.arguments` | string | 函数参数（JSON 字符串格式，使用时需先 `JSON.parse()`）。 |

#### usage 对象

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `prompt_tokens` | integer | 输入 Token 数（含 system、messages、tools 定义等） |
| `completion_tokens` | integer | 输出 Token 数（含思维链推理 Token） |
| `total_tokens` | integer | 总 Token 数 |
| `cache_read_tokens` | integer | 命中 Prompt Cache 读取的 Token 数（部分模型，可减少计费） |
| `cache_write_tokens` | integer | 写入 Prompt Cache 的 Token 数（部分模型） |
| `prompt_tokens_details` | object | 输入 Token 细分（部分模型） |
| `prompt_tokens_details.cached_tokens` | integer | 命中缓存的 Token 数 |
| `completion_tokens_details` | object | 输出 Token 细分（部分模型） |
| `completion_tokens_details.reasoning_tokens` | integer | 思维链消耗的 Token 数（OpenAI 兼容路径） |
| `completion_tokens_details.audio_tokens` | integer | 音频输出消耗的 Token 数 |

**注意：**

`total_tokens = prompt_tokens + completion_tokens`。`completion_tokens` 已包含思维链 Token，`reasoning_tokens` 是其中的细分。

#### search\_info（联网搜索时）

```json
{
  "search_info": {
    "search_results": [
      {
        "index": 1,
        "url": "https://example.com/article",
        "name": "文章标题",
        "snippet": "文章摘要",
        "icon": "https://...",
        "site": "来源站点",
        "published_time": "2026-06-26"
      }
    ]
  }
}
```

### 流式响应

流式输出使用 Server-Sent Events（SSE）协议：

HTTP 状态码：`200`

`Content-Type: text/event-stream`

`X-Accel-Buffering: no`

每个事件格式：`data: {json}\\n\\n`

结束标志：`data: [DONE]\\n\\n`

**Chunk 结构：**

```json
{
  "id": "chatcmpl-xxxxxxxxxxxxxxxxxxxxxxxx",
  "object": "chat.completion.chunk",
  "created": 1750924800,
  "model": "<your-model-name>",
  "choices": [
    {
      "index": 0,
      "delta": {
        "role": "assistant",
        "content": "增量文本",
        "reasoning_content": "增量思维链"
      },
      "finish_reason": null
    }
  ],
  "usage": null
}
```

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `object` | string | 固定为 `"chat.completion.chunk"`。 |
| `choices[].delta` | object | 增量内容。 |
| `choices[].delta.role` | string | 仅在第一个 chunk 中出现，值为 `"assistant"`。 |
| `choices[].delta.content` | string | 增量文本片段，累积拼接为完整回复。 |
| `choices[].delta.reasoning_content` | string | 增量思维链片段（思维链模式下，先于 `content` 输出）。 |
| `choices[].delta.reasoning_details` | array | 增量思维链块（含 `signature`，流结束后需完整收集并在多轮中回传）。 |
| `choices[].delta.tool_calls` | array | 增量工具调用（含 `index` 字段标识数组位置）。 |
| `choices[].delta.search_results` | array | 联网搜索结果增量（部分模型在流式中推送）。 |
| `choices[].finish_reason` | string 或 null | 生成中为 `null`，结束时为终止原因。 |
| `usage` | object 或 null | 仅在 `include_usage=true` 时，最后一个正式 chunk 携带。 |

**流式 tool\_calls 增量格式：**首次出现时包含 `id`、`type`、`function.name`；后续 chunk 仅追加 `function.arguments` 片段，客户端需按 `index` 将多个 chunk 的 `arguments` 拼接为完整 JSON 字符串。`arguments` 为增量片段，示例中 `{"ci` 为首帧截断值，属正常现象，非格式错误。以下为前两帧的示例：

**第一帧**（首次出现，含 `id`、`type`、`function.name`）：

```json
{
  "delta": {
    "tool_calls": [
      {
        "index": 0,
        "id": "call_xxx",
        "type": "function",
        "function": {
          "name": "get_weather",
          "arguments": "{\\"ci"
        }
      }
    ]
  }
}
```

第一帧返回 `{"ci`，第二帧返回 `ty":"Beijing"}`，两段拼接后得到完整参数 `{"city":"Beijing"}`。

**第二帧**（后续帧，仅追加 `function.arguments` 片段）：

```json
{
  "delta": {
    "tool_calls": [
      {
        "index": 0,
        "function": {
          "arguments": "ty\\":\\"Beijing\\"}"
        }
      }
    ]
  }
}
```

**流式错误处理：**

| 场景 | 行为 |
| --- | --- |
| 首包前失败（HTTP 200 写入前） | 返回标准 JSON 错误体，可正常解析错误码。若有 Fallback Provider 会自动降级重试。 |
| 200 响应头已发送后的错误 | 平台在 SSE 流中插入 `data: {"error":{"type":"...","message":"..."}}\\n\\n` 错误帧，随后发送 `data: [DONE]\\n\\n` 结束流。客户端需检测 `delta` 中是否含 `error` 字段。 |

### 错误响应

调用出错时，HTTP 状态码为非 2xx，响应体为 JSON 格式，并同时返回中英文错误描述。基本结构如下：

```json
{
  "error": {
    "message": "<英文错误描述>",
    "message_zh": "<中文错误描述>",
    "code": "<业务错误码>",
    "type": "<错误类型>",
    "request_id": "<请求唯一标识>"
  }
}
```

完整的错误响应结构、全部业务错误码速查表、各类错误的响应示例与排查建议，请参见 [API 错误码说明](https://cloud.tencent.com/document/product/1823/131595)。

**说明：**

请求链路早期被拦截的错误（如鉴权失败、参数非法），`type` 统一为 `gateway_error`。

限流（HTTP `429`）场景下，`code` 可能以整型数字返回，并携带响应头 `Retry-After`（单位：秒）。客户端解析 `error.code` 时应同时兼容字符串与数字类型。

流式请求若在响应头（HTTP 200）发送后才发生错误，网关会在 SSE 流中插入 `data: {"error":{...}}` 错误帧，随后发送 `data: [DONE]` 结束流。客户端需检测增量内容中是否包含 `error` 字段。

### 示例代码

#### 示例：基础对话

cURL

Python

Node.js

Java

Go

```bash
curl -X POST "https://tokenhub.tencentmaas.com/v1/chat/completions" \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{
    "model": "<your-model-name>",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "你好，请介绍一下自己"}
    ],
    "temperature": 0.7,
    "max_tokens": 1024
  }'
```

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

response = client.chat.completions.create(
    model="<your-model-name>",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "你好，请介绍一下自己"},
    ],
    temperature=0.7,
    max_tokens=1024,
)
print(response.choices[0].message.content)
```

```javascript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: 'YOUR_API_KEY',
  baseURL: 'https://tokenhub.tencentmaas.com/v1',
});

const response = await client.chat.completions.create({
  model: '<your-model-name>',
  messages: [
    { role: 'system', content: 'You are a helpful assistant.' },
    { role: 'user', content: '你好，请介绍一下自己' },
  ],
  temperature: 0.7,
  max_tokens: 1024,
});
console.log(response.choices[0].message.content);
```

```java
import okhttp3.*;
import com.google.gson.Gson;
import java.util.*;

public class BasicChat {
    public static void main(String[] args) throws Exception {
        Map<String, Object> body = new HashMap<>();
        body.put("model", "<your-model-name>");
        body.put("messages", List.of(
            Map.of("role", "system", "content", "You are a helpful assistant."),
            Map.of("role", "user", "content", "你好，请介绍一下自己")
        ));
        body.put("temperature", 0.7);
        body.put("max_tokens", 1024);

        Request request = new Request.Builder()
            .url("https://tokenhub.tencentmaas.com/v1/chat/completions")
            .header("Authorization", "Bearer YOUR_API_KEY")
            .post(RequestBody.create(new Gson().toJson(body), MediaType.parse("application/json")))
            .build();

        try (Response response = new OkHttpClient().newCall(request).execute()) {
            System.out.println(response.body().string());
        }
    }
}
```

```go
package main

import (
    "bytes"
    "encoding/json"
    "fmt"
    "io"
    "net/http"
)

func main() {
    body, _ := json.Marshal(map[string]interface{}{
        "model": "<your-model-name>",
        "messages": []map[string]string{
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "你好，请介绍一下自己"},
        },
        "temperature": 0.7,
        "max_tokens":  1024,
    })

    req, _ := http.NewRequest("POST",
        "https://tokenhub.tencentmaas.com/v1/chat/completions",
        bytes.NewBuffer(body))
    req.Header.Set("Authorization", "Bearer YOUR_API_KEY")
    req.Header.Set("Content-Type", "application/json")

    resp, err := http.DefaultClient.Do(req)
    if err != nil {
        panic(err)
    }
    defer resp.Body.Close()

    data, _ := io.ReadAll(resp.Body)
    fmt.Println(string(data))
}
```

#### 示例：Function Calling（工具调用）

cURL

Python

Node.js

Java

Go

```bash
curl -X POST "https://tokenhub.tencentmaas.com/v1/chat/completions" \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{
    "model": "<your-model-name>",
    "messages": [
      {"role": "user", "content": "北京今天天气怎么样？"}
    ],
    "tools": [
      {
        "type": "function",
        "function": {
          "name": "get_weather",
          "description": "获取指定城市的天气信息",
          "parameters": {
            "type": "object",
            "properties": {
              "city": {"type": "string", "description": "城市名称"}
            },
            "required": ["city"]
          }
        }
      }
    ],
    "tool_choice": "auto"
  }'
```

```python
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY", base_url="https://tokenhub.tencentmaas.com/v1")

response = client.chat.completions.create(
    model="<your-model-name>",
    messages=[{"role": "user", "content": "北京今天天气怎么样？"}],
    tools=[
        {
            "type": "function",
            "function": {
                "name": "get_weather",
                "description": "获取指定城市的天气信息",
                "parameters": {
                    "type": "object",
                    "properties": {"city": {"type": "string", "description": "城市名称"}},
                    "required": ["city"],
                },
            },
        }
    ],
    tool_choice="auto",
)
print(response.choices[0].message)
```

```javascript
import OpenAI from 'openai';

const client = new OpenAI({ apiKey: 'YOUR_API_KEY', baseURL: 'https://tokenhub.tencentmaas.com/v1' });

const response = await client.chat.completions.create({
  model: '<your-model-name>',
  messages: [{ role: 'user', content: '北京今天天气怎么样？' }],
  tools: [
    {
      type: 'function',
      function: {
        name: 'get_weather',
        description: '获取指定城市的天气信息',
        parameters: {
          type: 'object',
          properties: { city: { type: 'string', description: '城市名称' } },
          required: ['city'],
        },
      },
    },
  ],
  tool_choice: 'auto',
});
console.log(response.choices[0].message);
```

```java
import okhttp3.*;

public class FunctionCalling {
    public static void main(String[] args) throws Exception {
        String body = """
        {
          "model": "<your-model-name>",
          "messages": [
            {"role": "user", "content": "北京今天天气怎么样？"}
          ],
          "tools": [
            {
              "type": "function",
              "function": {
                "name": "get_weather",
                "description": "获取指定城市的天气信息",
                "parameters": {
                  "type": "object",
                  "properties": {
                    "city": {"type": "string", "description": "城市名称"}
                  },
                  "required": ["city"]
                }
              }
            }
          ],
          "tool_choice": "auto"
        }
        """;

        Request request = new Request.Builder()
            .url("https://tokenhub.tencentmaas.com/v1/chat/completions")
            .header("Authorization", "Bearer YOUR_API_KEY")
            .post(RequestBody.create(body, MediaType.parse("application/json")))
            .build();

        try (Response response = new OkHttpClient().newCall(request).execute()) {
            System.out.println(response.body().string());
        }
    }
}
```

```go
package main

import (
    "fmt"
    "io"
    "net/http"
    "strings"
)

func main() {
    body := `{
  "model": "<your-model-name>",
  "messages": [
    {"role": "user", "content": "北京今天天气怎么样？"}
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "get_weather",
        "description": "获取指定城市的天气信息",
        "parameters": {
          "type": "object",
          "properties": {
            "city": {"type": "string", "description": "城市名称"}
          },
          "required": ["city"]
        }
      }
    }
  ],
  "tool_choice": "auto"
}`

    req, _ := http.NewRequest("POST",
        "https://tokenhub.tencentmaas.com/v1/chat/completions",
        strings.NewReader(body))
    req.Header.Set("Authorization", "Bearer YOUR_API_KEY")
    req.Header.Set("Content-Type", "application/json")

    resp, err := http.DefaultClient.Do(req)
    if err != nil {
        panic(err)
    }
    defer resp.Body.Close()

    data, _ := io.ReadAll(resp.Body)
    fmt.Println(string(data))
}
```

#### 示例：流式 + 思考模式

cURL

Python

Node.js

Java

Go

```bash
curl -X POST "https://tokenhub.tencentmaas.com/v1/chat/completions" \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{
    "model": "<your-model-name>",
    "messages": [
      {"role": "user", "content": "证明根号2是无理数"}
    ],
    "stream": true,
    "stream_options": {"include_usage": true},
    "thinking": {"type": "enabled", "budget_tokens": 8000},
    "max_tokens": 4096
  }'
```

```python
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY", base_url="https://tokenhub.tencentmaas.com/v1")

stream = client.chat.completions.create(
    model="<your-model-name>",
    messages=[{"role": "user", "content": "证明根号2是无理数"}],
    stream=True,
    stream_options={"include_usage": True},
    extra_body={"thinking": {"type": "enabled", "budget_tokens": 8000}},
    max_tokens=4096,
)
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

```javascript
import OpenAI from 'openai';

const client = new OpenAI({ apiKey: 'YOUR_API_KEY', baseURL: 'https://tokenhub.tencentmaas.com/v1' });

const stream = await client.chat.completions.create({
  model: '<your-model-name>',
  messages: [{ role: 'user', content: '证明根号2是无理数' }],
  stream: true,
  stream_options: { include_usage: true },
  // thinking 为平台扩展参数
  thinking: { type: 'enabled', budget_tokens: 8000 },
  max_tokens: 4096,
});
for await (const chunk of stream) {
  const delta = chunk.choices[0]?.delta?.content;
  if (delta) process.stdout.write(delta);
}
```

```java
import okhttp3.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class StreamThinking {
    public static void main(String[] args) throws Exception {
        String body = """
        {
          "model": "<your-model-name>",
          "messages": [
            {"role": "user", "content": "证明根号2是无理数"}
          ],
          "stream": true,
          "stream_options": {"include_usage": true},
          "thinking": {"type": "enabled", "budget_tokens": 8000},
          "max_tokens": 4096
        }
        """;

        Request request = new Request.Builder()
            .url("https://tokenhub.tencentmaas.com/v1/chat/completions")
            .header("Authorization", "Bearer YOUR_API_KEY")
            .post(RequestBody.create(body, MediaType.parse("application/json")))
            .build();

        try (Response response = new OkHttpClient().newCall(request).execute();
             BufferedReader reader = new BufferedReader(
                 new InputStreamReader(response.body().byteStream()))) {
            String line;
            while ((line = reader.readLine()) != null) {
                if (!line.isEmpty()) System.out.println(line);
            }
        }
    }
}
```

```go
package main

import (
    "bufio"
    "fmt"
    "net/http"
    "strings"
)

func main() {
    body := `{
  "model": "<your-model-name>",
  "messages": [
    {"role": "user", "content": "证明根号2是无理数"}
  ],
  "stream": true,
  "stream_options": {"include_usage": true},
  "thinking": {"type": "enabled", "budget_tokens": 8000},
  "max_tokens": 4096
}`

    req, _ := http.NewRequest("POST",
        "https://tokenhub.tencentmaas.com/v1/chat/completions",
        strings.NewReader(body))
    req.Header.Set("Authorization", "Bearer YOUR_API_KEY")
    req.Header.Set("Content-Type", "application/json")

    resp, err := http.DefaultClient.Do(req)
    if err != nil {
        panic(err)
    }
    defer resp.Body.Close()

    scanner := bufio.NewScanner(resp.Body)
    for scanner.Scan() {
        if line := scanner.Text(); line != "" {
            fmt.Println(line)
        }
    }
}
```

#### 示例：多模态（图片理解）

cURL

Python

Node.js

Java

Go

```bash
curl -X POST "https://tokenhub.tencentmaas.com/v1/chat/completions" \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{
    "model": "<your-model-name>",
    "messages": [
      {
        "role": "user",
        "content": [
          {"type": "text", "text": "请描述这张图片的内容"},
          {"type": "image_url", "image_url": {"url": "https://example.com/image.jpg"}}
        ]
      }
    ]
  }'
```

```python
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY", base_url="https://tokenhub.tencentmaas.com/v1")

response = client.chat.completions.create(
    model="<your-model-name>",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "请描述这张图片的内容"},
                {"type": "image_url", "image_url": {"url": "https://example.com/image.jpg"}},
            ],
        }
    ],
)
print(response.choices[0].message.content)
```

```javascript
import OpenAI from 'openai';

const client = new OpenAI({ apiKey: 'YOUR_API_KEY', baseURL: 'https://tokenhub.tencentmaas.com/v1' });

const response = await client.chat.completions.create({
  model: '<your-model-name>',
  messages: [
    {
      role: 'user',
      content: [
        { type: 'text', text: '请描述这张图片的内容' },
        { type: 'image_url', image_url: { url: 'https://example.com/image.jpg' } },
      ],
    },
  ],
});
console.log(response.choices[0].message.content);
```

```java
import okhttp3.*;

public class Multimodal {
    public static void main(String[] args) throws Exception {
        String body = """
        {
          "model": "<your-model-name>",
          "messages": [
            {
              "role": "user",
              "content": [
                {"type": "text", "text": "请描述这张图片的内容"},
                {"type": "image_url", "image_url": {"url": "https://example.com/image.jpg"}}
              ]
            }
          ]
        }
        """;

        Request request = new Request.Builder()
            .url("https://tokenhub.tencentmaas.com/v1/chat/completions")
            .header("Authorization", "Bearer YOUR_API_KEY")
            .post(RequestBody.create(body, MediaType.parse("application/json")))
            .build();

        try (Response response = new OkHttpClient().newCall(request).execute()) {
            System.out.println(response.body().string());
        }
    }
}
```

```go
package main

import (
    "fmt"
    "io"
    "net/http"
    "strings"
)

func main() {
    body := `{
  "model": "<your-model-name>",
  "messages": [
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "请描述这张图片的内容"},
        {"type": "image_url", "image_url": {"url": "https://example.com/image.jpg"}}
      ]
    }
  ]
}`

    req, _ := http.NewRequest("POST",
        "https://tokenhub.tencentmaas.com/v1/chat/completions",
        strings.NewReader(body))
    req.Header.Set("Authorization", "Bearer YOUR_API_KEY")
    req.Header.Set("Content-Type", "application/json")

    resp, err := http.DefaultClient.Do(req)
    if err != nil {
        panic(err)
    }
    defer resp.Body.Close()

    data, _ := io.ReadAll(resp.Body)
    fmt.Println(string(data))
}
```

#### 示例：联网搜索

联网搜索通过 `web_search_options` 字段开启，需先在控制台开通联网搜索资源包。完整的请求参数、支持模型与响应示例，请参见 [联网搜索使用文档](https://cloud.tencent.com/document/product/1823/132358)。

#### 示例：多轮思维链对话（携带 signature）

cURL

Python

Node.js

Java

Go

```bash
curl -X POST "https://tokenhub.tencentmaas.com/v1/chat/completions" \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{
    "model": "<your-model-name>",
    "messages": [
      {"role": "user", "content": "分析这个算法的时间复杂度"},
      {
        "role": "assistant",
        "content": "该算法的时间复杂度是 O(n log n)。",
        "reasoning_details": [
          {
            "type": "thinking",
            "content": "让我分析一下：外层循环 n 次...",
            "signature": "EqoBCkgIARgCIkD..."
          }
        ]
      },
      {"role": "user", "content": "如何将其优化为 O(n)？"}
    ],
    "thinking": {"type": "enabled", "budget_tokens": 5000}
  }'
```

```python
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY", base_url="https://tokenhub.tencentmaas.com/v1")

response = client.chat.completions.create(
    model="<your-model-name>",
    messages=[
        {"role": "user", "content": "分析这个算法的时间复杂度"},
        {
            "role": "assistant",
            "content": "该算法的时间复杂度是 O(n log n)。",
            "reasoning_details": [
                {
                    "type": "thinking",
                    "content": "让我分析一下：外层循环 n 次...",
                    "signature": "EqoBCkgIARgCIkD...",
                }
            ],
        },
        {"role": "user", "content": "如何将其优化为 O(n)？"},
    ],
    extra_body={"thinking": {"type": "enabled", "budget_tokens": 5000}},
)
print(response.choices[0].message.content)
```

```javascript
import OpenAI from 'openai';

const client = new OpenAI({ apiKey: 'YOUR_API_KEY', baseURL: 'https://tokenhub.tencentmaas.com/v1' });

const response = await client.chat.completions.create({
  model: '<your-model-name>',
  messages: [
    { role: 'user', content: '分析这个算法的时间复杂度' },
    {
      role: 'assistant',
      content: '该算法的时间复杂度是 O(n log n)。',
      reasoning_details: [
        {
          type: 'thinking',
          content: '让我分析一下：外层循环 n 次...',
          signature: 'EqoBCkgIARgCIkD...',
        },
      ],
    },
    { role: 'user', content: '如何将其优化为 O(n)？' },
  ],
  // thinking 为平台扩展参数
  thinking: { type: 'enabled', budget_tokens: 5000 },
});
console.log(response.choices[0].message.content);
```

```java
import okhttp3.*;

public class MultiTurnThinking {
    public static void main(String[] args) throws Exception {
        String body = """
        {
          "model": "<your-model-name>",
          "messages": [
            {"role": "user", "content": "分析这个算法的时间复杂度"},
            {
              "role": "assistant",
              "content": "该算法的时间复杂度是 O(n log n)。",
              "reasoning_details": [
                {
                  "type": "thinking",
                  "content": "让我分析一下：外层循环 n 次...",
                  "signature": "EqoBCkgIARgCIkD..."
                }
              ]
            },
            {"role": "user", "content": "如何将其优化为 O(n)？"}
          ],
          "thinking": {"type": "enabled", "budget_tokens": 5000}
        }
        """;

        Request request = new Request.Builder()
            .url("https://tokenhub.tencentmaas.com/v1/chat/completions")
            .header("Authorization", "Bearer YOUR_API_KEY")
            .post(RequestBody.create(body, MediaType.parse("application/json")))
            .build();

        try (Response response = new OkHttpClient().newCall(request).execute()) {
            System.out.println(response.body().string());
        }
    }
}
```

```go
package main

import (
    "fmt"
    "io"
    "net/http"
    "strings"
)

func main() {
    body := `{
  "model": "<your-model-name>",
  "messages": [
    {"role": "user", "content": "分析这个算法的时间复杂度"},
    {
      "role": "assistant",
      "content": "该算法的时间复杂度是 O(n log n)。",
      "reasoning_details": [
        {
          "type": "thinking",
          "content": "让我分析一下：外层循环 n 次...",
          "signature": "EqoBCkgIARgCIkD..."
        }
      ]
    },
    {"role": "user", "content": "如何将其优化为 O(n)？"}
  ],
  "thinking": {"type": "enabled", "budget_tokens": 5000}
}`

    req, _ := http.NewRequest("POST",
        "https://tokenhub.tencentmaas.com/v1/chat/completions",
        strings.NewReader(body))
    req.Header.Set("Authorization", "Bearer YOUR_API_KEY")
    req.Header.Set("Content-Type", "application/json")

    resp, err := http.DefaultClient.Do(req)
    if err != nil {
        panic(err)
    }
    defer resp.Body.Close()

    data, _ := io.ReadAll(resp.Body)
    fmt.Println(string(data))
}
```
