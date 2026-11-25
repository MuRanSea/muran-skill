<!-- Official source: https://cloud.tencent.com/document/product/1823/140689 -->
<!-- Source SHA-256: 5f9b43a045a1c0c4a2603306a3e720e7c407ca65eb83989cb22feee7c018c9f1 -->

# HiDream 生图调用指南

官方来源：https://cloud.tencent.com/document/product/1823/140689
最近更新时间：2026-11-10 17:48:48

## 概述

HiDream-O1 是智象未来（HiDream.ai）推出的图像生成模型系列。本文介绍如何通过 TokenHub 调用 HiDream 图片生成模型 HiDream-O1-Image-1.5（`hidream-image-o1-1.5`）与 HiDream-O1-Image-Edit-1.5（`hidream-image-o1-1.5-edit`）：

**HiDream-O1-Image-1.5**：凭文本提示词同步生成图片，原生 2K 输出，支持 7 种常用比例，擅长中英文与数字的文字渲染、复杂版式与多主体控制。

**HiDream-O1-Image-Edit-1.5**：以文本提示词结合 1~6 张参考图同步生成图片，支持自然语言指令编辑（换风格、调色、增删元素、换背景、改写图中文字）与多图参考保持主体一致，无需蒙版。

**说明：**

两个模型均为**同步调用**：一次请求直接返回生成结果，无需提交任务与轮询。生图耗时通常为 30~120 秒，请将客户端超时时间设置为不低于 300 秒。

### 前提条件

已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号并开通 TokenHub 服务。

已在 [TokenHub 控制台](https://console.cloud.tencent.com/tokenhub/apikey) 获取 API Key。

在 [控制台-在线推理-视觉模型](https://console.cloud.tencent.com/tokenhub/inference?regionId=1&serviceType=VISION) 处开启对应模型的后付费。

**说明：**

下文所有示例中的 YOUR\_API\_KEY 均需替换为您自己的 API Key，鉴权方式为请求头 Authorization: Bearer YOUR\_API\_KEY。

### 模型列表

| 模型名称 | model 参数值 | 支持能力 | 输入上限 | 尺寸约束 | 简要说明 |
| --- | --- | --- | --- | --- | --- |
| HiDream-O1-Image-1.5 | `hidream-image-o1-1.5` | 文生图（同步） | 5000 字符 | 7 档预设尺寸，原生 2K | 主力文生图模型，文字渲染、复杂版式、长提示词理解与多主体控制表现突出，适合电商主图、营销海报、品牌物料、影视分镜等场景。 |
| HiDream-O1-Image-Edit-1.5 | `hidream-image-o1-1.5-edit` | 图生图 / 图片编辑（同步） | 5000 字符；参考图 1~6 张 | 7 档预设尺寸，原生 2K | 自然语言指令编辑，无需蒙版；多张参考图可锁定人物、商品或 IP 外观，适合商品精修、背景替换、海报改版与角色延展。 |

## HiDream-O1-Image-1.5 文生图

### 1. 接口描述

输入文本提示词，同步生成图片。未传 `size` 或传 `auto` 时，模型自适应决定输出尺寸，可选尺寸请参见附录“支持尺寸列表”。

**接口：** `POST https://tokenhub.tencentmaas.com/v1/wand/hidream-image/images/generations`

### 2. 输入参数

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| model | 是 | string | 模型 ID。取值：`hidream-image-o1-1.5` |
| prompt | 是 | string | 生成图片使用的文本提示词，长度 ≤ 5000 字符。 |
| size | 否 | string | 生成尺寸，格式 `${宽}x${高}`，支持 7 档：`2048x2048`（1:1）、`2304x1728`（4:3）、`1728x2304`（3:4）、`2560x1440`（16:9）、`1440x2560`（9:16）、`2496x1664`（3:2）、`1664x2496`（2:3）。传 `auto` 或不传时由模型自适应决定输出尺寸。 |

### 3. 请求示例

```bash
# 文生图
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/hidream-image/images/generations' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "hidream-image-o1-1.5",
  "prompt": "一只在沙滩上奔跑的金毛犬，傍晚的暖色光",
  "size": "2048x2048"
}'
```

### 4. 输出参数

| 参数名 | 类型 | 描述 |
| --- | --- | --- |
| created | integer | Unix 时间戳（秒）。 |
| data | array | 返回的图片生成内容数组。 |
| data[n].item\_index | integer | 图片在本次请求中的序号，从 0 起算。 |
| data[n].url | string | 生成的图片地址，为临时地址，有效期 12 小时，请及时下载转存。 |
| request\_id | string | 唯一请求标识，用于排查问题。 |
| tokenhub\_usage | object | 用量消耗。 |
| tokenhub\_usage.total\_tokens | integer | 本次任务消耗的 token 数，用于计费/对账。 |

### 5. 响应示例

```json
{
  "created": 1793780017,
  "data": [
    {
      "item_index": 0,
      "url": "https://xxx.png"
    }
  ],
  "request_id": "c9a668db-041b-4edc-bf1f-df657c1d332e",
  "tokenhub_usage": {
    "total_tokens": 60000
  }
}
```

返回的 url 为临时地址，有效期 12 小时。由于该地址带有鉴权校验，直接通过浏览器地址栏访问可能被拒绝。建议通过以下方式下载：

```bash
curl -o generated_image.png 'https://xxx.png'
```

或在代码中使用 HTTP 客户端下载保存到本地存储。

### 6. 错误码

<table><colgroup><col/><col/><col/></colgroup><tbody><tr><td><div>HTTP 状态码</div></td><td><div>说明</div></td><td><div>处理建议</div></td></tr><tr><td><div>400</div></td><td><div>请求格式有误</div></td><td><div>检查请求体字段类型/取值（如 size 取值、prompt 长度、模型名）。</div></td></tr><tr><td><div>401</div></td><td><div>鉴权不通过</div></td><td><div>检查 API_KEY 是否有效、Authorization 是否为 Bearer 格式。</div></td></tr><tr><td><div>429</div></td><td><div>请求并发数超过限额</div></td><td><div>触发并发上限，建议退避重试并控制调用并发。</div></td></tr><tr><td colspan="1" rowspan="1"><div>503</div></td><td colspan="1" rowspan="1"><div>服务内部错误</div></td><td colspan="1" rowspan="1"><div>记录 request_id，联系技术支持。</div></td></tr></tbody></table>

## HiDream-O1-Image-Edit-1.5 图生图 / 图片编辑

### 1. 接口描述

输入文本提示词与参考图片，同步生成编辑后的图片。传入 1 张参考图时按指令编辑该图；传入多张参考图时可锁定其中的人物、商品或 IP 外观，在新场景中保持主体一致。

**接口：** `POST https://tokenhub.tencentmaas.com/v1/wand/hidream-image/images/edits`

支持 `application/json`（传图片 URL）与 `multipart/form-data`（上传本地图片文件）两种请求方式。

### 2. 输入参数

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| model | 是 | string | 模型 ID。取值：`hidream-image-o1-1.5-edit` |
| prompt | 是 | string | 生成图片使用的文本提示词，描述对参考图的编辑意图，长度 ≤ 5000 字符。 |
| images | 是 | array[string] | 参考图片列表，支持 1~6 张。支持 URL 或 Base64，图片 URL 需公网可访问（http/https）；multipart/form-data 方式下通过 `image` 字段上传本地文件。输入约束请参见附录“参考图输入约束”。 |
| size | 否 | string | 生成尺寸，格式 `${宽}x${高}`，支持 7 档：`2048x2048`（1:1）、`2304x1728`（4:3）、`1728x2304`（3:4）、`2560x1440`（16:9）、`1440x2560`（9:16）、`2496x1664`（3:2）、`1664x2496`（2:3）。传 `auto` 或不传时由模型自适应决定输出尺寸。 |

### 3. 请求示例

**传入图片 URL（application/json）**

```bash
# 图片编辑
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/hidream-image/images/edits' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "hidream-image-o1-1.5-edit",
  "prompt": "换一件红色连衣裙",
  "images": ["https://example.com/reference.png"],
  "size": "2048x2048"
}'
```

**上传本地图片（multipart/form-data）**

```bash
# 图片编辑
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/hidream-image/images/edits' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -F 'model=hidream-image-o1-1.5-edit' \\
  -F 'prompt=换一件红色连衣裙' \\
  -F 'image=@reference.png' \\
  -F 'size=2048x2048'
```

### 4. 输出参数

| 参数名 | 类型 | 描述 |
| --- | --- | --- |
| created | integer | Unix 时间戳（秒）。 |
| data | array | 返回的图片生成内容数组。 |
| data[n].item\_index | integer | 图片在本次请求中的序号，从 0 起算。 |
| data[n].url | string | 生成的图片地址，为临时地址，有效期 12 小时，请及时下载转存。 |
| request\_id | string | 唯一请求标识，用于排查问题。 |
| tokenhub\_usage | object | 用量消耗。 |
| tokenhub\_usage.total\_tokens | integer | 本次任务消耗的 token 数，用于计费/对账。 |

### 5. 响应示例

```json
{
  "created": 1793780017,
  "data": [
    {
      "item_index": 0,
      "url": "https://xxx.png"
    }
  ],
  "request_id": "fcbdfc09-21c5-4e15-bb88-de8be73bc927",
  "tokenhub_usage": {
    "total_tokens": 65000
  }
}
```

返回的 url 为临时地址，有效期 12 小时。由于该地址带有鉴权校验，直接通过浏览器地址栏访问可能被拒绝。建议通过以下方式下载：

```bash
curl -o generated_image.png 'https://xxx.png'
```

或在代码中使用 HTTP 客户端下载保存到本地存储。

### 6. 错误码

| HTTP 状态码 | 说明 | 处理建议 |
| --- | --- | --- |
| 400 | 请求格式有误 | 检查请求体字段类型/取值（如 images 数量与格式、size 取值、模型名）。 |
| 401 | 鉴权不通过 | 检查 API\_KEY 是否有效、Authorization 是否为 Bearer 格式。 |
| 429 | 请求并发数超过限额 | 触发并发上限，建议退避重试并控制调用并发。 |
| 503 | 服务内部错误 | 记录 request\_id，联系技术支持。 |

## 附录

### 支持尺寸列表

两个模型的 `size` 取值一致，格式均为“宽 x 高”，均为原生 2K 输出，无需二次放大：

| 比例 | size 取值 | 适用场景参考 |
| --- | --- | --- |
| 1:1 | `2048x2048` | 商品主图、头像、社媒方图 |
| 4:3 | `2304x1728` | 横版配图、PPT 插图 |
| 3:4 | `1728x2304` | 竖版海报、小红书配图 |
| 16:9 | `2560x1440` | 横版 Banner、视频封面、分镜 |
| 9:16 | `1440x2560` | 手机壁纸、开屏、短视频封面 |
| 3:2 | `2496x1664` | 摄影横图、品牌物料 |
| 2:3 | `1664x2496` | 竖版海报、书籍封面 |
| 自适应 | `auto`（或不传） | 由模型自适应决定 |

### 参考图输入约束

仅 HiDream-O1-Image-Edit-1.5 支持参考图输入：

| 约束项 | 要求 |
| --- | --- |
| 数量 | 1~6 张 |
| 支持格式 | png / jpeg / jpg / bmp / tiff / webp / gif |
| 单图大小 | ≤ 20MB |
| 像素总数 | 大于 16384（128×128）且小于 16777216（4096×4096） |
| 长宽比 | 大于 0.25 且小于 4 |

建议使用 CDN 直链且不带鉴权，若为内网/带鉴权域名，需联系 TokenHub 侧加入白名单。

## 常见问题

#### **1. 两个模型怎么选？**

`hidream-image-o1-1.5` 适合纯文本生图场景，无需提供参考图，用于从零出图；`hidream-image-o1-1.5-edit` 适合基于已有图片改图的场景，需要提供参考图并用文本描述编辑意图（如换装、换背景、风格迁移、改写图中文字），或通过多张参考图保持角色、商品外观一致。两者可搭配使用：先用文生图出初稿，再用编辑模型精修。

#### **2. size 参数怎么传？**

从附录“支持尺寸列表”的 7 档中按目标比例选择，例如竖版海报传 `1728x2304`。不确定比例时传 `auto` 或不传，由模型自适应决定。

#### **3. 编辑时传多张参考图有什么作用？**

传入 1 张参考图时，模型按指令编辑该图并尽量保留原图构图与主体；传入多张参考图时，模型会提取图中的人物、商品或 IP 外观，在新的场景、姿态中保持同一主体。建议在 prompt 中明确说明每张图的用途，例如“参考第一张图的人物，穿上第二张图的衣服”。

#### **4. 请求耗时较长怎么处理？**

HiDream 生图为同步接口，单次请求耗时通常为 30~120 秒，请将客户端超时时间设置为不低于 300 秒。若持续超时，请联系技术支持并附 `request_id`。

#### **5. 生成结果图片链接会过期吗？**

会过期。两个模型的生成结果均通过 `data[n].url` 返回，为临时签名地址，有效期 12 小时，请在生成成功后及时下载转存，切勿长期依赖。
