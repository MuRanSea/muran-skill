<!-- Official source: https://cloud.tencent.com/document/product/1823/136473 -->
<!-- Source SHA-256: d1b26c30fcb92f951610f583aaf89dce4ea9b663f31e328cfdd3fa658eb50216 -->

# 节省计划

官方来源：https://cloud.tencent.com/document/product/1823/136473
最近更新时间：2026-09-07 18:45:32

## 产品概述

[节省计划](https://cloud.tencent.com/document/product/555/98375)（SP）是腾讯云提供的一种**折扣抵扣模式**，可以抵扣按量付费按小时计费的账单：用户承诺在一定期限内（1个月、3个月、6个月）按月花费一定金额，换取更低的按量付费折扣，帮助客户在保持按量付费灵活性的同时获得较低的按量付费折扣价格。

## 工作原理

用户承诺每月消费一定的金额，在用户每月承诺的范围内的用量适用节省计划折扣价格，超出范围的用量按正常按量价格计费。节省计划会按照用户每月承诺的费用全额收取，即使用户当月的实际使用量未达到承诺金额。

![](https://qcloudimg.tencent-cloud.cn/image/document/d633c0532c94d9deb969526c400ff488.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/d633c0532c94d9deb969526c400ff488.png)

## 产品配置

### 购买方式

TokenHub 节省计划属于**单产品型**，支持两种购买方式：

| 购买方式 | 说明 | 适用场景 |
| --- | --- | --- |
| **按套餐购买** | 一次购买包含多个模型的 TokenHub 套餐，一个节省计划同时覆盖套餐内所有模型的消费。 | 同时使用多个模型的客户 |
| **按单一产品购买** | 单独购买某一个模型的节省计划，仅抵扣该模型的消费，不跨模型共享。 | 用量集中在单一模型的客户 |

### 支持的模型

**按套餐购买 - TokenHub 套餐（包含以下模型）：**

意味着购买一个节省计划即可同时覆盖以下模型的消费，无论实际使用哪个模型产生的费用，都可以被该节省计划抵扣。适合同时使用多个模型的客户，一次购买，全面覆盖。

TokenHub GLM-5.1

TokenHub GLM-5.2

TokenHub DeepSeek-V4-Pro

TokenHub DeepSeek-V4-Flash

TokenHub DeepSeek-V4-Pro-0813

TokenHub DeepSeek-V4-Flash-0731

**按单一产品购买（支持以下模型，单独选择）：**

意味着只针对某一个指定模型购买节省计划，该节省计划仅抵扣该模型的消费，不跨模型共享。适合用量集中在单一模型、希望精准控制折扣范围的客户。

TokenHub GLM-5.1

TokenHub GLM-5.2

TokenHub DeepSeek-V4-Pro

TokenHub DeepSeek-V4-Flash

TokenHub DeepSeek-V4-Pro-0813

TokenHub DeepSeek-V4-Flash-0731

### 支持的地域

| 地域 | 中国站 | 国际站 |
| --- | --- | --- |
| 广州 | 支持 | 支持 |
| 新加坡 | 支持 | 支持 |

**注意：**

不同地域的节省计划不可互相抵扣，请选择客户实际使用的地域购买。中国站（CNY）与国际站（USD）也需分别购买对应的节省计划。

### 承诺消费周期

当前 TokenHub 节省计划支持**按月**承诺消费周期。

### 时长选项

| 时长 | 折扣力度 |
| --- | --- |
| 1个月 | 较低 |
| 3个月 | 居中 |
| 6个月 | 较高 |

### 付费类型

| 付费类型 | 说明 | 折扣力度 |
| --- | --- | --- |
| **全额预付**（推荐） | 一次性支付承诺期内全部费用 | 较高 |
| **部分预付** | 预付50%，剩余按月扣费 | 居中 |
| **零预付** | 预付0%，每月1号自动扣费；需联系商务经理申请开通 | 较低 |

## 折扣信息

TokenHub 节省计划采用**到达阶梯价**，按月承诺金额越高、时长越长、预付越多，折扣越大。

**注意：**

节省计划下单确认后不支持退款，请在购买前仔细评估用量需求。

<table><colgroup><col/><col/><col/><col/><col/><col/><col/><col/><col/><col/></colgroup><tbody><tr><td><div><b>付款方式</b></div></td><td colspan="3"><div><b>全额预付</b></div></td><td colspan="0" rowspan="0"><div></div></td><td colspan="0" rowspan="0"><div></div></td><td colspan="3"><div><b>部分预付</b></div></td><td colspan="0" rowspan="0"><div></div></td><td colspan="0" rowspan="0"><div></div></td><td colspan="3"><div><b>零预付</b></div></td><td colspan="0" rowspan="0"><div></div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>月承诺金额</div></td><td><div>1月</div></td><td><div>3月</div></td><td><div>6月</div></td><td><div>1月</div></td><td><div>3月</div></td><td><div>6月</div></td><td><div>1月</div></td><td><div>3月</div></td><td><div>6月</div></td></tr><tr><td><div>0 - 1万元</div></td><td><div>1.0</div></td><td><div>1.0</div></td><td><div>1.0</div></td><td><div>1.0</div></td><td><div>1.0</div></td><td><div>1.0</div></td><td><div>1.0</div></td><td><div>1.0</div></td><td><div>1.0</div></td></tr><tr><td><div>1万 - 3万元</div></td><td><div>9.4折</div></td><td><div>9.2折</div></td><td><div>9.0折</div></td><td><div>9.6折</div></td><td><div>9.4折</div></td><td><div>9.2折</div></td><td><div>9.8折</div></td><td><div>9.6折</div></td><td><div>9.4折</div></td></tr><tr><td><div>3万 - 10万元</div></td><td><div>9.2折</div></td><td><div>9.0折</div></td><td><div>8.8折</div></td><td><div>9.4折</div></td><td><div>9.2折</div></td><td><div>9.0折</div></td><td><div>9.6折</div></td><td><div>9.4折</div></td><td><div>9.2折</div></td></tr><tr><td><div>10万 - 30万元</div></td><td><div>9.0折</div></td><td><div>8.8折</div></td><td><div>8.6折</div></td><td><div>9.2折</div></td><td><div>9.0折</div></td><td><div>8.8折</div></td><td><div>9.4折</div></td><td><div>9.2折</div></td><td><div>9.0折</div></td></tr><tr><td><div>30万 - 100万元</div></td><td><div>8.8折</div></td><td><div>8.6折</div></td><td><div>8.4折</div></td><td><div>9.0折</div></td><td><div>8.8折</div></td><td><div>8.6折</div></td><td><div>9.2折</div></td><td><div>9.0折</div></td><td><div>8.8折</div></td></tr><tr><td><div>100万元以上</div></td><td><div>8.6折</div></td><td><div>8.4折</div></td><td><div>8.2折</div></td><td><div>8.8折</div></td><td><div>8.6折</div></td><td><div>8.4折</div></td><td><div>9.0折</div></td><td><div>8.8折</div></td><td><div>8.6折</div></td></tr></tbody></table>

以上折扣仅供参考，实际折扣以购买页实时展示及订单确认为准。

**折扣规律总结：**

**时长越长，折扣越大**：6个月 > 3个月 > 1个月

**预付越多，折扣越大**：全额预付 > 部分预付 > 零预付

**承诺金额越高，折扣越大**：到达更高阶梯后全额享受该阶梯折扣（不分段计算）

**折扣覆盖范围**：输入 Token、输出 Token、Cache Token 均适用

## 计费规则

### 抵扣顺序

系统抵扣优先级为：**免费额度 > 节省计划 > 按量付费**。即先用免费额度，用完后扣节省计划，最后使用账户余额。

| 优先级 | 抵扣方式 | 说明 |
| --- | --- | --- |
| ① | 免费额度 | 优先使用账户内免费额度抵扣。 |
| ② | 节省计划 | 免费额度用完后，使用节省计划折扣抵扣。 |
| ③ | 按量付费 | 节省计划覆盖范围外的用量，按正常按量价格计费；可使用代金券、赠送金、现金支付。 |

**注意：**

节省计划折扣与按量付费折扣**不可叠加**，节省计划覆盖的部分不再享受其他折扣；但多个节省计划之间可以叠加购买，共同抵扣消费。

### 开通时间

| 开通方式 | 生效时间 |
| --- | --- |
| **支付后立即开通** | 下单时刻对应的整点开始生效 |
| **指定时间开通** | 用户自定义开始时间 |

### 重要限制

| 限制项 | 说明 |
| --- | --- |
| 退款 | **不支持退款**，请谨慎确认后购买。 |
| 地域切换 | 创建成功后**不支持切换地域。** |
| 单账号上限 | 每个账号最多购买**40个**节省计划。 |
| 适用计费模式 | 仅适用于按量计费（按小时结算）的消费。 |

## 购买指引

### 购买入口

您可以登录腾讯云控制台，前往 [费用中心](https://console.cloud.tencent.com/expense) > **节省计划**页面，单击**购买节省计划**，进行节省计划的购买。

![](https://qcloudimg.tencent-cloud.cn/image/document/88e56039e9cb3bb33f1a3d441abdada1.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/88e56039e9cb3bb33f1a3d441abdada1.png)

### 购买页面

![](https://qcloudimg.tencent-cloud.cn/image/document/b9f326776a1d446dfaea1ea8366977a7.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/b9f326776a1d446dfaea1ea8366977a7.png)

### 按套餐购买

1. 请参考以下配置项进行选择：

| 配置项 | 配置说明 |
| --- | --- |
| 节省计划类型 | 选择**单产品型**。 |
| 选择产品 | 选择**大模型服务平台 TokenHub**。 |
| 地域 | 选择**广州**或**新加坡**。 |
| 可用区 | 选择**全部**。 |
| 购买方式 | 选择**按套餐购买**。 |
| 产品套餐 | 选择 **TokenHub 套餐**。包含6个产品，支持 GLM-5.1、GLM-5.2、DeepSeek-V4-Pro、DeepSeek-V4-Flash、DeepSeek-V4-Pro-0813、DeepSeek-V4-Flash-0731。 |
| 承诺消费周期 | 选择**按月**。 |
| 承诺消费 | 填写每月承诺金额。 |
| 时长 | 选择**1个月、3个月、6个月**。 |
| 付费类型 | 选择**全额预付**（推荐）或其他类型。 |
| 开通服务时间 | 选择**支付后立即开通**或**指定时间开通**。 |

2. 确认费用后，单击**立即购买**。

### 按单一产品购买

1. 请参考以下配置项进行选择：

| 配置项 | 配置说明 |
| --- | --- |
| 节省计划类型 | 选择**单产品型**。 |
| 选择产品 | 选择**大模型服务平台 TokenHub**。 |
| 地域 | 选择**广州**或**新加坡**。 |
| 可用区 | 选择**全部**。 |
| 购买方式 | 选择**按单一产品购买**。 |
| 单一产品 | 选择具体模型。支持 GLM-5.1、GLM-5.2、DeepSeek-V4-Pro、DeepSeek-V4-Flash、DeepSeek-V4-Pro-0813、DeepSeek-V4-Flash-0731。 |
| 承诺消费周期 | 选择**按月**。 |
| 承诺消费 | 填写每月承诺金额。 |
| 时长 | 选择**1个月、3个月、6个月**。 |
| 付费类型 | 选择**全额预付**（推荐）或其他类型。 |
| 开通服务时间 | 选择**支付后立即开通**或**指定时间开通**。 |

2. 确认费用后，单击**立即购买**。

## 常见问题

#### **1. 节省计划不使用时会怎样？**

承诺金额会按月正常扣费，不退差价。建议根据历史用量趋势设置承诺金额，并预留一定弹性空间，避免承诺过高导致未使用部分仍需支付。

#### **2. 用量超过承诺会怎样？**

超出部分按正常按量价格计费，不影响业务，只是超出部分不享受折扣。

#### **3. 可以提前退订吗？**

不支持退订退款，请在购买前确认好用量预期。

#### **4. 多个模型能用一个节省计划覆盖吗？**

可以，请选择**按套餐购买 - TokenHub 套餐**，GLM-5.1、GLM-5.2、DeepSeek-V4-Pro、DeepSeek-V4-Flash 、DeepSeek-V4-Pro-0813、DeepSeek-V4-Flash-0731的消费都可以被抵扣。

#### **5. 可以叠加购买多个节省计划吗？**

可以，同一账号下最多购买40个节省计划，多个节省计划会同时生效，共同抵扣消费。

#### **6. 广州和新加坡的消费可以互相抵扣吗？**

不可以，不同地域需要分别购买对应地域的节省计划。
