<!-- Official source: https://cloud.tencent.com/document/product/1823/130103 -->
<!-- Source SHA-256: 050a2460105cf82b942df1417b4ec04838dd5edcd388f154c3c36d18fc71b315 -->

# Coding Plan 常见问题

官方来源：https://cloud.tencent.com/document/product/1823/130103
最近更新时间：2026-06-22 22:27:30

## 购买及用量额度问题

### 可以购买几个 Coding Plan ？

同一主账号同时只能购买一个 Coding Plan 套餐（不区分 Lite 与 Pro 套餐）。如果一个主账号下有多个子账号，则主账号及其子账号合计只能购买一个套餐，且共用该套餐用量。

### 未开通自动续费，Coding Plan 套餐有效期多长？

Coding Plan 套餐自开通时起生效，有效期至次月对应日的同一时间结束。若次月没有对应日期，则有效期至次月最后一日 23:59:59（UTC+8）结束。

例如：2026 年 1 月 30 日 19:02:03购买 Coding Plan，有效期至2026 年 2 月 28 日 23:59:59。

### Coding Plan 用量额度消耗完了怎么办？

每5小时、每周、每订阅月的额度用完后，可等待用量限额刷新。

### Coding Plan 是否支持升配、降配？

Coding Plan 套餐不支持从 Lite 套餐升配 Pro 套餐，也不支持从 Pro 套餐降配到 Lite 套餐。

### Coding Plan 用量额度消耗完后会转为按量计费吗？

不会。Coding Plan 额度耗尽后，继续调用将会失败报错，不会自动转为按量付费。

### Coding Plan 套餐用量额度刷新规则是什么？

每5小时：根据实际请求发生时间，滑动5小时窗口动态刷新。

每周：每周一 00:00:00 重置周限额。

每订阅月：每订阅月到期时间的下一秒重置订阅月限额。如：2026 年 3 月 6 日 19:02:03购买 Coding Plan，在2026 年 4 月 6 日 19:02:03刷新订阅月限额。

### Coding Plan 可以使用腾讯云模型的免费额度吗？

不可以。Coding Plan 为独立订阅产品，其计费体系不参与大模型服务平台 TokenHub 免费额度。

### Coding Plan 套餐是否支持团队协作使用?

目前 Coding Plan 主要面向个人开发者。团队协作使用，请使用 [Token Plan 企业版](https://cloud.tencent.com/document/product/1823/130659) 服务。

### 如何查看 Coding Plan 套餐用量消耗？

可在控制台 [Coding Plan](https://console.cloud.tencent.com/tokenhub/codingplan) 页面，查看套餐每 5 小时、每周、每订阅月的用量使用情况。

![](https://qcloudimg.tencent-cloud.cn/image/document/569e8418fdb90053089d86db50154cd8.png)

### Coding Plan 和 Token Plan 有什么区别？

两款都是平台的大模型服务订阅套餐，Token Plan 是 Coding Plan 的全新升级，Coding Plan 之前是基于 Coding 场景设计的，而 Token Plan 是专门面向龙虾场景和编程场景设计的专属套餐，会有更多套餐档位可选，适合各种使用强度的场景，后续会持续集成在龙虾和编码场景下表现更优的模型，可以满足更多的使用场景。

用量统计方式和周期内使用限制不一样，Token Plan 是基于 Token 用量统计资源消耗，在订阅周内没有滑动窗口限制用量，您可以更灵活使用 Tokens。

### 我已经购买了 Coding Plan，还能再购买 Token Plan 吗？

Coding Plan 和 Token Plan 是独立的两款套餐，可以同时购买，两个套餐的用量和 API Key 都是互相独立的，双套餐权益不冲突。

## 使用相关问题

### 购买后如何获取 API Key ？

您可以在控制台 [Coding Plan](https://console.cloud.tencent.com/tokenhub/codingplan) 页面，获取并复制 Coding Plan **专属 API Key**（格式为 `sk-sp-xxxx`）。

![](https://qcloudimg.tencent-cloud.cn/image/document/3d0a58653250e3448cdb41539c01128f.png)

### Coding Plan 可以生成多个 API Key 吗？

仅支持生成一个 API Key。

### 如何重置 API Key？

您可以在控制台 [Coding Plan](https://console.cloud.tencent.com/tokenhub/codingplan) 页面，单击 API Key 右侧的**重置**。

**注意：**

此操作将立即生成新的 API Key，并使旧 API Key 失效（5 min 左右）。

所有使用旧 API Key 的应用/服务将立即无法调用 API，请确保已准备好更新配置。

重置后无法恢复旧 API Key，请谨慎操作。

### 是否可以使用模型列表以外的模型？

Coding Plan 当前**仅支持使用** [模型列表](https://cloud.tencent.com/document/product/1823/130092#540d21b1-f168-4435-8784-2e8d26331f65) 内的模型，使用其他模型将会报错。

### Coding Plan 有并发请求数限制吗？

Coding Plan 没有额外的并发请求数限制。使用时受套餐用量限制，包括每 5 小时、每周、每订阅月的请求次数上限，具体请参见 [Coding Plan 概述](https://cloud.tencent.com/document/product/1823/130092)。

### Lite 和 Pro 套餐的模型性能一样吗？

Lite 基础套餐与 Pro 高级套餐的**模型性能一致**，2 种套餐仅用量限制不同。

### 各模型的上下文长度是多少？最大输出长度是多少？

<table><colgroup><col/><col/><col/><col/></colgroup><tbody><tr><td colspan="1" rowspan="1"><div><b>模型</b></div></td><td colspan="1" rowspan="1"><div><b>model 参数值</b></div></td><td><div><b>上下文长度（Tokens）</b></div></td><td><div><b>最大输出长度（Tokens）</b></div></td></tr><tr><td colspan="1" rowspan="1"><div>MiniMax-M2.5</div></td><td colspan="1" rowspan="1"><div>minimax-m2.5</div></td><td><div>200k</div></td><td><div>128k</div></td></tr><tr><td colspan="1" rowspan="1"><div>Kimi-K2.5</div></td><td colspan="1" rowspan="1"><div>kimi-k2.5</div></td><td><div>256k</div></td><td><div>256k</div></td></tr><tr><td colspan="1" rowspan="1"><div>GLM-5</div></td><td colspan="1" rowspan="1"><div>glm-5</div></td><td><div>200k</div></td><td><div>128k</div></td></tr></tbody></table>

## 常见错误码

<table><colgroup><col/><col/><col/><col/></colgroup><tbody><tr><td><div><b>错误码</b></div></td><td><div><b>错误信息</b></div></td><td><div><b>可能原因</b></div></td><td><div><b>解决方法</b></div></td></tr><tr><td><div>401</div></td><td><div>unauthorized</div></td><td colspan="1" rowspan="1"><div>Base URL 或者 API Key 配置错误</div></td><td colspan="1" rowspan="1"><div>1.<!-- --> 确认 URL 和 API Key 参考 <a href="https://cloud.tencent.com/document/product/1823/130092#1d36eaac-8121-4a7b-81f6-0b2689b6ce12">Coding Plan 指引</a>正确获取。</div><div>2.<!-- --> 参考 <a href="https://cloud.tencent.com/document/product/1823/130093">Coding Plan 接入 AI 工具</a> 指引，确认 URL 和 API Key 配置正确。</div></td></tr><tr><td colspan="1" rowspan="1"><div>429</div></td><td colspan="1" rowspan="1"><div>tpm rate limit exceeded</div></td><td colspan="1" rowspan="1"><div>系统负载高触发限流</div></td><td colspan="1" rowspan="1"><div>请重试 1-2 次或者切换其他模型。</div></td></tr><tr><td><div>20033</div></td><td><div>invalid model</div></td><td><div>模型名称配置错误</div></td><td><div>跟 <a href="https://cloud.tencent.com/document/product/1823/130092#1d36eaac-8121-4a7b-81f6-0b2689b6ce12">Coding Plan 支持模型</a> 比对，检查配置的模型名称是否正确。</div></td></tr><tr><td><div>20059</div></td><td><div>input length too long</div></td><td><div>输入长度超出了允许范围</div></td><td><div>可通过新建会话解决报错。</div></td></tr><tr><td><div>20097</div></td><td><div>hour allocated quota exceeded</div></td><td><div>每5小时请求额度已用完</div></td><td><div>每 5 小时是滑动窗口限制，遇到此问题可以稍后重试。</div></td></tr><tr><td><div>20097</div></td><td><div>week allocated quota exceeded</div></td><td><div>每周请求额度已用完</div></td><td><div>等待至每周一 00:00:00（UTC+8）额度重置。</div></td></tr><tr><td><div>20097</div></td><td><div>month allocated quota exceeded</div></td><td><div>每个订阅月请求额度已用完</div></td><td><div>等待至下个订阅月的同一时刻（订阅时刻）额度重置。</div></td></tr></tbody></table>
