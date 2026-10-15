<!-- Official source: https://cloud.tencent.com/document/product/1823/136609 -->
<!-- Source SHA-256: a6adf8b3e213881ffa98fe6ccf0b93a28dcc41e13db46a787ab9f0ec5bf391ba -->

# Seedream 生图调用指南

官方来源：https://cloud.tencent.com/document/product/1823/136609
最近更新时间：2026-10-14 10:27:42

## 概述

Seedream 是火山引擎推出的图片生成模型系列。本文介绍如何通过 TokenHub 调用 Seedream 图片生成模型 Seedream-Image-v5.0-pro（`seedream-image-v5.0-pro`）、Seedream-Image-v5.0-lite（`seedream-image-v5.0-lite`）、Seedream-Image-v5.0-flash（`seedream-image-v5.0-flash`），支持**文生图、参考生图**，以参考图结合文本提示词生成图片，也可仅凭文本进行文生图。

### 前提条件

已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号并开通 TokenHub 服务。

已在 [TokenHub 控制台](https://console.cloud.tencent.com/tokenhub/apikey) 获取 API Key。

**说明：**

下文所有示例中的 YOUR\_API\_KEY 均需替换为您自己的 API Key，鉴权方式为请求头 Authorization: Bearer YOUR\_API\_KEY。

### 模型列表

<table><colgroup><col/><col/><col/><col/><col/></colgroup><tbody><tr><td><div>模型名称</div></td><td><div>model 参数值</div></td><td><div>支持能力</div></td><td><div>提示词上限</div></td><td><div>分辨率</div></td></tr><tr><td><div>Seedream-Image-v5.0-pro</div></td><td><div><code>seedream-image-v5.0-pro</code></div></td><td><div>参考生图 / 文生图</div></td><td><div>600字符</div></td><td><div>1K / 1.5K / 2K</div></td></tr><tr><td><div>Seedream-Image-v5.0-lite</div></td><td><div><code>seedream-image-v5.0-lite</code></div></td><td><div>参考生图 / 文生图</div></td><td><div>600字符</div></td><td colspan="1" rowspan="1"><div>2K / 3K / 4K</div></td></tr><tr><td><div>Seedream-Image-v5.0-flash</div></td><td><div><code>seedream-image-v5.0-flash</code></div></td><td><div>参考生图 / 文生图</div></td><td><div>600字符</div></td><td><div>1K / 1.5K / 2K</div></td></tr></tbody></table>

## 图片生成

### 1. 接口描述

Seedream 图片生成（参考生图 / reference-to-image）接口。支持参考生图、文生图与图片编辑：以参考图 + 文本提示词生成图片，未传图片时按文本进行文生图。

**接口：** `POST https://tokenhub.tencentmaas.com/v1/wand/si-image/generation`

### 2. 输入参数

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| model | 是 | string | 模型 ID。取值：`seedream-image-v5.0-pro、seedream-image-v5.0-lite、seedream-image-v5.0-flash` |
| prompt | 是 | string | 文本提示词，长度 ≤ 600 字符。未传 images 时按此文本进行文生图。  提示词字数建议：中文提示词不超过 300 字，英文提示词不超过 600 词。字数过多信息容易分散，模型可能因此忽略细节，只关注重点，造成图片缺失部分元素。 |
| images | 否 | array[string] | 图片 images：`seedream-image-v5.0-pro、seedream-image-v5.0-flash` 支持最多10 张，`seedream-image-v5.0-lite` 支持最多14 张， 支持 URL 和 Base64格式。  图片格式：jpeg/png/webp/bmp/tiff/gif/heic/heif，宽高比（宽 / 高）范围：[1/16， 16]，宽高长度（px）> 14，大小：<= 30MB，总像素：[196， 6000×6000（3600万）]（对单张图宽度和高度的像素乘积限制，而不是对宽度或高度的单独值进行限制）； |
| layer\_decomposition | 否 | boolean | 图层拆分开关，控制是否开启图层拆分功能。  图层拆分会将单张图片的主体、背景、文字等内容自动拆解为1张底图和最多16个可独立编辑的图层。每个图层为带透明通道的 PNG 图片。  模型支持 ：  `seedream-image-v5.0-pro`  `seedream-image-v5.0-flash` |
| size | 否 | string | 图像尺寸。  `seedream-image-v5.0-pro、seedream-image-v5.0-flash`（图片生成场景）  支持以下两种方式，不可混用：  **方式 1（推荐）**：指定分辨率档位，并在 prompt 中用自然语言描述图片宽高比、图片形状或图片用途，最终由模型判断生成图片的大小。  默认值：2K  可选值：1K、1.5K、2K  **方式 2**：指定宽高像素值（宽 x 高）。  总像素取值范围：[1280x720（921600）, 2048x2048x1.1025（4624220）]  宽高比取值范围：[1/16, 16]    `seedream-image-v5.0-pro、seedream-image-v5.0-flash`（图层拆分场景）  仅支持通过指定分辨率档位的方式设置。输出图的分辨率规则如下：  底图 ：输出底图的分辨率和 size 指定的分辨率一致；输出底图和原待拆分图的宽高比一致。  各图层 ：输出图层的分辨率和 size 指定的分辨率接近；每个输出图层和其在原图中的宽高比一致。  size 的默认值与可选值：  默认值：auto  可选值：1K、1.5K、2K、auto（根据输入图的尺寸和宽高比进行输出）    `seedream-image-v5.0-lite`  支持以下两种方式，不可混用：  方式1：指定分辨率，并在 prompt 中用自然语言描述图片宽高比、图片形状或图片用途，最终由模型判断生成图片的大小。  可选值：2K、3K、4K  方式2：指定生成图像的宽高像素值。  默认值：2048x2048  总像素取值范围：[2560x1440（3686400）, 4096x4096（16777216）]  宽高比取值范围：[1/16, 16] |
| optimize\_prompt\_options | 否 | object | 提示词优化配置。 |
| optimize\_prompt\_options.mode | 否 | string | 优化模式。  standard：标准模式，生成内容的质量更高，耗时较长。  fast：快速模式，生成内容的耗时更短，效果略低于标准模式；`seedream-image-v5.0-lite、seedream-image-v5.0-flash` 当前不支持。 |
| output\_format | 否 | string | 图像格式。  指定生成图像的文件格式。可选值：  png  jpeg |
| background | 否 | string | 图片透明通道。  用于控制是否生成带透明通道的图片。可选值：  transparent：透明背景模式，输出带有透明背景的图。  opaque：不透明背景模式，生成常规的实体背景图。  模型支持 ：  `seedream-image-v5.0-pro`  `seedream-image-v5.0-flash` |
| response\_format | 否 | string | 返回格式。  指定生成图像的返回格式。支持以下两种返回方式：  url：返回图片下载链接，链接在图片生成后12小时内有效，请及时下载图片。  b64\_json：以 Base64 编码字符串的 JSON 格式返回图像数据。 |
| sequential\_image\_generation | 否 | string | 组图模式。  控制是否关闭组图功能（组图：基于您输入的内容，生成的一组内容关联的图片）。  auto：自动判断模式，模型会根据用户提供的提示词自主判断是否返回组图以及组图包含的图片数量。  disabled：关闭组图功能，模型只会生成一张图。  模型支持：  `seedream-image-v5.0-lite` |
| sequential\_image\_generation\_options | 否 | object | 组图配置。  组图功能的配置。仅当 sequential\_image\_generation 为 auto 时生效。  模型支持：  `seedream-image-v5.0-lite` |
| sequential\_image\_generation\_options.max\_images | 否 | integer | 最大生成数量。  指定本次请求，最多可生成的图片数量。取值范围：[1, 15] |
| tools | 否 | object | 工具配置。  模型支持：  `seedream-image-v5.0-lite` |
| tools.type | 否 | string | 工具类型。指定使用的工具类型。  web\_search：联网搜索功能。 |
| watermark | 否 | boolean | 水印开关。  是否在生成的图片中添加水印。  false：不添加水印。  true：在图片右下角添加“AI 生成”字样的水印标识。 |

### 3. 请求示例

**参考生图**

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/si-image/generation' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "seedream-image-v5.0-pro",
  "images": ["https://example.com/reference.jpg"],
  "prompt": "a cat sitting on a windowsill at sunset",
  "size": "2048x2048"
}'
```

**文生图（不传 images）**

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/si-image/generation' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "seedream-image-v5.0-pro",
  "prompt": "a cat sitting on a windowsill at sunset",
  "size": "2048x2048"
}'
```

### 4. 输出参数

<table><colgroup><col/><col/><col/></colgroup><tbody><tr><td><div>字段</div></td><td><div>类型</div></td><td><div>说明</div></td></tr><tr><td><div>created</div></td><td><div>integer</div></td><td><div>任务创建时间。</div></td></tr><tr><td><div>data</div></td><td><div>object</div></td><td><div>返回图片内容。</div></td></tr><tr><td><div>data[].output_format</div></td><td><div>string</div></td><td><div>输出格式。</div></td></tr><tr><td><div>data[].size</div></td><td><div>string</div></td><td><div>图像尺寸。</div></td></tr><tr><td><div>data[].url</div></td><td><div>string</div></td><td><div>图片 URL。</div></td></tr><tr><td><div>data[].b64_json</div></td><td><div>string</div></td><td><div>图片 Base64 数据。</div></td></tr><tr><td><div>request_id</div></td><td><div>string</div></td><td><div>唯一请求标识，用于排查问题。</div></td></tr><tr><td><div>model</div></td><td><div>string</div></td><td><div>使用的生图模型。</div></td></tr><tr><td colspan="1" rowspan="1"><div>tokenhub_usage</div></td><td colspan="1" rowspan="1"><div>object</div></td><td colspan="1" rowspan="1"><div>用量消耗。</div></td></tr><tr><td colspan="1" rowspan="1"><div>tokenhub_usage.total_tokens</div></td><td colspan="1" rowspan="1"><div>integer</div></td><td colspan="1" rowspan="1"><div>本次任务消耗的 token 数，用于计费/对账。</div></td></tr></tbody></table>

### 5. 响应示例

```json
{
    "created": 1787309367,
    "data": [
        {
            "output_format": "jpeg",
            "size": "2048x2048",
            "url": "https://xxxxxxx.jpg"
        }
    ],
    "model": "doubao-seedream-5-0-pro-260628",
    "tokenhub_usage": {
        "total_tokens": 60000
    },
    "request_id": "f781d9dc-9792-43d8-82f3-90de51a1ff44"
}
```

## 附录

### 统一错误码

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| InvalidParameter | One or more parameters specified in the request are not valid. | 请求中存在一个或多个非法参数。请对照 API 文档核对参数名、类型、取值范围及参数间依赖关系后重试。 |
| MissingParameter | The request failed because it is missing %s parameter. | 请求缺少必填参数 %s。请补齐后重试。 |
| InvalidAction | The requested action is not valid for the current resource state. | 目标资源当前状态不允许该操作。请先将资源迁移到允许该操作的状态（例如结束正在进行的回合、恢复被暂停的资源）后再重试。 |
| InvalidPayload | Request payload is invalid. | 请求体不符合接口约定，可能由 JSON 解析失败、事件列表结构非法或事件参数非法导致。请对照接口文档校验请求体。 |
| EmptyEvents | Request must include at least one event. | POST events 请求体中的 events 数组为空。本码用于与 InvalidPayload 区分：InvalidPayload 表示 batch 结构非法，EmptyEvents 特指结构合法但长度为 0。 |
| RuntimeRejected | Runtime rejected the request. | POST create 阶段同步 materialize 被 runtime 拒绝。Tool Service 启动期致命错误也会归到此码；create-time 使用 public override 时 message 内容可能不同。请检查 agent snapshot 与 runtime 配置是否兼容。 |
| MissingSessionModel | Request provider mode requires agent.model.name. | POST create 在 request provider 模式下，managed-agent snapshot 中未包含可用的 agent.model.name。请在 agent 定义中补齐模型信息。 |
| MissingSessionId | session\_id is required. | POST create 请求体缺失 session\_id 或该字段为空白字符串。请携带非空 session\_id 后重试。 |
| ManagedAgentsRequired | Managed agents integration is required for request provider mode. | POST create 使用 request provider 模式，但服务端未配置 managed-agents loader。请在服务端完成 managed agents 集成后再调用。 |
| ManagedAgentsRejected | Managed agent definition was rejected. | POST create 阶段 managed-agents 业务层拒绝请求。常见原因：目标 session 不存在、session 已被删除、租户与 session 归属不一致等。 |
| ManagedAgentsInvalidAgent | Managed agent definition is invalid. | POST create 阶段 agent payload 无法翻译成合法的 AgentSpec。常见原因：agent.name 为空、权限策略或工具名不被识别、skill\_id 缺失等。 |
| InvalidSession.NotFound | The session %s does not exist or you do not have access to it. | 指定的 session\_id 不存在，或调用者对该 session 无访问权限。 |
| InvalidAgent.NotFound | The agent %s does not exist or you do not have access to it. | 指定的 agent\_id 不存在，或调用者对该 agent 无访问权限。 |
| InvalidEnvironment.NotFound | The environment %s does not exist or you do not have access to it. | 指定的 environment\_id 不存在，或调用者对该 environment 无访问权限。 |
| InvalidVault.NotFound | The vault %s does not exist or you do not have access to it. | 指定的 vault\_id 不存在，或调用者对该 vault 无访问权限。 |
| InvalidCredential.NotFound | The credential %s does not exist or you do not have access to it. | 指定的 credential\_id 不存在，或调用者对该 credential 无访问权限。 |
| InvalidMemoryStore.NotFound | The memory\_store %s does not exist or you do not have access to it. | 指定的 memory\_store\_id 不存在，或调用者对该 memory store 无访问权限。 |
| InvalidFile.NotFound | The file %s does not exist or you do not have access to it. | 指定的 file\_id 不存在，或调用者对该文件无访问权限。 |
| ResourceNotFound | The requested resource does not exist or you do not have access to it. | 请求的资源不存在或调用者无访问权限。当资源类型未落到上述具体 .NotFound 分支时使用此通用码。 |
| RequestTooLarge | The request entity is larger than the limit allowed. | 业务层单个 content / payload 超过上限（含单文件、zip 包、单条消息等业务粒度）。请拆分或压缩后重试。 |
| RequestBodyTooLarge | The request body is larger than the limit allowed. | HTTP 请求体的字节数超过了传输层上限。请压缩或分批传输。此码与 RequestTooLarge 的区别是：前者是业务粒度限制，本码是传输粒度限制。 |
| UpstreamUnavailable | An upstream dependency is temporarily unavailable. Please retry later or check that the upstream is healthy. | 客户侧上游依赖（如 MCP server、IdP）临时不可达，表现为超时、抖动或返回 5xx。请稍后重试，并排查上游服务健康度。 |
| InternalServiceError | The service encountered an unexpected internal error. Please retry later. | 服务内部出现未预期错误。可重试；持续复现时请携带 Request ID 提工单排查。 |
| SideEffectFailed | Request side effect failed. | 服务端在向运行时分派事件前执行关联操作失败。请重试；持续失败时携带 Request ID 提交工单。 |
| ManagedAgentsUnavailable | Managed agent definition is temporarily unavailable. | POST create 反查 managed-agents 的 InnerGetSession 出现网络错误、非 2xx 响应或响应解码失败，上游 managed-agents 服务暂时不可用。请稍后重试。 |

### 图片素材通用约束

参考图片 `seedream-image-v5.0-pro、seedream-image-v5.0-flash` 支持最多10 张，`seedream-image-v5.0-lite` 支持最多14 张；支持图片 URL 或 Base64；格式支持 jpeg/png/webp/bmp/tiff/gif/heic/heif，像素最小 14 x 14，总像素不大于3600万，比例须小于 1:16 或 16:1，单图 ≤ 30MB，POST body ≤ 20MB。

## 常见问题

#### **1. 文生图和参考生图怎么区分？**

同一接口：传 `images` 即为参考生图（以图中主体为参考）；不传 `images` 即为文生图（仅凭 prompt 生成）。`seedream-image-v5.0-pro` 两种模式都支持。

#### **2. 生成结果图片链接会过期吗？**

会过期。生成结果为临时地址，有效期 12 小时，请在任务成功后及时下载。
