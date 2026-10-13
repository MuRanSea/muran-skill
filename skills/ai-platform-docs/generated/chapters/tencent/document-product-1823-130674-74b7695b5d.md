<!-- Official source: https://cloud.tencent.com/document/product/1823/130674 -->
<!-- Source SHA-256: efaf718881c403d22bbe411b2b61901658e32a89320d1f5dc965bd7cb8a50ff5 -->

# CoPaw

官方来源：https://cloud.tencent.com/document/product/1823/130674
最近更新时间：2026-09-03 14:36:30

CoPaw 是阿里云通义实验室推出的开源国产 AI 智能体。CoPaw 支持通过“自定义提供商”功能接入任何兼容 OpenAI 协议的第三方模型服务。通过以下配置，可将腾讯云 Token Plan 企业版的模型接入 CoPaw。

本文介绍如何在 CoPaw 中配置与使用腾讯云大模型 Token Plan 企业版。

## 前置条件

在开始配置前，确保您已完成以下准备工作：

1. [订阅 Token Plan 企业版套餐](https://cloud.tencent.com/document/product/1823/130660#9bad146b-59b9-463a-b9d9-4c21a823f8a5)。

2. 获取模型配置：

2.1 [专业套餐模型配置](https://cloud.tencent.com/document/product/1823/130659#cde5404a-a7bb-4d53-acba-6e3b1b6b8264)；

2.2 [轻享套餐模型配置](https://cloud.tencent.com/document/product/1823/131173#b18f9f4d-fad3-49a9-a38e-2ef38854fa19)。

3. [获取 API Key](https://cloud.tencent.com/document/product/1823/130660#c517dcb2-4a6d-4fbc-9793-a6fc05467143)。

## 操作步骤

### 步骤一：启动 CoPaw 并进入模型配置页面

启动 CoPaw 应用后（安装详见 [CoPaw 官网](https://qwenpaw.agentscope.io/docs/quickstart/)），在浏览器中访问 `http://127.0.0.1:8088`（默认端口），单击左侧导航栏的**设置** > **模型**进入模型配置页面。

### 步骤二：添加自定义提供商

在模型配置页面中，单击**添加提供商 > 设置**，填写以下信息，然后单击**创作。**

| 参数 | 值 |
| --- | --- |
| 提供商 ID | `tencent-token-plan-ent` |
| 显示名称 | 腾讯云 Token Plan 企业版 |

![](https://qcloudimg.tencent-cloud.cn/image/document/a32fe985ceffe66a247ea14c67c4dcc3.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/a32fe985ceffe66a247ea14c67c4dcc3.png)

创建成功后，您可以在页面上看到新添加的提供商卡片。

### 步骤三：配置提供商

单击新添加的提供商卡片上的**设置**，填写以下连接参数：

| 参数 | 值 |
| --- | --- |
| Base URL | `https://tokenhub.tencentmaas.com/plan/v3` |
| API Key | 填写专属 API Key |

填写完成后保存设置。

### 步骤四：添加模型

单击自定义提供商卡片中的**模型**，在**模型 ID** 输入框中，根据您购买的套餐，填入套餐支持的模型 ID，单击**添加模型**。

专业套餐：具体模型请参考 [Token Plan 企业版专业套餐](https://cloud.tencent.com/document/product/1823/130659) 中的可用模型列表。

轻享套餐：具体模型请参考 [Token Plan 企业版轻享套餐](https://cloud.tencent.com/document/product/1823/131173#b18f9f4d-fad3-49a9-a38e-2ef38854fa19) 中的可用模型列表。

逐一添加需要使用的模型。

### 步骤五：选择模型并使用

在页面上方的 **LLM 配置**区域，将提供商选择为刚添加的自定义提供商，选择对应的模型，单击**保存**即可开始对话。
