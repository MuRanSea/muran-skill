<!-- Official source: https://platform.minimax.cn/docs/guides/server-tools.md -->
<!-- Source SHA-256: 0809d50dcc1120d667ffb890dd283fdde58ebad3f1e2e1be4ab3b858cce1b676 -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.minimaxi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 服务端工具（Server Tools）

## 什么是服务端工具

**服务端工具（Server Tools）** 是由 MiniMax 在服务端托管并自动执行的内置工具。与传统的 Function Call（客户端工具）不同，你无需自行实现工具的执行逻辑，也无需在多轮对话中手动回传工具结果——模型在生成回复的过程中会自动调用这些工具、获取结果并继续生成，整个流程在一次 API 请求内完成。

> [!NOTE]
>
> 该能力目前处于 **Beta** 阶段，功能与参数可能会调整。

> **客户端工具（Function Call）**
>
> 模型返回 `tool_use`，由**你的代码**执行，再把 `tool_result` 回传给模型。需要多轮交互。

> **服务端工具（Server Tools）**
>
> 模型在 MiniMax **服务端**自动执行工具并获取结果，**一次请求**内完成，你只需读取最终回复。

## 支持范围

| 能力 | 支持状态 |
| :- | :- |
| 接口 | **Anthropic Messages API**（`/anthropic/v1/messages`） **OpenAI Responses API**（`/v1/responses`） |
| 可用工具 | `web_search`（联网搜索） |
| 调用方式 | 在请求的 `tools` 数组中声明服务端工具 |

## web\_search

`web_search` 让模型在生成回复时自动进行联网搜索，获取实时信息，并基于搜索结果作答。适用于时效性强、需要最新事实的问题（如新闻、行情、文档查询等）。

### 声明工具

根据接口格式在 `tools` 数组中声明 `web_search`：

**Anthropic Messages API**

```json theme={null}
{
  "type": "web_search_20250305",
  "name": "web_search"
}
```

**OpenAI Responses API**

```json theme={null}
{
  "type": "web_search"
}
```

> [!NOTE]
>
> Anthropic Messages API 使用版本化类型标识 `web_search_20250305`；OpenAI Responses API 使用工具类型 `web_search`。请根据所调用的接口选择对应格式。

### 调用示例

**Anthropic Messages API**

```bash cURL theme={null}
curl https://api.minimax.cn/anthropic/v1/messages \
  -H "Content-Type: application/json" \
  -H "x-api-key: ${MINIMAX_API_KEY}" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "MiniMax-M3.1-Flash",
    "max_tokens": 8192,
    "messages": [
      {
        "role": "user",
        "content": "帮我搜一下今天上海的天气"
      }
    ],
    "tools": [
      {
        "type": "web_search_20250305",
        "name": "web_search"
      }
    ]
  }'
```

**OpenAI Responses API**

```bash cURL theme={null}
curl --location 'https://api.minimax.cn/v1/responses' \
  --header "Authorization: Bearer ${MINIMAX_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "MiniMax-M3.1-Flash",
    "input": "帮我搜一下今天上海的天气",
    "tools": [
      {
        "type": "web_search"
      }
    ]
  }'
```

### 响应说明

#### Anthropic Messages API

启用 `web_search` 后，模型会在服务端自动执行搜索并将结果用于生成最终回复。你无需处理 `tool_use` / `tool_result` 的多轮回传，直接读取 `message.content` 中的 `text` 内容块即可获取答案。

`message.content` 会按模型的执行顺序返回多个内容块，一次完整的搜索问答通常包含以下类型：

| 内容块类型 | 说明 |
| :- | :- |
| `thinking` | 模型的思考内容，模型按需生成，可能出现在搜索前后 |
| `text` | 模型生成的文本。搜索前的引导语与搜索后的最终答案都属于此类型 |
| `server_tool_use` | 模型在服务端发起的工具调用，`name` 为 `web_search`，`input.query` 为实际检索的关键词 |
| `web_search_tool_result` | 服务端返回的搜索结果，`content` 为 `web_search_result` 列表，含 `title`、`url`、`page_age`、`content` 等字段 |

若一次请求中模型发起的搜索次数达到上限，响应会以 `stop_reason: "pause_turn"` 结束，此时没有最终答案。将本次返回的 `content` 作为 assistant 消息原样追加到 `messages` 后再次请求，模型会继续执行并给出回复。

> **完整响应示例**
>
> ```json theme={null}
> {
>     "id": "0722ab84a6341c026ba2a809efbfcf30",
>     "type": "message",
>     "role": "assistant",
>     "model": "MiniMax-M3.1-Flash",
>     "content": [
>         {
>             "thinking": "The user wants today's weather in Shanghai. I should use web search to find this. Let me search.\n\nNote: I don't have a real-time weather tool, but I have web search. Let me do the search. I should also consider searching in Chinese.\n\nLet me make multiple independent searches in one block.",
>             "signature": "7dd59de84e48f8a88b349037988d5db9c1f6943fc7143fd3092a0e4c79d59d8b",
>             "type": "thinking"
>         },
>         {
>             "text": "我来帮你搜索一下今天上海的天气。",
>             "type": "text"
>         },
>         {
>             "type": "server_tool_use",
>             "id": "call_function_gznzlqvp7j32_1",
>             "name": "web_search",
>             "input": {
>                 "query": "上海今天天气预报"
>             }
>         },
>         {
>             "type": "web_search_tool_result",
>             "tool_use_id": "call_function_gznzlqvp7j32_1",
>             "content": [
>                 {
>                     "type": "web_search_result",
>                     "title": "上海24小时天气",
>                     "url": "https://beijing.tianqi.com/shanghai/today/",
>                     "page_age": "2026/10/17 20:00:15",
>                     "content": "上海24小时天气 天气网北京站。上海天气 [切换城市] 25℃ 晴22 ~ 28℃ 空气质量:优湿度:69%风向:东南风 2级紫外线:无日出: 05:58日落: 17:20 上海一周天气 上海10天天气 上海15天天气 上海30天天气 晴 多云 多云 多云 多云 多云 阴 多云 25 25 24 24 24 24 24……"
>                 },
>                 /// ...
>             ]
>         },
>         {
>             "type": "server_tool_use",
>             "id": "call_function_gznzlqvp7j32_2",
>             "name": "web_search",
>             "input": {
>                 "query": "上海 今日天气 实时 气温"
>             }
>         },
>         {
>             "type": "web_search_tool_result",
>             "tool_use_id": "call_function_gznzlqvp7j32_2",
>             "content": [
>                 {
>                     "type": "web_search_result",
>                     "title": "周末最高31,上海大歌剧院今正式启幕;上海东站､上海宝山站预计明年投用",
>                     "url": "https://www.toutiao.com/article/7697404067781296659/",
>                     "page_age": "2026/10/17 06:59:24",
>                     "content": "发布时间:2026年10月17日。2026-10-1706:59·上观新闻上海今天多云到阴,东南风4~5级,沿江沿海地区阵风有6级,今天上午转4~5级阵风6级,沿江沿海地区5级阵风6~7级。今天最高气温28℃,最低气温22℃。相对湿度90%~45%。周日的最高气温可达31℃。周日夜里到下周一上海转受冷空气影响,将有一次……"
>                 },
>                 /// ...
>             ]
>         },
>         {
>             "thinking": "The search results indicate the current date appears to be 2026/10/17 (Saturday). Let me summarize today's weather in Shanghai.\n\nToday (Oct 17, Saturday): 多云到阴 (cloudy to overcast), 22-28/29°C, southeast wind 4-5 with gusts 6, humidity 90%-45%, feels warm and humid. Xujiahui station 21.9°C in the morning, max ~29°C.\n\nLet me present it clearly. I should note data is from 上海市气象台.",
>             "signature": "a0a55f6614593651f36378bbed6adafe841d20afb4f82631424cbc13e2e2ee46",
>             "type": "thinking"
>         },
>         {
>             "text": "今天（**10月17日 星期六**）上海天气如下：\n\n## 今日天气\n| 项目 | 情况 |\n|---|---|\n| 天气 | 多云到阴，局部有短时小雨，阳光偶有露脸 |\n| 气温 | 最低 **22℃** ~ 最高 **28~29℃**（徐家汇站最高 29℃ 上下） |\n| 风力 | 东南风 4~5 级，阵风 6 级；沿江沿海地区 5 级阵风 6~7 级 |\n| 湿度 | 90%~45%，体感偏暖湿 |\n| 空气质量 | 优 |\n\n**实况**：早晨全市起步气温 19~22℃，徐家汇站 21.9℃，白天阳光不错，适合抓紧洗晒；午后暖湿感明显。\n\n## 出行建议\n- 建议带把伞（局部短时小雨 + 阵风较大）\n- 穿短袖/薄外套即可，但**随身备一件薄外套**，昼夜温差体感较大\n- 风大，注意骑车、走高架桥时安全\n\n## 未来几天趋势（重点提醒）\n- **明天（10/18 周日）**：多云到阴转阴到多云，**24℃~31℃**，午后有阵雨或雷雨。31℃ 在历史同期不多见，体感潮湿闷热\n- **周一（10/19）**：受冷空气影响，有明显降水过程，**可能伴雷电**，最高降至 25℃\n- **周二（10/20）**：阴到多云有时有阵雨，22℃~27℃\n- **周三（10/21）**：多云到阴，**17℃~22℃**，最低跌至\"1字头\"，早晚明显凉意\n\n👉 未来十天冷暖交替频繁、气温起伏较大，建议随时关注临近预报、及时增减衣物。（数据来源：上海市气象台/上海天气发布、中央气象台）",
>             "type": "text"
>         }
>     ],
>     "usage": {
>         "input_tokens": 10563,
>         "output_tokens": 647,
>         "cache_creation_input_tokens": 0,
>         "cache_read_input_tokens": 904,
>         "output_tokens_details": {
>             "thinking_tokens": 179
>         }
>     },
>     "stop_reason": "end_turn",
>     "base_resp": {
>         "status_code": 0,
>         "status_msg": ""
>     }
> }
> ```

#### OpenAI Responses API

启用 `web_search` 后，服务端会在一次请求内完成搜索和回复生成，无需回传工具结果。响应的 `output` 数组包含搜索调用和模型回复，直接读取顶层 `output_text` 即可获取最终答案。

| 字段或输出项 | 说明 |
| :- | :- |
| `reasoning` | 模型的思考内容，模型按需生成，可能出现在搜索前后 |
| `web_search_call` | 服务端执行的联网搜索调用，包含调用 ID、执行状态和 `action.query` 实际检索词 |
| `message` | 模型生成的文本，文本位于 `content` 中。搜索前的引导语与搜索后的最终答案都属于此类型 |
| `output_text` | 聚合后的最终文本，可直接读取 |

> **Responses API 响应示例**
>
> ```json theme={null}
> {
>     "id": "0722aabe22b03a2b97547a5ef5e9f5d3",
>     "object": "response",
>     "created_at": 1792243646,
>     "model": "MiniMax-M3.1-Flash",
>     "status": "completed",
>     "output": [
>         {
>             "id": "0722aabe22b03a2b97547a5ef5e9f5d3_rs",
>             "type": "reasoning",
>             "status": "completed",
>             "summary": [],
>             "content": [
>                 {
>                     "type": "reasoning_text",
>                     "text": "The user wants today's weather in Shanghai. I should use web search to find this. Let me search.\n\nLet me do a search for \"上海天气\" and also maybe \"上海天气预报 今天\".\n\nThe current date - I need to know today's date. Let me search and see.\n\nI'll make multiple independent calls in one block."
>                 }
>             ]
>         },
>         {
>             "id": "0722aabe22b03a2b97547a5ef5e9f5d3_msg",
>             "type": "message",
>             "status": "completed",
>             "role": "assistant",
>             "content": [
>                 {
>                     "type": "output_text",
>                     "text": "我来帮你搜索一下上海今天的天气。",
>                     "annotations": []
>                 }
>             ]
>         },
>         {
>             "id": "call_function_87l4jam0b0kj_1",
>             "type": "web_search_call",
>             "status": "completed",
>             "action": {
>                 "type": "search",
>                 "query": "上海天气预报 今天"
>             }
>         },
>         {
>             "id": "call_function_87l4jam0b0kj_2",
>             "type": "web_search_call",
>             "status": "completed",
>             "action": {
>                 "type": "search",
>                 "query": "上海 今日天气 气温 实时"
>             }
>         },
>         {
>             "id": "0722aabe22b03a2b97547a5ef5e9f5d3_rs_r1",
>             "type": "reasoning",
>             "status": "completed",
>             "summary": [],
>             "content": [
>                 {
>                     "type": "reasoning_text",
>                     "text": "The search results indicate today is 2026-10-17 (Saturday). Let me synthesize. The official 上海市气象台 forecast for today (10/17): 多云到阴, 东南风4~5级, 沿江沿海地区阵风有6级, 最高气温28℃, 最低气温22℃, 相对湿度90%~45%.\n\nSome sources mention 最高29℃ (新闻坊). 中国天气网: 阴 28/23℃. Let me present the main official forecast.\n\nLet me give a summary with today, tomorrow, and the week's trend.\n\nShould I do another search to confirm? The results are pretty consistent. Let me present it.\n\nNote: the date seems to be 2026-10-17. Let me present the info.\n\nI might do one more search for the most recent/current conditions, but the data seems sufficient. Let me just answer.\n\nActually, let me consider doing one more search to verify the most up-to-date hourly/real-time info. The search results include data updated 18:00 from 中国天气网 for 16日, and various 10/17 reports. I think that's enough. Let me answer."
>                 }
>             ]
>         },
>         {
>             "id": "0722aabe22b03a2b97547a5ef5e9f5d3_msg_r1",
>             "type": "message",
>             "status": "completed",
>             "role": "assistant",
>             "content": [
>                 {
>                     "type": "output_text",
>                     "text": "## 上海今日天气（2026年10月17日 星期六）\n\n**实况 / 今日预报**\n- **天气**：多云到阴，局部有短时小雨，阳光偶尔露脸\n- **气温**：22℃ ~ 28℃（部分媒体援引市气象台\"今日最高29℃左右\"；中国天气网城区预报为 28/23℃）\n- **早晨实况**：全市起步气温 19~22℃，徐家汇站 21.9℃；午后体感偏暖湿\n- **风力**：东南风 4~5 级，阵风 6 级，沿江沿海地区 5~6 级、阵风 6~7 级\n- **湿度**：90%~45%\n- **体感**：暖湿，午后偏闷；建议短袖 + 薄外套，风大注意防风，外出带把伞更稳妥\n\n**未来几天趋势（上海市气象台）**\n| 日期 | 天气 | 气温 |\n|---|---|---|\n| 10/18 周日 | 多云到阴转阴到多云，有时有阵雨或雷雨 | 24~31℃ |\n| 10/19 周一 | 阴到多云，有时有阵雨 | 21~25℃ |\n| 10/20 周二 | 阴到多云，有时有阵雨 | 22~27℃ |\n| 10/21 周三 | 多云到阴 | 17~22℃ |\n\n**几点提醒**\n1. **周日下午是转折点**：冷暖空气交汇，可能出现雷雨，气温随后明显回落。\n2. **周日 31℃ 属历史同期少见**（1872 年建站以来，10 月中旬日最高气温很少超 30℃，仅 11 天达到或超过）。\n3. **下周三前后最低气温跌到\"1 字头\"**，早晚凉意明显，衣物要能灵活增减。\n4. **台风\"蔷琵\"**（今年第 30 号）已在 16 日加强为强热带风暴/台风级，位于西北太平洋，未来 5 天对我国海区无直接影响，但是否奔我国要等 21~22 日形势明朗。\n5. 未来十天冷暖更替频繁，建议出门前再看一眼临近预报。\n\n（数据来源：上海市气象台/上海发布、中国天气网、上观新闻、新闻坊；不同来源对今日最高气温有 28℃/29℃ 的小幅差异，以实时观测为准。）",
>                     "annotations": [
>                         {
>                             "type": "url_citation",
>                             "title": "准备冲29度!",
>                             "url": "https://www.shhuangpu.gov.cn/xw/001015/20261013/ee809b0f-9ba2-48d4-8a3b-91897fc736e1.html",
>                             "start_index": 0,
>                             "end_index": 0,
>                             "content": "准备冲29度! 上海市黄浦区人民政府。今日回顾 今天空气里依旧弥漫着甜甜的桂花香,阳光上线,幸福感拉满~白天气温上升迅速,最高气温在26~28℃之间,市区徐家汇站26.9℃,空气不算干燥,体感较舒适。 今夜至明日天气 今天夜间到明天中东部降雨稀少。上海明天延续多云的好天气,但今天夜间稍有变化👇👇👇 01 具体预报 今天……"
>                         },
>                         /// ...
>                     ]
>                 }
>             ]
>         }
>     ],
>     "output_text": "我来帮你搜索一下上海今天的天气。## 上海今日天气（2026年10月17日 星期六）\n\n**实况 / 今日预报**\n- **天气**：多云到阴，局部有短时小雨，阳光偶尔露脸\n- **气温**：22℃ ~ 28℃（部分媒体援引市气象台\"今日最高29℃左右\"；中国天气网城区预报为 28/23℃）\n- **早晨实况**：全市起步气温 19~22℃，徐家汇站 21.9℃；午后体感偏暖湿\n- **风力**：东南风 4~5 级，阵风 6 级，沿江沿海地区 5~6 级、阵风 6~7 级\n- **湿度**：90%~45%\n- **体感**：暖湿，午后偏闷；建议短袖 + 薄外套，风大注意防风，外出带把伞更稳妥\n\n**未来几天趋势（上海市气象台）**\n| 日期 | 天气 | 气温 |\n|---|---|---|\n| 10/18 周日 | 多云到阴转阴到多云，有时有阵雨或雷雨 | 24~31℃ |\n| 10/19 周一 | 阴到多云，有时有阵雨 | 21~25℃ |\n| 10/20 周二 | 阴到多云，有时有阵雨 | 22~27℃ |\n| 10/21 周三 | 多云到阴 | 17~22℃ |\n\n**几点提醒**\n1. **周日下午是转折点**：冷暖空气交汇，可能出现雷雨，气温随后明显回落。\n2. **周日 31℃ 属历史同期少见**（1872 年建站以来，10 月中旬日最高气温很少超 30℃，仅 11 天达到或超过）。\n3. **下周三前后最低气温跌到\"1 字头\"**，早晚凉意明显，衣物要能灵活增减。\n4. **台风\"蔷琵\"**（今年第 30 号）已在 16 日加强为强热带风暴/台风级，位于西北太平洋，未来 5 天对我国海区无直接影响，但是否奔我国要等 21~22 日形势明朗。\n5. 未来十天冷暖更替频繁，建议出门前再看一眼临近预报。\n\n（数据来源：上海市气象台/上海发布、中国天气网、上观新闻、新闻坊；不同来源对今日最高气温有 28℃/29℃ 的小幅差异，以实时观测为准。）",
>     "usage": {
>         "input_tokens": 10485,
>         "output_tokens": 886,
>         "total_tokens": 11371,
>         "input_tokens_details": {
>             "cached_tokens": 905
>         },
>         "output_tokens_details": {
>             "reasoning_tokens": 313
>         }
>     },
>     "error": null,
>     "incomplete_details": null,
>     "instructions": null,
>     "metadata": {},
>     "tools": [
>         {
>             "type": "web_search",
>             "name": "",
>             "parameters": null
>         }
>     ],
>     "tool_choice": "auto",
>     "temperature": 1,
>     "top_p": 0.95,
>     "text": {
>         "format": {
>             "type": "text"
>         }
>     },
>     "reasoning": {
>         "effort": null,
>         "summary": null
>     },
>     "max_output_tokens": null,
>     "parallel_tool_calls": true,
>     "previous_response_id": null,
>     "conversation": null,
>     "store": false,
>     "safety_identifier": null,
>     "truncation": "disabled"
> }
> ```

> [!TIP]
>
> 搜索行为完全在服务端完成，因此单次请求的耗时可能比不启用工具时更长，请合理设置客户端超时时间。

## 注意事项

1. 服务端工具处于 **Beta** 阶段，行为与参数可能随时调整。
2. 目前服务端工具仅提供 `web_search`，支持通过 **Anthropic Messages API** 和 **OpenAI Responses API** 调用。
3. Anthropic Messages API 的 Base URL 为 `https://api.minimax.cn/anthropic`；OpenAI Responses API 的端点为 `https://api.minimax.cn/v1/responses`。接口详情分别参见 [Anthropic SDK](https://platform.minimaxi.com/docs/api-reference/text-anthropic-api.md) 和 [Responses API](https://platform.minimaxi.com/docs/api-reference/responses-create.md)。

如在使用过程中遇到问题，可通过邮箱 [Model@minimax.io](mailto:Model@minimax.io) 联系我们的技术支持团队。
