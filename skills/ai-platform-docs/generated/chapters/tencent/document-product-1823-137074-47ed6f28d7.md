<!-- Official source: https://cloud.tencent.com/document/product/1823/137074 -->
<!-- Source SHA-256: c3c866c72ca1b763bec140ff4a637a9621d5b4011e1903cf06f78510a5021963 -->

# Tripo-3D 调用指南

官方来源：https://cloud.tencent.com/document/product/1823/137074
最近更新时间：2026-10-21 10:09:00

本文档适用范围：tripo-3d-3.1、tripo-3d-p1、tripo-3d-p2

## 简介

Tripo 生3d 接口，根据输入的文本描述/图片智能生成3d。

## 对接说明

### 1. 获取 API Key

1. 进入 [API Key 管理](https://console.cloud.tencent.com/tokenhub/apikey) 页面，单击**创建 API Key**。操作详情请参见 [创建 API Key](https://cloud.tencent.com/document/product/1823/130090#40882178-aaf2-48c9-8559-dffc083a79bc)。

2. 创建完成后，请您务必**复制并妥善保管 API Key**，在后续配置到工具的流程中将会使用该信息。

![](https://qcloudimg.tencent-cloud.cn/image/document/debe9f0c03e4aa75ba429e7513d9a266.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/debe9f0c03e4aa75ba429e7513d9a266.png)

**说明：**

每个账户的密钥都只能当前账户查询，主账户的密钥信息子账户是看不到，子账户如果需要调用接口，需要使用账户自行创建密钥信息。

如果子账户没有办法创建，可能是没有权限创建密钥，需要主账户授权，主账户登录之后点击用户列表，在对应的子账户后面选择授权，会弹出关联策略的弹窗，输入授权策略名称之后搜索，选择对应的策略点击确认。

授权策略：QcloudTokenhubFullAccess

### 2. 并发额度

默认提供1个并发，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后，才能开始处理下一个任务。

并发任务数：表示在调用对应服务的时段内最大可运行的任务数，该任务未完成时，无法提交下一个任务，该任务完成后，可提交下一个任务。

## 接口文档

#### 提交 Tripo 生3d 任务

**输入参数**

<table><colgroup><col/><col/><col/><col/></colgroup><tbody><tr><td><div>参数名称</div></td><td><div>必选</div></td><td><div>类型</div></td><td><div>参数描述</div></td></tr><tr><td><div>model</div></td><td><div>是</div></td><td><div>string</div></td><td><div>tripo 生3d 模型名称。可选项：tripo-3d-3.1、tripo-3d-p1、tripo-3d-p2。</div><div>默认为 tripo-3d-3.1。</div><div>示例值：tripo-3d-3.1</div></td></tr><tr><td><div>prompt</div></td><td><div>否</div></td><td><div>string</div></td><td><div>文本提示词，最多 1024 个字符。仅使用文生3D 功能时生效。</div><div>描述形状、材质、风格和尺寸。</div></td></tr><tr><td><div>input</div></td><td><div>否</div></td><td><div> string</div></td><td><div>图片生成图像来源。仅使用图生3D 功能时生效。</div><div>支持 PNG、JPEG、WebP，最大 20 MB，建议分辨率不低于 256 × 256 px。主体应清晰可见，背景干净，遮挡尽量少。</div><div> </div><div>示例值：https://cos.ap-guangzhou.myqcloud.com/image.jpg</div></td></tr><tr><td><div>inputs</div></td><td><div>否</div></td><td><div>array of object</div></td><td><div>多视图生成图像来源。仅使用多图生3D 功能时生效。主体应清晰可见，遮挡最少。</div><div>正面视图不可省略。其他视图可省略，但至少需要 2 张图像。</div><div>所有图像应在一致光照下拍摄同一物体。</div><div>支持格式：PNG、JPEG、WebP</div><div>推荐分辨率：至少 256 × 256 px。</div><div>详情请参见 inputs 数据结构。</div></td></tr><tr><td><div>negative_prompt</div></td><td><div>否</div></td><td><div>string</div></td><td><div>反向提示词，最多 255 个字符。描述不希望在生成模型中出现的内容。</div><div>示例值："blurry, low quality, broken mesh"。</div></td></tr><tr><td><div>image_seed</div></td><td><div>否</div></td><td><div>integer</div></td><td><div>内部文本转图像阶段的随机种子。</div><div>控制从文本提示词生成的参考图像，然后再进行 3d 转换。若未设置，每次会使用随机种子。</div><div></div><div><b>注意：</b></div><div>建议谨慎使用该参数。由于不同 seed 可能产生不同质量的结果，固定 seed 可能会限制探索更优生成结果的机会。</div><div>seed 取值范围：-2147483648 ~ 2147483647。</div></td></tr><tr><td><div>model_seed</div></td><td><div>否</div></td><td><div>integer</div></td><td><div>几何体生成的随机种子。</div><div>使用相同种子和相同输入将生成相同的 3d 网格。</div><div>若未设置，每次会使用随机种子。</div><div></div><div><b>注意：</b></div><div>建议谨慎使用该参数。由于不同 seed 可能产生不同质量的结果，固定 seed 可能会限制探索更优生成结果的机会。</div><div>seed 取值范围：-2147483648 ~ 2147483647。</div></td></tr><tr><td><div>enable_image_autofix</div></td><td><div>否</div></td><td><div>boolean</div></td><td><div>是否在生成前自动优化输入图像。启用后，系统将增强低分辨率或低质量图像以改善 3d 生成效果。</div><div>默认为 false。</div></td></tr><tr><td><div>face_limit</div></td><td><div>否</div></td><td><div>integer</div></td><td><div>输出网格的最大面数。省略时模型使用自适应拓扑。</div><div>model 为 tripo-3d-3.1时：</div><div>纯三角面标准模式面数上限 1,500,000，超清模式上限 2,000,000。</div><div>四边面（quad: true）标准模式面数上限 150,000。</div><div>游戏资产推荐：50,000 – 100,000。web/移动端：10,000 – 50,000。</div><div>开启 smart_low_poly: true 时，面数限制与模型版本无关，统一为： 三角面 500 – 20,000，四边面 500 – 10,000。</div><div>model 为 tripo-3d-p1时：</div><div>输出网格的最大面数。支持范围：50 – 20,000。</div><div>省略时自适应确定面数。</div><div>最佳质量建议：简单模型从 150 面起步，复杂模型从 250 面起步。面数过低可能导致生成质量下降。</div><div>model 为 tripo-3d-p2时：</div><div>输出网格最大面数。三角面范围为 48–50,000；quad=true 时范围为 48–25,000；省略时自动确定。</div><div>最佳质量建议：简单模型从 150 面起步，复杂模型从 250 面起步。面数过低可能导致生成质量下降。</div></td></tr><tr><td><div>texture</div></td><td><div>否</div></td><td><div>boolean</div></td><td><div>是否为模型生成贴图。</div><div>设为 false 可获取无贴图的纯几何体。</div><div>默认为 true。</div></td></tr><tr><td><div>pbr</div></td><td><div>否</div></td><td><div>boolean</div></td><td><div>启用 pbr 材质贴图（base_color、metallic、roughness、normal）。</div><div>当 pbr 设为 true 时，texture 会自动强制设为 true。</div><div>默认为 true。</div></td></tr><tr><td><div>texture_seed</div></td><td><div>否</div></td><td><div>integer</div></td><td><div>贴图生成的随机种子。使用相同种子将生成相同的贴图。若未设置，每次会使用随机种子。如需获取相同几何体但不同贴图的模型，请保持 model_seed 不变并更改 texture_seed。</div><div><b>注意：</b></div><div>建议谨慎使用该参数。由于不同 seed 可能产生不同质量的结果，固定 seed 可能会限制探索更优生成结果的机会。</div><div>seed 取值范围：-2147483648 ~ 2147483647。</div></td></tr><tr><td><div>texture_alignment</div></td><td><div>否</div></td><td><div>string</div></td><td><div>确定 3d 模型中纹理对齐的优先级。</div><div>仅单图和多图输入时生效。</div><div>可选值包括：original_image、geometry。</div><div>original_image：优先保证与源图像的视觉保真度，生成纹理与原图更相似，但可能导致轻微 3d 不一致。</div><div>geometry：优先保证三维结构精度，使纹理更好地贴合模型几何形状，但可能与原图外观略有偏差。</div><div>默认值为 original_image。</div></td></tr><tr><td><div>texture_quality</div></td><td><div>否</div></td><td><div>string</div></td><td><div>贴图质量等级。</div><div>可选值包括：fast，standard，detailed，extreme。</div><div>fast：生成最快，以细节换速度；输出贴图尺寸与 standard 相同。 需要贴图版本 v3.5-20260815；积分与 standard 相同。</div><div>standard：质量与速度的平衡。</div><div>detailed：更高保真度，生成速度较慢。</div><div>extreme：8k 贴图，最高保真度。相比 detailed 额外消耗积分。</div><div>默认为 standard。</div><div>fast 仅在贴图版本 v3.5-20260815 下可用。生成接口需将 texture_version 设为该版本。</div></td></tr><tr><td><div>texture_version</div></td><td colspan="1" rowspan="1"><div>否</div></td><td colspan="1" rowspan="1"><div>string</div></td><td><div>独立指定贴图模型，与几何体 model 解耦。</div><div>v3.5-20260815：最新贴图模型。使用 texture_quality=fast 与 delight 时必填。</div><div>v3.0-20250812：v3.x 与 P 系列几何体的默认值。</div><div>v2.5-20250123：v2.5-20250123 几何体的默认值。</div><div>省略时按上表根据几何体 model 自动推导。</div></td></tr><tr><td><div>delight</div></td><td colspan="1" rowspan="1"><div>否</div></td><td colspan="1" rowspan="1"><div>boolean</div></td><td><div>贴图前去除参考图中的光照信息。设为 false 可保留原有明暗。仅 v3.5-20260815 贴图模型支持，更早的贴图版本会忽略该参数。</div><div>默认为 true。</div></td></tr><tr><td><div>auto_size</div></td><td><div>否</div></td><td><div>boolean</div></td><td><div>是否自动将生成的模型缩放至真实世界尺寸。启用后，模型尺寸将以米为单位，适用于 ar/vr 或游戏引擎场景。</div><div>默认为 false。</div></td></tr><tr><td><div>orientation</div></td><td><div>否</div></td><td><div>string</div></td><td><div>设置模型方向。</div><div>仅单图和多图输入时生效；</div><div>default：自动朝向。</div><div>align_image：将模型对齐至输入图像的视角。</div><div>仅当 texture 为 true 时生效，未开启贴图时此参数无效。</div><div>默认值为 default。</div></td></tr><tr><td><div>quad</div></td><td><div>否</div></td><td><div>boolean</div></td><td><div>model 为 tripo-3d-p2时有效。</div><div>是否输出四边面网格，默认 false；开启后 face_limit 上限为25000。</div></td></tr><tr><td><div>compress</div></td><td><div>否</div></td><td><div>string</div></td><td><div>model 为 tripo-3d-3.1时有效。</div><div>压缩类型。</div><div>geometry：meshopt 压缩，减小文件体积。</div></td></tr><tr><td><div>smart_low_poly</div></td><td><div>否</div></td><td><div>boolean</div></td><td><div>model 为 tripo-3d-3.1时有效。</div><div>是否生成具有手工风格、干净拓扑的低面数模型。</div><div>最适合简单、非复杂的输入。复杂模型可能偶尔失败。</div><div>默认为 false。</div></td></tr><tr><td><div>generate_parts</div></td><td><div>否</div></td><td><div>boolean</div></td><td><div>model 为 tripo-3d-3.1时有效。</div><div>生成可编辑的分割部件。</div><div>与 texture=true、pbr=true 或 quad=true 不兼容。要使用此功能，需将这三者均设为 false。</div><div>默认为 false。</div></td></tr><tr><td><div>export_uv</div></td><td><div>否</div></td><td><div>boolean</div></td><td><div>控制生成过程中的 uv 展开。设为 false 可加快生成速度并减小文件体积。uv 展开将在贴图阶段处理。</div><div>默认为 true。</div></td></tr><tr><td><div>geometry_quality</div></td><td><div>否</div></td><td><div>string</div></td><td><div>model 为 tripo-3d-3.1时有效。</div><div>几何体质量等级。</div><div>standard：质量与速度的平衡。</div><div>detailed：ultra 模式，更精细的几何细节。</div><div>默认为 standard。</div></td></tr></tbody></table>

**输出参数**

| 参数名称 | 类型 | 描述 |
| --- | --- | --- |
| id | string | 任务 id（有效期24小时）。  示例值：1315932989749215232 |
| request\_id | string | 唯一请求 id，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 request\_id）。定位问题时需要提供该次请求的 request\_id。 |
| object | string | 返回对象类型。3d 任务固定返回 3d\_job。 |
| created\_at | integer | 任务创建时间。 |
| status | string | completed：任务成功，failed：任务失败，in\_progress：执行中，queued：等待中。  示例值：completed |

#### 查询 Tripo 生3d 任务

**输入参数**

| 参数名称 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| model | 是 | string | tripo 生3d 模型名称。可选项：tripo-3d-3.1、tripo-3d-p1、tripo-3d-p2。  默认为 tripo-3d-3.1。  示例值：tripo-3d-3.1 |
| id | 是 | string | 任务 id。  示例值：1357237233311637504 |

**输出参数**

| 参数名称 | 类型 | 描述 |
| --- | --- | --- |
| status | string | completed：任务成功，failed：任务失败，in\_progress：执行中，queued：等待中。  示例值：completed |
| request\_id | string | 唯一请求 id，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 request\_id）。定位问题时需要提供该次请求的 request\_id。 |
| input | object | 本次任务实际使用的输入信息。详情请参见 [input](https://cloud.tencent.com/document/product/1823/137074#5bf616c7-2729-46f8-8cf4-24a5924b40a6) 数据结构。 |
| output | object | 任务生成结果。详情请参见 [output](https://cloud.tencent.com/document/product/1823/137074#199a7da6-862d-43e5-8bf9-92ed435a5509) 数据结构。 |
| object | string | 返回对象类型。3d 任务固定返回 3d\_job。 |
| created\_at | integer | 任务创建时间。 |
| completed\_at | integer | 任务完成时间。 |

## 示例

#### 提交 Tripo 生3d 任务

**输入示例**

```java
curl -X POST 'https://tokenhub.tencentmaas.com/v1/api/3d/submit' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
    "model": "tripo-3d-3.1",
    "prompt": "一只可爱的小猫"
  }'
```

**输出示例**

```java
{
  "id": "14721*****320",
  "request_id": "11f64379-bb0b-46b2-b89f-17d75fc12365",
  "object": "3d_job",
  "created_at": 1784885898,
  "status": "queued"
}
```

#### 查询 Tripo 生3d 任务

**输入示例**

```java
curl -X POST 'https://tokenhub.tencentmaas.com/v1/api/3d/query' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
    "model": "tripo-3d-3.1",
    "id": "14721*****320"
  }'
```

**输出示例**

```java
{
  "status": "completed",
  "input": {
    "prompt": "一只可爱的小猫",
    "pbr": true,
    "texture": true,
    "export_uv": true,
    "geometry_quality": "standard",
    "texture_alignment": "geometry",
    "model_version": "v3.1-20260211"
  },
  "output": {
    "type": "text_to_model",
    "model_url": "https://vcg-prod-1258344699.cos.ap-guangzhou.tencentcos.cn/**********12.glb",
    "generated_image_url": "https://vcg-prod-1258344699.cos.ap-guangzhou.tencentcos.cn/**********12.png",
    "rendered_image_url": "https://vcg-prod-1258344699.cos.ap-guangzhou.tencentcos.cn/**********12.png"
  },
  "created_at": 1785989483,
  "completed_at": 1785989483
}
```

## 数据结构

#### inputs

**本次任务实际使用的输入信息。**

| 参数名称 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| front | 是 | string | 正视图图片。 |
| back | 否 | string | 后视图图片。 |
| left | 否 | string | 左视图图片。 |
| right | 否 | string | 右视图图片。 |

#### input

**本次任务实际使用的输入信息。**

| 参数名称 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| prompt | 否 | string | 文生 3D 的输入提示词。 |
| pbr | 否 | boolean | 是否生成 pbr 材质。 |
| texture | 否 | boolean | 是否生成纹理贴图。 |
| export\_uv | 否 | boolean | 是否导出 uv 信息。 |
| geometry\_quality | 否 | string | 本次任务实际使用的几何模型质量。    示例值：standard |
| texture\_alignment | 否 | string | 纹理对齐方式    示例值：original\_image。 |
| model\_version | 否 | string | 本次任务实际使用的原厂模型版本。    示例值：v3.1-20260211 |

#### output

**任务生成结果。**

| 参数名称 | 类型 | 描述 |
| --- | --- | --- |
| type | string | 生成任务类型。    示例值：multiview\_to\_model |
| model\_url | string | 生成的3d 模型文件下载地址。 |
| generated\_image\_url | string | 生成的参考图片地址 |
| rendered\_image\_url | string | 生成结果的渲染预览图地址。 |
