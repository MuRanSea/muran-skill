# Matt 技能包

本目录收录 Matt Pocock 正式发布清单中的技能，每个子目录保留独立的 `SKILL.md`。`pack.json` 声明包入口；安装器只在用户选择本包后建立技能链接。

```powershell
.\muran.ps1 install --packages matt
.\muran.ps1 update --packages matt
.\muran.ps1 uninstall --packages matt
```

以上命令在仓库根目录运行。`update` 使用已记录的上游提交、本库版本和最新上游版本做三方合并，保留本地适配；冲突时停止。通过校验后仅提交本包技能、MIT 许可与来源记录。来源提交及文件清单见 [sources.json](../../sources.json)，许可见 [mattpocock-MIT.txt](../../licenses/mattpocock-MIT.txt)。

技能名称仍为 `grill-me`、`tdd` 等，智能体入口无需增加 `matt/` 前缀。同包技能之间继续按同级目录读取资源。
