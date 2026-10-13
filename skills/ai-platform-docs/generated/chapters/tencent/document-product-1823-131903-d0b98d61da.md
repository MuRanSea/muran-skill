<!-- Official source: https://cloud.tencent.com/document/product/1823/131903 -->
<!-- Source SHA-256: 878f88dc77e28f1c9612e6e672e1706c6576ec0ffe736e8ac587b32caaf5e13c -->

# Claude Code

官方来源：https://cloud.tencent.com/document/product/1823/131903
最近更新时间：2026-07-06 14:12:12

Claude Code 是一款运行在终端中的 AI 编程工具，可以通过灵活的自然语言辅助开发者高效编码、调试和管理代码。本文以 Hy3 模型为例演示如何将模型接入到 Claude Code 中使用。

## 安装 Claude Code

您需要根据实际环境类型安装 Claude Code，详情请参见 [Claude Code 安装](https://code.claude.com/docs/en/overview)。如果已安装 Claude Code，可以跳过这一步。

## 获取 API Key

1. 进入 [API Key 管理](https://console.cloud.tencent.com/tokenhub/apikey) 页面，单击**创建 API Key**。操作详情请参见 [创建 API Key](https://cloud.tencent.com/document/product/1823/130090#40882178-aaf2-48c9-8559-dffc083a79bc)。

**注意：**

在设置**可访问范围**时，如果选择“限定范围”，则需要确保勾选 **Hy3**。

2. 创建完成后，请您务必**复制并妥善保管 API Key**，在后续配置到工具的流程中将会使用该信息。

![](https://qcloudimg.tencent-cloud.cn/image/document/c57bb6eef94ed2d939f3690234cf3450.png)

## 配置 Claude Code

### 1. 手动配置模型的环境变量

完成 Claude Code 安装和 API Key 的获取后，需要配置 Hy3 模型的 API 信息，具体配置方式如下：

编辑或新增 `settings.json` 文件，并根据您获取 API Key 的渠道，增加对应的配置文件内容，不同系统的配置文件路径不同，具体可参考：

MacOS/Linux 对应路径为 `~/.claude/settings.json`

Windows 对应路径为 `用户目录/.claude/settings.json`

若 `settings.json` 文件不存在，可使用文本编辑器（如 VSCode、记事本等）手动创建，或在终端中执行以下命令创建：

```bash
 # MacOS/Linux
 mkdir -p ~/.claude && touch ~/.claude/settings.json

 # Windows（PowerShell）
 New-Item -ItemType Directory -Force -Path "$HOME\\.claude" | Out-Null; New-Item -ItemType File -Force -Path "$HOME\\.claude\\settings.json" | Out-Null
```

配置以下内容（注意将 `YOUR_API_KEY` 替换为真实 API Key）：

```bash
 {
   "env": {
     "ANTHROPIC_BASE_URL": "https://tokenhub.tencentmaas.com",
     "ANTHROPIC_AUTH_TOKEN": "YOUR_API_KEY",
     "ANTHROPIC_MODEL": "hy3",
     "ANTHROPIC_DEFAULT_OPUS_MODEL": "hy3",
     "ANTHROPIC_DEFAULT_SONNET_MODEL": "hy3",
     "ANTHROPIC_DEFAULT_HAIKU_MODEL": "hy3",
     "CLAUDE_CODE_SUBAGENT_MODEL": "hy3",
     "ENABLE_TOOL_SEARCH": false
   }
 }
```

各环境变量含义如下：

| 环境变量 | 是否必填 | 说明 |
| --- | --- | --- |
| `ANTHROPIC_BASE_URL` | 是 | Claude Code 请求的 API 网关地址。接入 TokenHub 时固定为 `https://tokenhub.tencentmaas.com`。 |
| `ANTHROPIC_AUTH_TOKEN` | 是 | 用于鉴权的 API Key，需替换为您在 TokenHub 控制台创建的真实 API Key。请妥善保管，避免泄露。 |
| `ANTHROPIC_MODEL` | 是 | Claude Code 默认调用的模型名。本文以 `hy3` 为例，您也可以替换为 TokenHub 支持的其他模型。 |
| `ANTHROPIC_DEFAULT_OPUS_MODEL` | 否 | Claude Code 中 Opus 档位（高复杂度任务）映射到的模型。这里设为 `hy3`，使所有档位统一指向同一个模型。 |
| `ANTHROPIC_DEFAULT_SONNET_MODEL` | 否 | Claude Code 中 Sonnet 档位（默认日常任务）映射到的模型。 |
| `ANTHROPIC_DEFAULT_HAIKU_MODEL` | 否 | Claude Code 中 Haiku 档位（轻量/快速任务）映射到的模型。 |
| `CLAUDE_CODE_SUBAGENT_MODEL` | 否 | Claude Code 创建子任务（subagent）时使用的模型。建议与主模型保持一致，避免出现跨模型调用导致的兼容性问题。 |
| `ENABLE_TOOL_SEARCH` | 否 | 是否启用 Claude Code 内置的原生 web search 工具。由于 Claude Code 禁止第三方模型使用内置搜索，这里需设为 `false`，如需搜索能力请参考下文 [常见问题](https://cloud.tencent.com/document/product/1823/131903#.E5.B8.B8.E8.A7.81.E9.97.AE.E9.A2.98) 配置 MCP 搜索服务。 |

保存配置后，请**打开新的终端窗口**执行后续命令，确保环境变量加载生效。

### 2. 确认环境变量是否生效

进入命令行界面，执行以下命令启动 Claude Code：

```bash
# 打开项目目录
cd your-project

# 启动 Claude Code
claude
```

**注意：**

若您是首次启动 Claude Code，终端会先进入交互式初始化向导，依次提示您选择主题（Theme）、登录方式（Login Method）等。请按照终端提示完成首次配置后再继续后续步骤。

启动成功后，在 Claude Code 中输入 `/status` 确认模型状态生效（参考下图示例）：当 `API Endpoint` 显示为 `https://tokenhub.tencentmaas.com`，且 `Model` 显示为 `hy3` 时，即表示模型配置已生效。

![](https://qcloudimg.tencent-cloud.cn/image/document/8f9459f0828053e9a3ad1b04f29f7efe.png)

### 3. 使用 Claude Code

确认配置生效后，即可开始对话。

**注意：**

1. 基于以上配置，Hy3 默认思考模式为 `no_think`，如需开启深度推理，请参考本文档的 [开启深度推理](https://cloud.tencent.com/document/product/1823/131903#4.-.E5.BC.80.E5.90.AF.E6.B7.B1.E5.BA.A6.E6.8E.A8.E7.90.86) 小节进行设置。

2. Claude Code 禁止第三方模型使用内置原生搜索工具，若您需要结合搜索使用，可在 [腾讯云 MCP 市场](https://cloud.tencent.com/developer/mcp/server/11764) 等渠道选用合适的 MCP 服务使用，详情请参见 [常见问题](https://cloud.tencent.com/document/product/1823/131903#.E5.B8.B8.E8.A7.81.E9.97.AE.E9.A2.98)。

### 4. 开启深度推理

若需要开启深度推理（high），则需要在 Claude Code 中输入 `/config`，将 Thinking mode 设置为 `true`。

![](https://qcloudimg.tencent-cloud.cn/image/document/d558777a8bc36dc1b959580593529fdd.png)

确认设置后，退出重新进入 Claude Code，即可生效。

![](https://qcloudimg.tencent-cloud.cn/image/document/78941c6f04ec0012f727c037ae1e44b1.png)

## 常见问题

#### 配置模型后为何无法在 Claude Code 中使用搜索（web search）？

Claude Code 禁止第三方模型使用内置原生搜索工具，因此在配置 Hy3 模型后，将无法正常使用 Claude Code 原生的 web search 工具，此时若使用中触发搜索，会出现如下图搜索失败的表现：

![](https://qcloudimg.tencent-cloud.cn/image/document/b6160e160f725759676737703333bceb.png)

若您需要结合搜索使用，可在 [腾讯云 MCP 市场](https://cloud.tencent.com/developer/mcp/server/11764) 等各开放渠道中，选用合适的搜索 MCP 服务配置在 Claude Code 中使用。

以下以腾讯云 MCP 市场的 [联网搜索 MCP](https://cloud.tencent.com/developer/mcp/server/11764) 为例，介绍搜索 MCP 的配置方法。

**步骤1**：访问 [联网搜索 MCP](https://cloud.tencent.com/developer/mcp/server/11764)，参考页面指引开通搜索 MCP 服务，并获取搜索 MCP 所需的云 API 密钥（注意，此 API 密钥是独立密钥，和您之前获取的大模型 API Key 不同）。

![](https://qcloudimg.tencent-cloud.cn/image/document/4468cff15d4411cf3a44dec0314a0c8b.png)

**步骤2**：开通服务后，页面上会显示连接搜索服务的配置 json，点击复制配置内容。

![](https://qcloudimg.tencent-cloud.cn/image/document/2829957a15db575b937bf5e45bba88e7.png)

**步骤3**：在 Claude Code 中，执行以下命令添加 MCP（注意将“XXX”替换为您获取的真实值）。

```bash
claude mcp add --transport sse WebSearchMCP "https://mcp-api.tencent-cloud.com/sse/XXX"
```

**步骤4**：执行以下命令启动 Claude Code（启动时，推荐通过 disallowedTools "WebSearch" 关闭原生搜索工具，可确保模型更稳定地调用您配置的搜索 MCP 服务）。

```bash
claude --disallowedTools "WebSearch"
```

**步骤5**：MCP 配置完成后，需**重启 Claude Code 才能生效**。请退出当前 Claude Code 会话（输入 `/exit` 或按 `Ctrl+C` 退出），再重新执行上述启动命令。重启后，即可在 Claude Code 中通过您配置的搜索 MCP 服务正常使用搜索能力。

![](https://qcloudimg.tencent-cloud.cn/image/document/d529e077ea14fadbb202faf79d16f532.png)
