<!-- Official source: https://cloud.tencent.com/document/product/1823/130670 -->
<!-- Source SHA-256: f50c02e6fe3c82ac47aa41f6f3f30856de8ea0fd3a0ecebc5a42e4515fa62aa1 -->

# Kilo Code

官方来源：https://cloud.tencent.com/document/product/1823/130670
最近更新时间：2026-09-03 14:36:30

Kilo Code 是一款开源 AI 编程助手，全场景适配您的开发工作流，无论在 IDE、终端、浏览器中，还是移动办公场景均可使用。借助深度理解代码库的 AI 能力，高效生成代码、自动化代码评审、调试问题，加速研发交付。本文介绍如何在 Kilo Code 中配置与使用腾讯云大模型 Token Plan 企业版。

## 前置条件

在开始配置前，确保您已完成以下准备工作：

1. [订阅 Token Plan 企业版套餐](https://cloud.tencent.com/document/product/1823/130660#9bad146b-59b9-463a-b9d9-4c21a823f8a5)。

2. 获取模型配置：

2.1 [专业套餐模型配置](https://cloud.tencent.com/document/product/1823/130659#cde5404a-a7bb-4d53-acba-6e3b1b6b8264)；

2.2 [轻享套餐模型配置](https://cloud.tencent.com/document/product/1823/131173#b18f9f4d-fad3-49a9-a38e-2ef38854fa19)。

3. [获取 API Key](https://cloud.tencent.com/document/product/1823/130660#c517dcb2-4a6d-4fbc-9793-a6fc05467143)。

## 安装 Kilo Code 并使用 Token Plan 企业版

在 IDE 中搜索安装 Kilo Code 插件，下面分别以 JetBrains 和 VS Code 为例展示安装配置过程。

VSCode

JetBrains

1. 打开 VSCode，在扩展市场中搜索 Kilo Code 并安装。

![](https://qcloudimg.tencent-cloud.cn/image/document/c19c0fad114f86c9d8e72f4134a53fba.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/c19c0fad114f86c9d8e72f4134a53fba.png)

2. 打开 Kilo Code，选择 **Bring my own Key**，并配置以下信息：

API Provider：**OpenAI Compatible**（Token Plan 接口兼容 OpenAI 标准）。

Base URL：

新加坡：`https://tokenhub-intl.tencentmaas.com/plan/v3`

广州：`https://tokenhub.tencentmaas.com/plan/v3`

API Key：Token Plan 专属的 API Key。

Model：根据您购买的套餐，填入套餐支持的模型 ID。

专业套餐：具体模型请参考 [Token Plan 企业版专业套餐](https://cloud.tencent.com/document/product/1823/130659) 中的可用模型列表。

轻享套餐：具体模型请参考 [Token Plan 企业版轻享套餐](https://cloud.tencent.com/document/product/1823/131173#b18f9f4d-fad3-49a9-a38e-2ef38854fa19) 中的可用模型列表。

单击 **Use custom**。

3. 配置完成后，您可以在输入框中输入需求，与模型进行交互。

![](https://qcloudimg.tencent-cloud.cn/image/document/002df8fe82c176eb31c8dd8fb0f875c9.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/002df8fe82c176eb31c8dd8fb0f875c9.png)

4. **模型切换：**您可以通过单击右上角的**设置**，在 **Model** 输入框搜索模型，选择 **Use custom** 进行切换。

1. 打开 JetBrains，在扩展市场中搜索 Kilo Code 并安装。

![](https://qcloudimg.tencent-cloud.cn/image/document/952113c3c2d7b8240e37ceac25a5baa3.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/952113c3c2d7b8240e37ceac25a5baa3.png)

2. 安装完成后重启 IDE，点击右侧图标，单击 **Bring my own Key** 进入设置界面，并配置以下信息：

API Provider：**OpenAI Compatible**（Token Plan 接口兼容 OpenAI 标准）。

Base URL：

新加坡：`https://tokenhub-intl.tencentmaas.com/plan/v3`

广州：`https://tokenhub.tencentmaas.com/plan/v3`

API Key：Token Plan 专属的 API Key。

Model：根据您购买的套餐，填入套餐支持的模型 ID。

专业套餐：具体模型请参考 [Token Plan 企业版专业套餐](https://cloud.tencent.com/document/product/1823/130659) 中的可用模型列表。

轻享套餐：具体模型请参考 [Token Plan 企业版轻享套餐](https://cloud.tencent.com/document/product/1823/131173#b18f9f4d-fad3-49a9-a38e-2ef38854fa19) 中的可用模型列表。

单击 **Use custom**。

3. 在 Kilo Code 中使用，单击右上角的**设置**，修改 Model 即可切换模型。
