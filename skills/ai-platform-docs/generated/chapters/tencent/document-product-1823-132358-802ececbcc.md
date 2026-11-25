<!-- Official source: https://cloud.tencent.com/document/product/1823/132358 -->
<!-- Source SHA-256: ed82ed95f2528bb5780d57cb191897161b044afc0beff93f05df2b4f375eadd8 -->

# 联网搜索

官方来源：https://cloud.tencent.com/document/product/1823/132358
最近更新时间：2026-11-18 14:47:30

## 功能概述

联网搜索是 TokenHub 提供的模型增强能力。开启后，大模型在回答时可自动调用搜索引擎获取实时网络信息，解决模型知识时效性不足的问题。模型会**自主判断**是否需要搜索、搜索什么关键词，并基于搜索结果生成回答。

### 联网搜索服务类型

TokenHub 当前提供两类联网搜索服务：

| 联网搜索方式 | 能力提供方 | 适用模型 | 使用方式 | 价格 |
| --- | --- | --- | --- | --- |
| TokenHub 联网搜索 | TokenHub | TokenHub 自建模型（非原厂直供），详情见[模型与协议支持矩阵](https://cloud.tencent.com/document/product/1823/132358#2fbb127a-dc23-4296-b791-3ba7eb734e75) | 需在**开通管理 >** [插件](https://console.cloud.tencent.com/tokenhub/open-management?regionId=1&tab=tools)打开联网搜索开关。详细使用方式请参考本文后续章节 | 按搜索次数计费，分轻量版 / 标准版，价格参见[模型价格](https://cloud.tencent.com/document/product/1823/130055) |
| DeepSeek 原厂联网搜索 | DeepSeek（模型供应商） | DeepSeek 原厂直供模型 | 无需开启可直接调用，请参见 [DeepSeek 调用指南](https://cloud.tencent.com/document/product/1823/132248) 的"联网搜索"章节了解详细调用方式 | 按搜索次数计费，网页 Search 与 Fetch 分别计费，价格参见[模型价格](https://cloud.tencent.com/document/product/1823/130055) |

**说明：**

本文后续章节介绍 **TokenHub 联网搜索** 的使用方式。

### 模型与协议支持矩阵

| **模型名称** | **model 参数值** | **API 协议** | **端点** |
| --- | --- | --- | --- |
| Hy4 | `hy4` | Responses API、Chat API | `/v1/responses`、`/v1/chat/completions` |
| Hy3 | `hy3` | Responses API、Chat API | `/v1/responses`、`/v1/chat/completions` |
| DeepSeek-V4.1-Flash-1017 | `deepseek-v4.1-flash-1017` | Responses API、Chat API、Message API | `/v1/responses`、`/v1/chat/completions`、`/v1/messages` |
| DeepSeek-V4.1-Flash | `deepseek-v4.1-flash` | Responses API、Chat API、Message API | `/v1/responses`、`/v1/chat/completions`、`/v1/messages` |
| DeepSeek-V4-Pro 0813 正式版 | `deepseek-v4-pro-0813` | Chat API、Message API | `/v1/chat/completions`、`/v1/messages` |
| DeepSeek V4 Pro | `deepseek-v4-pro` | Chat API、Message API | `/v1/chat/completions`、`/v1/messages` |

联网搜索可与思维链组合使用。开启思维链后，模型会在搜索前后进行深度推理，对多源信息进行交叉对比与综合分析，适合调研、比较、决策类场景。

#### 思维链默认策略

不同模型的默认思考开关和默认推理强度不同，具体默认策略请参见 [深度思考](https://cloud.tencent.com/document/product/1823/131208) 文档。

## 开通服务

如需开通 TokenHub 联网搜索服务，请在**开通管理 >** [插件](https://console.cloud.tencent.com/tokenhub/open-management?regionId=1&tab=tools)页面领取**联网搜索免费资源包**或主动开通按量付费。

**说明：**

如需快速体验联网搜索效果，可在 [模型体验-语言模型](https://console.cloud.tencent.com/tokenhub/text) 页面选择已支持联网搜索的模型，开启联网搜索后直接对话。

调用情况可在 开通管理 > [插件](https://console.cloud.tencent.com/tokenhub/open-management?regionId=1&tab=tools) > 用量监控中查询，包含联网搜索请求次数和搜索引擎调用次数。

DeepSeek 原厂联网搜索无需开通服务，可直接传入参数使用。

## 搜索版本与费用

联网搜索支持轻量版和标准版两种搜索版本，不同搜索版本对应不同价格。调用前请根据业务效果和成本需求选择搜索版本，具体价格请参见 [模型价格](https://cloud.tencent.com/document/product/1823/130055#b8d8c1d9-2f6d-4f3f-9389-e6b14efb770c)。

| 搜索版本 | 参数取值 | 说明 |
| --- | --- | --- |
| 轻量版 | `lite` | 选择轻量版时，将 `search_source` 指定为 `lite`。 |
| 标准版 | `standard` | 不传 `search_source` 时默认为标准版。 |

## 使用限制

| 限制项 | 说明 |
| --- | --- |
| QPS 限制 | 5 QPS |
| 使用地域 | 广州 |

## 通用能力说明

联网搜索用于补充模型知识时效性。基础调用参数、鉴权、BaseURL 和通用响应结构请参见 [语言模型调用概览](https://cloud.tencent.com/document/product/1823/130079)，本文只说明联网搜索相关差异。完整请求示例请参见 [Chat 协议](https://cloud.tencent.com/document/product/1823/132358#ec08a04e-5718-4181-b85a-b633f5d1e9d8)、[Responses 协议](https://cloud.tencent.com/document/product/1823/132358#19bb7ca1-b05c-4ba2-8989-6ad3a2396892) 和 [Message 协议](https://cloud.tencent.com/document/product/1823/132358#0f6edc95-f3ed-48cd-b103-3b4cdec24a5b)。

**开启搜索**：适用于天气、新闻、公开资料查询等需要实时信息的场景。Chat API 在联网搜索配置中开启，Responses API 在工具列表中声明联网搜索工具。

Chat API

Responses API

```json
{
  "web_search_options": {
    "enable": true
  }
}
```

```json
{
  "tools": [
    {
      "type": "web_search"
    }
  ]
}
```

**指定搜索版本**：需要指定本次请求使用的搜索版本时，可通过搜索版本参数选择轻量版或标准版；不传时默认使用标准版。

Chat API

Responses API

```json
{
  "web_search_options": {
    "enable": true,
    "search_source": "lite"
  }
}
```

```json
{
  "tools": [
    {
      "type": "web_search",
      "search_source": "lite"
    }
  ]
}
```

**补充用户位置**：当问题和用户所在地相关时，可传入用户位置参数。例如查询本地天气时，可提供国家、地区、城市和时区，帮助模型返回更贴近用户位置的搜索结果。

Chat API

Responses API

```json
{
  "web_search_options": {
    "enable": true,
    "user_location": {
      "type": "approximate",
      "country": "CN",
      "region": "Guangdong",
      "city": "Shenzhen",
      "timezone": "Asia/Shanghai"
    }
  }
}
```

```json
{
  "tools": [
    {
      "type": "web_search",
      "user_location": {
        "type": "approximate",
        "country": "CN",
        "region": "Guangdong",
        "city": "Shenzhen",
        "timezone": "Asia/Shanghai"
      }
    }
  ]
}
```

**调整搜索上下文**：Responses API 可通过搜索上下文参数控制每轮搜索注入模型的上下文体积。需要参考更多公开资料的调研类问题，可选择更大的搜索上下文；该参数不表示固定搜索次数或固定引用数量。

```json
{
  "tools": [
    {
      "type": "web_search",
      "search_context_size": "high"
    }
  ]
}
```

**查看引用来源**：开启联网搜索后，回答可包含引用标记。Chat API 通过 `search_results` 返回来源信息，Responses API 通过 `annotations` 返回来源信息。

Chat API

Responses API

```json
{
  "choices": [
    {
      "message": {
        "content": "根据检索结果，模型生成的示例回答正文[1]。",
        "search_results": [
          {
            "index": 1,
            "url": "https://example.com/source/1",
            "name": "示例来源标题"
          }
        ]
      }
    }
  ]
}
```

```json
{
  "output": [
    {
      "type": "message",
      "content": [
        {
          "type": "output_text",
          "text": "根据检索结果，模型生成的示例回答正文[1]。",
          "annotations": [
            {
              "type": "url_citation",
              "index": 1,
              "url": "https://example.com/source/1",
              "title": "示例来源标题"
            }
          ]
        }
      ]
    }
  ]
}
```

**查看搜索调用次数**：开启联网搜索后，响应的 `usage.tool_usage.web_search_call` 字段返回本次响应触发的搜索调用次数，可用于用量统计和成本核算。

Chat API

Responses API

```json
{
  "usage": {
    "prompt_tokens": 1234,
    "completion_tokens": 56,
    "total_tokens": 1290,
    "completion_tokens_details": {
      "reasoning_tokens": 0
    },
    "tool_usage": {
      "web_search_call": 1
    }
  }
}
```

```json
{
  "usage": {
    "prompt_tokens": 1234,
    "completion_tokens": 56,
    "total_tokens": 1290,
    "output_tokens_details": {
      "reasoning_tokens": 0
    },
    "tool_usage": {
      "web_search_call": 1
    }
  }
}
```

## Chat 协议

### 快速开始

通过 Chat API（`/v1/chat/completions`）发起联网搜索请求。在请求中设置 `web_search_options.enable` 为 `true` 即可开启搜索。下例同时带上搜索版本、用户位置和思维链等常用参数，将 `YOUR_API_KEY` 替换为您创建的 API Key 后即可运行。

cURL

Python

Node.js

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/chat/completions' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
    "model": "hy3",
    "messages": [
      {"role": "user", "content": "今天深圳天气怎么样？"}
    ],
    "web_search_options": {
      "enable": true,
      "search_source": "lite",
      "user_location": {
        "type": "approximate",
        "country": "CN",
        "region": "Guangdong",
        "city": "Shenzhen",
        "timezone": "Asia/Shanghai"
      }
    },
    "reasoning_effort": "low"
  }'
```

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

response = client.chat.completions.create(
    model="hy3",
    messages=[{"role": "user", "content": "今天深圳天气怎么样？"}],
    reasoning_effort="low",
    extra_body={
        "web_search_options": {
            "enable": True,
            "search_source": "lite",
            "user_location": {
                "type": "approximate",
                "country": "CN",
                "region": "Guangdong",
                "city": "Shenzhen",
                "timezone": "Asia/Shanghai",
            },
        }
    },
)
print(response.choices[0].message.content)
```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "YOUR_API_KEY",
  baseURL: "https://tokenhub.tencentmaas.com/v1",
});

async function main() {
  const response = await client.chat.completions.create({
    model: "hy3",
    messages: [{ role: "user", content: "今天深圳天气怎么样？" }],
    reasoning_effort: "low",
    // @ts-ignore - web_search_options 为 TokenHub 扩展字段
    web_search_options: {
      enable: true,
      search_source: "lite",
      user_location: {
        type: "approximate",
        country: "CN",
        region: "Guangdong",
        city: "Shenzhen",
        timezone: "Asia/Shanghai",
      },
    },
  });
  console.log(response.choices[0].message.content);
}
main();
```

### 联网搜索参数

Chat API 的基础参数（如 `model`、`messages`、`stream`、`reasoning_effort`）请参见 [Chat Completions 协议字段说明 - 请求参数](https://cloud.tencent.com/document/product/1823/135872#075ff7fa-3ae8-468a-8eed-decbd322c0e1)。使用联网搜索时，仅需在请求体中增加 `web_search_options` 字段。

| 参数 | 类型 | 必选 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `enable` | Boolean | 是 | - | 固定为 `true`，表示开启联网搜索。 |
| `search_source` | String | 否 | 标准版 | 搜索版本。可选值：`lite`（轻量版）和 `standard`（标准版）。 |
| `user_location` | Object | 否 | - | 用户位置信息，模型可据此返回更贴近用户位置的搜索结果。结构包含 `type`（固定 `"approximate"`）、`country`、`region`、`city`、`timezone`。 |

### 响应中的搜索结果

Chat API 联网搜索的响应仍遵循 Chat Completions 格式。通用字段请参见 [Chat Completions 协议字段说明 - 返回参数](https://cloud.tencent.com/document/product/1823/135872#eba38663-9a7b-4d1e-b047-bcb63205d5d8)。开启联网搜索后，搜索引用来源通过 `choices[0].message.search_results` 返回。

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `index` | Integer | 引用序号，对应回答正文中的 `[1]`、`[2]` 标记。 |
| `url` | String | 来源网页的 URL。 |
| `name` | String | 来源网页的标题。 |
| `snippet` | String | 来源网页的摘要片段。 |
| `site` | String | 来源网站名称。 |

响应示例：

```json
{
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": "根据检索结果，模型生成的示例回答正文[1]。",
        "reasoning_content": "示例思维链内容。",
        "search_results": [
          {
            "index": 1,
            "url": "https://example.com/source/1",
            "name": "示例来源标题",
            "snippet": "示例来源摘要。",
            "site": "示例来源"
          }
        ]
      }
    }
  ],
  "usage": {
    "prompt_tokens": 1234,
    "completion_tokens": 56,
    "total_tokens": 1290,
    "completion_tokens_details": {
      "reasoning_tokens": 0
    },
    "tool_usage": {
      "web_search_call": 1
    }
  }
}
```

Chat API 会在 `usage.tool_usage.web_search_call` 中返回本次响应触发的搜索调用次数。

### 流式响应

设置 `stream: true` 时，Chat API 按 Chat Completions 流式格式返回内容增量：

`delta.content`：最终回答的流式增量文本。

`delta.reasoning_content`：思维链的流式增量文本。开启思维链时可能出现；部分模型默认开启思维链，默认策略请参见 [深度思考](https://cloud.tencent.com/document/product/1823/131208) 文档。

每条事件以 `data: {JSON}` 格式推送，末尾以 `data: [DONE]` 标记结束。

与 Responses API 不同，Chat API 流式响应不包含独立的搜索过程事件，搜索过程对客户端不可见。

## Responses 协议

### 快速开始

发起一次联网搜索请求。下例同时带上搜索版本、搜索上下文、用户位置和思维链等常用参数，将 `YOUR_API_KEY` 替换为您创建的 API Key 后即可运行。示例中 `model` 使用平台默认服务 ID `hy3`，若您使用自定义服务，请替换为对应的服务 ID。

cURL

Python

Node.js

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/responses' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
    "model": "hy3",
    "input": "今天深圳天气怎么样？",
    "tools": [{
      "type": "web_search",
      "search_source": "lite",
      "search_context_size": "medium",
      "user_location": {
        "type": "approximate",
        "country": "CN",
        "region": "Guangdong",
        "city": "Shenzhen",
        "timezone": "Asia/Shanghai"
      }
    }],
    "reasoning": {"effort": "medium"}
  }'
```

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com/v1",
)

response = client.responses.create(
    model="hy3",
    input="今天深圳天气怎么样？",
    tools=[{
        "type": "web_search",
        "search_source": "lite",
        "search_context_size": "medium",
        "user_location": {
            "type": "approximate",
            "country": "CN",
            "region": "Guangdong",
            "city": "Shenzhen",
            "timezone": "Asia/Shanghai",
        },
    }],
    reasoning={"effort": "medium"},
)
print(response.output_text)
```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "YOUR_API_KEY",
  baseURL: "https://tokenhub.tencentmaas.com/v1",
});

async function main() {
  const response = await client.responses.create({
    model: "hy3",
    input: "今天深圳天气怎么样？",
    tools: [{
      type: "web_search",
      search_source: "lite",
      search_context_size: "medium",
      user_location: {
        type: "approximate",
        country: "CN",
        region: "Guangdong",
        city: "Shenzhen",
        timezone: "Asia/Shanghai",
      },
    }],
    // @ts-ignore - reasoning 为 Responses API 扩展字段
    reasoning: { effort: "medium" },
  });
  console.log(response.output_text);
}
main();
```

### 联网搜索参数

Responses API 的基础参数请参见 OpenAI Responses API 相关说明。使用联网搜索时，在 `tools` 数组中声明 `web_search` 工具，并按需配置搜索参数。

| 参数 | 类型 | 必选 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `type` | String | 是 | - | 固定为 `"web_search"`。 |
| `search_source` | String | 否 | 标准版 | 搜索版本。可选值：`lite`（轻量版）和 `standard`（标准版）。 |
| `search_context_size` | String | 否 | `"medium"` | 每轮搜索注入模型的上下文体积。取值：`low` / `medium` / `high`。 |
| `user_location` | Object | 否 | - | 用户位置信息，结构包含 `type`（固定 `"approximate"`）、`country`、`region`、`city`、`timezone`。 |

`search_context_size` 控制的是每轮搜索注入上下文的体积，并非搜索调用轮数。实际搜索调用次数由模型根据问题复杂度自主决定。

#### 思维链参数说明

联网搜索可与思维链组合使用。如需调整思维链（设置推理强度、关闭思维链、获取思维链摘要等），请参见 [深度思考](https://cloud.tencent.com/document/product/1823/131208) 文档。

### 响应中的搜索结果

Responses API 的 `output` 数组中可能包含以下与联网搜索相关的项：

| 类型 | 说明 |
| --- | --- |
| `web_search_call` | 一次搜索工具调用。可通过其中的 `action.query` 查看模型生成的搜索词。 |
| `message` | 模型生成的最终回答。引用来源通过 `content[].annotations` 返回。 |
| `reasoning` | 思维链产物。当请求启用思维链或模型默认策略返回思维链内容时，可能出现该类型项。如不希望返回思维链内容，请显式设置 `reasoning.effort` 为 `none`。 |

`message.content[].annotations` 中的引用字段如下：

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `type` | String | 固定为 `"url_citation"`。 |
| `index` | Integer | 引用序号，对应回答文本中的 `[1]`、`[2]` 标记。 |
| `url` | String | 来源网页的 URL。 |
| `title` | String | 来源网页的标题。 |
| `start_index` | Integer | 引用标记在文本中的起始位置。 |
| `end_index` | Integer | 引用标记在文本中的结束位置。 |

Responses API 会在 `usage.tool_usage.web_search_call` 中返回本次响应触发的搜索调用次数。

响应示例：

```json
{
  "output": [
    {
      "type": "web_search_call",
      "status": "completed",
      "action": {
        "type": "search",
        "query": "深圳 今日 天气"
      }
    },
    {
      "type": "message",
      "role": "assistant",
      "content": [
        {
          "type": "output_text",
          "text": "根据检索结果，模型生成的示例回答正文[1]。",
          "annotations": [
            {
              "type": "url_citation",
              "index": 1,
              "url": "https://example.com/source/1",
              "title": "示例来源标题",
              "start_index": 18,
              "end_index": 21
            }
          ]
        }
      ]
    }
  ],
  "usage": {
    "tool_usage": {
      "web_search_call": 1
    }
  }
}
```

### 流式响应

设置 `stream: true` 时，Responses API 通过 SSE 返回联网搜索过程和回答生成过程。与联网搜索相关的关键事件包括：

| 事件 | 含义 |
| --- | --- |
| `response.web_search_call.in_progress` | 搜索调用启动。 |
| `response.web_search_call.searching` | 正在执行搜索。 |
| `response.web_search_call.completed` | 搜索调用完成。 |
| `response.reasoning_summary_text.delta` | 思维链摘要的流式增量。当请求启用思维链并返回思维链摘要时可能出现；若 `reasoning.effort` 为 `none`，则不会返回该事件。 |
| `response.output_text.delta` | 最终回答的文本流式增量。 |
| `response.completed` | 响应整体完成，事件中的 `response` 字段包含完整 `output` 与 `usage`。 |

## Message 协议

### 快速开始

通过 Message API（`/v1/messages`）发起联网搜索请求，在请求中通过 `tools` 字段声明联网搜索工具即可开启搜索。将 `YOUR_API_KEY` 替换为您创建的 API Key 后即可运行。

cURL

Python

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/messages' \\
  -H 'x-api-key: YOUR_API_KEY' \\
  -H 'anthropic-version: 2023-06-01' \\
  -H 'Content-Type: application/json' \\
  -d '{
    "model": "deepseek-v4-pro",
    "max_tokens": 4096,
    "messages": [
      {"role": "user", "content": "最近一周有哪些重要的 AI 行业新闻？请附来源链接。"}
    ],
    "tools": [
      {"type": "web_search_20250305", "name": "web_search"}
    ]
  }'
```

```python
from anthropic import Anthropic

client = Anthropic(
    api_key="YOUR_API_KEY",
    base_url="https://tokenhub.tencentmaas.com",
)

response = client.messages.create(
    model="deepseek-v4-pro",
    max_tokens=4096,
    messages=[{"role": "user", "content": "最近一周有哪些重要的 AI 行业新闻？请附来源链接。"}],
    tools=[{"type": "web_search_20250305", "name": "web_search"}],
)
print(response.content)
```

### 联网搜索参数

Message API 通过 `tools` 字段声明联网搜索工具，工具类型为 `web_search_20250305`：

```json
{
  "tools": [
    {
      "type": "web_search_20250305",
      "name": "web_search"
    }
  ]
}
```

Message API 使用 `web_search_20250305` 工具类型，与 Responses API 的 `web_search` 工具类型不同，两者不可混用。

### 响应中的搜索结果

Message API 的搜索结果通过 `content` 数组中的内容块返回：

`server_tool_use`：一次服务端搜索调用，`input.query` 为模型生成的搜索词。

`web_search_tool_result`：搜索结果块，`content` 数组中的 `web_search_result` 对象包含来源信息。

`text`：最终回答，正文以 `[N]` 数字标记引用来源，`N` 对应 `web_search_result` 的顺序。

响应示例：

```json
{
  "id": "msg_7e34a0bf-e8fd-49b9-84c0-2da85c623800",
  "type": "message",
  "role": "assistant",
  "model": "deepseek-v4-pro",
  "content": [
    {
      "type": "server_tool_use",
      "id": "srvtoolu_c447e5f6a5fded34_33",
      "name": "web_search",
      "input": {"query": "AI 行业新闻 2026年11月"}
    },
    {
      "type": "web_search_tool_result",
      "content": [
        {
          "type": "web_search_result",
          "url": "https://example.com/source/1",
          "title": "示例来源标题",
          "page_age": "2026/11/16 16:49:10",
          "encrypted_content": "",
          "snippet": "示例来源摘要。"
        }
      ]
    },
    {
      "type": "text",
      "text": "根据检索结果，模型生成的示例回答正文[1]。"
    }
  ],
  "stop_reason": "end_turn",
  "usage": {
    "input_tokens": 6256,
    "output_tokens": 246,
    "cache_read_input_tokens": 5120,
    "server_tool_use": {
      "web_search_requests": 3
    }
  }
}
```

Message API 会在 `usage.server_tool_use.web_search_requests` 中返回本次响应触发的搜索调用次数。

### 流式响应

设置 `stream: true` 时，Message API 按 Anthropic Messages 流式格式返回内容增量：

`message_start`：消息开始，携带消息元数据。

`content_block_start`：内容块开始，`content_block` 字段标识 `server_tool_use`、`web_search_tool_result` 或 `text` 块。

`content_block_delta`：内容块增量，`delta.type` 为 `input_json_delta`（搜索词增量）或 `text_delta`（文本增量）。

`content_block_stop`：内容块结束。

`message_delta`：消息增量。

`message_stop`：消息整体结束。

## 错误处理

| 错误场景 | 行为 |
| --- | --- |
| 搜索引擎超时 | 模型使用已有知识回答，不包含搜索结果 |
| 搜索结果为空 | 模型正常回答，回答中不附带引用来源（Responses API 中 `annotations` 为空，Chat API 中不返回 `search_results`） |
| 模型判断无需搜索 | 直接回答，不触发搜索调用（Responses API 的 `output` 中不包含 `web_search_call`，Chat API 的 `message` 中不包含 `search_results`） |

## 相关文档

[语言模型调用概览](https://cloud.tencent.com/document/product/1823/130079)：TokenHub 语言模型通用调用文档（含 BaseURL、协议支持矩阵等），各协议完整字段说明请参见 [Chat Completions 协议字段说明](https://cloud.tencent.com/document/product/1823/135872) 和 [Response 协议字段说明](https://cloud.tencent.com/document/product/1823/135873)。

[深度思考](https://cloud.tencent.com/document/product/1823/131208)：思维链（深度思考）能力的参数说明与默认策略。

[API Key 管理](https://cloud.tencent.com/document/product/1823/130090)：API Key 创建与管理指南。

[模型体验-语言模型](https://console.cloud.tencent.com/tokenhub/text)：快速体验联网搜索效果。

[模型价格](https://cloud.tencent.com/document/product/1823/130055#b8d8c1d9-2f6d-4f3f-9389-e6b14efb770c)：查看联网搜索轻量版和标准版价格。
