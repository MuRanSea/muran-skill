<!-- Official source: https://cloud.tencent.com/document/product/1823/131063 -->
<!-- Source SHA-256: e505230f21fae23f907b28ca9d29c4c1b981ddca3745d08fd67a0cd6fba5e7b1 -->

# QClaw

官方来源：https://cloud.tencent.com/document/product/1823/131063
最近更新时间：2026-10-22 10:29:00

QClaw 是腾讯电脑管家基于 OpenClaw 开源生态打造的本地化 AI Agent 助手，被大家亲切称为 “小龙虾 AI”。它无需复杂配置，三步即可上手，自带安全防护；支持微信直连绑定，无论身处何地，只需通过微信发送指令，即可让电脑自动完成报表处理、文件传输、文档编辑等任务，数据安全不出本地，适用于办公、创作、开发等多类场景。

本文介绍如何在 QClaw 中配置与使用腾讯云大模型 Token Plan。

## 前置条件

在开始配置前，请确保您已完成以下准备工作：

[订阅 Token Plan 套餐](https://cloud.tencent.com/document/product/1823/130119#bdc49d9b-f68d-4b79-bb5a-0aa694f2624a)。

[获取 API Key 和 模型列表](https://cloud.tencent.com/document/product/1823/130119#ac63b2c4-a2da-4cec-a551-6a9aef1ebb75)。

## 操作步骤

### 步骤一：启动 QClaw，配置自定义模型

1. 启动 QClaw。

2. 选择对话框下方的模型配置，单击“自定义大模型”。如下图所示：

![](https://qcloudimg.tencent-cloud.cn/image/document/cc1558cb719a45392f19ee17ffa626e3.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/cc1558cb719a45392f19ee17ffa626e3.png)

3. 在**模型 API** 标签页，单击**自定义配置**。如下图所示：

![](https://qcloudimg.tencent-cloud.cn/image/document/b315c0d3c937608c43d59db452ee0380.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/b315c0d3c937608c43d59db452ee0380.png)

### 步骤二：配置接口地址、API 协议类型、API Key 和模型

请配置完成以下内容后，单击**确定**，等待配置生效。

| 配置项 | 填写说明 |
| --- | --- |
| 接口地址 | https://tokenhub.tencentmaas.com/plan/v3（直接复制使用） |
| API 协议类型 | 选择 “OpenAI 兼容协议”。 |
| API Key | 填写您在腾讯云控制台获取的 API Key，请参见 [获取 API Key](https://cloud.tencent.com/document/product/1823/130119#ac6f544e-6de6-46b7-8709-36d777248b34)。 |
| 模型名称 | 根据您购买的套餐类型，填写您套餐支持的 Model ID。  如果您购买通用 Token Plan 套餐：请参见 [可用模型](https://cloud.tencent.com/document/product/1823/130060#b6fdbed0-897c-475d-a9a1-f9af922027c4)，选择具体的 **Model ID** 配置。  如果您购买 Hy Token Plan 套餐：请参见 [可用模型](https://cloud.tencent.com/document/product/1823/130060#b145766a-c747-42eb-89c2-a04463d20cc5)，选择具体的 **Model ID** 配置。 |

**说明：**

配置模型名称时，请注意填入套餐中的 **Model ID** 的值。

每个模型都需要**单独配置**接口地址、API Key 和模型名称并**保存**。

### 步骤三：切换到自定义模型对话

返回对话界面，切换到上述步骤配置好的自定义模型，即可开始对话。

![](https://qcloudimg.tencent-cloud.cn/image/document/26aa067e99d3e96c01136fcf741fbf10.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/26aa067e99d3e96c01136fcf741fbf10.png)

##
