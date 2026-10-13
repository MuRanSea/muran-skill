<!-- Official source: https://cloud.tencent.com/document/product/1823/130936 -->
<!-- Source SHA-256: 9f2649ccef822a9891ff8dbc39ef684a1fdbeaeb779fb181a87c940b29cae775 -->

# OpenCode

官方来源：https://cloud.tencent.com/document/product/1823/130936
最近更新时间：2026-08-31 16:39:19

OpenCode 是一个开源的 AI 编程智能体，可以在终端、桌面客户端或 IDE 扩展中接入多种大模型使用，可帮助开发者进行代码分析、智能编码等多种任务。以 DeepSeek V4 Pro 模型为例演示如何将模型接入到 OpenCode 中使用。

**说明：**

本文分别介绍 OpenCode 桌面版与终端版（CLI）的配置方法。如您只需使用桌面版，可直接参考 [配置 OpenCode 桌面端](https://cloud.tencent.com/document/product/1823/130936#b44aa68d-a56b-42ca-a864-2bfad942e60f) 章节；如需使用终端版，请参考 [配置 OpenCode 终端（CLI）](https://cloud.tencent.com/document/product/1823/130936#f831a221-7034-448b-8644-488639b77c8f) 章节。

## 安装 OpenCode

安装 OpenCode，请参见 [OpenCode 安装指南](https://opencode.ai/)。如果已安装 OpenCode，可以跳过这一步。

## 获取 API Key

1. 进入[API Key 管理](https://console.cloud.tencent.com/tokenhub/apikey) 页面，单击**创建 API Key**。操作详情请参见 [创建 API Key](https://cloud.tencent.com/document/product/1823/130090#40882178-aaf2-48c9-8559-dffc083a79bc)。

**注意：**

在设置**可访问范围**时，如果选择“限定范围”，则需要确保勾选 **DeepSeek V4 Pro**。

2. 创建完成后，请您务必**复制并妥善保管 API Key**，在后续配置到工具的流程中将会使用该信息。

![](https://qcloudimg.tencent-cloud.cn/image/document/654b883e1243be9e2757c4eaebaaba29.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/654b883e1243be9e2757c4eaebaaba29.png)

## 配置 OpenCode 桌面端

1. 请根据实际环境类型进行操作：

以 Windows 为例，打开 OpenCode，在对话界面，展开模型列表，选择**管理模型**。单击右上角 **+链接提供商**，选择**自定义 OpenAI 兼容提供商**。

以 macOS 为例，打开 OpenCode，在对话界面，展开模型列表，点击右上角 “+” 打开模型设置界面。在打开的弹窗中，点击 “Show more providers”，选择 “Custom”。

![](https://qcloudimg.tencent-cloud.cn/image/document/1c677cb798266c23cf3b80f22e268f9f.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/1c677cb798266c23cf3b80f22e268f9f.png)

2. 在打开的弹窗中，点击填写信息：

**提供商 ID**：`tencent`

**显示名称**：`Tencent`

**基础 URL**：`https://tokenhub.tencentmaas.com/v1`

**API 密钥**：填写您的 API Key。

**模型 ID**：填写 `deepseek-v4-pro`

**模型显示名称**：填写 `DeepSeek V4 Pro`

![](https://qcloudimg.tencent-cloud.cn/image/document/027418c4331526353a95b69fe6cfe462.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/027418c4331526353a95b69fe6cfe462.png)

3. 重启 OpenCode 客户端，在对话窗口的模型列表中，找到并选定新配置的模型，即可进行对话使用。

![](https://qcloudimg.tencent-cloud.cn/image/document/995b796b153504b840b4ba2c7222ac2e.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/995b796b153504b840b4ba2c7222ac2e.png)

## 配置 OpenCode 终端（CLI）

OpenCode 同时提供命令行版本，配置方式与桌面端类似，区别仅在启动入口不同。

### 1. 安装 CLI

参考 [OpenCode 官方文档](https://opencode.ai/) 安装终端版本，安装完成后执行：

```bash
opencode --version
```

### 2. 编辑配置文件

创建并打开：

```bash
mkdir -p ~/.config/opencode && open -e ~/.config/opencode/opencode.json
```

**说明：**

`~/.config/opencode` 目录默认可能不存在，先创建目录；若文件不存在，`open -e` 保存后会自动创建。

复制以下配置：

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "tencent": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Tencent",
      "options": {
        "baseURL": "https://tokenhub.tencentmaas.com/v1"
      },
      "models": {
        "deepseek-v4-pro": {
          "name": "DeepSeek V4 Pro"
        }
      }
    }
  }
}
```

### 3. 连接并录入 API Key

1. 在终端中运行 `opencode`，进入 OpenCode 的命令行交互界面：

```bash
opencode
```

2. 在命令行界面输入：`/connect`

![](https://qcloudimg.tencent-cloud.cn/image/document/94fe220fe3069380595a87bd10dce1e3.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/94fe220fe3069380595a87bd10dce1e3.png)

3. 选择 **Tencent。**

![](https://qcloudimg.tencent-cloud.cn/image/document/7ac9931da1eb21ea299e58137fece7f5.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/7ac9931da1eb21ea299e58137fece7f5.png)

4. 粘贴从 TokenHub 控制台复制的 [API Key](https://console.cloud.tencent.com/tokenhub/apikey?regionId=1)。

![](https://qcloudimg.tencent-cloud.cn/image/document/89d4ef1e0a0c649ccc9294383066ba65.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/89d4ef1e0a0c649ccc9294383066ba65.png)

### 4. 切换模型

1. 在命令行界面输入：`/models`

2. 选择 **DeepSeek V4 Pro** 后即可开始对话。
