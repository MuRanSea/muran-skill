<!-- Official source: https://cloud.tencent.com/document/product/1823/136045 -->
<!-- Source SHA-256: 18146934da451e6400fd67b03f7feae1684d770b47e846974facd9306b3176cc -->

# DeepSeek Harness

官方来源：https://cloud.tencent.com/document/product/1823/136045
最近更新时间：2026-08-18 15:29:00

DeepSeek Harness 是 DeepSeek AI 开发的一套用来构建、运行和扩展智能体的应用框架，采用“一切皆插件”的架构。本文介绍如何在 DeepSeek Harness 中配置与使用腾讯云大模型 Token Plan 企业版。

## 前置条件

在开始配置前，请确保您已完成以下准备工作：

1. [订阅 Token Plan 企业版套餐](https://cloud.tencent.com/document/product/1823/130660#9bad146b-59b9-463a-b9d9-4c21a823f8a5)。

2. 获取模型配置：

2.1 [专业套餐模型配置](https://cloud.tencent.com/document/product/1823/130659#cde5404a-a7bb-4d53-acba-6e3b1b6b8264)。

2.2 [轻享套餐模型配置](https://cloud.tencent.com/document/product/1823/131173#b18f9f4d-fad3-49a9-a38e-2ef38854fa19)。

3. [获取 API Key](https://cloud.tencent.com/document/product/1823/130660#c517dcb2-4a6d-4fbc-9793-a6fc05467143)。

4. 您已安装 Node.js（建议使用 LTS 版本）。

## 配置 Token Plan 企业版

1. 在终端执行以下命令，下载 DeepSeek Harness 并启动其 Web UI。

```javascript
npx @deepseek-ai/dsh web
```

2. 在浏览器打开命令输出的访问地址。默认地址为 `http://127.0.0.1:3080`。

3. 在 DeepSeek Harness Web UI 中，单击左下角**设置**。

![](https://qcloudimg.tencent-cloud.cn/image/document/ef5587f28b4e3ce5093d79d109ce29a6.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/ef5587f28b4e3ce5093d79d109ce29a6.png)

4. 在左侧导航栏选择**模型**，单击**添加自定义提供方**，按下面信息填写完成提供方的创建。

Provider ID ：自定义设置，后续如需重命名则需要添加新的提供方，并删除旧的提供方。

显示名称 ：自定义设置。

API 地址 、API 协议 ：支持的 API 地址、API 协议及对应关系如下：

| API 协议 | API 地址 |
| --- | --- |
| openai-completions | https://tokenhub.tencentmaas.com/plan/v3 |
| openai-responses | https://tokenhub.tencentmaas.com/plan/v3 |
| anthropic-messages | https://tokenhub.tencentmaas.com/plan/anthropic |

API 密钥 ：填写您的密钥。

添加模型 ：按需添加套餐支持的模型 ，支持模型请参见：

[专业套餐模型配置](https://cloud.tencent.com/document/product/1823/130659#cde5404a-a7bb-4d53-acba-6e3b1b6b8264)

[轻享套餐模型配置](https://cloud.tencent.com/document/product/1823/131173#b18f9f4d-fad3-49a9-a38e-2ef38854fa19)

![](https://qcloudimg.tencent-cloud.cn/image/document/a7b09c09455665b2222a8056fa1eee0f.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/a7b09c09455665b2222a8056fa1eee0f.png)

## 使用 DeepSeek Harness

1. 在页面中点击**选择一个工作区开始**，添加您启动 dsh 时所在的项目目录。选中工作区后，会话输入框才可用。

2. 在输入框右下角，选择要使用的模型。

3. 在输入框输入需求即可开始使用 DeepSeek Harness。

![](https://qcloudimg.tencent-cloud.cn/image/document/97afbc95e5eee0af195e22a75849940f.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/97afbc95e5eee0af195e22a75849940f.png)
