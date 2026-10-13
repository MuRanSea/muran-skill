<!-- Official source: https://cloud.tencent.com/document/product/1823/135797 -->
<!-- Source SHA-256: aa401742e53a6de4d98fc8f731f1a7287e960b6c1ac8bc987264d4c6ff59b47b -->

# MiniMax 音色设计

官方来源：https://cloud.tencent.com/document/product/1823/135797
最近更新时间：2026-08-10 12:39:30

## 概述

Tokenhub 已上线 MiniMax 音色设计（文生音色）能力，通过语音合成接口下的 `sync_design` 端点实现，本文基于 MiniMax 官方 `voice_design` 接口编写，**调用参数与原厂基本一致**，详情请参见 [MiniMax API 文档](https://platform.minimaxi.com/docs/api-reference/voice-design-design)。

**功能说明：**音色设计（voice design / 文生音色）指用自然语言描述您期望的音色（如性别、年龄、音色特征、情绪、场景等），由系统据此生成一个全新的虚拟音色（返回唯一 `voice_id`），无需任何参考音频。后续在 TTS 语音合成接口传入该 `voice_id`，即可让任意文本以此音色朗读。适用于从零创造角色声音、虚拟主播、特定风格配音等场景。试听音频由平台默认 TTS 引擎合成。

**说明：**

设计得到的临时音色若 7 天内未正式调用，系统会删除该音色。

调用本接口获得设计音色时，不会立即收取音色设计费用。音色的设计费用将在首次使用此音色进行语音合成时收取。试听按字符计费。具体价格请参见 [模型价格](https://cloud.tencent.com/document/product/1823/130055)。

## 前提条件

已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号并开通 TokenHub 服务。

已在 [TokenHub 控制台](https://console.cloud.tencent.com/tokenhub/apikey) 获取 API Key。

## 接口信息

| 项 | 值 |
| --- | --- |
| 地址 | https://tokenhub.tencentmaas.com/v1/wand/minimax-tts/sync\_design |
| 方法 | POST |
| Content-Type | `application/json` |
| 鉴权 | `Authorization: Bearer YOUR_API_KEY` |

## 请求体

### 请求示例

cURL

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/minimax-tts/sync_design' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "minimax-voice-design",
  "prompt": "讲述悬疑故事的播音员，声音低沉富有磁性，语速时快时慢，营造紧张神秘的氛围。",
  "preview_text": "夜深了，古屋里只有他一人。窗外传来若有若无的脚步声，他屏住呼吸，慢慢地，慢慢地，走向那扇吱呀作响的门……"
}'

```

### 请求参数

**说明：**

以下为请求参数的简要说明，各参数的完整取值范围、枚举明细等请参见 [MiniMax API 文档](https://platform.minimaxi.com/docs/api-reference/voice-design-design)。

<table><colgroup><col/><col/><col/><col/></colgroup><tbody><tr><td><div>参数</div></td><td><div>类型</div></td><td><div>必选</div></td><td><div>说明</div></td></tr><tr><td><div>model</div></td><td colspan="1" rowspan="1"><div>string</div></td><td colspan="1" rowspan="1"><div>是</div></td><td colspan="1" rowspan="1"><div>固定传 minimax-voice-design。</div></td></tr><tr><td><div>prompt</div></td><td><div>string</div></td><td><div>是</div></td><td><div>音色描述（自然语言），描述性别、年龄、音色特征、情绪、场景等。</div></td></tr><tr><td><div>preview_text</div></td><td><div>string</div></td><td><div>是</div></td><td><div>试听音频文本，≤ 500 字符（试听由平台默认 TTS 引擎合成，按 T2A 标准计费）。</div></td></tr><tr><td><div>voice_id</div></td><td><div>string</div></td><td><div>否</div></td><td><div>自定义生成音色的 id；不传则自动生成并返回唯一 id。</div></td></tr><tr><td><div>output_format</div></td><td><div>string</div></td><td><div>否</div></td><td><div>试听音频返回形式，默认 hex，可选 url / hex（url 有效期 24h）。</div></td></tr><tr><td><div>aigc_watermark</div></td><td><div>boolean</div></td><td><div>否</div></td><td><div>末尾添加音频节奏标识，默认 <code>false</code>。</div></td></tr></tbody></table>

## 返回体

### 返回示例

```json
{
  "voice_id": "ttv-voice-2025060717322425-xxxxxxxx",
  "trial_audio": "<hex 编码音频或音频 URL，取决于 output_format>",
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

以下为返回字段的简要说明，各字段的完整含义与边界说明等请参见 [MiniMax API 文档](https://platform.minimaxi.com/docs/api-reference/voice-design-design)。

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `voice_id` | string | 生成的音色 id，可用于后续语音合成。 |
| `trial_audio` | string | 使用生成音色合成的试听音频（hex 编码或 URL，取决于 `output_format`）。 |
| `base_resp` | object | 本次请求的状态码与详情。 |
| `base_resp.status_code` | integer | 状态码（`0` 表示正常，详见下方错误码）。 |
| `base_resp.status_msg` | string | 状态详情。 |
| `usage` | object | 用量。 |
| `usage.total_token` | integer | 消耗 token 数。 |

## 错误码

请参见 [API 错误码说明](https://cloud.tencent.com/document/product/1823/131595)。
