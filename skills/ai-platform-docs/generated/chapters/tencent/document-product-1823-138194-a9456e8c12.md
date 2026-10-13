<!-- Official source: https://cloud.tencent.com/document/product/1823/138194 -->
<!-- Source SHA-256: c649d6f749c5c770ba75bf7d8ecbe5df004319e142a856df31034a333690a4b5 -->

# HY-3d-polygen-mesh 调用指南

官方来源：https://cloud.tencent.com/document/product/1823/138194
最近更新时间：2026-09-18 15:30:30

## 简介

HY-3d-polygen-mesh 接口，基于输入的3D 模型，通过大模型算法进行减面，生成低面片且布线更规整的3D 模型。

## 对接说明

### 1. 获取 API Key

1. 进入 [API Key 管理](https://console.cloud.tencent.com/tokenhub/apikey) 页面，单击**创建 API Key**。操作详情请参见 [创建 API Key](https://cloud.tencent.com/document/product/1823/130090#40882178-aaf2-48c9-8559-dffc083a79bc)。

2. 创建完成后，请您务必**复制并妥善保管 API Key**，在后续配置到工具的流程中将会使用该信息。

![](https://qcloudimg.tencent-cloud.cn/image/document/b2a931d3aa6f44b92a34a09baf7f4e1e.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/b2a931d3aa6f44b92a34a09baf7f4e1e.png)

**说明：**

每个账户的密钥都只能当前账户查询，主账户的密钥信息子账户是看不到，子账户如果需要调用接口，需要使用账户自行创建密钥信息。

如果子账户没有办法创建，可能是没有权限创建密钥，需要主账户授权，主账户登录之后点击用户列表，在对应的子账户后面选择授权，会弹出关联策略的弹窗，输入授权策略名称之后搜索，选择对应的策略点击确认。

授权策略：QcloudTokenhubFullAccess

### 2. 并发额度

默认提供1个并发，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后，才能开始处理下一个任务。

并发任务数：表示在调用对应服务的时段内最大可运行的任务数，该任务未完成时，无法提交下一个任务，该任务完成后，可提交下一个任务。

## 接口文档

### 提交智能减面任务

**输入参数**

<table><colgroup><col/><col/><col/><col/></colgroup><tbody><tr><td><div>参数名称</div></td><td><div>必选</div></td><td><div>类型</div></td><td><div>参数描述</div></td></tr><tr><td><div>model</div></td><td><div>是</div></td><td colspan="1" rowspan="1"><div>string</div></td><td><div>模型名称。默认为 hy-3d-polygen-mesh。</div><div>示例值：hy-3d-polygen-mesh</div></td></tr><tr><td><div>glb_url</div></td><td><div>否</div></td><td colspan="1" rowspan="1"><div>string</div></td><td><div>高面数的 GLB 格式3D 模型文件 URL，glb_url/obj_url/fbx_url/ascii_fbx_url 四选一。</div></td></tr><tr><td><div>obj_url</div></td><td><div>否</div></td><td colspan="1" rowspan="1"><div>string</div></td><td><div>高面数的 OBJ 格式3D 模型文件 URL，glb_url/obj_url/fbx_url/ascii_fbx_url 四选一。</div></td></tr><tr><td><div>fbx_url</div></td><td colspan="1" rowspan="1"><div>否</div></td><td colspan="1" rowspan="1"><div>string</div></td><td><div>高面数的 FBX 格式3D 模型文件 URL，glb_url/obj_url/fbx_url/ascii_fbx_url 四选一。</div></td></tr><tr><td><div>ascii_fbx_url</div></td><td colspan="1" rowspan="1"><div>否</div></td><td colspan="1" rowspan="1"><div>string</div></td><td><div>高面数的 ASCII FBX 格式3D 模型文件 URL，glb_url/obj_url/fbx_url/ascii_fbx_url 四选一。</div></td></tr><tr><td><div>num_of_faces</div></td><td colspan="1" rowspan="1"><div>否</div></td><td colspan="1" rowspan="1"><div>int</div></td><td><div>目标面数，默认10000，范围100～20000。不填或填0代表默认。</div></td></tr><tr><td><div>polygon_type</div></td><td colspan="1" rowspan="1"><div>否</div></td><td colspan="1" rowspan="1"><div>string</div></td><td><div>多边形类型，可选：triangle（默认）或 quadrilateral。</div></td></tr><tr><td><div>disable_normalization</div></td><td><div>否</div></td><td colspan="1" rowspan="1"><div>bool</div></td><td><div>是否禁用归一化，默认 false。设置为 true 则不进行归一化。</div></td></tr></tbody></table>

**输出参数**

| 参数名称 | 类型 | 描述 |
| --- | --- | --- |
| id | string | 任务 id（有效期24小时）。  示例值：1315932989749215232 |
| request\_id | string | 唯一请求 id，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 request\_id）。定位问题时需要提供该次请求的 request\_id。 |
| object | string | 返回对象类型。3d 任务固定返回 3d\_job。 |
| created\_at | integer | 任务创建时间。 |
| status | string | completed：任务成功，failed：任务失败，in\_progress：执行中，queued：等待中。  示例值：completed |

### 查询智能减面任务

**输入参数**

| 参数名称 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| model | 是 | string | 模型名称。默认为 hy-3d-polygen-mesh。  示例值：hy-3d-polygen-mesh |
| id | 是 | string | 任务 id。  示例值：1357237233311637504 |

**输出参数**

| 参数名称 | 类型 | 描述 |
| --- | --- | --- |
| request\_id | string | 唯一请求 id，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 request\_id）。定位问题时需要提供该次请求的 request\_id。 |
| object | string | 返回对象类型。3d 任务固定返回 3d\_job。 |
| created\_at | int | 创建时间（UNIX 时间戳）。 |
| status | string | completed：任务成功，failed：任务失败，in\_progress：执行中，queued：等待中。  示例值：completed |
| data | array | 生成结果数组（仅状态为 completed 时返回），包含生成的 3d 模型文件及相关资源信息。 |
| data[n].fbx\_url | string | 智能减面后的低面数 FBX 格式3D 模型下载 URL（有效期1天）。 |
| data[n].obj\_url | string | 智能减面后的低面数 OBJ 格式3D 模型下载 URL（有效期1天）。 |
| data[n].glb\_url | string | 智能减面后的低面数 GLB 格式3D 模型下载 URL（有效期1天）。 |
| data[n].image\_url | string | 减面生成模型的渲染图片 URL（有效期1天）。 |
| data[n].quads\_info | string | 四边面信息（JSON 字符串），仅当 polygon\_type=quadrilateral 时返回，包含点数、面数及坐标信息。 |
| error | object | 错误信息（仅状态为 failed 时返回）。 |
| error.code | string | 错误码。 |
| error.message | string | 错误信息。 |
| error.type | string | 错误类型。 |

## **示例**

### 提交智能减面任务

**输入示例**

```java
curl --location --request POST 'https://tokenhub.tencentmaas.com/v1/api/3d/submit' \\
--header "Authorization: Bearer ${APIKEY}" \\
--header 'Content-Type: application/json' \\
--data-raw '{
  "model": "hy-3d-polygen-mesh",
  "glb_url": "https://example.com/model.glb"
}'
```

**输出示例**

```java
{
  "created_at": 1787890699,
  "id": "xxxxx",
  "object": "3d_job",
  "request_id": "75c28fde-6abe-4fa5-973a-xxxxx",
  "status": "queued"
}
```

### 查询智能减面任务

**输入示例**

```java
curl --location --request POST 'https://tokenhub.tencentmaas.com/v1/api/3d/query' \\
--header "Authorization: Bearer ${APIKEY}" \\
--header 'Content-Type: application/json' \\
--data-raw '{
  "model": "hy-3d-polygen-mesh",
  "id": "id"
}'
```

**输出示例**

```java
{
    "created_at": 1787814686,
    "object": "3d_job",
    "request_id": "9f97cfa0-2939-46e6-a27d-xxx",
	"data": [
	    {
	      "fbx_url": "https://example.com/model.fbx",
	      "glb_url": "https://example.com/model.glb",
	      "image_url": "https://example.com/model.jpg",
	      "obj_url": "https://example.com/model.obj",
	      "quads_info": ""
	      }],
    "status": "completed"
}
```

## 错误码

| 错误码 | HTTP 状态码 | 说明 |
| --- | --- | --- |
| InvalidParameter | 400 | 请求参数错误（如 model 缺失、未提供3D 模型 URL 等）。 |
| MissingParameter | 400 | 缺少必填参数。 |
| FailedOperation | 500 | 任务执行失败。 |
| InternalError | 500 | 内部错误。 |
| FailedOperation.JobNotExist | 500 | 任务不存在或已过期。 |
