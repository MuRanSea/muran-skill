<!-- Official source: https://cloud.tencent.com/document/product/1823/130098 -->
<!-- Source SHA-256: 17b8786629d91747e5934588e8c7734b866834def6f7157e2b034ad89f3fe44e -->

# Codex

官方来源：https://cloud.tencent.com/document/product/1823/130098
最近更新时间：2026-06-26 18:12:00

Codex 是由 OpenAI 开发的新一代 AI 智能编程助手，基于 GPT 架构打造的强大代码生成引擎。Codex 通过深度学习技术，能够理解自然语言并转换为高质量代码，支持 Python、JavaScript、Java 等多种编程语言。本文介绍如何在 Codex 中配置与使用腾讯云大模型 Coding Plan。

## 前置条件

在开始配置前，请确保您已订阅 Coding Plan 套餐并获取 API Key，可参见 [Coding Plan 概述](https://cloud.tencent.com/document/product/1823/130092)。

## 安装 Codex

**注意：**

新版本 Codex 采用 Responses API 接口，暂不支持 Chat/Completions API，只有 **0.80.0 及以下版本**才支持（详情请参见 [Codex 官方说明](https://github.com/openai/codex/discussions/7782)）。请安装支持 Chat/Completions API 的旧版本 Codex，例如：0.80.0 版本。

在终端中执行以下命令安装 Codex。

```bash
npm install -g @openai/codex@0.80.0
```

在终端中执行以下命令，若输出版本号，则表示安装成功。

```bash
codex --version
```

## 配置 Coding Plan

完整复制以下内容并粘贴到 Codex 配置文件 ~/.codex/config.toml 中。

1. 找到 Codex 的配置文件，配置文件路径如下，配置文件不存在时新建即可。

Windows：`C:\\Users\\<用户名>\\.codex\\config.toml`。

macOS/Linux：`~/.codex/config.toml`。

2. 复制以下内容粘贴到 config.toml 配置文件中，将 <MODEL\_NAME> 替换为 Coding Plan 支持的 [Model Name](https://cloud.tencent.com/document/product/1823/130092#540d21b1-f168-4435-8784-2e8d26331f65)。

```bash
model_provider = "Lkeap_Coding_Plan"
model = "<MODEL_NAME>"
[model_providers.Lkeap_Coding_Plan]
name = "Lkeap_Coding_Plan"
base_url = "https://api.lkeap.cloud.tencent.com/coding/v3"
env_key = "CODING_API_KEY"
wire_api = "chat"
```

### 配置环境变量

在命令行中将 CODING\_API\_KEY 环境变量设置为 Coding Plan 专属的 API Key。

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
echo 'export CODING_API_KEY="USER_API_KEY"' >> ~/.zshrc

#配置生效
source ~/.zshrc
```

```bash
echo 'export CODING_API_KEY="USER_API_KEY"' >> ~/.bash_profile

#配置生效
source ~/.bash_profile
```

CMD

PowerShell

```bash
# 用您的Coding Plan API Key 替换 USER_API_KEY
set CODING_API_KEY "USER_API_KEY"

#新开 CMD 窗口检查是否生效
echo %CODING_API_KEY%

```

```bash
# 用Coding Plan的 API Key 替换 USER_API_KEY
[Environment]::SetEnvironmentVariable("CODING_API_KEY", "USER_API_KEY", [EnvironmentVariableTarget]::User)

#新开一个窗口验证是否生效
echo $CODING_API_KEY
```

## 使用 Codex

1. 在终端执行如下命令并回车，启动 Codex 工具。

```bash
codex
```

2. 选择 **Skip** 跳过。

![](https://qcloudimg.tencent-cloud.cn/image/document/14fcd6bfd9af13a305e701118a5b93d2.png)

3. 您可以输入问题或指令，开始对话。

![](https://qcloudimg.tencent-cloud.cn/image/document/389157388b446f95575d1a828f9957fe.png)
