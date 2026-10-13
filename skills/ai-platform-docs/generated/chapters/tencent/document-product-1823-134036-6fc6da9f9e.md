<!-- Official source: https://cloud.tencent.com/document/product/1823/134036 -->
<!-- Source SHA-256: 4f1c930f8c9767cbc3300f782db9317b7ca95083ae2ed701ec19f1e48ccae2c1 -->

# 创建推理服务

官方来源：https://cloud.tencent.com/document/product/1823/134036
最近更新时间：2026-07-14 03:02:36

## 1. 接口描述

接口请求域名： tokenhub.tencentcloudapi.com 。

创建推理服务。

创建一个在线推理服务，创建成功后返回推理服务 ID。

默认接口请求频率限制：20次/秒。

<div class="rno-api-explorer">
    <div class="rno-api-explorer-inner">
        <div class="rno-api-explorer-hd">
            <div class="rno-api-explorer-title">
                推荐使用 API Explorer
            </div>
            <a href="https://console.cloud.tencent.com/api/explorer?Product=tokenhub&Version=2026-03-22&Action=CreateEndpoint" class="rno-api-explorer-btn" hotrep="doc.api.explorerbtn"><i class="rno-icon-explorer"></i>点击调试</a>
        </div>
        <div class="rno-api-explorer-body">
            <div class="rno-api-explorer-cont">
                API Explorer 提供了在线调用、签名验证、SDK 代码生成和快速检索接口等能力。您可查看每次调用的请求内容和返回结果以及自动生成 SDK 调用示例。
            </div>
        </div>
    </div>
</div>

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数和部分公共参数，完整公共参数列表见 [公共请求参数](/document/api/1823/132283)。

| 参数名称 | 必选 | 类型 | 描述 |
|---------|---------|---------|---------|
| Action | 是 | String | [公共参数](/document/api/1823/132283)，本接口取值：CreateEndpoint。 |
| Version | 是 | String | [公共参数](/document/api/1823/132283)，本接口取值：2026-03-22。 |
| Region | 是 | String | [公共参数](/document/api/1823/132283)，详见产品支持的 [地域列表](/document/api/1823/132283#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)。 |
| EndpointName | 是 | String | <p>服务名称。最大 64 字符。</p><br/>示例值：test-endpoint |
| ModelId | 是 | String | <p>模型 ID。可通过 DescribeModelList 接口获取。</p><br/>示例值：deepseek-v4-pro |
| ChargeType | 是 | String | <p>计费方式。取值：FREE（免费体验）、TOKEN（按 Token 计费）、TPM（TPM 保障）、COMPUTE_UNIT（按算力单元计费）。</p><br/>示例值：TOKEN |
| RPM | 否 | Integer | <p>RPM（每分钟请求数）限流上限。可选。必须大于 0，且不能超过用户在该模型上的 RPM 上限。不传则使用默认值（60）。</p><br/>示例值：100 |
| TPM | 否 | Integer | <p>TPM（每分钟 Token 数）限流上限，单位为 tokens/min。可选。必须大于 0，且不能超过用户在该模型上的 TPM 上限。设置后会同时作用于输入 TPM 和输出 TPM。不传则使用默认值（0 表示不限流）。</p><br/>示例值：1000000 |
| AutoAdjustQuota | 否 | Integer | <p>自动调整配额</p><br/>示例值：1 |
| EndpointId | 否 | String | <p>自定义推理服务 id</p><br/>示例值：ep-123456 |

## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| EndpointId | String | <p>推理服务 ID。</p><br/>示例值：ep-abcd123|
| Endpoint | [EndpointCreateDetail](/document/api/1823/132279#EndpointCreateDetail) | <p>推理服务详情信息。</p>|
| StopReason | String | <p>停止原因。当推理服务状态为已停止时返回。取值：FREE_QUOTA_EXHAUSTED（免费额度已用尽）、NO_FREE_PACKAGE（无可用免费包）、INSUFFICIENT_BALANCE（余额不足）、BILLING_ISOLATED（账户欠费隔离）、INTERNAL_ERROR（内部错误）。</p><br/>示例值：INSUFFICIENT_BALANCE|
| RequestId | String | 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。|

## 4. 示例

### 示例1 正常响应

#### 输入示例

```
POST / HTTP/1.1
Host: tokenhub.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: CreateEndpoint
<公共请求参数>

{
    "EndpointName": "test-endpoint",
    "ModelId": "deepseek-v3.2",
    "ChargeType": "FREE"
}
```

#### 输出示例

```json
{
    "Response": {
        "Endpoint": {},
        "EndpointId": "ep-mxorl8ln",
        "RequestId": "41cb8232-655d-42b4-b021-4f500866bd57"
    }
}
```


## 5. 开发者资源

### 腾讯云 API 平台

[腾讯云 API 平台](https://cloud.tencent.com/api) 是综合 API 文档、错误码、API Explorer 及 SDK 等资源的统一查询平台，方便您从同一入口查询及使用腾讯云提供的所有 API 服务。

### API Inspector

用户可通过 [API Inspector](https://cloud.tencent.com/document/product/1278/49361) 查看控制台每一步操作关联的 API 调用情况，并自动生成各语言版本的 API 代码，也可前往 [API Explorer](https://cloud.tencent.com/document/product/1278/46697) 进行在线调试。

### SDK

云 API 3.0 提供了配套的开发工具集（SDK），支持多种编程语言，能更方便的调用 API。
* Tencent Cloud SDK 3.0 for Python: [CNB](https://cnb.cool/tencent/cloud/api/sdk/tencentcloud-sdk-python/-/blob/master/tencentcloud/tokenhub/v20260322/tokenhub_client.py), [GitHub](https://github.com/TencentCloud/tencentcloud-sdk-python/blob/master/tencentcloud/tokenhub/v20260322/tokenhub_client.py), [Gitee](https://gitee.com/TencentCloud/tencentcloud-sdk-python/blob/master/tencentcloud/tokenhub/v20260322/tokenhub_client.py)
* Tencent Cloud SDK 3.0 for Java: [CNB](https://cnb.cool/tencent/cloud/api/sdk/tencentcloud-sdk-java/-/blob/master/src/main/java/com/tencentcloudapi/tokenhub/v20260322/TokenhubClient.java), [GitHub](https://github.com/TencentCloud/tencentcloud-sdk-java/blob/master/src/main/java/com/tencentcloudapi/tokenhub/v20260322/TokenhubClient.java), [Gitee](https://gitee.com/TencentCloud/tencentcloud-sdk-java/blob/master/src/main/java/com/tencentcloudapi/tokenhub/v20260322/TokenhubClient.java)
* Tencent Cloud SDK 3.0 for PHP: [CNB](https://cnb.cool/tencent/cloud/api/sdk/tencentcloud-sdk-php/-/blob/master/src/TencentCloud/Tokenhub/V20260322/TokenhubClient.php), [GitHub](https://github.com/TencentCloud/tencentcloud-sdk-php/blob/master/src/TencentCloud/Tokenhub/V20260322/TokenhubClient.php), [Gitee](https://gitee.com/TencentCloud/tencentcloud-sdk-php/blob/master/src/TencentCloud/Tokenhub/V20260322/TokenhubClient.php)
* Tencent Cloud SDK 3.0 for Go: [CNB](https://cnb.cool/tencent/cloud/api/sdk/tencentcloud-sdk-go/-/blob/master/tencentcloud/tokenhub/v20260322/client.go), [GitHub](https://github.com/TencentCloud/tencentcloud-sdk-go/blob/master/tencentcloud/tokenhub/v20260322/client.go), [Gitee](https://gitee.com/TencentCloud/tencentcloud-sdk-go/blob/master/tencentcloud/tokenhub/v20260322/client.go)
* Tencent Cloud SDK 3.0 for Node.js: [CNB](https://cnb.cool/tencent/cloud/api/sdk/tencentcloud-sdk-nodejs/-/blob/master/src/services/tokenhub/v20260322/tokenhub_client.ts), [GitHub](https://github.com/TencentCloud/tencentcloud-sdk-nodejs/blob/master/src/services/tokenhub/v20260322/tokenhub_client.ts), [Gitee](https://gitee.com/TencentCloud/tencentcloud-sdk-nodejs/blob/master/src/services/tokenhub/v20260322/tokenhub_client.ts)
* Tencent Cloud SDK 3.0 for .NET: [CNB](https://cnb.cool/tencent/cloud/api/sdk/tencentcloud-sdk-dotnet/-/blob/master/TencentCloud/Tokenhub/V20260322/TokenhubClient.cs), [GitHub](https://github.com/TencentCloud/tencentcloud-sdk-dotnet/blob/master/TencentCloud/Tokenhub/V20260322/TokenhubClient.cs), [Gitee](https://gitee.com/TencentCloud/tencentcloud-sdk-dotnet/blob/master/TencentCloud/Tokenhub/V20260322/TokenhubClient.cs)
* Tencent Cloud SDK 3.0 for C++: [CNB](https://cnb.cool/tencent/cloud/api/sdk/tencentcloud-sdk-cpp/-/blob/master/tokenhub/src/v20260322/TokenhubClient.cpp), [GitHub](https://github.com/TencentCloud/tencentcloud-sdk-cpp/blob/master/tokenhub/src/v20260322/TokenhubClient.cpp), [Gitee](https://gitee.com/TencentCloud/tencentcloud-sdk-cpp/blob/master/tokenhub/src/v20260322/TokenhubClient.cpp)
* Tencent Cloud SDK 3.0 for Ruby: [CNB](https://cnb.cool/tencent/cloud/api/sdk/tencentcloud-sdk-ruby/-/blob/master/tencentcloud-sdk-tokenhub/lib/v20260322/client.rb), [GitHub](https://github.com/TencentCloud/tencentcloud-sdk-ruby/blob/master/tencentcloud-sdk-tokenhub/lib/v20260322/client.rb), [Gitee](https://gitee.com/TencentCloud/tencentcloud-sdk-ruby/blob/master/tencentcloud-sdk-tokenhub/lib/v20260322/client.rb)

### 命令行工具

* [Tencent Cloud CLI 3.0](https://cloud.tencent.com/document/product/440/6176)

## 6. 错误码

以下仅列出了接口业务逻辑相关的错误码，其他错误码详见 [公共错误码](/document/api/1823/132288#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。

| 错误码 | 描述 |
|---------|---------|
| FailedOperation.CreateInstanceFailed | FailedOperation.CreateInstanceFailed |
| FailedOperation.EnablePostPaidFailed | FailedOperation.EnablePostPaidFailed |
| FailedOperation.EndpointAlreadyExists | FailedOperation.EndpointAlreadyExists |
| FailedOperation.FreeQuotaExhausted | FailedOperation.FreeQuotaExhausted |
| FailedOperation.PackageQueryFailed | FailedOperation.PackageQueryFailed |
| FailedOperation.PurchaseTpmFailed | FailedOperation.PurchaseTPMFailed |
| InternalError.InternalError | InternalError.InternalError |
| InvalidParameter.InvalidParameter | InvalidParameter.InvalidParameter |
| InvalidParameter.ModelIdNotFound | InvalidParameter.ModelIdNotFound |
| InvalidParameter.QPMLimitExceeded | InvalidParameter.QPMLimitExceeded |
| InvalidParameter.TPMBelowQuota | InvalidParameter.TPMBelowQuota |
| InvalidParameter.TPMLimitExceeded | InvalidParameter.TPMLimitExceeded |
| InvalidParameterValue.EndpointNameTooLong | InvalidParameterValue.EndpointNameTooLong |
| InvalidParameterValue.InvalidParameterValue | InvalidParameterValue.InvalidParameterValue |
| LimitExceeded.EndpointQuota | LimitExceeded.EndpointQuota |
| MissingParameter.MissingParameter | MissingParameter.MissingParameter |
| UnauthorizedOperation.UnauthorizedOperation | UnauthorizedOperation.UnauthorizedOperation |
