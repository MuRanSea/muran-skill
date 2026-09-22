<!-- Official source: https://klingai.com/document-api/api/video/image-recognition.md -->
<!-- Source SHA-256: 04a9cf6886470138dd8e44af2b8dd798ff488d856e63f87ce5b8474815525eae -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://klingai.com/document-api/llms.txt
> Use this file to discover all available pages before exploring further.

# 图像识别

> 来源: https://klingai.com/document-api/api/video/image-recognition
> 语言: zh
> 当前 Tab: 图像识别
> 此内容为面向 LLM 优化的 Markdown，已展开页面内 Tab，并省略页面目录、复制按钮等 UI 控件。

---

## 图像识别

### 接口概览

- Method: `POST`
- Path: `/v1/videos/image-recognize`
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
| `image` | string | 是 | - | - | 待识别的图片 |

#### Request Body 字段补充说明

- `image`: 支持传入图片Base64编码或图片URL（确保可访问）
- `image`: 请注意，若您使用base64的方式，请确保您传递的所有图像数据参数均采用Base64编码格式。在提交数据时，请不要在Base64编码字符串前添加任何前缀，例如data:image/png;base64,。正确的参数格式应该直接是Base64编码后的字符串。请仅提供Base64编码的字符串部分，以便系统能够正确处理和解析您的数据。
- `image`: 图片格式支持.jpg / .jpeg / .png。图片文件大小不能超过10MB，图片宽高尺寸不小于300px，图片宽高比介于1:2.5 ~ 2.5:1之间

### Request Example

```bash
curl --request POST \
  --url https://api-beijing.klingai.com/v1/videos/image-recognize \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
    "image": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-qa-test/multi-1.png"
  }'
```

### Response Example

```json
{
  "code": 0, // 错误码；具体定义见错误码
  "message": "string", // 错误信息
  "request_id": "string", // 请求ID，系统生成，用于跟踪请求、排查问题
  "data": {
    "task_result": {
      "images": [
        {
          "type": "object_seg", // 主体识别结果标识
          "is_contain": true, // 是否识别到主体；布尔值
          "url": "string" //识别后图片的URL，例如https://p1.a.kwimgs.com/bs2/upload-ylab-stunt/special-effect/output/HB1_PROD_ai_web_46554461/-2878350957757294165/output.png（请注意，为保障信息安全，生成的图片/视频会在30天后被清理，请及时转存）
        },
        {
          "type": "head_seg", // 含头发的人物面部识别结果标识
          "is_contain": true, // 是否识别到主体；布尔值
          "url": "string" //识别后图片的URL，例如https://p1.a.kwimgs.com/bs2/upload-ylab-stunt/special-effect/output/HB1_PROD_ai_web_46554461/-2878350957757294165/output.png（请注意，为保障信息安全，生成的图片/视频会在30天后被清理，请及时转存）
        },
        {
          "type": "face_seg", // 不含头发的人物面部识别结果标识
          "is_contain": true, // 是否识别到主体；布尔值
          "url": "string" //识别后图片的URL，例如https://p1.a.kwimgs.com/bs2/upload-ylab-stunt/special-effect/output/HB1_PROD_ai_web_46554461/-2878350957757294165/output.png（请注意，为保障信息安全，生成的图片/视频会在30天后被清理，请及时转存）
        },
        {
          "type": "cloth_seg", // 服装识别结果标识
          "is_contain": true, // 是否识别到主体；布尔值
          "url": "string" //识别后图片的URL，例如https://p1.a.kwimgs.com/bs2/upload-ylab-stunt/special-effect/output/HB1_PROD_ai_web_46554461/-2878350957757294165/output.png（请注意，为保障信息安全，生成的图片/视频会在30天后被清理，请及时转存）
        }
      ]
    },
    "final_unit_deduction": "string" // 任务最终扣减积分数值
    "final_balance_deduction": { // 额度扣减信息
      "quota": "string", // 额度扣减折扣价
      "list_price": "string" // 额度扣减刊例价
    },
  }
}
```
