<!-- Official source: https://cloud.tencent.com/document/product/1823/137182 -->
<!-- Source SHA-256: 7295aa2babc2e7b0aa85f07393983f647776abf9b5101563cd4f03347e22dd8a -->

# HY-3D-Format 调用指南

官方来源：https://cloud.tencent.com/document/product/1823/137182
最近更新时间：2026-09-08 17:21:57

## 简介

格式转换接口，输入3D 模型文件后，可进行3D 模型文件格式转换。

## 对接说明

### 1. 获取 API Key

1. 进入 [API Key 管理](https://console.cloud.tencent.com/tokenhub/apikey) 页面，单击**创建 API Key**。操作详情请参见 [创建 API Key](https://cloud.tencent.com/document/product/1823/130090#40882178-aaf2-48c9-8559-dffc083a79bc)。

2. 创建完成后，请您务必**复制并妥善保管 API Key**，在后续配置到工具的流程中将会使用该信息。

![](https://qcloudimg.tencent-cloud.cn/image/document/9592c8ed0c8b2d52e6633be58cb40392.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/9592c8ed0c8b2d52e6633be58cb40392.png)

**说明：**

每个账户的密钥都只能当前账户查询，主账户的密钥信息子账户是看不到，子账户如果需要调用接口，需要使用账户自行创建密钥信息。

如果子账户没有办法创建，可能是没有权限创建密钥，需要主账户授权，主账户登录之后点击用户列表，在对应的子账户后面选择授权，会弹出关联策略的弹窗，输入授权策略名称之后搜索，选择对应的策略点击确认。

授权策略：QcloudTokenhubFullAccess

### 2. 并发额度

默认提供1个并发，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后，才能开始处理下一个任务。

并发任务数：表示在调用对应服务的时段内最大可运行的任务数，该任务未完成时，无法提交下一个任务，该任务完成后，可提交下一个任务。

## 接口文档

### 提交格式转换任务

**输入参数**

| 参数名称 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| model | 是 | string | 格式转换模型名称，默认为 hy-3d-format。  示例值：hy-3d-format |
| file | 是 | object | 3d 文件 url 地址，模型文件大小≤60m，支持 fbx，obj，glb 格式3D 文件输入。  示例值：url |
| format | 是 | string | 返回的3D 文件格式，参考值：STL, USDZ, FBX, MP4, GIF,OBJ,GLB。  示例值：STL |

**输出参数**

| 参数名称 | 类型 | 描述 |
| --- | --- | --- |
| id | string | 任务 id（有效期24小时）。  示例值：1315932989749215232 |
| request\_id | string | 唯一请求 id，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 request\_id）。定位问题时需要提供该次请求的 request\_id。 |
| object | string | 返回对象类型。3d 任务固定返回 3d\_job。 |
| created\_at | integer | 任务创建时间。 |
| status | string | completed：任务成功，failed：任务失败，in\_progress：执行中，queued：等待中。  示例值：completed |

### 查询格式转换任务

**输入参数**

| 参数名称 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| model | 是 | string | 格式转换模型名称，默认为 hy-3d-format。  示例值：hy-3d-format |
| id | 是 | string | 任务 id。  示例值：1357237233311637504 |

**输出参数**

| 参数名称 | 类型 | 描述 |
| --- | --- | --- |
| status | string | completed：任务成功，failed：任务失败，in\_progress：执行中，queued：等待中。  示例值：completed |
| request\_id | string | 唯一请求 id，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 request\_id）。定位问题时需要提供该次请求的 request\_id。 |
| object | string | 返回对象类型。3d 任务固定返回 3d\_job。 |
| created\_at | integer | 任务创建时间。 |
| completed\_at | integer | 任务完成时间。 |
| data | array of object | 生成结果列表，包含生成的 3d 模型文件及相关资源信息。详情请参见 [data](https://cloud.tencent.com/document/product/1823/137182#c9bb0852-073e-4e2e-8da9-5359d2b770bb) 数据结构。 |

## 示例

### 提交格式转换任务

**输入示例**

```java
curl -X POST 'https://tokenhub.tencentmaas.com/v1/api/3d/submit' 
  -H 'Authorization: Bearer YOUR_API_KEY' 
  -H 'Content-Type: application/json' 
  -d '{
    "model": "hy-3d-format",
    "file": {
        "url": "https://example.com/test.glb"
    },
    "format": "STL"
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

### 查询格式转换任务

**输入示例**

```java
curl -X POST 'https://tokenhub.tencentmaas.com/v1/api/3d/query' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
    "model": "hy-3d-format",
    "id": "14721*****320"
  }'
```

**输出示例**

```java
{
  "request_id": "97bacfc4-2a0f-4391-b185-e14dafb5d383",
  "object": "3d_job",
  "created_at": 1787129328,
  "completed_at": 1787129328,
  "status": "completed",
  "data": [
    {
      "type": "stl",
      "url": "https://vcg-prod-1258344699.cos.ap-guangzhou.tencentcos.cn/3d/output/12544******ae-24e742641595_output.stl"
    }
  ]
}
```

## 数据结构

### data

**生成结果对象。**

| 参数名称 | 类型 | 描述 |
| --- | --- | --- |
| format | string | 生成结果文件格式。参考值：stl、usdz、fbx、mp4、gif。  示例值：stl |
| url | string | 生成结果文件下载地址。 |
