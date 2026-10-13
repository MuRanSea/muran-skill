<!-- Official source: https://cloud.tencent.com/document/product/1823/137072 -->
<!-- Source SHA-256: 9f8bb11e66534e697097bc507c837db241e5b425521d272bbab025fa4de247c0 -->

# Tripo-3D-Rigging 调用指南

官方来源：https://cloud.tencent.com/document/product/1823/137072
最近更新时间：2026-08-27 11:35:32

## 简介

Tripo 自动绑骨接口，自动为 3D 模型添加骨骼绑定。

## 对接说明

### 1. 获取 API Key

1. 进入 [API Key 管理](https://console.cloud.tencent.com/tokenhub/apikey) 页面，单击**创建 API Key**。操作详情请参见 [创建 API Key](https://cloud.tencent.com/document/product/1823/130090#40882178-aaf2-48c9-8559-dffc083a79bc)。

2. 创建完成后，请您务必**复制并妥善保管 API Key**，在后续配置到工具的流程中将会使用该信息。

![](https://qcloudimg.tencent-cloud.cn/image/document/078182a08adc56d7010ccdcf508b8412.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/078182a08adc56d7010ccdcf508b8412.png)

**说明：**

每个账户的密钥都只能当前账户查询，主账户的密钥信息子账户是看不到，子账户如果需要调用接口，需要使用账户自行创建密钥信息。

如果子账户没有办法创建，可能是没有权限创建密钥，需要主账户授权，主账户登录之后点击用户列表，在对应的子账户后面选择授权，会弹出关联策略的弹窗，输入授权策略名称之后搜索，选择对应的策略点击确认。

授权策略：QcloudTokenhubFullAccess

### 2. 并发额度

默认提供1个并发，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后，才能开始处理下一个任务。

并发任务数：表示在调用对应服务的时段内最大可运行的任务数，该任务未完成时，无法提交下一个任务，该任务完成后，可提交下一个任务。

## 接口文档

#### 提交 Tripo 自动绑骨任务

**输入参数**

| 参数名称 | 必选 | 类型 | 参数描述 |
| --- | --- | --- | --- |
| model | 是 | string | 模型名称，默认为：tripo-3d-rigging  示例值：tripo-3d-rigging |
| input | 是 | string | 模型 URL：可公开访问的 3D 模型文件直链。  示例： https://example.com/model.glb    支持格式：GLB、GLTF、FBX、OBJ、STL  最大文件大小：**150 MB** |
| rig\_type | 否 | string | 骨骼类型。建议先调用 rig-check。  biped：双足人形。  quadruped：四足动物。  hexapod：六足生物。  octopod：八足生物。  avian：鸟类/有翼生物。  serpentine：蛇形生物。  aquatic：鱼类/水生生物。  默认值: biped |
| spec | 否 | string | 绑骨规范。  tripo：Tripo 原生骨骼命名。  mixamo：兼容 Mixamo 的骨骼命名。  默认值: tripo |
| out\_format | 否 | string | 输出格式。  glb：二进制 glTF，适用于 Web。  fbx：FBX，适用于 DCC 工具和游戏引擎。  默认值: glb |

**输出参数**

| 参数名称 | 类型 | 描述 |
| --- | --- | --- |
| id | string | 任务 id（有效期24小时）。  示例值：1315932989749215232 |
| request\_id | string | 唯一请求 id，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 request\_id）。定位问题时需要提供该次请求的 request\_id。 |
| object | string | 返回对象类型。3d 任务固定返回 3d\_job。 |
| created\_at | integer | 任务创建时间。 |
| status | string | completed：任务成功，failed：任务失败，in\_progress：执行中，queued：等待中。  示例值：completed |

#### 查询 Tripo 自动绑骨任务

**输入参数**

| 参数名称 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| model | 是 | string | 模型名称，默认为：tripo-3d-rigging  示例值：tripo-3d-rigging |
| id | 是 | string | 任务 id。  示例值：1357237233311637504 |

**输出参数**

| 参数名称 | 类型 | 描述 |
| --- | --- | --- |
| status | string | completed：任务成功，failed：任务失败，in\_progress：执行中，queued：等待中。  示例值：completed |
| request\_id | string | 唯一请求 id，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 request\_id）。定位问题时需要提供该次请求的 request\_id。 |
| output | object | 输出结果（TripoResult，任务完成时返回） |
| output.model\_url | string | 模型下载 URL |
| output.rendered\_image\_url | string | 渲染图片 URL |
| input | string | 输入参数回显 |
| object | string | 返回对象类型。3d 任务固定返回 3d\_job。 |
| created\_at | integer | 任务创建时间。 |
| completed\_at | integer | 任务完成时间。 |

## 示例

#### 提交 Tripo 自动绑骨任务

**输入示例**

```java
curl -X POST 'https://tokenhub.tencentmaas.com/v1/api/3d/submit' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -H 'Accept: */*' \\
  -H 'Connection: keep-alive' \\
  -d '{
    "model": "tripo-3d-rigging",
    "input": "https://example.com/test.glb"
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

#### 查询 Tripo 自动绑骨任务

**输入示例**

```java
curl -X POST 'https://tokenhub.tencentmaas.com/v1/api/3d/query' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -H 'Connection: keep-alive' \\
  -d '{
    "model": "tripo-3d-rigging",
    "id": "14721*****320"
  }'
```

**输出示例**

```java
{
  "status": "completed",
  "input":"{\\"spec\\":\\"tripo\\",\\"topology\\":\\"biped\\",\\"out_format\\":\\"glb\\",\\"original_model_id\\":\\"XXXXX-c1ac-49fb-8fe8-XXXXX\\"}",  "object": "3d_job",
  "output": {
      "model_url": "https://vcg-prod-1258344699.cos.ap-guangzhou.tencentcos.cn/**********12.glb"  
  },
  "request_id": "XXXXX-c925-4dda-90f0-XXXXX",
  "created_at": 1785989483,
  "completed_at": 1785989483
}
```
