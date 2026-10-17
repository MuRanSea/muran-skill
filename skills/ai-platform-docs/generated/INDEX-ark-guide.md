# 方舟指南区章节表（ark-guide）

来源：《火山方舟 文档指南》（2415 页）。165 个章节文件，接口级切分：一个接口/任务一个文件；超过 1500 行的按语义块自动再拆为`… - 第N部分`（10 个章节被拆分）。

「页码」是原 PDF 页码范围；「行范围」是中间 MD（`doc/<源文档>.md`）的 1 起始行号，可据此回查原文。章节文件本身已去掉页眉页脚，回查 PDF 时用这两列。文件名即章节标题，日常定位直接 Glob 文件名即可，用不到这两列。

**这张表用来 grep，不要整读。**

| 编号 | 标题 | 页码 | 行范围(源文件) | 行数 | 文件 |
|------|------|------|---------------|------|------|
| 1.1 | 产品简介 | 1-9 | 229-405 | 159 | `chapters/volcengine/ark-guide/1.1 产品简介.md` |
| 1.2 | 快速入门 | 10-33 | 406-1352 | 837 | `chapters/volcengine/ark-guide/1.2 快速入门.md` |
| 1.3 | 模型价格 | 10-55 | 1353-2646 | 1168 | `chapters/volcengine/ark-guide/1.3 模型价格.md` |
| 1.4 | Agent 场景模型调用的正确姿势 | 56-67 | 2647-3231 | 520 | `chapters/volcengine/ark-guide/1.4 Agent 场景模型调用的正确姿势.md` |
| 1.5 | 迁移到方舟官方 SDK | 68-70 | 3232-3336 | 64 | `chapters/volcengine/ark-guide/1.5 迁移到方舟官方 SDK.md` |
| 2.1 | 模型列表 - 第1部分 | 71-100 | 3337-5118 | 1711 | `chapters/volcengine/ark-guide/2.1 模型列表 - 第1部分.md` |
| 2.2 | Seed-Evolving | 101-105 | 5119-5302 | 117 | `chapters/volcengine/ark-guide/2.2 Seed-Evolving.md` |
| 2.3 | DeepSeek-V4.1-Flash | 106-117 | 5303-5820 | 474 | `chapters/volcengine/ark-guide/2.3 DeepSeek-V4.1-Flash.md` |
| 3.1 | 文本生成 | 118-132 | 5822-6420 | 514 | `chapters/volcengine/ark-guide/3.1 文本生成.md` |
| 3.2.1 | 图片理解 - 第1部分 | 133-170 | 6421-8047 | 1428 | `chapters/volcengine/ark-guide/3.2.1 图片理解 - 第1部分.md` |
| 3.2.1 | 图片理解 - 第2部分·代码示例 | 171-196 | 8048-9095 | 898 | `chapters/volcengine/ark-guide/3.2.1 图片理解 - 第2部分·代码示例.md` |
| 3.2.2 | 视频理解 - 第1部分 | 197-237 | 9096-10779 | 1483 | `chapters/volcengine/ark-guide/3.2.2 视频理解 - 第1部分.md` |
| 3.2.2 | 视频理解 - 第2部分 | 238-250 | 10780-11327 | 489 | `chapters/volcengine/ark-guide/3.2.2 视频理解 - 第2部分.md` |
| 3.2.3 | 文档理解 | 251-281 | 11328-12604 | 1140 | `chapters/volcengine/ark-guide/3.2.3 文档理解.md` |
| 3.2.4 | 音频理解 - 第1部分 | 282-323 | 12605-14312 | 1536 | `chapters/volcengine/ark-guide/3.2.4 音频理解 - 第1部分.md` |
| 3.2.4 | 音频理解 - 第2部分 | 324-339 | 14313-14962 | 515 | `chapters/volcengine/ark-guide/3.2.4 音频理解 - 第2部分.md` |
| 3.3.1 | Doubao Seedance 2.5 教程 - 第1部分 | 340-378 | 14963-16751 | 1509 | `chapters/volcengine/ark-guide/3.3.1 Doubao Seedance 2.5 教程 - 第1部分.md` |
| 3.3.1 | Doubao Seedance 2.5 教程 - 第2部分 | 379-414 | 16752-18290 | 1248 | `chapters/volcengine/ark-guide/3.3.1 Doubao Seedance 2.5 教程 - 第2部分.md` |
| 3.3.2 | Doubao Seedance 2.5 提示词指南 | 415-529 | 18291-19888 | 905 | `chapters/volcengine/ark-guide/3.3.2 Doubao Seedance 2.5 提示词指南.md` |
| 3.3.3 | Doubao Seedance 2.0 系列教程 - 第1部分 | 530-580 | 19889-21919 | 1810 | `chapters/volcengine/ark-guide/3.3.3 Doubao Seedance 2.0 系列教程 - 第1部分.md` |
| 3.3.4 | Doubao Seedance 2.0 系列提示词指南 | 581-635 | 21920-22733 | 528 | `chapters/volcengine/ark-guide/3.3.4 Doubao Seedance 2.0 系列提示词指南.md` |
| 3.3.5 | 视频生成教程 - 第1部分 | 636-675 | 22734-24397 | 1546 | `chapters/volcengine/ark-guide/3.3.5 视频生成教程 - 第1部分.md` |
| 3.3.5 | 视频生成教程 - 第2部分 | 676-698 | 24398-25268 | 721 | `chapters/volcengine/ark-guide/3.3.5 视频生成教程 - 第2部分.md` |
| 3.3.6 | Doubao Seedance 便利创作含肖像视频 | 699-717 | 25269-26017 | 667 | `chapters/volcengine/ark-guide/3.3.6 Doubao Seedance 便利创作含肖像视频.md` |
| 3.4.1 | Doubao Seedream 5.0 pro / flash 教程 | 718-750 | 26019-27210 | 1005 | `chapters/volcengine/ark-guide/3.4.1 Doubao Seedream 5.0 pro - flash 教程.md` |
| 3.4.2 | Doubao Seedream 5.0 pro / flash 实现交互编辑指南 | 751-760 | 27211-27580 | 300 | `chapters/volcengine/ark-guide/3.4.2 Doubao Seedream 5.0 pro - flash 实现交互编辑指南.md` |
| 3.4.3 | 图片生成教程 - 第1部分 | 761-804 | 27581-29251 | 1478 | `chapters/volcengine/ark-guide/3.4.3 图片生成教程 - 第1部分.md` |
| 3.4.3 | 图片生成教程 - 第2部分 | 805-825 | 29252-30227 | 857 | `chapters/volcengine/ark-guide/3.4.3 图片生成教程 - 第2部分.md` |
| 3.5 | 决策评估（beta） | 826-836 | 30228-30699 | 404 | `chapters/volcengine/ark-guide/3.5 决策评估（beta）.md` |
| 3.6.1 | 3D 生成 | 837-847 | 30701-31096 | 357 | `chapters/volcengine/ark-guide/3.6.1 3D 生成.md` |
| 3.6.2 | 向量化 | 848 | 31097-31099 | 1 | `chapters/volcengine/ark-guide/3.6.2 向量化.md` |
| 3.7.1 | 工具概述 | 849-856 | 31101-31421 | 283 | `chapters/volcengine/ark-guide/3.7.1 工具概述.md` |
| 3.7.2 | 豆包助手 | 857-878 | 31422-32376 | 813 | `chapters/volcengine/ark-guide/3.7.2 豆包助手.md` |
| 3.7.3 | 联网搜索工具 | 879-896 | 32377-33099 | 624 | `chapters/volcengine/ark-guide/3.7.3 联网搜索工具.md` |
| 3.7.4 | Image Process（图像处理） | 897-921 | 33100-34162 | 979 | `chapters/volcengine/ark-guide/3.7.4 Image Process（图像处理）.md` |
| 3.7.5 | 私域知识库搜索 Knowledge Search | 922-927 | 34163-34369 | 167 | `chapters/volcengine/ark-guide/3.7.5 私域知识库搜索 Knowledge Search.md` |
| 3.7.6 | 云部署 MCP / Remote MCP | 928-944 | 34370-35034 | 597 | `chapters/volcengine/ark-guide/3.7.6 云部署 MCP - Remote MCP.md` |
| 3.7.7 | Function Calling（函数调用） - 第1部分 | 945-987 | 35035-36817 | 1566 | `chapters/volcengine/ark-guide/3.7.7 Function Calling（函数调用） - 第1部分.md` |
| 3.7.8 | Apply Patch（代码补丁工具） | 988-1004 | 36818-37578 | 342 | `chapters/volcengine/ark-guide/3.7.8 Apply Patch（代码补丁工具）.md` |
| 3.8.1 | 深度思考 | 1005-1029 | 37580-39060 | 1353 | `chapters/volcengine/ark-guide/3.8.1 深度思考.md` |
| 3.8.2 | 上下文管理 | 1030-1064 | 39061-40518 | 1293 | `chapters/volcengine/ark-guide/3.8.2 上下文管理.md` |
| 3.8.3 | 流式输出 | 1065-1078 | 40519-41038 | 443 | `chapters/volcengine/ark-guide/3.8.3 流式输出.md` |
| 3.8.4 | 续写模式 | 1079-1086 | 41039-41411 | 331 | `chapters/volcengine/ark-guide/3.8.4 续写模式.md` |
| 3.8.5 | 上下文缓存 | 1087-1120 | 41412-42824 | 1210 | `chapters/volcengine/ark-guide/3.8.5 上下文缓存.md` |
| 3.8.6 | 文件输入(Files API) | 1121-1161 | 42825-44413 | 1444 | `chapters/volcengine/ark-guide/3.8.6 文件输入(Files API).md` |
| 3.8.7 | GUI Agent 能力 | 1162-1172 | 44414-44810 | 316 | `chapters/volcengine/ark-guide/3.8.7 GUI Agent 能力.md` |
| 3.8.8 | 视觉定位 Grounding | 1173-1180 | 44811-45052 | 219 | `chapters/volcengine/ark-guide/3.8.8 视觉定位 Grounding.md` |
| 3.8.9 | 提示词工程 | 1181-1185 | 45053-45271 | 152 | `chapters/volcengine/ark-guide/3.8.9 提示词工程.md` |
| 3.8.10 | 结构化输出(beta) | 1186-1209 | 45272-46226 | 856 | `chapters/volcengine/ark-guide/3.8.10 结构化输出(beta).md` |
| 3.9 | 接入三方工具 | 1210 | 46227-46229 | 1 | `chapters/volcengine/ark-guide/3.9 接入三方工具.md` |
| 3.10.1 | 迁移至 Responses API | 1211-1223 | 46231-46883 | 567 | `chapters/volcengine/ark-guide/3.10.1 迁移至 Responses API.md` |
| 3.10.2 | 文本生成 | 1224-1265 | 46884-48541 | 1459 | `chapters/volcengine/ark-guide/3.10.2 文本生成.md` |
| 3.10.3 | 深度思考 | 1266-1290 | 48542-49602 | 904 | `chapters/volcengine/ark-guide/3.10.3 深度思考.md` |
| 3.10.4 | 多模态理解 | 1291-1321 | 49603-50820 | 1099 | `chapters/volcengine/ark-guide/3.10.4 多模态理解.md` |
| 3.10.5 | 工具调用 | 1322-1334 | 50821-51363 | 482 | `chapters/volcengine/ark-guide/3.10.5 工具调用.md` |
| 3.10.6 | 结构化输出(beta) | 1335-1344 | 51364-51748 | 349 | `chapters/volcengine/ark-guide/3.10.6 结构化输出(beta).md` |
| 3.10.7 | 上下文编辑 | 1345-1351 | 51749-52020 | 238 | `chapters/volcengine/ark-guide/3.10.7 上下文编辑.md` |
| 4.1 | 推理方式概述 | 1345-1356 | 52022-52535 | 486 | `chapters/volcengine/ark-guide/4.1 推理方式概述.md` |
| 4.2 | 在线推理（常规） | 1357-1358 | 52536-52598 | 43 | `chapters/volcengine/ark-guide/4.2 在线推理（常规）.md` |
| 4.3 | 在线推理（低延迟） | 1359-1364 | 52599-52801 | 117 | `chapters/volcengine/ark-guide/4.3 在线推理（低延迟）.md` |
| 4.4 | 在线推理（低优） | 1365-1372 | 52802-53105 | 195 | `chapters/volcengine/ark-guide/4.4 在线推理（低优）.md` |
| 4.5 | 在线推理（TPM 保障包） | 1373-1381 | 53106-53363 | 181 | `chapters/volcengine/ark-guide/4.5 在线推理（TPM 保障包）.md` |
| 4.6.1 | 模型单元概述 | 1382-1383 | 53365-53451 | 45 | `chapters/volcengine/ark-guide/4.6.1 模型单元概述.md` |
| 4.6.2 | 创建模型单元 | 1384-1387 | 53452-53557 | 69 | `chapters/volcengine/ark-guide/4.6.2 创建模型单元.md` |
| 4.6.3 | 管理模型单元 | 1388 | 53558-53588 | 17 | `chapters/volcengine/ark-guide/4.6.3 管理模型单元.md` |
| 4.7 | 批量推理 | 1389-1423 | 53589-55032 | 1223 | `chapters/volcengine/ark-guide/4.7 批量推理.md` |
| 4.8.1 | 智能模型路由 | 1424-1428 | 55034-55182 | 85 | `chapters/volcengine/ark-guide/4.8.1 智能模型路由.md` |
| 4.8.2 | 使用 MLP 推理服务 | 1429-1435 | 55183-55453 | 208 | `chapters/volcengine/ark-guide/4.8.2 使用 MLP 推理服务.md` |
| 4.8.3 | 使用自定义模型进行推理 | 1436-1438 | 55454-55587 | 75 | `chapters/volcengine/ark-guide/4.8.3 使用自定义模型进行推理.md` |
| 5.1.1 | 模型精调概述 | 1439-1445 | 55590-55969 | 321 | `chapters/volcengine/ark-guide/5.1.1 模型精调概述.md` |
| 5.1.2 | 有监督微调最佳实践 | 1446-1459 | 55970-56603 | 226 | `chapters/volcengine/ark-guide/5.1.2 有监督微调最佳实践.md` |
| 5.1.3 | 直接偏好优化最佳实践 | 1460-1470 | 56604-57052 | 309 | `chapters/volcengine/ark-guide/5.1.3 直接偏好优化最佳实践.md` |
| 5.1.4 | 强化学习最佳实践 | 1471-1498 | 57053-58126 | 839 | `chapters/volcengine/ark-guide/5.1.4 强化学习最佳实践.md` |
| 5.1.5 | Plugin 异常处理 | 1499-1501 | 58127-58268 | 99 | `chapters/volcengine/ark-guide/5.1.5 Plugin 异常处理.md` |
| 5.1.6 | 精调 SDK 使用指南 | 1499-1531 | 58269-59660 | 1161 | `chapters/volcengine/ark-guide/5.1.6 精调 SDK 使用指南.md` |
| 5.1.7.1 | 格式总览 | 1532-1533 | 59662-59715 | 38 | `chapters/volcengine/ark-guide/5.1.7.1 格式总览.md` |
| 5.1.7.2 | 语言及多模态理解模型精调数据格式 - 第1部分 | 1532-1579 | 59716-61939 | 1921 | `chapters/volcengine/ark-guide/5.1.7.2 语言及多模态理解模型精调数据格式 - 第1部分.md` |
| 5.1.7.2 | 语言及多模态理解模型精调数据格式 - 第2部分·注意事项 | 1580-1581 | 61940-62022 | 52 | `chapters/volcengine/ark-guide/5.1.7.2 语言及多模态理解模型精调数据格式 - 第2部分·注意事项.md` |
| 5.1.7.3 | 图片生成模型精调数据格式 | 1582-1589 | 62023-62368 | 293 | `chapters/volcengine/ark-guide/5.1.7.3 图片生成模型精调数据格式.md` |
| 5.1.7.4 | 视频生成模型精调数据格式 | 1590-1592 | 62369-62465 | 88 | `chapters/volcengine/ark-guide/5.1.7.4 视频生成模型精调数据格式.md` |
| 5.1.8 | 管理自定义模型 | 1593-1595 | 62466-62556 | 54 | `chapters/volcengine/ark-guide/5.1.8 管理自定义模型.md` |
| 5.2.1 | 创建模型评测任务 | 1596-1601 | 62558-62623 | 31 | `chapters/volcengine/ark-guide/5.2.1 创建模型评测任务.md` |
| 5.2.2 | 查看并管理模型评测任务 | 1602-1604 | 62624-62643 | 11 | `chapters/volcengine/ark-guide/5.2.2 查看并管理模型评测任务.md` |
| 5.2.3 | 评测数据集格式说明 | 1605-1621 | 62644-63525 | 824 | `chapters/volcengine/ark-guide/5.2.3 评测数据集格式说明.md` |
| 5.2.4.1 | 人工评测作业 | 1622-1633 | 63527-63584 | 28 | `chapters/volcengine/ark-guide/5.2.4.1 人工评测作业.md` |
| 5.2.4.2 | 查看评测报告 | 1634-1638 | 63585-63694 | 61 | `chapters/volcengine/ark-guide/5.2.4.2 查看评测报告.md` |
| 5.3.1 | 数据集介绍 | 1639-1644 | 63696-63802 | 73 | `chapters/volcengine/ark-guide/5.3.1 数据集介绍.md` |
| 5.3.2 | 共享数据集 | 1645-1650 | 63803-63849 | 24 | `chapters/volcengine/ark-guide/5.3.2 共享数据集.md` |
| 6.1.1 | 概述 | 1651-1654 | 63852-64014 | 118 | `chapters/volcengine/ark-guide/6.1.1 概述.md` |
| 6.1.2 | 快速入门（代码） | 1655-1671 | 64015-64701 | 624 | `chapters/volcengine/ark-guide/6.1.2 快速入门（代码）.md` |
| 6.1.3 | 快速入门（控制台） | 1672-1674 | 64702-64799 | 56 | `chapters/volcengine/ark-guide/6.1.3 快速入门（控制台）.md` |
| 6.2.1 | Agent | 1675-1681 | 64801-65067 | 218 | `chapters/volcengine/ark-guide/6.2.1 Agent.md` |
| 6.2.2 | Skills | 1682-1686 | 65068-65216 | 108 | `chapters/volcengine/ark-guide/6.2.2 Skills.md` |
| 6.2.3 | MCP | 1687-1691 | 65217-65390 | 147 | `chapters/volcengine/ark-guide/6.2.3 MCP.md` |
| 6.2.4 | Tools | 1692-1706 | 65391-65991 | 457 | `chapters/volcengine/ark-guide/6.2.4 Tools.md` |
| 6.2.5 | 工具权限策略 | 1707-1711 | 65992-66170 | 158 | `chapters/volcengine/ark-guide/6.2.5 工具权限策略.md` |
| 6.2.6 | 模型支持的参数列表 | 1712-1714 | 66171-66333 | 140 | `chapters/volcengine/ark-guide/6.2.6 模型支持的参数列表.md` |
| 6.3.1 | 配置云环境 | 1715-1720 | 66335-66586 | 199 | `chapters/volcengine/ark-guide/6.3.1 配置云环境.md` |
| 6.3.2 | 云沙箱参考 | 1721-1724 | 66587-66739 | 125 | `chapters/volcengine/ark-guide/6.3.2 云沙箱参考.md` |
| 6.3.3.1 | 自托管环境概述 | 1725-1728 | 66741-66904 | 99 | `chapters/volcengine/ark-guide/6.3.3.1 自托管环境概述.md` |
| 6.3.3.2 | 配置并运行自托管环境 | 1729-1743 | 66905-67449 | 447 | `chapters/volcengine/ark-guide/6.3.3.2 配置并运行自托管环境.md` |
| 6.3.3.3 | 自托管环境安全说明 | 1744-1749 | 67450-67702 | 161 | `chapters/volcengine/ark-guide/6.3.3.3 自托管环境安全说明.md` |
| 6.4.1 | 启动 Session | 1750-1765 | 67704-68362 | 551 | `chapters/volcengine/ark-guide/6.4.1 启动 Session.md` |
| 6.4.2 | 管理 Session | 1766-1771 | 68363-68558 | 150 | `chapters/volcengine/ark-guide/6.4.2 管理 Session.md` |
| 6.4.3 | Session 事件流 | 1772-1793 | 68559-69441 | 729 | `chapters/volcengine/ark-guide/6.4.3 Session 事件流.md` |
| 6.4.4 | 使用 Vaults 认证 | 1794-1802 | 69442-69820 | 283 | `chapters/volcengine/ark-guide/6.4.4 使用 Vaults 认证.md` |
| 6.5.1 | 上传与挂载文件 | 1803-1808 | 69822-70054 | 181 | `chapters/volcengine/ark-guide/6.5.1 上传与挂载文件.md` |
| 6.5.2 | 持久化记忆 | 1809-1813 | 70055-70214 | 120 | `chapters/volcengine/ark-guide/6.5.2 持久化记忆.md` |
| 6.5.3 | 使用 Dream 整理长期记忆 | 1814-1822 | 70215-70586 | 272 | `chapters/volcengine/ark-guide/6.5.3 使用 Dream 整理长期记忆.md` |
| 6.6.1 | 编排 Multi Agent | 1823-1842 | 70588-71319 | 631 | `chapters/volcengine/ark-guide/6.6.1 编排 Multi Agent.md` |
| 7.1 | 将零代码应用迁移至 Managed Agents | 1843-1850 | 71321-71658 | 236 | `chapters/volcengine/ark-guide/7.1 将零代码应用迁移至 Managed Agents.md` |
| 7.2 | 知识库 | 1851 | 71659-71677 | 10 | `chapters/volcengine/ark-guide/7.2 知识库.md` |
| 8.1.1 | 套餐概览 | 1852-1862 | 71680-71977 | 237 | `chapters/volcengine/ark-guide/8.1.1 套餐概览.md` |
| 8.1.2 | 快速开始 | 1863-1871 | 71978-72243 | 203 | `chapters/volcengine/ark-guide/8.1.2 快速开始.md` |
| 8.1.3.1 | Codex | 1872-1883 | 72245-72567 | 253 | `chapters/volcengine/ark-guide/8.1.3.1 Codex.md` |
| 8.1.3.2 | Claude Code | 1884-1896 | 72568-73003 | 313 | `chapters/volcengine/ark-guide/8.1.3.2 Claude Code.md` |
| 8.1.3.3 | OpenCode | 1897-1913 | 73004-73671 | 591 | `chapters/volcengine/ark-guide/8.1.3.3 OpenCode.md` |
| 8.1.3.4 | OpenClaw | 1914-1934 | 73672-74429 | 636 | `chapters/volcengine/ark-guide/8.1.3.4 OpenClaw.md` |
| 8.1.3.5 | Hermes Agent | 1935-1943 | 74430-74689 | 192 | `chapters/volcengine/ark-guide/8.1.3.5 Hermes Agent.md` |
| 8.1.3.6 | TRAE | 1944-1946 | 74690-74759 | 52 | `chapters/volcengine/ark-guide/8.1.3.6 TRAE.md` |
| 8.1.3.7 | WorkBuddy | 1947-1954 | 74760-74920 | 105 | `chapters/volcengine/ark-guide/8.1.3.7 WorkBuddy.md` |
| 8.1.3.8 | ZCode | 1955-1967 | 74921-75323 | 333 | `chapters/volcengine/ark-guide/8.1.3.8 ZCode.md` |
| 8.1.3.9 | DeepSeek Harness | 1968-1976 | 75324-75537 | 134 | `chapters/volcengine/ark-guide/8.1.3.9 DeepSeek Harness.md` |
| 8.1.3.10 | Pi | 1977-1985 | 75538-75802 | 212 | `chapters/volcengine/ark-guide/8.1.3.10 Pi.md` |
| 8.1.3.11 | OpenViking | 1986-1994 | 75803-76085 | 231 | `chapters/volcengine/ark-guide/8.1.3.11 OpenViking.md` |
| 8.1.3.12 | 其他工具 | 1995-1999 | 76086-76232 | 103 | `chapters/volcengine/ark-guide/8.1.3.12 其他工具.md` |
| 8.1.4.1 | ArkClaw | 2000-2001 | 76234-76294 | 30 | `chapters/volcengine/ark-guide/8.1.4.1 ArkClaw.md` |
| 8.1.4.2 | 记忆增强-Embedding模型 | 2002-2005 | 76295-76420 | 98 | `chapters/volcengine/ark-guide/8.1.4.2 记忆增强-Embedding模型.md` |
| 8.1.5 | Ark CLI：Coding Plan 个人版使用指南 | 2006-2009 | 76421-76534 | 98 | `chapters/volcengine/ark-guide/8.1.5 Ark CLI：Coding Plan 个人版使用指南.md` |
| 8.1.6 | 常见问题 | 2010-2022 | 76535-76994 | 341 | `chapters/volcengine/ark-guide/8.1.6 常见问题.md` |
| 8.1.7.1 | 限时邀请活动 | 2023-2024 | 76996-77062 | 36 | `chapters/volcengine/ark-guide/8.1.7.1 限时邀请活动.md` |
| 8.1.7.2 | Coding Plan Lite & Pro 套餐 2.5 折普惠活动 | 2025-2026 | 77063-77131 | 45 | `chapters/volcengine/ark-guide/8.1.7.2 Coding Plan Lite & Pro 套餐 2.5 折普惠活动.md` |
| 8.1.7.3 | Agent/Coding Plan 指定模型抵扣系数限时折扣活动 | 2027-2028 | 77132-77223 | 72 | `chapters/volcengine/ark-guide/8.1.7.3 Agent-Coding Plan 指定模型抵扣系数限时折扣活动.md` |
| 8.1.7.4 | Coding Plan Pro 套餐赠送 ArkClaw 活动下线公告 | 2029 | 77224-77255 | 21 | `chapters/volcengine/ark-guide/8.1.7.4 Coding Plan Pro 套餐赠送 ArkClaw 活动下线公告.md` |
| 8.1.7.5 | 功能发布公告 | 2030-2034 | 77256-77430 | 165 | `chapters/volcengine/ark-guide/8.1.7.5 功能发布公告.md` |
| 8.1.7.6 | 模型上线公告 | 2035-2041 | 77431-77744 | 288 | `chapters/volcengine/ark-guide/8.1.7.6 模型上线公告.md` |
| 8.1.7.7 | 模型下线公告 | 2042-2048 | 77745-77978 | 206 | `chapters/volcengine/ark-guide/8.1.7.7 模型下线公告.md` |
| 9.1.1.1 | [基础] 构建连续对话的工单分诊助手 | 2049-2063 | 77982-78583 | 522 | `chapters/volcengine/ark-guide/9.1.1.1 [基础] 构建连续对话的工单分诊助手.md` |
| 9.1.1.2 | [基础] 工单分诊 Agent 系统提示词版本管理 | 2064-2070 | 78584-78844 | 192 | `chapters/volcengine/ark-guide/9.1.1.2 [基础] 工单分诊 Agent 系统提示词版本管理.md` |
| 9.1.1.3 | [基础] Custom Tool 使用教程 | 2071-2093 | 78845-79801 | 809 | `chapters/volcengine/ark-guide/9.1.1.3 [基础] Custom Tool 使用教程.md` |
| 9.1.1.4 | [基础] 使用 Viking 知识库检索构建知识问答 Agent | 2094-2101 | 79802-79986 | 107 | `chapters/volcengine/ark-guide/9.1.1.4 [基础] 使用 Viking 知识库检索构建知识问答 Agent.md` |
| 9.1.1.5 | [基础] 在豆包工作中使用 Managed Agents | 2102-2106 | 79987-80184 | 138 | `chapters/volcengine/ark-guide/9.1.1.5 [基础] 在豆包工作中使用 Managed Agents.md` |
| 9.1.1.6 | [基础] 使用视觉增强 Agent 生成图片和视频 | 2107-2132 | 80185-81252 | 924 | `chapters/volcengine/ark-guide/9.1.1.6 [基础] 使用视觉增强 Agent 生成图片和视频.md` |
| 9.1.1.7 | [进阶] 构建可持续迭代的 AI 研究交付工作台 | 2133-2145 | 81253-81753 | 411 | `chapters/volcengine/ark-guide/9.1.1.7 [进阶] 构建可持续迭代的 AI 研究交付工作台.md` |
| 9.1.1.8 | [进阶] 构建从 CSV 到交互式报告的数据分析 Agent | 2146-2160 | 81754-82362 | 520 | `chapters/volcengine/ark-guide/9.1.1.8 [进阶] 构建从 CSV 到交互式报告的数据分析 Agent.md` |
| 9.1.1.9 | [进阶] 使用 Vaults 让开发 Agent 以用户身份提交 | 2161-2176 | 82363-83023 | 573 | `chapters/volcengine/ark-guide/9.1.1.9 [进阶] 使用 Vaults 让开发 Agent 以用户身份提交.md` |
| 9.1.1.10 | [进阶] 使用 Memory Store 构建有记忆的购物助手 | 2177-2191 | 83024-83615 | 516 | `chapters/volcengine/ark-guide/9.1.1.10 [进阶] 使用 Memory Store 构建有记忆的购物助手.md` |
| 9.1.1.11 | [进阶] 用多智能体团队生成定制销售提案 | 2192-2218 | 83616-84732 | 1006 | `chapters/volcengine/ark-guide/9.1.1.11 [进阶] 用多智能体团队生成定制销售提案.md` |
| 9.1.1.12 | [进阶] 使用 arkcli 构建集成 Vault 与 Memory 的投研 | 2219-2228 | 84733-85084 | 252 | `chapters/volcengine/ark-guide/9.1.1.12 [进阶] 使用 arkcli 构建集成 Vault 与 Memory 的投研.md` |
| 9.1.2 | 快速入门(新手版) | 2229-2232 | 85085-85246 | 95 | `chapters/volcengine/ark-guide/9.1.2 快速入门(新手版).md` |
| 9.1.3 | Seedance 1.0 系列提示词指南 | 2233-2250 | 85247-85594 | 290 | `chapters/volcengine/ark-guide/9.1.3 Seedance 1.0 系列提示词指南.md` |
| 9.1.4 | Seedream 4.0-5.0 提示词指南 | 2251-2262 | 85595-85842 | 188 | `chapters/volcengine/ark-guide/9.1.4 Seedream 4.0-5.0 提示词指南.md` |
| 9.1.5 | Seedream 4.0 助力 Seedance 生视频最佳实践 | 2263-2275 | 85843-86063 | 166 | `chapters/volcengine/ark-guide/9.1.5 Seedream 4.0 助力 Seedance 生视频最佳实践.md` |
| 9.1.6 | RAG（检索增强）解决方案 | 2276-2277 | 86064-86115 | 26 | `chapters/volcengine/ark-guide/9.1.6 RAG（检索增强）解决方案.md` |
| 9.1.7 | 数据回流操作流程 | 2278-2286 | 86116-86230 | 63 | `chapters/volcengine/ark-guide/9.1.7 数据回流操作流程.md` |
| 9.1.8 | 强化学习最佳实践 | 2287-2320 | 86231-87282 | 756 | `chapters/volcengine/ark-guide/9.1.8 强化学习最佳实践.md` |
| 9.1.9 | 如何设置控制台登录保持时间 | 2321 | 87283-87299 | 8 | `chapters/volcengine/ark-guide/9.1.9 如何设置控制台登录保持时间.md` |
| 9.1.10 | 角色扮演场景提示词指南 | 2322-2347 | 87300-88155 | 683 | `chapters/volcengine/ark-guide/9.1.10 角色扮演场景提示词指南.md` |
| 9.1.11 | 机密部署最佳实践 | 2348-2353 | 88156-88293 | 86 | `chapters/volcengine/ark-guide/9.1.11 机密部署最佳实践.md` |
| 9.1.12 | 环境变量配置指南 | 2354-2359 | 88294-88475 | 130 | `chapters/volcengine/ark-guide/9.1.12 环境变量配置指南.md` |
| 9.1.13 | 突发流量处理最佳实践 | 2360-2387 | 88476-89552 | 925 | `chapters/volcengine/ark-guide/9.1.13 突发流量处理最佳实践.md` |
| 9.1.14 | 火山方舟分账最佳实践 | 2388-2398 | 89553-89779 | 106 | `chapters/volcengine/ark-guide/9.1.14 火山方舟分账最佳实践.md` |
| 9.1.15 | 在应用中使用 RTC 实现 AI 实时对话 | 2399-2403 | 89780-89931 | 119 | `chapters/volcengine/ark-guide/9.1.15 在应用中使用 RTC 实现 AI 实时对话.md` |
| 9.1.16 | 通过 TOS 内网预签名 URL 传入文件 | 2404-2406 | 89932-90048 | 93 | `chapters/volcengine/ark-guide/9.1.16 通过 TOS 内网预签名 URL 传入文件.md` |
| 9.1.17 | 用量明细 CSV 解析最佳实践 | 2407-2415 | 90049-90399 | 301 | `chapters/volcengine/ark-guide/9.1.17 用量明细 CSV 解析最佳实践.md` |
