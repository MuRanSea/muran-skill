<!-- Official source: https://cloud.tencent.com/document/product/1823/130849 -->
<!-- Source SHA-256: ae47d8a7cbbe60d087c98db18731b24367668ff3c18fc75a319c930ed193b384 -->

# 批量推理

官方来源：https://cloud.tencent.com/document/product/1823/130849
最近更新时间：2026-10-29 17:57:30

批量推理适用于对实时性要求不高、但需要大规模调用模型处理数据的场景。用户可将待处理的文本、图片或多模态数据整理为批量任务，由平台异步完成推理并输出结果，避免逐条调用 API 带来的开发和调度成本。典型场景包括离线内容审核、文档摘要生成、知识库数据清洗、客服对话质检、商品标题与描述生成、营销素材批量改写、数据标注辅助、模型效果评测等。通过批量推理，用户可以更低成本、更高效率地完成大规模 AI 任务处理，适合业务验证、周期性数据加工和生产环境中的离线智能处理流程。

Tokenhub 支持以 API 的形式发起批量推理任务，以下介绍使用方法：

## BaseURL

境内：`https://tokenhub.tencentmaas.com/v1/chat/completions`

## 支持的模型

<table><colgroup><col/><col/></colgroup><tbody><tr><td><div><b>模型名称</b></div></td><td><div><b>model 参数值</b></div></td></tr><tr><td><div>Hy3</div></td><td><div><code>hy3</code></div></td></tr><tr><td colspan="1" rowspan="1"><div>Hy4 preview</div></td><td colspan="1" rowspan="1"><div><code>hy4-preview</code></div></td></tr></tbody></table>

## 使用步骤

### 步骤一：准备推理数据

支持 JSONL 格式文件，每行一条。需将文件上传到**用户自有** [腾讯云 COS 桶](https://console.cloud.tencent.com/cos/bucket)**（支持公开桶和私有桶模式）**，通过 `cos://` 路径引用。

数据参考如下：

```json
{"custom_id":"req-001","method":"POST","url":"/v1/chat/completions","body":{"model":"hy3","messages":[{"role":"user","content":"你好，请介绍一下你自己"}],"max_tokens":200}}
{"custom_id":"req-002","method":"POST","url":"/v1/chat/completions","body":{"model":"hy3","messages":[{"role":"user","content":"请用一句话总结机器学习"}],"max_tokens":200}}
```

**注意：**

当前暂不支持在同一个数据文件中使用不同的模型，请确保同一个 JSONL 文件中 `body.model` 的唯一性。

字段说明：

| 字段 | 必填 | 说明 |
| --- | --- | --- |
| custom\_id | 是 | 自定义请求 ID，文件内唯一，用于关联输出结果。 |
| method | 是 | 固定填 "POST"。 |
| url | 是 | 固定填 "/v1/chat/completions"。 |
| body.messages | 是 | 对话消息，格式同 Chat Completions API。 |
| body.max\_tokens | 否 | 最大输出 Token 数。 |

### 步骤二：创建批量任务

请求参数：

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| input\_source | 是 | String | 固定填 `"user_cos"`，表示从用户自有 COS 读取输入文件。 |
| input\_file\_id | 是 | String | 输入文件路径，格式为 `cos://bucket 名.地域/输入文件对象 key`，需使用用户自有 COS 桶。 |
| output\_target | 是 | String | 固定填 `"user_cos"`，表示将结果回写到用户自有 COS 桶。 |
| output\_user\_cos\_path | 是 | String | 结果回写到用户自有 COS 的目录路径，格式为 `cos://bucket 名.地域/目录/`（**必须以** `/` **结尾）**。 |
| completion\_window | 是 | String | 任务处理最大时长，单位为小时（h），如：`24h`，超出时长后，未处理的数据将不再处理。 |
| name | 是 | String | 任务名称。 |

输入示例：

```bash
API_KEY="sk-xxxxx"  # 请替换为实际的 API Key
BASE_URL="https://tokenhub.tencentmaas.com"

# 国内站：tokenhub.tencentmaas.com

# 替换为您的 COS 信息
INPUT_BUCKET="your-bucket-1250000000"   # COS bucket 名（含 appid 后缀）
INPUT_REGION="ap-guangzhou"             # bucket 所在地域
INPUT_KEY="inputs/batch-data.jsonl"     # 输入文件对象 key
OUTPUT_PREFIX="outputs/"                # 结果回写目录（必须以 / 结尾）

curl -X POST "${BASE_URL}/v1/batches" \\
  -H "Authorization: Bearer ${API_KEY}" \\
  -H "Content-Type: application/json" \\
  -d '{
    "input_source": "user_cos",
    "input_file_id": "cos://'"${INPUT_BUCKET}"'.'"${INPUT_REGION}"'/'"${INPUT_KEY}"'",
    "output_target": "user_cos",
    "output_user_cos_path": "cos://'"${INPUT_BUCKET}"'.'"${INPUT_REGION}"'/'"${OUTPUT_PREFIX}"'",
    "completion_window": "24h",
    "name": "my-batch-cos"
  }'
```

响应示例（HTTP 202）：

```json
{
  "id": "batch_a1b2c3d4-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "object": "batch",
  "endpoint": "/v1/chat/completions",
  "input_file_id": "cos://your-bucket-1250000000.ap-guangzhou/inputs/batch-data.jsonl",
  "completion_window": "24h",
  "status": "validating",
  "output_file_id": null,
  "error_file_id": null,
  "created_at": 1744689600,
  "expires_at": 1744948800,
  "request_counts": {"total": 1000, "completed": 0, "failed": 0}
}
```

**注意：**

1. 若 input\_file\_id 无法访问，创建会立即返回 400 input\_file\_unavailable。

2. 返回的 id（即 batch\_id）可用于后续查询。

### 步骤三：查询任务状态

```bash
# 请将 YOUR_API_KEY 替换为您的 API KEY（sk- 开头）
BATCH_ID="batch_a1b2c3d4-xxxx-xxxx-xxxx-xxxxxxxxxxxx"  # 替换为创建时返回的 id
curl "https://tokenhub.tencentmaas.com/v1/batches/${BATCH_ID}" \\ 
  -H "Authorization: Bearer ${YOUR_API_KEY}"
```

任务完成后（status: "completed"）响应：

```json
{
  "id": "batch_a1b2c3d4-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "status": "completed",
  "output_file_id": "https://internal-cos.cos.ap-guangzhou.myqcloud.com/batch_.../output.jsonl?q-sign-algorithm=sha1&q-ak=...&q-signature=...",
  "error_file_id": null,
  "request_counts": {"total": 1000, "completed": 998, "failed": 2}
}
```

状态说明：

| 状态 | 说明 |
| --- | --- |
| validating | 已提交，正在验证和排队 |
| in\_progress | 执行中，`request_counts.completed` 实时更新 |
| completed | 已完成，`output_file_id` / `error_file_id` 有效 |
| cancelling | 取消中 |
| cancelled | 已取消 |
| failed | 任务失败 |
| expired | 超过 `completion_window` 未完成 |

### 步骤四：下载结果

```bash
# 针对特定的 BATCH_ID，从查询响应中提取 output_file_id 并下载
# 请将 YOUR_API_KEY 替换为您的 API KEY（sk- 开头）
BATCH_RESP=$(curl -s "https://tokenhub.tencentmaas.com/v1/batches/${BATCH_ID}" \\ 
  -H "Authorization: Bearer ${API_KEY}")

OUTPUT_URL=$(echo "${BATCH_RESP}" | python3 -c \\ 
  "import sys,json; d=json.load(sys.stdin); print(d.get('output_file_id') or '')")

ERROR_URL=$(echo "${BATCH_RESP}" | python3 -c \\ 
  "import sys,json; d=json.load(sys.stdin); print(d.get('error_file_id') or '')")

# 下载成功结果
[ -n "${OUTPUT_URL}" ] && curl -o output.jsonl "${OUTPUT_URL}" && echo "已保存 output.jsonl"

# 下载失败记录（有失败行时才有）
[ -n "${ERROR_URL}" ] && curl -o error.jsonl "${ERROR_URL}" && echo "已保存 error.jsonl"
```

**注意：**

任务完成后，结果文件会直接写入您创建任务时指定的 `output_user_cos_path` 目录，`output_file_id` 返回对应的 `cos://` 路径，可直接在 COS 控制台或通过 COS SDK 下载。

output.jsonl 每行格式（兼容 OpenAI）：

```json
{
  "id": "batch_req_req-001",
  "custom_id": "req-001",
  "response": {
    "status_code": 200,
    "body": {
      "id": "chatcmpl-xxx",
      "object": "chat.completion",
      "model": "hy3",
      "choices": [{"message": {"role": "assistant", "content": "..."}, "finish_reason": "stop"}],
      "usage": {"prompt_tokens": 10, "completion_tokens": 50, "total_tokens": 60}
    }
  },
  "error": null
}
```

error.jsonl 每行格式（有失败行时）：

```json
{"id":"batch_req_req-002","custom_id":"req-002","response":null,"error":{"code":"rate_limit","message":"429 Too Many Requests"}}
```

## 其他相关接口

### 列表查询

按创建时间倒序，支持游标翻页：

```bash
# 请将 YOUR_API_KEY 替换为您的 API KEY（sk- 开头）
# 第一页
curl "https://tokenhub.tencentmaas.com/v1/batches?limit=20" \\ 
  -H "Authorization: Bearer ${YOUR_API_KEY}"

# 翻页（使用上次响应的 last_id）
curl "https://tokenhub.tencentmaas.com/v1/batches?limit=20&after=batch_xxxxxxxx" \\ 
  -H "Authorization: Bearer ${YOUR_API_KEY}"
```

### 取消任务

```bash
# 请将 YOUR_API_KEY 替换为您的 API KEY（sk- 开头）
curl -X POST "https://tokenhub.tencentmaas.com/v1/batches/${BATCH_ID}/cancel" \\ 
  -H "Authorization: Bearer ${YOUR_API_KEY}"
```

**注意：**

已处于终态（`completed/cancelled/failed/expired`）的任务无法取消，返回 409 Conflict。

## 接口频率限制

| 限制项 | 限额 |
| --- | --- |
| 创建任务 | 20 次/分钟/账号 |
| 并发活跃任务数 | 10 个/账号 |

超出限频返回 HTTP 429，建议使用指数退避策略重试。
