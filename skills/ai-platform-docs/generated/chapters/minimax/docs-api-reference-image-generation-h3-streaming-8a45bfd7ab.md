<!-- Official source: https://platform.minimax.cn/docs/api-reference/image-generation-h3-streaming.md -->
<!-- Source SHA-256: ab89b6e80f3c42bd5a06148a8d8ca60d55c64b156ea168d82fb92238d58dc6b8 -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.minimaxi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 流式响应事件

> MiniMax-H3-Image 文生图与图片编辑接口在 `stream: true` 时推送的 Server-Sent Events（SSE）事件说明。

[文生图](https://platform.minimaxi.com/docs/api-reference/image-generation-h3-generations.md)与[图片编辑](https://platform.minimaxi.com/docs/api-reference/image-generation-h3-edits.md)接口设置 `stream: true` 后，以 SSE 逐张推送结果，全部结束后推送汇总事件。

* 仅支持 `response_format: "url"`
* 推送顺序为完成顺序，请用 `image_index` 区分
* 响应头返回前的错误（参数错误、鉴权失败、限流、余额不足等）直接返回 HTTP 错误，与非流式相同；之后的错误以 `error` 事件返回，`error.http_code` 与非流式的 HTTP 状态码一致
* 等待期间每 15 秒推送一行 SSE 注释 `: keepalive` 保活，可直接忽略；响应头最晚随第一行保活（约 15 秒）返回
* 流以 `completed` 或 `error` 结束，两者均携带 `usage` 与 `request_id`

## 事件类型

两个接口的事件结构相同，仅 `type` 前缀不同：

| 事件 | 文生图（`/v1/images/generations`） | 图片编辑（`/v1/images/edits`） |
| - | - | - |
| 单张成功 | `image_generation.partial_succeeded` | `image_edit.partial_succeeded` |
| 单张失败 | `image_generation.partial_failed` | `image_edit.partial_failed` |
| 全部结束 | `image_generation.completed` | `image_edit.completed` |
| 整体失败 | `error` | `error` |

每个事件由 `event:` 行与 `data:` 行组成，`data` 为 JSON，事件之间以空行分隔：

```text theme={null}
event: image_generation.partial_succeeded
data: {"type":"image_generation.partial_succeeded", ...}

```

### partial\_succeeded

单张图片生成成功。每成功一张推送一次。

**type** `string` *required*

事件类型：`image_generation.partial_succeeded` 或 `image_edit.partial_succeeded`。

**created** `integer`

事件产生时的 Unix 时间戳（秒）。

**model** `string`

模型名称。

**image\_index** `integer` *required*

图片序号，从 0 开始，取值范围 \[0, n-1]。

**url** `string` *required*

图片链接，有效期 24 小时。

**size** `string`

图片的实际尺寸，格式为 `宽x高`。

**output\_format** `string`

图片格式：`png`、`jpeg` 或 `webp`。

**revised\_prompt** `string`

实际用于生成该图片的 prompt。开启 prompt 增强时为增强后的结果，关闭时与请求中的 `prompt` 相同。

```json 示例 theme={null}
{
  "type": "image_generation.partial_succeeded",
  "created": 1792308690,
  "model": "MiniMax-H3-Image",
  "image_index": 1,
  "url": "https://example.com/h3-image/output-1.jpg",
  "size": "2720x1536",
  "output_format": "jpeg",
  "revised_prompt": "一只橘猫蜷在洒满阳光的窗台上打盹，窗外是模糊的城市街景，暖色调，胶片质感"
}
```

### partial\_failed

单张图片生成失败或未通过内容安全检查。其它图片不受影响，会继续推送。

**type** `string` *required*

事件类型：`image_generation.partial_failed` 或 `image_edit.partial_failed`。

**created** `integer`

事件产生时的 Unix 时间戳（秒）。

**model** `string`

模型名称。

**image\_index** `integer` *required*

图片序号，从 0 开始。

**code** `string` *required*

内部错误码，如 `1026`，可查看[错误码查询列表](https://platform.minimaxi.com/docs/api-reference/errorcode.md)。

**message** `string` *required*

错误详情。

```json 示例 theme={null}
{
  "type": "image_generation.partial_failed",
  "created": 1792308691,
  "model": "MiniMax-H3-Image",
  "image_index": 2,
  "code": "1027",
  "message": "output image failed content safety check"
}
```

### completed

所有图片处理完毕且至少一张成功时推送，是流中的最后一个事件，携带本次请求的用量与统计。

**type** `string` *required*

事件类型：`image_generation.completed` 或 `image_edit.completed`。

**created** `integer`

事件产生时的 Unix 时间戳（秒）。

**model** `string`

模型名称。

**usage** `object`

本次请求的 token 用量，用于计费。

**属性**

**generated\_images** `integer`

成功生成的图片数量，不含生成失败或未通过内容安全检查的图片。

**total\_tokens** `integer`

总 token 数。

**input\_tokens** `integer`

输入 token 数（文本与参考图）。

**output\_tokens** `integer`

输出 token 数（生成的图片）。

**input\_tokens\_details** `object`

输入 token 明细：`text_tokens`（文本）、`image_tokens`（参考图）。

**output\_tokens\_details** `object`

输出 token 明细：`image_tokens`（生成的图片）。

**request\_id** `string`

请求追踪 ID，便于排查问题。

```json 示例 theme={null}
{
  "type": "image_generation.completed",
  "created": 1792308695,
  "model": "MiniMax-H3-Image",
  "usage": {
    "generated_images": 2,
    "total_tokens": 13022,
    "input_tokens": 4862,
    "output_tokens": 8160,
    "input_tokens_details": {"text_tokens": 4862, "image_tokens": 0},
    "output_tokens_details": {"image_tokens": 8160}
  },
  "request_id": "021792308678142a2c883cf675b9804d"
}
```

### error

本次请求的顶层错误，推送后流结束。只在一张图片都没有生成成功时推送，不计费，`usage` 各项均为 0：

* 提交生成后全部失败：在全部 `n` 个 `partial_failed` 事件之后推送。所有图片都未通过内容安全检查时 `error.http_code` 为 `422`，全部因余额不足失败时为 `402`，否则为 `500`
* 提交生成前请求整体失败（如输入未通过内容安全检查、参考图处理失败），且响应头已经返回：`error` 字段与非流式请求 HTTP 错误响应中的 `error` 相同

`error` 事件不含 `created` 和 `data`，每张图的失败原因见此前推送的 `partial_failed` 事件。

**type** `string` *required*

固定为 `error`。

**error** `object` *required*

错误信息。

**属性**

**type** `string`

错误类型，如 `server_error`。

**message** `string`

错误详情，结尾括号内为内部错误码。

**http\_code** `string`

对应的 HTTP 状态码字符串。

**usage** `object`

本次请求的 token 用量，结构与 `completed` 事件的 `usage` 相同，各项均为 0。

**request\_id** `string`

请求追踪 ID，便于排查问题。

```json 示例 theme={null}
{
  "type": "error",
  "error": {
    "type": "server_error",
    "message": "internal error (1000)",
    "http_code": "500"
  },
  "usage": {
    "generated_images": 0,
    "total_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0,
    "input_tokens_details": {"text_tokens": 0, "image_tokens": 0},
    "output_tokens_details": {"image_tokens": 0}
  },
  "request_id": "021792308678142a2c883cf675b9804d"
}
```

## 完整示例

以 `n: 3`、`stream: true` 为例，其中第 3 张（`image_index` 为 2）未通过内容安全检查：

```bash 请求（文生图） theme={null}
curl https://api.minimax.cn/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $MINIMAX_API_KEY" \
  --no-buffer \
  -d '{
    "model": "MiniMax-H3-Image",
    "prompt": "一只橘猫趴在窗台上晒太阳，午后暖光，胶片质感",
    "size": "2720x1536",
    "n": 3,
    "stream": true
  }'
```

```bash 请求（图片编辑） theme={null}
curl https://api.minimax.cn/v1/images/edits \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $MINIMAX_API_KEY" \
  --no-buffer \
  -d '{
    "model": "MiniMax-H3-Image",
    "prompt": "把图1里的猫换成图2里的柴犬，保持背景不变",
    "images": [
      {"image_url": "https://example.com/cat.jpg"},
      {"image_url": "https://example.com/dog.png"}
    ],
    "n": 3,
    "stream": true
  }'
```

```text 响应（文生图） theme={null}
event: image_generation.partial_succeeded
data: {"type":"image_generation.partial_succeeded","created":1792308690,"model":"MiniMax-H3-Image","image_index":1,"url":"https://example.com/h3-image/output-1.jpg","size":"2720x1536","output_format":"jpeg","revised_prompt":"一只橘猫蜷在洒满阳光的窗台上打盹，窗外是模糊的城市街景，暖色调，胶片质感"}

event: image_generation.partial_failed
data: {"type":"image_generation.partial_failed","created":1792308691,"model":"MiniMax-H3-Image","image_index":2,"code":"1027","message":"output image failed content safety check"}

event: image_generation.partial_succeeded
data: {"type":"image_generation.partial_succeeded","created":1792308695,"model":"MiniMax-H3-Image","image_index":0,"url":"https://example.com/h3-image/output-0.jpg","size":"2720x1536","output_format":"jpeg","revised_prompt":"午后的暖光透过木质窗框洒在窗台上，一只橘猫侧身趴着晒太阳，眯着眼睛，胶片颗粒质感"}

event: image_generation.completed
data: {"type":"image_generation.completed","created":1792308695,"model":"MiniMax-H3-Image","usage":{"generated_images":2,"total_tokens":13022,"input_tokens":4862,"output_tokens":8160,"input_tokens_details":{"text_tokens":4862,"image_tokens":0},"output_tokens_details":{"image_tokens":8160}},"request_id":"021792308678142a2c883cf675b9804d"}
```

```text 响应（图片编辑） theme={null}
event: image_edit.partial_succeeded
data: {"type":"image_edit.partial_succeeded","created":1792308690,"model":"MiniMax-H3-Image","image_index":1,"url":"https://example.com/h3-image/output-1.jpg","size":"5440x3072","output_format":"jpeg","revised_prompt":"将图1中的橘猫替换为图2中的柴犬，柴犬坐在窗台上望向窗外，保持原有光线与背景"}

event: image_edit.partial_failed
data: {"type":"image_edit.partial_failed","created":1792308691,"model":"MiniMax-H3-Image","image_index":2,"code":"1027","message":"output image failed content safety check"}

event: image_edit.partial_succeeded
data: {"type":"image_edit.partial_succeeded","created":1792308695,"model":"MiniMax-H3-Image","image_index":0,"url":"https://example.com/h3-image/output-0.jpg","size":"5440x3072","output_format":"jpeg","revised_prompt":"将图1中趴在窗台上的橘猫替换为图2中的柴犬，姿态改为趴卧，窗台、光线与背景保持不变"}

event: image_edit.completed
data: {"type":"image_edit.completed","created":1792308695,"model":"MiniMax-H3-Image","usage":{"generated_images":2,"total_tokens":80450,"input_tokens":47810,"output_tokens":32640,"input_tokens_details":{"text_tokens":24186,"image_tokens":23624},"output_tokens_details":{"image_tokens":32640}},"request_id":"021792308678142a2c883cf675b9804d"}
```

Python 读取示例见[图片生成指南 - 流式输出](https://platform.minimaxi.com/docs/guides/image-generation.md#流式输出)。
