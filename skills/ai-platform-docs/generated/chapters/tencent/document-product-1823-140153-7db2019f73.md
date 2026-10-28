<!-- Official source: https://cloud.tencent.com/document/product/1823/140153 -->
<!-- Source SHA-256: 28ea7348aec61dec34868f3b81f14098f24c59e0a0e4154678b0b15b62422d40 -->

# Tenlai 同步语音合成

官方来源：https://cloud.tencent.com/document/product/1823/140153
最近更新时间：2026-10-27 16:28:08

## 概述

TokenHub 已上线语音合成（TTS）能力，本文对应**天籁语音合成**调用指南。模型为 `tenlai-tts-v1.0`。接口为**同步接口**。

## 前提条件

已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号并开通 TokenHub 服务。

已在 [TokenHub 控制台](https://console.cloud.tencent.com/tokenhub/apikey) 获取 API Key。

## 接口信息

| 项 | 值 |
| --- | --- |
| 地址 | https://tokenhub.tencentmaas.com/v1/tenlai/ttsproxy/text\_to\_voice |
| 方法 | POST |
| Content-Type | `application/json` |
| 鉴权 | `Authorization: Bearer YOUR_API_KEY` |

## 支持模型

<table><colgroup><col/><col/><col/></colgroup><tbody><tr><td><div>模型名称</div></td><td><div>model（调用参数）</div></td><td><div>能力说明</div></td></tr><tr><td colspan="1" rowspan="1"><div>Tenlai-TTS-v1</div></td><td colspan="1" rowspan="1"><div><code>tenlai-tts-v1.0</code></div></td><td><div>天籁语音合成，音质自然流畅，适合内容播报、有声阅读等场景。</div></td></tr></tbody></table>

## 请求体

### 请求示例

非流式

cURL

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/tenlai/ttsproxy/text_to_voice' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "tenlai-tts-v1.0",
  "text": "刚吹过晚风的巷口飘着糖炒栗子的香，连路灯都软乎乎的。",
  "voice_setting": {
    "voice_id": 502001,
    "speed": 1,
    "volume": 0
  },
  "audio_setting": {
    "sample_rate": 16000
  },
  "output_format": "mp3"
}'
```

### 请求参数

| 参数 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| model | string | 是 | 模型名 tenlai-tts-v1.0 |
| text | string | 是 | 合成语音的源文本，按 UTF-8编码统一计算。中文最大支持100个汉字（全角标点符号算一个汉字）；英文最大支持约300个字母。  示例值：你好 |
| voice\_setting.voice\_id | string | 是 | 音色编号，支持系统音色，详情可参考：  云小洋 403008  YunLeo 403007  YunMia 403006  云雅琴 403005  云大川 403004  云小天 403003  云大围 402002  云小团 402001  云晓芙 402000  云小朵 403000  云小帅 403002  云小和 403001  邻家女孩 603007  沉稳青叔 603006  知心大林 603005  温柔小柠 603004  随和老李 603003  软萌心心 603002  潇湘妹妹 603001  懂事少年 603000  专业梓欣 602005  暖心阿灿 602004  智小虎 502007  智小悟 502006  智小解 502005  爱小悠 602003  智小满 502004  智小敏 502003  智小柔 502001 |
| voice\_setting.speed | float | 否 | 语速，默认 1.0，范围 [-2, 6] |
| voice\_setting.volume | float | 否 | 音量，默认 0，范围 [-10，10] |
| audio\_setting.sample\_rate | integer | 否 | 采样率，默认 16000，可选 16000 / 24000 / 8000 |
| output\_format | string | 否 | 返回音频格式，可取值：mp3，pcm  示例值：mp3 |

## 返回体

### 返回示例

非流式

流式

```json
{
    "data": {
        "audio_url": "https://asr-console-cos-1256237915.cos.ap-guangzhou.myqcloud.com/tenlai_maas/tts/1256237915/20261026/8284d9f6-6936-4961-9290-38513497ebb3.mp3?q-sign-algorithm=sha1&q-ak=<TENCENT_CLOUD_SECRET_ID>&q-sign-time=1793026168%3B1793630968&q-key-time=1793026168%3B1793630968&q-header-list=host&q-url-param-list=&q-signature=4396cea265e30a4f1f7369b66fdb264153f33acd"
    },
    "status": "completed",
    "trace_id": "8284d9f6-6936-4961-9290-38513497ebb3"
}
```

```java

data: {"base_resp":{"status_code":0,"status_msg":"success"},"data":{"audio":"<hex编码的audio0>","status":1},"request_id":"2d4e75ca-229e-4c77-9853-629f3b142786","trace_id":"th_251414125_r00c00_minimax-tts_96633db4153604d295fe0a565d0bea40"}

data: {"base_resp":{"status_code":0,"status_msg":"success"},"data":{"audio":"<hex编码的audio1>","status":1},"request_id":"2d4e75ca-229e-4c77-9853-629f3b142786","trace_id":"th_251414125_r00c00_minimax-tts_96633db4153604d295fe0a565d0bea40"}

data: {"base_resp":{"status_code":0,"status_msg":"success"},"data":{"audio":"<hex编码的audio2>","status":1},"request_id":"2d4e75ca-229e-4c77-9853-629f3b142786","trace_id":"th_251414125_r00c00_minimax-tts_96633db4153604d295fe0a565d0bea40"}

data: {"base_resp":{"status_code":0,"status_msg":"success"},"data":{"audio":"<hex编码的audio3>","status":1},"request_id":"2d4e75ca-229e-4c77-9853-629f3b142786","trace_id":"th_251414125_r00c00_minimax-tts_96633db4153604d295fe0a565d0bea40"}

data: {"base_resp":{"status_code":0,"status_msg":"success"},"data":{"audio":"<hex编码的audio4>","status":1},"request_id":"2d4e75ca-229e-4c77-9853-629f3b142786","trace_id":"th_251414125_r00c00_minimax-tts_96633db4153604d295fe0a565d0bea40"}

data: {"base_resp":{"status_code":0,"status_msg":"success"},"data":{"audio":"<hex编码的audio5>","status":1},"request_id":"2d4e75ca-229e-4c77-9853-629f3b142786","trace_id":"th_251414125_r00c00_minimax-tts_96633db4153604d295fe0a565d0bea40"}

data: {"base_resp":{"status_code":0,"status_msg":"success"},"data":{"status":2},"request_id":"2d4e75ca-229e-4c77-9853-629f3b142786","status":"completed","trace_id":"th_251414125_r00c00_minimax-tts_96633db4153604d295fe0a565d0bea40","usage":{"chars":50,"total_tokens":1750,"use_count":26}}

data: [DONE]
```

### 返回字段

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| data.audio\_url | string | Base64编码的 mp3/pcm 音频数据  示例值：UklGRlR/AABXQVZFZm10IBAAAAABAAEAgD4AAAB9AAACABAAZGF0YSx9AAD+ |
| status | integer | { "0": "queued", "1": "in\_progress", "2": "completed", "3": "failed" } |
| trace\_id | string | 本次会话 ID，用于咨询/反馈时定位问题。 |

## 错误码

请参见 [API 错误码说明](https://cloud.tencent.com/document/product/1823/131595)。
