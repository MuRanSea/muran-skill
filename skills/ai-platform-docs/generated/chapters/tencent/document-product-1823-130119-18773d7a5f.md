<!-- Official source: https://cloud.tencent.com/document/product/1823/130119 -->
<!-- Source SHA-256: f1ef2605f1ebd1a2ba5c8990a26068186dc35fc9aae2fb541e4da2a0e1f8f40d -->

# Token Plan 个人版快速入门

官方来源：https://cloud.tencent.com/document/product/1823/130119
最近更新时间：2026-09-14 10:37:12

本文介绍如何在龙虾或者编程工具中快速使用 Token Plan 套餐所支持的模型进行办公或者代码开发。

## 步骤一：订阅套餐

前往对应的购买页，选择适合您的订阅套餐，套餐介绍请参见 [Token Plan 个人版套餐概览](https://cloud.tencent.com/document/product/1823/130060)：

[通用 Token Plan 购买页](https://console.cloud.tencent.com/tokenhub/tokenplan/common)

[Hy Token Plan 购买页](https://console.cloud.tencent.com/tokenhub/tokenplan/hy)

## 步骤二：获取核心配置

您可以获取**模型配置、Base URL、API Key**，用于工具中。

### 获取模型配置

在工具配置文件中指定模型，可实时切换模型。支持配置的模型列表如下：

**说明：**

配置 Model ID 时，必须使用全小写格式。

通用 Token Plan 与 Hy Token Plan 适配不同的模型列表，请根据需求选择对应套餐的模型使用。

[通用 Token Plan 可用模型](https://cloud.tencent.com/document/product/1823/130060#b6fdbed0-897c-475d-a9a1-f9af922027c4)

[Hy Token Plan 可用模型](https://cloud.tencent.com/document/product/1823/130060#b145766a-c747-42eb-89c2-a04463d20cc5)

### 获取 Base URL 和完整 URL

不同的工具配置的 URL 根据兼容的协议会有不同：

1. **Base URL**

兼容 OpenAI 接口协议工具：`https://api.lkeap.cloud.tencent.com/plan/v3`

兼容 Anthropic 接口协议工具：`https://api.lkeap.cloud.tencent.com/plan/anthropic`

2. **完整 URL**

兼容 OpenAI 接口协议工具：`https://api.lkeap.cloud.tencent.com/plan/v3/chat/completions`

兼容 Anthropic 接口协议工具：`https://api.lkeap.cloud.tencent.com/plan/anthropic/v1/messages`

### 获取 API Key

1. **生成 API Key**：在**大模型服务平台 TokenHub >** [**Token Plan**](https://console.cloud.tencent.com/tokenhub/tokenplan) **> 通用 Token Plan / Hy Token Plan** 标签页，单击**生成密钥**，生成您的专属 API Key。（如果您已生成密钥，请跳过步骤。）

**注意：**

通用 Token Plan 与 Hy Token Plan **共用同一个 API Key**，您购买后，可在任意一个套餐页面生成密钥，仅需生成一次即可通用。

2. **获取 API Key：**密钥生成成功后，即可单击**复制**，获取套餐专属 API Key（格式为 `sk-tp-xxx`）。

## 步骤三：快速验证模型调用

获取 API Key 后您可在命令行终端通过 cURL 简单验证连通性，请将下方`$your_api_key` 替换为您的实际 API Key，`$model_id` 可以对照 [模型配置](https://cloud.tencent.com/document/product/1823/130119#ac64e0d9-6ef1-475c-9bed-f15dc361859a) 换成您要测试的模型 Model ID：

```java
curl --location 'https://api.lkeap.cloud.tencent.com/plan/v3/chat/completions' \\
--header 'Authorization: Bearer $your_api_key' \\
--header 'Content-Type: application/json' \\
--data '{
  "model": "$model_id",
  "messages": [
    {
      "role": "user",
      "content": "hello"
    }
  ],
  "stream": false
}'
```

## 步骤四：配置 AI 工具

Token Plan 兼容热门的 [龙虾工具和 AI 编码工具](https://cloud.tencent.com/document/product/1823/130060#5104f44d-4433-4c57-a024-724c88fa0d30)，您可以根据自己的偏好选择，将 URL、API Key 和具体的模型（Model Name）配置到工具中，就能使用大模型服务。

## 步骤五（可选）：管理套餐用量

您可以在控制台查看您套餐的 Tokens 消耗情况，也可以根据需要对套餐进行升级。

### **1. 查看套餐用量消耗**

可以前往**大模型服务平台 TokenHub >** [**Token Plan**](https://console.cloud.tencent.com/tokenhub/tokenplan) **> 通用 Token Plan / Hy Token Plan** 标签页，查看当前周期套餐额度消耗情况。

**说明：**

**额度刷新规则：**套餐额度在订阅月的周期内耗尽后，不会消耗其他资源包或账户余额，需要等待下一个订阅月自动恢复额度。您也可以选择升级到更高等级套餐享有更充裕的 Token 配额。

1.1 在**剩余额度**版块查看套餐额度整体消耗情况。

![](https://qcloudimg.tencent-cloud.cn/image/document/1d46fdef36a812ecfccbb2cd324f124c.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/1d46fdef36a812ecfccbb2cd324f124c.png)

1.2 在页面下方的用量详情版块查看**每日 Token 总用量**、**分钟级输入 / 输出 Token 用量**、**请求维度 Token 用量。**

![](https://qcloudimg.tencent-cloud.cn/image/document/0986fe8a556af4614ed887c95ccd2400.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/0986fe8a556af4614ed887c95ccd2400.png)

### **2. 套餐升配**

**说明：**

Token Plan 套餐仅支持套餐升配，不支持套餐降配操作。

升配套餐的费用 = 新套餐费用 − 原套餐费用（补差价）。

升配后套餐 Token 剩余量 = 新套餐总 Token 量 - 原套餐 Token 使用量。

套餐升配成功后：

套餐的 API Key 保持一样。

套餐到期时间跟原套餐保持一样，例如：Lite 套餐是 2026-04-23 到期，升级到 Standard 套餐也是 2026-04-23 到期。

2.1 在**大模型服务平台 TokenHub >** [**Token Plan**](https://console.cloud.tencent.com/tokenhub/tokenplan) **> 通用 Token Plan / Hy Token Plan** 标签页，单击**升配**，进行套餐升配。

2.2 选择要升配的目标套餐名称，升级到更高等级套餐以获得更多 Token 量。

## 步骤六（可选）：API Key 管理

**注意：**

**通用 Token Plan** 和 **Hy Token Plan** 两个套餐共用同一个 API Key。在**通用 Token Plan** 和 **Hy Token Plan 页面上对** API Key 的生成、重置、删除都会影响另一个套餐。

### **1. 复制** API Key

在**大模型服务平台 TokenHub >** [**Token Plan**](https://console.cloud.tencent.com/tokenhub/tokenplan) **> 通用 Token Plan / Hy Token Plan** 标签页，点击**复制**即可获得 API Key。

### **2. 重置** API Key

在**大模型服务平台 TokenHub >** [**Token Plan**](https://console.cloud.tencent.com/tokenhub/tokenplan) **> 通用 Token Plan / Hy Token Plan** 标签页，单击**重置**即可重新生成 API Key。

**注意：**

Token Plan 个人版套餐（通用 / Hy Token Plan）**共用同一个 API Key**，重置后将导致旧 API Key 将于 5 分钟内永久失效，所有套餐的实时 API 调用会立即中断，直至您将新 API Key 配置到所有调用端，请谨慎操作。

### **3. 删除 API Key**

在**大模型服务平台 TokenHub >** [**Token Plan**](https://console.cloud.tencent.com/tokenhub/tokenplan) **> 通用 Token Plan / Hy Token Plan** 标签页，单击**删除**，删除 API Key。

**注意：**

Token Plan 个人版套餐（通用 / Hy Token Plan）共用同一个 API Key，删除后将导致旧 API Key 将立即永久失效并且无法恢复，所有套餐的实时 API 调用会立即中断，请谨慎操作。

## 步骤七（可选）：套餐续费

**警告：**

请您在 Token Plan 套餐到期前完成续费操作，**套餐到期后将无法进行续费**，套餐将失效，**API Key 也会失效**。

### 续费规则

套餐续费是指续订下一订阅月的套餐，续费完成后，新的额度将在**下个订阅月**生效：

若本订阅月额度未用尽：剩余额度可继续使用至本订阅月结束，下个订阅月自动重置为新的额度。

若本订阅月额度已用尽：**续费操作不会重置本订阅月的额度**，新的额度需等待下个订阅月生效。

**示例如下：**用户购买 Standard 套餐，本订阅月（2026-03-23～2026-04-23）Token 总额度 1 亿。用户为下个订阅月（2026-04-23～2026-05-23）续费，不同场景可用额度说明如下：

| **场景** | **本月额度消耗情况** | **可用额度说明** |
| --- | --- | --- |
| 本订阅月额度未用尽 | 假如本订阅月（2026-03-23～2026-04-23）已用 0.5 亿。 | 本订阅月（2026-03-23～2026-04-23）剩余可用额度 0.5 亿。  下个订阅月（2026-04-23～2026-05-23）可用额度 1 亿。 |
| 若本订阅月额度已用尽 | 假如本订阅月（2026-03-23～2026-04-23）已用 1 亿。 | 本订阅月（2026-03-23～2026-04-23）剩余可用额度 0。  下个订阅月（2026-04-23～2026-05-23）可用额度 1 亿。 |

### 续费方式

Token Plan 支持**手动续费**和**自动续费**两种方式。具体说明如下：

**手动续费**：套餐自购买到到期前，您可以在任意时间为套餐手动续费。

在**大模型服务平台 TokenHub >** [**Token Plan**](https://console.cloud.tencent.com/tokenhub/tokenplan)页面，单击**立即续费。**

![](https://qcloudimg.tencent-cloud.cn/image/document/4de78f855b9d7dc62df62d26cadcf4c9.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/4de78f855b9d7dc62df62d26cadcf4c9.png)

确认续费周期，单击**续费**，即可完成操作。

![](https://qcloudimg.tencent-cloud.cn/image/document/416c51f1ebc427133bec32e3a5742c0d.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/416c51f1ebc427133bec32e3a5742c0d.png)

**自动续费**：在**大模型服务平台 TokenHub >** [**Token Plan**](https://console.cloud.tencent.com/tokenhub/tokenplan) 页面，单击**开启**，开启自动续费。套餐开启自动续费后，在账户余额充足的情况下，套餐到期前一天会自动执行续费。自动续费可以减少手动续费的管理成本，避免因忘记手动续费而导致 API Key 失效。

![](https://qcloudimg.tencent-cloud.cn/image/document/e9e335a086959eeb211cad7fd6436204.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/e9e335a086959eeb211cad7fd6436204.png)

## 常见错误码

<table><colgroup><col/><col/><col/><col/></colgroup><tbody><tr><td colspan="1" rowspan="1"><div><b>错误码</b></div></td><td colspan="1" rowspan="1"><div><b>错误信息</b></div></td><td colspan="1" rowspan="1"><div><b>可能原因</b></div></td><td colspan="1" rowspan="1"><div><b>解决方法</b></div></td></tr><tr><td colspan="1" rowspan="1"><div>401</div></td><td colspan="1" rowspan="1"><div>unauthorized</div></td><td colspan="1" rowspan="1"><div>URL 或者 API Key 配置错误</div></td><td colspan="1" rowspan="1"><div>1.<!-- --> 确认 URL 是 <a href="https://cloud.tencent.com/document/product/1823/130119#e1c62985-ad37-4de9-bafd-2cde1ded2e22">Token Plan 的 URL</a>。</div><div>2.<!-- --> 确认 API Key 根据 <a href="https://cloud.tencent.com/document/product/1823/130119#ac6f544e-6de6-46b7-8709-36d777248b34">API Key 获取指引</a> 正确获取。</div><div>3.<!-- --> 参考 <a href="https://cloud.tencent.com/document/product/1823/130061">龙虾工具</a>、<a href="https://cloud.tencent.com/document/product/1823/130067">编程工具</a>指引，确认 URL 和 API Key 配置正确。</div></td></tr><tr><td><div>429</div></td><td colspan="1" rowspan="1"><div>tpm rate limit exceeded</div></td><td colspan="1" rowspan="1"><div>系统负载高触发限流</div></td><td colspan="1" rowspan="1"><div>请重试 1-2 次或者切换其他模型。</div></td></tr><tr><td colspan="1" rowspan="1"><div>20033</div></td><td colspan="1" rowspan="1"><div>invalid model</div></td><td colspan="1" rowspan="1"><div>模型名称配置错误</div></td><td colspan="1" rowspan="1"><div>根据您订阅的套餐，检查模型配置是否正确：</div><div>﻿<a href="https://cloud.tencent.com/document/product/1823/130060#b6fdbed0-897c-475d-a9a1-f9af922027c4">通用 Token Plan 可用模型列表</a>﻿</div><div>﻿<a href="https://cloud.tencent.com/document/product/1823/130060#b145766a-c747-42eb-89c2-a04463d20cc5">Hy Token Plan 可用模型列表</a>﻿</div></td></tr><tr><td colspan="1" rowspan="1"><div>20059</div></td><td colspan="1" rowspan="1"><div>Input length too long</div></td><td colspan="1" rowspan="1"><div>输入长度超出了允许范围</div></td><td colspan="1" rowspan="1"><div>可通过新建会话解决报错。</div></td></tr><tr><td colspan="1" rowspan="1"><div>20097</div></td><td colspan="1" rowspan="1"><div>month allocated quota  exceeded</div></td><td colspan="1" rowspan="1"><div>每个订阅月请求额度已用完</div></td><td colspan="1" rowspan="1"><div>等待至下个订阅月的同一时刻（订阅时刻）额度重置，或升级至更高级套餐。</div></td></tr></tbody></table>

## 常见问题

详情请参见 [Token Plan 常见问题](https://cloud.tencent.com/document/product/1823/130076)。
