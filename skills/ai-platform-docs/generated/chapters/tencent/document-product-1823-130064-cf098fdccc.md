<!-- Official source: https://cloud.tencent.com/document/product/1823/130064 -->
<!-- Source SHA-256: a05c0e14a5b4d1778fc82c91e99508cb9014882177b6bcee83e1c2bf902df7bb -->

# WorkBuddy

官方来源：https://cloud.tencent.com/document/product/1823/130064
最近更新时间：2026-05-20 14:29:30

WorkBuddy 是腾讯云推出的全场景桌面 AI 智能体，适配 QQ / 企微生态，支持本地操作电脑、多模型切换，以 Token 配额套餐模式提供商业化服务，兼顾个人与团队使用。本文介绍如何在 WorkBuddy 中配置与使用腾讯云大模型 Token Plan。

## 前置条件

在开始配置前，请确保您已完成以下准备工作：

1. [订阅 Token Plan 套餐](https://cloud.tencent.com/document/product/1823/130119#bdc49d9b-f68d-4b79-bb5a-0aa694f2624a)。

2. [获取 API Key 和 模型列表](https://cloud.tencent.com/document/product/1823/130119#ac63b2c4-a2da-4cec-a551-6a9aef1ebb75)。

## 操作步骤

请根据您的实际操作系统，参考 WorkBuddy 官网文档安装 WorkBuddy，随后配置 Token Plan。

### 步骤一：安装 WorkBuddy

如果您使用 Mac 系统，请参考 [Mac 系统安装指南](https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Installation-Mac-Guide) 进行安装。

如果您使用 Windows 系统，请参考 [Windows 系统安装指南](https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Installation-Win-Guide) 进行安装。

### 步骤二：启动 WorkBuddy，配置自定义模型

启动 WorkBuddy，在对话界面底部找到模型切换入口，单击 “**+配置自定义模型**”。

**说明：**

WorkBuddy 需要升级到 v4.22.15。

![](https://qcloudimg.tencent-cloud.cn/image/document/c1dcfd2f28c4ac7fcc047f0f382199c7.png)

### 步骤三：选择模型提供商

在**添加模型**页面，根据您购买的套餐类型，选择“**腾讯云 Token Plan / 通用 Token Plan（个人版）**”或者“**腾讯云 Token Plan / Hy Token Plan（个人版）**”。

![](https://qcloudimg.tencent-cloud.cn/image/document/c8e78630ff8ca342dfc0f1074069edc3.png)

### 步骤四：配置 API Key 和模型

请配置完成以下内容后，单击**保存**，等待配置生效。

| 配置项 | 填写说明 |
| --- | --- |
| API Key | 填写您在腾讯云控制台获取的 API Key，请参见 [获取 API Key](https://cloud.tencent.com/document/product/1823/130119#ac6f544e-6de6-46b7-8709-36d777248b34)。 |
| 模型名称 | 在下拉框选择套餐支持的模型名称 |

**配置示例**（以 Hy Token Plan 为例）：

![](https://qcloudimg.tencent-cloud.cn/image/document/c1902f07f5a335e0f7ec8afeaf52b98c.png)

### 步骤五：切换到自定义模型对话

在 WorkBuddy 对话框选择并切换到上述步骤配置好的自定义模型，开始对话。

![](https://qcloudimg.tencent-cloud.cn/image/document/755945e35c847057dbd79f9a61b40de5.png)
