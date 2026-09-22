<!-- Official source: https://klingai.com/document-api/api/video/avatar/text-to-speech.md -->
<!-- Source SHA-256: 5f9d3b50af72cfbcf825ab38816cece1d55e76830d5c382b2b98e14d385914cb -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://klingai.com/document-api/llms.txt
> Use this file to discover all available pages before exploring further.

# 语音合成

> 来源: https://klingai.com/document-api/api/video/avatar/text-to-speech
> 语言: zh
> 当前 Tab: 语音合成
> 同组 Tab: 数字人 / 语音合成
> 此内容为面向 LLM 优化的 Markdown，已展开页面内 Tab，并省略页面目录、复制按钮等 UI 控件。

---

## 创建任务

### 接口概览

- Method: `POST`
- Path: `/v1/audio/tts`
- Auth: `Authorization: Bearer <API_KEY>`
- Content-Type: `application/json`

### 说明

文字转语音合成 API，用于从文本生成音频。

### Headers

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `Content-Type` | string | 是 | `application/json` | - | 数据交换格式 |
| `Authorization` | string | 是 | - | - | 鉴权信息，参考接口鉴权 |

### Request Body

| 字段路径 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `text` | string | 是 | - | - | 合成音频的文案 |
| `voice_id` | string | 是 | - | - | 音色 ID |
| `voice_language` | string | 是 | `zh` | `zh`, `en` | 音色语种 |
| `voice_speed` | float | 否 | `1.0` | - | 语速 |

#### Request Body 字段补充说明

- `text`: 文本内容最大长度1000，内容过长会返回错误码等信息
- `text`: 系统会校验文本内容，如有问题会返回错误码等信息
- `voice_id`: 系统提供多种音色可供选择，具体音色效果、音色ID、音色语种对应关系[点此查看](https://docs.qingque.cn/s/home/eZQDvafJ4vXQkP8T9ZPvmye8S?identityId=2E1MlYrrPk4)；音色试听不支持自定义文案
- `voice_id`: 音色试听文件命名规范：音色名称#音色ID#音色语种
- `voice_language`: 音色语种与音色ID对应，详见上文
- `voice_speed`: 有效范围：0.8~2.0，精确至小数点后1位，超出部分将自动四舍五入

### Request Example

```bash
curl --request POST \
  --url https://api-beijing.klingai.com/v1/audio/tts \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
    "text": "Throughout my time in college, several memorable event left a significant impact on my life",
    "voice_id": "oversea_male1",
    "voice_language": "en",
    "voice_speed": 1
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
    "task_status": "string", // 任务状态，枚举值：submitted（已提交）、processing（处理中）、succeed（成功）、failed（失败）
    "task_status_msg": "string", // 任务状态信息，当任务失败时展示失败原因（如触发平台的内容风控等）
    "task_result": {
      "audios": [
        {
          "id": "string", // 生成的音频ID；全局唯一，将在30天后被清理
          "url": "string", // 生成音频的URL，如 https://p1.a.kwimgs.com/bs2/upload-ylab-stunt/special-effect/output/HB1_PROD_ai_web_46554461/-2878350957757294165/output.mp3（请注意，为保障信息安全，生成的图片/视频会在30天后被清理，请及时转存）
          "duration": "string" // 音频总时长，单位s（秒）
        }
      ]
    },
    "final_unit_deduction": "string", // 任务最终扣减积分数值
    "final_balance_deduction": { // 额度扣减信息
      "quota": "string", // 额度扣减折扣价
      "list_price": "string" // 额度扣减刊例价
    },
    "created_at": 1722769557708, // 任务创建时间，Unix时间戳、单位ms
    "updated_at": 1722769557708 // 任务更新时间，Unix时间戳、单位ms
  }
}
```
