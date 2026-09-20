---
name: volcengine-docs
description: 查询火山引擎官方文档的本地快照，涵盖 TOS 对象存储、火山方舟 API 与使用指南、AI MediaKit API 与使用指南。适用于接口参数、SDK、错误码、功能配置和开发流程。需要最新模型、价格、配额或时效信息时，结合快照日期核对官方在线文档。
---

# 火山引擎文档

文档正文保存在本技能目录的 `generated/`，由官方 PDF 构建，不随公开 Git 仓库分发。
所有相对路径都相对于本技能目录；读取技能入口后先确认 `generated/snapshot.json` 和 `generated/INDEX.md` 存在。

若正文尚未生成，说明本地快照不可用，并给出初始化命令：

```powershell
python "<本技能的实际目录>/scripts/build_all.py" --fetch
```

命令会下载官方 PDF 并构建本地语料。仅在用户要求初始化或更新时运行；普通检索不要自动下载或重建。
需要依赖时安装 `PyYAML` 和 `pypdfium2`。维护细节见 [MAINTENANCE.md](MAINTENANCE.md)。

## 检索

1. 选区：TOS → `tos`；方舟接口参数 → `ark`；方舟教程、模型与功能 → `ark-guide`；MediaKit 接口 → `mediakit`；MediaKit 使用指南 → `mediakit-guide`。不确定时读取 [总索引](generated/INDEX.md)。
2. 文件名就是章节标题，先按文件名查找 `generated/chapters/<区>/`，例如 `*Lifecycle*.md` 或 `*ListEndpoints*.md`；再用 `rg -n "关键词"` 搜正文。当前智能体没有 Glob 工具时使用文件搜索命令。
3. 读取命中的完整章节或相关段落。`INDEX-<区>.md` 是详细章节表，按关键词检索即可，无需整表加载。
4. 回答标明引用的章节路径；涉及时间敏感信息时说明本地快照时间，并核对官方在线来源。不要把构建时间当作官方文档发布时间。

## 文本格式

- 原 PDF 已按接口或任务切分；正文保留阅读顺序，标题多为普通文本行。
- 参数表按单元格分行，阅读时连同上下文；不要只依据单行判断参数归属。
- 示例代码可能没有 Markdown 围栏；超长接口会拆成“第 N 部分”，必要时一起读取。
- 产品区、章节数、构建时间以生成索引和 `snapshot.json` 为准，不假设固定数量。
