<!-- Official source: https://cloud.tencent.com/document/product/1823/130095 -->
<!-- Source SHA-256: e11694f4bea9a3e650e27d19883030cbbc0fa08b884a7122790189b623204864 -->

# CodeBuddy Code

官方来源：https://cloud.tencent.com/document/product/1823/130095
最近更新时间：2026-06-22 22:27:30

CodeBuddy Code 是基于腾讯云 AI 技术的智能编程工具，深度集成腾讯云生态，提供从代码编写到项目部署的全链路 AI 辅助。本文介绍如何在 CodeBuddy Code 中配置与使用腾讯云大模型 Coding Plan。

## 前置条件

在开始配置前，请确保您已订阅 Coding Plan 套餐并获取 API Key，可参见 [Coding Plan 概述](https://cloud.tencent.com/document/product/1823/130092)。

## 安装 CodeBuddy Code

请先确保本地已安装 Node.js 18.0 及以上版本，再执行以下命令安装 CodeBuddy Code。

```bash
npm install -g @tencent-ai/codebuddy-code
```

安装完成后，您可以执行如下命令检查，输出版本号则表示安装成功。

```bash
codebuddy --version
```

## 配置 Coding Plan

1. 找到 CodeBuddy Code 的配置文件，配置文件路径如下，配置文件不存在时新建即可。

Windows：`C:\\Users\\<用户名>\\.codebuddy\\models.json`。

macOS/Linux：`~/.codebuddy/models.json`。

2. 复制粘贴如下配置，并保存。

**说明：**

请您将代码中的 <USER\_API\_KEY> 替换为 Coding Plan 专属的 API Key。

```json
{
  "models": [
    {
      "id": "tc-code-latest",
      "name": "Auto",
      "vendor": "Tencent Cloud",
      "apiKey": "<USER_API_KEY>",
      "url": "https://api.lkeap.cloud.tencent.com/coding/v3"
    },
    {
      "id": "minimax-m2.5",
      "name": "MiniMax-M2.5",
      "vendor": "Tencent Cloud",
      "apiKey": "<USER_API_KEY>",
      "url": "https://api.lkeap.cloud.tencent.com/coding/v3"
    },
    {
      "id": "kimi-k2.5",
      "name": "Kimi-K2.5",
      "vendor": "Tencent Cloud",
      "apiKey": "<USER_API_KEY>",
      "url": "https://api.lkeap.cloud.tencent.com/coding/v3"
    },
    {
      "id": "glm-5",
      "name": "GLM-5",
      "vendor": "Tencent Cloud",
      "apiKey": "<USER_API_KEY>",
      "url": "https://api.lkeap.cloud.tencent.com/coding/v3"
    }
  ]
}
```

## 开始使用

配置完成后执行如下命令启动 CodeBuddy Code。

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

输入`/model`，选择模型，下图以 hunyuan-2.0-instruct 为例。

![](https://qcloudimg.tencent-cloud.cn/image/document/61dbe0931890c9b31b4abe954a6f0b7b.png)
