<!-- Official source: https://cloud.tencent.com/document/product/1823/135902 -->
<!-- Source SHA-256: da34b995ff3043075205b72778854850532242f5637f6bc1f946baa01b562034 -->

# 模型单元

官方来源：https://cloud.tencent.com/document/product/1823/135902
最近更新时间：2026-08-12 17:47:30

## 什么是模型单元

模型单元是大模型服务平台 TokenHub 提供的专属模型服务模式。模型单元为您提供专属推理资源及相应的资源隔离能力，并由平台统一托管运维，适用于对资源隔离有较高要求的业务场景；具体隔离范围、部署形态、网络边界和安全责任以产品文档及订单约定为准。

## 适用场景

**资源隔离**：需要专属推理资源、不与其他用户共享资源的业务。

**稳定专属资源**：需要长期稳定的专属资源，并希望由平台托管运维的生产业务。

## 计费说明

模型单元采用预付费模式，按月购买。价格请参见 [模型单元价格](https://cloud.tencent.com/document/product/1823/130055#0a3a8e19-a642-4756-b884-a9ab2d69b743)。

## 如何使用

**注意：**

模型单元需联系您的商务经理开通后方可使用。

1. 登录 [TokenHub 控制台](https://console.cloud.tencent.com/tokenhub)，在左侧导航选择**推理服务** > **在线推理**。

2. 单击**创建自定义推理服务**。

3. 在模型列表中选择需要使用的模型。

4. 在**计费方式**中选择**按模型单元计费**。

5. 按需配置资源规格、模型单元数量与购买时长。

6. 确认费用预估并同意相关服务协议后提交订单，完成创建。

![](https://qcloudimg.tencent-cloud.cn/image/document/35398a5552218c3bc67cc8f382fbb4fa.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/35398a5552218c3bc67cc8f382fbb4fa.png)

## 注意事项

暂不支持变配。

暂不支持自助退费。如需申请退费，请 [提交工单](https://console.cloud.tencent.com/workorder/category)，退费规则请参见 [预付费云资源退款规则说明](https://cloud.tencent.com/document/product/555/7440)，按订单剩余价值退款，具体退费金额以工单审核结果和订单约定为准。

更多权益边界（是否独享资源、是否承诺固定吞吐、适用模型/地域、超额或超出保障额度后的处理、是否支持变配/续费/退费等）请参见 [推理模式介绍](https://cloud.tencent.com/document/product/1823/135900)。

## 相关文档

[推理模式介绍](https://cloud.tencent.com/document/product/1823/135900)

[TPM 预留](https://cloud.tencent.com/document/product/1823/135901)

[计费方式](https://cloud.tencent.com/document/product/1823/130054)
