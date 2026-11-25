<!-- Official source: https://cloud.tencent.com/document/product/1823/141292 -->
<!-- Source SHA-256: 4cbf562153920bd2ff805d3566be7beeea101fad78ff96de7d675a1b7b462466 -->

# WAND 白模视频调用指南

官方来源：https://cloud.tencent.com/document/product/1823/141292
最近更新时间：2026-11-24 16:41:38

Tencent Cloud WAND Vega Previs是腾讯云面向视频生成提供的垂直场景化生成能力。可在提供剧本或分镜后，生成纯几何体搭建的 3D 白模预演视频，主要作用于确定视频场景、人物站位、景别、结构比例与物体大小、运镜走向，在确认效果后，再使用白模视频作为参考视频进行视频生成。白模元素大多用简洁的几何体制作，例如人物用人偶或圆柱体代替，场景只保留墙体、楼梯、门、桌椅等主要结构，整体不做材质和光影。

#### 适用场景

适用于人物与空间关系复杂，难以用文字描述清楚的场景，如：

**复杂空间：**如通过楼梯串联多楼层、通过走廊走向房间、打开门后的空间。

**多人或多物体站位：**隔桌对坐、多人围站、人物被遮挡场景。

**需确定起点和终点：**上楼、穿门、绕柱，需先确定起点、终点和路线。

**运镜变化较大：**绕拍、跟拍、或从门外进入室内镜头。

**多镜头共用布局：**同一场景内需用到全景、近景和反打等拍摄镜头。

#### 白模视频优势

**人物站位明确：**人物位置、物体大小和拍摄角度都可确定，不受提示词影响。

**空间关系稳定：**前后位置、距离和遮挡都有参考，防止场景偏移。

**可精准修改错误位置：**位置或镜头错误时，可精准修改对应白模细节。

**多镜头一致：**同个白模场景下可从不同机位输出视频，各镜头空间位置保持一致。

### 创作流程

**提示词输入：**输入**剧本 / 分镜、参考图（如有），**进行白模视频生成（由云端渲染完成）。

**输出白模视频文件：**输出**白模视频、3D 文件、白模、白模交接文档，**如需再次编辑，可在多轮对话中直接描述调整内容，编辑修改 3D 文件。

**参考提示词扩写：**使用 **LLM 模型** 或 **Agent** 进行参考视频提示词扩写。

**参考白模视频生成：**使用扩写后的参考视频提示词和白模视频提交至视频生成模型进行视频生成（仅支持可参考视频生成的视频生成模型）。

![](https://qcloudimg.tencent-cloud.cn/image/document/bd54978e44b19a2007bb4dadce298472.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/bd54978e44b19a2007bb4dadce298472.png)

### 前提条件

已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号并开通 TokenHub 服务。

已在 [TokenHub 控制台](https://console.cloud.tencent.com/tokenhub/apikey) 获取 API Key。

**说明：**

下文所有示例中的 YOUR\_API\_KEY 均需替换为您自己的 API Key，鉴权方式为请求头 Authorization: Bearer YOUR\_API\_KEY。

### **调用流程**

白模视频生成为耗时任务，接口采用异步调用模式，统一分两步：

1. **提交任务：**调用 `POST /v1/wand/videos/previs`，成功返回 `task_id`。

2. **轮询结果：**携带 `task_id` 调用 `POST /v1/wand/videos/previs/query`，直至 `status` 为 `success` 或 `failed`，成功后从 `video_url` 获取视频地址、从 `blender_url` 获取 Blender 工程文件地址。

3. **多轮编辑：**如需在上一轮结果基础上继续修改，将上一轮的 `task_id` 填入下一次提交的 `settings.previous_task_id` 即可。

### 模型列表

<table><colgroup><col/><col/><col/><col/><col/><col/></colgroup><tbody><tr><td colspan="1" rowspan="1"><div><b>模型名称</b></div></td><td colspan="1" rowspan="1"><div><b>model 参数值</b></div></td><td colspan="1" rowspan="1"><div><b>支持输入</b></div></td><td colspan="1" rowspan="1"><div><b>视频时长（秒）</b></div></td><td><div><b>适用场景</b></div></td><td colspan="1" rowspan="1"><div><b>输出产物</b></div></td></tr><tr><td colspan="1" rowspan="1"><div>WAND-Vega-Video-1.0-Previs-pro</div></td><td colspan="1" rowspan="1"><div>wand-vega-video-1.0-previs-pro</div></td><td colspan="1" rowspan="1"><div>文本、参考图片、Blender 工程文件</div></td><td colspan="1" rowspan="1"><div>60s</div></td><td><div>适合电影级、复杂场景的高质量视频生成，精细化打磨。</div></td><td colspan="1" rowspan="1"><div>MP4 视频、Blender 工程文件、预演描述（brief.md）</div></td></tr><tr><td colspan="1" rowspan="1"><div>WAND-Vega-Video-1.0-Previs-flash</div></td><td colspan="1" rowspan="1"><div>wand-vega-video-1.0-previs-flash</div></td><td colspan="1" rowspan="1"><div>文本、参考图片、Blender 工程文件</div></td><td colspan="1" rowspan="1"><div>60s</div></td><td colspan="1" rowspan="1"><div>适合短视频、短剧等简单场景生成，主打快速与空间/角色定位。</div></td><td colspan="1" rowspan="1"><div>MP4 视频、Blender 工程文件、预演描述（brief.md）</div></td></tr><tr><td colspan="1" rowspan="1"><div>WAND-Vega-Video-1.0-Previs-lite</div></td><td colspan="1" rowspan="1"><div>wand-vega-video-1.0-previs-lite</div></td><td colspan="1" rowspan="1"><div>文本、参考图片</div></td><td colspan="1" rowspan="1"><div>60s</div></td><td colspan="1" rowspan="1"><div>适合小空间对话、人物较少的场景，主打性价比和轻量化使用，Lite 版本输出仅提供白模视频。</div></td><td colspan="1" rowspan="1"><div>MP4 视频、预演描述（brief.md）</div></td></tr></tbody></table>

**说明：**

视频时长、比例、分辨率均可在输入中用自然语言自定义，若不填则统一由服务智能生成。

## 视频生成

### 1. 接口描述

提交一个白模视频生成任务。文生视频、参考生视频（参考图片 / Blender 工程）与多轮追问共用本接口，通过 contents 数组中元素的 type 以及 settings.previous\_task\_id 区分。

**接口：**`POST https://tokenhub.tencentmaas.com/v1/wand/videos/previs`

### 2. 输入参数

| **参数名** | **必选** | **类型** | **描述** |
| --- | --- | --- | --- |
| model | 是 | string | 模型名称。取值：  wand-vega-video-1.0-previs-pro  wand-vega-video-1.0-previs-flash  wand-vega-video-1.0-previs-lite |
| contents | 是 | array[object] | 多模态输入数组，必须包含至少 1 个 type=text 元素（生成需要文本提示词）。详细见下方 [contents 数组元素参数](https://cloud.tencent.com/document/product/1823/141292#dd50d097-8776-4af7-92ce-50968c5575b2)。 |
| settings | 否 | object | 生成设置。整体可缺省；未传等价于：首轮生成 + PRO 档位 + 默认画面比例。详细见下方 [settings 对象字段](https://cloud.tencent.com/document/product/1823/141292#cdfba603-32c2-4f10-8b4c-fe8d5631ccd9)。 |

#### **settings 对象字段**

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| settings.aspect\_ratio | 否 | string | 画面宽高比，建议取值形如 16:9、9:16、1:1。不传时按默认比例生成。最大 16 个字符，不可包含空格或控制字符，否则返回 400；不受支持的比例将按默认比例生成。 |
| settings.previous\_task\_id | 否 | string | 多轮追问时传入上一轮任务的 task\_id；不传表示首轮生成。最大 64 个字符。上一轮任务须为当前账号创建且已生成成功（status=success）。 |

**说明：**

多轮追问不继承上一轮的画面比例，如需保持一致，请在本轮重新传入 settings.aspect\_ratio。

#### contents 数组元素参数

`contents` 是一个按 `type` 区分的数组，每个元素结构如下：

<table><colgroup><col/><col/><col/><col/></colgroup><tbody><tr><td><div>参数名</div></td><td><div>必选</div></td><td><div>类型</div></td><td><div>描述</div></td></tr><tr><td><div>type</div></td><td><div>是</div></td><td><div>string</div></td><td><div>元素类型。取值：text、image_url、blender_url，传入其他值将返回 400。</div></td></tr><tr><td><div>text</div></td><td><div>是</div></td><td><div>string</div></td><td><div>文本提示词。type=text 时必填且不可为空（纯空白视为未填）。存在多个 text 元素时按数组顺序拼接为完整提示词，拼接后最大 100000 个字符。</div></td></tr><tr><td colspan="1" rowspan="1"><div>image_url</div></td><td><div>否</div></td><td><div>string</div></td><td><div>参考图地址。type=image_url 时为参考图片地址，type=blender_url 时为 Blender 工程文件（.blend）地址；必填且不可为空，最大 2048 个字符。</div></td></tr><tr><td colspan="1" rowspan="1"><div>blender_url</div></td><td><div>否</div></td><td><div>string</div></td><td><div>Blender 文件地址。type=blender_url 时为 Blender 工程文件（.blend）地址，最大 2048 个字符。</div></td></tr></tbody></table>

### 3. 文生视频请求示例

仅凭文本提示词生成白模视频。`contents` 数组只包含 `type=text` 元素，未传 `settings` 时按默认画面比例生成。

```json

curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/videos/previs' \\
  -H 'Content-Type: application/json' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -d '{
  "model": "wand-vega-video-1.0-previs-pro",
  "contents": [
    {
      "type": "text",
      "text": "一个机器人在雨夜街头慢慢走向镜头，镜头缓慢推近"
    }
  ],
  "settings": {
    "aspect_ratio": "16:9"
  }
}'
```

### 4. 参考生视频请求示例

以文本 + 参考图片 / Blender 工程文件的组合生成白模视频。在 `contents` 中传入 `type=image_url` 或 `type=blender_url` 元素。

**说明：**

至少包含 1 个 `type=text` 元素，用于描述镜头运动、人物动作等预演意图。

素材地址需为公网可访问的 URL，暂不支持 Base64 内联。

```json
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/videos/previs' \\
  -H 'Content-Type: application/json' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -d '{
  "model": "wand-vega-video-1.0-previs-pro",
  "contents": [
    {
      "type": "text",
      "text": "参考图片的人物造型，在 Blender 场景中从门口走到窗边，镜头缓慢推近"
    },
    {
      "type": "image_url",
      "url": "https://example.com/character.png"
    },
    {
      "type": "blender_url",
      "url": "https://example.com/scene.blend"
    }
  ],
  "settings": {
    "aspect_ratio": "9:16"
  }
}'
```

### 5. 多轮追问请求示例

在上一轮生成结果的基础上继续修改。将上一轮提交返回的 `task_id` 填入 `settings.previous_task_id`，并在 `contents` 中描述本轮的修改要求。

**说明：**

上一轮任务须已生成成功（`status=success`），仍在生成中或已失败时返回 409。

仅可基于当前账号创建的任务追问，否则返回 400。

```json
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/videos/previs' \\
  -H 'Content-Type: application/json' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -d '{
  "model": "wand-vega-video-1.0-previs-pro",
  "contents": [
    {
      "type": "text",
      "text": "把镜头改成从左向右横移"
    }
  ],
  "settings": {
    "previous_task_id": "1300000000-WmVideo-d4906359699a3e8934e5a169c7500ec9",
    "aspect_ratio": "16:9"
  }
}'
```

### 6. 输出参数

**说明：**

提交成功以响应体返回 `task_id` 且不含 `error` 字段为准。

提交接口不做请求级幂等：每次提交均生成新的任务 ID。请以业务侧请求标识自行管理重试，避免重复生成计费。

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| task\_id | string | 任务 ID，用于轮询查询任务状态，以及多轮追问时作为 `settings.previous_task_id` 传入。 |
| request\_id | string | 本次提交请求的 ID，用于问题排查。 |

### 7. 响应示例

```java
{
  "task_id": "1300000000-WmVideo-d4906359699a3e8934e5a169c7500ec9",
  "request_id": "req_5b0e1c9a3f2d4e6b8a7c1d2e3f4a5b6c"
}
```

## 查询任务结果

### 1. 接口描述

各生成形态共用的任务查询端点：提交任务返回 `task_id` 后，通过本接口轮询任务状态，成功后从 `video_url、blender_url、brief_url` 获取产物地址。

接口：`POST https://tokenhub.tencentmaas.com/v1/wand/videos/previs/query`

### 2. 输入参数

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| task\_id | 是 | string | 任务 ID，即提交任务时返回的 task\_id。仅可查询当前账号创建的任务。 |

### 3. 请求示例

```java
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/videos/previs/query' \\
  -H 'Content-Type: application/json' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -d '{
  "task_id": "1300000000-WmVideo-d4906359699a3e8934e5a169c7500ec9"
}'
```

### 4. 输出参数

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| status | string | 任务状态。取值：`processing`（生成中）、`success`（生成成功）、`failed`（生成失败）。 |
| video\_url | string | 生成视频（MP4）的下载地址。产物未就绪时为空字符串。 |
| blender\_url | string | Blender 工程文件的下载地址，可导入 Blender 二次编辑。产物未就绪时为空字符串。 |
| brief\_url | string | 预演描述文件（brief.md）的下载地址。产物未就绪时为空字符串。 |
| usage | object | 本会话累计 Token 用量。未产生用量时不返回该字段。 |
| usage.input\_tokens | integer | 累计输入 Token 数。 |
| usage.cached\_read\_tokens | integer | 输入中命中缓存的 Token 数，为 `input_tokens` 的子集。 |
| usage.output\_tokens | integer | 累计输出 Token 数。 |
| error\_message | string | 失败原因描述，仅在 `status=failed` 时非空。 |

**说明：**

`status=processing` 时 `video_url` 已非空属于正常情况：产物地址先于状态更新写入，地址非空即可下载，无需等待 status=success。

产物地址为临时下载地址，请在任务成功后及时下载并转存到自有存储。

### 5. 响应示例

```java
{
  "status": "success",
  "video_url": "https://example.cos.ap-guangzhou.myqcloud.com/out.mp4",
  "blender_url": "https://example.cos.ap-guangzhou.myqcloud.com/scene.blend",
  "brief_url": "https://example.cos.ap-guangzhou.myqcloud.com/brief.md",
  "usage": {
    "input_tokens": 135000,
    "cached_read_tokens": 90000,
    "output_tokens": 3200
  }
}
```

## 附录

### 统一错误码

除鉴权失败外，接口错误统一以 HTTP 状态码 200 返回，错误信息位于响应体的 `error` 字段；响应体不含 `error` 字段表示调用成功。

```java
{
  "error": {
    "code": 400,
    "message": "task_id is required"
  }
}
```

| error.code | 含义 | 处理建议 |
| --- | --- | --- |
| 401 | 鉴权失败：Authorization 头缺失或 API Key 无效 / 已过期。该错误在网关层返回，错误码以网关为准。 | 检查 Authorization: Bearer <API Key> 是否正确、是否在有效期内。 |
| 400 | 请求参数非法：必选项缺失、`type` 不支持、字段超长、`settings.aspect_ratio` 含空格、`settings.previous_task_id` 指向的任务不存在或不属于当前账号等。 | 对照本文档各参数的取值范围检查后重试。 |
| 404 | 查询的任务不存在，或不属于当前账号。 | 确认 `task_id` 是否正确，且为当前账号创建。 |
| 409 | 多轮追问时，`settings.previous_task_id` 指向的任务尚未生成成功（生成中或已失败）。 | 等待上一轮任务 `status=success` 后再提交；上一轮失败时请重新发起首轮生成。 |
| 500 | 服务内部错误。 | 重试；持续失败请联系技术支持。 |

**说明：**

请求未进入业务处理即失败时（如请求体无法解析、超时、服务过载），HTTP 状态码为对应的 4xx / 5xx，响应体结构不变。

## 常见问题

#### 1. 可以指定视频时长和分辨率吗？

支持，时长与分辨率统一可在文本输入中使用自然语言指定，请求中无需传入相关参数。

#### 2. 多轮追问会继承上一轮的场景吗？

会的。每一轮输入均按本轮传入的 `previous_task_id` 指定的文件进行编辑。

#### 3. 多轮追问提交时返回 409 怎么办？

409 表示上一轮任务尚未生成成功。请先轮询上一轮任务，待 `status=success` 后再提交追问；若上一轮已失败，请重新发起首轮生成。

#### 4. 为什么用正确的 task\_id 查询却返回 404？

仅可查询和追问当前账号创建的任务。请确认查询时使用的 API Key 与提交任务时属于同一账号。

#### 5. 生成结果的下载地址会过期吗？

会过期。产物地址为临时下载地址，有效期为14天，请在任务成功后及时下载视频、Blender 工程文件与预演描述，并转存到自有存储。
