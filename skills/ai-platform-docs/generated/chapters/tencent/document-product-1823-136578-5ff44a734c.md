<!-- Official source: https://cloud.tencent.com/document/product/1823/136578 -->
<!-- Source SHA-256: 947efeeb5a8b6e72d8357993d306a9d6a24892c5e7acb8557c977f9f5bb570c3 -->

# Hy 世界模型调用指南

官方来源：https://cloud.tencent.com/document/product/1823/136578
最近更新时间：2026-08-21 17:30:31

## 概述

**混元世界模型**是新一代多模态世界模型，致力于打通虚拟与现实的边界。它具备强大的跨模态认知能力，能够将文本描述或图片生成生动、高保真的 **3D 场景** 或 **360° 全景图。**

本文介绍如何通过 TokenHub 调用混元 3D 场景模型：Hy-World-2.1-scene，Hy-World-2.1-panorama

### 前提条件

已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号并开通 TokenHub 服务。

已在 [TokenHub 控制台](https://console.cloud.tencent.com/tokenhub/apikey) 获取 API Key。

**说明：**

下文所有示例中的 YOUR\_API\_KEY 均需替换为您自己的 API Key，鉴权方式为请求头 Authorization: Bearer YOUR\_API\_KEY。

### **调用流程**

两类接口采用不同的调用模式：

| 接口类型 | 说明 |
| --- | --- |
| 360° 全景图（同步接口） | 单次调用直接返回生成结果，无需轮询。 |
| 3D 场景生成（异步接口） | 耗时任务（通常 10～20 分钟），分两步调用：  1. **提交任务**：调用能力接口（文生场景/图生场景），成功返回任务 `id`。  2. **轮询结果**：携带 `id` 调用**查询任务结果**接口，建议**每 3~5 秒轮询一次**，直至 `status = succeeded`（生成成功）。  **说明：**  任务创建成功后请勿重复提交，通过轮询获取结果即可。 |

### 模型列表

| 模型名称 | model 参数值 | 支持能力 | 模型说明 |
| --- | --- | --- | --- |
| **HY-World-2.1-scene** | `hy-world2-scene` | 3D 场景生成 | 可交互，有空间感的立体3D 场景。 |
| **HY-World-2.1-panorama** | `hy-world2-panorama` | 360**°** 全景图生成 | 可360度环绕查看的场景图片。 |

## 3D 场景生成

### 1. 接口描述

根据文本或图片生成可交互，漫游的实体3D 场景。

**接口：** `POST https://tokenhub.tencentmaas.com/v1/wand/hunyuan-video/world2-scene`

### 2. 输入参数

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| prompt | 是 | string | 文本提示词，描述期望生成的场景内容。取值范围：≤ 600 字符。 |
| image\_url | 条件必选 | string | 图片地址，传入公网可访问的图片 URL，分辨率最低要求 **512\*512**，文件大小不超过 **10M。**  支持格式：**JPG、JPEG、PNG、WEBP。** |
| model | 条件必选 | string | 模型版本。取值范围：`hy-world2-scene` |

**说明：**

**3D 场景生成** 仅支持**文本或图片（二选一）**传入，暂不支持文本与图片同时输入**。**

### 3. 请求示例

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/hunyuan-video/world2-scene' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "hy-world2-scene",
  "image_url": "https://example.com/input.jpg"
}'
```

### 4. 输出参数

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 任务 ID，用于轮询查询任务状态。 |
| request\_id | string | 唯一请求标识，用于排查问题。 |

### 5. 响应示例

```json

{
  "id": "251435731-WandVideo-b917b8211a264cd5a7aa9fb9d836c033",
  "request_id": "02909efb-c5c8-44c6-97ed-bb2ce5e1618d"
}
```

### 6. 状态码

任务提交成功后，通**过查询任务结果**接口轮询，`status` 字段含义如下：

| status | 含义 | 处理建议 |
| --- | --- | --- |
| queued | 排队中 | 继续轮询。 |
| running | 生成中 | 每 3~5 秒轮询一次，直至 status=succeeded。 |
| succeeded | 生成成功 | 从 `data` 中获取各格式文件 URL。 |
| failed | 生成失败 | 服务端生成出错，请重试；持续失败请联系技术支持并附任务 id。 |
| cancelled | 已取消 | 任务已取消，需重新发起。 |
| unknown | 未知状态 | 请重试或联系技术支持。 |

## 360**°** 全景图

### 1. 接口描述

根据文本或图片生成可360度浏览的全景图片。

**接口：** `POST https://tokenhub.tencentmaas.com/v1/wand/hunyuan-image/world2-panorama`

### 2. 输入参数

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| prompt | 是 | string | 文本提示词，描述期望生成的场景内容。取值范围：≤ 600 字符。 |
| images | 否 | array of string | 图片地址列表，传入公网可访问的图片 URL，分辨率最低要求 **512\*512**，文件大小不超过 **10M。**  支持格式：**JPG、JPEG、PNG、WEBP。** |
| model | 是 | string | 模型版本。取值范围：`hy-world2-panorama` |

### 3. 请求示例

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/hunyuan-image/world2-panorama' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "model": "hy-world2-panorama",
  "prompt": "现代美术馆室内全景，柔和天光"
}'
```

### 4. 输出参数

<table><colgroup><col/><col/><col/></colgroup><tbody><tr><td><div>字段</div></td><td><div>类型</div></td><td><div>说明</div></td></tr><tr><td><div>id</div></td><td><div>string</div></td><td><div>本次请求的唯一 ID。</div></td></tr><tr><td><div>created</div></td><td><div>integer</div></td><td><div>请求创建时间（Unix 时间戳）。</div></td></tr><tr><td><div>status</div></td><td><div>string</div></td><td><div>任务状态：succeeded / failed。</div></td></tr><tr><td><div>data</div></td><td><div>array</div></td><td><div>生成结果列表。</div></td></tr><tr><td><div>data[].cover_image_url</div></td><td><div>string</div></td><td><div>封面图 URL，用于快速预览。</div></td></tr><tr><td><div>data[].super_resolution_image_url</div></td><td><div>string</div></td><td><div>超分辨率全景图 URL（主输出）。</div></td></tr><tr><td><div>request_id</div></td><td><div>string</div></td><td><div>唯一请求标识，用于排查问题。</div></td></tr><tr><td colspan="1" rowspan="1"><div>tokenhub_usage</div></td><td colspan="1" rowspan="1"><div>object</div></td><td colspan="1" rowspan="1"><div>用量消耗。</div></td></tr><tr><td colspan="1" rowspan="1"><div>tokenhub_usage.total_tokens</div></td><td colspan="1" rowspan="1"><div>integer</div></td><td colspan="1" rowspan="1"><div>本次任务消耗的 token 数，用于计费/对账。</div></td></tr></tbody></table>

### 5. 响应示例

```json

{
    "created": 1787287171,
    "data": [
        {
            "cover_image_url": "https://aigc-output-image-file-1326893053.cos.ap-guangzhou.myqcloud.com/1374200352/1374200352-WandImage-c763284ffc954a999329028a3a8a1013_1.png?q-sign-algorithm=sha1&q-ak=<TENCENT_CLOUD_SECRET_ID>&q-sign-time=1787287165;1787330375&q-key-time=1787287165;1787330375&q-header-list=host&q-url-param-list=&q-signature=970afd23704f1fa644e2c6ebaf7c79486a093278",
            "super_resolution_image_url": "https://aigc-output-image-file-1326893053.cos.ap-guangzhou.myqcloud.com/1374200352/1374200352-WandImage-c763284ffc954a999329028a3a8a1013_0.png?q-sign-algorithm=sha1&q-ak=<TENCENT_CLOUD_SECRET_ID>&q-sign-time=1787287164;1787330374&q-key-time=1787287164;1787330374&q-header-list=host&q-url-param-list=&q-signature=da7591e9deb002b9b7360fc8330083f19ea8d6c8"
        }
    ],
    "id": "1374200352-WandImage-c763284ffc954a999329028a3a8a1013",
    "status": "succeeded",
    "version": "1",
    "tokenhub_usage": {
        "total_tokens": 500000
    },
    "request_id": "9d73053a-cb9f-47fe-ab24-fdd2403eb7cf"
}
```

### 6. 响应状态码

同步接口直接返回结果，`status` 字段含义如下：

| status | 含义 | 处理建议 |
| --- | --- | --- |
| succeeded | 生成成功 | 从 `data[].super_resolution_image_url` 获取全景图。 |
| failed | 生成失败 | 请检查输入参数后重试；持续失败请联系技术支持并附 id。 |

## 查询任务结果

### 1. 接口描述

3D 场景生成为异步接口，任务提交后需轮询该接口获取生成结果。

**接口：** `GET https://tokenhub.tencentmaas.com/v1/wand/hunyuan-video/tasks/{task_id}`

**说明：**

路径中的 `{task_id}` 即提交任务时返回的 `id`（示例中以 `YOUR_TASK_ID` 占位）。生成约需 10～20 分钟，建议每 3~5 秒轮询一次。

### 2. 输入参数

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| task\_id | 是 | string | 任务 ID（路径参数），即提交任务时返回的 `id`。 |

### 3. 请求示例

```bash
curl -X GET 'https://tokenhub.tencentmaas.com/v1/wand/hunyuan-video/tasks/YOUR_TASK_ID' \\
  -H 'Authorization: Bearer YOUR_API_KEY'
```

### 4. 输出参数

<table><colgroup><col/><col/><col/></colgroup><tbody><tr><td><div>字段</div></td><td><div>类型</div></td><td><div>说明</div></td></tr><tr><td><div>id</div></td><td><div>string</div></td><td><div>本次请求的唯一 ID。</div></td></tr><tr><td><div>created</div></td><td><div>integer</div></td><td><div>请求创建时间（Unix 时间戳）。</div></td></tr><tr><td><div>status</div></td><td><div>string</div></td><td><div>任务状态：queued / running / succeeded / failed / cancelled / unknown。</div></td></tr><tr><td><div>data</div></td><td><div>array</div></td><td><div>生成结果列表（status=succeeded 时有值）。</div></td></tr><tr><td><div>data[].image_url</div></td><td><div>string</div></td><td><div>场景渲染预览图 URL。</div></td></tr><tr><td><div>data[].scene_url</div></td><td><div>string</div></td><td><div>3DGS 场景文件（SPZ 格式）URL。</div></td></tr><tr><td><div>data[].point_url</div></td><td><div>string</div></td><td><div>3D 点云文件（PLY 格式）URL。</div></td></tr><tr><td><div>data[].mesh_url</div></td><td><div>string</div></td><td><div>完整碰撞网格（PLY 格式）URL。</div></td></tr><tr><td><div>data[].mesh_simplified_url</div></td><td><div>string</div></td><td><div>简化碰撞网格（PLY 格式）URL，用于前端实时碰撞检测。</div></td></tr><tr><td><div>data[].position_info</div></td><td><div>string</div></td><td><div>场景空间位置信息 JSON，包含 up_direction、facing_direction、center_point、scale 及边界坐标。</div></td></tr><tr><td><div>data[].super_resolution_image_url</div></td><td><div>string</div></td><td><div>超分辨率渲染图 URL。</div></td></tr><tr><td><div>request_id</div></td><td><div>string</div></td><td><div>唯一请求标识，用于排查问题。</div></td></tr><tr><td colspan="1" rowspan="1"><div>tokenhub_usage</div></td><td colspan="1" rowspan="1"><div>object</div></td><td colspan="1" rowspan="1"><div>用量消耗。</div></td></tr><tr><td colspan="1" rowspan="1"><div>tokenhub_usage.total_tokens</div></td><td colspan="1" rowspan="1"><div>integer</div></td><td colspan="1" rowspan="1"><div>本次任务消耗的 token 数，用于计费/对账。</div></td></tr></tbody></table>

### 5. 响应示例

**生成成功：**

```json

{
  "created": 1787284437,
  "data": [
    {
      "air_wall": {
        "bbox": [
          -46.150852,
          47.925797,
          -6.937543,
          44.305508,
          -25.153587,
          22.927399,
          -0.67803955,
          -3.8229122,
          1.1482356,
          7.252456,
          4.407326,
          1.492669
        ],
        "scene_type": "outdoor"
      },
      "image_url": "https://hunyuan-base-prod-1258344703.cos.ap-guangzhou.myqcloud.com/openapi/text2img/398ddefd8606e2da40d67fd0ba2c0339.png?q-ak\\u003dAKIDRl074nOsGdJ9zjMsCRWP3ShmgS3VtX4S\\u0026q-header-list\\u003d\\u0026q-key-time\\u003d1787283299%3B1787369699\\u0026q-sign-algorithm\\u003dsha1\\u0026q-sign-time\\u003d1787283299%3B1787369699\\u0026q-signature\\u003dcaa743408027047c27f9b58a5b3a997162ee5280\\u0026q-url-param-list\\u003d",
      "mesh_simplified_url": "https://hunyuan-3d-1258344703.cos.ap-guangzhou.myqcloud.com/gen_tmp_test/05abab7cfa854ddf933d8cde043e50d3/d032b44f2d38203b0aef7cba6f4608e5.ply?q-sign-algorithm\\u003dsha1\\u0026q-ak\\u003dAKID17Naks8SJQhxaN5jNBpGduztbwAMRWtK\\u0026q-sign-time\\u003d1787284421%3B1787370821\\u0026q-key-time\\u003d1787284421%3B1787370821\\u0026q-header-list\\u003d\\u0026q-url-param-list\\u003d\\u0026q-signature\\u003d6ef9239ed9f6bc757ad8b148bbc1896eaff756b1",
      "mesh_url": "https://hunyuan-3d-1258344703.cos.ap-guangzhou.myqcloud.com/gen_tmp_test/05abab7cfa854ddf933d8cde043e50d3/f8ba40403c32fa4702b0490235bbcd62.ply?q-sign-algorithm\\u003dsha1\\u0026q-ak\\u003dAKID17Naks8SJQhxaN5jNBpGduztbwAMRWtK\\u0026q-sign-time\\u003d1787284421%3B1787370821\\u0026q-key-time\\u003d1787284421%3B1787370821\\u0026q-header-list\\u003d\\u0026q-url-param-list\\u003d\\u0026q-signature\\u003d8f1d174827d6f8bf357a332c3bc0ece17d24a115",
      "point_url": "https://hunyuan-3d-1258344703.cos.ap-guangzhou.myqcloud.com/gen_tmp_test/05abab7cfa854ddf933d8cde043e50d3/2900cb7bcfd123395c258af86e89f620.ply?q-sign-algorithm\\u003dsha1\\u0026q-ak\\u003dAKID17Naks8SJQhxaN5jNBpGduztbwAMRWtK\\u0026q-sign-time\\u003d1787284420%3B1787370820\\u0026q-key-time\\u003d1787284420%3B1787370820\\u0026q-header-list\\u003d\\u0026q-url-param-list\\u003d\\u0026q-signature\\u003d318af6155121913d1f9c9334d68812a344dcec8d",
      "position_info": "{\\"up_direction\\": [0.08356333782703931, 0...",
      "scene_url": "https://hunyuan-3d-1258344703.cos.ap-guangzhou.myqcloud.com/gen_tmp_test/05abab7cfa854ddf933d8cde043e50d3/e632c15fcf66db300e39fff9d71ab8b1.spz?q-sign-algorithm\\u003dsha1\\u0026q-ak\\u003dAKID17Naks8SJQhxaN5jNBpGduztbwAMRWtK\\u0026q-sign-time\\u003d1787284418%3B1787370818\\u0026q-key-time\\u003d1787284418%3B1787370818\\u0026q-header-list\\u003d\\u0026q-url-param-list\\u003d\\u0026q-signature\\u003d6bbe2526c4ac2f155d65e1e6908ca2907d4e87e6",
      "super_resolution_image_url": "https://hunyuan-base-prod-1258344703.cos.ap-guangzhou.myqcloud.com/openapi/text2img/7fcbe0fe146d8d564fab2651886bab76.png?q-ak\\u003dAKIDRl074nOsGdJ9zjMsCRWP3ShmgS3VtX4S\\u0026q-header-list\\u003d\\u0026q-key-time\\u003d1787283327%3B1787369727\\u0026q-sign-algorithm\\u003dsha1\\u0026q-sign-time\\u003d1787283327%3B1787369727\\u0026q-signature\\u003d6eb63978c077a5637d77ba8bac558f9733f985c6\\u0026q-url-param-list\\u003d"
    }
  ],
  "id": "4-WandVideo-01105813c9e443ed977daa511a0700b3",
  "status": "succeeded",
  "version": "1",
  "tokenhub_usage": {
    "total_tokens": 8000000
  },
  "request_id": "450ffc9c-29fb-4549-80a7-ee48549189cd"
}
```

### 6. 状态码

| status | 含义 | 处理建议 |
| --- | --- | --- |
| queued | 排队中 | 继续轮询。 |
| running | 生成中 | 每 3~5 秒轮询一次，直至 status=succeeded。 |
| succeeded | 生成成功 | 从 `data` 中获取各格式文件 URL。 |
| failed | 生成失败 | 服务端生成出错，请重试；持续失败请联系技术支持并附任务 id。 |
| cancelled | 已取消 | 任务已取消，需重新发起。 |
| unknown | 未知状态 | 请重试或联系技术支持。 |
