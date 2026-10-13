<!-- Official source: https://cloud.tencent.com/document/product/1823/131595 -->
<!-- Source SHA-256: d13a17ee128e3a58047895407c0dcecdcfcc0af26d730733527473479d029d24 -->

# API 错误码说明

官方来源：https://cloud.tencent.com/document/product/1823/131595
最近更新时间：2026-07-21 15:27:28

本文档帮助您理解 TokenHub API 的错误响应格式，快速定位并解决调用问题。

TokenHub 默认采用 OpenAI 兼容协议，同时兼容 Anthropic Messages 协议与 OpenAI Responses 协议。当 API 调用出错时，HTTP 状态码为非 2xx，响应体为 JSON 格式，并同时返回中英文错误描述，便于排查。

## 一、OpenAI / Responses 兼容协议（标准链路）

使用 OpenAI 兼容协议（`/v1/chat/completions`）或 Responses 协议（`/v1/responses`）接入时，错误响应遵循以下统一结构。

### 1.1 错误响应结构

```json
{
  "error": {
    "message": "<英文错误描述>",
    "message_zh": "<中文错误描述>",
    "code": "<业务错误码>",
    "type": "<错误类型>",
    "source": "client | gateway | upstream",
    "upstream_code": "<上游错误码，仅上游错误时返回>",
    "upstream_status": "<上游 HTTP 状态码，仅上游错误时返回>",
    "request_id": "<请求唯一标识>"
  }
}
```

**字段说明：**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `message` | string | 英文错误描述。 |
| `message_zh` | string | 中文错误描述，与 `message` 一一对应，便于中文场景直接展示。 |
| `code` | string | 平台业务错误码（如 `401002`），用于精确定位问题；限流场景下可能以整型数字返回。 |
| `type` | string | 错误类型，用于程序判断错误大类。请求链路早期短路的错误（如鉴权、参数校验）统一为 `gateway_error`。 |
| `source` | string | 错误来源：`client`（请求端）、`gateway`（网关）、`upstream`（上游服务）。仅 Handler 层错误返回该字段。 |
| `upstream_code` | string | 上游服务原始错误码，仅当 `source=upstream` 时出现。 |
| `upstream_status` | number | 上游服务 HTTP 状态码，仅当 `source=upstream` 时出现。 |
| `request_id` | string | 请求唯一标识，用于问题排查和提交工单。 |

**注意：**

请求链路早期被拦截的错误（如鉴权失败、参数非法）`type` 统一为 `gateway_error`，且不返回 `source` 字段。

限流（`429`）场景下，`code` 可能以整型数字返回，并携带响应头 `Retry-After`（单位：秒），客户端解析 `error.code` 时应同时兼容字符串与数字类型。

### 1.2 业务错误码速查表

下表为 maas-gateway 定义的全部业务错误码，含对应的 HTTP 状态码及错误原因和处理办法。内容中的 `{xxx}` 为运行时动态填充的具体值（如参数名、模型 ID、限额数值等）。

| **HTTP** | **错误码 Code** | **错误原因和处理办法** |
| --- | --- | --- |
| 400 | `400001`CodeInvalidRequest | 请求不合法，请检查请求体、必填字段及请求格式是否正确。 |
| 400 | `400002`CodeInvalidParameter | 请求参数无效或缺失，请检查该参数取值是否正确。 |
| 400 | `400003`CodeInputTooLong | 输入 Token 数超出模型上下文限制。 |
| 400 | `400004`CodeModelNotFound | 请求中的模型或服务 ID 不存在，请检查服务 ID 是否正确。服务 ID 可在控制台的在线推理服务列表中查看。 |
| 400 | `400005`CodeUnsupportedModel | 当前模型不支持所请求的协议或能力，请切换访问协议/能力或查看控制台调用示例。 |
| 400 | `400006`CodeUnsupportedFormat | 当前模型不支持请求的 response\_format 或输出格式，请查看控制台或产品文档中的参数支持范围。 |
| 400 | `401006`CodeInvalidEndpoint | 输入的服务 ID 不存在，或模型与服务不匹配，请在控制台的在线推理服务列表中确认服务 ID。 |
| 401 | `401001`CodeUnauthorized | 请求未携带认证信息，或认证方式无法识别，请检查 API Key 是否正确。 |
| 401 | `401002`CodeInvalidAPIKey | API Key 不存在或签名校验失败，请检查 API Key 是否正确。 |
| 401 | `401003`CodeAPIKeyExpired | API Key 已过期，请检查或重新生成 API Key。 |
| 401 | `401004`CodeAPIKeyDisabled | API Key 已被禁用，请检查 API Key 状态。 |
| 401 | `401005`CodeSignatureInvalid | CAM 或自定义签名校验未通过，请检查签名算法、密钥和请求时间。 |
| 402 | `401007`CodeEndpointNoFreePackage | 服务无可用免费体验额度，且未开启后付费，无法正常访问。请前往控制台 > 在线推理服务开启后付费。 |
| 402 | `401008`CodeEndpointFreeQuotaExhausted | 服务免费体验额度已耗尽，且未开启后付费，无法正常访问。请前往控制台 > 在线推理服务开启后付费。 |
| 402 | `403004`CodeInsufficientBalance | API Key 所属账号已欠费，访问的服务 ID 已被隔离。请充值后在控制台重新启用服务。 |
| 403 | `403001`CodePermissionDenied | 套餐包被禁用或无调用权限，请前往控制台查看套餐包状态。 |
| 403 | `403002`CodeModelAccessDenied | 当前 API Key 无权访问模型 ，请前往控制台 API Key 管理页检查 Key 可访问范围。 |
| 403 | `403003`CodeAccountBlocked | API Key 所属账号已被禁用，请联系腾讯云售后获取支持。 |
| 403 | `403005`CodeIPNotAllowed | 请求来源 IP 不在 API Key 白名单内，请前往控制台 API Key 管理页检查 IP 是否在白名单范围。 |
| 403 | `403006`CodeToolUnavailable | 所请求的工具不可用或未订阅，请前往控制台检查工具的订阅状态。 |
| 410 | `410001`CodeSessionExpired | 会话绑定的 provider 已下线，请使用新的 X-Session-ID 重建会话。 |
| 413 | `413001`CodeRequestBodyTooLarge | 请求体过大，最大允许字节，请减小请求体大小后重试。 |
| 429 | `429001`CodeRateLimitExceeded | 请求速率超过当前模型阈值 ，请降低访问频率或联系腾讯云售后申请更高限额。 |
| 429 | `429002`CodeRPMLimitExceeded | 请求速率超过当前模型 RPM（每分钟请求数）阈值 ，请降低访问频率或联系腾讯云售后申请更高限额。 |
| 429 | `429003`CodeTPMLimitExceeded | Token 使用量超过当前模型 TPM（每分钟 Token 数）阈值，请降低访问频率或联系腾讯云售后申请更高限额。 |
| 429 | `429004`CodeTPDLimitExceeded | Token 使用量超过当前模型 TPD（每日 Token 数）阈值，请降低访问频率或联系腾讯云售后申请更高限额。 |
| 429 | `429005`CodeConcurrencyLimitExceeded | 请求超过当前模型的限流阈值，请降低访问频率或联系腾讯云售后申请更高限额。 |
| 429 | `429006`CodeUpstreamRateLimitExceeded | 当前模型服务繁忙或已达服务容量上限，请降低请求频率后稍后重试。 |
| 451 | `451001`CodeContentFiltered | 输入或输出内容触发安全策略，请调整内容后重试。 |
| 499 | `499001`CodeRequestCanceled | 客户端已主动断开连接。 |
| 500 | `500001`CodeInternalError | 发生未知错误，请重试。如多次失败，请联系平台售后协助排查。 |
| 502 | `502001`CodeUpstreamError | 上游模型服务异常或不可达，请重试。如多次失败，请联系平台售后协助排查。 |
| 503 | `503001`CodeServiceUnavailable | 服务暂不可用，请重试。如多次失败，请联系平台售后协助排查。 |
| 504 | `504001`CodeGatewayTimeout | 上游响应超时，请重试。如多次失败，请联系平台售后协助排查。 |

### 1.3 错误响应示例

以下示例展示各类错误的响应格式，可作为客户端解析与排查的参考。其中示例 A~D 为真实调用触发的响应（`request_id` 为实际返回值），示例 E、F 按相同格式构造，用于说明限流与上游错误的字段特征。

#### 示例 A：API Key 无效（HTTP 401）

```json
{
  "error": {
    "message": "The API Key does not exist or signature verification failed. Please check whether the API Key is correct. See: https://console.cloud.tencent.com/tokenhub/apikey",
    "message_zh": "API Key 不存在或签名校验失败，请检查 API Key 是否正确，查看链接：https://console.cloud.tencent.com/tokenhub/apikey",
    "code": "401002",
    "type": "gateway_error",
    "request_id": "7e6dc7d0-a8d7-4993-a74d-f6cd24b33925"
  }
}
```

**排查建议**：检查请求头 `Authorization: Bearer <your-api-key>` 中的 API Key 是否正确、是否过期或被禁用，可前往 [API Key 管理页](https://console.cloud.tencent.com/tokenhub/apikey) 核对。

#### 示例 B：参数缺失（HTTP 400）

```json
{
  "error": {
    "message": "The request parameter messages is invalid or missing. Please check the value of this parameter.",
    "message_zh": "请求参数 messages 无效或缺失，请检查该参数取值是否正确。",
    "code": "400002",
    "type": "gateway_error",
    "request_id": "5fcdcb74-bd31-4bc6-b265-1389cea2d915"
  }
}
```

**排查建议**：检查请求体中 `messages`、`model` 等必填字段是否完整、取值是否合法。

#### 示例 C：模型不存在（HTTP 400）

```json
{
  "error": {
    "message": "The model or service ID gpt-9-turbo does not exist. Please check whether the service ID is correct. Service IDs are available in the Online Inference Service list in the console. See: https://cloud.tencent.com/document/product/1823/130079",
    "message_zh": "请求中的模型或服务 ID gpt-9-turbo 不存在，请检查服务 ID 是否正确。服务 ID 可在控制台的在线推理服务列表中查看，查看链接：https://cloud.tencent.com/document/product/1823/130079",
    "code": "400004",
    "type": "gateway_error",
    "request_id": "7a948a0f-740f-4d37-846f-0b500c3f1c48"
  }
}
```

**排查建议**：确认 `model` 字段填写的模型或服务 ID 在平台已上线，可在 [控制台在线推理服务列表](https://console.cloud.tencent.com/tokenhub/inference) 查看可用服务 ID。

#### 示例 D：Responses 协议参数非法（HTTP 400）

Responses 协议（`/v1/responses`）在 Handler 层校验失败时，会额外返回 `source` 字段：

```json
{
  "error": {
    "message": "The request is invalid: temperature must be [0.0, 2.0]. Please check the request body, required fields, and request format.",
    "message_zh": "请求不合法：temperature must be [0.0, 2.0]，请检查请求体、必填字段及请求格式是否正确。",
    "code": "400001",
    "type": "invalid_request_error",
    "source": "client",
    "request_id": "d4924d12-a56f-4a51-94f4-dab3608dd6c4"
  }
}
```

**排查建议**：按照 `message_zh` 提示修正参数取值，本例中 `temperature` 需在 `[0.0, 2.0]` 范围内。

#### 示例 E：触发限流（HTTP 429）

限流响应的 `code` 以整型数字返回，并携带响应头 `Retry-After`（单位：秒）：

```json
{
  "error": {
    "code": 429001,
    "message": "The request rate exceeds the current model deepseek-v4-flash-202605 limit 60. Please reduce the request frequency or contact Tencent Cloud support to request a higher limit.",
    "message_zh": "请求速率超过当前模型 deepseek-v4-flash-202605 阈值 60，请降低访问频率或联系腾讯云售后申请更高限额。",
    "request_id": "req-16c2ae01"
  }
}
```

**排查建议**：`message` 中携带超限维度（`rpm`/`tpm`/`tpd`/`concurrency`）。请依据响应头 `Retry-After` 退避重试，或降低调用频率、联系平台提升配额。

#### 示例 F：上游服务错误（HTTP 502）

当上游模型服务返回错误或不可达时，`source` 为 `upstream`，并透传上游状态：

```json
{
  "error": {
    "message": "The upstream model service is abnormal or unreachable. Please try again. If the issue persists, contact platform support for troubleshooting.",
    "message_zh": "上游模型服务异常或不可达，请重试。如多次失败，请联系平台售后协助排查。",
    "code": "502001",
    "type": "upstream_error",
    "source": "upstream",
    "upstream_status": 502,
    "request_id": "req-7d2c4a11"
  }
}
```

**排查建议**：上游模型服务暂时异常，建议使用指数退避策略进行重试；若持续失败请携带 `request_id` [提交工单](https://console.cloud.tencent.com/workorder/category)。

## 二、Anthropic 兼容协议

如果您使用 Anthropic Messages 协议（`/v1/messages`）接入 TokenHub，错误响应遵循 Anthropic 官方格式。

### 2.1 错误响应结构

```json
{
  "type": "error",
  "error": {
    "type": "<错误类型>",
    "message": "<错误描述>",
    "reqid": "<请求唯一标识>"
  }
}
```

### 2.2 与标准格式的区别

| 区别项 | OpenAI / Responses 协议 | Anthropic 协议 |
| --- | --- | --- |
| 外层结构 | 仅 `error` 对象 | 外层多一个 `"type": "error"` |
| 业务码 | 返回 `code` 字段 | **不返回** `code` |
| 中文描述 | 返回 `message_zh` 字段 | **不返回** `message_zh`（仅英文 `message`） |
| 请求 ID 字段名 | `request_id` | `reqid` |
| 错误来源 | 返回 `source` 字段 | **不返回** `source` |

### 2.3 Anthropic 协议错误类型

| 错误类型（type） | 含义 |
| --- | --- |
| `invalid_request_error` | 请求参数无效 |
| `authentication_error` | 鉴权失败 |
| `permission_error` | 权限不足 |
| `not_found_error` | 资源不存在 |
| `rate_limit_error` | 限流 |
| `overloaded_error` | 服务过载 |
| `api_error` | 服务端内部错误 |

### 2.4 示例：API Key 无效（HTTP 401）

以下为真实调用触发的 Anthropic 协议错误响应：

```json
{
  "type": "error",
  "error": {
    "type": "authentication_error",
    "message": "The API Key does not exist or signature verification failed. Please check whether the API Key is correct. See: https://console.cloud.tencent.com/tokenhub/apikey",
    "reqid": "e556c76e-acf8-46ef-88f4-8395f3cd6ffc"
  }
}
```

**排查建议**：Anthropic 协议不返回 `code` 与 `message_zh`，请依据 `type` 判断错误大类，并携带 `reqid` 排查或提交工单。

## 三、获取帮助与提交工单

如果您在排查问题后仍无法解决，可以 [提交工单](https://console.cloud.tencent.com/workorder/category) 联系腾讯云技术支持获取帮助。

提交工单时请提供以下信息：

| 必要信息 | 说明 |
| --- | --- |
| **Request ID** | 错误响应中的 `request_id`（OpenAI / Responses 协议）或 `reqid`（Anthropic 协议），这是后端排查问题的唯一索引，请务必在工单中提供。缺少该值将显著增加问题定位时间。 |
| 请求时间 | 出错的大致时间点。 |
| 请求参数 | 使用的 model 名称、endpoint 等。 |
| 错误响应 | 完整的错误响应 JSON。 |
