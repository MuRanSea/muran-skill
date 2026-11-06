<!-- Official source: https://cloud.tencent.com/document/product/1823/131208 -->
<!-- Source SHA-256: 4631c7381edd0df158e67d0a150eb8ca020cd1e9a2495f19556d28ad16eb6fdf -->

# 深度思考

官方来源：https://cloud.tencent.com/document/product/1823/131208
最近更新时间：2026-11-04 12:13:31

## 功能说明

深度思考模型支持在生成最终答案前先进行推理，提升复杂任务的准确性和可解释性。

## 适用场景

复杂代码生成、代码修复、代码重构。

数学推导、逻辑分析、多步骤决策。

复杂信息抽取后再综合归纳。

需要更强稳定性和更少推理失误的任务。

## 开启/关闭深度思考

通过 `thinking` 参数控制是否开启思考模式。

开启深度思考：`"thinking":{"type":"enabled"}`

关闭深度思考：`"thinking":{"type":"disabled"}`

### 支持模型

<table><colgroup><col/><col/><col/></colgroup><tbody><tr><td><div><b>模型名称</b></div></td><td><div><b>MODEL 参数值</b></div></td><td><div><b>默认值及说明</b></div></td></tr><tr><td><div>Hy4</div></td><td><div><code>hy4</code></div></td><td><div>enabled</div></td></tr><tr><td colspan="1" rowspan="1"><div>Hy4 preview</div></td><td colspan="1" rowspan="1"><div><code>hy4-preview</code></div></td><td colspan="1" rowspan="1"><div>enabled</div></td></tr><tr><td><div>Hy3</div></td><td><div><code>hy3</code></div></td><td><div>enabled</div></td></tr><tr><td><div>DeepSeek-V4-Flash（原厂直连）</div></td><td><div><code>deepseek-v4-flash-202605</code></div></td><td><div>enabled</div></td></tr><tr><td><div>DeepSeek-V4-Pro</div></td><td><div><code>deepseek-v4-pro</code></div></td><td><div>enabled</div></td></tr><tr><td><div>DeepSeek-V4-Pro（原厂直连）</div></td><td><div><code>deepseek-v4-pro-202606</code></div></td><td><div>enabled</div></td></tr><tr><td><div>GLM-5.3</div></td><td><div><code>glm-5.3</code></div></td><td><div>enabled（不支持关闭）</div></td></tr><tr><td><div>GLM-5.3-Flash</div></td><td><div><code>glm-5.3-flash</code></div></td><td><div>enabled（不支持关闭）</div></td></tr><tr><td><div>GLM-5.3-FlashX</div></td><td><div><code>glm-5.3-flashx</code></div></td><td><div>enabled（不支持关闭）</div></td></tr><tr><td><div>GLM-5.2</div></td><td><div><code>glm-5.2</code></div></td><td><div>enabled</div></td></tr><tr><td><div>GLM-5V-Turbo</div></td><td><div><code>glm-5v-turbo</code></div></td><td><div>enabled</div></td></tr><tr><td><div>Kimi K3</div></td><td><div><code>kimi-k3</code></div></td><td><div>enabled（不支持关闭）</div></td></tr><tr><td><div>Kimi-K2.7-Code</div></td><td><div><code>kimi-k2.7-code</code></div></td><td><div>enabled（不支持关闭）</div></td></tr><tr><td><div>Kimi-K2.7-Code-HighSpeed</div></td><td><div><code>kimi-k2.7-code-highspeed</code></div></td><td><div>enabled（不支持关闭）</div></td></tr><tr><td><div>Kimi-K2.6</div></td><td><div><code>kimi-k2.6</code></div></td><td><div>enabled</div></td></tr><tr><td><div>MiniMax-M3</div></td><td><div><code>minimax-m3</code></div></td><td><div>adaptive</div></td></tr><tr><td><div>MiniMax-M2.7</div></td><td><div><code>minimax-m2.7</code></div></td><td><div>enabled（不支持关闭）</div></td></tr></tbody></table>

### 调用示例：开启深度思考

**说明：**

请将 `YOUR_API_KEY` 替换为您创建的 [API Key](https://console.cloud.tencent.com/tokenhub/apikey)。

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
    "model": "MODEL 参数值",
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
    model="MODEL 参数值",
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

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: 'YOUR_API_KEY',
  baseURL: 'https://tokenhub.tencentmaas.com/v1',
});

// Node.js SDK：thinking 字段直接展开到顶层
const response = await client.chat.completions.create({
  model: 'MODEL 参数值',
  messages: [
    { role: 'user', content: '小明有5个苹果，给了小红2个，又买了3个，最后还剩几个？' },
  ],
  thinking: { type: 'enabled' },
} as any);

const msg: any = response.choices[0].message;
if (msg.reasoning_content) console.log('思考过程:', msg.reasoning_content);
console.log('最终回答:', msg.content);
```

```java
import okhttp3.*;
import com.google.gson.Gson;
import java.util.*;

public class ThinkingChat {
    public static void main(String[] args) throws Exception {
        Map<String, Object> body = new HashMap<>();
        body.put("model", "MODEL 参数值");
        body.put("messages", List.of(
            Map.of("role", "user", "content", "小明有5个苹果，给了小红2个，又买了3个，最后还剩几个？")
        ));
        body.put("thinking", Map.of("type", "enabled"));

        Request request = new Request.Builder()
            .url("https://tokenhub.tencentmaas.com/v1/chat/completions")
            .header("Authorization", "Bearer YOUR_API_KEY")
            .post(RequestBody.create(new Gson().toJson(body), MediaType.parse("application/json")))
            .build();

        try (Response response = new OkHttpClient().newCall(request).execute()) {
            // 响应体中 message.reasoning_content 为思考过程，message.content 为最终回答
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
        "model": "MODEL 参数值",
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

### 调用示例：关闭深度思考

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
    "model": "MODEL 参数值",
    "messages": [
      {"role": "user", "content": "小明有5个苹果，给了小红2个，又买了3个，最后还剩几个？"}
    ],
    "thinking": {"type": "disabled"},
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
    model="MODEL 参数值",
    messages=[
        {"role": "user", "content": "小明有5个苹果，给了小红2个，又买了3个，最后还剩几个？"},
    ],
    extra_body={"thinking": {"type": "disabled"}},
)
print(response.choices[0].message.content)
```

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: 'YOUR_API_KEY',
  baseURL: 'https://tokenhub.tencentmaas.com/v1',
});

const response = await client.chat.completions.create({
  model: 'MODEL 参数值',
  messages: [
    { role: 'user', content: '小明有5个苹果，给了小红2个，又买了3个，最后还剩几个？' },
  ],
  thinking: { type: 'disabled' },
} as any);
console.log(response.choices[0].message.content);
```

```java
import okhttp3.*;
import com.google.gson.Gson;
import java.util.*;

public class DisableThinking {
    public static void main(String[] args) throws Exception {
        Map<String, Object> body = new HashMap<>();
        body.put("model", "MODEL 参数值");
        body.put("messages", List.of(
            Map.of("role", "user", "content", "小明有5个苹果，给了小红2个，又买了3个，最后还剩几个？")
        ));
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
        "model": "MODEL 参数值",
        "messages": []map[string]string{
            {"role": "user", "content": "小明有5个苹果，给了小红2个，又买了3个，最后还剩几个？"},
        },
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

## 推理深度配置

通过 `reasoning_effort` 参数控制推理深度。该参数用于约束模型投入多少推理强度；推理强度越高，通常回答会更充分，但延迟和 token 消耗也会更高。

### 支持模型

<table><colgroup><col/><col/><col/></colgroup><tbody><tr><td><div><b>模型名称</b></div></td><td><div><b>MODEL 参数值</b></div></td><td><div><b>说明</b></div></td></tr><tr><td colspan="1" rowspan="1"><div>Hy4</div></td><td colspan="1" rowspan="1"><div><code>hy4</code></div></td><td><div>默认 <code>high</code>，支持 <code>high</code>、<code>no_think</code></div></td></tr><tr><td><div>Hy4 preview</div></td><td><div><code>hy4-preview</code></div></td><td><div>默认 <code>high</code>，支持 <code>high</code>、<code>no_think</code></div></td></tr><tr><td><div>Hy3</div></td><td><div><code>hy3</code></div></td><td><div>默认 <code>high</code>，支持 <code>low</code>、<code>high</code>、<code>no_think</code></div></td></tr><tr><td><div>DeepSeek-V4-Pro</div></td><td><div><code>deepseek-v4-pro</code></div></td><td><div>默认 <code>high</code>，支持 <code>low</code>、<code>high</code>、<code>max</code>、<code>none</code></div></td></tr><tr><td><div>GLM-5.3-Flash</div></td><td><div><code>glm-5.3-flash</code></div></td><td><div>默认 <code>max</code>，支持 <code>low</code>、<code>high</code>、<code>max</code></div></td></tr><tr><td><div>GLM-5.3-FlashX</div></td><td><div><code>glm-5.3-flashx</code></div></td><td><div>默认 <code>max</code>，支持 <code>low</code>、<code>high</code>、<code>max</code></div></td></tr><tr><td><div>GLM-5.3</div></td><td><div><code>glm-5.3</code></div></td><td><div>默认 <code>max</code>，支持 <code>low</code>、<code>high</code>、<code>max</code></div></td></tr><tr><td><div>GLM-5.2</div></td><td><div><code>glm-5.2</code></div></td><td><div>默认 <code>max</code>，支持 <code>max</code>、<code>xhigh</code>、<code>high</code>、<code>medium</code>、<code>low</code>、<code>minimal</code>、<code>none</code></div></td></tr><tr><td><div>Kimi K3</div></td><td><div><code>kimi-k3</code></div></td><td><div>默认 <code>max</code>，支持 <code>low</code>、<code>high</code>、<code>max</code></div></td></tr></tbody></table>

### 调用示例：推理深度配置

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
    "model": "MODEL 参数值",
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
    model="MODEL 参数值",
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

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: 'YOUR_API_KEY',
  baseURL: 'https://tokenhub.tencentmaas.com/v1',
});

const response = await client.chat.completions.create({
  model: 'MODEL 参数值',
  messages: [
    { role: 'user', content: '小明有5个苹果，给了小红2个，又买了3个，最后还剩几个？' },
  ],
  temperature: 0.9,
  reasoning_effort: 'high',
} as any);

const msg: any = response.choices[0].message;
if (msg.reasoning_content) console.log('思考过程:', msg.reasoning_content);
console.log('最终回答:', msg.content);
```

```java
import okhttp3.*;
import com.google.gson.Gson;
import java.util.*;

public class ReasoningEffortChat {
    public static void main(String[] args) throws Exception {
        Map<String, Object> body = new HashMap<>();
        body.put("model", "MODEL 参数值");
        body.put("messages", List.of(
            Map.of("role", "user", "content", "小明有5个苹果，给了小红2个，又买了3个，最后还剩几个？")
        ));
        body.put("temperature", 0.9);
        body.put("reasoning_effort", "high");

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
        "model": "MODEL 参数值",
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

### 响应示例

启用思考后，响应中会附带 `reasoning_content` 思考过程字段：

```json
{
  "id": "REPLACED_ID",
  "object": "chat.completion",
  "created": 1775146546,
  "model": "MODEL 参数值",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "答案是 6 个。",
        "reasoning_content": "用户现在需要解决的是小明苹果数量变化的问题，首先得理清楚每一步的变化。首先小明一开始有5个苹果，给了小红2个，那这时候应该减去2，对吧？然后又买了3个，这时候要加上3。所以计算的话就是5减2再加3。先算5-2=3，然后3+3=6。"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 22,
    "completion_tokens": 264,
    "total_tokens": 286
  }
}
```

思考模式下的工具调用，需在每一轮请求都回填历史 `reasoning_content`，以获取最佳效果，详情请参见 [保留式思考模式（Preserved Thinking）](https://cloud.tencent.com/document/product/1823/133534)。
