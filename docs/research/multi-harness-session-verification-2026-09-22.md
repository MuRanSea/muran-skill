# Multi-harness 续接与验收修复记录

日期：2026-09-22。针对 Jev 调研测试暴露的重复创建修订计划、草稿与纠错混传、写作回复过长、篇幅只能人工判断，以及原稿与主 agent 编辑混在同一工作区的问题，更新本地 multi-harness 技能和执行器。

## 已实现

- Codex 仍先确定 ready 计划、任务和显式模型。新增 `reject`、`revise`、`status`、`cancel`；同一任务修订沿用 run ID、task ID、session ID 和工作区，不重新复制全部材料。
- CLI 运行时持续消费事件，保存事件序号、工具状态、会话 ID 与心跳。状态查询无需读取完整 stdout。取消请求由执行器处理并终止子进程树。
- 区分执行状态与验收状态。CLI completed 后进入 awaiting_review；确定性检查失败进入 needs_revision；必须经 Codex 核验才能 accepted。
- 每轮保留 result、response、patch、检查与交付快照，修订放在 attempts/002 等目录。验收前核对文件内容、完整变更集合与 HEAD，后续人工修改不能冒充子 agent 原稿。
- 下游默认只接收 Codex 核验过的交接包，包含结论、来源 URL、证据等级和限制；不再自动拼接原始草稿。结果、任务、交接包与文件通过哈希关联。
- writer 提示默认成功只回交付路径；新增汉字数、文件存在、必含/禁含文字、URL 清单检查，以及 effort 参数和 agy 档位冲突校验。

当前是**每轮启动本地 CLI，再按会话 ID 续接**。未实现常驻双向代理、执行中追加消息、主会话 Watchdog 或自动重试。既有 worker 依赖仍需 Codex 整合到适当的干净基线；没有自动应用 patch。

## 真实 CLI 两轮测试

测试使用 `.cache/harness-session-v2/plan-v2.json`，两个独立小任务。所有模型与 effort 都写在计划中；不读取凭据、不修改全局配置。这是通信与修订能力测试，不是重新调研 Jev。

| 任务 | CLI / 版本 | 指定及报告模型 | 结果 |
|---|---|---|---|
| claude-memory | Claude Code 2.1.274 | claude-sonnet-5，effort=low | 两轮均 completed，Codex 验收 accepted |
| gemini-write | Antigravity 1.2.8 | gemini-3.8-flash-low，effort=low | 初稿检查失败，原会话修订后检查通过，Codex 验收 accepted |

Claude 第一轮只答 READY；第二轮反馈不含之前的测试口令，仍准确返回 `cedar-7831`，两轮均无工具调用。运行 ID 为 `b7900040b3144629b07ccc22149c8234`，会话 ID 为 `8139d8ba-a956-48bc-9bd6-b846c911d8a5`。

Gemini 第一轮只创建含“第一版”的 report.md，故意不满足预设的“第二版”检查，执行器记录 needs_revision。第二轮仅收到修改反馈，写入“第二版”以及之前未写入文件、也未在反馈重发的 `violet-8247`。两轮回复均仅 report.md，各有一次 write_to_file，无越界工具或文件变化。运行 ID 为 `d091511c2bd84876a8901890bf0dcd20`，会话 ID 为 `83cd9613-4b6a-4872-80d9-b2eeeba415ca`。

Codex 验证了相同任务/会话/工作区、初稿快照及原始结果未被覆盖、修订文件内容与哈希、检查前后状态、patch 可应用性和源项目 Git 干净状态，并为第二轮保存 acceptance.json。证据入口：`.cache/harness-session-v2/verification-summary.json`，验证脚本为同目录 verify.py；完整两轮日志位于 validated/ 下。

## 实测发现并修正

首次 agy 1.2.7 调用因 `gemini-3.8-flash-high` 配 low effort 被拒绝，没有工具调用或产物。保留该失败运行 `269188106f2549ada54063d166fd41b1`，新增调用前冲突校验。随后通过 `agy models` 核实 low 型号，明确建立 plan-v2.json；没有静默替换。正式验收运行探测到的本机版本为 1.2.8。

Claude 跨进程续接报告的用量/费用部分重新起算：正式两轮 CLI 原始估算金额分别为 $0.0029556 和 $0.001849。执行器不再假定统一累计语义，不自动相加或相减；usage_delta 和 cost_delta_usd 保留 null，原始 usage/cost 保留。Antigravity 未报告金额。上述数值不作为账单核算。

独立合成检查发现两类边界并完成修复：一是原 changed_files 未包含的文件在验收前后被修改，可能漏检，现核对完整变更集合；二是续接错误会话后再尝试修订可能接纳该错误会话，现阻止 protocol_error 结果继续 revise，要求主 agent 调查后建立新运行。保存的 task.json 也须匹配原任务指纹与计划，不能绕过计划更换模型或范围。

## 回归与限制

全库 92 项回归通过，使用项目独立 `UV_CACHE_DIR=.cache/harness-uv-cache`；随后执行器 29 项回归通过。最后对会话错误恢复、任务文件变更、双 adapter 修订和交接哈希的 4 项相关测试复测通过。技能格式校验通过。合成 CLI 测试使用真实 subprocess/Git，但不算提供商验收；上面的真实运行证据单独列出。

独立前向验证另覆盖 19 个合成场景，暴露并推动修复上述两类边界；最终代码定向复测两种 CLI 的正常修订和错误会话恢复共 4 个场景，全部符合预期。最终证据：`.cache/harness-revision-forward/evidence-20260922-122733/summary.json`；可复现脚本：同级工作目录中的 `verify_revision.py --focus-session`。该检查没有调用真实模型或修改产品源码。

自动检查统计整个文件的汉字，包括标题和参考文献；URL 检查只统计字符串，不证明原文支持结论。事实、文风和语义验收仍由 Codex 执行。Antigravity 继续采用原生权限、提示约束和事后审计，不能宣称有执行前工具拦截。源码未提交或推送。

命令、字段、状态和交接格式见[计划与执行契约](../../skills/multi-harness/references/execution.md)。
