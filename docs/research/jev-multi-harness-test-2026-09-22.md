# Jev 调研报告：多 Harness 协作实测记录

日期：2026-09-22。用户指定 Claude Code 调研、Gemini 写作、Codex 监工。最终交付见 [Jev 调研报告](jev-research-report-2026-09-22.md)。

## 计划与真实执行

Codex 先确认用户提供的 TypeSafe 文章，建立研究→验收→写作计划，为每一步明确 CLI、模型、输入与验收标准。在独立样例项目中执行，未提交主仓库改动。

| 阶段 | CLI / 指定及报告模型 | 运行 ID | 耗时 | 结果 |
|---|---|---|---|---|
| 一手材料调研 | Claude Code / `claude-sonnet-5` | `bfb84d363f0147f58b42fbce5752457c` | 约 58 秒 | 1 次 Read、5 次 WebFetch、2 次 WebSearch；Codex 核查并纠偏后验收 |
| 报告初稿 | Antigravity / `gemini-3.8-flash-high` | `7314958c0d8f443ca1a5faa4764bbfec` | 约 90 秒 | 只新增 report.md；CLI completed，但内容验收未通过 |
| 反馈修订 | Antigravity / `gemini-3.8-flash-high` | `ec82d82f799f4fc982133af65517b6fe` | 约 154 秒 | 根据具体反馈重写；Codex 完成最终编辑后验收 |

三个运行的模型报告均与指定 ID 一致。Claude CLI 估算费用为 **$0.1841314**；Antigravity 未报告费用，不能按零费用计算。以上耗时为各子任务运行时间，不含 Codex 规划、来源核查和编辑时间。

## 监工实际纠正了什么

Claude 的材料有真实网页工具返回，但仍需纠偏：System One 是模型类别，Jev 是具体模型；Noul 没有独立 confidence 字段；本次没核实第三方复现不能写成不存在复现；公开适配器的 MIT 许可不等于 Jev 权重许可。

Gemini 初稿自报约 2200 字，实际正文约 3499 个汉字；还把概率校准和 confidence 指标混为一谈，加入“确定性网关”以及未公开训练细节推断。Codex 没有因为 CLI 正常结束就验收，而是保存初稿，明确列出 11 项修改要求，用新计划再次派发同一 Gemini 模型。

新计划将前一步已验收研究及 Codex 反馈固化为只读输入，没有让旧计划的验收指纹自动适用于新计划。Gemini 修订后主要事实问题得到纠正，正文仍约 2429 个汉字；Codex 最后删除重复、修正文句和归因，形成正文约 2011 个汉字的交付版。原始初稿、Gemini 修订稿、终稿与日志分别保留。

最终稿的 9 个唯一来源链接由 Codex 实际打开核查。内容明确区分官方宣称、公开接口规格和本报告的评估建议。本次未登录 Jev 控制台或调用 Jev API，因此不构成性能实测。

## 技能与执行器验证

本次为实际调研需求补充 Claude `researcher` 模式：只在该模式增加 WebSearch/WebFetch，仍不开放 shell、文件写入或递归 agent。两个 adapter 的结果都记录实际 observed_tools；调研验收检查原始工具返回，而非仅看工具次数。

- 执行器针对性测试：21 项通过。
- 全库回归：项目独立 UV_CACHE_DIR 下 85 项通过。
- 技能格式校验通过。
- worker 文件范围检查与最终 patch 可应用性检查通过；两个研究源项目均保持干净。
- 初稿两次尝试中，Gemini 都曾先读取尚未创建的 report.md，收到文件不存在错误后继续写入；没有越范围工具调用。这不影响成文，但说明 CLI 最终成功不等于每一步工具都成功。

## 本地产物与当前边界

运行材料位于仓库忽略目录 `.cache/jev-research-20260922/`：

- `plan.json`：原研究→写作计划。
- `revision-plan.json`：反馈修订计划。
- `research-verification.md`：Codex 研究核查与写作修正。
- `writing-review.md`：初稿未通过验收的具体理由。
- `gemini-revision-original.md` / `.patch`：Gemini 未经父 agent 编辑的修订产物。
- `final-verification.md`：最终内容、来源和文件验收记录。
- `runs/<运行 ID>/`：原始事件、模型/用量、任务和计划快照、worktree 与验收记录。

此次证明了真实 CLI 调研、模型明确选择、材料交接、退回修改和父 agent 终审能够串联工作。当前修订通过新计划和输入快照完成，尚无原生“退回修改/继续会话”命令；调研深度与写作质量仍依赖主 agent 的实际核查，不能将 completed 等同于可交付。
