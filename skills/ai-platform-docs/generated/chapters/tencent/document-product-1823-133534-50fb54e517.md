<!-- Official source: https://cloud.tencent.com/document/product/1823/133534 -->
<!-- Source SHA-256: 1a71b939e0f9f5725b1ae8c9f3ed63068d6494273cd293ab86dfd0aefd75df57 -->

# 保留式思考模式（Preserved Thinking）

官方来源：https://cloud.tencent.com/document/product/1823/133534
最近更新时间：2026-07-06 14:11:45

## 功能概述

保留式思考模式（Preserved Thinking）将模型的思考内容（`reasoning_content`）的保留范围从“同一个用户提问轮内”进一步扩展到“跨用户提问轮”。当用户在后续轮次继续追问时，先前的推理草稿仍可保留并延续，从而在 Agent、Coding 等长流程、多轮任务中保持推理连续性、提升模型效果，并因上下文前缀更稳定而提高缓存命中率、节省 token。

#### **适用场景**

适用于慢思考（`low` / `high`）+ 工具调用（tool call）的**跨轮次**场景，例如：

Agent 长流程任务：多轮工具编排与信息汇总；

Coding 类任务：多轮代码补全 / 修改 / 调试，需延续上一轮的推理路径；

多轮对话中含追问：用户在同一会话中提出关联问题，需要模型基于先前思考继续回答。

此场景下的调用模式如下图所示：

![](https://qcloudimg.tencent-cloud.cn/image/document/12ca18116600ca33f80cebc2d6609234.png)

#### 与交错式思考的差异

两者均围绕“保留 `reasoning_content` 以延续思维链”这一核心机制，主要差异在于**保留的范围**不同。开发者对两种模式的操作方式是一致的——都是把模型返回的 `reasoning_content` 原样回填到下一次请求。

| 概念 | 思考内容的保留范围 | 通俗理解 |
| --- | --- | --- |
| 交错式思考（Interleaved） | 同一个用户提问轮（User turn）内 | 类似做同一道题时中途查资料：模型先写一段解题草稿，开发者在工具结果返回时把这份草稿原样带回，模型才能接着刚才的思路继续做。本轮结束后，下一轮用户提问不再带回这道题的草稿。 |
| 保留式思考（Preserved） | 跨用户提问轮（User turn） | 类似把每道题的解题草稿都收好：后续用户继续追问时，开发者把相关历史草稿原样带回请求里，模型继续参考回答。 |

关于交错式思考的完整说明，请参见 [交错式思考模式（Interleaved Thinking）](https://cloud.tencent.com/document/product/1823/130930)。

#### **支持模型与协议**

**支持模型**：`hy3`

**支持协议**：OpenAI Chat Completions、OpenAI Responses、Anthropic 三种协议均支持，开关方式略有差异（详见下文“开关方式”）。

## 开关方式

保留式思考支持通过参数显式开启或关闭，各协议开关字段如下：

| 协议 | 开关方式 | 参考示例 |
| --- | --- | --- |
| OpenAI Chat Completions | 请求体顶层字段 `preserved_thinking` | `{"reasoning_effort":"high","preserved_thinking":true}` |
| OpenAI Responses | `reasoning` 对象内字段 `preserved_thinking` | `{"reasoning":{"effort":"high","preserved_thinking":true}}` |
| Anthropic | 请求头 `HY-Preserved-Thinking`  取值为 `true` / `false` / 为空或不传：明确传 `true` 为开启、`false` 为关闭；为空或不传时采用 API 默认策略；传入非法值会报错。 | `HY-Preserved-Thinking: true` |

**建议****：**

1. 如无特殊需求，不建议手动传 `preserved_thinking`，平台会自动采用最优策略处理。

请求携带 `tools`（工具调用场景）时：**默认开启**保留式思考。

请求未携带 `tools`（纯文本对话场景）时：**默认关闭**。

2. 仅在下述特殊情形下再考虑手动开启：工具定义未通过标准 `tools` 数组注册（如写在 system prompt 中），此时平台无法自动识别为工具调用场景，可手动设置 `preserved_thinking: true`。更推荐的做法是仍将工具按标准方式注册到 `tools` 数组中，既能复用平台策略，也能获得最佳的模型效果。

## 字段回填要求

**注意：**

`preserved_thinking` 参数仅控制保留式思考的**启停**，不会自动处理历史 `reasoning_content` 的**回填**。开发者需要将模型上一轮返回的完整、未经修改的 `reasoning_content` 与工具结果一并原样回填给 API，否则可能影响模型效果，并降低缓存命中率。

#### **常用字段**

以 Chat Completions 协议为例：

| 字段 | 位置 | 说明 |
| --- | --- | --- |
| `reasoning_effort` | 请求 | 思考深度，取值 `no_think` / `low` / `high` |
| `preserved_thinking` | 请求 | 保留式思考开关，`true` / `false`。不传时由平台按默认策略处理 |
| `reasoning_content` | 响应（需回填） | 模型的思考过程，需在后续请求中原样回填 |
| `tool_calls` | 响应（需回填） | 模型输出的工具调用指令 |
| `content` | 响应 | 最终回答内容 |

#### **回填规则（务必遵守）**

**原样回填**：回填的 `reasoning_content` 必须与模型生成时完全一致，不要改写、截断或重新排序，否则会降低效果并影响缓存命中率。

**跟随对应的 assistant 消息**：把 `reasoning_content` 放回它所属的那条 `assistant` 消息中（与 `content`、`tool_calls` 同级）。

**持续保留**：在拿到最终回答前的每一次请求，都要带上历史的 `reasoning_content`。

## 调用流程

以 Chat Completions 协议为例，在慢思考 + 工具调用场景下，建议严格遵循此调用流程：

**step1**：发起首次请求（包含 system/user 内容与 `tools` 列表），保留式思考默认开启。

**step2**：API 输出 assistant 消息，其中可能包含：

`reasoning_content`

`tool_calls`

**step3**：业务方执行工具。

**step4**：将工具结果以 `role=tool` 回填，并将上一步 assistant 消息（含 `reasoning_content` 与 `tool_calls`）原样加入 `messages` 数组，再次发起请求。

**step5**：模型可能继续发起新的 tool call，或输出最终答案。若继续 tool call，则重复 step3~4。

**step6**：用户发起下一轮追问时（跨用户提问轮），**同样需要将此前所有轮次的 assistant 消息（含** `reasoning_content`**）原样保留在** `messages` **中**，这是保留式思考与交错式思考最核心的差异。

## 调用示例（慢思考 + 多步工具调用）

以下以 Chat Completions 协议为例，提供一个简单的保留式思考示例。

**场景**：一个企业 IT 权限助理 Agent，提供两个工具：`get_user_groups`（查用户所属的组）、`get_group_permissions`（查某个组对各资源的权限）。用户分三轮提问，每一轮都保留此前轮的思考：

第 1 轮用户输入：`Alice 属于哪些用户组？`

第 2 轮用户输入：`这些组分别有什么权限？`

第 3 轮用户输入：`综合看，Alice 对"生产数据库"到底是什么权限？`

**说明：**

1. 对于保留式思考，通常难以在简单任务上产生显著效果增益（在多轮、长流程的复杂任务上，保留式思考的效果和成本增益会更加显著），因此此示例仅用于演示跨轮调用的使用方式。

2. 请您将示例代码中的 `YOUR_API_KEY` 替换为您真实的 API Key。如您还没有 API Key，请参见 [创建 API Key](https://cloud.tencent.com/document/product/1823/130090#40882178-aaf2-48c9-8559-dffc083a79bc)。

### 1. 首次请求（用户第一次提问）

**请求：**

cURL

Python

Node.js

Java

Go

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/chat/completions' \\
  -H 'Content-Type: application/json' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -d '{
    "model": "hy3",
    "stream": false,
    "reasoning_effort": "high",
    "tool_choice": "auto",
    "messages": [
      { "role": "system", "content": "你是一个企业 IT 权限助理 Agent，通过调用工具查询组织与权限数据来回答问题。请始终用中文进行逐步推理与思考。" },
      { "role": "user",   "content": "Alice 属于哪些用户组？" }
    ],
    "tools": [
      {
        "type": "function",
        "function": {
          "name": "get_user_groups",
          "description": "查询某个用户所属的所有用户组。",
          "parameters": {
            "type": "object",
            "properties": {
              "user": { "type": "string" }
            },
            "required": ["user"]
          }
        }
      },
      {
        "type": "function",
        "function": {
          "name": "get_group_permissions",
          "description": "查询某个用户组对各资源的访问权限。",
          "parameters": {
            "type": "object",
            "properties": {
              "group": { "type": "string" }
            },
            "required": ["group"]
          }
        }
      }
    ]
  }'
```

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_user_groups",
            "description": "查询某个用户所属的所有用户组。",
            "parameters": {
                "type": "object",
                "properties": {
                    "user": {"type": "string"},
                },
                "required": ["user"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_group_permissions",
            "description": "查询某个用户组对各资源的访问权限。",
            "parameters": {
                "type": "object",
                "properties": {
                    "group": {"type": "string"},
                },
                "required": ["group"],
            },
        },
    },
]

messages = [
    {"role": "system", "content": "你是一个企业 IT 权限助理 Agent，通过调用工具查询组织与权限数据来回答问题。请始终用中文进行逐步推理与思考。"},
    {"role": "user", "content": "Alice 属于哪些用户组？"},
]

# 携带 tools 时，hy3 默认开启保留式思考。
# 如需显式控制，可在 extra_body 中传 preserved_thinking: True/False
resp1 = client.chat.completions.create(
    model="hy3",
    messages=messages,
    tools=tools,
    tool_choice="auto",
    extra_body={"reasoning_effort": "high"},
)
msg1 = resp1.choices[0].message
print("第 1 轮 reasoning_content:", getattr(msg1, "reasoning_content", ""))
print("第 1 轮 tool_calls:", msg1.tool_calls)
```

```javascript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: 'YOUR_API_KEY',
  baseURL: 'https://tokenhub.tencentmaas.com/v1',
});

const tools = [
  {
    type: 'function',
    function: {
      name: 'get_user_groups',
      description: '查询某个用户所属的所有用户组。',
      parameters: {
        type: 'object',
        properties: {
          user: { type: 'string' },
        },
        required: ['user'],
      },
    },
  },
  {
    type: 'function',
    function: {
      name: 'get_group_permissions',
      description: '查询某个用户组对各资源的访问权限。',
      parameters: {
        type: 'object',
        properties: {
          group: { type: 'string' },
        },
        required: ['group'],
      },
    },
  },
];

const messages = [
  { role: 'system', content: '你是一个企业 IT 权限助理 Agent，通过调用工具查询组织与权限数据来回答问题。请始终用中文进行逐步推理与思考。' },
  { role: 'user', content: 'Alice 属于哪些用户组？' },
];

const resp1 = await client.chat.completions.create({
  model: 'hy3',
  messages,
  tools,
  tool_choice: 'auto',
  reasoning_effort: 'high',
});

const msg1 = resp1.choices[0].message;
console.log('第 1 轮 reasoning_content:', msg1.reasoning_content);
console.log('第 1 轮 tool_calls:', msg1.tool_calls);
```

```java
import okhttp3.*;
import com.google.gson.*;
import java.util.*;

public class PreservedThinking {
    static final String URL = "https://tokenhub.tencentmaas.com/v1/chat/completions";
    static final String API_KEY = "YOUR_API_KEY";
    static final OkHttpClient HTTP = new OkHttpClient();
    static final Gson GSON = new Gson();

    /** 通用 chat 调用，返回原始 JSON 响应字符串。 */
    static String chat(List<Map<String, Object>> messages, List<Map<String, Object>> tools) throws Exception {
        Map<String, Object> body = new HashMap<>();
        body.put("model", "hy3");
        body.put("messages", messages);
        body.put("tools", tools);
        body.put("tool_choice", "auto");
        body.put("reasoning_effort", "high");
        body.put("stream", false);
        // 显式控制可加：body.put("preserved_thinking", true);

        Request req = new Request.Builder()
            .url(URL)
            .header("Authorization", "Bearer " + API_KEY)
            .post(RequestBody.create(GSON.toJson(body), MediaType.parse("application/json")))
            .build();
        try (Response resp = HTTP.newCall(req).execute()) {
            return resp.body().string();
        }
    }

    public static void main(String[] args) throws Exception {
        List<Map<String, Object>> tools = List.of(
            Map.of(
                "type", "function",
                "function", Map.of(
                    "name", "get_user_groups",
                    "description", "查询某个用户所属的所有用户组。",
                    "parameters", Map.of(
                        "type", "object",
                        "properties", Map.of(
                            "user", Map.of("type", "string")
                        ),
                        "required", List.of("user")
                    )
                )
            ),
            Map.of(
                "type", "function",
                "function", Map.of(
                    "name", "get_group_permissions",
                    "description", "查询某个用户组对各资源的访问权限。",
                    "parameters", Map.of(
                        "type", "object",
                        "properties", Map.of(
                            "group", Map.of("type", "string")
                        ),
                        "required", List.of("group")
                    )
                )
            )
        );

        List<Map<String, Object>> messages = new ArrayList<>();
        messages.add(Map.of("role", "system", "content", "你是一个企业 IT 权限助理 Agent，通过调用工具查询组织与权限数据来回答问题。请始终用中文进行逐步推理与思考。"));
        messages.add(Map.of("role", "user",   "content", "Alice 属于哪些用户组？"));

        // 第 1 轮：模型决定是否调用工具
        String r1 = chat(messages, tools);
        System.out.println("第 1 轮响应：" + r1);
        // 后续按响应里的 reasoning_content / tool_calls 回填到 messages，见第 2 步
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

const (
    URL    = "https://tokenhub.tencentmaas.com/v1/chat/completions"
    APIKEY = "YOUR_API_KEY"
)

// 通用 chat 调用
func chat(messages []map[string]interface{}, tools []map[string]interface{}) (map[string]interface{}, error) {
    body, _ := json.Marshal(map[string]interface{}{
        "model":            "hy3",
        "messages":         messages,
        "tools":            tools,
        "tool_choice":      "auto",
        "reasoning_effort": "high",
        "stream":           false,
        // 显式控制可加："preserved_thinking": true,
    })
    req, _ := http.NewRequest("POST", URL, bytes.NewBuffer(body))
    req.Header.Set("Authorization", "Bearer "+APIKEY)
    req.Header.Set("Content-Type", "application/json")
    resp, err := http.DefaultClient.Do(req)
    if err != nil {
        return nil, err
    }
    defer resp.Body.Close()
    data, _ := io.ReadAll(resp.Body)
    var out map[string]interface{}
    json.Unmarshal(data, &out)
    return out, nil
}

func main() {
    tools := []map[string]interface{}{
        {
            "type": "function",
            "function": map[string]interface{}{
                "name":        "get_user_groups",
                "description": "查询某个用户所属的所有用户组。",
                "parameters": map[string]interface{}{
                    "type": "object",
                    "properties": map[string]interface{}{
                        "user": map[string]string{"type": "string"},
                    },
                    "required": []string{"user"},
                },
            },
        },
        {
            "type": "function",
            "function": map[string]interface{}{
                "name":        "get_group_permissions",
                "description": "查询某个用户组对各资源的访问权限。",
                "parameters": map[string]interface{}{
                    "type": "object",
                    "properties": map[string]interface{}{
                        "group": map[string]string{"type": "string"},
                    },
                    "required": []string{"group"},
                },
            },
        },
    }

    messages := []map[string]interface{}{
        {"role": "system", "content": "你是一个企业 IT 权限助理 Agent，通过调用工具查询组织与权限数据来回答问题。请始终用中文进行逐步推理与思考。"},
        {"role": "user", "content": "Alice 属于哪些用户组？"},
    }

    // 第 1 轮：模型决定是否调用工具
    r1, _ := chat(messages, tools)
    fmt.Printf("第 1 轮响应: %+v\\n", r1)
    // 后续按响应里的 reasoning_content / tool_calls 回填到 messages，见第 2 步
}
```

**响应：**模型先思考，并决定调用 `get_user_groups`。

```json
{
    "id": "REPLACED_ID",
    "object": "chat.completion",
    "created": 1783084572,
    "model": "hy3",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "我来查询 Alice 所属的用户组。",
                "reasoning_content": "用户问 Alice 属于哪些用户组。我需要调用 get_user_groups 工具来查询 Alice 所属的用户组。只有一个调用，没有依赖。",
                "tool_calls": [
                    {
                        "id": "chatcmpl-tool-93cc85d5f381f88d",
                        "type": "function",
                        "function": {
                            "name": "get_user_groups",
                            "arguments": "{\\"user\\": \\"Alice\\"}"
                        }
                    }
                ]
            },
            "finish_reason": "tool_calls"
        }
    ],
    "usage": {
        "prompt_tokens": 289,
        "completion_tokens": 60,
        "total_tokens": 349,
        "completion_tokens_details": { "reasoning_tokens": 31 }
    }
}
```

### 2. 回填工具结果，延续思考

把上一步 assistant 消息（含 `reasoning_content`）与工具结果一起回填。假设 `get_user_groups` 返回 `["Engineering","OnCall"]`：

**请求：**

cURL

Python

Node.js

Java

Go

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/chat/completions' \\
  -H 'Content-Type: application/json' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -d '{
    "model": "hy3",
    "stream": false,
    "reasoning_effort": "high",
    "tool_choice": "auto",
    "messages": [
      { "role": "system", "content": "你是一个企业 IT 权限助理 Agent，通过调用工具查询组织与权限数据来回答问题。请始终用中文进行逐步推理与思考。" },
      { "role": "user",   "content": "Alice 属于哪些用户组？" },
      { "role": "assistant", "content": "我来查询 Alice 所属的用户组。",
        "reasoning_content": "用户问 Alice 属于哪些用户组。我需要调用 get_user_groups 工具来查询 Alice 所属的用户组。只有一个调用，没有依赖。",
        "tool_calls": [
          { "id": "chatcmpl-tool-93cc85d5f381f88d", "type": "function",
            "function": { "name": "get_user_groups", "arguments": "{\\"user\\": \\"Alice\\"}" } }
        ] },
      { "role": "tool", "tool_call_id": "chatcmpl-tool-93cc85d5f381f88d",
        "content": "{\\"user\\": \\"Alice\\", \\"groups\\": [\\"Engineering\\", \\"OnCall\\"]}" }
    ],
    "tools": [ /* 同上，省略 */ ]
  }'
```

```python
# 接续 step1：把第 1 轮的 assistant 消息（含 reasoning_content + tool_calls）
# 与工具结果一起回填到 messages
import json

# 第 1 轮 assistant 消息的回写：reasoning_content 必须保留
assistant_msg = {
    "role": "assistant",
    "content": msg1.content or "",
    "reasoning_content": getattr(msg1, "reasoning_content", ""),
    "tool_calls": [
        {
            "id": tc.id,
            "type": tc.type,
            "function": {
                "name": tc.function.name,
                "arguments": tc.function.arguments,
            },
        } for tc in (msg1.tool_calls or [])
    ],
}
messages.append(assistant_msg)

# 业务侧执行 get_user_groups，把结果以 role=tool 回填
for tc in (msg1.tool_calls or []):
    # 这里替换为真实业务逻辑
    tool_result = json.dumps({"user": "Alice", "groups": ["Engineering", "OnCall"]}, ensure_ascii=False)
    messages.append({
        "role": "tool",
        "tool_call_id": tc.id,
        "content": tool_result,
    })

# 第 2 轮：把工具结果送回模型，模型继续思考
resp2 = client.chat.completions.create(
    model="hy3",
    messages=messages,
    tools=tools,
    tool_choice="auto",
    extra_body={"reasoning_effort": "high"},
)
msg2 = resp2.choices[0].message
print("第 2 轮 reasoning_content:", getattr(msg2, "reasoning_content", ""))
print("第 2 轮 content:", msg2.content)
```

```javascript
// 接续 step1：把第 1 轮 assistant 消息与工具结果回填
const assistantMsg = {
  role: 'assistant',
  content: msg1.content || '',
  reasoning_content: msg1.reasoning_content,
  tool_calls: msg1.tool_calls,
};
messages.push(assistantMsg);

for (const tc of msg1.tool_calls || []) {
  // 这里替换为真实业务逻辑
  const toolResult = JSON.stringify({ user: 'Alice', groups: ['Engineering', 'OnCall'] });
  messages.push({
    role: 'tool',
    tool_call_id: tc.id,
    content: toolResult,
  });
}

const resp2 = await client.chat.completions.create({
  model: 'hy3',
  messages,
  tools,
  tool_choice: 'auto',
  reasoning_effort: 'high',
});
const msg2 = resp2.choices[0].message;
console.log('第 2 轮 reasoning_content:', msg2.reasoning_content);
console.log('第 2 轮 content:', msg2.content);
```

```java
// 接续 main()：把第 1 轮 assistant 消息与工具结果回填，再发起第 2 轮请求
// 完整流程示意（仅展示消息构造，HTTP 调用复用 chat() 函数）

// 1. 解析第 1 轮响应
JsonObject r1Obj = JsonParser.parseString(r1).getAsJsonObject();
JsonObject msg1 = r1Obj.getAsJsonArray("choices").get(0).getAsJsonObject()
    .getAsJsonObject("message");

// 2. 把 assistant 消息（含 reasoning_content）整体回写到 messages
Map<String, Object> assistantEntry = new LinkedHashMap<>();
assistantEntry.put("role", "assistant");
assistantEntry.put("content", msg1.has("content") ? msg1.get("content").getAsString() : "");
if (msg1.has("reasoning_content")) {
    assistantEntry.put("reasoning_content", msg1.get("reasoning_content").getAsString());
}
if (msg1.has("tool_calls")) {
    assistantEntry.put("tool_calls", GSON.fromJson(msg1.get("tool_calls"), List.class));
}
messages.add(assistantEntry);

// 3. 业务侧执行 get_user_groups，把结果以 role=tool 回填
for (JsonElement el : msg1.getAsJsonArray("tool_calls")) {
    JsonObject call = el.getAsJsonObject();
    // 这里替换为真实业务逻辑
    String toolResult = "{\\"user\\": \\"Alice\\", \\"groups\\": [\\"Engineering\\", \\"OnCall\\"]}";
    messages.add(Map.of(
        "role", "tool",
        "tool_call_id", call.get("id").getAsString(),
        "content", toolResult
    ));
}

// 4. 第 2 轮：把工具结果送回模型
String r2 = chat(messages, tools);
System.out.println("第 2 轮响应：" + r2);
```

```go
// 接续 main()：把第 1 轮 assistant 消息与工具结果回填，再发起第 2 轮请求

// 1. 从第 1 轮响应中取出 assistant 消息
msg1Wrap := r1["choices"].([]interface{})[0].(map[string]interface{})
msg1 := msg1Wrap["message"].(map[string]interface{})

// 2. 把 assistant 消息（含 reasoning_content）整体回写到 messages
messages = append(messages, msg1)

// 3. 业务侧执行 get_user_groups，把结果以 role=tool 回填
toolCalls, _ := msg1["tool_calls"].([]interface{})
for _, c := range toolCalls {
    call := c.(map[string]interface{})
    // 这里替换为真实业务逻辑
    toolResult := `{"user": "Alice", "groups": ["Engineering", "OnCall"]}`
    messages = append(messages, map[string]interface{}{
        "role":         "tool",
        "tool_call_id": call["id"],
        "content":      toolResult,
    })
}

// 4. 第 2 轮：把工具结果送回模型
r2, _ := chat(messages, tools)
fmt.Printf("第 2 轮响应: %+v\\n", r2)
```

**响应：**模型本轮回答完成，`finish_reason=stop`：

```json
{
    "id": "REPLACED_ID",
    "object": "chat.completion",
    "created": 1783084576,
    "model": "hy3",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "根据查询结果，Alice 属于以下两个用户组：\\n\\n- **Engineering**\\n- **OnCall**\\n\\n所以 Alice 同时是 Engineering 组和 OnCall 组的成员。",
                "reasoning_content": "根据工具返回结果，Alice 属于 Engineering 和 OnCall 两个用户组。"
            },
            "finish_reason": "stop"
        }
    ],
    "usage": {
        "prompt_tokens": 375,
        "completion_tokens": 54,
        "total_tokens": 429,
        "prompt_tokens_details": { "cached_tokens": 320 },
        "completion_tokens_details": { "reasoning_tokens": 18 }
    }
}
```

### 3. 新一轮用户提问，保留此前思考

追加第 2 个 user 提问，并把此前轮次的 `reasoning_content` 等上下文原样保留再次发起请求：

**请求：**

cURL

Python

Node.js

Java

Go

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/chat/completions' \\
  -H 'Content-Type: application/json' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -d '{
    "model": "hy3",
    "stream": false,
    "reasoning_effort": "high",
    "tool_choice": "auto",
    "messages": [
      { "role": "system", "content": "你是一个企业 IT 权限助理 Agent，通过调用工具查询组织与权限数据来回答问题。请始终用中文进行逐步推理与思考。" },
      { "role": "user",   "content": "Alice 属于哪些用户组？" },
      { "role": "assistant", "content": "我来查询 Alice 所属的用户组。",
        "reasoning_content": "用户问 Alice 属于哪些用户组。我需要调用 get_user_groups 工具来查询 Alice 所属的用户组。只有一个调用，没有依赖。",
        "tool_calls": [
          { "id": "chatcmpl-tool-93cc85d5f381f88d", "type": "function",
            "function": { "name": "get_user_groups", "arguments": "{\\"user\\": \\"Alice\\"}" } }
        ] },
      { "role": "tool", "tool_call_id": "chatcmpl-tool-93cc85d5f381f88d",
        "content": "{\\"user\\": \\"Alice\\", \\"groups\\": [\\"Engineering\\", \\"OnCall\\"]}" },
      { "role": "assistant",
        "content": "根据查询结果，Alice 属于以下两个用户组：\\n\\n- **Engineering**\\n- **OnCall**\\n\\n所以 Alice 同时是 Engineering 组和 OnCall 组的成员。",
        "reasoning_content": "根据工具返回结果，Alice 属于 Engineering 和 OnCall 两个用户组。" },
      { "role": "user", "content": "这些组分别有哪些资源的访问权限？" }
    ],
    "tools": [ /* 同上，省略 */ ]
  }'
```

```python
# 接续 step2：把第 2 轮 assistant 消息（含 reasoning_content）追加到 messages，
# 然后追加第 2 轮用户提问，再次发起请求
messages.append({
    "role": "assistant",
    "content": msg2.content or "",
    "reasoning_content": getattr(msg2, "reasoning_content", ""),
})
messages.append({"role": "user", "content": "这些组分别有哪些资源的访问权限？"})

resp3 = client.chat.completions.create(
    model="hy3",
    messages=messages,
    tools=tools,
    tool_choice="auto",
    extra_body={"reasoning_effort": "high"},
)
msg3 = resp3.choices[0].message
print("第 3 轮 reasoning_content:", getattr(msg3, "reasoning_content", ""))
print("第 3 轮 tool_calls:", msg3.tool_calls)
```

```javascript
// 接续 step2：把第 2 轮 assistant 消息（含 reasoning_content）追加到 messages，
// 然后追加第 2 轮用户提问，再次发起请求
messages.push({
  role: 'assistant',
  content: msg2.content || '',
  reasoning_content: msg2.reasoning_content,
});
messages.push({ role: 'user', content: '这些组分别有哪些资源的访问权限？' });

const resp3 = await client.chat.completions.create({
  model: 'hy3',
  messages,
  tools,
  tool_choice: 'auto',
  reasoning_effort: 'high',
});
const msg3 = resp3.choices[0].message;
console.log('第 3 轮 reasoning_content:', msg3.reasoning_content);
console.log('第 3 轮 tool_calls:', msg3.tool_calls);
```

```java
// 接续第 2 轮响应 r2：把第 2 轮 assistant 消息（含 reasoning_content）追加到 messages
JsonObject r2Obj = JsonParser.parseString(r2).getAsJsonObject();
JsonObject msg2 = r2Obj.getAsJsonArray("choices").get(0).getAsJsonObject()
    .getAsJsonObject("message");

Map<String, Object> assistant2 = new LinkedHashMap<>();
assistant2.put("role", "assistant");
assistant2.put("content", msg2.has("content") ? msg2.get("content").getAsString() : "");
if (msg2.has("reasoning_content")) {
    assistant2.put("reasoning_content", msg2.get("reasoning_content").getAsString());
}
messages.add(assistant2);

// 追加第 2 轮用户提问
messages.add(Map.of("role", "user", "content", "这些组分别有哪些资源的访问权限？"));

// 第 3 轮：把新提问送回模型
String r3 = chat(messages, tools);
System.out.println("第 3 轮响应：" + r3);
```

```go
// 接续第 2 轮响应 r2：把第 2 轮 assistant 消息（含 reasoning_content）追加到 messages
msg2Wrap := r2["choices"].([]interface{})[0].(map[string]interface{})
msg2 := msg2Wrap["message"].(map[string]interface{})
messages = append(messages, msg2)

// 追加第 2 轮用户提问
messages = append(messages, map[string]interface{}{
    "role":    "user",
    "content": "这些组分别有哪些资源的访问权限？",
})

// 第 3 轮：把新提问送回模型
r3, _ := chat(messages, tools)
fmt.Printf("第 3 轮响应: %+v\\n", r3)
```

**响应：**模型延续之前的思路，发起 `get_group_permissions` 调用（本轮并行发起两个工具调用）：

```json
{
    "id": "REPLACED_ID",
    "object": "chat.completion",
    "created": 1783084580,
    "model": "hy3",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "我来查询这两个用户组各自的资源访问权限。",
                "reasoning_content": "用户想知道 Alice 所属的两个组（Engineering 和 OnCall）分别有哪些资源的访问权限。我需要调用 get_group_permissions 工具来查询这两个组的权限。这两个调用之间没有依赖关系，可以同时进行。",
                "tool_calls": [
                    {
                        "id": "chatcmpl-tool-83653bb310744682",
                        "type": "function",
                        "function": {
                            "name": "get_group_permissions",
                            "arguments": "{\\"group\\": \\"Engineering\\"}"
                        }
                    },
                    {
                        "id": "chatcmpl-tool-b2ee9d73aef14658",
                        "type": "function",
                        "function": {
                            "name": "get_group_permissions",
                            "arguments": "{\\"group\\": \\"OnCall\\"}"
                        }
                    }
                ]
            },
            "finish_reason": "tool_calls"
        }
    ],
    "usage": {
        "prompt_tokens": 440,
        "completion_tokens": 94,
        "total_tokens": 534,
        "prompt_tokens_details": { "cached_tokens": 400 },
        "completion_tokens_details": { "reasoning_tokens": 44 }
    }
}
```

### 4. 再次回填工具结果

回填工具结果（假设 Engineering：生产库只读；OnCall：生产库读写）：

**请求：**

cURL

Python

Node.js

Java

Go

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/chat/completions' \\
  -H 'Content-Type: application/json' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -d '{
    "model": "hy3",
    "stream": false,
    "reasoning_effort": "high",
    "tool_choice": "auto",
    "messages": [
      /* …前 6 条消息同上，保留全部 reasoning_content，省略… */
      { "role": "assistant", "content": "我来查询这两个用户组各自的资源访问权限。",
        "reasoning_content": "用户想知道 Alice 所属的两个组（Engineering 和 OnCall）分别有哪些资源的访问权限。……这两个调用之间没有依赖关系，可以同时进行。",
        "tool_calls": [
          { "id": "chatcmpl-tool-83653bb310744682", "type": "function",
            "function": { "name": "get_group_permissions", "arguments": "{\\"group\\": \\"Engineering\\"}" } },
          { "id": "chatcmpl-tool-b2ee9d73aef14658", "type": "function",
            "function": { "name": "get_group_permissions", "arguments": "{\\"group\\": \\"OnCall\\"}" } }
        ] },
      { "role": "tool", "tool_call_id": "chatcmpl-tool-83653bb310744682",
        "content": "{\\"group\\": \\"Engineering\\", \\"permissions\\": [{\\"resource\\": \\"生产数据库\\", \\"access\\": \\"read-only\\"}, {\\"resource\\": \\"staging环境\\", \\"access\\": \\"read-write\\"}, {\\"resource\\": \\"内部Wiki\\", \\"access\\": \\"read-write\\"}]}" },
      { "role": "tool", "tool_call_id": "chatcmpl-tool-b2ee9d73aef14658",
        "content": "{\\"group\\": \\"OnCall\\", \\"permissions\\": [{\\"resource\\": \\"告警系统\\", \\"access\\": \\"read-write\\"}, {\\"resource\\": \\"生产数据库\\", \\"access\\": \\"read-write\\"}]}" }
    ],
    "tools": [ /* 同上，省略 */ ]
  }'
```

```python
# 接续 step3：把第 3 轮的 assistant 消息（含 reasoning_content + tool_calls）回写，
# 然后对两个 tool_call 并行回填工具结果
import json

assistant_msg3 = {
    "role": "assistant",
    "content": msg3.content or "",
    "reasoning_content": getattr(msg3, "reasoning_content", ""),
    "tool_calls": [
        {
            "id": tc.id,
            "type": tc.type,
            "function": {
                "name": tc.function.name,
                "arguments": tc.function.arguments,
            },
        } for tc in (msg3.tool_calls or [])
    ],
}
messages.append(assistant_msg3)

# 业务侧并行执行 get_group_permissions，把两个结果依次回填
tool_results = {
    "Engineering": {
        "group": "Engineering",
        "permissions": [
            {"resource": "生产数据库", "access": "read-only"},
            {"resource": "staging环境", "access": "read-write"},
            {"resource": "内部Wiki", "access": "read-write"},
        ],
    },
    "OnCall": {
        "group": "OnCall",
        "permissions": [
            {"resource": "告警系统", "access": "read-write"},
            {"resource": "生产数据库", "access": "read-write"},
        ],
    },
}
for tc in (msg3.tool_calls or []):
    args = json.loads(tc.function.arguments)
    result = tool_results[args["group"]]
    messages.append({
        "role": "tool",
        "tool_call_id": tc.id,
        "content": json.dumps(result, ensure_ascii=False),
    })

# 第 4 轮：把两个工具结果一起送回模型
resp4 = client.chat.completions.create(
    model="hy3",
    messages=messages,
    tools=tools,
    tool_choice="auto",
    extra_body={"reasoning_effort": "high"},
)
msg4 = resp4.choices[0].message
print("第 4 轮 reasoning_content:", getattr(msg4, "reasoning_content", ""))
print("第 4 轮 content:", msg4.content)
```

```javascript
// 接续 step3：把第 3 轮 assistant 消息与两个工具结果回填
messages.push({
  role: 'assistant',
  content: msg3.content || '',
  reasoning_content: msg3.reasoning_content,
  tool_calls: msg3.tool_calls,
});

// 业务侧并行执行 get_group_permissions
const toolResults = {
  Engineering: {
    group: 'Engineering',
    permissions: [
      { resource: '生产数据库', access: 'read-only' },
      { resource: 'staging环境', access: 'read-write' },
      { resource: '内部Wiki', access: 'read-write' },
    ],
  },
  OnCall: {
    group: 'OnCall',
    permissions: [
      { resource: '告警系统', access: 'read-write' },
      { resource: '生产数据库', access: 'read-write' },
    ],
  },
};
for (const tc of msg3.tool_calls || []) {
  const args = JSON.parse(tc.function.arguments);
  messages.push({
    role: 'tool',
    tool_call_id: tc.id,
    content: JSON.stringify(toolResults[args.group]),
  });
}

const resp4 = await client.chat.completions.create({
  model: 'hy3',
  messages,
  tools,
  tool_choice: 'auto',
  reasoning_effort: 'high',
});
const msg4 = resp4.choices[0].message;
console.log('第 4 轮 reasoning_content:', msg4.reasoning_content);
console.log('第 4 轮 content:', msg4.content);
```

```java
// 接续第 3 轮响应 r3：把 assistant 消息（含 reasoning_content + tool_calls）回写
JsonObject r3Obj = JsonParser.parseString(r3).getAsJsonObject();
JsonObject msg3 = r3Obj.getAsJsonArray("choices").get(0).getAsJsonObject()
    .getAsJsonObject("message");

Map<String, Object> assistant3 = new LinkedHashMap<>();
assistant3.put("role", "assistant");
assistant3.put("content", msg3.has("content") ? msg3.get("content").getAsString() : "");
if (msg3.has("reasoning_content")) {
    assistant3.put("reasoning_content", msg3.get("reasoning_content").getAsString());
}
if (msg3.has("tool_calls")) {
    assistant3.put("tool_calls", GSON.fromJson(msg3.get("tool_calls"), List.class));
}
messages.add(assistant3);

// 业务侧并行执行 get_group_permissions
Map<String, String> toolResults = Map.of(
    "Engineering", "{\\"group\\": \\"Engineering\\", \\"permissions\\": [{\\"resource\\": \\"生产数据库\\", \\"access\\": \\"read-only\\"}, {\\"resource\\": \\"staging环境\\", \\"access\\": \\"read-write\\"}, {\\"resource\\": \\"内部Wiki\\", \\"access\\": \\"read-write\\"}]}",
    "OnCall",      "{\\"group\\": \\"OnCall\\", \\"permissions\\": [{\\"resource\\": \\"告警系统\\", \\"access\\": \\"read-write\\"}, {\\"resource\\": \\"生产数据库\\", \\"access\\": \\"read-write\\"}]}"
);
for (JsonElement el : msg3.getAsJsonArray("tool_calls")) {
    JsonObject call = el.getAsJsonObject();
    JsonObject args = JsonParser.parseString(
        call.getAsJsonObject("function").get("arguments").getAsString()
    ).getAsJsonObject();
    String group = args.get("group").getAsString();
    messages.add(Map.of(
        "role", "tool",
        "tool_call_id", call.get("id").getAsString(),
        "content", toolResults.get(group)
    ));
}

// 第 4 轮：把两个工具结果一起送回模型
String r4 = chat(messages, tools);
System.out.println("第 4 轮响应：" + r4);
```

```go
// 接续第 3 轮响应 r3：把 assistant 消息（含 reasoning_content + tool_calls）回写
msg3Wrap := r3["choices"].([]interface{})[0].(map[string]interface{})
msg3 := msg3Wrap["message"].(map[string]interface{})
messages = append(messages, msg3)

// 业务侧并行执行 get_group_permissions
toolResults := map[string]string{
    "Engineering": `{"group": "Engineering", "permissions": [{"resource": "生产数据库", "access": "read-only"}, {"resource": "staging环境", "access": "read-write"}, {"resource": "内部Wiki", "access": "read-write"}]}`,
    "OnCall":      `{"group": "OnCall", "permissions": [{"resource": "告警系统", "access": "read-write"}, {"resource": "生产数据库", "access": "read-write"}]}`,
}
toolCalls, _ := msg3["tool_calls"].([]interface{})
for _, c := range toolCalls {
    call := c.(map[string]interface{})
    fn := call["function"].(map[string]interface{})
    var args map[string]interface{}
    json.Unmarshal([]byte(fn["arguments"].(string)), &args)
    group := args["group"].(string)
    messages = append(messages, map[string]interface{}{
        "role":         "tool",
        "tool_call_id": call["id"],
        "content":      toolResults[group],
    })
}

// 第 4 轮：把两个工具结果一起送回模型
r4, _ := chat(messages, tools)
fmt.Printf("第 4 轮响应: %+v\\n", r4)
```

**响应：**模型完成本轮回答，`finish_reason=stop`：

```json
{
    "id": "REPLACED_ID",
    "object": "chat.completion",
    "created": 1783084585,
    "model": "hy3",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "根据查询结果，这两个用户组的资源访问权限如下：\\n\\n**Engineering 组**\\n- 生产数据库：只读（read-only）\\n- staging环境：读写（read-write）\\n- 内部Wiki：读写（read-write）\\n\\n**OnCall 组**\\n- 告警系统：读写（read-write）\\n- 生产数据库：读写（read-write）\\n\\n**补充说明：** 两个组都对「生产数据库」拥有权限，但级别不同——Engineering 是只读，而 OnCall 是读写。因为 Alice 同时属于这两个组，所以她实际对生产数据库能享有最高级别的**读写**权限。",
                "reasoning_content": "现在我有了两个组的权限信息：\\n\\nEngineering 组：\\n- 生产数据库: read-only\\n- staging环境: read-write\\n- 内部Wiki: read-write\\n\\nOnCall 组：\\n- 告警系统: read-write\\n- 生产数据库: read-write\\n\\n我需要整理这些信息并回答用户。注意两个组对生产数据库都有权限，但 Engineering 是 read-only，OnCall 是 read-write。由于 Alice 同时属于两个组，实际上她对生产数据库的实际权限应该取并集/最高权限，即 read-write……"
            },
            "finish_reason": "stop"
        }
    ],
    "usage": {
        "prompt_tokens": 641,
        "completion_tokens": 266,
        "total_tokens": 907,
        "prompt_tokens_details": { "cached_tokens": 512 },
        "completion_tokens_details": { "reasoning_tokens": 140 }
    }
}
```

### 5. 再次发起新一轮用户提问（保留式思考的核心价值）

追加第 3 个 user 提问。此时完整的 `messages` 数组如下，注意**每工具轮的** `reasoning_content` **等内容都被原样保留**：

```json
[
  { "role": "system", "content": "你是一个企业 IT 权限助理 Agent……请始终用中文进行逐步推理与思考。" },
  { "role": "user", "content": "Alice 属于哪些用户组？" },
  { "role": "assistant", "content": "我来查询 Alice 所属的用户组。",
    "reasoning_content": "用户问 Alice 属于哪些用户组……只有一个调用，没有依赖。",
    "tool_calls": [ { "id": "chatcmpl-tool-93cc85d5f381f88d", "type": "function",
      "function": { "name": "get_user_groups", "arguments": "{\\"user\\": \\"Alice\\"}" } } ] },
  { "role": "tool", "tool_call_id": "chatcmpl-tool-93cc85d5f381f88d",
    "content": "{\\"user\\": \\"Alice\\", \\"groups\\": [\\"Engineering\\", \\"OnCall\\"]}" },
  { "role": "assistant", "content": "根据查询结果，Alice 属于以下两个用户组：……",
    "reasoning_content": "根据工具返回结果，Alice 属于 Engineering 和 OnCall 两个用户组。" },
  { "role": "user", "content": "这些组分别有哪些资源的访问权限？" },
  { "role": "assistant", "content": "我来查询这两个用户组各自的资源访问权限。",
    "reasoning_content": "……这两个调用之间没有依赖关系，可以同时进行。",
    "tool_calls": [
      { "id": "chatcmpl-tool-83653bb310744682", "type": "function",
        "function": { "name": "get_group_permissions", "arguments": "{\\"group\\": \\"Engineering\\"}" } },
      { "id": "chatcmpl-tool-b2ee9d73aef14658", "type": "function",
        "function": { "name": "get_group_permissions", "arguments": "{\\"group\\": \\"OnCall\\"}" } } ] },
  { "role": "tool", "tool_call_id": "chatcmpl-tool-83653bb310744682",
    "content": "{\\"group\\": \\"Engineering\\", \\"permissions\\": [{\\"resource\\": \\"生产数据库\\", \\"access\\": \\"read-only\\"}, …]}" },
  { "role": "tool", "tool_call_id": "chatcmpl-tool-b2ee9d73aef14658",
    "content": "{\\"group\\": \\"OnCall\\", \\"permissions\\": [{\\"resource\\": \\"生产数据库\\", \\"access\\": \\"read-write\\"}, …]}" },
  { "role": "assistant", "content": "根据查询结果，这两个用户组的资源访问权限如下：……（含各组权限表）",
    "reasoning_content": "现在我有了两个组的权限信息：\\nEngineering 组：\\n- 生产数据库: read-only …\\nOnCall 组：\\n- 生产数据库: read-write …" },

  // 👇 用户第 3 个提问轮：综合追问
  { "role": "user", "content": "那么综合来看，Alice 对『生产数据库』到底拥有什么级别的访问权限？" }
]
```

**响应：**模型不再重复调用工具，直接把前两轮思考里积累的中间结论链起来（`Alice ∈ {Engineering, OnCall}` → 推导出两组对生产库的权限为「只读 / 读写」→ 取最高权限 → 即读写权限）：

```json
{
    "id": "REPLACED_ID",
    "object": "chat.completion",
    "created": 1783084590,
    "model": "hy3",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "基于前面查询到的信息，我可以直接综合判断，无需再次调用工具：\\n\\n- **Engineering 组** → 生产数据库：只读（read-only）\\n- **OnCall 组** → 生产数据库：读写（read-write）\\n\\n由于 Alice **同时属于** Engineering 和 OnCall 两个组，当多个组对同一资源拥有不同级别的权限时，通常取**最高级别**（权限取并集）。\\n\\n因此，综合来看，Alice 对「生产数据库」拥有 **读写（read-write）** 级别的访问权限。",
                "reasoning_content": "用户问 Alice 对生产数据库的综合访问权限。根据之前的查询结果：\\n\\n- Engineering 组：生产数据库 - read-only（只读）\\n- OnCall 组：生产数据库 - read-write（读写）\\n\\nAlice 同时属于这两个组。综合来看，她应该拥有最高级别的权限，即读写（read-write）。……我不需要再调用工具，因为之前已经获得了所有必要信息。我可以基于已有数据直接回答。"
            },
            "finish_reason": "stop"
        }
    ],
    "usage": {
        "prompt_tokens": 925,
        "completion_tokens": 283,
        "total_tokens": 1208,
        "prompt_tokens_details": { "cached_tokens": 624 },
        "completion_tokens_details": { "reasoning_tokens": 139 }
    }
}
```

## 常见问题

### 需要手动传 `preserved_thinking` 吗？

一般**不需要**。若无特殊需求，建议不传，平台会自动采用最优策略——请求携带 `tools` 时默认开启，纯文本对话默认关闭。仅在"工具未通过标准 `tools` 数组注册"等特殊情形下才需要手动设置为 `true`。

### 开启保留式思考后，一定要回填历史 `reasoning_content` 吗？

**是**。`preserved_thinking` 仅控制启停，不会自动处理历史思考的回填。开发者需要将模型上一轮返回的完整、未经修改的 `reasoning_content` 与工具结果一并原样带回，否则可能影响模型效果并降低缓存命中率。

### 从 `hy3-preview` 升级到 `hy3` 需要改造代码吗？

若业务角度无需求变化则**无需改造**，API 链路内已实现兼容。仅需注意：若希望利用保留式思考的跨轮次能力，需要把此前所有轮次的 assistant 消息（含 `reasoning_content`）都保留在 `messages` 数组中。

### `reasoning_content` 回填时可以做摘要压缩吗？

**不建议**。回填的 `reasoning_content` 必须与模型生成时完全一致，不要改写、截断或重新排序，否则会降低模型效果并影响缓存命中率。

### 保留式思考会显著增加 token 消耗吗？

从单次请求 body 长度来看会略有增加，但由于上下文前缀更稳定，**缓存命中率显著提升**，在多轮长流程任务下整体 token 成本通常会**下降**，同时响应延迟也会降低。
