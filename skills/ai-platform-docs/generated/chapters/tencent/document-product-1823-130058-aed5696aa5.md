<!-- Official source: https://cloud.tencent.com/document/product/1823/130058 -->
<!-- Source SHA-256: de56a53a1536cacb1ccacd2b8c73334d8b8b440b3f274df97907ead80a79a4c7 -->

# 快速入门

官方来源：https://cloud.tencent.com/document/product/1823/130058
最近更新时间：2026-10-23 18:08:00

本文将为您介绍如何在大模型服务平台 TokenHub 完成您的首次 API 调用。

## 准备工作

在使用腾讯云大模型服务平台 TokenHub 之前，您需要 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。

## 操作步骤

### 步骤一：登录大模型服务平台 TokenHub 控制台

登录 [腾讯云大模型服务平台 TokenHub 控制台](https://console.cloud.tencent.com/tokenhub/)，按照界面提示开通大模型服务平台 TokenHub 后，您可以在模型广场浏览选择模型，详细模型信息可参见 [模型列表](https://cloud.tencent.com/document/product/1823/130051)。

![](https://qcloudimg.tencent-cloud.cn/image/document/28eef8ef5fd4917633029c1b62b1c66e.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/28eef8ef5fd4917633029c1b62b1c66e.png)

### 步骤二：领取免费体验包

平台为新用户提供一定额度的免费体验额度，让您零成本试用模型。各模型免费体验额度信息可参见 [新人免费体验包](https://cloud.tencent.com/document/product/1823/130053)，具体免费额度及有效期请以控制台显示为准。

#### 领取方式

1. 进入 [模型广场](https://console.cloud.tencent.com/tokenhub/models) 页面，单击右上角的**新用户福利免费体验**。

2. 在弹窗中勾选模型后，单击**立即领取**，即可获得多个模型的免费使用额度。

### 步骤三：创建 API Key

在调用模型 API 之前，您需要先创建 API Key 作为鉴权凭证。

1. 进入[API Key 管理](https://console.cloud.tencent.com/tokenhub/apikey) 页面。

2. 在页面上方选择地域后，单击**创建 API Key。**

3. 在**创建 API Key** 对话框填写 **Key 名称**，并设置**额度限制**及**可访问范围**：

**额度限制：**开启后，该 API Key 的 token 用量达到配额上限将停止服务，用量统计不区分模型与推理服务接入点（免费包不计算入内）。

**全选**：可访问当前账号下所有模型和推理服务。

**限定范围**：指定当前账号下可访问的模型和/或推理服务，实现访问范围控制。

4. 单击**确定**，完成创建。

创建完成后，请您务必**复制并妥善保管 API Key**，在后续调用 API 流程中将会使用该信息。更多 API Key 管理信息，请参见 [API Key 管理](https://cloud.tencent.com/document/product/1823/130090)。

![](https://qcloudimg.tencent-cloud.cn/image/document/acc114fd208cdb72c59df7d1e85f9baa.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/acc114fd208cdb72c59df7d1e85f9baa.png)

### 步骤四：调用模型

#### 通过 API 调用模型

大模型服务平台 TokenHub 兼容 **OpenAI API 协议**，您可以使用熟悉的 SDK 和工具直接接入。API 调用详情请参见 [调用指南](https://cloud.tencent.com/document/product/1823/130077)。

**说明：**

请您将示例代码中的 `YOUR_API_KEY` 替换为您真实的 API KEY。

修改 `model` 字段，更换您需要调用的模型，各模型对应 model 值可参见 [模型列表](https://cloud.tencent.com/document/product/1823/130051) 中的 **model（调用参数）**。

CURL

Python

NodeJS

Java

Go

```bash
# 请将 YOUR_API_KEY 替换为您在前面步骤创建的 API KEY
# 请在 model 字段中更换您需要体验的模型名称
curl -X POST 'https://tokenhub.tencentmaas.com/v1/chat/completions' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
    "model": "deepseek-v3",
    "messages": [{"role": "user", "content": "你好"}],
    "stream": true
  }'
```

```python
from openai import OpenAI

client = OpenAI(
# 请将 YOUR_API_KEY 替换为您在前面步骤创建的 API KEY
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1"
)

response = client.chat.completions.create(
# 请在 model 字段中更换您需要体验的模型名称
    model="deepseek-v3",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "你好，请介绍一下你自己"}
    ]
)
print(response.choices[0].message.content)
```

```javascript
import OpenAI from 'openai';


const client = new OpenAI({
// 请将 YOUR_API_KEY 替换为您在前面步骤创建的 API KEY
  apiKey: 'YOUR_API_KEY',
  baseURL: 'https://tokenhub.tencentmaas.com/v1',
});


async function main() {
  const response = await client.chat.completions.create({
// 请在 model 字段中更换您需要体验的模型名称
    model: 'deepseek-v3',
    messages: [
      { role: 'system', content: 'You are a helpful assistant.' },
      { role: 'user', content: '你好，请介绍一下你自己' },
    ],
  });
  console.log(response.choices[0].message.content);
}


main();
```

```java
import java.net.http.*;
import java.net.URI;


public class MaaSExample {
    public static void main(String[] args) throws Exception {
// 请将 YOUR_API_KEY 替换为您在前面步骤创建的 API KEY
        String apiKey = "YOUR_API_KEY";
// 请在 model 字段中更换您需要体验的模型名称
        String body = """
            {
                "model": "deepseek-v3",
                "messages": [{"role": "user", "content": "你好"}]
            }
            """;


        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create("https://tokenhub.tencentmaas.com/v1/chat/completions"))
            .header("Authorization", "Bearer " + apiKey)
            .header("Content-Type", "application/json")
            .POST(HttpRequest.BodyPublishers.ofString(body))
            .build();


        HttpClient client = HttpClient.newHttpClient();
        HttpResponse<String> response = client.send(request,
            HttpResponse.BodyHandlers.ofString());
        System.out.println(response.body());
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
// 请将 YOUR_API_KEY 替换为您在前面步骤创建的 API KEY
    apiKey := "YOUR_API_KEY"
    body := map[string]interface{}{
    // 请在 model 字段中更换您需要体验的模型名称
        "model": "deepseek-v3",
        "messages": []map[string]string{
            {"role": "user", "content": "你好"},
        },
    }

    jsonBody, _ := json.Marshal(body)
    req, _ := http.NewRequest("POST",
        "https://tokenhub.tencentmaas.com/v1/chat/completions",
        bytes.NewBuffer(jsonBody))
    req.Header.Set("Authorization", "Bearer "+apiKey)
    req.Header.Set("Content-Type", "application/json")

    resp, err := http.DefaultClient.Do(req)
    if err != nil {
        panic(err)
    }
    defer resp.Body.Close()

    result, _ := io.ReadAll(resp.Body)
    fmt.Println(string(result))
}
```

#### 通过命令行工具调用

您也可以使用 TokenHub 命令行工具（`thcli`），在终端一条命令完成模型调用，无需编写代码：

```bash
npm i -g tencent-tokenhub-cli
thcli auth login
thcli +chat --model <模型 Id>  "你好"
```

**说明：**

除对话调用外，`thcli` 还支持查模型、管 API Key、看用量、排障等操作，详情请参见 [TokenHub CLI 使用指南](https://cloud.tencent.com/document/product/1823/138217)。

#### 通过 AI 工具调用模型

详情参考：

在 [Claude Code](https://cloud.tencent.com/document/product/1823/131903) 中调用

在 [Cursor](https://cloud.tencent.com/document/product/1823/130933) 中调用

在 [OpenClaw](https://cloud.tencent.com/document/product/1823/130935) 中调用

在 [Hermes Agent](https://cloud.tencent.com/document/product/1823/131927) 中调用

在 [WorkBuddy](https://cloud.tencent.com/document/product/1823/131902) 中调用

在 [CodeBuddy Code](https://cloud.tencent.com/document/product/1823/131901) 中调用

在 [OpenCode](https://cloud.tencent.com/document/product/1823/130936) 中调用

在 [Cline](https://cloud.tencent.com/document/product/1823/130932) 中调用

在 [Kilo Code](https://cloud.tencent.com/document/product/1823/131904) 中调用

在 [Roo Code](https://cloud.tencent.com/document/product/1823/131905) 中调用

## 下一步

您可以前往**体验中心**，在线体验模型能力，详情请参见 [体验中心](https://cloud.tencent.com/document/product/1823/130085)。

您可以前往**开通管理**，快速批量开启模型按量付费，详情请参见[开通管理](https://cloud.tencent.com/document/product/1823/137795)。

您可以前往**在线推理**，管理正在使用的模型服务，详情请参见 [在线推理](https://cloud.tencent.com/document/product/1823/130087)。

如果您需要查看模型用量，请参见 [用量统计](https://cloud.tencent.com/document/product/1823/130088)。
