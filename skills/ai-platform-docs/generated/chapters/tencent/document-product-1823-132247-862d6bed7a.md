<!-- Official source: https://cloud.tencent.com/document/product/1823/132247 -->
<!-- Source SHA-256: 467afb08fec032d5187b12c791c1c3d904d122f21d9ee16241c4289442e6de0b -->

# Qwen 调用指南

官方来源：https://cloud.tencent.com/document/product/1823/132247
最近更新时间：2026-08-19 15:15:12

通义千问 Qwen 系列模型兼容 OpenAI / Anthropic 协议，可直接通过 OpenAI SDK 或标准 HTTP 接口调用。本文给出常用场景的 5 语言调用示例（cURL / Python / Node.js / Java / Go），并说明 Qwen 在思考模式相关参数上的特殊用法。

**注意：**

本文以 TokenHub 网关为例，所有调用均通过 `https://tokenhub.tencentmaas.com/v1` 接入，使用 TokenHub 自有 [API Key](https://console.cloud.tencent.com/tokenhub/apikey) 完成鉴权。

## 支持的模型

TokenHub 当前支持以下 Qwen 模型（具体以 [模型列表](https://cloud.tencent.com/document/product/1823/130051) 为准）：

| 模型 ID | 类型 | 思考能力 | 默认是否开启思考 |
| --- | --- | --- | --- |
| `qwen3.5-plus` | 通用对话模型 | 可开关 | ✅ 默认开启 |
| `qwen3.5-flash` | 轻量对话模型 | 可开关 | ✅ 默认开启 |

**说明：**

Qwen3.5 系列同时是**对话模型和思考模型**，无需在普通模型与思考模型之间切换 model ID，通过 `enable_thinking` 参数即可控制是否启用思考能力。下文示例以 `qwen3.5-plus` 为例，将 `model` 参数替换为 `qwen3.5-flash` 即可切换为轻量版本。

## 与其他模型的关键差异（速查）

| 维度 | Qwen3.5 Plus | OpenAI / Claude 等 |
| --- | --- | --- |
| 思考能力开关 | `enable_thinking`（顶层布尔字段） | 通常切换 model 或单独 reasoning 参数 |
| 默认是否思考 | ✅ 默认开启 | ❌ 默认关闭 |
| 推理过程字段 | `reasoning_content` | 多数模型不暴露 |
| Prompt 级开关 | 消息中加 `/no_think`、`/think` | 不支持 |
| 多轮对话保留思考 | `preserve_thinking: true` | 不支持 |
| OpenAI Python SDK 传参 | 通过 `extra_body` 传 `enable_thinking` 等 | 无需特殊处理 |
| OpenAI Node.js SDK 传参 | 顶层直接传入即可（TypeScript 用户需追加 `as any` 绕过类型检查） | 无需特殊处理 |
| 多模态 | `qwen3.5-plus` 支持图片、视频输入（OpenAI 兼容 `image_url`、`video_url`） | 多数为纯文本，需切换专用多模态模型 |

下面分别说明每一项的具体用法。

## 通用调用示例

以下是 Qwen3.5-Plus 的常用调用场景，均使用 OpenAI 兼容协议。所有示例与 [语言模型调用概览](https://cloud.tencent.com/document/product/1823/130079) 中的示例代码保持一致写法，调用方式直接复用。Qwen 特有能力（思考模式开关、Prompt 级开关、`preserve_thinking` 等）见下文 [Qwen 思考模式](https://cloud.tencent.com/document/product/1823/132247#ec3cd544-19a8-44db-9cb8-58a374717320) 章节。

### 基础对话

请将 `YOUR_API_KEY` 替换为您创建的 API Key。

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
    "model": "qwen3.5-plus",
    "messages": [
      {"role": "user", "content": "你好，请介绍一下你自己"}
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
    model="qwen3.5-plus",
    messages=[
        {"role": "user", "content": "你好，请介绍一下你自己"},
    ],
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
  model: 'qwen3.5-plus',
  messages: [
    { role: 'user', content: '你好，请介绍一下你自己' },
  ],
});
console.log(response.choices[0].message.content);
```

```java
// 基于 OpenAI 兼容协议，使用 OkHttp 直接调用 HTTP 接口
import okhttp3.*;
import com.google.gson.Gson;
import java.io.IOException;
import java.util.*;
import java.util.concurrent.TimeUnit;

public class BasicChat {
    public static void main(String[] args) {
        OkHttpClient client = new OkHttpClient.Builder()
                .connectTimeout(15, TimeUnit.SECONDS)
                .readTimeout(120, TimeUnit.SECONDS)
                .writeTimeout(60, TimeUnit.SECONDS)
                .callTimeout(180, TimeUnit.SECONDS)
                .build();

        Map<String, Object> body = new HashMap<>();
        body.put("model", "qwen3.5-plus");
        body.put("messages", List.of(
            Map.of("role", "user", "content", "你好，请介绍一下你自己")
        ));

        Request request = new Request.Builder()
            .url("https://tokenhub.tencentmaas.com/v1/chat/completions")
            .header("Authorization", "Bearer YOUR_API_KEY")
            .header("Content-Type", "application/json")
            .post(RequestBody.create(new Gson().toJson(body), MediaType.parse("application/json")))
            .build();

        try (Response response = client.newCall(request).execute()) {
            if (!response.isSuccessful()) {
                System.err.println("请求失败, HTTP " + response.code()
                    + " : " + (response.body() != null ? response.body().string() : ""));
                return;
            }
            System.out.println(response.body() != null ? response.body().string() : "");
        } catch (IOException e) {
            System.err.println("请求异常: " + e.getMessage());
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
        "model":           "qwen3.5-plus",
        "messages": []map[string]string{
            {"role": "user", "content": "你好，请介绍一下你自己"},
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

### 流式输出

启用 `stream: true` 即可流式获取响应，便于打字机效果展示，并能避免长响应触发网关超时。

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
    "model": "qwen3.5-plus",
    "stream": true,
    "messages": [
      {"role": "user", "content": "请用一句话介绍一下你自己"}
    ]
  }'
```

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

stream = client.chat.completions.create(
    model="qwen3.5-plus",
    messages=[{"role": "user", "content": "请用一句话介绍一下你自己"}],
    stream=True,
)
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

```javascript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: 'YOUR_API_KEY',
  baseURL: 'https://tokenhub.tencentmaas.com/v1',
});

const stream = await client.chat.completions.create({
  model: 'qwen3.5-plus',
  messages: [{ role: 'user', content: '请用一句话介绍一下你自己' }],
  stream: true,
});

for await (const chunk of stream) {
  const content = chunk.choices?.[0]?.delta?.content;
  if (content) process.stdout.write(content);
}
```

```java
import okhttp3.*;
import okhttp3.sse.*;
import com.google.gson.Gson;
import java.util.*;
import java.util.concurrent.TimeUnit;

public class StreamChat {
    public static void main(String[] args) {
        OkHttpClient client = new OkHttpClient.Builder()
                .connectTimeout(15, TimeUnit.SECONDS)
                .readTimeout(120, TimeUnit.SECONDS)
                .writeTimeout(60, TimeUnit.SECONDS)
                .build();

        Map<String, Object> body = new HashMap<>();
        body.put("model", "qwen3.5-plus");
        body.put("stream", true);
        body.put("messages", List.of(
            Map.of("role", "user", "content", "请用一句话介绍一下你自己")
        ));

        Request request = new Request.Builder()
            .url("https://tokenhub.tencentmaas.com/v1/chat/completions")
            .header("Authorization", "Bearer YOUR_API_KEY")
            .header("Content-Type", "application/json")
            .post(RequestBody.create(new Gson().toJson(body), MediaType.parse("application/json")))
            .build();

        EventSources.createFactory(client).newEventSource(request,
            new EventSourceListener() {
                @Override public void onEvent(EventSource es, String id, String type, String data) {
                    System.out.println(data);
                }
                @Override public void onFailure(EventSource es, Throwable t, Response response) {
                    System.err.println("流式请求失败: " + (t != null ? t.getMessage() : "")
                            + (response != null ? " HTTP " + response.code() : ""));
                }
            });
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

func main() {
    body, _ := json.Marshal(map[string]interface{}{
        "model":           "qwen3.5-plus",
        "stream":          true,
        "messages": []map[string]string{
            {"role": "user", "content": "请用一句话介绍一下你自己"},
        },
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
        if strings.HasPrefix(line, "data: ") {
            fmt.Println(strings.TrimPrefix(line, "data: "))
        }
    }
}
```

### System Prompt

通过 `system` 角色的消息可以为模型设定全局指令、人设、回复风格等。

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
    "model": "qwen3.5-plus",
    "messages": [
      {"role": "system", "content": "你是通义千问，一名严谨的物理学助教，回答需配合简单类比。"},
      {"role": "user", "content": "请解释什么是量子纠缠"}
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
    model="qwen3.5-plus",
    messages=[
        {"role": "system", "content": "你是通义千问，一名严谨的物理学助教，回答需配合简单类比。"},
        {"role": "user", "content": "请解释什么是量子纠缠"},
    ],
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
  model: 'qwen3.5-plus',
  messages: [
    { role: 'system', content: '你是通义千问，一名严谨的物理学助教，回答需配合简单类比。' },
    { role: 'user', content: '请解释什么是量子纠缠' },
  ],
});
console.log(response.choices[0].message.content);
```

```java
import okhttp3.*;
import com.google.gson.Gson;
import java.io.IOException;
import java.util.*;
import java.util.concurrent.TimeUnit;

public class SystemPromptChat {
    public static void main(String[] args) {
        OkHttpClient client = new OkHttpClient.Builder()
                .connectTimeout(15, TimeUnit.SECONDS)
                .readTimeout(120, TimeUnit.SECONDS)
                .writeTimeout(60, TimeUnit.SECONDS)
                .callTimeout(180, TimeUnit.SECONDS)
                .build();

        Map<String, Object> body = new HashMap<>();
        body.put("model", "qwen3.5-plus");
        body.put("messages", List.of(
            Map.of("role", "system", "content", "你是通义千问，一名严谨的物理学助教，回答需配合简单类比。"),
            Map.of("role", "user", "content", "请解释什么是量子纠缠")
        ));

        Request request = new Request.Builder()
            .url("https://tokenhub.tencentmaas.com/v1/chat/completions")
            .header("Authorization", "Bearer YOUR_API_KEY")
            .header("Content-Type", "application/json")
            .post(RequestBody.create(new Gson().toJson(body), MediaType.parse("application/json")))
            .build();

        try (Response response = client.newCall(request).execute()) {
            if (!response.isSuccessful()) {
                System.err.println("请求失败, HTTP " + response.code()
                    + " : " + (response.body() != null ? response.body().string() : ""));
                return;
            }
            System.out.println(response.body() != null ? response.body().string() : "");
        } catch (IOException e) {
            System.err.println("请求异常: " + e.getMessage());
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
        "model":           "qwen3.5-plus",
        "messages": []map[string]string{
            {"role": "system", "content": "你是通义千问，一名严谨的物理学助教，回答需配合简单类比。"},
            {"role": "user", "content": "请解释什么是量子纠缠"},
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

### 多轮对话（基础版）

Qwen API 与其他主流模型一样是**无状态**的，需要在每次请求中传入完整的 `messages` 历史。下例不开启思考，所以只回写 `content` 即可；如果启用了思考，建议同时回写 `reasoning_content` 并开启 `preserve_thinking`，详见下文 [Qwen 思考模式](https://cloud.tencent.com/document/product/1823/132247#ec3cd544-19a8-44db-9cb8-58a374717320) → 多轮对话保留思考小节。

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
    "model": "qwen3.5-plus",
    "messages": [
      {"role": "system", "content": "你是通义千问。"},
      {"role": "user", "content": "推荐一本科普读物"},
      {"role": "assistant", "content": "推荐《时间简史》。"},
      {"role": "user", "content": "再说一本进阶的"}
    ]
  }'
```

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

messages = [
    {"role": "system", "content": "你是通义千问。"},
    {"role": "user", "content": "推荐一本科普读物"},
    {"role": "assistant", "content": "推荐《时间简史》。"},
    {"role": "user", "content": "再说一本进阶的"},
]
response = client.chat.completions.create(
    model="qwen3.5-plus",
    messages=messages,
)
print(response.choices[0].message.content)
```

```javascript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: 'YOUR_API_KEY',
  baseURL: 'https://tokenhub.tencentmaas.com/v1',
});

const messages = [
  { role: 'system', content: '你是通义千问。' },
  { role: 'user', content: '推荐一本科普读物' },
  { role: 'assistant', content: '推荐《时间简史》。' },
  { role: 'user', content: '再说一本进阶的' },
];
const response = await client.chat.completions.create({
  model: 'qwen3.5-plus',
  messages,
});
console.log(response.choices[0].message.content);
```

```java
import okhttp3.*;
import com.google.gson.Gson;
import java.io.IOException;
import java.util.*;
import java.util.concurrent.TimeUnit;

public class MultiTurnChat {
    public static void main(String[] args) {
        OkHttpClient client = new OkHttpClient.Builder()
                .connectTimeout(15, TimeUnit.SECONDS)
                .readTimeout(120, TimeUnit.SECONDS)
                .writeTimeout(60, TimeUnit.SECONDS)
                .callTimeout(180, TimeUnit.SECONDS)
                .build();

        Map<String, Object> body = new HashMap<>();
        body.put("model", "qwen3.5-plus");
        body.put("messages", List.of(
            Map.of("role", "system",    "content", "你是通义千问。"),
            Map.of("role", "user",      "content", "推荐一本科普读物"),
            Map.of("role", "assistant", "content", "推荐《时间简史》。"),
            Map.of("role", "user",      "content", "再说一本进阶的")
        ));

        Request request = new Request.Builder()
            .url("https://tokenhub.tencentmaas.com/v1/chat/completions")
            .header("Authorization", "Bearer YOUR_API_KEY")
            .header("Content-Type", "application/json")
            .post(RequestBody.create(new Gson().toJson(body), MediaType.parse("application/json")))
            .build();

        try (Response response = client.newCall(request).execute()) {
            if (!response.isSuccessful()) {
                System.err.println("请求失败, HTTP " + response.code()
                    + " : " + (response.body() != null ? response.body().string() : ""));
                return;
            }
            System.out.println(response.body() != null ? response.body().string() : "");
        } catch (IOException e) {
            System.err.println("请求异常: " + e.getMessage());
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
        "model":           "qwen3.5-plus",
        "messages": []map[string]string{
            {"role": "system", "content": "你是通义千问。"},
            {"role": "user", "content": "推荐一本科普读物"},
            {"role": "assistant", "content": "推荐《时间简史》。"},
            {"role": "user", "content": "再说一本进阶的"},
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

### Function Calling（工具调用）

Qwen 支持标准的 OpenAI Function Calling 协议。下例演示如何注册一个查天气的工具，并在模型决定调用工具后把工具结果回填给模型。

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
    "model": "qwen3.5-plus",
    "messages": [
      {"role": "user", "content": "今天北京天气怎么样？"}
    ],
    "tools": [{
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
    }],
    "tool_choice": "auto"
  }'
```

```python
import json
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "查询指定城市的天气",
        "parameters": {
        "type": "object",
        "properties": {"city": {"type": "string", "description": "城市名称"}},
        "required": ["city"],
        },
    },
}]

messages = [{"role": "user", "content": "今天北京天气怎么样？"}]

# 第 1 轮：模型决定是否调用工具
resp = client.chat.completions.create(
    model="qwen3.5-plus",
    messages=messages,
    tools=tools,
    tool_choice="auto",
)
msg = resp.choices[0].message
messages.append(msg.model_dump(exclude_none=True))

if msg.tool_calls:
    for call in msg.tool_calls:
        args = json.loads(call.function.arguments)
        # 这里替换为真实业务逻辑
        result = {"city": args["city"], "temperature": "22°C", "weather": "晴"}
        messages.append({
            "role": "tool",
            "tool_call_id": call.id,
            "content": json.dumps(result, ensure_ascii=False),
        })

    # 第 2 轮：把工具结果送回模型，得到最终回复
    final = client.chat.completions.create(
        model="qwen3.5-plus",
        messages=messages,
        tools=tools,
        )
    print(final.choices[0].message.content)
else:
    print(msg.content)
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
    description: '查询指定城市的天气',
    parameters: {
      type: 'object',
      properties: { city: { type: 'string', description: '城市名称' } },
      required: ['city'],
    },
  },
}];

const messages = [{ role: 'user', content: '今天北京天气怎么样？' }];

const resp = await client.chat.completions.create({
  model: 'qwen3.5-plus',
  messages,
  tools,
  tool_choice: 'auto',
});
const msg = resp.choices[0].message;
messages.push(msg);

if (msg.tool_calls) {
  for (const call of msg.tool_calls) {
    const args = JSON.parse(call.function.arguments);
    const result = { city: args.city, temperature: '22°C', weather: '晴' };
    messages.push({
      role: 'tool',
      tool_call_id: call.id,
      content: JSON.stringify(result),
    });
  }
  const final = await client.chat.completions.create({
    model: 'qwen3.5-plus',
    messages,
    tools,
    });
  console.log(final.choices[0].message.content);
} else {
  console.log(msg.content);
}
```

```java
import okhttp3.*;
import com.google.gson.*;
import java.io.IOException;
import java.util.*;
import java.util.concurrent.TimeUnit;

public class FunctionCallingDemo {
    static final String URL = "https://tokenhub.tencentmaas.com/v1/chat/completions";
    static final String API_KEY = "YOUR_API_KEY";
    static final OkHttpClient HTTP = new OkHttpClient.Builder()
            .connectTimeout(15, TimeUnit.SECONDS)
            .readTimeout(120, TimeUnit.SECONDS)
            .writeTimeout(60, TimeUnit.SECONDS)
            .callTimeout(180, TimeUnit.SECONDS)
            .build();
    static final Gson GSON = new Gson();

    static String chat(List<Map<String, Object>> messages, List<Map<String, Object>> tools) throws IOException {
        Map<String, Object> body = new HashMap<>();
        body.put("model", "qwen3.5-plus");
        body.put("messages", messages);
        body.put("tools", tools);
        body.put("tool_choice", "auto");

        Request req = new Request.Builder()
            .url(URL)
            .header("Authorization", "Bearer " + API_KEY)
            .header("Content-Type", "application/json")
            .post(RequestBody.create(GSON.toJson(body), MediaType.parse("application/json")))
            .build();

        try (Response resp = HTTP.newCall(req).execute()) {
            if (!resp.isSuccessful()) {
                throw new IOException("请求失败, HTTP " + resp.code()
                        + " : " + (resp.body() != null ? resp.body().string() : ""));
            }
            return resp.body() != null ? resp.body().string() : "";
        }
    }

    public static void main(String[] args) throws Exception {
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

        List<Map<String, Object>> messages = new ArrayList<>();
        messages.add(Map.of("role", "user", "content", "今天北京天气怎么样？"));

        String r1 = chat(messages, tools);
        JsonObject msg = JsonParser.parseString(r1).getAsJsonObject()
            .getAsJsonArray("choices").get(0).getAsJsonObject()
            .getAsJsonObject("message");
        messages.add(GSON.fromJson(msg, Map.class));

        if (msg.has("tool_calls")) {
            for (JsonElement el : msg.getAsJsonArray("tool_calls")) {
                JsonObject call = el.getAsJsonObject();
                JsonObject argsObj = JsonParser.parseString(
                    call.getAsJsonObject("function").get("arguments").getAsString()
                ).getAsJsonObject();
                Map<String, String> result = Map.of(
                    "city", argsObj.get("city").getAsString(),
                    "temperature", "22°C",
                    "weather", "晴"
                );
                messages.add(Map.of(
                    "role", "tool",
                    "tool_call_id", call.get("id").getAsString(),
                    "content", GSON.toJson(result)
                ));
            }
            System.out.println(chat(messages, tools));
        } else {
            System.out.println(msg.get("content").getAsString());
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

const (
    URL    = "https://tokenhub.tencentmaas.com/v1/chat/completions"
    APIKEY = "YOUR_API_KEY"
)

func chat(messages []map[string]interface{}, tools []map[string]interface{}) (map[string]interface{}, error) {
    body, _ := json.Marshal(map[string]interface{}{
        "model":           "qwen3.5-plus",
        "messages":        messages,
        "tools":           tools,
        "tool_choice":     "auto",
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
        "description": "查询指定城市的天气",
        "parameters": map[string]interface{}{
                "type": "object",
                "properties": map[string]interface{}{
                    "city": map[string]string{"type": "string", "description": "城市名称"},
                },
                "required": []string{"city"},
            },
        },
    }}

    messages := []map[string]interface{}{
        {"role": "user", "content": "今天北京天气怎么样？"},
    }

    // 第 1 轮：模型决定是否调用工具
    r1, _ := chat(messages, tools)
    msg := r1["choices"].([]interface{})[0].(map[string]interface{})["message"].(map[string]interface{})
    messages = append(messages, msg)

    if calls, ok := msg["tool_calls"].([]interface{}); ok {
        for _, c := range calls {
            call := c.(map[string]interface{})
            argsStr := call["function"].(map[string]interface{})["arguments"].(string)
            var args map[string]string
            json.Unmarshal([]byte(argsStr), &args)
            result, _ := json.Marshal(map[string]string{
                "city":        args["city"],
                "temperature": "22°C",
                "weather":     "晴",
            })
            messages = append(messages, map[string]interface{}{
                "role":         "tool",
                "tool_call_id": call["id"],
                "content":      string(result),
            })
        }
        r2, _ := chat(messages, tools)
        fmt.Printf("%+v\\n", r2)
    } else {
        fmt.Println(msg["content"])
    }
}
```

## 多模态调用

Qwen3.5-Plus 是**多模态模型**，除文本外还支持**图片**与**视频**输入，复用 OpenAI 兼容的 `image_url` / `video_url` 结构即可。

### 1. 图片输入：URL 形式

适合公网可直接访问的图片：

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
    "model": "qwen3.5-plus",
    "messages": [{
      "role": "user",
      "content": [
        {"type": "text", "text": "这张图里是什么？请用一句话描述。"},
        {"type": "image_url", "image_url": {"url": "https://www.gstatic.com/webp/gallery/1.jpg"}}
      ]
    }]
  }'
```

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

response = client.chat.completions.create(
    model="qwen3.5-plus",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "这张图里是什么？请用一句话描述。"},
            {"type": "image_url", "image_url": {"url": "https://www.gstatic.com/webp/gallery/1.jpg"}},
        ],
    }],
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
  model: 'qwen3.5-plus',
  messages: [{
    role: 'user',
    content: [
      { type: 'text', text: '这张图里是什么？请用一句话描述。' },
      { type: 'image_url', image_url: { url: 'https://www.gstatic.com/webp/gallery/1.jpg' } },
    ],
  }],
});
console.log(response.choices[0].message.content);
```

```java
import okhttp3.*;
import com.google.gson.Gson;
import java.io.IOException;
import java.util.*;
import java.util.concurrent.TimeUnit;

public class ImageUrlChat {
    public static void main(String[] args) {
        OkHttpClient client = new OkHttpClient.Builder()
                .connectTimeout(15, TimeUnit.SECONDS)
                .readTimeout(120, TimeUnit.SECONDS)
                .writeTimeout(60, TimeUnit.SECONDS)
                .callTimeout(180, TimeUnit.SECONDS)
                .build();

        Map<String, Object> body = new HashMap<>();
        body.put("model", "qwen3.5-plus");
        body.put("messages", List.of(Map.of(
            "role", "user",
            "content", List.of(
                Map.of("type", "text", "text", "这张图里是什么？请用一句话描述。"),
                // 请替换为您自己的可公网访问图片 URL
                Map.of("type", "image_url",
                       "image_url", Map.of("url", "https://example.com/path/to/your/image.jpg"))
            )
        )));

        Request request = new Request.Builder()
            .url("https://tokenhub.tencentmaas.com/v1/chat/completions")
            .header("Authorization", "Bearer YOUR_API_KEY")
            .header("Content-Type", "application/json")
            .post(RequestBody.create(new Gson().toJson(body), MediaType.parse("application/json")))
            .build();

        try (Response response = client.newCall(request).execute()) {
            if (!response.isSuccessful()) {
                System.err.println("请求失败, HTTP " + response.code()
                    + " : " + (response.body() != null ? response.body().string() : ""));
                return;
            }
            System.out.println(response.body() != null ? response.body().string() : "");
        } catch (IOException e) {
            System.err.println("请求异常: " + e.getMessage());
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
        "model": "qwen3.5-plus",
        "messages": []map[string]interface{}{{
            "role": "user",
            "content": []map[string]interface{}{
                {"type": "text", "text": "这张图里是什么？请用一句话描述。"},
                {"type": "image_url",
                 "image_url": map[string]string{"url": "https://www.gstatic.com/webp/gallery/1.jpg"}},
            },
        }},
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

### 2. 图片输入：Base64 编码

适合本地文件 / 内网图片场景：

**说明：**

以下示例从当前目录读取 `image.jpg`，运行前请准备一张测试图片并命名为 `image.jpg` 放到当前目录。

cURL

Python

Node.js

Java

Go

```bash
# 先把图片读为 base64
IMAGE_B64=$(base64 -i image.jpg | tr -d '\\n')

# 用临时文件传 body，避免 base64 字符串过大触发 "Argument list too long"
cat > /tmp/req.json <<EOF
{
  "model": "qwen3.5-plus",
  "messages": [{
    "role": "user",
    "content": [
      {"type": "text", "text": "请描述这张图片"},
      {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,${IMAGE_B64}"}}
    ]
  }]
}
EOF

curl -X POST 'https://tokenhub.tencentmaas.com/v1/chat/completions' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d @/tmp/req.json
```

```python
import base64
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

with open("image.jpg", "rb") as f:
    image_b64 = base64.b64encode(f.read()).decode()

response = client.chat.completions.create(
    model="qwen3.5-plus",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "请描述这张图片"},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_b64}"}},
        ],
    }],
)
print(response.choices[0].message.content)
```

```javascript
import fs from 'fs';
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: 'YOUR_API_KEY',
  baseURL: 'https://tokenhub.tencentmaas.com/v1',
});

const imageB64 = fs.readFileSync('image.jpg').toString('base64');

const response = await client.chat.completions.create({
  model: 'qwen3.5-plus',
  messages: [{
    role: 'user',
    content: [
      { type: 'text', text: '请描述这张图片' },
      { type: 'image_url', image_url: { url: `data:image/jpeg;base64,${imageB64}` } },
    ],
  }],
});
console.log(response.choices[0].message.content);
```

```java
import okhttp3.*;
import com.google.gson.Gson;
import java.nio.file.*;
import java.util.*;

public class ImageBase64Chat {
    public static void main(String[] args) throws Exception {
        byte[] bytes = Files.readAllBytes(Path.of("image.jpg"));
        String b64 = Base64.getEncoder().encodeToString(bytes);

        Map<String, Object> body = new HashMap<>();
        body.put("model", "qwen3.5-plus");
        body.put("messages", List.of(Map.of(
            "role", "user",
            "content", List.of(
                Map.of("type", "text", "text", "请描述这张图片"),
                Map.of("type", "image_url",
                       "image_url", Map.of("url", "data:image/jpeg;base64," + b64))
            )
        )));

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
    "encoding/base64"
    "encoding/json"
    "fmt"
    "io"
    "net/http"
    "os"
)

func main() {
    raw, _ := os.ReadFile("image.jpg")
    b64 := base64.StdEncoding.EncodeToString(raw)

    body, _ := json.Marshal(map[string]interface{}{
        "model": "qwen3.5-plus",
        "messages": []map[string]interface{}{{
            "role": "user",
            "content": []map[string]interface{}{
                {"type": "text", "text": "请描述这张图片"},
                {"type": "image_url",
                 "image_url": map[string]string{"url": "data:image/jpeg;base64," + b64}},
            },
        }},
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

### 3. 视频输入：URL 形式

视频输入与图片类似，将 `image_url` 替换为 `video_url` 即可：

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
    "model": "qwen3.5-plus",
    "messages": [{
      "role": "user",
      "content": [
        {"type": "text", "text": "请简述这段视频的内容"},
        {"type": "video_url", "video_url": {"url": "https://www.w3schools.com/html/mov_bbb.mp4"}}
      ]
    }]
  }'
```

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

response = client.chat.completions.create(
    model="qwen3.5-plus",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "请简述这段视频的内容"},
            {"type": "video_url", "video_url": {"url": "https://www.w3schools.com/html/mov_bbb.mp4"}},
        ],
    }],
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
  model: 'qwen3.5-plus',
  messages: [{
    role: 'user',
    content: [
      { type: 'text', text: '请简述这段视频的内容' },
      { type: 'video_url', video_url: { url: 'https://www.w3schools.com/html/mov_bbb.mp4' } },
    ],
  }],
});
console.log(response.choices[0].message.content);
```

```java
import okhttp3.*;
import com.google.gson.Gson;
import java.util.*;

public class VideoUrlChat {
    public static void main(String[] args) throws Exception {
        Map<String, Object> body = new HashMap<>();
        body.put("model", "qwen3.5-plus");
        body.put("messages", List.of(Map.of(
            "role", "user",
            "content", List.of(
                Map.of("type", "text", "text", "请简述这段视频的内容"),
                Map.of("type", "video_url",
                       "video_url", Map.of("url", "https://www.w3schools.com/html/mov_bbb.mp4"))
            )
        )));

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
        "model": "qwen3.5-plus",
        "messages": []map[string]interface{}{{
            "role": "user",
            "content": []map[string]interface{}{
                {"type": "text", "text": "请简述这段视频的内容"},
                {"type": "video_url",
                 "video_url": map[string]string{"url": "https://www.w3schools.com/html/mov_bbb.mp4"}},
            },
        }},
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

## Qwen 思考模式

Qwen3.5-Plus 同时是对话模型和思考模型，**默认开启思考**，通过 `enable_thinking` 字段控制思考能力开关，并提供 Prompt 级开关、`preserve_thinking` 等独有能力。

### 1. `enable_thinking` 参数

`enable_thinking` 是请求体顶层的布尔字段：

| 取值 | 行为 |
| --- | --- |
| `true`（默认） | 模型先思考再回复，响应中会包含 `reasoning_content` 字段 |
| `false` | 模型直接回复，关闭思考 |

**注意：**

`enable_thinking` 不是 OpenAI 标准字段，使用官方 SDK 时需通过 `extra_body`（Python）或直接展开到顶层（Node.js）透传；HTTP 直接调用时放在请求体顶层即可。

### 2. `reasoning_content` 字段

启用思考后，响应消息中会新增一个**与** `content` **同级**的 `reasoning_content` 字段，承载模型的推理过程：

```json
{
  "choices": [{
    "message": {
      "role": "assistant",
      "reasoning_content": "首先我们需要分析...",
      "content": "最终答案是 ..."
    }
  }]
}
```

#### OpenAI SDK 访问限制（重要）

OpenAI 官方 SDK 的 `ChatCompletionMessage` / `ChoiceDelta` 类型**不直接声明** `reasoning_content` 属性，因此**不能用** `obj.reasoning_content` **直接访问**，必须用以下方式：

```python
# ❌ 错误
content = message.reasoning_content

# ✅ 正确
if hasattr(message, "reasoning_content"):
    content = getattr(message, "reasoning_content")
```

如果您是通过 HTTP 直接调用、或使用 requests / httpx 等通用框架解析 JSON，则无此限制，可直接读取同级字段。

### 3. 流式思考输出

启用思考时**强烈建议使用流式调用**（`stream: true`）：

**避免超时**：思考内容可能较长，整体响应时间较久，非流式容易触发网关超时。

**顺序明确**：流式模式下 `reasoning_content` 一定在 `content` 之前完整输出，便于 UI 区分思考中和正在回答两种状态。

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
    "model": "qwen3.5-plus",
    "stream": true,
    "enable_thinking": true,
    "messages": [
      {"role": "user", "content": "请用一句话解释傅里叶变换。"}
    ]
  }'
# 响应为 SSE 流：每个 data: 行包含一个 chunk，
# delta.reasoning_content 一定先于 delta.content 出现
```

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

stream = client.chat.completions.create(
    model="qwen3.5-plus",
    messages=[{"role": "user", "content": "请用一句话解释傅里叶变换。"}],
    stream=True,
    extra_body={
        "enable_thinking": True,
        },
)

thinking = False
for chunk in stream:
    if not chunk.choices:
        continue
    delta = chunk.choices[0].delta
    # 思考阶段
    if hasattr(delta, "reasoning_content") and getattr(delta, "reasoning_content"):
        if not thinking:
            print("=== 开始思考 ===")
            thinking = True
        print(getattr(delta, "reasoning_content"), end="", flush=True)
    # 回答阶段
    if delta.content:
        if thinking:
            print("\\n=== 思考结束 ===")
            thinking = False
        print(delta.content, end="", flush=True)
```

```javascript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: 'YOUR_API_KEY',
  baseURL: 'https://tokenhub.tencentmaas.com/v1',
});

const stream = await client.chat.completions.create({
  model: 'qwen3.5-plus',
  messages: [{ role: 'user', content: '请用一句话解释傅里叶变换。' }],
  stream: true,
  enable_thinking: true,
});

let thinking = false;
for await (const chunk of stream) {
  const delta = chunk.choices?.[0]?.delta;
  if (!delta) continue;
  if (delta.reasoning_content) {
    if (!thinking) { console.log('=== 开始思考 ==='); thinking = true; }
    process.stdout.write(delta.reasoning_content);
  }
  if (delta.content) {
    if (thinking) { console.log('\\n=== 思考结束 ==='); thinking = false; }
    process.stdout.write(delta.content);
  }
}
```

```java
import okhttp3.*;
import okhttp3.sse.*;
import com.google.gson.*;
import java.util.*;

public class ThinkingStream {
    public static void main(String[] args) {
        Map<String, Object> body = new HashMap<>();
        body.put("model", "qwen3.5-plus");
        body.put("stream", true);
        body.put("enable_thinking", true);
        body.put("messages", List.of(
            Map.of("role", "user", "content", "请用一句话解释傅里叶变换。")
        ));

        Request request = new Request.Builder()
            .url("https://tokenhub.tencentmaas.com/v1/chat/completions")
            .header("Authorization", "Bearer YOUR_API_KEY")
            .header("Content-Type", "application/json")
            .post(RequestBody.create(new Gson().toJson(body), MediaType.parse("application/json")))
            .build();

        EventSources.createFactory(new OkHttpClient()).newEventSource(request,
            new EventSourceListener() {
                @Override public void onEvent(EventSource es, String id, String type, String data) {
                    if ("[DONE]".equals(data)) return;
                    JsonObject delta = JsonParser.parseString(data).getAsJsonObject()
                        .getAsJsonArray("choices").get(0).getAsJsonObject()
                        .getAsJsonObject("delta");
                    if (delta.has("reasoning_content") && !delta.get("reasoning_content").isJsonNull()) {
                        System.out.print(delta.get("reasoning_content").getAsString());
                    }
                    if (delta.has("content") && !delta.get("content").isJsonNull()) {
                        System.out.print(delta.get("content").getAsString());
                    }
                }
            });
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

func main() {
    body, _ := json.Marshal(map[string]interface{}{
        "model":            "qwen3.5-plus",
        "stream":           true,
        "enable_thinking":  true,
        "messages": []map[string]string{
            {"role": "user", "content": "请用一句话解释傅里叶变换。"},
        },
    })

    req, _ := http.NewRequest("POST",
        "https://tokenhub.tencentmaas.com/v1/chat/completions",
        bytes.NewBuffer(body))
    req.Header.Set("Authorization", "Bearer YOUR_API_KEY")
    req.Header.Set("Content-Type", "application/json")

    resp, _ := http.DefaultClient.Do(req)
    defer resp.Body.Close()

    scanner := bufio.NewScanner(resp.Body)
    thinking := false
    for scanner.Scan() {
        line := scanner.Text()
        if !strings.HasPrefix(line, "data: ") {
            continue
        }
        data := strings.TrimPrefix(line, "data: ")
        if data == "[DONE]" {
            break
        }
        var chunk map[string]interface{}
        if err := json.Unmarshal([]byte(data), &chunk); err != nil {
            continue
        }
        choices, _ := chunk["choices"].([]interface{})
        if len(choices) == 0 {
            continue
        }
        delta, _ := choices[0].(map[string]interface{})["delta"].(map[string]interface{})
        if rc, ok := delta["reasoning_content"].(string); ok && rc != "" {
            if !thinking {
                fmt.Println("=== 开始思考 ===")
                thinking = true
            }
            fmt.Print(rc)
        }
        if c, ok := delta["content"].(string); ok && c != "" {
            if thinking {
                fmt.Println("\\n=== 思考结束 ===")
                thinking = false
            }
            fmt.Print(c)
        }
    }
}
```

### 4. Prompt 级思考开关（Qwen 独有）

除了 `enable_thinking` 字段，Qwen 还支持在用户消息内容中加入 **Prompt 级开关**，方便在多轮对话中**仅对单条消息**临时切换思考状态：

| 标记 | 作用 | 说明 |
| --- | --- | --- |
| `/no_think` | 本条消息**关闭**思考 | 常用于不需要推理的简单回复（如打招呼、确认） |
| `/think` | 本条消息**开启**思考 | 默认行为，主要用于在 `/no_think` 之后恢复 |

**说明：**

多个标记同时出现时**以最后一条为准**。该机制需要 `enable_thinking: true` 配合使用，仅作用于当前轮次，不改变全局参数。

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
    "model": "qwen3.5-plus",
    "stream": true,
    "enable_thinking": true,
    "messages": [
      {"role": "user", "content": "你好 /no_think"}
    ]
  }'
```

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

# Prompt 级开关：在 user 消息文本里直接加入 /no_think 或 /think
stream = client.chat.completions.create(
    model="qwen3.5-plus",
    messages=[{"role": "user", "content": "你好 /no_think"}],
    stream=True,
    extra_body={"enable_thinking": True},
)

for chunk in stream:
    delta = chunk.choices[0].delta
    if delta.content:
        print(delta.content, end="", flush=True)
print()
```

```javascript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: 'YOUR_API_KEY',
  baseURL: 'https://tokenhub.tencentmaas.com/v1',
});

// Prompt 级开关：在 user 消息文本里直接加入 /no_think 或 /think
const stream = await client.chat.completions.create({
  model: 'qwen3.5-plus',
  messages: [{ role: 'user', content: '你好 /no_think' }],
  stream: true,
  enable_thinking: true,
});

for await (const chunk of stream) {
  const delta = chunk.choices?.[0]?.delta;
  if (delta?.content) process.stdout.write(delta.content);
}
console.log();
```

```java
import okhttp3.*;
import com.google.gson.Gson;
import java.util.*;

public class PromptThinkSwitch {
    public static void main(String[] args) throws Exception {
        Map<String, Object> body = new HashMap<>();
        body.put("model", "qwen3.5-plus");
        body.put("stream", true);
        body.put("enable_thinking", true);
        body.put("messages", List.of(
            Map.of("role", "user", "content", "你好 /no_think")
        ));

        Request request = new Request.Builder()
            .url("https://tokenhub.tencentmaas.com/v1/chat/completions")
            .header("Authorization", "Bearer YOUR_API_KEY")
            .post(RequestBody.create(new Gson().toJson(body), MediaType.parse("application/json")))
            .build();

        try (Response response = new OkHttpClient().newCall(request).execute()) {
            // 流式 SSE：逐行读取 data: 行
            try (java.io.BufferedReader r = new java.io.BufferedReader(
                    new java.io.InputStreamReader(response.body().byteStream()))) {
                String line;
                while ((line = r.readLine()) != null) {
                    if (line.startsWith("data: ")) System.out.println(line.substring(6));
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

func main() {
    body, _ := json.Marshal(map[string]interface{}{
        "model":           "qwen3.5-plus",
        "stream":          true,
        "enable_thinking": true,
        "messages": []map[string]string{
            {"role": "user", "content": "你好 /no_think"},
        },
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
        if strings.HasPrefix(line, "data: ") {
            fmt.Println(strings.TrimPrefix(line, "data: "))
        }
    }
}
```

### 5. 多轮对话保留思考（`preserve_thinking`，Qwen 独有）

`preserve_thinking` 控制**历史轮次**的 `reasoning_content` 是否参与下一轮推理：

| 取值 | 含义 | 适用场景 |
| --- | --- | --- |
| `false` / 不传（默认） | 历史轮次的推理内容不透传，上下文更短，成本更低 | 普通多轮对话 |
| `true` | 完整保留历史轮次的推理过程，让模型延续之前的思考脉络 | 复杂多步推理、Agent 工具调用、长程代码任务 |

**注意：**

开启 `preserve_thinking: true` 后，历史 `reasoning_content` 会**计入输入 Token 数和计费**，请按需启用。多轮 Function Calling 场景下建议开启，可显著提升后续轮次的准确性。

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
    "model": "qwen3.5-plus",
    "stream": true,
    "enable_thinking": true,
    "preserve_thinking": true,
    "messages": [
      {"role": "system", "content": "你是通义千问。"},
      {"role": "user", "content": "我需要为电商系统选消息队列"},
      {
        "role": "assistant",
        "reasoning_content": "<上一轮 API 返回的 reasoning_content>",
        "content": "<上一轮 API 返回的 content>"
      },
      {"role": "user", "content": "你为何排除了 Kafka？"}
    ]
  }'
```

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

messages = [
    {"role": "system", "content": "你是通义千问。"},
    {"role": "user", "content": "我需要为电商系统选消息队列"},
    {
        "role": "assistant",
        "reasoning_content": "<上一轮 API 返回的 reasoning_content>",
        "content": "<上一轮 API 返回的 content>",
    },
    {"role": "user", "content": "你为何排除了 Kafka？"},
]

response = client.chat.completions.create(
    model="qwen3.5-plus",
    messages=messages,
    stream=True,
    extra_body={
        "enable_thinking": True,
        "preserve_thinking": True,
    },
)

for chunk in response:
    delta = chunk.choices[0].delta
    if getattr(delta, "reasoning_content", None):
        print(delta.reasoning_content, end="", flush=True)
    if delta.content:
        print(delta.content, end="", flush=True)
print()
```

```javascript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: 'YOUR_API_KEY',
  baseURL: 'https://tokenhub.tencentmaas.com/v1',
});

const messages = [
  { role: 'system', content: '你是通义千问。' },
  { role: 'user', content: '我需要为电商系统选消息队列' },
  {
    role: 'assistant',
    reasoning_content: '<上一轮 API 返回的 reasoning_content>',
    content: '<上一轮 API 返回的 content>',
  },
  { role: 'user', content: '你为何排除了 Kafka？' },
];

const stream = await client.chat.completions.create({
  model: 'qwen3.5-plus',
  messages,
  stream: true,
  enable_thinking: true,
  preserve_thinking: true,
});

for await (const chunk of stream) {
  const delta = chunk.choices?.[0]?.delta;
  if (!delta) continue;
  if (delta.reasoning_content) process.stdout.write(delta.reasoning_content);
  if (delta.content) process.stdout.write(delta.content);
}
console.log();
```

```java
import okhttp3.*;
import com.google.gson.Gson;
import java.util.*;

public class MultiTurnPreserveThinking {
    public static void main(String[] args) {
        Map<String, Object> body = new HashMap<>();
        body.put("model", "qwen3.5-plus");
        body.put("stream", true);
        body.put("enable_thinking", true);
        body.put("preserve_thinking", true);
        body.put("messages", List.of(
            Map.of("role", "system", "content", "你是通义千问。"),
            Map.of("role", "user",   "content", "我需要为电商系统选消息队列"),
            Map.of(
                "role", "assistant",
                "reasoning_content", "<上一轮 API 返回的 reasoning_content>",
                "content", "<上一轮 API 返回的 content>"
            ),
            Map.of("role", "user", "content", "你为何排除了 Kafka？")
        ));

        Request request = new Request.Builder()
            .url("https://tokenhub.tencentmaas.com/v1/chat/completions")
            .header("Authorization", "Bearer YOUR_API_KEY")
            .post(RequestBody.create(new Gson().toJson(body), MediaType.parse("application/json")))
            .build();

        try (Response response = new OkHttpClient().newCall(request).execute();
             java.io.BufferedReader r = new java.io.BufferedReader(
                 new java.io.InputStreamReader(response.body().byteStream()))) {
            String line;
            while ((line = r.readLine()) != null) {
                if (line.startsWith("data: ")) System.out.println(line.substring(6));
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

func main() {
    body, _ := json.Marshal(map[string]interface{}{
        "model":              "qwen3.5-plus",
        "stream":             true,
        "enable_thinking":    true,
        "preserve_thinking":  true,
        "messages": []map[string]interface{}{
            {"role": "system", "content": "你是通义千问。"},
            {"role": "user", "content": "我需要为电商系统选消息队列"},
            {
                "role":              "assistant",
                "reasoning_content": "<上一轮 API 返回的 reasoning_content>",
                "content":           "<上一轮 API 返回的 content>",
            },
            {"role": "user", "content": "你为何排除了 Kafka？"},
        },
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
        if strings.HasPrefix(line, "data: ") {
            fmt.Println(strings.TrimPrefix(line, "data: "))
        }
    }
}
```

## 推荐参数与最佳实践

| 参数 / 实践 | 建议 | 说明 |
| --- | --- | --- |
| `enable_thinking` | 按需显式设置 | Qwen3.5-Plus **默认开启**思考；不需要推理时务必显式设置 `false` |
| `stream` | 建议开启 | 思考模式下输出较长，流式可改善体验并避免网关超时 |
| `preserve_thinking` | 多轮 Function Calling / 复杂推理时开启 | 开启后历史 `reasoning_content` 会计入输入 Token 计费 |
| Prompt 级开关 | 对单轮临时切换 | 在 user 消息中加 `/no_think` 或 `/think`，仅作用于当前轮次 |
| OpenAI SDK 访问推理 | `hasattr` / `getattr` | 不要直接 `.reasoning_content`，否则属性访问报错 |
| Python SDK 传参 | `extra_body={"enable_thinking": ..., "preserve_thinking": ...}` | `enable_thinking`、`preserve_thinking` 都是非 OpenAI 标准字段 |
| Node.js SDK 传参 | 顶层直接传入；TypeScript 用户追加 `as any` | Node.js SDK 不支持 `extra_body`；JavaScript 直接传字段即可，TypeScript 类型签名上需配合 `as any` 透传 |
