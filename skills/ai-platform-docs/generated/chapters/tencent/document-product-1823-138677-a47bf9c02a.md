<!-- Official source: https://cloud.tencent.com/document/product/1823/138677 -->
<!-- Source SHA-256: 1febc1a9ffc911d1d623160d6d2ec6c5e1ee12e62a290330f4ec8540f79789b9 -->

# Xiaomi MiMo 调用指南

官方来源：https://cloud.tencent.com/document/product/1823/138677
最近更新时间：2026-09-23 22:30:01

## 概述

Xiaomi MiMo 系列模型已接入大模型服务平台 TokenHub，同时支持 OpenAI Chat Completions、OpenAI Responses 与 Anthropic Messages 三种协议，开发者无需更换 SDK 即可快速接入。本文介绍通用调用示例以及 MiMo 特有的思考模式、Function Calling、结构化输出等核心能力。

**注意：**

TokenHub 当前上线的所有 MiMo 模型，该模型默认开启深度思考。若在多轮工具调用场景中开启思考模式，建议完整回传历史 `reasoning_content` 以保持最佳效果；TokenHub 侧缺失该字段不会报错，但可能影响模型表现，详见本文 [多轮工具调用回传 reasoning\_content](https://cloud.tencent.com/document/product/1823/138677#694005b4-5365-4049-ba25-8cc9d6c73d9f)。

## 支持的模型

TokenHub 当前支持以下 MiMo 模型（具体以 [模型列表](https://cloud.tencent.com/document/product/1823/130051) 为准）：

<table><colgroup><col/><col/><col/><col/><col/><col/></colgroup><tbody><tr><td><div>模型 ID</div></td><td><div>类型</div></td><td><div>思考能力</div></td><td><div>上下文窗口</div></td><td><div>最大输入</div></td><td><div>最大输出</div></td></tr><tr><td><div><code>mimo-v2.6-pro</code></div></td><td><div>通用全模态模型（文本输入、图片输入、视频输入 / 文本输出）</div></td><td><div>支持（默认开启，可关闭）</div></td><td><div>1M</div></td><td><div>1M</div></td><td><div>128K</div></td></tr><tr><td colspan="1" rowspan="1"><div><code>mimo-v2.6-flash</code></div></td><td colspan="1" rowspan="1"><div>通用全模态模型（文本输入、图片输入、视频输入 / 文本输出）</div></td><td colspan="1" rowspan="1"><div>支持（默认开启，可关闭）</div></td><td colspan="1" rowspan="1"><div>1M</div></td><td colspan="1" rowspan="1"><div>1M</div></td><td colspan="1" rowspan="1"><div>128K</div></td></tr><tr><td colspan="1" rowspan="1"><div><code>mimo-v2.5-pro</code></div></td><td colspan="1" rowspan="1"><div>通用对话模型（文本输入 / 文本输出）</div></td><td colspan="1" rowspan="1"><div>支持（默认开启，可关闭）</div></td><td colspan="1" rowspan="1"><div>1M</div></td><td colspan="1" rowspan="1"><div>1M</div></td><td colspan="1" rowspan="1"><div>128K</div></td></tr></tbody></table>

模型主要能力：深度思考、Function Calling、结构化输出、Cache 缓存、流式输出。

MiMo 模型对三种协议的支持情况请参见 [语言模型调用概览](https://cloud.tencent.com/document/product/1823/130079#cef303de-23e1-4983-93b0-76542729ef10)。

## 前提条件

已注册腾讯云账号并开通 TokenHub 服务。

已在 [TokenHub 控制台](https://console.cloud.tencent.com/tokenhub/apikey) 获取 API Key。

已根据所用语言安装对应 SDK 或具备 HTTP 请求能力。

## 协议与接入地址

**Base URL（按接入地域二选一）**

广州：`https://tokenhub.tencentmaas.com/v1`

新加坡：`https://tokenhub-intl.tencentmaas.com/v1`

**协议路径与认证方式**

| 协议 | 路径 | 适用 SDK | 认证请求头 |
| --- | --- | --- | --- |
| OpenAI Chat Completions | `/v1/chat/completions` | OpenAI SDK 及兼容客户端 | `Authorization: Bearer YOUR_API_KEY` |
| OpenAI Responses | `/v1/responses` | OpenAI SDK（Responses 接口） | `Authorization: Bearer YOUR_API_KEY` |
| Anthropic Messages | `/v1/messages` | Anthropic SDK 及兼容客户端 | `x-api-key: YOUR_API_KEY` |

**说明：**

本文示例默认使用广州地域与 OpenAI Chat Completions 协议，新加坡地域只需替换 Base URL。Responses 与 Anthropic 协议的调用方式参见本文 [Anthropic Messages 协议调用](https://cloud.tencent.com/document/product/1823/138677#d62bb863-01d5-4cff-a628-36203b8f7504)、[Responses API 协议调用](https://cloud.tencent.com/document/product/1823/138677#06a80903-c4ae-49aa-9358-f433d6d0966e)，完整字段说明请参见 [OpenAI Chat Completions 协议字段说明](https://cloud.tencent.com/document/product/1823/135872)、[OpenAI Response 协议字段说明](https://cloud.tencent.com/document/product/1823/135873)、[Anthropic Message 协议字段说明](https://cloud.tencent.com/document/product/1823/135874)。

## 快速开始

以下示例展示最简单的单轮对话调用，请将 `YOUR_API_KEY` 替换为您创建的 API Key。

cURL

Python

Node.js

Java

Go

```bash
curl https://tokenhub.tencentmaas.com/v1/chat/completions \\
  -H "Content-Type: application/json" \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -d '{
    "model": "mimo-v2.5-pro",
    "messages": [
      {"role": "user", "content": "你好，请介绍一下你自己"}
    ],
    "max_tokens": 2048
  }'
```

```python
# pip install openai
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

response = client.chat.completions.create(
    model="mimo-v2.5-pro",
    messages=[
        {"role": "user", "content": "你好，请介绍一下你自己"}
    ],
    max_tokens=2048,
)
print(response.choices[0].message.content)
```

```javascript
// npm install openai
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "YOUR_API_KEY",
  baseURL: "https://tokenhub.tencentmaas.com/v1",
});

const response = await client.chat.completions.create({
  model: "mimo-v2.5-pro",
  messages: [
    { role: "user", content: "你好，请介绍一下你自己" }
  ],
  max_tokens: 2048,
});
console.log(response.choices[0].message.content);
```

```java
// 使用 OkHttp，添加依赖：implementation("com.squareup.okhttp3:okhttp:4.12.0")
import okhttp3.*;
import org.json.*;

OkHttpClient httpClient = new OkHttpClient();

JSONObject body = new JSONObject();
body.put("model", "mimo-v2.5-pro");
body.put("max_tokens", 2048);
JSONArray messages = new JSONArray();
messages.put(new JSONObject().put("role", "user").put("content", "你好，请介绍一下你自己"));
body.put("messages", messages);

Request request = new Request.Builder()
    .url("https://tokenhub.tencentmaas.com/v1/chat/completions")
    .addHeader("Authorization", "Bearer YOUR_API_KEY")
    .addHeader("Content-Type", "application/json")
    .post(RequestBody.create(body.toString(), MediaType.get("application/json")))
    .build();

try (Response response = httpClient.newCall(request).execute()) {
    JSONObject result = new JSONObject(response.body().string());
    System.out.println(result.getJSONArray("choices")
        .getJSONObject(0).getJSONObject("message").getString("content"));
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
    body := map[string]interface{}{
        "model": "mimo-v2.5-pro",
        "messages": []map[string]string{
            {"role": "user", "content": "你好，请介绍一下你自己"},
        },
        "max_tokens": 2048,
    }
    data, _ := json.Marshal(body)

    req, _ := http.NewRequest("POST",
        "https://tokenhub.tencentmaas.com/v1/chat/completions",
        bytes.NewBuffer(data))
    req.Header.Set("Authorization", "Bearer YOUR_API_KEY")
    req.Header.Set("Content-Type", "application/json")

    resp, _ := http.DefaultClient.Do(req)
    defer resp.Body.Close()
    respBody, _ := io.ReadAll(resp.Body)

    var result map[string]interface{}
    json.Unmarshal(respBody, &result)
    choices := result["choices"].([]interface{})
    msg := choices[0].(map[string]interface{})["message"].(map[string]interface{})
    fmt.Println(msg["content"])
}
```

## 通用调用示例

### 基础对话

发送单轮对话请求，获取模型回复。

cURL

Python

Node.js

Java

Go

```bash
curl https://tokenhub.tencentmaas.com/v1/chat/completions \\
  -H "Content-Type: application/json" \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -d '{
    "model": "mimo-v2.5-pro",
    "messages": [
      {"role": "user", "content": "介绍一下大语言模型"}
    ],
    "max_tokens": 2048
  }'
```

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

response = client.chat.completions.create(
    model="mimo-v2.5-pro",
    messages=[
        {"role": "user", "content": "介绍一下大语言模型"}
    ],
    max_tokens=2048,
)
print(response.choices[0].message.content)
```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "YOUR_API_KEY",
  baseURL: "https://tokenhub.tencentmaas.com/v1",
});

const response = await client.chat.completions.create({
  model: "mimo-v2.5-pro",
  messages: [
    { role: "user", content: "介绍一下大语言模型" }
  ],
  max_tokens: 2048,
});
console.log(response.choices[0].message.content);
```

```java
import okhttp3.*;
import org.json.*;

OkHttpClient httpClient = new OkHttpClient();

JSONObject body = new JSONObject();
body.put("model", "mimo-v2.5-pro");
body.put("max_tokens", 2048);
body.put("messages", new JSONArray()
    .put(new JSONObject().put("role", "user").put("content", "介绍一下大语言模型")));

Request request = new Request.Builder()
    .url("https://tokenhub.tencentmaas.com/v1/chat/completions")
    .addHeader("Authorization", "Bearer YOUR_API_KEY")
    .addHeader("Content-Type", "application/json")
    .post(RequestBody.create(body.toString(), MediaType.get("application/json")))
    .build();

try (Response response = httpClient.newCall(request).execute()) {
    JSONObject result = new JSONObject(response.body().string());
    System.out.println(result.getJSONArray("choices")
        .getJSONObject(0).getJSONObject("message").getString("content"));
}
```

```go
body := map[string]interface{}{
    "model": "mimo-v2.5-pro",
    "messages": []map[string]string{
        {"role": "user", "content": "介绍一下大语言模型"},
    },
    "max_tokens": 2048,
}
// ... 其余请求代码同快速开始示例
```

### 流式输出

将 `stream` 设置为 `true` 开启 SSE 流式输出。MiMo-V2.5-Pro 默认开启深度思考，响应耗时相对较长，建议长文本或复杂推理场景统一开启流式输出，避免请求超时。

cURL

Python

Node.js

Java

Go

```bash
curl https://tokenhub.tencentmaas.com/v1/chat/completions \\
  -H "Content-Type: application/json" \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -d '{
    "model": "mimo-v2.5-pro",
    "messages": [
      {"role": "user", "content": "写一首关于春天的短诗"}
    ],
    "max_tokens": 2048,
    "stream": true
  }'
```

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

stream = client.chat.completions.create(
    model="mimo-v2.5-pro",
    messages=[
        {"role": "user", "content": "写一首关于春天的短诗"}
    ],
    max_tokens=2048,
    stream=True,
)

for chunk in stream:
    if chunk.choices and chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "YOUR_API_KEY",
  baseURL: "https://tokenhub.tencentmaas.com/v1",
});

const stream = await client.chat.completions.create({
  model: "mimo-v2.5-pro",
  messages: [
    { role: "user", content: "写一首关于春天的短诗" }
  ],
  max_tokens: 2048,
  stream: true,
});

for await (const chunk of stream) {
  const content = chunk.choices[0]?.delta?.content;
  if (content) process.stdout.write(content);
}
```

```java
import okhttp3.*;
import okhttp3.sse.*;
import org.json.*;

OkHttpClient httpClient = new OkHttpClient();

JSONObject body = new JSONObject();
body.put("model", "mimo-v2.5-pro");
body.put("max_tokens", 2048);
body.put("stream", true);
body.put("messages", new JSONArray()
    .put(new JSONObject().put("role", "user").put("content", "写一首关于春天的短诗")));

Request request = new Request.Builder()
    .url("https://tokenhub.tencentmaas.com/v1/chat/completions")
    .addHeader("Authorization", "Bearer YOUR_API_KEY")
    .addHeader("Content-Type", "application/json")
    .post(RequestBody.create(body.toString(), MediaType.get("application/json")))
    .build();

EventSources.createFactory(httpClient).newEventSource(request, new EventSourceListener() {
    @Override
    public void onEvent(EventSource source, String id, String type, String data) {
        if ("[DONE]".equals(data)) return;
        try {
            JSONObject json = new JSONObject(data);
            JSONObject delta = json.getJSONArray("choices").getJSONObject(0).getJSONObject("delta");
            String content = delta.optString("content", "");
            if (!content.isEmpty()) System.out.print(content);
        } catch (JSONException ignored) {}
    }
});
```

```go
import (
    "bufio"
    "bytes"
    "encoding/json"
    "fmt"
    "net/http"
    "strings"
)

body := map[string]interface{}{
    "model":      "mimo-v2.5-pro",
    "messages":   []map[string]string{{"role": "user", "content": "写一首关于春天的短诗"}},
    "max_tokens": 2048,
    "stream":     true,
}
data, _ := json.Marshal(body)

req, _ := http.NewRequest("POST",
    "https://tokenhub.tencentmaas.com/v1/chat/completions",
    bytes.NewBuffer(data))
req.Header.Set("Authorization", "Bearer YOUR_API_KEY")
req.Header.Set("Content-Type", "application/json")

resp, _ := http.DefaultClient.Do(req)
defer resp.Body.Close()

scanner := bufio.NewScanner(resp.Body)
for scanner.Scan() {
    line := scanner.Text()
    if !strings.HasPrefix(line, "data: ") || line == "data: [DONE]" {
        continue
    }
    var chunk map[string]interface{}
    json.Unmarshal([]byte(strings.TrimPrefix(line, "data: ")), &chunk)
    choices := chunk["choices"].([]interface{})
    delta := choices[0].(map[string]interface{})["delta"].(map[string]interface{})
    if content, ok := delta["content"].(string); ok {
        fmt.Print(content)
    }
}
```

### System Prompt

通过 `system` 角色消息设置模型的行为指令和背景信息。

**说明：**

建议在 `system` 消息中注入当前日期（可同时携带身份与角色说明），可提升时间类问题的回答准确度。通用模板如下（`{date}` 与 `{week}` 替换为实际日期与星期）：

`你是一位乐于助人的 AI 智能助手。今天的日期：{date} {week}。`

cURL

Python

Node.js

Java

Go

```bash
curl https://tokenhub.tencentmaas.com/v1/chat/completions \\
  -H "Content-Type: application/json" \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -d '{
    "model": "mimo-v2.5-pro",
    "messages": [
      {"role": "system", "content": "你是一位专业的 Python 编程助手，只回答与 Python 相关的问题，回答简洁明了。"},
      {"role": "user", "content": "如何读取一个 CSV 文件？"}
    ],
    "max_tokens": 2048
  }'
```

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

response = client.chat.completions.create(
    model="mimo-v2.5-pro",
    messages=[
        {
            "role": "system",
            "content": "你是一位专业的 Python 编程助手，只回答与 Python 相关的问题，回答简洁明了。",
        },
        {"role": "user", "content": "如何读取一个 CSV 文件？"},
    ],
    max_tokens=2048,
)
print(response.choices[0].message.content)
```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "YOUR_API_KEY",
  baseURL: "https://tokenhub.tencentmaas.com/v1",
});

const response = await client.chat.completions.create({
  model: "mimo-v2.5-pro",
  messages: [
    {
      role: "system",
      content: "你是一位专业的 Python 编程助手，只回答与 Python 相关的问题，回答简洁明了。",
    },
    { role: "user", content: "如何读取一个 CSV 文件？" },
  ],
  max_tokens: 2048,
});
console.log(response.choices[0].message.content);
```

```java
JSONObject body = new JSONObject();
body.put("model", "mimo-v2.5-pro");
body.put("max_tokens", 2048);
body.put("messages", new JSONArray()
    .put(new JSONObject().put("role", "system")
        .put("content", "你是一位专业的 Python 编程助手，只回答与 Python 相关的问题，回答简洁明了。"))
    .put(new JSONObject().put("role", "user")
        .put("content", "如何读取一个 CSV 文件？")));
// ... 发送请求代码同上
```

```go
body := map[string]interface{}{
    "model": "mimo-v2.5-pro",
    "messages": []map[string]string{
        {"role": "system", "content": "你是一位专业的 Python 编程助手，只回答与 Python 相关的问题，回答简洁明了。"},
        {"role": "user", "content": "如何读取一个 CSV 文件？"},
    },
    "max_tokens": 2048,
}
// ... 发送请求代码同快速开始
```

### 多轮对话

将历史消息一并传入 `messages` 数组，即可实现上下文记忆的多轮对话。

**说明：**

纯对话场景（历史消息中不含工具调用）只需回写 `content`，无需回写 `reasoning_content`，可有效减少 token 消耗；一旦历史消息中出现过工具调用，则建议完整回传 `reasoning_content` 以保持最佳效果，详见本文 [多轮工具调用回传 reasoning\_content](https://cloud.tencent.com/document/product/1823/138677#694005b4-5365-4049-ba25-8cc9d6c73d9f)。

cURL

Python

Node.js

Java

Go

```bash
curl https://tokenhub.tencentmaas.com/v1/chat/completions \\
  -H "Content-Type: application/json" \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -d '{
    "model": "mimo-v2.5-pro",
    "messages": [
      {"role": "user", "content": "我叫小明，我喜欢打篮球"},
      {"role": "assistant", "content": "你好，小明！打篮球是一项很棒的运动。"},
      {"role": "user", "content": "你还记得我的名字和爱好吗？"}
    ],
    "max_tokens": 2048
  }'
```

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

# 维护对话历史
conversation = [
    {"role": "system", "content": "你是一个友好的 AI 助手。"},
]

def chat(user_input):
    conversation.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="mimo-v2.5-pro",
        messages=conversation,
        max_tokens=2048,
    )
    reply = response.choices[0].message.content
    # 纯对话场景只回写 content，不回写 reasoning_content
    conversation.append({"role": "assistant", "content": reply})
    return reply

print(chat("我叫小明，我喜欢打篮球"))
print(chat("你还记得我的名字和爱好吗？"))
```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "YOUR_API_KEY",
  baseURL: "https://tokenhub.tencentmaas.com/v1",
});

const conversation = [
  { role: "system", content: "你是一个友好的 AI 助手。" },
];

async function chat(userInput) {
  conversation.push({ role: "user", content: userInput });
  const response = await client.chat.completions.create({
    model: "mimo-v2.5-pro",
    messages: conversation,
    max_tokens: 2048,
  });
  const reply = response.choices[0].message.content;
  conversation.push({ role: "assistant", content: reply });
  return reply;
}

console.log(await chat("我叫小明，我喜欢打篮球"));
console.log(await chat("你还记得我的名字和爱好吗？"));
```

```java
JSONArray messages = new JSONArray();
messages.put(new JSONObject().put("role", "system").put("content", "你是一个友好的 AI 助手。"));
messages.put(new JSONObject().put("role", "user").put("content", "我叫小明，我喜欢打篮球"));
messages.put(new JSONObject().put("role", "assistant").put("content", "你好，小明！打篮球是一项很棒的运动。"));
messages.put(new JSONObject().put("role", "user").put("content", "你还记得我的名字和爱好吗？"));

JSONObject body = new JSONObject();
body.put("model", "mimo-v2.5-pro");
body.put("messages", messages);
body.put("max_tokens", 2048);
// ... 发送请求代码同上
```

```go
body := map[string]interface{}{
    "model": "mimo-v2.5-pro",
    "messages": []map[string]string{
        {"role": "system", "content": "你是一个友好的 AI 助手。"},
        {"role": "user", "content": "我叫小明，我喜欢打篮球"},
        {"role": "assistant", "content": "你好，小明！打篮球是一项很棒的运动。"},
        {"role": "user", "content": "你还记得我的名字和爱好吗？"},
    },
    "max_tokens": 2048,
}
// ... 发送请求代码同快速开始
```

### Function Calling（工具调用）

Function Calling 允许模型调用外部工具获取实时数据。模型本身不执行函数，而是返回应调用的函数名和参数，由用户代码执行后将结果传回模型，最终得到自然语言回答。

**调用流程：**

1. 用户提问 → 模型返回 `tool_calls`（包含函数名和参数）。

2. 用户代码执行该函数 → 将结果以 `role: tool` 消息传回。

3. 模型根据函数结果生成最终自然语言回答。

**注意：**

`tool_choice` 仅支持 `auto`。传入其他值时该字段会被移除，模型行为等同于 `auto`。

工具函数名（`tools.function.name`）只能由 `a-z`、`A-Z`、`0-9`、下划线（`_`）、连字符（`-`）组成，最大长度为 64。

开启思考模式时，模型会在返回 `tool_calls` 的同时返回 `reasoning_content`，后续轮次建议完整回传以保持最佳效果（缺失不会报错，但可能影响模型表现）。

cURL

Python

Node.js

Java

Go

```bash
# 第一轮：发送问题 + 工具定义
curl https://tokenhub.tencentmaas.com/v1/chat/completions \\
  -H "Content-Type: application/json" \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -d '{
    "model": "mimo-v2.5-pro",
    "messages": [
      {"role": "user", "content": "北京今天天气怎么样？"}
    ],
    "tools": [{
      "type": "function",
      "function": {
        "name": "get_weather",
        "description": "获取指定城市的天气信息",
        "parameters": {
          "type": "object",
          "properties": {
            "city": {"type": "string", "description": "城市名称，如北京"}
          },
          "required": ["city"]
        }
      }
    }],
    "tool_choice": "auto"
  }'

# 第二轮：将工具执行结果传回（tool_call_id、reasoning_content 替换为第一轮实际返回值）
curl https://tokenhub.tencentmaas.com/v1/chat/completions \\
  -H "Content-Type: application/json" \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -d '{
    "model": "mimo-v2.5-pro",
    "messages": [
      {"role": "user", "content": "北京今天天气怎么样？"},
      {"role": "assistant", "content": "", "reasoning_content": "用户询问北京天气，需要调用 get_weather 工具获取实时数据。", "tool_calls": [{"id": "call_xxx", "type": "function", "function": {"name": "get_weather", "arguments": "{\\"city\\": \\"北京\\"}"}}]},
      {"role": "tool", "tool_call_id": "call_xxx", "content": "晴，气温28℃，湿度50%"}
    ],
    "tools": [{"type": "function", "function": {"name": "get_weather", "description": "获取指定城市的天气信息", "parameters": {"type": "object", "properties": {"city": {"type": "string"}}, "required": ["city"]}}}]
  }'
```

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

# 定义工具
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "获取指定城市的天气信息",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "城市名称，如北京"}
                },
                "required": ["city"],
            },
        },
    }
]

# 第一轮：发送问题
messages = [{"role": "user", "content": "北京今天天气怎么样？"}]
response = client.chat.completions.create(
    model="mimo-v2.5-pro",
    messages=messages,
    tools=tools,
    max_tokens=2048,
)
assistant_message = response.choices[0].message

# 模型发起工具调用
if response.choices[0].finish_reason == "tool_calls":
    tool_call = assistant_message.tool_calls[0]
    print(f"模型调用工具：{tool_call.function.name}，参数：{tool_call.function.arguments}")

    # 执行工具（此处为模拟返回）
    tool_result = "晴，气温28℃，湿度50%"

    # 第二轮：完整回传 assistant 消息（含 reasoning_content）+ 工具结果
    messages.append(assistant_message)
    messages.append({
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": tool_result,
    })

    final_response = client.chat.completions.create(
        model="mimo-v2.5-pro",
        messages=messages,
        tools=tools,
        max_tokens=2048,
    )
    print(final_response.choices[0].message.content)
```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "YOUR_API_KEY",
  baseURL: "https://tokenhub.tencentmaas.com/v1",
});

const tools = [
  {
    type: "function",
    function: {
      name: "get_weather",
      description: "获取指定城市的天气信息",
      parameters: {
        type: "object",
        properties: {
          city: { type: "string", description: "城市名称，如北京" },
        },
        required: ["city"],
      },
    },
  },
];

// 第一轮
const messages = [{ role: "user", content: "北京今天天气怎么样？" }];
const response1 = await client.chat.completions.create({
  model: "mimo-v2.5-pro",
  messages,
  tools,
  max_tokens: 2048,
});

const assistantMsg = response1.choices[0].message;
if (response1.choices[0].finish_reason === "tool_calls") {
  const toolCall = assistantMsg.tool_calls[0];
  console.log(`工具调用：${toolCall.function.name}，参数：${toolCall.function.arguments}`);

  const toolResult = "晴，气温28℃，湿度50%";
  // 原样回传 assistantMsg（含 reasoning_content），不要手动裁剪字段
  messages.push(assistantMsg);
  messages.push({ role: "tool", tool_call_id: toolCall.id, content: toolResult });

  const response2 = await client.chat.completions.create({
    model: "mimo-v2.5-pro",
    messages,
    tools,
    max_tokens: 2048,
  });
  console.log(response2.choices[0].message.content);
}
```

```java
JSONObject toolFunc = new JSONObject()
    .put("name", "get_weather")
    .put("description", "获取指定城市的天气信息")
    .put("parameters", new JSONObject()
        .put("type", "object")
        .put("properties", new JSONObject()
            .put("city", new JSONObject().put("type", "string").put("description", "城市名称")))
        .put("required", new JSONArray().put("city")));

JSONArray tools = new JSONArray()
    .put(new JSONObject().put("type", "function").put("function", toolFunc));

JSONObject body = new JSONObject();
body.put("model", "mimo-v2.5-pro");
body.put("messages", new JSONArray()
    .put(new JSONObject().put("role", "user").put("content", "北京今天天气怎么样？")));
body.put("tools", tools);
// ... 发送请求，解析 tool_calls 与 reasoning_content，执行工具，构造第二轮请求
```

```go
body := map[string]interface{}{
    "model": "mimo-v2.5-pro",
    "messages": []map[string]string{
        {"role": "user", "content": "北京今天天气怎么样？"},
    },
    "tools": []map[string]interface{}{{
        "type": "function",
        "function": map[string]interface{}{
            "name":        "get_weather",
            "description": "获取指定城市的天气信息",
            "parameters": map[string]interface{}{
                "type": "object",
                "properties": map[string]interface{}{
                    "city": map[string]string{"type": "string", "description": "城市名称"},
                },
                "required": []string{"city"},
            },
        },
    }},
}
// ... 发送请求，解析 tool_calls 与 reasoning_content，构造第二轮请求
```

## 思考模式

MiMo 系列模型，内置深度思考能力且**默认开启**。开启思考后，模型先通过内部思维链逐步分析问题，再输出最终答案，推理过程通过独立的 `reasoning_content` 字段返回，不与 `content` 混排。

### thinking 参数说明

| 字段 | 类型 | 默认值 | 取值范围 | 说明 |
| --- | --- | --- | --- | --- |
| `thinking.type` | string | `"enabled"` | `"enabled"` / `"disabled"` | `enabled`：开启深度思考，响应中返回 `reasoning_content`；`disabled`：关闭思考直接作答，响应更快、成本更低。 |

**注意：**

`thinking` 不是 OpenAI 标准参数。使用 OpenAI Python SDK 时需通过 `extra_body` 传入；Node.js SDK 可作为顶层参数传入。

开启思考模式时，`temperature` 与 `top_p` 不支持自定义，即使传入也会被强制采用推荐默认值 `1.0` 和 `0.95`。

`max_tokens` 限制的是思考内容与最终回答的**总长度**。思考过程较长时会压缩最终答案的可用空间，建议设置足够大的值（推荐 ≥ 2048）以避免回答被截断。

### 开启或关闭思考

cURL

Python

Node.js

Java

Go

```bash
# 关闭思考：直接作答，适合简单问答、格式转换等低延迟场景
curl https://tokenhub.tencentmaas.com/v1/chat/completions \\
  -H "Content-Type: application/json" \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -d '{
    "model": "mimo-v2.5-pro",
    "messages": [
      {"role": "user", "content": "用一句话解释什么是机器学习"}
    ],
    "max_tokens": 1024,
    "thinking": {"type": "disabled"}
  }'
```

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

# 开启思考（默认行为，此处显式声明）
response = client.chat.completions.create(
    model="mimo-v2.5-pro",
    messages=[{"role": "user", "content": "解方程 x^2 - 5x + 6 = 0"}],
    max_tokens=4096,
    extra_body={"thinking": {"type": "enabled"}},
)

msg = response.choices[0].message

# 获取推理过程（思考模式专属字段）
reasoning = getattr(msg, "reasoning_content", None)
if reasoning:
    print("=== 推理过程 ===")
    print(reasoning)

print("=== 最终答案 ===")
print(msg.content)

# 关闭思考
fast_response = client.chat.completions.create(
    model="mimo-v2.5-pro",
    messages=[{"role": "user", "content": "用一句话解释什么是机器学习"}],
    max_tokens=1024,
    extra_body={"thinking": {"type": "disabled"}},
)
print(fast_response.choices[0].message.content)
```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "YOUR_API_KEY",
  baseURL: "https://tokenhub.tencentmaas.com/v1",
});

const response = await client.chat.completions.create({
  model: "mimo-v2.5-pro",
  messages: [{ role: "user", content: "解方程 x^2 - 5x + 6 = 0" }],
  max_tokens: 4096,
  // @ts-ignore - thinking 为扩展字段
  thinking: { type: "enabled" },
});

const msg = response.choices[0].message;
const reasoning = (msg as any).reasoning_content;
if (reasoning) {
  console.log("=== 推理过程 ===");
  console.log(reasoning);
}
console.log("=== 最终答案 ===");
console.log(msg.content);
```

```java
JSONObject body = new JSONObject();
body.put("model", "mimo-v2.5-pro");
body.put("max_tokens", 4096);
body.put("thinking", new JSONObject().put("type", "enabled"));
body.put("messages", new JSONArray()
    .put(new JSONObject().put("role", "user").put("content", "解方程 x^2 - 5x + 6 = 0")));

// ... 发送请求
try (Response response = httpClient.newCall(request).execute()) {
    JSONObject result = new JSONObject(response.body().string());
    JSONObject message = result.getJSONArray("choices")
        .getJSONObject(0).getJSONObject("message");
    String reasoning = message.optString("reasoning_content", "");
    String content = message.getString("content");
    System.out.println("推理过程: " + reasoning);
    System.out.println("最终答案: " + content);
}
```

```go
body := map[string]interface{}{
    "model":      "mimo-v2.5-pro",
    "max_tokens": 4096,
    "thinking":   map[string]string{"type": "enabled"},
    "messages": []map[string]string{
        {"role": "user", "content": "解方程 x^2 - 5x + 6 = 0"},
    },
}
// ... 发送请求，从响应中解析 reasoning_content 和 content 字段
```

**注意：**

OpenAI SDK 的类型定义中没有 `reasoning_content` 字段，直接用属性访问会报错，必须通过安全取值方式读取：

Python：`getattr(msg, "reasoning_content", None)`

Node.js / TypeScript：`(msg as any).reasoning_content`

### 响应结构说明

开启思考时，推理过程在 `reasoning_content` 中返回，最终答案在 `content` 中返回。思考消耗的 token 计入 `usage.completion_tokens` 总量；当前 `usage.completion_tokens_details.reasoning_tokens` 恒为 `0`，无法单独拆分思考 token 用量：

```json
{
  "id": "2b92b0964c9b4335bffad7c2f75cfe9e",
  "choices": [{
    "index": 0,
    "message": {
      "role": "assistant",
      "reasoning_content": "这是一个一元二次方程，先尝试因式分解：(x-2)(x-3) = 0，所以 x = 2 或 x = 3。",
      "content": "方程 x² - 5x + 6 = 0 的解为：**x = 2** 或 **x = 3**",
      "tool_calls": null
    },
    "finish_reason": "stop"
  }],
  "model": "mimo-v2.5-pro",
  "object": "chat.completion",
  "usage": {
    "prompt_tokens": 25,
    "completion_tokens": 120,
    "total_tokens": 145,
    "completion_tokens_details": {
      "reasoning_tokens": 0
    },
    "prompt_tokens_details": {
      "cached_tokens": 0
    }
  }
}
```

关闭思考时，`reasoning_content` 不返回。

### 流式思考输出

开启流式输出时，`reasoning_content` 和 `content` 均以增量 delta 形式返回，且 `delta.reasoning_content` 一定先于 `delta.content` 出现，需分别处理：

Python

Node.js

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

stream = client.chat.completions.create(
    model="mimo-v2.5-pro",
    messages=[{"role": "user", "content": "分析一下量子计算的优势和挑战"}],
    max_tokens=4096,
    stream=True,
    extra_body={"thinking": {"type": "enabled"}},
)

print("=== 推理过程（实时）===")
answer_started = False

for chunk in stream:
    if not chunk.choices:
        continue
    delta = chunk.choices[0].delta

    reasoning_delta = getattr(delta, "reasoning_content", None)
    if reasoning_delta:
        print(reasoning_delta, end="", flush=True)

    if delta.content:
        if not answer_started:
            print("\\n\\n=== 最终答案（实时）===")
            answer_started = True
        print(delta.content, end="", flush=True)
```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "YOUR_API_KEY",
  baseURL: "https://tokenhub.tencentmaas.com/v1",
});

const stream = await client.chat.completions.create({
  model: "mimo-v2.5-pro",
  messages: [{ role: "user", content: "分析一下量子计算的优势和挑战" }],
  max_tokens: 4096,
  stream: true,
  // @ts-ignore
  thinking: { type: "enabled" },
});

let answerStarted = false;
process.stdout.write("=== 推理过程（实时）===\\n");

for await (const chunk of stream) {
  const delta = chunk.choices[0]?.delta;
  if (!delta) continue;

  const reasoning = (delta as any).reasoning_content;
  if (reasoning) process.stdout.write(reasoning);

  if (delta.content) {
    if (!answerStarted) {
      process.stdout.write("\\n\\n=== 最终答案（实时）===\\n");
      answerStarted = true;
    }
    process.stdout.write(delta.content);
  }
}
```

### 多轮工具调用回传 reasoning\_content

开启思考模式且历史会话中存在工具调用时，后续每一轮请求中带有 `tool_calls` 的 `assistant` 消息**建议完整回传** `reasoning_content` **字段**，以保持模型的最佳表现。实测在 TokenHub 侧缺失该字段不会导致接口报错，但小米官方建议回传，避免历史推理内容缺失造成上下文不完整。

**警告：**

历史 `reasoning_content` 一旦缺失，模型上下文将不完整，即使未直接报错也可能出现指令遵循能力下降、幻觉增多等现象。使用 OpenAI SDK 时，建议直接把响应返回的 `assistant` 消息对象原样追加到 `messages`，不要手动重建或裁剪字段。

正确的回传格式如下（`assistant` 消息同时携带 `content`、`reasoning_content` 与 `tool_calls`）：

```json
{
  "model": "mimo-v2.5-pro",
  "messages": [
    {"role": "user", "content": "北京今天天气怎么样？"},
    {
      "role": "assistant",
      "content": "",
      "reasoning_content": "用户询问北京天气，需要调用 get_weather 工具获取实时数据。",
      "tool_calls": [{
        "id": "call_xxx",
        "type": "function",
        "function": {"name": "get_weather", "arguments": "{\\"city\\": \\"北京\\"}"}
      }]
    },
    {"role": "tool", "tool_call_id": "call_xxx", "content": "晴，气温28℃，湿度50%"},
    {"role": "user", "content": "那明天呢？"}
  ]
}
```

**说明：**

通过 TRAE、Cursor、Codex、OpenClaw、OpenCode、Kilo Code 等 AI 编程工具接入时，工具侧一般已实现 `reasoning_content` 回传逻辑，无需额外处理；若自行开发 Agent 应用，请务必按上述格式处理。

## JSON 模式

设置 `response_format` 为 `json_object` 可以确保模型输出合法的 JSON 字符串，适合数据抽取、表单填充、分类打标等需要结构化数据的场景。

**注意：**

必须在 `system` 或 `user` 消息中明确要求模型只返回 JSON，并完整定义字段、层级与数据类型，否则可能导致输出不符合预期。

`response_format` 仅支持 `{"type": "json_object"}`，**不支持** `json_schema`。如需强校验结构，建议在业务侧配合 `jsonschema` 等库做二次校验并设计重试兜底。

注意合理设置 `max_tokens`，取值过小会导致 JSON 被截断而无法解析。

cURL

Python

Node.js

Java

Go

```bash
curl https://tokenhub.tencentmaas.com/v1/chat/completions \\
  -H "Content-Type: application/json" \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -d '{
    "model": "mimo-v2.5-pro",
    "messages": [
      {"role": "system", "content": "只返回 JSON，不要附带任何解释、注释或 Markdown 代码块。格式：{\\"cities\\": [{\\"name\\": string, \\"province\\": string, \\"population\\": number}]}"},
      {"role": "user", "content": "返回三座中国城市的信息"}
    ],
    "max_tokens": 2048,
    "response_format": {"type": "json_object"}
  }'
```

```python
import json
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

response = client.chat.completions.create(
    model="mimo-v2.5-pro",
    messages=[
        {
            "role": "system",
            "content": (
                "只返回 JSON，不要附带任何解释、注释或 Markdown 代码块。\\n"
                '格式：{"cities": [{"name": string, "province": string, "population": number}]}\\n'
                "未知字段请填充 null。"
            ),
        },
        {"role": "user", "content": "返回三座中国城市的信息"},
    ],
    max_tokens=2048,
    response_format={"type": "json_object"},
)

try:
    result = json.loads(response.choices[0].message.content)
    print(json.dumps(result, ensure_ascii=False, indent=2))
except json.JSONDecodeError as e:
    print(f"JSON 解析失败：{e}")
    print(f"原始内容：{response.choices[0].message.content}")
```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "YOUR_API_KEY",
  baseURL: "https://tokenhub.tencentmaas.com/v1",
});

const response = await client.chat.completions.create({
  model: "mimo-v2.5-pro",
  messages: [
    {
      role: "system",
      content:
        '只返回 JSON，不要附带任何解释、注释或 Markdown 代码块。格式：{"cities": [{"name": string, "province": string, "population": number}]}',
    },
    { role: "user", content: "返回三座中国城市的信息" },
  ],
  max_tokens: 2048,
  response_format: { type: "json_object" },
});

const result = JSON.parse(response.choices[0].message.content);
console.log(JSON.stringify(result, null, 2));
```

```java
JSONObject body = new JSONObject();
body.put("model", "mimo-v2.5-pro");
body.put("max_tokens", 2048);
body.put("response_format", new JSONObject().put("type", "json_object"));
body.put("messages", new JSONArray()
    .put(new JSONObject().put("role", "system").put("content", "只返回 JSON，不要附带任何解释。"))
    .put(new JSONObject().put("role", "user").put("content", "返回三座中国城市的信息")));
// ... 发送请求，解析返回的 JSON 字符串
```

```go
body := map[string]interface{}{
    "model":           "mimo-v2.5-pro",
    "max_tokens":      2048,
    "response_format": map[string]string{"type": "json_object"},
    "messages": []map[string]string{
        {"role": "system", "content": "只返回 JSON，不要附带任何解释。"},
        {"role": "user", "content": "返回三座中国城市的信息"},
    },
}
// ... 发送请求
```

## Anthropic Messages 协议调用

MiMo 系列模型支持 Anthropic Messages 协议，可直接使用 Anthropic SDK 或兼容客户端（Claude Code、OpenClaw、Cline 等）接入。

**注意：**

请求路径为 `/v1/messages`，认证请求头为 `x-api-key`（不是 `Authorization: Bearer`）。

Anthropic 协议下 `max_tokens` 为**必填**参数。

开启思考模式时同样建议在多轮工具调用中完整回传推理内容，规则参见本文 [多轮工具调用回传 reasoning\_content](https://cloud.tencent.com/document/product/1823/138677#694005b4-5365-4049-ba25-8cc9d6c73d9f)。

实测返回的 `content` 数组中 `text` block 在前、`thinking` block 在后（与 Claude 惯例相反），读取推理内容时请按 `type` 字段过滤，不要按下标取值。

cURL

Python

Node.js

Java

Go

```bash
curl https://tokenhub.tencentmaas.com/v1/messages \\
  -H "Content-Type: application/json" \\
  -H "x-api-key: YOUR_API_KEY" \\
  -H "anthropic-version: 2023-06-01" \\
  -d '{
    "model": "mimo-v2.5-pro",
    "max_tokens": 2048,
    "system": "你是一个专业的技术助手，回答简洁准确。",
    "messages": [
      {"role": "user", "content": "介绍一下 MoE 架构的优势"}
    ]
  }'
```

```python
# pip install anthropic
from anthropic import Anthropic

client = Anthropic(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com",
)

message = client.messages.create(
    model="mimo-v2.5-pro",
    max_tokens=2048,
    system="你是一个专业的技术助手，回答简洁准确。",
    messages=[
        {"role": "user", "content": "介绍一下 MoE 架构的优势"}
    ],
)
print(message.content[0].text)
```

```javascript
// npm install @anthropic-ai/sdk
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: "YOUR_API_KEY",
  baseURL: "https://tokenhub.tencentmaas.com",
});

const message = await client.messages.create({
  model: "mimo-v2.5-pro",
  max_tokens: 2048,
  system: "你是一个专业的技术助手，回答简洁准确。",
  messages: [
    { role: "user", content: "介绍一下 MoE 架构的优势" }
  ],
});
console.log(message.content[0].text);
```

```java
import okhttp3.*;
import org.json.*;

OkHttpClient httpClient = new OkHttpClient();

JSONObject body = new JSONObject();
body.put("model", "mimo-v2.5-pro");
body.put("max_tokens", 2048);
body.put("system", "你是一个专业的技术助手，回答简洁准确。");
body.put("messages", new JSONArray()
    .put(new JSONObject().put("role", "user").put("content", "介绍一下 MoE 架构的优势")));

Request request = new Request.Builder()
    .url("https://tokenhub.tencentmaas.com/v1/messages")
    .addHeader("x-api-key", "YOUR_API_KEY")
    .addHeader("anthropic-version", "2023-06-01")
    .addHeader("Content-Type", "application/json")
    .post(RequestBody.create(body.toString(), MediaType.get("application/json")))
    .build();

try (Response response = httpClient.newCall(request).execute()) {
    JSONObject result = new JSONObject(response.body().string());
    System.out.println(result.getJSONArray("content").getJSONObject(0).getString("text"));
}
```

```go
body := map[string]interface{}{
    "model":      "mimo-v2.5-pro",
    "max_tokens": 2048,
    "system":     "你是一个专业的技术助手，回答简洁准确。",
    "messages": []map[string]string{
        {"role": "user", "content": "介绍一下 MoE 架构的优势"},
    },
}
data, _ := json.Marshal(body)

req, _ := http.NewRequest("POST",
    "https://tokenhub.tencentmaas.com/v1/messages",
    bytes.NewBuffer(data))
req.Header.Set("x-api-key", "YOUR_API_KEY")
req.Header.Set("anthropic-version", "2023-06-01")
req.Header.Set("Content-Type", "application/json")
// ... 发送请求，从 content[0].text 读取回复
```

## Responses API 协议调用

MiMo 系列模型支持 OpenAI Responses 协议，可用于新版 Codex 等基于 Responses 接口的客户端接入。请求路径为 `/v1/responses`，认证方式与 Chat Completions 一致。

**说明：**

Responses 协议使用 `input` 传入对话内容、`max_output_tokens` 控制输出长度（与 Chat Completions 的 `messages`、`max_tokens` 相对应）。完整字段说明与兼容性范围请参见 [OpenAI Response 协议字段说明](https://cloud.tencent.com/document/product/1823/135873) 与 [Responses API 兼容模式说明](https://cloud.tencent.com/document/product/1823/133813)。

cURL

Python

Node.js

Java

Go

```bash
curl https://tokenhub.tencentmaas.com/v1/responses \\
  -H "Content-Type: application/json" \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -d '{
    "model": "mimo-v2.5-pro",
    "input": "介绍一下 MoE 架构的优势",
    "max_output_tokens": 2048
  }'
```

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

response = client.responses.create(
    model="mimo-v2.5-pro",
    input="介绍一下 MoE 架构的优势",
    max_output_tokens=2048,
)
print(response.output_text)
```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "YOUR_API_KEY",
  baseURL: "https://tokenhub.tencentmaas.com/v1",
});

const response = await client.responses.create({
  model: "mimo-v2.5-pro",
  input: "介绍一下 MoE 架构的优势",
  max_output_tokens: 2048,
});
console.log(response.output_text);
```

```java
JSONObject body = new JSONObject();
body.put("model", "mimo-v2.5-pro");
body.put("input", "介绍一下 MoE 架构的优势");
body.put("max_output_tokens", 2048);

Request request = new Request.Builder()
    .url("https://tokenhub.tencentmaas.com/v1/responses")
    .addHeader("Authorization", "Bearer YOUR_API_KEY")
    .addHeader("Content-Type", "application/json")
    .post(RequestBody.create(body.toString(), MediaType.get("application/json")))
    .build();
// ... 发送请求，从 output 数组中读取文本内容
```

```go
body := map[string]interface{}{
    "model":             "mimo-v2.5-pro",
    "input":             "介绍一下 MoE 架构的优势",
    "max_output_tokens": 2048,
}
data, _ := json.Marshal(body)

req, _ := http.NewRequest("POST",
    "https://tokenhub.tencentmaas.com/v1/responses",
    bytes.NewBuffer(data))
req.Header.Set("Authorization", "Bearer YOUR_API_KEY")
req.Header.Set("Content-Type", "application/json")
// ... 发送请求，从 output 数组中读取文本内容
```

## 与其他模型的关键差异

| 维度 | MiMo 系列模型 | OpenAI / Claude / GLM 等 |
| --- | --- | --- |
| 思考能力开关 | 通过 `thinking.type` 控制（`enabled`/`disabled`），默认开启 | 通常通过切换 model 或单独的 reasoning 参数控制 |
| 推理过程字段 | 独立 `reasoning_content` 字段返回，不嵌入 `content` | 多数模型不暴露推理过程 |
| OpenAI SDK 访问推理字段 | 必须用 `getattr` / `as any` | - |
| 思考模式下的采样参数 | `temperature`、`top_p` 不可自定义，强制为 `1.0` / `0.95` | 通常可自由设置 |
| `temperature` 范围 | 0-1.5，默认 1.0 | 通常 0-2 |
| `top_p` 范围 | 0.01-1.0，默认 0.95 | 通常 0-1 |
| 多轮工具调用回写 | 含工具调用时建议回写 `reasoning_content`（缺失不报错） | 通常只需回写 `content` |
| `tool_choice` | 仅支持 `auto` | 通常支持 `none`/`required`/指定函数 |
| 结构化输出 | 仅支持 `json_object` | 多数支持 `json_schema` |
| 上下文窗口 | 1M tokens | 通常 128K tokens |
| 最大输出 | 128K tokens | 通常 16K tokens |
| 多模态输入 | 不支持，仅文本输入 | 部分模型支持图片/视频 |

## 推荐参数与最佳实践

| 参数 / 实践 | 建议 | 说明 |
| --- | --- | --- |
| `max_tokens` | 普通任务 2048-4096；复杂推理建议 ≥ 8192 | 思考内容与最终答案共享 token 配额，取值过小会导致答案被截断 |
| `thinking.type` | 复杂推理、代码生成、Agent 任务保持默认 `enabled`；简单问答、格式转换改为 `disabled` | 关闭思考可显著降低延迟与成本 |
| `stream` | 开启思考时建议开启 | 思考耗时较长，流式可避免超时并实时呈现推理过程 |
| `temperature` | 关闭思考时可按需调整（创意写作 1.2-1.5，代码生成 0.2-0.5）；开启思考时无需设置 | 取值范围 0-1.5，思考模式下会被强制为 1.0 |
| `top_p` | 与 `temperature` 二选一，不建议同时调整 | 取值范围 0.01-1.0，默认 0.95 |
| System Prompt | 建议声明模型身份与当前日期 | 提升时间类问题准确度，模板参见本文「通用调用示例 > System Prompt」 |
| 多轮对话 | 纯对话只回写 `content`；含工具调用建议完整回写 `reasoning_content` | 前者节省 token，后者为官方最佳实践（缺失不报错） |
| SDK 访问推理字段 | Python 用 `getattr(msg, "reasoning_content", None)`；Node.js 用 `(msg as any).reasoning_content` | OpenAI SDK 类型定义中无此字段 |
| 上下文缓存 | 无需配置，自动生效 | 隐式缓存自动开启，命中量见 `usage.prompt_tokens_details.cached_tokens` |

## 使用限制

| 限制项 | 说明 |
| --- | --- |
| 思考模式采样参数 | 开启思考时不支持自定义 `temperature` 和 `top_p`，传入后实际生效值为 `1.0` 和 `0.95`。 |
| 多轮工具调用 | 开启思考且历史存在工具调用时，建议完整回传 `reasoning_content`；缺失不会报错，但可能影响指令遵循与输出质量。 |
| `tool_choice` | 仅支持 `auto`，传入其他值时该字段会被忽略。 |
| 工具函数名 | 仅允许 `a-z`、`A-Z`、`0-9`、下划线、连字符，长度 1-64。 |
| 结构化输出 | `response_format` 仅支持 `json_object`，不支持 `json_schema`。 |
| 超时风险 | 开启思考时响应时间较长，建议配合 `stream=true` 使用，避免超时。 |
| `finish_reason` | 除 `stop`/`length`/`tool_calls`/`content_filter` 外，模型检测到复读时会返回 `repetition_truncation`。 |
| 协议差异 | Anthropic Messages 协议使用 `x-api-key` 认证且 `max_tokens` 必填；Responses 协议使用 `input` 与 `max_output_tokens`，字段命名与 Chat Completions 不同。 |

## 相关文档

[语言模型调用概览](https://cloud.tencent.com/document/product/1823/130079)：TokenHub 语言模型通用调用文档，包含 BaseURL、API Key、多轮对话、Function Calling、Anthropic 协议等通用说明。

[OpenAI Chat Completions 协议字段说明](https://cloud.tencent.com/document/product/1823/135872)：Chat Completions 协议的完整请求与响应字段说明。

[OpenAI Response 协议字段说明](https://cloud.tencent.com/document/product/1823/135873)：Responses 协议的完整请求与响应字段说明。

[Anthropic Message 协议字段说明](https://cloud.tencent.com/document/product/1823/135874)：Anthropic Messages 协议的完整请求与响应字段说明。

[深度思考](https://cloud.tencent.com/document/product/1823/131208)：TokenHub 各模型深度思考能力的通用说明与参数对照。
