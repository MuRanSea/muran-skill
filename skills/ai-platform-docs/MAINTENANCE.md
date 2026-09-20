# 平台文档维护

本技能保留官方文档的本地快照：火山五个产品区使用 PDF；可灵和 MiniMax 使用官方 Markdown 导出。`generated/` 正文、`.cache/` 源资料与中间文件都不提交公开仓库。

## 日常操作

```powershell
.\muran.ps1 docs update
.\muran.ps1 docs status
.\muran.ps1 docs auto-update enable
.\muran.ps1 docs auto-update status
.\muran.ps1 docs auto-update disable
```

任务 `MuranSkill-DocsUpdate` 每天北京时间 09:30 检查来源，错过后补跑；需要当前用户登录。任务最长运行两小时，和仓库管理操作共享锁。失败原因记录到本机更新日志，下次按计划重试。

`docs update` 获取官方来源，变化时重建。`docs build` 使用缓存强制重建；`docs build --fetch` 先获取来源再强制重建。`docs import <旧火山项目目录>` 复用已有火山正文，并下载尚未缓存的另外两家文档。

独立安装技能后，从任意工作目录运行：

```powershell
uv run --locked --script "<技能目录>/scripts/build_all.py" --fetch --if-changed
```

uv 自动准备脚本声明的运行时与依赖。独立脚本的 `--convert` 可重新提取缓存 PDF；`--only tos` 只重建指定火山区并保留其他区，前提是已有完整快照。

## 来源与覆盖范围

- 火山：[TOS](https://docs.volcengine.com/docs/6349/)、[方舟](https://docs.volcengine.com/docs/82379/)、[AI MediaKit](https://docs.volcengine.com/docs/6448/)。PDF 文件名中的版本时间戳用于判断是否重新下载和提取，文档库 ID 和五个产品区由 `providers.json` 中的 `volcengine` 定义。
- 可灵：[中国区文档目录](https://klingai.com/document-api/llms.txt)，收录 API、鉴权、错误码、回调、快速接入和能力地图。中国区与国际区域名及功能可能不同；国际区开发须核对 [kling.ai 文档](https://kling.ai/document-api/llms.txt)。
- MiniMax：[中文文档目录](https://platform.minimax.cn/docs/llms.txt)，收录全部 API 参考、核心接入与模态指南、相关 FAQ。目录中旧域名的链接使用其当前官方目标域名读取；产品首页、订阅介绍和跳转后的解决方案站不作为 API 正文。

三家平台统一在 [providers.json](providers.json) 维护：火山使用 `volcengine-pdf` 类型，配置 `library_ids` 和 `products`；可灵与 MiniMax 使用 `markdown` 类型，配置目录、官方域名和必要入口。`scripts/products.py` 仅从该配置读取火山产品区，下载和构建共用同一份配置。新增 Markdown 平台可复用现有适配器，其他导出形式需要单独适配。页面中的相对在线链接以对应官方文档 URL 为基准解析，不能当作本地文件。

## 更新与恢复

每次在独立临时目录获取输入。Markdown 目录会重新发现新增、删除的页面；页面内容哈希、火山源文本及 PDF 版本、构建脚本和配置共同决定是否需要重建。无变化时保持原快照，最近一次检查时间看管理器状态；`snapshot.json` 记录的是已发布快照的构建时间与来源。

构建会检查火山源行覆盖、内容无损和 PDF 中文字符抽样，核对 Markdown 原文哈希及正文保留情况，再生成索引和快照哈希清单。全部平台通过后才替换 `generated/` 和源缓存；任一下载、校验或替换失败均保留上一份完整快照。来源格式变化会报告错误，需要维护者更新适配。

下载及生成的官方正文、索引和 PDF 的权利归各平台，仓库许可不覆盖这些内容。

## 依赖维护

修改脚本顶部依赖声明后运行 `uv lock --script "<技能目录>/scripts/build_all.py" --upgrade`，验证后提交脚本与 `.lock` 文件。同步维护根目录依赖约束及 `uv.lock`，日常命令使用锁定模式。

## 平台目录层级

总索引只列 `volcengine`、`kling`、`minimax` 三个平台。火山索引 `INDEX-volcengine.md` 下再进入五个产品分区；新版正文路径是 `generated/chapters/volcengine/<区>/`。旧快照仍可按其索引检索，成功完整重建后切换到新布局，`snapshot.json` 的 `layout_version: 2` 表示已使用嵌套目录。
