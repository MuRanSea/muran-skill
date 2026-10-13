<!-- Official source: https://cloud.tencent.com/document/product/1823/135323 -->
<!-- Source SHA-256: d5977fdf0becde9161960ece6b9c74425f5e7f0dbc9e77920d789f02e82a08ee -->

# MiniMax 音乐生成

官方来源：https://cloud.tencent.com/document/product/1823/135323
最近更新时间：2026-09-24 21:20:31

## 概述

MiniMax 音乐生成模型支持通过文本描述（风格、情绪、场景）生成完整歌曲或纯音乐，支持自定义歌词（含结构标签）、自动写词、多音质参数配置。本文介绍如何通过 TokenHub 调用 MiniMax 音乐模型：`minimax-music-v3.0`、`minimax-music-v2.6`。

### **调用方式**

音乐生成为**同步调用**：一次请求直接返回生成结果，无需创建任务和轮询。音频支持两种返回形式：

**hex**：十六进制编码的音频数据（默认），需客户端自行解码写文件。

**url**：音频文件下载链接，**有效期 12 小时**，请及时下载。

### 前提条件

已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号并开通 TokenHub 服务。

已在 [TokenHub 控制台](https://console.cloud.tencent.com/tokenhub/apikey) 获取 API Key。

在 [控制台-在线推理-语音模型](https://console.cloud.tencent.com/tokenhub/inference?serviceType=SPEECH) 处开启对应模型的后付费。

**说明：**

下文所有示例中的 `YOUR_API_KEY` 均需替换为您自己的 API Key，鉴权方式为请求头 `Authorization: Bearer YOUR_API_KEY`。

### 模型列表

<table><colgroup><col/><col/><col/><col/><col/><col/></colgroup><tbody><tr><td><div>模型名称</div></td><td><div>model ID</div></td><td><div>支持能力</div></td><td><div>歌词上限</div></td><td><div>提示词上限</div></td><td><div>选型建议</div></td></tr><tr><td><div>MiniMax-Music-v3.0</div></td><td><div>minimax-music-v3.0</div></td><td><div>歌曲生成（人声）/ 纯音乐 / 自动写词</div></td><td><div>3500 字符</div></td><td><div>2000 字符</div></td><td><div>音质全面跃升，人声合成更自然</div></td></tr><tr><td colspan="1" rowspan="1"><div>MiniMax-Music-v2.6</div></td><td colspan="1" rowspan="1"><div>minimax-music-v2.6</div></td><td colspan="1" rowspan="1"><div>歌曲生成（人声）/ 纯音乐 / 自动写词</div></td><td colspan="1" rowspan="1"><div>3500 字符</div></td><td colspan="1" rowspan="1"><div>2000 字符</div></td><td colspan="1" rowspan="1"><div>高质量音乐生成模型</div></td></tr></tbody></table>

## 音乐生成

### 1. 接口描述

输入歌曲描述与歌词，生成完整音乐。支持三种创作模式：**自定义歌词**、**自动写词**（按 prompt 自动生成歌词）、**纯音乐**（无人声）。

**接口：**`POST https://tokenhub.tencentmaas.com/v1/wand/minimax-music/generation`

### 2. 输入参数

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| model | 是 | string | 模型版本。取值：`minimax-music-v3.0`、`minimax-music-v2.6` |
| prompt | 条件必选 | string | 音乐描述，用于指定风格、情绪和场景，如 “Pop, melancholic, perfect for a rainy night”。长度限制 [0, 2000] 字符；**生成纯音乐（**`is_instrumental: true`**）时必填**，长度限制 [1, 2000] 字符。 |
| lyrics | 条件必选 | string | 歌曲歌词，使用 `\\n` 分隔每行。支持结构标签：`[Intro]`、`[Verse]`、`[Pre Chorus]`、`[Chorus]`、`[Interlude]`、`[Bridge]`、`[Outro]`、`[Post Chorus]`、`[Transition]`、`[Break]`、`[Hook]`、`[Build Up]`、`[Inst]`、`[Solo]`。**生成带人声歌曲时必填**，长度限制 [1, 3500] 字符；纯音乐时非必填。 |
| lyrics\_optimizer | 否 | boolean | 是否根据 `prompt` 描述自动生成歌词。设为 `true` 且 `lyrics` 为空时，系统按 prompt 自动写词。默认值：false。 |
| is\_instrumental | 否 | boolean | 是否生成纯音乐（无人声）。设为 `true` 时 `lyrics` 非必填。默认值：false。 |
| output\_format | 否 | string | 音频返回格式。可选值：`hex`（十六进制编码，默认）/ `url`（下载链接，**有效期 12小时**）。 |
| audio\_setting | 否 | object | 音频输出配置，子字段见下表。 |
| aigc\_watermark | 否 | boolean | 是否在音频末尾添加水印。默认值：false。 |

**audio\_setting 对象子字段：**

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| sample\_rate | 否 | integer | 采样率（Hz），如 44100 |
| bitrate | 否 | integer | 码率（bps），如 256000 |
| format | 否 | string | 音频格式，如 `mp3` |

**注意：**

**三种创作模式的参数组合如下：**

**自定义歌词**：传 `lyrics`（必填）+ `prompt`（可选）。

**自动写词**：`lyrics_optimizer: true`，`lyrics` 留空，`prompt` 描述歌曲主题。

**纯音乐**：`is_instrumental: true` + `prompt`（必填），无需 `lyrics`。

### 3. 请求示例

**模式一：自动写词（按 prompt 生成歌词与人声歌曲）**

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/minimax-music/generation' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "minimax-music-v2.6",
  "prompt": "Pop, melancholic, perfect for a rainy night",
  "lyrics_optimizer": true,
  "output_format":"url"
}'
```

**模式二：自定义歌词**

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/minimax-music/generation' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "minimax-music-v2.6",
  "prompt": "独立民谣, 忧郁, 内省, 咖啡馆",
  "lyrics": "[verse]\\n街灯微亮晚风轻抚\\n影子拉长独自漫步\\n旧外套裹着深深忧郁\\n不知去向渴望何处\\n[chorus]\\n推开木门香气弥漫\\n熟悉的角落陌生人看",
  "output_format": "url",
  "audio_setting": {
    "sample_rate": 44100,
    "bitrate": 256000,
    "format": "mp3"
  }
}'
```

**模式三：纯音乐（无人声）**

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/minimax-music/generation' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "minimax-music-v2.6",
  "prompt": "舒缓的钢琴曲, 适合专注学习, 平静放松",
  "is_instrumental": true
}'
```

### 4. 输出参数

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| data | object | 生成结果数据对象。 |
| data.audio | string | 音频内容。`output_format=hex` 时为十六进制编码音频数据；`output_format=url` 时为音频下载链接（有效期 12 小时）。 |
| data.status | integer | 生成状态：1 生成中 / 2 已完成。 |
| trace\_id | string | 请求的任务的 ID，用于问题排查。 |
| extra\_info | object | 音频信息对象。 |
| extra\_info.music\_duration | integer | 音频时长（毫秒）。 |
| extra\_info.music\_sample\_rate | integer | 采样率（Hz）。 |
| extra\_info.music\_channel | integer | 声道数。 |
| extra\_info.bitrate | integer | 码率（bps）。 |
| extra\_info.music\_size | integer | 音频文件大小（字节）。 |
| base\_resp | object | 状态码对象。 |
| base\_resp.status\_code | integer | 状态码；0 表示成功。 |
| base\_resp.status\_msg | string | 状态描述信息。 |
| usage | object | 用量消耗。 |
| usage.total\_tokens | integer | 本次任务消耗的 token 数。 |
| request\_id | string | 请求的唯一标识，用于问题排查。 |

### 5. 响应示例

```json
{
	"data": {
		"audio": "hex编码的音频数据或URL",
		"status": 2
	},
	"trace_id": "4-WandAudio-37d8fc5946e6419380fa5627fe6ae5ff",
	"extra_info": {
		"music_duration": 25364,
		"music_sample_rate": 44100,
		"music_channel": 2,
		"bitrate": 256000,
		"music_size": 813651
	},
	"base_resp": {
		"status_code": 0,
		"status_msg": "success"
	},
	"usage": {
		"total_tokens": 100000
	},
	"request_id": "3aec3299-06ad-4654-8b45-c57b823a15d2"
}
```

**说明：**

`output_format=hex`（默认）时，`data.audio` 为十六进制编码字符串，需将其按 hex 解码后写入音频文件（如 output.mp3）即可播放；`output_format=url` 时，`data.audio` 直接返回下载链接。

### 6. 错误码

请求失败时 HTTP 状态码不为 200，或响应体中 `base_resp.status_code` 不为 0，具体原因见 `base_resp.status_msg`。常见失败场景：

| 失败场景 | 处理建议 |
| --- | --- |
| 鉴权失败 | 检查 API Key 是否正确、是否已开通 TokenHub 服务。 |
| 缺少必填参数 | 检查参数组合：带人声歌曲必须传 `lyrics`（或开启 `lyrics_optimizer`）；纯音乐必须传 `prompt`。 |
| 内容审核未通过 | 检查 prompt / lyrics 是否含违规内容，修改后重试。 |
| 触发限流 | 降低请求频率后重试。 |
| 服务端生成失败 | 请重试；持续失败请联系技术支持并附 `trace_id`。 |

## 常见问题

#### **1. 只传 prompt、不传 lyrics 能生成歌曲吗？**

可以，但必须设置 `lyrics_optimizer: true`，系统会根据 prompt 自动生成歌词。如果 `lyrics_optimizer` 为 false 且未传 `lyrics`，生成带人声歌曲的请求会失败——纯音乐场景除外（`is_instrumental: true` 时无需歌词）。

#### **2. hex 和 url 两种返回格式怎么选？**

想直接拿到可下载/可播放的链接：用 `url`，注意链接 12 **小时后过期**，请及时下载转存。

#### **3. 歌词里的 [Verse]、[Chorus] 这些标签是必须的吗？**

不是必须的，但建议使用。结构标签（`[Intro]`、`[Verse]`、`[Chorus]` 等）能显著提升歌曲的结构完整度和听感，标签不计入歌词正文字符。

#### **4. 生成失败排查时需要提供什么信息？**

请提供响应中的 `trace_id`，它是请求的任务 id，可用于定位生成链路中的具体问题。
