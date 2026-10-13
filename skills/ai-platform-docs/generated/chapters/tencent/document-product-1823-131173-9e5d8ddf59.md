<!-- Official source: https://cloud.tencent.com/document/product/1823/131173 -->
<!-- Source SHA-256: 754bfaf0c7754d2f0a0e021d9e8b7f4c02a1051f59e8f806630c548a185f2933 -->

# Token Plan 企业版轻享套餐

官方来源：https://cloud.tencent.com/document/product/1823/131173
最近更新时间：2026-09-03 12:14:41

Token Plan 企业版轻享套餐为面向企业及团队的大模型月度预付费 API 订阅产品，支持采购自定义规格的专属 Token 资源池。同时支持多密钥配额精细化分配，适配轻量化大模型调用需求的团队使用场景。

## 快速开始

已经了解 Token Plan 企业版轻享套餐的用户，可以参照 [快速入门](https://cloud.tencent.com/document/product/1823/130660) 指引快速开始。

## 套餐详情

<table><colgroup><col/><col/></colgroup><tbody><tr><td colspan="1" rowspan="1"><div><b>配置项</b></div></td><td colspan="1" rowspan="1"><div><b>说明</b></div></td></tr><tr><td colspan="1" rowspan="1"><div>套餐规格</div></td><td colspan="1" rowspan="1"><div>支持按月自定义购买 token 额度，单次购买最低 5,000 万 tokens，最终价格及规则请以 <a href="https://console.cloud.tencent.com/tokenhub/tokenplan-e/buy?type=lite">控制台</a> 为准。</div></td></tr><tr><td colspan="1" rowspan="1"><div>刊例价</div></td><td colspan="1" rowspan="1"><div>广州： 5,000 万 tokens 售价 100 元/月</div><div>新加坡：5,000 万 tokens 售价 130 元/月</div></td></tr><tr><td><div>抵扣规则</div></td><td><div>模型调用过程中，将依据实时 Token 消耗从套餐包中抵扣。</div><div><div><b>说明：</b></div><div>缓存命中的输入内容、缓存未命中的输入内容、输出内容所产生的 Token 数，均从套餐包内统一抵扣。建议您密切关注 <a href="https://cloud.tencent.com/document/product/1823/130661#ef9c2063-19f6-489a-baa0-b64f8d652de5">套餐 Token 用量</a> 消耗情况，避免产生超预期的消耗。</div></div></td></tr></tbody></table>

## 购买须知

| **类别** | **说明** |
| --- | --- |
| 购买说明 | Token Plan 企业版套餐一经购买开通，即刻生效，请尽快创建 API Key 并开始使用。 |
| 额度说明 | 在月度计费周期内未使用的积分，将在该计费周期结束时作废，且无法结转到后续周期、无法转让，也无法在任何后续周期内兑换。 |
| 续费说明 | 请在套餐过期前完成续费，否则，**API Key 将失效，**使用该 API Key 的工具/应用/服务将立即无法调用大模型服务。详情请参见 [续费指南](https://cloud.tencent.com/document/product/1823/130661#0d953594-b67d-412d-912b-cada2d7a549b)。 |

## 可用模型

<table><colgroup><col/><col/></colgroup><tbody><tr><td colspan="1" rowspan="1"><div><b>Model Name</b></div></td><td colspan="1" rowspan="1"><div><b>Model ID</b></div></td></tr><tr><td colspan="1" rowspan="1"><div>Auto 智能路由模型</div></td><td colspan="1" rowspan="1"><div>auto</div></td></tr></tbody></table>

## 接入地址

针对不同的地域，平台提供了不同的接入地址，以便于为您提供稳定的接入。默认接入地址如下：

**注意：**

请根据服务开通的地域选择对应的接口地址，不支持跨地域、跨站点调用服务。

| 地域 | 接入地址 | 资源调度范围 |
| --- | --- | --- |
| 广州 | Base URL  兼容 OpenAI 接口协议工具：`https://tokenhub.tencentmaas.com/plan/v3`  兼容 Anthropic 接口协议工具：`https://tokenhub.tencentmaas.com/plan/anthropic`  完整 URL  兼容 OpenAI Chat Completions 接口协议工具：`https://tokenhub.tencentmaas.com/plan/v3/chat/completions`  兼容 OpenAI Responses 接口协议工具：`https://tokenhub.tencentmaas.com/plan/v3/responses`  兼容 Anthropic 接口协议工具：`https://tokenhub.tencentmaas.com/plan/anthropic/v1/messages` | 中国大陆 |
| 新加坡 | Base URL  兼容 OpenAI 接口协议工具：`https://tokenhub-intl.tencentmaas.com/plan/v3`  兼容 Anthropic 接口协议工具：`https://tokenhub-intl.tencentmaas.com/plan/anthropic`  完整 URL  兼容 OpenAI 接口协议工具：`https://tokenhub-intl.tencentmaas.com/plan/v3/chat/completions`  兼容 OpenAI Responses 接口协议工具：`https://tokenhub-intl.tencentmaas.com/plan/v3/responses`  兼容 Anthropic 接口协议工具：`https://tokenhub-intl.tencentmaas.com/plan/anthropic/v1/messages` | 全球 |

## 配额与限制

### 配额

| **配额** | **说明** |
| --- | --- |
| API Key 创建数量 | 每个套餐包每 5,000 万 tokens 可创建 1 个 API Key。 |
| API Key 配置修改次数 | 每个 API Key 每日最多可修改 10 次。 |

### 限制

Token Plan 企业版轻享套餐不支持降配。

Token Plan 企业版轻享套餐一经购买不支持退订。

## 更多操作

API Key 管理、用量查询、套餐升配、续费等请参见 [操作指南](https://cloud.tencent.com/document/product/1823/130661)。
