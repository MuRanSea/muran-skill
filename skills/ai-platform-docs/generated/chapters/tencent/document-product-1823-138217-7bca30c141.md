<!-- Official source: https://cloud.tencent.com/document/product/1823/138217 -->
<!-- Source SHA-256: c0ad59b56d8fe780b87e21f752d8345d7db78e6861300e4eeffc4827bbfca07b -->

# TokenHub CLI 使用指南

官方来源：https://cloud.tencent.com/document/product/1823/138217
最近更新时间：2026-11-06 16:30:30

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

**方式三**：手动填入密钥——已有 [腾讯云永久密钥](https://console.cloud.tencent.com/cam/capi)（SecretId/SecretKey）时可直接填入。

```bash
thcli auth set --secret-id <SecretId> --secret-key <SecretKey>
```

3. 验证登录状态。

```bash
thcli auth status
```

复制以下 Prompt 发给 Agent，自动完成安装与登录：

```plaintext
请阅读以下文档，帮我安装 TokenHub CLI：https://tokenhub-cli.tencentmaas.com/tokenhub-cli-skills/install.md
```

**说明：**

为避免 AI Agent 在自动执行任务时因理解偏差而误触发删除、创建、变更等操作，对生产环境造成不可预期的影响，当前版本**注入 Agent 的 Skill 仅封装只读命令**：

**支持**：查用量、选模型、看套餐余量、查服务状态。

**不支持**：直接通过自然语言触发创建、修改、删除、购买等写操作。

## 核心能力

### 1. 认证与身份

<table><colgroup><col/><col/><col/><col/></colgroup><tbody><tr><td><div>能力</div></td><td><div>能力说明</div></td><td><div>核心命令</div></td><td><div>Agent 自然语言描述（示例）</div></td></tr><tr><td colspan="1" rowspan="3"><div>登录与凭证</div></td><td><div>登录腾讯云账号（OAuth，登录后自动生成并保存一个名为 <code>thcli-key</code> 的数据面 API Key，用于推理调用）或手动填入密钥。</div></td><td><div>thcli auth login / set</div></td><td colspan="1" rowspan="3"><div>“查一下我现在登录的账号、站点和凭证有效期”</div></td></tr><tr><td colspan="0" rowspan="0"><div></div></td><td><div>查看当前凭证来源、有效期。</div></td><td><div>thcli auth status</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td colspan="0" rowspan="0"><div></div></td><td><div>登出。</div></td><td><div>thcli auth logout</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td colspan="1" rowspan="3"><div>API Key 管理</div></td><td><div>查看 Key 列表、详情、明文。</div></td><td><div>thcli key list / get / reveal</div></td><td colspan="1" rowspan="3"><div>“列出我名下所有的 API Key，包括名称和访问范围”。</div><div>“查一下这把 Key 的额度用得怎么样了”</div></td></tr><tr><td colspan="0" rowspan="0"><div></div></td><td><div>创建 Key（可限定可访问的模型、服务与 Token 额度）；修改备注与 IP 白名单。</div></td><td><div>thcli key create / update / quota</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td colspan="0" rowspan="0"><div></div></td><td><div>启用、停用、删除；调整额度限制。</div></td><td><div>thcli key enable / disable / delete</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td colspan="1" rowspan="2"><div>多账号、多站点</div></td><td><div>查看 / 创建 / 切换默认 Profile（同站多账号身份隔离）。</div></td><td><div>thcli profile list / current / use / create</div></td><td colspan="1" rowspan="2"><div>“看看我当前用的是哪个 Profile、哪个站点”</div></td></tr><tr><td colspan="0" rowspan="0"><div></div></td><td><div>查看 / 切换默认站点（cn 中国站 / intl 国际站）。</div></td><td><div>thcli site list / current / use</div></td><td colspan="0" rowspan="0"><div></div></td></tr></tbody></table>

### 2. 模型发现

| 能力 | 能力说明 | 核心命令 | Agent 自然语言描述（示例） |
| --- | --- | --- | --- |
| 模型列表与详情 | 查看平台全量模型（含语言、视觉、多模态、语音、向量等各类型）；  可按类型、厂商、标签筛选；  查看单个模型的上下文窗口、最大输出、限流值等规格与计费信息。 | thcli models list  thcli models search  thcli models get | “有哪些模型，能力和厂商分别是什么”  “deepseek-v3 的上下文窗口和输出上限是多少” |
| 比价 | 横向比较多个模型的输入、输出、缓存单价。 | thcli models compare  thcli models pricing | “帮我对比一下 deepseek-v3 和 glm-5v-turbo 的价格” |

### 3. 模型调用

#### 语言模型相关

<table><colgroup><col/><col/><col/><col/></colgroup><tbody><tr><td colspan="1" rowspan="1"><div>能力</div></td><td colspan="1" rowspan="1"><div>能力说明</div></td><td colspan="1" rowspan="1"><div>核心命令</div></td><td colspan="1" rowspan="1"><div>Agent 自然语言描述（示例）</div></td></tr><tr><td colspan="1" rowspan="1"><div>对话</div></td><td colspan="1" rowspan="1"><div>对语言模型发起推理调用，支持多轮对话、图片/文档多模态输入、联网搜索、深度思考、流式输出。</div></td><td colspan="1" rowspan="1"><div>thcli +chat --model &lt;模型 Id&gt;  "你好"</div><div><div><b>说明：</b></div><div>+chat 按 token 计费，优先使用模型的免费额度，免费额度耗尽时，需通过<code>endpoint postpaid on</code>开通按量付费才可继续调用。</div></div></td><td colspan="1" rowspan="1"><div>“用 deepseek-v4-flash 这个模型帮我看看这张截图里的报错并解释”</div><div>“证明一下勾股定理，帮我一步步推导”</div></td></tr></tbody></table>

#### 视觉模型（图像、视频、3D生成）、语音模型相关

| 能力 | 能力说明 | 核心命令 | Agent 自然语言描述（示例） |
| --- | --- | --- | --- |
| 图片生成 | 文生图、图生图、多轮会话编辑、组图、透明底、图层拆分。覆盖混元 Hy、WAND-Vega、Vidu、Kling 等系列模型。 | thcli +gen <接口 ID（接口路径）> --model <模型 Id> --prompt "<图片描述>" [--images <参考图>]  **示例：**  文生图：`thcli +gen wand/hunyuan-image/v35-generation --model hy-image-v3.5-preview --messages '[{"role":"user","content":[{"type":"text","text":"一只橘猫趴在窗台上"}]}]' --size 1024x1024 --output ./out`  图生图：`thcli +gen wand/hunyuan-image/v35-generation --model hy-image-v3.5-preview --messages '[{"role":"user","content":[{"type":"text","text":"改成水彩风格"},{"type":"image_url","image_url":{"url":"./ref.png"}}]}]' --output ./out`  **说明：**  +gen 按 token 计费，优先使用模型的免费额度，若模型不含免费额度，或免费额度耗尽时，需通过`endpoint postpaid on`开通按量付费才可继续调用。 | “用 hy-image-v3.5-preview 画一张赛博朋克风格的城市夜景，保存到 ./out”    “用 hy-image-v3 参考这张图，生成一张水彩风格的版本” |
| 视频生成 | 文生视频、图生视频、首尾帧生视频、参考生视频、动作控制。覆盖混元 Hy、Kling、Vidu、PixVerse、MiniMax、WAND-Vega 等系列模型。 | thcli +gen <接口 ID（接口路径）> --model <模型 Id> --prompt "<视频描述>" [--image <首帧图>] [--no-wait]    **示例：**  文生视频：`thcli +gen wand/hunyuan-video/generation --model hy-video-v1.5 --prompt "海边日落" --aspect-ratio 16:9 --output ./out`  图生视频：`thcli +gen wand/hunyuan-video/generation --model hy-video-v1.5 --image ./cat.jpg --prompt "猫咪转头" --no-wait`  **说明：**  +gen 按 token 计费，优先使用模型的免费额度，若模型不含免费额度，或免费额度耗尽时，需通过`endpoint postpaid on`开通按量付费才可继续调用。 | “用 hy-video-v1.5 生成一段 16:9 的海边日落视频”    “用 hy-video-v1.5 以这张图做首帧，生成一段猫咪转头的视频” |
| 3D 与世界模型 | 文生 3D、图生 3D 模型。  生成 3D 世界 360° 全景图、3D 世界场景。 | thcli +gen <接口 ID（接口路径）> --model <模型 Id> --prompt "<场景或物体描述>" [--<参考图字段> <参考图>]    **示例：**  360° 全景图：`thcli +gen wand/hunyuan-image/world2-panorama --model hy-world2-panorama --prompt "清晨的江南古镇" --output ./out`  **说明：**  +gen 按 token 计费，优先使用模型的免费额度，若模型不含免费额度，或免费额度耗尽时，需通过`endpoint postpaid on`开通按量付费才可继续调用。 | “用 hy-world2-panorama 生成一张清晨江南古镇的 360° 全景图” |
| 语音生成与识别 | 语音合成（TTS）、音色复刻、音色设计。  语音识别（ASR，输出文本与字幕）、AI 配音、音乐生成。 | 语音识别：thcli +gen <接口 ID（接口路径）> --model <模型 Id> --data <本地音频> 或 --input-url <音频 URL>  语音合成：thcli +gen <接口 ID（接口路径）> --model <模型 Id> --text "<文本>" --voice-setting '<音色配置>'    **示例：**  语音识别：`thcli +gen wand/asrproxy/sync_transcribe --model hy-asr-3.0-preview --data ./speech.wav --output ./out`  语音合成：`thcli +gen wand/minimax-tts/sync_tts --model minimax-speech-2.8-hd --text "你好" --voice-setting '{"voice_id":"male-qn-qingse"}' --output ./out`  **说明：**  +gen 按 token 计费，优先使用模型的免费额度，若模型不含免费额度，或免费额度耗尽时，需通过`endpoint postpaid on`开通按量付费才可继续调用。 | “用 hy-asr-3.0-preview 识别这段录音的内容，输出 SRT 字幕”    “用 minimax-speech-2.8-hd 把这段文案合成语音，音色 ID 用 xxx” |
| 生成接口与任务管理 | 查看全部生成接口、调用方式（同步 / 异步）及单个接口的完整参数。  查询异步任务状态并下载结果；列出本机提交过的任务。 | 查看生成接口参数： thcli +gen apis [接口 ID（接口路径）]  查询异步任务：thcli +gen status <接口 ID（接口路径）> <任务 ID> [--wait] [--output <目录>]  列出本机生成任务： thcli +gen tasks    **示例：**  查看混元图片生成模型接口参数：`thcli +gen apis wand/hunyuan-image/v35-generation`  查询并下载任务结果：`thcli +gen status wand/hunyuan-video/generation <任务 ID> --wait --output ./out`  **说明：**  以上查询类命令不会产生费用。 | “TokenHub 有哪些混元图片生成模型，哪些是同步的”  “我刚才提交的 hy-video-v1.5 视频任务好了没，好了就下载到 ./out” |

**更多说明：**

接口 ID（接口路径）即生成接口的请求路径去掉 /v1 前缀，例如请求路径 /v1/wand/hunyuan-image/v35-generation 对应接口 ID wand/hunyuan-image/v35-generation。可通过 thcli +gen models 查看全部接口 ID 及对应模型。

同步接口提交后直接返回结果；异步接口默认等待完成，加 --no-wait 则只提交并返回任务 ID，之后用 +gen status 查询。

支持 Base64 的字段可直接传本地文件路径，CLI 自动编码；仅支持公网 URL 的字段需传 URL。

加 --output <目录> 可将结果下载到本地。结果链接约 12 小时后失效，请及时保存。

### 4. 推理服务与部署

| 能力 | 能力说明 | 核心命令 | Agent 自然语言描述（示例） |
| --- | --- | --- | --- |
| 服务查询 | 查看服务（endpoint）列表与详情，包括运行状态、计费方式、限流阈值、免费额度用量。 | thcli endpoint list  thcli endpoint get | “我有哪些服务，分别是什么状态”  “这个服务当前的限流是多少” |
| 部署 / 改配 / 删除 | 自定义服务创建（设置计费方式、RPM / TPM 限流）。  修改配置；删除。  开启/关闭服务的按量付费。 | thcli deploy  thcli endpoint update / delete  thcli endpoint postpaid on / off  **说明：**  endpoint postpaid on、deploy 会产生费用、默认二次确认。 | 无  **注意：**  部署、修改、删除接入点属于写操作，当前不支持通过自然语言直接触发。 |

### 5. 套餐与额度

<table><colgroup><col/><col/><col/><col/><col/></colgroup><tbody><tr><td><div>类型</div></td><td><div>能力</div></td><td><div>能力说明</div></td><td><div>核心命令</div></td><td><div>Agent 自然语言描述（示例）</div></td></tr><tr><td colspan="1" rowspan="3"><div>企业版套餐</div></td><td><div>套餐查询</div></td><td><div>查看已持有的企业版 Token Plan 套餐详情、可用模型范围、用量明细。</div></td><td><div>thcli plan list</div><div>thcli plan info / models / detail</div></td><td><div>“我有哪些企业版套餐，分别还剩多少额度”</div><div>“这个套餐下能用哪些模型”</div><div>“我要看这个套餐用量明细”</div></td></tr><tr><td colspan="0" rowspan="0"><div></div></td><td><div>购买 / 续费 / 升配</div></td><td><div>购买企业版套餐（专业版/轻享版）、续费、升配规格额度。</div></td><td><div>thcli plan buy</div><div>thcli plan renew / upgrade</div><div><div><b>说明：</b></div><div>plan buy/renew/upgrade 会产生费用、默认二次确认。</div></div></td><td><div>无</div><div><div><b>注意：</b></div><div>购买、续费、升配属于产生费用的写操作，当前不支持通过自然语言直接触发。</div></div></td></tr><tr><td colspan="0" rowspan="0"><div></div></td><td><div>套餐专属 Key</div></td><td><div>查看、创建、修改、重置、删除企业套餐的专属 API Key（与平台 Key 相互独立，额度单独计算）。</div></td><td><div>thcli plan key list / get</div><div>thcli plan key create / update / rotate / delete</div></td><td><div>“这个套餐下有哪些专属 Key”</div></td></tr><tr><td colspan="1" rowspan="2"><div>个人版套餐</div></td><td><div>套餐查询</div></td><td><div>查看已持有的个人版 Token Plan 套餐详情、可用模型范围、用量明细。</div></td><td><div>thcli plan personal list</div><div>thcli plan personal info / models / usage --series &lt;common / hy&gt;</div></td><td><div>“我有哪些个人版套餐，分别还剩多少额度”</div><div>“这个套餐下能用哪些模型”</div><div>“我要看这个套餐用量明细”</div></td></tr><tr><td colspan="0" rowspan="0"><div></div></td><td><div>个人版共享 Key</div></td><td><div>查看 / 生成 / 显示明文 / 重置 / 删除个人版共享 Key（通用 / Hy 共用一把，额度单独计算）</div></td><td><div>thcli plan personal key show / create / reveal / rotate / delete</div></td><td><div>「我的个人版共享 Key 是什么状态」「生成一把个人版共享 Key」</div></td></tr></tbody></table>

### 6. 观测与诊断

| 能力 | 能力说明 | 核心命令 | Agent 自然语言描述（示例） |
| --- | --- | --- | --- |
| 用量统计 | 按模型、接入点、API Key 维度查看 Token 消耗排行与趋势，支持按小时、天等粒度聚合；导出用量明细为 CSV 用于对账。 | thcli usage rank / trend / export | “今天用了多少 Token，哪个模型消耗最多”  “看一下 xx 服务近 7 日的 tpm 趋势”  “导出最近 7 天按 Key 的用量到 CSV” |
| 模型监控 | 按语言、视觉、语音模型类型查看监控数据。  支持按模型、接入点、API Key 维度查看 RPM、TTFT、TPOT、错误率等指标，支持按小时、天等粒度聚合。 | thcli monitor text / vision / audio  thcli monitor text --model <name> | “查一下 hy3 模型近七日有无调用失败记录” |
| 诊断与排障 | 全链路体检（凭证、地域、权限）  Key、服务、模型、套餐诊断，查看状态及是否可用。  错误码翻译。 | thcli doctor all  thcli doctor key / endpoint / model / plan  thcli doctor error | “为什么调用失败，检查一下什么环节出了问题”  “这个错误码什么意思”  “用 hy-image-v3.5-preview 生图前，帮我检查一下能不能调通”  “Kling 视频生成返回 1201 是什么意思，怎么修” |

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
| +gen | 生成图片、视频、3D 与语音；查询异步任务 | thcli +gen --help |
| chat-config | 本地维护 `+chat` 对话与 `+gen` 生成时用的 API Key | thcli chat-config --help |
| plan | 企业套餐列表、详情、购买、续费、升配、用量明细 | thcli plan --help |
| plan personal | 个人套餐列表、详情、购买、续费、升配、用量明细 | thcli plan personal --help |
| usage | 用量排行、导出 CSV | thcli usage --help |
| monitor | RPM、TTFT、TPOT、错误率等 | thcli monitor --help |
| doctor | 全链路体检、输出修复动作 | thcli doctor --help |
| profile | 多账号 Profile 管理 | thcli profile --help |
| site | 站点（cn / intl）切换 | thcli site --help |
| lang | 界面语言（zh / en）切换 | thcli lang --help |
| +connect | Agent Skills 一键注入 | thcli +connect --help |

## **参考信息**

关于站点与地域的资源隔离规则、本地文件结构（`~/.thcli/`）、调用日志等进阶说明，请参见 [开源仓库](https://github.com/TencentCloud/THCLI)。
