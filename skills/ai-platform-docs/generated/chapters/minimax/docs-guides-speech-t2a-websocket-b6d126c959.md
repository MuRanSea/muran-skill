<!-- Official source: https://platform.minimax.cn/docs/guides/speech-t2a-websocket.md -->
<!-- Source SHA-256: e7a02beb6661f67fc295ce315b0762f4229364bdf831470e9c7e827acf330a34 -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.minimaxi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 同步语音合成

> 同步语音合成支持基于文本到语音的同步生成，单次可处理最长 10,000 字符的文本。

## 支持模型

以下为 MiniMax 提供的语音模型及其特性说明。

| 模型 | 特性 |
| :- | :- |
| speech-2.8-hd | 情绪渲染融合语气词，重塑自然听感 |
| speech-2.8-turbo | 极致生成速度，更自然逼真的音频效果 |
| speech-2.6-hd | 超低延时，归一化升级，更高自然度 |
| speech-2.6-turbo | 极速版，更快更优惠，更适用于语音聊天和数字人场景 |
| speech-02-hd | 拥有出色的韵律、稳定性和复刻相似度，音质表现突出 |
| speech-02-turbo | 拥有出色的韵律和稳定性，小语种能力加强，性能表现出色 |

## 支持语言

MiniMax 的语音合成模型具备卓越的跨语言能力，全面支持 40 种全球广泛使用的语言。我们致力于打破语言壁垒，构建真正意义上的全球通用人工智能模型。

目前支持的语言包含：

| 支持语种 | | |
| :- | :- | :- |
| 1. 中文（Chinese） | 15. 土耳其语（Turkish） | 28. 马来语（Malay） |
| 2. 粤语（Cantonese） | 16. 荷兰语（Dutch） | 29. 波斯语（Persian） |
| 3. 英语（English） | 17. 乌克兰语（Ukrainian） | 30. 斯洛伐克语（Slovak） |
| 4. 西班牙语（Spanish） | 18. 泰语（Thai） | 31. 瑞典语（Swedish） |
| 5. 法语（French） | 19. 波兰语（Polish） | 32. 克罗地亚语（Croatian） |
| 6. 俄语（Russian） | 20. 罗马尼亚语（Romanian） | 33. 菲律宾语（Filipino） |
| 7. 德语（German） | 21. 希腊语（Greek） | 34. 匈牙利语（Hungarian） |
| 8. 葡萄牙语（Portuguese） | 22. 捷克语（Czech） | 35. 挪威语（Norwegian） |
| 9. 阿拉伯语（Arabic） | 23. 芬兰语（Finnish） | 36. 斯洛文尼亚语（Slovenian） |
| 10. 意大利语（Italian） | 24. 印地语（Hindi） | 37. 加泰罗尼亚语（Catalan） |
| 11. 日语（Japanese） | 25. 保加利亚语（Bulgarian） | 38. 尼诺斯克语（Nynorsk） |
| 12. 韩语（Korean） | 26. 丹麦语（Danish） | 39. 泰米尔语（Tamil） |
| 13. 印尼语（Indonesian） | 27. 希伯来语（Hebrew） | 40. 阿非利卡语（Afrikaans） |
| 14. 越南语（Vietnamese） | | |

## 文本归一化

控制语音合成前如何将书面文本转换为口语文本。

文本归一化会把书面写法转换为更适合朗读的形式。例如数字、日期、时间、货币、电话号码等结构化表达，往往需要结合上下文进行展开或解读。

不传 `text_normalization_mode` 时，沿用 `voice_setting.text_normalization` 的设置（默认关闭）。

通过 `text_normalization_mode` 字段控制归一化策略：

* `basic`：基于规则的快速文本归一化，延迟低
* `quality`：采用 LLM + 规则的混合方案，归一化质量更高，但会增加额外延迟

### Basic 模式

`basic` 面向低延迟的文本归一化。

它使用基于规则的归一化系统，在生成语音前处理常见的书面表达。

对于大多数语音合成请求，`basic` 能在归一化质量、稳定性和延迟之间取得良好平衡。

```json theme={null}
{
  "text_normalization_mode": "basic"
}
```

### Quality 模式

`quality` 适用于归一化质量比延迟更重要的场景。

它采用 LLM + 规则的混合方案，系统会根据输入文本自动将请求路由到规则分支或 LLM 分支。

与 `basic` 相比，该模式对更复杂、更依赖上下文的输入有更好的归一化效果。

```json theme={null}
{
  "text_normalization_mode": "quality"
}
```

<Note>
  `quality` 目前仅对非流式 HTTP 请求（`stream=false`）生效，且仅支持 `speech-2.8-hd`、`speech-2.8-turbo`、`speech-2.6-hd`、`speech-2.6-turbo`。流式请求（包括 WebSocket）或其他模型传入 `quality` 时按 `basic` 处理，不会报错。
</Note>

### 延迟

`quality` 会增加额外的预处理延迟：

* 选择规则分支时约 30 ms
* 触发 LLM 分支时约 100 ms

分支由系统根据输入文本自动选择。

### 如何选择

大多数应用推荐使用 `basic`。

当归一化准确性更重要、且可以接受额外的预处理延迟时，使用 `quality`。

## 接入地址

同步语音合成的 3 个接口均支持以下域名，华北地区建议接入 `api-bj.minimaxi.com`，首包延迟更低。

| 接口 | 默认地址 | 华北地区建议接入 |
| :- | :- | :- |
| [同步语音合成（HTTP）](/docs/api-reference/speech-t2a-http) | `https://api.minimax.cn/v1/t2a_v2` | `https://api-bj.minimaxi.com/v1/t2a_v2` |
| [同步语音合成（WebSocket）](/docs/api-reference/speech-t2a-websocket) | `wss://api.minimax.cn/ws/v1/t2a_v2` | `wss://api-bj.minimaxi.com/ws/v1/t2a_v2` |
| [双向流式语音合成（WebSocket）](/docs/api-reference/speech-t2a-websocket-bidi) | `wss://api.minimax.cn/ws/v1/t2a_v2_bidi` | `wss://api-bj.minimaxi.com/ws/v1/t2a_v2_bidi` |

## 流式请求示例

本指南指导，流式播放返回的音频文件，并保存完整音频文件。

⚠️ 注意，为实时播放音频流，需要先安装 [mpv 播放器](https://mpv.io/installation/)。并且，需要先将密钥信息写入环境变量 `MINIMAX_API_KEY`。

请求示例

```python theme={null}

import asyncio
import websockets
import json
import ssl
import subprocess
import os

model = "speech-2.8-hd"
file_format = "mp3"

class StreamAudioPlayer:
    def __init__(self):
        self.mpv_process = None

    def start_mpv(self):
        """Start MPV player process"""
        try:
            mpv_command = ["mpv", "--no-cache", "--no-terminal", "--", "fd://0"]
            self.mpv_process = subprocess.Popen(
                mpv_command,
                stdin=subprocess.PIPE,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            print("MPV player started")
            return True
        except FileNotFoundError:
            print("Error: mpv not found. Please install mpv")
            return False
        except Exception as e:
            print(f"Failed to start mpv: {e}")
            return False

    def play_audio_chunk(self, hex_audio):
        """Play audio chunk"""
        try:
            if self.mpv_process and self.mpv_process.stdin:
                audio_bytes = bytes.fromhex(hex_audio)
                self.mpv_process.stdin.write(audio_bytes)
                self.mpv_process.stdin.flush()
                return True
        except Exception as e:
            print(f"Play failed: {e}")
            return False
        return False

    def stop(self):
        """Stop player"""
        if self.mpv_process:
            if self.mpv_process.stdin and not self.mpv_process.stdin.closed:
                self.mpv_process.stdin.close()
            try:
                self.mpv_process.wait(timeout=20)
            except subprocess.TimeoutExpired:
                self.mpv_process.terminate()

async def establish_connection(api_key):
    """Establish WebSocket connection"""
    url = "wss://api.minimax.cn/ws/v1/t2a_v2"
    headers = {"Authorization": f"Bearer {api_key}"}

    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    try:
        ws = await websockets.connect(url, additional_headers=headers, ssl=ssl_context)
        connected = json.loads(await ws.recv())
        if connected.get("event") == "connected_success":
            print("Connection successful")
            return ws
        return None
    except Exception as e:
        print(f"Connection failed: {e}")
        return None

async def start_task(websocket):
    """Send task start request"""
    start_msg = {
        "event": "task_start",
        "model": model,
        "voice_setting": {
            "voice_id": "male-qn-qingse",
            "speed": 1,
            "vol": 1,
            "pitch": 0,
            "english_normalization": False
        },
        "audio_setting": {
            "sample_rate": 32000,
            "bitrate": 128000,
            "format": file_format,
            "channel": 1
        }
    }
    await websocket.send(json.dumps(start_msg))
    response = json.loads(await websocket.recv())
    return response.get("event") == "task_started"

async def continue_task_with_stream_play(websocket, text, player):
    """Send continue request and stream play audio"""
    await websocket.send(json.dumps({
        "event": "task_continue",
        "text": text
    }))

    chunk_counter = 1
    total_audio_size = 0
    audio_data = b""

    while True:
        try:
            response = json.loads(await websocket.recv())

            if "data" in response and "audio" in response["data"]:
                audio = response["data"]["audio"]
                if audio:
                    print(f"Playing chunk #{chunk_counter}")
                    audio_bytes = bytes.fromhex(audio)
                    if player.play_audio_chunk(audio):
                        total_audio_size += len(audio_bytes)
                        audio_data += audio_bytes
                        chunk_counter += 1

            if response.get("is_final"):
                print(f"Audio synthesis completed: {chunk_counter-1} chunks")
                if player.mpv_process and player.mpv_process.stdin:
                    player.mpv_process.stdin.close()

                # Save audio to file
                with open(f"output.{file_format}", "wb") as f:
                    f.write(audio_data)
                print(f"Audio saved as output.{file_format}")

                estimated_duration = total_audio_size * 0.0625 / 1000
                wait_time = max(estimated_duration + 5, 10)
                return wait_time

        except Exception as e:
            print(f"Error: {e}")
            break

    return 10

async def close_connection(websocket):
    """Close connection"""
    if websocket:
        try:
            await websocket.send(json.dumps({"event": "task_finish"}))
            await websocket.close()
        except Exception:
            pass

async def main():
    API_KEY = os.getenv("MINIMAX_API_KEY")
    TEXT = "真正的危险不是计算机开始像人一样思考(sighs)，而是人开始像计算机一样思考。计算机只是可以帮我们处理一些简单事务。"

    player = StreamAudioPlayer()

    try:
        if not player.start_mpv():
            return

        ws = await establish_connection(API_KEY)
        if not ws:
            return

        if not await start_task(ws):
            print("Task startup failed")
            return

        wait_time = await continue_task_with_stream_play(ws, TEXT, player)
        await asyncio.sleep(wait_time)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        player.stop()
        if 'ws' in locals():
            await close_connection(ws)

if __name__ == "__main__":
    asyncio.run(main())
```

## 推荐阅读

<Columns cols={2}>
  <Card title="同步语音合成（HTTP）" icon="book-open" href="/docs/api-reference/speech-t2a-http" arrow="true" cta="点击查看">
    通过 HTTP 请求一次提交完整文本并返回合成音频，支持流式输出。
  </Card>

  <Card title="同步语音合成（WebSocket）" icon="book-open" href="/docs/api-reference/speech-t2a-websocket" arrow="true" cta="点击查看">
    通过 WebSocket 连接由客户端按句发送文本，流式返回合成音频，适合低延迟的实时播报。
  </Card>

  <Card title="双向流式语音合成（WebSocket）" icon="book-open" href="/docs/api-reference/speech-t2a-websocket-bidi" arrow="true" cta="点击查看">
    通过 WebSocket 连接按任意粒度（含逐字）流式发送文本，由服务端自动攒句合成，适合对接大模型流式输出。
  </Card>

  <Card title="产品定价" icon="book-open" href="/docs/pricing/overview#overview" arrow="true" cta="点击查看">
    各模型的定价说明、计费方式及使用限制。
  </Card>

  <Card title="速率限制" icon="book-open" href="/docs/guides/rate-limits#语音" arrow="true" cta="点击查看">
    为保证资源的高效使用，引入速率限制，以确保服务的可用性、稳定性。
  </Card>
</Columns>
