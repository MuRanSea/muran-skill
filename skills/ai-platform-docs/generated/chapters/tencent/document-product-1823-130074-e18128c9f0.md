<!-- Official source: https://cloud.tencent.com/document/product/1823/130074 -->
<!-- Source SHA-256: 2ba2fee4f0bb895080239384af90b911b9818f9a4e1f329e1a79b090f36e38fa -->

# Kilo CLI

官方来源：https://cloud.tencent.com/document/product/1823/130074
最近更新时间：2026-10-22 10:29:01

Kilo CLI 是 Kilo Code 全栈式 AI 编程代理平台的命令行形态。本文介绍如何在 Kilo CLI 中配置与使用腾讯云大模型 Token Plan。

## 前置条件

在开始配置前，请确保您已完成以下准备工作：

1. [订阅 Token Plan 套餐](https://cloud.tencent.com/document/product/1823/130119#bdc49d9b-f68d-4b79-bb5a-0aa694f2624a)。

2. [获取 API Key 和 模型列表](https://cloud.tencent.com/document/product/1823/130119#ac63b2c4-a2da-4cec-a551-6a9aef1ebb75)。

## 安装 Kilo CLI

在终端执行如下命令安装 Kilo CLI。

```bash
npm install -g @kilocode/cli
```

安装完成后，您可以执行如下命令检查，输出版本号则表示安装成功。

```bash
kilo --version
```

## 配置 Token Plan

1. 打开 Kilo CLI 的配置文件，配置文件路径如下：

macOS/Linux：`~/.config/kilo/config.json`。

Windows：`C:\\Users\\<用户名>\\.config\\kilo\\config.json`。

2. 在配置文件中，复制粘贴如下配置，并保存。

**注意：**

请您将代码中的 <USER\_API\_KEY> 替换为 Token Plan 专属的 API Key。下方配置已根据套餐类型预填了 `models` 列表，可按需保留所需模型。

通用 Token Plan

Hy Token Plan

```json
{
  "$schema": "https://kilo.ai/config.json",
  "provider": {
    "lkeap": {
      "npm": "@ai-sdk/anthropic",
      "name": "Tencent Token Plan",
      "options": {
        "baseURL": "https://tokenhub.tencentmaas.com/plan/anthropic/v1",
        "apiKey": "<USER_API_KEY>"
      },
      "models": {
        "tc-code-latest": { "name": "Auto", "options": { "thinking": { "type": "enabled", "budgetTokens": 1024 } } },
        "deepseek-v4-flash-202605": { "name": "DeepSeek-V4-Flash 正式版 原厂直供", "options": { "thinking": { "type": "enabled", "budgetTokens": 1024 } } },
        "deepseek-v4-pro-202606": { "name": "DeepSeek-V4-Pro 正式版 原厂直供", "options": { "thinking": { "type": "enabled", "budgetTokens": 1024 } } },
        "minimax-m2.7": { "name": "MiniMax-M2.7", "options": { "thinking": { "type": "enabled", "budgetTokens": 1024 } } },
        "minimax-m3": { "name": "MiniMax-M3", "options": { "thinking": { "type": "enabled", "budgetTokens": 1024 } } },
        "glm-5.2": { "name": "GLM-5.2", "options": { "thinking": { "type": "enabled", "budgetTokens": 1024 } } },
        "glm-5.3": { "name": "GLM-5.3", "options": { "thinking": { "type": "enabled", "budgetTokens": 1024 } } },
        "glm-5.3-flash": { "name": "GLM-5.3-Flash", "options": { "thinking": { "type": "enabled", "budgetTokens": 1024 } } },
        "hy4-preview": { "name": "Hy4 preview", "options": { "thinking": { "type": "enabled", "budgetTokens": 1024 } } },
        "kimi-k2.7-code": { "name": "Kimi K2.7 Code", "options": { "thinking": { "type": "enabled", "budgetTokens": 1024 } } },
        "kimi-k3": { "name": "Kimi K3", "options": { "thinking": { "type": "enabled", "budgetTokens": 1024 } } }
      }
    }
  }
}
```

```json

{
  "$schema": "https://kilo.ai/config.json",
  "provider": {
    "lkeap": {
      "npm": "@ai-sdk/anthropic",
      "name": "Tencent Token Plan",
      "options": {
        "baseURL": "https://tokenhub.tencentmaas.com/plan/anthropic/v1",
        "apiKey": "<USER_API_KEY>"
      },
      "models": {
        "hy3": { "name": "Hy3", "options": { "thinking": { "type": "enabled", "budgetTokens": 1024 } } },
        "hy4-preview": { "name": "Hy4 preview", "options": { "thinking": { "type": "enabled", "budgetTokens": 1024 } } }
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

输入`/models`，选择 Tencent Token Plan 分组下的模型。
