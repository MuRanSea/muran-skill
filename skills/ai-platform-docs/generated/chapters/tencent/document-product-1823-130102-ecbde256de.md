<!-- Official source: https://cloud.tencent.com/document/product/1823/130102 -->
<!-- Source SHA-256: b2d51583e9ab02c6c4874b025623c4b0e55c32feed8b526ee0d23263fb9481e0 -->

# Kilo Code

官方来源：https://cloud.tencent.com/document/product/1823/130102
最近更新时间：2026-04-03 16:27:22

Kilo Code 是一款开源 AI 编程助手，全场景适配您的开发工作流，无论在 IDE、终端、浏览器中，还是移动办公场景均可使用。借助深度理解代码库的 AI 能力，高效生成代码、自动化代码评审、调试问题，加速研发交付。本文介绍如何在 Kilo Code 中配置与使用腾讯云大模型 Coding Plan。

## 前置条件

在开始配置前，请确保您已订阅 Coding Plan 套餐并获取 API Key，可参见 [Coding Plan 概述](https://cloud.tencent.com/document/product/1823/130092)。

## 安装 Kilo Code 并使用 Coding Plan

在 IDE 中搜索安装 Kilo Code 插件，下面分别以 JetBrains 和 VS Code 为例展示安装配置过程。

VSCode

JetBrains

1. 打开 VSCode，在扩展市场中搜索 Kilo Code 并安装。

![](https://qcloudimg.tencent-cloud.cn/image/document/c19c0fad114f86c9d8e72f4134a53fba.png)

2. 单击 Kilo Code 右上角的**设置**按钮，选择 **Use your own API key**，并配置以下信息：

API Provider：**OpenAI Compatible**（Coding Plan 接口兼容 OpenAI 标准）。

Base URL：`https://api.lkeap.cloud.tencent.com/coding/v3`。

API Key：Coding Plan 专属的 API Key。

Model：填写 Coding Plan 支持的 [Model Name](https://cloud.tencent.com/document/product/1823/130092#540d21b1-f168-4435-8784-2e8d26331f65)，单击 **Use custom**。

3. 配置完成后，您可以在输入框中输入需求，与模型进行交互。

![](https://qcloudimg.tencent-cloud.cn/image/document/002df8fe82c176eb31c8dd8fb0f875c9.png)

4. **模型切换：**您可以通过单击右上角的**设置**，在 **Model** 输入框搜索模型，选择 **Use custom** 进行切换。

![](https://qcloudimg.tencent-cloud.cn/image/document/a698a0af71b5bc48366996cc2ffec3ce.png)

1. 打开 JetBrains ，在扩展市场中搜索 Kilo Code 并安装，安装完成后重启 IDE 生效。

![](https://qcloudimg.tencent-cloud.cn/image/document/952113c3c2d7b8240e37ceac25a5baa3.png)

2. 安装成功后，单击 Kilo Code 右侧图标，选择 **Bring my own Key** ，并配置以下信息：

API Provider：**OpenAI Compatible**（Coding Plan 接口兼容 OpenAI 标准）。

Base URL：`https://api.lkeap.cloud.tencent.com/coding/v3`。

API Key：Coding Plan 专属的 API Key。

Model：填写 Coding Plan 支持的 [Model Name](https://cloud.tencent.com/document/product/1823/130092#540d21b1-f168-4435-8784-2e8d26331f65)，单击 **Use custom**。

![](https://qcloudimg.tencent-cloud.cn/image/document/83f073c79cf649dc376458395f247cac.png)

3. 在 Kilo Code 中使用，单击右上角的**设置**按钮，修改 Model 即可切换模型。

![](https://qcloudimg.tencent-cloud.cn/image/document/a60af9f060664fb959a63f202d021e1f.png)
