<!-- Official source: https://cloud.tencent.com/document/product/1823/131904 -->
<!-- Source SHA-256: 7f0959ad199aca154e0b77c463edb8315fcea3353270e456fa97b95639ba9e06 -->

# Kilo Code

官方来源：https://cloud.tencent.com/document/product/1823/131904
最近更新时间：2026-07-06 14:12:42

Kilo 插件（Kilo Code）是一个开源 AI 编码 Agent，能在编辑器里直接帮您按自然语言生成代码、改代码、跑终端任务，并提供补全、重构、调试等能力。本文以 Hy3 模型为例演示如何将模型接入到 Kilo Code 中使用。

## 环境要求

Kilo Code 支持 VS Code（及 Cursor、VSCodium、Windsurf 等 VS Code 兼容编辑器）和 JetBrains 系列 IDE。具体的编辑器版本、操作系统、Node.js 等环境要求，请以 Kilo Code 官方文档为准，详见 [Kilo Code 安装指南](https://kilo.org.cn/docs/getting-started/installing)。

## 安装 Kilo

在 IDE 中搜索安装 Kilo Code 插件，本文以 VS Code 为例展示安装配置过程。

打开 VS Code，在扩展市场中搜索 Kilo Code 并安装。

![](https://qcloudimg.tencent-cloud.cn/image/document/d43c60335f2d87a953f632df0231de93.png)

## 获取 API Key

1. 进入 [API Key 管理](https://console.cloud.tencent.com/tokenhub/apikey) 页面，单击**创建 API Key**。操作详情请参见 [创建 API Key](https://cloud.tencent.com/document/product/1823/130090#40882178-aaf2-48c9-8559-dffc083a79bc)。

**注意：**

在设置**可访问范围**时，如果选择“限定范围”，则需要确保勾选 **Hy3**。

2. 创建完成后，请您务必**复制并妥善保管 API Key**，在后续配置到工具的流程中将会使用该信息。

![](https://qcloudimg.tencent-cloud.cn/image/document/cda475ec2129fc6ce31c9446d0cf1c7f.png)

## 配置 Kilo Code

1. 在 VS Code 中打开 Kilo Code，点击右上角**设置**按钮进入 Kilo Settings。

![](https://qcloudimg.tencent-cloud.cn/image/document/b754e9f16f8a3aac0e73e87a71aa344e.png)

2. 在 Kilo Settings 中，选择**提供商 > 自定义提供商**，点击“**+ 连接**” 打开配置弹窗。

![](https://qcloudimg.tencent-cloud.cn/image/document/20c7b84af24bfe6e7d660a049138b537.png)

3. 配置以下信息，并保存提交。

**提供商 ID**：填入提供商 ID，例如 `tencent`**。**

**提供商显示名称**：填入提供商名称，例如 `Hy`**。**

**基础 URL**：`https://tokenhub.tencentmaas.com/v1`

**API 密钥**：填入您在 [获取 API Key](https://console.cloud.tencent.com/tokenhub/apikey) 步骤中创建的 API Key。

**模型 ID**：输入模型 ID `hy3`。

**模型显示名称**：输入 `Hy3`。

4. 在 Kilo Code 的模型列表中，找到并选定 **Hy3** 模型，即可进行对话使用。

![](https://qcloudimg.tencent-cloud.cn/image/document/d58fada5fcc101ee855bf95399a3f3cf.png)

**注意：**

默认配置下，Kilo Code 各思考档位和 Hy3 思考强度（reasoning\_effort）模式的映射关系为：

low/medium：对应 `low`

High：对应 `high`

5. （可选）若您需要使用 Hy3 的 no\_think 模式，可以通过以下方式进行附加配置。

5.1 编辑 kilo.jsonc 文件，不同系统的配置文件路径不同，具体可参考：

MacOS/Linux 对应路径为 `~/.config/kilo/kilo.jsonc`

Windows 对应路径为 `用户目录/.config/kilo/kilo.jsonc`

5.2  打开文件后，在配置中**新增** `"reasoning": false` 字段（若文件已存在该字段，则将其值设为 `false`），保存并关闭。

5.3 重新打开 VS Code 加载 Kilo Code 插件，看到界面上不再显示思考档位的切换选项，即设置生效，此时发送消息给 Hy3，都将以 no\_think 模式处理。

## 常见问题

#### **插件提示 "Not Connected to CLI Backend"**

Kilo Code VSCode 插件依赖 Kilo CLI 作为后端服务，出现此提示说明插件未能连接到 CLI 后端。请按以下步骤排查：

**步骤1**：确认 Node.js 已安装（v18.0+）：在终端中执行 `node --version`，若未安装或版本低于 v18.0，请前往 [Node.js 官网](https://nodejs.org/en/download/) 下载安装。

**步骤2**：安装 Kilo CLI，您可以在终端中执行以下命令安装：

```bash
npm install -g @kilocode/cli
```

**步骤3**：验证安装：执行 `kilo --version`，确认有版本号输出。

**步骤4**：重启 VS Code。安装完成后，完全关闭并重新打开 VSCode，插件会自动检测并连接到 Kilo CLI 后端。
