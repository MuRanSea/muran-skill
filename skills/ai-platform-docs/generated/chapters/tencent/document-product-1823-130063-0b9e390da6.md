<!-- Official source: https://cloud.tencent.com/document/product/1823/130063 -->
<!-- Source SHA-256: c96b0c535a63e8061bf79c53d327410ed7c4b735693af21f3ebcc93b783e7f36 -->

# AutoClaw

官方来源：https://cloud.tencent.com/document/product/1823/130063
最近更新时间：2026-10-23 15:47:30

AutoClaw 是智谱 AI 推出的零门槛本地 AI 智能体，支持 OpenClaw 核心执行能力，主打普通用户轻松上手。本文介绍如何在 AutoClaw 中配置与使用腾讯云大模型 Token Plan。

AutoClaw 支持通过“**自定义模型**”功能接入任何兼容 OpenAI 协议的第三方模型服务。通过以下配置，可将腾讯云 Token Plan 的模型接入 AutoClaw。

## 前置条件

在开始配置前，请确保您已完成以下准备工作：

1. [订阅 Token Plan 套餐](https://cloud.tencent.com/document/product/1823/130119#bdc49d9b-f68d-4b79-bb5a-0aa694f2624a)。

2. [获取 API Key](https://cloud.tencent.com/document/product/1823/130119#ac6f544e-6de6-46b7-8709-36d777248b34)。

## 操作步骤

### 步骤一：打开 AutoClaw 应用

启动 AutoClaw 应用，进入主界面。

![](https://qcloudimg.tencent-cloud.cn/image/document/4f923a822d34c3935345f74e978ca4f6.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/4f923a822d34c3935345f74e978ca4f6.png)

### 步骤二：进入设置界面

单击左下角**反馈**按钮旁的**设置**，进入设置界面。

![](https://qcloudimg.tencent-cloud.cn/image/document/512f0799c4257710daf01f4116da4811.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/512f0799c4257710daf01f4116da4811.png)

### 步骤三：进入模型配置页面

在设置界面的左侧导航栏中，单击**模型与 API**，进入模型配置页面。页面会显示**内置模型**和**自定义模型**两个区域。

### 步骤四：添加自定义模型

单击右侧**添加自定义模型**，在弹出的**添加模型**对话框中，选择**服务商**为**自定义**，依次填写模型 ID、API Key、Base URL 等信息。

![](https://qcloudimg.tencent-cloud.cn/image/document/73a7a80f3d1f39c0dd5ba2e616486abe.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/73a7a80f3d1f39c0dd5ba2e616486abe.png)

根据您购买的套餐类型，配置项如下：

| 配置项 | 填写说明 |
| --- | --- |
| 服务商 | 选择**自定义** |
| 接口地址 | https://tokenhub.tencentmaas.com/plan/v3（直接复制使用） |
| API 协议类型 | 选择 **OpenAI** |
| API Key | 填写您在腾讯云控制台获取的 API Key，请参见 [获取 API Key](https://cloud.tencent.com/document/product/1823/130119#ac6f544e-6de6-46b7-8709-36d777248b34)。 |
| 模型名称 | 根据您购买的套餐类型，填写您套餐支持的 Model ID。  如果您购买通用 Token Plan 套餐：请参见 [可用模型](https://cloud.tencent.com/document/product/1823/130060#b6fdbed0-897c-475d-a9a1-f9af922027c4)，选择具体的 **Model ID** 配置。  如果您购买 Hy Token Plan 套餐：请参见 [可用模型](https://cloud.tencent.com/document/product/1823/130060#b145766a-c747-42eb-89c2-a04463d20cc5)，选择具体的 **Model ID** 配置。 |

### 步骤五：连通测试

填写完成后，单击**连通测试**，系统会按当前配置真实发起一次请求，验证接口是否可用。当状态显示为**测试成功**时，说明配置正确。

![image_1774007166635.png](https://qcloudimg.tencent-cloud.cn/image/document/4f2c1bbac9d7efcda739c9b3084ba572.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/4f2c1bbac9d7efcda739c9b3084ba572.png)

### 步骤六：添加模型

连通测试成功后，单击**添加**，完成模型的添加。重复第四步至第六步，逐一添加其余模型。

### 步骤七：设为默认模型

返回**模型与 API** 页面，在**自定义模型**列表中找到刚添加的模型，单击**设为默认**，即可将该模型设为默认使用的模型。

![image_1774007288519.png](https://qcloudimg.tencent-cloud.cn/image/document/af10f27f25e3908af6287da5c4754384.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/af10f27f25e3908af6287da5c4754384.png)
