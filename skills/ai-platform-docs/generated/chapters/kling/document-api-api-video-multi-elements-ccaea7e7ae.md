<!-- Official source: https://klingai.com/document-api/api/video/multi-elements.md -->
<!-- Source SHA-256: 76362275740d5c0c36f85433f21a5123b6b7257a834aa7dc90e2ed26435f4cea -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://klingai.com/document-api/llms.txt
> Use this file to discover all available pages before exploring further.

# 多模态视频参考编辑

> 来源: https://klingai.com/document-api/api/video/multi-elements
> 语言: zh
> 当前 Tab: 多模态视频参考编辑
> 此内容为面向 LLM 优化的 Markdown，已展开页面内 Tab，并省略页面目录、复制按钮等 UI 控件。

---

## 初始化待编辑视频

### 接口概览

- Method: `POST`
- Path: `/v1/videos/multi-elements/init-selection`
- Auth: `Authorization: Bearer <API_KEY>`
- Content-Type: `application/json`

### 说明

> 使用"多模态视频编辑"功能时，需先对原始视频进行初始化处理。其中，在替换或删除现有视频中的元素时，需先标记视频中相关元素。

### Headers

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `Content-Type` | string | 是 | `application/json` | - | 数据交换格式 |
| `Authorization` | string | 是 | - | - | 鉴权信息，参考接口鉴权 |

### Request Body

| 字段路径 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `video_id` | string | 否 | - | - | 视频 ID，从历史作品中选择待编辑的视频，仅支持 30 天内生成的视频作品 |
| `video_url` | string | 否 | - | - | 获取视频的 URL，上传时传视频下载链接，编辑选区时传接口返回的视频 URL |

#### Request Body 字段补充说明

- `video_id`: 仅支持 30 天内生成的视频作品
- `video_id`: 仅支持时长 ≥2 秒且 ≤5 秒，或 ≥7 秒且 ≤10 秒的视频
- `video_id`: 与 video_url 参数相关，不能同时为空，也不能同时有值
- `video_url`: 仅支持 MP4 和 MOV 格式
- `video_url`: 仅支持时长 ≥2 秒且 ≤5 秒，或 ≥7 秒且 ≤10 秒的视频
- `video_url`: 视频宽高尺寸需介于 720px（含）和 2160px（含）之间
- `video_url`: 仅支持上传 24、30 或 60fps 的视频
- `video_url`: 与 video_id 参数相关，不能同时为空，也不能同时有值

### Request Example

```bash
curl --request POST \
  --url https://api-beijing.klingai.com/v1/videos/multi-elements/init-selection \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
    "video_id": "",
    "video_url": "https://v1-kling.klingai.com/kcdn/cdn-kcdn112452/kling-qa-test/animals-output-5s.mp4"
  }'
```

### Response Example

```json
{
  "code": 0, // 错误码；具体定义见错误码
  "message": "string", // 错误信息
  "request_id": "string", // 请求ID，系统生成，用于跟踪请求、排查问题
  "data": {
    "status": 0, // 拒识码，非0为识别失败
    "session_id": "id", // 会话ID，会基于视频初始化任务生成，不会随编辑选区行为而改变，有效期24小时
    "final_unit_deduction": "string", // 任务最终扣减积分数值
    "final_balance_deduction": { // 额度扣减信息
      "quota": "string", // 额度扣减折扣价
      "list_price": "string" // 额度扣减刊例价
    },
    "fps": 30.0, // 解析后视频的帧数，在获取选区展示视频时需携参
    "original_duration": 1000, // 解析后视频的时长，在创建任务时需携参
    "width": 720, // 解析后视频的宽，暂无作用
    "height": 1280, // 解析后视频的高，暂无作用
    "total_frame": 300, // 解析后视频的总帧数，在创建任务时需携参
    "normalized_video": "url" // 初始化后的视频URL
}
```

---

## 增加视频选区

### 接口概览

- Method: `POST`
- Path: `/v1/videos/multi-elements/add-selection`
- Auth: `Authorization: Bearer <API_KEY>`
- Content-Type: `application/json`

### Headers

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `Content-Type` | string | 是 | `application/json` | - | 数据交换格式 |
| `Authorization` | string | 是 | - | - | 鉴权信息，参考接口鉴权 |

### Request Body

| 字段路径 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `session_id` | string | 是 | - | - | 会话 ID，会基于视频初始化任务生成，不会随编辑选区行为而改变 |
| `frame_index` | int | 是 | - | - | 帧号 |
| `points` | array | 是 | - | - | 点选坐标，用 x、y 表示 |
| `points[].x` | float | 是 | - | - | X 坐标 [0-1] |
| `points[].y` | float | 是 | - | - | Y 坐标 [0-1] |

#### Request Body 字段补充说明

- `frame_index`: 最多支持添加 10 个标记帧，即最多基于 10 帧标记视频选区
- `frame_index`: 1 次仅支持标记 1 帧
- `points`: 取值范围：[0, 1]，用百分比表示；[0, 1] 代表画面左上角
- `points`: 支持同时增加多个标记点，某一帧最多可标记 10 个点

### Request Example

```bash
curl --request POST \
  --url https://api-beijing.klingai.com/v1/videos/multi-elements/add-selection \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
    "session_id": "847570360458960960",
    "frame_index": 0,
    "points": [
      {
        "x": 0.7738498789346246,
        "y": 0.297142857142857
      }
    ]
  }'
```

### Response Example

```json
{
  "code": 0, // 错误码；具体定义见错误码
  "message": "string", // 错误信息
  "request_id": "string", // 请求ID，系统生成，用于跟踪请求、排查问题
  "data": {
    "status": 0, // 拒识码，非0为识别失败
    "session_id": "id", // 会话ID，会基于视频初始化任务生成，不会随编辑选区行为而改变，有效期24小时
    "final_unit_deduction": "string", // 任务最终扣减积分数值
    "final_balance_deduction": { // 额度扣减信息
      "quota": "string", // 额度扣减折扣价
      "list_price": "string" // 额度扣减刊例价
    },
    "res": {
      "frame_index": 0,
      "rle_mask_list": [{
        "object_id": 0,
        "rle_mask": {
          "size": [720, 1280],
          "counts": "string"
        },
        "png_mask": {
          "size": [720, 1280],
          "base64": "string"
        }
      }]
    }
  }
}
```

### 代码示例

#### 解析图像分割结果

```typescript
export type RLEObject = {
  size: [h: number, w: number]
  counts: string
}
type RLE = {
  h: number
  w: number
  m: number
  binaries: number[]
}
export function decode(rleObj: RLEObject) {
  const [h, w] = rleObj.size
  const R: RLE = { h, w, m: 0, binaries: [0] }
  rleFrString(R, rleObj.counts)
  const unitArray = new Uint8Array(h * w)
  rleDecode(R, unitArray)
  return unitArray
}
function rleDecode(R: RLE, M: Uint8Array) {
  let j
  let k
  let p = 0
  let v = false
  for (j = 0; j < R.m; j++) {
    for (k = 0; k < R.binaries[j]; k++) {
      const x = Math.floor(p / R.h)
      const y = p % R.h
      M[y * R.w + x] = v === false ? 0 : 1 // 注意此处是 y * width + x，即横着排列
      p++
    }
    v = !v
  }
}
function rleFrString(R: RLE, s: string) {
  let m = 0
  let p = 0
  let k
  let x
  let more
  const binaries = []
  while (s[p]) {
    x = 0
    k = 0
    more = 1
    while (more) {
      const c = s.charCodeAt(p) - 48
      x |= (c & 0x1f) << (5 * k)
      more = c & 0x20
      p++
      k++
      if (!more && c & 0x10) {
        x |= -1 << (5 * k)
      }
    }
    if (m > 2) {
      x += binaries[m - 2]
    }
    binaries[m++] = x
  }
  R.m = m
  R.binaries = binaries
}
```

#### 绘制图像分割图层

```typescript
// height 为视频的高度 width 为视频的宽度
function drawMask(rleMask: string, height: number, width: number) {
  if (!canvasRef.value) return
  const ctx = canvasRef.value.getContext('2d')
  if (!ctx) return

  const decodeData = decode({ counts: rleMask, size: [height, width] })
  const imageData = ctx.createImageData(width, height)
  for (let y = 0; y < height; y++) {
    for (let x = 0; x < width; x++) {
      const index = y * width + x
      if (decodeData[index]) {
        const imageIndex = index * 4
        // 设置像素点颜色：红色，绿色，蓝色，透明度
        imageData.data[imageIndex] = 116 // 红色
        imageData.data[imageIndex + 1] = 255 // 绿色
        imageData.data[imageIndex + 2] = 82 // 蓝色
        imageData.data[imageIndex + 3] = 163 // 透明度
      }
    }
  }
  ctx.putImageData(imageData, 0, 0)
}
```

---

## 删减视频选区

### 接口概览

- Method: `POST`
- Path: `/v1/videos/multi-elements/delete-selection`
- Auth: `Authorization: Bearer <API_KEY>`
- Content-Type: `application/json`

### Headers

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `Content-Type` | string | 是 | `application/json` | - | 数据交换格式 |
| `Authorization` | string | 是 | - | - | 鉴权信息，参考接口鉴权 |

### Request Body

| 字段路径 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `session_id` | string | 是 | - | - | 会话 ID，会基于视频初始化任务生成，不会随编辑选区行为而改变 |
| `frame_index` | int | 是 | - | - | 帧号 |
| `points` | array | 是 | - | - | 点选坐标，用 x、y 表示 |
| `points[].x` | float | 是 | - | - | X 坐标 [0-1] |
| `points[].y` | float | 是 | - | - | Y 坐标 [0-1] |

#### Request Body 字段补充说明

- `points`: 取值范围：[0, 1]，用百分比表示；[0, 1] 代表画面左上角
- `points`: 支持同时增加多个标记点
- `points`: 坐标点需与增加视频选区时完全一致

### Request Example

```bash
curl --request POST \
  --url https://api-beijing.klingai.com/v1/videos/multi-elements/delete-selection \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
    "session_id": "847570360458960960",
    "frame_index": 0,
    "points": [
      {
        "x": 0.7738498789346246,
        "y": 0.297142857142857
      }
    ]
  }'
```

### Response Example

```json
{
  "code": 0, // 错误码；具体定义见错误码
  "message": "string", // 错误信息
  "request_id": "string", // 请求ID，系统生成，用于跟踪请求、排查问题
  "data": {
    "status": 0, // 拒识码，非0为识别失败
    "session_id": "id", // 会话ID，会基于视频初始化任务生成，不会随编辑选区行为而改变，有效期24小时
    "final_unit_deduction": "string", // 任务最终扣减积分数值
    "final_balance_deduction": { // 额度扣减信息
      "quota": "string", // 额度扣减折扣价
      "list_price": "string" // 额度扣减刊例价
    },
    "res": {
      "frame_index": 0,
      "rle_mask_list": [{
        "object_id": 0,
        "rle_mask": {
          "size": [720, 1280],
          "counts": "string"
        },
        "png_mask": {
          "size": [720, 1280],
          "base64": "string"
        }
      }]
    }
  }
}
```

---

## 清除视频选区

### 接口概览

- Method: `POST`
- Path: `/v1/videos/multi-elements/clear-selection`
- Auth: `Authorization: Bearer <API_KEY>`
- Content-Type: `application/json`

### Headers

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `Content-Type` | string | 是 | `application/json` | - | 数据交换格式 |
| `Authorization` | string | 是 | - | - | 鉴权信息，参考接口鉴权 |

### Request Body

| 字段路径 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `session_id` | string | 是 | - | - | 会话 ID，会基于视频初始化任务生成，不会随编辑选区行为而改变 |

### Request Example

```bash
curl --request POST \
  --url https://api-beijing.klingai.com/v1/videos/multi-elements/clear-selection \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
    "session_id": "847570360458960960"
  }'
```

### Response Example

```json
{
  "code": 0, // 错误码；具体定义见错误码
  "message": "string", // 错误信息
  "request_id": "string", // 请求ID，系统生成，用于跟踪请求、排查问题
  "data": {
    "status": 0, // 拒识码，非0为识别失败
    "session_id": "id" // 会话ID，会基于视频初始化任务生成，不会随编辑选区行为而改变，有效期24小时
    "final_unit_deduction": "string", // 任务最终扣减积分数值
    "final_balance_deduction": { // 额度扣减信息
      "quota": "string", // 额度扣减折扣价
      "list_price": "string" // 额度扣减刊例价
    },
  }
}
```

---

## 预览已选区视频

### 接口概览

- Method: `POST`
- Path: `/v1/videos/multi-elements/preview-selection`
- Auth: `Authorization: Bearer <API_KEY>`
- Content-Type: `application/json`

### Headers

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `Content-Type` | string | 是 | `application/json` | - | 数据交换格式 |
| `Authorization` | string | 是 | - | - | 鉴权信息，参考接口鉴权 |

### Request Body

| 字段路径 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `session_id` | string | 是 | - | - | 会话 ID，会基于视频初始化任务生成，不会随编辑选区行为而改变 |

### Request Example

```bash
curl --request POST \
  --url https://api-beijing.klingai.com/v1/videos/multi-elements/preview-selection \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
    "session_id": "847570360458960960"
  }'
```

### Response Example

```json
{
  "code": 0, // 错误码；具体定义见错误码
  "message": "string", // 错误信息
  "request_id": "string", // 请求ID，系统生成，用于跟踪请求、排查问题
  "data": {
    "status": 0, // 拒识码，非0为识别失败
    "session_id": "id", // 会话ID，会基于视频初始化任务生成，不会随编辑选区行为而改变，有效期24小时
    "final_unit_deduction": "string", // 任务最终扣减积分数值
    "final_balance_deduction": { // 额度扣减信息
      "quota": "string", // 额度扣减折扣价
      "list_price": "string" // 额度扣减刊例价
    },
    "res": {
      "video": "url", // 含mask的视频
      "video_cover": "url", // 含mask的视频的封面
      "tracking_output": "url" // 图像分割结果中，每一帧mask结果
    }
  }
}
```

---

## 创建任务

### 接口概览

- Method: `POST`
- Path: `/v1/videos/multi-elements`
- Auth: `Authorization: Bearer <API_KEY>`
- Content-Type: `application/json`

### Headers

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `Content-Type` | string | 是 | `application/json` | - | 数据交换格式 |
| `Authorization` | string | 是 | - | - | 鉴权信息，参考接口鉴权 |

### Request Body

| 字段路径 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `session_id` | string | 是 | - | - | 会话 ID，会基于视频初始化任务生成，不会随编辑选区行为而改变 |
| `edit_mode` | string | 是 | - | `addition`, `swap`, `removal` | 操作类型 |
| `image_list` | array | 否 | - | - | 裁剪后的参考图像 |
| `image_list[].image` | string | 是 | - | - | 图片 URL 或 Base64 字符串 |
| `prompt` | string | 是 | - | - | 正向文本提示词 |
| `negative_prompt` | string | 否 | - | - | 负向文本提示词 |
| `mode` | string | 否 | `std` | `std`, `pro` | 生成视频的模式 |
| `duration` | string | 否 | `5` | `5`, `10` | 生成视频时长，单位 s |
| `watermark_info` | object | 否 | - | - | 是否同时生成含水印的结果 |
| `callback_url` | string | 否 | - | - | 本次任务结果回调通知地址，如果配置，服务端会在任务状态发生变更时主动通知 |
| `external_task_id` | string | 否 | - | - | 自定义任务 ID |

#### Request Body 字段补充说明

- `edit_mode`: addition：增加元素
- `edit_mode`: swap：替换元素
- `edit_mode`: removal：删除元素
- `image_list`: 增加视频元素时：当前参数必填，可上传 1~2 张图片
- `image_list`: 编辑视频元素时：当前参数必填，仅可上传 1 张图片
- `image_list`: 删除视频元素时，当前参数无需填写
- `image_list`: 用 key:value 承载，如下：
  ```json
  "image_list":[
    { "image":"image_url" },
    { "image":"image_url" }
  ]
  ```
- `image_list`: API 端无裁剪逻辑，请直接上传已选主体后的图片
- `image_list`: 支持传入图片 Base64 编码或图片 URL（确保可访问）
- `image_list`: 注意：若您使用 Base64 方式，请不要在 Base64 编码字符串前添加任何前缀（如 `data:image/png;base64,`），直接传递 Base64 编码后的字符串即可。
- `image_list`: 正确的 Base64 编码参数：
  ```plaintext
  iVBORw0KGgoAAAANSUhEUgAAAAUA...
  ```
- `image_list`: 错误的 Base64 编码参数（包含 data: 前缀）：
  ```plaintext
  data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA...
  ```
- `image_list`: 图片格式支持 .jpg / .jpeg / .png
- `image_list`: 图片文件大小不能超过 10MB，图片宽高尺寸不小于 300px，图片宽高比要在 1:2.5 ~ 2.5:1 之间
- `prompt`: 用 <<<xxx>>> 的格式来特指某个视频或某张图片，如 <<<video_1>>>、<<<image_1>>>
- `prompt`: 为保证效果，提示词中需包含视频编辑所需的视频和图片（如有）
- `prompt`: 不能超过 2500 个字符
- `prompt`: > **推荐的 Prompt 模板：**
  >
  > 
  >
  > **增加元素：**
  > - 中文：基于<<<video_1>>>中的原始内容，以自然生动的方式，将<<<image_1>>>中的【】，融入<<<video_1>>>的【】
  > - 英文：Using the context of <<<video_1>>>, seamlessly add [x] from <<<image_1>>>
  >
  > 
  >
  > **替换元素：**
  > - 中文：使用<<<image_1>>>中的【】，替换<<<video_1>>>中的【】
  > - 英文：swap [x] from <<<image_1>>> for [x] from <<<video_1>>>
  >
  > 
  >
  > **删除元素：**
  > - 中文：删除<<<video_1>>>中的【】
  > - 英文：Delete [x] from <<<video_1>>>
  >
  > 
  >
  > 注：中文的【】，英文的 [x]，是需要用户填写的部分
- `negative_prompt`: 不能超过 2500 个字符
- `mode`: std：标准模式（标准），基础模式，性价比高
- `mode`: pro：专家模式（高品质），高表现模式，生成视频质量更佳
- `duration`: 支持且仅支持生成 5s 和 10s 的视频
- `duration`: 如生成 5s 时长视频，输入视频时长需 ≥2s 且 ≤5s
- `duration`: 如生成 10s 时长视频，输入视频时长需 ≥7s 且 ≤10s
- `watermark_info`: 通过enabled参数定义，具体格式如下：
  ```json
   "watermark_info": { "enabled": boolean } 
  ```
- `watermark_info`: true 为生成，false 为不生成
- `watermark_info`: 暂不支持自定义水印
- `callback_url`: 具体通知的消息 schema 见 [Callback 协议](https://klingai.com/document-api/api/get-started/callbacks)
- `external_task_id`: 用户自定义任务 ID，传入不会覆盖系统生成的任务 ID，但支持通过该 ID 进行任务查询
- `external_task_id`: 请注意，单用户下需要保证唯一性

### Request Example

```bash
curl --request POST \
  --url https://api-beijing.klingai.com/v1/videos/multi-elements \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
    "session_id": "847570360458960960",
    "edit_mode": "removal",
    "image_list": [],
    "prompt": "删除<<<video_1>>>中的【小鸡】",
    "negative_prompt": "",
    "mode": "std",
    "duration": "5",
    "callback_url": "",
    "external_task_id": ""
  }'
```

### Response Example

```json
{
  "code": 0, // 错误码；具体定义见错误码
  "message": "string", // 错误信息
  "request_id": "string", // 请求ID，系统生成，用于跟踪请求、排查问题
  "data": {
    "task_id": "string", // 任务ID，系统生成
    "task_status": "string", // 任务状态，枚举值：submitted（已提交）、processing（处理中）、succeed（成功）、failed（失败）
    "task_info": {
      "external_task_id": "string" // 客户自定义任务ID
    },
    "created_at": 1722769557708, // 任务创建时间，Unix时间戳、单位ms
    "updated_at": 1722769557708 // 任务更新时间，Unix时间戳、单位ms
  }
}
```

---

## 查询任务（单个）

### 接口概览

- Method: `GET`
- Path: `/v1/videos/multi-elements/{id}`
- Auth: `Authorization: Bearer <API_KEY>`
- Content-Type: `application/json`

### Headers

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `Content-Type` | string | 是 | `application/json` | - | 数据交换格式 |
| `Authorization` | string | 是 | - | - | 鉴权信息，参考接口鉴权 |

### Path Params

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `task_id` | string | 否 | - | - | 多模态视频编辑的任务 ID |
| `external_task_id` | string | 否 | - | - | 多模态视频编辑的自定义任务 ID |

#### Path Params 字段补充说明

- `task_id`: 请求路径参数，直接将值填写在请求路径中
- `task_id`: 与 external_task_id 两种查询方式二选一
- `external_task_id`: 创建任务时填写的 external_task_id，与 task_id 两种查询方式二选一

### Request Example

```bash
curl --request GET \
  --url https://api-beijing.klingai.com/v1/videos/multi-elements/{task_id} \
  --header 'Authorization: Bearer <token>'
```

### Response Example

```json
{
  "code": 0, // 错误码；具体定义见错误码
  "message": "string", // 错误信息
  "request_id": "string", // 请求ID，系统生成，用于跟踪请求、排查问题
  "data": {
    "task_id": "string", // 任务ID，系统生成
    "task_status": "string", // 任务状态，枚举值：submitted（已提交）、processing（处理中）、succeed（成功）、failed（失败）
    "task_status_msg": "string", // 任务状态信息，当任务失败时展示失败原因（如触发平台的内容风控等）
    "task_info": { // 任务创建时的参数信息
      "external_task_id": "string" // 客户自定义任务ID
    },
    "task_result": {
      "videos": [
        {
          "id": "string", // 生成的视频ID；全局唯一
          "session_id": "id", // 会话ID，会基于视频初始化任务生成，不会随编辑选区行为而改变，有效期24小时
          "url": "string", // 生成视频的URL（请注意，为保障信息安全，生成的图片/视频会在30天后被清理，请及时转存）
          "watermark_url": "string", // 含水印视频下载URL，防盗链格式
          "duration": "string" // 视频总时长，单位s
        }
      ]
    },
    "watermark_info": {
      "enabled": boolean
    },
    "final_unit_deduction": "string", // 任务最终扣减积分数值
    "final_balance_deduction": { // 额度扣减信息
      "quota": "string", // 额度扣减折扣价
      "list_price": "string" // 额度扣减刊例价
    },
    "created_at": 1722769557708, // 任务创建时间，Unix时间戳、单位ms
    "updated_at": 1722769557708 // 任务更新时间，Unix时间戳、单位ms
  }
}
```

---

## 查询任务（列表）

### 接口概览

- Method: `GET`
- Path: `/v1/videos/multi-elements`
- Auth: `Authorization: Bearer <API_KEY>`
- Content-Type: `application/json`

### Headers

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `Content-Type` | string | 是 | `application/json` | - | 数据交换格式 |
| `Authorization` | string | 是 | - | - | 鉴权信息，参考接口鉴权 |

### Query Params

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `pageNum` | int | 否 | `1` | - | 页码 |
| `pageSize` | int | 否 | `30` | - | 每页数据量 |

#### Query Params 字段补充说明

- `pageNum`: 取值范围：[1, 1000]
- `pageSize`: 取值范围：[1, 500]

### Request Example

```bash
curl --request GET \
  --url 'https://api-beijing.klingai.com/v1/videos/multi-elements?pageNum=1&pageSize=30' \
  --header 'Authorization: Bearer <token>'
```

### Response Example

```json
{
  "code": 0, // 错误码；具体定义见错误码
  "message": "string", // 错误信息
  "request_id": "string", // 请求ID，系统生成，用于跟踪请求、排查问题
  "data": [
    {
      "task_id": "string", // 任务ID，系统生成
      "task_status": "string", // 任务状态，枚举值：submitted（已提交）、processing（处理中）、succeed（成功）、failed（失败）
      "task_status_msg": "string", // 任务状态信息，当任务失败时展示失败原因（如触发平台的内容风控等）
      "task_info": { // 任务创建时的参数信息
        "external_task_id": "string" // 客户自定义任务ID
      },
      "task_result": {
        "videos": [
          {
            "id": "string", // 生成的视频ID；全局唯一
            "session_id": "id", // 会话ID，会基于视频初始化任务生成，不会随编辑选区行为而改变，有效期24小时
            "url": "string", // 生成视频的URL（请注意，为保障信息安全，生成的图片/视频会在30天后被清理，请及时转存）
            "watermark_url": "string", // 含水印视频下载URL，防盗链格式
            "duration": "string" // 视频总时长，单位s
          }
        ]
      },
      "watermark_info": {
        "enabled": boolean
      },
      "final_unit_deduction": "string", // 任务最终扣减积分数值
      "final_balance_deduction": { // 额度扣减信息
        "quota": "string", // 额度扣减折扣价
        "list_price": "string" // 额度扣减刊例价
      },
      "created_at": 1722769557708, // 任务创建时间，Unix时间戳、单位ms
      "updated_at": 1722769557708 // 任务更新时间，Unix时间戳、单位ms
    }
  ]
}
```
