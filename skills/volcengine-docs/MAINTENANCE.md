# 火山文档维护

本技能的 `scripts/` 自包含构建脚本，`generated/` 是完整可检索快照，`.cache/` 保存源 PDF、中间文本与构建清单。后两者不提交公开仓库。

从仓库入口运行：

```powershell
.\muran.ps1 docs import D:\Work\volcengine_doc_skill
.\muran.ps1 docs build --fetch
.\muran.ps1 docs build
.\muran.ps1 docs status
```

技能独立安装后可以直接运行 `python <技能目录>/scripts/build_all.py --fetch`。
`--convert` 重新提取缓存 PDF；`--only tos` 只重建一区，前提是已存在完整快照。

构建在独立临时目录完成：下载（启用 TLS 校验）→ pypdfium2 抽文本 → 按接口切分 → 生成索引 → 文件/覆盖范围/内容无损校验 → 写入哈希清单 → 替换本地快照。
PDF 提取还有中文字符抽样检查，低于 80% 时终止。下载、解析或校验失败均保留现有正文；替换目录失败时恢复原快照。

保留 pypdfium2 提取方式：原流程发现其他提取器可能丢失中文或打乱参数表顺序。表格仍需结合上下文阅读。

新增产品修改 `scripts/products.py` 的 `PRODUCTS`，并核对官方库中的源文档名称。文档变更不会由每日仓库更新任务触发。

官方来源：[TOS](https://docs.volcengine.com/docs/6349/)、[火山方舟](https://docs.volcengine.com/docs/82379/)、[AI MediaKit](https://docs.volcengine.com/docs/6448/)。这些官方材料的权利归原权利人，仓库许可不覆盖下载的文档正文。
