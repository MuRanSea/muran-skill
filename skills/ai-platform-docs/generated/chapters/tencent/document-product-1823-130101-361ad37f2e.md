<!-- Official source: https://cloud.tencent.com/document/product/1823/130101 -->
<!-- Source SHA-256: ed9ff84762391d7719fdee3a05feac5d6835f43864e23285039c4fe1f0725d2d -->

# Kilo CLI

官方来源：https://cloud.tencent.com/document/product/1823/130101
最近更新时间：2026-04-03 16:27:22

Kilo CLI 是 Kilo Code 全栈式 AI 编程代理平台的命令行形态。本文介绍如何在 Kilo CLI 中配置与使用腾讯云大模型 Coding Plan。

## 前置条件

在开始配置前，请确保您已订阅 Coding Plan 套餐并获取 API Key，可参见 [Coding Plan 概述](https://cloud.tencent.com/document/product/1823/130092)。

## 安装 Kilo CLI

在终端执行如下命令安装 Kilo CLI。

```bash
npm install -g @kilocode/cli
```

安装完成后，您可以执行如下命令检查，输出版本号则表示安装成功。

```bash
kilo --version
```

## 配置 Coding Plan

1. 打开 Kilo CLI 的配置文件，配置文件路径如下：

macOS/Linux：`~/.config/kilo/config.json`。

Windows：`C:\\Users\\<用户名>\\.config\\kilo\\config.json`。

2. 在配置文件中，复制粘贴如下配置，并保存。

**注意：**

请您将代码中的 <USER\_API\_KEY> 替换为 Coding Plan 专属的 API Key，将<MODEL\_NAME> 替换为 Coding Plan 支持的 [Model Name](https://cloud.tencent.com/document/product/1823/130092#540d21b1-f168-4435-8784-2e8d26331f65)。

```json
{
  "$schema": "https://kilo.ai/config.json",
  "provider": {
    "lkeap": {
      "npm": "@ai-sdk/anthropic",
      "name": "Lkeap Coding Plan",
      "options": {
        "baseURL": "https://api.lkeap.cloud.tencent.com/coding/anthropic/v1",
        "apiKey": "<USER_API_KEY>"
      },
      "models": {
        "glm-5": {
          "name": "<MODEL_NAME>",
          "options": {
            "thinking": {
              "type": "enabled",
              "budgetTokens": 1024
            }
          }
        }
      }
    }
  }
}
```

## 使用 Kilo CLI

配置完成后执行如下命令启动 Kilo CLI。

```bash
kilo
```

输入`/models`，选择 Lkeap Coding Plan 分组下的模型。
