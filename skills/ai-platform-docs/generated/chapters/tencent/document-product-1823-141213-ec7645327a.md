<!-- Official source: https://cloud.tencent.com/document/product/1823/141213 -->
<!-- Source SHA-256: a0395f228c0bbbc40978b4080753e51531829e01eabc8c1614296e31fa971d40 -->

# Tripo-3D-Retopology 调用指南

官方来源：https://cloud.tencent.com/document/product/1823/141213
最近更新时间：2026-11-23 19:12:04

## 简介

Tripo 重拓扑模型支持对 3D 模型进行减面与拓扑优化，支持保留干净的拓扑结构，并可在新一代重拓扑任务中同步完成智能 UV 展开。

## 对接说明

### 1. 获取 API Key

1. 进入 [API Key 管理](https://console.cloud.tencent.com/tokenhub/apikey) 页面，单击**创建 API Key**。操作详情请参见 [创建 API Key](https://cloud.tencent.com/document/product/1823/130090#40882178-aaf2-48c9-8559-dffc083a79bc)。

2. 创建完成后，请您务必**复制并妥善保管 API Key**，在后续配置到工具的流程中将会使用该信息。

![](https://qcloudimg.tencent-cloud.cn/image/document/17a9112fd42a170926280855d9e12893.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/17a9112fd42a170926280855d9e12893.png)

**说明：**

每个账户的密钥都只能当前账户查询，主账户的密钥信息对子账户不可见，子账户如果需要调用接口，需要使用账户自行创建密钥信息。

如果子账户没有办法创建，可能是没有权限创建密钥，需要主账户授权，主账户登录之后点击用户列表，在对应的子账户后面选择授权，会弹出关联策略的弹窗，输入授权策略名称之后搜索，选择对应的策略点击确认。

授权策略：QcloudTokenhubFullAccess

### 2. 并发额度

默认提供 3 个并发，代表最多可同时处理 3 个已提交的任务，超出并发限制的任务需等待前面的任务处理完成后才能开始处理。

并发任务数：表示在调用对应服务的时段内最大可运行的任务数，该任务未完成时，无法提交下一个任务，该任务完成后，可提交下一个任务。

## 接口文档

### 提交 Tripo 重拓扑任务

**输入参数**

| 参数名称 | 必选 | 类型 | 参数描述 |
| --- | --- | --- | --- |
| model | 是 | string | 模型名称。默认为 tripo-3d-retopology。示例值：tripo-3d-retopology。 |
| input | 是 | string | 可公开访问的3D 模型文件 URL；支持 GLB、GLTF、FBX、OBJ、STL，最大150 MB。 |
| model\_version | 否 | string | 重拓扑算法版本。可选值：v3.0 、v2.0、v1.0  重拓扑 v3.0：最新一代重拓扑，可在同一任务内顺带展开 UV。 按输出拓扑计费：三角面 35 积分，四边面（quad=true）40 积分。  face\_limit：可选。三角面：500–20,000；四边面：500–10,000。省略则自适应。  quad：支持  smart\_uv：支持（仅 v3.0）  bake：支持（默认 true）  part\_names：支持  智能重拓扑：重建干净拓扑，保边保细节。  face\_limit：可选。三角面：500–20,000；四边面：500–10,000。省略则自适应。  quad：支持  bake：支持（默认 true）  part\_names：支持  format：不支持（输出 GLB；quad=true 时输出 FBX）  基础减面：后处理管线减面。  face\_limit：必填。三角面最高 2,000,000；四边面最高 150,000。  quad：支持  bake、part\_names：不支持 |
| face\_limit | 条件必选 | integer | 目标面数：v3.0/v2.0 可选，三角面500～20000、四边面500～10000，省略则自适应；v1.0 必填，三角面最高2000000、四边面最高150000。 |
| smart\_uv | 否 | boolean | 重拓扑时展开 UV，仅 model\_version=v3.0 有效，默认 false；v1.0/v2.0 传入返回400（错误码1004），不会静默忽略。 |
| quad | 否 | boolean | 输出四边面网格。v3.0、v2.0、v1.0 均支持。v3.0 输出四边面按 40 积分计费（三角面为 35）。 |
| bake | 否 | boolean | 是否将贴图烘焙到低面数模型，默认 true；v1.0 不支持。 |
| part\_names | 否 | string[] | 要减面的部件名称，来自语义分割；v1.0 不支持。 |

**输出参数**

| 参数名称 | 类型 | 描述 |
| --- | --- | --- |
| id | string | 任务 ID，有效期24小时，用于查询结果。 |
| request\_id | string | 服务端生成的唯一请求 ID，用于定位问题。 |
| object | string | 返回对象类型。示例为 3d\_job。 |
| created\_at | integer | 任务创建时间。 |
| status | string | 任务状态：queued（等待中）、in\_progress（执行中）、completed（成功）、failed（失败）。 |

### 查询 Tripo 重拓扑任务

**输入参数**

| 参数名称 | 必选 | 类型 | 参数描述 |
| --- | --- | --- | --- |
| model | 是 | string | 模型名称。默认为 tripo-3d-retopology。示例值：tripo-3d-retopology。 |
| id | 是 | string | 提交接口返回的任务 ID。示例值：xxxxx。 |

**输出参数**

| 参数名称 | 类型 | 描述 |
| --- | --- | --- |
| status | string | 任务状态：completed（成功）、failed（失败）、in\_progress（执行中）、queued（等待中）。 |
| request\_id | string | 服务端生成的请求 ID，用于定位问题。 |
| object | string | 返回对象类型。示例为 3d\_job。 |
| created\_at | integer | 任务创建时间。 |
| completed\_at | integer | 任务完成时间。 |
| progress | integer | 任务进度，0～100。 |
| data | object | 生成结果，仅 status=completed 时有值。 |
| data.model\_url | string | 重拓扑后的3D 模型文件 URL（GLB 格式）。 |
| data.rendered\_image\_url | string | 渲染预览图 URL。 |
| error\_code | integer | status=failed 时返回，标识失败原因。 |
| error\_message | string | status=failed 且有 error\_code 时返回对应错误描述。 |
| credits\_consumed | number | 已消耗的额度，最小两位小数。 |

## 示例

### 提交 Tripo 重拓扑任务

**输入示例**

```java
curl --location --request POST 'https://tokenhub.tencentmaas.com/v1/api/3d/submit' \\
--header "Authorization: Bearer ${APIKEY}" \\
--header 'Content-Type: application/json' \\
--data-raw '{
  "model": "tripo-3d-retopology",
  "input": "https://example.com/model.glb"
}'
```

**输出示例**

```java
{
  "created_at": 1793094400,
  "id": "<JOB_ID>",
  "object": "3d_job",
  "request_id": "<REQUEST_ID>",
  "status": "queued"
}
```

### 查询 Tripo 重拓扑任务

**输入示例**

```java
curl --location --request POST 'https://tokenhub.tencentmaas.com/v1/api/3d/query' \\
--header "Authorization: Bearer ${APIKEY}" \\
--header 'Content-Type: application/json' \\
--data-raw '{
  "model": "tripo-3d-retopology",
  "id": "<JOB_ID>"
}'
```

**输出示例**

```java
{
  "created_at": 1793094500,
  "data": [
    {
      "model_url": "https://example.com/model.glb",
      "rendered_image_url": "https://example.com/model.png"
    }
  ],
  "object": "3d_job",
  "request_id": "<REQUEST_ID>",
  "status": "completed"
}
```
