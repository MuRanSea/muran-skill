<!-- Official source: https://cloud.tencent.com/document/product/1823/130068 -->
<!-- Source SHA-256: abb2ce3715cbd6a8447cae5eab773885171d9cb6ef7a213e1b74f4c2f5fd4aaf -->

# CodeBuddy

官方来源：https://cloud.tencent.com/document/product/1823/130068
最近更新时间：2026-09-29 14:11:34

CodeBuddy 腾讯云推出的 AI 辅助编程工具，通过将 AI 深度融入全流程，实现从产品构思到产品发布的一站式高效交付平台。 产品支持 IDE、插件和 CLI 三种形态，覆盖从专业开发者到零基础用户的全场景需求。本文介绍如何在 CodeBuddy 中配置与使用腾讯云大模型 Token Plan，适用于 CodeBuddy IDE 和 CodeBuddy CLI。

## 前置条件

在开始配置前，请确保您已完成以下准备工作：

1. [订阅 Token Plan 套餐](https://cloud.tencent.com/document/product/1823/130119#bdc49d9b-f68d-4b79-bb5a-0aa694f2624a)。

2. [获取 API Key](https://cloud.tencent.com/document/product/1823/130119#ac6f544e-6de6-46b7-8709-36d777248b34)。

3. 安装 CodeBuddy，您可以按需选择安装 CodeBuddy IDE 或者 CLI：

安装 CodeBuddy IDE

安装 CodeBuddy CLI

访问 [CodeBuddy IDE](https://copilot.tencent.com/ide/) 下载安装即可使用。

请先确保本地已安装 Node.js 18.0 及以上版本，再执行以下命令安装 CodeBuddy Code。

```bash
npm install -g @tencent-ai/codebuddy-code
```

安装完成后，您可以执行如下命令检查，输出版本号则表示安装成功。

```bash
codebuddy --version
```

## 配置 Token Plan

1. 找到 CodeBuddy 的配置文件，配置文件路径如下，配置文件不存在时新建即可。

Windows：`C:\\Users\\<用户名>\\.codebuddy\\models.json`。

macOS/Linux：`~/.codebuddy/models.json`。

2. 根据您购买的套餐类型，复制粘贴如下配置到 `models.json` 文件中，并保存。

**说明：**

请您将代码中的 $your\_api\_key 替换为 Token Plan 专属的 API Key。

配置通用 Token Plan

配置 Hy Token Plan

```json

{
  "models": [
    { "id": "tc-code-latest", "name": "Auto", "vendor": "Tencent Cloud 通用 Token Plan", "apiKey": "$your_api_key", "url": "https://api.lkeap.cloud.tencent.com/plan/v3" },
    { "id": "deepseek-v4-flash-202605", "name": "DeepSeek-V4-Flash 正式版 原厂直供", "vendor": "Tencent Cloud 通用 Token Plan", "apiKey": "$your_api_key", "url": "https://api.lkeap.cloud.tencent.com/plan/v3" },
    { "id": "deepseek-v4-pro-202606", "name": "DeepSeek-V4-Pro 正式版 原厂直供", "vendor": "Tencent Cloud 通用 Token Plan", "apiKey": "$your_api_key", "url": "https://api.lkeap.cloud.tencent.com/plan/v3" },
    { "id": "minimax-m2.7", "name": "MiniMax-M2.7", "vendor": "Tencent Cloud 通用 Token Plan", "apiKey": "$your_api_key", "url": "https://api.lkeap.cloud.tencent.com/plan/v3" },
    { "id": "minimax-m3", "name": "MiniMax-M3", "vendor": "Tencent Cloud 通用 Token Plan", "apiKey": "$your_api_key", "url": "https://api.lkeap.cloud.tencent.com/plan/v3" },
    { "id": "glm-5", "name": "GLM-5", "vendor": "Tencent Cloud 通用 Token Plan", "apiKey": "$your_api_key", "url": "https://api.lkeap.cloud.tencent.com/plan/v3" },
    { "id": "glm-5.1", "name": "GLM-5.1", "vendor": "Tencent Cloud 通用 Token Plan", "apiKey": "$your_api_key", "url": "https://api.lkeap.cloud.tencent.com/plan/v3" },
    { "id": "glm-5.2", "name": "GLM-5.2", "vendor": "Tencent Cloud 通用 Token Plan", "apiKey": "$your_api_key", "url": "https://api.lkeap.cloud.tencent.com/plan/v3" },
    { "id": "glm-5.3", "name": "GLM-5.3", "vendor": "Tencent Cloud 通用 Token Plan", "apiKey": "$your_api_key", "url": "https://api.lkeap.cloud.tencent.com/plan/v3" },
    { "id": "glm-5.3-flash", "name": "GLM-5.3-Flash", "vendor": "Tencent Cloud 通用 Token Plan", "apiKey": "$your_api_key", "url": "https://api.lkeap.cloud.tencent.com/plan/v3" },
    { "id": "hy4-preview", "name": "Hy4 preview", "vendor": "Tencent Cloud 通用 Token Plan", "apiKey": "$your_api_key", "url": "https://api.lkeap.cloud.tencent.com/plan/v3" },
    { "id": "kimi-k2.7-code", "name": "Kimi K2.7 Code", "vendor": "Tencent Cloud 通用 Token Plan", "apiKey": "$your_api_key", "url": "https://api.lkeap.cloud.tencent.com/plan/v3" },
    { "id": "kimi-k3", "name": "Kimi K3", "vendor": "Tencent Cloud 通用 Token Plan", "apiKey": "$your_api_key", "url": "https://api.lkeap.cloud.tencent.com/plan/v3" }
  ]
}
```

```json
{
  "models": [
    { "id": "hy3", "name": "Hy3", "vendor": "Tencent Cloud Hy Token Plan", "apiKey": "$your_api_key", "url": "https://api.lkeap.cloud.tencent.com/plan/v3" },
    { "id": "hy4-preview", "name": "Hy4 preview", "vendor": "Tencent Cloud Hy Token Plan", "apiKey": "$your_api_key", "url": "https://api.lkeap.cloud.tencent.com/plan/v3" }
  ]
}
```

## 开始使用

CodeBuddy IDE

CodeBuddy CLI

模型配置完成后，在对话框即可选到配置好的模型进行对话。以下截图以 Hy Token Plan 为例：

![](https://qcloudimg.tencent-cloud.cn/image/document/1eef501e7e055ebf8b7f8b83dcc96bcd.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/1eef501e7e055ebf8b7f8b83dcc96bcd.png)

模型配置完成后执行如下命令启动 CodeBuddy Code。

```bash
codebuddy
```

首次使用 CodeBuddy Code 时，您需要完成登录认证。启动后会显示登录方式选择界面：

```bash
Select login method:
› Log in via Chinese Site
  Log in via International Site
  Log in via Enterprise Domain
  Log in via iOA (Tencent only)
```

登录方式说明如下：

| 登录方式 | 适用场景 | 说明 |
| --- | --- | --- |
| Chinese Site | 中国站用户 | 通过腾讯云中国站 (copilot.tencent.com) 进行认证，支持境内主流模型。 |
| International Site | 国际站用户 | 通过腾讯云国际站 (codebuddy.ai) 进行认证，支持境外主流模型。 |
| Enterprise Domain | 专享版/私有化部署 | 连接企业专享版或自建的 CodeBuddy 服务，需要输入企业提供的服务地址。 |
| iOA | 腾讯内部员工 | 通过腾讯 iOA 零信任系统进行认证，仅限腾讯内部员工使用。 |

使用 ↑↓ 键选择登录方式，按 Enter 确认后会自动打开浏览器完成认证。

输入`/model`，选择模型即可进行对话。
