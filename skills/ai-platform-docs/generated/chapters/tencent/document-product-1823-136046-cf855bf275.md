<!-- Official source: https://cloud.tencent.com/document/product/1823/136046 -->
<!-- Source SHA-256: a09968253daf23298271a0bd638ee36515f49b874b6dafd2f5c01992d6a9bc86 -->

# DeepSeek Harness

官方来源：https://cloud.tencent.com/document/product/1823/136046
最近更新时间：2026-10-22 10:29:00

DeepSeek Harness 是 DeepSeek AI 开发的一套用来构建、运行和扩展智能体的应用框架，采用“一切皆插件”的架构。本文介绍如何在 DeepSeek Harness 中配置与使用腾讯云大模型 Token Plan 个人版。

## 前置条件

在开始配置前，请确保您已完成以下准备工作：

[订阅 Token Plan 套餐](https://cloud.tencent.com/document/product/1823/130119#bdc49d9b-f68d-4b79-bb5a-0aa694f2624a)。

[获取 API Key 和模型列表](https://cloud.tencent.com/document/product/1823/130119#ac63b2c4-a2da-4cec-a551-6a9aef1ebb75)。

已安装 Node.js（建议使用 LTS 版本）。

## 操作步骤

1. 在终端执行以下命令，下载 DeepSeek Harness 并启动其 Web UI。

```java
npx @deepseek-ai/dsh web
```

![](https://qcloudimg.tencent-cloud.cn/image/document/582856d4d4e25bc6fa28059a93524a69.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/582856d4d4e25bc6fa28059a93524a69.png)

2. 在浏览器打开命令输出的访问地址。默认地址为 `http://127.0.0.1:3080`。

3. 在 DeepSeek Harness Web UI 中，单击左下角**设置**。

![](https://qcloudimg.tencent-cloud.cn/image/document/2c9b88ee699936be76654570f89dafbb.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/2c9b88ee699936be76654570f89dafbb.png)

4. 在左侧导航栏选择**模型**，单击**添加自定义提供方**，按下面信息填写完成提供方的创建。

| 配置项 | 填写说明 |
| --- | --- |
| Provider ID | 自定义设置，后续如需重命名则需要添加新的提供方，并删除旧的提供方。 |
| 显式名称 | 自定义设置 |
| API 协议、API 地址 | openai-completions：`https://tokenhub.tencentmaas.com/plan/v3`  openai-responses：`https://tokenhub.tencentmaas.com/plan/v3`  anthropic-messages：`https://tokenhub.tencentmaas.com/plan/anthropic` |
| API 密钥 | 填写您在腾讯云控制台获取的 API Key，请参见 [获取 API Key](https://cloud.tencent.com/document/product/1823/130119#ac6f544e-6de6-46b7-8709-36d777248b34)。 |
| 模型目录 | 单击**添加模型**，并根据您购买的套餐类型，填写您套餐支持的 Model ID。  如果您购买通用 Token Plan 套餐：请参见 [可用模型](https://cloud.tencent.com/document/product/1823/130060#b6fdbed0-897c-475d-a9a1-f9af922027c4)，选择具体的 **Model ID** 配置。  如果您购买 Hy Token Plan 套餐：请参见 [可用模型](https://cloud.tencent.com/document/product/1823/130060#b145766a-c747-42eb-89c2-a04463d20cc5)，选择具体的 **Model ID** 配置。 |

5. 请配置完成以上内容后，单击**创建提供方**，等待配置生效。

## 使用 DeepSeek Harness

1. 在页面中点击**选择一个工作区开始**，添加您启动 dsh 时所在的项目目录。选中工作区后，会话输入框才可用。

2. 在输入框右下角，选择要使用的模型。

3. 在输入框输入需求即可开始使用 DeepSeek Harness。

![](https://qcloudimg.tencent-cloud.cn/image/document/53721a17e3899d30039a800c6afaf05e.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/53721a17e3899d30039a800c6afaf05e.png)
