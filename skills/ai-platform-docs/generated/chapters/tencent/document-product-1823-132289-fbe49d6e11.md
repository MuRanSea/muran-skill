<!-- Official source: https://cloud.tencent.com/document/product/1823/132289 -->
<!-- Source SHA-256: ac28149dbbef1d473b6eb71a1b5148d4a4fd6ee631d75b4d4d8a4d57aaeb1c8f -->

# API 概览

官方来源：https://cloud.tencent.com/document/product/1823/132289
最近更新时间：2026-08-19 03:05:01

## API 密钥管理相关接口

| 接口名称 | 接口功能 | 频率限制（次/秒） |
|-|-|-|
| [CreateApiKey](/document/api/1823/133810) | 创建 API 密钥 | 20 |
| [DeleteApiKey](/document/api/1823/133809) | 删除 API 密钥 | 20 |
| [DescribeApiKey](/document/api/1823/132345) | 查询 API 密钥详情 | 20 |
| [DescribeApiKeyList](/document/api/1823/132344) | 查询 API 密钥列表 | 20 |
| [ModifyApiKeyInfo](/document/api/1823/133808) | 更新 API 密钥信息 | 20 |
| [ModifyApiKeyStatus](/document/api/1823/133807) | 更新 API 密钥状态 | 20 |

## 在线推理相关接口

| 接口名称 | 接口功能 | 频率限制（次/秒） |
|-|-|-|
| [CreateEndpoint](/document/api/1823/134036) | 创建推理服务 | 20 |
| [DeleteEndpoint](/document/api/1823/134035) | 删除推理服务 | 20 |
| [DescribeEndpoint](/document/api/1823/134034) | 查询推理服务详情 | 20 |
| [DescribeModelEndpointList](/document/api/1823/134033) | 查询模型接入点列表 | 20 |
| [ModifyEndpoint](/document/api/1823/134032) | 修改推理服务 | 20 |

## 术语库管理相关接口

| 接口名称 | 接口功能 | 频率限制（次/秒） |
|-|-|-|
| [CreateGlossary](/document/api/1823/132887) | 创建术语库 | 20 |
| [DescribeGlossaries](/document/api/1823/132883) | 查询术语库列表 | 20 |
| [DeleteGlossary](/document/api/1823/132885) | 删除术语库 | 20 |
| [CreateGlossaryEntries](/document/api/1823/132886) | 批量创建术语条目 | 20 |
| [DescribeGlossaryEntries](/document/api/1823/132882) | 查询术语条目列表 | 20 |
| [ModifyGlossaryEntries](/document/api/1823/132881) | 批量修改术语条目 | 20 |
| [DeleteGlossaryEntries](/document/api/1823/132884) | 批量删除术语条目 | 20 |

## TokenPlan 套餐购买相关接口

| 接口名称 | 接口功能 | 频率限制（次/秒） |
|-|-|-|
| [CreateTokenPlanTeamOrderAndBuy](/document/api/1823/132267) | 创建或重新开通 Token Plan 套餐 | 20 |
| [RenewTokenPlanTeamOrder](/document/api/1823/132266) | 续费 Token Plan 套餐 | 20 |
| [UpgradeTokenPlanTeamOrder](/document/api/1823/132265) | 升配 Token Plan 套餐 | 20 |

## 模型管理相关接口

| 接口名称 | 接口功能 | 频率限制（次/秒） |
|-|-|-|
| [DescribeModelList](/document/api/1823/132614) | 查询模型列表 | 20 |

## 模型相关接口

| 接口名称 | 接口功能 | 频率限制（次/秒） |
|-|-|-|
| [DescribeModelQuota](/document/api/1823/136110) | 查询模型配额 | 20 |

## TokenPlan 套餐管理相关接口

| 接口名称 | 接口功能 | 频率限制（次/秒） |
|-|-|-|
| [DescribeTokenPlan](/document/api/1823/132270) | 查询 Token Plan 套餐详情 | 20 |
| [DescribeTokenPlanList](/document/api/1823/132269) | 查询 Token Plan 套餐列表 | 20 |

## TokenPlan APIKey 管理相关接口

| 接口名称 | 接口功能 | 频率限制（次/秒） |
|-|-|-|
| [CreateTokenPlanApiKeys](/document/api/1823/132278) | 批量创建 Token Plan 套餐的 API Key | 20 |
| [DeleteTokenPlanApiKey](/document/api/1823/132277) | 删除 Token Plan 套餐的 API Key | 20 |
| [DescribeTokenPlanApiKey](/document/api/1823/132276) | 查询 Token Plan 套餐的 API Key 详情 | 20 |
| [DescribeTokenPlanApiKeyList](/document/api/1823/132275) | 查询 Token Plan 套餐的 API Key 列表 | 20 |
| [DescribeTokenPlanApiKeySecret](/document/api/1823/132274) | 查询 Token Plan 套餐的 API Key 密钥（明文） | 20 |
| [ModifyTokenPlanApiKey](/document/api/1823/132273) | 修改 Token Plan 套餐的 API Key 配置 | 20 |
| [ModifyTokenPlanApiKeySecret](/document/api/1823/132272) | 重置 Token Plan 套餐的 API Key 密钥 | 20 |

## TokenPlan 调用明细相关接口

| 接口名称 | 接口功能 | 频率限制（次/秒） |
|-|-|-|
| [DescribeTokenPlanApiKeyUsageDetail](/document/api/1823/132342) | 查询 TokenPlan 企业版 API Key 调用明细 | 20 |

## 用量统计相关接口

| 接口名称 | 接口功能 | 频率限制（次/秒） |
|-|-|-|
| [DescribeUsageRankList](/document/api/1823/132340) | 查询用量排行列表 | 20 |

>! 以上给出的接口频率限制维度为`API + 接入地域 + 子账号`，有关限频更多说明参考：[API 频率限制说明](https://cloud.tencent.com/document/product/1278/109059)
