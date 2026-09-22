<!-- Official source: https://klingai.com/document-api/api/assets/billing-deduction/package.md -->
<!-- Source SHA-256: 17c646b276a674ba90bbc6870caed4e28c557033796a4ee8c5ca9dc45b98f30c -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://klingai.com/document-api/llms.txt
> Use this file to discover all available pages before exploring further.

# 资源包抵扣明细

> 来源: https://klingai.com/document-api/api/assets/billing-deduction/package
> 语言: zh
> 当前 Tab: 资源包抵扣明细
> 同组 Tab: 额度抵扣明细 / 资源包抵扣明细
> 此内容为面向 LLM 优化的 Markdown，已展开页面内 Tab，并省略页面目录、复制按钮等 UI 控件。

---

## 导出资源包抵扣明细

### 接口概览

- Method: `POST`
- Path: `/account/billing/package`
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
| `filters` | array | 否 | - | - | 查询任务筛选维度，如：API Key名称、资源包类型、资源包名称、资源包ID。 |
| `filters[].key` | string | 是 | - | `api_key_name`, `product_type`, `package_name`, `package_id` | 查询任务筛选维度，支持：API Key名称、资源包类型、资源包名称、资源包ID。 |
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
    },
    {
      "key": "product_type",
      "values": [
        "string"
      ]
    },
    {
      "key": "package_name",
      "values": [
        "string"
      ]
    },
    {
      "key": "package_id",
      "values": [
        "string"
      ]
    }
  ]
  ```
- `filters`: 当前参数与cursor参数互斥：
    - cursor参数不为空时，当前参数无效。
- `filters[].key`: api_key_name：按API Key名称查询，values填写要筛选的API Key名称。
  - product_type：按资源包类型查询，values填写要筛选的资源包类型，枚举值：video、image、try-on，依次对应视频资源包、图片资源包、虚拟试穿资源包。
  - package_name：按资源包名称查询，values填写要筛选的资源包名称。
  - package_id：按资源包ID查询，values填写要筛选的资源包ID。
  - 设置多个不同维度筛选条件时，筛选结果取交集。
  - package_name 参数与 package_id 参数互斥，不可同时设置为筛选条件。
- `filters[].values`: 可通过设置多个values参数的值实现选择多个查询条件，筛选结果取并集。
- `cursor`: 参数值来自上次查询时返回的next_cursor参数。
- `cursor`: 当前参数不为空时，会优先基于当前参数值查询，此时其他参数无效，包括时间范围（start_time&end_time）、筛选条件（filters）、最大查询量（limit）。

### Request Example

```bash
curl --location --request POST 'https://api-beijing.klingai.com/account/billing/package' \
--header 'Authorization: Bearer xxx' \
--header 'Content-Type: application/json' \
--data-raw '{
  "start_time": 1751284003293,
  "end_time": 1782219793736,
  "cursor": "",
  "limit": 50,
  "filters": [
    {
      "key": "product_type",
      "values": []
    },
    {
      "key": "api_key_name",
      "values": []
    },
    {
      "key": "package_name",
      "values": []
    },
    {
      "key": "package_id",
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
          "package_id": "string", // 资源包ID
          "product_type": "video", // 资源包类型，枚举值：video、image、try-on；依次对应视频资源包、图片资源包、虚拟试穿资源包
          "task_id": "string", // 系统生成的任务ID
          "api_key_name": "string", // API Key名称
          "product_function": "string", // 任务相关功能，如：Image to Video
          "model_name": "string", // 任务所用模型版本，与创建任务时所选模型版本一致
          "resolution": "string", // 生成结果的分辨率，枚举值：720p、1080p、4k（较早版本API通过mode参数定义分辨率，与当前参数对应关系为：720p=std、1080p=pro）
          "duration": "5.04", // 生成视频的时长（当前参数仅生效于生成视频任务相关明细）
          "refer_video_input": true, // 生成视频时是否有参考视频，布尔值：true, false（当前参数仅生效于生成视频任务相关明细）
          "video_sound": "native", // 生成的视频是否包含声音，枚举值：native、original、off；依次对应随画面生成声音、保留参考视频原声、无声音（当前参数仅生效于生成视频任务相关明细）
          "voice_control": false, // 生成的视频是否有指定音色，布尔值：true, false；依次对应有指定音色、未指定音色（当前参数仅生效于生成视频任务相关明细）
          "deduction_time": "1779549455861", // 积分抵扣时间，Unix时间戳、单位ms时间
          "unit_before_deduction": 13037.3, // 积分抵扣前余额
          "deduction_amount": 5.0, // 积分抵扣量
          "unit_after_deduction": 13032.3 // 积分抵扣后余额
        }
      ],
      "count": 20 // 本次查询的结果的数量
    },
    "next_cursor": "string", // 游标信息，可用继续查询后续
    "has_more": true // 基于游标信息，是否还有未查询到的数据，boolean值
  }
}
```
