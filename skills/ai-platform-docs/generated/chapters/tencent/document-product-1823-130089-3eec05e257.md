<!-- Official source: https://cloud.tencent.com/document/product/1823/130089 -->
<!-- Source SHA-256: 7d26268df73fc28a2476ff7bf5a49745e9127f044bb5208b6fb985cc9a625746 -->

# 模型监控

官方来源：https://cloud.tencent.com/document/product/1823/130089
最近更新时间：2026-08-13 20:42:00

## 功能概述

[模型监控](https://console.cloud.tencent.com/tokenhub/monitor/metrics) 提供实时的模型推理性能监控仪表板，帮助您追踪各模型的请求并发、Token 吞吐、响应延迟等核心指标，及时发现性能瓶颈。

## 筛选介绍

提供以下模型分类筛选：

<table><colgroup><col/><col/></colgroup><tbody><tr><td><div>分类</div></td><td><div>监控内容</div></td></tr><tr><td><div>语言模型、多模态理解、向量模型</div></td><td><div>RPM（Requests Per Minute）、TTFT（Time To First Token）、TPOT（Time Per Output Token）、错误率、调用次数等性能指标。</div></td></tr><tr><td colspan="1" rowspan="4"><div>视觉模型</div></td><td><div>图像生成相关模型的请求数、Token 消耗数、图片张数、成功率、任务时长等指标。</div></td></tr><tr><td colspan="0" rowspan="0"><div></div></td><td><div>Kling、Vidu、PixVerse、MiniMax 系列模型的请求数、Token 消耗数、视频秒数、成功率、任务时长等指标。</div></td></tr><tr><td colspan="0" rowspan="0"><div></div></td><td><div>HY、YT 系列模型的调用量、并发量等指标。</div></td></tr><tr><td colspan="0" rowspan="0"><div></div></td><td><div>3D 生成模型的调用量、并发量等指标。</div></td></tr><tr><td><div>语音模型</div></td><td><div>语音模型的请求数、Token 消耗数、音乐数量、字符数、秒数、成功率、任务时长等指标。</div></td></tr></tbody></table>

支持按照以下维度进行筛选：

| 筛选项 | 说明 |
| --- | --- |
| 筛选维度 | 支持按服务/按模型筛选，切换不同的聚合视角。 |
| 服务选择 | 下拉选择特定推理服务（默认显示**全部服务**）。 |
| 时间范围 | 1小时/今天/近3天/近7天/近30天，或自定义时间区间。 |

## 监控指标说明

### 语言模型核心指标

以时序折线图的形式展示以下核心性能指标：

<table><colgroup><col/><col/><col/><col/></colgroup><tbody><tr><td><div>指标</div></td><td><div>全称</div></td><td><div>单位</div></td><td><div>说明</div></td></tr><tr><td><div>首 Token 延迟（TTFT）</div></td><td><div>Time To First Token</div></td><td><div>ms</div></td><td><div>从请求发送到收到第一个 Token 的响应时间（单位时间内流式请求的 TTFT 均值，不包含非流式请求）。</div></td></tr><tr><td><div>每 Token 输出时延（TPOT）</div></td><td><div>Time Per Output Token</div></td><td><div>ms</div></td><td><div>生成每个输出 Token 的平均耗时。</div></td></tr><tr><td colspan="1" rowspan="1"><div>缓存命中率</div></td><td colspan="1" rowspan="1"><div>Cache Hit Ratio</div></td><td colspan="1" rowspan="1"><div>%</div></td><td colspan="1" rowspan="1"><div>请求缓存命中 token 数 / 输入总 token 数。</div></td></tr><tr><td colspan="1" rowspan="1"><div>超时错误率</div></td><td colspan="1" rowspan="1"><div>Request Canceled Ratio</div></td><td colspan="1" rowspan="1"><div>%</div></td><td colspan="1" rowspan="1"><div>因客户端超时等原因触发的取消请求 / 总调用次数。</div></td></tr><tr><td><div>RPM 限流率</div></td><td><div>RPM Rate Limited Ratio</div></td><td><div>%</div></td><td><div>限流次数 / 总调用次数。</div></td></tr><tr><td><div>非流式接口延时</div></td><td><div>Non-Stream Latency</div></td><td><div>ms</div></td><td><div>单位时间内针对非流式请求的 latency，端到端耗时。</div></td></tr><tr><td><div>错误率</div></td><td><div>Request Error Ratio</div></td><td><div>%</div></td><td><div>HTTP 状态码非200请求数 / 总请求数。</div></td></tr><tr><td><div>客户端错误率</div></td><td><div>Client Error Ratio</div></td><td><div>%</div></td><td><div>4xx 请求数 / 总请求数。</div></td></tr><tr><td><div>服务端错误率</div></td><td><div>Server Error Ratio</div></td><td><div>%</div></td><td><div>5xx 请求数 / 总请求数。</div></td></tr><tr><td><div>429限流错误率</div></td><td><div>Rate Limited Ratio</div></td><td><div>%</div></td><td><div>429 请求数 / 总请求数。</div></td></tr><tr><td colspan="1" rowspan="1"><div>每分钟请求数（RPM）</div></td><td colspan="1" rowspan="1"><div>Requests Per Minute</div></td><td colspan="1" rowspan="1"><div>reqs/min</div></td><td colspan="1" rowspan="1"><div>每分钟的请求并发数（调用次数），反映当前的请求吞吐量。</div></td></tr><tr><td><div>调用失败次数</div></td><td><div>Failure Count</div></td><td><div>reqs/min</div></td><td><div>每分钟请求调用失败的次数。</div></td></tr><tr><td><div>调用成功次数</div></td><td><div>Success Count</div></td><td><div>reqs/min</div></td><td><div>每分钟请求调用成功的次数</div></td></tr></tbody></table>

### 图片生成核心指标

以时序折线图的形式展示以下核心性能指标：

<table><colgroup><col/><col/></colgroup><tbody><tr><td colspan="1" rowspan="1"><div>指标</div></td><td colspan="1" rowspan="1"><div>说明</div></td></tr><tr><td colspan="1" rowspan="1"><div>每分钟请求数</div></td><td colspan="1" rowspan="1"><div>每分钟的任务请求数。</div></td></tr><tr><td colspan="1" rowspan="1"><div>图片张数</div></td><td colspan="1" rowspan="1"><div>单位时间内所有生成图片的数量总和。</div></td></tr><tr><td colspan="1" rowspan="1"><div>Token 消耗数</div></td><td colspan="1" rowspan="1"><div>单位时间内所有任务请求的 Token 消耗数。</div></td></tr><tr><td colspan="1" rowspan="1"><div>错误率</div></td><td colspan="1" rowspan="1"><div>单位时间内任务请求的失败率。</div></td></tr><tr><td colspan="1" rowspan="1"><div>任务时长</div></td><td colspan="1" rowspan="1"><div>单位时间内任务请求的端到端平均耗时。</div></td></tr></tbody></table>

### 视频生成核心指标

**Kling、Vidu、PixVerse、MiniMax 系列视频生成模型** 以时序折线图的形式展示以下核心性能指标：

| 指标 | 说明 |
| --- | --- |
| 每分钟请求数 | 每分钟的任务请求数。 |
| 视频秒数 | 单位时间内所有生成视频的时长总和。 |
| Token 消耗数 | 单位时间内所有任务请求的 Token 消耗数。 |
| 错误率 | 单位时间内任务请求的失败率。 |
| 任务时长 | 单位时间内任务请求的端到端平均耗时。 |

**HY、YT 系列视频生成模型** 以时序折线图的形式展示以下核心性能指标：

| 指标 | 说明 |
| --- | --- |
| 调用次数 | 每个时间点的调用请求数。 |
| 消耗积分数 | 每个时间点的积分消耗数。 |

### 3D 生成核心指标

以时序折线图的形式展示以下核心性能指标：

<table><colgroup><col/><col/></colgroup><tbody><tr><td colspan="1" rowspan="1"><div>指标</div></td><td colspan="1" rowspan="1"><div>说明</div></td></tr><tr><td colspan="1" rowspan="1"><div>调用次数</div></td><td colspan="1" rowspan="1"><div>每个时间点的调用请求数。</div></td></tr><tr><td colspan="1" rowspan="1"><div>消耗积分数</div></td><td colspan="1" rowspan="1"><div>每个时间点的积分消耗数。</div></td></tr></tbody></table>

### 语音模型核心指标

以时序折线图的形式展示以下核心性能指标：

<table><colgroup><col/><col/></colgroup><tbody><tr><td><div>指标</div></td><td><div>说明</div></td></tr><tr><td colspan="1" rowspan="1"><div>每分钟请求数</div></td><td colspan="1" rowspan="1"><div>每分钟的任务请求数。</div></td></tr><tr><td colspan="1" rowspan="1"><div>音乐数量</div></td><td colspan="1" rowspan="1"><div>单位时间内生成音乐的数量。</div></td></tr><tr><td><div>字符数</div></td><td colspan="1" rowspan="1"><div>单位时间内进行合成的字符数。</div></td></tr><tr><td><div>秒数</div></td><td colspan="1" rowspan="1"><div>单位时间内进行配音的视频时长。</div></td></tr><tr><td colspan="1" rowspan="1"><div>Token 消耗数</div></td><td colspan="1" rowspan="1"><div>单位时间内所有任务请求的 Token 消耗数。</div></td></tr><tr><td colspan="1" rowspan="1"><div>错误率</div></td><td colspan="1" rowspan="1"><div>单位时间内任务请求的失败率。</div></td></tr><tr><td colspan="1" rowspan="1"><div>任务时长</div></td><td colspan="1" rowspan="1"><div>单位时间内任务请求的端到端平均耗时。</div></td></tr></tbody></table>
