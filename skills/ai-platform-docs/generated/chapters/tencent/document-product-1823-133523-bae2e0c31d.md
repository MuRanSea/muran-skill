<!-- Official source: https://cloud.tencent.com/document/product/1823/133523 -->
<!-- Source SHA-256: eed2561e000f5973a4041f34705c5ac9b27be9c76985712f9f19ee896201e2dd -->

# 日志采集

官方来源：https://cloud.tencent.com/document/product/1823/133523
最近更新时间：2026-09-21 14:35:30

TokenHub 支持将模型调用相关日志投递至腾讯云日志服务 CLS，帮助用户进行调用审计、用量核查、问题排查和日志长期留存。日志采集包括如下两类：

| **日志类型** | **记录内容** | **适用场景** |
| --- | --- | --- |
| 审计日志 | 单次调用的结构化元数据，例如 Request ID、请求时间、模型、服务、API Key、客户端 IP、状态码、Token 用量、时延等 | 合规审计、调用追踪、用量核查、安全排查 |
| 调用日志 | 审计日志字段，以及原始请求、模型响应、日志上报来源等明细字段 | 单次请求排障、模型效果分析、调用链路追溯 |

**注意：**

调用日志可能包含用户输入和模型输出，数据量较大，开启前请确认已按业务安全要求配置 CLS 日志主题权限、保留周期和访问控制。

开启日志投递后，**在线推理服务**与 **TokenPlan 企业版**的日志将一并投递至 CLS 日志服务。请注意：CLS 日志服务为腾讯云**独立计费产品**，开启后即开始计费，费用标准请参考 [CLS 计费概述](https://cloud.tencent.com/document/product/614/45802)。

## 前提条件

已开通腾讯云日志服务 CLS，并完成服务角色 TokenHub\_QCSLinkedRoleInCloudLogService 的授权。

当前账号具备 TokenHub 控制台操作权限，以及目标 CLS 日志集、日志主题的访问权限。

使用日志投递会产生 CLS 相关费用，费用按日志服务计费规则收取。

## 开启日志投递

1. 登录 [TokenHub 控制台](https://console.cloud.tencent.com/tokenhub)。

2. 在左侧导航栏选择**平台配置 > 系统配置**。

3. 在**日志采集**区域，选择需要开启的日志类型，单击对应卡片中的**立即启用**，在**开启日志投递**弹窗中完成配置。

开启成功后，日志卡片展示 **已开启** 状态，并展示已绑定的日志集、日志主题。后续新增的对应类型日志将写入指定 CLS 日志主题。

| **配置项** | **说明** |
| --- | --- |
| 目标地域 | 选择目标 CLS 日志集所在地域，需与 TokenHub 所在地域保持一致。 |
| 日志主题操作 | 支持选择已有日志主题，或按页面提示创建新的日志主题。 |
| 日志集 | 选择用于接收 TokenHub 日志的 CLS 日志集。 |
| 日志主题 | 选择用于存储当前日志类型的 CLS 日志主题。建议审计日志和调用日志使用不同日志主题，便于权限、索引和保留周期独立管理。 |

## 查看调用明细

**说明：**

仅支持日志投递开启后，新发起的请求才可以查看日志详情。

您可以进入 CLS 控制台统一检索日志，也可以在 TokenHub 控制台分开查看在线推理日志、企业版 Token Plan 日志。

### CLS 控制台查看日志

1. 进入**平台配置 > 系统配置 > 日志采集**。

2. 在已开启的审计日志或调用日志卡片中，单击**检索分析**。

3. 页面跳转至 CLS 对应日志主题，可按字段检索日志。

### 用量统计页面查看在线推理日志

1. 在左侧导航栏选择**观测 > 用量统计**，进入**语言模型**页签。

2. 可按以下条件筛选调用记录：

| **筛选项** | **说明** |
| --- | --- |
| API Key | 查看全部 Key 或指定 Key 的调用记录。 |
| 状态 | 查看全部状态或指定状态码的调用记录。 |
| 时间范围 | 支持今天、近 7 天、近 30 天或自定义时间范围。 |
| 关键字 | 支持输入 API Key ID 或 Request ID 进行搜索。 |

3. 在调用记录列表中，查看请求时间、请求 ID、模型、服务名称 / ID、API Key 名称 / ID、状态码、Token 用量等信息。

4. 在操作列单击 **审计日志** 或 **调用日志**，查看本条日志详情。若对应日志投递未开启，无法查看该类型日志详情。

### 企业版 Token Plan 套餐详情页面查看 Token Plan 日志

1. 在 [Token Plan 企业版](https://console.cloud.tencent.com/tokenhub/tokenplan-e) 套餐列表，选择您的套餐 > 进入套餐详情页面

2. 在调用明细列表，单击操作列的**审计日志**或**调用日志**，查看本次请求的日志详情。

## 关闭日志投递

1. 进入**平台配置 > 系统配置 > 日志采集**。

2. 在已开启的日志卡片中，单击**关闭投递**，按页面提示确认。

关闭后，TokenHub 停止向对应 CLS 日志主题写入新增日志。已投递到 CLS 的历史日志不受影响，其保留周期和存储费用按 CLS 配置执行。

## 日志字段说明

### 审计日志与调用日志共有字段

| **分类** | **字段** | **类型** | **说明** |
| --- | --- | --- | --- |
| 请求基本信息 | `request_id` | string | 请求唯一标识，用于全链路追踪与排障。 |
| 请求基本信息 | `created_at` | datetime | 请求开始时间，时间戳格式。 |
| 请求基本信息 | `finished_at` | datetime | 请求结束时间，可用于计算端到端时延。 |
| 请求基本信息 | `status` | int | HTTP 状态码，包含 2xx、4xx、5xx 等状态。 |
| 接口与协议 | `api` | string | 请求路径，例如 `/v1/chat/completions`。 |
| 接口与协议 | `api_type` | string | 协议类型，例如 `chat`、`responses`、`embedding`。 |
| 接口与协议 | `is_stream` | bool | 是否为流式请求。 |
| 模型信息 | `model_id` | string | 路由命中的模型 ID。 |
| 模型信息 | `model_name` | string | 模型名称。 |
| 模型信息 | `model_type` | string | 模型类型，例如 `llm`、`embedding`、`multimodal`。 |
| 认证与客户端 | `api_key_id` | string | API Key ID。 |
| 认证与客户端 | `auth_type` | string | 认证方式，例如 `apikey`。 |
| 认证与客户端 | `user_agent` | string | 客户端 User-Agent。 |
| 认证与客户端 | `client_ip` | string | 客户端来源 IP。 |
| Token 统计 | `input_tokens` | int | 输入 Token 数，已包含读缓存命中的 Token 数。 |
| Token 统计 | `output_tokens` | int | 输出 Token 数。 |
| Token 统计 | `total_tokens` | int | 总 Token 数，`total_tokens = input_tokens + output_tokens`。 |
| Token 统计 | `cache_tokens` | int | 读缓存命中的 Token 数。 |
| Token 统计 | `thinking_tokens` | int | 思考 Token 数，适用于深度思考模型。 |
| 性能与时延 | `ttft` | int(ms) | 首 Token 时延，Time To First Token。 |
| 性能与时延 | `tpot` | int(ms) | 每 Token 输出时延，Time Per Output Token。 |
| 性能与时延 | `is_timeout` | bool | 请求是否超时。 |
| 性能与时延 | `is_canceled` | bool | 请求是否被客户端取消或断开。 |
| 业务标识 | `service_type` | string | 服务类型  在线推理服务取值为 inference\_service  TokenPlan 企业套餐取值为 token\_plan\_enterprise |
| 业务标识 | `endpoint_id` | string | 在线推理服务 ID。TokenPlan 场景下为空。 |
| 业务标识 | `endpoint_name` | string | 在线推理服务名称。TokenPlan 场景下为空。 |
| 业务标识 | `team_id` | string | 套餐 ID，TokenPlan 场景使用。 |
| 业务标识 | `team_name` | string | 套餐名称，TokenPlan 场景使用。 |

### 调用日志独有字段

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `input` | string(JSON) | 用户完整请求体，包含模型、消息内容、流式参数等信息。 |
| `output` | string(JSON) | 模型完整响应。不同产品或接口的响应结构可能不同，以实际日志内容为准。 |

## 常见问题

### 开启日志投递后，为什么没有立即看到日志？

日志仅记录开启后的新增调用。若刚完成配置，请先确认是否有新的模型调用产生，并检查目标地域、日志集、日志主题是否选择正确。

### 关闭日志投递会影响模型调用吗？

不会。关闭投递只停止写入新增日志，不影响在线推理服务或 TokenPlan 的正常调用。

### 历史日志在哪里保留？

已投递的历史日志保留在 CLS 中，保留周期、索引、检索分析和费用均按 CLS 配置执行。TokenHub 关闭投递后不会删除 CLS 中的历史日志。

## 相关文档

[日志服务 CLS](https://cloud.tencent.com/document/product/614)

[用量统计](https://cloud.tencent.com/document/product/1823/130088)

[模型监控](https://cloud.tencent.com/document/product/1823/130089)
