<!-- Official source: https://klingai.com/document-api/api/video/lip-sync/face-detection.md -->
<!-- Source SHA-256: f7021ad95bf158406fdb1f227bfe5c2d9abfec8c7b14b06254c2d637708e7ec1 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://klingai.com/document-api/llms.txt
> Use this file to discover all available pages before exploring further.

# 人脸识别

> 来源: https://klingai.com/document-api/api/video/lip-sync/face-detection
> 语言: zh
> 当前 Tab: 人脸识别
> 同组 Tab: 对口型 / 人脸识别
> 此内容为面向 LLM 优化的 Markdown，已展开页面内 Tab，并省略页面目录、复制按钮等 UI 控件。

---

## 人脸识别

### 接口概览

- Method: `POST`
- Path: `/v1/videos/identify-face`
- Auth: `Authorization: Bearer <API_KEY>`
- Content-Type: `application/json`

### 说明

识别视频中的人脸以进行对口型处理。

### Headers

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `Content-Type` | string | 是 | `application/json` | - | 数据交换格式 |
| `Authorization` | string | 是 | - | - | 鉴权信息，参考接口鉴权 |

### Request Body

| 字段路径 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `video_id` | string | 否 | - | - | 通过可灵 AI 生成的视频的 ID |
| `video_url` | string | 否 | - | - | 所上传视频的获取 URL |

#### Request Body 字段补充说明

- `video_id`: 用于指定视频、判断视频是否可用于对口型服务
- `video_id`: 与 video_url 参数二选一填写，不能同时为空，也不能同时有值
- `video_id`: 仅支持使用 30 天内生成的时长不超过 60 秒的视频
- `video_url`: 用于指定视频，并判断视频是否可用于对口型服务
- `video_url`: 与 video_id 参数二选一填写，不能同时为空，也不能同时有值
- `video_url`: 视频文件支持 .mp4/.mov，文件大小不超过 100MB，视频时长不超过 60s 且不短于 2s，仅支持 720p 和 1080p、长宽的边长均位于 512px~2160px 之间，上述校验不通过会返回错误码等信息
- `video_url`: 系统会校验视频内容，如有问题会返回错误码等信息

### Request Example

```bash
curl --request POST \
  --url https://api-beijing.klingai.com/v1/videos/identify-face \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
    "video_url": "https://p1-kling.klingai.com/kcdn/cdn-kcdn112452/kling-qa-test/kling20260206mp4.mp4",
    "video_id": ""
  }'
```

### Response Example

```json
{
  "code": 0, // 错误码；具体定义见错误码
  "message": "string", // 错误信息
  "request_id": "string", // 请求ID，系统生成，用于跟踪请求、排查问题
  "data": {
    "session_id": "id", // 会话ID
    "final_unit_deduction": "string", // 任务最终扣减积分数值
    "final_balance_deduction": { // 额度扣减信息
      "quota": "string", // 额度扣减折扣价
      "list_price": "string" // 额度扣减刊例价
    },
    "face_data": [ //人脸数据列表
      {
        "face_id": "string", // 人脸ID
        "face_image": "url", // 人脸图片URL
        "start_time": 0, // 人脸出现开始时间，单位ms
        "end_time": 5200 //人脸出现结束时间，单位ms
      }
    ]
  }
}
```
