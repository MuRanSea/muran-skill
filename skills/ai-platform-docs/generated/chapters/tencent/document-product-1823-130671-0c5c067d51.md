<!-- Official source: https://cloud.tencent.com/document/product/1823/130671 -->
<!-- Source SHA-256: 8968e4f62c438d0c6cdad53c58ae90e29323af626d159c03bf5a8cb3f43d2ef0 -->

# OpenClaw

官方来源：https://cloud.tencent.com/document/product/1823/130671
最近更新时间：2026-04-17 23:32:42

OpenClaw 是一款开源的本地 AI 代理框架，能让 AI 从“回答问题”进化为“动手执行任务”。它支持在 Windows、macOS 和 Linux 上自主运行，通过内置工具和可扩展的插件体系，自动完成文件整理、邮件处理、代码编写等操作。

腾讯云 Token Plan 企业版支持在 OpenClaw 中使用，可参考本文进行配置及使用。

## 前置条件

在开始配置前，确保您已完成以下准备工作：

1. [订阅 Token Plan 企业版套餐](https://cloud.tencent.com/document/product/1823/130660#9bad146b-59b9-463a-b9d9-4c21a823f8a5)。

2. [获取模型配置](https://cloud.tencent.com/document/product/1823/130660#e1afdc13-96a1-46ac-b648-fa94ce3a3e7f)。

3. [获取 API Key](https://cloud.tencent.com/document/product/1823/130660#c517dcb2-4a6d-4fbc-9793-a6fc05467143)。

## 安装 OpenClaw

您需要根据实际环境类型，执行对应命令安装 OpenClaw。

macOS/Linux

Windows

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

在 PowerShell 中执行以下命令。

```bash
iwr -useb https://openclaw.ai/install.ps1 | iex
```

根据提示信息完成 OpenClaw 配置，参考配置如下。

| 向导配置项 | 配置内容 |
| --- | --- |
| I understand this is powerful and inherently risky. Continue? | 选择 **Yes**。 |
| Onboarding mode | 选择 **QuickStart**。 |
| Model/auth provider | 选择 **Skip for now**，后续可以配置。 |
| Filter models by provider | 选择 **All providers**。 |
| Default model | 使用默认配置。 |
| Select channel (QuickStart) | 选择 **Skip for now**，后续可以配置。 |
| Search provider | 选择 **Skip for now**，后续可以配置。 |
| Configure skills now? (recommended) | 选择 **No**，后续可以配置。 |
| Enable hooks? | 按空格键选中选项，按回车键进入下一步。 |
| How do you want to hatch your bot? | 选择 **Hatch in TUI**。 |

## 配置 Token Plan 企业版

**注意：**

如果出现配置正常但是访问404，401等问题是因为 OpenClaw 的缓存问题导致，您可以直接修改本地配置文件，重启 OpenClaw gateway，配置文件路径如下：

Windows：`C:\\Users\\<用户名>\\.openclaw\\openclaw.json`

macOS/Linux：`~/.openclaw/openclaw.json`

1. 执行以下命令打开 OpenClaw 的 WebUI，然后在 WebUI 的左侧菜单栏中选择 **Config** > **Raw**。

```bash
openclaw dashboard
```

2. 在 openclaw.json 配置项中增加 models.providers 的配置。

baseUrl：参考样例，使用 Token Plan 兼容 OpenAI 接口协议的 Base URL（`https://tokenhub.tencentmaas.com/plan/v3`） 配置。

<USER\_API\_KEY>：替换成您自己的 API Key。

```json
"models": {
    "mode": "merge",
    "providers": {
      "tencent-token-plan": {
        "baseUrl": "https://tokenhub.tencentmaas.com/plan/v3",
        "apiKey": "<USER_API_KEY>", 
        "api": "openai-completions",
        "models": [       
         {
            "id": "auto",
            "name": "Auto",
            "reasoning": false,
            "input": ["text"],
            "cost": { "input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0 },
            "contextWindow": 196608,
            "maxTokens": 32768
          },
          {
            "id": "minimax-m2.5",
            "name": "MiniMax-M2.5",
            "reasoning": false,
            "input": ["text"],
            "cost": { "input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0 },
            "contextWindow": 196608,
            "maxTokens": 32768
          },
                    {
            "id": "kimi-k2.5",
            "name": "Kimi-K2.5",
            "reasoning": false,
            "input": ["text"],
            "cost": { "input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0 },
            "contextWindow": 262144,
            "maxTokens": 32768
          },
          {
            "id": "glm-5",
            "name": "GLM-5",
            "reasoning": false,
            "input": ["text"],
            "cost": { "input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0 },
            "contextWindow": 202752,
            "maxTokens": 16384
          }
        ]
      }
    }
 }
```

3. 在 openclaw.json 配置项中修改 agents.default，增加模型列表信息，其中：**primary** 字段指定的模型可以根据您的偏好进行配置。

```json
"agents": {
    "defaults": {
      "model": {
        "primary": "tencent-token-plan/glm-5"
      },
      "models": {  
        "tencent-token-plan/tc-code-latest": {},
        "tencent-token-plan/hunyuan-2.0-instruct": {},
        "tencent-token-plan/hunyuan-2.0-thinking": {},
        "tencent-token-plan/hunyuan-t1": {},
        "tencent-token-plan/hunyuan-turbos": {},
        "tencent-token-plan/minimax-m2.5": {},
        "tencent-token-plan/kimi-k2.5": {},
        "tencent-token-plan/glm-5": {}
      }
    }
  }
```

4. 在界面上单击 **Save** 保存配置，保存完成后，单击 **Update** 使配置生效。

![](https://qcloudimg.tencent-cloud.cn/image/document/35892ab6adcd7714cabb98efd4273bd8.png)

## 使用 OpenClaw

OpenClaw 支持通过 WebUI 和 TUI 的形式进行交互使用。

WebUI

您可以通过 `openclaw dashboard` 命令打开 WebUI，单击 WebUI 左侧的**聊天**，即可进行交互。

![](https://qcloudimg.tencent-cloud.cn/image/document/f83db5fd93fe8202a0045f64b99a9062.png)

TUI

您可以通过 `openclaw tui` 命令打开 TUI 进行交互。

![](https://qcloudimg.tencent-cloud.cn/image/document/f5a48e525d80ca80411f10c4b1d77a62.png)
