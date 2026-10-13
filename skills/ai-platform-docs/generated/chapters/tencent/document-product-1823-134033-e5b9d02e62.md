<!-- Official source: https://cloud.tencent.com/document/product/1823/134033 -->
<!-- Source SHA-256: 472d58a947e245233e0b1af96053e26fa9d8538a0b65a1b1335a84c9c5d0f421 -->

# 查询模型接入点列表

官方来源：https://cloud.tencent.com/document/product/1823/134033
最近更新时间：2026-07-14 03:02:36

## 1. 接口描述

接口请求域名： tokenhub.tencentcloudapi.com 。

查询模型接入点列表。

以模型为基准展示所有在线文本类型模型的接入点概览，支持按状态、计费方式、创建来源等条件筛选，使用 Offset/Limit 分页。

默认接口请求频率限制：20次/秒。

<div class="rno-api-explorer">
    <div class="rno-api-explorer-inner">
        <div class="rno-api-explorer-hd">
            <div class="rno-api-explorer-title">
                推荐使用 API Explorer
            </div>
            <a href="https://console.cloud.tencent.com/api/explorer?Product=tokenhub&Version=2026-03-22&Action=DescribeModelEndpointList" class="rno-api-explorer-btn" hotrep="doc.api.explorerbtn"><i class="rno-icon-explorer"></i>点击调试</a>
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
| Action | 是 | String | [公共参数](/document/api/1823/132283)，本接口取值：DescribeModelEndpointList。 |
| Version | 是 | String | [公共参数](/document/api/1823/132283)，本接口取值：2026-03-22。 |
| Region | 是 | String | [公共参数](/document/api/1823/132283)，详见产品支持的 [地域列表](/document/api/1823/132283#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)。 |
| Offset | 否 | Integer | <p>偏移量，从 0 开始，默认为 0。</p><br/>示例值：0 |
| Limit | 否 | Integer | <p>每页返回数量，默认为 20，最大值为 100。</p><br/>示例值：100 |
| Filters.N | 否 | Array of [RequestFilter](/document/api/1823/132279#RequestFilter) | <p>过滤条件列表。支持的过滤字段：Status（状态，取值 ACTIVE/INACTIVE）、ChargeType（计费方式，取值 FREE/TOKEN）、RequestSource（创建来源，取值 MC/GW）、ModelName（模型名称）、ModelId（模型 ID）、PaymentEnabled（是否已开启后付费，取值 true/false）。</p> |
| Sorts.N | 否 | Array of [RequestSort](/document/api/1823/132279#RequestSort) | <p>排序条件列表。支持的排序字段：CreatedTime、UpdatedTime。不传时使用默认排序规则。</p> |

## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| ModelEndpointSet | Array of [ModelEndpointView](/document/api/1823/132279#ModelEndpointView) | <p>模型接入点列表。</p>|
| TotalCount | Integer | <p>符合条件的总数。</p><br/>示例值：543|
| RequestId | String | 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。|

## 4. 示例

### 示例1 成功示例

#### 输入示例

```
POST / HTTP/1.1
Host: tokenhub.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeModelEndpointList
<公共请求参数>

{}
```

#### 输出示例

```json
{
    "Response": {
        "ModelEndpointSet": [
            {
                "ModelId": "hunyuan-role-latest",
                "ModelName": "Hunyuan-role",
                "PaymentEnabled": false,
                "ServiceType": "TEXT_GENERATION",
                "Status": "INACTIVE"
            },
            {
                "ModelId": "minimax-m2.5",
                "ModelName": "MiniMax-M2.5",
                "PaymentEnabled": false,
                "ServiceType": "TEXT_GENERATION",
                "Status": "INACTIVE"
            },
            {
                "ModelId": "glm-5",
                "ModelName": "GLM-5",
                "PaymentEnabled": false,
                "ServiceType": "TEXT_GENERATION",
                "Status": "INACTIVE"
            },
            {
                "ModelId": "kimi-k2.5",
                "ModelName": "kimi-k2.5",
                "PaymentEnabled": false,
                "ServiceType": "TEXT_GENERATION",
                "Status": "INACTIVE"
            },
            {
                "ModelId": "deepseek-v3.2",
                "ModelName": "Deepseek-v3.2",
                "PaymentEnabled": false,
                "ServiceType": "TEXT_GENERATION",
                "Status": "INACTIVE"
            },
            {
                "ModelId": "hunyuan-2.0-instruct-20251111",
                "ModelName": "HY 2.0 Instruct",
                "PaymentEnabled": false,
                "ServiceType": "TEXT_GENERATION",
                "Status": "INACTIVE"
            },
            {
                "ModelId": "hunyuan-2.0-thinking-20251109",
                "ModelName": "HY 2.0 Think",
                "PaymentEnabled": false,
                "ServiceType": "TEXT_GENERATION",
                "Status": "INACTIVE"
            },
            {
                "ModelId": "kimi-k2-thinking-turbo",
                "ModelName": "kimi-k2-thinking-turbo",
                "PaymentEnabled": false,
                "ServiceType": "TEXT_GENERATION",
                "Status": "INACTIVE"
            },
            {
                "ModelId": "deepseek-v3.1-terminus",
                "ModelName": "Deepseek-v3.1",
                "PaymentEnabled": false,
                "ServiceType": "TEXT_GENERATION",
                "Status": "INACTIVE"
            },
            {
                "ModelId": "kimi-k2-turbo-preview",
                "ModelName": "kimi-k2-turbo-preview",
                "PaymentEnabled": false,
                "ServiceType": "TEXT_GENERATION",
                "Status": "INACTIVE"
            },
            {
                "ModelId": "deepseek-r1-0528",
                "ModelName": "Deepseek-r1-0528",
                "PaymentEnabled": false,
                "ServiceType": "TEXT_GENERATION",
                "Status": "INACTIVE"
            },
            {
                "ModelId": "deepseek-v3-0324",
                "ModelName": "Deepseek-v3-0324",
                "PaymentEnabled": false,
                "ServiceType": "TEXT_GENERATION",
                "Status": "INACTIVE"
            }
        ],
        "RequestId": "96f7a35a-31fe-47c1-b481-ff9c95f716ee",
        "TotalCount": 12
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
| InternalError.InternalError | InternalError.InternalError |
| InvalidParameter.InvalidParameter | InvalidParameter.InvalidParameter |
| InvalidParameter.Limit | InvalidParameter.Limit |
| InvalidParameterValue.InvalidParameterValue | InvalidParameterValue.InvalidParameterValue |
| MissingParameter.MissingParameter | MissingParameter.MissingParameter |
| UnauthorizedOperation.UnauthorizedOperation | UnauthorizedOperation.UnauthorizedOperation |
