<!-- Official source: https://platform.minimax.cn/docs/guides/quickstart-sdk.md -->
<!-- Source SHA-256: f63826b1bd169000465bd3badfea84714b61b5194d8a4c781798c48884ff712e -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.minimaxi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 通过 SDK 接入

> 使用 Anthropic SDK 快速接入 MiniMax API，开始调用 MiniMax-M3 模型。

**1. 安装 Anthropic SDK（推荐）**

```bash Python theme={null}
pip install anthropic
```

```bash Node.js theme={null}
npm install @anthropic-ai/sdk
```

**2. 调用 MiniMax-M3**

```python Python theme={null}
import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="MiniMax-M3",
    max_tokens=1000,
    system="You are a helpful assistant.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Hi, how are you?"
                }
            ]
        }
    ]
)

for block in message.content:
    if block.type == "thinking":
        print(f"Thinking:\n{block.thinking}\n")
    elif block.type == "text":
        print(f"Text:\n{block.text}\n")
```

**3. 示例输出**

```json theme={null}
{
  "thinking": "The user is just greeting me casually. I should respond in a friendly, professional manner.",
  "text": "Hi there! I'm doing well, thanks for asking. I'm ready to help you with whatever you need today—whether it's coding, answering questions, brainstorming ideas, or just chatting. What can I do for you?"
}
```

## 探索更多

> [card] [语言模型](https://platform.minimaxi.com/docs/guides/text-generation.md)
>
> 探索 MiniMax 最新语言模型

> [card] [视频生成](https://platform.minimaxi.com/docs/guides/video-generation.md)
>
> 使用 MiniMax-H3 创建视频生成任务

> [card] [同步语音合成](https://platform.minimaxi.com/docs/guides/speech-t2a-websocket.md)
>
> 使用 Speech 2.8 进行同步语音合成

> [card] [异步语音合成](https://platform.minimaxi.com/docs/guides/speech-t2a-async.md)
>
> 使用 Speech 2.8 进行异步语音合成

> [card] [音色复刻](https://platform.minimaxi.com/docs/guides/speech-voice-clone.md)
>
> 创建音色复刻任务

> [card] [音乐生成](https://platform.minimaxi.com/docs/guides/music-generation.md)
>
> 使用 Music 3.0 进行音乐创作
