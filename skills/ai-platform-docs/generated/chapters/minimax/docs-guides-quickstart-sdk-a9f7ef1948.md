<!-- Official source: https://platform.minimax.cn/docs/guides/quickstart-sdk.md -->
<!-- Source SHA-256: 9bcce6c8877657553a0473300e11d71ae36b1cd7d20e60e7ae7ed2ea7ebfcc42 -->

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

> **[语言模型](/docs/guides/text-generation)**
>
> 探索 MiniMax 最新语言模型

> **[视频生成](/docs/guides/video-generation)**
>
> 使用 MiniMax-H3 创建视频生成任务

> **[同步语音合成](/docs/guides/speech-t2a-websocket)**
>
> 使用 Speech 2.8 进行同步语音合成

> **[异步语音合成](/docs/guides/speech-t2a-async)**
>
> 使用 Speech 2.8 进行异步语音合成

> **[音色复刻](/docs/guides/speech-voice-clone)**
>
> 创建音色复刻任务

> **[音乐生成](/docs/guides/music-generation)**
>
> 使用 Music 3.0 进行音乐创作
