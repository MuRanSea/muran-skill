<!-- Official source: https://cloud.tencent.com/document/product/1823/133532 -->
<!-- Source SHA-256: 70f59735fd36847b9ef9256e29ac8997dd5e5cfacca78cdd1327d29160323ebc -->

# Codex

官方来源：https://cloud.tencent.com/document/product/1823/133532
最近更新时间：2026-09-28 11:12:30

Codex 是 OpenAI 推出的 AI 编程工具，可通过自然语言将完整的编程任务交由其自主完成，辅助开发者读懂代码库、编辑文件。为满足广大开发者的需求，目前已增加对 Codex 的支持，本文以 Hy3 模型为例演示如何将模型接入到 Codex 中使用。

## 安装 Codex

请根据实际环境类型安装 Codex，详情请参见 [Codex 安装](https://developers.openai.com/codex/quickstart)。如果已安装 Codex，可跳过此步骤。

## 获取 API Key

1. 进入 [API Key 管理](https://console.cloud.tencent.com/tokenhub/apikey) 页面，单击**创建 API Key**。操作详情请参见 [创建 API Key](https://cloud.tencent.com/document/product/1823/130090#40882178-aaf2-48c9-8559-dffc083a79bc)。

**注意：**

在设置**可访问范围**时，如果选择“限定范围”，则需要确保勾选 **Hy3**。

2. 创建完成后，请您务必**复制并妥善保管 API Key**，在后续配置到工具的流程中将会使用该信息。

![](https://qcloudimg.tencent-cloud.cn/image/document/97bd39109afd2aa7e0b9b00dbe4c2723.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/97bd39109afd2aa7e0b9b00dbe4c2723.png)

## 配置 Codex

### 配置模型设置

1. 打开 Codex，单击左下角**设置**，进入**配置**页面后单击右侧**打开 config.toml**，以系统默认编辑器打开配置文件。

![](https://qcloudimg.tencent-cloud.cn/image/document/a89f1f63facf346089ad57e880a3e04b.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/a89f1f63facf346089ad57e880a3e04b.png)

2. 在打开的 config.toml 顶部写入以下内容（若已有其他内容，将以下配置段添加至文件开头即可）。

```bash
model_provider = "hy3-tokenhub"
model = "hy3"
disable_response_storage = true
# Hy3 不兼容 Responses API 的 web_search 工具，需禁用；换用支持联网搜索的模型（如 deepseek-v4-pro）时删除本行
web_search = "disabled"

[model_providers.hy3-tokenhub]
name = "Hy3 via tokenhub"
base_url = "https://tokenhub.tencentmaas.com/v1"
env_key = "HY3_API_KEY"
wire_api = "responses"

```

3. 打开终端，运行以下命令注入 API Key。

```bash
# macOS系统
launchctl setenv HY3_API_KEY "您的 API Key"

# Windows系统
setx HY3_API_KEY "您的 API Key"
```

### 确认模型是否生效

完全退出 Codex（仅关闭窗口无效），再重新启动。启动后将自动读取刚才注入的 Key 及 config.toml 配置。

在主界面输入框输入测试消息，若模型正常返回响应（如 Hello! How can I help you today?），则表示接入成功。

![](https://qcloudimg.tencent-cloud.cn/image/document/b1eb71a3b3282fe2d94fdc6e59c25ac1.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/b1eb71a3b3282fe2d94fdc6e59c25ac1.png)

## 常见问题

### Codex 提示 “Model metadata for hy3 not found. Defaulting to fallback metadata”，是否说明 Hy3 模型在 Codex 中不被支持或能力受限？

不是。Hy3 通过 Codex 官方开放的自定义模型 Provider（custom model provider）机制接入，这是 Codex 官方提供的标准接入能力，按文档配置即可使用。

该提示来源于 Codex 的模型元数据机制：Codex 内置模型目录仅包含其自有模型，通过自定义 Provider 接入的模型不在该目录内，Codex 会采用默认的上下文窗口估算值并输出此提示。这不影响 Hy3 在 Codex 中的正常对话与工具调用，模型能力完整可用。

如需使用更精确的上下文窗口，可通过 Codex 官方提供的配置项自主指定：在 config.toml 中增加一行设置 `model_context_window = 实际上下文窗口值`，即可调整窗口估算；如需完整指定模型元数据，可使用 model\_catalog\_json 指向本地模型目录文件，具体配置方式请参见 [Codex 示例配置](https://developers.openai.ac.cn/codex/config-sample)。
