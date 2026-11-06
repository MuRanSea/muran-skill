# 方舟指南区章节表（ark-guide）

来源：《火山方舟 文档指南》（2433 页）。178 个章节文件，接口级切分：一个接口/任务一个文件；超过 1500 行的按语义块自动再拆为`… - 第N部分`（11 个章节被拆分）。

「页码」是原 PDF 页码范围；「行范围」是中间 MD（`doc/<源文档>.md`）的 1 起始行号，可据此回查原文。章节文件本身已去掉页眉页脚，回查 PDF 时用这两列。文件名即章节标题，日常定位直接 Glob 文件名即可，用不到这两列。

**这张表用来 grep，不要整读。**

| 编号 | 标题 | 页码 | 行范围(源文件) | 行数 | 文件 |
|------|------|------|---------------|------|------|
| 1.1 | 产品简介 | 1-5 | 243-399 | 147 | `chapters/volcengine/ark-guide/1.1 产品简介.md` |
| 1.2 | 快速入门 | 6-30 | 400-1352 | 836 | `chapters/volcengine/ark-guide/1.2 快速入门.md` |
| 1.3 | 模型价格 | 31-54 | 1353-2797 | 1297 | `chapters/volcengine/ark-guide/1.3 模型价格.md` |
| 1.4 | Agent 场景模型调用的正确姿势 | 55-65 | 2798-3367 | 495 | `chapters/volcengine/ark-guide/1.4 Agent 场景模型调用的正确姿势.md` |
| 1.5 | 迁移到方舟官方 SDK | 66-68 | 3368-3472 | 64 | `chapters/volcengine/ark-guide/1.5 迁移到方舟官方 SDK.md` |
| 2.1 | 模型列表 - 第1部分 | 69-91 | 3473-5086 | 1558 | `chapters/volcengine/ark-guide/2.1 模型列表 - 第1部分.md` |
| 2.1 | 模型列表 - 第2部分 | 92-98 | 5087-5661 | 461 | `chapters/volcengine/ark-guide/2.1 模型列表 - 第2部分.md` |
| 2.2 | Seed-Evolving | 99-103 | 5662-5838 | 130 | `chapters/volcengine/ark-guide/2.2 Seed-Evolving.md` |
| 2.3 | DeepSeek-V4.1-Flash（升级 1017） | 104-115 | 5839-6430 | 504 | `chapters/volcengine/ark-guide/2.3 DeepSeek-V4.1-Flash（升级 1017）.md` |
| 3.1 | 文本生成 | 116-129 | 6432-6991 | 474 | `chapters/volcengine/ark-guide/3.1 文本生成.md` |
| 3.2.1 | 图片理解 - 第1部分 | 130-168 | 6992-8623 | 1426 | `chapters/volcengine/ark-guide/3.2.1 图片理解 - 第1部分.md` |
| 3.2.1 | 图片理解 - 第2部分·代码示例 | 169-194 | 8624-9676 | 902 | `chapters/volcengine/ark-guide/3.2.1 图片理解 - 第2部分·代码示例.md` |
| 3.2.2 | 视频理解 - 第1部分 | 195-235 | 9677-11368 | 1494 | `chapters/volcengine/ark-guide/3.2.2 视频理解 - 第1部分.md` |
| 3.2.2 | 视频理解 - 第2部分 | 236-248 | 11369-11919 | 484 | `chapters/volcengine/ark-guide/3.2.2 视频理解 - 第2部分.md` |
| 3.2.3 | 文档理解 | 249-277 | 11920-13106 | 1051 | `chapters/volcengine/ark-guide/3.2.3 文档理解.md` |
| 3.2.4 | 音频理解 - 第1部分 | 278-331 | 13107-15323 | 1903 | `chapters/volcengine/ark-guide/3.2.4 音频理解 - 第1部分.md` |
| 3.3.1 | Doubao Seedance 2.5 教程 - 第1部分 | 332-373 | 15324-17119 | 1494 | `chapters/volcengine/ark-guide/3.3.1 Doubao Seedance 2.5 教程 - 第1部分.md` |
| 3.3.1 | Doubao Seedance 2.5 教程 - 第2部分 | 374-414 | 17120-18843 | 1384 | `chapters/volcengine/ark-guide/3.3.1 Doubao Seedance 2.5 教程 - 第2部分.md` |
| 3.3.2 | Doubao Seedance 2.5 提示词指南 | 415-483 | 18844-20429 | 939 | `chapters/volcengine/ark-guide/3.3.2 Doubao Seedance 2.5 提示词指南.md` |
| 3.3.3 | Doubao Seedance 2.0 系列教程 - 第1部分 | 484-532 | 20430-22431 | 1738 | `chapters/volcengine/ark-guide/3.3.3 Doubao Seedance 2.0 系列教程 - 第1部分.md` |
| 3.3.4 | Doubao Seedance 2.0 系列提示词指南 | 533-582 | 22432-23229 | 512 | `chapters/volcengine/ark-guide/3.3.4 Doubao Seedance 2.0 系列提示词指南.md` |
| 3.3.5 | 视频生成教程 - 第1部分 | 583-622 | 23230-24910 | 1532 | `chapters/volcengine/ark-guide/3.3.5 视频生成教程 - 第1部分.md` |
| 3.3.5 | 视频生成教程 - 第2部分 | 623-642 | 24911-25696 | 644 | `chapters/volcengine/ark-guide/3.3.5 视频生成教程 - 第2部分.md` |
| 3.3.6 | Doubao Seedance 便利创作含肖像视频 | 643-661 | 25697-26439 | 652 | `chapters/volcengine/ark-guide/3.3.6 Doubao Seedance 便利创作含肖像视频.md` |
| 3.4.1 | Doubao Seedream 5.0 pro / flash 教程 | 662-692 | 26441-27563 | 939 | `chapters/volcengine/ark-guide/3.4.1 Doubao Seedream 5.0 pro - flash 教程.md` |
| 3.4.2 | Doubao Seedream 5.0 pro / flash 实现交互编辑指南 | 693-702 | 27564-27931 | 298 | `chapters/volcengine/ark-guide/3.4.2 Doubao Seedream 5.0 pro - flash 实现交互编辑指南.md` |
| 3.4.3 | 图片生成教程 - 第1部分 | 703-745 | 27932-29619 | 1482 | `chapters/volcengine/ark-guide/3.4.3 图片生成教程 - 第1部分.md` |
| 3.4.3 | 图片生成教程 - 第2部分 | 746-761 | 29620-30410 | 681 | `chapters/volcengine/ark-guide/3.4.3 图片生成教程 - 第2部分.md` |
| 3.5 | 决策评估（beta） | 762-772 | 30411-30881 | 404 | `chapters/volcengine/ark-guide/3.5 决策评估（beta）.md` |
| 3.6.1 | 3D 生成 | 773-782 | 30883-31294 | 350 | `chapters/volcengine/ark-guide/3.6.1 3D 生成.md` |
| 3.6.2 | 向量化 | 783-806 | 31295-32335 | 856 | `chapters/volcengine/ark-guide/3.6.2 向量化.md` |
| 3.7.1 | 工具概述 | 807-813 | 32337-32631 | 257 | `chapters/volcengine/ark-guide/3.7.1 工具概述.md` |
| 3.7.2 | 豆包助手 | 807-834 | 32632-33578 | 783 | `chapters/volcengine/ark-guide/3.7.2 豆包助手.md` |
| 3.7.3 | 联网搜索工具 | 835-853 | 33579-34372 | 656 | `chapters/volcengine/ark-guide/3.7.3 联网搜索工具.md` |
| 3.7.4 | Image Process（图像处理） | 854-880 | 34373-35372 | 906 | `chapters/volcengine/ark-guide/3.7.4 Image Process（图像处理）.md` |
| 3.7.5 | 私域知识库搜索 Knowledge Search | 881-886 | 35373-35560 | 146 | `chapters/volcengine/ark-guide/3.7.5 私域知识库搜索 Knowledge Search.md` |
| 3.7.6 | 云部署 MCP / Remote MCP | 887-903 | 35561-36208 | 580 | `chapters/volcengine/ark-guide/3.7.6 云部署 MCP - Remote MCP.md` |
| 3.7.7 | Function Calling（函数调用） - 第1部分 | 904-947 | 36209-38011 | 1567 | `chapters/volcengine/ark-guide/3.7.7 Function Calling（函数调用） - 第1部分.md` |
| 3.7.8 | Apply Patch（代码补丁工具） | 948-964 | 38012-38752 | 321 | `chapters/volcengine/ark-guide/3.7.8 Apply Patch（代码补丁工具）.md` |
| 3.8.1 | 深度思考 | 965-988 | 38754-39828 | 947 | `chapters/volcengine/ark-guide/3.8.1 深度思考.md` |
| 3.8.2 | 上下文管理 | 989-1020 | 39829-41187 | 1187 | `chapters/volcengine/ark-guide/3.8.2 上下文管理.md` |
| 3.8.3 | 流式输出 | 1021-1046 | 41188-42314 | 999 | `chapters/volcengine/ark-guide/3.8.3 流式输出.md` |
| 3.8.4 | 续写模式 | 1047-1055 | 42315-42739 | 379 | `chapters/volcengine/ark-guide/3.8.4 续写模式.md` |
| 3.8.5 | 上下文缓存 | 1056-1092 | 42740-44403 | 1407 | `chapters/volcengine/ark-guide/3.8.5 上下文缓存.md` |
| 3.8.6 | 文件输入(Files API) | 1093-1128 | 44404-45812 | 1270 | `chapters/volcengine/ark-guide/3.8.6 文件输入(Files API).md` |
| 3.8.7 | GUI Agent 能力 | 1129-1139 | 45813-46210 | 317 | `chapters/volcengine/ark-guide/3.8.7 GUI Agent 能力.md` |
| 3.8.8 | 视觉定位 Grounding | 1140-1146 | 46211-46454 | 223 | `chapters/volcengine/ark-guide/3.8.8 视觉定位 Grounding.md` |
| 3.8.9 | 提示词工程 | 1147-1151 | 46455-46672 | 152 | `chapters/volcengine/ark-guide/3.8.9 提示词工程.md` |
| 3.8.10 | 结构化输出(beta) | 1152-1174 | 46673-47590 | 818 | `chapters/volcengine/ark-guide/3.8.10 结构化输出(beta).md` |
| 3.9.1 | 迁移至 Responses API | 1175-1187 | 47592-48288 | 618 | `chapters/volcengine/ark-guide/3.9.1 迁移至 Responses API.md` |
| 3.9.2 | 文本生成 | 1188-1225 | 48289-49813 | 1330 | `chapters/volcengine/ark-guide/3.9.2 文本生成.md` |
| 3.9.3 | 深度思考 | 1226-1248 | 49814-50854 | 847 | `chapters/volcengine/ark-guide/3.9.3 深度思考.md` |
| 3.9.4 | 多模态理解 | 1249-1276 | 50855-52011 | 1039 | `chapters/volcengine/ark-guide/3.9.4 多模态理解.md` |
| 3.9.5 | 工具调用 | 1277-1288 | 52012-52530 | 458 | `chapters/volcengine/ark-guide/3.9.5 工具调用.md` |
| 3.9.6 | 结构化输出(beta) | 1289-1297 | 52531-52887 | 320 | `chapters/volcengine/ark-guide/3.9.6 结构化输出(beta).md` |
| 3.9.7 | 上下文编辑 | 1298-1303 | 52888-53137 | 218 | `chapters/volcengine/ark-guide/3.9.7 上下文编辑.md` |
| 3.10.1 | Codex | 1304-1312 | 53139-53357 | 165 | `chapters/volcengine/ark-guide/3.10.1 Codex.md` |
| 3.10.2 | Claude Code | 1313-1320 | 53358-53611 | 176 | `chapters/volcengine/ark-guide/3.10.2 Claude Code.md` |
| 3.10.3 | OpenCode | 1321-1324 | 53612-53751 | 106 | `chapters/volcengine/ark-guide/3.10.3 OpenCode.md` |
| 3.10.4 | OpenClaw | 1325-1330 | 53752-53948 | 155 | `chapters/volcengine/ark-guide/3.10.4 OpenClaw.md` |
| 3.10.5 | Hermes Agent | 1331-1334 | 53949-54065 | 84 | `chapters/volcengine/ark-guide/3.10.5 Hermes Agent.md` |
| 3.10.6 | TRAE | 1335-1337 | 54066-54119 | 30 | `chapters/volcengine/ark-guide/3.10.6 TRAE.md` |
| 3.10.7 | WorkBuddy | 1338-1342 | 54120-54209 | 60 | `chapters/volcengine/ark-guide/3.10.7 WorkBuddy.md` |
| 3.10.8 | ZCode | 1343-1347 | 54210-54376 | 132 | `chapters/volcengine/ark-guide/3.10.8 ZCode.md` |
| 3.10.9 | DeepSeek Harness | 1348-1353 | 54377-54534 | 90 | `chapters/volcengine/ark-guide/3.10.9 DeepSeek Harness.md` |
| 3.10.10 | Pi | 1354-1356 | 54535-54634 | 78 | `chapters/volcengine/ark-guide/3.10.10 Pi.md` |
| 3.10.11 | 其他工具 | 1357-1360 | 54635-54774 | 103 | `chapters/volcengine/ark-guide/3.10.11 其他工具.md` |
| 4.1 | 推理方式概述 | 1357-1365 | 54776-55420 | 574 | `chapters/volcengine/ark-guide/4.1 推理方式概述.md` |
| 4.2 | 在线推理（常规） | 1366-1367 | 55421-55483 | 43 | `chapters/volcengine/ark-guide/4.2 在线推理（常规）.md` |
| 4.3 | 在线推理（低延迟） | 1368-1373 | 55484-55686 | 117 | `chapters/volcengine/ark-guide/4.3 在线推理（低延迟）.md` |
| 4.4 | 在线推理（低优） | 1374-1381 | 55687-55980 | 183 | `chapters/volcengine/ark-guide/4.4 在线推理（低优）.md` |
| 4.5 | 在线推理（TPM 保障包） | 1382-1389 | 55981-56251 | 187 | `chapters/volcengine/ark-guide/4.5 在线推理（TPM 保障包）.md` |
| 4.6.1 | 模型单元概述 | 1390-1391 | 56253-56340 | 46 | `chapters/volcengine/ark-guide/4.6.1 模型单元概述.md` |
| 4.6.2 | 创建模型单元 | 1392-1394 | 56341-56444 | 62 | `chapters/volcengine/ark-guide/4.6.2 创建模型单元.md` |
| 4.6.3 | 管理模型单元 | 1395 | 56445-56475 | 17 | `chapters/volcengine/ark-guide/4.6.3 管理模型单元.md` |
| 4.7 | 批量推理 | 1396-1429 | 56476-57966 | 1224 | `chapters/volcengine/ark-guide/4.7 批量推理.md` |
| 4.8.1 | 智能模型路由 | 1430-1434 | 57968-58116 | 85 | `chapters/volcengine/ark-guide/4.8.1 智能模型路由.md` |
| 4.8.2 | 使用 MLP 推理服务 | 1435-1441 | 58117-58378 | 196 | `chapters/volcengine/ark-guide/4.8.2 使用 MLP 推理服务.md` |
| 4.8.3 | 使用自定义模型进行推理 | 1442-1444 | 58379-58512 | 75 | `chapters/volcengine/ark-guide/4.8.3 使用自定义模型进行推理.md` |
| 5.1.1 | 模型精调概述 | 1445-1450 | 58515-58893 | 322 | `chapters/volcengine/ark-guide/5.1.1 模型精调概述.md` |
| 5.1.2 | 有监督微调最佳实践 | 1451-1464 | 58894-59513 | 205 | `chapters/volcengine/ark-guide/5.1.2 有监督微调最佳实践.md` |
| 5.1.3 | 直接偏好优化最佳实践 | 1465-1474 | 59514-59946 | 291 | `chapters/volcengine/ark-guide/5.1.3 直接偏好优化最佳实践.md` |
| 5.1.4 | 强化学习最佳实践 | 1475-1502 | 59947-61045 | 865 | `chapters/volcengine/ark-guide/5.1.4 强化学习最佳实践.md` |
| 5.1.5 | Plugin 异常处理 | 1503-1505 | 61046-61187 | 99 | `chapters/volcengine/ark-guide/5.1.5 Plugin 异常处理.md` |
| 5.1.6 | 精调 SDK 使用指南 - 第1部分 | 1503-1553 | 61188-63245 | 1682 | `chapters/volcengine/ark-guide/5.1.6 精调 SDK 使用指南 - 第1部分.md` |
| 5.1.7.1 | 格式总览 | 1554-1555 | 63247-63300 | 38 | `chapters/volcengine/ark-guide/5.1.7.1 格式总览.md` |
| 5.1.7.2 | 语言及多模态理解模型精调数据格式 - 第1部分 | 1554-1602 | 63301-65562 | 1936 | `chapters/volcengine/ark-guide/5.1.7.2 语言及多模态理解模型精调数据格式 - 第1部分.md` |
| 5.1.7.2 | 语言及多模态理解模型精调数据格式 - 第2部分·注意事项 | 1603-1604 | 65563-65655 | 60 | `chapters/volcengine/ark-guide/5.1.7.2 语言及多模态理解模型精调数据格式 - 第2部分·注意事项.md` |
| 5.1.7.3 | 图片生成模型精调数据格式 | 1605-1612 | 65656-66006 | 293 | `chapters/volcengine/ark-guide/5.1.7.3 图片生成模型精调数据格式.md` |
| 5.1.7.4 | 视频生成模型精调数据格式 | 1613-1615 | 66007-66103 | 88 | `chapters/volcengine/ark-guide/5.1.7.4 视频生成模型精调数据格式.md` |
| 5.1.8 | 管理自定义模型 | 1616-1618 | 66104-66194 | 54 | `chapters/volcengine/ark-guide/5.1.8 管理自定义模型.md` |
| 5.2.1 | 创建模型评测任务 | 1619-1624 | 66196-66261 | 31 | `chapters/volcengine/ark-guide/5.2.1 创建模型评测任务.md` |
| 5.2.2 | 查看并管理模型评测任务 | 1625-1627 | 66262-66281 | 11 | `chapters/volcengine/ark-guide/5.2.2 查看并管理模型评测任务.md` |
| 5.2.3 | 评测数据集格式说明 | 1628-1644 | 66282-67185 | 833 | `chapters/volcengine/ark-guide/5.2.3 评测数据集格式说明.md` |
| 5.2.4.1 | 人工评测作业 | 1645-1654 | 67187-67240 | 28 | `chapters/volcengine/ark-guide/5.2.4.1 人工评测作业.md` |
| 5.2.4.2 | 查看评测报告 | 1655-1659 | 67241-67350 | 61 | `chapters/volcengine/ark-guide/5.2.4.2 查看评测报告.md` |
| 5.3.1 | 数据集介绍 | 1660-1665 | 67352-67462 | 74 | `chapters/volcengine/ark-guide/5.3.1 数据集介绍.md` |
| 5.3.2 | 共享数据集 | 1666-1671 | 67463-67509 | 24 | `chapters/volcengine/ark-guide/5.3.2 共享数据集.md` |
| 6.1.1 | 概述 | 1672-1675 | 67512-67673 | 117 | `chapters/volcengine/ark-guide/6.1.1 概述.md` |
| 6.1.2 | 快速入门（代码） | 1676-1691 | 67674-68330 | 596 | `chapters/volcengine/ark-guide/6.1.2 快速入门（代码）.md` |
| 6.1.3 | 快速入门（控制台） | 1692-1694 | 68331-68429 | 57 | `chapters/volcengine/ark-guide/6.1.3 快速入门（控制台）.md` |
| 6.2.1 | Agent | 1695-1701 | 68431-68696 | 213 | `chapters/volcengine/ark-guide/6.2.1 Agent.md` |
| 6.2.2 | Skills | 1702-1706 | 68697-68845 | 107 | `chapters/volcengine/ark-guide/6.2.2 Skills.md` |
| 6.2.3 | MCP | 1707-1710 | 68846-69000 | 127 | `chapters/volcengine/ark-guide/6.2.3 MCP.md` |
| 6.2.4 | Tools | 1711-1725 | 69001-69645 | 491 | `chapters/volcengine/ark-guide/6.2.4 Tools.md` |
| 6.2.5 | 工具权限策略 | 1726-1729 | 69646-69801 | 135 | `chapters/volcengine/ark-guide/6.2.5 工具权限策略.md` |
| 6.2.6 | 模型支持的参数列表 | 1730-1732 | 69802-69964 | 140 | `chapters/volcengine/ark-guide/6.2.6 模型支持的参数列表.md` |
| 6.3.1 | 配置云环境 | 1733-1739 | 69966-70245 | 217 | `chapters/volcengine/ark-guide/6.3.1 配置云环境.md` |
| 6.3.2 | 云沙箱参考 | 1740-1743 | 70246-70401 | 128 | `chapters/volcengine/ark-guide/6.3.2 云沙箱参考.md` |
| 6.3.3.1 | 自托管环境概述 | 1744-1748 | 70403-70618 | 126 | `chapters/volcengine/ark-guide/6.3.3.1 自托管环境概述.md` |
| 6.3.3.2 | 配置并运行自托管环境 | 1749-1763 | 70619-71203 | 476 | `chapters/volcengine/ark-guide/6.3.3.2 配置并运行自托管环境.md` |
| 6.3.3.3 | 自托管环境安全说明 | 1764-1770 | 71204-71498 | 186 | `chapters/volcengine/ark-guide/6.3.3.3 自托管环境安全说明.md` |
| 6.4.1 | 启动 Session | 1771-1785 | 71500-72125 | 509 | `chapters/volcengine/ark-guide/6.4.1 启动 Session.md` |
| 6.4.2 | 管理 Session | 1786-1792 | 72126-72404 | 205 | `chapters/volcengine/ark-guide/6.4.2 管理 Session.md` |
| 6.4.3 | Session 事件流 | 1793-1814 | 72405-73317 | 738 | `chapters/volcengine/ark-guide/6.4.3 Session 事件流.md` |
| 6.4.4 | 使用 Webhook 接收事件通知 | 1815-1827 | 73318-73832 | 387 | `chapters/volcengine/ark-guide/6.4.4 使用 Webhook 接收事件通知.md` |
| 6.4.5 | 使用 Vaults 认证 | 1828-1835 | 73833-74177 | 246 | `chapters/volcengine/ark-guide/6.4.5 使用 Vaults 认证.md` |
| 6.4.6 | 运行和管理后台工具任务 | 1836-1841 | 74178-74407 | 155 | `chapters/volcengine/ark-guide/6.4.6 运行和管理后台工具任务.md` |
| 6.5.1 | 上传与挂载文件 | 1842-1848 | 74409-74652 | 189 | `chapters/volcengine/ark-guide/6.5.1 上传与挂载文件.md` |
| 6.5.2 | 持久化记忆 | 1849-1853 | 74653-74818 | 122 | `chapters/volcengine/ark-guide/6.5.2 持久化记忆.md` |
| 6.5.3 | 使用 Dream 整理长期记忆 | 1854-1863 | 74819-75192 | 274 | `chapters/volcengine/ark-guide/6.5.3 使用 Dream 整理长期记忆.md` |
| 6.5.4 | 配置上下文压缩 | 1864-1866 | 75193-75324 | 79 | `chapters/volcengine/ark-guide/6.5.4 配置上下文压缩.md` |
| 6.6.1 | 编排 Multi Agent | 1867-1891 | 75326-76320 | 800 | `chapters/volcengine/ark-guide/6.6.1 编排 Multi Agent.md` |
| 7.1 | 将零代码应用迁移至 Managed Agents | 1892-1899 | 76322-76662 | 239 | `chapters/volcengine/ark-guide/7.1 将零代码应用迁移至 Managed Agents.md` |
| 7.2 | 知识库 | 1900 | 76663-76681 | 10 | `chapters/volcengine/ark-guide/7.2 知识库.md` |
| 8.1.1 | 套餐概览 | 1901-1909 | 76684-76992 | 223 | `chapters/volcengine/ark-guide/8.1.1 套餐概览.md` |
| 8.1.2 | 快速开始 | 1910-1916 | 76993-77235 | 172 | `chapters/volcengine/ark-guide/8.1.2 快速开始.md` |
| 8.1.3.1 | Codex | 1917-1925 | 77237-77468 | 169 | `chapters/volcengine/ark-guide/8.1.3.1 Codex.md` |
| 8.1.3.2 | Claude Code | 1926-1934 | 77469-77781 | 217 | `chapters/volcengine/ark-guide/8.1.3.2 Claude Code.md` |
| 8.1.3.3 | OpenCode | 1935-1948 | 77782-78401 | 552 | `chapters/volcengine/ark-guide/8.1.3.3 OpenCode.md` |
| 8.1.3.4 | OpenClaw | 1949-1967 | 78402-79108 | 588 | `chapters/volcengine/ark-guide/8.1.3.4 OpenClaw.md` |
| 8.1.3.5 | Hermes Agent | 1968-1973 | 79109-79326 | 147 | `chapters/volcengine/ark-guide/8.1.3.5 Hermes Agent.md` |
| 8.1.3.6 | TRAE | 1974-1975 | 79327-79364 | 20 | `chapters/volcengine/ark-guide/8.1.3.6 TRAE.md` |
| 8.1.3.7 | WorkBuddy | 1976-1981 | 79365-79486 | 76 | `chapters/volcengine/ark-guide/8.1.3.7 WorkBuddy.md` |
| 8.1.3.8 | ZCode | 1982-1990 | 79487-79860 | 318 | `chapters/volcengine/ark-guide/8.1.3.8 ZCode.md` |
| 8.1.3.9 | DeepSeek Harness | 1991-1998 | 79861-80053 | 108 | `chapters/volcengine/ark-guide/8.1.3.9 DeepSeek Harness.md` |
| 8.1.3.10 | Pi | 1999-2004 | 80054-80269 | 175 | `chapters/volcengine/ark-guide/8.1.3.10 Pi.md` |
| 8.1.3.11 | OpenViking | 2005-2011 | 80270-80494 | 178 | `chapters/volcengine/ark-guide/8.1.3.11 OpenViking.md` |
| 8.1.3.12 | 其他工具 | 2012-2015 | 80495-80621 | 86 | `chapters/volcengine/ark-guide/8.1.3.12 其他工具.md` |
| 8.1.4.1 | ArkClaw | 2016-2017 | 80623-80684 | 32 | `chapters/volcengine/ark-guide/8.1.4.1 ArkClaw.md` |
| 8.1.4.2 | 记忆增强-Embedding模型 | 2018-2020 | 80685-80800 | 87 | `chapters/volcengine/ark-guide/8.1.4.2 记忆增强-Embedding模型.md` |
| 8.1.5 | Ark CLI：Coding Plan 个人版使用指南 | 2021-2024 | 80801-80892 | 73 | `chapters/volcengine/ark-guide/8.1.5 Ark CLI：Coding Plan 个人版使用指南.md` |
| 8.1.6 | 常见问题 | 2025-2037 | 80893-81357 | 341 | `chapters/volcengine/ark-guide/8.1.6 常见问题.md` |
| 8.1.7.1 | 限时邀请活动 | 2038-2039 | 81359-81425 | 36 | `chapters/volcengine/ark-guide/8.1.7.1 限时邀请活动.md` |
| 8.1.7.2 | Coding Plan Lite & Pro 套餐 2.5 折普惠活动 | 2040-2041 | 81426-81503 | 52 | `chapters/volcengine/ark-guide/8.1.7.2 Coding Plan Lite & Pro 套餐 2.5 折普惠活动.md` |
| 8.1.7.3 | Agent/Coding Plan 指定模型抵扣系数限时折扣活动 | 2042-2044 | 81504-81615 | 87 | `chapters/volcengine/ark-guide/8.1.7.3 Agent-Coding Plan 指定模型抵扣系数限时折扣活动.md` |
| 8.1.7.4 | Coding Plan Pro 套餐赠送 ArkClaw 活动下线公告 | 2045 | 81616-81647 | 21 | `chapters/volcengine/ark-guide/8.1.7.4 Coding Plan Pro 套餐赠送 ArkClaw 活动下线公告.md` |
| 8.1.7.5 | 功能发布公告 | 2046-2050 | 81648-81866 | 189 | `chapters/volcengine/ark-guide/8.1.7.5 功能发布公告.md` |
| 8.1.7.6 | 模型上线公告 | 2051-2057 | 81867-82206 | 314 | `chapters/volcengine/ark-guide/8.1.7.6 模型上线公告.md` |
| 8.1.7.7 | 模型下线公告 | 2058-2065 | 82207-82523 | 247 | `chapters/volcengine/ark-guide/8.1.7.7 模型下线公告.md` |
| 9.1.1.1 | [基础] 构建连续对话的工单分诊助手 | 2066-2080 | 82527-83133 | 527 | `chapters/volcengine/ark-guide/9.1.1.1 [基础] 构建连续对话的工单分诊助手.md` |
| 9.1.1.2 | [基础] 工单分诊 Agent 系统提示词版本管理 | 2081-2087 | 83134-83396 | 193 | `chapters/volcengine/ark-guide/9.1.1.2 [基础] 工单分诊 Agent 系统提示词版本管理.md` |
| 9.1.1.3 | [基础] Custom Tool 使用教程 | 2088-2110 | 83397-84376 | 828 | `chapters/volcengine/ark-guide/9.1.1.3 [基础] Custom Tool 使用教程.md` |
| 9.1.1.4 | [基础] 使用 Viking 知识库检索构建知识问答 Agent | 2111-2118 | 84377-84560 | 106 | `chapters/volcengine/ark-guide/9.1.1.4 [基础] 使用 Viking 知识库检索构建知识问答 Agent.md` |
| 9.1.1.5 | [基础] 在豆包工作中使用 Managed Agents | 2119-2123 | 84561-84759 | 139 | `chapters/volcengine/ark-guide/9.1.1.5 [基础] 在豆包工作中使用 Managed Agents.md` |
| 9.1.1.6 | [基础] 使用 Seedance Managed Agent 生成图片和视频 | 2124-2149 | 84760-85829 | 926 | `chapters/volcengine/ark-guide/9.1.1.6 [基础] 使用 Seedance Managed Agent 生成图片和视频.md` |
| 9.1.1.7 | [进阶] 构建可持续迭代的 AI 研究交付工作台 | 2150-2162 | 85830-86329 | 410 | `chapters/volcengine/ark-guide/9.1.1.7 [进阶] 构建可持续迭代的 AI 研究交付工作台.md` |
| 9.1.1.8 | [进阶] 构建从 CSV 到交互式报告的数据分析 Agent | 2163-2178 | 86330-86946 | 526 | `chapters/volcengine/ark-guide/9.1.1.8 [进阶] 构建从 CSV 到交互式报告的数据分析 Agent.md` |
| 9.1.1.9 | [进阶] 使用 Vaults 让开发 Agent 以用户身份提交 | 2179-2195 | 86947-87613 | 577 | `chapters/volcengine/ark-guide/9.1.1.9 [进阶] 使用 Vaults 让开发 Agent 以用户身份提交.md` |
| 9.1.1.10 | [进阶] 使用 Memory Store 构建有记忆的购物助手 | 2196-2211 | 87614-88212 | 521 | `chapters/volcengine/ark-guide/9.1.1.10 [进阶] 使用 Memory Store 构建有记忆的购物助手.md` |
| 9.1.1.11 | [进阶] 用多智能体团队生成定制销售提案 | 2212-2238 | 88213-89328 | 1005 | `chapters/volcengine/ark-guide/9.1.1.11 [进阶] 用多智能体团队生成定制销售提案.md` |
| 9.1.1.12 | [进阶] 使用 arkcli 构建集成 Vault 与 Memory 的投研 | 2239-2248 | 89329-89682 | 254 | `chapters/volcengine/ark-guide/9.1.1.12 [进阶] 使用 arkcli 构建集成 Vault 与 Memory 的投研.md` |
| 9.1.2 | 快速入门(新手版) | 2249-2252 | 89683-89845 | 96 | `chapters/volcengine/ark-guide/9.1.2 快速入门(新手版).md` |
| 9.1.3 | Seedance 1.0 系列提示词指南 | 2253-2269 | 89846-90191 | 292 | `chapters/volcengine/ark-guide/9.1.3 Seedance 1.0 系列提示词指南.md` |
| 9.1.4 | Seedream 4.0-5.0 提示词指南 | 2270-2281 | 90192-90448 | 197 | `chapters/volcengine/ark-guide/9.1.4 Seedream 4.0-5.0 提示词指南.md` |
| 9.1.5 | Seedream 4.0 助力 Seedance 生视频最佳实践 | 2282-2294 | 90449-90685 | 185 | `chapters/volcengine/ark-guide/9.1.5 Seedream 4.0 助力 Seedance 生视频最佳实践.md` |
| 9.1.6 | RAG（检索增强）解决方案 | 2295-2296 | 90686-90737 | 26 | `chapters/volcengine/ark-guide/9.1.6 RAG（检索增强）解决方案.md` |
| 9.1.7 | 数据回流操作流程 | 2297-2305 | 90738-90852 | 63 | `chapters/volcengine/ark-guide/9.1.7 数据回流操作流程.md` |
| 9.1.8 | 强化学习最佳实践 | 2306-2340 | 90853-91957 | 802 | `chapters/volcengine/ark-guide/9.1.8 强化学习最佳实践.md` |
| 9.1.9 | 如何设置控制台登录保持时间 | 2341 | 91958-91974 | 8 | `chapters/volcengine/ark-guide/9.1.9 如何设置控制台登录保持时间.md` |
| 9.1.10 | 角色扮演场景提示词指南 | 2342-2367 | 91975-92841 | 688 | `chapters/volcengine/ark-guide/9.1.10 角色扮演场景提示词指南.md` |
| 9.1.11 | 机密部署最佳实践 | 2368-2373 | 92842-92979 | 86 | `chapters/volcengine/ark-guide/9.1.11 机密部署最佳实践.md` |
| 9.1.12 | 环境变量配置指南 | 2374-2379 | 92980-93161 | 131 | `chapters/volcengine/ark-guide/9.1.12 环境变量配置指南.md` |
| 9.1.13 | 突发流量处理最佳实践 | 2380-2406 | 93162-94231 | 911 | `chapters/volcengine/ark-guide/9.1.13 突发流量处理最佳实践.md` |
| 9.1.14 | 火山方舟分账最佳实践 | 2407-2415 | 94232-94456 | 108 | `chapters/volcengine/ark-guide/9.1.14 火山方舟分账最佳实践.md` |
| 9.1.15 | 在应用中使用 RTC 实现 AI 实时对话 | 2416-2420 | 94457-94608 | 119 | `chapters/volcengine/ark-guide/9.1.15 在应用中使用 RTC 实现 AI 实时对话.md` |
| 9.1.16 | 通过 TOS 内网预签名 URL 传入文件 | 2421-2423 | 94609-94725 | 93 | `chapters/volcengine/ark-guide/9.1.16 通过 TOS 内网预签名 URL 传入文件.md` |
| 9.1.17 | 用量明细 CSV 解析最佳实践 | 2424-2433 | 94726-95113 | 331 | `chapters/volcengine/ark-guide/9.1.17 用量明细 CSV 解析最佳实践.md` |
