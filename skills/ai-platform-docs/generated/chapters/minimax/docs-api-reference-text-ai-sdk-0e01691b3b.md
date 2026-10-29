<!-- Official source: https://platform.minimax.cn/docs/api-reference/text-ai-sdk.md -->
<!-- Source SHA-256: 7cd52cd02be53f9e5e6acd7297b860ee62da967204fa81ecebce497cbf023e6e -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.minimaxi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# AI SDK

> 通过 AI SDK 调用 MiniMax 模型

为了满足开发者对 [AI SDK](https://ai-sdk.dev) 生态的使用需求，MiniMax 提供了官方社区 Provider。通过简单的配置，即可将 MiniMax 的能力接入到 AI SDK 生态中。

## 快速开始

### 1. 安装 AI SDK 和 MiniMax Provider

```bash npm theme={null}
npm install ai @minimax-ai/ai-sdk-provider
```

```bash pnpm theme={null}
pnpm add ai @minimax-ai/ai-sdk-provider
```

### 2. 配置环境变量

```bash theme={null}
export MINIMAX_API_KEY=${YOUR_API_KEY}
```

配置方法见[配置环境变量](https://platform.minimaxi.com/docs/guides/quickstart-preparation.md#env-vars)。

### 3. 调用 API

```typescript TypeScript theme={null}
import { createMinimax } from '@minimax-ai/ai-sdk-provider';
import { generateText } from 'ai';

const minimax = createMinimax({
  baseURL: 'https://api.minimax.cn/anthropic/v1',
});

const { text, reasoningText } = await generateText({
  model: minimax('MiniMax-M3.1-Flash'),
  system: 'You are a helpful assistant.',
  prompt: 'Hi, how are you?',
});

if (reasoningText) {
  console.log(`Thinking:\n${reasoningText}\n`);
}
console.log(`Text:\n${text}\n`);
```

### 4. 特别注意

在多轮 Function Call 对话中，必须将完整的模型返回（即 assistant 消息）添加到对话历史，以保持思维链的连续性：

* 将完整的 `result.response.messages` 添加到消息历史（包含所有 assistant 和 tool 消息）

## 支持的模型

使用 AI SDK 时，支持以下模型。

| 模型名称 | 上下文窗口 | 模型介绍 |
| :- | :-: | :- |
| MiniMax-M3.1-Flash | 1,000,000 | **原生多模态、1M 上下文的 Frontier Coding 模型，思考深度可调** |
| MiniMax-M3 | 1,000,000 | **原生多模态、1M 上下文的 Frontier Coding 模型** |

> [!NOTE]
>
> TPS（Tokens Per Second）的计算方式详见[常见问题 > 接口相关](https://platform.minimaxi.com/docs/faq/about-apis.md#%E9%97%AE%EF%BC%9A%E8%AF%AD%E8%A8%80%E6%A8%A1%E5%9E%8B%E7%9A%84-tps%EF%BC%88tokens-per-second%EF%BC%89%E6%98%AF%E5%A6%82%E4%BD%95%E8%AE%A1%E7%AE%97%E7%9A%84)。

> [!NOTE]
>
> AI SDK 兼容接口支持 `MiniMax-M3.1-Flash` `MiniMax-M3`
> 模型。如需使用其他模型，请使用标准的 MiniMax API 接口。

## 兼容性说明

### 支持的参数

在使用 AI SDK 接入时，我们支持以下输入参数：

| 参数 | 支持状态 | 说明 |
| :- | :- | :- |
| `model` | 完全支持 | 支持 `MiniMax-M3.1-Flash` `MiniMax-M3` 模型 |
| `messages` | 部分支持 | 支持文本、图片和工具调用；使用默认的 `minimax`（Anthropic 兼容格式）时还支持 PDF 文档；不支持视频输入 |
| `maxOutputTokens` | 完全支持 | 最大生成 token 数 |
| `system` | 完全支持 | 系统提示词 |
| `toolChoice` | 部分支持 | 工具选择策略，仅支持 `auto` |
| `tools` | 完全支持 | 工具定义 |
| `temperature` | 忽略 | 暂不支持指定，传入的值不会生效。`MiniMax-M3.1-Flash` 和 `MiniMax-M3` 固定使用 1 |
| `topP` | 忽略 | 暂不支持指定，传入的值不会生效。`MiniMax-M3.1-Flash` 和 `MiniMax-M3` 固定使用 0.95。若传入，取值需在 (0, 1] 范围内 |

### Messages 字段支持

| 字段类型 | 支持状态 | 说明 |
| :- | :- | :- |
| `role="user"` | 完全支持 | 用户文本消息 |
| `role="assistant"` | 完全支持 | 助手响应 |
| `role="tool"` | 完全支持 | 工具调用结果 |
| `type="text"` | 完全支持 | 文本内容 |
| `type="tool-call"` | 完全支持 | 工具调用 |
| `type="tool-result"` | 完全支持 | 工具调用结果 |
| `type="image"` | 部分支持 | 图片输入。使用默认的 `minimax` 传图片 URL 时，需指定具体的 `mediaType`（如 `image/jpeg`）。AI SDK 已不再推荐该类型，建议改用 `type="file"` |
| `type="file"` | 部分支持 | 支持图片，`mediaType` 需为具体的图片类型（如 `image/jpeg`、`image/png`），可传 URL 或 base64；使用默认的 `minimax` 时还支持 PDF（`application/pdf`）；不支持视频 |

## 示例代码

### OpenAI 兼容格式

默认的 `minimax` 使用 Anthropic 兼容格式（`/anthropic/v1/messages`）。如需使用 OpenAI Chat Completions 兼容格式（`/v1/chat/completions`），请改用 `createMinimaxOpenAI`：

```typescript TypeScript theme={null}
import { createMinimaxOpenAI } from '@minimax-ai/ai-sdk-provider';
import { generateText } from 'ai';

const minimax = createMinimaxOpenAI({
  baseURL: 'https://api.minimax.cn/v1',
});

const { text, reasoningText } = await generateText({
  model: minimax('MiniMax-M3.1-Flash'),
  system: 'You are a helpful assistant.',
  prompt: 'Hi, how are you?',
});

if (reasoningText) {
  console.log(`Thinking:\n${reasoningText}\n`);
}
console.log(`Text:\n${text}\n`);
```

### 流式响应

```typescript TypeScript theme={null}
import { createMinimax } from '@minimax-ai/ai-sdk-provider';
import { streamText } from 'ai';

const minimax = createMinimax({
  baseURL: 'https://api.minimax.cn/anthropic/v1',
});

console.log("Starting stream response...\n");
console.log("=".repeat(60));
console.log("Thinking Process:");
console.log("=".repeat(60));

const result = streamText({
  model: minimax('MiniMax-M3.1-Flash'),
  system: 'You are a helpful assistant.',
  prompt: 'Hi, how are you?',
  onError({ error }) {
    console.error(error);
  },
});

let inText = false;

for await (const part of result.fullStream) {
  if (part.type === 'reasoning-delta') {
    // 流式输出思考过程
    process.stdout.write(part.text);
  } else if (part.type === 'text-delta') {
    if (!inText) {
      inText = true;
      console.log("\n" + "=".repeat(60));
      console.log("Response Content:");
      console.log("=".repeat(60));
    }
    // 流式输出文本内容
    process.stdout.write(part.text);
  }
}

console.log("\n");
```

## 注意事项

> [!WARNING]
>
> 1. AI SDK 兼容接口目前支持 `MiniMax-M3.1-Flash` `MiniMax-M3` 模型
>
> 2. `temperature`、`topP` 参数会被忽略
>
> 3. 当前不支持通过 AI SDK 输入视频；PDF 文档仅在使用默认的 `minimax`（Anthropic 兼容格式）时支持
>
> 4. 默认的 `minimax` Provider 实例使用 Anthropic 兼容 API 格式。如需使用 OpenAI 兼容格式，请使用 `createMinimaxOpenAI`，详见 [OpenAI 兼容格式](#openai-兼容格式)。
>
> 5. 更多信息请参阅 [MiniMax AI Provider on AI SDK](https://ai-sdk.dev/providers/community-providers/minimax) 和 [GitHub 仓库](https://github.com/MiniMax-AI/vercel-minimax-ai-provider)
