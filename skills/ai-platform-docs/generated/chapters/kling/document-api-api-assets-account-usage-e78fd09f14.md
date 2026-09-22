<!-- Official source: https://klingai.com/document-api/api/assets/account-usage.md -->
<!-- Source SHA-256: abcece1d59456b8fbdf625029ceb8d6287eeb639dd00a07b22cac8a6b7d617b7 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://klingai.com/document-api/llms.txt
> Use this file to discover all available pages before exploring further.

# 账号信息查询

> 来源: https://klingai.com/document-api/api/assets/account-usage
> 语言: zh
> 当前 Tab: 账号信息查询
> 此内容为面向 LLM 优化的 Markdown，已展开页面内 Tab，并省略页面目录、复制按钮等 UI 控件。

---

## 查询账号下资源包列表及余量

### 接口概览

- Method: `GET`
- Path: `/account/costs`
- Auth: `Authorization: Bearer <API_KEY>`
- Content-Type: `application/json`

### 说明

> 注：该接口免费调用，方便您查询账号下的资源包列表和余量，但请您注意控制请求速率（QPS<=1）

### Headers

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `Content-Type` | string | 是 | `application/json` | - | 数据交换格式 |
| `Authorization` | string | 是 | - | - | 鉴权信息，参考接口鉴权 |

### Query Params

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `start_time` | int | 是 | - | - | 查询的开始时间，Unix时间戳、单位ms |
| `end_time` | int | 是 | - | - | 查询的结束时间，Unix时间戳、单位ms |
| `resource_pack_name` | string | 否 | - | - | 资源包名称，用于精准指定查询某个资源包 |

### Request Example

```bash
curl --request GET \
  --url 'https://api-beijing.klingai.com/account/costs?start_time=1726124664368&end_time=1727366400000' \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json'
```

### Response Example

```json
{
  "code": 0, // 错误码；具体定义见错误码
  "message": "string", // 错误信息
  "request_id": "string", // 请求ID，系统生成，用于跟踪请求、排查问题
  "data": {
    "code": 0, // 错误码；具体定义见错误码
    "msg": "string", // 错误信息
    "resource_pack_subscribe_infos": [ // 资源包列表
      {
        "resource_pack_name": "视频生成-10000条", // 资源包名称
        "resource_pack_id": "509f3fd3d4ab4a3f9eec5db27aa44f27", // 资源包ID
        "resource_pack_type": "decreasing_total", // 资源包类型，枚举值，"decreasing_total" = 总量递减型，"constant_period" = 周期恒定型
        "total_quantity": 200.0, // 总量
        "remaining_quantity": 118.0, // 余量（请注意，余量统计有12h的延迟）
        "purchase_time": 1726124664368, // 购买时间，Unix时间戳、单位ms
        "effective_time": 1726124664368, // 生效时间，Unix时间戳、单位ms
        "invalid_time": 1727366400000, // 失效时间，Unix时间戳、单位ms
        "status": "expired" // 资源包状态，枚举值，"toBeOnline" = 待生效，"online" = 生效中，"expired" = 已到期，"runOut" = 已用完
      }
    ]
  }
}
```
