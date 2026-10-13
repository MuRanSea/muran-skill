<!-- Official source: https://cloud.tencent.com/document/product/1823/130666 -->
<!-- Source SHA-256: 580aff085221dca96656ab8ed5e65b5eb6b0945fead3679f829b30ab7ce26c4e -->

# Codex

官方来源：https://cloud.tencent.com/document/product/1823/130666
最近更新时间：2026-09-14 10:35:32

Codex 是由 OpenAI 开发的新一代 AI 智能编程助手，基于 GPT 架构打造的强大代码生成引擎。Codex 通过深度学习技术，能够理解自然语言并转换为高质量代码，支持 Python、JavaScript、Java 等多种编程语言。本文介绍如何在 Codex 中配置与使用腾讯云大模型 Token Plan 企业版。

## 前置条件

在开始配置前，确保您已完成以下准备工作：

1. [订阅 Token Plan 企业版套餐](https://cloud.tencent.com/document/product/1823/130660#9bad146b-59b9-463a-b9d9-4c21a823f8a5)。

2. 获取模型配置：

2.1 [专业套餐模型配置](https://cloud.tencent.com/document/product/1823/130659#cde5404a-a7bb-4d53-acba-6e3b1b6b8264)；

2.2 [轻享套餐模型配置](https://cloud.tencent.com/document/product/1823/131173#b18f9f4d-fad3-49a9-a38e-2ef38854fa19)。

3. [获取 API Key](https://cloud.tencent.com/document/product/1823/130660#c517dcb2-4a6d-4fbc-9793-a6fc05467143)。

## 安装 Codex

Codex 通过 npm 安装，需先安装 Node.js（建议 ≥ 18）。如未安装，请访问 [Node.js 官网](https://nodejs.org/) 下载 LTS 版本。

在终端中执行以下命令安装 Codex。

```bash
npm install -g @openai/codex
```

在终端中执行以下命令，若输出版本号，则表示安装成功。

```bash
codex --version
```

## 配置 Token Plan 企业版

完整复制以下内容并粘贴到 Codex 配置文件 `~/.codex/config.toml` 中。

1. 找到 Codex 的配置文件，配置文件路径如下，配置文件不存在时新建即可。

macOS/Linux：`~/.codex/config.toml`。

Windows：`C:\\Users\\<用户名>\\.codex\\config.toml`。

2. 复制以下内容粘贴到 config.toml 配置文件中，将 <MODEL\_ID> 替换为套餐支持的模型配置。

专业套餐：具体模型请参考 [Token Plan 企业版专业套餐](https://cloud.tencent.com/document/product/1823/130659) 中的可用模型列表。

轻享套餐：具体模型请参考 [Token Plan 企业版轻享套餐](https://cloud.tencent.com/document/product/1823/131173#b18f9f4d-fad3-49a9-a38e-2ef38854fa19) 中的可用模型列表。

```bash
model_provider = "Token_Plan_Ent"
model = "<MODEL_ID>"

[model_providers.Token_Plan_Ent]
name = "Token_Plan_Ent"
base_url = "https://tokenhub.tencentmaas.com/plan/v3"
env_key = "TP_ENT_API_KEY"
wire_api = "responses"
```

### 配置环境变量

在命令行中将 TP\_ENT\_API\_KEY 环境变量设置为您的 API Key。

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
echo 'export TP_ENT_API_KEY="USER_API_KEY"' >> ~/.zshrc

#配置生效
source ~/.zshrc
```

```bash
echo 'export TP_ENT_API_KEY="USER_API_KEY"' >> ~/.bash_profile

#配置生效
source ~/.bash_profile
```

CMD

PowerShell

```bash
# 用您的 API Key 替换 USER_API_KEY
setx TP_ENT_API_KEY "USER_API_KEY"

#新开 CMD 窗口检查是否生效
echo %TP_ENT_API_KEY%
```

```bash
# 用您的 API Key 替换 USER_API_KEY
[Environment]::SetEnvironmentVariable("TP_ENT_API_KEY", "USER_API_KEY", [EnvironmentVariableTarget]::User)

#新开一个窗口验证是否生效
echo $env:TP_ENT_API_KEY
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
