<!-- Official source: https://cloud.tencent.com/document/product/1823/130054 -->
<!-- Source SHA-256: 0f4d36c70f76ac9cb76d3732500f871d94790b1f9efbbbe0e70dbc3aa71192df -->

# 计费方式

官方来源：https://cloud.tencent.com/document/product/1823/130054
最近更新时间：2026-09-18 14:22:00

大模型服务平台 TokenHub 中，不同的模型计费方式可能有所不同，以下为您介绍各类型模型的计费方式，您也可以从 [模型广场](https://console.cloud.tencent.com/tokenhub/models) 进入模型详情页查看每个模型的计费规则。

## 语言模型

| 计费项 | 计费模式 | 计费单位 | 说明 |
| --- | --- | --- | --- |
| 推理输入 | 后付费 | 元/百万 tokens | 用户输入文本（含 system prompt）的 Token 消耗 |
| 推理输出 | 后付费 | 元/百万 tokens | 模型生成文本的 Token 消耗 |
| 缓存输入 | 后付费 | 元/百万 tokens | 命中缓存的输入 Token 消耗 |

**计费说明**：

输入 Tokens 和输出 Tokens 分别计价，不同模型的单价不同，请参见 [模型价格（语言模型）](https://cloud.tencent.com/document/product/1823/130055#fe64a45e-7f1e-4442-9abf-191dbdb5475d)。

当推理请求中断（包括用户主动中断或其他原因导致的被动中断）时，服务端已生成但未完成输出的 Token 也会计费。

部分模型支持**分段定价**（如不同输入长度段对应不同单价）。

Token 估算：中文约 1.8 字符 ≈ 1 Token，英文约 0.75 单词 ≈ 1 Token，该估算仅适用于文字模型，不适用于视觉模型；

## 视觉模型

### 图片生成

| 模型类别 | 计费模式 | 计费单位 | 说明 |
| --- | --- | --- | --- |
| 图片生成 | 后付费 | 元/百万 tokens | 按每张图片生成消耗的 Token 用量计费 |

**计费说明：**

按生成图片的实际消耗 Tokens 计费，详细价格信息请参见 [模型价格](https://cloud.tencent.com/document/product/1823/130055#56b6dc6d-6a32-47a6-901d-5660b2dd86cb)。

不同模型，不同分辨率可能消耗不同的 Tokens 数。

批量生成（如一次生成 4 张）按实际生成张数计费，未成功返回可用结果的任务不计费；用户主动取消、已产生部分结果、超时重试及重复提交的计费规则以最终返回结果的图片张数为准。

### 视频生成

<table><colgroup><col/><col/><col/><col/></colgroup><tbody><tr><td><div>计费项</div></td><td><div>计费模式</div></td><td><div>计费单位</div></td><td><div>说明</div></td></tr><tr><td colspan="1" rowspan="2"><div>视频生成</div></td><td colspan="1" rowspan="2"><div>后付费</div></td><td><div>元/百万 tokens</div></td><td><div><b>MiniMax、Kling、Vidu、PixVerse 系列 </b>模型按视频生成视频 <b>消耗的 Token 用量 </b>计费。</div></td></tr><tr><td colspan="0" rowspan="0"><div></div></td><td colspan="0" rowspan="0"><div></div></td><td><div>元/秒</div><div>积分/秒</div></td><td><div><b>HY、YT 系列 </b>模型按<b>秒/积分</b>计费。</div></td></tr></tbody></table>

**计费说明：**

各模型的具体计费单位和单价以模型价格页及控制台调用前展示为准。

各模型具体计费规则，详见 [模型价格（视频生成）](https://cloud.tencent.com/document/product/1823/130055#video-generation-price-section)。

按生成视频的实际 Token 或 时长（秒）计费，详细价格信息请参考 [模型价格（视频生成）](https://cloud.tencent.com/document/product/1823/130055#video-generation-price-section)。

不同模型和分辨率可能消耗不同的 Tokens 或 积分数。

视频生成模型 Token 用量以模型、参数、时长和实际调用结果为准，不适用于语言模型 Token 估算规则。

未成功返回可用结果的任务不计费，用户主动取消、已产生部分结果、超时重试及重复提交的计费规则以最终返回结果的视频秒数为准。

### 3D 生成

| 计费项 | 计费模式 | 计费单位 | 说明 |
| --- | --- | --- | --- |
| 3D 生成 | 后付费 | 积分/次 | 每次 3D 模型生成调用 |

**计费说明**：

按生成次数计费，不同类型的 3D 任务单价不同，详情请参见 [模型价格（3D 生成）](https://cloud.tencent.com/document/product/1823/130055#f3467bce-0fb1-471f-a528-1a4e5885db33)。

模型复杂度（面数、精度等）可能影响计费。

未成功返回可用结果的任务不计费；用户主动取消、已产生部分结果、超时重试及重复提交的计费规则以最终返回结果的模型个数为准。

## 语音模型

<table><colgroup><col/><col/><col/><col/></colgroup><tbody><tr><td><div>计费项</div></td><td><div>计费模式</div></td><td><div>计费单位</div></td><td><div>说明</div></td></tr><tr><td><div>音乐生成</div></td><td><div>后付费</div></td><td><div>元/百万 tokens</div></td><td><div>按每次生成消耗的 Token 用量计费</div></td></tr><tr><td><div>语音合成</div></td><td colspan="1" rowspan="1"><div>后付费</div></td><td colspan="1" rowspan="1"><div>元/百万 tokens</div></td><td><div>按每次生成消耗的 Token 用量计费</div></td></tr><tr><td><div>语音识别</div></td><td colspan="1" rowspan="1"><div>后付费</div></td><td colspan="1" rowspan="1"><div>元/百万 tokens</div></td><td><div>按每次生成消耗的 Token 用量计费</div></td></tr><tr><td><div>AI 配音</div></td><td colspan="1" rowspan="1"><div>后付费</div></td><td colspan="1" rowspan="1"><div>元/百万 tokens</div></td><td><div>按每次生成消耗的 Token 用量计费</div></td></tr></tbody></table>

**计费说明：**

按语音生成模型的实际消耗 Tokens 计费，详情请参见 [模型价格（语音模型）](https://cloud.tencent.com/document/product/1823/130055#voice-generation-price-section)；

不同模型参数可能消耗不同的 Tokens 数；

语音模型 Token 用量以模型、参数、时长和实际调用结果为准，不适用于语言模型 Token 估算规则。

未成功返回可用结果的任务不计费；用户主动取消、已产生部分结果、超时重试及重复提交的计费规则以最终返回结果的音乐首数为准。

## 结算周期

按量计费采用按小时后付费方式，每小时结算一次。

费用出账预计存在 2 - 3 个小时的延时，实际出账时间以账单为准。

## 订阅套餐

| 计费项 | 计费模式 | 计费单位 | 说明 |
| --- | --- | --- | --- |
| Coding Plan 套餐 | 预付费 | 元/月 | 面向 AI 编程场景大模型服务包月订阅套餐。套餐价格请参见 [Coding Plan 价格](https://cloud.tencent.com/document/product/1823/130092#ec59decc-2a32-4a49-9c2a-7c0b9a383a1c)。 |
| 通用 Token Plan 套餐 | 预付费 | 元/月 | 面向龙虾和 AI 编程场景大模型服务包月订阅套餐。套餐价格请参见 [通用 Token Plan 价格](https://cloud.tencent.com/document/product/1823/130060#db4343ca-7f74-4b07-88ff-d088c157bf5d)。 |
| Hy Token Plan 套餐 | 预付费 | 元/月 | 面向 Agent 工作负载设计的专属订阅方案，集成 Hy3 preview 模型，适配 Coding Agent、文档自动化、多步工具调用等工作流，满足开发者对任务完成可靠性与推理成本可控的双重需求。套餐价格请参见 [Hy Token Plan 价格](https://cloud.tencent.com/document/product/1823/130060#ecb3c3e6-35aa-44bc-87dd-663ce622db7a)。 |
| Token Plan 企业版专业套餐 | 预付费 | 元/月 | Token Plan 企业版专业套餐是面向企业/团队的大模型 API 按月预付费套餐，购买一个积分池，调用模型时，按各模型的 Token 单价从积分池中实时扣减，不同模型单价不同，各个模型单价及抵扣逻辑请参见 [专业套餐价格](https://cloud.tencent.com/document/product/1823/130659#fb8617d0-73bf-4d26-878a-8d286636aeac)。 |
| Token Plan 企业版轻享套餐 | 预付费 | 元/月 | Token Plan 企业版轻享套餐为面向企业及团队的大模型月度预付费 API 订阅产品，购买一个 Token 池，调用模型时，按实际请求的 Token 数从 Token 池中实时扣减，详情请参见 [轻享套餐价格](https://cloud.tencent.com/document/product/1823/131173)。 |

## 相关文档

各模型详细定价信息请参见 [模型价格](https://cloud.tencent.com/document/product/1823/130055)。

新人免费额度详情请参见 [新人免费体验包](https://cloud.tencent.com/document/product/1823/130053)。

欠费影响与恢复机制详情请参见 [欠费说明](https://cloud.tencent.com/document/product/1823/130056)。
