<!-- Official source: https://cloud.tencent.com/document/product/1823/130076 -->
<!-- Source SHA-256: cded531607e0ab311b050c6e05c31e514b5f9b6340458064a6513bea8df303cb -->

# Token Plan 个人版常见问题

官方来源：https://cloud.tencent.com/document/product/1823/130076
最近更新时间：2026-08-31 17:49:28

## 购买及用量额度问题

### 我已经购买了通用 Token Plan（原 Token Plan），还能再购买 Hy Token Plan 吗 ？

可以的。每个主账号（包含其名下的所有子账号）最多可同时持有 2 个​ Token Plan：

1 个通用 Token Plan（不区分 Lite、Standard、Pro、Max 等具体套餐规格）；

1 个 Hy Token Plan（不区分 Lite、Standard、Pro、Max 等具体套餐规格）。

### 如何抵扣我套餐包的用量？

通用 Token Plan 与 Hy Token Plan 共用同一套 API Key 和 URL，系统将根据您调用时指定的 Model ID，自动从支持该 Model ID 的对应套餐包中抵扣额度，详见 [Token Plan 个人版积分用量抵扣规则](https://cloud.tencent.com/document/product/1823/133811)。

### Token Plan 用量额度消耗完了怎么办？

等待下个订阅月用量刷新，或者升级套餐到更高的等级，享用更充裕的配额。

### Token Plan 用量额度消耗完后会转为按量计费吗？

不会。Token Plan 额度耗尽后，继续调用将会失败报错，不会自动转为按量付费。如需继续使用，可升级至更高等级版本获取更多额度，或等待下一订阅周期额度刷新。

### Token Plan 可以使用新人免费体验包吗？

不可以。Token Plan 为独立订阅产品，其计费体系不参与腾讯云大模型服务平台 TokenHub 免费体验包。

## 使用相关问题

### 我已经有通用 Token Plan（原 Token Plan）的 API Key，如果我再购买一个 Hy Token Plan，需要生成新的 API Key 吗？

不用生成新的 API Key，原有的 API Key 可以在两个套餐上一起使用。

### Token Plan 可以生成多个 API Key 吗？

不可以，Token Plan 个人版套餐（含通用 Token Plan 套餐和 Hy Token Plan 套餐）仅支持生成一个 API Key 。

### Token Plan 到期不续费，套餐失效后，重新购买套餐， API Key 能继续使用吗？

从 2026 年 4 月 23 日起，Token Plan 到期失效后，如果您没有主动删除 API Key，重新购买套餐后，可以继续使用该 API Key。

### 是否可以使用模型列表以外的模型？

Token Plan 当前**仅支持套餐内指定的模型**，使用其他模型将会报错。其中，不同系列套餐支持模型如下：

[通用 Token Plan 可用模型列表](https://cloud.tencent.com/document/product/1823/130060#b6fdbed0-897c-475d-a9a1-f9af922027c4)

[Hy Token Plan 可用模型列表](https://cloud.tencent.com/document/product/1823/130060#b145766a-c747-42eb-89c2-a04463d20cc5)

### Token Plan 有并发请求数限制吗？

Token Plan 并发速率与您的套餐等级相关，平台会根据资源进行动态调整，基本原则 Max > Pro > Standard > Lite。

### 不同套餐的模型性能一样吗？

所有套餐的**模型性能一致**。

### Token Plan 套餐是否支持团队协作使用?

目前 Token Plan 主要面向个人开发者。团队协作使用，请使用 [Token Plan 企业版](https://cloud.tencent.com/document/product/1823/130659) 服务。

### 各模型的上下文长度是多少？最大输出长度是多少？

不同模型的相关参数详见 [模型列表](https://cloud.tencent.com/document/product/1823/130051#a102fd18-4592-49ea-899b-d64b511fb297) 信息。

##
