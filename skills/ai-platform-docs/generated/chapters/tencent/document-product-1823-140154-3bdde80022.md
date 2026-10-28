<!-- Official source: https://cloud.tencent.com/document/product/1823/140154 -->
<!-- Source SHA-256: 88a655bb6fb535f5b2bd854723fc17a0dacd1ae2e6ecbea9d026b49f8b71d9b1 -->

# Tenlai 异步语音识别

官方来源：https://cloud.tencent.com/document/product/1823/140154
最近更新时间：2026-10-27 16:28:48

## 概述

TokenHub 已上线语音识别（ASR）能力，本文对应**天籁非实时、异步语音识别**调用指南。模型为 `tenlai-asr-v1.0。`接口为**异步接口**：提交识别任务后返回任务标识，需通过任务查询接口轮询获取识别结果。

## 前提条件

已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号并开通 TokenHub 服务。

已在 [TokenHub 控制台](https://console.cloud.tencent.com/tokenhub/apikey) 获取 API Key。

## 接口信息

| 项 | 值 |
| --- | --- |
| 地址 | https://tokenhub.tencentmaas.com/v1/tenlai/asrproxy/create\_rec\_task |
| 方法 | POST |
| Content-Type | application/json |
| 鉴权 | Authorization: Bearer YOUR\_API\_KEY |

## 支持模型

<table><colgroup><col/><col/><col/></colgroup><tbody><tr><td><div>模型名称</div></td><td><div>model（调用参数）</div></td><td><div>能力说明</div></td></tr><tr><td colspan="1" rowspan="1"><div>Tenlai-ASR-v1</div></td><td colspan="1" rowspan="1"><div><code>tenlai-asr-v1.0</code></div></td><td><div>中文普通话、英语及多种方言的混合引擎，可适用于中英文识别、普通话与方言识别等场景。</div><div>除普通话和英语外，还支持以下31种方言：</div><div>粤语、武汉话、贵阳话、西安话、郑州话、太原话、兰州话、银川话、西宁话、南京话、合肥话、南昌话、长沙话、苏州话、杭州话、济南话、天津话、石家庄话、黑龙江话、吉林话、辽宁话、闽南语、客家话、南宁话、潮汕话、宁波话、无锡话、吴语、上海话、四川话、昆明话。</div></td></tr></tbody></table>

## 发起异步语音识别任务

### 请求示例

cURL

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/tenlai/asrproxy/create_rec_task' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H "Content-Type: application/json" \\
  -d '{
    "model": "tenlai-asr-v1.0",
    "input_url": "https://cos.example.com/xxx.mp4"
  }'
```

### 请求参数

| 参数 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| model | string | 是 | 模型名称，固定为 `tenlai-asr-v1.0`。 |
| input\_url | string | 否（二选一） | 待识别的音视频文件地址（支持常见音视频格式）。最大支持音频/视频时长 <= 5小时，需要公网可访问（http/https）。 |
| data | string | 否（二选一） | base64编码的音频文件。 |

### 返回示例

**说明：**

接口为异步提交，返回任务标识，不立即返回识别结果。

```json
{
    "id": 17256336078,
    "request_id": "94f62035-de54-40dd-b32e-4ed8f0310ed0"
}
```

### 返回字段

<table><colgroup><col/><col/><col/></colgroup><tbody><tr><td><div>字段</div></td><td><div>类型</div></td><td><div>说明</div></td></tr><tr><td><div>id</div></td><td><div>string</div></td><td><div>任务标识，用于后续查询任务结果。</div></td></tr><tr><td><div>request_id</div></td><td colspan="1" rowspan="1"><div>string</div></td><td colspan="1" rowspan="1"><div>本次会话 ID，用于咨询/反馈时定位问题。</div></td></tr></tbody></table>

## 异步任务查询

### 接口信息

| 项 | 值 |
| --- | --- |
| 地址 | https://tokenhub.tencentmaas.com/v1/tenlai/asrproxy/describe\_task\_status |
| 方法 | POST |
| Content-Type | application/json |
| 鉴权 | Authorization: Bearer YOUR\_API\_KEY |

### 请求示例

cURL

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/tenlai/asrproxy/describe_task_status' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H "Content-Type: application/json" \\
  -d '{
    "model": "tenlai-asr-v1.0",
    "task_id": 17256336078
  }'
```

### 响应字段

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| request\_id | string | 请求标识。 |
| id | string | 任务标识。 |
| object | string | 对象类型，固定 asr.task。 |
| status | string | 任务状态：queued / in\_progress / completed / failed。 |
| output.text | string | 全文识别文本。 |
| audio\_duration | int64 | 音频总时长（秒）。 |
| error | object | 错误信息，仅 failed 时存在。 |

### 返回示例

```json
{
    "request_id": "b69af3ab-05f8-4493-9946-b81fc08ac97c",
    "id": 17256336078,
    "status": "completed",
    "output": {
        "text": "[0:0.000,0:4.850]  然后最后一点就是我们今年做这个 voc这个分析平台，\\n"
    },
    "audio_duration": 746.098625,
    "object": "asr.task"
}
```

## 错误码

请参见 [API 错误码说明](https://cloud.tencent.com/document/product/1823/131595)。
