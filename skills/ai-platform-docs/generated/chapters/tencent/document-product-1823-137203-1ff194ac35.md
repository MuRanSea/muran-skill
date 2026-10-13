<!-- Official source: https://cloud.tencent.com/document/product/1823/137203 -->
<!-- Source SHA-256: b5218982b6537c358e5421a4c157a8783159420aa98a14511ed8cc11eca609e3 -->

# WAND 生图调用指南

官方来源：https://cloud.tencent.com/document/product/1823/137203
最近更新时间：2026-09-29 17:20:04

## **概述**

[Tencent Cloud WAND（腾讯云音视频 AI）](https://cloud.tencent.com/product/wand)是腾讯云面向音视频场景打造的 AI 能力品牌。音视频场景复杂多样，通用 AI 难以直接发挥效果；WAND 依托腾讯云多年音视频技术积累与海量业务实践，将多模态大模型与音视频工程经验深度结合，提供经真实场景验证的 AI 原子能力。**WAND-Vega-Image** 是**高性价比多模态图像生成**模型，提供 **Lite、Flash、Pro** 三档能力。无论是对效率优先的大批量内容生产，还是对画面质量要求更高的专业创作，均可按需选择合适档位，在可控成本下获得稳定、高效的图像生成效果。

### 前提条件

已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号并开通 TokenHub 服务。

已在 [TokenHub 控制台](https://console.cloud.tencent.com/tokenhub/apikey) 获取 API Key。

**说明：**

下文所有示例中的 YOUR\_API\_KEY 均需替换为您自己的 API Key，鉴权方式为请求头 Authorization: Bearer YOUR\_API\_KEY。

### 调用流程

图片生成为耗时任务，接口采用**异步调用**模式，统一分两步：

1. **提交任务**：调用图片生成接口，成功返回 `task_id`。

2. **轮询结果**：携带 `task_id` 调用 [查询任务结果](https://cloud.tencent.com/document/product/1823/137203#b4e13c20-c450-4679-9048-3144b725db42) 接口，直至 `status = completed`，从结果中获取图片地址。

### 模型列表

**说明：**

WAND-Vega 生图模型提供 Lite、Flash、Pro 三档能力模型，支持文生图与参考生图。其中，Lite、Flash 档输入图片全部免费；Pro 档前 3 张输入图片免费，第 4 张起按张收取输入图片费用。

<table><colgroup><col/><col/><col/><col/><col/><col/></colgroup><tbody><tr><td><div><b>模型名称</b></div></td><td><div><b>model 参数值</b></div></td><td><div><b>支持能力</b></div></td><td><div><b>提示词上限</b></div></td><td><div><b>分辨率</b></div></td><td><div><b>画面宽高比</b></div></td></tr><tr><td><div>WAND-Vega-Image-1.0-Lite</div></td><td><div>wand-vega-image-lite</div></td><td><div>文生图/参考生图</div></td><td><div>8192 字符</div></td><td><div>1K / 2K / 4K</div></td><td colspan="1" rowspan="4"><div>支持 1:1、2:3、3:2、3:4、4:3、9:16、16:9、21:9 常见尺寸</div></td></tr><tr><td><div>WAND-Vega-Image-1.0-Flash</div></td><td><div>wand-vega-image-flash</div></td><td><div>文生图/参考生图</div></td><td><div>8192 字符</div></td><td><div>1K / 2K / 4K</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>WAND-Vega-Image-1.0-Pro</div></td><td><div>wand-vega-image-pro</div></td><td><div>文生图/参考生图</div></td><td><div>8192 字符</div></td><td><div>1K / 2K / 4K</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>WAND-Vega-Image-1.5-Pro</div></td><td><div>wand-vega-image-1.5-pro</div></td><td><div>文生图/参考生图</div></td><td><div>8192 字符</div></td><td><div>1K / 2K / 4K</div></td><td colspan="0" rowspan="0"><div></div></td></tr></tbody></table>

## 图片生成

### 1. 接口描述

WAND-Vega 图片生成接口支持文生图、参考生图：以输入参考图+文本提示词生成图片，未传图片时按文本进行文生图。

**接口：**`POST https://tokenhub.tencentmaas.com/v1/wand/vega-images/generations`

### 2. 输入参数

| **参数名** | **必选** | **类型** | **描述** |
| --- | --- | --- | --- |
| model | 是 | string | 模型 ID。取值：  wand-vega-image-lite  wand-vega-image-flash  wand-vega-image-pro  wand-vega-image-1.5-pro |
| prompt | 是 | string | 文本提示词，长度 ≤ 8192 字符。未传 images 时按此文本进行文生图。 |
| input | 否 | array[object] | 多模态输入内容数组，用于图生图 / 参考图场景。 |
| input.content | 否 | array[object] | 输入内容片段数组，按顺序拼接为多模态提示。 |
| input.content.type | 否 | string | 内容类型，取值 input\_image（参考图片）。 |
| input.content.image\_url | 否 | string | 参考图片地址。最多支持10张。格式 png/jpeg。大小不超过20MB。 |
| size | 否 | string | 输出图片尺寸，格式 `${宽}x${高}`。 |

### 3. 请求示例

**文生图**

```json
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/vega-images/generations' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "wand-vega-image-lite",
  "prompt": "A detailed painting of a butterfly",
  "size": "1024x1024"
}'
```

**参考生图**

```json
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/vega-images/generations' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "wand-vega-image-lite",
  "prompt": "A seamless composition of all reference images",
  "input": [
    {
      "content": [
        {
          "type": "input_image",
          "image_url": "https://example.com/reference.jpg"
        }
      ]
    }
  ],
  "size": "1024x1024"
}'
```

### 4. 输出参数

<table><colgroup><col/><col/><col/></colgroup><tbody><tr><td colspan="1" rowspan="1"><div><b>参数名</b></div></td><td colspan="1" rowspan="1"><div><b>类型</b></div></td><td colspan="1" rowspan="1"><div><b>描述</b></div></td></tr><tr><td colspan="1" rowspan="1"><div>task_id</div></td><td colspan="1" rowspan="1"><div>string</div></td><td colspan="1" rowspan="1"><div>WAND-Vega 生图生成的任务 ID，用于后续查询任务与回调匹配。</div></td></tr><tr><td><div>request_id</div></td><td><div>string</div></td><td><div>唯一请求标识，用于排查问题。</div></td></tr></tbody></table>

### 5. 响应示例

```json
{
  "task_id":"251380669-VegaImage-f91e7435e1e34dfa9898a451946bb3d3",
  "request_id":"5b7c57a3-e5e4-4df0-958b-e72d35582be1"
}
```

## 查询任务结果

### 1. 接口描述

查询图片生成任务的状态与结果。提交任务返回 `task_id` 后，通过本接口轮询获取结果。

**接口：**`GET https://tokenhub.tencentmaas.com/v1/wand/vega-images/tasks/<task_id>`

**说明：**

路径中的 `{task_id}` 即提交任务时返回的 `task_id`（示例中以 `YOUR_TASK_ID` 占位）。图片生成约需数秒至数十秒，建议每 3~5 秒轮询一次。

### 2. 输入参数

| **参数名** | **必选** | **类型** | **描述** |
| --- | --- | --- | --- |
| task\_id | 是 | string | 任务 ID（路径参数），即提交任务时返回的 `task_id`。 |

### 3. 请求示例

```json
curl -X GET 'https://tokenhub.tencentmaas.com/v1/wand/vega-images/tasks/<task_id>' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json'
```

### 4. 输出参数

| **字段** | **类型** | **说明** |
| --- | --- | --- |
| status | string | 处理状态：queued/in\_progress/completed/failed/cancelled/incomplete。  queued：任务已接受，排队等待执行。  in\_progress：任务正在处理中。  completed: 任务成功完成，可读取 `data[].url` 获取生成图片。  failed: 任务执行失败。  cancelled: 任务已被取消。  incomplete: 任务被中断/未完成（如达到 token 上限） |
| request\_id | string | 唯一请求标识，用于排查问题。 |
| data | array[object] | 生成结果列表。 |
| data[].url | string | 生成图片的下载地址，临时地址（含签名），请及时下载转存。 |
| usage | object | 用量消耗。 |
| usage.total\_tokens | integer | 本次任务消耗的 token 数，用于计费/对账。 |
| created\_at | string | 任务创建时间。 |
| finished\_at | string | 任务完成时间。 |

### 5. 响应示例

```json
{
  "task_id": "251380669-VegaImage-68a067d14b3c43c0961ce83373709f44",
  "status": "completed",
  "request_id": "92aa30e9-7549-4319-a0eb-467302d446f5",
  "data": [
    {
      "url": "https://aigc-image.cos.myqcloud.com/xxx/result.png"
    }
  ],
  "usage": {
    "total_tokens": 16200
  },
  "created_at": 1787560807,
  "finished_at": 1787560820
}
```

### 错误码

请参见 [API 错误码说明](https://cloud.tencent.com/document/product/1823/131595)。
