<!-- Official source: https://cloud.tencent.com/document/product/1823/132275 -->
<!-- Source SHA-256: 8010b7a5b44b36a9f87ab893bbe710e7ed51f3f946ab4cfdad1b80cc6c7789c4 -->

# 查询 Token Plan 套餐的 API Key 列表

官方来源：https://cloud.tencent.com/document/product/1823/132275
最近更新时间：2026-05-29 10:58:20

## 1. 接口描述

接口请求域名： tokenhub.tencentcloudapi.com 。

查询 TokenPlan APIKey 列表。

返回指定套餐下的 APIKey 列表，密钥已脱敏。主账号可查看全部，子账号仅可查看自己创建的。

默认接口请求频率限制：20次/秒。

<div class="rno-api-explorer">
    <div class="rno-api-explorer-inner">
        <div class="rno-api-explorer-hd">
            <div class="rno-api-explorer-title">
                推荐使用 API Explorer
            </div>
            <a href="https://console.cloud.tencent.com/api/explorer?Product=tokenhub&Version=2026-03-22&Action=DescribeTokenPlanApiKeyList" class="rno-api-explorer-btn" hotrep="doc.api.explorerbtn"><i class="rno-icon-explorer"></i>点击调试</a>
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
| Action | 是 | String | [公共参数](/document/api/1823/132283)，本接口取值：DescribeTokenPlanApiKeyList。 |
| Version | 是 | String | [公共参数](/document/api/1823/132283)，本接口取值：2026-03-22。 |
| Region | 是 | String | [公共参数](/document/api/1823/132283)，详见产品支持的 [地域列表](/document/api/1823/132283#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)。 |
| TeamId | 是 | String | 套餐 ID。可通过DescribeTokenPlanList接口获取。<br/>示例值：tp-ent-abcdefgh |
| Offset | 否 | Integer | 分页查询偏移量，默认为 0。<br/>示例值：0 |
| Limit | 否 | Integer | 分页查询返回数量，默认为 20，最大值为 100。<br/>示例值：20 |
| Filters.N | 否 | Array of [RequestFilter](/document/api/1823/132279#RequestFilter) | 分页查询过滤条件列表。支持的过滤字段：ApiKeyId （API Key ID）、Name （API Key 名称）、Status （API Key是否可用）、StopReason （API Key停用原因）、UseStatus （API Key用户侧开关）。 |
| Sorts.N | 否 | Array of [RequestSort](/document/api/1823/132279#RequestSort) | 分页查询排序条件列表。支持的排序字段：CreatedAt（创建时间）、UpdatedAt（更新时间）。默认按 CreatedAt 降序。 |

## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| ApiKeySet | Array of [TokenPlanApiKeyListItem](/document/api/1823/132279#TokenPlanApiKeyListItem) | API Key 列表。|
| TotalCount | Integer | API Key总数量。<br/>示例值：1|
| RequestId | String | 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。|

## 4. 示例

### 示例1 DescribeTokenPlanApiKeyList

#### 输入示例

```
POST / HTTP/1.1
Host: tokenhub.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeTokenPlanApiKeyList
<公共请求参数>

{
    "TeamId": "team-3a834f2dbcf48840115cbf4b48f25342",
    "Offset": 1,
    "Limit": 1
}
```

#### 输出示例

```json
{
    "Response": {
        "ApiKeySet": [
            {
                "AllowedModels": "[\"glm-5\"]",
                "ApiKey": "sk-tp-****lQw0",
                "ApiKeyId": "ak-tp-20260407-cd2b616ac0ce4d89ffc0f8be03220606",
                "AppId": "1300056794",
                "CreatedAt": "2026-05-25T15:04:10+08:00",
                "Creator": "600000563014",
                "KeyVersion": 1,
                "Name": "syytest1111",
                "Status": "enable",
                "StopReason": "",
                "TeamId": "team-3a834f2dbcf48840115cbf4b48f25342",
                "Uin": "600000563014",
                "UpdatedAt": "2026-05-25T15:04:26+08:00",
                "UseStatus": "enable"
            }
        ],
        "RequestId": "c2e09e22-f9eb-4881-b1a2-7f9f170381d3",
        "TotalCount": 47
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
| MissingParameter.MissingParameter | MissingParameter.MissingParameter |
| UnauthorizedOperation.UnauthorizedOperation | UnauthorizedOperation.UnauthorizedOperation |
