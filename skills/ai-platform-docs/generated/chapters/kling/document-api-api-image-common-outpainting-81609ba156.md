<!-- Official source: https://klingai.com/document-api/api/image/common/outpainting.md -->
<!-- Source SHA-256: 07588821e7f0ca720a3c22669669181deda74b54ce82184e44e33d2548dd25d7 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://klingai.com/document-api/llms.txt
> Use this file to discover all available pages before exploring further.

# 扩图

> 来源: https://klingai.com/document-api/api/image/common/outpainting
> 语言: zh
> 当前 Tab: 扩图
> 同组 Tab: 智能补全主体图 / 扩图
> 此内容为面向 LLM 优化的 Markdown，已展开页面内 Tab，并省略页面目录、复制按钮等 UI 控件。

---

## 创建任务

### 接口概览

- Method: `POST`
- Path: `/v1/images/editing/expand`
- Auth: `Authorization: Bearer <API_KEY>`
- Content-Type: `application/json`

### 说明

基于原始图像向任意方向扩展图像。

### Headers

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `Content-Type` | string | 是 | `application/json` | - | 数据交换格式 |
| `Authorization` | string | 是 | - | - | 鉴权信息，参考接口鉴权 |

### Request Body

| 字段路径 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `image` | string | 是 | - | - | 参考图片 |
| `up_expansion_ratio` | float | 是 | - | - | 向上扩充范围；基于原图高度的倍数而计算 |
| `down_expansion_ratio` | float | 是 | - | - | 向下扩充范围；基于原图高度的倍数而计算 |
| `left_expansion_ratio` | float | 是 | - | - | 向左扩充范围；基于原图宽度的倍数而计算 |
| `right_expansion_ratio` | float | 是 | - | - | 向右扩充范围；基于原图宽度的倍数而计算 |
| `prompt` | string | 否 | - | - | 正向文本提示词 |
| `n` | int | 否 | `1` | - | 生成图片数量 |
| `watermark_info` | object | 否 | - | - | 是否同时生成含水印的结果 |
| `callback_url` | string | 否 | - | - | 本次任务结果回调通知地址，如果配置，服务端会在任务状态发生变更时主动通知。 |
| `external_task_id` | string | 否 | - | - | 自定义任务 ID |

#### Request Body 字段补充说明

- `image`: 支持传入图片 Base64 编码或图片 URL（确保可访问）
- `image`: 注意：若您使用 Base64 方式，请不要在 Base64 编码字符串前添加任何前缀（如 `data:image/png;base64,`），直接传递 Base64 编码后的字符串即可。
- `image`: **正确的 Base64 编码参数：**
  ```plaintext
  iVBORw0KGgoAAAANSUhEUgAAAAUA...
  ```
- `image`: 错误的 Base64 编码参数（包含 data: 前缀）：
  ```plaintext
  data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA...
  ```
- `image`: 图片格式支持 .jpg / .jpeg / .png
- `image`: 图片文件大小不能超过 10MB，图片宽高尺寸不小于 300px，图片宽高比要在 1:2.5 ~ 2.5:1 之间
- `up_expansion_ratio`: 取值范围：[0, 2]，新图片整体面积不得超过原图片 3 倍
- `up_expansion_ratio`: 如原图高 20，当前参数值为 0.1，则：
    - 原图顶边距离新图顶边为 20 × 0.1 = 2，区域内均为扩图范围
- `down_expansion_ratio`: 取值范围：[0, 2]，新图片整体面积不得超过原图片 3 倍
- `down_expansion_ratio`: 如原图高 20，当前参数值为 0.2，则：
    - 原图底边距离新图底边为 20 × 0.2 = 4，区域内均为扩图范围
- `left_expansion_ratio`: 取值范围：[0, 2]，新图片整体面积不得超过原图片 3 倍
- `left_expansion_ratio`: 如原图宽 30，当前参数值为 0.3，则：
    - 原图左边距离新图左边为 30 × 0.3 = 9，区域内均为扩图范围
- `right_expansion_ratio`: 取值范围：[0, 2]，新图片整体面积不得超过原图片 3 倍
- `right_expansion_ratio`: 如原图宽 30，当前参数值为 0.4，则：
    - 原图右边距离新图右边为 30 × 0.4 = 12，区域内均为扩图范围
- `prompt`: 不能超过 2500 个字符
- `n`: 取值范围：[1, 9]
- `watermark_info`: 通过enabled参数定义，具体格式如下：
  ```json
   "watermark_info": { "enabled": boolean } 
  ```
- `watermark_info`: true 为生成，false 为不生成
- `watermark_info`: 暂不支持自定义水印
- `callback_url`: 具体通知的消息 schema 见 [Callback 协议](https://klingai.com/document-api/api/get-started/callbacks)
- `external_task_id`: 传入不会覆盖系统生成的任务 ID，但支持通过该 ID 进行任务查询
- `external_task_id`: 请注意，单用户下需要保证唯一性

### Request Example

```bash
curl --request POST \
  --url https://api-beijing.klingai.com/v1/images/editing/expand \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
    "up_expansion_ratio": 0.1495,
    "down_expansion_ratio": 0.1495,
    "left_expansion_ratio": 0.6547,
    "right_expansion_ratio": 0.6547,
    "prompt": "",
    "image": "https://p1-kling.klingai.com/kcdn/cdn-kcdn112452/kling-qa-test/dog.png",
    "n": 2,
    "external_task_id": ""
  }'
```

### Response Example

```json
{
  "code": 0, // 错误码；具体定义见错误码
  "message": "string", // 错误信息
  "request_id": "string", // 请求ID，系统生成，用于跟踪请求、排查问题
  "data": {
    "task_id": "string", // 任务ID，系统生成
    "task_info": { // 任务创建时的参数信息
      "external_task_id": "string" // 客户自定义任务ID
    },
    "task_status": "string", // 任务状态，枚举值：submitted（已提交）、processing（处理中）、succeed（成功）、failed（失败）
    "created_at": 1722769557708, // 任务创建时间，Unix时间戳、单位ms
    "updated_at": 1722769557708 // 任务更新时间，Unix时间戳、单位ms
  }
}
```

## 示例代码

```Python
import math

def calculate_expansion_ratios(width, height, area_multiplier, aspect_ratio):
    """
    计算图片外围扩展区域的上下左右比例。

    参数:
    - width: 原始图片宽度
    - height: 原始图片高度
    - area_multiplier: 外围区域面积是原图的倍数
    - aspect_ratio: 外围区域的宽高比（width/height）

    返回:
    - 格式化为四位小数的字符串，如 "0.1495,0.1495,0.6547,0.6547"
    """
    # 计算目标总面积
    target_area = area_multiplier * width * height

    # 计算目标高度和宽度（保持宽高比）
    target_height = math.sqrt(target_area / aspect_ratio)
    target_width = target_height * aspect_ratio

    # 计算扩展像素
    expand_top = (target_height - height) / 2
    expand_bottom = expand_top
    expand_left = (target_width - width) / 2
    expand_right = expand_left

    # 计算相对比例
    top_ratio = expand_top / height
    bottom_ratio = expand_bottom / height
    left_ratio = expand_left / width
    right_ratio = expand_right / width

    # 格式化为四位小数
    return f"{top_ratio:.4f},{bottom_ratio:.4f},{left_ratio:.4f},{right_ratio:.4f}"

# 示例：内部100x100，外部3倍面积，16:9
print(calculate_expansion_ratios(100, 100, 3, 16/9))
# 输出: "0.1495,0.1495,0.6547,0.6547"
```

---

## 查询任务（单个）

### 接口概览

- Method: `GET`
- Path: `/v1/images/editing/expand/{id}`
- Auth: `Authorization: Bearer <API_KEY>`
- Content-Type: `application/json`

### Headers

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `Content-Type` | string | 是 | `application/json` | - | 数据交换格式 |
| `Authorization` | string | 是 | - | - | 鉴权信息，参考接口鉴权 |

### Path Params

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `task_id` | string | 是 | - | - | 图片生成的任务ID。请求路径参数，直接将值填写在请求路径中 |
| `external_task_id` | string | 否 | - | - | 用户自定义任务 ID |

#### Path Params 字段补充说明

- `external_task_id`: 创建任务时填写的 external_task_id，与 task_id 两种查询方式二选一
  - 请注意，单用户下需要保证唯一性

### Request Example

```bash
curl --request GET \
  --url https://api-beijing.klingai.com/v1/images/editing/expand/{id} \
  --header 'Authorization: Bearer <token>'
```

### Response Example

```json
{
  "code": 0, // 错误码；具体定义见错误码
  "message": "string", // 错误信息
  "request_id": "string", // 请求ID，系统生成，用于跟踪请求、排查问题
  "data": {
    "task_id": "string", // 任务ID，系统生成
    "task_status": "string", // 任务状态，枚举值：submitted（已提交）、processing（处理中）、succeed（成功）、failed（失败）
    "task_status_msg": "string", // 任务状态信息，当任务失败时展示失败原因（如触发平台的内容风控等）
    "task_info": { // 任务创建时的参数信息
      "external_task_id": "string" // 客户自定义任务ID
    },
    "final_unit_deduction": "string", // 任务最终扣减积分数值
    "final_balance_deduction": { // 额度扣减信息
      "quota": "string", // 额度扣减折扣价
      "list_price": "string" // 额度扣减刊例价
    },
    "watermark_info": {
      "enabled": boolean
    },
    "created_at": 1722769557708, // 任务创建时间，Unix时间戳、单位ms
    "updated_at": 1722769557708, // 任务更新时间，Unix时间戳、单位ms
    "task_result": {
      "images": [
        {
          "index": 0, // 图片编号，0-9
          "url": "string", // 生成图片的URL（请注意，为保障信息安全，生成的图片/视频会在30天后被清理，请及时转存）
        }
      ]
    }
  }
}
```

---

## 查询任务（列表）

### 接口概览

- Method: `GET`
- Path: `/v1/images/editing/expand`
- Auth: `Authorization: Bearer <API_KEY>`
- Content-Type: `application/json`

### Headers

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `Content-Type` | string | 是 | `application/json` | - | 数据交换格式 |
| `Authorization` | string | 是 | - | - | 鉴权信息，参考接口鉴权 |

### Query Params

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `pageNum` | int | 否 | `1` | - | 页码 |
| `pageSize` | int | 否 | `30` | - | 每页数据量 |

#### Query Params 字段补充说明

- `pageNum`: 取值范围：[1, 1000]
- `pageSize`: 取值范围：[1, 500]

### Request Example

```bash
curl --request GET \
  --url 'https://api-beijing.klingai.com/v1/images/editing/expand?pageNum=1&pageSize=30' \
  --header 'Authorization: Bearer <token>'
```

### Response Example

```json
{
  "code": 0, // 错误码；具体定义见错误码
  "message": "string", // 错误信息
  "request_id": "string", // 请求ID，系统生成，用于跟踪请求、排查问题
  "data": [
    {
      "task_id": "string", // 任务ID，系统生成
      "task_status": "string", // 任务状态，枚举值：submitted（已提交）、processing（处理中）、succeed（成功）、failed（失败）
      "task_status_msg": "string", // 任务状态信息，当任务失败时展示失败原因（如触发平台的内容风控等）
      "task_info": { // 任务创建时的参数信息
        "external_task_id": "string" // 客户自定义任务ID
      },
      "final_unit_deduction": "string", // 任务最终扣减积分数值
      "final_balance_deduction": { // 额度扣减信息
        "quota": "string", // 额度扣减折扣价
        "list_price": "string" // 额度扣减刊例价
      },
      "watermark_info": {
        "enabled": boolean
      },
      "created_at": 1722769557708, // 任务创建时间，Unix时间戳、单位ms
      "updated_at": 1722769557708, // 任务更新时间，Unix时间戳、单位ms
      "task_result": {
        "images": [
          {
            "index": 0, // 图片编号，0-9
            "url": "string", // 生成图片的URL（请注意，为保障信息安全，生成的图片/视频会在30天后被清理，请及时转存）
            "watermark_url": "string", // 含水印视频下载URL，防盗链格式
          }
        ]
      }
    }
  ]
}
```
