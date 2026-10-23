<!-- Official source: https://platform.minimax.cn/docs/guides/text-m3-function-call.md -->
<!-- Source SHA-256: 58723ebb2ff5fc89f419c5978e8bb705706f06817e396655ea7857dc51978a39 -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.minimaxi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 工具使用 & 交错思维链

> MiniMax-M3.1-Flash 是一款 Agentic Model，具备优秀的工具使用 (Tool Use) 能力。

MiniMax-M3.1-Flash 原生支持 Interleaved Thinking。它能够在每轮 Tool Use 前，根据环境或工具的返回 (Output) 进行思考，并决策下一步行动。

![](https://filecdn.minimax.chat/public/4f4b43c1-f0a5-416a-8770-1a4f80feeb1e.png)

这种能力使其在长程、复杂任务中表现出色，并在 SWE、BrowseCamp、xBench 等 Code & Agent Benchmark 上达到了 SOTA 水平。

下面我们通过具体的案例，说明 MiniMax-M3.1-Flash 在 Tool Use 和 Interleaved Thinking 上的最佳实践，它的核心是：回传每一次模型 Response 的全部信息，尤其是其中的思考字段（`thinking` / `reasoning_content`）。

## 参数说明

### 请求参数说明

* `tools`: 定义可调用的函数列表，包含函数名、描述和参数规范

### 响应参数说明

工具使用响应中的关键字段：

* `thinking` / `reasoning_content`: 模型的思考（thinking）
* `text` / `content`: 模型输出的文本
* `tool_use` / `tool_calls`: 模型决定调用工具
* `name` / `function.name`: 被调用的工具名称
* `input` / `function.arguments`: 工具调用参数（OpenAI 格式下为 JSON 字符串）
* `id`: 工具调用的唯一标识符

> [!NOTE]
>
> MiniMax-M3.1-Flash 按需思考：在简单的工具调用中，模型可能直接调用工具而不输出思考内容，此时该轮响应中没有 `thinking` 内容块或 `reasoning_content` 字段。解析时请先判断字段是否存在，无论本轮是否包含思考内容，都需要完整回传模型返回的消息。

## 特别注意

在多轮 Function Call 对话中，必须将完整的模型返回（即 assistant 消息）添加到对话历史，以保持思维链的连续性：

**OpenAI SDK:**

* 将完整的 `response_message` 对象（包含 `reasoning_content` 和 `tool_calls` 字段）添加到消息历史
* 模型的思考内容通过 `reasoning_content` 字段返回，回传时需要一并保留

**Anthropic SDK:**

* 将完整的 `response.content`（包含 thinking/text/tool\_use 等所有块）添加到消息历史
* `response.content` 是一个列表，包含多种类型的内容块，必须完整回传

## 请求示例

### Anthropic SDK

#### 配置环境变量

```bash theme={null}
export ANTHROPIC_BASE_URL=https://api.minimax.cn/anthropic
export ANTHROPIC_API_KEY=${YOUR_API_KEY}
```

#### 示例代码

```python theme={null}
import anthropic
import json

# 初始化客户端
client = anthropic.Anthropic()

# 定义工具：天气查询
tools = [
    {
        "name": "get_weather",
        "description": "Get weather of a location, the user should supply a location first.",
        "input_schema": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The city and state, e.g. San Francisco, US",
                }
            },
            "required": ["location"]
        }
    }
]

def send_messages(messages):
    params = {
        "model": "MiniMax-M3.1-Flash",
        "max_tokens": 4096,
        "messages": messages,
        "tools": tools,
    }

    response = client.messages.create(**params)
    return response

def process_response(response):
    thinking_blocks = []
    text_blocks = []
    tool_use_blocks = []

    # 遍历所有内容块
    for block in response.content:
        if block.type == "thinking":
            thinking_blocks.append(block)
            print(f"💭 Thinking>\n{block.thinking}\n")
        elif block.type == "text":
            text_blocks.append(block)
            print(f"💬 Model>\t{block.text}")
        elif block.type == "tool_use":
            tool_use_blocks.append(block)
            print(f"🔧 Tool>\t{block.name}({json.dumps(block.input, ensure_ascii=False)})")

    return thinking_blocks, text_blocks, tool_use_blocks

# 1. 用户提问
messages = [{"role": "user", "content": "How's the weather in San Francisco?"}]
print(f"\n👤 User>\t {messages[0]['content']}")

# 2. 模型返回第一轮响应（可能包含工具调用）
response = send_messages(messages)
thinking_blocks, text_blocks, tool_use_blocks = process_response(response)

# 3. 如果有工具调用，执行工具并继续对话
if tool_use_blocks:
    # ⚠️ 关键：将助手的完整响应回传到消息历史
    # response.content 包含所有块的列表：[thinking块, text块, tool_use块]
    # 必须完整回传，否则后续对话会丢失上下文信息
    messages.append({
        "role": "assistant",
        "content": response.content
    })

    # 执行工具并返回结果（这里模拟天气API调用）
    print(f"\n🔨 执行工具: {tool_use_blocks[0].name}")
    tool_result = "24℃, sunny"
    print(f"📊 工具返回: {tool_result}")

    # 添加工具执行结果
    messages.append({
        "role": "user",
        "content": [
            {
                "type": "tool_result",
                "tool_use_id": tool_use_blocks[0].id,
                "content": tool_result
            }
        ]
    })

    # 4. 获取最终回复
    final_response = send_messages(messages)
    process_response(final_response)
```

**代码输出结果如下：**

```nushell theme={null}
👤 User>	 How's the weather in San Francisco?
💬 Model>	I'll check that for you.
🔧 Tool>	get_weather({"location": "San Francisco, US"})

🔨 执行工具: get_weather
📊 工具返回: 24℃, sunny
💭 Thinking>
The user asked about the weather in San Francisco. The tool returned 24°C and sunny. Let me present that. Note 24°C is 75°F. I should just report the result. Maybe add a note about the temperature being unusually warm for SF, but I shouldn't over-speculate. I'll present the result clearly.

💬 Model>	The weather in San Francisco is currently:

- **Temperature:** 24°C (about 75°F)
- **Conditions:** Sunny

A warm, sunny day — you'd typically want light clothing and maybe sunscreen if you're heading outside. Let me know if you'd like the forecast for a different location or need more details!
```

**第一轮请求的返回结果**

```json theme={null}
{
    "id": "0722aa34c63ce29f90ac9051ece69b22",
    "type": "message",
    "role": "assistant",
    "model": "MiniMax-M3.1-Flash",
    "content": [
        {
            "text": "I'll check that for you.",
            "type": "text"
        },
        {
            "type": "tool_use",
            "id": "call_function_a5g4we9cji7p_1",
            "name": "get_weather",
            "input": {
                "location": "San Francisco, US"
            }
        }
    ],
    "usage": {
        "input_tokens": 280,
        "output_tokens": 37,
        "cache_creation_input_tokens": 0,
        "cache_read_input_tokens": 188
    },
    "stop_reason": "tool_use",
    "base_resp": {
        "status_code": 0,
        "status_msg": ""
    }
}
```

### OpenAI SDK

#### 配置环境变量

```bash theme={null}
export OPENAI_BASE_URL=https://api.minimax.cn/v1
export OPENAI_API_KEY=${YOUR_API_KEY}
```

#### 示例代码

通过 OpenAI SDK 调用 MiniMax-M3.1-Flash 时，思考内容通过 `reasoning_content` 字段返回，可以直接用于展示。

> [!NOTE]
>
> 重要提醒：为了保证 Interleaved Thinking 的生效、模型思维链不被打断，包含 `reasoning_content` 在内的完整 `response_message` 必须被保留在 Message History 中，在下一轮调用中回传给模型。如此才能发挥模型的最佳性能！

请注意请求并解析 API 返回的函数 `send_messages` 的实现，和追加历史消息 `messages.append(response_message)` 操作：

```python theme={null}
import json

from openai import OpenAI

client = OpenAI()

# 定义工具：天气查询
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get weather of a location, the user should supply a location first.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, US",
                    }
                },
                "required": ["location"],
            },
        },
    },
]


def send_messages(messages):
    """发送消息并返回响应"""
    response = client.chat.completions.create(
        model="MiniMax-M3.1-Flash",
        messages=messages,
        tools=tools,
    )
    return response.choices[0].message


# 1. 用户提问
messages = [{"role": "user", "content": "How's the weather in San Francisco?"}]
print(f"👤 User>\t {messages[0]['content']}")

# 2. 模型返回工具调用
response_message = send_messages(messages)

if response_message.tool_calls:
    tool_call = response_message.tool_calls[0]
    function_args = json.loads(tool_call.function.arguments)
    if getattr(response_message, "reasoning_content", None):
        print(f"💭 Thinking>\t {response_message.reasoning_content}")
    print(f"💬 Model>\t {response_message.content}")
    print(f"🔧 Tool>\t {tool_call.function.name}({function_args['location']})")

    # 3. 执行工具并返回结果
    # ⚠️ 关键：完整回传 response_message（包含 reasoning_content 和 tool_calls）
    messages.append(response_message)
    messages.append(
        {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": "24℃, sunny",  # 实际应用中这里应该调用真实的天气API
        }
    )

    # 4. 获取最终回复
    final_message = send_messages(messages)
    if getattr(final_message, "reasoning_content", None):
        print(f"💭 Thinking>\t {final_message.reasoning_content}")
    print(f"💬 Model>\t {final_message.content}")
else:
    print(f"💬 Model>\t {response_message.content}")
```

**代码输出结果如下：**

```
👤 User>	 How's the weather in San Francisco?
💬 Model>	 I'll check the weather in San Francisco for you.
🔧 Tool>	 get_weather(San Francisco, US)
💬 Model>	 The weather in San Francisco is currently **24°C (75°F) and sunny** — pleasant conditions for a day out. If you need more detail (like wind, humidity, or a multi-day forecast), just let me know.
```

**第一轮请求的返回结果**

```json theme={null}
{
    "id": "0722aa35f6b10a17627b07ff112caa6a",
    "choices": [
        {
            "finish_reason": "tool_calls",
            "index": 0,
            "message": {
                "content": "I'll check that for you.",
                "role": "assistant",
                "name": "MiniMax AI",
                "tool_calls": [
                    {
                        "id": "call_function_y7ipauye40nx_1",
                        "type": "function",
                        "function": {
                            "name": "get_weather",
                            "arguments": "{\"location\": \"San Francisco, US\"}"
                        },
                        "index": 0
                    }
                ],
                "audio_content": ""
            }
        }
    ],
    "created": 1792243509,
    "model": "MiniMax-M3.1-Flash",
    "object": "chat.completion",
    "usage": {
        "total_tokens": 505,
        "total_characters": 0,
        "prompt_tokens": 468,
        "completion_tokens": 37,
        "prompt_tokens_details": {
            "cached_tokens": 466
        }
    },
    "input_sensitive": false,
    "output_sensitive": false,
    "input_sensitive_type": 0,
    "output_sensitive_type": 0,
    "output_sensitive_int": 0,
    "base_resp": {
        "status_code": 0,
        "status_msg": ""
    }
}
```

## 注意事项

如果在使用MiniMax模型过程中遇到任何问题：

* 通过邮箱 [Model@minimax.io](mailto:Model@minimax.io) 等官方渠道联系我们的技术支持团队
* 在我们的 [Github](https://github.com/MiniMax-AI/MiniMax-M2/issues) 仓库提交Issue

## 推荐阅读

> **[在 AI 编程工具里使用 MiniMax-M3.1-Flash](/docs/m-plan/openclaw.md)**
>
> 具备代码理解能力，适用于代码助手等场景。

> **[文本生成指南](/docs/guides/text-generation.md)**
>
> 支持通过 Anthropic 和 OpenAI 兼容接口进行文本生成调用

> **[Anthropic API 兼容（推荐）](/docs/api-reference/text-anthropic-api.md)**
>
> 通过 Anthropic SDK 调用 MiniMax 模型

> **[OpenAI API 兼容](/docs/api-reference/text-openai-api.md)**
>
> 通过 OpenAI SDK 调用 MiniMax 模型
