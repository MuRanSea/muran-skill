<!-- Official source: https://cloud.tencent.com/document/product/1823/131410 -->
<!-- Source SHA-256: 0f2b2e2012f50ad5672b128d05d7e53ee6c1d72778d672f48915be8370bca213 -->

# 提升 Cache 命中率指南

官方来源：https://cloud.tencent.com/document/product/1823/131410
最近更新时间：2026-05-11 22:06:01

本文档介绍如何通过合理的请求设计，提升 TokenHub 平台的 Prompt Cache 命中率，从而降低首 Token 响应时间（TTFT）和推理成本。

## 一、使用 prompt\_cache\_key

### 1.1 什么是 prompt\_cache\_key

`prompt_cache_key` 是请求级别的缓存标识字段，用于告诉缓存系统哪些请求的前缀是相同的，可以复用 KV Cache。

其核心原则是：**赋值为整体上下文总 ID（conversation\_id），而非单一会话 ID（session\_id）。**

### 1.2 使用方式

在请求体中添加 `prompt_cache_key` 字段：

```json
{
  "model": "your-model",
  "prompt_cache_key": "conv-6900xxxx",
  "messages": [
    {"role": "system", "content": "你是一个助手..."},
    {"role": "user", "content": "你好"}
  ]
}
```

### 1.3 最佳实践

同一对话上下文的所有请求使用**相同的** `prompt_cache_key`。

不同对话使用**不同的** `prompt_cache_key`，避免缓存污染。

值建议使用业务侧的 conversation\_id 或等价的全局唯一标识。

## 二、使用 X-Session-ID

### 2.1 什么是 X-Session-ID

`X-Session-ID` 是通过 HTTP Header 传递的会话标识，用于将同一用户的连续请求路由到同一个推理实例，从而提高该实例上的 KV Cache 局部命中率。

### 2.2 使用方式

在请求 Header 中添加：

```bash
X-Session-ID: session-abc123
```

完整请求示例：

```bash
curl -X POST 'https://tokenhub.tencentmaas.com/v1/chat/completions' \\
  -H 'Content-Type: application/json' \\
  -H 'Authorization: Bearer your-api-key' \\
  -H 'X-Session-ID: session-abc123' \\
  -d '{
    "model": "your-model",
    "messages": [...]
  }'
```

### 2.3 最佳实践

同一用户的多轮对话，保持 `X-Session-ID` 不变。

不同用户或不同对话上下文，使用不同的 Session ID。

配合 `prompt_cache_key` 一起使用效果更佳。

## 三、缓存 TTL 机制

### 3.1 什么是缓存 TTL

TTL（Time To Live）是缓存的存活时间。超过 TTL 后，缓存的 KV 数据将被淘汰，后续请求需要重新计算。

### 3.2 TTL 对命中率的影响

在 TTL 有效期内，相同前缀的请求可直接复用已缓存的 KV 数据，TTL 过期后，即使前缀相同也需要重新计算，导致 TTFT 回升。**用户可以通过优化请求设计，避免缓存被意外提前失效**，从而在 TTL 有效期内获得最大命中收益。核心关注点：**保持请求前缀稳定，不要让前缀中的内容频繁变化。**

### 3.3 注意事项

#### **避免 System Prompt 中写入时间相关内容**

**注意：**

不要在 System Prompt 中写入当天日期、当前时间等动态内容。

**原因**：时间变化会导致 System Prompt 内容变更 → 前缀不匹配 → 缓存完全失效。例如，过了 0 点日期变更，瞬间所有缓存失效，TTFT 暴涨，用户体验为"特别卡"。

**正确做法：**

```json
// ❌ 错误：system prompt 包含动态时间
{
  "messages": [
    {"role": "system", "content": "今天是2026年5月9日，你是一个助手..."}
  ]
}

// ✅ 正确：system prompt 保持稳定
{
  "messages": [
    {"role": "system", "content": "你是一个助手..."},
    {"role": "user", "content": "今天是2026年5月9日，请帮我..."}
  ]
}
```

将动态内容放在 messages 末尾（用户消息中），而非 system prompt 中，这样不影响前缀缓存。

## 四、Request 结构设计原则

合理的请求结构设计是提升缓存命中率的基础。

### 4.1 核心原则

**Key 不变**：messages 中各消息的 role 保持稳定。

**Key 的个数不变**：消息数量结构保持一致。

**Key 的顺序不变**：消息排列顺序保持一致。

### 4.2 Message 结构变化原则

**末尾追加 Key**：新的对话轮次只在 messages 数组末尾追加，不要在中间插入或修改已有消息。

```json
// 第 1 轮
{
  "messages": [
    {"role": "system", "content": "你是助手"},
    {"role": "user", "content": "问题1"}
  ]
}

// 第 2 轮（末尾追加，前缀不变）
{
  "messages": [
    {"role": "system", "content": "你是助手"},
    {"role": "user", "content": "问题1"},
    {"role": "assistant", "content": "回答1"},
    {"role": "user", "content": "问题2"}
  ]
}
```

这样前两条消息的 KV Cache 可以被完全复用。

## 五、新版本发版建议

在产品发版更新时，如果涉及 System Prompt 变更，可能导致缓存大面积失效。建议：

1. **发版前预热缓存**：少量模拟会话数据访问 API，提前构建 KV Cache。

2. **避免突增流量冲击**：灰度发布，防止发版 + 突增流量同时命中导致 Cache Rate 骤降。

3. **监控 Cache Rate**：发版后密切关注缓存命中率指标，如异常下降及时排查。

## 六、总结

| 优化手段 | 作用 | 使用方式 |
| --- | --- | --- |
| `prompt_cache_key` | 标识相同上下文，提升缓存复用 | 请求体字段，值为 conversation\_id |
| `X-Session-ID` | 路由到同一实例，提升局部命中 | HTTP Header |
| 稳定 System Prompt | 避免缓存因前缀变化而失效 | 不写入动态时间内容 |
| 末尾追加消息 | 保持前缀一致性 | messages 只在末尾追加 |
| 发版前预热 | 防止冷启动冲击 | 提前模拟请求构建 KV |
