<!-- Official source: https://cloud.tencent.com/document/product/1823/131726 -->
<!-- Source SHA-256: 705b0c680fa5bf26332a1d1cba3587a245e1c32e6abaf5c69d4621aead53c140 -->

# 账单分账

官方来源：https://cloud.tencent.com/document/product/1823/131726
最近更新时间：2026-08-31 15:27:47

本文介绍 TokenHub 的账单维度、账单查看方式，以及如何使用分账账单按 **API Key** 维度、**标签**维度查看资源消耗。

## TokenHub 账单维度

### 账单产生来源

TokenHub 的账单**仅来自付费资源的实际消耗**。当前会产生账单的资源类型包括：

**在线推理服务**：通过 OpenAI Chat Completions / Responses / Anthropic 等接口实时调用模型产生的费用。

**批量推理服务**：通过批量推理任务异步处理大批量请求产生的费用。由于均为购买后按用量计费，账单的标准维度即为**资源维度**，因此账单按“在线推理服务”、“批量推理服务”两类资源分别出账。

### 默认账单的查看方式

由于账单的最终金额会受到代金券、折扣、套餐抵扣等多维度因素影响，**TokenHub 控制台仅展示 Token 用量数据，不展示费用金额**。如需查看实际的费用账单，请前往腾讯云 [费用中心](https://console.cloud.tencent.com/expense)：

1. 登录 [腾讯云费用中心](https://console.cloud.tencent.com/expense)。

2. 在左侧导航选择**费用账单 > 账单查看 > 资源账单**。

3. 通过**产品名称**过滤 `TokenHub`，即可查看按资源维度（在线推理服务、批量推理服务）出账的费用明细。

![](https://qcloudimg.tencent-cloud.cn/image/document/887af57745b49be808d28bd41ce53a16.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/887af57745b49be808d28bd41ce53a16.png)

**说明：**

控制台仅展示 Token 用量统计；折扣、代金券抵扣、最终应付金额等费用相关信息均以费用中心账单为准。

## 按 API Key 维度查看分账账单

**说明：**

API Key 分账仅针对**后付费资源**生效。预付费类资源（如 Token Plan、TPM 保障包等）在购买时已经一次性完成费用支付，无法按 API Key 进行分账。

### 适用场景

TokenHub 当前已支持**按 API Key 维度进行分账**，适合以下场景：

同一应用下分发多把 API Key 给不同模块或环境（如生产、测试），需要分别统计。

向客户或外部合作方分发独立 API Key，需按 Key 计量并对账。

### 查看分账账单

1. 登录 [腾讯云费用中心](https://console.cloud.tencent.com/expense)。

2. 在左侧导航中选择**分账管理 > 分账账单**。

3. 在筛选区将**统计维度**切换为**资源**。

4. 通过**产品名称**过滤 `TokenHub`。

5. 在结果列表中，**资源 ID** 列展示的内容即为 **API Key ID（keyID，完整字符串）**，对应每把 Key 各自的 Token 消耗与费用。

6. **统计周期** 支持按**日**或按**月**切换，便于对账与日常监控。

![](https://qcloudimg.tencent-cloud.cn/image/document/4b4d6ffc2ae1e52dc6a98db4176b0230.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/4b4d6ffc2ae1e52dc6a98db4176b0230.png)

### 使用限制

请注意：

**出账周期为 T+1**：当日的分账数据需在次日出账后方可查看，请避免在当日实时对账。

**存量数据不可查**：分账功能于2026年5月16日上线，**该日期之前的历史用量数据无法在分账账单中查看**。如需历史数据，请使用 TokenHub 控制台的用量统计模块。

## 按标签维度查看分账账单

### 适用场景

除按 API Key 分账外，TokenHub 还支持**按标签维度对在线推理服务、批量推理任务进行分账**，适合以下场景：

按**业务线 / 项目 / 部门**等自定义维度归集和分摊费用，例如同一账号下同时承接多个业务线，需要按业务线核算成本。

同一业务线下创建了多个在线推理服务或批量推理任务（如不同模型、不同环境），需要把它们聚合成一组进行汇总统计。

已经在使用腾讯云分账标签体系，希望把 TokenHub 的费用纳入统一的分账分析视图。

### 操作步骤

#### 1. 在 TokenHub 上为资源设置标签

TokenHub 中的**在线推理服务**和**批量推理任务**都支持设置标签，您可以在以下三类入口完成设置（**同一个资源可以设置多个标签**）：

**创建时设置**

进入 [在线推理](https://console.cloud.tencent.com/tokenhub/inference) 或 [批量推理](https://console.cloud.tencent.com/tokenhub/batch-inference) 页面，单击**新建**进入创建表单，在"标签"配置项中选择已有标签键值对；如还未创建过标签，或需新增标签，可前往 [标签管理](https://console.cloud.tencent.com/tag/taglist) 创建后再返回选择。

**在列表页设置**

进入资源列表页，单击操作列中的**编辑标签**（在线推理还支持勾选多条进行批量编辑）；在弹出的对话框中添加 / 修改 / 删除标签键值对后单击**确定**保存。

**在详情页设置**

进入资源详情页，在"基本信息"区域可看到当前的标签列表，单击标签列表右侧的**编辑**图标即可修改。

**说明：**

标签的**创建**和**键值对管理**统一在腾讯云 [标签管理](https://console.cloud.tencent.com/tag/taglist) 服务中进行；TokenHub 控制台仅负责**绑定**已有标签。

单个标签可以同时绑定多个云资源，单个云资源也可以绑定多个标签。

#### 2. 在费用中心设置分账标签并查看账单

打了标签的资源**默认不会**在账单中按标签维度展示，需要在费用中心把目标标签键**显式标记为分账标签**后才会生效。

设置和查看流程请参见腾讯云官方文档：

[费用中心 - 分账标签](https://cloud.tencent.com/document/product/555/37959)：介绍如何把已有的标签键设置为分账标签、生效时间、回溯规则与使用限制。

[费用中心 - 账单查看（多维度汇总账单）](https://cloud.tencent.com/document/product/555/96169#fed24a30-2d1d-4c34-8996-87ca87048195)：介绍如何在多维度汇总账单中按**标签**维度查看费用，并联动跳转资源账单查看明细。

## 相关文档

[API Key 管理](https://cloud.tencent.com/document/product/1823/130090)

[腾讯云标签管理](https://cloud.tencent.com/document/product/651)

[腾讯云费用中心 - 分账标签](https://cloud.tencent.com/document/product/555/37959)

[腾讯云费用中心 - 账单查看（多维度汇总账单）](https://cloud.tencent.com/document/product/555/96169#fed24a30-2d1d-4c34-8996-87ca87048195)
