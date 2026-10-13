<!-- Official source: https://cloud.tencent.com/document/product/1823/131905 -->
<!-- Source SHA-256: d4eb1acb22a6d7d443d0173aefe6e7d6e2f57e975a114991e6cc16bb116df786 -->

# Roo Code

官方来源：https://cloud.tencent.com/document/product/1823/131905
最近更新时间：2026-07-06 14:12:57

Roo Code 是一款用于智能编程的 VS Code 插件，本文以 Hy3 模型为例演示如何将模型接入到 Roo Code 中使用。

## 安装 Roo Code

如果已安装 Roo Code，可以跳过这一步。

在 IDE 中搜索安装 Roo Code 插件，下面以 VS Code 为例展示安装配置过程，安装完成后建议重启 VS Code 客户端。

![](https://qcloudimg.tencent-cloud.cn/image/document/af4600dca19e49db4560e2e8d0e9f01d.png)

## 获取 API Key

1. 进入 [API Key 管理](https://console.cloud.tencent.com/tokenhub/apikey) 页面，单击**创建 API Key**。操作详情请参见 [创建 API Key](https://cloud.tencent.com/document/product/1823/130090#40882178-aaf2-48c9-8559-dffc083a79bc)。

**注意：**

在设置**可访问范围**时，如果选择“限定范围”，则需要确保勾选 **Hy3**。

2. 创建完成后，请您务必**复制并妥善保管 API Key**，在后续配置到工具的流程中将会使用该信息。

![](https://qcloudimg.tencent-cloud.cn/image/document/ceac7e5eb69b58d01fd4526459720f4d.png)

## 配置 Roo Code

1. 打开 VS Code，选择左侧边栏的 Roo Code 图标。

**注意：**

若您是首次启动 Roo Code，会先弹出使用模式选择界面（如 Code、Architect、Ask 等），请按需选择并完成首次设置后，再继续后续步骤。

2. 选择第三方供应商。

![](https://qcloudimg.tencent-cloud.cn/image/document/07b26d114572c48ad803254fccc2f6e4.png)

3. 开始配置以下信息。请注意，如果您之前使用过 Roo Code，可直接单击主界面右上角的设置按钮进行配置增加/修改。

**API 提供商**：选择 `OpenAI Compatible`（接口兼容 OpenAI 标准）。

**OpenAI 基础 URL**：`https://tokenhub.tencentmaas.com/v1`

**API 密钥**：填写您的 API Key。

**模型**：填写 `hy3` （使用自定义）

**启用推理工作量**：默认为关闭，即极速响应（no\_think），若您需使用 Hy3 的其他思考模式，则需勾选开启，并选择对应推理强度（修改后需重启 VS Code 生效），各推理强度选项和 Hy3 的思考强度的对应关系为：

**低/中**：快速思考（low）

**高/超高**：深度推理（high）

4. 完成配置后，您可以在 Roo Code 中使用 Hy3 进行交互。

![](https://qcloudimg.tencent-cloud.cn/image/document/9d163be0f6db1cfa01767b88e99cfac0.png)
