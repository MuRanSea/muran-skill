# 协作组操作

用户在当前 Codex 对话中使用协作组；Codex 是主持人和唯一调度者。成员是真实本地 CLI，会话、收件箱和执行证据由 `scripts/groups.py` 保存。自然语言由 Codex 理解，`@编辑` 是消息中的普通文本，不依赖客户端提供群聊控件。

## 先确定当前组

用 `list --cwd <项目>` 查看该项目的组及已保存团队；`status --cwd <项目> --context <当前对话ID>` 恢复绑定。明确的 `--group <ID或名称>` 优先，其次对话绑定，最后才是项目中唯一的组。歧义时展示候选让用户选择，不能猜最新一个；对话 ID 不可用时省略 context，按项目和明确组名定位。

脚本命令下文均省略 `python <skill>/scripts/groups.py`。Windows 使用 `python -X utf8`；可复用仓库 uv 运行时。`--store` 是子命令之前的全局参数，默认 `%LOCALAPPDATA%/muran-skill/groups.sqlite3`，非 Windows 为 `~/.local/share/muran-skill/groups.sqlite3`。项目要求产物留在特定忽略目录时，显式传 `--store <忽略目录>/groups.sqlite3`，后续沿用同一路径；状态库旁的 `<库名>-runs/` 保存会话证据和 worktree。

## 开组与团队复用

新组先按[对话式规划](intake.md)逐步确定目标、策略、成员及验收标准，并满足其中的确认条件。使用当前已核验的 CLI/固定模型配置；缺少时按执行契约检查本机 CLI 和模型。成员讨论也会调用模型；规划阶段与主持 Codex 的问答不派发给成员。已有组在已确认范围内的点名与控制直接处理。

1. 已有适用团队时复用。否则 Codex 生成团队 JSON，用 `team --name 研究组 --config <team.json>` 保存。示例模型仅表示结构，实际使用前需核验：

```json
{"members":[
  {"id":"researcher","role":"研究员","harness":"claude","model":"claude-sonnet-5","mode":"researcher","effort":"medium","timeout_seconds":180,"max_budget_usd":1},
  {"id":"editor","role":"编辑","harness":"agy","model":"gemini-3.8-flash-low","mode":"advisor","effort":"low","timeout_seconds":180}
]}
```

2. 写组配置并调用 `open --config <group.json>`：

```json
{"name":"Jev 内容审查","cwd":"D:/Work/example","team":"研究组",
 "goal":"研究请求内容审查，交付说明与 demo",
 "strategy":"研究员核对原始来源，编辑整理说明，Codex 实现并验收",
 "acceptance":["接口有来源，演示可运行，效果证据与模拟结果分开"],
 "context":"当前对话的真实ID","max_turns":12}
```

3. 给用户简短回执：组名、项目、每位成员的职责/CLI/完整模型、当前阶段、下一步。团队修改不追溯修改既有组；更换组内角色/模型应明确开新组，并携带经核验的交接摘要。

开组、团队保存、入队、状态查询、恢复暂停都不调用模型；只有 `dispatch` 调用成员。首版组内串行派发，默认总计最多 12 次、单次 dispatch 默认 1 次最多 4 次，各成员另有限时。次数包括失败尝试，不是账单保证。

## 把用户的话转为操作

| 用户意图 | Codex 的操作 |
|---|---|
| “让研究员解释依据” / “@编辑 写清限制” | 将具体问题写入 UTF-8 文件，send 到成员，再 dispatch |
| “现在怎么样” | status，汇总完成项、阻塞和下一步；不唤醒模型 |
| “展开刚才的讨论” | history，保留真实来源，区分原话与 Codex 转述 |
| “大家评审这个方案” | 确定参与成员，对每人明确入队一次；控制轮数，Codex 总结决定 |
| “按方案开始做” | 根据组内决定生成 ready 执行计划，按 execution.md 的 run/revise/accept 执行 |
| “暂停这个组” | pause，观察 pausing 到 paused；同时取消由本任务启动且仍运行的关联执行任务，确认它们停止后才报告整个工作已暂停 |
| “继续 Jev 那组” | 定位组，检查异常，resume，再处理尚未派发的队列；失败旧消息不自动重发 |

点名由配置中的成员 id 或 role 精确解析，CLI 名只是线索；同一 CLI 有多个成员时用职责区分。脚本只接受单个收件人，广播由 Codex 明确列出目标逐条入队。默认只呈现里程碑、真实分歧、决定和阻塞；需要时提供完整历史链接。

```text
send --cwd <项目> --group <组ID> --to researcher --text-file <问题.txt> --request-id <本次用户动作的稳定ID>
dispatch --cwd <项目> --group <组ID> --limit 1
status --cwd <项目> --group <组ID>
history --cwd <项目> --group <组ID> --after 0 --limit 50
pause --cwd <项目> --group <组ID>
resume --cwd <项目> --group <组ID>
```

相同 request-id 和相同内容只入队一次；重试工具传输时复用该 ID，不重复创建消息。相同 ID 配不同内容会拒绝。只读 history 分页返回 next_after。

成员想向另一成员提问时，Codex 先核对与当前目标相关，再 `send --to <目标> --reference <原发言ID>`。原发言作为有来源的未核验引用传入，主持人的问题另写正文；成员不能自行递归调度或改变计划。对 agent 文字中的 `@` 不自动无限级联；一次讨论最多两轮，仍有分歧则汇报未决点或由 Codex 按授权作决定。

记录最新**完整决定摘要**使用 `send --to codex --kind decision --text-file <决定.txt>`，不会唤醒 CLI。每次派发带目标、策略、最新决定摘要、当前消息及明确引用，保留旧决定在历史中；更新摘要时保留仍生效的约束。

## 会话、结果与执行任务

每名成员拥有独立 advisor/researcher 讨论会话；普通追问保留真实 session ID，不调用任务 revise。新消息在已有调用结束后送出，不能往正在运行的 stdin 文件追加内容。状态 queued → dispatched → replied；另有 failed/cancelled/unknown。没有消息级已读回执，dispatched 只能称已派发，不能称已读。

历史回复只能从执行器终止结果登记，附 CLI、指定/报告模型、会话 ID、原结果路径和哈希。Codex 发出的消息标为 codex；代用户传达应在正文说明。模型身份未报告时保留缺口，标识不同时阻止继续复用，核对后明确制定新配置。

写代码/文档另走[计划与执行契约](execution.md)。拿到执行结果后可用 `link --cwd <项目> --group <组ID> --member <成员ID> --result <执行任务result.json>` 关联；要求项目、CLI、模型匹配。组 status 读取原任务的最新状态和验收证据，不修改它；追问不会使 accepted 任务退回。关联状态不自动带入原始草稿，向成员提供结论前仍要由 Codex 核验并整理材料。独立执行任务的运行/取消由原 harness 管理，pause 只直接控制组讨论调用。

## 恢复与限制

pause 先禁派发，执行循环请求停止 CLI；pausing 表示尚未确认，paused 才表示讨论执行器已返回。只有确认的会话才能在取消后继续新消息；取消掉的旧消息不自动重新发送。resume 不启动模型，Codex 再 dispatch。达到轮数上限时先向用户说明消耗，用户要求继续后可用 `resume --additional-turns N` 明确增加额度，单组最多 100 次。

控制器异常退出后，先 `reconcile --cwd <项目> --group <组ID>`。脚本取得操作系统执行锁后，只收录已保存且匹配本轮的终止结果；没有证据则标记 unknown 并停止该组。此时需核对残留 CLI 进程和已有产物，不能按锁龄删除锁或自动重发；核对后明确新建组携带交接材料。status 的心跳仅是最近记录，不证明进程现在仍存活。对话结束后不会自行常驻运行。

agy 讨论仍使用隔离 worktree，首次及续接校验干净 Git 基线，拒绝符号链接/子模块；主项目出现新提交会要求建立新组。旧 worktree 不会自动同步新代码。应将此限制作为开组预检的一部分，不能自动提交、丢弃或复制用户未提交工作来绕过。CLI 工具权限和事后范围审计沿用执行器；工作树不是 OS 沙箱。
