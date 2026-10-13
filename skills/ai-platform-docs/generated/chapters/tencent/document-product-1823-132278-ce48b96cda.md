<!-- Official source: https://cloud.tencent.com/document/product/1823/132278 -->
<!-- Source SHA-256: 0340d9853db2b91c38a101533f62e4239635e58ba33e504e6bab7a6251b3cf0b -->

# 批量创建 Token Plan 套餐的 API Key

官方来源：https://cloud.tencent.com/document/product/1823/132278
最近更新时间：2026-05-29 10:58:22

## 1. 接口描述

接口请求域名： tokenhub.tencentcloudapi.com 。

批量创建 TokenPlan APIKey。

传入名称前缀和数量，自动按 {ApiKeyName}-{序号} 格式生成名称（如 aaa-1, aaa-2）。允许同名。支持部分成功，最多 100 条。

默认接口请求频率限制：20次/秒。

<div class="rno-api-explorer">
    <div class="rno-api-explorer-inner">
        <div class="rno-api-explorer-hd">
            <div class="rno-api-explorer-title">
                推荐使用 API Explorer
            </div>
            <a href="https://console.cloud.tencent.com/api/explorer?Product=tokenhub&Version=2026-03-22&Action=CreateTokenPlanApiKeys" class="rno-api-explorer-btn" hotrep="doc.api.explorerbtn"><i class="rno-icon-explorer"></i>点击调试</a>
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
| Action | 是 | String | [公共参数](/document/api/1823/132283)，本接口取值：CreateTokenPlanApiKeys。 |
| Version | 是 | String | [公共参数](/document/api/1823/132283)，本接口取值：2026-03-22。 |
| Region | 是 | String | [公共参数](/document/api/1823/132283)，详见产品支持的 [地域列表](/document/api/1823/132283#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)。 |
| TeamId | 是 | String | 套餐 ID。可通过DescribeTokenPlanList接口获取。<br/>示例值：tp-ent-a1b2c3d4 |
| ApiKeyName | 是 | String | API Key 名称，最大 128 字符。如果创建 API Key 的数量超过1个，实际名称格式为 {ApiKeyName}-{序号}（如 mykey-1, mykey-2）。<br/>示例值：生产Key |
| Count | 是 | Integer | 创建数量。取值范围：1 ~ 10。<br/>示例值：5 |
| AllowedModels.N | 否 | Array of String | 可用模型列表。如果套餐类型为企业版专业套餐，可以指定模型，也可以传入“all”，传入 “all“表示可以使用套餐支持的所有模型，如果要指定具体模型，传入 Model ID，“all“和具体的 Model ID 不能同时传入，如果不传则表示该API Key不支持任何模型，从而影响API Key的正常使用。如果套餐类型为企业版轻享套餐，则无论是否传入该字段，以及该字段传入什么值，都会被强制覆盖为["auto"]。<br/>示例值：["glm-5","kimi-k2.5"] |
| ExclusiveQuota | 否 | Integer | 独占额度。不传则为0，代表该 API Key 不被分配任何独占配额。单位说明如下：<br/>- 套餐类型为专业，单位取值为积分；<br/>- 套餐类型为轻享套餐，单位取值为 token。<br/>示例值：500000 |
| TotalQuota | 否 | Integer | 总额度上限。-1 表示不限，必须为 -1 或 >= API Key 当前的 ExclusiveQuota（独占额度）。不传表示不设置上限。单位说明如下：<br/>- 套餐类型为专业，单位取值为积分；<br/>- 套餐类型为轻享套餐，单位取值为 token。<br/>示例值：-1 |
| TPM | 否 | Integer | TPM（Tokens Per Minute）限制。不传使用套餐级别 TPM。必须 >= 0 且 <= 套餐 TPM。<br/>示例值：4400 |

## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| Items | Array of [CreateApiKeysResultItem](/document/api/1823/132279#CreateApiKeysResultItem) | 成功创建的项列表。|
| FailedItems | Array of [BatchCreateFailedItem](/document/api/1823/132279#BatchCreateFailedItem) | 创建失败的项列表。|
| RequestId | String | 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。|

## 4. 示例

### 示例1 CreateTokenPlanApiKeys

#### 输入示例

```
POST / HTTP/1.1
Host: tokenhub.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: CreateTokenPlanApiKeys
<公共请求参数>

{
    "TeamId": "team-3a834f2dbcf48840115cbf4b48f25342",
    "ApiKeyName": "syytest-1",
    "Count": 2,
    "AllowedModels": [
        "glm-5"
    ]
}
```

#### 输出示例

```json
{
    "Response": {
        "Items": [
            {
                "ApiKeyId": "ak-tp-20260412-b2ddcfeb599f8345cb7ad22c370b1acd"
            },
            {
                "ApiKeyId": "ak-tp-20260412-c727346e6086cc5c5594b40786957aa1"
            }
        ],
        "RequestId": "2c146814-7ca2-494b-8d09-2f4cc6cef3a2"
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
| InvalidParameterValue.InvalidParameterValue | InvalidParameterValue.InvalidParameterValue |
| MissingParameter.MissingParameter | MissingParameter.MissingParameter |
| OperationDenied | 操作被拒绝。 |
| ResourceNotFound | 资源不存在。 |
| UnauthorizedOperation.UnauthorizedOperation | UnauthorizedOperation.UnauthorizedOperation |
