<!-- Official source: https://cloud.tencent.com/document/product/1823/135900 -->
<!-- Source SHA-256: 59bd7ebf7f1f7bb4c56809b31e17e95ea6bf20dcd86912732f93f3e53d326715 -->

# 推理模式介绍

官方来源：https://cloud.tencent.com/document/product/1823/135900
最近更新时间：2026-09-08 17:10:42

大模型服务平台 TokenHub 提供按量付费、TPM 预留、模型单元三种推理模式，覆盖从灵活接入、日常生产到吞吐保障、专属资源的不同诉求。本文介绍三种模式的区别，帮助您根据业务场景选择合适的模式。

## 推理模式

### 按量付费

按量付费是平台默认的推理模式。您无需提前预留资源，按照实际消耗的 Token 量后付费，随用随付，适用于业务起步、调用量波动较大或希望灵活控制成本的场景。各模型的按量价格请参见 [模型价格](https://cloud.tencent.com/document/product/1823/130055)。

### TPM 预留

TPM 预留是预付费的吞吐保障模式。您按 kTPM（千 Tokens Per Minute）粒度提前预留吞吐容量，开通后在已购 TPM 额度、适用模型和地域范围内，可提供相应的预留吞吐能力，有助于降低因共享资源高峰导致的限流风险。详细介绍请参见 [TPM 预留](https://cloud.tencent.com/document/product/1823/135901)。

### 模型单元

模型单元是资源独占的专属模型服务模式，为您提供专属推理资源及相应的资源隔离能力，并由平台统一托管运维，适用于对数据安全、资源隔离和专属资源有较高要求的业务场景。具体隔离范围、部署形态、网络边界和安全责任以产品文档及订单约定为准。详细介绍请参见 [模型单元](https://cloud.tencent.com/document/product/1823/135902)。

## 模式对比

| 对比项 | 按量付费 | TPM 预留 | 模型单元 |
| --- | --- | --- | --- |
| 计费模式 | 后付费，按实际 Token 消耗计费 | 预付费，按月购买 | 预付费，按月购买 |
| 保障内容 | 不提供吞吐保障 | 按 kTPM 粒度预留专属吞吐容量 | 专属的单位容量推理资源 |
| 资源形态 | 共享资源 | 共享资源 + 预留吞吐配额 | 专属推理资源 |
| 典型场景 | 业务起步、调用量波动大 | 稳定生产吞吐、高峰防限流 | 资源隔离、数据安全 |
| 开通方式 | 默认开通，无需申请 | 联系商务经理或 [提交工单](https://console.cloud.tencent.com/workorder/category?source=14) | 联系商务经理或 [提交工单](https://console.cloud.tencent.com/workorder/category?source=14) |
| 是否独享资源 | 否 | 否（共享资源 + 预留吞吐配额） | 是 |
| 是否承诺固定吞吐 | 否 | 在已购额度内承诺 | 提供单个单元容量预估，按需扩容 |
| 适用模型/地域 | 全部模型、全部地域 | GLM 5.2（广州） | 通用模型单元 B（广州） |
| 超额或超出保障额度后的处理 | 不适用 | **超出预留的 TPM 按量付费，可用额度受该模型在所属账号下的 TPM 额度限制。** | 超出单元容量后会出现请求错误 |
| 是否支持变配、续费及退费 | 不适用 | 支持变配  暂不支持自动续费（后续版本将支持），退费需提交工单，退款按订单剩余价值计算，具体金额以工单审核结果和订单约定为准 | 支持变配  暂不支持自动续费（后续版本将支持），退费需提交工单，退款按订单剩余价值计算，具体金额以工单审核结果和订单约定为准 |

## 如何选择

![](https://qcloudimg.tencent-cloud.cn/image/document/0d99335cb68aa7bfd76ecc1e89b72fd0.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/0d99335cb68aa7bfd76ecc1e89b72fd0.png)

## 相关文档

[TPM 预留](https://cloud.tencent.com/document/product/1823/135901)

[模型单元](https://cloud.tencent.com/document/product/1823/135902)

[计费方式](https://cloud.tencent.com/document/product/1823/130054)

[模型价格](https://cloud.tencent.com/document/product/1823/130055)
