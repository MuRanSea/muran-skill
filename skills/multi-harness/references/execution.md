# 计划与执行契约

脚本只使用 Python 标准库，需要 Python 3.12+ 和 Git。命令中的 `<skill>` 是本技能的绝对目录；从当前项目调用时可用 `uv run --project <muran-skill 仓库> --locked python <skill>/scripts/harness.py ...`，已有 Python 时直接运行。

```text
python <skill>/scripts/harness.py doctor
python <skill>/scripts/harness.py doctor --harness agy
python <skill>/scripts/harness.py check-plan --plan <plan.json 的绝对路径>
python <skill>/scripts/harness.py run --plan <plan.json> --task-id inspect
python <skill>/scripts/harness.py status --run-dir <运行根目录>
python <skill>/scripts/harness.py reject --plan <plan.json> --task-id inspect --result <result.json> --feedback <feedback.md>
python <skill>/scripts/harness.py revise --plan <plan.json> --task-id inspect --result <result.json> --feedback <feedback.md>
python <skill>/scripts/harness.py accept --plan <plan.json> --task-id inspect --result <最新 result.json> --evidence <verification.md> --handoff <handoff.json>
python <skill>/scripts/harness.py run --plan <plan.json> --task-id implement --dependency-result <inspect 的 result.json>
python <skill>/scripts/harness.py cancel --run-dir <运行根目录>
```

`doctor` 只检查程序、版本和必要参数，不发送模型请求，也不检查登录凭据。Windows 自动解析 npm 的标准启动 shim，直接启动 Node 或原生可执行文件；不通过 shell 拼接 prompt。

## 先计划，后派发

新任务先完成[对话式规划](intake.md)。Codex 展示供用户确认的简短方案，完整技术任务表保存到本地忽略目录，用户需要时再展开。计划的 `goal`、`strategy`、整体验收标准与每项任务分工都须齐全。CLI / 模型组合按任务确定，不能把某个 CLI 永久等同于某种角色。未委派的验证与整合由 Codex 执行。

以下为完整的两步计划结构。替换 `cwd`、任务文件及目标，执行前重新核对模型可用性；示例模型 ID 来自本机 2026-09-22 验证，不是永久默认值。

```json
{
  "schema_version": 1,
  "plan_id": "normalize-v1",
  "state": "draft",
  "goal": "修复标签归一化中的空值和重复项问题",
  "strategy": "先阅读实现和测试确认规则，Codex 核对分析后委派限定文件的实现，最后运行完整测试。",
  "cwd": "D:/Work/example",
  "acceptance": ["空值过滤、稳定去重和现有行为全部通过测试", "源仓库仅包含验收过的修改"],
  "tasks": [
    {
      "id": "inspect",
      "depends_on": [],
      "rationale": "用已核实可用的 Antigravity 模型完成一次小范围源码分析，为实现提供反例。",
      "task": {
        "harness": "agy",
        "model": "gemini-3.8-flash-high",
        "mode": "advisor",
        "objective": "阅读实现和测试，指出空值与重复项的具体反例。",
        "files": ["tag_utils.py", "tests/test_tags.py"],
        "constraints": ["只报告有文件证据的问题，输出限三行"],
        "acceptance": ["Codex 对照代码和现有测试确认反例"],
        "timeout_seconds": 180
      }
    },
    {
      "id": "implement",
      "depends_on": ["inspect"],
      "rationale": "用本机已经验证可执行代码修改的 Claude 模型实现小范围补丁，并保留独立 worktree。",
      "task": {
        "harness": "claude",
        "model": "claude-sonnet-5",
        "mode": "worker",
        "objective": "根据验收后的分析修复空值过滤和稳定去重，保留现有接口。",
        "files": ["tag_utils.py", "tests/test_tags.py"],
        "allowed_paths": ["tag_utils.py"],
        "acceptance": ["Codex 运行现有测试全部通过", "diff 仅包含目标文件且无空白错误"],
        "timeout_seconds": 180,
        "max_budget_usd": 1
      }
    }
  ]
}
```

- `plan_id`、任务 `id`：最长 64 字符的字母、数字、连字符或下划线标识，首字符为字母/数字；任务 ID 唯一。
- `state`：`draft` 或 `ready`。`check-plan` 校验完整性、模型与依赖图，不调用 CLI，也不将草稿自动变为 ready。计划齐全且满足对话式规划的确认条件后，Codex 才定稿为 ready；未确认、仅设计或明确待审时保留 draft。运行器不独立判定用户是否已确认。
- `depends_on`：前置任务 ID 列表，无依赖用 `[]`；拒绝循环、自依赖和未知 ID。`rationale` 说明选用该 CLI / 模型的理由。
- `run` 只派发计划中的一个任务，不自动遍历整份计划。旧的 `run --task` 已移除；不能在派发命令中临时覆盖模型。
- 前置任务每个提供一次 `--dependency-result`，且必须是该运行最新一轮并有 Codex 的 `acceptance.json`。仅将主 agent 核验过的 `handoff.json`、结果指纹和交付文件哈希注入下游，不再自动注入原始回答。
- `accept` 用 `--evidence` 读取 Codex 验证记录（命令、实际结果、文件证据和未解决限制）。该命令仅记录已经进行的核验，不运行测试，也不是让用户额外审批。失败结果、空证据和子 agent 自验收均拒绝。
- 计划和结果通过 SHA-256 绑定；改动计划会让旧结果不再适用于该计划的后续派发。修订时由 Codex 重新核对受影响工作，不自动切换或重试。
- worker 的已验收修改需出现在计划 `cwd` 才能派发依赖它的任务；执行器按验收时文件哈希检查，且隔离运行仍要求干净 HEAD。首版适合“咨询 → 实现”与独立实现任务；代码串行依赖由 Codex 先整合或准备合适基线，不能仅传一段文字就声称已传递代码。

## 每项任务

`task` 沿用以下字段，`schema_version` 和 `cwd` 从计划继承；所有任务属于同一源项目。

- `harness`：`claude` 或 `agy`；`mode`：`advisor`、`researcher` 或 `worker`。researcher 目前仅支持 Claude，增加 WebSearch/WebFetch，不开放编辑、shell 或嵌套 agent；网页内容属于待核对的资料。写作任务用 worker 并指定报告文件 allowed_paths。
- `cwd`：存在的绝对目录。worker 和 Antigravity advisor 必须是有 HEAD 的干净 Git 仓库根目录，首版拒绝包含 Git 符号链接或子模块的基线。
- `objective`、`acceptance`：必填目标和非空验收标准列表；`context`、`files`、`constraints` 可选。Codex 应显式传递相关项目规则；Claude 的 safe mode 不自动加载 CLAUDE.md。
- `files`：相对 `cwd` 的上下文路径。工具可以探索其他相关项目文件；这不是读取权限白名单。
- worker 额外要求 `allowed_paths`：允许变更的**精确相对文件名**列表，例如 `["src/normalize.py", "tests/test_normalize.py"]`。不支持目录前缀和 glob。超范围变更会保留但标为 `scope_violation`，不会自动恢复。
- `model`：必填具体模型 ID，始终以 `--model <ID>` 传给对应 CLI。拒绝省略、空值、auto、default、占位符和空白字符。Antigravity 用 `agy models` 查询当前清单；Claude 使用用户提供或已经通过本机调用核实的模型 ID。认证或模型不可用时停止该任务，报告后由 Codex 调整计划。
- `timeout_seconds`：默认 180，范围 1–3600 秒。到期停止子进程树，保留已有结果。
- `max_budget_usd`：仅 Claude 可用，默认 1 美元的 CLI 估算上限；Antigravity 不提供这个字段。CLI 估算和墙钟上限都不是提供商账单保证。
- 不接受任意 CLI flags 或命令字符串。prompt 通过 UTF-8 stdin 传递，环境凭据由原 CLI 自行使用，不读取或复制凭据文件。
- `profile`：默认与模式一致，worker 默认为 coder；文档写作设置 writer，其提示只要求按核验材料成文。`response_format` 默认为 report，writer 默认为 paths（成功仅返回修改路径，正文在文件中；遇阻必须如实说明）。paths 仅供 worker 使用。
- `effort`：可省略；Claude 接受 low/medium/high/xhigh/max，agy 接受 low/medium/high，显式传给 CLI。agy 的 `gemini-3.8-flash-high` 等带档位模型不能配 low effort；执行器在调用前拒绝冲突，不能静默换模型。选择实际可用组合仍由 Codex 负责。
- `checks`：可选确定性检查数组；失败进入 needs_revision 并阻止验收。它们不会替代事实、文风或代码行为的核验。示例：

```json
[
  {"type": "exists", "path": "report.md"},
  {"type": "cjk_count", "path": "report.md", "min": 1800, "max": 2500},
  {"type": "urls", "path": "report.md", "min": 4},
  {"type": "contains", "path": "report.md", "text": "证据限制"},
  {"type": "excludes", "path": "report.md", "text": "待补充"}
]
```

`cjk_count` 按**整个文件**统计汉字，包括标题与参考文献，不是正文词数；在计划中给出一致口径。`urls` 统计去重后的 HTTP(S) URL 字符串并列出清单，不检查链接可达性或内容是否支持结论。检查文件哈希同时保存，accept 时重新核对检查输入与结果。

## 退回、续接与交接

`run` 启动一项任务的第一轮；`revise` 保留 run ID、task ID、显式模型、工作区和 CLI session ID，创建 `attempts/002/` 等新轮次，只发送具体反馈、原目标、范围和检查要求。Claude 用 `--resume <session_id>`，agy 用 `--conversation <conversation_id>`，不使用按目录选“最近会话”的 `--continue`。两者都每轮启动一个进程，结束后退出；会话由 CLI 持久化，没有常驻代理或执行中注入消息。原始上下文仍由 CLI 保存，续接并不保证免除上下文 token 费用。

`reject` 只登记 needs_revision 与反馈，不调用模型。`revise` 自带退回记录，无须先执行 reject。必须指定当前最新 result；已验收、正在运行、已被新轮次取代的结果不能续改。会话缺失、模型恢复失败或会话 ID 不匹配会停止，不静默改为新会话；范围或协议违规需主 agent 调查并建立新运行，不允许以错误返回的另一会话 ID 继续修订。已保存的任务也须匹配计划和原始指纹，不能通过修改 task.json 偷换模型、范围或检查要求。`operation.lock` 防止同一个运行被并发修订或验收，进程异常终止留下锁时需人工确认该 PID 已停止，再删除指定锁文件。

每轮 `result.json`、日志、回答、patch、检查与文件快照独立保留；新版结果不会覆盖旧版。验收会核对快照与当前交付内容，禁止把主 agent 后续编辑误记为子 agent 原稿。Codex 自己编辑的最终稿应另存并明确记录归属；需要子 agent 修订时保持原工作区、发送反馈即可。

交接材料由 Codex 核验后填写，不让子 agent 自行把未核验断言标为事实。`accept --handoff` 接收以下 JSON，存入本轮目录并用 SHA-256 绑定验收；没有 --handoff 时仅使用 --evidence 正文作为 summary。原始回答仍在 response.md 中供 Codex 审阅，不自动进入下游提示。

```json
{
  "summary": "供下一任务使用的精简结论，已移除错误或冲突草稿。",
  "claims": [
    {
      "claim": "原始来源支持的具体陈述",
      "source_url": "https://example.com/primary-source",
      "evidence_level": "vendor_reported",
      "limitations": "仅为厂商声明，未做独立性能实测"
    }
  ],
  "limitations": ["未开展运行时基准测试"]
}
```

证据等级可选 vendor_reported、source_verified、independently_verified、inference；source_verified 表示原文核对，不等于独立验证厂商结论。summary 上限 12000 字符，最多 100 条 claims，总交接包上限 40000 字符。大段原文不要塞进交接包；相关项目内资料可通过计划 files 指定。

## 运行结果与工作区

默认保存到 `<cwd>/.cache/harness-runs/<随机运行 ID>/`，可用 `--output-root` 指定其他本地目录。运行数据可能包含项目内容，保持在 Git 忽略目录内；新增项目需由主 agent 确认忽略规则。

| 产物 | 用途 |
|---|---|
| `plan.json` | 归一化后的完整计划快照；结果包含计划指纹和任务 ID |
| `task.json` / `prompt.txt` | 实际任务与输入，便于复现 |
| `input.jsonl` | Antigravity 的单条 NDJSON 输入 |
| `run.json` | 运行 ID、版本、工作流状态、轮次与最新结果路径 |
| `progress.json` / `events.jsonl` | 每秒心跳、最近事件、会话 ID、工具状态，以及去掉原始内容的顺序事件摘要 |
| `stdout.jsonl` / `stderr.log` | 原始 CLI 事件和诊断，按需读取 |
| `result.json` | 统一结果、最终回答、模型/用量（有报告时）、工具调用次数、错误与文件范围检查 |
| `acceptance.json` | Codex 验证证据、结果指纹和已验收文件哈希；验收命令成功后创建 |
| `review.json` / `feedback.json` | 主 agent 退回原因，以及下一轮使用的反馈和前轮指纹 |
| `handoff.json` | 主 agent 整理的事实、来源、证据等级和限制 |
| `checks.json` | 自动检查实测值、文件哈希、通过/失败与 URL 清单 |
| `artifacts/` / `response.md` | 本轮交付文件副本与回答；原文件删除在 artifacts 映射中记录为 null |
| `attempts/002/` 等 | 后续轮次的完整证据；第一轮保留在运行根目录 |
| `changes.patch` | worker 的已跟踪及新文件修改；支持二进制差异 |
| `worktree/` | worker 及 Antigravity advisor 的独立 detached worktree，保留供主 agent 验证 |

`result.json.status` 为执行结果：`completed`、`failed`、`protocol_error`、`timed_out`、`cancelled`、`output_limit` 或 `scope_violation`。CLI 退出码、有效终止事件和最终回答一起决定完成状态。`run.json.status` 是当前工作流状态：preparing → running → awaiting_review / needs_revision / failed → accepted；CLI completed 但自动检查失败时进入 needs_revision。原始 `result.json.acceptance` 保持 pending，验收另存 acceptance.json。

`requested_model` 是计划明确指定且传给 CLI 的 ID；`model` 仅记录 CLI 事件报告的实际标识，未报告为 null。`model_verification` 为 `matching`、`different_identifier` 或 `not_reported`；标识不同可能涉及别名映射，需 Codex 核对，不能直接认定切错模型。CLI 不报告模型时只能证明参数已指定，不能宣称提供商实际模型已核实。

单次日志上限 16 MiB；超限终止，原始文件可能包含越过阈值的最后一个写入块，不能当作完整运行。执行中持续消费 stdout 完整行，落盘 events.jsonl；status 返回心跳与最近事件，无须读取整个 token 流。心跳只代表监督进程存活，last_activity_at 才代表 CLI 最近发出事件；不能据心跳认定模型在推进。cancel 写入当前轮次的取消请求，执行器读取后结束进程树并保留日志，返回 cancellation_requested 不等于已经退出，应再查看 status。

`usage` 与 `cost_usd` 保留 CLI 原始报告；usage_scope 明确为 cli_reported_aggregation_unverified，usage_delta 与 cost_delta_usd 均为 null，不跨轮次自动汇总。真实 Claude 2.1.274 的续接报告会重置部分用量/费用，不能直接套用常驻流的累计计数语义。Antigravity 未报告金额时保持 null。CLI 估算不是提供商账单。

隔离运行不自动复制未提交改动、不初始化子模块、不安装依赖。文件任务限定读取、搜索、编辑、写入工具；Claude researcher 额外开放公开网页查询与读取。执行测试与应用修改由主 agent 完成。Claude 通过 CLI 限制可用工具；Antigravity 沿用用户原生权限，通过 prompt 和事后事件审计限制任务范围，尚无执行前工具拦截。`tool_scope_control` 分别为 `cli_allowlist` / `prompt_and_audit`。文件范围是 prompt 约束加事后核查，文件工具本身不是路径沙箱。首版不支持不可信仓库或不可信 agent 的隔离执行。

调研结果的 `observed_tools` 记录实际调用名，须结合原始工具返回核实是否真正获取到材料。WebFetch/WebSearch 均失败时不能验收为完成调研，也不能静默由主 agent 代做后声称是子 agent 的成果。Codex 可提供公开原文快照或修订计划，但应记录分工变化。

脚本正常结束或超时会回收所启动的进程；如果主 agent 强制结束了整个 Python 宿主，应人工核对残留进程。worktree 不自动删除；确认产物已整合或不再需要后，由主 agent 使用 Git 的 worktree remove 清理指定目录。

## 已核对接口

首版开发环境：Windows；Claude Code 2.1.274；Antigravity CLI 1.2.7。每次实际运行仍重新探测版本和 flags。

- Claude：`-p --output-format stream-json --verbose`，以 `result` 事件的 subtype 和 is_error 判断；`--safe-mode` 保留登录和模型配置，禁用定制资源。使用工具白名单和无交互权限模式。
- Antigravity：`--input-format stream-json --output-format stream-json`，发送一条 user 事件后关闭 stdin；以最终 `result.status == SUCCESS`、非空回答及退出码共同判断。`WAITING`、`RUNNING` 或缺少结果均不算成功。工具调用按 step_index 去重。
- Antigravity 自定义 agent 白名单在 1.2.7 实测中未收窄模型工具，因此首版不依赖该配置。咨询/执行都在独立 worktree 运行；任务包提供绝对 `project_root`。worker 使用 `accept-edits`，不使用跳过全部权限的参数；原生权限仍可能要求交互，此时任务失败并保留日志。
- 对 Antigravity 实际工具事件逐项审计：允许文件读取、搜索、`finish`，worker 额外允许文件修改；命令、嵌套 agent、外部工具及未知工具标记 `scope_violation`。这只能发现已发生的调用，不能回滚其副作用。
- CLI 自身的会话记录遵循原产品行为。模型未通过事件报告时，结果 `model` 为 null，不猜测模型名称。
- 本次版本新增任务归一化字段；此前历史结果与报告保留作证据，不自动迁移旧计划指纹/验收，也不能给先前禁用持久化的 Claude 运行补造 session。需要继续旧工作时，由 Codex 明确准备新计划和已核验材料。
- 参考：[Claude 非交互接口](https://code.claude.com/docs/en/headless)、[Antigravity 非交互协议](https://antigravity.google/docs/cli/headless/)、[自定义 agent](https://antigravity.google/docs/subagents?tab=cli)。
