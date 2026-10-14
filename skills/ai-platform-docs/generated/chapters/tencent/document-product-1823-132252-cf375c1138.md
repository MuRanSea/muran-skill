<!-- Official source: https://cloud.tencent.com/document/product/1823/132252 -->
<!-- Source SHA-256: 0a984bcf05d41cbe0dc7d477508ff52a0d951824e947b49de76b195bcb08da08 -->

# 混元调用指南

官方来源：https://cloud.tencent.com/document/product/1823/132252
最近更新时间：2026-10-13 15:50:31

## 概述

腾讯混元大模型（Tencent Hy）是由腾讯研发的大语言模型，具备强大的中文创作能力，复杂语境下的逻辑推理能力，以及可靠的任务执行能力。

## 前提条件

已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号并开通 TokenHub 服务。

已在 [TokenHub 控制台](https://console.cloud.tencent.com/tokenhub/apikey) 获取 API Key。

## Hy4 preview 调用示例

`hy4-preview` 兼容 OpenAI Chat Completions API 、OpenAI Responses 、Anthropic Messages API 协议。通用接口规范与所有语言模型一致，请参见 [语言模型调用概览](https://cloud.tencent.com/document/product/1823/130079) 与 [API 使用说明](https://cloud.tencent.com/document/product/1823/130078)。

以下为 OpenAI Chat Completions API 调用示例。

<table><colgroup><col/><col/><col/><col/><col/></colgroup><tbody><tr><td><div>model（调用参数）</div></td><td><div>能力说明</div></td><td><div>上下文窗口</div></td><td><div>最大输入</div></td><td><div>最大输出</div></td></tr><tr><td><div><code>hy4-preview</code></div></td><td><div>新一代生产力模型，Agent 与复杂任务执行能力全面升级。</div></td><td><div>1024k</div></td><td><div>960k</div></td><td><div>64k</div></td></tr><tr><td><div><code>hy3</code></div></td><td><div>Hy3 基于真实业务场景打磨，兼具效果和性价比，强化 Coding、长文、推理和 Agent 等能力。</div></td><td colspan="1" rowspan="1"><div>256k</div></td><td colspan="1" rowspan="1"><div>192k</div></td><td colspan="1" rowspan="1"><div>128k</div></td></tr></tbody></table>

**说明：**

所有示例统一使用 `Authorization: Bearer YOUR_API_KEY` 鉴权，请将 `YOUR_API_KEY` 替换为您在 [TokenHub 控制台](https://console.cloud.tencent.com/tokenhub/apikey) 创建的 API Key。

Python / Node.js 直接使用 OpenAI 官方 SDK；Java / Go 使用标准 HTTP 客户端调用 OpenAI 兼容接口。

### 基础对话

最简单的单轮对话请求，演示基本的请求和响应结构。

cURL

Python

Java

Node.js

Go

```bash

curl -X POST 'https://tokenhub.tencentmaas.com/v1/chat/completions' \\
  -H 'Content-Type: application/json' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -d '{
    "model": "hy4-preview",
    "messages": [
      {"role": "user", "content": "你好，请简单介绍一下你自己。"}
    ],
    "stream": false,
    "temperature": 0.9
  }'
```

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

response = client.chat.completions.create(
    model="hy4-preview",
    messages=[
        {"role": "user", "content": "你好，请简单介绍一下你自己。"},
    ],
    temperature=0.9,
)
print(response.choices[0].message.content)
```

```java
// 本示例依赖：com.squareup.okhttp3:okhttp:4.12.0、com.google.code.gson:gson:2.10.1
import okhttp3.*;
import com.google.gson.Gson;
import java.io.IOException;
import java.util.*;
import java.util.concurrent.TimeUnit;

public class BasicChat {
    public static void main(String[] args) {
        OkHttpClient client = new OkHttpClient.Builder()
                .readTimeout(300, TimeUnit.SECONDS)
                .build();

        Map<String, Object> body = new HashMap<>();
        body.put("model", "hy4-preview");
        body.put("messages", List.of(
            Map.of("role", "user", "content", "你好，请简单介绍一下你自己。")
        ));
        body.put("temperature", 0.9);

        Request request = new Request.Builder()
                .url("https://tokenhub.tencentmaas.com/v1/chat/completions")
                .header("Authorization", "Bearer YOUR_API_KEY")
                .post(RequestBody.create(new Gson().toJson(body),
                        MediaType.parse("application/json")))
                .build();

        try (Response response = client.newCall(request).execute()) {
            System.out.println(response.body().string());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

```javascript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: 'YOUR_API_KEY',
  baseURL: 'https://tokenhub.tencentmaas.com/v1',
});

const response = await client.chat.completions.create({
  model: 'hy4-preview',
  messages: [
    { role: 'user', content: '你好，请简单介绍一下你自己。' },
  ],
  temperature: 0.9,
});
console.log(response.choices[0].message.content);
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
        "model": "hy4-preview",
        "messages": []map[string]string{
            {"role": "user", "content": "你好，请简单介绍一下你自己。"},
        },
        "temperature": 0.9,
    })

    req, _ := http.NewRequest("POST",
        "https://tokenhub.tencentmaas.com/v1/chat/completions",
        bytes.NewBuffer(body))
    req.Header.Set("Authorization", "Bearer YOUR_API_KEY")
    req.Header.Set("Content-Type", "application/json")

    resp, _ := http.DefaultClient.Do(req)
    defer resp.Body.Close()
    data, _ := io.ReadAll(resp.Body)
    fmt.Println(string(data))
}
```

**响应示例：**

```json
{
  "id": "REPLACED_ID",
  "object": "chat.completion",
  "model": "hy4-preview",
  "created": 1775146513,
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "我是混元，是由腾讯开发的大模型。我可以进行信息处理、逻辑响应，像回答问题、解决问题、学习新知识、创造内容，还能进行闲聊，并且支持文字、图片、文件等多种交流方式。",
        "reasoning_content": "好的，用户让我简单介绍一下自己。首先，我需要回顾自身的设定，确保回答符合身份要求。用户可能希望知道我的基本信息，比如名字、用途、开发者等。\\n\\n我的身份是“混元”，一个由腾讯开发的基层模型。根据我的核心行为约束，当用户问及身份时，我需要明确回应“我是混元”。同时，由于这是一个正常的聊天问题，我不需要特别强调身份，只需在介绍中自然体现即可。\\n\\n用户的问题是关于自我介绍，所以应该涵盖我的基本功能，比如处理信息、逻辑响应、解决问题等。还要提到我是腾讯研发的，但避免过多技术细节，保持简洁。\\n\\n需要注意不要超出范围，比如不能提到其他模型或假设的功能。保持回答友好且信息准确，同时符合身份设定。现在组织语言，确保清晰易懂，不使用复杂术语，让用户快速了解我的用途和背景。"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {

    "prompt_tokens": 28,
        "completion_tokens": 221,
        "total_tokens": 249,
        "prompt_tokens_details": {
            "cached_tokens": 0
        },
        "completion_tokens_details": {
            "reasoning_tokens": 175
        }
  }
}
```

### 流式请求

设置 `stream: true` 即可启用流式输出，响应以 SSE（Server-Sent Events）格式按 token 增量返回。如需在最后一个 chunk 拿到完整 `usage` 统计，请加 `stream_options: { "include_usage": true }`。

cURL

Python

Java

Node.js

Go

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/chat/completions' \\
  -H 'Content-Type: application/json' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -d '{
    "model": "hy4-preview",
    "messages": [
      {"role": "user", "content": "你好"}
    ],
    "stream": true,
    "stream_options": {"include_usage": true}
  }'
```

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

stream = client.chat.completions.create(
    model="hy4-preview",
    messages=[{"role": "user", "content": "你好"}],
    stream=True,
    stream_options={"include_usage": True},
)
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
    if chunk.usage:
        print("\\nusage:", chunk.usage)
```

```java
// 本示例依赖：com.squareup.okhttp3:okhttp:4.12.0、com.squareup.okhttp3:okhttp-sse:4.12.0、com.google.code.gson:gson:2.10.1
import okhttp3.*;
import okhttp3.sse.*;
import com.google.gson.Gson;
import java.util.*;
import java.util.concurrent.TimeUnit;

public class StreamingChat {
    public static void main(String[] args) {
        OkHttpClient client = new OkHttpClient.Builder()
                .readTimeout(300, TimeUnit.SECONDS)
                .build();

        Map<String, Object> body = new HashMap<>();
        body.put("model", "hy4-preview");
        body.put("messages", List.of(Map.of("role", "user", "content", "你好")));
        body.put("stream", true);
        body.put("stream_options", Map.of("include_usage", true));

        Request request = new Request.Builder()
                .url("https://tokenhub.tencentmaas.com/v1/chat/completions")
                .header("Authorization", "Bearer YOUR_API_KEY")
                .post(RequestBody.create(new Gson().toJson(body),
                        MediaType.parse("application/json")))
                .build();

        EventSources.createFactory(client).newEventSource(request,
                new EventSourceListener() {
                    @Override
                    public void onEvent(EventSource es, String id, String type, String data) {
                        if (!"[DONE]".equals(data)) System.out.println(data);
                    }
                });
    }
}
```

```javascript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: 'YOUR_API_KEY',
  baseURL: 'https://tokenhub.tencentmaas.com/v1',
});

const stream = await client.chat.completions.create({
  model: 'hy4-preview',
  messages: [{ role: 'user', content: '你好' }],
  stream: true,
  stream_options: { include_usage: true },
});

for await (const chunk of stream) {
  process.stdout.write(chunk.choices[0]?.delta?.content || '');
  if (chunk.usage) console.log('\\nusage:', chunk.usage);
}
```

```go
package main

import (
    "bufio"
    "bytes"
    "encoding/json"
    "fmt"
    "net/http"
    "strings"
)

func main() {
    body, _ := json.Marshal(map[string]interface{}{
        "model": "hy4-preview",
        "messages": []map[string]string{
            {"role": "user", "content": "你好"},
        },
        "stream":         true,
        "stream_options": map[string]bool{"include_usage": true},
    })

    req, _ := http.NewRequest("POST",
        "https://tokenhub.tencentmaas.com/v1/chat/completions",
        bytes.NewBuffer(body))
    req.Header.Set("Authorization", "Bearer YOUR_API_KEY")
    req.Header.Set("Content-Type", "application/json")

    resp, _ := http.DefaultClient.Do(req)
    defer resp.Body.Close()

    scanner := bufio.NewScanner(resp.Body)
    for scanner.Scan() {
        line := scanner.Text()
        if strings.HasPrefix(line, "data: ") && line != "data: [DONE]" {
            fmt.Println(strings.TrimPrefix(line, "data: "))
        }
    }
}
```

**响应示例（SSE 片段）：**

```text
data: {"id": "REPLACED_ID", "object": "chat.completion.chunk", "created": 1779958293, "model": "hy4-preview", "choices": [{"index": 0, "delta": {"role": "assistant"}}]}

data: {"id": "REPLACED_ID", "object": "chat.completion.chunk", "created": 1779958293, "model": "hy4-preview", "choices": [{"index": 0, "delta": {"content": "你好"}}]}

data: {"id": "REPLACED_ID", "object": "chat.completion.chunk", "created": 1779958293, "model": "hy4-preview", "choices": [{"index": 0, "delta": {"content": "帮你的吗"}}]}

data: {"id": "REPLACED_ID", "object": "chat.completion.chunk", "created": 1779958293, "model": "hy4-preview", "choices": [{"index": 0, "delta": {"content": " 😊"}, "finish_reason": "stop"}]}

data: {"id": "REPLACED_ID", "object": "chat.completion.chunk", "created": 1779958293, "model": "hy4-preview", "choices": [], "usage": {"prompt_tokens": 16, "completion_tokens": 11, "total_tokens": 27, "prompt_tokens_details": {"cached_tokens": 0}, "completion_tokens_details": {"reasoning_tokens": 0}}}

data: [DONE]
```

### 深度思考

`hy4-preview` 默认开启深度思考，详细说明请参见 [深度思考](https://cloud.tencent.com/document/product/1823/131208)。

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
    "model": "hy4-preview",
    "messages": [
      {"role": "user", "content": "小明有5个苹果，给了小红2个，又买了3个，最后还剩几个？"}
    ],
    "thinking": {"type": "enabled"},
    "stream": false
  }'
```

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

response = client.chat.completions.create(
    model="hy4-preview",
    messages=[
        {"role": "user", "content": "小明有5个苹果，给了小红2个，又买了3个，最后还剩几个？"},
    ],
    extra_body={"thinking": {"type": "enabled"}},
)

# OpenAI SDK 不直接声明 reasoning_content 字段，需用 getattr 访问
msg = response.choices[0].message
if hasattr(msg, "reasoning_content"):
    print("思考过程:", getattr(msg, "reasoning_content"))
print("最终回答:", msg.content)
```

```javascript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: 'YOUR_API_KEY',
  baseURL: 'https://tokenhub.tencentmaas.com/v1',
});

// Node.js SDK：thinking 字段直接展开到顶层
const response = await client.chat.completions.create({
  model: 'hy4-preview',
  messages: [
    { role: 'user', content: '小明有5个苹果，给了小红2个，又买了3个，最后还剩几个？' },
  ],
  thinking: { type: 'enabled' },
});

const msg = response.choices[0].message;
if (msg.reasoning_content) console.log('思考过程:', msg.reasoning_content);
console.log('最终回答:', msg.content);
```

```java
// 本示例依赖：com.squareup.okhttp3:okhttp:4.12.0、com.google.code.gson:gson:2.10.1
import okhttp3.*;
import com.google.gson.Gson;
import java.io.IOException;
import java.util.*;
import java.util.concurrent.TimeUnit;

public class ThinkingChat {
    public static void main(String[] args) {
        OkHttpClient client = new OkHttpClient.Builder()
                .readTimeout(300, TimeUnit.SECONDS)
                .build();

        Map<String, Object> body = new HashMap<>();
        body.put("model", "hy4-preview");
        body.put("messages", List.of(
            Map.of("role", "user", "content", "小明有5个苹果，给了小红2个，又买了3个，最后还剩几个？")
        ));
        body.put("thinking", Map.of("type", "enabled"));

        Request request = new Request.Builder()
                .url("https://tokenhub.tencentmaas.com/v1/chat/completions")
                .header("Authorization", "Bearer YOUR_API_KEY")
                .post(RequestBody.create(new Gson().toJson(body),
                        MediaType.parse("application/json")))
                .build();

        try (Response response = client.newCall(request).execute()) {
            // 响应体中 message.reasoning_content 为思考过程，message.content 为最终回答
            System.out.println(response.body().string());
        } catch (IOException e) {
            e.printStackTrace();
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
        "model": "hy4-preview",
        "messages": []map[string]string{
            {"role": "user", "content": "小明有5个苹果，给了小红2个，又买了3个，最后还剩几个？"},
        },
        "thinking": map[string]string{"type": "enabled"},
    })

    req, _ := http.NewRequest("POST",
        "https://tokenhub.tencentmaas.com/v1/chat/completions",
        bytes.NewBuffer(body))
    req.Header.Set("Authorization", "Bearer YOUR_API_KEY")
    req.Header.Set("Content-Type", "application/json")

    resp, _ := http.DefaultClient.Do(req)
    defer resp.Body.Close()

    data, _ := io.ReadAll(resp.Body)
    // 响应体中 message.reasoning_content 为思考过程，message.content 为最终回答
    fmt.Println(string(data))
}
```

**响应示例：**

启用思考后，响应中会附带 `reasoning_content` 思考过程字段。

```json
{
  "id": "REPLACED_ID",
  "object": "chat.completion",
  "created": 1775146546,
  "model": "hy4-preview",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "小明最后还剩 **6个** 苹果。\\n\\n计算过程：\\n1. 一开始有 5 个苹果；\\n2. 给了小红 2 个后，剩下：5 - 2 = 3 个；\\n3. 又买了 3 个后，变成：3 + 3 = 6 个。",
        "reasoning_content": "用户问：小明有5个苹果，给了小红2个，又买了3个，最后还剩几个？\\n我们来一步步计算：\\n初始：5个苹果\\n给了小红2个：5 - 2 = 3个\\n又买了3个：3 + 3 = 6个\\n最后还剩6个苹果。\\n\\n确认一下有没有语言陷阱。\\"给了小红2个\\"是减去，\\"又买了3个\\"是加上。\\n5 - 2 + 3 = 6。\\n答案应该是6个。"
        },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 31,
    "completion_tokens": 178,
    "total_tokens": 209,
    "prompt_tokens_details": {
        "cached_tokens": 0
    },
    "completion_tokens_details": {
        "reasoning_tokens": 106
    }
  }
}
```

**推理深度配置**

`hy4-preview` 、`hy3` 默认为 `high`。详细说明请参见 [深度思考](https://cloud.tencent.com/document/product/1823/131208)。

**注意：**

Hy3正式版在 toolcall 场景下，模型已具备 adaptive thinking 能力，即可以根据任务复杂度，自主决定推理深度。当请求携带 tools 时，出于兼容考虑，此场景下若设置 `reasoning_effort` 为 `low`，API 会自动将 `low` 映射为 `high`。

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
    "model": "hy4-preview",
    "messages": [
      {"role": "user", "content": "小明有5个苹果，给了小红2个，又买了3个，最后还剩几个？"}
    ],
    "stream": false,
    "temperature": 0.9,
    "reasoning_effort": "high"
  }'
```

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

response = client.chat.completions.create(
    model="hy4-preview",
    messages=[
        {"role": "user", "content": "小明有5个苹果，给了小红2个，又买了3个，最后还剩几个？"},
    ],
    temperature=0.9,
    extra_body={"reasoning_effort": "high"},
)

msg = response.choices[0].message
if hasattr(msg, "reasoning_content"):
    print("思考过程:", getattr(msg, "reasoning_content"))
print("最终回答:", msg.content)
```

```javascript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: 'YOUR_API_KEY',
  baseURL: 'https://tokenhub.tencentmaas.com/v1',
});

const response = await client.chat.completions.create({
  model: 'hy4-preview',
  messages: [
    { role: 'user', content: '小明有5个苹果，给了小红2个，又买了3个，最后还剩几个？' },
  ],
  temperature: 0.9,
  reasoning_effort: 'high',
});

const msg = response.choices[0].message;
if (msg.reasoning_content) console.log('思考过程:', msg.reasoning_content);
console.log('最终回答:', msg.content);
```

```java
// 本示例依赖：com.squareup.okhttp3:okhttp:4.12.0、com.google.code.gson:gson:2.10.1
import okhttp3.*;
import com.google.gson.Gson;
import java.io.IOException;
import java.util.*;
import java.util.concurrent.TimeUnit;

public class ReasoningEffortChat {
    public static void main(String[] args) {
        OkHttpClient client = new OkHttpClient.Builder()
                .readTimeout(300, TimeUnit.SECONDS)
                .build();

        Map<String, Object> body = new HashMap<>();
        body.put("model", "hy4-preview");
        body.put("messages", List.of(
            Map.of("role", "user", "content", "小明有5个苹果，给了小红2个，又买了3个，最后还剩几个？")
        ));
        body.put("temperature", 0.9);
        body.put("reasoning_effort", "high");

        Request request = new Request.Builder()
                .url("https://tokenhub.tencentmaas.com/v1/chat/completions")
                .header("Authorization", "Bearer YOUR_API_KEY")
                .post(RequestBody.create(new Gson().toJson(body),
                        MediaType.parse("application/json")))
                .build();

        try (Response response = client.newCall(request).execute()) {
            System.out.println(response.body().string());
        } catch (IOException e) {
            e.printStackTrace();
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
        "model": "hy4-preview",
        "messages": []map[string]string{
            {"role": "user", "content": "小明有5个苹果，给了小红2个，又买了3个，最后还剩几个？"},
        },
        "temperature":      0.9,
        "reasoning_effort": "high",
    })

    req, _ := http.NewRequest("POST",
        "https://tokenhub.tencentmaas.com/v1/chat/completions",
        bytes.NewBuffer(body))
    req.Header.Set("Authorization", "Bearer YOUR_API_KEY")
    req.Header.Set("Content-Type", "application/json")

    resp, _ := http.DefaultClient.Do(req)
    defer resp.Body.Close()

    data, _ := io.ReadAll(resp.Body)
    fmt.Println(string(data))
}
```

**响应示例：**

启用思考后，响应中会附带 `reasoning_content` 思考过程字段。

```json
{
  "id": "c95dc87ecce440678c3bb08f5868fee6",
  "object": "chat.completion",
  "created": 1775146546,
  "model": "hy4-preview",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "小明原本有5个苹果，给了小红2个后剩下：  \\n5 - 2 = 3（个）  \\n然后又买了3个，现在共有：  \\n3 + 3 = 6（个）  \\n\\n所以最后还剩 **6个** 苹果。",
        "reasoning_content": "我们被问到：\\"小明有5个苹果，给了小红2个，又买了3个，最后还剩几个？\\" 我们需要逐步计算。\\n\\n初始：5个苹果。\\n给了小红2个：5 - 2 = 3个苹果。\\n又买了3个：3 + 3 = 6个苹果。\\n所以最后还剩6个苹果。\\n\\n答案：6。"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 3,
    "completion_tokens": 136,
    "total_tokens": 167
  }
}
```

#### 交错式思考（深度思考 + 工具调用）

本示例仅用于说明完整流程与字段回传逻辑；实际使用时，请根据业务部署环境和业务字段调整具体值（此案例仅用于理解流程，不代表模型能力边界）。详细说明请参见 [交错式思考模式（Interleaved Thinking）](https://cloud.tencent.com/document/product/1823/130930)。

**第 1 轮 - 用户提问：**

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
    "model": "hy4-preview",
    "messages": [
      { "role": "system", "content": "你是一个 Agent，必须按步骤推理并调用工具完成任务。" },
      { "role": "user",   "content": "深圳今天天气怎么样？" }
    ],
    "stream": false,
    "tool_choice": "auto",
    "reasoning_effort": "high",
    "tools": [
      {
        "type": "function",
        "function": {
          "name": "get_weather",
          "description": "获取某地天气信息，输入 location。",
          "parameters": {
            "type": "object",
            "properties": { "location": { "type": "string" } },
            "required": ["location"]
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

tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "获取某地天气信息，输入 location。",
        "parameters": {
            "type": "object",
            "properties": {"location": {"type": "string"}},
            "required": ["location"],
        },
    },
}]

messages = [
    {"role": "system", "content": "你是一个 Agent，必须按步骤推理并调用工具完成任务。"},
    {"role": "user", "content": "深圳今天天气怎么样？"},
]

# OpenAI Python SDK 类型签名严格，非标字段（如 reasoning_effort）需通过 extra_body 透传
resp1 = client.chat.completions.create(
    model="hy4-preview",
    messages=messages,
    tools=tools,
    tool_choice="auto",
    extra_body={"reasoning_effort": "high"},
)
msg1 = resp1.choices[0].message
print("第 1 轮 assistant.reasoning_content:", getattr(msg1, "reasoning_content", ""))
print("第 1 轮 tool_calls:", msg1.tool_calls)
```

```javascript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: 'YOUR_API_KEY',
  baseURL: 'https://tokenhub.tencentmaas.com/v1',
});

const tools = [{
  type: 'function',
  function: {
    name: 'get_weather',
    description: '获取某地天气信息，输入 location。',
    parameters: {
      type: 'object',
      properties: { location: { type: 'string' } },
      required: ['location'],
    },
  },
}];

const messages = [
  { role: 'system', content: '你是一个 Agent，必须按步骤推理并调用工具完成任务。' },
  { role: 'user', content: '深圳今天天气怎么样？' },
];

const resp1 = await client.chat.completions.create({
  model: 'hy4-preview',
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
// 本示例依赖：com.squareup.okhttp3:okhttp:4.12.0、com.google.code.gson:gson:2.10.1
import okhttp3.*;
import com.google.gson.Gson;
import java.io.IOException;
import java.util.*;
import java.util.concurrent.TimeUnit;

public class InterleavedThinking {
    static final String URL = "https://tokenhub.tencentmaas.com/v1/chat/completions";
    static final String API_KEY = "YOUR_API_KEY";
    static final OkHttpClient HTTP = new OkHttpClient.Builder()
            .readTimeout(300, TimeUnit.SECONDS)
            .build();
    static final Gson GSON = new Gson();

    /** 通用 chat 调用，返回原始 JSON 响应字符串。 */
    static String chat(List<Map<String, Object>> messages, List<Map<String, Object>> tools) {
        Map<String, Object> body = new HashMap<>();
        body.put("model", "hy4-preview");
        body.put("messages", messages);
        body.put("tools", tools);
        body.put("tool_choice", "auto");
        body.put("reasoning_effort", "high");
        body.put("stream", false);

        Request req = new Request.Builder()
                .url(URL)
                .header("Authorization", "Bearer " + API_KEY)
                .post(RequestBody.create(GSON.toJson(body), MediaType.parse("application/json")))
                .build();
        try (Response resp = HTTP.newCall(req).execute()) {
            return resp.body().string();
        } catch (IOException e) {
            e.printStackTrace();
            return "";
        }
    }

    public static void main(String[] args) {
        List<Map<String, Object>> tools = List.of(Map.of(
            "type", "function",
            "function", Map.of(
                "name", "get_weather",
                "description", "获取某地天气信息，输入 location。",
                "parameters", Map.of(
                    "type", "object",
                    "properties", Map.of("location", Map.of("type", "string")),
                    "required", List.of("location")
                )
            )
        ));

        List<Map<String, Object>> messages = new ArrayList<>();
        messages.add(Map.of("role", "system", "content", "你是一个 Agent，必须按步骤推理并调用工具完成任务。"));
        messages.add(Map.of("role", "user", "content", "深圳今天天气怎么样？"));

        String r1 = chat(messages, tools);
        System.out.println("第 1 轮响应：" + r1);
        // 接下来按响应里的 reasoning_content / tool_calls 回填到 messages，参见第 2 步
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
        "model":            "hy4-preview",
        "messages":         messages,
        "tools":            tools,
        "tool_choice":      "auto",
        "reasoning_effort": "high",
        "stream":           false,
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
    tools := []map[string]interface{}{{
        "type": "function",
        "function": map[string]interface{}{
            "name":        "get_weather",
            "description": "获取某地天气信息，输入 location。",
            "parameters": map[string]interface{}{
                "type": "object",
                "properties": map[string]interface{}{
                    "location": map[string]string{"type": "string"},
                },
                "required": []string{"location"},
            },
        },
    }}

    messages := []map[string]interface{}{
        {"role": "system", "content": "你是一个 Agent，必须按步骤推理并调用工具完成任务。"},
        {"role": "user", "content": "深圳今天天气怎么样？"},
    }

    // 第 1 轮：模型决定是否调用工具
    r1, _ := chat(messages, tools)
    fmt.Printf("第 1 轮响应: %+v\\n", r1)
    // 接下来按响应里的 reasoning_content / tool_calls 回填到 messages，参见第 2 步
}
```

**响应：**

```json
{
    "id": "31be91fe574e41e49616352366b4fa1b",
    "object": "chat.completion",
    "created": 1776057110,
    "model": "hy4-preview",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "我来帮你查询深圳今天的天气情况。",
                "reasoning_content": "用户问的是\\"深圳今天天气怎么样？\\"，这是一个简单的天气查询请求。我需要使用get_weather函数来获取深圳的天气信息。根据函数描述，这个函数需要一个location参数，用户已经明确提供了\\"深圳\\"作为地点。所以，我应该直接调用get_weather函数，参数location设为\\"深圳\\"。不需要额外的推理步骤，因为用户的问题很直接。现在，我准备调用函数。",
                "tool_calls": [
                    {
                        "id": "chatcmpl-tool-b39c6375f812783a",
                        "type": "function",
                        "function": {
                            "name": "get_weather",
                            "arguments": "{\\"location\\": \\"深圳\\"}"
                        }
                    }
                ]
            },
            "finish_reason": "tool_calls"
        }
    ],
    "usage": {
        "prompt_tokens": 209,
        "completion_tokens": 111,
        "total_tokens": 320
    }
}
```

**第 2 轮 - 回填工具结果（在同一轮中延续思维链）：**

假设工具执行返回的结果为：`Cloudy，气温 7~13°C`。您需要在请求中，回填工具执行结果，同时保留首次请求中响应体里获取的 `reasoning_content`。

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
    "model": "hy4-preview",
    "messages": [
      { "role": "system", "content": "你是一个 Agent，必须按步骤推理并调用工具完成任务。" },
      { "role": "user",   "content": "深圳今天天气怎么样？" },
      {
        "role": "assistant",
        "content": "我来帮你查询深圳今天的天气情况。",
        "reasoning_content": "用户问的是\\"深圳今天天气怎么样？\\"...",
        "tool_calls": [
          {
            "id": "chatcmpl-tool-b39c6375f812783a",
            "type": "function",
            "function": {
              "name": "get_weather",
              "arguments": "{\\"location\\": \\"深圳\\"}"
            }
          }
        ]
      },
      {
        "role": "tool",
        "tool_call_id": "chatcmpl-tool-b39c6375f812783a",
        "content": "Cloudy，气温 7~13°C"
      }
    ],
    "stream": false,
    "tool_choice": "auto",
    "reasoning_effort": "high",
    "tools": [
      {
        "type": "function",
        "function": {
          "name": "get_weather",
          "description": "获取某地天气信息，输入 location。",
          "parameters": {
            "type": "object",
            "properties": { "location": { "type": "string" } },
            "required": ["location"]
          }
        }
      }
    ]
  }'
```

```python
# 接续上一步：把第 1 轮的 assistant 消息（含 reasoning_content + tool_calls）
# 与工具结果一起回填到 messages
import json

# 第 1 轮 assistant 消息的回写：reasoning_content 必须保留
assistant_msg = {
    "role": "assistant",
    "content": msg1.content,
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

# 业务侧执行工具，把结果以 role=tool 回填
for tc in (msg1.tool_calls or []):
    args = json.loads(tc.function.arguments)
    # 这里替换为真实业务逻辑
    tool_result = "Cloudy，气温 7~13°C"
    messages.append({
        "role": "tool",
        "tool_call_id": tc.id,
        "content": tool_result,
    })

# 第 2 轮：把工具结果送回模型，模型继续思考并输出最终回答
resp2 = client.chat.completions.create(
    model="hy4-preview",
    messages=messages,
    tools=tools,
    tool_choice="auto",
    extra_body={"reasoning_effort": "high"},
)
print("最终回答:", resp2.choices[0].message.content)
```

```javascript
// 接续上一步：把第 1 轮的 assistant 消息（含 reasoning_content + tool_calls）
// 与工具结果一起回填到 messages

const assistantMsg = {
  role: 'assistant',
  content: msg1.content,
  reasoning_content: msg1.reasoning_content,
  tool_calls: msg1.tool_calls,
};
messages.push(assistantMsg);

for (const tc of msg1.tool_calls || []) {
  const args = JSON.parse(tc.function.arguments);
  // 这里替换为真实业务逻辑
  const toolResult = 'Cloudy，气温 7~13°C';
  messages.push({
    role: 'tool',
    tool_call_id: tc.id,
    content: toolResult,
  });
}

const resp2 = await client.chat.completions.create({
  model: 'hy4-preview',
  messages,
  tools,
  tool_choice: 'auto',
  reasoning_effort: 'high',
});
console.log('最终回答:', resp2.choices[0].message.content);
```

```java
// 接续 main()：把第 1 轮 assistant 消息和工具结果回填，再发起第 2 轮请求
// 完整流程示意（仅展示消息构造，HTTP 调用复用上一步的 chat() 函数）

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

// 3. 业务侧执行工具，把工具结果以 role=tool 回填
for (JsonElement el : msg1.getAsJsonArray("tool_calls")) {
    JsonObject call = el.getAsJsonObject();
    String toolResult = "Cloudy，气温 7~13°C"; // 这里替换为真实业务逻辑
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
// 接续 main()：把第 1 轮 assistant 消息和工具结果回填，再发起第 2 轮请求
// 完整流程示意（仅展示消息构造，HTTP 调用复用上一步的 chat() 函数）

// 1. 从第 1 轮响应中取出 assistant 消息
msg1Wrap := r1["choices"].([]interface{})[0].(map[string]interface{})
msg1 := msg1Wrap["message"].(map[string]interface{})

// 2. 把 assistant 消息（含 reasoning_content）整体回写到 messages
messages = append(messages, msg1)

// 3. 业务侧执行工具，把工具结果以 role=tool 回填
toolCalls, _ := msg1["tool_calls"].([]interface{})
for _, c := range toolCalls {
    call := c.(map[string]interface{})
    toolResult := "Cloudy，气温 7~13°C" // 这里替换为真实业务逻辑
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

**响应：**

之后，模型会根据实际推理结果继续输出（可能继续 tool\_calls，也可能输出最终答案），在获得最终答案前，每次调用都需遵循上述流程，通过“保留 reasoning\_content + 回填 tool 输出”以维持大模型的思维链。

```json
{
    "id": "ae8941415e154a3c9749f0cf897469a4",
    "object": "chat.completion",
    "created": 1776057913,
    "model": "hy4-preview",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "根据查询结果，深圳今天的天气是**多云**，气温在 **7°C 到 13°C** 之间。今天天气比较凉爽，建议适当增添衣物，注意保暖哦！🧥",
                "reasoning_content": "用户询问深圳今天的天气，我已经调用了get_weather工具获取了深圳的天气信息。结果显示是\\"Cloudy，气温 7~13°C\\"。\\n\\n现在我需要用中文回复用户，告诉他深圳今天的天气情况。天气是多云（Cloudy），气温在7到13摄氏度之间。\\n\\n我应该简洁明了地回复用户。"
            },
            "finish_reason": "stop"
        }
    ],
    "usage": {
        "prompt_tokens": 340,
        "completion_tokens": 114,
        "total_tokens": 454
    }
}
```

### 多轮对话

通过 `messages` 数组传递系统提示与历史对话，模型按顺序理解上下文并续接回复。消息顺序需为 `system（可选）→ user → assistant → user → ...`，且必须以 `user` 结尾。

cURL

Python

Java

Node.js

Go

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/chat/completions' \\
  -H 'Content-Type: application/json' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -d '{
    "model": "hy4-preview",
    "messages": [
      {"role": "system", "content": "你是一个专业的 AI 编程助手。"},
      {"role": "user", "content": "Python 中如何读取 JSON 文件？"},
      {"role": "assistant", "content": "可以使用内置的 json 模块：import json; with open(\\"data.json\\") as f: data = json.load(f)"},
      {"role": "user", "content": "如果 JSON 文件很大怎么办？"}
    ]
  }'
```

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

response = client.chat.completions.create(
    model="hy4-preview",
    messages=[
        {"role": "system", "content": "你是一个专业的 AI 编程助手。"},
        {"role": "user", "content": "Python 中如何读取 JSON 文件？"},
        {"role": "assistant", "content": "可以使用内置的 json 模块：import json; with open('data.json') as f: data = json.load(f)"},
        {"role": "user", "content": "如果 JSON 文件很大怎么办？"},
    ],
)
print(response.choices[0].message.content)
```

```java
import okhttp3.*;
import com.google.gson.Gson;
import java.util.*;

public class MultiTurn {
    public static void main(String[] args) throws Exception {
        Map<String, Object> body = new HashMap<>();
        body.put("model", "hy4-preview");
        body.put("messages", List.of(
            Map.of("role", "system",    "content", "你是一个专业的 AI 编程助手。"),
            Map.of("role", "user",      "content", "Python 中如何读取 JSON 文件？"),
            Map.of("role", "assistant", "content", "可以使用内置的 json 模块：import json; with open(\\"data.json\\") as f: data = json.load(f)"),
            Map.of("role", "user",      "content", "如果 JSON 文件很大怎么办？")
        ));

        Request request = new Request.Builder()
            .url("https://tokenhub.tencentmaas.com/v1/chat/completions")
            .header("Authorization", "Bearer YOUR_API_KEY")
            .post(RequestBody.create(new Gson().toJson(body),
                MediaType.parse("application/json")))
            .build();

        try (Response response = new OkHttpClient().newCall(request).execute()) {
            System.out.println(response.body().string());
        }
    }
}
```

```javascript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: 'YOUR_API_KEY',
  baseURL: 'https://tokenhub.tencentmaas.com/v1',
});

const response = await client.chat.completions.create({
  model: 'hy4-preview',
  messages: [
    { role: 'system',    content: '你是一个专业的 AI 编程助手。' },
    { role: 'user',      content: 'Python 中如何读取 JSON 文件？' },
    { role: 'assistant', content: '可以使用内置的 json 模块：import json; with open("data.json") as f: data = json.load(f)' },
    { role: 'user',      content: '如果 JSON 文件很大怎么办？' },
  ],
});
console.log(response.choices[0].message.content);
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
        "model": "hy4-preview",
        "messages": []map[string]string{
            {"role": "system",    "content": "你是一个专业的 AI 编程助手。"},
            {"role": "user",      "content": "Python 中如何读取 JSON 文件？"},
            {"role": "assistant", "content": "可以使用内置的 json 模块：import json; with open(\\"data.json\\") as f: data = json.load(f)"},
            {"role": "user",      "content": "如果 JSON 文件很大怎么办？"},
        },
    })

    req, _ := http.NewRequest("POST",
        "https://tokenhub.tencentmaas.com/v1/chat/completions",
        bytes.NewBuffer(body))
    req.Header.Set("Authorization", "Bearer YOUR_API_KEY")
    req.Header.Set("Content-Type", "application/json")

    resp, _ := http.DefaultClient.Do(req)
    defer resp.Body.Close()
    data, _ := io.ReadAll(resp.Body)
    fmt.Println(string(data))
}
```

**说明：**

当历史对话中包含思考类响应时，回写 `assistant` 消息建议同时携带 `content` 与 `reasoning_content` 两个字段，避免推理上下文丢失。

### 工具调用（Function Calling）

通过 `tools` 定义模型可调用的函数列表，模型在判断需要调用工具时返回 `tool_calls`；业务执行后将结果以 `role: "tool"` 消息回填，模型据此生成最终回答。

cURL

Python

Java

Node.js

Go

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/chat/completions' \\
  -H 'Content-Type: application/json' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -d '{
    "model": "hy4-preview",
    "messages": [
      {"role": "user", "content": "深圳今天天气怎么样？"}
    ],
    "tools": [{
      "type": "function",
      "function": {
        "name": "get_weather",
        "description": "获取指定城市的当前天气信息",
        "parameters": {
          "type": "object",
          "properties": {
            "city": {"type": "string", "description": "城市名称，例如：北京"}
          },
          "required": ["city"]
        }
      }
    }],
    "tool_choice": "auto"
  }'
```

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "获取指定城市的当前天气信息",
        "parameters": {
            "type": "object",
            "properties": {"city": {"type": "string", "description": "城市名称，例如：北京"}},
            "required": ["city"],
        },
    },
}]

response = client.chat.completions.create(
    model="hy4-preview",
    messages=[{"role": "user", "content": "深圳今天天气怎么样？"}],
    tools=tools,
    tool_choice="auto",
)
print(response.choices[0].message)
```

```java
import okhttp3.*;
import com.google.gson.Gson;
import java.util.*;

public class FunctionCalling {
    public static void main(String[] args) throws Exception {
        Map<String, Object> tool = Map.of(
            "type", "function",
            "function", Map.of(
                "name", "get_weather",
                "description", "获取指定城市的当前天气信息",
                "parameters", Map.of(
                    "type", "object",
                    "properties", Map.of("city", Map.of("type", "string", "description", "城市名称，例如：北京")),
                    "required", List.of("city")
                )
            )
        );

        Map<String, Object> body = new HashMap<>();
        body.put("model", "hy4-preview");
        body.put("messages", List.of(Map.of("role", "user", "content", "深圳今天天气怎么样？")));
        body.put("tools", List.of(tool));
        body.put("tool_choice", "auto");

        Request request = new Request.Builder()
            .url("https://tokenhub.tencentmaas.com/v1/chat/completions")
            .header("Authorization", "Bearer YOUR_API_KEY")
            .post(RequestBody.create(new Gson().toJson(body),
                MediaType.parse("application/json")))
            .build();

        try (Response response = new OkHttpClient().newCall(request).execute()) {
            System.out.println(response.body().string());
        }
    }
}
```

```javascript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: 'YOUR_API_KEY',
  baseURL: 'https://tokenhub.tencentmaas.com/v1',
});

const tools = [{
  type: 'function',
  function: {
    name: 'get_weather',
    description: '获取指定城市的当前天气信息',
    parameters: {
      type: 'object',
      properties: { city: { type: 'string', description: '城市名称，例如：北京' } },
      required: ['city'],
    },
  },
}];

const response = await client.chat.completions.create({
  model: 'hy4-preview',
  messages: [{ role: 'user', content: '深圳今天天气怎么样？' }],
  tools,
  tool_choice: 'auto',
});
console.log(response.choices[0].message);
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
    tool := map[string]interface{}{
        "type": "function",
        "function": map[string]interface{}{
            "name":        "get_weather",
            "description": "获取指定城市的当前天气信息",
            "parameters": map[string]interface{}{
                "type": "object",
                "properties": map[string]interface{}{
                    "city": map[string]interface{}{"type": "string", "description": "城市名称，例如：北京"},
                },
                "required": []string{"city"},
            },
        },
    }

    body, _ := json.Marshal(map[string]interface{}{
        "model":       "hy4-preview",
        "messages":    []map[string]string{{"role": "user", "content": "深圳今天天气怎么样？"}},
        "tools":       []map[string]interface{}{tool},
        "tool_choice": "auto",
    })

    req, _ := http.NewRequest("POST",
        "https://tokenhub.tencentmaas.com/v1/chat/completions",
        bytes.NewBuffer(body))
    req.Header.Set("Authorization", "Bearer YOUR_API_KEY")
    req.Header.Set("Content-Type", "application/json")

    resp, _ := http.DefaultClient.Do(req)
    defer resp.Body.Close()
    data, _ := io.ReadAll(resp.Body)
    fmt.Println(string(data))
}
```

**模型决定调用工具时的响应：**

```json
{
  "id": "REPLACED_ID",
  "object": "chat.completion",
  "model": "hy4-preview",
  "created": 1775146513,
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "我来帮你查询深圳今天的天气情况。",
        "reasoning_content": "用户问深圳今天的天气怎么样。我需要调用get_weather函数来获取深圳的天气信息。",
        "tool_calls": [
          {
            "id": "REPLACED_ID",
            "type": "function",
            "function": {
              "name": "get_weather",
              "arguments": "{\\"city\\": \\"深圳\\"}"
            }
          }
        ]
      },
      "finish_reason": "tool_calls"
    }
  ],
  "usage": {
        "prompt_tokens": 199,
        "completion_tokens": 43,
        "total_tokens": 242,
        "prompt_tokens_details": {
            "cached_tokens": 0
        },
        "completion_tokens_details": {
            "reasoning_tokens": 19
        }
    }
}
```

**回填工具执行结果继续对话：**

```json
{
  "model": "hy4-preview",
  "messages": [
    {"role": "user", "content": "深圳今天天气怎么样？"},
    {
      "role": "assistant",
      "content": "我来帮您查询深圳今天的天气情况。",
      "tool_calls": [{
          "id": "REPLACED_ID",
          "type": "function",
          "function": {"name": "get_weather", "arguments": "{\\"city\\": \\"深圳\\"}"}
        }]
    },
    {
      "role": "tool",
      "tool_call_id": "REPLACED_ID",
      "content": "{\\"temperature\\":28,\\"weather\\":\\"晴\\",\\"humidity\\":\\"65%\\"}"
    }
  ]
}
```

**注意：**

在 `reasoning_effort=low/high` 的慢思考模式下进行工具调用，**每一轮请求都需要回填历史** `reasoning_content`，以获取最佳效果。

### 结构化输出

通过 `response_format` 约束模型按指定的 JSON Schema 输出，常用于信息抽取、结构化数据生成等场景。

cURL

Python

Java

Node.js

Go

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/chat/completions' \\
  -H 'Content-Type: application/json' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -d '{
    "model": "hy4-preview",
    "messages": [
      {"role": "user", "content": "请从以下文本中提取人物信息：张三，35岁，是一名高级软件工程师，擅长Python、Java和机器学习。"}
    ],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "person_info",
        "schema": {
          "type": "object",
          "properties": {
            "name":       {"type": "string",  "description": "人物姓名"},
            "age":        {"type": "integer", "description": "年龄"},
            "occupation": {"type": "string",  "description": "职业"},
            "skills":     {"type": "array",   "items": {"type": "string"}, "description": "技能列表"}
          },
          "required": ["name", "age", "occupation", "skills"]
        }
      }
    }
  }'
```

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

schema = {
    "type": "object",
    "properties": {
        "name":       {"type": "string",  "description": "人物姓名"},
        "age":        {"type": "integer", "description": "年龄"},
        "occupation": {"type": "string",  "description": "职业"},
        "skills":     {"type": "array",   "items": {"type": "string"}, "description": "技能列表"},
    },
    "required": ["name", "age", "occupation", "skills"],
}

response = client.chat.completions.create(
    model="hy4-preview",
    messages=[
        {"role": "user", "content": "请从以下文本中提取人物信息：张三，35岁，是一名高级软件工程师，擅长Python、Java和机器学习。"},
    ],
    response_format={
        "type": "json_schema",
        "json_schema": {"name": "person_info", "schema": schema},
    },
)
print(response.choices[0].message.content)
```

```java
import okhttp3.*;
import com.google.gson.Gson;
import java.util.*;

public class StructuredOutput {
    public static void main(String[] args) throws Exception {
        Map<String, Object> schema = Map.of(
            "type", "object",
            "properties", Map.of(
                "name",       Map.of("type", "string",  "description", "人物姓名"),
                "age",        Map.of("type", "integer", "description", "年龄"),
                "occupation", Map.of("type", "string",  "description", "职业"),
                "skills",     Map.of("type", "array",   "items", Map.of("type", "string"), "description", "技能列表")
            ),
            "required", List.of("name", "age", "occupation", "skills")
        );

        Map<String, Object> body = new HashMap<>();
        body.put("model", "hy4-preview");
        body.put("messages", List.of(Map.of("role", "user", "content",
            "请从以下文本中提取人物信息：张三，35岁，是一名高级软件工程师，擅长Python、Java和机器学习。")));
        body.put("response_format", Map.of(
            "type", "json_schema",
            "json_schema", Map.of("name", "person_info", "schema", schema)
        ));

        Request request = new Request.Builder()
            .url("https://tokenhub.tencentmaas.com/v1/chat/completions")
            .header("Authorization", "Bearer YOUR_API_KEY")
            .post(RequestBody.create(new Gson().toJson(body),
                MediaType.parse("application/json")))
            .build();

        try (Response response = new OkHttpClient().newCall(request).execute()) {
            System.out.println(response.body().string());
        }
    }
}
```

```javascript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: 'YOUR_API_KEY',
  baseURL: 'https://tokenhub.tencentmaas.com/v1',
});

const schema = {
  type: 'object',
  properties: {
    name:       { type: 'string',  description: '人物姓名' },
    age:        { type: 'integer', description: '年龄' },
    occupation: { type: 'string',  description: '职业' },
    skills:     { type: 'array',   items: { type: 'string' }, description: '技能列表' },
  },
  required: ['name', 'age', 'occupation', 'skills'],
};

const response = await client.chat.completions.create({
  model: 'hy4-preview',
  messages: [
    { role: 'user', content: '请从以下文本中提取人物信息：张三，35岁，是一名高级软件工程师，擅长Python、Java和机器学习。' },
  ],
  response_format: {
    type: 'json_schema',
    json_schema: { name: 'person_info', schema },
  },
});
console.log(response.choices[0].message.content);
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
    schema := map[string]interface{}{
        "type": "object",
        "properties": map[string]interface{}{
            "name":       map[string]interface{}{"type": "string", "description": "人物姓名"},
            "age":        map[string]interface{}{"type": "integer", "description": "年龄"},
            "occupation": map[string]interface{}{"type": "string", "description": "职业"},
            "skills": map[string]interface{}{
                "type": "array", "items": map[string]string{"type": "string"}, "description": "技能列表",
            },
        },
        "required": []string{"name", "age", "occupation", "skills"},
    }

    body, _ := json.Marshal(map[string]interface{}{
        "model": "hy4-preview",
        "messages": []map[string]string{
            {"role": "user", "content": "请从以下文本中提取人物信息：张三，35岁，是一名高级软件工程师，擅长Python、Java和机器学习。"},
        },
        "response_format": map[string]interface{}{
            "type": "json_schema",
            "json_schema": map[string]interface{}{
                "name":   "person_info",
                "schema": schema,
            },
        },
    })

    req, _ := http.NewRequest("POST",
        "https://tokenhub.tencentmaas.com/v1/chat/completions",
        bytes.NewBuffer(body))
    req.Header.Set("Authorization", "Bearer YOUR_API_KEY")
    req.Header.Set("Content-Type", "application/json")

    resp, _ := http.DefaultClient.Do(req)
    defer resp.Body.Close()
    data, _ := io.ReadAll(resp.Body)
    fmt.Println(string(data))
}
```

**响应示例：**

```json
{
  "id": "REPLACED_ID",
  "object": "chat.completion",
  "model": "hy4-preview",
  "created": 1775146513,
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "{\\n  \\"name\\": \\"张三\\",\\n  \\"age\\": 35,\\n  \\"occupation\\": \\"高级软件工程师\\",\\n  \\"skills\\": [\\"Python\\", \\"Java\\", \\"机器学习\\"]\\n}",
        "reasoning_content": "We need answer in Chinese. User asks: \\"请从以下文本中提取人物信息：张三，35岁，是一名高级软件工程师，擅长Python、Java和机器学习。\\" Need extract person info. We can present structured fields: 姓名: 张三; 年龄: 35岁; 职业/职位: 高级软件工程师; 技能: Python、Java、机器学习. Possibly also mention we can format. The task is simple. Need not overcomplicate. Ensure answer directly. Maybe include a table or JSON. Since asked extract person info. I can output JSON and/or bullet list. Let's craft concise. Use Chinese. Could say: \\"提取结果如下：\\" then bullet list. Maybe include raw text? Not needed. Let's provide structured info.\\n\\nNeed consider if there is ambiguity: \\"高级软件工程师\\" is job title. \\"擅长\\" are skills/proficient in. Age 35. Name 张三. Good.\\n\\nLet's final: \\n{\\n  \\"姓名\\": \\"张三\\",\\n  \\"年龄\\": 35,\\n  \\"职业\\": \\"高级软件工程师\\",\\n  \\"技能\\": [\\"Python\\", \\"Java\\", \\"机器学习\\"]\\n}\\nOr with units. Maybe note age unit岁. That's it."
      },
      "finish_reason": "stop"
    }
  ],
    "usage": {
        "prompt_tokens": 45,
        "completion_tokens": 294,
        "total_tokens": 339,
        "prompt_tokens_details": {
            "cached_tokens": 0
        },
        "completion_tokens_details": {
            "reasoning_tokens": 252
        }
    }
}
```

## 翻译模型

Hy-MT2 是一款面向真实复杂场景的“快思考”多语言翻译模型家族，包含 **1.8B、7B、30B-A3B（MoE）**三种体量，支持 **33 个语种**之间的互译，并能高效遵循多语言翻译指令。多维度评测显示，Hy-MT2 在通用翻译、真实业务场景翻译、垂直领域翻译以及指令遵循翻译等任务上均表现出色。

### 支持的模型

<table><colgroup><col/><col/><col/><col/><col/></colgroup><tbody><tr><td><div>model（调用参数）</div></td><td><div>能力说明</div></td><td><div>上下文窗口</div></td><td><div>最大输入</div></td><td><div>最大输出</div></td></tr><tr><td><div><code>hy-mt2-pro</code></div></td><td><div>混元翻译旗舰模型，参数量30B-A3B，适合专业领域等对译文质量要求高的场景，有优秀的指令遵循能力。支持语种齐全，重点支持33个语种互译，支持5种民汉/方言。</div></td><td><div>8k</div></td><td><div>4k</div></td><td><div>4k</div></td></tr><tr><td><div><code>hy-mt2-plus</code></div></td><td><div>混元翻译模型，参数量7B。业界效果领先，开源测试集 Flores 200、WMT25效果领先，专业领域和真实业务场景表现优秀。支持语种齐全，重点支持33个语种互译，支持5种民汉/方言。</div></td><td colspan="1" rowspan="1"><div>8k</div></td><td colspan="1" rowspan="1"><div>4k</div></td><td colspan="1" rowspan="1"><div>4k</div></td></tr><tr><td><div><code>hy-mt2-lite</code></div></td><td><div>混元翻译轻量级模型，参数量1.8B。适合对耗时有高要求的场景。支持语种齐全，重点支持33个语种互译，支持5种民汉/方言。</div></td><td colspan="1" rowspan="1"><div>8k</div></td><td colspan="1" rowspan="1"><div>4k</div></td><td colspan="1" rowspan="1"><div>4k</div></td></tr></tbody></table>

### 基础翻译

最常见的翻译场景，在 `user` 消息中**明确指定目标语种**（`target_lang` 使用完整中文名，如“中文”、“英语”）。

```plaintext
"messages": {"role": "user", "content": "将以下文本翻译为 {target_lang}，注意只需要输出翻译后的结果，不要额外解释：{source_text}"}
```

cURL

Python

Java

Node.js

Go

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/chat/completions' \\
  -H 'Content-Type: application/json' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -d '{
    "model": "hy-mt2-plus",
    "messages": [
      {"role": "user", "content": "将以下文本翻译为英语，注意只需要输出翻译后的结果，不要额外解释： 会议开始前请确认所有参会人员都收到了议程。"}
    ]
  }'
```

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

target_lang = "英语"
source_text = "会议开始前请确认所有参会人员都收到了议程。"

prompt = f"""将以下文本翻译为 {target_lang}，注意只需要输出翻译后的结果，不要额外解释：
{source_text}"""

response = client.chat.completions.create(
    model="hy-mt2-plus",
    messages=[{"role": "user", "content": prompt}],
)
print(response.choices[0].message.content)
```

```java
import okhttp3.*;
import com.google.gson.Gson;
import java.util.*;

public class TranslationDemo {
    public static void main(String[] args) throws Exception {
        String targetLang = "英语";
        String sourceText = "会议开始前请确认所有参会人员都收到了议程。";
        String prompt = "将以下文本翻译为 " + targetLang + "，注意只需要输出翻译后的结果，不要额外解释：\\n" + sourceText;

        Map<String, Object> body = new HashMap<>();
        body.put("model", "hy-mt2-plus");
        body.put("messages", List.of(
            Map.of("role", "user", "content", prompt)
        ));

        Request request = new Request.Builder()
            .url("https://tokenhub.tencentmaas.com/v1/chat/completions")
            .header("Authorization", "Bearer YOUR_API_KEY")
            .post(RequestBody.create(new Gson().toJson(body),
                MediaType.parse("application/json")))
            .build();

        try (Response response = new OkHttpClient().newCall(request).execute()) {
            System.out.println(response.body().string());
        }
    }
}
```

```javascript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: 'YOUR_API_KEY',
  baseURL: 'https://tokenhub.tencentmaas.com/v1',
});

const targetLang = '英语';
const sourceText = '会议开始前请确认所有参会人员都收到了议程。';
const prompt = `将以下文本翻译为 ${targetLang}，注意只需要输出翻译后的结果，不要额外解释：\\n${sourceText}`;

const response = await client.chat.completions.create({
  model: 'hy-mt2-plus',
  messages: [{ role: 'user', content: prompt }],
});
console.log(response.choices[0].message.content);
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
    targetLang := "英语"
    sourceText := "会议开始前请确认所有参会人员都收到了议程。"
    prompt := "将以下文本翻译为 " + targetLang + "，注意只需要输出翻译后的结果，不要额外解释：\\n" + sourceText

    body, _ := json.Marshal(map[string]interface{}{
        "model": "hy-mt2-plus",
        "messages": []map[string]string{
            {"role": "user", "content": prompt},
        },
    })

    req, _ := http.NewRequest("POST",
        "https://tokenhub.tencentmaas.com/v1/chat/completions",
        bytes.NewBuffer(body))
    req.Header.Set("Authorization", "Bearer YOUR_API_KEY")
    req.Header.Set("Content-Type", "application/json")

    resp, _ := http.DefaultClient.Do(req)
    defer resp.Body.Close()
    data, _ := io.ReadAll(resp.Body)
    fmt.Println(string(data))
}
```

**响应示例：**

```json
{
  "id": "REPLACED_ID",
  "object": "chat.completion",
  "model": "hy-mt2-plus",
  "created": 1775146513,
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Please ensure that all attendees have received the agenda before the meeting starts."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 35,
    "completion_tokens": 15,
    "total_tokens": 50,
    "prompt_tokens_details": {"cached_tokens": 0},
    "completion_tokens_details": {"reasoning_tokens": 0}
  }
}
```

### 结构化数据翻译

当原文是 **JSON / Markdown / HTML / XML 等结构化数据**时，模型会“锁定结构、仅翻译可见 value、保留所有 key 与占位符”。

```plaintext
"messages": {"role": "user", "content": "
# 任务目标
将下方 {source_text} 中的 {format_type} 格式数据翻译为 {target_lang}。

# 严格约束
1. 结构锁定：绝对保持原有的 {format_type} 数据结构、缩进和层级完全不变。
2. 选择性翻译：仅翻译面向用户展示的可见文本内容。
3. 禁止修改：严禁翻译或更改任何代码标签、键名 (Key)、变量占位符（如 {{var}}、${var}、%s、%d 等）或代码属性。

# 数据输入
{source_text}"}
```

cURL

Python

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/chat/completions' \\
  -H 'Content-Type: application/json' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -d '{
    "model": "hy-mt2-plus",
    "messages": [
      {"role": "user", "content": "# 任务目标\\n将下方 source_text 中的 JSON 格式数据翻译为 英语。\\n\\n# 严格约束\\n1. 结构锁定：绝对保持原有的 JSON 数据结构、缩进和层级完全不变。\\n2. 选择性翻译：仅翻译面向用户展示的可见文本内容。\\n3. 禁止修改：严禁翻译或更改任何代码标签、键名 (Key)、变量占位符（如 {{var}}、${var}、%s、%d 等）或代码属性。\\n\\n# 数据输入\\n{\\"title\\": \\"西湖风景区\\", \\"description\\": \\"位于杭州市中心，是国家 5A 级旅游景区，四季景色宜人。\\", \\"tags\\": [\\"自然风光\\", \\"世界遗产\\", \\"免费开放\\"]}"}
    ]
  }'
```

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

target_lang = "英语"
format_type = "JSON"
source_text = '{"title": "西湖风景区", "description": "位于杭州市中心，是国家 5A 级旅游景区，四季景色宜人。", "tags": ["自然风光", "世界遗产", "免费开放"]}'

prompt = f"""# 任务目标
将下方 source_text 中的 {format_type} 格式数据翻译为 {target_lang}。

# 严格约束
1. 结构锁定：绝对保持原有的 {format_type} 数据结构、缩进和层级完全不变。
2. 选择性翻译：仅翻译面向用户展示的可见文本内容。
3. 禁止修改：严禁翻译或更改任何代码标签、键名 (Key)、变量占位符（如 {{var}}、${{var}}、%s、%d 等）或代码属性。

# 数据输入
{source_text}"""

response = client.chat.completions.create(
    model="hy-mt2-plus",
    messages=[{"role": "user", "content": prompt}],
)
print(response.choices[0].message.content)
```

**响应示例：**

```json
{
  "id": "REPLACED_ID",
  "object": "chat.completion",
  "model": "hy-mt2-plus",
  "created": 1779966611,
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "{\\"title\\": \\"West Lake Scenic Area\\", \\"description\\": \\"Located in the heart of Hangzhou, it is a national 5A-level tourist attraction known for its pleasant scenery throughout the four seasons.\\", \\"tags\\": [\\"Natural Scenery\\", \\"World Heritage\\", \\"Free Admission\\"]}"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 159,
    "completion_tokens": 59,
    "total_tokens": 218,
    "prompt_tokens_details": {"cached_tokens": 0},
    "completion_tokens_details": {"reasoning_tokens": 0}
  }
}
```

### 分隔符翻译

需要**逐句对照**或**批量翻译多段文本**时，让模型保留**等量的分隔符**且不遗漏、不转义、不翻译，便于业务侧按下标对齐。

推荐使用 `<SEP>`、`###` 等不会与目标语言标点冲突的标签作为分隔符。`|||`、`---` 等容易被部分语言识别为感叹号、破折号等标点，导致译文不可切分。

```plaintext
"messages": {"role": "user", "content": "请将以下文本准确翻译为 {target_lang}。
你必须在译文中保留等量的分隔符，绝对不可遗漏、转义或翻译该符号，并注意分隔符的位置。{source_text}"}
```

cURL

Python

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/chat/completions' \\
  -H 'Content-Type: application/json' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -d '{
    "model": "hy-mt2-plus",
    "messages": [
      {"role": "user", "content": "请将以下文本准确翻译为英语。你必须在译文中保留等量的分隔符，绝对不可遗漏、转义或翻译该符号，并注意分隔符的位置。\\n每天保持八小时睡眠有助于身体健康<SEP>合理规划工作与休息可以提升效率<SEP>适度运动能有效缓解压力"}
    ]
  }'
```

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

target_lang = "英语"
SEP = "<SEP>"
source_segments = ["每天保持八小时睡眠有助于身体健康", "合理规划工作与休息可以提升效率", "适度运动能有效缓解压力"]
source_text = SEP.join(source_segments)

prompt = f"""请将以下文本准确翻译为 {target_lang}。你必须在译文中保留等量的分隔符，绝对不可遗漏、转义或翻译该符号，并注意分隔符的位置。
{source_text}"""

response = client.chat.completions.create(
    model="hy-mt2-plus",
    messages=[{"role": "user", "content": prompt}],
)

translated = response.choices[0].message.content.split(SEP)
for src, tgt in zip(source_segments, translated):
    print(f"{src.strip()}  →  {tgt.strip()}")
```

**响应示例：**

```json
{
  "id": "REPLACED_ID",
  "object": "chat.completion",
  "model": "hy-mt2-plus",
  "created": 1779966612,
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Getting eight hours of sleep every day is beneficial for good health<SEP>Properly planning work and rest can improve efficiency<SEP>Moderate exercise can effectively relieve stress"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 65,
    "completion_tokens": 36,
    "total_tokens": 101,
    "prompt_tokens_details": {"cached_tokens": 0},
    "completion_tokens_details": {"reasoning_tokens": 0}
  }
}
```

### 上下文翻译

当原文存在**多义词、专有名词、代词指代**等需要语境消歧的情况时，提供“背景信息”可以让模型选用与上下文一致的术语。

```plaintext
"messages": {"role": "user", "content": "
【背景信息】{background_text}
请结合背景信息将以下文本翻译为 {target_lang}。
【待翻译文本】{source_text}"}
```

cURL

Python

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/chat/completions' \\
  -H 'Content-Type: application/json' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -d '{
    "model": "hy-mt2-plus",
    "messages": [
      {"role": "user", "content": "【背景信息】\\n这是一篇介绍数据库系统的技术文档，上文提到的 transaction 指数据库事务，index 指数据库索引。\\n请结合背景信息将以下文本翻译为英语。\\n【待翻译文本】\\n事务提交后，索引会被异步刷新到磁盘。"}
    ]
  }'
```

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

target_lang = "英语"
background_text = "这是一篇介绍数据库系统的技术文档，上文提到的 transaction 指数据库事务，index 指数据库索引。"
source_text = "事务提交后，索引会被异步刷新到磁盘。"

prompt = f"""【背景信息】
{background_text}
请结合背景信息将以下文本翻译为 {target_lang}。
【待翻译文本】
{source_text}"""

response = client.chat.completions.create(
    model="hy-mt2-plus",
    messages=[{"role": "user", "content": prompt}],
)
print(response.choices[0].message.content)
```

**响应示例：**

```json
{
  "id": "REPLACED_ID",
  "object": "chat.completion",
  "model": "hy-mt2-plus",
  "created": 1779966614,
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "After a transaction is committed, the index is asynchronously flushed to disk."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 68,
    "completion_tokens": 15,
    "total_tokens": 83,
    "prompt_tokens_details": {"cached_tokens": 0},
    "completion_tokens_details": {"reasoning_tokens": 0}
  }
}
```

### 术语表翻译

业务侧拥有**领域术语表**（产品名、品牌词、专有名词等需固定译法）时，将术语对照清单作为参考前置，模型会优先按指定译法翻译。

```plaintext
"messages": {"role": "user", "content": "
参考下面的翻译：
{text} 翻译成 {text}
{text} 翻译成 {text}
{text} 翻译成 {text}
将以下文本翻译为 {target_lang}，注意只需要输出翻译后的结果，不要额外解释：{source_text}"}
```

cURL

Python

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/chat/completions' \\
  -H 'Content-Type: application/json' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -d '{
    "model": "hy-mt2-plus",
    "messages": [
      {"role": "user", "content": "参考下面的翻译：\\n首播 翻译成 premiere\\n收视率 翻译成 ratings\\n将以下文本翻译为英语，注意只需要输出翻译后的结果，不要额外解释：\\n这部剧在媒体平台首播后收视率一路走高。"}
    ]
  }'
```

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

target_lang = "英语"
glossary = [
    ("首播", "premiere"),
    ("收视率", "ratings"),
]
source_text = "这部剧在媒体平台首播后收视率一路走高。"

glossary_text = "\\n".join(f"{src} 翻译成 {tgt}" for src, tgt in glossary)
prompt = f"""参考下面的翻译：
{glossary_text}
将以下文本翻译为 {target_lang}，注意只需要输出翻译后的结果，不要额外解释：
{source_text}"""

response = client.chat.completions.create(
    model="hy-mt2-plus",
    messages=[{"role": "user", "content": prompt}],
)
print(response.choices[0].message.content)
```

**响应示例：**

```json
{
  "id": "REPLACED_ID",
  "object": "chat.completion",
  "model": "hy-mt2-plus",
  "created": 1779967706,
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "The ratings for this drama kept rising after its premiere on media platforms."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 56,
    "completion_tokens": 15,
    "total_tokens": 71,
    "prompt_tokens_details": {"cached_tokens": 0},
    "completion_tokens_details": {"reasoning_tokens": 0}
  }
}
```

### 风格翻译

不同业务场景对译文风格要求不同（口语化 / 书面化 / 营销文案 / 法律合同 / 学术 / 古文等），描述出**目标风格**，模型会按要求调整用词与句式。

```plaintext
"messages": {"role": "user", "content": "
请将以下文本翻译为 {target_lang}。
注意翻译的风格要严格符合【{target_style}】
{source_text}"}
```

cURL

Python

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/chat/completions' \\
  -H 'Content-Type: application/json' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -d '{
    "model": "hy-mt2-plus",
    "messages": [
      {"role": "user", "content": "请将以下文本翻译为英语。注意翻译的风格要严格符合【科普文案：语言简洁有力、富有感染力】\\n适度户外活动有助于调节情绪，缓解精神压力。"}
    ]
  }'
```

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

target_lang = "英语"
target_style = "科普文案：语言简洁有力、富有感染力"
source_text = "适度户外活动有助于调节情绪，缓解精神压力。"

prompt = f"""请将以下文本翻译为 {target_lang}。注意翻译的风格要严格符合【{target_style}】
{source_text}"""

response = client.chat.completions.create(
    model="hy-mt2-plus",
    messages=[{"role": "user", "content": prompt}],
)
print(response.choices[0].message.content)
```

**响应示例：**

```json
{
  "id": "REPLACED_ID",
  "object": "chat.completion",
  "model": "hy-mt2-plus",
  "created": 1779966617,
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Moderate outdoor activities help regulate emotions and alleviate mental stress."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 48,
    "completion_tokens": 13,
    "total_tokens": 61,
    "prompt_tokens_details": {"cached_tokens": 0},
    "completion_tokens_details": {"reasoning_tokens": 0}
  }
}
```

### 术语库

与上述 [术语表翻译](https://cloud.tencent.com/document/product/1823/132252#a7ff516f-553b-44b9-98f5-b3c6459a956c)（prompt 内嵌术语）不同，本节使用独立的翻译接口与持久化术语库，更适合术语量大、复用频率高的工程化场景。

**注意：**

目前仅 OpenAPI 协议支持使用混元翻译术语库。接口地址：https://tokenhub.tencentmaas.com/v1/api/translations

可参考 [术语库管理相关接口](https://cloud.tencent.com/document/product/1823/132887) 创建、修改、查询术语库。

**请求参数说明**

<table><colgroup><col/><col/><col/><col/></colgroup><tbody><tr><td><div>参数</div></td><td><div>类型</div></td><td><div>必填</div></td><td><div>说明</div></td></tr><tr><td><div><code>model</code></div></td><td><div>string</div></td><td><div>是</div></td><td><div>model 参数，如 <code>hy-mt2-plus</code></div></td></tr><tr><td><div><code>text</code></div></td><td><div>string</div></td><td><div>是</div></td><td><div>待翻译的文本</div></td></tr><tr><td colspan="1" rowspan="1"><div><code>target</code></div></td><td colspan="1" rowspan="1"><div>string</div></td><td colspan="1" rowspan="1"><div>是</div></td><td colspan="1" rowspan="1"><div>目标语言代码</div></td></tr><tr><td><div><code>source</code></div></td><td><div>string</div></td><td><div>否</div></td><td><div>源语言代码，如不传参则模型自动识别</div></td></tr><tr><td colspan="1" rowspan="1"><div><code>stream</code></div></td><td colspan="1" rowspan="1"><div>bool</div></td><td colspan="1" rowspan="1"><div>否</div></td><td colspan="1" rowspan="1"><div>是否流式返回，默认 <code>false</code></div></td></tr><tr><td><div><code>context</code></div></td><td><div>string</div></td><td><div>否</div></td><td><div>上下文信息，用于让译文更连贯</div></td></tr><tr><td><div><code>references</code></div></td><td><div>list of object</div></td><td><div>否</div></td><td><div>参考示例（句子或术语），最多 10 个</div></td></tr><tr><td><div><code>references[n].type</code></div></td><td><div>string</div></td><td><div>否</div></td><td><div>翻译文本类型，其中"sentence"表示句子， "term"表示术语</div></td></tr><tr><td><div><code>references[n].text</code></div></td><td colspan="1" rowspan="1"><div>string</div></td><td colspan="1" rowspan="1"><div>否</div></td><td><div>参考示例的原文</div></td></tr><tr><td><div><code>references[n].translation</code></div></td><td colspan="1" rowspan="1"><div>string</div></td><td colspan="1" rowspan="1"><div>否</div></td><td><div>参考示例的译文</div></td></tr><tr><td colspan="1" rowspan="1"><div><code>glossary_ids</code></div></td><td colspan="1" rowspan="1"><div>list of string</div></td><td colspan="1" rowspan="1"><div>否</div></td><td colspan="1" rowspan="1"><div>术语库 ID 列表，最多 10 个，可参考 <a href="https://cloud.tencent.com/document/product/1823/132887">术语库管理相关接口</a> 创建术语库</div></td></tr></tbody></table>

**响应字段说明**

<table><colgroup><col/><col/><col/></colgroup><tbody><tr><td><div>字段</div></td><td><div>类型</div></td><td><div>说明</div></td></tr><tr><td><div><code>id</code></div></td><td><div>string</div></td><td><div>此次请求的 id</div></td></tr><tr><td><div><code>created</code></div></td><td><div>integer</div></td><td><div>Unix 时间戳</div></td></tr><tr><td><div><code>choices</code></div></td><td><div>list</div></td><td><div>返回的回复, 支持多个</div></td></tr><tr><td colspan="1" rowspan="1"><div><code>choices[n].finish_reason</code></div></td><td colspan="1" rowspan="1"><div>string</div></td><td colspan="1" rowspan="1"><div><code>stop</code> 表示正常结束，<code>sensitive</code> 表示审核不通过</div></td></tr><tr><td><div><code>choices[n].message</code></div></td><td><div>json</div></td><td><div>返回的内容</div></td></tr><tr><td><div><code>choices[n].message.role</code></div></td><td><div>string</div></td><td><div>角色名称</div></td></tr><tr><td><div><code>choices[n].message.content</code></div></td><td><div>string</div></td><td><div>翻译后的文本</div></td></tr><tr><td><div><code>choices[n].delta</code></div></td><td><div>json</div></td><td><div>返回的内容（流式）</div></td></tr><tr><td><div><code>choices[n].delta.role</code></div></td><td><div>string</div></td><td><div>角色名称（流式）</div></td></tr><tr><td><div><code>choices[n].delta.content</code></div></td><td><div>string</div></td><td><div>翻译后的文本（流式）</div></td></tr><tr><td><div><code>source</code> </div></td><td><div>string</div></td><td><div>请求源语言</div></td></tr><tr><td colspan="1" rowspan="1"><div><code>target</code></div></td><td colspan="1" rowspan="1"><div>string</div></td><td colspan="1" rowspan="1"><div>目标语言</div></td></tr><tr><td><div><code>usage</code></div></td><td><div>object</div></td><td><div>token 使用量</div></td></tr></tbody></table>

**请求示例**

cURL

Python

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/api/translations' \\
  -H 'Content-Type: application/json' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -d '{
    "model": "hy-mt2-plus",
    "text": "该车型搭载先进的电池管理系统，续航里程超过 600 公里并支持快充。",
    "source": "zh",
    "target": "en",
    "glossary_ids": ["YOUR_GLOSSARY_ID"]
  }'
```

```python
import requests

url = "https://tokenhub.tencentmaas.com/v1/api/translations"
headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json",
}
payload = {
    "model": "hy-mt2-plus",
    "text": "该车型搭载先进的电池管理系统，续航里程超过 600 公里并支持快充。",
    "source": "zh",
    "target": "en",
    "glossary_ids": ["YOUR_GLOSSARY_ID"],
}

response = requests.post(url, headers=headers, json=payload)
data = response.json()
print(data["choices"][0]["message"]["content"])
```

**响应示例**

```json
{
  "id": "REPLACED_ID",
  "created": 1781604284,
  "choices": [
    {
      "index": 0,
      "finish_reason": "stop",
      "message": {
        "role": "assistant",
        "content": "This model is equipped with an advanced Battery Management System (BMS), offering a driving range of over 600 kilometers along with fast charging support."
      }
    }
  ],
  "source": "zh",
  "target": "en",
  "usage": {
    "prompt_tokens": 82,
    "completion_tokens": 32,
    "total_tokens": 114
  }
}
```

### 支持的语言

| 语言 | 英文名 | 代码 |
| --- | --- | --- |
| 简体中文 | Chinese | `zh` |
| 繁体中文 | Traditional Chinese | `zh-TR` |
| 英语 | English | `en` |
| 法语 | French | `fr` |
| 葡萄牙语 | Portuguese | `pt` |
| 西班牙语 | Spanish | `es` |
| 日语 | Japanese | `ja` |
| 土耳其语 | Turkish | `tr` |
| 俄语 | Russian | `ru` |
| 阿拉伯语 | Arabic | `ar` |
| 韩语 | Korean | `ko` |
| 泰语 | Thai | `th` |
| 意大利语 | Italian | `it` |
| 德语 | German | `de` |
| 越南语 | Vietnamese | `vi` |
| 马来语 | Malay | `ms` |
| 印尼语 | Indonesian | `id` |
| 菲律宾语 | Filipino | `fil` |
| 印地语 | Hindi | `hi` |
| 波兰语 | Polish | `pl` |
| 捷克语 | Czech | `cs` |
| 荷兰语 | Dutch | `nl` |
| 高棉语 | Khmer | `km` |
| 缅甸语 | Burmese | `my` |
| 波斯语 | Persian | `fa` |
| 古吉拉特语 | Gujarati | `gu` |
| 乌尔都语 | Urdu | `ur` |
| 泰卢固语 | Telugu | `te` |
| 马拉地语 | Marathi | `mr` |
| 希伯来语 | Hebrew | `he` |
| 孟加拉语 | Bengali | `bn` |
| 泰米尔语 | Tamil | `ta` |
| 乌克兰语 | Ukrainian | `uk` |
| 藏语 | Tibetan | `bo` |
| 哈萨克语 | Kazakh | `kk` |
| 蒙古语 | Mongolian | `mn` |
| 维吾尔语 | Uyghur | `ug` |
| 粤语 | Cantonese | `yue` |

## 角色扮演模型

`hunyuan-role-latest` 是混元的**角色扮演模型**，适用于 AI 数字分身、AI 角色扮演、AI 情感陪聊等场景。建议在 `system` 中给出清晰的人设描述（背景/性格/语言风格/禁忌），多轮对话中模型会保持人设一致性。

### 支持的模型

<table><colgroup><col/><col/><col/><col/><col/></colgroup><tbody><tr><td><div>model（调用参数）</div></td><td><div>能力说明</div></td><td><div>上下文窗口</div></td><td><div>最大输入</div></td><td><div>最大输出</div></td></tr><tr><td><div><code>hunyuan-role-latest</code></div></td><td><div>角色扮演模型，深度优化聊天体验与剧情互动</div></td><td><div>32k</div></td><td><div>28k</div></td><td><div>4k</div></td></tr><tr><td><div><code>hy-role</code></div></td><td><div>角色扮演模型，贴合各种人设、剧情演绎</div></td><td colspan="1" rowspan="1"><div>32k</div></td><td colspan="1" rowspan="1"><div>28k</div></td><td colspan="1" rowspan="1"><div>4k</div></td></tr></tbody></table>

调用示例

cURL

Python

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/chat/completions' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
    "model": "hunyuan-role-latest",
    "messages": [
      {"role": "system", "content": "你叫小溪，是一名性格温柔、有耐心的咖啡店店员，喜欢和客人轻松聊天。请保持自然口语化的中文回复，不要承认自己是 AI。"},
      {"role": "user", "content": "今天工作好累，想喝杯什么提提神？"}
    ]
  }'
```

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

response = client.chat.completions.create(
    model="hunyuan-role-latest",
    messages=[
        {
            "role": "system",
            "content": "你叫小溪，是一名性格温柔、有耐心的咖啡店店员，喜欢和客人轻松聊天。请保持自然口语化的中文回复，不要承认自己是 AI。",
        },
        {"role": "user", "content": "今天工作好累，想喝杯什么提提神？"},
    ],
)
print(response.choices[0].message.content)
```

**响应示例：**

```json
{
  "id": "REPLACED_ID",
  "object": "chat.completion",
  "model": "hunyuan-role-latest",
  "created": 1775146513,
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "那你试试美式吧，苦中带点香，一口下去超提神的！（歪头思索片刻，眼睛亮晶晶地看着你）或者你喜欢甜一点的话，拿铁也不错哦。"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 52,
    "completion_tokens": 44,
    "total_tokens": 96,
    "prompt_tokens_details": {"cached_tokens": 0},
    "completion_tokens_details": {"reasoning_tokens": 0}
  }
}
```

## 视觉与多模态模型指引

本文中的混元语言模型**不支持图片、视频等多模态输入**。如需多模态能力，请改用对应的视觉模型、多模态理解模型，调用方式与请求格式请参见各专项文档：

[图像生成](https://cloud.tencent.com/document/product/1823/130080)

[视频生成](https://cloud.tencent.com/document/product/1823/130081)

[3D 生成](https://cloud.tencent.com/document/product/1823/130082)

[多模态理解](https://cloud.tencent.com/document/product/1823/130988)

## 错误处理与调试建议

**错误码**：API 报错请参见 [API 错误码说明](https://cloud.tencent.com/document/product/1823/131595)。

**思考模式调试**：使用 `hy3` 时，如果只看到空响应或被截断，请优先检查 `max_tokens` 是否设置过小（思考模型的推理 + 回答共享 token 额度，建议 ≥ 16000）。请参见 [深度思考](https://cloud.tencent.com/document/product/1823/131208)、[交错式思考模式](https://cloud.tencent.com/document/product/1823/130930)。

**流式超时**：长输出场景建议开启 `stream: true`，避免网关侧超时。
