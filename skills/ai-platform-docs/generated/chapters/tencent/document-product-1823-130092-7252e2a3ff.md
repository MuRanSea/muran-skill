<!-- Official source: https://cloud.tencent.com/document/product/1823/130092 -->
<!-- Source SHA-256: 427978610b3618217f883872570fc49ae9368a826febf8832210588b299d6de0 -->

# Coding Plan 概述

官方来源：https://cloud.tencent.com/document/product/1823/130092
最近更新时间：2026-09-10 12:23:58

腾讯云 Coding Plan，是为 AI Coding 场景推出的专属订阅套餐。支持使用 OpenClaw、CodeBuddy、Claude Code、Cline、Cursor 等主流编程工具。

## 适用场景

**个人开发场景**：助力开发者完成个人项目、学习实践、工具搭建等编码任务。

**说明**：

企业级开发需求，请通过 [文本生成服务](https://cloud.tencent.com/document/product/1823/130079) 调用模型服务。

## 套餐介绍

访问 [Coding Plan 购买页](https://console.cloud.tencent.com/tokenhub/codingplan)，根据实际需求选择并购买套餐。

### 套餐详情

<table><colgroup><col/><col/><col/></colgroup><tbody><tr><td><div><b>套餐内容</b></div></td><td><div><b>Lite 套餐</b></div></td><td><div><b>Pro 套餐</b></div></td></tr><tr><td><div><b>原价</b></div></td><td><div><b>40元/月</b></div></td><td><div><b>200元/月	</b></div></td></tr><tr><td><div><b>用量限制</b></div></td><td colspan="1" rowspan="1"><div>每 5 小时：最多约 <b>1,200 </b>次请求</div><div>每周：最多约 <b>9,000</b> 次请求</div><div>每订阅月：最多约 <b>18,000</b> 次请求</div></td><td colspan="1" rowspan="1"><div>每 5 小时：最多约 <b>6,000</b> 次请求</div><div>每周：最多约 <b>45,000 </b>次请求</div><div>每订阅月：最多约 <b>90,000</b> 次请求</div></td></tr></tbody></table>

**额度消耗**：

请求次数为模型调用的预估数值。通常一次用户提问会触发多次模型调用，且每次调用均会消耗 1 次用量额度，因此实际消耗的请求次数一般多于用户提问次数。

简单任务单次提问约消耗 5~15 次模型调用，复杂任务单次提问约消耗15~30次或更多模型调用。用量信息可在 [Coding Plan 页面](https://console.cloud.tencent.com/tokenhub/codingplan) 查看。

### 订阅前须知

1. **订阅账号规范：**为订阅人专享使用，**严禁账号共享**。若存在账号共享行为，可能**导致订阅权益受限**，腾讯不承担赔偿责任，敬请知悉。

2. **严禁 API 调用**：仅限在编程工具（例如：Claude Code、CodeBuddy Code、OpenClaw 等）中使用，禁止以 API 调用的形式用于自动化脚本、自定义应用程序后端或任何非交互式批量调用场景。将套餐 API Key 用于允许范围之外的调用将被视为违规或滥用，可能会导致订阅被暂停或 API Key 被封禁。对于违规而导致服务受损，腾讯不承担赔偿责任。

## 使用说明

### 获取专属 API Key 和 Base URL

如果您已经购买了套餐，您需要获取并在 AI 工具中配置套餐专属的 API Key 和 Base URL，才能正确使用并抵扣套餐额度。

**API Key：**在 [Coding Plan 页面](https://console.cloud.tencent.com/tokenhub/codingplan)，获取 Coding Plan **专属 API Key**（格式为 `sk-sp-xxxx`）。

**Base URL：**后续需在 AI 工具中配置以下其中一个 Base URL（因工具而异），具体操作请参见对应的 AI 工具文档。

OpenAI 兼容协议：`https://api.lkeap.cloud.tencent.com/coding/v3`。

Anthropic 兼容协议：`https://api.lkeap.cloud.tencent.com/coding/anthropic`。

**说明：**

Coding Plan 专属的 API Key 和 Base URL 与腾讯云预付费及后付费的 API Key（`sk-xxxx`）和 Base URL（`https://api.lkeap.cloud.tencent.com/xxxxx/`）不互通，请勿混用。

![](https://qcloudimg.tencent-cloud.cn/image/document/e043e66b8ea414bab6a8a1fbeaa5e850.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/e043e66b8ea414bab6a8a1fbeaa5e850.png)

### 套餐支持的模型

**注意：**

为持续优化模型服务能力与使用体验，平台套餐内提供的 AI 模型为动态更新的模型库，可能根据模型性能、服务稳定性、合规要求、授权状况及第三方模型供应情况等进行新增、替换、版本升级、可用范围调整或逐步下线。套餐所提供的是“可使用平台当期模型库中相应模型”的服务，而非对任一特定模型的持续、固定或永久提供作出承诺。用户在订阅时所见的模型仅代表当时的可用情况，实际可用模型、版本及调用范围以购买页、控制台展示及平台公告为准。对可能影响已订阅用户使用的模型下线或重大调整，平台将通过公告、站内信或控制台提示等合理方式提前告知。

通过配置 Model Name，切换模型。

选择 Auto 模型会通过算法自动匹配模型，请通过 model 参数值配置。

**说明：**

Coding Plan 可用模型暂不支持多模态能力。

| **模型** | **model 参数值** | **备注** |
| --- | --- | --- |
| Auto | tc-code-latest | - |
| GLM-5 | glm-5  glm-5-0 | 将于2026年10月9日下线 |

### 支持的 AI 工具

Coding Plan 支持主流的 AI 工具，可按需选择。

<table><colgroup><col/><col/><col/></colgroup><tbody><tr><td colspan="3" rowspan="1"><div><b>AI 工具</b></div></td><td colspan="0" rowspan="0"><div></div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div><a href="https://cloud.tencent.com/document/product/1823/130094">OpenClaw</a></div><div></div><div>开源、自托管个人 AI 助手</div></td><td><div><a href="https://cloud.tencent.com/document/product/1823/130095">CodeBuddy Code</a></div><div></div><div>腾讯云 AI 技术的智能编程工具</div></td><td><div><a href="https://cloud.tencent.com/document/product/1823/130097">Claude Code</a></div><div></div><div>AI 终端编程助手，支持自然语言编程</div></td></tr><tr><td><div> <a href="https://cloud.tencent.com/document/product/1823/130096">OpenCode</a></div><div></div><div>开源 AI 编程代码工具</div></td><td><div><a href="https://cloud.tencent.com/document/product/1823/130099">Cline</a></div><div></div><div>VSCode 扩展，代码补全和调试</div></td><td><div><a href="https://cloud.tencent.com/document/product/1823/130100">Cursor</a></div><div></div><div>AI 原生代码编辑器</div></td></tr><tr><td><div><a href="https://cloud.tencent.com/document/product/1823/130098">Codex</a></div><div></div><div>OpenAI 推出的命令行编程工具</div></td><td><div><a href="https://cloud.tencent.com/document/product/1823/130101">Kilo CLI</a></div><div></div><div>轻量高性能命令行编程工具</div></td><td><div><a href="https://cloud.tencent.com/document/product/1823/130102">Kilo Code</a></div><div></div><div>高效编程助手</div></td></tr></tbody></table>
