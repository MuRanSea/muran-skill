<!-- Official source: https://cloud.tencent.com/document/product/1823/131062 -->
<!-- Source SHA-256: 0fbf1c3ff85151b450a29a91dbf766c319aa2b7357199dd97709d0fb3bcb03e6 -->

# QClaw

官方来源：https://cloud.tencent.com/document/product/1823/131062
最近更新时间：2026-09-03 14:36:30

QClaw 是腾讯电脑管家基于 OpenClaw 开源生态打造的本地化 AI Agent 助手，被大家亲切称为 “小龙虾 AI”。它无需复杂配置，三步即可上手，自带安全防护；支持微信直连绑定，无论你身处何地，通过微信发送指令，就能让电脑自动完成报表处理、文件传输、文档编辑等工作，数据安全不出本地，适合办公、创作、开发等多场景使用。

本文介绍如何在 QClaw 中配置与使用腾讯云大模型 Token Plan 企业版。

## 前置条件

在开始配置前，确保您已完成以下准备工作：

1. [订阅 Token Plan 企业版套餐](https://cloud.tencent.com/document/product/1823/130660#9bad146b-59b9-463a-b9d9-4c21a823f8a5)。

2. 获取模型配置：

2.1 [专业套餐模型配置](https://cloud.tencent.com/document/product/1823/130659#cde5404a-a7bb-4d53-acba-6e3b1b6b8264)；

2.2 [轻享套餐模型配置](https://cloud.tencent.com/document/product/1823/131173#b18f9f4d-fad3-49a9-a38e-2ef38854fa19)。

3. [获取 API Key](https://cloud.tencent.com/document/product/1823/130660#c517dcb2-4a6d-4fbc-9793-a6fc05467143)。

## 操作步骤

### 步骤一：启动 QClaw，配置自定义模型

1. 启动 QClaw。

2. 选择对话框下方的模型配置，单击“自定义大模型”。如下图所示：

![](https://qcloudimg.tencent-cloud.cn/image/document/d8c4476a95bee3469ed5cc05a1ec0549.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/d8c4476a95bee3469ed5cc05a1ec0549.png)

3. 在**模型 API** 标签页，单击**自定义配置**。如下图所示：

![](https://qcloudimg.tencent-cloud.cn/image/document/e707da94a02445ba154bc5f88392a02e.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/e707da94a02445ba154bc5f88392a02e.png)

### 步骤二：配置接口地址、API 协议类型、API Key 和模型

请配置完成以下内容后，单击**确定**，等待配置生效。

| 配置项 | 填写说明 |
| --- | --- |
| 接口地址 | 新加坡：`https://tokenhub-intl.tencentmaas.com/plan/v3`  广州：`https://tokenhub.tencentmaas.com/plan/v3` |
| API 协议类型 | 选择 “OpenAI 兼容协议”。 |
| API Key | 填写您的专属 API Key。 |
| 模型名称 | 根据您购买的套餐，填入套餐支持的 **Model ID**。  专业套餐：具体模型请参考 [Token Plan 企业版专业套餐](https://cloud.tencent.com/document/product/1823/130659) 中的可用模型列表。  轻享套餐：具体模型请参考 [Token Plan 企业版轻享套餐](https://cloud.tencent.com/document/product/1823/131173#b18f9f4d-fad3-49a9-a38e-2ef38854fa19) 中的可用模型列表。 |

**说明：**

配置模型名称时，请注意填入套餐中的 **Model ID** 的值。

每个模型都需要**单独配置**接口地址、API Key 和模型名称并**保存**。

### 步骤三：切换到自定义模型对话

返回对话界面，切换到上述步骤配置好的自定义模型，即可开始对话。
