<!-- Official source: https://cloud.tencent.com/document/product/1823/130096 -->
<!-- Source SHA-256: ea825ac8876ddc497d78b4ed85589b00e92b18c26a071c20c1d9a3a543705b73 -->

# OpenCode

官方来源：https://cloud.tencent.com/document/product/1823/130096
最近更新时间：2026-06-22 22:27:30

OpenCode 是一款开源的 AI 编程代理工具，提供终端界面、桌面应用和 IDE 扩展等多种使用方式。本文介绍如何在 OpenCode 中配置与使用腾讯云大模型 Coding Plan。

## 前置条件

在开始配置前，请确保您已订阅 Coding Plan 套餐并获取 API Key，可参见 [Coding Plan 概述](https://cloud.tencent.com/document/product/1823/130092)。

## 安装 OpenCode

执行如下命令安装 OpenCode，更多操作可参考 [OpenCode 官方配置指引](https://open-code.ai/zh/docs#%E5%AE%89%E8%A3%85)。

```bash
npm install -g opencode-ai
```

安装完成后，您可以执行如下命令检查，输出版本号则表示安装成功。

```bash
opencode -v
```

## 配置 Coding Plan

您需要按照下面的示例修改 OpenCode 的配置文件，配置文件路径如下，配置文件不存在时新建即可。

macOS / Linux：`~/.config/opencode/opencode.json`。

Windows：`C:\\Users\\<用户名>\\.config\\opencode\\opencode.json`。

**说明：**

请您将 <USER\_API\_KEY> 替换为 Coding Plan 专属的 API Key。

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "myprovider": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "lkeap",
      "options": {
        "baseURL": "https://api.lkeap.cloud.tencent.com/coding/v3",
        "apiKey": "<USER_API_KEY>"
      },
      "models": {
        "tc-code-latest": {
          "name": "Auto",
          "modalities": {
            "input": [
              "text"
            ],
            "output": [
              "text"
            ]
          },
          "options": {
            "thinking": {
              "type": "enabled",
              "budgetTokens": 8192
            }
          },
          "limit": {
            "context": 196608,
            "output": 32768
          }
        },
        "minimax-m2.5": {
          "name": "MiniMax-M2.5",
          "modalities": {
            "input": [
              "text"
            ],
            "output": [
              "text"
            ]
          },
          "options": {
            "thinking": {
              "type": "enabled",
              "budgetTokens": 8192
            }
          },
          "limit": {
            "context": 196608,
            "output": 32768
          }
        },
        "kimi-k2.5": {
          "name": "Kimi-K2.5",
          "modalities": {
            "input": [
              "text"
            ],
            "output": [
              "text"
            ]
          },
          "options": {
            "thinking": {
              "type": "enabled",
              "budgetTokens": 8192
            }
          },
          "limit": {
            "context": 262144,
            "output": 32768
          }
        },
        "glm-5": {
          "name": "GLM-5",
          "modalities": {
            "input": [
              "text"
            ],
            "output": [
              "text"
            ]
          },
          "options": {
            "thinking": {
              "type": "enabled",
              "budgetTokens": 8192
            }
          },
          "limit": {
            "context": 202752,
            "output": 16384
          }
        }
      }
    }
  }
}
```

## 使用 OpenCode

执行如下命令启动 OpenCode：

```bash
opencode
```

输入`/models`，选择配置的模型并在 OpenCode 中使用。

![选择模型](https://qcloudimg.tencent-cloud.cn/image/document/a10830b31c95357875defd4af7c309f3.png)

完成上述配置后，即可开始使用 OpenCode。

![开始对话](https://qcloudimg.tencent-cloud.cn/image/document/bd925154068956c11a95108c6a817733.png)
