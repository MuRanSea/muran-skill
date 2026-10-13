<!-- Official source: https://cloud.tencent.com/document/product/1823/132290 -->
<!-- Source SHA-256: c6a7b9bcd1248ce1061e6b1f1bb72a1f845fd2876d97e8f2a5e06ccc8073c667 -->

# 更新历史

官方来源：https://cloud.tencent.com/document/product/1823/132290
最近更新时间：2026-09-18 02:06:33

## 第 26 次发布

发布时间：2026-09-18 02:06:27

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [SubPackageBalance](/document/api/1823/132279#SubPackageBalance)
	* 新增成员：TotalUsed

## 第 25 次发布

发布时间：2026-09-16 03:08:05

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [Model](/document/api/1823/132279#Model)
	* 新增成员：ProviderIntroduction

## 第 24 次发布

发布时间：2026-09-14 03:04:07

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeUsageRankList](/document/api/1823/132340)
	* 新增入参：Anchor, SortKey
	* 新增出参：SortKey

## 第 23 次发布

发布时间：2026-09-11 03:09:09

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [UsageSeries](/document/api/1823/132279#UsageSeries)
	* 新增成员：RequestCount, RequestFailCount
* [UsageStats](/document/api/1823/132279#UsageStats)
	* 新增成员：RequestCount, RequestFailCount

## 第 22 次发布

发布时间：2026-09-08 04:21:53

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeModelQuota](/document/api/1823/136110)
	* 新增出参：TPMInputReservePostPaidLimit, TPMOutputReservePostPaidLimit

## 第 21 次发布

发布时间：2026-09-04 02:03:15

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [EndpointDetail](/document/api/1823/132279#EndpointDetail)
	* 新增成员：ModelStatus

## 第 20 次发布

发布时间：2026-08-20 03:12:17

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeModelQuota](/document/api/1823/136110)
	* 新增入参：ModelId
	* 新增出参：ModelId, TPMLimit, RPMLimit, TPMInputQuotaLimit, TPMOutputQuotaLimit, TPMInputReserveLimit, TPMOutputReserveLimit

## 第 19 次发布

发布时间：2026-08-19 03:04:39

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeModelQuota](/document/api/1823/136110)

## 第 18 次发布

发布时间：2026-08-17 03:05:54

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [Model](/document/api/1823/132279#Model)
	* 新增成员：ExtraModelIds
* [ModelChargingItem](/document/api/1823/132279#ModelChargingItem)
	* 新增成员：Specification, Usage, ReferencePrice
* [ModelEndpointView](/document/api/1823/132279#ModelEndpointView)
	* 新增成员：ExtraModelIds, ModelStatus

## 第 17 次发布

发布时间：2026-08-06 02:09:06

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [Model](/document/api/1823/132279#Model)
	* 新增成员：DiscontinuedAt

## 第 16 次发布

发布时间：2026-07-31 03:02:49

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [TokenPlanListItem](/document/api/1823/132279#TokenPlanListItem)
	* 新增成员：ApiKeyCount

## 第 15 次发布

发布时间：2026-07-17 02:06:01

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateTokenPlanTeamOrderAndBuy](/document/api/1823/132267)
	* 新增入参：TeamId

## 第 14 次发布

发布时间：2026-07-14 03:02:16

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateEndpoint](/document/api/1823/134036)
* [DeleteEndpoint](/document/api/1823/134035)
* [DescribeEndpoint](/document/api/1823/134034)
* [DescribeModelEndpointList](/document/api/1823/134033)
* [ModifyEndpoint](/document/api/1823/134032)

新增数据结构：

* [EndpointCreateDetail](/document/api/1823/132279#EndpointCreateDetail)
* [EndpointDetail](/document/api/1823/132279#EndpointDetail)
* [ModelEndpointView](/document/api/1823/132279#ModelEndpointView)

## 第 13 次发布

发布时间：2026-07-13 03:00:50

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateApiKey](/document/api/1823/133810)
	* 新增入参：ApiKeyName, Platform, BindType, Remark, Status, Bindings, IpWhitelist, Quotas
	* 新增出参：ApiKeyId
* [DeleteApiKey](/document/api/1823/133809)
	* 新增入参：ApiKeyId, Platform
* [ModifyApiKeyInfo](/document/api/1823/133808)
	* 新增入参：ApiKeyId, Platform, ApiKeyName, Remark, IpWhitelist, QuotasDesired
* [ModifyApiKeyStatus](/document/api/1823/133807)
	* 新增入参：ApiKeyId, Platform, Status

新增数据结构：

* [QuotaCreateItem](/document/api/1823/132279#QuotaCreateItem)
* [QuotasDesired](/document/api/1823/132279#QuotasDesired)

## 第 12 次发布

发布时间：2026-07-10 03:04:21

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [ModelChargingItem](/document/api/1823/132279#ModelChargingItem)
	* 新增成员：PeakPrice

## 第 11 次发布

发布时间：2026-07-08 03:01:59

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateApiKey](/document/api/1823/133810)
* [DeleteApiKey](/document/api/1823/133809)
* [ModifyApiKeyInfo](/document/api/1823/133808)
* [ModifyApiKeyStatus](/document/api/1823/133807)

## 第 10 次发布

发布时间：2026-07-07 02:57:34

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeModelList](/document/api/1823/132614)
	* 新增入参：ModelIds, ModelNames, ModelTypes, Tags, Limit, Offset

## 第 9 次发布

发布时间：2026-07-06 14:15:19

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeModelList](/document/api/1823/132614)
	* 新增出参：ModelSet, TotalCount

新增数据结构：

* [Model](/document/api/1823/132279#Model)
* [ModelAccessInfo](/document/api/1823/132279#ModelAccessInfo)
* [ModelChargingInfo](/document/api/1823/132279#ModelChargingInfo)
* [ModelChargingItem](/document/api/1823/132279#ModelChargingItem)
* [ModelFreeTrialInfo](/document/api/1823/132279#ModelFreeTrialInfo)
* [ModelImage](/document/api/1823/132279#ModelImage)
* [ModelSiteRegion](/document/api/1823/132279#ModelSiteRegion)
* [ModelSpec](/document/api/1823/132279#ModelSpec)

## 第 8 次发布

发布时间：2026-06-29 03:02:45

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [UsageSeries](/document/api/1823/132279#UsageSeries)
	* 新增成员：CacheTotalToken, SearchRequestCount, SearchCount
* [UsageStats](/document/api/1823/132279#UsageStats)
	* 新增成员：CacheTotalToken, SearchRequestCount, SearchCount

## 第 7 次发布

发布时间：2026-06-18 01:59:46

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeApiKey](/document/api/1823/132345)
	* 新增出参：QuotaSet, QuotaStatus

新增数据结构：

* [QuotaInfo](/document/api/1823/132279#QuotaInfo)

修改数据结构：

* [ApiKeyDetail](/document/api/1823/132279#ApiKeyDetail)
	* 新增成员：QuotaSet, QuotaStatus

## 第 6 次发布

发布时间：2026-06-15 01:59:15

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateGlossary](/document/api/1823/132887)
* [CreateGlossaryEntries](/document/api/1823/132886)
* [DeleteGlossary](/document/api/1823/132885)
* [DeleteGlossaryEntries](/document/api/1823/132884)
* [DescribeGlossaries](/document/api/1823/132883)
* [DescribeGlossaryEntries](/document/api/1823/132882)
* [ModifyGlossaryEntries](/document/api/1823/132881)

新增数据结构：

* [DeleteGlossaryEntryInput](/document/api/1823/132279#DeleteGlossaryEntryInput)
* [GlossaryEntryInput](/document/api/1823/132279#GlossaryEntryInput)
* [GlossaryEntryItem](/document/api/1823/132279#GlossaryEntryItem)
* [GlossaryItem](/document/api/1823/132279#GlossaryItem)
* [ModifyGlossaryEntryInput](/document/api/1823/132279#ModifyGlossaryEntryInput)

## 第 5 次发布

发布时间：2026-06-09 03:04:04

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [BindingItem](/document/api/1823/132279#BindingItem)
	* 新增成员：Status

## 第 4 次发布

发布时间：2026-06-08 02:00:45

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeModelList](/document/api/1823/132614)

## 第 3 次发布

发布时间：2026-06-04 02:57:45

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeTokenPlanApiKeyUsageDetail](/document/api/1823/132342)
	* 新增入参：TeamId, From, To, Sort, Limit, Context, ApiKeyId, ApiKeyName, ModelName
	* 新增出参：Context, ListOver, List, ProductType

新增数据结构：

* [UsageDetailItem](/document/api/1823/132279#UsageDetailItem)

## 第 2 次发布

发布时间：2026-06-01 02:59:39

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeApiKey](/document/api/1823/132345)
* [DescribeApiKeyList](/document/api/1823/132344)
* [DescribeTokenPlanApiKeyUsageDetail](/document/api/1823/132342)
* [DescribeUsageRankList](/document/api/1823/132340)

新增数据结构：

* [ApiKeyDetail](/document/api/1823/132279#ApiKeyDetail)
* [BindingItem](/document/api/1823/132279#BindingItem)
* [UsageRankItem](/document/api/1823/132279#UsageRankItem)
* [UsageSeries](/document/api/1823/132279#UsageSeries)
* [UsageStats](/document/api/1823/132279#UsageStats)

## 第 1 次发布

发布时间：2026-05-29 10:58:06

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateTokenPlanApiKeys](/document/api/1823/132278)
* [CreateTokenPlanTeamOrderAndBuy](/document/api/1823/132267)
* [DeleteTokenPlanApiKey](/document/api/1823/132277)
* [DescribeTokenPlan](/document/api/1823/132270)
* [DescribeTokenPlanApiKey](/document/api/1823/132276)
* [DescribeTokenPlanApiKeyList](/document/api/1823/132275)
* [DescribeTokenPlanApiKeySecret](/document/api/1823/132274)
* [DescribeTokenPlanList](/document/api/1823/132269)
* [ModifyTokenPlanApiKey](/document/api/1823/132273)
* [ModifyTokenPlanApiKeySecret](/document/api/1823/132272)
* [RenewTokenPlanTeamOrder](/document/api/1823/132266)
* [UpgradeTokenPlanTeamOrder](/document/api/1823/132265)

新增数据结构：

* [BatchCreateFailedItem](/document/api/1823/132279#BatchCreateFailedItem)
* [CreateApiKeysResultItem](/document/api/1823/132279#CreateApiKeysResultItem)
* [RequestFilter](/document/api/1823/132279#RequestFilter)
* [RequestSort](/document/api/1823/132279#RequestSort)
* [SubPackageBalance](/document/api/1823/132279#SubPackageBalance)
* [TokenPlanApiKeyInfo](/document/api/1823/132279#TokenPlanApiKeyInfo)
* [TokenPlanApiKeyListItem](/document/api/1823/132279#TokenPlanApiKeyListItem)
* [TokenPlanListItem](/document/api/1823/132279#TokenPlanListItem)
* [TokenPlanPackageInfo](/document/api/1823/132279#TokenPlanPackageInfo)
* [TokenSummary](/document/api/1823/132279#TokenSummary)
* [TokenSummaryBillingItem](/document/api/1823/132279#TokenSummaryBillingItem)
