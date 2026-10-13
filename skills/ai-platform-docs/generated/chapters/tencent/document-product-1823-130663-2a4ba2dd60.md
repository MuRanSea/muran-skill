<!-- Official source: https://cloud.tencent.com/document/product/1823/130663 -->
<!-- Source SHA-256: 19991962df4b1f64cb0bfe778616258b2bfd4be32e39dd9b4ec91ff48bdf55ab -->

# CodeBuddy

官方来源：https://cloud.tencent.com/document/product/1823/130663
最近更新时间：2026-07-10 19:09:00

CodeBuddy 是腾讯云推出的 AI 辅助编程工具，通过将 AI 深度融入全流程，实现从产品构思到产品发布的一站式高效交付的平台。 产品支持 IDE、插件和 CLI 三种形态，覆盖从专业开发者到零基础用户的全场景需求。本文介绍如何在 CodeBuddy 中配置与使用腾讯云大模型 Token Plan 企业版，适用于 CodeBuddy IDE 和 CodeBuddy CLI。

## 前置条件

在开始配置前，请确保您已完成以下准备工作：

1. [订阅 Token Plan 企业版套餐](https://cloud.tencent.com/document/product/1823/130660#9bad146b-59b9-463a-b9d9-4c21a823f8a5)。

2. [获取模型配置](https://cloud.tencent.com/document/product/1823/130660#e1afdc13-96a1-46ac-b648-fa94ce3a3e7f)。

3. [获取 API Key](https://cloud.tencent.com/document/product/1823/130660#c517dcb2-4a6d-4fbc-9793-a6fc05467143)。

4. 安装 CodeBuddy，您可以按需选择安装 CodeBuddy IDE 或 CLI：

安装 CodeBuddy IDE

安装 CodeBuddy CLI

访问 [CodeBuddy IDE](https://copilot.tencent.com/ide/) 下载并安装即可使用。

请先确保本地已安装 Node.js 18.0 及以上版本，再执行以下命令安装 CodeBuddy CLI。

```bash
npm install -g @tencent-ai/codebuddy-code
```

安装完成后，您可以执行如下命令检查，输出版本号则表示安装成功。

```bash
codebuddy --version
```

## 配置 Token Plan 企业版

1. 找到 CodeBuddy 的配置文件，配置文件路径如下，配置文件不存在时新建即可。

Windows:`C:\\Users\\<用户名>\\.codebuddy\\models.json`。

macOS/Linux:`~/.codebuddy/models.json`。

2. 根据您购买的套餐类型，将如下配置复制粘贴到 `models.json` 文件中，并保存。

**说明：**

请您将代码中的 <USER\_API\_KEY> 替换为您的 API Key。下方配置已根据套餐类型预填了 `models` 列表，可按需保留所需模型。

配置专业套餐

配置轻享套餐

```json
{
  "models": [
    {
      "id": "auto",
      "name": "Auto",
      "vendor": "Tencent Cloud Token Plan 企业版 专业套餐",
      "apiKey": "<USER_API_KEY>",
      "url": "https://tokenhub.tencentmaas.com/plan/v3"
    },
    {
      "id": "glm-5",
      "name": "GLM-5",
      "vendor": "Tencent Cloud Token Plan 企业版 专业套餐",
      "apiKey": "<USER_API_KEY>",
      "url": "https://tokenhub.tencentmaas.com/plan/v3"
    },
    {
      "id": "glm-5.1",
      "name": "GLM-5.1",
      "vendor": "Tencent Cloud Token Plan 企业版 专业套餐",
      "apiKey": "<USER_API_KEY>",
      "url": "https://tokenhub.tencentmaas.com/plan/v3"
    },
    {
      "id": "glm-5.2",
      "name": "GLM-5.2",
      "vendor": "Tencent Cloud Token Plan 企业版 专业套餐",
      "apiKey": "<USER_API_KEY>",
      "url": "https://tokenhub.tencentmaas.com/plan/v3"
    },
    {
      "id": "glm-5-turbo",
      "name": "GLM-5-Turbo",
      "vendor": "Tencent Cloud Token Plan 企业版 专业套餐",
      "apiKey": "<USER_API_KEY>",
      "url": "https://tokenhub.tencentmaas.com/plan/v3"
    },
    {
      "id": "kimi-k2.5",
      "name": "Kimi-K2.5",
      "vendor": "Tencent Cloud Token Plan 企业版 专业套餐",
      "apiKey": "<USER_API_KEY>",
      "url": "https://tokenhub.tencentmaas.com/plan/v3"
    },
    {
      "id": "kimi-k2.6",
      "name": "Kimi-K2.6",
      "vendor": "Tencent Cloud Token Plan 企业版 专业套餐",
      "apiKey": "<USER_API_KEY>",
      "url": "https://tokenhub.tencentmaas.com/plan/v3"
    },
    {
      "id": "kimi-k2.7-code",
      "name": "Kimi K2.7 Code",
      "vendor": "Tencent Cloud Token Plan 企业版 专业套餐",
      "apiKey": "<USER_API_KEY>",
      "url": "https://tokenhub.tencentmaas.com/plan/v3"
    },
    {
      "id": "kimi-k2.7-code-highspeed",
      "name": "Kimi K2.7 Code HighSpeed",
      "vendor": "Tencent Cloud Token Plan 企业版 专业套餐",
      "apiKey": "<USER_API_KEY>",
      "url": "https://tokenhub.tencentmaas.com/plan/v3"
    },
    {
      "id": "minimax-m2.5",
      "name": "MiniMax-M2.5",
      "vendor": "Tencent Cloud Token Plan 企业版 专业套餐",
      "apiKey": "<USER_API_KEY>",
      "url": "https://tokenhub.tencentmaas.com/plan/v3"
    },
    {
      "id": "minimax-m2.7",
      "name": "MiniMax-M2.7",
      "vendor": "Tencent Cloud Token Plan 企业版 专业套餐",
      "apiKey": "<USER_API_KEY>",
      "url": "https://tokenhub.tencentmaas.com/plan/v3"
    },
    {
      "id": "minimax-m3",
      "name": "MiniMax-M3",
      "vendor": "Tencent Cloud Token Plan 企业版 专业套餐",
      "apiKey": "<USER_API_KEY>",
      "url": "https://tokenhub.tencentmaas.com/plan/v3"
    },
    {
      "id": "deepseek-v4-flash",
      "name": "DeepSeek-V4-Flash",
      "vendor": "Tencent Cloud Token Plan 企业版 专业套餐",
      "apiKey": "<USER_API_KEY>",
      "url": "https://tokenhub.tencentmaas.com/plan/v3"
    },
    {
      "id": "deepseek-v4-pro",
      "name": "DeepSeek-V4-Pro",
      "vendor": "Tencent Cloud Token Plan 企业版 专业套餐",
      "apiKey": "<USER_API_KEY>",
      "url": "https://tokenhub.tencentmaas.com/plan/v3"
    },
    {
      "id": "deepseek-v4-flash-202605",
      "name": "DeepSeek-V4-Flash 原厂直供",
      "vendor": "Tencent Cloud Token Plan 企业版 专业套餐",
      "apiKey": "<USER_API_KEY>",
      "url": "https://tokenhub.tencentmaas.com/plan/v3"
    },
    {
      "id": "deepseek-v4-pro-202606",
      "name": "DeepSeek-V4-Pro 原厂直供",
      "vendor": "Tencent Cloud Token Plan 企业版 专业套餐",
      "apiKey": "<USER_API_KEY>",
      "url": "https://tokenhub.tencentmaas.com/plan/v3"
    }
  ]
}
```

```json
{
  "models": [
    {
      "id": "auto",
      "name": "Auto",
      "vendor": "Tencent Cloud Token Plan 企业版 轻享套餐",
      "apiKey": "<USER_API_KEY>",
      "url": "https://tokenhub.tencentmaas.com/plan/v3"
    }
  ]
}
```

## 开始使用

CodeBuddy IDE

CodeBuddy CLI

模型配置完成后，在对话框即可选到配置好的模型进行对话。

模型配置完成后执行如下命令启动 CodeBuddy CLI。

```bash
codebuddy
```

首次使用 CodeBuddy CLI 时，您需要完成登录认证。启动后会显示登录方式选择界面：

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

输入`/model`命令，选择模型即可进行对话。
