<!-- Official source: https://cloud.tencent.com/document/product/1823/132296 -->
<!-- Source SHA-256: 2cd040f86d2b60291eec8ac9b408ae51810b4bd3c932a0181c09fb34858e72cd -->

# TRAE

官方来源：https://cloud.tencent.com/document/product/1823/132296
最近更新时间：2026-10-22 10:29:00

TRAE IDE 是一款深度融合 AI 能力的开发工具，提供从代码编写、项目理解、调试运行到变更管理的完整开发体验。本文介绍如何在 TRAE 中配置与使用腾讯云大模型 Token Plan。

## 前置条件

在开始配置前，请确保您已完成以下准备工作：

1. [订阅 Token Plan 套餐](https://cloud.tencent.com/document/product/1823/130119#bdc49d9b-f68d-4b79-bb5a-0aa694f2624a)。

2. [获取 API Key](https://cloud.tencent.com/document/product/1823/130119#ac6f544e-6de6-46b7-8709-36d777248b34)。

## 操作步骤

### 步骤一：进入设置中心添加模型

1. 选择个人用户入口登录后，点击界面右上角的设置图标，进入设置中心。

2. 在左侧导航栏中，选择**模型**，进入模型管理页面。

3. 点击 **+ 添加模型**，打开添加模型窗口。

4. 在添加模型窗口，选择**自定义配置**。

![](https://qcloudimg.tencent-cloud.cn/image/document/dd8f87c26164b80601e516fb5513053a.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/dd8f87c26164b80601e516fb5513053a.png)

### 步骤二：在自定义配置板块配置模型

配置以下内容，并单击**添加模型。**

1. **API 格式**：选择 **OpenAI Chat Completions 格式。**

2. **自定义请求地址**：`https://tokenhub.tencentmaas.com/plan/v3`。

3. **模型 ID**：根据您购买的套餐，填入 [套餐支持的模型 ID](https://cloud.tencent.com/document/product/1823/130119)。

如果您购买通用 Token Plan 套餐：请参见 [可用模型](https://cloud.tencent.com/document/product/1823/130060#b6fdbed0-897c-475d-a9a1-f9af922027c4)，选择具体的 **Model ID** 配置。

如果您购买 Hy Token Plan 套餐：请参见 [可用模型](https://cloud.tencent.com/document/product/1823/130060#b145766a-c747-42eb-89c2-a04463d20cc5)，选择具体的 **Model ID** 配置。

4. **API 密钥**：从套餐中 [获取 API Key](https://cloud.tencent.com/document/product/1823/130119#ac6f544e-6de6-46b7-8709-36d777248b34) 并填入。

### 步骤三：使用 TRAE

1. 在 AI 对话输入框的右下角，单击当前模型名称；若显示为 **Auto**，点击关闭。

![](https://qcloudimg.tencent-cloud.cn/image/document/3b4fb93559f1482a0f6315026417dc62.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/3b4fb93559f1482a0f6315026417dc62.png)

2. 在模型列表中，找到自定义模型，并选择已经配置好的模型。

![](https://qcloudimg.tencent-cloud.cn/image/document/e98f463240750bbaf08bbabb0680296e.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/e98f463240750bbaf08bbabb0680296e.png)

3. 选定模型后，即可使用 TRAE 进行开发任务。
