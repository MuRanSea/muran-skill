<!-- Official source: https://cloud.tencent.com/document/product/1823/132279 -->
<!-- Source SHA-256: 7a2affe05c0f7d77802eff30c6e7564034d69eb4d29100c94da02c425d77a5cf -->

# 数据结构

官方来源：https://cloud.tencent.com/document/product/1823/132279
最近更新时间：2026-09-18 02:06:32

## ApiKeyDetail

API 密钥详情

被如下接口引用：DescribeApiKeyList。

| 名称 | 类型 |  描述 |
|------|------|-------|
| ApiKeyId | String | API 密钥 ID。<br/>示例值：ak-20260320-a1b2c3d4 |
| Name | String | 名称。<br/>示例值：my-api-key |
| ApiKey | String | API 密钥值。接口返回脱敏值<br/>示例值：sk-abc***defg |
| Remark | String | 备注。<br/>示例值：test api key |
| Platform | String | 平台类型。当前支持填值：maas<br/>示例值：maas |
| Uin | String | 主账号。<br/>示例值：100000000001 |
| SubUin | String | 子账号。<br/>示例值：100000000002 |
| Status | String | 状态。取值：enable（启用）、disable（禁用）。<br/>示例值：enable |
| BindType | String | 绑定类型。取值：all（全部模型和服务）、model_all_endpoint_custom（全部模型+自定义服务）、model_custom_endpoint_all（自定义模型+全部服务）、model_custom_endpoint_custom（自定义模型+自定义服务）。<br/>示例值：all |
| CreateTime | String | 创建时间。格式：YYYY-MM-DD HH:mm:ss。<br/>示例值：2026-03-01 00:00:00 |
| UpdateTime | String | 更新时间。格式：YYYY-MM-DD HH:mm:ss。<br/>示例值：2026-03-01 00:00:00 |
| AppId | String | 应用 ID。<br/>示例值：1300000001 |
| Editable | Boolean | 是否可编辑。true 表示可编辑，false 表示不可编辑。<br/>示例值：true |
| BindingItems | Array of [BindingItem](#BindingItem) | 绑定资源列表，区分 endpoint 和 model 类型。 |
| IpWhitelist | Array of String | IP 白名单列表。支持 IPv4 和 CIDR 格式。空数组表示不限制 IP。<br/>示例值：["1.1.1.1"] |
| Creator | String | 当Platform为maas时该字段为空<br/>示例值：张三 |
| QuotaSet | Array of [QuotaInfo](#QuotaInfo) | Token 限额信息多维度列表。未配置限额时不返回该字段。 |
| QuotaStatus | String | Token 限额状态。空字符串表示未配置任何限额包；active 表示已配置且当前可用；inactive 表示已配置但额度耗尽<br/>示例值：active |

## BatchCreateFailedItem

批量创建失败项

被如下接口引用：CreateTokenPlanApiKeys。

| 名称 | 类型 |  描述 |
|------|------|-------|
| Index | Integer | 失败项的序号（从 1 开始，对应后缀编号）。<br/>示例值：1 |
| Name | String | 失败项的名称。<br/>示例值：aaa-1-x7k2m9 |
| Reason | String | 失败原因。<br/>示例值：create sub package failed |

## BindingItem

绑定资源项

被如下接口引用：CreateApiKey, DescribeApiKey, DescribeApiKeyList。

| 名称 | 类型 | 必选 | 描述 |
|------|------|----------|------|
| ResourceId | String | 是 | <p>资源 ID（模型 ID 或服务 ID）。</p><br/>示例值：ep-xxx |
| ResourceType | String | 是 | <p>资源类型。取值：endpoint（推理服务）、model（模型）。推荐绑定endpoint，绑定model即将下线。已绑定model的apikey仍可使用，但控制台回显将不会展示模型绑定列表。</p><p>枚举值：</p><ul><li>endpoint： 绑定到endpoint（默认推理服务或自定义推理服务）</li></ul><br/>示例值：endpoint |
| Status | String | 否 | <p>资源状态</p><br/>示例值：pre-offline |

## CreateApiKeysResultItem

批量创建成功项

被如下接口引用：CreateTokenPlanApiKeys。

| 名称 | 类型 |  描述 |
|------|------|-------|
| ApiKeyId | String | APIKey ID。<br/>示例值：ak-tp-20260401-a1b2c3d4 |

## DeleteGlossaryEntryInput

删除术语条目项

被如下接口引用：DeleteGlossaryEntries。

| 名称 | 类型 | 必选 | 描述 |
|------|------|----------|------|
| EntryId | String | 是 | 术语条目 ID。可通过 DescribeGlossaryEntries 接口获取。<br/>示例值：0b93af68c6cdc928b99d5b3fed6a3f93 |

## EndpointCreateDetail

创建推理服务返回的详情信息

被如下接口引用：CreateEndpoint。

| 名称 | 类型 |  描述 |
|------|------|-------|
| PreResourceId | String | 预付费包 id<br/>示例值：free-new-test |

## EndpointDetail

推理服务详情

被如下接口引用：DescribeEndpoint。

| 名称 | 类型 |  描述 |
|------|------|-------|
| EndpointId | String | <p>推理服务 ID。</p><br/>示例值：ep-abcd123 |
| EndpointName | String | <p>服务名称。</p><br/>示例值：测试推理服务 |
| ModelName | String | <p>模型名称。</p><br/>示例值：deepseek-v4-pro |
| ModelId | String | <p>模型 ID。</p><br/>示例值：deepseek |
| Status | String | <p>状态。取值：ACTIVE（使用中）、INACTIVE（停止中）。</p><br/>示例值：ACTIVE |
| ServiceType | String | <p>服务类型。取值：TEXT_GENERATION（文本生成）、IMAGE_GENERATION（图片生成）、VIDEO_GENERATION（视频生成）。</p><br/>示例值：TEXT_GENERATION |
| ChargeType | String | <p>计费方式。取值：FREE（免费体验）、TOKEN（按 Token 计费）</p><p>枚举值：</p><ul><li>FREE： 免费体验</li><li>TOKEN： 按 Token 计费</li></ul><br/>示例值：TOKEN |
| PaymentEnabled | Boolean | <p>是否开启付费计费。true 表示已开启付费资源包，false 表示仅使用免费额度。</p><br/>示例值：true |
| ChargeDetail | String | <p>计费详情信息，JSON 格式字符串。不同 ChargeType 对应不同的 JSON 结构：</p><ul><li>免费额度信息（所有类型均可能包含）：{&quot;FreeQuota&quot;: {&quot;TotalQuota&quot;: 200, &quot;UsedQuota&quot;: 56, &quot;UsagePercent&quot;: 28, &quot;ExpireTime&quot;: &quot;2026-06-15T00:00:00Z&quot;}}</li><li>TPM 类型额外包含：{&quot;Tpm&quot;: {&quot;TpmInputLimit&quot;: 1000, &quot;TpmOutputLimit&quot;: 1000}}</li><li>其他类型：预留扩展。</li></ul><br/>示例值："{}" |
| StopReason | String | <p>停止原因。当状态为 INACTIVE 时返回。取值：FREE_QUOTA_EXHAUSTED（免费额度已用尽）、NO_FREE_PACKAGE（无可用免费包）、INSUFFICIENT_BALANCE（余额不足，格式为 INSUFFICIENT_BALANCE:&lt;待支付资源ID&gt;）、BILLING_ISOLATED（账户欠费隔离）、INTERNAL_ERROR（内部错误）。当值为 INSUFFICIENT_BALANCE 时，冒号后附带待支付的 TPM 包资源 ID，前端可据此引导用户前往对应订单页完成支付。</p><br/>示例值：FREE_QUOTA_EXHAUSTED |
| TPM | Integer | <p>TPM（每分钟 Token 限流）。当推理服务未单独设置时，回退为关联模型的默认 TPM 值。</p><br/>示例值：1000000 |
| AutoAdjustQuota | Integer | <p>自动调整配额</p><br/>示例值：1 |
| RPM | Integer | <p>RPM（每分钟请求数限流）。当推理服务未单独设置时，回退为关联模型的默认 RPM 值。</p><br/>示例值：100 |
| ModelStatus | String | <p>模型状态</p><p>枚举值：</p><ul><li>online： 在线</li><li>pre-offline： 预下线</li><li>discontinued： 停止新购</li><li>maintenance： 维护</li><li>offline： 下线</li></ul><br/>示例值：online |

## GlossaryEntryInput

新建术语条目项

被如下接口引用：CreateGlossaryEntries。

| 名称 | 类型 | 必选 | 描述 |
|------|------|----------|------|
| SourceTerm | String | 是 | 源语言术语。最大 1000 字符。<br/>示例值：云服务器 |
| TargetTerm | String | 是 | 目标语言术语。最大 1000 字符。<br/>示例值：Cloud Server |

## GlossaryEntryItem

术语条目详情

被如下接口引用：CreateGlossaryEntries, DescribeGlossaryEntries, ModifyGlossaryEntries。

| 名称 | 类型 |  描述 |
|------|------|-------|
| EntryId | String | 术语条目 ID。<br/>示例值：0b93af68c6cdc928b99d5b3fed6a3f93 |
| SourceTerm | String | 源语言术语。<br/>示例值：云服务器 |
| TargetTerm | String | 目标语言术语。<br/>示例值：Cloud Server |
| UpdatedAt | Integer | 更新时间。Unix 时间戳（毫秒）。<br/>示例值：1780561971 |

## GlossaryItem

术语库详情

被如下接口引用：DescribeGlossaries。

| 名称 | 类型 |  描述 |
|------|------|-------|
| GlossaryId | String | 术语库 ID。<br/>示例值：glossary-a1b2c3d4 |
| Name | String | 术语库名称。<br/>示例值：my-glossary |
| Description | String | 术语库描述。<br/>示例值：test glossary |
| Source | String | 源语言代码。<br/>示例值：zh |
| Target | String | 目标语言代码。<br/>示例值：en |
| CreatedTime | [Timestamp ISO8601](/document/api/1823/132287) | 创建时间。<br/>示例值：2026-03-01T00:00:00Z |
| UpdatedTime | [Timestamp ISO8601](/document/api/1823/132287) | 更新时间。<br/>示例值：2026-03-01T00:00:00Z |

## Model

模型信息

被如下接口引用：DescribeModelList。

| 名称 | 类型 |  描述 |
|------|------|-------|
| ModelName | String | <p>模型名称</p><br/>示例值：Hy3 preview |
| ModelId | String | <p>模型 ID。</p><br/>示例值：hy3-preview |
| ExtraModelIds | Array of String | <p>模型id别名列表</p><br/>示例值：["deepseek"] |
| DisplayName | String | <p>模型显示名称。</p><br/>示例值：Hy3 preview |
| Description | String | <p>模型描述。</p><br/>示例值：混元 Hy3 preview 面向 Agent 工作负载设计，采用 295B/21B 激活的 MoE 架构。 |
| Summary | String | <p>模型概要。</p><br/>示例值：代码生成、长上下文与 Agent 能力扎实，适合 Coding Agent、文档自动化及多步工具调用工作流 |
| ModelType | String | <p>模型类型。取值：Text（文本）、Vision（视觉）、Multimodal（多模态）、Speech（语音）、Embedding（向量）。</p><p>枚举值：</p><ul><li>Text： 语言模型</li><li>Vision： 视觉模型</li><li>Multimodal： 多模态模型</li></ul><br/>示例值：Text |
| Brand | String | <p>模型品牌。</p><br/>示例值：混元 |
| ModelImage | [ModelImage](#ModelImage) | <p>模型图标。</p> |
| Provider | String | <p>模型供应商。</p><br/>示例值：腾讯云 |
| ProviderIntroduction | String | <p>markdown 原生内容的模型提供方详情</p><br/>示例值：# 模型提供方 - 杭州深度求索人工智能基础技术研究有限公司 |
| Status | String | <p>模型状态。取值：online（上线）、offline（下线）。</p><p>枚举值：</p><ul><li>online ： 上线</li><li>pre-offline： 预下线</li><li>discontinued： 停止新购</li><li>maintenance： 维护中</li></ul><br/>示例值：online |
| Tags | Array of String | <p>标签列表。</p><br/>示例值：[                             "深度思考",                             "文本生成"                         ] |
| ModelChargingInfo | Array of [ModelChargingInfo](#ModelChargingInfo) | <p>计费信息列表。</p> |
| ModelSpec | [ModelSpec](#ModelSpec) | <p>模型规格。</p> |
| ReleaseAt | [Timestamp ISO8601](/document/api/1823/132287) | <p>发布时间。</p><br/>示例值：2026-04-23T00:00:00+08:00 |
| RecommendWeight | Integer | <p>推荐顺序，值越小排序越靠前。</p><br/>示例值：1 |
| ModelAccessInfo | [ModelAccessInfo](#ModelAccessInfo) | <p>模型访问信息。包含模型在各站点和地域的可用性配置。为空时表示未配置地域信息，模型不可用。</p> |
| FreeTrialInfo | [ModelFreeTrialInfo](#ModelFreeTrialInfo) | <p>体验包信息。</p> |
| OfflineAt | [Timestamp ISO8601](/document/api/1823/132287) | <p>模型下线时间，Status=pre-offline 时，会配置模型下线时间</p><br/>示例值：2026-05-02T00:00:00Z |
| DiscontinuedAt | [Timestamp ISO8601](/document/api/1823/132287) | <p>停止新购时间</p><br/>示例值：2026-05-02T00:00:00Z |

## ModelAccessInfo

模型访问信息

被如下接口引用：DescribeModelList。

| 名称 | 类型 |  描述 |
|------|------|-------|
| ModelSiteRegions | Array of [ModelSiteRegion](#ModelSiteRegion) | 各站点的地域可用性列表。为空时表示未配置地域信息，模型不可用。 |

## ModelChargingInfo

模型计费信息

被如下接口引用：DescribeModelList。

| 名称 | 类型 |  描述 |
|------|------|-------|
| Type | String | 计费类型。取值：Uniform（统一计费）、Tiered（阶梯计费）。<br/>示例值：Tiered |
| Name | String | 计费名称，阶梯计费时表示区间标识，统一计费为空。<br/>示例值：0<=输入<32k |
| Scenario | String | 计费场景，用于区分同一产品不同功能的计费。<br/>示例值：在线推理 |
| ChargingItems | Array of [ModelChargingItem](#ModelChargingItem) | 计费条目列表，顺序即前端展示顺序。 |
| ChargeUnit | String | 计费单位。取值：TOKEN（词元）、COUNT（次）、CREDIT（积分）、PICTURE（张）。<br/>示例值：TOKEN |
| Reference | String | 计费参考链接。<br/>示例值：https://cloud.tencent.com/document/product/1804/123461#7aff517a-9178-43a0-9093-9f822dc07739 |

## ModelChargingItem

计费条目

被如下接口引用：DescribeModelList。

| 名称 | 类型 |  描述 |
|------|------|-------|
| PriceName | String | <p>价格维度标识。取值：Input（输入）、Output（输出）、Cache（缓存命中）、Thinking（思考）、BatchInput（批量输入）、BatchOutput（批量输出）、BatchCache（批量缓存命中）、ImageInput（输入图片）、ImageOutput（输出图片）、Search（搜索调用）。</p><br/>示例值：Input |
| DisplayName | String | <p>价格维度展示名，后端直接提供当前语言文本（如 输入、Input），前端无需翻译。</p><br/>示例值：输入 |
| Price | String | <p>价格数值。</p><br/>示例值：1 |
| PriceUnit | String | <p>价格单位，后端直接提供当前语言文本（如 元/百万tokens、元/张、积分/次）。</p><br/>示例值：元/百万tokens |
| PeakPrice | String | <p>高峰价格，为空表示无高峰定价</p><br/>示例值：1 |
| Specification | String | <p>规格描述，例如视觉/语音类模型有值（如 有参考视频 540P、图生视频 首帧 720P、动作控制 1080P、有声-未指定音色），其他模型为空。</p><br/>示例值：有参考视频 540P |
| Usage | String | <p>Token 用量描述，例如视觉/语音类模型有值（如 第1秒 62,500 Tokens，后续每秒 15,625 Tokens），其他模型为空。</p><br/>示例值：第1秒 62,500 Tokens，后续每秒 15,625 Tokens |
| ReferencePrice | String | <p>参考费用/预估费用描述，例如视觉/语音类模型有值（如 第1秒 0.625 元，后续每秒 0.15625 元），其他模型为空。</p><br/>示例值：第1秒 0.625 元，后续每秒 0.15625 元 |

## ModelEndpointView

模型接入点概览信息

被如下接口引用：DescribeModelEndpointList。

| 名称 | 类型 |  描述 |
|------|------|-------|
| EndpointId | String | <p>推理服务 ID。网关默认创建的 id 与模型 id 相同；控制台自定义推理服务以 ep- 开头。</p><br/>示例值：ep-abcd123 |
| EndpointName | String | <p>推理服务名称。未激活时与 ModelId 相同。</p><br/>示例值：测试推理服务 |
| ModelId | String | <p>模型 ID。</p><br/>示例值：deepseek-v4-pro |
| ExtraModelIds | Array of String | <p>模型id别名列表</p><br/>示例值：["deepseek"] |
| ModelName | String | <p>模型名称。</p><br/>示例值：deepseek-v4-pro |
| Status | String | <p>状态。取值：ACTIVE（运行中）、INACTIVE（已停止）。</p><br/>示例值：ACTIVE |
| ModelStatus | String | <p>模型状态</p><p>枚举值：</p><ul><li>online： 在线</li><li>pre-offline： 预下线</li><li>discontinued： 停止新购</li><li>maintenance： 维护中</li><li>offline： 下线</li></ul><br/>示例值：online |
| ServiceType | String | <p>服务类型。固定为 TEXT_GENERATION（文本生成）。</p><br/>示例值：TEXT_GENERATION |
| ChargeType | String | <p>计费方式。取值：FREE（免费体验）、TOKEN（按 Token 计费）。未激活时为空。</p><br/>示例值：FREE |
| PaymentEnabled | Boolean | <p>是否已开启后付费。true 表示已开启，false 表示未开启。未激活时为 false。</p><br/>示例值：true |
| ChargeDetail | String | <p>计费详情信息，JSON 格式字符串，包含免费额度用量等信息。未激活时为空。</p><br/>示例值：{"FreeQuota":{"TotalQuota":1000000,"UsedQuota":27,"UsagePercent":0,"ExpireTime":"2026-08-12T11:03:44Z"}} |
| StopReason | String | <p>停止原因。当状态为 INACTIVE 时返回。取值：FREE_QUOTA_EXHAUSTED（免费额度已用尽）、NO_FREE_PACKAGE（无可用免费包）、INSUFFICIENT_BALANCE（余额不足）、BILLING_ISOLATED（账户欠费隔离）、INTERNAL_ERROR（内部错误）。</p><br/>示例值：FREE_QUOTA_EXHAUSTED |
| RPM | Integer | <p>推理服务的 rpm 限制，没设置就按模型维度 rpm 限制展示</p><br/>示例值：60 |
| TPM | Integer | <p>推理服务的tpm 限制，没设置就按模型维度 tpm 限制展示</p><br/>示例值：1000000 |

## ModelFreeTrialInfo

模型体验包信息

被如下接口引用：DescribeModelList。

| 名称 | 类型 |  描述 |
|------|------|-------|
| RecommendWeight | Integer | 推荐顺序，值越小排序越靠前。为空表示使用模型默认权重。<br/>示例值：1 |
| CapacitySize | Integer | 体验包容量大小。<br/>示例值：1000000 |
| Unit | String | 容量单位。取值：token。<br/>示例值：token |
| ValidityDays | Integer | 有效期天数（如90天）。为空表示不限期。<br/>示例值：90 |

## ModelImage

模型图标信息

被如下接口引用：DescribeModelList。

| 名称 | 类型 |  描述 |
|------|------|-------|
| Url | String | 图标 URL。<br/>示例值：https://qcloudimg.tencent-cloud.cn/raw/672552a315809509bda19ecb65230671.png |

## ModelSiteRegion

模型上线的站点、地域信息

被如下接口引用：DescribeModelList。

| 名称 | 类型 |  描述 |
|------|------|-------|
| Site | String | 站点标识。取值：domestic（国内站）、international（国际站）。<br/>示例值：domestic |
| Regions | Array of String | 该站点下可用的地域列表，遵循腾讯云标准地域编码（如 ap-guangzhou、ap-beijing、ap-singapore、na-siliconvalley 等）。为空数组时表示该站点无可用地域。<br/>示例值：["ap-guangzhou"] |

## ModelSpec

模型规格信息

被如下接口引用：DescribeModelList。

| 名称 | 类型 |  描述 |
|------|------|-------|
| TPM | String | 每分钟处理 Token 数（Tokens Per Minute）。<br/>示例值：1000k |
| QPM | String | 每分钟请求数（Queries Per Minute）。<br/>示例值：60 |
| MaxInputToken | String | 最大输入 Token 长度。<br/>示例值：192k |
| MaxOutputToken | String | 最大输出 Token 长度。<br/>示例值：128k |
| ContextLength | String | 上下文窗口长度。<br/>示例值：256k |
| Concurrency | String | 并发数。<br/>示例值：10 |
| InputDescription | String | 输入要求描述。<br/>示例值：图片分辨率不超过4k (4096*2160)，视频分辨率不超过2k (2048*1080) |

## ModifyGlossaryEntryInput

修改术语条目项

被如下接口引用：ModifyGlossaryEntries。

| 名称 | 类型 | 必选 | 描述 |
|------|------|----------|------|
| EntryId | String | 是 | 术语条目 ID。可通过 DescribeGlossaryEntries 接口获取。<br/>示例值：3a82012132f4da00ab3cf623b43a6aa1 |
| SourceTerm | String | 否 | 源语言术语。最大 1000 字符。不传则保持不变。<br/>示例值：云服务器 |
| TargetTerm | String | 否 | 目标语言术语。最大 1000 字符。不传则保持不变。<br/>示例值：cloud server |

## QuotaCreateItem

Token 限额配置项（创建 API 密钥时用）

被如下接口引用：CreateApiKey。

| 名称 | 类型 | 必选 | 描述 |
|------|------|----------|------|
| CycleUnit | String | 是 | <p>限额周期。取值：d（按日）、m（按月）、lifetime（总额度，不重置）。</p><br/>示例值：m |
| CycleCredits | String | 是 | <p>维度当期限额总量（Token 数），不能大于10万亿。使用字符串避免大数精度丢失。</p><br/>示例值：1000 |
| MonthStartDay | Integer | 否 | <p>月度限额起始日。CycleUnit 为 m 时可选，1~31，默认 1。小月（如 2 月）由下游自动取该月最后一天。</p><br/>示例值：1 |

## QuotaInfo

Token 限额信息

被如下接口引用：DescribeApiKey, DescribeApiKeyList。

| 名称 | 类型 |  描述 |
|------|------|-------|
| PkgId | String | 限额包 ID。<br/>示例值：limit-6xaznx2ke5 |
| Status | Integer | 限额包状态。取值：1（正常）、3（已耗尽）、4（已销毁）。<br/>示例值：1 |
| CycleUnit | String | 限额周期。取值：d（按日）、m（按月）、lifetime（总额度，不重置）。<br/>示例值：d |
| CycleCredits | String | 维度当期限额总量（Token 数）。使用字符串避免大数精度丢失。<br/>示例值：1000 |
| CycleUsed | String | 维度当期已使用量（Token 数）。使用字符串避免大数精度丢失。<br/>示例值：0 |
| StartTime | [Timestamp ISO8601](/document/api/1823/132287) | 限额生效起始时间。<br/>示例值：2026-06-09T00:00:00+08:00 |
| ExpireTime | [Timestamp ISO8601](/document/api/1823/132287) | 限额过期时间。<br/>示例值：2046-06-09T21:12:17+08:00 |

## QuotasDesired

Token 限额期望状态

被如下接口引用：ModifyApiKeyInfo。

| 名称 | 类型 | 必选 | 描述 |
|------|------|----------|------|
| CycleUnit | String | 是 | <p>限额周期，必填。取值：d（按日）、m（按月）、lifetime（总额度）。</p><br/>示例值：m |
| CycleCredits | String | 是 | <p>单周期额度（Token 数），必填，不能大于10万亿。使用字符串避免大数精度丢失。同维度若与现网不同视为升配/降配。</p><br/>示例值：1000 |
| MonthStartDay | Integer | 否 | <p>月度限额起始日。CycleUnit=m 时可选，1~31，默认 1。小月（如 2 月）由下游自动取该月最后一天。已有月度限额包时，更新月起始日视为周期窗口切换，会 delete 旧包后 add 新包，累计额度会重置</p><br/>示例值：2 |

## RequestFilter

过滤条件

被如下接口引用：DescribeApiKeyList, DescribeGlossaries, DescribeModelEndpointList, DescribeTokenPlanApiKeyList, DescribeTokenPlanList。

| 名称 | 类型 | 必选 | 描述 |
|------|------|----------|------|
| Name | String | 是 | 过滤字段名称。<br/>示例值：ResourceType |
| Op | String | 是 | 过滤操作符。取值：EXACT（精确匹配）、FUZZY（模糊匹配）、NOT（排除匹配）。<br/>示例值：EXACT |
| Values | Array of String | 是 | 过滤值列表。最多支持 10 个。<br/>示例值：["model"] |

## RequestSort

排序条件

被如下接口引用：DescribeApiKeyList, DescribeGlossaries, DescribeModelEndpointList, DescribeTokenPlanApiKeyList, DescribeTokenPlanList。

| 名称 | 类型 | 必选 | 描述 |
|------|------|----------|------|
| Name | String | 是 | 排序字段名称。<br/>示例值：CreatedAt |
| Order | String | 是 | 排序方向。取值：ASC（升序）、DESC（降序）。<br/>示例值：DESC |

## SubPackageBalance

API Key 额度及用量信息

被如下接口引用：DescribeTokenPlanApiKey, DescribeTokenPlanApiKeyList。

| 名称 | 类型 |  描述 |
|------|------|-------|
| ExclusiveQuota | String | <p>独占额度。单位说明如下：</p><ul><li>套餐类型为专业套餐，单位取值为积分；</li><li>套餐类型为轻享套餐，单位取值为 token。</li></ul><br/>示例值：500000 |
| ExclusiveUsed | String | <p>独占额度已用量。单位说明如下：</p><ul><li>套餐类型为专业套餐，单位取值为积分；</li><li>套餐类型为轻享套餐，单位取值为 token。</li></ul><br/>示例值：100000 |
| ExclusiveRemain | String | <p>独占额度剩余量。单位说明如下：</p><ul><li>套餐类型为专业套餐，单位取值为积分；</li><li>套餐类型为轻享套餐，单位取值为 token。</li></ul><br/>示例值：400000 |
| SharedQuota | String | <p>共享额度上限，-1 表示不限。单位说明如下：</p><ul><li>套餐类型为专业套餐，单位取值为积分；</li><li>套餐类型为轻享套餐，单位取值为 token。</li></ul><br/>示例值：-1 |
| SharedUsed | String | <p>共享额度已用量。单位说明如下：</p><ul><li>套餐类型为专业套餐，单位取值为积分；</li><li>套餐类型为轻享套餐，单位取值为 token。</li></ul><br/>示例值：50000 |
| SharedRemain | String | <p>共享额度剩余量。单位说明如下：</p><ul><li>套餐类型为专业套餐，单位取值为积分；</li><li>套餐类型为轻享套餐，单位取值为 token。</li></ul><br/>示例值：-1 |
| TotalUsed | String | <p>当前周期已用总量 exclusive_used + shared_used + overflow_used</p><br/>示例值：50000 |
| Status | Integer | <p>API Key 额度包状态。取值：0（正常）、1（耗尽）。</p><br/>示例值：0 |

## TokenPlanApiKeyInfo

Token Plan API Key 详情

被如下接口引用：DescribeTokenPlanApiKey。

| 名称 | 类型 |  描述 |
|------|------|-------|
| ApiKeyId | String | API Key ID。<br/>示例值：ak-tp-20260401-a1b2c3d4 |
| ApiKey | String | API Key 密钥值（脱敏）。<br/>示例值：sk-tp-xxxxxxxx |
| Name | String | API Key 名称。<br/>示例值：生产环境主Key |
| TeamId | String | 所属套餐 ID。<br/>示例值：tp-ent-abcdefgh |
| AppId | String | 账号APP ID。<br/>示例值：1300000001 |
| Uin | String | 主账号 UIN。<br/>示例值：100000000001 |
| AllowedModels | String | API Key 可用模型列表（JSON 数组字符串）。<br/>示例值：["glm-5","kimi-k2.5","tc-code-latest"] |
| Status | String | API Key 是否可用。取值：enable（启用）、disable（停用）。<br/>示例值：enable |
| StopReason | String | API Key 停用原因。取值：NORMAL（正常，默认值），QUOTA_EXHAUSTED（API Key额度包耗尽），ABNORMAL（异常，需人工介入）<br/>示例值：NORMAL |
| UseStatus | String | 用户侧开关。取值：enable（启用）、disable（停用）。<br/>示例值：enable |
| KeyVersion | Integer | 密钥版本号。<br/>示例值：1 |
| LastRotatedAt | [Timestamp ISO8601](/document/api/1823/132287) | 最近一次重置时间。（ISO 8601）<br/>示例值：2026-04-01T00:00:00Z |
| Creator | String | 创建人，如果是子账号创建，则该值为子账号UIN。<br/>示例值：100000000002 |
| CreatedAt | [Timestamp ISO8601](/document/api/1823/132287) | 创建时间。<br/>示例值：2026-04-01T00:00:00Z |
| UpdatedAt | [Timestamp ISO8601](/document/api/1823/132287) | 更新时间。<br/>示例值：2026-04-01T00:00:00Z |
| TPM | Integer | TPM 限制（Tokens Per Minute）。<br/>示例值：1000000 |
| ProductType | String | 套餐类型。取值：enterprise（企业版专业套餐）、enterprise-auto（企业版轻享套餐）<br/>示例值：enterprise |

## TokenPlanApiKeyListItem

Token Plan API Key 列表项

被如下接口引用：DescribeTokenPlanApiKeyList。

| 名称 | 类型 |  描述 |
|------|------|-------|
| ApiKeyId | String | API Key ID。<br/>示例值：ak-tp-20260401-a1b2c3d4 |
| ApiKey | String | API Key 密钥值（脱敏）。<br/>示例值：sk-tp-****xxxx |
| Name | String | API Key 名称。<br/>示例值：生产Key |
| TeamId | String | 所属套餐 ID。<br/>示例值：team-tp-20260401-a1b2c3d4 |
| AppId | String | 账号APP ID。<br/>示例值：1300000001 |
| Uin | String | 主账号 UIN。最大 128 字符。<br/>示例值：100000000001 |
| AllowedModels | String | API Key 可用模型列表（JSON 数组字符串）。<br/>示例值：["glm-5"] |
| Status | String | API Key 是否可用。取值：enable（启用）、disable（停用）。<br/>示例值：enable |
| StopReason | String | API Key 停用原因。取值：NORMAL（正常，默认值），QUOTA_EXHAUSTED（API Key额度包耗尽），ABNORMAL（异常，需人工介入）<br/>示例值：NORMAL |
| UseStatus | String | 用户侧开关。取值：enable（启用）、disable（停用）。<br/>示例值：enable |
| KeyVersion | Integer | 密钥版本号。<br/>示例值：1 |
| LastRotatedAt | [Timestamp ISO8601](/document/api/1823/132287) | 最近一次重置时间。（ISO 8601）<br/>示例值：2026-04-01T00:00:00Z |
| Creator | String | 创建人，如果是子账号创建，则该值为子账号UIN。<br/>示例值：100000000002 |
| CreatedAt | [Timestamp ISO8601](/document/api/1823/132287) | 创建时间。<br/>示例值：2026-04-01T00:00:00Z |
| UpdatedAt | [Timestamp ISO8601](/document/api/1823/132287) | 更新时间。<br/>示例值：2026-04-01T00:00:00Z |
| Balance | [SubPackageBalance](#SubPackageBalance) | API Key 额度用量信息 |
| ProductType | String | 套餐类型。取值：enterprise（企业版专业套餐）、enterprise-auto（企业版轻享套餐）。<br/>示例值：enterprise |

## TokenPlanListItem

Token Plan 套餐列表项

被如下接口引用：DescribeTokenPlanList。

| 名称 | 类型 |  描述 |
|------|------|-------|
| TeamId | String | <p>套餐 ID。</p><br/>示例值：tp-ent-abcdefgh |
| ProductType | String | <p>套餐类型。取值：enterprise（企业版专业套餐）、enterprise-auto（企业版轻享套餐）</p><br/>示例值：enterprise |
| Name | String | <p>套餐名称。最大 128 字符。</p><br/>示例值：生产环境套餐 |
| AppId | String | <p>账号 APP ID。</p><br/>示例值：1300000001 |
| Uin | String | <p>主账号 UIN。</p><br/>示例值：100000000001 |
| Status | String | <p>套餐状态。取值：enable（启用）、disable（停用）。</p><br/>示例值：enable |
| StopReason | String | <p>套餐关停原因。取值：NORMAL（正常）、ISOLATED（隔离/欠费）、FROZEN（冻结）、EXHAUSTED（额度耗尽）、DESTROYED（已销毁）</p><br/>示例值：none |
| ApiKeyMax | Integer | <p>可创建 API Key 上限。</p><br/>示例值：0 |
| ApiKeyCount | Integer | <p>当前已创建的 APIKey 数量</p><br/>示例值：1 |
| PrepayResourceID | String | <p>云计费预付费资源包 ID。</p><br/>示例值：prepay-123 |
| Creator | String | <p>创建人。若为子账号创建的套餐，则该值为子账号UIN。</p><br/>示例值：100000000002 |
| CreatedAt | [Timestamp ISO8601](/document/api/1823/132287) | <p>创建时间。</p><br/>示例值：2026-04-01T00:00:00Z |
| UpdatedAt | [Timestamp ISO8601](/document/api/1823/132287) | <p>更新时间。</p><br/>示例值：2026-04-01T00:00:00Z |
| PackageInfo | [TokenPlanPackageInfo](#TokenPlanPackageInfo) | <p>套餐包基本信息。</p> |
| AutoRenewFlag | Integer | <p>是否开启自动续费。取值：0（未开启），1（开启）</p><br/>示例值：1 |

## TokenPlanPackageInfo

主额度包信息

被如下接口引用：DescribeTokenPlan, DescribeTokenPlanList。

| 名称 | 类型 |  描述 |
|------|------|-------|
| TotalQuota | String | 总额度。根据套餐类型区分单位：credits（企业版专业套餐），tokens（企业版auto套餐）<br/>示例值：1000000 |
| TotalUsed | String | 总已使用额度。根据套餐类型区分单位：credits（企业版专业套餐），tokens（企业版auto套餐）<br/>示例值：100000 |
| TotalCycles | Integer | 总周期数。<br/>示例值：1 |
| CycleUnit | String | 周期单位。取值：month（月）<br/>示例值：month |
| StartTime | [Timestamp ISO8601](/document/api/1823/132287) | 套餐包生效时间。<br/>示例值：2026-04-01T00:00:00Z |
| ExpireTime | [Timestamp ISO8601](/document/api/1823/132287) | 套餐包到期时间。<br/>示例值：2027-04-01T00:00:00Z |
| ExclusiveAllocated | String | 独占池已分配额度。根据套餐类型区分单位：credits（企业版专业套餐），tokens（企业版auto套餐）<br/>示例值：500000 |
| ExclusiveUsed | String | 独占池已用额度。根据套餐类型区分单位：credits（企业版专业套餐），tokens（企业版auto套餐）<br/>示例值：100000 |
| SharedPool | String | 共享池总额度。根据套餐类型区分单位：credits（企业版专业套餐），tokens（企业版auto套餐）<br/>示例值：500000 |
| SharedUsed | String | 共享已用额度。根据套餐类型区分单位：credits（企业版专业套餐），tokens（企业版auto套餐）<br/>示例值：50000 |
| CycleQuota | String | 当期额度。根据套餐类型区分单位：credits（企业版专业套餐），tokens（企业版auto套餐）<br/>示例值：1000000 |
| CurrentCycle | Integer | 当前周期。<br/>示例值：1 |
| RemainCycles | Integer | 剩余周期。<br/>示例值：0 |

## TokenSummary

主包Token总结

被如下接口引用：DescribeTokenPlan。

| 名称 | 类型 |  描述 |
|------|------|-------|
| CycleSeq | Integer | 套餐包当前计费周期序号<br/>示例值：1 |
| CycleStartTime | String | 套餐包计费周期开始时间（RFC3339）<br/>示例值：2026-04-01T00:00:00+08:00 |
| CycleEndTime | String | 套餐包当前计费周期结束时间（RFC3339）<br/>示例值：2026-05-01T00:00:00+08:00 |
| BillingItems | Array of [TokenSummaryBillingItem](#TokenSummaryBillingItem) | 按计费项分组的 token 汇总列表 |

## TokenSummaryBillingItem

Token 汇总计费项

被如下接口引用：DescribeTokenPlan。

| 名称 | 类型 |  描述 |
|------|------|-------|
| BillingItem | String | 计费项。取值：input（输入 Token）、output（输出 Token）、cache（缓存 Token）、call_count（调用次数）。<br/>示例值：input |
| TotalQty | Integer | 该计费项在周期内的原始用量汇总，单位：tokens。<br/>示例值：1500000 |

## UsageDetailItem

Token Plan 企业版套餐调用明细项（字段与 CLS 日志对齐）

被如下接口引用：DescribeTokenPlanApiKeyUsageDetail。

| 名称 | 类型 |  描述 |
|------|------|-------|
| Uin | String | 主账号 UIN。<br/>示例值：700002501094 |
| ModelName | String | 模型名称。<br/>示例值：deepseek-v3.2 |
| ApiKeyId | String | APIKey ID。<br/>示例值：ak-test |
| ApiKeyName | String | APIKey 名称。<br/>示例值：hello-world |
| RequestId | String | 请求 ID。<br/>示例值：test-001 |
| RequestTime | String | 请求时间（RFC3339 格式）。<br/>示例值：2026-04-06T12:00:00Z |
| InputToken | Integer | 输入 token 数。<br/>示例值：1200 |
| CacheToken | Integer | 缓存 token 数。<br/>示例值：100 |
| OutputToken | Integer | 输出 token 数。<br/>示例值：800 |
| TotalToken | Integer | 总 token 数。<br/>示例值：2100 |
| InputQuota | String | 未命中缓存输入消耗额度。单位说明如下：<br/>- 套餐类型为专业套餐（enterprise），单位取值为积分；<br/>- 套餐类型轻享套餐（enterprise-auto），单位取值为 token。<br/>示例值：1000 |
| CacheQuota | String | 缓存消耗额度。单位说明如下：<br/>- 套餐类型为专业套餐（enterprise），单位取值为积分；<br/>- 套餐类型轻享套餐（enterprise-auto），单位取值为 token。<br/>示例值：500 |
| OutputQuota | String | 输出消耗额度。单位说明如下：<br/>- 套餐类型为专业套餐（enterprise），单位取值为积分；<br/>- 套餐类型轻享套餐（enterprise-auto），单位取值为 token。<br/>示例值：500 |
| TotalQuota | String | 总消耗额度。单位说明如下：<br/>- 套餐类型为专业套餐（enterprise），单位取值为积分；<br/>- 套餐类型轻享套餐（enterprise-auto），单位取值为 token。<br/>示例值：2000 |

## UsageRankItem

排行列表中的单个对象用量项，含对象标识、时间周期内的统计值（Stats）和时间周期内的时序点列表（Series，仅 ShowAll=false 时返回）。

被如下接口引用：DescribeUsageRankList。

| 名称 | 类型 |  描述 |
|------|------|-------|
| Rank | Integer | 全局排名（从 1 起）。分页场景下仍为全量排序中的位次，非页内序号<br/>示例值：11 |
| Key | String | 对象标识。apikey 维度为 APIKey ID；endpoint 维度为接入点；model 维度为模型名。<br/>示例值：ak-xxx |
| Name | String | 对象展示名。apikey 维度返回 APIKey 名称（已删除的 APIKey 仍保留原名）；<br/>endpoint / model 维度等于 Key。<br/>示例值：syytest123 |
| Stats | [UsageStats](#UsageStats) | 时间周期内的统计值<br/>注意：此字段可能返回 null，表示取不到有效值。 |
| Series | [UsageSeries](#UsageSeries) | 时间周期内的时序点列表<br/>注意：此字段可能返回 null，表示取不到有效值。 |

## UsageSeries

用量时间周期内的时序点列表（按 metric key 索引）。为 JSON 数组的字符串形式,数组长度与响应 Timestamps 一致，无数据点处为 null。具体包含哪些 key 由响应 MetricKeys 决定。

被如下接口引用：DescribeUsageRankList。

| 名称 | 类型 |  描述 |
|------|------|-------|
| TotalToken | String | <p>[tokens / apikey_usage 族]总 token 数用量时间周期内的 JSON 字符串形式，如 <code>&quot;[12,null,15]&quot;</code>。</p><br/>示例值：[12,null,15] |
| InputTotalToken | String | <p>[tokens / apikey_usage 族]输入 token 数用量时间周期内的 JSON 字符串形式，如 <code>&quot;[7,null,9]&quot;</code>。</p><br/>示例值：[7,null,9] |
| OutputTotalToken | String | <p>[tokens / apikey_usage 族]输出 token 数用量时间周期内的 JSON 字符串形式，如 <code>&quot;[5,null,6]&quot;</code>。</p><br/>示例值：[5,null,6] |
| CacheTotalToken | String | <p>[tokens / apikey_usage 族]读缓存 token 数用量时间周期内的 JSON 字符串形式，如<code>&quot;[5,null,6]&quot;</code>。</p><br/>示例值：[5,null,6] |
| SearchRequestCount | String | <p>[search 族] 搜索请求数用量时间周期内的 JSON 字符串形式，如<code>&quot;[5,null,6]&quot;</code>。</p><br/>示例值：[5,null,6] |
| SearchCount | String | <p>[search 族] 搜索引擎调用次数用量时间周期内的 JSON 字符串形式，如<code>&quot;[5,null,6]&quot;</code>。</p><br/>示例值：[5,null,6] |
| RequestCount | String | <p>[apikey_usage 族] 请求次数在时间周期内的 JSON 字符串形式，如 <code>&quot;[12,null,15]&quot;</code>。</p><br/>示例值：[5,null,6] |
| RequestFailCount | String | <p>[apikey_usage 族] 请求失败次数在时间周期内的 JSON 字符串形式，如 &quot;[12,null,15]&quot;。</p><br/>示例值：[5,null,6] |

## UsageStats

时间周期内的统计聚合值，按 MetricKeys 实际返回取值，参见响应顶层 `MetricKeys` 字段。

被如下接口引用：DescribeUsageRankList。

| 名称 | 类型 |  描述 |
|------|------|-------|
| TotalToken | Integer | <p>[tokens / apikey_usage 族] 时间周期内的累计总 token 数。</p><br/>示例值：1834000 |
| InputTotalToken | Integer | <p>[tokens / apikey_usage 族] 时间周期内的累计输入 token 数。</p><br/>示例值：1100000 |
| OutputTotalToken | Integer | <p>[tokens / apikey_usage 族] 时间周期内的累计输出 token 数。</p><br/>示例值：734000 |
| CacheTotalToken | Integer | <p>[tokens / apikey_usage 族] 时间周期内的累计读缓存 token 数（命中缓存部分）注意：CacheTotalToken 是 InputTotalToken 的子集（已包含在内）。</p><br/>示例值：120000 |
| SearchRequestCount | Integer | <p>[search 族] 时间周期内的累计联网搜索请求数</p><br/>示例值：100 |
| SearchCount | Integer | <p>[search 族] 时间周期内的累计搜索引擎调用次数</p><br/>示例值：100 |
| RequestCount | Integer | <p>[apikey_usage 族] 时间周期内的累计请求次数</p><br/>示例值：100 |
| RequestFailCount | Integer | <p>[apikey_usage 族] 时间周期内的累计请求失败次数</p><br/>示例值：10 |
