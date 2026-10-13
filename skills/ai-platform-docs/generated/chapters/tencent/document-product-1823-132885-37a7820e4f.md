<!-- Official source: https://cloud.tencent.com/document/product/1823/132885 -->
<!-- Source SHA-256: 2182a0c867b7af35298a49c7baabe75adbb093cc2fa16ec17829c561a3425d18 -->

# 删除术语库

官方来源：https://cloud.tencent.com/document/product/1823/132885
最近更新时间：2026-06-15 01:59:22

## 1. 接口描述

接口请求域名： tokenhub.tencentcloudapi.com 。

删除术语库。

删除指定的术语库及其下所有术语条目。删除操作幂等，对不存在的术语库返回成功。调用接口后，若通过 DescribeGlossaries 接口查询不到对应术语库，则表示删除成功。

默认接口请求频率限制：20次/秒。

<div class="rno-api-explorer">
    <div class="rno-api-explorer-inner">
        <div class="rno-api-explorer-hd">
            <div class="rno-api-explorer-title">
                推荐使用 API Explorer
            </div>
            <a href="https://console.cloud.tencent.com/api/explorer?Product=tokenhub&Version=2026-03-22&Action=DeleteGlossary" class="rno-api-explorer-btn" hotrep="doc.api.explorerbtn"><i class="rno-icon-explorer"></i>点击调试</a>
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
| Action | 是 | String | [公共参数](/document/api/1823/132283)，本接口取值：DeleteGlossary。 |
| Version | 是 | String | [公共参数](/document/api/1823/132283)，本接口取值：2026-03-22。 |
| Region | 是 | String | [公共参数](/document/api/1823/132283)，详见产品支持的 [地域列表](/document/api/1823/132283#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)。 |
| GlossaryId | 是 | String | 术语库 ID。可通过 DescribeGlossaries 接口获取。<br/>示例值：glossary-a1b2c3d4 |

## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| RequestId | String | 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。|

## 4. 示例

### 示例1 DeleteGlossary

#### 输入示例

```
POST / HTTP/1.1
Host: tokenhub.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DeleteGlossary
<公共请求参数>

{
    "GlossaryId": "b76ebbab3525c1df42be2d4d33076c7c"
}
```

#### 输出示例

```json
{
    "Response": {
        "RequestId": "48ca2eec-0f0b-4ff7-a28c-18a7410e5461"
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
| UnauthorizedOperation.UnauthorizedOperation | UnauthorizedOperation.UnauthorizedOperation |
