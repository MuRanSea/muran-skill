# 多 Harness 协作首版

## 目标与职责

用户通过 Codex 提出目标，Codex 先制定方案和任务表，逐项指定本地 CLI、具体模型、文件范围、依赖和验收标准，再按计划派发。技能承载规划和调度规则，Python 脚本负责计划校验、CLI 执行及证据保存。首版接入 Claude Code 与 Antigravity CLI（agy）；主 agent 保留判断、验证和整合职责。

```text
用户目标 → Codex 方案与任务表 → ready 计划
         → 按任务指定 CLI + 模型 → 结果与 patch
         → Codex 验收记录 → 派发后续任务 → 整体验收与整合
```

`check-plan` 检查完整任务分工和依赖图，不调用模型。`run --plan --task-id` 只派发一个已定稿任务。依赖必须持有与当前计划绑定的验收记录；前序回答和验收证据会传入下一任务。`accept` 记录 Codex 已经完成的验证，不产生额外用户审批，也不代替实际测试。仅讨论方案时保留 draft；已授权执行时由 Codex 定稿并继续。

| 模式 | 工作区 | 工具 | 交付物 |
|---|---|---|---|
| advisor | Claude 使用指定项目；Antigravity 使用独立 worktree | 读取、搜索 | 有文件证据的建议 |
| researcher | Claude 使用指定项目 | 文件读取、搜索、WebSearch、WebFetch | 带原始来源与证据分级的调研材料 |
| worker | 干净 HEAD 的独立 detached worktree | 读取、搜索、编辑、写入 | 代码、完整 patch、待验证说明 |

验证命令由 Codex 执行。Claude 的 CLI 白名单不提供 shell 或其他 agent 工具；researcher 仅额外开放公开网页调研工具。Antigravity 原生工具权限保持原状，依靠任务指令和事后审计约束范围，不能承诺执行前拦截。原始日志保存到本地忽略目录，常规回读使用统一 `result.json`。`completed` 表示有效 CLI 终止事件及成功退出，不等于验收通过。

## 首版边界

- 按轮次同步调用 CLI；宿主工具可保留执行会话并异步等待。新任务拥有独立运行目录，revise 沿用同一会话和工作区，每轮证据独立保存。
- 每次运行重新探测 CLI 版本和 flags，强制使用任务中显式指定的模型 ID；模型缺失或使用 auto/default 时拒绝派发。CLI、模型、任务角色独立选择，认证或模型错误不触发静默替换。
- 保存计划快照、任务 ID、计划指纹与 requested_model。CLI 实际报告模型另记 model；未报告时保持 null，不能把指定参数等同于提供商侧实际模型证明。
- 计划修改使旧结果不再用于新计划的后续派发；Codex 需重新核对受影响工作。worker 依赖按已验收文件哈希检查目标基线，不能在旧源码上仅携带文字结论继续工作。
- prompt 走 UTF-8 stdin，Windows npm shim 解析后直接启动 Node 或 EXE；不将 prompt 插入 shell。
- 180 秒默认时限，16 MiB 日志上限；超时终止所启动的进程树。保留失败产物，不自动重试。
- worker 要求精确文件范围，含未跟踪/被忽略的新文件在内都参与事后检查。越范围标记失败、保留修改，不自动恢复。
- 工作树是协作隔离，不是安全沙箱。只面向可信本地项目；文件工具的操作系统访问能力没有额外隔离。主进程被强制终止时需检查遗留进程。
- Antigravity 1.2.7 自定义 agent 的工具白名单未通过实测，首版不依赖它。运行结果明确记录 `prompt_and_audit`，所有调用在 worktree 执行，对越范围工具和文件修改标记失败；不会自动改写全局账号、agent 或权限配置。
- CLI 自身使用现有账号；执行器不探查认证文件、不输出环境变量。

支持显式子会话恢复、实时事件、取消、退回、检查和验收；常驻双向消息、主会话 Watchdog、自动重试和其他 CLI 适配器留在后续版本。路由决策由 Codex 在计划中作出，脚本不自动选择模型或执行整张任务图；跨 worker 的代码传递与基线准备也由 Codex 处理。原始日志和运行结果不纳入 Git。

## 验证方式

自动化测试使用合成 CLI 与真实 subprocess/Git，覆盖显式模型传递、计划图校验、草稿拒绝执行、依赖验收、计划/结果变更失效、worker 代码依赖、任务传输、协议错误、文件范围、patch 可应用性、超时进程树清理和日志上限。这些是执行器测试，不是模型验收。

```powershell
uv run --locked python -X utf8 -m unittest discover -s tests -p test_harness.py -v
uv run --locked python -X utf8 -m unittest discover -s tests -v
```

真实 CLI 使用独立标签规范化样例：去空白、转小写、去空值、稳定去重、Unicode 和输入不变性。原始实现六项测试中三项失败。advisor 应阅读文件并指出缺失逻辑；worker 只修改函数文件；主 agent 在独立 worktree 运行六项测试，并确认源仓库保持原样。

## 2026-09-22 初版实测记录（调整计划流程之前）

真实任务均调用本机已有 CLI 和默认账号/模型；未读取凭据或修改 CLI 全局配置。样例与原始日志位于本地 `.cache/harness-smoke-v1/`，未纳入 Git。

| CLI / 模式 | 运行 ID | 实际结果 |
|---|---|---|
| Claude advisor | `e375a6685d7840c6a69068e251fb7b53` | completed；4 次工具调用，指出空值和重复项问题 |
| Claude worker | `c28186e6a81044a5986c26324c1594cc` | completed；3 次工具调用，仅修改 tag_utils.py；父 agent 的 6 项测试全部通过，patch 可应用 |
| Antigravity advisor | `f5005bc68d9e48ecb021cbba1cd77dce` | completed；3 次 view_file 调用，无文件修改，三行输出准确定位缺陷 |
| Antigravity worker | `302255262ca54b7f8d5b218c74e11ad1` | completed；4 次工具调用，仅 view_file / replace_file_content；只修改目标文件，父 agent 的 6 项测试全部通过 |

两次 Claude 样例合计 CLI 估算费用约 $0.0618；Antigravity 事件未报告实际模型名称或金额，统一结果保留 null。两者的原始工作区均保持原有源码。Antigravity worker 多留了一行文件尾空白，功能测试通过但 `git diff --check` 有提示，体现主 agent 仍需执行质量检查。

Antigravity 首次 advisor 在 120 秒时限内读取了两个文件但未返回终止结果，保留为 timed_out；核对无文件修改后，主 agent 用三行输出要求和 180 秒时限发起了新任务，约 48 秒完成。这是显式测试决策，执行器本身没有自动重试。

独立 Codex 前向测试按技能完成一次 Claude 咨询：`9704964342c4459588df4ae51ffd0cb8`，约 14.56 秒、CLI 估算 $0.0244842；仅两次 Read，源码哈希、HEAD 和 Git 状态均未变化，验收仍为 pending。该测试发现 doctor 无法仅检查选定 CLI，已增加 `doctor --harness` 并通过回归。模型报告的一处标题分类不准确，主 agent 已按文件证据核对，而非直接采信文字。

技能通过 skill-creator 格式校验；安装器新增 3 个共享链接、复用原有 78 个链接，无冲突、无移除。首版执行器的 13 项自动化测试通过，包括 Antigravity 咨询修改文件和越范围工具调用的失败审计。

最终全库回归执行 77 项：75 项通过，2 项既有 uv 启动测试在默认共享缓存中分别遇到 `too many temporary files exist` 和 Windows `os error 183`。保持代码不变，将 `UV_CACHE_DIR` 指向项目 `.cache/harness-uv-cache` 并准备锁定版本依赖后，这两项单独复测通过。全局 uv 缓存未改动；此结果不表述为默认缓存下全库全绿。仓库 `git diff --check` 通过，所有源代码改动保持未提交状态。

## 2026-09-22 计划优先流程验证

根据使用反馈，入口调整为 Codex 先制定方案与任务表，再从 ready 计划派发；每项任务显式指定 CLI 和模型，后继任务要求主 agent 验收前序结果。移除直接 `run --task` 和模型省略行为。

自动化测试增加到 20 项，全数通过。全库使用项目独立 `UV_CACHE_DIR=.cache/harness-uv-cache` 回归 84 项，全部通过；技能格式校验通过。共享全局 uv 缓存未修改。

真实顺序执行计划为 `.cache/harness-plan-v1/plan.json`，使用原有干净样例：

| 任务 | CLI / 指定模型 | 运行 ID | 结果 |
|---|---|---|---|
| inspect | Antigravity / `gemini-3.8-flash-high` | `f376958935f44084814f95b87cd8a66e` | 约 38 秒，2 次 view_file，无修改，CLI 报告模型与指定一致 |
| implement | Claude / `claude-sonnet-5` | `16f56dd061254ff1aac4d138c135ba23` | 约 10 秒，3 次工具调用，仅修改 tag_utils.py，CLI 报告模型与指定一致 |

Antigravity 的模型 ID 从本机 `agy models` 清单核实。Codex 运行基线测试，确认分析中的反例与三项失败一致，写入验收证据后才启动 Claude。后续任务输入包含前序分析和验证记录；Claude 实现后 6 项测试全部通过，`git diff --check` 和 patch 可应用性检查通过，源样例保持干净且源码未改变。

两步分别保存计划快照、指定与报告模型、原始事件及验收证据。Claude CLI 估算费用 $0.033404；Antigravity 未报告费用。该测试证明带明确模型与验收依赖的咨询→实现链路已跑通，不代表其他 CLI 已接入或 worker patch 会自动传递。

独立前向测试另验证“先给方案，等用户看完再执行”：产出包含 CLI、模型、依赖和验收标准的 draft 计划，`check-plan` 返回 valid；没有启动模型任务、运行 accept 或修改样例源码。结果保存在 `.cache/harness-forward-plan/`。据此澄清规划阶段可复用当前会话已核实的模型信息，实际派发仍重新检查 CLI。

## 2026-09-22 联网调研与写作验证

新增仅 Claude 支持的 researcher 模式，以 WebSearch/WebFetch 进行公开调研。真实测试由 Claude 调研 Jev、Gemini 写作、Codex 验收；初稿内容未达标后，明确建立修订计划，再由 Codex 完成终稿编辑。执行器 21 项针对性测试与项目独立 uv 缓存下全库 85 项回归通过。见 [报告](research/jev-research-report-2026-09-22.md) 和 [执行记录](research/jev-multi-harness-test-2026-09-22.md)。

## 2026-09-22 会话续接与验收修复

Jev 测试后的修复增加显式会话续接、逐轮证据快照、实时状态和取消、主 agent 退回/验收、经过整理的交接包、writer 输出约定与确定性检查。Claude 和 Gemini 均完成真实两轮续接验收；具体记录及当前边界见[续接与验收修复记录](research/multi-harness-session-verification-2026-09-22.md)。
