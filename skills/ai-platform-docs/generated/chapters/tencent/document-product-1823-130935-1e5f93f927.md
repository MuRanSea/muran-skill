<!-- Official source: https://cloud.tencent.com/document/product/1823/130935 -->
<!-- Source SHA-256: 4538dd4b89e7d161651bcc9423312d59e2f1eb5d9de51952df79009282f3fc1d -->

# OpenClaw

官方来源：https://cloud.tencent.com/document/product/1823/130935
最近更新时间：2026-09-28 11:12:30

OpenClaw 是一款开源的本地 AI 代理框架，能让 AI 从“回答问题”进化为“动手执行任务”。它支持在 Windows、macOS 和 Linux 上自主运行，通过内置工具和可扩展的插件体系，自动完成文件整理、邮件处理、代码编写等操作。本文以 Hy3 模型为例演示如何将模型接入到 OpenClaw 中使用。

## 安装方式

您需要根据实际环境类型安装 OpenClaw，详情请参见 [OpenClaw 安装方式](https://docs.openclaw.ai/zh-CN)。如果已安装 OpenClaw，可以跳过这一步。

## 获取 API Key

1. 进入[API Key 管理](https://console.cloud.tencent.com/tokenhub/apikey) 页面，单击**创建 API Key**。操作详情请参见 [创建 API Key](https://cloud.tencent.com/document/product/1823/130090#40882178-aaf2-48c9-8559-dffc083a79bc)。

**注意：**

在设置**可访问范围**时，如果选择“限定范围”，则需要确保勾选 **Hy3**。

2. 创建完成后，请您务必**复制并妥善保管 API Key**，在后续配置到工具的流程中将会使用该信息。

![](https://qcloudimg.tencent-cloud.cn/image/document/654b883e1243be9e2757c4eaebaaba29.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/654b883e1243be9e2757c4eaebaaba29.png)

## 配置 OpenClaw

### onboard 引导

通过 OpenClaw 官方的 onboard 向导完成接入，适合首次配置。向导会自动完成模型注册与密钥写入。

#### 1. 将模型接入 OpenClaw

打开终端，运行以下命令。

```bash
openclaw onboard --auth-choice tokenhub-api-key
```

根据终端显示的提示信息，依次完成相关配置，配置信息参考如下。

##### **基础配置**

| **终端提示信息** | **配置内容** |
| --- | --- |
| I understand this is personal-by-default and shared/multi-user use requires lock-down. Continue? | 选择 `Yes` |
| Setup mode | 选择 `QuickStart`  **注意：**  若您之前已配置过 OpenClaw，选择 QuickStart 后，可能会触发如下图的 “Existing config detected”。请根据需求选择：  沿用原有配置：选择 Use existing values 继续即可；  更换或新增模型：改选 Reset，配置您想要的默认模型。 |

完成后终端信息呈现如下图：

![](https://qcloudimg.tencent-cloud.cn/image/document/1e601222d960d1cc4d9bab01c5ca7b6b.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/1e601222d960d1cc4d9bab01c5ca7b6b.png)

##### **模型配置**

| **终端提示信息** | **配置内容** |
| --- | --- |
| Enter Tencent TokenHub API key | 填写获取的 API Key |
| Default model | 设置为 tencent-tokenhub/hy3  **说明：**  若要配置其他模型，请将 hy3 替换为您实际要使用的[模型 ID](https://cloud.tencent.com/document/product/1823/130051)。 |

##### **功能配置**

| **终端提示信息** | **配置内容** |
| --- | --- |
| Select channel (QuickStart) | 选择 `Skip for now`，可以后续再进行配置。 |
| Configure skills now? (recommended) | 选择 `No`，可以后续再进行配置。 |
| Enable hooks? | 首次体验推荐选 `Skip for now`，如需记录命令审计、自动执行启动脚本等高级能力，可按 **↑/↓** 选择对应 hook 后按空格勾选。 |
| How do you want to hatch your agent? | 选择 `Hatch in Terminal`。 |

##### 验证模型是否可用

完成配置后，可在终端运行以下命令，验证模型是否可用：

```bash
openclaw models list --provider tencent-tokenhub
```

终端输出如下图信息，即配置成功，您即可以在 OpenClaw 中使用 Hy3 模型。

![](https://qcloudimg.tencent-cloud.cn/image/document/152cb7e3742adac72b455399fe6e1c8e.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/152cb7e3742adac72b455399fe6e1c8e.png)

#### 2. 非交互式快速接入

打开终端，运行以下命令（注意将 `YOUR_API_KEY` 修改为您的 API Key）。

**说明：**

以下命令以 macOS/Linux 为例。Windows 用户请删除所有行尾 `\\` 后写在一行执行，或使用 `^` 代替 `\\` 作为续行符。

```bash
openclaw onboard --non-interactive \\
  --mode local \\
  --auth-choice tokenhub-api-key \\
  --tokenhub-api-key "YOUR_API_KEY" \\
  --skip-health \\
  --accept-risk
```

### 直接编辑配置文件

如果您不希望使用 onboard 向导（例如已有自定义配置），可直接编辑 OpenClaw 配置文件完成接入。

#### 1. 打开配置文件

使用文本编辑器打开 `openclaw.json` 文件（若文件不存在，新建即可，内容需用 `{}` 包裹）。

#### 2. 增加 models.providers 配置

在 `openclaw.json` 中增加 `models.providers` 配置：

`baseUrl`：TokenHub 兼容 OpenAI 接口协议的 Base URL，固定为 `https://tokenhub.tencentmaas.com/v1`。

`<USER_API_KEY>`：替换为您的 API Key。

```json
"models": {
    "mode": "merge",
    "providers": {
      "tencent-tokenhub": {
        "baseUrl": "https://tokenhub.tencentmaas.com/v1",
        "apiKey": "<USER_API_KEY>",
        "api": "openai-completions",
        "models": [
          {
            "id": "hy3",
            "name": "Hy3",
            "reasoning": true,
            "input": ["text"],
            "contextWindow": 262144,
            "contextTokens": 196608,
            "maxTokens": 131072
          }
        ]
      }
    }
  }
```

#### 3. 配置默认模型

在 `openclaw.json` 中修改 `agents.defaults`，指定默认模型 `hy3`。

```json
"agents": {
    "defaults": {
      "model": {
        "primary": "tencent-tokenhub/hy3"
      },
      "models": {
        "tencent-tokenhub/hy3": {}
      }
    }
  }

```

#### 4. 使配置生效

保存文件后，OpenClaw Gateway 会自动热加载配置；如未生效，请重启 OpenClaw Gateway。

**说明：**

若配置文件中已有内容，请将上述 `models`、`agents` 字段与现有内容合并，不要整体覆盖。

如需接入其他模型，请将 `id` 与 `primary` 中的 `hy3` 替换为实际 [模型 ID](https://cloud.tencent.com/document/product/1823/130051)，并按该模型规格调整 `contextWindow`、`contextTokens`、`maxTokens`。

#### 5. 验证

执行以下命令确认模型已注册：

```bash
openclaw models list --provider tencent-tokenhub
```

终端输出 Hy3 模型信息，即表示配置成功。

**注意：**

OpenClaw 对配置文件执行严格校验，字段名或类型错误会导致 Gateway 启动失败。若配置后出现异常，可执行 `openclaw doctor` 查看具体问题，或执行 `openclaw doctor --fix` 自动修复。更多字段说明请参见 [OpenClaw 配置文档](https://docs.openclaw.ai/configuration)。

## 通用配置

### 1. 思考模式

Hy3 模型支持通过 `reasoning_effort` 参数控制推理深度。OpenClaw 的思考级别会自动按下表映射：

| **OpenClaw 思考级别** | **传入给 API 的值** | **说明** |
| --- | --- | --- |
| off | 不传该参数 | 不启用思考，极速响应（no\_think） |
| minimal | low | 快速思考（low） |
| low | low | 快速思考（low） |
| medium | low | 快速思考（low） |
| high | high | 深度推理（high） |
| xhigh | high | 深度推理（high） |

在 OpenClaw 的聊天中使用 `/think low` 或 `/think high` 指令即可切换思考模式。

### 2. 高级配置-环境和守护进程设置

如果 Gateway 以守护进程（launchd/systemd）方式运行，请确保 `YOUR_API_KEY` 对该进程可用（例如放在 `~/.openclaw/.env` 中，或通过 `env.shellEnv` 提供）。

自定义 Provider 方式下，API Key 直接写在配置文件里，守护进程会自动读取，具体配置方式请参见上文 [配置 OpenClaw（直接编辑配置文件）](https://cloud.tencent.com/document/product/1823/130935#3623b6e5-7de9-43a5-affa-eee4a5d8b467)。

### 3. 相关参考文档

[OpenClaw 配置文档](https://docs.openclaw.ai/configuration)
