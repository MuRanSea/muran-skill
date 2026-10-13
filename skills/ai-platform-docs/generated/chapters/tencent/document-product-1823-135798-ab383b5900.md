<!-- Official source: https://cloud.tencent.com/document/product/1823/135798 -->
<!-- Source SHA-256: 088c5aeacd22eba20db6bf7ea955ba6028d92eacea768997b9eae75ce1189ab9 -->

# MiniMax 音色复刻

官方来源：https://cloud.tencent.com/document/product/1823/135798
最近更新时间：2026-08-10 12:39:30

## 概述

Tokenhub 已上线 MiniMax 音色复刻能力，通过语音合成接口下的 `sync_clone` 端点实现，本文基于 MiniMax 官方 voice\_clone 接口编写，**调用参数与原厂基本一致**，详情请参见 [MiniMax API 文档](https://platform.minimaxi.com/docs/api-reference/voice-cloning-clone)。

**功能说明：** 音色复刻（voice clone）指上传一段参考音频，由系统提取并复刻其中的说话人音色特征，生成一个可复用的自定义音色（返回唯一 `voice_id`）。后续在 TTS 语音合成接口传入该 `voice_id`，即可让任意文本以此音色朗读。复刻过程返回的试听音频由 `model` 指定的语音模型合成。

**说明：**

复刻得到的临时音色若 7 天内未正式调用，系统会删除该音色。

调用本接口获得复刻音色时，不会立即收取音色复刻费用。音色的复刻费用将在首次使用此复刻音色进行语音合成时收取。试听字符根据选择的试听模型收费。具体价格请参见 [模型价格](https://cloud.tencent.com/document/product/1823/130055)。

## 前提条件

已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号并开通 TokenHub 服务。

已在 [TokenHub 控制台](https://console.cloud.tencent.com/tokenhub/apikey) 获取 API Key。

## 接口信息

| 项 | 值 |
| --- | --- |
| 地址 | https://tokenhub.tencentmaas.com/v1/wand/minimax-tts/sync\_clone |
| 方法 | POST |
| Content-Type | `application/json` |
| 鉴权 | `Authorization: Bearer YOUR_API_KEY` |

## 请求体

### 请求示例

cURL

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/minimax-tts/sync_clone' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "minimax-voice-clone",
  "audio_url": "https://example.com/clone-source.wav",
  "tts_model":"minimax-speech-2.8-hd",
  "text": "A gentle breeze sweeps across the soft grass(breath), carrying the fresh scent along with the songs of birds.",
  "output_format": "url"
}'
```

### 请求参数

**说明：**

以下为请求参数的简要说明，各参数的完整取值范围、枚举明细等请参见 [MiniMax API 文档](https://platform.minimaxi.com/docs/api-reference/voice-cloning-clone)。

<table><colgroup><col/><col/><col/><col/></colgroup><tbody><tr><td><div>参数</div></td><td><div>类型</div></td><td><div>必选</div></td><td><div>说明</div></td></tr><tr><td><div><code>model</code></div></td><td><div>string</div></td><td><div>是</div></td><td><div>固定填 <code>minimax-voice-clone</code>。</div></td></tr><tr><td><div><code>audio_url</code></div></td><td><div>string</div></td><td><div>否</div></td><td><div>待复刻音频的 URL 地址（http/https 链接）。音频规范：mp3 / m4a / wav，建议时长 10 秒–5 分钟，大小 ≤ 20MB。</div></td></tr><tr><td><div><code>audio_data</code></div></td><td><div>string</div></td><td><div>否</div></td><td><div>待复刻音频的 base64 音频。（<code>audio_url</code> 或 <code>audio_data</code> 至少传一个）</div></td></tr><tr><td><div><code>tts_model</code></div></td><td colspan="1" rowspan="1"><div>string</div></td><td colspan="1" rowspan="1"><div>否</div></td><td><div>试听用的 TTS 语音合成模型，取值为 tokenhub 已上线的 speech 模型（如 <code>minimax-speech-2.8-hd</code>）。</div></td></tr><tr><td><div><code>voice_id</code></div></td><td><div>string</div></td><td><div>否</div></td><td><div>自定义音色 id；不传则自动生成并返回唯一 id。长度 [8, 256]，首字符须为英文字母，允许字母/数字/<code>-</code>/<code>_</code>，末位不可为 <code>-</code>/<code>_</code>。</div></td></tr><tr><td><div><code>text</code></div></td><td><div>string</div></td><td><div>否</div></td><td><div>复刻试听文本，≤ 1000 字符；提供后将以复刻音色朗读并返回试听音频（按 T2A 标准计费）。</div></td></tr><tr><td><div><code>text_validation</code></div></td><td><div>string</div></td><td><div>否</div></td><td><div>音频复刻样本的预期文本，≤ 200 字符；服务做 ASR 识别并比对相似度，低于 <code>accuracy</code> 则拒绝。</div></td></tr><tr><td><div><code>accuracy</code></div></td><td><div>number</div></td><td><div>否</div></td><td><div>ASR 相似度阈值，默认 <code>0.7</code>，范围 <code>[0, 1]</code>。</div></td></tr><tr><td><div><code>output_format</code></div></td><td><div>string</div></td><td><div>否</div></td><td><div>试听音频返回形式，默认 <code>hex</code>，可选 <code>url</code> / <code>hex</code>（url 有效期 24h）。</div></td></tr></tbody></table>

## 返回体

### 返回示例

```json
{
  "voice_id": "MiniMax001-xxxxxxxx",
  "input_sensitive": false,
  "demo_audio": "https://...试听音频链接",
  "extra_info": {
    "audio_length": 11124,
    "audio_sample_rate": 32000,
    "audio_size": 179926,
    "bitrate": 128000,
    "word_count": 18,
    "usage_characters": 18
  },
  "base_resp": {
    "status_code": 0,
    "status_msg": "success"
  },
  "usage":{
    "total_token":1920
  }
}
```

### 返回字段

**说明：**

以下为返回字段的简要说明，各字段的完整含义与边界说明等请参见 [MiniMax API 文档](https://platform.minimaxi.com/docs/api-reference/voice-cloning-clone)。

<table><colgroup><col/><col/><col/></colgroup><tbody><tr><td><div>字段</div></td><td><div>类型</div></td><td><div>说明</div></td></tr><tr><td><div>voice_id</div></td><td><div>string</div></td><td><div>复刻成功返回的音色 id，可用于后续语音合成。</div></td></tr><tr><td><div>input_sensitive</div></td><td><div>boolean</div></td><td><div>输入音频是否命中风控。</div></td></tr><tr><td><div>demo_audio</div></td><td><div>string</div></td><td><div>试听音频链接（形式取决于 output_format）；仅当请求传入 text 时返回，否则为空。</div></td></tr><tr><td><div>extra_info</div></td><td><div>object</div></td><td><div>试听音频的元信息与计费信息，仅当传入 text（触发试听合成）时返回。</div></td></tr><tr><td><div>extra_info.audio_length</div></td><td><div>integer</div></td><td><div>音频时长（毫秒）。</div></td></tr><tr><td><div>extra_info.audio_sample_rate</div></td><td><div>integer</div></td><td><div>音频采样率。</div></td></tr><tr><td><div>extra_info.audio_size</div></td><td><div>integer</div></td><td><div>音频文件大小（字节）。</div></td></tr><tr><td><div>extra_info.bitrate</div></td><td><div>integer</div></td><td><div>音频比特率。</div></td></tr><tr><td><div>extra_info.word_count</div></td><td><div>integer</div></td><td><div>已发音字数。</div></td></tr><tr><td><div>extra_info.usage_characters</div></td><td><div>integer</div></td><td><div>计费字符数。</div></td></tr><tr><td><div>base_resp</div></td><td><div>object</div></td><td><div>本次请求的状态码与详情。</div></td></tr><tr><td><div>base_resp.status_code</div></td><td><div>integer</div></td><td><div>状态码（0 表示正常，详见下方错误码）。</div></td></tr><tr><td><div>base_resp.status_msg</div></td><td><div>string</div></td><td><div>状态详情。</div></td></tr><tr><td><div>usage</div></td><td><div>object</div></td><td><div>用量。</div></td></tr><tr><td colspan="1" rowspan="1"><div>usage.total_token</div></td><td colspan="1" rowspan="1"><div>integer</div></td><td colspan="1" rowspan="1"><div>消耗 token 总量。</div></td></tr></tbody></table>

## 错误码

请参见 [API 错误码说明](https://cloud.tencent.com/document/product/1823/131595)。
