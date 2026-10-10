# 操作手册

脚本只用 Python 3.12+ 标准库和 Git。下文省略 `python -X utf8 <skill>/scripts/groups.py`；也可用 `uv run --project <muran-skill 仓库> --locked python ...`。所有输出都是 JSON。除 `doctor`、`team`、`open`、`list` 外，命令都带 `--cwd <项目>` 和 `--group <组 ID 或名称>`。

## 定位组

- 状态库默认在 `%LOCALAPPDATA%/muran-skill/collab.sqlite3`（非 Windows 为 `~/.local/share/...`）。项目要求产物留在指定忽略目录时，每条命令都传同一个 `--store <目录>/collab.sqlite3`，参数放在子命令之前。证据和工作区放在库旁的 `<库名>-runs/<组 ID>/`。
- 组的定位顺序：先看明确的 `--group`，再看 `--context <当前对话 ID>` 绑定的组，最后才用项目里唯一的那个组。有歧义时脚本返回候选列表，把候选给用户选，不要猜。
- `list --cwd <项目>` 列出项目里的组和已保存的团队。

## 开组：成员与任务一次写完

```json
{"name": "Jev 内容审查", "cwd": "D:/Work/example", "context": "<当前对话 ID>",
 "goal": "研究请求内容审查，交付说明与 demo",
 "strategy": "研究员核对原始来源，编辑整理说明，Codex 验收并整合",
 "acceptance": ["接口有原始来源", "演示可运行"],
 "members": [
   {"id": "researcher", "role": "研究员", "harness": "claude", "model": "<已核实的 ID>", "mode": "researcher", "effort": "medium"},
   {"id": "editor", "role": "编辑", "harness": "agy", "model": "<已核实的 ID>"}
 ],
 "plan_state": "draft",
 "tasks": [
   {"id": "sources", "member": "researcher", "objective": "收集并核对接口文档", "acceptance": ["每条结论附原始 URL"]},
   {"id": "report", "member": "editor", "mode": "worker", "profile": "writer", "depends_on": ["sources"],
    "objective": "依据已核实材料写 report.md", "allowed_paths": ["report.md"], "acceptance": ["事实与推断分开"],
    "checks": [{"type": "cjk_count", "path": "report.md", "min": 1500, "max": 2500}]}
 ]}
```

`open --config <文件>`。之后需要追加或替换未开始的任务时，写 `{"state": "ready", "tasks": [...]}` 并 `plan --config`；用户确认 draft 方案后 `approve`。可复用的成员组合用 `team --name <名> --config {"members": [...]}` 保存，开组时以 `"team": "<名>"` 代替 `members`；保存后再改团队，不影响已开的组。

**成员字段**：`id`（小写短标识）、`role`（可用来点名）、`harness`（`claude` / `agy`）、`model`（完整 ID，不能写 auto/default）、`mode`（讨论模式：`advisor`，或仅 Claude 支持的 `researcher`）、可选 `effort`、`timeout_seconds`（默认 600，上限 3600）、`max_budget_usd`（仅 Claude，默认 1，是 CLI 自己的估算）。agy 模型名带档位后缀时，`effort` 必须与之一致。

**任务字段**：`id`、`member`、`objective`、`acceptance` 必填；可选 `mode`（默认取成员的讨论模式；写文件用 `worker`）、`depends_on`、`rationale`、`context`、`files`（提示要看的文件，不是读权限）、`constraints`、`allowed_paths`（worker 必填，精确的相对文件名，不支持目录或通配）、`profile`（worker 可用 `coder` / `writer`）、`response_format`（`report`，writer 默认 `paths`）、`checks`，以及覆盖成员设置的 `effort`、`timeout_seconds`、`max_budget_usd`。任务一定用成员的 CLI 和模型。

**checks**：`exists`、`contains` / `excludes`（`text`）、`cjk_count`（全文件汉字数，含标题和参考文献）、`urls`（去重后的 URL 字符串数，不验证可达性），后两种填 `min` / `max`。检查不通过时任务进入 `needs_revision`。

## 把用户的话转为命令

| 用户说 | 命令 |
|---|---|
| “让研究员解释依据” / “@编辑 写清限制” | `send --to <id或role> --text "..."`（长文本用 `--text-file`），然后 `advance` |
| “大家评审这个方案” | `send --to all --text "..."` 后 `advance`，各成员并行回复；汇总分歧，由 Codex 作决定 |
| 记录已定下的决定 | `send --to codex --kind decision --text "<完整的当前决定摘要>"`；之后每次派发都会带上最新一条 |
| “现在怎么样” | `status`：看 `next` 提示、各任务状态、阻塞成员；不调用模型 |
| “展开刚才的讨论” | `history --after <id>`，保留原话与来源，转述时标明是转述 |
| “开始做” / “按方案执行” | `approve` 后进入交付循环 |
| “暂停” / “继续” | `pause` / `resume`，再 `advance` |

消息转给另一位成员时，用 `--reference <原消息 ID>`（可多次）附上原文；对方看到的是带出处、未经核实的引用。`--request-id` 让重试的工具调用不会重复入队；同一 ID 配不同内容会被拒绝。

## 推进

`advance [--parallel N] [--limit M] [--only tasks|messages] [--detach]`

- 开始前先自动恢复已经死掉的执行器（同 `reconcile`），然后并行运行：所有 `ready` 且依赖都已验收的任务，以及每位有排队消息的成员（每人本轮最多处理 `--limit` 条，默认 1）。`--parallel` 默认 3，最大 8。
- 返回 `results`（每项的状态、改动文件、检查结果、模型核对、回答摘要、结果路径）和 `next`。有失败、取消或错误时退出码为 1。
- `--detach` 在后台运行同样的推进并立即返回日志路径；用 `wait --timeout <秒>` 等它结束，期间可以随时 `status`。
- `dispatch` 等同 `advance --only messages`。
- 讨论轮数默认每组 12 次（含失败的轮次），用完后 `resume --additional-turns N` 追加，单组最多 100 次。每个任务默认最多 5 次尝试（组配置 `max_task_attempts`）。

## 验收、修订、fork、整合

- `show --task <id>`：完整回答、检查结果、实际调用的工具、指定/报告模型、工作区和 patch 路径。
- `accept --task <id> --note "<核验记录>"`（或 `--evidence <文件>`）`[--handoff <文件>]`。只接受 `awaiting_review` 的最新一次尝试。验收时脚本会确认交付文件、工作区和检查输入在执行后没有被改动；你自己修改的版本另存为新文件，不要改成员的工作区。交接包格式：

```json
{"summary": "供下游任务使用的已核实结论", "claims": [
  {"claim": "具体陈述", "source_url": "https://...", "evidence_level": "vendor_reported", "limitations": "仅为厂商声明"}],
 "limitations": ["未做运行时实测"]}
```

  `evidence_level` 可选 `vendor_reported`、`source_verified`、`independently_verified`、`inference`。省略 `--handoff` 时，下游只收到验收记录。下游任务不会收到原始回答。
- `revise --task <id> --feedback "..."`：下一次 `advance` 在同一会话、同一工作区里续做，新尝试单独存档。适用于 `awaiting_review`、`needs_revision`、`cancelled`，以及能续接的 `failed`（例如超时）。
- `fork --task <id> [--note "..."]`：用新会话、新工作区（最新快照加上已验收依赖）重新开始，`--note` 作为指导传给新会话。协议错误、范围违规、`interrupted`，或没有会话 ID 时用它。
- `fork --member <id> [--note "..."]`：解除成员的阻塞，下一条消息开启新会话；`--note` 作为前情摘要，不写时自动带上该成员最近几轮问答。无法核实结果的旧消息会标为 `abandoned`，不会重发。
- `integrate --task <id>`：把已验收 worker 任务的 patch 应用到项目工作区（不改暂存区、不提交）。已经应用过时返回 `already_present`；有冲突时报错，需要手动处理。

## 状态

| 对象 | 状态 |
|---|---|
| 任务 | `draft` → `ready` → `running` → `awaiting_review` / `needs_revision` / `failed` / `cancelled` / `interrupted` → `accepted` |
| 讨论轮次 | `dispatched` → `replied` / `failed` / `cancelled` / `unknown` / `abandoned` |
| 组 | `active`、`pausing`（正在停止运行中的工作）、`paused` |
| 成员 | `blocked` 非空时不再派发消息给它，直到 `fork --member` |

一位成员失败只阻塞这位成员，组内其他成员照常工作。报告模型和指定模型不一致的回复记为失败，并阻塞该成员；任务则在 `model_verification` 中标出，由你核对是不是别名。CLI 没报告模型时为 `not_reported`，只能证明参数已经传入。`dispatched` 只表示已派发，没有已读回执。

## 工作区

- Claude 的 advisor / researcher 直接在项目目录中只读运行。Antigravity 的所有模式、所有 worker，以及依赖了 worker 任务的任务，都在独立 worktree 中运行。
- worktree 的基线是工作区**快照**：HEAD 加上未提交和未跟踪的文件（被 `.gitignore` 忽略的文件不包括在内）。生成快照用的是临时索引，不改用户的分支、暂存区或文件。不需要先 commit。
- 依赖的 worker 任务验收后，它的 patch 会自动应用到下游任务的 worktree；已经整合进项目的部分会自动跳过，冲突会报错。
- Antigravity 讨论成员的 worktree 每轮都跟到项目的最新快照，会话保持不变。
- 范围控制：Claude 由 CLI 工具白名单限制（researcher 额外开放 WebSearch / WebFetch）。Antigravity 沿用原生权限，靠任务指令加事后审计：越权调用工具或越范围改文件会标为 `scope_violation`，改动保留但不会合入。worktree 用于隔离协作，不是操作系统沙箱，只适用于可信的本地项目。基线里含符号链接或子模块时，隔离运行会被拒绝。

## 暂停、取消与恢复

- `pause`：停止新的派发，并取消正在运行的讨论和任务；全部停下后状态从 `pausing` 变为 `paused`。`resume` 只解除暂停，被取消的消息不会重发；被取消的任务用 `revise` 续做或 `fork` 重来。
- `cancel --task <id>`：只取消一个正在运行的任务。
- 控制进程意外退出后，`reconcile`（`advance`、`wait`、`resume` 也会自动执行）只收录已经保存的终止结果；没有结果的讨论轮次标为 `unknown` 并阻塞成员，没有结果的任务标为 `interrupted`。先确认没有残留的 CLI 进程，再用 `fork`。
- 运行中的执行器持有操作系统锁；进程退出时锁自动释放，所以不必手工删锁文件。

## 产物

`<库名>-runs/<组>/` 下：`members/<id>/turns/<轮次>/`（讨论）、`tasks/<id>/attempts/NNN/`（每次尝试）、`tasks/<id>/ws-NNN/`（worktree）、`supervisor/`（后台推进日志）。每次尝试保存 `prompt.txt`、`stdout.jsonl`、`stderr.log`、`events.jsonl`、`progress.json`、`result.json`、`checks.json`、`changes.patch`、`artifacts/`，验收后还有 `acceptance.json` 和 `handoff.json`。worktree 不会自动删除，确认不再需要后用 `git worktree remove` 清理。用量和费用是 CLI 的估算，不同尝试之间不累加，也不代表实际账单。
