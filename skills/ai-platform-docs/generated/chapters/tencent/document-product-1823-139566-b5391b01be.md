<!-- Official source: https://cloud.tencent.com/document/product/1823/139566 -->
<!-- Source SHA-256: 022f7d9240e841442b9ef93d1f712c965f7b7e8ed1062a7e6bb944efd55c0d1a -->

# Rodin-Gen-3D-2.5 调用指南

官方来源：https://cloud.tencent.com/document/product/1823/139566
最近更新时间：2026-10-21 00:32:00

## 简介

rodin-gen-3d-2.5接口，根据输入的图片或文本智能生成高质量3D 模型。

## 对接说明

### 1. 获取 API Key

1. 进入 [API Key 管理](https://console.cloud.tencent.com/tokenhub/apikey) 页面，单击**创建 API Key**。操作详情请参见 [创建 API Key](https://cloud.tencent.com/document/product/1823/130090#40882178-aaf2-48c9-8559-dffc083a79bc)。

2. 创建完成后，请您务必**复制并妥善保管 API Key**，在后续配置到工具的流程中将会使用该信息。

![](https://qcloudimg.tencent-cloud.cn/image/document/110e17773d7a4b8e857c9c894734329f.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/110e17773d7a4b8e857c9c894734329f.png)

**说明：**

每个账户的密钥都只能当前账户查询，主账户的密钥信息子账户是看不到，子账户如果需要调用接口，需要使用账户自行创建密钥信息。

如果子账户没有办法创建，可能是没有权限创建密钥，需要主账户授权，主账户登录之后点击用户列表，在对应的子账户后面选择授权，会弹出关联策略的弹窗，输入授权策略名称之后搜索，选择对应的策略点击确认。

授权策略：QcloudTokenhubFullAccess

### 2. 并发额度

默认提供1个并发，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后，才能开始处理下一个任务。

并发任务数：表示在调用对应服务的时段内最大可运行的任务数，该任务未完成时，无法提交下一个任务，该任务完成后，可提交下一个任务。

## 接口文档

### 提交3D 生成任务

**输入参数**

| 参数名称 | 必选 | 类型 | 参数描述 |
| --- | --- | --- | --- |
| model | 是 | string | 模型名称。默认为 rodin-gen-3d-2.5。示例值：rodin-gen-3d-2.5 |
| prompt | 条件必选 | string | 文本描述，文生3D 时必填，最大1024字符。与 images 严格互斥，不能同时传递。 |
| images | 条件必选 | array<string> | 图片 URL 数组，图生3D 时必填，1～5张。支持 jpeg/jpg/png/webp，分辨率须大于128×128，单张小于10MB。与 prompt 严格互斥。 |
| tier | 是 | string | 模型档位。可选：Gen-2.5-Extreme-Low、Gen-2.5-Low、Gen-2.5-Medium、Gen-2.5-High、Gen-2.5-Extreme-High。 |
| mesh\_mode | 否 | string | 网格拓扑模式。可选 Raw（三角面，默认）或 Quad（四边面）。 |
| quality | 否 | string | 网格质量预设。可选 extra-low、low、medium（默认）、high。 |
| quality\_override | 否 | int | 自定义目标面数，范围500～2000000；设置后优先于 quality。 |
| texture\_mode | 否 | string | 纹理模式。可选 legacy、extreme-low、low、medium、high、extreme-high；默认值取决于 tier。 |
| material | 否 | string | 材质类型。可选 PBR（默认）、Shaded、All、Hybrid、None。 |
| geometry\_file\_format | 否 | string | 输出文件格式。可选 glb（默认）、usdz、fbx、obj、stl。 |
| seed | 否 | int | 随机种子，范围0～65535。 |
| soft | 否 | bool | 是否平滑边缘，默认 false。 |
| detail\_level | 否 | int | 几何优化阶段数量，范围1～3。 |
| quad\_normal | 否 | bool | 是否将高分辨率几何细节烘焙为法线贴图，默认 false。 |
| bbox\_condition | 否 | array<int> | 控制最大尺寸 (x, y, z)，需提供3个整数。 |
| addons | 否 | array<string> | 附加项，如 HighPack（将 pack 纹理由2K 提升至4K）。 |
| TAPose | 否 | bool | 类人模型是否使用 T/A-pose，默认 false。 |
| use\_original\_alpha | 否 | bool | 是否使用原始 alpha 通道，默认 false。 |
| preview\_render | 否 | bool | 是否生成预览渲染图，默认 false。 |
| is\_symmetric | 否 | string | 对称性。可选 symmetric、balanced、asymmetric、unknown（默认）。 |
| image\_label | 否 | array<string> | 图像方向标签。可选 F、FL、FR、B、BL、BR、L、R、U、D、?。 |
| hd\_texture | 否 | bool | 是否启用纹理超分辨率增强，默认 false。 |
| uhd\_texture | 否 | bool | 是否启用纹理额外锐化，默认 false。 |
| is\_micro | 否 | bool | 是否启用微小表面细节，仅 Gen-2.5-Extreme-High 有效，默认 false。 |
| geometry\_instruct\_mode | 否 | string | 几何策略。可选 creative（默认，更灵活）或 faithful（更忠实）。 |
| texture\_delight | 否 | bool | 是否移除参考图像中的高光和烘焙光照，默认 false。 |

**输出参数**

| 参数名称 | 类型 | 描述 |
| --- | --- | --- |
| id | string | 任务 ID，有效期24小时，用于查询任务状态。  示例值：1315932989749215232 |
| object | string | 返回对象类型，3D 任务固定为 3d\_job。 |
| created\_at | int | 任务创建时间（Unix 时间戳）。 |
| status | string | 任务状态。提交成功时为 queued。 |
| request\_id | string | 请求追踪 ID，用于定位问题。 |

### 查询3D 生成任务

**输入参数**

| 参数名称 | 必选 | 类型 | 参数描述 |
| --- | --- | --- | --- |
| model | 是 | string | 模型名称。默认为 rodin-gen-3d-2.5。  示例值：rodin-gen-3d-2.5 |
| id | 是 | string | 提交接口返回的任务 ID。  示例值：1315932989749215232 |

**输出参数**

| 参数名称 | 类型 | 描述 |
| --- | --- | --- |
| request\_id | string | 请求追踪 ID，用于定位问题。 |
| object | string | 返回对象类型，3D 任务固定为 3d\_job。 |
| created\_at | int | 任务创建时间（Unix 时间戳）。 |
| status | string | 任务状态：queued（等待中）、in\_progress（执行中）、completed（任务成功）、failed（任务失败）。 |
| data | array | 生成结果文件列表，仅 completed 状态返回。 |
| data[n].name | string | 文件名称，如 model.glb。 |
| data[n].url | string | 文件下载 URL，有效期1天。 |
| error | object | 错误信息，仅 failed 状态返回。 |
| error.code | string | 错误码。 |
| error.message | string | 错误信息。 |
| error.type | string | 错误类型。 |

## 示例

### 提交3D 生成任务

**输入示例**

```java
curl --location --request POST 'https://tokenhub.tencentmaas.com/v1/api/3d/submit' \\
--header "Authorization: Bearer ${APIKEY}" \\
--header 'Content-Type: application/json' \\
--data-raw '{
  "model": "rodin-gen-3d-2.5",
  "tier": "Gen-2.5-Medium",
  "images": [
    "https://example.com/input.png"
  ]
}'
```

**输出示例**

```java
{
  "created_at": 1791431478,
  "id": "<JOB_ID>",
  "object": "3d_job",
  "request_id": "<REQUEST_ID>",
  "status": "queued"
}
```

### 查询3D 生成任务

**输入示例**

```java
curl --location --request POST 'https://tokenhub.tencentmaas.com/v1/api/3d/query' \\
--header "Authorization: Bearer ${APIKEY}" \\
--header 'Content-Type: application/json' \\
--data-raw '{
  "model": "rodin-gen-3d-2.5",
  "id": "<JOB_ID>"
}'
```

**输出示例**

```java
{
  "created_at": 1791431598,
  "data": [
    {
      "name": "base_basic_pbr.glb",
      "url": "https://example.com/base_basic_pbr.glb"
    },
    {
      "name": "preview.webp",
      "url": "https://example.com/preview.webp"
    }
  ],
  "object": "3d_job",
  "request_id": "<REQUEST_ID>",
  "status": "completed"
}
```

## 错误码

| 错误码 | HTTP 状态码 | 说明 |
| --- | --- | --- |
| InvalidParameter.InvalidParameter | 400 | 请求参数不合法。 |
| InvalidParameter.InputRequired | 400 | images 和 prompt 必填其一。 |
| InvalidParameter.InputConflict | 400 | images 和 prompt 不能同时存在。 |
| InvalidParameter.TierNotValid | 400 | tier 取值不在合法范围内。 |
| InvalidParameter.ImagesExceedsLimit | 400 | 图片数量超限，最多5张。 |
| InvalidParameter.PromptTooLong | 400 | prompt 文本长度超限。 |
| InvalidParameter.FileTypeNotSupported | 400 | 图片中未检测到有效对象。 |
| RequestLimitExceeded.JobNumExceed | 429 | API 并发限制已达上限。 |
| FailedOperation.ModerationFailed | 400 | 图片内容违规，审核不通过。 |
| FailedOperation.ImageSizeExceed | 400 | 图片标签数量超出限制。 |
| FailedOperation.InnerError | 500 | 内部服务错误，包括任务不存在、原厂未知错误、订阅过期或权限不足等情况。 |
| FailedOperation.ServerError | 500 | 算法服务异常。 |
