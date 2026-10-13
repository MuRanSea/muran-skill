<!-- Official source: https://cloud.tencent.com/document/product/1823/137780 -->
<!-- Source SHA-256: ba8d1e4a8734f360a50eaddc3d1ced06f4629b731d4f22ce77752d1a5342864b -->

# HY-3D-Motion 调用指南

官方来源：https://cloud.tencent.com/document/product/1823/137780
最近更新时间：2026-09-09 18:13:39

## 简介

文生动作接口，输入文本后，可根据文本描述生成对应的 3D 人物动作数据，输出带动画数据的 FBX 文件。

## 对接说明

### 1. 获取 API Key

1. 进入 [API Key 管理](https://console.cloud.tencent.com/tokenhub/apikey) 页面，单击**创建 API Key**。操作详情请参见 [创建 API Key](https://cloud.tencent.com/document/product/1823/130090#40882178-aaf2-48c9-8559-dffc083a79bc)。

2. 创建完成后，请您务必**复制并妥善保管 API Key**，在后续配置到工具的流程中将会使用该信息。

![](https://qcloudimg.tencent-cloud.cn/image/document/b7985526b97da0eefa3b58616213265d.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/b7985526b97da0eefa3b58616213265d.png)

**说明：**

每个账户的密钥都只能当前账户查询，主账户的密钥信息子账户是看不到，子账户如果需要调用接口，需要使用账户自行创建密钥信息。

如果子账户没有办法创建，可能是没有权限创建密钥，需要主账户授权，主账户登录之后点击用户列表，在对应的子账户后面选择授权，会弹出关联策略的弹窗，输入授权策略名称之后搜索，选择对应的策略点击确认。

授权策略：QcloudTokenhubFullAccess

### 2. 并发额度

默认提供1个并发，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后，才能开始处理下一个任务。

并发任务数：表示在调用对应服务的时段内最大可运行的任务数，该任务未完成时，无法提交下一个任务，该任务完成后，可提交下一个任务。

## 接口文档

### 提交文生动作任务

**输入参数**

| 参数名称 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| model | 是 | string | 文生动作模型名称，默认为 hy-3d-motion。  示例值：hy-3d-motion |
| prompt | 是 | string | 输入文本 prompt，限定最大字符为128。  示例值：A person walks forward |
| retarget\_file | 否 | object | 需重定向的模型地址，只能支持混元生3D 动画生成的模型（动画模板的接口）。 |
| duration | 否 | integer | 生成动画的时长，默认5，范围：1-12（单位 s）。  示例值：5 |
| enable\_mesh | 否 | boolean | 默认 true，返回的 fbx 是否带蒙皮 mesh。  示例值：true |
| enable\_rewrite | 否 | boolean | 是否开启 prompt 扩写，开启后将补充完善输入的 prompt。  默认 false。  示例值：true |
| enable\_duration\_est | 否 | boolean | 是否开启时长自动匹配，开启后将自动根据 prompt 匹配适合时长的动作数据。  默认 false。  示例值：true |

**输出参数**

| 参数名称 | 类型 | 描述 |
| --- | --- | --- |
| id | string | 任务 id（有效期24小时）。  示例值：1315932989749215232 |
| request\_id | string | 唯一请求 id，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 request\_id）。定位问题时需要提供该次请求的 request\_id。 |
| object | string | 返回对象类型。3d 任务固定返回 3d\_job。 |
| created\_at | integer | 任务创建时间。 |
| status | string | completed：任务成功，failed：任务失败，in\_progress：执行中，queued：等待中。  示例值：completed |

### 查询文生动作任务

**输入参数**

| 参数名称 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| model | 是 | string | 文生动作模型名称，默认为 hy-3d-motion。  示例值：hy-3d-motion |
| id | 是 | string | 任务 id。  示例值：1357237233311637504 |

**输出参数**

| 参数名称 | 类型 | 描述 |
| --- | --- | --- |
| status | string | completed：任务成功，failed：任务失败，in\_progress：执行中，queued：等待中。  示例值：completed |
| request\_id | string | 唯一请求 id，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 request\_id）。定位问题时需要提供该次请求的 request\_id。 |
| object | string | 返回对象类型。3d 任务固定返回 3d\_job。 |
| created\_at | integer | 任务创建时间。 |
| completed\_at | integer | 任务完成时间。 |
| data | array of object | 生成结果列表，包含生成的 3d 模型文件及相关资源信息。详情请参见 [data 数据结构](https://cloud.tencent.com/document/product/1823/137780#c9bb0852-073e-4e2e-8da9-5359d2b770bb)。 |

## 示例

### 提交文生动作任务

**输入示例**

```java
curl -X POST 'https://tokenhub.tencentmaas.com/v1/api/3d/submit' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
    "model": "hy-3d-motion",
    "prompt": "A person walks forward"
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

### 查询文生动作任务

**输入示例**

```java
curl -X POST 'https://tokenhub.tencentmaas.com/v1/api/3d/query' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
    "model": "hy-3d-motion",
    "id": "14721*****320"
  }'
```

**输出示例**

```java
{
  "request_id": "73b59d47-9*********e32f5",
  "object": "3d_job",
  "created_at": 1788420377,
  "completed_at": 1788420377,
  "status": "completed",
  "data": [
    {
      "type": "fbx",
      "url": "https://vcg-prod-1258344699.cos.ap-guangzhou.tencentcos.cn/text2motion/output/12544******13-4c1a-b70a-dbae7052291d_output.fbx"
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
