<!-- Official source: https://cloud.tencent.com/document/product/1823/135874 -->
<!-- Source SHA-256: 8c752b1eedc03fbb17bed766a073d57c33bc93698cc58c0678dd78e7a2d54acb -->

# Anthropic Message 协议字段说明

官方来源：https://cloud.tencent.com/document/product/1823/135874
最近更新时间：2026-10-12 12:50:00

## Anthropic Messages API 使用

### 请求参数详解

#### 基础参数

| 参数 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `model` | string | 是 | 要使用的模型名称，如 `hy3`。也支持 Claude 系列及其他 Anthropic 兼容模型名。需要图像输入时，请选择支持视觉能力的模型（如 `glm-5.3-flash`）。 |
| `messages` | array | 是 | 对话消息列表，按时间顺序排列，含完整上下文。平台不做会话管理，多轮对话需由客户端完整携带历史。详情请参见 [Message 对象详解](https://cloud.tencent.com/document/product/1823/135874#95b79d85-4224-46db-8e25-9bfd13146f7b)。 |
| `system` | string 或 array | 否 | 系统提示词。不在 `messages` 内，通过顶层 `system` 字段单独传入。这是与 OpenAI Chat 协议的关键区别。 |
| `max_tokens` | integer | 是 | 模型单次输出的最大 Token 数上限。不同模型有各自上限；思维链消耗的 Token 计入此限制，因此开启 thinking 时须大于 `budget_tokens`。达到上限时 `stop_reason` 为 `"max_tokens"`。 |
| `stream` | boolean | 否 | 是否启用流式响应（默认 `false`）。`true` 时以 SSE 格式逐事件返回。 |

`system` 支持两种形式：

```plaintext
// 字符串
"system": "你是一个友好的助手"

// 内容块数组（可携带 cache_control）
"system": [
  { "type": "text", "text": "你是一个友好的助手" },
  { "type": "text", "text": "<长文档>", "cache_control": { "type": "ephemeral" } }
]
```

**说明：**

**关于** `max_tokens`：Anthropic 协议中该字段为必填。部分模型对缺失或非法 `max_tokens` 会做宽松兜底处理，但请始终按协议标准显式传入该字段，不要依赖兜底行为。

#### 生成控制参数

| 参数 | 类型 | 范围 | 说明 |
| --- | --- | --- | --- |
| `temperature` | float | [0, 1] | 采样温度。注意 Anthropic 范围为 [0, 1]，与 OpenAI 的 [0, 2] 不同。 |
| `top_p` | float | (0, 1] | 核采样。一般 `temperature` 与 `top_p` 只调其中一个。 |
| `top_k` | integer | - | 只从概率最高的前 K 个 token 中采样。Anthropic 特有参数，OpenAI Chat 协议无此字段。 |
| `stop_sequences` | string[] | - | 自定义停止序列。命中任一序列时立即停止，`stop_reason` 为 `"stop_sequence"`，命中的序列回写在响应的 `stop_sequence` 字段。 |

**说明：**

**关于 thinking 与 temperature**：开启 thinking 时，部分模型要求 `temperature` 固定为 `1`；也有模型会容忍 `temperature != 1`。建议 thinking 场景使用默认值或 `1`，是否强校验按模型而定。
**关于** `stop_sequences`：部分模型能稳定回写 `stop_reason=stop_sequence` 与命中的 `stop_sequence`，部分模型不保证回写。依赖精确停止语义的业务应针对目标模型验证。

#### 工具调用

Anthropic 的工具定义结构与 OpenAI 不同：字段直接平铺，参数字段名为 `input_schema`（OpenAI 为 `function.parameters`）。

```json
{
  "name": "get_weather",
  "description": "查询指定城市的天气信息",
  "input_schema": {
    "type": "object",
    "properties": {
      "location": { "type": "string", "description": "城市名称" }
    },
    "required": ["location"]
  }
}
```

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| `name` | string | 是 | 工具名称。 |
| `description` | string | 否 | 工具用途描述，帮助模型判断何时调用。 |
| `input_schema` | object | 是 | 参数定义，遵循 JSON Schema 格式。 |
| `type` | string | 否 | 普通工具留空；内置工具填类型名（如 `web_search_20250305`）。 |
| `max_uses` | integer | 否 | 内置工具单次会话最大调用次数。 |
| `cache_control` | object | 否 | 工具定义级缓存标记。 |

`tool_choice`**（Anthropic 用对象形式）：**

| Anthropic tool\_choice | 等价 OpenAI | 说明 |
| --- | --- | --- |
| `{"type":"auto"}` | `"auto"` | 默认，模型自行决定 |
| `{"type":"any"}` | `"required"` | 强制调用任一工具 |
| `{"type":"none"}` | `"none"` | 禁止调用工具 |
| `{"type":"tool","name":"x"}` | `{"type":"function","function":{"name":"x"}}` | 强制调用指定工具 |

可选子字段 `disable_parallel_tool_use`（boolean）：设为 `true` 时禁止单次响应并行调用多个工具。

**注意：**

**与 thinking 的组合限制**：开启或默认进入 thinking 模式时，部分模型不支持强制工具调用（`tool_choice:any` 与 `tool_choice:tool`），通常仅支持 `auto` / `none` 与 thinking 共用。如需强制工具调用，建议先显式传 `thinking: {"type":"disabled"}` 再使用 `any` 或指定工具。各模型的具体差异见 [各模型字段兼容情况](https://cloud.tencent.com/document/product/1823/130079)。

#### 思维链（Extended Thinking）

启用扩展思维链，让模型在生成最终回复前先进行内部推理，适用于复杂逻辑、数学、代码等任务。

```json
{
  "thinking": {
    "type": "enabled",
    "budget_tokens": 8000
  }
}
```

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| `type` | string | 是 | `"enabled"` 开启 / `"disabled"` 关闭 / `"adaptive"` 自适应。 |
| `budget_tokens` | integer | 视情况 | `enabled` 时建议提供，思维链 token 预算（建议 1024~32000），须小于 `max_tokens`。 |
| `display` | string | 否 | 思维过程展示方式（部分模型支持）。 |

**不同 type 的字段要求**：`enabled` 携带 `budget_tokens`（及可选 `display`）；`disabled` 仅 `type`；`adaptive` 携带 `type`（及可选 `display`），由模型自适应分配预算。

**说明：**

**模型差异**：部分推理模型在不传 `thinking` 时也会默认返回 thinking block；部分模型会容忍缺失 `budget_tokens`、`budget_tokens >= max_tokens` 或 `temperature != 1` 等非严格约束。这类属于模型/平台兼容行为，不应当作所有模型的通用契约。如不希望返回思考内容，建议显式传 `thinking: {"type":"disabled"}`。
**与 OpenAI 兼容参数的关系**：部分厂商文档会使用 `enable_thinking`、`reasoning_effort` 等字段描述思考能力。在 Anthropic Messages 协议中，对应表达为 `thinking.type`、`output_config.effort`，以及多轮历史中原样回传 assistant 的 `thinking` / `redacted_thinking` 内容块；不要在 Messages 请求体中直接混用 `enable_thinking`。

**交错思维链（Interleaved Thinking）**：部分模型支持在生成回复过程中穿插思维内容。混元等模型通过请求头 `Hunyuan-Beta` 开启，平台会将该头透传给模型服务。该请求头属扩展能力，不支持的模型会忽略该头而不报错；是否实际生效需结合所用模型的能力说明确认。

#### 输出配置

`output_config`（object）：控制输出努力程度与结构化格式。

```json
{
  "output_config": {
    "effort": "high",
    "format": {
      "type": "json_schema",
      "schema": { "type": "object", "properties": { "answer": { "type": "string" } } }
    }
  }
}
```

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `effort` | string | 输出努力程度：`low` / `medium` / `high` / `xhigh` / `max`。 |
| `format.type` | string | 结构化输出类型（如 `json_schema`）。 |
| `format.schema` | object | JSON Schema 定义。 |

**说明：**

该字段为扩展能力，各厂商支持情况不一：`output_config.effort` 多数模型可接收；`output_config.format.type=json_schema` 的结构化输出仅部分模型能稳定按 schema 生成 JSON，部分模型返回 200 但 JSON 不完全符合 schema，也有模型返回 400。不要将 `json_schema` 当作所有模型的通用能力，使用前请针对目标模型验证。

#### 缓存（Prompt Caching）

通过 `cache_control` 标记可缓存内容，命中后大幅降低重复 prompt 的 `input_tokens` 计费。支持三个层级标记：

| 层级 | 标记位置 | 说明 |
| --- | --- | --- |
| 工具级 | `tools[n].cache_control` | 缓存工具定义 |
| 系统级 | `system[n].cache_control` | 缓存 system 内容块 |
| 消息/内容块级 | `messages[n].content[m].cache_control` | 缓存历史消息或内容块 |

`cache_control` 对象结构：

```json
{ "type": "ephemeral" }              // 默认 5 分钟 TTL
{ "type": "ephemeral", "ttl": "1h" } // 1 小时 TTL
```

缓存命中情况通过响应 `usage` 中的 `cache_creation_input_tokens`、`cache_read_input_tokens` 返回。若模型不支持缓存，相关 token 统计为 0。

**说明：**

**能力说明**：多数模型可观察到部分 cache token，但顶层 `cache_control`、文档块级 cache、`ttl:"1h"` 明细、`cache_creation.ephemeral_1h_input_tokens` 等普遍不完整。建议按“部分支持 Prompt Caching” 理解，不要依赖完整的 Anthropic TTL / usage 明细。

#### 元信息与服务层级

`metadata`（object）：请求元信息，`metadata.user_id`（string）为终端用户唯一标识，用于滥用检测、用量归因。

`service_tier`（string）：服务层级 / TPM 保障渠道标识，响应中会回写实际命中的层级。

| 取值 | 说明 |
| --- | --- |
| `auto` | 自动选择 |
| `standard` | 标准层级 |
| `priority` | 优先层级（更高保障） |
| `batch` | 批处理层级 |

#### 请求头

| 请求头 | 必填 | 说明 |
| --- | --- | --- |
| `x-api-key` | 是 | API Key（Anthropic 官方习惯）；平台同时兼容 `Authorization: Bearer <key>`。 |
| `anthropic-version` | 是 | API 版本，固定 `2023-06-01`。 |
| `content-type` | 是 | `application/json` |
| `anthropic-beta` | 否 | beta 功能开关（如 `prompt-caching`、`interleaved-thinking` 等），平台原样透传给模型服务。 |

### Message 对象详解

`messages` 数组中的每个元素代表对话中的一条消息。

**role 枚举：**

| role | 含义 | 使用位置 |
| --- | --- | --- |
| `user` | 人类用户的输入（含工具结果 tool\_result） | 奇数轮对话。 |
| `assistant` | 模型的历史回复（可含 text / thinking / tool\_use） | 偶数轮对话，多轮时需携带历史。 |

**说明：**

**关键差异**：Anthropic 协议没有独立的 `tool` role。工具执行结果以 `user` 消息中的 `tool_result` 内容块表达，且紧跟在对应 `assistant` 的 `tool_use` 之后。这与 OpenAI Chat 协议（独立 `tool` role）不同。`system` 不在 messages 内，通过顶层 `system` 字段传入。

**content 格式：**支持字符串与内容块数组两种形式。

```json
// 字符串
{ "role": "user", "content": "你好" }

// 内容块数组
{
  "role": "user",
  "content": [
    { "type": "text", "text": "这张图片里有什么？" },
    { "type": "image", "source": { "type": "url", "url": "https://example.com/img.jpg" } }
  ]
}
```

**content block 类型：**

| block type | 关键字段 | 适用 role | 说明 |
| --- | --- | --- | --- |
| `text` | `text`、`cache_control` | user / assistant | 文本内容 |
| `image` | `source` | user | 图片 |
| `video` | `source` | user | 视频 |
| `document` | `source`、`title`、`context`、`citations`、`cache_control` | user | 文档输入与引用 |
| `search_result` | `source`、`title`、`content`、`citations` | user | 搜索结果内容块 |
| `tool_use` | `id`、`name`、`input` | assistant | 模型请求调用工具 |
| `tool_result` | `tool_use_id`、`content` | user | 工具执行结果 |
| `thinking` | `thinking`、`signature` | assistant | 思维链内容 |
| `redacted_thinking` | `data` | assistant | 加密思维链 |

**说明：**

**能力说明**：`text`、`tool_use`、文本 `tool_result`、`thinking` 在支持相应能力的模型上整体可用。`image` block 需使用明确支持视觉/多模态的模型；纯文本模型会返回 400。`document` 多数模型可接收但不返回 citations；`search_result` 当前模型普遍不支持。

**多模态 block：**

图片块（`type: "image"`）：

```json
// Base64
{ "type": "image", "source": { "type": "base64", "media_type": "image/jpeg", "data": "/9j/4AAQ..." } }

// URL
{ "type": "image", "source": { "type": "url", "url": "https://example.com/photo.jpg" } }
```

| `source` 字段 | 类型 | 说明 |
| --- | --- | --- |
| `type` | string | `"base64"` 或 `"url"`。 |
| `media_type` | string | `base64` 时必填，如 `image/jpeg`、`image/png`、`image/gif`、`image/webp`。 |
| `data` | string | `base64` 时的图片数据。 |
| `url` | string | `url` 时的图片地址。 |
| `detail` | string | `low` / `high` / `auto`，图像分析精度。 |

**说明：**

**能力说明**：需要图片理解时应使用明确支持视觉/多模态（VL）的模型，并在模型能力说明中单独确认；纯文本模型对 image block 返回 400。

文档块（`type: "document"`）：`source`（支持文本、base64、URL 等）、`title`、`context`、`citations`、`cache_control`。多数模型可接收文档请求（返回 200），但响应不包含 citations，适合作为普通上下文降级处理，不应承诺 Anthropic 引用能力。

搜索结果块（`type: "search_result"`）：用于把外部搜索结果作为带来源的内容块交给模型，通常配合 citations 使用。当前模型普遍返回 400，不支持该 content block。

视频块（`type: "video"`）：结构与图片块一致，`source` 额外支持 `fps`（采样帧率）字段。视频理解为各厂商扩展能力，并非 Anthropic 官方原生支持。

**工具相关 block：**

tool\_use（assistant 消息）——模型请求调用工具时携带：

```json
{ "type": "tool_use", "id": "toolu_001", "name": "get_weather", "input": { "location": "北京" } }
```

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `id` | string | 工具调用唯一 ID，需在对应 `tool_result` 中回传。 |
| `name` | string | 调用的工具名称。 |
| `input` | object | 工具参数（对象，非 JSON 字符串，与 OpenAI 的 `arguments` 字符串不同）。 |

tool\_result（user 消息）——工具执行后，结果以 `tool_result` 块放入 user 消息：

```json
{ "type": "tool_result", "tool_use_id": "toolu_001", "content": "北京今天晴天，25度" }
```

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `tool_use_id` | string | 对应 `tool_use.id`。 |
| `content` | string 或 array | 工具结果，可为纯文本或内容块数组（支持文本+图片）。 |
| `is_error` | boolean | 工具执行失败时设为 `true`。 |
| `cache_control` | object | 缓存标记。 |

**注意：**

**排列要求**：同一 assistant 轮次产生的所有 `tool_result`，必须放在同一条紧随其后的 user 消息中。图片类型的 `tool_result.content` 仅部分多模态模型支持。

**思维链相关 block：**

thinking（assistant 消息）：

```json
{ "type": "thinking", "thinking": "让我逐步分析：外层 n 次，内层 log n 次...", "signature": "EqoBCkgIARgC..." }
```

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `thinking` | string | 模型的推理过程文本 |
| `signature` | string | 思维块完整性签名 |

**注意：**

**多轮回传要求**：多轮对话时，assistant 历史消息中的 thinking 块必须原样携带 `signature` 回传，否则服务返回 `400 Invalid signature`。`signature` 是加密凭证，不能截断或修改。该校验语义主要适用于 Claude 系列模型；其他模型以自有协议承载思维链时，回传要求以对应模型的说明为准。部分模型（如 `deepseek-v4-flash`、`hy3`）不返回 `signature`，此时多轮对话无需回传该字段。

redacted\_thinking（assistant 消息）：部分思维内容因安全原因被加密，以 `{ "type": "redacted_thinking", "data": "<加密数据>" }` 返回，仅含 `data` 字段。多轮对话时需按原顺序全部回传，以维持上下文续写能力。该内容块主要出现在 Claude 系列模型，其他模型通常不返回。

### 响应参数详解

#### 非流式响应

```json
{
  "id": "msg_xxx",
  "type": "message",
  "role": "assistant",
  "model": "<your-model-name>",
  "content": [
    { "type": "thinking", "thinking": "...", "signature": "..." },
    { "type": "text", "text": "回复内容" },
    { "type": "tool_use", "id": "toolu_xxx", "name": "get_weather", "input": { "location": "北京" } }
  ],
  "stop_reason": "end_turn",
  "stop_sequence": null,
  "usage": {
    "input_tokens": 12,
    "output_tokens": 6,
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 0
  },
  "service_tier": "standard"
}
```

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `id` | string | 响应唯一标识（`msg_` 前缀）。 |
| `type` | string | 固定 `"message"`。 |
| `role` | string | 固定 `"assistant"`。 |
| `model` | string | 实际使用的模型名称。 |
| `content` | array | 内容块数组，顺序通常为 `thinking → text → tool_use`。 |
| `stop_reason` | string | 停止原因，见下方枚举。 |
| `stop_sequence` | string 或 null | 命中的停止序列（命中 `stop_sequences` 时）。 |
| `usage` | object | Token 用量，请参见 [Token 用量](https://cloud.tencent.com/document/product/1823/135874#c641cf0b-b87d-4f6f-9285-1fa190016d59)。 |
| `container` | object | 代码执行容器信息（`id`、`expires_at`），仅用到 `code_execution` 内置工具时返回。 |
| `service_tier` | string | 实际命中的服务层级。 |

**说明：**

**请求追踪 ID**：排查日志时优先使用响应体 `id`；流式响应优先使用 `message_start` 事件的 `data.message.id`。平台会同时透传/生成客户端请求头中的 `X-Request-Id` / `X-Tc-Requestid`，但最终有效的模型响应 ID 以 message `id` 为准。

#### 流式响应（SSE）

`stream: true` 时返回 SSE，响应头 `Content-Type: text/event-stream`、`Cache-Control: no-cache`、`Connection: keep-alive`。

**标准事件顺序：**

```undefined
message_start
  → content_block_start → content_block_delta(多次) → content_block_stop   （第 1 个块）
  → content_block_start → content_block_delta(多次) → content_block_stop   （第 2 个块）
  ...
  → message_delta → message_stop
```

辅助事件：`ping`（保活心跳）、`error`（错误）。每个 SSE 帧格式为 `event: <类型>` + `data: {json}`。

**主要事件说明：**

| 事件 | 含义 | 关键字段 |
| --- | --- | --- |
| `message_start` | 消息开始，返回初始 message 骨架 | `message`（含初始 usage 的 input/cache） |
| `content_block_start` | 一个内容块开始 | `index`、`content_block`（type 为 text/thinking/tool\_use） |
| `content_block_delta` | 内容增量 | `index`、`delta`（见下表） |
| `content_block_stop` | 一个内容块结束 | `index` |
| `message_delta` | 消息级增量 | `delta.stop_reason`、`usage`（最终 output\_tokens） |
| `message_stop` | 消息结束 | - |

`content_block_delta.delta` **类型：**

| delta.type | 字段 | 含义 |
| --- | --- | --- |
| `text_delta` | `text` | 文本增量。 |
| `thinking_delta` | `thinking` | 思维过程增量。 |
| `signature_delta` | `signature` | 思维块完整性签名（在 thinking 块结束前下发）。 |
| `input_json_delta` | `partial_json` | 工具参数 JSON 片段，需累积后整体解析。 |

**说明：**

**流式错误处理**：若在发送响应头（HTTP 200）之前发生错误，返回标准 JSON 错误体或触发故障转移重试；若流已开始后发生错误，以 `error` 事件下发或直接关闭连接，客户端需通过连接异常感知。
**能力说明**：基础 SSE 事件在支持相应能力的模型上均可用；`citations_delta` 当前普遍不返回。流式工具参数（`input_json_delta`）在部分模型上需先显式关闭 thinking 才可用。

#### stop\_reason 枚举

| 值 | 含义 | 处理建议 |
| --- | --- | --- |
| `end_turn` | 模型正常结束 | 正常处理。 |
| `max_tokens` | 达到 `max_tokens` 限制，输出被截断 | 增大 `max_tokens` 或分段生成。 |
| `stop_sequence` | 命中 `stop_sequences` | 检查命中的 `stop_sequence` 字段。 |
| `tool_use` | 模型请求调用工具 | 执行工具，将结果以 `tool_result` 回传继续对话。 |
| `pause_turn` | server tool 长轮次暂停 | 原样回传当前内容继续请求以恢复。 |
| `refusal` | 模型因安全原因拒答 | 检查输入是否触发安全策略。 |

#### Token 用量（usage）

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `input_tokens` | integer | 净输入 token（不含缓存读写部分） |
| `output_tokens` | integer | 输出 token（含 thinking 内容） |
| `cache_creation_input_tokens` | integer | 写入缓存的 token 数 |
| `cache_read_input_tokens` | integer | 命中缓存读取的 token 数（计费大幅降低） |
| `cache_creation.ephemeral_5m_input_tokens` | integer | 5 分钟 TTL 缓存创建 token（分 TTL 明细） |
| `cache_creation.ephemeral_1h_input_tokens` | integer | 1 小时 TTL 缓存创建 token（分 TTL 明细） |
| `server_tool_use.web_search_requests` | integer | 内置 web\_search 调用次数 |
| `server_tool_use.web_fetch_requests` | integer | 内置 web\_fetch 调用次数 |
| `service_tier` | string | 实际命中的服务层级 |

**说明：**

**input\_tokens 互斥规则**：Anthropic 规范中 `input_tokens`、`cache_read_input_tokens`、`cache_creation_input_tokens` 三者互斥，真实总输入 = 三者之和。计算成本时需将三项相加，不要只看 `input_tokens`。
流式响应中，`message_start` 事件给出初始的 `input_tokens` 与缓存 token；`message_delta` 事件给出最终的 `output_tokens`。

### 典型场景示例

**说明：**

所有示例统一请求入口：`POST /v1/messages`，需带 `anthropic-version` 与 `x-api-key` 头。以下 `${BASE_URL}` 取 `https://tokenhub.tencentmaas.com`。

#### 示例：基础对话

cURL

Python

Node.js

Java

Go

```bash
curl -s -X POST "${BASE_URL}/v1/messages" \\
  -H 'Content-Type: application/json' \\
  -H 'anthropic-version: 2023-06-01' \\
  -H "x-api-key: ${API_KEY}" \\
  -d '{
    "model": "<your-model-name>",
    "messages": [{ "role": "user", "content": "你好" }],
    "max_tokens": 1024
  }'
```

```python
import requests

resp = requests.post(
    "https://tokenhub.tencentmaas.com/v1/messages",
    headers={
        "Content-Type": "application/json",
        "anthropic-version": "2023-06-01",
        "x-api-key": "YOUR_API_KEY",
    },
    json={
        "model": "<your-model-name>",
        "messages": [{"role": "user", "content": "你好"}],
        "max_tokens": 1024,
    },
)
print(resp.json())
```

```javascript
const resp = await fetch("https://tokenhub.tencentmaas.com/v1/messages", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "anthropic-version": "2023-06-01",
    "x-api-key": "YOUR_API_KEY",
  },
  body: JSON.stringify({
    model: "<your-model-name>",
    messages: [{ role: "user", content: "你好" }],
    max_tokens: 1024,
  }),
});
console.log(await resp.json());
```

```java
import okhttp3.*;

public class BasicMessage {
    public static void main(String[] args) throws Exception {
        String body = """
        {
          "model": "<your-model-name>",
          "messages": [{ "role": "user", "content": "你好" }],
          "max_tokens": 1024
        }
        """;

        Request request = new Request.Builder()
            .url("https://tokenhub.tencentmaas.com/v1/messages")
            .header("Content-Type", "application/json")
            .header("anthropic-version", "2023-06-01")
            .header("x-api-key", "YOUR_API_KEY")
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
  "messages": [{ "role": "user", "content": "你好" }],
  "max_tokens": 1024
}`

    req, _ := http.NewRequest("POST",
        "https://tokenhub.tencentmaas.com/v1/messages",
        strings.NewReader(body))
    req.Header.Set("Content-Type", "application/json")
    req.Header.Set("anthropic-version", "2023-06-01")
    req.Header.Set("x-api-key", "YOUR_API_KEY")

    resp, err := http.DefaultClient.Do(req)
    if err != nil {
        panic(err)
    }
    defer resp.Body.Close()

    data, _ := io.ReadAll(resp.Body)
    fmt.Println(string(data))
}
```

#### 示例：带 system + 流式

cURL

Python

Node.js

Java

Go

```bash
curl -s -N -X POST "${BASE_URL}/v1/messages" \\
  -H 'Content-Type: application/json' \\
  -H 'anthropic-version: 2023-06-01' \\
  -H "x-api-key: ${API_KEY}" \\
  -d '{
    "model": "<your-model-name>",
    "system": [{ "type": "text", "text": "你是一个友好的助手" }],
    "messages": [{ "role": "user", "content": "1+1等于几？" }],
    "max_tokens": 1024,
    "stream": true
  }'
```

```python
import requests

resp = requests.post(
    "https://tokenhub.tencentmaas.com/v1/messages",
    headers={
        "Content-Type": "application/json",
        "anthropic-version": "2023-06-01",
        "x-api-key": "YOUR_API_KEY",
    },
    json={
        "model": "<your-model-name>",
        "system": [{"type": "text", "text": "你是一个友好的助手"}],
        "messages": [{"role": "user", "content": "1+1等于几？"}],
        "max_tokens": 1024,
        "stream": True,
    },
    stream=True,
)
for line in resp.iter_lines(decode_unicode=True):
    if line:
        print(line)
```

```javascript
const resp = await fetch("https://tokenhub.tencentmaas.com/v1/messages", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "anthropic-version": "2023-06-01",
    "x-api-key": "YOUR_API_KEY",
  },
  body: JSON.stringify({
    model: "<your-model-name>",
    system: [{ type: "text", text: "你是一个友好的助手" }],
    messages: [{ role: "user", content: "1+1等于几？" }],
    max_tokens: 1024,
    stream: true,
  }),
});
const reader = resp.body.getReader();
const decoder = new TextDecoder();
while (true) {
  const { done, value } = await reader.read();
  if (done) break;
  process.stdout.write(decoder.decode(value));
}
```

```java
import okhttp3.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class SystemStream {
    public static void main(String[] args) throws Exception {
        String body = """
        {
          "model": "<your-model-name>",
          "system": [{ "type": "text", "text": "你是一个友好的助手" }],
          "messages": [{ "role": "user", "content": "1+1等于几？" }],
          "max_tokens": 1024,
          "stream": true
        }
        """;

        Request request = new Request.Builder()
            .url("https://tokenhub.tencentmaas.com/v1/messages")
            .header("Content-Type", "application/json")
            .header("anthropic-version", "2023-06-01")
            .header("x-api-key", "YOUR_API_KEY")
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
  "system": [{ "type": "text", "text": "你是一个友好的助手" }],
  "messages": [{ "role": "user", "content": "1+1等于几？" }],
  "max_tokens": 1024,
  "stream": true
}`

    req, _ := http.NewRequest("POST",
        "https://tokenhub.tencentmaas.com/v1/messages",
        strings.NewReader(body))
    req.Header.Set("Content-Type", "application/json")
    req.Header.Set("anthropic-version", "2023-06-01")
    req.Header.Set("x-api-key", "YOUR_API_KEY")

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

期望 SSE 事件链：`message_start → content_block_start → content_block_delta → content_block_stop → message_delta → message_stop`。

#### 示例：多轮对话

多轮对话需完整携带历史消息（平台不做会话管理）：

```json
{
  "model": "<your-model-name>",
  "messages": [
    { "role": "user", "content": "如何读取 CSV 文件？" },
    { "role": "assistant", "content": "使用 pandas：pd.read_csv('file.csv')" },
    { "role": "user", "content": "如果文件很大内存放不下怎么办？" }
  ],
  "max_tokens": 1024
}
```

#### 示例：多模态（图片理解）

理解图片（URL）：

```json
{
  "model": "<your-model-name>",
  "messages": [{
    "role": "user",
    "content": [
      { "type": "text", "text": "请详细描述图中的场景" },
      { "type": "image", "source": { "type": "url", "url": "https://example.com/photo.jpg" } }
    ]
  }],
  "max_tokens": 1024
}
```

Base64 图片：

```json
{
  "role": "user",
  "content": [
    { "type": "text", "text": "识别图中的文字" },
    { "type": "image", "source": { "type": "base64", "media_type": "image/jpeg", "data": "/9j/4AAQSkZJRgAB..." } }
  ]
}
```

#### 示例：工具调用

cURL

Python

Node.js

Java

Go

```bash
curl -s -X POST "${BASE_URL}/v1/messages" \\
  -H 'Content-Type: application/json' \\
  -H 'anthropic-version: 2023-06-01' \\
  -H "x-api-key: ${API_KEY}" \\
  -d '{
    "model": "<your-model-name>",
    "messages": [{ "role": "user", "content": "北京今天天气怎么样？" }],
    "max_tokens": 1024,
    "tools": [{
      "name": "get_weather",
      "description": "查询指定城市的天气信息",
      "input_schema": {
        "type": "object",
        "properties": { "location": { "type": "string", "description": "城市名称" } },
        "required": ["location"]
      }
    }],
    "tool_choice": { "type": "auto" }
  }'
```

```python
import requests

resp = requests.post(
    "https://tokenhub.tencentmaas.com/v1/messages",
    headers={
        "Content-Type": "application/json",
        "anthropic-version": "2023-06-01",
        "x-api-key": "YOUR_API_KEY",
    },
    json={
        "model": "<your-model-name>",
        "messages": [{"role": "user", "content": "北京今天天气怎么样？"}],
        "max_tokens": 1024,
        "tools": [
            {
                "name": "get_weather",
                "description": "查询指定城市的天气信息",
                "input_schema": {
                    "type": "object",
                    "properties": {"location": {"type": "string", "description": "城市名称"}},
                    "required": ["location"],
                },
            }
        ],
        "tool_choice": {"type": "auto"},
    },
)
print(resp.json())
```

```javascript
const resp = await fetch("https://tokenhub.tencentmaas.com/v1/messages", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "anthropic-version": "2023-06-01",
    "x-api-key": "YOUR_API_KEY",
  },
  body: JSON.stringify({
    model: "<your-model-name>",
    messages: [{ role: "user", content: "北京今天天气怎么样？" }],
    max_tokens: 1024,
    tools: [
      {
        name: "get_weather",
        description: "查询指定城市的天气信息",
        input_schema: {
          type: "object",
          properties: { location: { type: "string", description: "城市名称" } },
          required: ["location"],
        },
      },
    ],
    tool_choice: { type: "auto" },
  }),
});
console.log(await resp.json());
```

```java
import okhttp3.*;

public class ToolUse {
    public static void main(String[] args) throws Exception {
        String body = """
        {
          "model": "<your-model-name>",
          "messages": [{ "role": "user", "content": "北京今天天气怎么样？" }],
          "max_tokens": 1024,
          "tools": [{
            "name": "get_weather",
            "description": "查询指定城市的天气信息",
            "input_schema": {
              "type": "object",
              "properties": { "location": { "type": "string", "description": "城市名称" } },
              "required": ["location"]
            }
          }],
          "tool_choice": { "type": "auto" }
        }
        """;

        Request request = new Request.Builder()
            .url("https://tokenhub.tencentmaas.com/v1/messages")
            .header("Content-Type", "application/json")
            .header("anthropic-version", "2023-06-01")
            .header("x-api-key", "YOUR_API_KEY")
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
  "messages": [{ "role": "user", "content": "北京今天天气怎么样？" }],
  "max_tokens": 1024,
  "tools": [{
    "name": "get_weather",
    "description": "查询指定城市的天气信息",
    "input_schema": {
      "type": "object",
      "properties": { "location": { "type": "string", "description": "城市名称" } },
      "required": ["location"]
    }
  }],
  "tool_choice": { "type": "auto" }
}`

    req, _ := http.NewRequest("POST",
        "https://tokenhub.tencentmaas.com/v1/messages",
        strings.NewReader(body))
    req.Header.Set("Content-Type", "application/json")
    req.Header.Set("anthropic-version", "2023-06-01")
    req.Header.Set("x-api-key", "YOUR_API_KEY")

    resp, err := http.DefaultClient.Do(req)
    if err != nil {
        panic(err)
    }
    defer resp.Body.Close()

    data, _ := io.ReadAll(resp.Body)
    fmt.Println(string(data))
}
```

模型返回 `tool_use` 后，客户端执行工具并以 `tool_result`（放入 user 消息）回传：

```json
{
  "model": "<your-model-name>",
  "messages": [
    { "role": "user", "content": "北京今天天气怎么样？" },
    { "role": "assistant", "content": [
      { "type": "tool_use", "id": "toolu_001", "name": "get_weather", "input": { "location": "北京" } }
    ]},
    { "role": "user", "content": [
      { "type": "tool_result", "tool_use_id": "toolu_001", "content": "北京今天晴天，25度" }
    ]}
  ],
  "max_tokens": 1024,
  "tools": [{
    "name": "get_weather", "description": "查询天气",
    "input_schema": { "type": "object", "properties": { "location": { "type": "string" } }, "required": ["location"] }
  }]
}
```

#### 示例：思维链

cURL

Python

Node.js

Java

Go

```bash
curl -s -X POST "${BASE_URL}/v1/messages" \\
  -H 'Content-Type: application/json' \\
  -H 'anthropic-version: 2023-06-01' \\
  -H "x-api-key: ${API_KEY}" \\
  -d '{
    "model": "<your-model-name>",
    "messages": [{ "role": "user", "content": "请解释什么是递归" }],
    "max_tokens": 4096,
    "thinking": { "type": "enabled", "budget_tokens": 2048 }
  }'
```

```python
import requests

resp = requests.post(
    "https://tokenhub.tencentmaas.com/v1/messages",
    headers={
        "Content-Type": "application/json",
        "anthropic-version": "2023-06-01",
        "x-api-key": "YOUR_API_KEY",
    },
    json={
        "model": "<your-model-name>",
        "messages": [{"role": "user", "content": "请解释什么是递归"}],
        "max_tokens": 4096,
        "thinking": {"type": "enabled", "budget_tokens": 2048},
    },
)
print(resp.json())
```

```javascript
const resp = await fetch("https://tokenhub.tencentmaas.com/v1/messages", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "anthropic-version": "2023-06-01",
    "x-api-key": "YOUR_API_KEY",
  },
  body: JSON.stringify({
    model: "<your-model-name>",
    messages: [{ role: "user", content: "请解释什么是递归" }],
    max_tokens: 4096,
    thinking: { type: "enabled", budget_tokens: 2048 },
  }),
});
console.log(await resp.json());
```

```java
import okhttp3.*;

public class Thinking {
    public static void main(String[] args) throws Exception {
        String body = """
        {
          "model": "<your-model-name>",
          "messages": [{ "role": "user", "content": "请解释什么是递归" }],
          "max_tokens": 4096,
          "thinking": { "type": "enabled", "budget_tokens": 2048 }
        }
        """;

        Request request = new Request.Builder()
            .url("https://tokenhub.tencentmaas.com/v1/messages")
            .header("Content-Type", "application/json")
            .header("anthropic-version", "2023-06-01")
            .header("x-api-key", "YOUR_API_KEY")
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
  "messages": [{ "role": "user", "content": "请解释什么是递归" }],
  "max_tokens": 4096,
  "thinking": { "type": "enabled", "budget_tokens": 2048 }
}`

    req, _ := http.NewRequest("POST",
        "https://tokenhub.tencentmaas.com/v1/messages",
        strings.NewReader(body))
    req.Header.Set("Content-Type", "application/json")
    req.Header.Set("anthropic-version", "2023-06-01")
    req.Header.Set("x-api-key", "YOUR_API_KEY")

    resp, err := http.DefaultClient.Do(req)
    if err != nil {
        panic(err)
    }
    defer resp.Body.Close()

    data, _ := io.ReadAll(resp.Body)
    fmt.Println(string(data))
}
```

响应 `content` 中会包含 `thinking` 块（带 `signature`）与 `text` 块。注意 `max_tokens` 须大于 `budget_tokens`。

#### 示例：多轮思维链（携带 signature）

多轮对话时，必须将上一轮 assistant 的 `thinking` 块连同 `signature` 原样回传：

```json
{
  "model": "<your-model-name>",
  "messages": [
    { "role": "user", "content": "分析这段代码复杂度" },
    { "role": "assistant", "content": [
      { "type": "thinking", "thinking": "外层 n 次内层 log n 次...", "signature": "EqoBCkgIARgC..." },
      { "type": "text", "text": "O(n log n)" }
    ]},
    { "role": "user", "content": "如何优化成 O(n)？" }
  ],
  "max_tokens": 4096,
  "thinking": { "type": "enabled", "budget_tokens": 2048 }
}
```

**注意：**

**关键**：`signature` 必须原样保留回传，否则服务报 `400 Invalid signature`。

#### 示例：内置工具（web\_search）

cURL

Python

Node.js

Java

Go

```bash
curl -s -X POST "${BASE_URL}/v1/messages" \\
  -H 'Content-Type: application/json' \\
  -H 'anthropic-version: 2023-06-01' \\
  -H "x-api-key: ${API_KEY}" \\
  -d '{
    "model": "<your-model-name>",
    "messages": [{ "role": "user", "content": "2026年有哪些新大模型？" }],
    "max_tokens": 2048,
    "tools": [{ "type": "web_search_20250305", "name": "web_search", "max_uses": 3 }]
  }'
```

```python
import requests

resp = requests.post(
    "https://tokenhub.tencentmaas.com/v1/messages",
    headers={
        "Content-Type": "application/json",
        "anthropic-version": "2023-06-01",
        "x-api-key": "YOUR_API_KEY",
    },
    json={
        "model": "<your-model-name>",
        "messages": [{"role": "user", "content": "2026年有哪些新大模型？"}],
        "max_tokens": 2048,
        "tools": [{"type": "web_search_20250305", "name": "web_search", "max_uses": 3}],
    },
)
print(resp.json())
```

```javascript
const resp = await fetch("https://tokenhub.tencentmaas.com/v1/messages", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "anthropic-version": "2023-06-01",
    "x-api-key": "YOUR_API_KEY",
  },
  body: JSON.stringify({
    model: "<your-model-name>",
    messages: [{ role: "user", content: "2026年有哪些新大模型？" }],
    max_tokens: 2048,
    tools: [{ type: "web_search_20250305", name: "web_search", max_uses: 3 }],
  }),
});
console.log(await resp.json());
```

```java
import okhttp3.*;

public class BuiltinTool {
    public static void main(String[] args) throws Exception {
        String body = """
        {
          "model": "<your-model-name>",
          "messages": [{ "role": "user", "content": "2026年有哪些新大模型？" }],
          "max_tokens": 2048,
          "tools": [{ "type": "web_search_20250305", "name": "web_search", "max_uses": 3 }]
        }
        """;

        Request request = new Request.Builder()
            .url("https://tokenhub.tencentmaas.com/v1/messages")
            .header("Content-Type", "application/json")
            .header("anthropic-version", "2023-06-01")
            .header("x-api-key", "YOUR_API_KEY")
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
  "messages": [{ "role": "user", "content": "2026年有哪些新大模型？" }],
  "max_tokens": 2048,
  "tools": [{ "type": "web_search_20250305", "name": "web_search", "max_uses": 3 }]
}`

    req, _ := http.NewRequest("POST",
        "https://tokenhub.tencentmaas.com/v1/messages",
        strings.NewReader(body))
    req.Header.Set("Content-Type", "application/json")
    req.Header.Set("anthropic-version", "2023-06-01")
    req.Header.Set("x-api-key", "YOUR_API_KEY")

    resp, err := http.DefaultClient.Do(req)
    if err != nil {
        panic(err)
    }
    defer resp.Body.Close()

    data, _ := io.ReadAll(resp.Body)
    fmt.Println(string(data))
}
```

**说明：**

内置工具通过 `type` 指定版本化类型名，无需 `input_schema`。内置工具的支持情况因模型而异，详情请参见 [各模型字段兼容情况](https://cloud.tencent.com/document/product/1823/130079)。

#### 示例：Prompt Caching

在 system 长文档或工具定义上打 `cache_control` 标记，命中缓存后大幅降低 `input_tokens` 计费：

```json
{
  "model": "<your-model-name>",
  "system": [
    { "type": "text", "text": "你是一个文档问答助手。" },
    { "type": "text", "text": "<很长的文档内容...>", "cache_control": { "type": "ephemeral", "ttl": "1h" } }
  ],
  "messages": [{ "role": "user", "content": "文档第三章讲了什么？" }],
  "max_tokens": 1024
}
```

响应 `usage` 中可见 `cache_creation_input_tokens`（首次写缓存）与 `cache_read_input_tokens`（后续命中读取）。
