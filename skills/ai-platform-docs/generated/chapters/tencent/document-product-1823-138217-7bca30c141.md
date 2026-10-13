<!-- Official source: https://cloud.tencent.com/document/product/1823/138217 -->
<!-- Source SHA-256: 9c5449c9edb973374faaeda6a36945db029b576d6409b3aac6e59a1cbc33ba31 -->

# TokenHub CLI 使用指南

官方来源：https://cloud.tencent.com/document/product/1823/138217
最近更新时间：2026-09-16 15:32:46

## 概述

TokenHub CLI（命令行工具，命令名 `thcli` / `th`）是大模型服务平台 TokenHub **面向终端开发者**与 **AI Agent** 提供的命令行接入方式。

CLI 命令入口统一为 `thcli <命令> [子命令] [--参数]`，任意层级均可加 `-h` 或 `--help` 查看完整参数说明。

**说明：**

您可以在终端中直接完成登录鉴权、模型查询、推理调用、套餐额度查看、用量统计等操作，无需切换到控制台页面；

也可一键将 TokenHub 能力注入主流 AI Agent，让 Agent 通过自然语言理解并调用 TokenHub 的能力。

安装完成后提供两个等价命令：`thcli` 与短别名 `th`。下文示例统一使用 `thcli`；将其替换为 `th` 效果完全一致，例如 `th models list` = `thcli models list`。

## 准备工作

在使用 TokenHub CLI 之前，您需要：

[注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。

登录 [腾讯云大模型服务平台 TokenHub 控制台](https://console.cloud.tencent.com/tokenhub/)，按照界面提示开通大模型服务平台 TokenHub 。

本机已安装 **Node.js ≥ 18**（用于运行 CLI）。

## 安装与登录

手动安装

AI Agent安装

1. 在终端输入安装指令。

```bash
npm i -g tencent-tokenhub-cli

# （可选）一键将 TokenHub 能力作为 Skill 注入本地 Agent，使 Agent 可通过自然语言调用 TokenHub 的只读能力
thcli +connect
```

2. 登录鉴权。

**方式一**：OAuth 快捷登录（推荐）——登录腾讯云账号后，自动生成并在本地保存一个数据面 API Key（名为 `thcli-key`），用于后续推理调用，无需手动配置。

```bash
thcli auth login
```

**方式二：**无浏览器环境（远程开发机、CI、容器）使用 `--browser no`，按提示将网页上的凭据串粘贴回终端。

```bash
thcli auth login --browser no
```

**方式三**：手动填入密钥——已有腾讯云永久密钥（SecretId/SecretKey）时可直接填入。

```bash
thcli auth set --secret-id <SecretId> --secret-key <SecretKey>
```

3. 验证登录状态。

```bash
thcli auth status 
```

复制以下 Prompt 发给 Agent，自动完成安装与登录：

```plaintext
根据下面命令帮我安装 THCLI：https://gz-thcli-skills-1258344699.cos.ap-guangzhou.myqcloud.com/tokenhub-cli-skills/install.md
```

**说明：**

为避免 AI Agent 在自动执行任务时因理解偏差而误触发删除、创建、变更等操作，对生产环境造成不可预期的影响，当前版本**注入 Agent 的 Skill 仅封装只读命令**：

**支持**：查用量、选模型、看套餐余量、查服务状态。

**不支持**：直接通过自然语言触发创建、修改、删除、购买等写操作。

## 核心能力

### 1. 认证与身份

<table><colgroup><col/><col/><col/><col/></colgroup><tbody><tr><td><div>能力</div></td><td><div>能力说明</div></td><td><div>核心命令</div></td><td><div>Agent 自然语言描述（示例）</div></td></tr><tr><td colspan="1" rowspan="3"><div>登录与凭证</div></td><td><div>登录腾讯云账号（OAuth，登录后自动生成并保存一个名为 <code>thcli-key</code> 的数据面 API Key，用于推理调用）或手动填入密钥。</div></td><td><div>thcli auth login / set</div></td><td colspan="1" rowspan="3"><div>“查一下我现在登录的账号、站点和凭证有效期”</div></td></tr><tr><td colspan="0" rowspan="0"><div></div></td><td><div>查看当前凭证来源、有效期。</div></td><td><div>thcli auth status</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td colspan="0" rowspan="0"><div></div></td><td><div>登出。</div></td><td><div>thcli auth logout</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td colspan="1" rowspan="3"><div>API Key 管理</div></td><td><div>查看 Key 列表、详情、明文。</div></td><td><div>thcli key list / get / reveal</div></td><td colspan="1" rowspan="3"><div>“列出我名下所有的 API Key，包括名称和访问范围”。</div><div>“查一下这把 Key 的额度用得怎么样了”</div></td></tr><tr><td colspan="0" rowspan="0"><div></div></td><td><div>创建 Key（可限定可访问的模型、服务与 Token 额度）；修改备注与 IP 白名单。</div></td><td><div>thcli key create / update / quota</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td colspan="0" rowspan="0"><div></div></td><td><div>启用、停用、删除；调整额度限制。</div></td><td><div>thcli key enable / disable / delete</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td colspan="1" rowspan="2"><div>多账号、多站点</div></td><td><div>查看 / 创建 / 切换默认 Profile（同站多账号身份隔离）。</div></td><td><div>thcli profile list / current / use / create</div></td><td colspan="1" rowspan="2"><div>“看看我当前用的是哪个 Profile、哪个站点”</div></td></tr><tr><td colspan="0" rowspan="0"><div></div></td><td><div>查看 / 切换默认站点（cn 国内站 / intl 国际站）。</div></td><td><div>thcli site list / current / use</div></td><td colspan="0" rowspan="0"><div></div></td></tr></tbody></table>

### 2. 模型发现

| 能力 | 能力说明 | 核心命令 | Agent 自然语言描述（示例） |
| --- | --- | --- | --- |
| 模型列表与详情 | 查看平台全量模型（含语言、视觉、多模态、语音、向量等各类型）；  可按类型、厂商、标签筛选；  查看单个模型的上下文窗口、最大输出、限流值等规格与计费信息。 | thcli models list  thcli models search  thcli models get | “有哪些模型，能力和厂商分别是什么”  “deepseek-v3 的上下文窗口和输出上限是多少” |
| 比价 | 横向比较多个模型的输入、输出、缓存单价。 | thcli models compare  thcli models pricing | “帮我对比一下 deepseek-v3 和 glm-5v-turbo 的价格” |

### 3. 模型调用

| 能力 | 能力说明 | 核心命令 | Agent 自然语言描述（示例） |
| --- | --- | --- | --- |
| 对话 | 对语言模型发起推理调用，支持多轮对话、图片/文档多模态输入、联网搜索、深度思考、流式输出。 | thcli +chat --model <模型 Id> "你好"  **说明：**  +chat 按 token 计费，优先使用模型的免费额度，免费额度耗尽时，需通过`endpoint postpaid on`开通按量付费才可继续调用。 | “用 deepseek-v4-flash 这个模型帮我看看这张截图里的报错并解释”  “证明一下勾股定理，帮我一步步推导” |

**注意：**

文生图、图生图、文生视频、图生视频、文生语音等模型能力，当前版本 CLI 暂不支持，请前往控制台 [模型体验](https://console.cloud.tencent.com/tokenhub/creation?regionId=1) 或 [模型广场](https://console.cloud.tencent.com/tokenhub/inference?regionId=1) 进行体验或调用，后续版本将陆续上线。

### 4. 推理服务与部署

| 能力 | 能力说明 | 核心命令 | Agent 自然语言描述（示例） |
| --- | --- | --- | --- |
| 服务查询 | 查看服务（endpoint）列表与详情，包括运行状态、计费方式、限流阈值、免费额度用量。 | thcli endpoint list  thcli endpoint get | “我有哪些服务，分别是什么状态”  “这个服务当前的限流是多少” |
| 部署 / 改配 / 删除 | 自定义服务创建（设置计费方式、RPM / TPM 限流）。  修改配置；删除。  开启/关闭服务的按量付费。 | thcli deploy  thcli endpoint update / delete  thcli endpoint postpaid on / off  **说明：**  endpoint postpaid on、deploy 会产生费用、默认二次确认。 | 无  **注意：**  部署、修改、删除接入点属于写操作，当前不支持通过自然语言直接触发。 |

### 5. 套餐与额度

| 能力 | 能力说明 | 核心命令 | Agent 自然语言描述（示例） |
| --- | --- | --- | --- |
| 套餐查询 | 查看已持有的 Token Plan 套餐详情、可用模型范围、用量明细。  **说明：**  当前仅支持查看企业版 Token Plan 套餐信息，个人版 Token Plan 暂不支持，后续版本即将上线。 | thcli plan list  thcli plan info / models / detail | “我有哪些企业版套餐，分别还剩多少额度”  “这个套餐下能用哪些模型”  “我要看这个套餐用量明细” |
| 购买 / 续费 / 升配 | 购买企业版套餐（专业版/轻享版）、续费、升配规格额度。 | thcli plan buy  thcli plan renew / upgrade  **说明：**  plan buy/renew/upgrade 会产生费用、默认二次确认。 | 无  **注意：**  购买、续费、升配属于产生费用的写操作，当前不支持通过自然语言直接触发。 |
| 套餐专属 Key | 查看、创建、修改、重置、删除企业套餐的专属 API Key（与平台 Key 相互独立，额度单独计算）。 | thcli plan key list / get  thcli plan key create / update / rotate / delete | “这个套餐下有哪些专属 Key” |

### 6. 观测与诊断

| 能力 | 能力说明 | 核心命令 | Agent 自然语言描述（示例） |
| --- | --- | --- | --- |
| 用量统计 | 按模型、接入点、API Key 维度查看 Token 消耗排行与趋势，支持按小时、天等粒度聚合；导出用量明细为 CSV 用于对账。 | thcli usage rank / trend / export | “今天用了多少 Token，哪个模型消耗最多”  “看一下 xx 服务近 7 日的 tpm 趋势”  “导出最近 7 天按 Key 的用量到 CSV” |
| 模型监控 | 按语言、视觉、语音模型类型查看监控数据。  支持按模型、接入点、API Key 维度查看 RPM、TTFT、TPOT、错误率等指标，支持按小时、天等粒度聚合。 | thcli monitor text / vision / audio  thcli monitor text --model <name> | “查一下 hy3 模型近七日有无调用失败记录” |
| 诊断与排障 | 全链路体检（凭证、地域、权限）  Key、服务、模型、套餐诊断，查看状态及是否可用。  错误码翻译。 | thcli doctor all  thcli doctor key / endpoint / model / plan  thcli doctor error | “为什么调用失败，检查一下什么环节出了问题”  “这个错误码什么意思” |

### 7. Agent 集成与接入

| 能力 | 能力说明 | 核心命令 | Agent 自然语言描述（示例） |
| --- | --- | --- | --- |
| Skill 一键注入 | 将 TokenHub 的只读能力作为 Skill 注入本地 Agent，使 Agent 可用自然语言理解并调用 TokenHub。 | thcli +connect  thcli +connect uninstall  thcli +connect status | “请阅读 <安装文档链接> ，帮我把 TokenHub CLI 接入我的 Claude Code”  “看看我本机已经装了哪些 TokenHub 相关的 Skill” |

### 8. Skill 专属能力

| 能力 | 能力说明 | Agent 自然语言描述（示例） |
| --- | --- | --- |
| 文档检索 | 基于 TokenHub 官方文档内容，快速理解并帮助用户检索所需信息。 | “hy3 的调用参数和步骤有哪些？”  “我的费用账单要去哪里看？给个链接”  “给我解释一下什么是推理服务”  “根据官方文档要求，帮我把 hy3 模型接入 WorkBuddy” |

## 查看命令的完整参数

每个命令或子命令实际支持的完整参数请通过 `-h` 或 `--help` 查看，任意层级均适用，例如 `thcli --help`、`thcli plan --help`、`thcli plan key create --help`。

下表列出各核心命令组对应的完整参数查看方式：

| 命令组 | 说明 | 查看完整参数 |
| --- | --- | --- |
| auth | 登录、登出、手填密钥、查看状态 | thcli auth --help |
| key | API 密钥列表、详情、增删改、启停、明文 | thcli key --help |
| models | 模型列表、详情、比价、搜索推荐 | thcli models --help |
| endpoint / deploy | 接入点列表、详情、改配、删除；创建接入点 | thcli endpoint --help  thcli deploy --help |
| +chat | 推理调用 | thcli +chat --help |
| chat-config | 本地维护 `+chat` 对话时用的 API Key | thcli chat-config --help |
| plan | 企业套餐列表、详情、购买、续费、升配、用量明细 | thcli plan --help |
| plan key | 企业套餐专属 Key 增删改查 | thcli plan key --help |
| usage | 用量排行、导出 CSV | thcli usage --help |
| monitor | RPM、TTFT、TPOT、错误率等 | thcli monitor --help |
| doctor | 全链路体检、输出修复动作 | thcli doctor --help |
| profile | 多账号 Profile 管理 | thcli profile --help |
| site | 站点（cn / intl）切换 | thcli site --help |
| lang | 界面语言（zh / en）切换 | thcli lang --help |
| +connect | Agent Skills 一键注入 | thcli +connect --help |

## **参考信息**

关于站点与地域的资源隔离规则、本地文件结构（`~/.thcli/`）、调用日志等进阶说明，请参见 [开源仓库](https://github.com/TencentCloud/THCLI)。
