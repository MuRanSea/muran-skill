<!-- Official source: https://cloud.tencent.com/document/product/1823/137070 -->
<!-- Source SHA-256: c4007f7887dd26ea24a32aebd76542e9d3dc42546e9b119ea323a5c1a8758f77 -->

# Tripo-3D-Format 调用指南

官方来源：https://cloud.tencent.com/document/product/1823/137070
最近更新时间：2026-10-24 13:10:22

## 简介

Tripo 格式转换接口，将 3D 模型转换为其他格式，支持可选的网格处理、贴图烘焙和导出设置。

## 对接说明

### 1. 获取 API Key

1. 进入 [API Key 管理](https://console.cloud.tencent.com/tokenhub/apikey) 页面，单击**创建 API Key**。操作详情请参见 [创建 API Key](https://cloud.tencent.com/document/product/1823/130090#40882178-aaf2-48c9-8559-dffc083a79bc)。

2. 创建完成后，请您务必**复制并妥善保管 API Key**，在后续配置到工具的流程中将会使用该信息。

![](https://qcloudimg.tencent-cloud.cn/image/document/85b287d2907c8ba9319cc2ab16cc248d.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/85b287d2907c8ba9319cc2ab16cc248d.png)

**说明：**

每个账户的密钥都只能当前账户查询，主账户的密钥信息子账户是看不到，子账户如果需要调用接口，需要使用账户自行创建密钥信息。

如果子账户没有办法创建，可能是没有权限创建密钥，需要主账户授权，主账户登录之后点击用户列表，在对应的子账户后面选择授权，会弹出关联策略的弹窗，输入授权策略名称之后搜索，选择对应的策略点击确认。

授权策略：QcloudTokenhubFullAccess

### 2. 并发额度

默认提供1个并发，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后，才能开始处理下一个任务。

并发任务数：表示在调用对应服务的时段内最大可运行的任务数，该任务未完成时，无法提交下一个任务，该任务完成后，可提交下一个任务。

## 接口文档

### 提交 Tripo 格式转换任务

**输入参数**

| 参数名称 | 必选 | 类型 | 参数描述 |
| --- | --- | --- | --- |
| model | 是 | string | 模型名称，默认为：tripo-3d-format  示例值：tripo-3d-format |
| input | 是 | string | 模型 URL：可公开访问的 3D 模型文件直链。  示例： https://example.com/model.glb    支持格式：GLB、GLTF、FBX、OBJ、STL  最大文件大小：**150 MB** |
| format | 是 | string | 目标导出格式。  GLTF：Web 查看器、WebGL 引擎。  FBX：Unreal、Unity、DCC 工具。  USDZ：Apple AR Quick Look。  OBJ：传统交换格式，无动画。  STL：3D 打印，仅几何体。  3MF：3D 打印，支持颜色。    **说明：**  GLTF：Web 查看器、WebGL 引擎（Three.js、Babylon.js）。  FBX：Unreal、Unity、DCC 工具（Maya、Blender）。  USDZ：Apple AR Quick Look、RealityKit。  OBJ：传统交换格式，不支持动画。  STL / 3MF：3D 打印，仅几何体。 |
| quad | 否 | boolean | 是否输出四边面网格（四边形多边形）而非三角面。若未设置 face\_limit，默认面数为 10,000。  默认值：false    **说明：**  启用 quad 会强制输出格式为 FBX。 |
| force\_symmetry | 否 | boolean | 强制对称。仅 quad 为 true 时有效。  默认值：false |
| face\_limit | 否 | integer | 转换时的输出网格最大面数。不传时保持原模型面数。 |
| flatten\_bottom | 否 | boolean | 展平模型底部。  默认值：false |
| flatten\_bottom\_threshold | 否 | float | 展平深度阈值。  默认值：0.01 |
| texture\_size | 否 | integer | 漫反射贴图尺寸（像素）。  默认值：4096 |
| texture\_format | 否 | string | 贴图图像格式。  JPEG：默认，文件体积最小。  PNG：无损，支持透明度。  WEBP：现代 Web 格式。  BMP / DPX / HDR / OPEN\_EXR / TARGA / TIFF：专业用途。  默认值: JPEG |
| bake | 否 | boolean | 将高级材质烘焙为基础贴图。  默认值：true |
| pack\_uv | 否 | boolean | 将所有 UV 打包为统一布局。  默认值：false |
| export\_vertex\_colors | 否 | boolean | 包含顶点颜色。仅对 OBJ 和 GLTF 有效。  默认值：false |
| pivot\_to\_center\_bottom | 否 | boolean | 将轴心点移至底部中心。  默认值：false |
| scale\_factor | 否 | float | 导出模型的缩放系数。  默认值：1 |
| with\_animation | 否 | boolean | 包含骨骼和动画数据。  默认值：true |
| animate\_in\_place | 否 | boolean | 原地动画（无根骨位移）。  默认值：false |
| part\_names | 否 | string[] | 要导出的部件名称，来自网格 / 分割数据。 |
| export\_orientation | 否 | string | 导出朝向（前向轴）。  +x：默认，X 轴正方向朝前。  -x：X 轴负方向朝前。  -y：Y 轴负方向朝前。  +y：Y 轴正方向朝前。  默认值：+x |
| fbx\_preset | 否 | string | FBX 兼容性预设。（仅导出 FBX 时生效）。  blender：针对 Blender 导入优化。  3dsmax：针对 3ds Max 导入优化。  mixamo：兼容 Mixamo 绑骨  默认值：blender。 |

**说明：**

**格式转换触发高级（传入以下任一非默认值参数即为 10 积分）:**

quad、face\_limit、flatten\_bottom、flatten\_bottom\_threshold、texture\_size、texture\_format、pivot\_to\_center\_bottom、scale\_factor

**输出参数**

| 参数名称 | 类型 | 描述 |
| --- | --- | --- |
| id | string | 任务 id（有效期24小时）。  示例值：1315932989749215232 |
| request\_id | string | 唯一请求 id，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 request\_id）。定位问题时需要提供该次请求的 request\_id。 |
| object | string | 返回对象类型。3d 任务固定返回 3d\_job。 |
| created\_at | integer | 任务创建时间。 |
| status | string | completed：任务成功，failed：任务失败，in\_progress：执行中，queued：等待中。  示例值：completed |

### 查询 Tripo 格式转换任务

**输入参数**

| 参数名称 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| model | 是 | string | 模型名称，默认为：tripo-3d-format  示例值：tripo-3d-format |
| id | 是 | string | 任务 id。  示例值：1357237233311637504 |

**输出参数**

<table><colgroup><col/><col/><col/></colgroup><tbody><tr><td><div>参数名称</div></td><td><div>类型</div></td><td><div>描述</div></td></tr><tr><td><div>status</div></td><td><div>string</div></td><td><div>completed：任务成功，failed：任务失败，in_progress：执行中，queued：等待中。</div><div>示例值：completed</div></td></tr><tr><td><div>request_id</div></td><td><div>string</div></td><td><div>唯一请求 id，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 request_id）。定位问题时需要提供该次请求的 request_id。</div></td></tr><tr><td><div>output</div></td><td><div>object</div></td><td><div>输出结果（TripoResult，任务完成时返回）</div></td></tr><tr><td><div>output.model_url</div></td><td><div>string</div></td><td><div>转换后的模型下载 URL</div></td></tr><tr><td><div>input</div></td><td><div>string</div></td><td><div>输入参数回显</div></td></tr><tr><td><div>object</div></td><td><div>string</div></td><td><div>返回对象类型。3d 任务固定返回 3d_job。</div></td></tr><tr><td><div>created_at</div></td><td><div>integer</div></td><td><div>任务创建时间。</div></td></tr><tr><td><div>completed_at</div></td><td><div>integer</div></td><td><div>任务完成时间。</div></td></tr><tr><td colspan="1" rowspan="1"><div>credits_consumed</div></td><td colspan="1" rowspan="1"><div>number</div></td><td colspan="1" rowspan="1"><div>当前任务实际消耗的积分数。</div></td></tr></tbody></table>

## 示例

### 提交 Tripo 格式转换任务

**输入示例**

```java
curl -X POST 'https://tokenhub.tencentmaas.com/v1/api/3d/submit' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -H 'Accept: */*' \\
  -H 'Connection: keep-alive' \\
  -d '{
    "model": "tripo-3d-format",
    "format":"GLTF",
     "input": "https://example.com/test.fbx"
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

### 查询 Tripo 格式转换任务

**输入示例**

```java
curl -X POST 'https://tokenhub.tencentmaas.com/v1/api/3d/query' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -H 'Connection: keep-alive' \\
  -d '{
    "model": "tripo-3d-format",
    "id": "14721*****320"
  }'
```

**输出示例**

```java
{
  "status": "completed",
  "input": "{\\"format\\":\\"GLTF\\",\\"original_model_id\\":\\"XXXXX\\"}",
  "object": "3d_job",
  "output": {
      "model_url": "https://vcg-prod-1258344699.cos.ap-guangzhou.tencentcos.cn/**********12.glb"
   },
  "request_id": "XXXXX-c925-4dda-90f0-XXXXX",
  "credits_consumed": 5,
  "created_at": 1785989483,
  "completed_at": 1785989483
}
```
