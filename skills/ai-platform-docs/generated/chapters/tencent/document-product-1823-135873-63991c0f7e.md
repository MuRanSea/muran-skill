<!-- Official source: https://cloud.tencent.com/document/product/1823/135873 -->
<!-- Source SHA-256: 75d46a9e98cd385f740be97369bcee95a5d8956235912ae32f3406746f29ff79 -->

# OpenAI Response 协议字段说明

官方来源：https://cloud.tencent.com/document/product/1823/135873
最近更新时间：2026-10-10 14:05:00

## OpenAI Responses API 使用

### 请求体参数

#### 基础参数

| 参数 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `model` | string | 否 | 用于生成响应的模型 ID，如 `hy3` 或 `qwen3.5-flash`。支持的推理模型：`hy3`、`deepseek-v4-flash`、`deepseek-v4-pro` 支持 `reasoning.effort` 全部取值；`qwen3.5-flash`、`qwen3.5-plus` 默认开启推理，`reasoning.effort` 支持 `none`、`low`、`medium`，传入 `high` 会返回 400。 |
| `input` | string 或 array | 否 | 发送给模型的文本、图像或文件输入。string 为纯文本（等同 `user` 角色文本）；array 为输入条目列表，详见 [输入类型详解](https://cloud.tencent.com/document/product/1823/135873#35a07989-dc30-43f5-9e25-3506b2abeea0)。 |
| `instructions` | string | 否 | 插入模型上下文的系统（或开发者）消息。与 `previous_response_id` 一起使用时，上一次响应的指令不会延续到下一次响应，便于替换系统消息。 |
| `stream` | boolean | 否 | 设为 `true` 时，模型响应数据将通过 SSE 流式传输，事件包括 `response.created`、`response.output_text.delta`、`response.completed` 等。 |

#### 生成控制参数

| 参数 | 类型 | 取值范围 | 说明 |
| --- | --- | --- | --- |
| `max_output_tokens` | number | ≥ 1 | 响应可生成的 Token 数量上限，包括可见输出 Token 和推理 Token。推理模型的推理 Token 也计入此限制。 |
| `temperature` | number | [0, 2] | 采样温度，控制输出随机性。较高值更随机有创意，较低值更集中确定。 |
| `top_p` | number | (0, 1] | 核采样参数。模型只考虑概率质量前 `top_p` 的 Token。建议只调 `temperature` 或 `top_p` 之一。 |
| `truncation` | string | `"auto"` / `"disabled"` | 上下文超出模型最大长度时的截断策略。`auto` 从对话开头删除条目；`disabled`（默认）超出时请求以 400 失败。三个模型均接受此参数但不在响应体中回显。 |

#### 工具调用

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| `tools` | array | 模型在生成响应时可调用的工具数组，支持函数调用、文件搜索、网络搜索等，详见 [工具类型详解](https://cloud.tencent.com/document/product/1823/135873#216b6cb3-644d-4e55-b780-7667e322452e)。 |
| `tool_choice` | string 或 object | 模型如何选择工具，取值见下表。 |
| `parallel_tool_calls` | boolean | 是否允许模型并行运行工具调用。 |

`tool_choice` **取值：**

| 值/类型 | 说明 |
| --- | --- |
| `"none"` | 模型不调用任何工具，直接生成消息。 |
| `"auto"` | 模型可选择生成消息或调用一个或多个工具。 |
| `{ "type": "function", "name": "..." }` | 强制模型调用特定函数。 |
| `{ "type": "mcp", "server_label": "...", "name": "..." }` | 强制调用特定 MCP 服务器上的工具。 |

**注意：**

`tool_choice` 取值 `"required"` 及指定函数对象的支持情况因模型而异：

`qwen3.5-flash`、`qwen3.5-plus`、`deepseek-v4-flash`、`deepseek-v4-pro`：默认开启思考模式，此时传入 `"required"` 或函数对象会返回 400。如需强制工具调用，请先显式关闭思考模式。

`hy3`：当前不支持 `"required"` 及指定函数对象，请使用 `"auto"` 或 `"none"`。

`"required"` 的支持情况最终取决于所调用模型本身，若返回错误，建议改用 `"auto"` 或直接指定具体的工具名称。

#### 输出格式控制

`text` 参数（object）：配置模型输出的文本格式，通过 `text.format` 子字段指定。

| 格式类型 | 说明 |
| --- | --- |
| `{ "type": "text" }` | 默认格式，生成文本响应。 |
| `{ "type": "json_schema", "name": "...", "schema": {...} }` | 结构化输出，确保模型输出符合指定 JSON Schema。 |
| `{ "type": "json_object" }` | 旧版 JSON 模式，确保输出为有效 JSON（不推荐用于新模型）。 |

**注意：**

使用 `json_schema` 或 `json_object` 时，`hy3`、`deepseek-v4-flash` 会严格输出纯 JSON；`qwen3.5-flash`、`qwen3.5-plus` 的输出可能被 Markdown 代码块（```json ... ```）包裹，需自行去除后再解析。另外 `json_schema` 的 schema 中需包含 `"additionalProperties": false`，否则 `hy3` 会报错。

`include` 参数（array）：指定响应中额外包含的字段列表。三个模型均接受此参数，但额外字段实际是否返回取决于模型支持情况。

| 值 | 说明 |
| --- | --- |
| `file_search_call.results` | 包含文件搜索工具调用的搜索结果。 |
| `web_search_call.results` | 包含网络搜索工具调用的结果。 |
| `message.input_image.image_url` | 包含输入消息中的图像 URL。 |
| `code_interpreter_call.outputs` | 包含代码解释器执行的输出。 |
| `reasoning.encrypted_content` | 包含推理 Token 的加密版本，用于无状态多轮对话。 |
| `message.output_text.logprobs` | 包含助手消息的对数概率。 |

#### 推理控制

`reasoning` 参数（object）：仅适用于推理模型的配置选项。

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `effort` | `"none"` / `"low"` / `"medium"` / `"high"` | 推理努力程度约束。降低推理努力可减少响应时间和推理 Token 消耗。 |
| `summary` | `"auto"` / `"concise"` / `"detailed"` | 模型推理过程的摘要，用于调试和理解推理过程。 |

#### 对话管理

`previous_response_id` 参数（string）：上一次响应的 ID，用于多轮对话。通过链接响应 ID 来维护对话状态，无需手动管理消息历史。不能与 `conversation` 同时使用。

**说明：**

**模型支持**：`qwen3.5-flash`、`qwen3.5-plus` 支持此参数；`hy3` 及通过兼容模式接入的模型（如 `deepseek-v4-flash`、`deepseek-v4-pro`、`glm-5.2`、`kimi-k3` 等）不支持，传入非空值会返回 400 `previous_response_id is not supported in chat-compat mode`，多轮对话请通过 `input` 数组自行携带完整历史。

#### 其他参数

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| `background` | boolean | 是否后台异步运行。各模型均接受此参数，但实际均为同步返回（`hy3` 回显 `null`，`qwen3.5-flash/plus` 回显 `false`）。 |
| `store` | boolean | 是否存储响应以便后续检索。三个模型均接受（不报错），但实际不回显。 |
| `metadata` | object | 附加到响应的键值对元数据（最多 16 对，键最长 64 字符，值最长 512 字符）。三个模型均接受但不在响应体中回显。 |
| `service_tier` | string | 服务层级：`auto` / `default` / `flex` / `scale` / `priority`。`qwen3.5-flash/plus` 在响应中回显，`hy3` 不回显。 |

### 输入类型详解

`input` 为数组时，每个元素为一个输入条目，支持以下类型：

**EasyInputMessage：**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `content` | string 或 array | 文本、图像或音频输入，也可包含之前的助手响应。 |
| `role` | `"user"` / `"assistant"` / `"system"` / `"developer"` | 消息角色。`developer` 或 `system` 的指令优先于 `user`。 |
| `phase` | `"commentary"` / `"final_answer"` | 可选。将助手消息标记为中间注释或最终答案。 |
| `type` | `"message"` | 可选。消息输入类型，始终为 `message`。 |

**ResponseInputImage：**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `detail` | `"low"` / `"high"` / `"auto"` / `"original"` | 图像细节级别，默认 `auto`。 |
| `type` | `"input_image"` | 类型，始终为 `input_image`。 |
| `file_id` | string | 可选。文件 ID。 |
| `image_url` | string | 可选。图像 URL 或 base64 编码的 data URL。 |

**ResponseInputFile：**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `type` | `"input_file"` | 类型，始终为 `input_file`。 |
| `file_data` | string | 可选。文件内容（base64 编码）。 |
| `file_id` | string | 可选。文件 ID。 |
| `file_url` | string | 可选。文件 URL。 |
| `filename` | string | 可选。文件名。 |

### 工具类型详解

**Function（函数工具）：**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `type` | `"function"` | 类型，始终为 `function`。 |
| `name` | string | 函数名称。 |
| `parameters` | object | 描述函数参数的 JSON Schema 对象。 |
| `strict` | boolean | 是否强制严格参数验证，默认 `true`。 |
| `description` | string | 可选。函数描述，供模型判断是否调用。 |

**FileSearch（文件搜索工具）：**支持模型 `qwen3.5-flash`、`qwen3.5-plus`；`hy3` 不支持。需提供有效的 `vector_store_ids`。

未配置有效 `vector_store_ids` 时，请求不会报错，但也不会执行检索，模型将直接基于自身知识作答。通过兼容模式接入的模型（如 `deepseek-v4-flash`、`deepseek-v4-pro`、`glm-5.2`、`kimi-k3` 等）仅支持 `function` 类型工具，`file_search`、`web_search`、`code_interpreter` 等内置工具会被自动丢弃且不报错。

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `type` | `"file_search"` | 类型，始终为 `file_search`。 |
| `vector_store_ids` | array of string | 要搜索的向量存储 ID 列表。 |
| `max_num_results` | number | 可选。最大返回结果数，范围 1-50。 |
| `filters` | ComparisonFilter 或 CompoundFilter | 可选。过滤条件，详见 [过滤器类型](https://cloud.tencent.com/document/product/1823/135873#e78ad826-a9c7-4e18-a60d-01dbb786d322)。 |

**WebSearch（网络搜索工具）：**工具类型为 `"web_search"`（非 OpenAI 官方的 `web_search_preview`）。支持模型 `qwen3.5-flash`、`qwen3.5-plus`；`hy3` 需开通联网搜索资源包。

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `type` | `"web_search"` | 工具类型。 |
| `search_context_size` | `"low"` / `"medium"` / `"high"` | 可选。搜索使用的上下文窗口大小，默认 `medium`。 |
| `user_location` | object | 可选。用户的大致位置，包含 `city`、`country`、`region`、`timezone`。 |

**CodeInterpreter（代码解释器工具）：**当前暂不支持。

**MCP（MCP 工具）：**当前暂不支持。

### 返回值详解

返回 `Response` 对象。

```json
{
  "id": "resp_67ccd2bed1ec8190b14f964abc0542670bb6a6b452d3795b",
  "object": "response",
  "created_at": 1741476542,
  "status": "completed",
  "completed_at": 1741476543,
  "error": null,
  "incomplete_details": null,
  "instructions": null,
  "max_output_tokens": null,
  "model": "<your-model-name>",
  "output": [...],
  "usage": {
    "input_tokens": 20,
    "output_tokens": 11,
    "total_tokens": 31
  }
}
```

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `id` | string | 响应的唯一标识符。 |
| `object` | `"response"` | 对象类型，始终为 `response`。 |
| `created_at` | number | 响应创建时的 Unix 时间戳（秒）。 |
| `status` | string | 响应状态：`completed` / `incomplete` / `failed` / `in_progress` / `cancelled`。 |
| `completed_at` | number | 响应完成时的 Unix 时间戳（秒）。 |
| `error` | object | 请求失败时返回的错误对象，正常完成时不返回。 |
| `incomplete_details` | object | 响应被截断时的详情，`reason` 可为 `"max_output_tokens"` 或 `"content_filter"`。 |
| `instructions` | string | 请求中传入的系统消息，原样回显。 |
| `max_output_tokens` | number | 请求中传入的最大输出 Token 数，未传入时不返回。 |
| `model` | string | 用于生成响应的模型 ID。 |
| `output` | array | 模型生成的输出条目列表，详见 [输出条目类型](https://cloud.tencent.com/document/product/1823/135873#output)。 |
| `parallel_tool_calls` | boolean 或 null | 是否允许并行工具调用。`hy3` 返回 `null`；`qwen3.5-flash/plus` 返回 `true`/`false`。 |
| `previous_response_id` | string | 多轮对话时上一次响应的 ID，单轮时不返回。 |
| `usage` | object | Token 使用统计，详见 [ResponseUsage 对象](https://cloud.tencent.com/document/product/1823/135873#ResponseUsage)。 |
| `service_tier` | string | 实际使用的服务层级。`qwen3.5-flash/plus` 返回（值为 `"default"`）；`hy3` 不返回。 |

**说明：**

`temperature`、`top_p`、`tool_choice`、`tools`、`top_logprobs`、`background` 等字段：`qwen3.5-flash`、`qwen3.5-plus` 会在响应中回显；`hy3` 不回显。

**ResponseUsage 对象：**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `input_tokens` | number | 输入 Token 数量。 |
| `input_tokens_details` | object | 输入 Token 详情，包含 `cached_tokens`。`qwen3.5-flash/plus` 返回；`hy3` 不返回。 |
| `output_tokens` | number | 输出 Token 数量。 |
| `output_tokens_details` | object | 输出 Token 详情，包含 `reasoning_tokens`。`qwen3.5-flash/plus` 返回；`hy3` 不返回。 |
| `total_tokens` | number | 总 Token 数量（input + output）。 |

**输出条目类型（** `output` **数组）：**

*ResponseOutputMessage（消息输出）：*

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `id` | string | 输出消息的唯一 ID。 |
| `type` | `"message"` | 类型，始终为 `message`。 |
| `role` | `"assistant"` | 角色，始终为 `assistant`。 |
| `status` | `"in_progress"` / `"completed"` / `"incomplete"` | 消息状态。 |
| `content` | array | 消息内容数组，每项含 `type: "output_text"` 和 `text` 字段。 |

*FunctionCall（函数调用输出）：*

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `id` | string | 唯一 ID。 |
| `type` | `"function_call"` | 类型，始终为 `function_call`。 |
| `call_id` | string | 函数调用 ID，提交 `function_call_output` 时需传入此值。 |
| `name` | string | 被调用的函数名称。 |
| `arguments` | string | 函数参数的 JSON 字符串。 |
| `status` | string | `in_progress` / `completed` / `incomplete`。 |

*ReasoningItem（推理条目）：*推理模型（`hy3`、`deepseek-v4-flash`、`deepseek-v4-pro` 传入 `reasoning.effort` 时，或 `qwen3.5-flash`/`qwen3.5-plus` 默认）会在 `output` 中额外返回此条目。

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `id` | string | 唯一 ID。 |
| `type` | `"reasoning"` | 类型，始终为 `reasoning`。 |
| `summary` | array | 推理摘要文本列表，每项含 `type: "summary_text"` 和 `text` 字段。 |
| `status` | string | 状态。仅 `hy3` 返回，`qwen3.5-flash/plus` 不返回此字段。 |

### 使用示例

#### 示例：文本输入

cURL

Python

Node.js

Java

Go

```bash
curl https://tokenhub.tencentmaas.com/v1/responses \\
  -H "Content-Type: application/json" \\
  -H "Authorization: Bearer $API_KEY" \\
  -d '{
    "model": "<your-model-name>",
    "input": "给我讲一个关于独角兽的三句话睡前故事。"
  }'
```

```python
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY", base_url="https://tokenhub.tencentmaas.com/v1")

response = client.responses.create(
    model="<your-model-name>",
    input="给我讲一个关于独角兽的三句话睡前故事。",
)
print(response.output_text)
```

```javascript
import OpenAI from 'openai';

const client = new OpenAI({ apiKey: 'YOUR_API_KEY', baseURL: 'https://tokenhub.tencentmaas.com/v1' });

const response = await client.responses.create({
  model: '<your-model-name>',
  input: '给我讲一个关于独角兽的三句话睡前故事。',
});
console.log(response.output_text);
```

```java
import okhttp3.*;

public class TextInput {
    public static void main(String[] args) throws Exception {
        String body = """
        {
          "model": "<your-model-name>",
          "input": "给我讲一个关于独角兽的三句话睡前故事。"
        }
        """;

        Request request = new Request.Builder()
            .url("https://tokenhub.tencentmaas.com/v1/responses")
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
  "input": "给我讲一个关于独角兽的三句话睡前故事。"
}`

    req, _ := http.NewRequest("POST",
        "https://tokenhub.tencentmaas.com/v1/responses",
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

响应示例：

```json
{
  "id": "resp_67ccd2bed1ec8190b14f964abc0542670bb6a6b452d3795b",
  "object": "response",
  "status": "completed",
  "model": "<your-model-name>",
  "output": [
    {
      "type": "message",
      "id": "msg_20260614212356mlaob0d2",
      "status": "completed",
      "role": "assistant",
      "content": [
        {
          "type": "output_text",
          "text": "我是混元，是由腾讯开发的大模型。",
          "annotations": []
        }
      ]
    }
  ],
  "usage": {
    "input_tokens": 20,
    "output_tokens": 11,
    "total_tokens": 31
  }
}
```

#### 示例：图像输入

**说明：**

支持模型：`qwen3.5-flash`、`qwen3.5-plus`（`hy3`、`deepseek-v4-flash` 为纯文本模型，传入图像不会报错但不会被识别）。

图像 URL 需为公网可达的直链；无法访问时将返回 400 错误。也可使用 `data:image/png;base64,...` 形式的 Base64 数据。

cURL

Python

Node.js

Java

Go

```bash
curl https://tokenhub.tencentmaas.com/v1/responses \\
  -H "Content-Type: application/json" \\
  -H "Authorization: Bearer $API_KEY" \\
  -d '{
    "model": "<your-model-name>",
    "input": [
      {
        "role": "user",
        "content": [
          { "type": "input_text", "text": "这张图片里有什么？" },
          {
            "type": "input_image",
            "image_url": "https://example.com/image.jpg"
          }
        ]
      }
    ]
  }'
```

```python
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY", base_url="https://tokenhub.tencentmaas.com/v1")

response = client.responses.create(
    model="<your-model-name>",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "这张图片里有什么？"},
                {"type": "input_image", "image_url": "https://example.com/image.jpg"},
            ],
        }
    ],
)
print(response.output_text)
```

```javascript
import OpenAI from 'openai';

const client = new OpenAI({ apiKey: 'YOUR_API_KEY', baseURL: 'https://tokenhub.tencentmaas.com/v1' });

const response = await client.responses.create({
  model: '<your-model-name>',
  input: [
    {
      role: 'user',
      content: [
        { type: 'input_text', text: '这张图片里有什么？' },
        { type: 'input_image', image_url: 'https://example.com/image.jpg' },
      ],
    },
  ],
});
console.log(response.output_text);
```

```java
import okhttp3.*;

public class ImageInput {
    public static void main(String[] args) throws Exception {
        String body = """
        {
          "model": "<your-model-name>",
          "input": [
            {
              "role": "user",
              "content": [
                { "type": "input_text", "text": "这张图片里有什么？" },
                { "type": "input_image", "image_url": "https://example.com/image.jpg" }
              ]
            }
          ]
        }
        """;

        Request request = new Request.Builder()
            .url("https://tokenhub.tencentmaas.com/v1/responses")
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
  "input": [
    {
      "role": "user",
      "content": [
        { "type": "input_text", "text": "这张图片里有什么？" },
        { "type": "input_image", "image_url": "https://example.com/image.jpg" }
      ]
    }
  ]
}`

    req, _ := http.NewRequest("POST",
        "https://tokenhub.tencentmaas.com/v1/responses",
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

#### 示例：文件输入

**说明：**

文件输入（`input_file`）：`qwen3.5-flash`、`qwen3.5-plus` 支持，文件 URL 需为公网可达直链；`hy3` 暂不可用。

cURL

Python

Node.js

Java

Go

```bash
curl https://tokenhub.tencentmaas.com/v1/responses \\
  -H "Content-Type: application/json" \\
  -H "Authorization: Bearer $API_KEY" \\
  -d '{
    "model": "<your-model-name>",
    "input": [
      {
        "role": "user",
        "content": [
          { "type": "input_text", "text": "这个文件里有什么内容？" },
          {
            "type": "input_file",
            "file_url": "https://www.example.com/document.pdf"
          }
        ]
      }
    ]
  }'
```

```python
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY", base_url="https://tokenhub.tencentmaas.com/v1")

response = client.responses.create(
    model="<your-model-name>",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "这个文件里有什么内容？"},
                {"type": "input_file", "file_url": "https://www.example.com/document.pdf"},
            ],
        }
    ],
)
print(response.output_text)
```

```javascript
import OpenAI from 'openai';

const client = new OpenAI({ apiKey: 'YOUR_API_KEY', baseURL: 'https://tokenhub.tencentmaas.com/v1' });

const response = await client.responses.create({
  model: '<your-model-name>',
  input: [
    {
      role: 'user',
      content: [
        { type: 'input_text', text: '这个文件里有什么内容？' },
        { type: 'input_file', file_url: 'https://www.example.com/document.pdf' },
      ],
    },
  ],
});
console.log(response.output_text);
```

```java
import okhttp3.*;

public class FileInput {
    public static void main(String[] args) throws Exception {
        String body = """
        {
          "model": "<your-model-name>",
          "input": [
            {
              "role": "user",
              "content": [
                { "type": "input_text", "text": "这个文件里有什么内容？" },
                { "type": "input_file", "file_url": "https://www.example.com/document.pdf" }
              ]
            }
          ]
        }
        """;

        Request request = new Request.Builder()
            .url("https://tokenhub.tencentmaas.com/v1/responses")
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
  "input": [
    {
      "role": "user",
      "content": [
        { "type": "input_text", "text": "这个文件里有什么内容？" },
        { "type": "input_file", "file_url": "https://www.example.com/document.pdf" }
      ]
    }
  ]
}`

    req, _ := http.NewRequest("POST",
        "https://tokenhub.tencentmaas.com/v1/responses",
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

#### 示例：网络搜索

**说明：**

网络搜索工具类型为 `"web_search"`。支持模型：`qwen3.5-flash`、`qwen3.5-plus`；`hy3` 需开通联网搜索资源包。

未开通联网搜索资源包时，请求不会报错，但搜索不会生效，响应中 `annotations` 为空。

cURL

Python

Node.js

Java

Go

```bash
curl https://tokenhub.tencentmaas.com/v1/responses \\
  -H "Content-Type: application/json" \\
  -H "Authorization: Bearer $API_KEY" \\
  -d '{
    "model": "<your-model-name>",
    "tools": [{ "type": "web_search" }],
    "input": "今天有什么积极的新闻？"
  }'
```

```python
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY", base_url="https://tokenhub.tencentmaas.com/v1")

response = client.responses.create(
    model="<your-model-name>",
    tools=[{"type": "web_search"}],
    input="今天有什么积极的新闻？",
)
print(response.output_text)
```

```javascript
import OpenAI from 'openai';

const client = new OpenAI({ apiKey: 'YOUR_API_KEY', baseURL: 'https://tokenhub.tencentmaas.com/v1' });

const response = await client.responses.create({
  model: '<your-model-name>',
  tools: [{ type: 'web_search' }],
  input: '今天有什么积极的新闻？',
});
console.log(response.output_text);
```

```java
import okhttp3.*;

public class WebSearch {
    public static void main(String[] args) throws Exception {
        String body = """
        {
          "model": "<your-model-name>",
          "tools": [{ "type": "web_search" }],
          "input": "今天有什么积极的新闻？"
        }
        """;

        Request request = new Request.Builder()
            .url("https://tokenhub.tencentmaas.com/v1/responses")
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
  "tools": [{ "type": "web_search" }],
  "input": "今天有什么积极的新闻？"
}`

    req, _ := http.NewRequest("POST",
        "https://tokenhub.tencentmaas.com/v1/responses",
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

#### 示例：文件搜索

**说明：**

文件搜索（`file_search`）支持模型：`qwen3.5-flash`、`qwen3.5-plus`；`hy3` 不支持。需提供有效的 `vector_store_ids`。

传入不存在的 `vector_store_ids` 时不会报错，但不会执行检索。

cURL

Python

Node.js

Java

Go

```bash
curl https://tokenhub.tencentmaas.com/v1/responses \\
  -H "Content-Type: application/json" \\
  -H "Authorization: Bearer $API_KEY" \\
  -d '{
    "model": "<your-model-name>",
    "tools": [{
      "type": "file_search",
      "vector_store_ids": ["vs_1234567890"],
      "max_num_results": 20
    }],
    "input": "古代棕龙的属性是什么？"
  }'
```

```python
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY", base_url="https://tokenhub.tencentmaas.com/v1")

response = client.responses.create(
    model="<your-model-name>",
    tools=[
        {
            "type": "file_search",
            "vector_store_ids": ["vs_1234567890"],
            "max_num_results": 20,
        }
    ],
    input="古代棕龙的属性是什么？",
)
print(response.output_text)
```

```javascript
import OpenAI from 'openai';

const client = new OpenAI({ apiKey: 'YOUR_API_KEY', baseURL: 'https://tokenhub.tencentmaas.com/v1' });

const response = await client.responses.create({
  model: '<your-model-name>',
  tools: [
    {
      type: 'file_search',
      vector_store_ids: ['vs_1234567890'],
      max_num_results: 20,
    },
  ],
  input: '古代棕龙的属性是什么？',
});
console.log(response.output_text);
```

```java
import okhttp3.*;

public class FileSearch {
    public static void main(String[] args) throws Exception {
        String body = """
        {
          "model": "<your-model-name>",
          "tools": [{
            "type": "file_search",
            "vector_store_ids": ["vs_1234567890"],
            "max_num_results": 20
          }],
          "input": "古代棕龙的属性是什么？"
        }
        """;

        Request request = new Request.Builder()
            .url("https://tokenhub.tencentmaas.com/v1/responses")
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
  "tools": [{
    "type": "file_search",
    "vector_store_ids": ["vs_1234567890"],
    "max_num_results": 20
  }],
  "input": "古代棕龙的属性是什么？"
}`

    req, _ := http.NewRequest("POST",
        "https://tokenhub.tencentmaas.com/v1/responses",
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

#### 示例：流式输出

cURL

Python

Node.js

Java

Go

```bash
curl https://tokenhub.tencentmaas.com/v1/responses \\
  -H "Content-Type: application/json" \\
  -H "Authorization: Bearer $API_KEY" \\
  -d '{
    "model": "<your-model-name>",
    "instructions": "你是一个有帮助的助手。",
    "input": "你好！",
    "stream": true
  }'
```

```python
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY", base_url="https://tokenhub.tencentmaas.com/v1")

stream = client.responses.create(
    model="<your-model-name>",
    instructions="你是一个有帮助的助手。",
    input="你好！",
    stream=True,
)
for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)
```

```javascript
import OpenAI from 'openai';

const client = new OpenAI({ apiKey: 'YOUR_API_KEY', baseURL: 'https://tokenhub.tencentmaas.com/v1' });

const stream = await client.responses.create({
  model: '<your-model-name>',
  instructions: '你是一个有帮助的助手。',
  input: '你好！',
  stream: true,
});
for await (const event of stream) {
  if (event.type === 'response.output_text.delta') process.stdout.write(event.delta);
}
```

```java
import okhttp3.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class StreamResponse {
    public static void main(String[] args) throws Exception {
        String body = """
        {
          "model": "<your-model-name>",
          "instructions": "你是一个有帮助的助手。",
          "input": "你好！",
          "stream": true
        }
        """;

        Request request = new Request.Builder()
            .url("https://tokenhub.tencentmaas.com/v1/responses")
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
  "instructions": "你是一个有帮助的助手。",
  "input": "你好！",
  "stream": true
}`

    req, _ := http.NewRequest("POST",
        "https://tokenhub.tencentmaas.com/v1/responses",
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

流式响应事件序列：

```text
event: response.created
event: response.in_progress
event: response.output_item.added
event: response.content_part.added
event: response.output_text.delta
event: response.output_text.done
event: response.content_part.done
event: response.output_item.done
event: response.completed
```

**说明：**

`qwen3.5-flash` / `qwen3.5-plus` 等推理模型在流式模式下会额外输出推理过程事件（`response.reasoning_summary_text.delta` / `response.reasoning_summary_text.done`）。

#### 示例：函数调用（Function Calling）

函数调用是一个多轮交互过程。第一轮定义工具、发起请求：

cURL

Python

Node.js

Java

Go

```bash
curl https://tokenhub.tencentmaas.com/v1/responses \\
  -H "Content-Type: application/json" \\
  -H "Authorization: Bearer $API_KEY" \\
  -d '{
    "model": "<your-model-name>",
    "input": "北京今天天气怎么样？",
    "tools": [
      {
        "type": "function",
        "name": "get_current_weather",
        "description": "获取指定地点的当前天气",
        "parameters": {
          "type": "object",
          "properties": {
            "location": { "type": "string", "description": "城市和省份，例如：北京市" },
            "unit": { "type": "string", "enum": ["celsius", "fahrenheit"] }
          },
          "required": ["location", "unit"]
        }
      }
    ],
    "tool_choice": "auto"
  }'
```

```python
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY", base_url="https://tokenhub.tencentmaas.com/v1")

response = client.responses.create(
    model="<your-model-name>",
    input="北京今天天气怎么样？",
    tools=[
        {
            "type": "function",
            "name": "get_current_weather",
            "description": "获取指定地点的当前天气",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "城市和省份，例如：北京市"},
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                },
                "required": ["location", "unit"],
            },
        }
    ],
    tool_choice="auto",
)
print(response.output)
```

```javascript
import OpenAI from 'openai';

const client = new OpenAI({ apiKey: 'YOUR_API_KEY', baseURL: 'https://tokenhub.tencentmaas.com/v1' });

const response = await client.responses.create({
  model: '<your-model-name>',
  input: '北京今天天气怎么样？',
  tools: [
    {
      type: 'function',
      name: 'get_current_weather',
      description: '获取指定地点的当前天气',
      parameters: {
        type: 'object',
        properties: {
          location: { type: 'string', description: '城市和省份，例如：北京市' },
          unit: { type: 'string', enum: ['celsius', 'fahrenheit'] },
        },
        required: ['location', 'unit'],
      },
    },
  ],
  tool_choice: 'auto',
});
console.log(response.output);
```

```java
import okhttp3.*;

public class FunctionCallStep1 {
    public static void main(String[] args) throws Exception {
        String body = """
        {
          "model": "<your-model-name>",
          "input": "北京今天天气怎么样？",
          "tools": [
            {
              "type": "function",
              "name": "get_current_weather",
              "description": "获取指定地点的当前天气",
              "parameters": {
                "type": "object",
                "properties": {
                  "location": { "type": "string", "description": "城市和省份，例如：北京市" },
                  "unit": { "type": "string", "enum": ["celsius", "fahrenheit"] }
                },
                "required": ["location", "unit"]
              }
            }
          ],
          "tool_choice": "auto"
        }
        """;

        Request request = new Request.Builder()
            .url("https://tokenhub.tencentmaas.com/v1/responses")
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
  "input": "北京今天天气怎么样？",
  "tools": [
    {
      "type": "function",
      "name": "get_current_weather",
      "description": "获取指定地点的当前天气",
      "parameters": {
        "type": "object",
        "properties": {
          "location": { "type": "string", "description": "城市和省份，例如：北京市" },
          "unit": { "type": "string", "enum": ["celsius", "fahrenheit"] }
        },
        "required": ["location", "unit"]
      }
    }
  ],
  "tool_choice": "auto"
}`

    req, _ := http.NewRequest("POST",
        "https://tokenhub.tencentmaas.com/v1/responses",
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

第一轮响应（模型调用函数）会在 `output` 中返回 `function_call` 条目，其中的 `call_id` 用于下一轮提交结果。

获取到函数结果后，通过 `previous_response_id` + `function_call_output` 提交，模型生成最终回答：

cURL

Python

Node.js

Java

Go

```bash
curl https://tokenhub.tencentmaas.com/v1/responses \\
  -H "Content-Type: application/json" \\
  -H "Authorization: Bearer $API_KEY" \\
  -d '{
    "model": "<your-model-name>",
    "previous_response_id": "<上一轮响应的 id>",
    "input": [
      {
        "type": "function_call_output",
        "call_id": "<function_call 中的 call_id>",
        "output": "{\\"temperature\\": 28, \\"unit\\": \\"celsius\\", \\"description\\": \\"晴天，微风\\"}"
      }
    ]
  }'
```

```python
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY", base_url="https://tokenhub.tencentmaas.com/v1")

response = client.responses.create(
    model="<your-model-name>",
    previous_response_id="<上一轮响应的 id>",
    input=[
        {
            "type": "function_call_output",
            "call_id": "<function_call 中的 call_id>",
            "output": '{"temperature": 28, "unit": "celsius", "description": "晴天，微风"}',
        }
    ],
)
print(response.output_text)
```

```javascript
import OpenAI from 'openai';

const client = new OpenAI({ apiKey: 'YOUR_API_KEY', baseURL: 'https://tokenhub.tencentmaas.com/v1' });

const response = await client.responses.create({
  model: '<your-model-name>',
  previous_response_id: '<上一轮响应的 id>',
  input: [
    {
      type: 'function_call_output',
      call_id: '<function_call 中的 call_id>',
      output: '{"temperature": 28, "unit": "celsius", "description": "晴天，微风"}',
    },
  ],
});
console.log(response.output_text);
```

```java
import okhttp3.*;

public class FunctionCallStep2 {
    public static void main(String[] args) throws Exception {
        String body = """
        {
          "model": "<your-model-name>",
          "previous_response_id": "<上一轮响应的 id>",
          "input": [
            {
              "type": "function_call_output",
              "call_id": "<function_call 中的 call_id>",
              "output": "{\\\\"temperature\\\\": 28, \\\\"unit\\\\": \\\\"celsius\\\\", \\\\"description\\\\": \\\\"晴天，微风\\\\"}"
            }
          ]
        }
        """;

        Request request = new Request.Builder()
            .url("https://tokenhub.tencentmaas.com/v1/responses")
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
  "previous_response_id": "<上一轮响应的 id>",
  "input": [
    {
      "type": "function_call_output",
      "call_id": "<function_call 中的 call_id>",
      "output": "{\\"temperature\\": 28, \\"unit\\": \\"celsius\\", \\"description\\": \\"晴天，微风\\"}"
    }
  ]
}`

    req, _ := http.NewRequest("POST",
        "https://tokenhub.tencentmaas.com/v1/responses",
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

#### 示例：推理模型（Reasoning）

cURL

Python

Node.js

Java

Go

```bash
curl https://tokenhub.tencentmaas.com/v1/responses \\
  -H "Content-Type: application/json" \\
  -H "Authorization: Bearer $API_KEY" \\
  -d '{
    "model": "<your-model-name>",
    "input": "请解释量子纠缠的基本原理。",
    "reasoning": {
      "effort": "high"
    }
  }'
```

```python
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY", base_url="https://tokenhub.tencentmaas.com/v1")

response = client.responses.create(
    model="<your-model-name>",
    input="请解释量子纠缠的基本原理。",
    reasoning={"effort": "high"},
)
print(response.output_text)
```

```javascript
import OpenAI from 'openai';

const client = new OpenAI({ apiKey: 'YOUR_API_KEY', baseURL: 'https://tokenhub.tencentmaas.com/v1' });

const response = await client.responses.create({
  model: '<your-model-name>',
  input: '请解释量子纠缠的基本原理。',
  reasoning: { effort: 'high' },
});
console.log(response.output_text);
```

```java
import okhttp3.*;

public class Reasoning {
    public static void main(String[] args) throws Exception {
        String body = """
        {
          "model": "<your-model-name>",
          "input": "请解释量子纠缠的基本原理。",
          "reasoning": {
            "effort": "high"
          }
        }
        """;

        Request request = new Request.Builder()
            .url("https://tokenhub.tencentmaas.com/v1/responses")
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
  "input": "请解释量子纠缠的基本原理。",
  "reasoning": {
    "effort": "high"
  }
}`

    req, _ := http.NewRequest("POST",
        "https://tokenhub.tencentmaas.com/v1/responses",
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

### 过滤器类型

用于文件搜索工具的 `filters` 字段。

**ComparisonFilter（比较过滤器）：**将指定属性键与给定值进行比较。

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `key` | string | 要比较的属性键 |
| `type` | `"eq"` / `"ne"` / `"gt"` / `"gte"` / `"lt"` / `"lte"` / `"in"` / `"nin"` | 比较操作符 |
| `value` | string / number / boolean / array | 要比较的值 |

**CompoundFilter（复合过滤器）：**使用 `and` 或 `or` 组合多个过滤器。

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `type` | `"and"` / `"or"` | 操作类型 |
| `filters` | array | 要组合的过滤器数组（ComparisonFilter 或 CompoundFilter） |
