# muran-skill

个人技能库：在一处维护技能，Codex、Claude Code、Pi、OpenCode、Grok Build 共用同一份文件。

第一版面向 **Windows 当前用户**。包含 Matt Pocock 的 25 个正式技能（后续随正式发布清单更新）、`ai-platform-docs` 官方 API 文档快照，以及 `multi-harness` 本地 CLI 委派技能。技能来源与许可见 [NOTICE.md](NOTICE.md)。

## 技能包与选择

```text
skills/
├── matt/
│   ├── pack.json
│   ├── grill-me/SKILL.md
│   └── ...
├── multi-harness/
│   ├── pack.json
│   ├── SKILL.md
│   └── scripts/harness.py
└── ai-platform-docs/
    ├── pack.json
    ├── SKILL.md
    ├── scripts/
    └── generated/
```

终端运行 `install` 会显示编号菜单，可输入包名、多个编号或 `all`；回车取消。脚本或非交互环境必须传 `--packages`。选择记录在本机状态中，新增包不会自动安装；已安装包内新增技能会随 `sync` 生效。旧版安装按已有链接自动迁移，保留原先安装的技能；可随后按包卸载。

客户端发现目录保持扁平，技能名称必须跨包唯一。若一个包依赖另一个包内的技能，安装时会提示缺少依赖，不会擅自安装另一包；卸载也会检查依赖。Git 拉取仍同步整个源仓库，按包选择控制客户端安装及上游更新任务，不是 Git 稀疏下载。

每天 09:00 拉取本库，只对已安装的 Matt 包检查上游；09:30 文档任务仅在已安装文档包时运行。卸载文档包会关闭文档计划任务，再次需要时手动启用。其他包默认仅跟随本库 Git 更新。

新增包：建立 `skills/<包名>/pack.json`，填写如下配置，将各技能放入其直接子目录。无需改安装器；使用 `skills: ["."]` 可将包目录本身作为单一技能入口（如 ai-platform-docs）。

```json
{"schema_version":1,"name":"my-pack","description":"我的技能包","skills":["*"],"updater":"git"}
```

## 多 Harness 协作首版

`multi-harness` 从一句目标开始：`$multi-harness 帮我调研 Jev。` Codex 每轮只问一个关键选择，给出推荐，已有答案直接沿用；最后汇总目标、分工、具体模型和验收标准，等你确认后再调用本地 Claude Code 或 Antigravity CLI（agy）。JSON、文件范围、依赖和派发命令由 Codex 处理。见[对话式规划](skills/multi-harness/references/intake.md)。

你可以说“按推荐”“沿用上次团队”，也可以指定某个成员或模型。信息齐全时直接进入方案确认；明确说“先展示计划，然后执行”或“直接执行，不用再问”则按该要求推进。执行后由 Codex 验收前序结果、处理必要修订并整合产物。

支持实时进度、取消、退回和显式会话续接；每轮文件快照独立保存。写作可配置汉字数、引用 URL 等自动检查，后续任务仅接收 Codex 核验后的交接材料。当前按轮次启动 CLI 并 resume，不是常驻消息服务。

还可在当前 Codex 对话中使用持久协作组：`$multi-harness 开一个研究组。` Codex 同样逐步帮你确定团队；开组后直接说“让研究员解释依据”“现在怎么样”“暂停这个组”“继续 Jev 那组”，不重新访谈。成员使用明确的 CLI/模型和独立讨论会话，消息按需排队派发；文件执行任务继续走原计划与验收。首次由 Codex 根据本机已核验模型保存团队配置，无需用户手填 JSON。见[协作组操作](skills/multi-harness/references/groups.md)与[设计和验收范围](docs/multi-harness-groups.md)。

```powershell
.\muran.ps1 install --packages multi-harness
uv run --locked python skills/multi-harness/scripts/harness.py doctor
```

执行器要求 ready 计划和显式模型 ID；对话中的推荐不会变成省略模型或静默降级。worker 使用独立 worktree；`doctor` 与 `check-plan` 不调用模型，真实执行使用 CLI 现有账号。见 [设计与验收](docs/multi-harness-v1.md) 和 [计划与执行契约](skills/multi-harness/references/execution.md)。

## 安装

需要 Git、[uv](https://docs.astral.sh/uv/getting-started/installation/) 和 Windows PowerShell 5.1。运行环境与依赖由 uv 自动准备。先安装你需要使用的智能体；本工具只安装技能。部分 Matt 工作流另需 Git Bash、`gh` 等工具，在使用相应技能时按其要求准备。

首次安装 uv 后重新打开 PowerShell：

```powershell
winget install --id astral-sh.uv -e
```

```powershell
git clone https://github.com/MuRanSea/muran-skill.git
cd muran-skill
.\muran.ps1 install
.\muran.ps1 doctor
```

若 PowerShell 的本地执行策略阻止脚本，用单次进程参数运行：

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\muran.ps1 install
```

入口使用 `uv run --locked`，项目配置使用 uv 管理的运行时，首次运行自动下载所需运行时和锁定的依赖，以后复用本地缓存。`pyproject.toml` 声明依赖，`uv.lock` 固定版本；环境由 uv 管理，无需激活。可用 `MURAN_UV` 指定 `uv.exe` 的绝对路径。`CLAUDE_CONFIG_DIR` 会影响 Claude 技能目录。

可选：在维护文档的机器上配置独立文档更新：

```powershell
# 已有旧火山项目时导入；同时补齐尚未缓存的可灵和 MiniMax 文档
.\muran.ps1 docs import D:\Work\volcengine_doc_skill

# 可选：维护文档的机器刷新官方来源并上传；首次下载和提取 PDF 可能较慢
.\muran.ps1 docs update
.\muran.ps1 docs auto-update enable
.\muran.ps1 doctor
```

旧版管理器会拒绝含文档正文或分包目录的候选版本。已安装旧版的其他机器需在工作区干净时先执行一次 `git pull --ff-only origin main` 升级发布规则，之后恢复正常自动更新。

公开仓库包含技能入口、脚本、来源说明，以及 `generated/` 下构建好的正文、索引和快照清单。其他机器拉取即可检索，无需首次下载 PDF。`.cache/` 源资料、PDF 和中间文件仍不进 Git。

旧版 `volcengine-docs` 安装更新仓库后执行一次 `sync`：保留本地快照和缓存，迁移到新名称，并退役指向本库旧入口的链接及已复用别名。随后执行 `docs update` 和 `docs auto-update enable`，补齐平台文档并启用新任务。

## 常用命令

| 命令 | 行为 |
|---|---|
| `.\muran.ps1 list` | 列出技能包、技能数量和安装状态 |
| `.\muran.ps1 install` | 终端选择一个或多个包，再为已发现的客户端建立链接 |
| `.\muran.ps1 install --packages matt` | 只新增安装 Matt 包，保留已安装的其他包 |
| `.\muran.ps1 install --packages ai-platform-docs` | 只新增安装平台文档包 |
| `.\muran.ps1 install --packages all` | 明确选择安装全部现有包 |
| `.\muran.ps1 update --packages matt` | 只检查合并 Matt 上游，校验后提交推送 |
| `.\muran.ps1 update --packages ai-platform-docs` | 只刷新并发布平台文档快照 |
| `.\muran.ps1 uninstall --packages matt` | 只移除 Matt 包的受管链接，保留其他包 |
| `.\muran.ps1 install --packages matt --agents codex claude-code pi opencode grok` | 显式选择客户端，适合 PATH 未配置的机器 |
| `.\muran.ps1 sync` | 只同步已选择包的增删技能、修复缺失链接 |
| `.\muran.ps1 update` | 校验远端候选版本、快进本库 main，再同步链接 |
| `.\muran.ps1 doctor` | 检查格式、依赖、链接、文档哈希、任务及最近更新状态 |
| `.\muran.ps1 daily-update` | 拉取本库，仅在已安装 Matt 包时三方合并其正式技能，校验后自动提交推送 |
| `.\muran.ps1 auto-update enable` | 开启每天北京时间 09:00 的自动更新 |
| `.\muran.ps1 auto-update status` | 查看任务状态、执行结果和下次运行时间 |
| `.\muran.ps1 auto-update disable` | 关闭本工具的每日任务 |
| `.\muran.ps1 docs update` | 检查火山 PDF 和可灵/MiniMax Markdown；内容或构建脚本变化时重建 |
| `.\muran.ps1 docs build` | 使用缓存源资料强制重建全部平台文档 |
| `.\muran.ps1 docs build --fetch` | 拉取官方来源并强制重建 |
| `.\muran.ps1 docs status` | 检查本地文档快照完整性 |
| `.\muran.ps1 docs auto-update enable` | 开启每天北京时间 09:30 的文档检查与重建 |
| `.\muran.ps1 docs auto-update status` | 查看文档任务状态、执行结果和下次运行时间 |
| `.\muran.ps1 docs auto-update disable` | 关闭文档任务 |
| `.\muran.ps1 uninstall` | 关闭两类任务并删除本工具创建的链接，保留技能源文件和文档 |

命令输出 JSON，成功退出码为 0，错误或冲突为 1。`--quiet` 只输出失败；`--json` 可显式标注自动化用途。机器状态和滚动日志位于 `%LOCALAPPDATA%\muran-skill\`，不进入仓库。`operations.jsonl` 记录更新结果，`state.json` 保存最近一次文档检查，`docs-build.log` 保存最近成功运行的构建输出。

## 一处维护如何生效

智能体入口仍按技能名逐个建立链接：Matt 技能指向 `skills/matt/<技能名>`，文档技能指向 `skills/ai-platform-docs`。只为已选择的包建立链接：

| 客户端 | 当前用户的入口 |
|---|---|
| Codex、Pi、OpenCode | `~/.agents/skills/<技能名>` |
| Claude Code | `~/.claude/skills/<技能名>` |
| Grok Build | `~/.grok/skills/<技能名>` |

编辑已有技能后，下一次读取会得到同一份正文。新增、删除技能后运行 `sync`，或等待每日同步。客户端可能缓存技能列表：Pi 可执行 `/reload`，其他客户端可使用自身重载功能或启动新会话。

同名普通目录和指向其他来源的链接会保留并报告冲突。已存在、指向本库的链接可复用；不是本工具创建的链接不会在卸载时被删除。不要移动已安装的仓库；需要换目录时，先从旧目录卸载，再在新目录安装。

## 更新规则

任务名为 `MuranSkill-DailyUpdate`，每天北京时间 09:00 执行 `daily-update`，开启 `StartWhenAvailable`。任务使用当前用户交互登录身份，不保存密码；电脑关机或用户未登录时不会运行，错过后在下次可运行时补跑。后台窗口隐藏，并发运行会被锁阻止。

文档任务为 `MuranSkill-DocsUpdate`，每天北京时间 09:30 运行 `docs update`，同样支持错过补跑、隐藏运行和并发保护。火山以官方 PDF 导出版本判断是否重新提取；可灵和 MiniMax 每次读取官方目录与所收录页面，比较内容哈希。来源与构建脚本都未变化、现有快照完整时返回 `unchanged`。任一来源下载或校验失败，保留上一份完整快照并记录失败原因；下次按计划重试。

任务记录 `uv.exe` 的绝对路径，运行时按仓库锁文件准备环境。升级旧版安装或移动 uv 后，分别执行 `auto-update enable` 和 `docs auto-update enable` 更新两个任务；对应 `status` 的 `runtime_current` 表示入口是否已更新。

`update` 只拉取本库 `origin/main` 并同步链接。`daily-update` 在此基础上检查 Matt 官方仓库 HEAD，按正式插件发布清单导入新增、修改和删除的技能。以记录的旧上游版本、本库已提交版本、新上游版本做三方合并，保留本地兼容性适配；同处修改、删除已定制技能、名称冲突或校验失败均停止，保留已安装内容。

自动导入在独立临时 Git 克隆中完成，仅提交对应技能资源、Matt MIT 许可和 `sources.json`。校验技能、依赖、资源路径、脚本语法、公开文件排除规则与 uv 锁文件后，用当前 Git 用户身份提交并正常推送到本库 `origin/main`，然后拉取到本机、同步技能链接。没有上游变化不创建提交；使用当前用户的 Git 凭据，不保存额外令牌。推送失败下次重试，不强推。

本地分支不是 `main`、有未提交修改、与远程分叉时跳过；不会自动提交你的手动编辑，也不会自动 stash、reset 或解决冲突。推送期间远程出现新提交会拒绝推送。运行记录见本地管理状态中的 `last_upstream_update`；手动修改仍由你验证后提交。定时任务调用固定脚本，更新脚本后新逻辑即生效。

官方文档通过独立任务或手动 `docs update` 刷新，校验成功后自动提交并推送 `generated/` 正文、索引和快照清单；PDF、缓存与中间文件仍不上传。任务开始时要求 main 分支且工作区干净；推送失败保留待推送提交，下次重试；远程分叉停止，不强推。`docs build` 和 `docs import` 仅本地构建，手动构建后需要自行检查提交。平台来源和覆盖范围见 [文档维护说明](skills/ai-platform-docs/MAINTENANCE.md)。文档最近一次重建失败时，`doctor` 会报告失败，即使上一份快照仍可读取。

## 技能兼容性

- 通用正文共享。出现“Skill tool”时，使用当前智能体的原生加载方式；没有原生工具则读取同级对应技能的 `SKILL.md`。
- 上游显式调用技能保留 `disable-model-invocation: true`，并提供 Codex 的 `agents/openai.yaml` 等价策略。OpenCode 忽略该 frontmatter 字段，正文中的显式调用指引不等于运行时强制限制。
- 多智能体独立评审等流程依赖客户端能力；没有子智能体时按顺序完成并说明验证方式。
- Matt 工程技能有项目级约定。首次在某个项目使用，可主动调用 `setup-matt-pocock-skills` 配置问题跟踪与文档位置；安装器不会替你修改各项目的规则文件。
- 原生发现和权限规则参考：[Codex](https://learn.chatgpt.com/docs/build-skills)、[Claude Code](https://code.claude.com/docs/en/skills)、[Pi](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/skills.md)、[OpenCode](https://opencode.ai/docs/skills/)、[Grok Build](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/08-skills.md)。

## 开发与验证

```powershell
uv run --locked -m unittest discover -s tests -v
.\muran.ps1 doctor
git diff --check
```

测试使用独立临时用户目录和本地 Git 远端，验证目录联接、内容共享、增删、冲突、更新保护和文档回滚。文件校验不代表客户端已实际加载；客户端发现结果应通过各自原生接口单独验证。

主动升级依赖时运行 `uv lock --upgrade`，验证后将 `pyproject.toml` 与 `uv.lock` 一并提交。文档技能独立运行所需的脚本锁文件维护方式见其 [维护说明](skills/ai-platform-docs/MAINTENANCE.md)。日常命令和 CI 均使用锁定模式。

发布前会将官方示例中形似访问密钥、API Token、JWT 和私钥的值替换成占位符，再生成快照哈希。源文档仍保存在被忽略的缓存中；接口参数、说明与其余示例保持原内容。GitHub 拒绝密钥推送时停止发布，不绕过扫描。
