<!-- Official source: https://cloud.tencent.com/document/product/1823/131927 -->
<!-- Source SHA-256: e16066333f87b3b91242f72bb7cc0ae2867ebe1113248de493f073732e6d44a2 -->

# Hermes Agent

官方来源：https://cloud.tencent.com/document/product/1823/131927
最近更新时间：2026-07-06 14:12:22

Hermes Agent 是 Nous Research 开源的自主 AI 智能体框架，您可以将其部署在本地服务器上，接入多种大模型，它能跨会话记忆、自动创建技能并持续自我进化，完成复杂的自动化任务。本文以 Hy3 模型为例演示如何将模型接入到 Hermes Agent 中使用。

## 安装 Hermes Agent

您需要根据实际环境类型安装 Hermes Agent，详情请参见 [Hermes Agent 安装](https://github.com/nousresearch/hermes-agent#quick-install)。如果已安装 Hermes Agent，可以跳过这一步。

## 获取 API Key

1. 进入[API Key 管理](https://console.cloud.tencent.com/tokenhub/apikey) 页面，单击**创建 API Key**。操作详情请参见 [创建 API Key](https://cloud.tencent.com/document/product/1823/130090#40882178-aaf2-48c9-8559-dffc083a79bc)。

**注意：**

在设置**可访问范围**时，如果选择“限定范围”，则需要确保勾选 **Hy3**。

2. 创建完成后，请您务必**复制并妥善保管 API Key**，在后续配置到工具的流程中将会使用该信息。

![](https://qcloudimg.tencent-cloud.cn/image/document/654b883e1243be9e2757c4eaebaaba29.png)

## 配置 Hermes Agent

**注意：**

配置步骤可能随 Agent 版本有所调整，请以您使用的版本为准。

1. 打开终端，运行以下命令：

```bash
hermes setup
```

2. 若您为安装后首次启动，终端会显示如下信息，选择 `Full setup`。

![](https://qcloudimg.tencent-cloud.cn/image/document/04a99166d132210d2b6d84e5e75482ac.png)

**注意：**

若您之前已配置过 Hermes Agent，则运行 hermes setup 后，终端输出可能如下图示意，此时选择 Model & Provider 即可进入模型配置。

![](https://qcloudimg.tencent-cloud.cn/image/document/e2da36c2d33434638c0b3c28a91ea0e9.png)

3. 完成选择后，终端将展示可选的模型 Provider，选择 `Tencent TokenHub (Hy3 via tokenhub.tencentmaas.com)`，按回车键确认。

![](https://qcloudimg.tencent-cloud.cn/image/document/bbd46ab717606bf2963b26c727927524.png)

4. 配置模型信息：根据终端指引逐步填写相关配置。

| **终端提示信息** | **配置内容** |
| --- | --- |
| API base URL [e.g. https://api.example.com/v1]: | https://tokenhub.tencentmaas.com/v1 |
| API key [optional]: | 填写对应的 API Key |

![](https://qcloudimg.tencent-cloud.cn/image/document/4334da030e2347362261d8fa8ea065a8.png)

## 使用 Hermes Agent

完成配置后，在终端执行 `hermes` 命令，即可启动 Hermes 并使用 Hy3 进行对话。

![](https://qcloudimg.tencent-cloud.cn/image/document/38569ce73351fdde1483fa605daacca6.png)

**说明：**

Hy3 默认为极速响应（no\_think）模式，受 Hermes Agent 当前适配限制，暂不支持切换思考模式。
