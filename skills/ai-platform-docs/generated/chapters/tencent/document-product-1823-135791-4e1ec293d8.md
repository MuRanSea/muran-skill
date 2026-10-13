<!-- Official source: https://cloud.tencent.com/document/product/1823/135791 -->
<!-- Source SHA-256: 41eefd19a2720a5858e5285512c4b3469467d0ddfd68ccc09e0c234ac07f21ef -->

# Hy 同步语音识别

官方来源：https://cloud.tencent.com/document/product/1823/135791
最近更新时间：2026-09-29 17:39:17

## 概述

Tokenhub 已上线语音识别（ASR）能力，本文对应**混元非实时语音识别**的**同步**接口。接口接收音视频文件地址，同步返回识别文本结果。

## 前提条件

已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号并开通 TokenHub 服务。

已在 [TokenHub 控制台](https://console.cloud.tencent.com/tokenhub/apikey) 获取 API Key。

## 接口信息

| 项 | 值 |
| --- | --- |
| 地址 | https://tokenhub.tencentmaas.com/v1/wand/asrproxy/sync\_transcribe |
| 方法 | POST |
| Content-Type | application/json |
| 鉴权 | Authorization: Bearer YOUR\_API\_KEY |

## 支持模型

| 模型名称 | model（调用参数） | 能力说明 |
| --- | --- | --- |
| Hy-ASR-3.0-Preview | `hy-asr-3.0-preview` | 中文普通话+英语＋多方言混合引擎，除中英外，支持多种方言，包括粤语、东北话、河南话、陕西话、成都话、重庆话、武汉话、贵阳话、青岛话、济南话、长沙话、合肥话等。 |

## 请求体

### 请求示例

cURL

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/asrproxy/sync_transcribe' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H "Content-Type: application/json" \\
  -d '{
    "model": "hy-asr-3.0-preview",
    "input_url": "https://cos.example.com/xxx.mp4"
  }'
```

### 请求参数

| 参数 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| model | string | 是 | 模型名称，固定为 `hy-asr-3.0-preview`。 |
| input\_url | string | 二选一 | 待识别的音视频文件地址（支持常见音视频格式）。最大支持30分钟音频/视频；文件大小 <= 100MB；需要公网可访问（http/https）。 |
| data | string | 二选一 | Base64 格式，最大支持音频/视频时长 <= 30分钟；文件大小 <= 75MB， 转为 Base64 大小 <= 100MB；格式要求：视频：<base64编码数据>； 音频：<base64编码数据>；与 input\_url 同时传则以 data 为准。 |
| source | string | 否 | 识别语种：zh / en 等；缺省时后端自动检测。 |
| voice\_encode\_format | string | 否 | 音频编码：pcm / wav / ogg / mp3等；缺省 auto。 |

## 返回体

### 返回示例

```json
{
  "id": "th_251416641_700001910665_asrproxy_2dc6dad8df55a082a5a17b01f2426a20",
  "object": "asr.task",
  "created_at": 1721808000,
  "status": "completed",
  "request_id": "fd8a1c2f-feb6-48ff-b904-e14056693b9c",
  "output": {
    "source": "zh",
    "duration_ms": 15230,
    "text": "大家好，欢迎来到今天的会议 今天我们讨论产品规划",
    "sentences": [
      { "begin_ms": 500,  "end_ms": 3200, "text": "大家好，欢迎来到今天的会议" },
      { "begin_ms": 3500, "end_ms": 5800, "text": "今天我们讨论产品规划" }
    ],
    "subtitle_url": "https://xxx.cos.ap-guangzhou.myqcloud.com/subtitle/xxx.srt"
  },
  "usage": { "total_token": 761 }
}
```

### 返回字段

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| output.source | string | 实际识别的语种。 |
| output.duration\_ms | int64 | 音频总时长（毫秒）。 |
| output.text | string | 全文识别文本（自动拼接所有分句）。 |
| output.sentences[] | array | 分句时间戳：{ begin\_ms, end\_ms, text }。 |
| output.subtitle\_url | string | 字幕文件下载 URL（SRT 格式）。 |
| usage.total\_token | int64 | 消耗 token 总数。 |

## 错误码

请参见 [API 错误码说明](https://cloud.tencent.com/document/product/1823/131595)。
