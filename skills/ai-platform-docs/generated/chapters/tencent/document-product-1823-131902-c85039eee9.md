<!-- Official source: https://cloud.tencent.com/document/product/1823/131902 -->
<!-- Source SHA-256: 82aa37f64c02c1a6c4274949a6da106d85b0ce37780ac1c065a4aae060d960f7 -->

# WorkBuddy

官方来源：https://cloud.tencent.com/document/product/1823/131902
最近更新时间：2026-09-21 10:08:00

WorkBuddy 是腾讯云推出的全场景桌面 AI 智能体，适配 QQ / 企微生态，支持本地操作电脑、多模型切换，以 Token 配额套餐模式提供商业化服务，兼顾个人与团队使用。本文以 `hy3` 为例介绍如何在 WorkBuddy 中配置使用腾讯云 TokenHub 大模型。

## 安装 WorkBuddy

访问 [WorkBuddy 官网](https://www.codebuddy.cn/work/)，下载和安装 WorkBuddy：

如果您使用 Mac 系统，请参考 [Mac 系统安装指南](https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Installation-Mac-Guide) 进行安装。

如果您使用 Windows 系统，请参考 [Windows 系统安装指南](https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Installation-Win-Guide) 进行安装。

## 获取 API Key

1. 进入 [API Key 管理](https://console.cloud.tencent.com/tokenhub/apikey) 页面，单击**创建 API Key**。操作详情请参见 [创建 API Key](https://cloud.tencent.com/document/product/1823/130090#40882178-aaf2-48c9-8559-dffc083a79bc)。

**注意：**

需确认 Key 的**可访问范围**，如果为“限定范围”，需确保已勾选 `hy3` 。

2. 创建完成后，请您务必**复制并妥善保管 API Key**，在后续配置到工具的流程中将会使用该信息。

![](https://qcloudimg.tencent-cloud.cn/image/document/d973620716387578df90271067e311c7.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/d973620716387578df90271067e311c7.png)

## 配置 WorkBuddy

1. 启动 WorkBuddy，单击左下角账户，选择**设置**。

![](https://qcloudimg.tencent-cloud.cn/image/document/b1a8b32f329160748eb507f1d46977ee.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/b1a8b32f329160748eb507f1d46977ee.png)

2. 在左侧导航中选择**模型**，在自定义模型中，单击**添加模型**。

![](https://qcloudimg.tencent-cloud.cn/image/document/3ef5f446d37d23f6024c8d22260699ba.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/3ef5f446d37d23f6024c8d22260699ba.png)

3. 配置以下信息，单击**保存**：

3.1 在提供商中，选择**自定义 / Custom**。如下图所示：

![](https://qcloudimg.tencent-cloud.cn/image/document/6b8e57c365e20d396be857f8a3928e7b.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/6b8e57c365e20d396be857f8a3928e7b.png)

3.2 填写以下字段信息：

**接口地址**：`https://tokenhub.tencentmaas.com/v1/chat/completions`

**API Key**：填入您的 API Key。

**模型名称**：填写 `hy3`。若要配置其他模型，请将 `hy3` 替换为您实际要使用的 [模型 ID](https://cloud.tencent.com/document/product/1823/130051)（不支持自定义模型名称）。

**高级工具**：非必填，按需使用。建议勾选：工具调用、图片输入、推理模式。

![](https://qcloudimg.tencent-cloud.cn/image/document/f6897a03aeea3fbbc7acffbef8905bf5.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/f6897a03aeea3fbbc7acffbef8905bf5.png)

4. 配置完成后，在 WorkBuddy 模型选择框中选择已添加的 `hy3` 模型，即可开始对话。
