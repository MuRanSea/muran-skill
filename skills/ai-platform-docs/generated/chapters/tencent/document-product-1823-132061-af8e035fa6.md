<!-- Official source: https://cloud.tencent.com/document/product/1823/132061 -->
<!-- Source SHA-256: a34dc90aa467affce01c8fa144c94f36d136b0cb86b180a1ee10bde7d5cd58f1 -->

# GLM 调用指南

官方来源：https://cloud.tencent.com/document/product/1823/132061
最近更新时间：2026-10-13 15:50:30

## 概述

智谱 GLM 系列模型已接入 TokenHub 平台。您可以通过 OpenAI 兼容协议调用 GLM 系列模型，实现通用对话、深度推理、工具调用和多模态理解等能力。

通用调用方式（BaseURL、API Key、messages 拼接、Function Calling、流式输出等）请参见 [语言模型调用概览](https://cloud.tencent.com/document/product/1823/130079)。本文仅介绍 GLM 系列的特有能力和使用方式。

## 前提条件

已注册腾讯云账号并开通 TokenHub 服务。

已在 [TokenHub 控制台](https://console.cloud.tencent.com/tokenhub/apikey) 获取 API Key。

已根据所用语言安装对应 SDK 或具备 HTTP 请求能力。

## 快速开始

以下示例展示如何调用 `glm-5.3` 模型完成一次基础对话。请将 `YOUR_API_KEY` 替换为您创建的 API Key。

cURL

Python

Node.js

Java

Go

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/chat/completions' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
    "model": "glm-5.3",
    "messages": [{"role": "user", "content": "你好"}],
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
    model="glm-5.3",
    messages=[{"role": "user", "content": "你好"}],
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
  model: 'glm-5.3',
  messages: [{ role: 'user', content: '你好' }],
  max_tokens: 1024,
});
console.log(response.choices[0].message.content);
```

```java
import okhttp3.*;
import com.google.gson.Gson;
import java.util.*;

public class GlmQuickStart {
    public static void main(String[] args) throws Exception {
        Map<String, Object> body = new HashMap<>();
        body.put("model", "glm-5.3");
        body.put("messages", List.of(Map.of("role", "user", "content", "你好")));
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
        "model":      "glm-5.3",
        "messages":   []map[string]string{{"role": "user", "content": "你好"}},
        "max_tokens": 1024,
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

GLM 系列模型默认开启思考模式，响应中会包含 `reasoning_content` 字段。如不需要思考过程，请参见下文 [思考模式](https://cloud.tencent.com/document/product/1823/132061#f5553c9a-2806-4260-b944-d2fcfb7136be) 章节关闭。

## 支持的模型

| model 参数值 | 定位 | 上下文 / 最大输出 | 多模态 | 推荐场景 |
| --- | --- | --- | --- | --- |
| `glm-5.3` | 旗舰（最新） | 1M tokens / 128K tokens | 不支持 | 深度推理、复杂任务、Agent 与编码、长程任务 |
| `glm-5.3-flashx` | 轻量多模态（增强） | 1M tokens / 128K tokens | 支持图片、视频、文件 | 多模态理解、高速推理（200 tokens/s）、日常对话与创作 |
| `glm-5.3-flash` | 轻量多模态 | 1M tokens / 128K tokens | 支持图片、视频、文件 | 多模态理解、快速推理、日常对话与创作 |
| `glm-5.2` | 旗舰 | 1M tokens / 128K tokens | 不支持 | Agent 与编码、长程任务、全栈开发、代码翻译、科研复现 |
| `glm-5v-turbo`（即将下线） | 多模态 | 200K tokens / 128K tokens | 支持图片、视频、文件 | 图像理解、视频分析、文档解析 |

## 思考模式

GLM 系列将对话能力与推理能力合为一体，可通过 `thinking` 参数控制是否启用思考能力，无需切换 model 参数。

### 开启或关闭思考

通过 `thinking` 字段控制思考行为。该字段为对象格式，包含一个 `type` 属性：

| 字段 | 类型 | 取值 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `type` | String | `enabled` / `disabled` | `enabled` | 控制当前请求是否启用思考能力。**GLM-5.3、GLM-5.3-Flash 和 GLM-5.3-FlashX 默认启用且不支持关闭（即不支持** `disabled` **值），传入** `disabled` **会导致请求失败** |

以下示例展示如何在请求中关闭思考：

cURL

Python

Node.js

Java

Go

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/chat/completions' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
    "model": "glm-5.3",
    "messages": [{"role": "user", "content": "你好"}],
    "thinking": {"type": "disabled"}
  }'
```

```python
response = client.chat.completions.create(
    model="glm-5.3",
    messages=[{"role": "user", "content": "你好"}],
    extra_body={"thinking": {"type": "disabled"}},
)
```

```javascript
const response = await client.chat.completions.create({
  model: 'glm-5.3',
  messages: [{ role: 'user', content: '你好' }],
  // @ts-ignore - thinking 为 GLM 扩展字段
  thinking: { type: 'disabled' },
});
```

```java
import okhttp3.*;
import com.google.gson.Gson;
import java.util.*;

public class GlmThinkingDisabled {
    public static void main(String[] args) throws Exception {
        Map<String, Object> body = new HashMap<>();
        body.put("model", "glm-5.3");
        body.put("messages", List.of(Map.of("role", "user", "content", "你好")));
        body.put("thinking", Map.of("type", "disabled"));

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
        "model":    "glm-5.3",
        "messages": []map[string]string{{"role": "user", "content": "你好"}},
        "thinking": map[string]string{"type": "disabled"},
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

`thinking` 不是 OpenAI 标准字段。使用 OpenAI SDK 时需通过 SDK 提供的额外字段机制（Python 用 `extra_body`、Node.js 直接传字段）；HTTP 直接调用时放在请求体顶层。

### 获取思考内容

开启思考后，响应中会新增 `reasoning_content` 字段，与 `content` 同级：

```json
{
  "choices": [{
    "message": {
      "role": "assistant",
      "reasoning_content": "让我分析一下这个问题...",
      "content": "最终答案是..."
    }
  }]
}
```

由于 `reasoning_content` 不是 OpenAI 标准字段，使用各语言 SDK 时需通过判空或反射方式访问；HTTP 直接调用时直接读取响应 JSON 即可。

Python

Node.js

Java

Go

```python
message = response.choices[0].message
if hasattr(message, "reasoning_content") and message.reasoning_content:
    print("思考过程：", message.reasoning_content)
print("回答：", message.content)
```

```javascript
const message = response.choices[0].message;
// @ts-ignore - reasoning_content 为 GLM 扩展字段
if (message.reasoning_content) {
  console.log('思考过程：', message.reasoning_content);
}
console.log('回答：', message.content);
```

```java
// HTTP 调用拿到响应字符串后，用 Gson 解析 reasoning_content 和 content 字段
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;

String respBody = response.body().string();
JsonObject json = JsonParser.parseString(respBody).getAsJsonObject();
JsonObject message = json.getAsJsonArray("choices")
    .get(0).getAsJsonObject()
    .getAsJsonObject("message");

if (message.has("reasoning_content") && !message.get("reasoning_content").isJsonNull()) {
    System.out.println("思考过程：" + message.get("reasoning_content").getAsString());
}
System.out.println("回答：" + message.get("content").getAsString());
```

```go
type Message struct {
    Role             string `json:"role"`
    Content          string `json:"content"`
    ReasoningContent string `json:"reasoning_content,omitempty"`
}

type Choice struct {
    Index   int     `json:"index"`
    Message Message `json:"message"`
}

type ChatResponse struct {
    Choices []Choice `json:"choices"`
}

var result ChatResponse
json.Unmarshal(data, &result)

if result.Choices[0].Message.ReasoningContent != "" {
    fmt.Println("思考过程：", result.Choices[0].Message.ReasoningContent)
}
fmt.Println("回答：", result.Choices[0].Message.Content)
```

### 多轮对话处理

构建后续轮次的 `messages` 时，无需回写 `reasoning_content`。仅将 `content` 字段作为 `assistant` 消息传入即可。

### 流式调用

启用思考模式时建议使用流式调用（`stream=True`）。思考内容可能较长，非流式调用容易触发网关超时。

流式模式下，`reasoning_content` 会在 `content` 之前完整输出。客户端处理逻辑：累积 `delta.reasoning_content` 输出思考过程，再累积 `delta.content` 输出最终回答。

cURL

Python

Node.js

Java

Go

```bash
curl -N -X POST 'https://tokenhub.tencentmaas.com/v1/chat/completions' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
    "model": "glm-5.3",
    "messages": [{"role": "user", "content": "解释量子纠缠"}],
    "stream": true,
    "stream_options": {"include_usage": true},
    "thinking": {"type": "enabled"}
  }'
```

```python
stream = client.chat.completions.create(
    model="glm-5.3",
    messages=[{"role": "user", "content": "解释量子纠缠"}],
    stream=True,
    stream_options={"include_usage": True},
    extra_body={"thinking": {"type": "enabled"}},
)

is_answering = False
for chunk in stream:
    if not chunk.choices:
        continue
    delta = chunk.choices[0].delta
    if hasattr(delta, "reasoning_content") and delta.reasoning_content:
        print(delta.reasoning_content, end="", flush=True)
    if hasattr(delta, "content") and delta.content:
        if not is_answering:
            print("\\n--- 回答 ---\\n")
            is_answering = True
        print(delta.content, end="", flush=True)
```

```javascript
const stream = await client.chat.completions.create({
  model: 'glm-5.3',
  messages: [{ role: 'user', content: '解释量子纠缠' }],
  stream: true,
  stream_options: { include_usage: true },
  // @ts-ignore - thinking 为 GLM 扩展字段
  thinking: { type: 'enabled' },
});

let isAnswering = false;
for await (const chunk of stream) {
  if (!chunk.choices?.length) continue;
  const delta = chunk.choices[0].delta;
  // @ts-ignore - reasoning_content 为 GLM 扩展字段
  if (delta.reasoning_content) {
    process.stdout.write(delta.reasoning_content);
  }
  if (delta.content) {
    if (!isAnswering) {
      process.stdout.write('\\n--- 回答 ---\\n');
      isAnswering = true;
    }
    process.stdout.write(delta.content);
  }
}
```

```java
import okhttp3.*;
import com.google.gson.*;
import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class GlmStream {
    public static void main(String[] args) throws Exception {
        Map<String, Object> body = new HashMap<>();
        body.put("model", "glm-5.3");
        body.put("messages", List.of(Map.of("role", "user", "content", "解释量子纠缠")));
        body.put("stream", true);
        body.put("stream_options", Map.of("include_usage", true));
        body.put("thinking", Map.of("type", "enabled"));

        Request request = new Request.Builder()
            .url("https://tokenhub.tencentmaas.com/v1/chat/completions")
            .header("Authorization", "Bearer YOUR_API_KEY")
            .post(RequestBody.create(new Gson().toJson(body), MediaType.parse("application/json")))
            .build();

        try (Response response = new OkHttpClient().newCall(request).execute();
             BufferedReader reader = new BufferedReader(
                 new InputStreamReader(response.body().byteStream()))) {
            String line;
            boolean isAnswering = false;
            while ((line = reader.readLine()) != null) {
                if (!line.startsWith("data: ")) continue;
                String data = line.substring(6);
                if (data.equals("[DONE]")) break;

                JsonObject chunk = JsonParser.parseString(data).getAsJsonObject();
                JsonArray choices = chunk.getAsJsonArray("choices");
                if (choices == null || choices.size() == 0) continue;
                JsonObject delta = choices.get(0).getAsJsonObject().getAsJsonObject("delta");

                if (delta.has("reasoning_content") && !delta.get("reasoning_content").isJsonNull()) {
                    System.out.print(delta.get("reasoning_content").getAsString());
                }
                if (delta.has("content") && !delta.get("content").isJsonNull()) {
                    if (!isAnswering) {
                        System.out.println("\\n--- 回答 ---");
                        isAnswering = true;
                    }
                    System.out.print(delta.get("content").getAsString());
                }
            }
        }
    }
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

type StreamDelta struct {
    Content          string `json:"content,omitempty"`
    ReasoningContent string `json:"reasoning_content,omitempty"`
}

type StreamChoice struct {
    Delta StreamDelta `json:"delta"`
}

type StreamChunk struct {
    Choices []StreamChoice `json:"choices"`
}

func main() {
    body, _ := json.Marshal(map[string]interface{}{
        "model":          "glm-5.3",
        "messages":       []map[string]string{{"role": "user", "content": "解释量子纠缠"}},
        "stream":         true,
        "stream_options": map[string]bool{"include_usage": true},
        "thinking":       map[string]string{"type": "enabled"},
    })

    req, _ := http.NewRequest("POST",
        "https://tokenhub.tencentmaas.com/v1/chat/completions",
        bytes.NewBuffer(body))
    req.Header.Set("Authorization", "Bearer YOUR_API_KEY")
    req.Header.Set("Content-Type", "application/json")

    resp, _ := http.DefaultClient.Do(req)
    defer resp.Body.Close()

    isAnswering := false
    scanner := bufio.NewScanner(resp.Body)
    for scanner.Scan() {
        line := scanner.Text()
        if !strings.HasPrefix(line, "data: ") {
            continue
        }
        data := strings.TrimPrefix(line, "data: ")
        if data == "[DONE]" {
            break
        }
        var chunk StreamChunk
        if err := json.Unmarshal([]byte(data), &chunk); err != nil {
            continue
        }
        if len(chunk.Choices) == 0 {
            continue
        }
        delta := chunk.Choices[0].Delta
        if delta.ReasoningContent != "" {
            fmt.Print(delta.ReasoningContent)
        }
        if delta.Content != "" {
            if !isAnswering {
                fmt.Println("\\n--- 回答 ---")
                isAnswering = true
            }
            fmt.Print(delta.Content)
        }
    }
}
```

### 思考深度（reasoning\_effort）

`glm-5.2`、`glm-5.3`、`glm-5.3-flash` 和 `glm-5.3-flashx` 在 `thinking` 字段之外，额外提供 `reasoning_effort` 参数用于控制思考深度，便于在效果与延迟之间灵活权衡。该参数仅 `glm-5.2`、`glm-5.3`、`glm-5.3-flash` 和 `glm-5.3-flashx` 支持，其他 GLM 模型请使用 `thinking` 字段控制（参见上文 [开启或关闭思考](https://cloud.tencent.com/document/product/1823/132061#649d4082-6015-4dcd-b6e1-d98852cf50ff)）。不传时默认 `max`。

<table><colgroup><col/><col/><col/></colgroup><tbody><tr><td><div>模型</div></td><td><div>取值</div></td><td><div>说明</div></td></tr><tr><td rowspan="3"><div><code>glm-5.3</code></div></td><td><div><code>max</code></div></td><td><div>深度推理（<b>默认值</b>）。适合复杂推理、长程任务、深度代码分析等场景。</div></td></tr><tr><td colspan="0" rowspan="0"><div></div></td><td><div><code>high</code></div></td><td><div>增强推理。适合常规推理、代码生成等场景。</div></td></tr><tr><td colspan="0" rowspan="0"><div></div></td><td><div><code>low</code></div></td><td><div>轻度推理。适合简单问答、快速响应等对延迟敏感的场景。</div></td></tr><tr><td rowspan="3"><div><code>glm-5.2</code></div></td><td><div><code>max</code>、<code>xhigh</code></div></td><td><div>深度推理（<b>默认值</b>，<code>xhigh</code> 效果等同 <code>max</code>）。适合复杂推理、长程任务等场景。</div></td></tr><tr><td colspan="0" rowspan="0"><div></div></td><td><div><code>high</code>、<code>medium</code>、<code>low</code></div></td><td><div>增强推理（三者效果等同）。适合常规推理、代码生成等场景。</div></td></tr><tr><td colspan="0" rowspan="0"><div></div></td><td><div><code>minimal</code>、<code>none</code></div></td><td><div>放弃思考，等同于关闭思考。</div></td></tr></tbody></table>

`reasoning_effort` 不是 OpenAI 标准字段。使用 OpenAI SDK 时需通过 SDK 提供的额外字段机制（Python 用 `extra_body`、Node.js 直接传字段）；HTTP 直接调用时放在请求体顶层。示例如下：

cURL

Python

Node.js

```bash
curl --location -X POST 'https://tokenhub.tencentmaas.com/v1/chat/completions' \\
  --header "Authorization: Bearer ${API_KEY}" \\
  --header 'Content-Type: application/json' \\
  --data-raw '{
    "model": "glm-5.2",
    "messages": [
      {"role": "user", "content": "请分析以下代码的性能瓶颈并给出优化方案。"}
    ],
    "thinking": {"type": "enabled"},
    "reasoning_effort": "max",
    "temperature": 1.0,
    "max_tokens": 65536
  }'
```

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1"
)

response = client.chat.completions.create(
    model="glm-5.2",
    messages=[
        {"role": "user", "content": "请证明根号 2 是无理数。"}
    ],
    extra_body={
        "thinking": {"type": "enabled"},
        "reasoning_effort": "max",
    },
    temperature=1.0,
    max_tokens=65536,
)

print(response.choices[0].message.content)
```

```javascript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: 'YOUR_API_KEY',
  baseURL: 'https://tokenhub.tencentmaas.com/v1',
});

const completion = await client.chat.completions.create({
  model: 'glm-5.2',
  messages: [
    { role: 'user', content: '请分析这段代码的复杂度并给出优化建议。' },
  ],
  // @ts-ignore - thinking / reasoning_effort 为 GLM 扩展字段
  thinking: { type: 'enabled' },
  // @ts-ignore
  reasoning_effort: 'max',
  temperature: 1.0,
  max_tokens: 65536,
});

console.log(completion.choices[0].message.content);
```

**说明：**

`thinking` 控制是否启用思考能力（开启 / 关闭）。`glm-5.3` 和 `glm-5.3-flash` 不支持关闭，传入 `disabled` 会导致请求失败。

`reasoning_effort` 控制思考深度，仅 `glm-5.2` / `glm-5.3` / `glm-5.3-flash` 支持，默认 `max`。

`thinking` 对象还支持 `clear_thinking` 布尔字段，智谱建议设置为 `false`。

`glm-5.2` 的 `xhigh` 等同 `max`，`medium` 等同 `high`，`low` 映射为 `high`，`minimal` / `none` 等同关闭思考。

开启深度思考时，建议同时设置 `thinking: {"type": "enabled"}` 和 `reasoning_effort: "max"`。

### 推荐参数

为获得最佳效果，建议使用以下参数配置：

| 参数 | 推荐值 | 说明 |
| --- | --- | --- |
| `temperature` | `1`（默认值） | GLM-5.3、GLM-5.3-Flash 和 GLM-5.3-FlashX 推荐使用默认值，可获得更稳定的输出质量。 |
| `top_p` | `0.95`（默认值） | 与 temperature 配合使用，控制采样范围。 |

**说明：**

以上参数为 GLM-5.3、GLM-5.3-Flash 和 GLM-5.3-FlashX 的推荐配置。其他 GLM 版本可能需要根据实际情况调整。

## 工具调用

GLM 系列的 Function Calling 遵循 OpenAI 标准协议（`tools` / `tool_choice`）。通用用法请参见 [调用概览](https://cloud.tencent.com/document/product/1823/130079)。

### 流式场景下的参数拼接

GLM 模型在流式调用时，`tool_call.arguments` 会分多个 chunk 增量返回，客户端需要按 `tool_call.index` 累积拼接：

Python

Node.js

Java

Go

```python
tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "查询指定城市的天气",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "城市名称"}
            },
            "required": ["city"]
        }
    }
}]

completion = client.chat.completions.create(
    model="glm-5.3",
    messages=[{"role": "user", "content": "查询深圳天气"}],
    tools=tools,
    stream=True,
    extra_body={"thinking": {"type": "disabled"}},
)

arg_buffer = ""
tool_name = ""
for chunk in completion:
    if not chunk.choices:
        continue
    delta = chunk.choices[0].delta
    if hasattr(delta, "tool_calls") and delta.tool_calls:
        for tc in delta.tool_calls:
            if tc.function and tc.function.name:
                tool_name = tc.function.name
            if tc.function and tc.function.arguments:
                arg_buffer += tc.function.arguments

print(f"调用工具：{tool_name}")
print(f"完整参数：{arg_buffer}")  # 输出：{"city": "深圳"}
```

```javascript
const tools = [{
  type: 'function',
  function: {
    name: 'get_weather',
    description: '查询指定城市的天气',
    parameters: {
      type: 'object',
      properties: {
        city: { type: 'string', description: '城市名称' }
      },
      required: ['city']
    }
  }
}];

const completion = await client.chat.completions.create({
  model: 'glm-5.3',
  messages: [{ role: 'user', content: '查询深圳天气' }],
  tools: tools,
  stream: true,
  // @ts-ignore - thinking 为 GLM 扩展字段
  thinking: { type: 'disabled' },
});

let argBuffer = '';
let toolName = '';
for await (const chunk of completion) {
  if (!chunk.choices?.length) continue;
  const delta = chunk.choices[0].delta;
  if (delta.tool_calls) {
    for (const tc of delta.tool_calls) {
      if (tc.function?.name) toolName = tc.function.name;
      if (tc.function?.arguments) argBuffer += tc.function.arguments;
    }
  }
}

console.log(`调用工具：${toolName}`);
console.log(`完整参数：${argBuffer}`);  // 输出：{"city": "深圳"}
```

```java
import okhttp3.*;
import com.google.gson.*;
import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;

List<Map<String, Object>> tools = List.of(Map.of(
    "type", "function",
    "function", Map.of(
        "name", "get_weather",
        "description", "查询指定城市的天气",
        "parameters", Map.of(
            "type", "object",
            "properties", Map.of("city", Map.of("type", "string", "description", "城市名称")),
            "required", List.of("city")
        )
    )
));

Map<String, Object> body = new HashMap<>();
body.put("model", "glm-5.3");
body.put("messages", List.of(Map.of("role", "user", "content", "查询深圳天气")));
body.put("tools", tools);
body.put("stream", true);
body.put("thinking", Map.of("type", "disabled"));

Request request = new Request.Builder()
    .url("https://tokenhub.tencentmaas.com/v1/chat/completions")
    .header("Authorization", "Bearer YOUR_API_KEY")
    .post(RequestBody.create(new Gson().toJson(body), MediaType.parse("application/json")))
    .build();

StringBuilder argBuffer = new StringBuilder();
String toolName = "";

try (Response response = new OkHttpClient().newCall(request).execute();
     BufferedReader reader = new BufferedReader(
         new InputStreamReader(response.body().byteStream()))) {
    String line;
    while ((line = reader.readLine()) != null) {
        if (!line.startsWith("data: ")) continue;
        String data = line.substring(6);
        if (data.equals("[DONE]")) break;

        JsonObject chunk = JsonParser.parseString(data).getAsJsonObject();
        JsonArray choices = chunk.getAsJsonArray("choices");
        if (choices == null || choices.size() == 0) continue;
        JsonObject delta = choices.get(0).getAsJsonObject().getAsJsonObject("delta");

        if (delta.has("tool_calls") && delta.get("tool_calls").isJsonArray()) {
            for (JsonElement tcEl : delta.getAsJsonArray("tool_calls")) {
                JsonObject fn = tcEl.getAsJsonObject().getAsJsonObject("function");
                if (fn != null) {
                    if (fn.has("name") && !fn.get("name").isJsonNull()) {
                        toolName = fn.get("name").getAsString();
                    }
                    if (fn.has("arguments") && !fn.get("arguments").isJsonNull()) {
                        argBuffer.append(fn.get("arguments").getAsString());
                    }
                }
            }
        }
    }
}
System.out.println("调用工具：" + toolName);
System.out.println("完整参数：" + argBuffer);
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

type ToolCallFunction struct {
    Name      string `json:"name,omitempty"`
    Arguments string `json:"arguments,omitempty"`
}

type ToolCall struct {
    Index    int              `json:"index"`
    Function ToolCallFunction `json:"function"`
}

type ToolStreamDelta struct {
    ToolCalls []ToolCall `json:"tool_calls,omitempty"`
}

type ToolStreamChoice struct {
    Delta ToolStreamDelta `json:"delta"`
}

type ToolStreamChunk struct {
    Choices []ToolStreamChoice `json:"choices"`
}

func main() {
    tools := []map[string]interface{}{{
        "type": "function",
        "function": map[string]interface{}{
            "name":        "get_weather",
            "description": "查询指定城市的天气",
            "parameters": map[string]interface{}{
                "type": "object",
                "properties": map[string]interface{}{
                    "city": map[string]interface{}{"type": "string", "description": "城市名称"},
                },
                "required": []string{"city"},
            },
        },
    }}

    body, _ := json.Marshal(map[string]interface{}{
        "model":    "glm-5.3",
        "messages": []map[string]string{{"role": "user", "content": "查询深圳天气"}},
        "tools":    tools,
        "stream":   true,
        "thinking": map[string]string{"type": "disabled"},
    })

    req, _ := http.NewRequest("POST",
        "https://tokenhub.tencentmaas.com/v1/chat/completions",
        bytes.NewBuffer(body))
    req.Header.Set("Authorization", "Bearer YOUR_API_KEY")
    req.Header.Set("Content-Type", "application/json")

    resp, _ := http.DefaultClient.Do(req)
    defer resp.Body.Close()

    var argBuffer strings.Builder
    var toolName string
    scanner := bufio.NewScanner(resp.Body)
    for scanner.Scan() {
        line := scanner.Text()
        if !strings.HasPrefix(line, "data: ") {
            continue
        }
        data := strings.TrimPrefix(line, "data: ")
        if data == "[DONE]" {
            break
        }
        var chunk ToolStreamChunk
        if err := json.Unmarshal([]byte(data), &chunk); err != nil {
            continue
        }
        if len(chunk.Choices) == 0 {
            continue
        }
        for _, tc := range chunk.Choices[0].Delta.ToolCalls {
            if tc.Function.Name != "" {
                toolName = tc.Function.Name
            }
            if tc.Function.Arguments != "" {
                argBuffer.WriteString(tc.Function.Arguments)
            }
        }
    }
    fmt.Printf("调用工具：%s\\n完整参数：%s\\n", toolName, argBuffer.String())
}
```

### tool\_stream 参数

GLM 系列支持 `tool_stream` 参数（Boolean 类型），用于控制工具调用参数的流式分片粒度：

```python
extra_body={"tool_stream": True, "thinking": {"type": "disabled"}}
```

## 多模态调用

`glm-5v-turbo`、`glm-5.3-flash` 和 `glm-5.3-flashx` 支持 GLM 系列中的多模态输入，支持图像、视频和文件输入，输出为文本。

### 使用限制

图像、视频、文件不可在同一请求中混合传入。

文件输入仅支持 URL，不支持 Base64。

图像输入支持 URL 和 Base64 两种方式。

### 图像输入

已验证支持的格式：PNG、JPG、JPEG、WebP。其他格式如需使用，请先进行小样本测试确认。

cURL

Python

Node.js

Java

Go

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/chat/completions' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
    "model": "glm-5v-turbo",
    "messages": [{
      "role": "user",
      "content": [
        {"type": "text", "text": "请描述这张图片"},
        {"type": "image_url", "image_url": {"url": "https://example.com/photo.png"}}
      ]
    }],
    "max_tokens": 1024,
    "thinking": {"type": "disabled"}
  }'
```

```python
response = client.chat.completions.create(
    model="glm-5v-turbo",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "请描述这张图片"},
            {"type": "image_url", "image_url": {"url": "https://example.com/photo.png"}},
        ],
    }],
    max_tokens=1024,
    extra_body={"thinking": {"type": "disabled"}},
)
print(response.choices[0].message.content)
```

```javascript
const response = await client.chat.completions.create({
  model: 'glm-5v-turbo',
  messages: [{
    role: 'user',
    content: [
      { type: 'text', text: '请描述这张图片' },
      { type: 'image_url', image_url: { url: 'https://example.com/photo.png' } },
    ],
  }],
  max_tokens: 1024,
  // @ts-ignore - thinking 为 GLM 扩展字段
  thinking: { type: 'disabled' },
});
console.log(response.choices[0].message.content);
```

```java
import okhttp3.*;
import com.google.gson.Gson;
import java.util.*;

public class GlmImageInput {
    public static void main(String[] args) throws Exception {
        List<Map<String, Object>> content = List.of(
            Map.of("type", "text", "text", "请描述这张图片"),
            Map.of("type", "image_url", "image_url",
                Map.of("url", "https://example.com/photo.png"))
        );

        Map<String, Object> body = new HashMap<>();
        body.put("model", "glm-5v-turbo");
        body.put("messages", List.of(Map.of("role", "user", "content", content)));
        body.put("max_tokens", 1024);
        body.put("thinking", Map.of("type", "disabled"));

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
        "model": "glm-5v-turbo",
        "messages": []map[string]interface{}{
            {
                "role": "user",
                "content": []map[string]interface{}{
                    {"type": "text", "text": "请描述这张图片"},
                    {"type": "image_url", "image_url": map[string]string{
                        "url": "https://example.com/photo.png",
                    }},
                },
            },
        },
        "max_tokens": 1024,
        "thinking":   map[string]string{"type": "disabled"},
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

**Base64 方式（Python 示例）：**

将本地图片读取为 Base64 后，通过 Data URI 形式传入 `image_url.url`：

```python
import base64

with open("local.jpg", "rb") as f:
    b64 = base64.b64encode(f.read()).decode()

response = client.chat.completions.create(
    model="glm-5v-turbo",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "图中有什么？"},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64}"}},
        ],
    }],
    max_tokens=1024,
    extra_body={"thinking": {"type": "disabled"}},
)
```

### 视频输入

已验证支持的格式：MP4、MPEG、MOV、AVI、WebM、WMV、3GPP。其他格式如需使用，请先进行小样本测试确认。

将上文图像示例中的 `image_url` 字段替换为 `video_url`，即可传入视频文件 URL：

cURL

Python

Node.js

Java

Go

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/chat/completions' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
    "model": "glm-5v-turbo",
    "messages": [{
      "role": "user",
      "content": [
        {"type": "text", "text": "请总结这段视频的内容"},
        {"type": "video_url", "video_url": {"url": "https://example.com/demo.mp4"}}
      ]
    }],
    "max_tokens": 2048,
    "thinking": {"type": "disabled"}
  }'
```

```python
response = client.chat.completions.create(
    model="glm-5v-turbo",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "请总结这段视频的内容"},
            {"type": "video_url", "video_url": {"url": "https://example.com/demo.mp4"}},
        ],
    }],
    max_tokens=2048,
    extra_body={"thinking": {"type": "disabled"}},
)
print(response.choices[0].message.content)
```

```javascript
const response = await client.chat.completions.create({
  model: 'glm-5v-turbo',
  messages: [{
    role: 'user',
    content: [
      { type: 'text', text: '请总结这段视频的内容' },
      { type: 'video_url', video_url: { url: 'https://example.com/demo.mp4' } },
    ],
  }],
  max_tokens: 2048,
  // @ts-ignore - thinking 为 GLM 扩展字段
  thinking: { type: 'disabled' },
});
console.log(response.choices[0].message.content);
```

```java
List<Map<String, Object>> content = List.of(
    Map.of("type", "text", "text", "请总结这段视频的内容"),
    Map.of("type", "video_url", "video_url",
        Map.of("url", "https://example.com/demo.mp4"))
);

Map<String, Object> body = new HashMap<>();
body.put("model", "glm-5v-turbo");
body.put("messages", List.of(Map.of("role", "user", "content", content)));
body.put("max_tokens", 2048);
body.put("thinking", Map.of("type", "disabled"));
// 其余 HTTP 请求逻辑同图像示例
```

```go
body, _ := json.Marshal(map[string]interface{}{
    "model": "glm-5v-turbo",
    "messages": []map[string]interface{}{
        {
            "role": "user",
            "content": []map[string]interface{}{
                {"type": "text", "text": "请总结这段视频的内容"},
                {"type": "video_url", "video_url": map[string]string{
                    "url": "https://example.com/demo.mp4",
                }},
            },
        },
    },
    "max_tokens": 2048,
    "thinking":   map[string]string{"type": "disabled"},
})
// 其余 HTTP 请求逻辑同图像示例
```

### 文件输入

已验证支持的格式：PDF、TXT、DOC。其他格式如需使用，请先进行小样本测试确认。

文件输入仅支持通过 URL 传入，不支持 Base64 编码。如本地有文件需要解析，请先上传至对象存储服务（如腾讯云 COS），再使用生成的 URL。

cURL

Python

Node.js

Java

Go

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/chat/completions' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
    "model": "glm-5v-turbo",
    "messages": [{
      "role": "user",
      "content": [
        {"type": "text", "text": "请提取这份文档的核心要点"},
        {"type": "file_url", "file_url": {"url": "https://example.com/report.pdf"}}
      ]
    }],
    "max_tokens": 4096,
    "thinking": {"type": "disabled"}
  }'
```

```python
response = client.chat.completions.create(
    model="glm-5v-turbo",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "请提取这份文档的核心要点"},
            {"type": "file_url", "file_url": {"url": "https://example.com/report.pdf"}},
        ],
    }],
    max_tokens=4096,
    extra_body={"thinking": {"type": "disabled"}},
)
print(response.choices[0].message.content)
```

```javascript
const response = await client.chat.completions.create({
  model: 'glm-5v-turbo',
  messages: [{
    role: 'user',
    content: [
      { type: 'text', text: '请提取这份文档的核心要点' },
      { type: 'file_url', file_url: { url: 'https://example.com/report.pdf' } },
    ],
  }],
  max_tokens: 4096,
  // @ts-ignore - thinking 为 GLM 扩展字段
  thinking: { type: 'disabled' },
});
console.log(response.choices[0].message.content);
```

```java
List<Map<String, Object>> content = List.of(
    Map.of("type", "text", "text", "请提取这份文档的核心要点"),
    Map.of("type", "file_url", "file_url",
        Map.of("url", "https://example.com/report.pdf"))
);

Map<String, Object> body = new HashMap<>();
body.put("model", "glm-5v-turbo");
body.put("messages", List.of(Map.of("role", "user", "content", content)));
body.put("max_tokens", 4096);
body.put("thinking", Map.of("type", "disabled"));
// 其余 HTTP 请求逻辑同图像示例
```

```go
body, _ := json.Marshal(map[string]interface{}{
    "model": "glm-5v-turbo",
    "messages": []map[string]interface{}{
        {
            "role": "user",
            "content": []map[string]interface{}{
                {"type": "text", "text": "请提取这份文档的核心要点"},
                {"type": "file_url", "file_url": map[string]string{
                    "url": "https://example.com/report.pdf",
                }},
            },
        },
    },
    "max_tokens": 4096,
    "thinking":   map[string]string{"type": "disabled"},
})
// 其余 HTTP 请求逻辑同图像示例
```

## 使用限制

| 限制项 | 说明 |
| --- | --- |
| 思考模式默认开启 | 不传 `thinking` 参数时默认启用，响应中会包含 `reasoning_content` 字段。不需要时请显式关闭。 |
| 非流式调用超时风险 | 思考模式下输出较长，建议使用 `stream=True`。 |
| 多模态仅限 glm-5v-turbo、glm-5.3-flash 和 glm-5.3-flashx | 其余模型不支持图像、视频、文件输入。 |
| 多模态输入不可混合 | 图像、视频、文件在同一请求中只能传入一类。 |
| 文件输入仅支持 URL | `file_url` 不支持 Base64 或 Data URI。 |
| 工具参数增量返回 | 流式调用时 `tool_call.arguments` 分多个 chunk 返回，需客户端拼接。 |
| 请求体积上限 | 单次请求 body 不超过 100 MB。 |

## 相关文档

[语言模型调用概览](https://cloud.tencent.com/document/product/1823/130079)：TokenHub 语言模型通用调用文档，包含 BaseURL、API Key、多轮对话、Function Calling、Anthropic 协议等通用说明。

[TokenHub 控制台](https://console.cloud.tencent.com/tokenhub/apikey)：API Key 创建与管理入口。
