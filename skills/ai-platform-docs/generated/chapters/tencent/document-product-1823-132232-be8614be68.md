<!-- Official source: https://cloud.tencent.com/document/product/1823/132232 -->
<!-- Source SHA-256: b4986452e4fc21b50c9ea47479a2330f6f290cf56c3488621339ea5ce407e281 -->

# Kimi 调用指南

官方来源：https://cloud.tencent.com/document/product/1823/132232
最近更新时间：2026-10-24 14:51:30

Kimi 系列模型兼容 OpenAI / Anthropic 协议，可直接通过 OpenAI SDK 或标准 HTTP 接口调用。本文给出常用场景的 5 语言调用示例（cURL / Python / Node.js / Java / Go），并说明 Kimi 在思考模式、多模态等方面的特殊用法。

**注意：**

本文以 TokenHub 平台为例，所有调用均通过 `https://tokenhub.tencentmaas.com/v1` 接入，使用 TokenHub 自有 [API Key](https://console.cloud.tencent.com/tokenhub/apikey) 完成鉴权。

## 支持的模型

TokenHub 当前支持以下 Kimi 模型（具体以 [模型列表](https://cloud.tencent.com/document/product/1823/130051) 为准）：

<table><colgroup><col/><col/><col/><col/><col/></colgroup><tbody><tr><td><div>模型 ID</div></td><td><div>类型</div></td><td><div>思考能力</div></td><td><div>视觉能力</div></td><td><div>视频能力</div></td></tr><tr><td colspan="1" rowspan="1"><div><code>kimi-k3.1-pro-highspeed</code></div></td><td colspan="1" rowspan="1"><div>通用对话模型</div></td><td colspan="1" rowspan="1"><div>仅思考（不可关闭）</div></td><td colspan="1" rowspan="1"><div>支持</div></td><td colspan="1" rowspan="1"><div>支持</div></td></tr><tr><td colspan="1" rowspan="1"><div><code>kimi-k3.1-pro</code></div></td><td colspan="1" rowspan="1"><div>通用对话模型</div></td><td colspan="1" rowspan="1"><div>仅思考（不可关闭）</div></td><td colspan="1" rowspan="1"><div>支持</div></td><td colspan="1" rowspan="1"><div>支持</div></td></tr><tr><td><div><code>kimi-k3</code></div></td><td><div>通用对话模型</div></td><td><div>仅思考（不可关闭）</div></td><td><div>支持</div></td><td><div>支持</div></td></tr><tr><td><div><code>kimi-k2.8-preview</code></div></td><td><div>通用对话模型</div></td><td><div>仅思考（不可关闭）</div></td><td><div>支持</div></td><td><div>支持</div></td></tr><tr><td><div><code>kimi-k2.7-code-highspeed</code></div></td><td colspan="1" rowspan="1"><div>Coding 模型</div></td><td colspan="1" rowspan="1"><div>仅思考（不可关闭）</div></td><td colspan="1" rowspan="1"><div>支持</div></td><td colspan="1" rowspan="1"><div>支持</div></td></tr><tr><td><div><code>kimi-k2.7-code</code></div></td><td><div>Coding 模型</div></td><td><div>仅思考（不可关闭）</div></td><td><div>支持</div></td><td><div>支持</div></td></tr><tr><td><div><code>kimi-k2.6</code></div></td><td><div>通用对话模型</div></td><td><div>可开关（默认开启）</div></td><td><div>支持</div></td><td><div>支持</div></td></tr></tbody></table>

## Kimi 各模型调用差异

Kimi 系列模型整体兼容 OpenAI Chat Completions 协议，但不同模型的参数约束不同。接入时请按具体模型 ID 维护参数模板，不要把一套请求参数复用于所有 Kimi 模型。

| 维度 | `kimi-k3 / kimi-k3.1-pro / kimi-k3.1-pro-highspeed` | `kimi-k2.8-preview` | `kimi-k2.7-code` / `kimi-k2.7-code-highspeed` | `kimi-k2.6` |
| --- | --- | --- | --- | --- |
| 模型定位 | 旗舰通用模型，适合长上下文、知识工作、综合推理和多模态理解 | 综合性能接近 K3，编码与 Agent 能力较 K2.7 Code 提升，思考效率更高，适合长上下文代码任务 | Coding 模型，适合长程代码任务和工程 Agent；HighSpeed 版本更偏低延迟交互 | 通用对话 / 思考模型，适合通用推理、对话和多模态任务 |
| 思考参数 | 使用顶层 `reasoning_effort`，支持 `"low"` / `"high"` / `"max"` 三档，默认 `"high"` | 使用顶层 `reasoning_effort`，支持 `"low"` / `"high"` / `"max"` 三档，默认 `"max"` | 仅支持思考，`thinking.type` 默认 `"enabled"`，关闭会报错 | 使用 `thinking.type`，可在 `enabled` / `disabled` 间切换 |
| 是否使用 `thinking` | **不要套用** K2.7 Code、K2.6 的 `thinking` 配置 | **不要套用** K2.7 Code、K2.6 的 `thinking` 配置，使用 `reasoning_effort` | 使用 `thinking`，默认开启且不可关闭 | 按需传入 |
| 输出 token 参数 | 使用 `max_completion_tokens`；默认 131072，最大 1048576 | 使用 `max_tokens`；默认 32768（32k），按需调整 | 使用 `max_tokens`；默认 32768（32k），按需调整 | 使用 `max_tokens`，推荐 ≥ 16000（推理 + 回答共享额度） |
| 采样参数 | `temperature=1.0`、`top_p=0.95`、`n=1`、`presence_penalty=0`、`frequency_penalty=0` 为固定值，建议不显式传入 | `temperature=1.0`、`top_p=0.95`、`n=1`、`presence_penalty=0`、`frequency_penalty=0` 为固定值；传其他值报错，建议全部不传 | `temperature=1.0`、`top_p=0.95`、`n=1`、`presence_penalty=0`、`frequency_penalty=0` 为固定值；传其他值报错，建议全部不传 | 思考模式 `temperature=1.0`，非思考模式 `temperature=0.6`；`top_p` / `n` / 惩罚项可在合理范围内调节 |
| 流式输出 | 分别处理 `reasoning_content` 和 `content` | 分别处理 `reasoning_content` 和 `content` | 分别处理 `reasoning_content` 和 `content` | 启用思考时分别处理 `reasoning_content` 和 `content` |
| 多轮回写 | 将 API 返回的完整 assistant message 原样加入下一轮请求，不要只保留 `content` | 保留完整 assistant message，尤其是 `reasoning_content` 和工具调用信息 | 保留完整 assistant message，尤其是 `reasoning_content` 和工具调用信息 | 启用思考时保留 `reasoning_content`；需要长期保留时使用 `thinking.keep` |
| `tool_choice` | 支持 `tool_choice="required"` 强制首轮至少调用一个工具；工具结果需按 `tool_call_id` 回写 | 仅支持 `"auto"`（默认）/ `"none"`；多步工具调用须保留 assistant 的 `reasoning_content` | 仅支持 `"auto"`（默认）/ `"none"`；多步工具调用须保留 assistant 的 `reasoning_content` | 支持标准 OpenAI Function Calling 协议，具体能力以平台支持为准 |
| 图片输入 | 支持 Base64 与公网 URL 直链两种方式，单次请求 body ≤ 100M | 支持 Base64 与公网 URL 直链两种方式，单次请求 body ≤ 100M | 支持 Base64 与公网 URL 直链两种方式，单次请求 body ≤ 100M | 支持 Base64 与公网 URL 直链两种方式，单次请求 body ≤ 100M |
| 视频输入 | 支持 | 支持 | 支持 | 支持 |
| 上下文长度 | 1M | 1M | 256K | 256K |

## 多模态输入限制

Kimi 视觉模型对图片和视频的格式、分辨率及传参方式有以下约束：

| 维度 | 图片 | 视频 |
| --- | --- | --- |
| 支持格式 | JPEG、PNG、GIF、WebP、BMP、HEIC、HEIF | MP4、MPEG、MOV、AVI、FLV、MPG、WebM、WMV、3GPP |
| 不支持 | SVG（可以 XML 文本方式传入源码） | - |
| 建议分辨率 | ≤ 4K（4096 × 2160） | ≤ FHD（1920 × 1080） |
| 传入方式 | Base64 编码 或 文件上传（`purpose="image"`） | 仅文件上传（`purpose="video"`，通过 `ms://` 引用） |
| 动图处理 | GIF / WebP 动图会被解码为视频，按视频计 Token | - |

**说明：**

超过建议分辨率不会提升理解效果，只会增加处理耗时。

## 关键调用场景示例

以下示例保留多轮回写、图片输入和视频输入等容易踩坑的场景。示例中的 `kimi-k2.6` 已在 TokenHub 模型列表中确认为有效调用参数；当前环境没有配置 TokenHub 模型调用 API Key，因此未在本地发起真实推理请求，实际可用性仍以账号权限和控制台模型列表为准。

### 多轮对话回写 `reasoning_content`

启用思考时，必须把上一轮 API 返回的 `reasoning_content` 与 `content` **一并**回写到 `messages`，否则模型在后续轮次中会丢失推理脉络。

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
    "model": "kimi-k2.6",
    "stream": true,
    "thinking": {"type": "enabled", "keep": "all"},
    "messages": [
      {"role": "system", "content": "你是 Kimi。"},
      {"role": "user", "content": "第一个问题..."},
      {
        "role": "assistant",
        "reasoning_content": "<上一轮 API 返回的 reasoning_content>",
        "content": "<上一轮 API 返回的 content>"
      },
      {"role": "user", "content": "请基于之前的分析继续推导。"}
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
    {"role": "system", "content": "你是 Kimi。"},
    {"role": "user", "content": "第一个问题..."},
    {
        "role": "assistant",
        "reasoning_content": "<上一轮 API 返回的 reasoning_content>",
        "content": "<上一轮 API 返回的 content>",
    },
    {"role": "user", "content": "请基于之前的分析继续推导。"},
]

response = client.chat.completions.create(
    model="kimi-k2.6",
    messages=messages,
    stream=True,
    extra_body={"thinking": {"type": "enabled", "keep": "all"}},
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
  { role: 'system', content: '你是 Kimi。' },
  { role: 'user', content: '第一个问题...' },
  {
    role: 'assistant',
    reasoning_content: '<上一轮 API 返回的 reasoning_content>',
    content: '<上一轮 API 返回的 content>',
  },
  { role: 'user', content: '请基于之前的分析继续推导。' },
];

const stream = await client.chat.completions.create({
  model: 'kimi-k2.6',
  messages,
  stream: true,
  thinking: { type: 'enabled', keep: 'all' },
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
import java.io.IOException;
import java.util.*;
import java.util.concurrent.TimeUnit;

public class MultiTurnWithThinking {
    public static void main(String[] args) {
        OkHttpClient client = new OkHttpClient.Builder()
                .connectTimeout(30, TimeUnit.SECONDS)
                .readTimeout(300, TimeUnit.SECONDS)
                .writeTimeout(60, TimeUnit.SECONDS)
                .callTimeout(600, TimeUnit.SECONDS)
                .build();

        Map<String, Object> body = new HashMap<>();
        body.put("model", "kimi-k2.6");
        body.put("stream", true);
        body.put("thinking", Map.of("type", "enabled", "keep", "all"));
        body.put("messages", List.of(
            Map.of("role", "system", "content", "你是 Kimi。"),
            Map.of("role", "user",   "content", "第一个问题..."),
            Map.of(
                "role", "assistant",
                "reasoning_content", "<上一轮 API 返回的 reasoning_content>",
                "content", "<上一轮 API 返回的 content>"
            ),
            Map.of("role", "user", "content", "请基于之前的分析继续推导。")
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
            try (java.io.BufferedReader r = new java.io.BufferedReader(
                    new java.io.InputStreamReader(response.body().byteStream()))) {
                String line;
                while ((line = r.readLine()) != null) {
                    if (line.startsWith("data: ")) System.out.println(line.substring(6));
                }
            }
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
    "bufio"
    "bytes"
    "encoding/json"
    "fmt"
    "net/http"
    "strings"
)

func main() {
    body, _ := json.Marshal(map[string]interface{}{
        "model":    "kimi-k2.6",
        "stream":   true,
        "thinking": map[string]string{"type": "enabled", "keep": "all"},
        "messages": []map[string]interface{}{
            {"role": "system", "content": "你是 Kimi。"},
            {"role": "user", "content": "第一个问题..."},
            {
                "role":              "assistant",
                "reasoning_content": "<上一轮 API 返回的 reasoning_content>",
                "content":           "<上一轮 API 返回的 content>",
            },
            {"role": "user", "content": "请基于之前的分析继续推导。"},
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

### 多模态调用

#### 1. 图片输入：Base64 编码

适合本地文件 / 内网图片场景：

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
  "model": "kimi-k2.6",
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
    model="kimi-k2.6",
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
import fs from 'node:fs';
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: 'YOUR_API_KEY',
  baseURL: 'https://tokenhub.tencentmaas.com/v1',
});

const imageB64 = fs.readFileSync('image.jpg').toString('base64');

const response = await client.chat.completions.create({
  model: 'kimi-k2.6',
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
import java.io.IOException;
import java.nio.file.*;
import java.util.*;
import java.util.Base64;
import java.util.concurrent.TimeUnit;

public class ImageBase64Chat {
    public static void main(String[] args) throws IOException {
        // 请准备您本地的图片文件，支持 PNG/JPG/JPEG/WebP 格式
        byte[] bytes = Files.readAllBytes(Paths.get("image.jpg"));
        String imageB64 = Base64.getEncoder().encodeToString(bytes);

        OkHttpClient client = new OkHttpClient.Builder()
                .connectTimeout(30, TimeUnit.SECONDS)
                .readTimeout(300, TimeUnit.SECONDS)
                .writeTimeout(60, TimeUnit.SECONDS)
                .callTimeout(600, TimeUnit.SECONDS)
                .build();

        Map<String, Object> body = new HashMap<>();
        body.put("model", "kimi-k2.6");
        body.put("messages", List.of(Map.of(
            "role", "user",
            "content", List.of(
                Map.of("type", "text", "text", "请描述这张图片"),
                Map.of("type", "image_url", "image_url", Map.of(
                    "url", "data:image/jpeg;base64," + imageB64
                ))
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
    "encoding/base64"
    "encoding/json"
    "fmt"
    "io"
    "net/http"
    "os"
)

func main() {
    img, _ := os.ReadFile("image.jpg")
    imageB64 := base64.StdEncoding.EncodeToString(img)

    body, _ := json.Marshal(map[string]interface{}{
        "model": "kimi-k2.6",
        "messages": []map[string]interface{}{
            {
                "role": "user",
                "content": []map[string]interface{}{
                    {"type": "text", "text": "请描述这张图片"},
                    {
                        "type": "image_url",
                        "image_url": map[string]string{
                            "url": "data:image/jpeg;base64," + imageB64,
                        },
                    },
                },
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

#### 2. 图片输入：公网 URL 直链（仅适用于支持 URL 的模型）

适合已托管在 CDN / 对象存储的图片，可显著减小请求体积。但公网 URL 并非所有 Kimi 模型都支持，例如 K3 官方限制为不支持公网图片 URL，需改用 Base64 或 `ms://<file-id>`。

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
    "model": "kimi-k2.6",
    "messages": [{
      "role": "user",
      "content": [
        {"type": "text", "text": "请描述这张图片"},
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
    model="kimi-k2.6",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "请描述这张图片"},
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
  model: 'kimi-k2.6',
  messages: [{
    role: 'user',
    content: [
      { type: 'text', text: '请描述这张图片' },
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
                .connectTimeout(30, TimeUnit.SECONDS)
                .readTimeout(300, TimeUnit.SECONDS)
                .writeTimeout(60, TimeUnit.SECONDS)
                .callTimeout(600, TimeUnit.SECONDS)
                .build();

        Map<String, Object> body = new HashMap<>();
        body.put("model", "kimi-k2.6");
        body.put("messages", List.of(Map.of(
            "role", "user",
            "content", List.of(
                Map.of("type", "text", "text", "请描述这张图片"),
                // 请替换为您自己的可公网访问图片 URL
                Map.of("type", "image_url", "image_url", Map.of(
                    "url", "https://example.com/path/to/your/image.jpg"
                ))
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
        "model": "kimi-k2.6",
        "messages": []map[string]interface{}{
            {
                "role": "user",
                "content": []map[string]interface{}{
                    {"type": "text", "text": "请描述这张图片"},
                    {
                        "type":      "image_url",
                        "image_url": map[string]string{"url": "https://www.gstatic.com/webp/gallery/1.jpg"},
                    },
                },
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

**注意：**

使用 URL 直链时，请确保该 URL **公网可访问**且无需鉴权；私网 / 内网图片或带签名校验的 URL 仍需先下载并以 Base64 方式上传。

#### 3. 视频输入（按模型支持情况使用）

视频输入与图片类似，但不同 Kimi 模型支持范围不同：K3、K2.8 Preview、K2.7 Code、K2.6 可按平台能力使用视频输入。具体传入方式请以对应模型的接口约束为准，不应直接将下方 K2.6 示例替换为其他模型 ID。

cURL

Python

Node.js

Java

Go

```bash
# 先把视频读为 base64
VIDEO_B64=$(base64 -i demo.mp4 | tr -d '\\n')

# 用临时文件传 body，避免 base64 字符串过大触发 "Argument list too long"
cat > /tmp/req.json <<EOF
{
  "model": "kimi-k2.6",
  "messages": [{
    "role": "user",
    "content": [
      {"type": "text", "text": "请总结视频内容"},
      {"type": "video_url", "video_url": {"url": "data:video/mp4;base64,${VIDEO_B64}"}}
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

with open("demo.mp4", "rb") as f:
    video_b64 = base64.b64encode(f.read()).decode()

response = client.chat.completions.create(
    model="kimi-k2.6",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "请总结视频内容"},
            {"type": "video_url", "video_url": {"url": f"data:video/mp4;base64,{video_b64}"}},
        ],
    }],
)
print(response.choices[0].message.content)
```

```javascript
import fs from 'node:fs';
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: 'YOUR_API_KEY',
  baseURL: 'https://tokenhub.tencentmaas.com/v1',
});

const videoB64 = fs.readFileSync('demo.mp4').toString('base64');

const response = await client.chat.completions.create({
  model: 'kimi-k2.6',
  messages: [{
    role: 'user',
    content: [
      { type: 'text', text: '请总结视频内容' },
      { type: 'video_url', video_url: { url: `data:video/mp4;base64,${videoB64}` } },
    ],
  }],
});
console.log(response.choices[0].message.content);
```

```java
import okhttp3.*;
import com.google.gson.Gson;
import java.io.IOException;
import java.nio.file.*;
import java.util.*;
import java.util.Base64;
import java.util.concurrent.TimeUnit;

public class VideoChat {
    public static void main(String[] args) throws IOException {
        // 请准备您本地的视频文件，支持 MP4/MOV/AVI 等格式
        byte[] bytes = Files.readAllBytes(Paths.get("demo.mp4"));
        String videoB64 = Base64.getEncoder().encodeToString(bytes);

        OkHttpClient client = new OkHttpClient.Builder()
                .connectTimeout(30, TimeUnit.SECONDS)
                .readTimeout(300, TimeUnit.SECONDS)
                .writeTimeout(60, TimeUnit.SECONDS)
                .callTimeout(600, TimeUnit.SECONDS)
                .build();

        Map<String, Object> body = new HashMap<>();
        body.put("model", "kimi-k2.6");
        body.put("messages", List.of(Map.of(
            "role", "user",
            "content", List.of(
                Map.of("type", "text", "text", "请总结视频内容"),
                Map.of("type", "video_url", "video_url", Map.of(
                    "url", "data:video/mp4;base64," + videoB64
                ))
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
    "encoding/base64"
    "encoding/json"
    "fmt"
    "io"
    "net/http"
    "os"
)

func main() {
    video, _ := os.ReadFile("demo.mp4")
    videoB64 := base64.StdEncoding.EncodeToString(video)

    body, _ := json.Marshal(map[string]interface{}{
        "model": "kimi-k2.6",
        "messages": []map[string]interface{}{
            {
                "role": "user",
                "content": []map[string]interface{}{
                    {"type": "text", "text": "请总结视频内容"},
                    {
                        "type": "video_url",
                        "video_url": map[string]string{
                            "url": "data:video/mp4;base64," + videoB64,
                        },
                    },
                },
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

**说明：**

单次请求 body 大小受平台限制（通常 100MB 以内），过大的视频请先压缩或截取关键片段后再上传。

## Kimi 思考模式

Kimi 系列模型的思考参数需按具体模型配置：K3 和 K2.8 Preview 使用 `reasoning_effort`，K2.7 Code、K2.6 使用 `thinking`。

### 1. K3 和 K2.8 Preview：`reasoning_effort` 参数

`kimi-k3` 和 `kimi-k2.8-preview` 始终开启思考模式，通过顶层 `reasoning_effort` 配置思考力度，支持 `"low"`、`"high"`、`"max"` 三档，默认 `"max"`。下方以 K3 为例；K2.8 Preview 的输出 token 参数使用 `max_tokens`。

```json
{
  "model": "kimi-k3",
  "reasoning_effort": "max",
  "messages": [
    {"role": "user", "content": "证明根号 2 是无理数。"}
  ]
}
```

**注意：**

调用 `kimi-k3` 和 `kimi-k2.8-preview` 时不要套用 K2.7 Code、K2.6 的 `thinking` 配置；多轮对话和工具调用时，需要将 API 返回的完整 assistant message 原样加入下一轮请求，不要只保留 `content`。

### 2. K2.7 Code、K2.6：`thinking` 参数

K2.6 / K2.7 Code 的 `thinking` 字段位于请求体顶层，结构如下：

```json
"thinking": {
    "type": "enabled",
    "keep": "all"
}
```

| 字段 | 类型 | 默认值 | 取值 | 说明 |
| --- | --- | --- | --- | --- |
| `type` | string | `"enabled"` | `"enabled"` / `"disabled"` | 当前请求是否启用思考能力 |
| `keep` | string | null | `null` | `"all"` / 不传 | 多轮对话中是否透传历史 `reasoning_content` |

**注意：**

`thinking` 不是 OpenAI 标准字段，本节用法适用于 K2.7 Code、K2.6，不直接适用于 K2.8 Preview。使用官方 SDK 时需通过 `extra_body`（Python）或直接展开到顶层（Node.js）透传；HTTP 直接调用时放在请求体顶层即可。

### 3. `reasoning_content` 字段

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

### 4. 流式思考输出

启用思考时**强烈建议使用流式调用**（`stream: true`）：

**避免超时**：思考内容可能较长，整体响应时间较久，非流式容易触发服务超时。

**顺序明确**：流式模式下 `reasoning_content` 一定在 `content` 之前完整输出，便于 UI 区分**思考中**和**正在回答**两种状态。

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
    "model": "kimi-k2.6",
    "max_tokens": 32768,
    "stream": true,
    "thinking": {"type": "enabled"},
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
    model="kimi-k2.6",
    messages=[{"role": "user", "content": "请用一句话解释傅里叶变换。"}],
    max_tokens=32768,
    stream=True,
    extra_body={"thinking": {"type": "enabled"}},
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

// Node.js SDK 暂未原生支持 thinking / extra_body，直接展开到顶层即可
// 注：若使用 TypeScript，最后一个对象后面加 `as any` 绕过类型检查
const stream = await client.chat.completions.create({
  model: 'kimi-k2.6',
  messages: [{ role: 'user', content: '请用一句话解释傅里叶变换。' }],
  max_tokens: 32768,
  stream: true,
  thinking: { type: 'enabled' },
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
import java.util.concurrent.TimeUnit;

public class ThinkingStream {
    public static void main(String[] args) {
        OkHttpClient client = new OkHttpClient.Builder()
                .connectTimeout(30, TimeUnit.SECONDS)
                .readTimeout(300, TimeUnit.SECONDS)
                .writeTimeout(60, TimeUnit.SECONDS)
                // SSE 流式不设 callTimeout，避免整条流被整体超时截断
                .build();

        Map<String, Object> body = new HashMap<>();
        body.put("model", "kimi-k2.6");
        body.put("max_tokens", 32768);
        body.put("stream", true);
        body.put("thinking", Map.of("type", "enabled"));
        body.put("messages", List.of(
            Map.of("role", "user", "content", "请用一句话解释傅里叶变换。")
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
                    if ("[DONE]".equals(data)) return;
                    JsonObject delta = JsonParser.parseString(data).getAsJsonObject()
                        .getAsJsonArray("choices").get(0).getAsJsonObject()
                        .getAsJsonObject("delta");
                    if (delta.has("reasoning_content")) {
                        System.out.print(delta.get("reasoning_content").getAsString());
                    }
                    if (delta.has("content") && !delta.get("content").isJsonNull()) {
                        System.out.print(delta.get("content").getAsString());
                    }
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
        "model":      "kimi-k2.6",
        "max_tokens": 32768,
        "stream":     true,
        "thinking":   map[string]string{"type": "enabled"},
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

### 5. Preserved Thinking（多轮保留思考）

本节沿用 K2.7 Code、K2.6 的参数说明，不直接适用于 K2.8 Preview。`thinking.keep` 控制**历史轮次**的 `reasoning_content` 是否参与下一轮推理：

| 取值 | 含义 | 适用场景 |
| --- | --- | --- |
| 不传 / `null`（默认） | 历史轮次的推理内容不透传，上下文更短，成本更低 | 普通多轮对话 |
| `"all"` | 完整保留历史轮次的推理过程，让模型延续之前的思考脉络 | 复杂多步推理、Agent 工具调用、长程代码任务 |

**注意：**

`keep` 只影响**历史**思考是否传给模型，不影响**当前轮次**是否产生思考；推荐在需要连续推理的场景下与 `type: "enabled"` 搭配使用。
