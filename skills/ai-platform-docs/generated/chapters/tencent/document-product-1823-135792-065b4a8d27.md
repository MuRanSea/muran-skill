<!-- Official source: https://cloud.tencent.com/document/product/1823/135792 -->
<!-- Source SHA-256: f39549b709e3ca83076069b3af563d3a911deabc45cfcb4609485856061d1480 -->

# Hy 异步语音识别

官方来源：https://cloud.tencent.com/document/product/1823/135792
最近更新时间：2026-09-29 17:39:23

## 概述

Tokenhub 已上线语音识别（ASR）能力，本文对应**混元非实时、异步语音识别**调用指南。接口为**异步接口**：提交识别任务后返回任务标识，需通过任务查询接口轮询获取识别结果。

## 前提条件

已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号并开通 TokenHub 服务。

已在 [TokenHub 控制台](https://console.cloud.tencent.com/tokenhub/apikey) 获取 API Key。

## 接口信息

| 项 | 值 |
| --- | --- |
| 地址 | https://tokenhub.tencentmaas.com/v1/wand/asrproxy/async\_create |
| 方法 | POST |
| Content-Type | application/json |
| 鉴权 | Authorization: Bearer YOUR\_API\_KEY |

## 支持模型

<table><colgroup><col/><col/><col/></colgroup><tbody><tr><td><div>模型名称</div></td><td><div>model（调用参数）</div></td><td><div>能力说明</div></td></tr><tr><td colspan="1" rowspan="1"><div>Hy-ASR-3.0-Preview</div></td><td colspan="1" rowspan="1"><div><code>hy-asr-3.0-preview</code></div></td><td><div>中文普通话+英语＋多方言混合引擎，除中英外，支持多种方言，包括粤语、东北话、河南话、陕西话、成都话、重庆话、武汉话、贵阳话、青岛话、济南话、长沙话、合肥话等。</div></td></tr></tbody></table>

## 发起异步语音识别任务

### 请求示例

cURL

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/asrproxy/async_create' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H "Content-Type: application/json" \\
  -d '{
    "model": "hy-asr-3.0-preview",
    "input_url": "https://cos.example.com/xxx.mp4"
  }'
```

### 请求参数

| 参数 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| model | string | 是 | 模型名称，固定为 `hy-asr-3.0-preview`。 |
| input\_url | string | 是 | 待识别的音视频文件地址（支持常见音视频格式）。最大支持音频/视频时长 <= 10小时，文件大小 <= 10GB，处理速度 2～3 倍速；需要公网可访问（http/https）。 |
| source | string | 否 | 识别语种；缺省时后端自动检测。 |
| subtitle\_format | string | 否 | 字幕格式：srt / vtt；缺省 srt。 |

### 返回示例

**说明：**

接口为异步提交，返回任务标识，不立即返回识别结果。

```json
{
  "id": "th_251416641_700001910665_asrproxy_781c68c15207f3a7fc6c7ca48512b964",
  "created_at": 1721808000,
  "status": "queued",
  "request_id": "64094fda-c5ae-4e32-97cf-1cf71ff2ae09"
}
```

### 返回字段

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 任务标识，用于后续查询任务结果。 |
| status | string | 任务状态：queued / in\_progress / completed / failed。 |

## 异步任务查询

### 接口信息

| 项 | 值 |
| --- | --- |
| 地址 | https://tokenhub.tencentmaas.com/v1/wand/asrproxy/tasks/{id} |
| 方法 | GET |
| Content-Type | application/json |
| 鉴权 | Authorization: Bearer YOUR\_API\_KEY |

### 请求示例

cURL

```bash
curl -X GET 'https://tokenhub.tencentmaas.com/v1/wand/asrproxy/tasks/YOUR_TASK_ID' \\
  -H 'Authorization: Bearer YOUR_API_KEY'
```

### 响应字段

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| request\_id | string | 请求标识。 |
| id | string | 任务标识。 |
| object | string | 对象类型，固定 asr.task。 |
| created\_at | int | 创建时间戳（Unix 秒）。 |
| status | string | 任务状态：queued / in\_progress / completed / failed。 |
| output.source | string | 实际识别的语种。 |
| output.duration\_ms | int64 | 音频总时长（毫秒）。 |
| output.text | string | 全文识别文本。 |
| output.sentences[] | array | 分句时间戳：{ begin\_ms, end\_ms, text }。 |
| output.subtitle\_url | string | 字幕文件下载 URL。 |
| usage.total\_token | int64 | 消耗 token 总数。 |
| error | object | 错误信息，仅 failed 时存在。 |

### 返回示例

```json
{
  "id": "th_251416641_700001910665_asrproxy_781c68c15207f3a7fc6c7ca48512b964",
  "object": "asr.task",
  "created_at": 1721808000,
  "status": "completed",
  "request_id": "b1504f51-0d47-4662-8389-c76b9b0db54e",
  "output": { "subtitle_url": "https://xxx.cos.ap-guangzhou.myqcloud.com/subtitle/xxx.srt" },
  "usage":  { "total_token": 6025 }
}
```

## 错误码

请参见 [API 错误码说明](https://cloud.tencent.com/document/product/1823/131595)。
