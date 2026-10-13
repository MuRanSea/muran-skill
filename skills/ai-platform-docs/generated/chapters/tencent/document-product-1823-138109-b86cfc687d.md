<!-- Official source: https://cloud.tencent.com/document/product/1823/138109 -->
<!-- Source SHA-256: c82cbc43c375d27289273e46acab5deebf22a77b0df6adf86a050f6ab3e6ca18 -->

# DeepSeek Harness

官方来源：https://cloud.tencent.com/document/product/1823/138109
最近更新时间：2026-09-14 16:21:52

DeepSeek Harness 是 DeepSeek AI 开发的一套用来构建、运行和扩展智能体的应用框架，采用“一切皆插件”的架构。本文以 Hy3 模型为例演示如何将模型接入到 DeepSeek Harness 中使用。

## 安装与启动 DeepSeek Harness

1. 在终端执行以下命令，下载 DeepSeek Harness 并启动其 Web UI：

**注意：**

安装 DeepSeek Harness 前，请确认您已安装 Node.js（建议使用 LTS 版本）。

```bash
npx @deepseek-ai/dsh web
```

2. 在浏览器打开命令输出的访问地址。默认地址为 `http://127.0.0.1:3080`。

## 获取 API Key

1. 进入 [API Key 管理](https://console.cloud.tencent.com/tokenhub/apikey) 页面，单击**创建 API Key**。操作详情请参见 [创建 API Key](https://cloud.tencent.com/document/product/1823/130090#40882178-aaf2-48c9-8559-dffc083a79bc)。

**注意：**

在设置**可访问范围**时，如果选择“限定范围”，则需要确保勾选 **Hy3**。

2. 创建完成后，请您务必**复制并妥善保管 API Key**，在后续配置到工具的流程中将会使用该信息。

![](https://qcloudimg.tencent-cloud.cn/image/document/f80357b19af7522ad21ba0389e3b4dae.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/f80357b19af7522ad21ba0389e3b4dae.png)

## 配置 DeepSeek Harness

1. 在 DeepSeek Harness Web UI 中，单击左下角**设置**。

2. 在左侧导航栏选择**模型**，单击**添加自定义提供方**，按下面信息填写完成提供方的创建。

![](https://qcloudimg.tencent-cloud.cn/image/document/5e7c584e05248907195358fad749bad5.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/5e7c584e05248907195358fad749bad5.png)

**Provider ID**：自定义设置，后续如需重命名则需要添加新的提供方，并删除旧的提供方。

**显示名称**：自定义设置。

**API 地址、API 协议**：

<table><colgroup><col/><col/><col/></colgroup><tbody><tr><td><div>站点</div></td><td colspan="1" rowspan="1"><div>API 协议</div></td><td><div>API 地址</div></td></tr><tr><td colspan="1" rowspan="3"><div>广州</div></td><td colspan="1" rowspan="1"><div>openai-completions</div></td><td><div><code>https://tokenhub.tencentmaas.com/v1</code></div></td></tr><tr><td colspan="0" rowspan="0"><div></div></td><td colspan="1" rowspan="1"><div>openai-responses</div></td><td><div><code>https://tokenhub.tencentmaas.com/v1</code></div></td></tr><tr><td colspan="0" rowspan="0"><div></div></td><td colspan="1" rowspan="1"><div>anthropic-messages</div></td><td><div><code>https://tokenhub.tencentmaas.com</code></div></td></tr><tr><td colspan="1" rowspan="3"><div>新加坡</div></td><td colspan="1" rowspan="1"><div>openai-completions</div></td><td colspan="1" rowspan="1"><div><code>https://tokenhub-intl.tencentmaas.com/v1</code></div></td></tr><tr><td colspan="0" rowspan="0"><div></div></td><td colspan="1" rowspan="1"><div>openai-responses</div></td><td colspan="1" rowspan="1"><div><code>https://tokenhub-intl.tencentmaas.com/v1</code></div></td></tr><tr><td colspan="0" rowspan="0"><div></div></td><td colspan="1" rowspan="1"><div>anthropic-messages</div></td><td colspan="1" rowspan="1"><div><code>https://tokenhub-intl.tencentmaas.com</code></div></td></tr></tbody></table>

**API 密钥**：填写您从控制台获取的 **API Key**。

**添加模型**：按需添加 hy3 或当前站点支持的其他模型，详细模型清单请参见 [模型列表](https://cloud.tencent.com/document/product/1823/130051)。

3. （可选）如果需要让模型支持图片输入，则需要在配置文件中进行更改。

单击 **打开配置文件**，路径`$DSH_HOME/settings.yaml`。

![](https://qcloudimg.tencent-cloud.cn/image/document/6b221fdaf5e283b8b91fe2f4e2452f18.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/6b221fdaf5e283b8b91fe2f4e2452f18.png)

在模型配置部分加上 `input: [text, image]`，配置示例如下，保存后生效。

![](https://qcloudimg.tencent-cloud.cn/image/document/b1c3d0212e1eef186fad4f0096764360.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/b1c3d0212e1eef186fad4f0096764360.png)

## 使用 DeepSeek Harness

1. 在页面中点击**选择一个工作区开始**，添加您启动 dsh 时所在的项目目录。选中工作区后，会话输入框才可用。

2. 在输入框右下角，选择要使用的模型。

3. 在输入框输入需求即可开始使用 DeepSeek Harness。

## 常见问题

#### **1. 可以同时使用多个地域吗？**

可以。每个地域对应一个独立提供方 + 独立 API Key，重复“添加自定义提供方”步骤即可。如果需要在同一会话中跨地域切换模型，添加多个提供方后在输入框右下角切换。

#### **2. 调用时报** `No free trial quota` **或** `INSUFFICIENT_BALANCE`**？**

模型无免费试用额度，需在控制台开通按量付费并确保账户余额充足。开通后重试即可。

#### **3. 可以同时配置 Token Plan 套餐和按量付费吗？**

可以。两者使用不同的端点和不同的 API Key，分别“添加自定义提供方”互不冲突。注意 Token Plan 套餐端点带 `/plan/` 前缀，按量付费不带。
