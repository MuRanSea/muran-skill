<!-- Official source: https://platform.minimax.cn/docs/guides/speech-to-text.md -->
<!-- Source SHA-256: 3f4a2a584873e608e396c8985c9d4e1691522b8d1dba134f1ebf1d8406c1f287 -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.minimaxi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 语音识别

> MiniMax ASR 将音频转写为文本，支持流式返回、说话人分离与字幕导出，可直接用于会议纪要、播客/视频转写、内容审核、通话质检等场景。

若需要使用语音识别能力，请点击 [按量购买 API](/docs/guides/pricing-paygo#语音)，或 [订阅 Token Plan](/docs/guides/pricing-token-plan)。

## 模型介绍

MiniMax 语音识别（ASR）把音频转写成文本，当前对外提供的模型为 `asr-1.0`：

* **多语种混合识别**：不指定语种自动识别音频主要语言与中英混合表达，也可通过 `language` 请求头显式指定。
* **一次性 / 流式返回**：默认一次性返回；开启 `stream=true` 后以 SSE 逐段推送 `delta`，适合直播字幕、语音助手等对首字延迟敏感的场景。
* **说话人分离**：`response_format=verbose_json` 时返回 `n_speakers` 与逐句 `speaker` 标签，输出"谁在什么时间说了什么"。
* **精确时间戳与字幕导出**：`verbose_json` 输出逐句起止时间；也可直接以 `srt` / `vtt` 字幕格式返回。
* **稳定性**：模型侧针对幻觉做了专项优化，重噪、口语、专业术语等真实场景下的可用性大大提升。

## 核心能力

| 能力          | 启用方式                           | 典型用途               |
| :---------- | :----------------------------- | :----------------- |
| 纯语音识别       | `response_format=json`（默认）     | 只关心文本内容            |
| 流式识别        | `stream=true`，仅支持 `json`       | 直播字幕、边说边转、低延迟语音交互  |
| 说话人分离 + 时间戳 | `response_format=verbose_json` | 会议纪要、访谈整理、多人通话质检   |
| 字幕导出        | `response_format=srt` 或 `vtt`  | 直接投喂剪辑工具           |
| 多语种混合识别     | 不传 `language`；或按需指定            | 跨语种会议、双语播客、海外内容本地化 |

<Note>
  `verbose_json` / `srt` / `vtt` 会启用说话人分离与时间戳对齐，**不能与 `stream=true` 同时使用**。
</Note>

## 基础规格

### 音频文件

| 项    | 约束                                                                     |
| :--- | :--------------------------------------------------------------------- |
| 支持格式 | `wav` / `aiff` / `flac` / `alac`(m4a) / `mp3` / `aac` / `opus` / `ogg` |
| 单次时长 | 不超过 **500 秒**；超出返回 `400`，不会被截断                                         |
| 单次大小 | 不超过 **50 MB**；超出返回 `413`                                               |
| 不支持  | 无容器的裸 PCM；音频流式输入（可自行用 VAD 切段实现伪流式）                                     |

<Note>
  ASR 不依赖高采样率与立体声。未压缩高规格音频容易超上限（500 秒 48 kHz 立体声 WAV ≈ 92 MB），建议先转为**单声道 16 kHz**，或使用 `mp3` / `aac` / `opus`，识别结果不受影响。
</Note>

### 支持的语言

不传 `language`（或传空）时启用混合语言识别；语种明确时建议显式指定，短音频与专业术语通常更稳。

| 类别    | 语言（BCP-47 标签）                                                                    |
| :---- | :------------------------------------------------------------------------------- |
| 中文与东亚 | 中文 `zh`、粤语 `yue`、日语 `ja`、韩语 `ko`                                                 |
| 东南亚   | 泰语 `th`、越南语 `vi`、印尼语 `id`、马来语 `ms`、菲律宾语 `fil`                                    |
| 欧美    | 英语 `en`、法语 `fr`、德语 `de`、西班牙语 `es`、意大利语 `it`、葡萄牙语 `pt`、波兰语 `pl`、俄语 `ru`、乌克兰语 `uk` |
| 其他    | 阿拉伯语 `ar`、土耳其语 `tr`                                                              |

### 返回格式

通过 `response_format` 参数指定，可选取值如下：

| 取值             | 响应类型               | 主要字段 / 内容                                                     |
| :------------- | :----------------- | :------------------------------------------------------------ |
| `json`（默认）     | `application/json` | `text` + `duration` + `trace_id`                              |
| `verbose_json` | `application/json` | `text` + `duration` + `n_speakers` + `segments[]`（含说话人、逐句时间戳） |
| `srt`          | `text/plain`       | 标准 SRT 字幕                                                     |
| `vtt`          | `text/vtt`         | WebVTT 字幕                                                     |

流式返回时 `response_format` 仅支持 `json`，事件以 `data: <json>` 逐行推送，字段为 `index` / `delta` / `finish` / `duration`（`duration` 仅终止事件返回）。

## 功能与代码示例

在 [账户管理 → 接口密钥](https://platform.minimax.cn/user-center/basic-information/interface-key) 获取 API Key 并写入环境变量 `MINIMAX_API_KEY`。

### 一次性识别（默认）

<CodeGroup>
  ```python theme={null}
  import os, requests

  api_key = os.getenv("MINIMAX_API_KEY")
  url = "https://api.minimax.cn/v1/speech_to_text"
  headers = {"Authorization": f"Bearer {api_key}"}

  with open("/path/to/audio.mp3", "rb") as f:
      files = {"file": ("audio.mp3", f)}
      data = {"model": "asr-1.0"}
      response = requests.post(url, headers=headers, data=data, files=files)

  response.raise_for_status()
  print(response.json())
  # {"text": "...", "duration": 26.325, "trace_id": "..."}
  ```

  ```bash theme={null}
  curl --location 'https://api.minimax.cn/v1/speech_to_text' \
    --header "Authorization: Bearer ${MINIMAX_API_KEY}" \
    --form 'model="asr-1.0"' \
    --form 'file=@"/path/to/audio.mp3"'
  ```
</CodeGroup>

### 指定语种

<CodeGroup>
  ```python theme={null}
  import os, requests

  api_key = os.getenv("MINIMAX_API_KEY")
  url = "https://api.minimax.cn/v1/speech_to_text"
  headers = {"Authorization": f"Bearer {api_key}", "language": "en"}

  with open("/path/to/podcast.mp3", "rb") as f:
      files = {"file": ("podcast.mp3", f)}
      data = {"model": "asr-1.0"}
      print(requests.post(url, headers=headers, data=data, files=files).json())
  ```

  ```bash theme={null}
  curl --location 'https://api.minimax.cn/v1/speech_to_text' \
    --header "Authorization: Bearer ${MINIMAX_API_KEY}" \
    --header 'language: en' \
    --form 'model="asr-1.0"' \
    --form 'file=@"/path/to/podcast.mp3"'
  ```
</CodeGroup>

### 说话人分离与逐句时间戳

<CodeGroup>
  ```python theme={null}
  import os, requests

  api_key = os.getenv("MINIMAX_API_KEY")
  url = "https://api.minimax.cn/v1/speech_to_text"
  headers = {"Authorization": f"Bearer {api_key}"}

  with open("/path/to/meeting.wav", "rb") as f:
      files = {"file": ("meeting.wav", f)}
      data = {"model": "asr-1.0", "response_format": "verbose_json"}
      result = requests.post(url, headers=headers, data=data, files=files).json()

  for seg in result["segments"]:
      print(f"[{seg['speaker']}] {seg['start']:.2f}-{seg['end']:.2f} {seg['text']}")
  ```

  ```bash theme={null}
  curl --location 'https://api.minimax.cn/v1/speech_to_text' \
    --header "Authorization: Bearer ${MINIMAX_API_KEY}" \
    --form 'model="asr-1.0"' \
    --form 'response_format="verbose_json"' \
    --form 'file=@"/path/to/meeting.wav"'
  ```
</CodeGroup>

返回示例：

```json theme={null}
{
  "text": "嘎嘎会，可以，这把稳了。来检查一下，读下题。",
  "duration": 12.744,
  "n_speakers": 2,
  "segments": [
    {"id": 0, "start": 0.1, "end": 1.66, "speaker": "S1", "text": "嘎嘎会，可以，这把稳了。"},
    {"id": 1, "start": 2.0, "end": 6.10, "speaker": "S2", "text": "来检查一下，读下题。"}
  ],
  "trace_id": "021785229015510a2c883cf675b9804d"
}
```

### 导出 SRT / VTT 字幕

<CodeGroup>
  ```python theme={null}
  import os, requests

  api_key = os.getenv("MINIMAX_API_KEY")
  url = "https://api.minimax.cn/v1/speech_to_text"
  headers = {"Authorization": f"Bearer {api_key}"}

  with open("/path/to/video.mp3", "rb") as f:
      files = {"file": ("video.mp3", f)}
      data = {"model": "asr-1.0", "response_format": "srt"}
      resp = requests.post(url, headers=headers, data=data, files=files)

  with open("subtitle.srt", "w", encoding="utf-8") as out:
      out.write(resp.text)
  ```

  ```bash theme={null}
  curl --location 'https://api.minimax.cn/v1/speech_to_text' \
    --header "Authorization: Bearer ${MINIMAX_API_KEY}" \
    --form 'model="asr-1.0"' \
    --form 'response_format="srt"' \
    --form 'file=@"/path/to/video.mp3"' \
    --output subtitle.srt
  ```
</CodeGroup>

### 流式识别

<CodeGroup>
  ```python theme={null}
  import os, json, requests

  api_key = os.getenv("MINIMAX_API_KEY")
  url = "https://api.minimax.cn/v1/speech_to_text"
  headers = {"Authorization": f"Bearer {api_key}"}

  with open("/path/to/audio.mp3", "rb") as f:
      files = {"file": ("audio.mp3", f)}
      data = {"model": "asr-1.0", "stream": "true"}
      with requests.post(url, headers=headers, data=data, files=files, stream=True) as resp:
          resp.raise_for_status()
          for raw in resp.iter_lines(decode_unicode=True):
              if not raw or not raw.startswith("data:"):
                  continue
              event = json.loads(raw[len("data:"):].strip())
              print(event.get("delta", ""), end="", flush=True)
              if event.get("finish"):
                  break
  ```

  ```bash theme={null}
  curl --location 'https://api.minimax.cn/v1/speech_to_text' \
    --header "Authorization: Bearer ${MINIMAX_API_KEY}" \
    --form 'model="asr-1.0"' \
    --form 'stream="true"' \
    --form 'file=@"/path/to/audio.mp3"' \
    --no-buffer
  ```
</CodeGroup>

推送格式（事件之间以空行分隔）：

```
data: {"index":0,"delta":"实际上","finish":false}

data: {"index":1,"delta":"还是商家赚了","finish":false}

data: {"index":2,"delta":"","finish":true,"duration":26.325}
```

## 错误码

服务采用 OpenAI 风格的错误响应，HTTP 状态码即为错误码，响应体形如 `{"type":"error","error":{...},"request_id":"..."}`。

| HTTP  | `error.type`                 | 触发原因                        |
| :---- | :--------------------------- | :-------------------------- |
| `400` | `bad_request_error`          | 参数不合法，如音频时长超过 500 秒         |
| `401` | `authorized_error`           | API Key 缺失或无效               |
| `402` | `insufficient_balance_error` | 账户余额 / 资源包不足                |
| `413` | `invalid_request_error`      | 请求体超过 50 MB 上限              |
| `422` | `unprocessable_entity_error` | 音频内容涉及敏感内容                  |
| `429` | `rate_limit_error`           | 触发限流                        |
| `500` | `server_error`               | 服务端错误，可携带 `request_id` 联系我们 |

## 推荐阅读

<Columns cols={2}>
  <Card title="语音识别接口" icon="book-open" href="/docs/api-reference/speech-to-text" arrow="true" cta="点击查看">
    Speech to Text 接口的完整参数、返回结构与错误码。
  </Card>

  <Card title="产品定价" icon="book-open" href="/docs/guides/pricing-paygo#语音" arrow="true" cta="点击查看">
    各语音模型的定价说明、计费方式与使用限制。
  </Card>
</Columns>
