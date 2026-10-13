<!-- Official source: https://cloud.tencent.com/document/product/1823/132340 -->
<!-- Source SHA-256: c6650ab52319b9b6cc823b337312efe8fd9cefd819e6c2aec495b76acb3db833 -->

# 查询用量排行列表

官方来源：https://cloud.tencent.com/document/product/1823/132340
最近更新时间：2026-09-14 03:04:13

## 1. 接口描述

接口请求域名： tokenhub.tencentcloudapi.com 。

查询用量排行列表。

指标族（MetricType）
- `tokens`（默认）：Token 用量统计。支持 Dimension = apikey / endpoint / model。
  返回指标：TotalToken（总）/ InputTotalToken（输入）/ OutputTotalToken（输出）/ CacheTotalToken（读缓存）。
- `search`：联网搜索用量统计。支持 Dimension = apikey / endpoint / model。
  返回指标：SearchRequestCount（搜索请求数）/ SearchCount（搜索引擎调用次数）。
- `apikey_usage`：APIKey 锚定用量统计（某 APIKey 下按模型或接入点展开）。支持 Dimension = endpoint / model。
  返回指标：TotalToken（总 Token）/ InputTotalToken（输入 Token）/ OutputTotalToken（输出 Token）/ CacheTotalToken（读缓存）/ RequestCount（请求次数）/ SuccessCount（成功次数）。

响应内容
- MetricType 字段用于切换指标族，响应回显 MetricType 与 MetricKeys。
- TotalStats：时间窗内全部对象的整段聚合值。
- PageStats：当前翻页内对象的整段聚合值。
- TopList：按MetricKeys[0]降序的对象列表，含整段聚合值与逐时间点曲线。

默认接口请求频率限制：20次/秒。

<div class="rno-api-explorer">
    <div class="rno-api-explorer-inner">
        <div class="rno-api-explorer-hd">
            <div class="rno-api-explorer-title">
                推荐使用 API Explorer
            </div>
            <a href="https://console.cloud.tencent.com/api/explorer?Product=tokenhub&Version=2026-03-22&Action=DescribeUsageRankList" class="rno-api-explorer-btn" hotrep="doc.api.explorerbtn"><i class="rno-icon-explorer"></i>点击调试</a>
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
| Action | 是 | String | [公共参数](/document/api/1823/132283)，本接口取值：DescribeUsageRankList。 |
| Version | 是 | String | [公共参数](/document/api/1823/132283)，本接口取值：2026-03-22。 |
| Region | 是 | String | [公共参数](/document/api/1823/132283)，详见产品支持的 [地域列表](/document/api/1823/132283#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)。 |
| Dimension | 是 | String | <p>统计维度。取值：apikey（按 APIKey 统计）、endpoint（按接入点统计）、model（按模型统计）。</p><br/>示例值：apikey |
| StartTime | 是 | [Timestamp ISO8601](/document/api/1823/132287) | <p>起始时间（闭区间），RFC3339 格式。</p><br/>示例值：2026-04-09T00:00:00+08:00 |
| EndTime | 是 | [Timestamp ISO8601](/document/api/1823/132287) | <p>结束时间（开区间），RFC3339 格式。与 StartTime 的跨度最大 90 天。</p><br/>示例值：2026-05-09T00:00:00+08:00 |
| MetricType | 否 | String | <p>指标族切换字段。</p><ul><li>tokens（默认）：Token 用量消耗（statistics=sum），支持 Dimension = apikey/endpoint/model</li><li>search：联网搜索调用次数（statistics=sum），仅支持 Dimension = model</li><li>apikey_usage: APIKey 锚定用量统计（某 APIKey 下按模型或接入点展开）（statistics=sum），支持 Dimension = endpoint/model</li><li>其他值返回 InvalidParameter。</li></ul><br/>示例值：tokens |
| Anchor | 否 | String | <p>锚定对象，用于缩小统计范围「在哪个具体对象之内」，MetricType 为 apikey_usage 时必填。<br>各 MetricType 是否支持/如何使用 Anchor，见 MetricType 字段说明。</p><br/>示例值：ak-20260618-************************** |
| Target | 否 | String | <p>维度过滤值。空字符串表示查询全部对象，非空时仅查询指定单个对象（如指定 APIKey ID）。最大 256 字符。</p><br/>示例值：ak-20260618-************************** |
| Period | 否 | Integer | <p>统计粒度（秒）。取值：60、300、3600、86400。必须不小于跨度对应下限：跨度 ≤ 1 天 → 60；1 ~ 5 天 → 300；5 ~ 10 天 → 3600；&gt; 10 天 → 86400。仅 ShowAll=false 时使用。</p><br/>示例值：300 |
| Offset | 否 | Integer | <p>翻页起点，从 0 起，默认 0。ShowAll=true 时忽略。页大小固定为 10。</p><br/>示例值：0 |
| ShowAll | 否 | Boolean | <p>是否返回全量结果。</p><ul><li>false（默认）：按 Offset 分页返回 TopList（每页 10 条），每个对象包含<br>Series 时序点用于绘制曲线。</li><li>true：忽略 Offset，返回全量对象列表，不返回 Series（CSV 导出场景）。</li></ul><br/>示例值：false |
| SortKey | 否 | String | <p>排序指标键（可选），具体值见响应 MetricKeys。为空时按 <code>MetricKeys[0]</code> 降序排序（tokens/apikey_usage 族为 TotalToken，search 族为 SearchRequestCount）。非法值返回 InvalidParameter。</p><br/>示例值：TotalToken |

## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| Dimension | String | <p>回填请求的统计维度。</p><br/>示例值：apikey|
| MetricType | String | <p>回填请求的指标族：取值同入参 MetricType（tokens / search / apikey_usage）</p><p>枚举值：</p><ul><li>tokens： tokens</li></ul><br/>示例值：tokens|
| MetricKeys | Array of String | <p>本次响应中 Stats / Series / PageStats / TotalStats 实际包含的 metric key 列表，按MetricType 区分：<br>tokens=[TotalToken, InputTotalToken, OutputTotalToken, CacheTotalToken]<br>search=[SearchRequestCount,SearchCount]<br>apikey_usage=[TotalToken, InputTotalToken, OutputTotalToken, CacheTotalToken, RequestCount, RequestFailCount]</p><br/>示例值：["TotalToken","InputTotalToken","OutputTotalToken"]|
| ViewName | String | <p>视图（数据来源）</p><br/>示例值：tokenhub_uin_apikeyid|
| Period | Integer | <p>回填请求的统计粒度（秒）。ShowAll=true 时为 0。</p><br/>示例值：300|
| StartTime | [Timestamp ISO8601](/document/api/1823/132287) | <p>回填请求的起始时间。</p><br/>示例值：2026-04-09T00:00:00+08:00|
| EndTime | [Timestamp ISO8601](/document/api/1823/132287) | <p>回填请求的结束时间。</p><br/>示例值：2026-05-09T00:00:00+08:00|
| Total | Integer | <p>全量对象数。</p><br/>示例值：53|
| Offset | Integer | <p>回填请求的翻页起点。ShowAll=true 时为 0。</p><br/>示例值：10|
| Limit | Integer | <p>页大小，恒为 10。ShowAll=true 时为 Total。</p><br/>示例值：10|
| Timestamps | Array of Integer | <p>Series 数组对应的时间戳序列（Unix 秒）。ShowAll=true 时为空数组。</p><br/>示例值：[1715000000,1715000300]|
| TopList | Array of [UsageRankItem](/document/api/1823/132279#UsageRankItem) | <p>对象排行列表，按 SortKey 降序排序。ShowAll=false 时为当前页 10 个对象（含 Series）；ShowAll=true 时为全量对象（不含 Series，用于 CSV 导出）。</p>|
| PageStats | [UsageStats](/document/api/1823/132279#UsageStats) | <p>分页统计结果</p>|
| TotalStats | [UsageStats](/document/api/1823/132279#UsageStats) | <p>总统计结果</p>|
| SortKey | String | <p>排序指标键</p><br/>示例值：TotalToken|
| RequestId | String | 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。|

## 4. 示例

### 示例1 DescribeUsageRankList

#### 输入示例

```
POST / HTTP/1.1
Host: tokenhub.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeUsageRankList
<公共请求参数>

{
    "Dimension": "apikey",
    "StartTime": "2026-04-09T00:00:00+08:00",
    "EndTime": "2026-05-09T00:00:00+08:00",
    "Period": 86400,
    "Target": "ak-20260618-**************************"
}
```

#### 输出示例

```json
{
    "Response": {
        "Dimension": "apikey",
        "EndTime": "2026-05-09T00:00:00+08:00",
        "Limit": 0,
        "MetricKeys": [
            "TotalToken",
            "InputTotalToken",
            "OutputTotalToken"
        ],
        "MetricType": "tokens",
        "Offset": 0,
        "PageStats": {
            "InputTotalToken": 0,
            "OutputTotalToken": 0,
            "TotalToken": 0
        },
        "Period": 86400,
        "RequestId": "1568bc1c-946b-4c2b-b69f-6ba93f2bb258",
        "StartTime": "2026-04-09T00:00:00+08:00",
        "Timestamps": [],
        "TopList": [],
        "Total": 0,
        "TotalStats": {
            "InputTotalToken": 0,
            "OutputTotalToken": 0,
            "TotalToken": 0
        },
        "ViewName": "tokenhub_uin_apikeyid",
        "SortKey": "TotalToken"
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
| InternalError.BaradError | InternalError.BaradError |
| InternalError.InternalError | InternalError.InternalError |
| InvalidParameter.InvalidParameter | InvalidParameter.InvalidParameter |
| InvalidParameter.PeriodExceedsSpan | InvalidParameter.PeriodExceedsSpan |
| InvalidParameter.PeriodTooFineForData | InvalidParameter.PeriodTooFineForData |
| InvalidParameter.TooManyObjects | InvalidParameter.TooManyObjects |
| MissingParameter.MissingParameter | MissingParameter.MissingParameter |
| UnauthorizedOperation.UnauthorizedOperation | UnauthorizedOperation.UnauthorizedOperation |
