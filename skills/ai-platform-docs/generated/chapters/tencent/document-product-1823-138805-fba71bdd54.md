<!-- Official source: https://cloud.tencent.com/document/product/1823/138805 -->
<!-- Source SHA-256: 6ce5c10c2c5d7415a54ba416d2c5b4bd3d6a555b1b9322252a8747f664b07242 -->

# Mureka 音乐生成

官方来源：https://cloud.tencent.com/document/product/1823/138805
最近更新时间：2026-10-23 18:08:00

## 概述

Mureka 是昆仑万维推出的 AI 音乐生成模型，支持根据歌词、提示词或风格生成完整歌曲与纯音乐。本文介绍如何通过 TokenHub 调用 Mureka 音乐生成模型 Mureka-Music-v9（`mureka-music-v9`），提供三种生成能力：**歌词生成歌曲、提示词生成歌曲、生成纯音乐**。

### 调用方式

音乐生成为**同步调用**：一次请求直接返回生成结果，无需创建任务和轮询。

### 前提条件

已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号并开通 TokenHub 服务。

已在 [TokenHub 控制台](https://console.cloud.tencent.com/tokenhub/apikey) 获取 API Key。

在 [控制台-在线推理-语音模型](https://console.cloud.tencent.com/tokenhub/inference?serviceType=SPEECH) 处开启对应模型的后付费。

**说明：**

下文所有示例中的 YOUR\_API\_KEY 均需替换为您自己的 API Key，鉴权方式为请求头 Authorization: Bearer YOUR\_API\_KEY。

### 模型列表

| 模型名称 | model 参数值 | 支持能力 | 歌词上限 | 提示词上限 |
| --- | --- | --- | --- | --- |
| Mureka-Music-v9 | `mureka-music-v9` | 歌词生成歌曲 / 提示词生成歌曲 / 生成纯音乐 | 5000 字符 | 提示词生成歌曲 2000 字符；歌词生成歌曲的风格提示词、纯音乐提示词 1024 字符 |

**注意：**

三种能力的 `n` 参数默认值均为 2，且**按生成数量计费**，仅需 1 首时请显式传 `"n": 1`。

## 歌词生成歌曲

### 1. 接口描述

根据用户输入的歌词生成歌曲。传入完整歌词，可搭配风格提示词与人声性别倾向，模型据此完成作曲与演唱。

**接口：** `POST https://tokenhub.tencentmaas.com/v1/wand/mureka-music/generation`

### 2. 输入参数

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| model | 是 | string | 模型 ID。取值：`mureka-music-v9` |
| lyrics | 是 | string | 歌词内容，长度 ≤ 5000 字符。  支持使用分段标签组织歌曲结构：`[Intro]`、`[Verse]`、`[Pre-Chorus]`、`[Chorus]`、`[Bridge]`、`[Outro]`。 |
| prompt | 否 | string | 风格提示词，控制曲风、情绪、人声等（如 `r&b, slow, passionate, male vocal`），长度 ≤ 1024 字符。 |
| gender | 否 | string | 人声性别倾向。可选值：female、male。 |
| n | 否 | integer | 每次请求生成的歌曲数量，取值范围 [1, 3]，默认 2。 |

### 3. 请求示例

```bash
# 歌词生成歌曲
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/mureka-music/generation' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "mureka-music-v9",
  "lyrics": "[Verse]\\nWalking through the city lights at midnight\\n[Chorus]\\nHold on to the memories",
  "prompt": "pop, emotional, female vocal, slow tempo",
  "gender": "female",
  "n": 1
}'
```

### 4. 输出参数

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 任务 ID。 |
| created\_at | integer | 任务创建时间，Unix 时间戳，单位 s。 |
| finished\_at | integer | 任务完成时间，Unix 时间戳，单位 s。 |
| model | string | 用于音乐生成的模型。 |
| status | string | 任务状态，枚举值：preparing（准备中）、queued（排队中）、running（生成中）、streaming（流式生成中）、reviewing（审核中）、succeeded（成功）、failed（失败）、timeouted（超时）、cancelled（已取消）。 |
| failed\_reason | string | 任务失败原因，`status` 为 failed 时返回。 |
| watermarked | boolean | 是否在音乐尾部添加 5 秒水印音频，true 表示已添加。 |
| choices | array[object] | 生成结果列表，仅 `status` 为 succeeded 时返回；元素数量与请求的 `n` 一致。 |
| choices[].url | string | 生成音频的下载地址，为临时地址，请及时下载转存。 |
| tokenhub\_usage.total\_tokens | integer | 本次任务消耗的 token 数，用于计费/对账。 |
| request\_id | string | 唯一请求标识，用于排查问题。 |

### 5. 响应示例

```json

{
    "id": "1256342408-WandAudio-c6313c32b0b74c648f401571c515be00",
    "created_at": 1790166087,
    "finished_at": 1790166137,
    "model": "mureka-9",
    "status": "succeeded",
    "choices": [
        {
            "url": "https://xxxx.mp3",
            "flac_url": "https://xxxx.mp3",
            "duration": 162630,
            "lyrics_sections": [
                {
                    "section_type": "verse",
                    "start": 12120,
                    "end": 20240,
                    "lines": [
                        {
                            "start": 12120,
                            "end": 20240,
                            "text": "Walking through the city lights at midnight",
                            "words": [
                                {
                                    "start": 12120,
                                    "end": 12200,
                                    "text": "Walking "
                                },
                                {
                                    "start": 13160,
                                    "end": 13200,
                                    "text": "through "
                                },
                                {
                                    "start": 13800,
                                    "end": 13840,
                                    "text": "the "
                                },
                                {
                                    "start": 14120,
                                    "end": 14160,
                                    "text": "city "
                                },
                                {
                                    "start": 14560,
                                    "end": 15560,
                                    "text": "lights "
                                },
                                {
                                    "start": 18640,
                                    "end": 18680,
                                    "text": "at "
                                },
                                {
                                    "start": 19040,
                                    "end": 20240,
                                    "text": "midnight"
                                }
                            ]
                        }
                    ]
                },
                {
                    "section_type": "chorus",
                    "start": 38280,
                    "end": 76800,
                    "lines": [
                        {
                            "start": 38280,
                            "end": 76800,
                            "text": "Hold on to the memories",
                            "words": [
                                {
                                    "start": 38280,
                                    "end": 40520,
                                    "text": "Hold "
                                },
                                {
                                    "start": 40920,
                                    "end": 40960,
                                    "text": "on "
                                },
                                {
                                    "start": 55920,
                                    "end": 55960,
                                    "text": "to "
                                },
                                {
                                    "start": 71800,
                                    "end": 71840,
                                    "text": "the "
                                },
                                {
                                    "start": 74320,
                                    "end": 76800,
                                    "text": "memories"
                                }
                            ]
                        }
                    ]
                }
            ],
            "id": "162503562821633",
            "wav_url": "https://xxxx.mp3"
        }
    ],
    "trace_id": "4c0611edea3fc3493c82c3db7e71cb50",
    "watermarked": true,
    "tokenhub_usage": {
        "total_tokens": 33000
    },
    "request_id": "1019e5dc-a80b-43b7-9122-6a325d01ca97"
}
```

## 提示词生成歌曲

### 1. 接口描述

根据用户输入的提示词生成歌曲，可搭配风格枚举，无需自己写歌词，模型自动完成作词、作曲与演唱。

**接口：** `POST https://tokenhub.tencentmaas.com/v1/wand/mureka-music/easy-generation`

### 2. 输入参数

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| model | 是 | string | 模型 ID。取值：`mureka-music-v9` |
| prompt | 是 | string | 提示词，描述想要的歌曲内容、情绪与画面感，长度 ≤ 2000 字符。 |
| styles | 否 | array[string] | 风格列表，从枚举值中选择一个或多个风格：  pop、rock、jazz、r&b、edm、ambient、folk、latin、k-pop、j-pop、house、gospel、lo-fi。 |
| n | 否 | integer | 每次请求生成的歌曲数量，取值范围 [1, 3]，默认 2。 |

### 3. 请求示例

```bash
# 提示词生成歌曲
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/mureka-music/easy-generation' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "mureka-music-v9",
  "prompt": "一首明亮夏日氛围、带有抓耳副歌的情歌",
  "styles": ["pop", "rock"],
  "n": 1
}'
```

提交任务的输出参数与响应示例同 歌词生成歌曲。

## 生成纯音乐

### 1. 接口描述

根据用户输入的提示词生成无人声的纯音乐，适用于背景音乐、伴奏等场景。

**接口：** `POST https://tokenhub.tencentmaas.com/v1/wand/mureka-music/instrumental-generation`

### 2. 输入参数

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| model | 是 | string | 模型 ID。取值：`mureka-music-v9` |
| prompt | 是 | string | 提示词，描述想要的纯音乐风格与场景，长度 ≤ 1024 字符。 |
| n | 否 | integer | 每次请求生成的纯音乐数量，取值范围 [1, 3]，默认 2。 |

### 3. 请求示例

```bash
# 生成纯音乐
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/mureka-music/instrumental-generation' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "mureka-music-v9",
  "prompt": "lo-fi, cozy, warm piano and soft drums, late night study vibe",
  "n": 1
}'
```

## 附录

### 错误码说明

| 错误码 | 概述 |
| --- | --- |
| 400 - Invalid Request | 原因：请求参数不正确。  解决方案：请参考文档以输入正确的请求参数。 |
| 401 - Invalid Authentication | 原因：认证无效。  解决方案：请确保使用正确的 API 密钥。 |
| 403 - Forbidden | 原因：您正在从不支持的地区访问 API。  解决方案：请确保您的访问来自支持的地区。 |
| 429 - Rate limit reached for requests | 原因：您发送请求的速度过快。  解决方案：请控制请求速度，查看价格方案中的并发请求限制。 |
| 429 - You exceeded your current quota, please check your billing details | 原因：您的充值已用完。  解决方案：请充值。 |
| 451 - Unavailable For Legal Reasons | 原因：请求参数没有通过安审。  解决方案：请修改请求参数。 |
| 500 - The server had an error while processing your request | 原因：我们的服务出现了问题。  解决方案：稍后重试您的请求，如果问题仍然存在，请联系我们。 |
| 503 - The engine is currently overloaded, please try again later | 原因：我们的服务负载过高。  解决方案：请稍后重试您的请求。 |

## 常见问题

#### **1. 三种生成能力怎么区分？**

三者请求 model 相同，但接口 path 不同，歌词生歌曲使用 /v1/wand/mureka-music/generation，提示词生歌曲使用 /v1/wand/mureka-music/easy-generation，生成纯音乐使用 /v1/wand/mureka-music/instrumental-generation。注意三者的提示词上限不同：提示词生成歌曲为 2000 字符，歌词生成歌曲的风格提示词与纯音乐提示词均为 1024 字符。

#### **2. 为什么默认生成了 2 首？**

`n` 参数默认为 2，且按生成数量计费。只需 1 首时，请在请求中显式传入 `"n": 1`；最多可传 3。

#### **3. 歌词怎么写效果更好？**

建议用分段标签组织歌词结构：`[Intro]`（前奏）、`[Verse]`（主歌）、`[Pre-Chorus]`（预副歌）、`[Chorus]`（副歌）、`[Bridge]`（桥段）、`[Outro]`（尾奏）。同时可用 `prompt` 补充曲风、情绪与人声描述（如 `r&b, slow, passionate, male vocal`），用 `gender` 指定人声性别倾向。

#### **4. styles 和 prompt 有什么区别？**

`styles` 是固定风格枚举（pop、rock、jazz 等 13 种），用于框定曲风大类，仅提示词生成歌曲支持；`prompt` 是自由文本，用于描述歌曲主题、情绪与画面感。两者可同时传入，由模型综合生效。

#### **5. 生成结果有水印吗？**

默认在音乐尾部添加 5 秒水印音频，查询结果中 `watermarked` 为 true 表示已添加。

#### **6. 生成结果音频链接会过期吗？**

会过期。`choices[].url` 为临时地址，存储 12 h，请在任务成功后及时下载转存，不要长期引用该链接。
