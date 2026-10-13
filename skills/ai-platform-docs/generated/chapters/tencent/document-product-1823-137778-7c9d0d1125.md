<!-- Official source: https://cloud.tencent.com/document/product/1823/137778 -->
<!-- Source SHA-256: db94f69194c5d12a2018253399e9e3c12cb6d504e08e968489e4ba632cea88ae -->

# HY-3D-Retopology 调用指南

官方来源：https://cloud.tencent.com/document/product/1823/137778
最近更新时间：2026-09-09 18:13:31

## 简介

智能拓扑接口，采用 Polygon 1.5模型，输入3D 高模后，可生成布线规整，较低面数的3D 模型。

## 对接说明

### 1. 获取 API Key

1. 进入 [API Key 管理](https://console.cloud.tencent.com/tokenhub/apikey) 页面，单击**创建 API Key**。操作详情请参见 [创建 API Key](https://cloud.tencent.com/document/product/1823/130090#40882178-aaf2-48c9-8559-dffc083a79bc)。

2. 创建完成后，请您务必**复制并妥善保管 API Key**，在后续配置到工具的流程中将会使用该信息。

![](https://qcloudimg.tencent-cloud.cn/image/document/9b63790b95ba700b39de3ea2efe2e2a8.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/9b63790b95ba700b39de3ea2efe2e2a8.png)

**说明：**

每个账户的密钥都只能当前账户查询，主账户的密钥信息子账户是看不到，子账户如果需要调用接口，需要使用账户自行创建密钥信息。

如果子账户没有办法创建，可能是没有权限创建密钥，需要主账户授权，主账户登录之后点击用户列表，在对应的子账户后面选择授权，会弹出关联策略的弹窗，输入授权策略名称之后搜索，选择对应的策略点击确认。

授权策略：QcloudTokenhubFullAccess

### 2. 并发额度

默认提供1个并发，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后，才能开始处理下一个任务。

并发任务数：表示在调用对应服务的时段内最大可运行的任务数，该任务未完成时，无法提交下一个任务，该任务完成后，可提交下一个任务。

## 接口文档

### 提交智能拓扑任务

**输入参数**

| 参数名称 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| model | 是 | string | 智能拓扑模型名称，默认为 hy-3d-retopology。  示例值：hy-3d-retopology |
| file\_3d | 是 | object | 源3D 模型文件。  type 可选值：obj，glb，fbx  详情请参见 [file\_3d](https://cloud.tencent.com/document/product/1823/137778#44f6b64f-fe91-487d-a298-5b897bde847f)数据结构。 |
| polygon\_type | 否 | string | 多边形类型，表示模型的表面由几边形网格构成，默认为 triangle,参考值:  triangle：三角形面。  quadrilateral：四边形面。  示例值：triangle |
| face\_level | 否 | string | 减面后面数档位类型，可选值：high，medium, low。  示例值：high |

**输出参数**

| 参数名称 | 类型 | 描述 |
| --- | --- | --- |
| id | string | 任务 id（有效期24小时）。  示例值：1315932989749215232 |
| request\_id | string | 唯一请求 id，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 request\_id）。定位问题时需要提供该次请求的 request\_id。 |
| object | string | 返回对象类型。3d 任务固定返回 3d\_job。 |
| created\_at | integer | 任务创建时间。 |
| status | string | completed：任务成功，failed：任务失败，in\_progress：执行中，queued：等待中。  示例值：completed |

### 查询智能拓扑任务

**输入参数**

| 参数名称 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| model | 是 | string | 智能拓扑模型名称，默认为 hy-3d-retopology。  示例值：hy-3d-retopology |
| id | 是 | string | 任务 id。  示例值：1357237233311637504 |

**输出参数**

| 参数名称 | 类型 | 描述 |
| --- | --- | --- |
| status | string | completed：任务成功，failed：任务失败，in\_progress：执行中，queued：等待中。  示例值：completed |
| request\_id | string | 唯一请求 id，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 request\_id）。定位问题时需要提供该次请求的 request\_id。 |
| object | string | 返回对象类型。3d 任务固定返回 3d\_job。 |
| created\_at | integer | 任务创建时间。 |
| completed\_at | integer | 任务完成时间。 |
| data | array of object | 生成结果列表，包含生成的 3d 模型文件及相关资源信息。详情请参见 [data](https://cloud.tencent.com/document/product/1823/137778#c9bb0852-073e-4e2e-8da9-5359d2b770bb) 数据结构。 |

## 示例

### 提交智能拓扑任务

**输入示例**

```json
curl -X POST 'https://tokenhub.tencentmaas.com/v1/api/3d/submit' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
    "model": "hy-3d-retopology",
    "file_3d": {
        "url": "https://example.com/test.glb"
    }
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

### 查询智能拓扑任务

**输入示例**

```java
curl -X POST 'https://tokenhub.tencentmaas.com/v1/api/3d/query' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
    "model": "hy-3d-retopology",
    "id": "14721*****320"
  }'
```

**输出示例**

```java
{
  "request_id": "74a967e4-0e81-48c1-afde-555b79a1cdf3",
  "object": "3d_job",
  "created_at": 1786947866,
  "completed_at": 1786947866,
  "status": "completed",
  "data": [
    {
      "type": "obj",
      "url": "https://hunyuan-prod-1258344699.cos.ap-guangzhou.tencentcos.cn/texture_to_3d/output/1254418******-4b66-bc94-8ad7285e659f.obj"
    },
    {
      "type": "glb",
      "url": "https://hunyuan-prod-1258344699.cos.ap-guangzhou.tencentcos.cn/texture_to_3d/output/125441*****3-4b66-bc94-8ad7285e659f.glb"
    },
    {
      "type": "image",
      "url": "https://hunyuan-prod-1258344699.cos.ap-guangzhou.tencentcos.cn/texture_to_3d/output/125441*****d3-4b66-bc94-8ad7285e659f_latent.png"
    }
  ]
}
```

## 数据结构

### file\_3d

**输入3D 模型文件对象。**

| 参数名称 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| type | 否 | string | 3D 模型文件类型。  示例值：fbx |
| url | 是 | string | 3D 模型文件地址。 |

### data

**生成结果对象。**

| 参数名称 | 类型 | 描述 |
| --- | --- | --- |
| type | string | 生成结果文件类型。  示例值：obj |
| url | string | 生成结果文件下载地址。 |
