<!-- Official source: https://cloud.tencent.com/document/product/1823/130071 -->
<!-- Source SHA-256: 99d42c9f7e6f9ad6c9331eba6e3b8767d6d99e11e9a01283f7ab931b8d77c4cf -->

# Codex

官方来源：https://cloud.tencent.com/document/product/1823/130071
最近更新时间：2026-10-15 18:21:31

Codex 是由 OpenAI 开发的新一代 AI 智能编程助手，基于 GPT 架构打造的强大代码生成引擎。Codex 通过深度学习技术，能够理解自然语言并转换为高质量代码，支持 Python、JavaScript、Java 等多种编程语言。本文介绍如何在 Codex 中配置与使用腾讯云大模型 Token Plan。

## 前置条件

在开始配置前，请确保您已完成以下准备工作：

1. [订阅 Token Plan 套餐](https://cloud.tencent.com/document/product/1823/130119#bdc49d9b-f68d-4b79-bb5a-0aa694f2624a)。

2. [获取 API Key](https://cloud.tencent.com/document/product/1823/130119#ac6f544e-6de6-46b7-8709-36d777248b34)。

## 安装 Codex

请根据实际环境类型安装 Codex，详情请参见 [Codex 安装](https://developers.openai.com/codex/quickstart)。如果已安装 Codex，可跳过此步骤。

## 配置 Token Plan

完整复制以下内容并粘贴到 Codex 配置文件 `~/.codex/config.toml` 中。

1. 找到 Codex 的配置文件，配置文件路径如下，配置文件不存在时新建即可。

macOS/Linux：`~/.codex/config.toml`。

Windows：`C:\\Users\\<用户名>\\.codex\\config.toml`。

2. 复制以下内容粘贴到 config.toml 配置文件中，根据您购买的套餐类型，将 $model\_id 替换为 [套餐支持的模型 ID](https://cloud.tencent.com/document/product/1823/130119)。

如果您购买通用 Token Plan 套餐：请参见 [可用模型](https://cloud.tencent.com/document/product/1823/130060#b6fdbed0-897c-475d-a9a1-f9af922027c4)，选择具体的 **Model ID** 配置。

如果您购买 Hy Token Plan 套餐：请参见 [可用模型](https://cloud.tencent.com/document/product/1823/130060#b145766a-c747-42eb-89c2-a04463d20cc5)，选择具体的 **Model ID** 配置。

```bash
model_provider = "Tencent_Cloud_Token_Plan"
model = "$model_id"
[model_providers.Tencent_Cloud_Token_Plan]
name = "Tencent_Cloud_Token_Plan"
base_url = "https://tokenhub.tencentmaas.com/plan/v3"
env_key = "Token_Plan_API_KEY"
wire_api = "responses"
```

### 配置环境变量

在命令行中将 Token\_Plan\_API\_KEY 环境变量设置为 Token Plan 专属的 API Key。

macOS/Linux

Windows

在终端中执行以下命令，查看默认 Shell 类型。

```bash
echo $SHELL
```

根据 Shell 类型设置环境变量，命令如下：

Zsh

Bash

```bash
echo 'export Token_Plan_API_KEY="USER_API_KEY"' >> ~/.zshrc

#配置生效
source ~/.zshrc
```

```bash
echo 'export Token_Plan_API_KEY="USER_API_KEY"' >> ~/.bash_profile

#配置生效
source ~/.bash_profile
```

CMD

PowerShell

```bash
# 用您的Token Plan API Key 替换 USER_API_KEY
setx Token_Plan_API_KEY "USER_API_KEY"

#新开 CMD 窗口检查是否生效
echo %Token_Plan_API_KEY%

```

```bash
# 用 Token Plan 的 API Key 替换 USER_API_KEY
[Environment]::SetEnvironmentVariable("Token_Plan_API_KEY", "USER_API_KEY", [EnvironmentVariableTarget]::User)

#新开一个窗口验证是否生效
echo $env:Token_Plan_API_KEY
```

## 使用 Codex

1. 在终端执行如下命令并回车，启动 Codex 工具。

```bash
codex
```

2. 选择 **Skip** 跳过。

![](https://qcloudimg.tencent-cloud.cn/image/document/14fcd6bfd9af13a305e701118a5b93d2.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/14fcd6bfd9af13a305e701118a5b93d2.png)

3. 您可以输入问题或指令，开始对话。

![](https://qcloudimg.tencent-cloud.cn/image/document/389157388b446f95575d1a828f9957fe.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/389157388b446f95575d1a828f9957fe.png)
