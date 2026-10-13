<!-- Official source: https://cloud.tencent.com/document/product/1823/135800 -->
<!-- Source SHA-256: fb5470c2194576493c03e4086f50e489de56667c3c9efb1bb4ea8f1365e0991c -->

# WAND AI 配音（WAND-Dubbing-Clone）

官方来源：https://cloud.tencent.com/document/product/1823/135800
最近更新时间：2026-09-29 16:23:57

## 概述

TokenHub 已上线 `wand-dubbing-clone` 系列 AI 配音（视频翻译配音）模型，相关能力由 [腾讯云 WAND](https://cloud.tencent.com/product/wand) 提供。

**功能说明：**上传视频 → 识别并翻译视频字幕与语音内容 → 以目标语言重新生成配音及字幕 → 输出翻译后的视频。适用于影视、课程、短视频等内容的多语言翻译与本地化。具体价格请参见 [TokenHub 模型价格说明](https://cloud.tencent.com/document/product/1823/130055)。

**说明：**

本能力为**异步任务**接口（`async_generation`）。提交请求后系统后台处理，不会立即返回配音视频，而是返回任务标识；需通过任务查询接口轮询处理状态与最终结果。

## 前提条件

已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号并开通 TokenHub 服务。

已在 [TokenHub 控制台](https://console.cloud.tencent.com/tokenhub/apikey) 获取 API Key。

## 调用流程

AI 配音为耗时任务，接口采用**异步调用模式**，统一分两步：

1. **提交任务**：调用能力接口（`model` / `input_url` / `src_language` / `dst_language` 等），成功返回 `id`（任务 ID）。

2. **轮询结果**：携带 `id` 调用 [查询任务结果](https://cloud.tencent.com/document/product/1823/135800#56c511d4-d523-4c0b-9690-6336ac61da39) 接口，建议每 **3–5 秒**轮询一次，直至 `status = completed`（生成成功），从 `output.result_url` 获取翻译配音后的视频地址。

**说明：**

任务创建成功后请勿重复提交，通过轮询获取结果即可。

通用响应格式：`request_id`（请求标识）、`object`（对象类型）、`status`（任务状态）、`error`（错误对象，仅失败时存在）。

## 支持模型

| 模型名称 | model（调用参数） | 能力说明 |
| --- | --- | --- |
| WAND AI 配音-克隆音色  （WAND-Dubbing-Clone-V1） | `wand-dubbing-clone-v1` | 翻译视频字幕与配音，输出目标语言视频。 |
| WAND AI 配音-克隆音色-加强版  （WAND-Dubbing-Clone-V2） | `wand-dubbing-clone-v2` | 翻译视频字幕与配音，输出目标语言视频。最新模型版本，相比 v1 表达措辞更自然，高保真还原原声情绪、语气与说话韵律，复刻质感更贴近真人原版。 |

## 发起异步配音任务

### 接口信息

| 项 | 值 |
| --- | --- |
| 地址 | `https://tokenhub.tencentmaas.com/v1/wand/dubbing/async_generation` |
| 方法 | POST |
| Content-Type | `application/json` |
| 鉴权 | `Authorization: Bearer YOUR_API_KEY` |

### 请求示例

cURL

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/wand/dubbing/async_generation' \\
  -H 'Authorization: Bearer YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{
    "model": "wand-dubbing-clone-v1",
    "input_url": "https://example.com/video.mp4",
    "src_language": "zh",
    "dst_language": "en"
  }'

```

### 请求参数

| 参数 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `model` | string | 是 | 配音模型，可选 `wand-dubbing-clone-v1` / `wand-dubbing-clone-v2` |
| `input_url` | string | 是 | 视频（单个）：支持 URL 和 Base64格式，视频格式：mp4/mov/m4v；单个视频时长 ≤ 45分钟；  1. Base64：单个视频大小 ≤ 75MB，转为 Base64大小 ≤ 100MB；格式要求：data:video/<视频格式>;base64,<Base64 编码>。注：视频为 mov 时视频格式填 quicktime。  2. URL：单个文件大小 ≤ 1GB；需要公网可访问（http/https）。 |
| `src_language` | string | 否 | 源语言代码，如 `zh`（中文）、`en`（英文）等，具体支持语言请参见 [附录：支持语种](https://cloud.tencent.com/document/product/1823/135800#lan)，默认 `zh` |
| `dst_language` | string | 否 | 目标语言代码，如 `zh`（中文）、`en`（英文）等，具体支持语言请参见 [附录：支持语种](https://cloud.tencent.com/document/product/1823/135800#lan)，默认 `en` |

### 返回示例

**说明：**

本接口为异步任务，提交成功后返回任务标识（`id`），用于后续查询。

```json
{
  "request_id": "req-xxx",
  "id": "th_xxxx_xxxx_dubbing_xxxxxxxxx",
  "object": "dubbing.task",
  "created_at": 1753172400,
  "status": "queued"
}
```

### 返回字段

<table><colgroup><col/><col/><col/></colgroup><tbody><tr><td><div>字段</div></td><td><div>类型</div></td><td><div>说明</div></td></tr><tr><td><div><code>id</code></div></td><td><div>string</div></td><td><div>任务标识，用于查询任务状态与最终结果。</div></td></tr><tr><td><div><code>request_id</code></div></td><td><div>string</div></td><td><div>请求标识。</div></td></tr><tr><td colspan="1" rowspan="1"><div><code>object</code></div></td><td colspan="1" rowspan="1"><div>string</div></td><td colspan="1" rowspan="1"><div>对象类型，固定 dubbing.task。</div></td></tr><tr><td><div><code>status</code></div></td><td><div>string</div></td><td><div>任务状态：<code>queued</code>（已提交）/ <code>in_progress</code>（处理中）/ <code>completed</code>（完成）/ <code>failed</code>（失败）。</div></td></tr><tr><td><div><code>created_at</code></div></td><td><div>int</div></td><td><div>创建时间戳。</div></td></tr></tbody></table>

## 异步任务查询

提交 `async_generation` 后，需通过任务查询接口轮询处理状态，待任务完成后获取翻译配音的视频结果。

### 接口信息

| 项 | 值 |
| --- | --- |
| 地址 | `https://tokenhub.tencentmaas.com/v1/wand/dubbing/tasks/{id}`  **说明：**  `{id}` 为提交返回的任务标识。 |
| 方法 | GET |
| 鉴权 | `Authorization: Bearer YOUR_API_KEY` |

### 请求示例

cURL

```bash
curl -X GET 'https://tokenhub.tencentmaas.com/v1/wand/dubbing/tasks/YOUR_ID' \\
  -H 'Authorization: Bearer YOUR_API_KEY'
```

### 返回说明

返回指定任务的状态与结果。任务成功时返回翻译配音后的视频地址等结果。

### 返回示例

```json
{
  "request_id": "req-xxx",
  "id": "th_xxxx_xxxx_dubbing_xxxxxxxxx",
  "object": "dubbing.task",
  "status": "completed",
  "output": {
    "result_url": "https://xxx.mp4"
  },
  "usage": {
    "total_tokens": 118240,
    "duration": 12.5
  }
}
```

### 返回字段

<table><colgroup><col/><col/><col/></colgroup><tbody><tr><td><div>字段</div></td><td><div>类型</div></td><td><div>说明</div></td></tr><tr><td><div>id</div></td><td><div>string</div></td><td><div>任务标识，用于查询任务状态与最终结果。</div></td></tr><tr><td><div>request_id</div></td><td><div>string</div></td><td><div>请求标识。</div></td></tr><tr><td><div>status</div></td><td><div>string</div></td><td><div>任务状态：queued（已提交）/ in_progress（处理中）/ completed（完成）/ failed（失败）等，以 TokenHub 实际返回为准。</div></td></tr><tr><td colspan="1" rowspan="1"><div>object</div></td><td colspan="1" rowspan="1"><div>string</div></td><td colspan="1" rowspan="1"><div>对象类型，固定 dubbing.task。</div></td></tr><tr><td><div>created_at</div></td><td><div>int</div></td><td><div>创建时间戳。</div></td></tr><tr><td><div>error</div></td><td><div>object</div></td><td><div>错误信息，仅任务状态为 failed 时存在。</div></td></tr><tr><td><div>error.code</div></td><td><div>string</div></td><td><div>6 位业务错误码，前 3 位 = HTTP 状态码。</div></td></tr><tr><td><div>error.type</div></td><td><div>string</div></td><td><div>错误类型枚举。</div></td></tr><tr><td><div>error.message</div></td><td><div>string</div></td><td><div>英文错误描述。</div></td></tr><tr><td><div>error.message_zh</div></td><td><div>string</div></td><td><div>中文错误描述。</div></td></tr><tr><td><div>error.source</div></td><td><div>string</div></td><td><div>错误来源：client（客户端）/ gateway（网关）/ upstream（上游）。</div></td></tr><tr><td><div>error.upstream_status</div></td><td><div>int</div></td><td><div>仅 source=upstream 时存在，后端原始 HTTP 状态码。</div></td></tr><tr><td><div>error.request_id</div></td><td><div>string</div></td><td><div>请求唯一标识。</div></td></tr><tr><td><div>output</div></td><td><div>object</div></td><td><div>任务结果，仅任务状态为 completed 时存在。</div></td></tr><tr><td><div>output.result_url</div></td><td><div>string</div></td><td><div>结果视频地址。</div></td></tr><tr><td><div>usage</div></td><td><div>object</div></td><td><div>用量信息，仅任务状态为 completed 时存在。</div></td></tr><tr><td><div>usage.total_token</div></td><td><div>int</div></td><td><div>本次任务消耗 token 总数。</div></td></tr><tr><td><div>usage.duration</div></td><td><div>float</div></td><td><div>本次任务输入时长（秒）。</div></td></tr></tbody></table>

## 附录：支持语种

WAND AI 配音支持以下语种：

<table><colgroup><col/><col/><col/><col/></colgroup><tbody><tr><td><div>语种</div></td><td><div>Code</div></td><td><div>是否可用于源语言（src_language）</div></td><td><div>是否可用于翻译目标语言（dst_language）</div></td></tr><tr><td><div>中文 (Chinese)</div></td><td><div>zh</div></td><td><div>✓</div></td><td><div>✓</div></td></tr><tr><td><div>英语 (English)</div></td><td><div>en</div></td><td><div>✓</div></td><td><div>✓</div></td></tr><tr><td><div>日语 (Japanese)</div></td><td><div>ja</div></td><td><div>✓</div></td><td><div>✓</div></td></tr><tr><td><div>德语 (German)</div></td><td><div>de</div></td><td><div>✓</div></td><td><div>✓</div></td></tr><tr><td><div>法语 (French)</div></td><td><div>fr</div></td><td><div>✓</div></td><td><div>✓</div></td></tr><tr><td><div>韩语 (Korean)</div></td><td><div>ko</div></td><td><div>✓</div></td><td><div>✓</div></td></tr><tr><td><div>俄语 (Russian)</div></td><td><div>ru</div></td><td><div>✓</div></td><td><div>✓</div></td></tr><tr><td><div>乌克兰语 (Ukrainian)</div></td><td><div>uk</div></td><td><div>✓</div></td><td><div>✓</div></td></tr><tr><td><div>葡萄牙语 (Portuguese)</div></td><td><div>pt</div></td><td><div>✓</div></td><td><div>✓</div></td></tr><tr><td><div>意大利语 (Italian)</div></td><td><div>it</div></td><td><div>✓</div></td><td><div>✓</div></td></tr><tr><td><div>西班牙语 (Spanish)</div></td><td><div>es</div></td><td><div>✓</div></td><td><div>✓</div></td></tr><tr><td><div>印度尼西亚语 (Indonesian)</div></td><td><div>id</div></td><td><div>✓</div></td><td><div>✓</div></td></tr><tr><td><div>荷兰语 (Dutch)</div></td><td><div>nl</div></td><td><div>✓</div></td><td><div>✓</div></td></tr><tr><td><div>土耳其语 (Turkish)</div></td><td><div>tr</div></td><td><div>✓</div></td><td><div>✓</div></td></tr><tr><td><div>菲律宾语 (Filipino)</div></td><td><div>fil</div></td><td><div>✓</div></td><td><div>✓</div></td></tr><tr><td><div>马来语 (Malay)</div></td><td><div>ms</div></td><td><div>✓</div></td><td><div>✓</div></td></tr><tr><td><div>希腊语 (Greek)</div></td><td><div>el</div></td><td><div>✓</div></td><td><div>✓</div></td></tr><tr><td><div>芬兰语 (Finnish)</div></td><td><div>fi</div></td><td><div>✓</div></td><td><div>✓</div></td></tr><tr><td><div>克罗地亚语 (Croatian)</div></td><td><div>hr</div></td><td><div>✓</div></td><td><div>✓</div></td></tr><tr><td><div>斯洛伐克语 (Slovak)</div></td><td><div>sk</div></td><td><div>✓</div></td><td><div>✓</div></td></tr><tr><td><div>波兰语 (Polish)</div></td><td><div>pl</div></td><td><div>✓</div></td><td><div>✓</div></td></tr><tr><td><div>瑞典语 (Swedish)</div></td><td><div>sv</div></td><td><div>✓</div></td><td><div>✓</div></td></tr><tr><td><div>印地语 (Hindi)</div></td><td><div>hi</div></td><td><div>✓</div></td><td><div>✓</div></td></tr><tr><td><div>保加利亚语 (Bulgarian)</div></td><td><div>bg</div></td><td><div>✓</div></td><td><div>✓</div></td></tr><tr><td><div>罗马尼亚语 (Romanian)</div></td><td><div>ro</div></td><td><div>✓</div></td><td><div>✓</div></td></tr><tr><td><div>阿拉伯语 (Arabic)</div></td><td><div>ar</div></td><td><div>✓</div></td><td><div>✓</div></td></tr><tr><td><div>捷克语 (Czech)</div></td><td><div>cs</div></td><td><div>✓</div></td><td><div>✓</div></td></tr><tr><td><div>丹麦语 (Danish)</div></td><td><div>da</div></td><td><div>✓</div></td><td><div>✓</div></td></tr><tr><td><div>泰米尔语 (Tamil)</div></td><td><div>ta</div></td><td><div>✓</div></td><td><div>✓</div></td></tr><tr><td><div>匈牙利语（Hungarian）</div></td><td><div>hun</div></td><td><div>✓</div></td><td><div>✓</div></td></tr><tr><td><div>越南语（Vietnamese）	</div></td><td><div>vi</div></td><td><div>✓</div></td><td><div>✓</div></td></tr><tr><td><div>泰语（Thai）</div></td><td><div>th</div></td><td><div>✓</div></td><td><div>✓</div></td></tr><tr><td colspan="1" rowspan="1"><div>粤语（Cantonese）</div></td><td colspan="1" rowspan="1"><div>yue</div></td><td colspan="1" rowspan="1"><div>✓</div></td><td colspan="1" rowspan="1"><div>✓</div></td></tr></tbody></table>

## 错误码

请参见 [API 错误码说明](https://cloud.tencent.com/document/product/1823/131595)。
