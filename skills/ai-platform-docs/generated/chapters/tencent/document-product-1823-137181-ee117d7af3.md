<!-- Official source: https://cloud.tencent.com/document/product/1823/137181 -->
<!-- Source SHA-256: 373706bef8609761ac6d8577b5b7d75e95a75317de5dc804c9fbd7b0097fa597 -->

# HY-3D 调用指南

官方来源：https://cloud.tencent.com/document/product/1823/137181
最近更新时间：2026-09-29 10:46:48

本文档适用范围：hy-3d-3.0，hy-3d-3.1

## 简介

混元生3d 接口，基于混元大模型，根据输入的文本描述/图片智能生成3d。

## 对接说明

### 1. 获取 API Key

1. 进入 [API Key 管理](https://console.cloud.tencent.com/tokenhub/apikey) 页面，单击**创建 API Key**。操作详情请参见 [创建 API Key](https://cloud.tencent.com/document/product/1823/130090#40882178-aaf2-48c9-8559-dffc083a79bc)。

2. 创建完成后，请您务必**复制并妥善保管 API Key**，在后续配置到工具的流程中将会使用该信息。

![](https://qcloudimg.tencent-cloud.cn/image/document/9afdfd306d98c7a021f935da00660a67.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/9afdfd306d98c7a021f935da00660a67.png)

**说明：**

每个账户的密钥都只能当前账户查询，主账户的密钥信息子账户是看不到，子账户如果需要调用接口，需要使用账户自行创建密钥信息。

如果子账户没有办法创建，可能是没有权限创建密钥，需要主账户授权，主账户登录之后点击用户列表，在对应的子账户后面选择授权，会弹出关联策略的弹窗，输入授权策略名称之后搜索，选择对应的策略点击确认。

授权策略：QcloudTokenhubFullAccess

### 2. 并发额度

默认提供3个并发，代表最多能同时处理3个已提交的任务，上一个任务处理完毕后，才能开始处理下一个任务。

并发任务数：表示在调用对应服务的时段内最大可运行的任务数，该任务未完成时，无法提交下一个任务，该任务完成后，可提交下一个任务。

## 接口文档

### 提交混元生3d 专业版任务

**输入参数**

| 参数名称 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| model | 是 | string | 混元生3d 模型名称，默认为 hy-3d-3.0，可选项：hy-3d-3.0，hy-3d-3.1。  选择 hy-3d-3.1版本时，low\_poly 参数不可用。  示例值：hy-3d-3.1 |
| prompt | 否 | string | 文生3d，3d 内容的描述，中文正向提示词。  最多支持1024个 utf-8 字符。  image\_base64、image\_url 和 prompt 必填其一，且 prompt 和 image\_base64/image\_url 不能同时存在。  示例值：一只小猫 |
| image\_base64 | 否 | string | 输入图 base64 数据。  大小: 单边分辨率要求不小于128，不大于5000，大小≤6m (因 base64编码后会大30%左右)。  格式: jpg，png，jpeg，webp。  image\_base64、image\_url 和 prompt 必填其一，且 prompt 和 image\_base64/image\_url 不能同时存在。  示例值：/9j/4QlQaHR0c...N6a2M5ZCI |
| image\_url | 否 | string | 输入图 url。  大小: 单边分辨率要求不小于128，不大于5000，大小≤8m。  格式: jpg，png，jpeg，webp。  image\_base64、image\_url 和 prompt 必填其一，且 prompt 和 image\_base64/image\_url 不能同时存在。  示例值：https://cos.ap-guangzhou.myqcloud.com/image.jpg |
| multi\_view\_images | 否 | array of view\_image | 多视角的模型图片，视角参考值：  left：左视图  right：右视图  back：后视图  top：顶视图  bottom：底视图  left\_front：左前45°视图  right\_front：右前45°视图  每个视角仅限制一张图片。  图片大小限制：图片大小总和小于100M，单图小于8M。  图片分辨率限制：单边分辨率小于5000且大于128。  支持图片格式：支持 jpg 或 png。  详情请参见 [view\_image](https://cloud.tencent.com/document/product/1823/137181#917bb676-4a51-4ab3-9e37-f980ec67ea6d) 数据结构。 |
| enable\_pbr | 否 | boolean | 是否开启 pbr 材质生成，默认 false。  示例值：true |
| face\_count | 否 | integer | 生成3d 模型的面数，默认值为500000。可支持生成面数范围，参考值：3000-1500000。generate\_type 中选择 low\_poly 时，此参数不生效。  取值范围：[3000, 1500000]。  示例值：100000 |
| generate\_type | 否 | string | 生成任务类型，默认 Normal。  枚举值：  Normal： 可生成带纹理的几何模型。  LowPoly： 可生成智能拓扑后的模型，face\_count 参数不生效。  Geometry： 可生成不带纹理的几何模型（白模），enable\_pbr 参数不生效。  Sketch： 可输入草图或线稿图生成模型，此模式下 image\_base64、image\_url 和 prompt 可一起输入。  示例值：Normal |
| polygon\_type | 否 | string | 该参数仅在 generate\_type 中选择 LowPoly 模式可生效。  多边形类型，表示模型的表面由几边形网格构成，默认为 triangle,参考值:  triangle: 三角形面。  quadrilateral: 四边形面与三角形面混合生成。  示例值：triangle |
| result\_format | 否 | string | 生成模型的格式，仅限制生成一种格式； 生成模型文件组默认返回 obj、glb 格式（generate\_type 选择 Geometry 时，默认为 glb 格式）； 可选值：stl，usdz，fbx。  示例值：stl |

**输出参数**

| 参数名称 | 类型 | 描述 |
| --- | --- | --- |
| id | string | 任务 id（有效期24小时）。  示例值：1315932989749215232 |
| request\_id | string | 唯一请求 id，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 request\_id）。定位问题时需要提供该次请求的 request\_id。 |
| object | string | 返回对象类型。3d 任务固定返回 3d\_job。 |
| created\_at | integer | 任务创建时间。 |
| status | string | completed：任务成功，failed：任务失败，in\_progress：执行中，queued：等待中。  示例值：completed |

### 查询混元生3d 专业版任务

**输入参数**

| 参数名称 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| model | 是 | string | 混元生3d 模型名称，默认为 hy-3d-3.0，可选项：hy-3d-3.0，hy-3d-3.1。  选择 hy-3d-3.1版本时，LowPoly 参数不可用。  示例值：hy-3d-3.1 |
| id | 是 | string | 任务 id。  示例值：1357237233311637504 |

**输出参数**

| 参数名称 | 类型 | 描述 |
| --- | --- | --- |
| status | string | completed：任务成功，failed：任务失败，in\_progress：执行中，queued：等待中。  示例值：completed |
| request\_id | string | 唯一请求 id，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 request\_id）。定位问题时需要提供该次请求的 request\_id。 |
| object | string | 返回对象类型。3d 任务固定返回 3d\_job。 |
| created\_at | integer | 任务创建时间。 |
| completed\_at | integer | 任务完成时间。 |
| data | array of object | 生成结果列表，包含生成的 3d 模型文件及相关资源信息。详情请参见 [data](https://cloud.tencent.com/document/product/1823/137181#c9bb0852-073e-4e2e-8da9-5359d2b770bb) 数据结构。 |

## 示例

### 提交混元生3d 专业版任务

**输入示例**

```java
curl -X POST 'https://tokenhub.tencentmaas.com/v1/api/3d/submit' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
    "model": "hy-3d-3.1",
    "prompt": "一只小狗"
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

### 查询混元生3d 专业版任务

**输入示例**

```java
curl -X POST 'https://tokenhub.tencentmaas.com/v1/api/3d/query' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
    "model": "hy-3d-3.1",
    "id": "14721*****320"
  }'
```

**输出示例**

```java
{
"request_id":"ab3beaeb-b4aa-4387-b5aa-e2ec1bba4ef0",
"object":"3d_job",
"created_at":1784884760,
"completed_at":1784884760,
"status":"completed",
"data":[
{

"type":"obj",
"url":"https://hunyuan-prod-1258344699.cos.ap-guangzhou.tencentcos.cn/3d/output/1254418*****d3272_0.zip",
"preview_image_url":"https://hunyuan-prod-1258344699.cos.ap-guangzhou.tencentcos.cn/3d/output/12544*****2-89ec2ff1967a_0.png"
},
{
"type":"glb",
"url":"https://hunyuan-prod-1258344699.cos.ap-guangzhou.tencentcos.cn/3d/output/125441************ec2ff1967a_0.glb",
"preview_image_url":"https://hunyuan-prod-1258344699.cos.ap-guangzhou.tencentcos.cn/3d/output/125441*******-bbe2-89ec2ff1967a_0.png"
}
]
}
```

## 数据结构

### data

**生成结果对象。**

| 参数名称 | 类型 | 描述 |
| --- | --- | --- |
| type | string | 生成结果文件类型。  示例值：obj |
| url | string | 生成结果文件下载地址。 |
| preview\_image\_url | string | 生成结果预览图下载地址。 |

### view\_image

**多视角输入图片对象。**

| 参数名称 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| view\_type | 是 | string | 图片视角。 |
| view\_image\_url | 是 | string | 图片 url。 |
