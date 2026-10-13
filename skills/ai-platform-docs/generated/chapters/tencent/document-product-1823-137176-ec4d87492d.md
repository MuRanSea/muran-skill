<!-- Official source: https://cloud.tencent.com/document/product/1823/137176 -->
<!-- Source SHA-256: b5d27e1ab04acd9b167036288177bbdd7e648757184a02a6502aa097eae1afa6 -->

# HY-3D-Component 调用指南

官方来源：https://cloud.tencent.com/document/product/1823/137176
最近更新时间：2026-09-08 17:21:53

## 简介

组件生成接口，输入3D 模型后，可自动识别模型结构，生成对应模型的3D 组件。

## 对接说明

### 1. 获取 API Key

1. 进入 [API Key 管理](https://console.cloud.tencent.com/tokenhub/apikey) 页面，单击**创建 API Key**。操作详情请参见 [创建 API Key](https://cloud.tencent.com/document/product/1823/130090#40882178-aaf2-48c9-8559-dffc083a79bc)。

2. 创建完成后，请您务必**复制并妥善保管 API Key**，在后续配置到工具的流程中将会使用该信息。

![](https://qcloudimg.tencent-cloud.cn/image/document/f45f2f5d289fa77ca4cc1ce459fe5c71.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/f45f2f5d289fa77ca4cc1ce459fe5c71.png)

**说明：**

每个账户的密钥都只能当前账户查询，主账户的密钥信息子账户是看不到，子账户如果需要调用接口，需要使用账户自行创建密钥信息。

如果子账户没有办法创建，可能是没有权限创建密钥，需要主账户授权，主账户登录之后点击用户列表，在对应的子账户后面选择授权，会弹出关联策略的弹窗，输入授权策略名称之后搜索，选择对应的策略点击确认。

授权策略：QcloudTokenhubFullAccess

### 2. 并发额度

默认提供1个并发，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后，才能开始处理下一个任务。

并发任务数：表示在调用对应服务的时段内最大可运行的任务数，该任务未完成时，无法提交下一个任务，该任务完成后，可提交下一个任务。

## 接口文档

### 提交组件生成任务

**输入参数**

| 参数名称 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| model | 是 | string | 组件生成模型名称，默认为 hy-3d-component。  示例值：hy-3d-component |
| file | 是 | input\_file\_3d | 需进行组件生成的3d 模型文件，仅支持 fbx 格式。 |
| part\_segmentation\_info | 否 | string | 是否分步骤进行组件生成。  开启后，输入原始模型后，可生成带分割信息的模型以及分割数据，可对此信息编辑后再传入带有分割信息的模型和分割数据进行编辑后的组件生成。  此参数默认关闭。  示例值：{"part\_0": {"face\_ids": [ xxx ]} |
| enable\_staged\_generation | 否 | boolean | 是否分步骤进行组件生成。  开启后，输入原始模型后，可生成带分割信息的模型以及分割数据，可对此信息编辑后再传入带有分割信息的模型和分割数据进行编辑后的组件生成。  此参数默认关闭。  示例值：true |
| enable\_post\_process | 否 | boolean | 是否开启后处理，开启后将只输出一个模型链接，默认关闭。（开启此接口后，需额外增加20积分）  示例值：true |

**输出参数**

<table><colgroup><col/><col/><col/></colgroup><tbody><tr><td><div>参数名称</div></td><td><div>类型</div></td><td><div>描述</div></td></tr><tr><td><div>id</div></td><td><div>string</div></td><td><div>任务 id（有效期24小时）。</div><div>示例值：1315932989749215232</div></td></tr><tr><td><div>request_id</div></td><td><div>string</div></td><td><div>唯一请求 id，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 request_id）。定位问题时需要提供该次请求的 request_id。</div></td></tr><tr><td colspan="1" rowspan="1"><div>object</div></td><td colspan="1" rowspan="1"><div>string</div></td><td colspan="1" rowspan="1"><div>返回对象类型。3d 任务固定返回 3d_job。</div></td></tr><tr><td colspan="1" rowspan="1"><div>created_at</div></td><td colspan="1" rowspan="1"><div>integer</div></td><td colspan="1" rowspan="1"><div>任务创建时间。</div></td></tr><tr><td colspan="1" rowspan="1"><div>status</div></td><td colspan="1" rowspan="1"><div>string</div></td><td colspan="1" rowspan="1"><div>completed：任务成功，failed：任务失败，in_progress：执行中，queued：等待中。</div><div>示例值：completed</div></td></tr></tbody></table>

### 查询组件生成任务

**输入参数**

| 参数名称 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| model | 是 | string | 组件生成模型版本，默认为 hy-3d-component。  示例值：hy-3d-component |
| id | 是 | string | 任务 id。  示例值：1357237233311637504 |

**输出参数**

| 参数名称 | 类型 | 描述 |
| --- | --- | --- |
| status | string | completed：任务成功，failed：任务失败，in\_progress：执行中，queued：等待中。  示例值：completed |
| request\_id | string | 唯一请求 id，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 request\_id）。定位问题时需要提供该次请求的 request\_id。 |
| data | array of object | 生成结果列表，包含生成的 3d 模型文件及相关资源信息。详情请参见 [data](https://cloud.tencent.com/document/product/1823/137176#c9bb0852-073e-4e2e-8da9-5359d2b770bb) 数据结构。 |
| object | string | 返回对象类型。3d 任务固定返回 3d\_job。 |
| created\_at | integer | 任务创建时间。 |
| completed\_at | integer | 任务完成时间。 |

## 示例

### 提交组件生成任务

**输入示例**

```java
curl -X POST 'https://tokenhub.tencentmaas.com/v1/api/3d/submit' 
  -H 'Authorization: Bearer YOUR_API_KEY' 
  -H 'Content-Type: application/json' 
  -d '{
    "model": "hy-3d-component",
    "file": {
        "url": "https://example.com/test.fbx"
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

### 查询组件生成任务

**输入示例**

```java
curl -X POST 'https://tokenhub.tencentmaas.com/v1/api/3d/query' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
    "model": "hy-3d-component",
    "id": "14721*****320"
  }'
```

**输出示例**

```java
{
  "request_id": "6df5ce8a-1290-4c2e-aff1-0740fd6e30eb",
  "object": "3d_job",
  "created_at": 1787043728,
  "completed_at": 1787043728,
  "status": "completed",
  "data": [
    {
      "type": "glb",
      "url": "https://vcg-prod-1258344699.cos.ap-guangzhou.tencentcos.cn/3dpart/output/12544******5-afddb37d7c21_1787043584_part_0.glb"
    },
    {
      "type": "glb",
      "url": "https://vcg-prod-1258344699.cos.ap-guangzhou.tencentcos.cn/3dpart/output/12544******5-afddb37d7c21_1787043584_part_0.glb"
    },
    {
      "type": "glb",
      "url": "https://vcg-prod-1258344699.cos.ap-guangzhou.tencentcos.cn/3dpart/output/12544******5-afddb37d7c21_1787043584_part_0.glb"
    },
    {
      "type": "glb",
      "url": "https://vcg-prod-1258344699.cos.ap-guangzhou.tencentcos.cn/3dpart/output/12544******5-afddb37d7c21_1787043584_part_0.glb"
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

##
