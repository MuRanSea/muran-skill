<!-- Official source: https://cloud.tencent.com/document/product/1823/130065 -->
<!-- Source SHA-256: e2f0c8f67fee551633e0cb6668d2a72738170e1f0f363dbba3edd2c808952566 -->

# CoPaw

官方来源：https://cloud.tencent.com/document/product/1823/130065
最近更新时间：2026-10-23 15:47:30

CoPaw 是阿里云通义实验室推出的开源国产 AI 智能体。CoPaw 支持通过“自定义提供商”功能接入任何兼容 OpenAI 协议的第三方模型服务。通过以下配置，可将腾讯云 Token Plan 的模型接入 CoPaw。

本文介绍如何在 CoPaw 中配置与使用腾讯云大模型 Token Plan。

## 前置条件

在开始配置前，请确保您已完成以下准备工作：

1. [订阅 Token Plan 套餐](https://cloud.tencent.com/document/product/1823/130119#bdc49d9b-f68d-4b79-bb5a-0aa694f2624a)。

2. [获取 API Key](https://cloud.tencent.com/document/product/1823/130119#ac6f544e-6de6-46b7-8709-36d777248b34)。

## 操作步骤

### 步骤一：启动 CoPaw 并进入模型配置页面

启动 CoPaw 应用后，在浏览器中访问 `http://127.0.0.1:8088`（默认端口），单击左侧导航栏的**设置** > **模型**进入模型配置页面。

### 步骤二：添加自定义提供商

在模型配置页面中，单击**添加提供商 > 设置**，填写以下信息，然后单击**创建。**

| 参数 | 值 |
| --- | --- |
| 提供商 ID | `tencent-token-plan` |
| 显示名称 | 腾讯云 Token Plan |

创建成功后，您可以在页面上看到新添加的提供商卡片。

### 步骤三：配置提供商

单击新添加的提供商卡片上的**设置**，填写以下连接参数：

| 参数 | 值 |
| --- | --- |
| Base URL | `https://tokenhub.tencentmaas.com/plan/v3` |
| API Key | 购买 Token Plan 后获取的专属 API Key |

填写完成后保存设置。

### 步骤四：添加模型

单击自定义提供商卡片中的**模型**，在**模型 ID** 输入框中填写**模型 ID**，单击**添加模型**。

根据您购买的套餐类型，填写您套餐支持的 Model ID。

如果您购买通用 Token Plan 套餐：请参见 [可用模型](https://cloud.tencent.com/document/product/1823/130060#b6fdbed0-897c-475d-a9a1-f9af922027c4)，选择具体的 **Model ID** 配置。

如果您购买 Hy Token Plan 套餐：请参见 [可用模型](https://cloud.tencent.com/document/product/1823/130060#b145766a-c747-42eb-89c2-a04463d20cc5)，选择具体的 **Model ID** 配置。

### 步骤五：选择模型并使用

在页面上方的 **LLM 配置**区域，将提供商选择为刚添加的自定义提供商，选择对应的模型，单击**保存**即可开始对话。
