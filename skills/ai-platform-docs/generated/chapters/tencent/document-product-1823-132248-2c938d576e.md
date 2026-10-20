<!-- Official source: https://cloud.tencent.com/document/product/1823/132248 -->
<!-- Source SHA-256: eab2d0044b23de0ecc54eb64465134a7c7733e9be265e3b1787b1ef01e95c766 -->

# DeepSeek 调用指南

官方来源：https://cloud.tencent.com/document/product/1823/132248
最近更新时间：2026-10-19 15:53:02

## 概述

DeepSeek 系列模型已接入大模型服务平台 TokenHub，支持 OpenAI Chat Completions 和 Anthropic 两种协议，开发者无需更换 SDK 即可快速接入。本文介绍通用调用示例以及 DeepSeek 特有的思考模式、Function Calling 等核心能力。

**注意：**

**DeepSeek-V4-Flash（Model ID：deepseek-v4-flash）**目前仍基于深度求索 **DeepSeek-V4-Flash 预览版**为您提供服务，此前通知中提及的自动静默升级将暂缓推进，后续以新版本上线为准。您现有的业务调用不会受到影响，模型服务能力、调用方式及计费标准均与此前保持一致，无需做任何调整。同时，考虑到新旧版本在模型能力与性能表现上存在较大差异，为避免对您的存量业务产生非预期影响，正式版模型将通过新的 Model ID 对外提供，由您按需自主切换。详情请查看[产品公告](https://cloud.tencent.com/document/product/1823/130758)。

**DeepSeek-V4-Flash 0731 正式版** **原厂直供**对应深度求索 **DeepSeek-V4-Flash-0731 正式版**，API 调用方式不变，model 调用参数设置为 deepseek-v4-flash-202605 即可使用最新版本。原本使用 DeepSeek-V4-Flash（**model:deepseek-v4-flash-202605**）的用户，平台将自动完成静默升级，无需任何操作即可体验最新能力。

**DeepSeek-V4-Pro 0813 正式版** **原厂直供**对应深度求索 **DeepSeek-V4-Pro-0813 正式版**，API 调用方式不变，model 调用参数设置为 deepseek-v4-pro-202606 即可使用最新版本。原本使用 DeepSeek-V4-Pro（**model:deepseek-v4-pro-202606**）的用户，平台将自动完成静默升级，无需任何操作即可体验最新能力。

## 前提条件

已注册腾讯云账号并开通 TokenHub 服务。

已在 [TokenHub 控制台](https://console.cloud.tencent.com/tokenhub/apikey) 获取 API Key。

已根据所用语言安装对应 SDK 或具备 HTTP 请求能力。

## 支持的模型

TokenHub 当前支持以下 DeepSeek 模型（具体以 [模型列表](https://cloud.tencent.com/document/product/1823/130051) 为准）：

| 模型 ID | 类型 | 思考能力 | 上下文窗口 | 最大输入 | 最大输出 |
| --- | --- | --- | --- | --- | --- |
| `deepseek/deepseek-flash` | 通用对话模型 | 可开关（默认开启） | 1M | 1M | 384K |
| `deepseek-v4-flash-202605`  `deepseek/deepseek-v4-flash-0731`  `deepseek/deepseek-v4-flash` | 通用对话模型 | 可开关（默认开启） | 1M | 1M | 384K |
| `deepseek-v4-pro-202606`  `deepseek/deepseek-v4-pro-0813`  `deepseek/deepseek-v4-pro` | 通用对话模型 | 可开关（默认开启） | 1M | 1M | 384K |
| `deepseek-v4-flash-0731` | 通用对话模型 | 可开关（默认开启） | 1M | 1M | 384K |
| `deepseek-v4-pro-0813` | 通用对话模型 | 可开关（默认开启） | 1M | 1M | 384K |
| `deepseek-v4-flash` | 通用对话模型 | 可开关（默认开启） | 1M | 1M | 384K |
| `deepseek-v4-pro` | 通用对话模型 | 可开关（默认开启） | 1M | 1M | 384K |
| `deepseek/deepseek-v4-flash-vision-exp` | 多模态理解模型 | 可开关（默认开启） | 1M | 1M | 384K |

**说明：**

**原厂直供模型特殊说明：**

由 DeepSeek 直接提供的模型服务，TokenHub 不对该服务提供 SLA 保障，且 TokenHub 的服务协议不对此模型服务生效。使用即视为您已知晓并同意遵守 [DeepSeek 的服务协议](https://cdn.deepseek.com/policies/zh-CN/deepseek-terms-of-use.html)，请您在使用前务必仔细阅读相关内容。如不接受上述内容，请立即停止使用。

DeepSeek V4-Flash / V4-Pro 同时是对话模型和思考模型，无需像其他厂商那样在普通模型和思考模型之间切换 model ID，只需通过 `thinking` 参数控制是否启用思考能力即可。

## 与其他模型的关键差异

| 维度 | DeepSeek V4-Flash / V4-Pro | OpenAI / Claude / GLM 等 |
| --- | --- | --- |
| 思考能力开关 | 通过 `thinking.type` 参数显式控制 | 通常通过切换 model 或单独的 reasoning 参数控制 |
| 推理过程字段 | 响应中独立返回 `reasoning_content` | 多数模型不暴露推理过程 |
| OpenAI SDK 访问推理字段 | 必须用 `hasattr` / `getattr` | - |
| `temperature` | 0~2，默认 1，可自由调节 | 默认可在 0~2 自由调节 |
| `max_tokens` 推荐值 | 普通任务 1024~4096；思考模式建议 ≥ 2048 | 通常 1024~4096 即可 |
| 上下文窗口 | 最高 1M tokens | 通常 128K tokens |
| 最大输出 | 最高 384K tokens | 通常 16K tokens |
| 多轮对话 messages 回写 | 只需回写 `content`，无需回写 `reasoning_content` | 通常只需回写 `content` |

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
    "model": "deepseek-v4-flash",
    "messages": [
      {"role": "user", "content": "你好，请介绍一下你自己"}
    ],
    "max_tokens": 1024
  }'
```

#### Running Environment

```
Operating System: Ubuntu 24.04.3 LTS / x86_64Runtime Version: GNU bash, version 5.2.21(1)-release (x86_64-pc-linux-gnu)
```

```python
# pip install openai
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

response = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[
        {"role": "user", "content": "你好，请介绍一下你自己"}
    ],
    max_tokens=1024,
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
  model: "deepseek-v4-flash",
  messages: [
    { role: "user", content: "你好，请介绍一下你自己" }
  ],
  max_tokens: 1024,
});
console.log(response.choices[0].message.content);
```

```java
// 使用 OkHttp，添加依赖：implementation("com.squareup.okhttp3:okhttp:4.12.0")
import okhttp3.*;
import org.json.*;

OkHttpClient httpClient = new OkHttpClient();

JSONObject body = new JSONObject();
body.put("model", "deepseek-v4-flash");
body.put("max_tokens", 1024);
JSONArray messages = new JSONArray();
JSONObject userMsg = new JSONObject();
userMsg.put("role", "user");
userMsg.put("content", "你好，请介绍一下你自己");
messages.put(userMsg);
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
        "model": "deepseek-v4-flash",
        "messages": []map[string]string{
            {"role": "user", "content": "你好，请介绍一下你自己"},
        },
        "max_tokens": 1024,
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
    "model": "deepseek-v4-flash",
    "messages": [
      {"role": "user", "content": "介绍一下大语言模型"}
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

response = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[
        {"role": "user", "content": "介绍一下大语言模型"}
    ],
    max_tokens=1024,
    extra_body={"thinking": {"type": "disabled"}},  # 关闭思考模式，减少 token 消耗
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
  model: "deepseek-v4-flash",
  messages: [
    { role: "user", content: "介绍一下大语言模型" }
  ],
  max_tokens: 1024,
  // @ts-ignore - thinking 为 DeepSeek 扩展字段
  thinking: { type: "disabled" },
});
console.log(response.choices[0].message.content);
```

```java
import okhttp3.*;
import org.json.*;

OkHttpClient httpClient = new OkHttpClient();

JSONObject body = new JSONObject();
body.put("model", "deepseek-v4-flash");
body.put("max_tokens", 1024);

JSONArray messages = new JSONArray();
JSONObject userMsg = new JSONObject();
userMsg.put("role", "user");
userMsg.put("content", "介绍一下大语言模型");
messages.put(userMsg);
body.put("messages", messages);

JSONObject thinking = new JSONObject();
thinking.put("type", "disabled");
body.put("thinking", thinking);

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
    "model": "deepseek-v4-flash",
    "messages": []map[string]string{
        {"role": "user", "content": "介绍一下大语言模型"},
    },
    "max_tokens": 1024,
    "thinking":   map[string]string{"type": "disabled"},
}
// ... 其余请求代码同快速开始示例
```

### 流式输出

将 `stream` 设置为 `true` 开启 SSE 流式输出，适合长文本生成场景，可有效避免超时，改善用户体验。

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
    "model": "deepseek-v4-flash",
    "messages": [
      {"role": "user", "content": "写一首关于春天的短诗"}
    ],
    "max_tokens": 512,
    "stream": true,
    "thinking": {"type": "disabled"}
  }'
```

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

stream = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[
        {"role": "user", "content": "写一首关于春天的短诗"}
    ],
    max_tokens=512,
    stream=True,
    extra_body={"thinking": {"type": "disabled"}},
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
  model: "deepseek-v4-flash",
  messages: [
    { role: "user", content: "写一首关于春天的短诗" }
  ],
  max_tokens: 512,
  stream: true,
  // @ts-ignore
  thinking: { type: "disabled" },
});

for await (const chunk of stream) {
  const content = chunk.choices[0]?.delta?.content;
  if (content) process.stdout.write(content);
}
```

```java
// 流式输出建议使用 OkHttp EventSource
import okhttp3.*;
import okhttp3.sse.*;
import org.json.*;

OkHttpClient httpClient = new OkHttpClient();

JSONObject body = new JSONObject();
body.put("model", "deepseek-v4-flash");
body.put("max_tokens", 512);
body.put("stream", true);
JSONArray messages = new JSONArray();
JSONObject msg = new JSONObject();
msg.put("role", "user");
msg.put("content", "写一首关于春天的短诗");
messages.put(msg);
body.put("messages", messages);
body.put("thinking", new JSONObject().put("type", "disabled"));

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
            String content = json.getJSONArray("choices").getJSONObject(0)
                .getJSONObject("delta").optString("content", "");
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
    "model":      "deepseek-v4-flash",
    "messages":   []map[string]string{{"role": "user", "content": "写一首关于春天的短诗"}},
    "max_tokens": 512,
    "stream":     true,
    "thinking":   map[string]string{"type": "disabled"},
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
    "model": "deepseek-v4-flash",
    "messages": [
      {"role": "system", "content": "你是一位专业的 Python 编程助手，只回答与 Python 相关的问题，回答简洁明了。"},
      {"role": "user", "content": "如何读取一个 CSV 文件？"}
    ],
    "max_tokens": 512,
    "thinking": {"type": "disabled"}
  }'
```

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

response = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[
        {
            "role": "system",
            "content": "你是一位专业的 Python 编程助手，只回答与 Python 相关的问题，回答简洁明了。",
        },
        {"role": "user", "content": "如何读取一个 CSV 文件？"},
    ],
    max_tokens=512,
    extra_body={"thinking": {"type": "disabled"}},
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
  model: "deepseek-v4-flash",
  messages: [
    {
      role: "system",
      content: "你是一位专业的 Python 编程助手，只回答与 Python 相关的问题，回答简洁明了。",
    },
    { role: "user", content: "如何读取一个 CSV 文件？" },
  ],
  max_tokens: 512,
  // @ts-ignore
  thinking: { type: "disabled" },
});
console.log(response.choices[0].message.content);
```

```java
JSONObject body = new JSONObject();
body.put("model", "deepseek-v4-flash");
body.put("max_tokens", 512);
body.put("thinking", new JSONObject().put("type", "disabled"));

JSONArray messages = new JSONArray();
messages.put(new JSONObject().put("role", "system")
    .put("content", "你是一位专业的 Python 编程助手，只回答与 Python 相关的问题，回答简洁明了。"));
messages.put(new JSONObject().put("role", "user")
    .put("content", "如何读取一个 CSV 文件？"));
body.put("messages", messages);
// ... 发送请求代码同上
```

```go
body := map[string]interface{}{
    "model": "deepseek-v4-flash",
    "messages": []map[string]string{
        {"role": "system", "content": "你是一位专业的 Python 编程助手，只回答与 Python 相关的问题，回答简洁明了。"},
        {"role": "user", "content": "如何读取一个 CSV 文件？"},
    },
    "max_tokens": 512,
    "thinking":   map[string]string{"type": "disabled"},
}
// ... 发送请求代码同快速开始
```

### 多轮对话

将历史消息一并传入 `messages` 数组，即可实现上下文记忆的多轮对话。

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
    "model": "deepseek-v4-flash",
    "messages": [
      {"role": "user", "content": "我叫小明，我喜欢打篮球"},
      {"role": "assistant", "content": "你好，小明！打篮球是一项很棒的运动。"},
      {"role": "user", "content": "你还记得我的名字和爱好吗？"}
    ],
    "max_tokens": 256,
    "thinking": {"type": "disabled"}
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
        model="deepseek-v4-flash",
        messages=conversation,
        max_tokens=1024,
        extra_body={"thinking": {"type": "disabled"}},
    )
    reply = response.choices[0].message.content
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
    model: "deepseek-v4-flash",
    messages: conversation,
    max_tokens: 1024,
    // @ts-ignore
    thinking: { type: "disabled" },
  });
  const reply = response.choices[0].message.content;
  conversation.push({ role: "assistant", content: reply });
  return reply;
}

console.log(await chat("我叫小明，我喜欢打篮球"));
console.log(await chat("你还记得我的名字和爱好吗？"));
```

```java
// 多轮对话核心：将 messages 数组累积传入
JSONArray messages = new JSONArray();
messages.put(new JSONObject().put("role", "system").put("content", "你是一个友好的 AI 助手。"));
messages.put(new JSONObject().put("role", "user").put("content", "我叫小明，我喜欢打篮球"));
messages.put(new JSONObject().put("role", "assistant").put("content", "你好，小明！打篮球是一项很棒的运动。"));
messages.put(new JSONObject().put("role", "user").put("content", "你还记得我的名字和爱好吗？"));

JSONObject body = new JSONObject();
body.put("model", "deepseek-v4-flash");
body.put("messages", messages);
body.put("max_tokens", 1024);
body.put("thinking", new JSONObject().put("type", "disabled"));
// ... 发送请求代码同上
```

```go
body := map[string]interface{}{
    "model": "deepseek-v4-flash",
    "messages": []map[string]string{
        {"role": "system", "content": "你是一个友好的 AI 助手。"},
        {"role": "user", "content": "我叫小明，我喜欢打篮球"},
        {"role": "assistant", "content": "你好，小明！打篮球是一项很棒的运动。"},
        {"role": "user", "content": "你还记得我的名字和爱好吗？"},
    },
    "max_tokens": 1024,
    "thinking":   map[string]string{"type": "disabled"},
}
// ... 发送请求代码同快速开始
```

### Function Calling（工具调用）

Function Calling 允许模型调用外部工具获取实时数据。模型本身不执行函数，而是返回应调用的函数名和参数，由用户代码执行后将结果传回模型，最终得到自然语言回答。

**调用流程：**

1. 用户提问 → 模型返回 `tool_calls`（包含函数名和参数）。

2. 用户代码执行该函数 → 将结果以 `role: tool` 消息传回。

3. 模型根据函数结果生成最终自然语言回答。

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
    "model": "deepseek-v4-flash",
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
    "thinking": {"type": "disabled"}
  }'

# 第二轮：将工具执行结果传回（tool_call_id 替换为实际返回的 id）
curl https://tokenhub.tencentmaas.com/v1/chat/completions \\
  -H "Content-Type: application/json" \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -d '{
    "model": "deepseek-v4-flash",
    "messages": [
      {"role": "user", "content": "北京今天天气怎么样？"},
      {"role": "assistant", "tool_calls": [{"id": "call_xxx", "type": "function", "function": {"name": "get_weather", "arguments": "{\\"city\\": \\"北京\\"}"}}]},
      {"role": "tool", "tool_call_id": "call_xxx", "content": "晴，气温28℃，湿度50%"}
    ],
    "tools": [{"type": "function", "function": {"name": "get_weather", "description": "获取指定城市的天气信息", "parameters": {"type": "object", "properties": {"city": {"type": "string"}}, "required": ["city"]}}}],
    "thinking": {"type": "disabled"}
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
    model="deepseek-v4-flash",
    messages=messages,
    tools=tools,
    extra_body={"thinking": {"type": "disabled"}},
)
assistant_message = response.choices[0].message

# 模型发起工具调用
if response.choices[0].finish_reason == "tool_calls":
    tool_call = assistant_message.tool_calls[0]
    print(f"模型调用工具：{tool_call.function.name}，参数：{tool_call.function.arguments}")

    # 执行工具（此处为模拟返回）
    tool_result = "晴，气温28℃，湿度50%"

    # 第二轮：将工具结果传回模型
    messages.append(assistant_message)
    messages.append({
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": tool_result,
    })

    final_response = client.chat.completions.create(
        model="deepseek-v4-flash",
        messages=messages,
        tools=tools,
        extra_body={"thinking": {"type": "disabled"}},
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
  model: "deepseek-v4-flash",
  messages,
  tools,
  // @ts-ignore
  thinking: { type: "disabled" },
});

const assistantMsg = response1.choices[0].message;
if (response1.choices[0].finish_reason === "tool_calls") {
  const toolCall = assistantMsg.tool_calls[0];
  console.log(`工具调用：${toolCall.function.name}，参数：${toolCall.function.arguments}`);

  const toolResult = "晴，气温28℃，湿度50%";
  messages.push(assistantMsg);
  messages.push({ role: "tool", tool_call_id: toolCall.id, content: toolResult });

  const response2 = await client.chat.completions.create({
    model: "deepseek-v4-flash",
    messages,
    tools,
    // @ts-ignore
    thinking: { type: "disabled" },
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
body.put("model", "deepseek-v4-flash");
body.put("messages", new JSONArray().put(new JSONObject().put("role", "user").put("content", "北京今天天气怎么样？")));
body.put("tools", tools);
body.put("thinking", new JSONObject().put("type", "disabled"));
// ... 发送请求，解析 tool_calls，执行工具，构造第二轮请求
```

```go
body := map[string]interface{}{
    "model": "deepseek-v4-flash",
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
    "thinking": map[string]string{"type": "disabled"},
}
// ... 发送请求，解析 tool_calls，构造第二轮请求
```

## 思考模式

DeepSeek 模型支持通过 `thinking` 参数控制是否开启推理思考模式，无需切换模型 ID。开启思考模式后，模型会先进行内部推理再给出最终答案，适合需要精确推理的复杂任务。

### thinking 参数说明

| 字段 | 类型 | 默认值 | 取值范围 | 说明 |
| --- | --- | --- | --- | --- |
| `type` | string | `"enabled"` | `"enabled"` / `"disabled"` | 控制思考模式开关 |

### 思考深度（reasoning\_effort）

`reasoning_effort` 是请求**顶层参数**，与 `thinking` 平级，用于控制模型的推理强度，便于在效果与延迟之间灵活权衡。

| 取值 | 说明 |
| --- | --- |
| `"low"` | 轻度推理。适合简单任务、快速响应场景。 |
| `"high"` | 增强推理（默认值）。适合常规推理、代码生成等场景。 |
| `"max"` | 深度推理。适合复杂推理、长程任务、深度代码分析等场景。 |

出于兼容考虑，`medium`、`xhigh` 会映射为 `high`。

**模型支持情况**：

`deepseek-v4-flash`：支持 `low`、`high`、`max` 三档。

`deepseek-v4-pro`：暂时只支持 `high`、`max` 两档（`low` 按 `high` 处理，`xhigh` 按 `max` 处理），预计 2026年8月初支持三档。

`reasoning_effort` 不是 OpenAI 标准字段。使用 OpenAI SDK 时需通过 SDK 提供的额外字段机制（Python 用 `extra_body`、Node.js 直接传字段）；HTTP 直接调用时放在请求体顶层。示例如下：

### 开启或关闭思考

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
    "model": "deepseek-v4-flash",
    "messages": [
      {"role": "user", "content": "解方程 x^2 - 5x + 6 = 0"}
    ],
    "max_tokens": 2048,
    "reasoning_effort": "high",
    "thinking": {"type": "enabled"}
  }'
```

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

response = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[{"role": "user", "content": "解方程 x^2 - 5x + 6 = 0"}],
    max_tokens=2048,
    extra_body={"thinking": {"type": "enabled"}},
    reasoning_effort="high",
)

msg = response.choices[0].message

# 获取推理过程（思考模式专属字段）
reasoning = getattr(msg, "reasoning_content", None)
if reasoning:
    print("=== 推理过程 ===")
    print(reasoning)

print("=== 最终答案 ===")
print(msg.content)
```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "YOUR_API_KEY",
  baseURL: "https://tokenhub.tencentmaas.com/v1",
});

const response = await client.chat.completions.create({
  model: "deepseek-v4-flash",
  messages: [{ role: "user", content: "解方程 x^2 - 5x + 6 = 0" }],
  max_tokens: 2048,
  // @ts-ignore
  thinking: { type: "enabled" },
  reasoning_effort: "high",
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
body.put("model", "deepseek-v4-flash");
body.put("max_tokens", 2048);
body.put("messages", new JSONArray()
    .put(new JSONObject().put("role", "user").put("content", "解方程 x^2 - 5x + 6 = 0")));
body.put("thinking", new JSONObject().put("type", "enabled"));
body.put("reasoning_effort", "high");

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
    "model":      "deepseek-v4-flash",
    "max_tokens": 2048,
    "messages": []map[string]string{
        {"role": "user", "content": "解方程 x^2 - 5x + 6 = 0"},
    },
    "thinking":        map[string]string{"type": "enabled"},
    "reasoning_effort": "high",
}
// ... 发送请求，从响应中解析 reasoning_content 和 content 字段
```

### 响应结构示例

开启思考模式后，响应的 `message` 中会包含 `reasoning_content` 字段：

```json
{
  "choices": [{
    "message": {
      "role": "assistant",
      "reasoning_content": "我需要解二次方程 x^2 - 5x + 6 = 0。\\n因式分解：(x-2)(x-3) = 0\\n所以 x = 2 或 x = 3。",
      "content": "方程 x² - 5x + 6 = 0 的解为：**x = 2** 或 **x = 3**"
    },
    "finish_reason": "stop"
  }],
  "usage": {
    "completion_tokens": 120,
    "completion_tokens_details": {
      "reasoning_tokens": 80
    }
  }
}
```

### 流式思考输出

开启流式输出时，`reasoning_content` 和 `content` 均以增量 delta 形式返回，需分别处理：

Python

Node.js

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

stream = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[{"role": "user", "content": "分析一下量子计算的优势和挑战"}],
    max_tokens=2048,
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
  model: "deepseek-v4-flash",
  messages: [{ role: "user", content: "分析一下量子计算的优势和挑战" }],
  max_tokens: 2048,
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

### 多轮对话中使用思考模式

在多轮对话中，无需将上一轮的 `reasoning_content` 回传给模型，只需回传 `content` 字段即可。

Python

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

messages = [{"role": "user", "content": "斐波那契数列的第10项是多少？"}]

response = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=messages,
    max_tokens=1024,
    extra_body={"thinking": {"type": "enabled"}},
)

assistant_msg = response.choices[0].message
print("第一轮回答：", assistant_msg.content)

# 多轮对话：只回传 content，不回传 reasoning_content
messages.append({"role": "assistant", "content": assistant_msg.content})
messages.append({"role": "user", "content": "那第20项呢？"})

response2 = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=messages,
    max_tokens=1024,
    extra_body={"thinking": {"type": "enabled"}},
)
print("第二轮回答：", response2.choices[0].message.content)
```

**说明：**

多轮对话回写 `assistant` 消息时，只需将 `content` 字段传入，无需传入 `reasoning_content`。

## JSON 模式

设置 `response_format` 为 `json_object` 可以确保模型输出合法的 JSON 字符串，适合需要结构化数据的场景。

**注意：**

使用 JSON 模式时，必须在 `system` 或 `user` 消息中明确要求模型输出 JSON 格式，否则可能导致模型一直输出空内容。

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
    "model": "deepseek-v4-flash",
    "messages": [
      {"role": "system", "content": "请以 JSON 格式返回结果。"},
      {"role": "user", "content": "返回三座中国城市的信息，每个包含 name、province、population 字段"}
    ],
    "max_tokens": 512,
    "response_format": {"type": "json_object"},
    "thinking": {"type": "disabled"}
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
    model="deepseek-v4-flash",
    messages=[
        {"role": "system", "content": "请以 JSON 格式返回结果。"},
        {
            "role": "user",
            "content": "返回三座中国城市的信息，每个包含 name、province、population 字段",
        },
    ],
    max_tokens=512,
    response_format={"type": "json_object"},
    extra_body={"thinking": {"type": "disabled"}},
)

result = json.loads(response.choices[0].message.content)
print(json.dumps(result, ensure_ascii=False, indent=2))
```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "YOUR_API_KEY",
  baseURL: "https://tokenhub.tencentmaas.com/v1",
});

const response = await client.chat.completions.create({
  model: "deepseek-v4-flash",
  messages: [
    { role: "system", content: "请以 JSON 格式返回结果。" },
    {
      role: "user",
      content: "返回三座中国城市的信息，每个包含 name、province、population 字段",
    },
  ],
  max_tokens: 512,
  response_format: { type: "json_object" },
  // @ts-ignore
  thinking: { type: "disabled" },
});

const result = JSON.parse(response.choices[0].message.content);
console.log(JSON.stringify(result, null, 2));
```

```java
JSONObject body = new JSONObject();
body.put("model", "deepseek-v4-flash");
body.put("max_tokens", 512);
body.put("response_format", new JSONObject().put("type", "json_object"));
body.put("thinking", new JSONObject().put("type", "disabled"));
body.put("messages", new JSONArray()
    .put(new JSONObject().put("role", "system").put("content", "请以 JSON 格式返回结果。"))
    .put(new JSONObject().put("role", "user").put("content",
        "返回三座中国城市的信息，每个包含 name、province、population 字段")));
// ... 发送请求，解析返回的 JSON 字符串
```

```go
body := map[string]interface{}{
    "model":           "deepseek-v4-flash",
    "max_tokens":      512,
    "response_format": map[string]string{"type": "json_object"},
    "thinking":        map[string]string{"type": "disabled"},
    "messages": []map[string]string{
        {"role": "system", "content": "请以 JSON 格式返回结果。"},
        {"role": "user", "content": "返回三座中国城市的信息，每个包含 name、province、population 字段"},
    },
}
// ... 发送请求
```

## 联网搜索

DeepSeek 原厂直供模型支持服务端联网搜索能力。开启后，模型在回答时可自动调用联网搜索工具获取实时网络信息，解决模型知识时效性不足的问题，适合新闻资讯、时事查询、公开资料检索等场景。联网搜索过程由模型在服务端自主完成：模型自行判断是否需要搜索、生成搜索词、阅读搜索结果，必要时打开网页读取正文，并在多轮搜索后生成带来源链接的回答。

联网搜索通过对话接口的 `tools` 参数开启。当前不支持以独立 API 端点的形式调用搜索或网页抓取能力（即不提供独立的 Search API / Fetch API 端点，无法单独调用搜索或抓取能力获取结果），也不支持通过 OpenAI Chat Completions API 的 `tools` 参数为原厂直供模型开启联网搜索。

### 支持的模型与协议

| 模型 ID | Anthropic Messages API | OpenAI Responses API |
| --- | --- | --- |
| `deepseek/deepseek-flash` | 支持 | 不支持 |
| `deepseek-v4-flash-202605`、`deepseek/deepseek-v4-flash-0731`、`deepseek/deepseek-v4-flash` | 支持 | 不支持 |
| `deepseek-v4-pro-202606`、`deepseek/deepseek-v4-pro-0813`、`deepseek/deepseek-v4-pro` | 支持 | 支持 |
| `deepseek/deepseek-v4-flash-vision-exp` | 支持 | 不支持 |

**注意：**

Responses API 仅 DeepSeek-V4-Pro 系列模型支持联网搜索。Flash 系列模型在 Responses API 中传入 `web_search` 工具时请求不会报错，但联网能力不生效，模型将基于自身知识回答。

如使用平台渠道模型（如 `deepseek-v4-flash-0731`、`deepseek-v4-pro-0813`、`deepseek-v4-flash`、`deepseek-v4-pro`）并通过 Chat API 开启联网搜索，请参见 [联网搜索](https://cloud.tencent.com/document/product/1823/132358)。

### 使用方式

Anthropic Messages API 与 OpenAI Responses API 的基础调用参数（Base URL、鉴权方式、通用请求参数）请参见 [语言模型调用概览](https://cloud.tencent.com/document/product/1823/130079)。使用联网搜索时，仅需在请求体中增加 `tools` 字段，两个协议的工具写法不同：

| 协议 | 端点 | 工具写法 |
| --- | --- | --- |
| Anthropic Messages API | `/v1/messages` | `{"type": "web_search_20250305", "name": "web_search"}` |
| OpenAI Responses API | `/v1/responses` | `{"type": "web_search"}` |

Anthropic Messages API 请求示例：

cURL

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/messages' \\
  -H 'x-api-key: YOUR_API_KEY' \\
  -H 'anthropic-version: 2023-06-01' \\
  -H 'Content-Type: application/json' \\
  -d '{
    "model": "deepseek/deepseek-flash",
    "max_tokens": 4096,
    "messages": [
      {
        "role": "user",
        "content": "最近一周有哪些重要的 AI 行业新闻？请附来源链接。"
      }
    ],
    "tools": [
      {
        "type": "web_search_20250305",
        "name": "web_search"
      }
    ]
  }'
```

OpenAI Responses API 请求示例（仅 DeepSeek-V4-Pro 系列模型支持）：

cURL

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/responses' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
    "model": "deepseek-v4-pro-202606",
    "input": "最近一周有哪些重要的 AI 行业新闻？请附来源链接。",
    "tools": [
      {
        "type": "web_search"
      }
    ]
  }'
```

### 响应结构

开启联网搜索后，可通过响应中的搜索调用内容块确认联网是否生效，模型最终回答中直接包含来源链接：

| 协议 | 搜索调用内容块 | 说明 |
| --- | --- | --- |
| Anthropic Messages API | `server_tool_use` | 一次服务端搜索调用，`input.query` 为模型生成的搜索词。搜索调用次数通过 `usage.server_tool_use.web_search_requests` 返回。 |
| OpenAI Responses API | `web_search_call` | 一次服务端搜索工具调用，`action.type` 为 `search` 时表示执行搜索，为 `open_page` 时表示模型打开网页读取正文。搜索调用次数可通过统计该类内容项数量获取。 |

搜索结果注入的内容计入输入 Token，按模型标准价格计费。联网搜索能力本身的计费规则，正式收费时间和定价将另行通知。

**注意：**

工具类型与协议必须匹配：Anthropic Messages API 使用 `web_search_20250305`（误写为 `web_search` 时请求返回 400 错误），OpenAI Responses API 使用 `web_search`（误写为 `web_search_20250305` 时联网能力不生效）。

## 推荐参数与最佳实践

| 参数 / 实践 | 建议 | 说明 |
| --- | --- | --- |
| `max_tokens` | 普通任务 1024~4096；思考模式建议 ≥ 2048 | 思考内容和回答共享 token 配额 |
| `thinking` | 简单问答用 `disabled`；逻辑推理、数学题用 `enabled` | 合理使用可降低成本 |
| `stream` | 长文本生成建议开启 | 避免请求超时，提升响应体验 |
| `temperature` | 一般无需修改，使用默认值 1 | 创意写作可调高至 1.3-1.5；代码生成可调低至 0.2-0.5 |
| 多轮对话 | 只将 `content` 回传，不回传 `reasoning_content` | 减少 token 消耗 |
| SDK 访问推理字段 | Python 用 `getattr(msg, "reasoning_content", None)`；Node.js 用 `(msg as any).reasoning_content` | OpenAI SDK 类型定义中无此字段 |
| 模型选择 | 日常任务用 `deepseek-v4-flash`；高精度任务用 `deepseek-v4-pro` | Flash 并发上限更高（2500 vs 500） |

## 使用限制

| 限制项 | 说明 |
| --- | --- |
| 思考模式与 JSON 模式 | 不建议同时开启 `thinking.type=enabled` 和 `response_format.type=json_object`。 |
| `frequency_penalty` / `presence_penalty` | 已废弃，传入无效果。 |
| 超时风险 | 思考模式开启时响应时间较长，建议配合 `stream=true` 使用，避免超时。 |

## 相关文档

[语言模型调用概览](https://cloud.tencent.com/document/product/1823/130079)：TokenHub 语言模型通用调用文档，包含 BaseURL、API Key、多轮对话、Function Calling、Anthropic 协议等通用说明。
