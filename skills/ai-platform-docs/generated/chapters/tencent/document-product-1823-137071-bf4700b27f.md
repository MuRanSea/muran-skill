<!-- Official source: https://cloud.tencent.com/document/product/1823/137071 -->
<!-- Source SHA-256: 601e1c8b3c43dbe4c05a1b348c91775fa48db222a19c6105bcacb8024bb89da8 -->

# Tripo-3D-Animation 调用指南

官方来源：https://cloud.tencent.com/document/product/1823/137071
最近更新时间：2026-10-26 19:10:23

## 简介

Tripo 动画重定向接口，将预设动画应用到已绑骨的 3D 模型上。

## 对接说明

### 1. 获取 API Key

1. 进入 [API Key 管理](https://console.cloud.tencent.com/tokenhub/apikey) 页面，单击**创建 API Key**。操作详情请参见 [创建 API Key](https://cloud.tencent.com/document/product/1823/130090#40882178-aaf2-48c9-8559-dffc083a79bc)。

2. 创建完成后，请您务必**复制并妥善保管 API Key**，在后续配置到工具的流程中将会使用该信息。

![](https://qcloudimg.tencent-cloud.cn/image/document/2511498370a647b7520c70ae00b06568.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/2511498370a647b7520c70ae00b06568.png)

**说明：**

每个账户的密钥都只能当前账户查询，主账户的密钥信息子账户是看不到，子账户如果需要调用接口，需要使用账户自行创建密钥信息。

如果子账户没有办法创建，可能是没有权限创建密钥，需要主账户授权，主账户登录之后点击用户列表，在对应的子账户后面选择授权，会弹出关联策略的弹窗，输入授权策略名称之后搜索，选择对应的策略点击确认。

授权策略：QcloudTokenhubFullAccess

### 2. 并发额度

默认提供1个并发，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后，才能开始处理下一个任务。

并发任务数：表示在调用对应服务的时段内最大可运行的任务数，该任务未完成时，无法提交下一个任务，该任务完成后，可提交下一个任务。

## 接口文档

#### 提交 Tripo 动画重定向任务

**输入参数**

| 参数名称 | 必选 | 类型 | 参数描述 |
| --- | --- | --- | --- |
| model | 是 | string | 模型名称，默认为：tripo-3d-animation  示例值：tripo-3d-animation |
| input | 是 | string | 已绑骨模型的 id |
| animation | 条件必选 | string | 单个预设动画标识符。  与 animations 互斥，只能二选一。  骨骼类型详见：[骨骼类型说明](https://cloud.tencent.com/document/product/1823/137071#c06b9539-7724-4fdc-896c-8ac7f1a4311a) |
| animations | 条件必选 | string[] | 多个预设动画标识符列表，最多 5 个；超过 5 个会报错。  与 animation 互斥，只能二选一。 |
| out\_format | 否 | string | 输出格式。  glb：二进制 glTF，适用于 Web。  fbx：FBX，适用于 DCC 工具和游戏引擎。  默认值: glb |
| export\_with\_geometry | 否 | boolean | 导出时包含几何体。  默认值: true |
| animate\_in\_place | 否 | boolean | 原地播放动画，无位移。  默认值: false |

**输出参数**

| 参数名称 | 类型 | 描述 |
| --- | --- | --- |
| id | string | 任务 id（有效期24小时）。  示例值：1315932989749215232 |
| request\_id | string | 唯一请求 id，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 request\_id）。定位问题时需要提供该次请求的 request\_id。 |
| object | string | 返回对象类型。3d 任务固定返回 3d\_job。 |
| created\_at | integer | 任务创建时间。 |
| status | string | completed：任务成功，failed：任务失败，in\_progress：执行中，queued：等待中。  示例值：completed |

#### 查询 Tripo 动画重定向任务

**输入参数**

| 参数名称 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| model | 是 | string | 模型名称，默认为：tripo-3d-animation  示例值：tripo-3d-animation |
| id | 是 | string | 任务 id。  示例值：1357237233311637504 |

**输出参数**

<table><colgroup><col/><col/><col/></colgroup><tbody><tr><td><div>参数名称</div></td><td><div>类型</div></td><td><div>描述</div></td></tr><tr><td><div>status</div></td><td><div>string</div></td><td><div>completed：任务成功，failed：任务失败，in_progress：执行中，queued：等待中。</div><div>示例值：completed</div></td></tr><tr><td><div>request_id</div></td><td><div>string</div></td><td><div>唯一请求 id，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 request_id）。定位问题时需要提供该次请求的 request_id。</div></td></tr><tr><td><div>output</div></td><td><div>object</div></td><td><div>输出结果（TripoResult，任务完成时返回）</div></td></tr><tr><td><div>output.model_url</div></td><td><div>string</div></td><td><div>模型下载 URL</div></td></tr><tr><td><div>input</div></td><td><div>string</div></td><td><div>输入参数回显</div></td></tr><tr><td><div>object</div></td><td><div>string</div></td><td><div>返回对象类型。3d 任务固定返回 3d_job。</div></td></tr><tr><td><div>created_at</div></td><td><div>integer</div></td><td><div>任务创建时间。</div></td></tr><tr><td><div>completed_at</div></td><td><div>integer</div></td><td><div>任务完成时间。</div></td></tr><tr><td colspan="1" rowspan="1"><div>credits_consumed</div></td><td colspan="1" rowspan="1"><div>number</div></td><td colspan="1" rowspan="1"><div>当前任务实际消耗的积分数。</div></td></tr></tbody></table>

## 示例

#### 提交 Tripo 动画重定向任务

**输入示例**

```java
curl -X POST 'https://tokenhub.tencentmaas.com/v1/api/3d/submit' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -H 'Accept: */*' \\
  -H 'Connection: keep-alive' \\
  -d '{
    "model": "tripo-3d-animation",
    "input": "ID",
    "animation": "preset:walk"
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

#### 查询 Tripo 动画重定向任务

**输入示例**

```java
curl -X POST 'https://tokenhub.tencentmaas.com/v1/api/3d/query' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -H 'Connection: keep-alive' \\
  -d '{
    "model": "tripo-3d-animation",
    "id": "14721*****320"
  }'
```

**输出示例**

```java
{
  "status": "completed",
  "input":"{\\"animations\\":[\\"preset:walk\\",\\"preset:run\\"],\\"out_format\\":\\"fbx\\",\\"original_model_id\\":\\"XXXXX-5f79-4bfb-9de9-XXXXX\\"}",
  "object": "3d_job",
  "output": {
      "model_url": "https://vcg-prod-1258344699.cos.ap-guangzhou.tencentcos.cn/**********12.glb" 
   },
  "request_id": "XXXXX-c925-4dda-90f0-XXXXX",
  "credits_consumed": 10,
  "created_at": 1785989483,
  "completed_at": 1785989483
}
```

## 骨骼类型说明：

双足：preset:idle、preset:walk、preset:run、preset:dive、preset:climb、preset:jump、preset:slash、preset:shoot、preset:hurt、preset:fall、preset:turn

四足：preset:quadruped:walk

其他：preset:hexapod:walk、preset:octopod:walk、preset:serpentine:march、preset:aquatic:march

| preset:biped:afraid | preset:biped:agree |
| --- | --- |
| preset:biped:angry\_01 | preset:biped:angry\_02 |
| preset:biped:angry\_03 | preset:biped:basketball\_shot |
| preset:biped:bow | preset:biped:box\_01 |
| preset:biped:box\_02 | preset:biped:box\_03 |
| preset:biped:cast\_a\_spell | preset:biped:cheer |
| preset:biped:chop | preset:biped:clap |
| preset:biped:climb | preset:biped:complain\_01 |
| preset:biped:complain\_02 | preset:biped:cross\_body\_crunch |
| preset:biped:crossover\_dribble | preset:biped:cry |
| preset:biped:dance\_01 | preset:biped:dance\_02 |
| preset:biped:dance\_03 | preset:biped:dance\_04 |
| preset:biped:dance\_05 | preset:biped:dance\_06 |
| preset:biped:defeat\_02 | preset:biped:defeat\_03 |
| preset:biped:depressed | preset:biped:dig |
| preset:biped:dive | preset:biped:dribble |
| preset:biped:fall | preset:biped:fire |
| preset:biped:flee\_01 | preset:biped:flee\_02 |
| preset:biped:flip | preset:biped:fold\_arms |
| preset:biped:football\_catch | preset:biped:football\_save |
| preset:biped:football\_pass | preset:biped:freaky |
| preset:biped:frightened | preset:biped:front\_kick\_01 |
| preset:biped:front\_kick\_02 | preset:biped:frustrated\_01 |
| preset:biped:frustrated\_02 | preset:biped:golf |
| preset:biped:greet\_01 | preset:biped:greet\_02 |
| preset:biped:greet\_03 | preset:biped:greet\_04 |
| preset:biped:heart\_pose | preset:biped:hit\_to\_body\_01 |
| preset:biped:hit\_to\_body\_02 | preset:biped:hit\_to\_head |
| preset:biped:hit\_to\_side | preset:biped:hit\_to\_stomach |
| preset:biped:hug | preset:biped:hurt |
| preset:biped:idle | preset:biped:jump\_down |
| preset:biped:jump | preset:biped:jump\_rope\_01 |
| preset:biped:jump\_rope\_02 | preset:biped:laugh\_01 |
| preset:biped:laugh\_02 | preset:biped:lift\_heavy |
| preset:biped:look\_around | preset:biped:make\_a\_call\_01 |
| preset:biped:make\_a\_call\_02 | preset:biped:pitch\_baseball |
| preset:biped:play\_mobile\_game | preset:biped:play\_video\_game |
| preset:biped:press-up | preset:biped:run\_upstairs |
| preset:biped:run | preset:biped:scared\_01 |
| preset:biped:scared\_02 | preset:biped:scratch |
| preset:biped:shoot | preset:biped:shovel |
| preset:biped:sing\_01 | preset:biped:sing\_02 |
| preset:biped:sing\_03 | preset:biped:sing\_04 |
| preset:biped:sit | preset:biped:slash |
| preset:biped:sob | preset:biped:standing\_relax |
| preset:biped:surf | preset:biped:swagger |
| preset:biped:swim | preset:biped:turn |
| preset:biped:victory\_celebration | preset:biped:volleyball |
| preset:biped:wait | preset:biped:walk |
| preset:biped:warm\_up | preset:biped:wave\_goodbye\_01 |
| preset:biped:wave\_goodbye\_02 | - |
