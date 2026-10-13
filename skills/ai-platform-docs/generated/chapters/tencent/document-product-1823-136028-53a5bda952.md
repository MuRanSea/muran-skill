<!-- Official source: https://cloud.tencent.com/document/product/1823/136028 -->
<!-- Source SHA-256: 7c7bf124ff05035d74b06d682be98d72fdeb09c222a3cbd171d7d73e7720398f -->

# 配额管理

官方来源：https://cloud.tencent.com/document/product/1823/136028
最近更新时间：2026-08-17 21:20:30

## 功能概述

配额管理用于处理模型**默认最大 TPM（每分钟 Token 数）无法满足业务需求**、需要申请更多额度（提配）的场景。

## 查看最大 TPM

[TokenHub 控制台](https://console.cloud.tencent.com/tokenhub) 展示的是**当前生效的配额**——如果该模型曾成功申请过提配，展示的是提配后的额度。可在以下三处查看：

1. [模型广场](https://console.cloud.tencent.com/tokenhub/models) **> 模型详情页 > 模型限制**

![](https://qcloudimg.tencent-cloud.cn/image/document/ffbeff0d407f2514c02f9d72e6edc191)

![](https://qcloudimg.tencent-cloud.cn/image/document/ffbeff0d407f2514c02f9d72e6edc191)

2. [启用管理](https://console.cloud.tencent.com/tokenhub/open-management) **页面**

![](https://qcloudimg.tencent-cloud.cn/image/document/c7c4ea0ed162e136995f8551eb9f8cc1.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/c7c4ea0ed162e136995f8551eb9f8cc1.png)

3. **创建** [自定义推理服务](https://console.cloud.tencent.com/tokenhub/inference/create?regionId=1) **时**

![](https://qcloudimg.tencent-cloud.cn/image/document/55b7c6bc5677815c59d9b2c8cb493b93)

![](https://qcloudimg.tencent-cloud.cn/image/document/55b7c6bc5677815c59d9b2c8cb493b93)

## 申请提配

### 操作入口

1. 登录 [TokenHub 控制台](https://console.cloud.tencent.com/tokenhub)，在左侧导航中选择 [配额管理](https://console.cloud.tencent.com/tokenhub/quota)。

2. 单击**申请提额**。

![](https://qcloudimg.tencent-cloud.cn/image/document/2dd9e1c6ed7f99ec1d976a9f2b905238)

![](https://qcloudimg.tencent-cloud.cn/image/document/2dd9e1c6ed7f99ec1d976a9f2b905238)

### 提配条件

申请提额需同时满足以下条件：

**周峰值利用率 > 60%。**

在控制台限定的额度上限内提额。

单周申请不超过2次。

提交结果：

**满足条件**：申请将直接通过，额度立即更新。

**不满足条件**：申请失败。

**注意：**

配额申请成功后，若该模型连续7天 TPM 利用率均 < 60%，平台将回收超出**保留量**的闲置部分。其中：**保留量 = MAX(周峰值 TPM × 1.4, 1M)**（1M = 1,000,000）。

## 其他情况

对于控制台提额无法满足需求的场景，请联系商务经理或 [提交工单](https://console.cloud.tencent.com/workorder/category?from=connect-us&source=14&level1_id=1&level2_id=3333&data_title=%E5%A4%A7%E6%A8%A1%E5%9E%8B%E6%9C%8D%E5%8A%A1%E5%B9%B3%E5%8F%B0+TokenHub&level3_id=3334&radio_title=%E4%BD%BF%E7%94%A8%E5%92%A8%E8%AF%A2&queue=3241&scene_code=358184)申请。
