<!-- Official source: https://platform.minimax.cn/docs/guides/image-generation.md -->
<!-- Source SHA-256: 538777042aff36e24ed741aad44684a8915b4717b62fbe216ccbdc33093d4c89 -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.minimaxi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 图片生成

> 本文档介绍 MiniMax 图片生成服务（MiniMax-H3-Image）的使用方法，支持文生图与图片编辑。

**MiniMax-H3-Image** 支持文生图与图片编辑，输出面积最大 20,000,000 像素，可自定义宽高，或按宽高比与面积档位生成。

| 生成方式 | 接口 | 输入 |
| :- | :- | :- |
| 文生图 | `POST /v1/images/generations` | prompt |
| 图片编辑 | `POST /v1/images/edits` | prompt + 1 \~ 16 张参考图 |

两个接口均为同步接口，开启 `stream` 后逐张推送结果。

高速版 `MiniMax-H3-Image-Highspeed` 的参数与限制与 MiniMax-H3-Image 相同，将请求中的 `model` 改为 `MiniMax-H3-Image-Highspeed` 即可使用。

## 模型规格

| 项 | 说明 |
| :- | :- |
| Prompt 长度 | ≤ 32000 字符；关闭 Prompt 增强时只读取约前 4096 个 token |
| 输出尺寸 | `auto`（默认，配合 `aspect_ratio`、`area`）或 `宽x高`，见[输出尺寸](#输出尺寸) |
| 单次张数 | 1 \~ 10，默认 1 |
| 输出格式 | `jpeg`（默认，也可写作 `jpg`）、`png`、`webp` |
| 返回方式 | `url`（默认，链接有效期 24 小时）、`b64_json`（不支持流式，有总面积上限） |
| 参考图 | 1 \~ 16 张，限制见[图片编辑](#图片编辑) |
| 暂不支持 | 预览图、局部编辑（mask）、透明背景 |

## 输出尺寸

输出尺寸有两种指定方式，二选一：`size` 传 `宽x高` 时，再传 `aspect_ratio` 或 `area` 会返回 400。

> [tab] 宽高比 + 面积档位
>
> ```json theme={null}
> { "aspect_ratio": "16:9", "area": "4K" }
> ```
>
> `size` 不传或传 `auto` 时按这种方式生成，`aspect_ratio` 和 `area` 都可以单独传，每张的实际宽高见 `data[].size`。
>
> * `aspect_ratio`：默认 `auto`，由 Prompt 增强根据内容决定；也可指定 `X:Y`，X、Y 为 1 \~ 300 的整数，宽高比在 1:3 \~ 3:1 之间（含边界），如 `16:9`、`3:4`、`21:9`
> * `area`：`1K`、`2K`、`4K`（默认），目标面积分别为 1024 × 1024、2048 × 2048、4096 × 4096 像素，宽高由服务端按宽高比计算，如 `2K` 搭配 `16:9` 输出 2720 × 1536

> [tab] 指定宽高
>
> ```json theme={null}
> { "size": "2720x1536" }
> ```
>
> 面积（宽 × 高）需在 655,360 \~ 20,000,000 像素之间，宽高比在 1:3 \~ 3:1 之间，均含边界；不满足时返回 400，不会自动缩放或取整。
>
> 下表的宽高与 `area` 为 `2K`、`4K` 时按对应宽高比输出的宽高相同：
>
> | 宽高比 | `2K` | `4K` |
> | :- | :- | :- |
> | 1:1 | `2048x2048` | `4096x4096` |
> | 4:3 / 3:4 | `2368x1760` / `1760x2368` | `4736x3552` / `3552x4736` |
> | 16:9 / 9:16 | `2720x1536` / `1536x2720` | `5472x3072` / `3072x5472` |
> | 3:1 / 1:3 | `3552x1184` / `1184x3552` | `7104x2368` / `2368x7104` |

> [!NOTE]
>
> 文生图设置 `disable_prompt_enhanced: true` 时，必须用 `size` 指定宽高，或用 `aspect_ratio` 指定 `X:Y`，否则返回 400。

## 文生图

```python requests theme={null}
import os
import requests

url = "https://api.minimax.cn/v1/images/generations"
api_key = os.environ.get("MINIMAX_API_KEY")
headers = {"Authorization": f"Bearer {api_key}"}

payload = {
    "model": "MiniMax-H3-Image",
    "prompt": "一只橘猫趴在窗台上晒太阳，午后暖光，胶片质感",
    "size": "2720x1536",
    "n": 1,
    "response_format": "url",
}

response = requests.post(url, headers=headers, json=payload, timeout=600)
response.raise_for_status()

result = response.json()
ext = result["output_format"]

# 链接有效期 24 小时，请下载后自行保存
for i, item in enumerate(result["data"]):
    if "error" in item:
        print(f"第 {i} 张失败：{item['error']['message']}")
        continue
    with open(f"output-{i}.{ext}", "wb") as f:
        f.write(requests.get(item["url"]).content)
```

```python OpenAI SDK theme={null}
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.minimax.cn/v1",
    api_key=os.environ.get("MINIMAX_API_KEY"),
    timeout=600,
    max_retries=0,  # 接口不支持幂等，关闭自动重试，避免重复生成与计费
)

result = client.images.generate(
    model="MiniMax-H3-Image",
    prompt="一只橘猫趴在窗台上晒太阳，午后暖光，胶片质感",
    size="2720x1536",
    response_format="url",
)

for i, item in enumerate(result.data):
    print(i, item.url)  # 生成失败的图片 url 为 None
```

## 图片编辑

参考图通过 `images[].image_url` 传入，支持公网 URL、`mm_file://{file_id}`（引用已上传文件，file\_id 通过[文件上传](https://platform.minimaxi.com/docs/api-reference/file-management-upload.md)接口以 `purpose` 为 `image_generation_input` 上传获得）或 `data:image/<格式>;base64,<Base64>` data URI。也可以用 OpenAI SDK 的 `images.edit` 直接上传图片文件（`multipart/form-data`，上传顺序即 Picture 编号），见下方示例。

**参考图限制**（请求体总大小 ≤ 64 MiB，Base64 编码后的大小约为原文件的 4/3；超过该上限时请改用公网 URL 或 `mm_file://`）

| 项 | 限制 |
| :- | :- |
| 格式 | JPG、JPEG、PNG、WEBP、HEIC、HEIF |
| 单文件大小 | ≤ 64 MiB |
| 宽高范围 | \[128, 8192] px |
| 长宽比（长边/短边） | ≤ 4:1 |
| 数量 | 1 \~ 16 |

```python requests theme={null}
import os
import requests

url = "https://api.minimax.cn/v1/images/edits"
api_key = os.environ.get("MINIMAX_API_KEY")
headers = {"Authorization": f"Bearer {api_key}"}

payload = {
    "model": "MiniMax-H3-Image",
    "prompt": "把图1里的猫换成图2里的柴犬，保持背景不变",
    "images": [
        {"image_url": "https://example.com/cat.jpg"},
        {"image_url": "https://example.com/dog.png"},
    ],
    "size": "auto",
    "response_format": "url",
}

response = requests.post(url, headers=headers, json=payload, timeout=600)
response.raise_for_status()

result = response.json()
ext = result["output_format"]

# 链接有效期 24 小时，请下载后自行保存
for i, item in enumerate(result["data"]):
    if "error" in item:
        print(f"第 {i} 张失败：{item['error']['message']}")
        continue
    with open(f"output-{i}.{ext}", "wb") as f:
        f.write(requests.get(item["url"]).content)
```

```python OpenAI SDK theme={null}
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.minimax.cn/v1",
    api_key=os.environ.get("MINIMAX_API_KEY"),
    timeout=600,
    max_retries=0,  # 接口不支持幂等，关闭自动重试，避免重复生成与计费
)

# 参考图以文件上传，列表顺序即 Picture 编号
result = client.images.edit(
    model="MiniMax-H3-Image",
    image=[open("cat.jpg", "rb"), open("dog.png", "rb")],
    prompt="把图1里的猫换成图2里的柴犬，保持背景不变",
    size="auto",
    response_format="url",
)

for i, item in enumerate(result.data):
    print(i, item.url)  # 生成失败的图片 url 为 None
```

## Prompt 增强

文生图默认开启 prompt 增强，可通过 `disable_prompt_enhanced: true` 关闭，此时需指定宽高或固定的 `aspect_ratio`；图片编辑始终开启 prompt 增强。每张图实际使用的 prompt 见 `data[].revised_prompt`。

如需精细调整，可修改 `revised_prompt` 后作为文生图新请求的 `prompt`，并设置 `disable_prompt_enhanced: true`。

也可以调用[H3-Image-Context-IR](https://platform.minimaxi.com/docs/api-reference/image-generation-h3-context-ir.md)接口单独获取增强结果，不生成图片，该接口仅支持 `MiniMax-H3-Image`。

## 部分失败

只要有一张图片生成成功，请求即返回 200。`data` 共 `n` 项，失败或未通过内容安全检查的项只返回 `error`，成功张数见 `usage.generated_images`：

```json theme={null}
"data": [
  {"url": "https://example.com/h3-image/output-0.jpg", "size": "2720x1536", "revised_prompt": "..."},
  {"error": {"code": "1027", "message": "output image failed content safety check"}}
]
```

全部失败时返回错误响应，并附带每张的 `data` 与 `usage`。全部因内容安全检查失败返回 422，全部因余额不足失败返回 402，否则返回 500。

## 流式输出

设置 `stream: true` 后，每张图片完成即通过 SSE 推送，仅支持 `response_format: "url"`。推送顺序为完成顺序，请用 `image_index` 区分。

| 事件 | 说明 |
| :- | :- |
| `<前缀>.partial_succeeded` | 单张成功 |
| `<前缀>.partial_failed` | 单张失败 |
| `<前缀>.completed` | 全部结束且至少一张成功，携带 `usage` |
| `error` | 一张都没有生成成功（含提交生成前失败），不计费，`usage` 各项为 0 |

前缀：文生图为 `image_generation`，图片编辑为 `image_edit`。字段详见[流式响应事件](https://platform.minimaxi.com/docs/api-reference/image-generation-h3-streaming.md)。

```python requests theme={null}
import json
import os
import requests

url = "https://api.minimax.cn/v1/images/generations"
headers = {"Authorization": f"Bearer {os.environ.get('MINIMAX_API_KEY')}"}

payload = {
    "model": "MiniMax-H3-Image",
    "prompt": "一只橘猫趴在窗台上晒太阳，午后暖光，胶片质感",
    "size": "2720x1536",
    "n": 3,
    "stream": True,
}

with requests.post(url, headers=headers, json=payload, stream=True, timeout=600) as response:
    response.raise_for_status()
    for line in response.iter_lines(decode_unicode=True):
        if not line or not line.startswith("data:"):
            continue
        event = json.loads(line[len("data:"):])
        event_type = event["type"]
        if event_type.endswith(".partial_succeeded"):
            print(event["image_index"], event["url"])
        elif event_type.endswith(".partial_failed"):
            print(event["image_index"], event["message"])
        elif event_type.endswith(".completed"):
            print(event["usage"])
        elif event_type == "error":
            raise RuntimeError(event["error"]["message"])
```

## 推荐阅读

> [card] [MiniMax-H3-Image 文生图接口](https://platform.minimaxi.com/docs/api-reference/image-generation-h3-generations.md)
>
> 使用 MiniMax-H3-Image，输入文本描述，进行图片生成。

> [card] [MiniMax-H3-Image 图片编辑接口](https://platform.minimaxi.com/docs/api-reference/image-generation-h3-edits.md)
>
> 使用 MiniMax-H3-Image，输入参考图与文本描述，生成新图片。

> [card] [流式响应事件](https://platform.minimaxi.com/docs/api-reference/image-generation-h3-streaming.md)
>
> 开启 `stream` 后推送的 SSE 事件类型与字段说明。

> [card] [产品定价](https://platform.minimaxi.com/docs/pricing/overview.md#models/image)
>
> 各模型的定价说明、计费方式及使用限制。

> [card] [速率限制](https://platform.minimaxi.com/docs/guides/rate-limits.md#图片)
>
> 为保证资源的高效使用，引入速率限制，以确保服务的可用性、稳定性。
