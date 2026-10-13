<!-- Official source: https://cloud.tencent.com/document/product/1823/130673 -->
<!-- Source SHA-256: 6b596056e1a1c646887c0a042606554c649496d0f52100a4b5147b257507cea5 -->

# WorkBuddy

官方来源：https://cloud.tencent.com/document/product/1823/130673
最近更新时间：2026-05-20 14:29:30

WorkBuddy 是腾讯云推出的全场景桌面 AI 智能体，适配 QQ / 企微生态，支持本地操作电脑、多模型切换，以 Token 配额套餐模式提供商业化服务，兼顾个人与团队使用。本文介绍如何在 WorkBuddy 中配置与使用腾讯云大模型 Token Plan 企业版。

## 前置条件

在开始配置前，确保您已完成以下准备工作：

1. [订阅 Token Plan 企业版套餐](https://cloud.tencent.com/document/product/1823/130660#9bad146b-59b9-463a-b9d9-4c21a823f8a5)。

2. [获取模型配置](https://cloud.tencent.com/document/product/1823/130660#e1afdc13-96a1-46ac-b648-fa94ce3a3e7f)。

3. [获取 API Key](https://cloud.tencent.com/document/product/1823/130660#c517dcb2-4a6d-4fbc-9793-a6fc05467143)。

## 操作步骤

请根据您的实际操作系统，参考 WorkBuddy 官网文档安装 WorkBuddy，随后配置 Token Plan 企业版。

### 步骤一：安装 WorkBuddy

如果您使用 Mac 系统，请参考 [Mac 系统安装指南](https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Installation-Mac-Guide) 进行安装。

如果您使用 Windows 系统，请参考 [Windows 系统安装指南](https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Installation-Win-Guide) 进行安装。

### 步骤二：启动 WorkBuddy，配置自定义模型

启动 WorkBuddy，在对话界面底部找到模型切换入口，单击 “**+配置自定义模型**”。

**说明：**

WorkBuddy 需要升级到 v4.22.15。

![](https://qcloudimg.tencent-cloud.cn/image/document/185670aca66b3655fec17ed7846dac42.png)

### 步骤三：选择模型提供商

在**添加模型**页面，根据您购买的套餐类型，选择“**腾讯云 Token Plan / Token Plan 企业版专业套餐**”或者“**腾讯云 Token Plan / Token Plan 企业版轻享套餐**”。

![](https://qcloudimg.tencent-cloud.cn/image/document/f2ac6ed5cf2fc2f70dd3c5857c319a38.png)

### 步骤四：配置接口地址、API Key 和模型

请根据您购买的套餐，配置以下内容，并单击**保存。**

**API Key**：请参见 [获取 API Key](https://cloud.tencent.com/document/product/1823/130660#c517dcb2-4a6d-4fbc-9793-a6fc05467143)。

**模型名称**：选择套餐支持的模型。

配置示例如下图所示，本文以“**腾讯云 Token Plan / Token Plan 企业版专业套餐**” 为例：

![](https://qcloudimg.tencent-cloud.cn/image/document/070878bf1bc4b03324f1bf420fab8cc2.png)

### 步骤五：切换到自定义模型对话

在 WorkBuddy 对话框选择并切换到上述步骤配置好的自定义模型，开始对话。

![](https://qcloudimg.tencent-cloud.cn/image/document/0f576c3c5276c9e6ee84d305087cc381.png)
