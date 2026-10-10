# 多 Harness 协作 v2：统一模型与脚本推进

2026-10-10。保留首版原则：Codex 规划和验收，本地 CLI 执行有边界的子任务，靠证据验收，不静默换模型。重写的是实现。首版的设计记录见 [v1](multi-harness-v1.md) 和[协作组首版](multi-harness-groups.md)。

## 首版的问题

1. **流程靠主持人手工推进**：`run` 一次只派发一个任务，依赖顺序、验收后带 `--dependency-result` 这些步骤都写在 SKILL.md 里让 LLM 照做。两步计划要十几次纯流程操作。
2. **计划和协作组互不相通**：计划存在 `.cache/harness-runs` 文件里，组存在 SQLite 里。组成员只能讨论，干活要另开计划再 `link` 回组，讨论过的上下文进不了任务会话。
3. **对真实环境太脆**：worker 和 agy 要求仓库干净；串联的 worker 之间必须先 commit；超时、基线变化或模型名不一致都只能开新组；所有派发串行且阻塞。
4. **CLI 差异散落**：`if harness == 'claude'` 分布在七八个函数里，讨论模块还要切开 harness 拼好的 prompt 字符串。

## v2 结构

| 模块 | 职责 |
|---|---|
| `adapters.py` | 每个 CLI 一个 `Adapter` 子类：参数、输入编码、事件摘要与解析、工具白名单或审计、启动器解析。新增 CLI 只加一个类。 |
| `worktrees.py` | 工作区快照、worktree、依赖 patch 的应用与跳过、`integrate`、改动收集。 |
| `runner.py` | 任务校验、prompt 构造、单次尝试的进程监督与证据保存。 |
| `groups.py` | 唯一的命令入口：SQLite 中的组、成员会话、消息、轮次和任务；并行推进、验收关口、修订、fork、暂停与恢复、后台运行。 |

关键决定：

- **任务属于组并指派给成员**，CLI 和模型从成员继承，因此不再需要 `link` 和模型匹配检查。成员最近几轮问答作为 `member_discussion` 带进它的任务（标为未核实的上下文）。Claude 的 `--resume` 按项目目录查找会话，讨论会话无法搬进 worktree，所以带的是讨论记录，而不是共享同一个会话。
- **advance 只推进一轮**：并行运行所有依赖已验收的任务，以及每位成员排队的消息，然后停在验收关口。验收这一步不交给脚本自动完成。
- **快照基线**：用临时索引执行 `add -A` 和 `commit-tree`，得到包含未提交、未跟踪文件的提交对象，不改用户的分支、暂存区和文件。worktree 的 HEAD 引用这个提交，所以它不会被 gc 清理。依赖的 patch 若已经存在于基线中（反向检查通过），就跳过。
- **失败局部化**：轮次失败只阻塞该成员，其他成员照常工作；`fork --member` / `fork --task` 是明确的恢复路径。agy 讨论成员每轮跟到最新快照，会话不变。
- **哈希只用在关口**：验收时核对交付快照、工作区和检查输入；下游启动时核对交接包和 patch 的哈希。中间状态以 SQLite 为准。
- **执行锁**：每个运行中的成员或任务都持有一个操作系统文件锁。`reconcile` 能拿到锁，就说明执行器已经退出，这时只收录已经落盘的终止结果，没有结果的标为 unknown 或 interrupted，不会重发。
- **后台推进**：`advance --detach` 启动一个脱离当前进程的监督进程，它持有 supervisor 锁；`wait` 轮询到工作结束。
- 默认时限从 180 秒改为 600 秒。新的状态库文件名为 `collab.sqlite3`；检测到旧格式的库时拒绝打开，不做迁移。
- 新增 `MURAN_HARNESS_<NAME>_LAUNCHER` 环境变量，用 JSON argv 指定不在 PATH 中的 CLI；测试也用它在子进程中替换为假 CLI。

## 不变的边界

模型 ID 必须显式填写；不读取凭据，不传任意 CLI 参数；prompt 通过 UTF-8 stdin 传入；子 agent 不能控制组、验收或递归委派；Claude 用工具白名单，agy 靠指令加事后审计；worktree 不是操作系统沙箱；不自动重试，不自动 commit。没有常驻代理、执行中追加消息或已读回执。

## 验证

`tests/test_harness.py`（15 项）覆盖适配器、执行器和快照；`tests/test_groups.py`（19 项）通过公开命令覆盖开组、幂等消息、成员并行、会话续接、失败隔离与 fork、暂停与取消、控制进程崩溃后的恢复、模型不一致、agy 跟随新基线、计划→验收→交接→整合、无需 commit 的 worker 串联、任务并行、修订与检查关口、证据篡改、尝试上限，以及后台推进。两组测试都使用合成 CLI，加真实 subprocess 和 Git，不构成真实模型验收。

### 2026-10-10 真实 CLI 端到端

样例项目放在被忽略的 `.cache/real-e2e-2026-10-10/` 下：`normalize_tags` 会按字母重排、保留空值、遇到 None 就崩溃；新增的要求写在一份**未提交**的 NOTES.md 里。

| 步骤 | 成员 / CLI / 指定与报告模型 | 结果 |
|---|---|---|
| `send --to all` 后 `advance` | 实现者 Claude Code 2.1.285 `claude-sonnet-5-5`；测试者 agy 1.3.3 `gemini-3.8-flash-low` | 两人并行回复，共 22.8 秒；指出的缺陷都附行号，经核对属实；agy 在快照 worktree 中读到了未提交的 NOTES.md |
| `approve` 后 `advance` → `fix`（Claude worker） | 同上 | 10.9 秒；只改了 `tag_utils.py`；Codex 在其 worktree 运行 3 项测试通过，手工用例结果正确，随后验收 |
| `advance` → `tests`（agy worker，依赖 `fix`） | 同上 | 31.0 秒；worktree 的基线依次是快照提交和自动应用 `fix` 的提交，中间没有任何 commit；只改了测试文件，新增 3 项测试；6 项全部通过；工具只用了 `view_file` 和 `replace_file_content` |
| `integrate` 两个任务 | — | 两个 patch 都应用到项目工作区，项目中 6 项测试通过；NOTES.md 保持未跟踪，没有产生提交 |

4 次调用报告的模型都与指定一致。Claude CLI 估算费用为 $0.0226 + $0.0278；agy 不报告费用。整个过程中主持人用到的命令只有 open、send、advance、approve、accept、integrate、status。
