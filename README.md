# muran-skill

个人技能库：在一处维护技能，Codex、Claude Code、Pi、OpenCode、Grok Build 共用同一份文件。

第一版面向 **Windows 当前用户**。包含 Matt Pocock 的 25 个正式技能，以及火山引擎文档技能。技能来源与许可见 [NOTICE.md](NOTICE.md)。

## 安装

需要 Git、Python 3.12+ 和 Windows PowerShell 5.1。先安装你需要使用的智能体；本工具只安装技能。部分 Matt 工作流另需 Git Bash、`gh` 等工具，在使用相应技能时按其要求准备。

```powershell
git clone https://github.com/MuRanSea/muran-skill.git
cd muran-skill
python -m pip install -r requirements.txt
.\muran.ps1 install
.\muran.ps1 doctor
```

若 PowerShell 的本地执行策略阻止脚本，用单次进程参数运行：

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\muran.ps1 install
```

可以使用 `.venv`，入口会优先寻找 `.venv\Scripts\python.exe`；也可用环境变量 `MURAN_PYTHON` 指定解释器。`CLAUDE_CONFIG_DIR` 会影响 Claude 技能目录。

首次准备火山文档：

```powershell
# 已有旧项目时直接导入，原项目不会被修改
.\muran.ps1 docs import D:\Work\volcengine_doc_skill

# 新机器从官方 PDF 构建；会下载文档，耗时取决于网络和 CPU
.\muran.ps1 docs build --fetch
.\muran.ps1 doctor
```

公开仓库只包含入口、脚本和来源说明。`generated/` 正文与 `.cache/` 源资料都不进 Git；没有本地正文时，doctor 会报告火山技能尚未就绪，并给出构建命令。

## 常用命令

| 命令 | 行为 |
|---|---|
| `.\muran.ps1 install` | 检测已安装的五种智能体，建立或复用技能 Junction |
| `.\muran.ps1 install --agents codex claude-code pi opencode grok` | 显式选择客户端，适合 PATH 未配置的机器 |
| `.\muran.ps1 sync` | 补齐新增技能、修复缺失链接、清理已删除技能的受管链接 |
| `.\muran.ps1 update` | 校验远端候选版本、快进本库 main，再同步链接 |
| `.\muran.ps1 doctor` | 检查格式、依赖、链接、文档哈希、任务及最近更新状态 |
| `.\muran.ps1 auto-update enable` | 开启每天北京时间 09:00 的自动更新 |
| `.\muran.ps1 auto-update status` | 查看任务状态、执行结果和下次运行时间 |
| `.\muran.ps1 auto-update disable` | 关闭本工具的每日任务 |
| `.\muran.ps1 docs build` | 用缓存源文本重建火山文档 |
| `.\muran.ps1 docs build --fetch` | 主动拉取官方 PDF 并重建 |
| `.\muran.ps1 docs status` | 检查本地文档快照完整性 |
| `.\muran.ps1 uninstall` | 关闭任务并删除本工具创建的链接，保留技能源文件 |

命令输出 JSON，成功退出码为 0，错误或冲突为 1。`--quiet` 只输出失败；`--json` 可显式标注自动化用途。机器状态和滚动日志位于 `%LOCALAPPDATA%\muran-skill\`，不进入仓库。

## 一处维护如何生效

每个智能体的入口都链接到本库的 `skills/<技能名>`：

| 客户端 | 当前用户的入口 |
|---|---|
| Codex、Pi、OpenCode | `~/.agents/skills/<技能名>` |
| Claude Code | `~/.claude/skills/<技能名>` |
| Grok Build | `~/.grok/skills/<技能名>` |

编辑已有技能后，下一次读取会得到同一份正文。新增、删除技能后运行 `sync`，或等待每日同步。客户端可能缓存技能列表：Pi 可执行 `/reload`，其他客户端可使用自身重载功能或启动新会话。

同名普通目录和指向其他来源的链接会保留并报告冲突。已存在、指向本库的链接可复用；不是本工具创建的链接不会在卸载时被删除。不要移动已安装的仓库；需要换目录时，先从旧目录卸载，再在新目录安装。

## 更新规则

任务名为 `MuranSkill-DailyUpdate`，每天北京时间 09:00 执行，开启 `StartWhenAvailable`。任务使用当前用户交互登录身份，不保存密码；电脑关机或用户未登录时不会运行，错过后在下次可运行时补跑。后台窗口隐藏，并发运行会被锁阻止。

自动更新只跟随本库 `origin/main`。其他分支、未提交修改、分叉均跳过拉取并记录原因；断网或候选校验失败保留当前工作树。不会自动 stash、reset、合并冲突、提交或推送。可校验的本地技能仍会同步链接。

你在本库修改、验证后正常提交并推送即可供其他机器更新。Matt 上游的新版本需要维护者审阅并迁入，更新 `sources.json`；火山文档只有显式运行构建命令才刷新。

## 技能兼容性

- 通用正文共享。出现“Skill tool”时，使用当前智能体的原生加载方式；没有原生工具则读取同级对应技能的 `SKILL.md`。
- 上游显式调用技能保留 `disable-model-invocation: true`，并提供 Codex 的 `agents/openai.yaml` 等价策略。OpenCode 忽略该 frontmatter 字段，正文中的显式调用指引不等于运行时强制限制。
- 多智能体独立评审等流程依赖客户端能力；没有子智能体时按顺序完成并说明验证方式。
- Matt 工程技能有项目级约定。首次在某个项目使用，可主动调用 `setup-matt-pocock-skills` 配置问题跟踪与文档位置；安装器不会替你修改各项目的规则文件。
- 原生发现和权限规则参考：[Codex](https://learn.chatgpt.com/docs/build-skills)、[Claude Code](https://code.claude.com/docs/en/skills)、[Pi](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/skills.md)、[OpenCode](https://opencode.ai/docs/skills/)、[Grok Build](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/08-skills.md)。

## 开发与验证

```powershell
python -B -m unittest discover -s tests -v
.\muran.ps1 doctor
git diff --check
```

测试使用独立临时用户目录和本地 Git 远端，验证目录联接、内容共享、增删、冲突、更新保护和文档回滚。文件校验不代表客户端已实际加载；客户端发现结果应通过各自原生接口单独验证。
