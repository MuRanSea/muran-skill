<!-- Official source: https://klingai.com/document-api/api/assets/billing-deduction/balance.md -->
<!-- Source SHA-256: ebac5226e3a378a08d352b8ca4fab6438378945ef30717d78fc786ccdecd208f -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://klingai.com/document-api/llms.txt
> Use this file to discover all available pages before exploring further.

# 额度抵扣明细

> 来源: https://klingai.com/document-api/api/assets/billing-deduction/balance
> 语言: zh
> 当前 Tab: 额度抵扣明细
> 同组 Tab: 额度抵扣明细 / 资源包抵扣明细
> 此内容为面向 LLM 优化的 Markdown，已展开页面内 Tab，并省略页面目录、复制按钮等 UI 控件。

---

## 导出余额抵扣明细

### 接口概览

- Method: `POST`
- Path: `/account/billing/balance`
- Auth: `Authorization: Bearer <API_KEY>`
- Content-Type: `application/json`

### Headers

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `Content-Type` | string | 是 | `application/json` | - | 数据交换格式 |
| `Authorization` | string | 是 | - | - | 鉴权信息，参考接口鉴权 |

### Request Body

| 字段路径 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `start_time` | long | 否 | - | - | 任务创建时间筛选的开始时间。 |
| `end_time` | long | 否 | - | - | 任务创建时间筛选的结束时间。 |
| `limit` | int | 否 | `500` | - | 查询任务数量。 |
| `filters` | array | 否 | - | - | 查询任务筛选维度，如：API Key名称。 |
| `filters[].key` | string | 是 | - | `api_key_name` | 查询任务筛选维度，支持：API Key名称。 |
| `filters[].values` | array | 是 | - | - | 要筛选的查询条件。 |
| `cursor` | string | 否 | - | - | 续页游标，即查询起点。 |

#### Request Body 字段补充说明

- `start_time`: Unix时间戳、单位ms。
  - 开始时间需早于结束时间。
  - 当前参数与cursor参数互斥：
    - 首轮查询时当前参数必填，即cursor参数为空时必填。
    - cursor参数不为空时，当前参数无效。
- `end_time`: Unix时间戳、单位ms。
  - 结束时间需晚于开始时间。
  - 当前参数与cursor参数互斥：
    - 首轮查询时当前参数必填，即cursor参数为空时必填。
    - cursor参数不为空时，当前参数无效。
- `limit`: 最大值500；当筛选结果数量不足500时候，展示所有结果
  - 当前参数与cursor参数互斥：
    - cursor参数不为空时，当前参数无效。
- `filters`: 可通过设置多个同类型查询条件实现多选，筛选结果取并集；设置多个不同维度筛选条件时，筛选结果取交集。
  - 通过key&value的方式设置查询条件，参考格式如下，参数说明详见下文：
- `filters`: ```JSON
  "filters": [
    {
      "key": "api_key_name",
      "values": [
        "string"
      ]
    }
  ]
  ```
- `filters`: 当前参数与cursor参数互斥：
    - cursor参数不为空时，当前参数无效。
- `filters[].key`: api_key_name：API Key名称。
  - 设置多个不同维度筛选条件时，筛选结果取交集。
- `filters[].values`: 可通过设置多个values参数的值实现选择多个查询条件，筛选结果取并集。
- `cursor`: 参数值来自上次查询时返回的next_cursor参数。
- `cursor`: 当前参数不为空时，会优先基于当前参数值查询，此时其他参数无效，包括时间范围（start_time&end_time）、筛选条件（filters）、最大查询量（limit）。

### Request Example

```bash
curl --location --request POST 'https://api-beijing.klingai.com/account/billing/balance' \
--header 'Authorization: Bearer xxx' \
--header 'Content-Type: application/json; charset=utf-8' \
--data-raw '{
  "start_time": 1741284003293,
  "end_time": 1792219793736,
  "cursor": "",
  "limit": 50,
  "filters": [
    {
      "key": "api_key_name",
      "values": []
    }
  ]
}'
```

### Response Example

```json
{
  "code": 0, //错误码；具体定义见错误码
  "message": "string", //错误信息
  "request_id": "string", //请求ID，系统生成，用于跟踪请求、排查问题
  "data": {
    "result": {
      "detail": [
        {
          "task_id": "string", // 系统生成的任务ID
          "api_key_name": "string", // API Key名称
          "product_function": "string", // 任务相关功能，如：Image to Video
          "model_name": "string", // 任务所用模型版本，与创建任务时所选模型版本一致
          "resolution": "string", // 生成结果的分辨率，枚举值：720p、1080p、4k（较早版本API通过mode参数定义分辨率，与当前参数对应关系为：720p=std、1080p=pro）
          "duration": "5.04", // 生成视频的时长（当前参数仅生效于生成视频任务相关明细）
          "refer_video_input": true, // 生成视频时是否有参考视频，布尔值：true, false（当前参数仅生效于生成视频任务相关明细）
          "video_sound": "native", // 生成的视频是否包含声音，枚举值：native、original、off；依次对应随画面生成声音、保留参考视频原声、无声音（当前参数仅生效于生成视频任务相关明细）
          "voice_control": false, // 生成的视频是否有指定音色，布尔值：true, false；依次对应有指定音色、未指定音色（当前参数仅生效于生成视频任务相关明细）
          "deduction_time": "1779549455861", // 余额抵扣时间，Unix时间戳、单位ms时间
          "cash_type": "string", // 额度类型；如果消耗的是正式额度则参数值为balance，如果是消耗的是测试金则参数值为test_balance
          "balance_before_deduction": 13037.3, // 抵扣前余额
          "deduction_amount": 5.0, // 抵扣金额
          "balance_after_deduction": 13032.3, // 抵扣后余额
          "list_price": 5.0, // 抵扣金额刊例价
          "currency": "string" // 余额单位，枚举值：CNY、USD
        }
      ],
      "count": 20 // 本次查询的结果的数量
    },
    "next_cursor": "string", // 游标信息，可用继续查询后续
    "has_more": true // 基于游标信息，是否还有未查询到的数据，boolean值
  }
}
```
