<!-- Official source: https://cloud.tencent.com/document/product/1823/137779 -->
<!-- Source SHA-256: 022f15e0493822141ad15a9245a7b3a940031c8322ebba72a3a5bf0711dd6544 -->

# HY-3D-Rigging 调用指南

官方来源：https://cloud.tencent.com/document/product/1823/137779
最近更新时间：2026-09-09 18:13:35

## 简介

绑骨蒙皮接口，基于混元大模型，根据输入的人物或动物模型进行绑骨蒙皮，输出带骨骼信息的3D 模型。

## 对接说明

### 1. 获取 API Key

1. 进入 [API Key 管理](https://console.cloud.tencent.com/tokenhub/apikey) 页面，单击**创建 API Key**。操作详情请参见 [创建 API Key](https://cloud.tencent.com/document/product/1823/130090#40882178-aaf2-48c9-8559-dffc083a79bc)。

2. 创建完成后，请您务必**复制并妥善保管 API Key**，在后续配置到工具的流程中将会使用该信息。

![](https://qcloudimg.tencent-cloud.cn/image/document/c7a130d10a8fa64257031c2cc2fbc4bd.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/c7a130d10a8fa64257031c2cc2fbc4bd.png)

**说明：**

每个账户的密钥都只能当前账户查询，主账户的密钥信息子账户是看不到，子账户如果需要调用接口，需要使用账户自行创建密钥信息。

如果子账户没有办法创建，可能是没有权限创建密钥，需要主账户授权，主账户登录之后点击用户列表，在对应的子账户后面选择授权，会弹出关联策略的弹窗，输入授权策略名称之后搜索，选择对应的策略点击确认。

授权策略：QcloudTokenhubFullAccess

### 2. 并发额度

默认提供1个并发，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后，才能开始处理下一个任务。

并发任务数：表示在调用对应服务的时段内最大可运行的任务数，该任务未完成时，无法提交下一个任务，该任务完成后，可提交下一个任务。

## 接口文档

### 提交绑骨蒙皮任务

**输入参数**

| 参数名称 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| model | 是 | string | 绑骨蒙皮模型名称，默认为 hy-3d-rigging。  示例值：hy-3d-rigging |
| file\_3d | 是 | object | 人形角色需采用标准姿态（A Pose 或 T Pose），尽量保持无动作状态。  模型中不应包含人体以外的组件（如坐骑、翅膀等），避免松散衣物、配饰及复杂发型。  非人形角色建议上传二足、四足、鸟类等单一生命体模型，姿态应尽量简洁，无夸张或复杂动作，且不支持动作模板生成。3D 模型文件必选其一，参考值：  fbx：3D 模型文件，格式为 fbx，文件大小不超过60mb；  glb：3D 模型文件，格式为 glb，文件大小不超过60mb；  详情请参见 [file\_3d](https://cloud.tencent.com/document/product/1823/137779#44f6b64f-fe91-487d-a298-5b897bde847f) 数据结构。 |
| motion\_type | 否 | Integer | 预设动作类型，参考值：  1. 回旋踢  2. 左勾拳  3. 蓄力攻击  4. 蓄力出拳  5. 二连击打  6. 二连击打-2  7. 后撤  8. 受击  9. 受击-2  10. 受击-3  11. 受击倒地-1  12. 受击倒地-2  13. 落地  14. 沮丧  15. 割喉  16. 刺拳  17. 连续击打  18. 踢腿  19. 侧踢  20. 打太极  21. 后空翻  22. 蹲姿转体  23. 走路-1  24. 走路-2  25. 走路-3  26. 待机-1  27. 待机-2  28. 街舞  29. 扭扭舞  30. 左转弯  31. 右转弯  32. 慢跑  33. 慢跑-2  34. 奔跑  35. 冲刺跑-1  36. 冲刺跑-2  37. 冲刺跑-3  38. 原地跳-1  39. 滑铲  40. 向前大跳  41. 向前大跳-2  42. 跨越  43. 恐吓  44. 向前跌倒  45. 右转  46. 原地跳-2  47. 转身  48. 发送冲击波    示例值：1 |

**输出参数**

| 参数名称 | 类型 | 描述 |
| --- | --- | --- |
| id | string | 任务 id（有效期24小时）。  示例值：1315932989749215232 |
| request\_id | string | 唯一请求 id，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 request\_id）。定位问题时需要提供该次请求的 request\_id。 |
| object | string | 返回对象类型。3d 任务固定返回 3d\_job。 |
| created\_at | integer | 任务创建时间。 |
| status | string | completed：任务成功，failed：任务失败，in\_progress：执行中，queued：等待中。  示例值：completed |

### 查询绑骨蒙皮任务

**输入参数**

| 参数名称 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| model | 是 | string | 绑骨蒙皮模型名称，默认为 hy-3d-rigging。  示例值：hy-3d-rigging |
| id | 是 | string | 任务 id。  示例值：1357237233311637504 |

**输出参数**

| 参数名称 | 类型 | 描述 |
| --- | --- | --- |
| status | string | completed：任务成功，failed：任务失败，in\_progress：执行中，queued：等待中。  示例值：completed |
| request\_id | string | 唯一请求 id，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 request\_id）。定位问题时需要提供该次请求的 request\_id。 |
| object | string | 返回对象类型。3d 任务固定返回 3d\_job。 |
| created\_at | integer | 任务创建时间。 |
| completed\_at | integer | 任务完成时间。 |
| data | array of object | 生成结果列表，包含生成的 3d 模型文件及相关资源信息。详情请参见 [data](https://cloud.tencent.com/document/product/1823/137779#c9bb0852-073e-4e2e-8da9-5359d2b770bb) 数据结构。 |

## 示例

### 提交绑骨蒙皮任务

**输入示例**

```java
curl -X POST 'https://tokenhub.tencentmaas.com/v1/api/3d/submit' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
    "model": "hy-3d-rigging",
    "file_3d": {
        "url": "https://example.com/test.fbx"
    },
    "motion_type": 1
}'
```

**输出示例**

```java
{
  "id": "14721*****320",
  "request_id": "1f64379-bb*****d75fc12365",
  "object": "3d_job",
  "created_at": 1784885898,
  "status": "queued"
}
```

### 查询绑骨蒙皮任务

**输入示例**

```java
curl -X POST 'https://tokenhub.tencentmaas.com/v1/api/3d/query' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
    "model": "hy-3d-rigging",
    "id": "14721*****320"
  }'
```

**输出示例**

```java
{
  "request_id": "1f64379-bb*****d75fc12365",
  "object": "3d_job",
  "created_at": 1788492072,
  "completed_at": 1788492072,
  "status": "completed",
  "data": [
    {
      "type": "fbx",
      "url": "https://vcg-prod-1258344699.cos.ap-guangzhou.tencentcos.cn/auto_rigging/output/1254418*****28-9f58-876386e48d44_0.fbx"
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
