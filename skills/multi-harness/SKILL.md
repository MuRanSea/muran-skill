---
name: multi-harness
description: 由 Codex 先制定计划、拆分任务、为每项任务指定 CLI 和模型，再调度本地 Claude Code、Antigravity CLI（agy）并验收。适用于跨 harness 协作、本地 CLI 子 agent、联网调研与写作分工和独立审查；普通单 agent 任务无需启用。
---

# 多 Harness 计划与调度

用户给目标，Codex 负责规划、拆解、分工、验收与整合，CLI 执行有边界的子任务。先读 [计划与执行契约](references/execution.md)。首版支持 Claude Code 和 Antigravity CLI。

1. 先由 Codex 阅读项目规则和必要源码，确定目标、边界、方案、验收方法及需要委派的工作。调度决策由 Codex 作出；计划阶段可检查 CLI 和模型清单，模型任务须等计划就绪。
2. 核对可用 CLI 与模型：规划可复用当前会话已核实的信息，缺少时用 `scripts/harness.py doctor --harness claude|agy` 检查接口、用 `agy models` 查询 Antigravity 当前模型 ID；实际派发会重新探测 CLI。遵守用户指定的选择，否则依据任务难度、已知能力、时限和预算选择已核实的具体模型，并写明分工理由。无法确定可用模型时才询问；每项任务必填模型 ID，不使用本地默认值、auto 或静默降级。
3. 向用户展示总体方案与任务表：任务 ID、目标、CLI、模型、模式、文件范围、依赖、交付物与验收标准；标明 Codex 自己负责的验证和整合。文件咨询用 advisor，Claude 公开网页调研用 researcher，代码或文档写入用 worker；写作设置 `profile: writer`，默认只返回交付路径，正文留在文件。明确篇幅时配置 `checks` 自动统计，并按需要指定 `effort`；agy 的模型档位须与 effort 一致。按契约写 `.cache/` 下的 `plan.json`，用 `check-plan --plan <绝对路径>` 校验。用户仅要求设计时保留 draft；已授权实施且信息齐全时由 Codex 定稿为 ready 并继续，用户要求先审计划时等待其确认。
4. 按依赖顺序调用 `run --plan <绝对路径> --task-id <ID>`，依赖任务需提供 `--dependency-result`。只有已验收前置任务齐全的任务可启动。独立且文件范围不重叠的任务可并行；委派深度一层。保留工具执行会话，通过 `status --run-dir ...` 查看心跳和最近事件，需要停止时用 `cancel`。任务背景仅传计划与主 agent 核验后的交接材料，不自动拼接原始草稿。
5. 读取最新 `result.json` 和 `checks.json`，核对指定模型与报告模型、文件证据、完整 diff、范围告警，并由 Codex 执行验收命令。`completed` 只是 CLI 正常结束，不能直接解锁后续任务。不合格时将具体问题写入反馈文件，用 `revise --plan ... --task-id ... --result ... --feedback ...` 续接同一任务和会话；仅登记退回用 `reject`。通过后把真实验证结果写成证据文件，用 `accept --plan ... --task-id ... --result ... --evidence ...` 记录验收。需要后续写作时另外准备精简 `handoff.json` 并传 `--handoff`，逐条写事实、原始 URL、证据等级与限制；省略时只传验证证据，不传未经整理的子 agent 回答。这是 Codex 的核验记录，不是额外的人类审批。模型标识不同需核对别名/路由，未报告实际模型需保留证据缺口。
6. Codex 整合经过验证的修改并执行整体验收，报告每项任务的 CLI、指定/报告模型、结果及未解决项。worker 和 Antigravity advisor 从干净 HEAD 创建独立 worktree；未提交内容不会复制。后续任务依赖 worker 代码时，先准备包含该代码的合适基线；执行器检查前置文件内容，避免在旧代码上继续工作。整合、commit、push、PR 遵守原任务授权。

任务范围：advisor 只读取和搜索文件；researcher 额外开放 Claude 的 WebSearch/WebFetch，交付带原始链接的证据材料；worker 增加文件编辑和写入，测试命令由 Codex 执行。调研验收需确认真实网页工具返回和来源内容，不能以调用次数或 CLI completed 代替来源核验；写作任务依据已验收材料成文。Claude 使用 safe mode 与 CLI 工具白名单。Antigravity 1.2.7 未能通过工具白名单实测，沿用原生权限，依靠任务指令和事后工具审计；其范围限制不属于执行前强制拦截。Antigravity 两种模式都放入独立 worktree，越范围调用或文件修改标记失败。工作树也不是操作系统沙箱；首版仅用于可信本地项目。

同一任务的内容修订不改计划，沿用 session ID、worktree 与 run ID，每轮产物独立保存。缺少会话 ID、会话恢复失败或范围违规时停止，由 Codex 核对后明确建立新任务；不静默新开会话。更换 CLI、模型、范围或依赖要写入计划再执行。脚本不自动重试或应用 patch；修改计划会使旧验收无法直接用于新计划调度。不要覆盖子 agent 的快照或修改其工作区后仍冒充原始交付；Codex 自行编辑应另存最终稿并记录归属。当前是逐轮调用 CLI 并显式 resume，不是常驻双向代理；Watchdog、执行中追加消息及其他 CLI 留待后续实现。
