<!-- Official source: https://cloud.tencent.com/document/product/1823/131901 -->
<!-- Source SHA-256: ebb01d2f10c9897a57d360f7da0dc27d4308688a16545ef10b6bd7dc8d3919df -->

# CodeBuddy Code

官方来源：https://cloud.tencent.com/document/product/1823/131901
最近更新时间：2026-09-07 18:31:15

CodeBuddy Code 是基于腾讯云 AI 技术的智能编程工具，深度集成腾讯云生态，提供从代码编写到项目部署的全链路 AI 辅助。本文以 Hy3 模型为例演示如何将模型接入到 CodeBuddy Code 中使用。

## 安装 CodeBuddy Code

您需要根据实际环境类型安装 CodeBuddy Code，详情请参见 [CodeBuddy Code 安装](https://www.codebuddy.cn/docs/cli/installation)。如果已安装 CodeBuddy Code，可以跳过这一步。

## 获取 API Key

1. 进入 [API Key 管理](https://console.cloud.tencent.com/tokenhub/apikey) 页面，单击**创建 API Key**。操作详情请参见 [创建 API Key](https://cloud.tencent.com/document/product/1823/130090#40882178-aaf2-48c9-8559-dffc083a79bc)。

**注意：**

在设置**可访问范围**时，如果选择“限定范围”，则需要确保勾选 **Hy3**。

2. 创建完成后，请您务必**复制并妥善保管 API Key**，在后续配置到工具的流程中将会使用该信息。

![](https://qcloudimg.tencent-cloud.cn/image/document/f10c6e567870a48a8fe282bdd0988a7c.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/f10c6e567870a48a8fe282bdd0988a7c.png)

## 配置 CodeBuddy Code

1. 找到 CodeBuddy Code 的配置文件，配置文件路径如下，配置文件不存在时新建即可。

Windows：`C:\\Users\\<用户名>\\.codebuddy\\models.json`。

macOS/Linux：`~/.codebuddy/models.json`。

2. 复制粘贴如下配置，并保存。

**说明：**

请将代码中的 `<USER_API_KEY>` 替换为您在 [API Key 管理](https://console.cloud.tencent.com/tokenhub/apikey) 页面获取的 API Key 字符串。该密钥用于身份认证，**请妥善保管，切勿泄露或提交至代码仓库**。

`models.json` 为 CodeBuddy Code 模型配置文件，如已存在则仅需在 `models`、`availableModels` 中追加 `hy3`配置即可，更多相关配置，请参见 [CodeBuddy Code 模型配置](https://www.codebuddy.ai/docs/zh/cli/models)。

CodeBuddy Code 不同版本间的参数配置存在差异，请以实际使用的版本为准。若需配置思考强度相关参数，请参见 [深度思考](https://cloud.tencent.com/document/product/1823/131208)。

```json
   {
     "models": [
       {
         "id": "hy3",
         "name": "hy3",
         "vendor": "Tencent Cloud",
         "apiKey": "<USER_API_KEY>",
         "url": "https://tokenhub.tencentmaas.com/v1"
       }
     ],
     "availableModels": ["hy3"]
   }
```

## 开始使用

配置完成后执行如下命令启动 CodeBuddy Code。

```bash
codebuddy
```

首次使用 CodeBuddy Code 时，会先弹出**信任文件选择**界面，询问是否信任当前工作目录下的项目文件。请按以下建议选择：

**Yes, proceed**（推荐）：仅当您信任当前目录下的所有文件时选择此项。CodeBuddy Code 才能读写项目文件、执行命令辅助开发。

**No, exit**：当前目录包含您不信任或来源不明的代码时选择此项，工具将退出，确保安全。

![](https://qcloudimg.tencent-cloud.cn/image/document/832d25a09ad8f20fbb3a9436b684cc01.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/832d25a09ad8f20fbb3a9436b684cc01.png)

完成登录认证。启动后会显示登录方式选择界面：

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

**说明：**

如果浏览器未自动打开，或登录页面长时间显示 \*Waiting for auth...，可复制终端中显示的登录 URL，手动粘贴到浏览器地址栏完成认证。

认证成功后，**返回 CodeBuddy Code 命令行交互界面**，在输入框中直接输入 `/model` 并按回车，即可进入模型选择列表，选择本文配置的 `hy3` 即可开始使用。

更多关于 CodeBuddy Code 使用，请参见 [CodeBuddy Code 文档](https://www.codebuddy.cn/docs/cli/overview)。
