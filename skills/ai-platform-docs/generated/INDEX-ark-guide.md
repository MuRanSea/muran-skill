# 方舟指南区章节表（ark-guide）

来源：《火山方舟 文档指南》（2388 页）。168 个章节文件，接口级切分：一个接口/任务一个文件；超过 1500 行的按语义块自动再拆为`… - 第N部分`（10 个章节被拆分）。

「页码」是原 PDF 页码范围；「行范围」是中间 MD（`doc/<源文档>.md`）的 1 起始行号，可据此回查原文。章节文件本身已去掉页眉页脚，回查 PDF 时用这两列。文件名即章节标题，日常定位直接 Glob 文件名即可，用不到这两列。

**这张表用来 grep，不要整读。**

| 编号 | 标题 | 页码 | 行范围(源文件) | 行数 | 文件 |
|------|------|------|---------------|------|------|
| 1.1 | 产品简介 | 1-5 | 232-388 | 147 | `chapters/volcengine/ark-guide/1.1 产品简介.md` |
| 1.2 | 快速入门 | 6-30 | 389-1341 | 836 | `chapters/volcengine/ark-guide/1.2 快速入门.md` |
| 1.3 | 模型价格 | 31-54 | 1342-2790 | 1302 | `chapters/volcengine/ark-guide/1.3 模型价格.md` |
| 1.4 | Agent 场景模型调用的正确姿势 | 55-65 | 2791-3360 | 495 | `chapters/volcengine/ark-guide/1.4 Agent 场景模型调用的正确姿势.md` |
| 1.5 | 迁移到方舟官方 SDK | 66-68 | 3361-3465 | 64 | `chapters/volcengine/ark-guide/1.5 迁移到方舟官方 SDK.md` |
| 2.1 | 模型列表 - 第1部分 | 69-91 | 3466-5042 | 1520 | `chapters/volcengine/ark-guide/2.1 模型列表 - 第1部分.md` |
| 2.1 | 模型列表 - 第2部分 | 92-98 | 5043-5620 | 465 | `chapters/volcengine/ark-guide/2.1 模型列表 - 第2部分.md` |
| 2.2 | Seed-Evolving | 99-103 | 5621-5809 | 120 | `chapters/volcengine/ark-guide/2.2 Seed-Evolving.md` |
| 2.3 | DeepSeek-V4.1-Flash（升级 1017） | 104-115 | 5810-6393 | 496 | `chapters/volcengine/ark-guide/2.3 DeepSeek-V4.1-Flash（升级 1017）.md` |
| 3.1 | 文本生成 | 116-129 | 6395-6960 | 477 | `chapters/volcengine/ark-guide/3.1 文本生成.md` |
| 3.2.1 | 图片理解 - 第1部分 | 130-168 | 6961-8592 | 1426 | `chapters/volcengine/ark-guide/3.2.1 图片理解 - 第1部分.md` |
| 3.2.1 | 图片理解 - 第2部分·代码示例 | 169-194 | 8593-9645 | 903 | `chapters/volcengine/ark-guide/3.2.1 图片理解 - 第2部分·代码示例.md` |
| 3.2.2 | 视频理解 - 第1部分 | 195-235 | 9646-11337 | 1494 | `chapters/volcengine/ark-guide/3.2.2 视频理解 - 第1部分.md` |
| 3.2.2 | 视频理解 - 第2部分 | 236-248 | 11338-11888 | 484 | `chapters/volcengine/ark-guide/3.2.2 视频理解 - 第2部分.md` |
| 3.2.3 | 文档理解 | 249-277 | 11889-13075 | 1051 | `chapters/volcengine/ark-guide/3.2.3 文档理解.md` |
| 3.2.4 | 音频理解 - 第1部分 | 278-331 | 13076-15292 | 1903 | `chapters/volcengine/ark-guide/3.2.4 音频理解 - 第1部分.md` |
| 3.3.1 | Doubao Seedance 2.5 教程 - 第1部分 | 332-373 | 15293-17088 | 1494 | `chapters/volcengine/ark-guide/3.3.1 Doubao Seedance 2.5 教程 - 第1部分.md` |
| 3.3.1 | Doubao Seedance 2.5 教程 - 第2部分 | 374-414 | 17089-18812 | 1384 | `chapters/volcengine/ark-guide/3.3.1 Doubao Seedance 2.5 教程 - 第2部分.md` |
| 3.3.2 | Doubao Seedance 2.5 提示词指南 | 415-483 | 18813-20398 | 939 | `chapters/volcengine/ark-guide/3.3.2 Doubao Seedance 2.5 提示词指南.md` |
| 3.3.3 | Doubao Seedance 2.0 系列教程 - 第1部分 | 484-531 | 20399-22378 | 1727 | `chapters/volcengine/ark-guide/3.3.3 Doubao Seedance 2.0 系列教程 - 第1部分.md` |
| 3.3.4 | Doubao Seedance 2.0 系列提示词指南 | 532-581 | 22379-23176 | 512 | `chapters/volcengine/ark-guide/3.3.4 Doubao Seedance 2.0 系列提示词指南.md` |
| 3.3.5 | 视频生成教程 - 第1部分 | 582-621 | 23177-24857 | 1532 | `chapters/volcengine/ark-guide/3.3.5 视频生成教程 - 第1部分.md` |
| 3.3.5 | 视频生成教程 - 第2部分 | 622-641 | 24858-25643 | 644 | `chapters/volcengine/ark-guide/3.3.5 视频生成教程 - 第2部分.md` |
| 3.3.6 | Doubao Seedance 便利创作含肖像视频 | 642-659 | 25644-26365 | 634 | `chapters/volcengine/ark-guide/3.3.6 Doubao Seedance 便利创作含肖像视频.md` |
| 3.4.1 | Doubao Seedream 5.0 pro / flash 教程 | 660-690 | 26367-27489 | 939 | `chapters/volcengine/ark-guide/3.4.1 Doubao Seedream 5.0 pro - flash 教程.md` |
| 3.4.2 | Doubao Seedream 5.0 pro / flash 实现交互编辑指南 | 691-700 | 27490-27857 | 298 | `chapters/volcengine/ark-guide/3.4.2 Doubao Seedream 5.0 pro - flash 实现交互编辑指南.md` |
| 3.4.3 | 图片生成教程 - 第1部分 | 701-743 | 27858-29545 | 1482 | `chapters/volcengine/ark-guide/3.4.3 图片生成教程 - 第1部分.md` |
| 3.4.3 | 图片生成教程 - 第2部分 | 744-759 | 29546-30336 | 681 | `chapters/volcengine/ark-guide/3.4.3 图片生成教程 - 第2部分.md` |
| 3.5 | 决策评估（beta） | 760-770 | 30337-30807 | 405 | `chapters/volcengine/ark-guide/3.5 决策评估（beta）.md` |
| 3.6.1 | 3D 生成 | 771-780 | 30809-31220 | 350 | `chapters/volcengine/ark-guide/3.6.1 3D 生成.md` |
| 3.6.2 | 向量化 | 781-804 | 31221-32261 | 856 | `chapters/volcengine/ark-guide/3.6.2 向量化.md` |
| 3.7.1 | 工具概述 | 805-811 | 32263-32557 | 257 | `chapters/volcengine/ark-guide/3.7.1 工具概述.md` |
| 3.7.2 | 豆包助手 | 805-832 | 32558-33514 | 791 | `chapters/volcengine/ark-guide/3.7.2 豆包助手.md` |
| 3.7.3 | 联网搜索工具 | 833-851 | 33515-34308 | 655 | `chapters/volcengine/ark-guide/3.7.3 联网搜索工具.md` |
| 3.7.4 | Image Process（图像处理） | 852-878 | 34309-35308 | 906 | `chapters/volcengine/ark-guide/3.7.4 Image Process（图像处理）.md` |
| 3.7.5 | 私域知识库搜索 Knowledge Search | 879-884 | 35309-35496 | 146 | `chapters/volcengine/ark-guide/3.7.5 私域知识库搜索 Knowledge Search.md` |
| 3.7.6 | 云部署 MCP / Remote MCP | 885-901 | 35497-36144 | 580 | `chapters/volcengine/ark-guide/3.7.6 云部署 MCP - Remote MCP.md` |
| 3.7.7 | Function Calling（函数调用） - 第1部分 | 902-945 | 36145-37931 | 1551 | `chapters/volcengine/ark-guide/3.7.7 Function Calling（函数调用） - 第1部分.md` |
| 3.7.8 | Apply Patch（代码补丁工具） | 946-962 | 37932-38672 | 321 | `chapters/volcengine/ark-guide/3.7.8 Apply Patch（代码补丁工具）.md` |
| 3.8.1 | 深度思考 | 963-986 | 38674-39748 | 947 | `chapters/volcengine/ark-guide/3.8.1 深度思考.md` |
| 3.8.2 | 上下文管理 | 987-1018 | 39749-41107 | 1187 | `chapters/volcengine/ark-guide/3.8.2 上下文管理.md` |
| 3.8.3 | 流式输出 | 1019-1044 | 41108-42236 | 1001 | `chapters/volcengine/ark-guide/3.8.3 流式输出.md` |
| 3.8.4 | 续写模式 | 1045-1053 | 42237-42661 | 379 | `chapters/volcengine/ark-guide/3.8.4 续写模式.md` |
| 3.8.5 | 上下文缓存 | 1054-1085 | 42662-44010 | 1120 | `chapters/volcengine/ark-guide/3.8.5 上下文缓存.md` |
| 3.8.6 | 文件输入(Files API) | 1086-1121 | 44011-45416 | 1269 | `chapters/volcengine/ark-guide/3.8.6 文件输入(Files API).md` |
| 3.8.7 | GUI Agent 能力 | 1122-1132 | 45417-45814 | 317 | `chapters/volcengine/ark-guide/3.8.7 GUI Agent 能力.md` |
| 3.8.8 | 视觉定位 Grounding | 1133-1139 | 45815-46058 | 223 | `chapters/volcengine/ark-guide/3.8.8 视觉定位 Grounding.md` |
| 3.8.9 | 提示词工程 | 1140-1144 | 46059-46276 | 152 | `chapters/volcengine/ark-guide/3.8.9 提示词工程.md` |
| 3.8.10 | 结构化输出(beta) | 1145-1167 | 46277-47194 | 818 | `chapters/volcengine/ark-guide/3.8.10 结构化输出(beta).md` |
| 3.9 | 接入三方工具 | 1168-1196 | 47195-48078 | 647 | `chapters/volcengine/ark-guide/3.9 接入三方工具.md` |
| 3.10.1 | 迁移至 Responses API | 1197-1209 | 48080-48776 | 618 | `chapters/volcengine/ark-guide/3.10.1 迁移至 Responses API.md` |
| 3.10.2 | 文本生成 | 1210-1247 | 48777-50303 | 1331 | `chapters/volcengine/ark-guide/3.10.2 文本生成.md` |
| 3.10.3 | 深度思考 | 1248-1270 | 50304-51344 | 847 | `chapters/volcengine/ark-guide/3.10.3 深度思考.md` |
| 3.10.4 | 多模态理解 | 1271-1298 | 51345-52501 | 1039 | `chapters/volcengine/ark-guide/3.10.4 多模态理解.md` |
| 3.10.5 | 工具调用 | 1299-1310 | 52502-53020 | 458 | `chapters/volcengine/ark-guide/3.10.5 工具调用.md` |
| 3.10.6 | 结构化输出(beta) | 1311-1319 | 53021-53377 | 320 | `chapters/volcengine/ark-guide/3.10.6 结构化输出(beta).md` |
| 3.10.7 | 上下文编辑 | 1320-1325 | 53378-53627 | 218 | `chapters/volcengine/ark-guide/3.10.7 上下文编辑.md` |
| 4.1 | 推理方式概述 | 1320-1330 | 53629-54273 | 574 | `chapters/volcengine/ark-guide/4.1 推理方式概述.md` |
| 4.2 | 在线推理（常规） | 1331-1332 | 54274-54336 | 43 | `chapters/volcengine/ark-guide/4.2 在线推理（常规）.md` |
| 4.3 | 在线推理（低延迟） | 1333-1338 | 54337-54539 | 117 | `chapters/volcengine/ark-guide/4.3 在线推理（低延迟）.md` |
| 4.4 | 在线推理（低优） | 1339-1346 | 54540-54833 | 183 | `chapters/volcengine/ark-guide/4.4 在线推理（低优）.md` |
| 4.5 | 在线推理（TPM 保障包） | 1347-1354 | 54834-55104 | 187 | `chapters/volcengine/ark-guide/4.5 在线推理（TPM 保障包）.md` |
| 4.6.1 | 模型单元概述 | 1355-1356 | 55106-55193 | 46 | `chapters/volcengine/ark-guide/4.6.1 模型单元概述.md` |
| 4.6.2 | 创建模型单元 | 1357-1359 | 55194-55297 | 62 | `chapters/volcengine/ark-guide/4.6.2 创建模型单元.md` |
| 4.6.3 | 管理模型单元 | 1360 | 55298-55328 | 17 | `chapters/volcengine/ark-guide/4.6.3 管理模型单元.md` |
| 4.7 | 批量推理 | 1361-1394 | 55329-56820 | 1222 | `chapters/volcengine/ark-guide/4.7 批量推理.md` |
| 4.8.1 | 智能模型路由 | 1395-1399 | 56822-56970 | 85 | `chapters/volcengine/ark-guide/4.8.1 智能模型路由.md` |
| 4.8.2 | 使用 MLP 推理服务 | 1400-1406 | 56971-57232 | 196 | `chapters/volcengine/ark-guide/4.8.2 使用 MLP 推理服务.md` |
| 4.8.3 | 使用自定义模型进行推理 | 1407-1409 | 57233-57366 | 75 | `chapters/volcengine/ark-guide/4.8.3 使用自定义模型进行推理.md` |
| 5.1.1 | 模型精调概述 | 1410-1415 | 57369-57747 | 322 | `chapters/volcengine/ark-guide/5.1.1 模型精调概述.md` |
| 5.1.2 | 有监督微调最佳实践 | 1416-1429 | 57748-58365 | 207 | `chapters/volcengine/ark-guide/5.1.2 有监督微调最佳实践.md` |
| 5.1.3 | 直接偏好优化最佳实践 | 1430-1439 | 58366-58798 | 292 | `chapters/volcengine/ark-guide/5.1.3 直接偏好优化最佳实践.md` |
| 5.1.4 | 强化学习最佳实践 | 1440-1467 | 58799-59897 | 865 | `chapters/volcengine/ark-guide/5.1.4 强化学习最佳实践.md` |
| 5.1.5 | Plugin 异常处理 | 1468-1470 | 59898-60039 | 99 | `chapters/volcengine/ark-guide/5.1.5 Plugin 异常处理.md` |
| 5.1.6 | 精调 SDK 使用指南 | 1468-1504 | 60040-61633 | 1332 | `chapters/volcengine/ark-guide/5.1.6 精调 SDK 使用指南.md` |
| 5.1.7.1 | 格式总览 | 1505-1506 | 61635-61688 | 38 | `chapters/volcengine/ark-guide/5.1.7.1 格式总览.md` |
| 5.1.7.2 | 语言及多模态理解模型精调数据格式 - 第1部分 | 1505-1553 | 61689-63950 | 1936 | `chapters/volcengine/ark-guide/5.1.7.2 语言及多模态理解模型精调数据格式 - 第1部分.md` |
| 5.1.7.2 | 语言及多模态理解模型精调数据格式 - 第2部分·注意事项 | 1554-1555 | 63951-64043 | 60 | `chapters/volcengine/ark-guide/5.1.7.2 语言及多模态理解模型精调数据格式 - 第2部分·注意事项.md` |
| 5.1.7.3 | 图片生成模型精调数据格式 | 1556-1563 | 64044-64394 | 293 | `chapters/volcengine/ark-guide/5.1.7.3 图片生成模型精调数据格式.md` |
| 5.1.7.4 | 视频生成模型精调数据格式 | 1564-1566 | 64395-64491 | 88 | `chapters/volcengine/ark-guide/5.1.7.4 视频生成模型精调数据格式.md` |
| 5.1.8 | 管理自定义模型 | 1567-1569 | 64492-64582 | 54 | `chapters/volcengine/ark-guide/5.1.8 管理自定义模型.md` |
| 5.2.1 | 创建模型评测任务 | 1570-1575 | 64584-64649 | 31 | `chapters/volcengine/ark-guide/5.2.1 创建模型评测任务.md` |
| 5.2.2 | 查看并管理模型评测任务 | 1576-1578 | 64650-64669 | 11 | `chapters/volcengine/ark-guide/5.2.2 查看并管理模型评测任务.md` |
| 5.2.3 | 评测数据集格式说明 | 1579-1595 | 64670-65576 | 835 | `chapters/volcengine/ark-guide/5.2.3 评测数据集格式说明.md` |
| 5.2.4.1 | 人工评测作业 | 1596-1605 | 65578-65631 | 28 | `chapters/volcengine/ark-guide/5.2.4.1 人工评测作业.md` |
| 5.2.4.2 | 查看评测报告 | 1606-1610 | 65632-65741 | 61 | `chapters/volcengine/ark-guide/5.2.4.2 查看评测报告.md` |
| 5.3.1 | 数据集介绍 | 1611-1616 | 65743-65853 | 74 | `chapters/volcengine/ark-guide/5.3.1 数据集介绍.md` |
| 5.3.2 | 共享数据集 | 1617-1622 | 65854-65900 | 24 | `chapters/volcengine/ark-guide/5.3.2 共享数据集.md` |
| 6.1.1 | 概述 | 1623-1626 | 65903-66064 | 117 | `chapters/volcengine/ark-guide/6.1.1 概述.md` |
| 6.1.2 | 快速入门（代码） | 1627-1642 | 66065-66721 | 596 | `chapters/volcengine/ark-guide/6.1.2 快速入门（代码）.md` |
| 6.1.3 | 快速入门（控制台） | 1643-1645 | 66722-66820 | 57 | `chapters/volcengine/ark-guide/6.1.3 快速入门（控制台）.md` |
| 6.2.1 | Agent | 1646-1651 | 66822-67072 | 203 | `chapters/volcengine/ark-guide/6.2.1 Agent.md` |
| 6.2.2 | Skills | 1652-1656 | 67073-67221 | 107 | `chapters/volcengine/ark-guide/6.2.2 Skills.md` |
| 6.2.3 | MCP | 1657-1660 | 67222-67372 | 126 | `chapters/volcengine/ark-guide/6.2.3 MCP.md` |
| 6.2.4 | Tools | 1661-1675 | 67373-68006 | 486 | `chapters/volcengine/ark-guide/6.2.4 Tools.md` |
| 6.2.5 | 工具权限策略 | 1676-1679 | 68007-68162 | 135 | `chapters/volcengine/ark-guide/6.2.5 工具权限策略.md` |
| 6.2.6 | 模型支持的参数列表 | 1680-1682 | 68163-68325 | 140 | `chapters/volcengine/ark-guide/6.2.6 模型支持的参数列表.md` |
| 6.3.1 | 配置云环境 | 1683-1688 | 68327-68589 | 206 | `chapters/volcengine/ark-guide/6.3.1 配置云环境.md` |
| 6.3.2 | 云沙箱参考 | 1689-1692 | 68590-68745 | 128 | `chapters/volcengine/ark-guide/6.3.2 云沙箱参考.md` |
| 6.3.3.1 | 自托管环境概述 | 1693-1697 | 68747-68950 | 120 | `chapters/volcengine/ark-guide/6.3.3.1 自托管环境概述.md` |
| 6.3.3.2 | 配置并运行自托管环境 | 1698-1712 | 68951-69535 | 476 | `chapters/volcengine/ark-guide/6.3.3.2 配置并运行自托管环境.md` |
| 6.3.3.3 | 自托管环境安全说明 | 1713-1719 | 69536-69830 | 186 | `chapters/volcengine/ark-guide/6.3.3.3 自托管环境安全说明.md` |
| 6.4.1 | 启动 Session | 1720-1734 | 69832-70457 | 509 | `chapters/volcengine/ark-guide/6.4.1 启动 Session.md` |
| 6.4.2 | 管理 Session | 1735-1740 | 70458-70687 | 170 | `chapters/volcengine/ark-guide/6.4.2 管理 Session.md` |
| 6.4.3 | Session 事件流 | 1741-1762 | 70688-71588 | 736 | `chapters/volcengine/ark-guide/6.4.3 Session 事件流.md` |
| 6.4.4 | 使用 Webhook 接收事件通知 | 1763-1775 | 71589-72103 | 387 | `chapters/volcengine/ark-guide/6.4.4 使用 Webhook 接收事件通知.md` |
| 6.4.5 | 使用 Vaults 认证 | 1776-1783 | 72104-72448 | 246 | `chapters/volcengine/ark-guide/6.4.5 使用 Vaults 认证.md` |
| 6.4.6 | 运行和管理后台工具任务 | 1784-1789 | 72449-72678 | 155 | `chapters/volcengine/ark-guide/6.4.6 运行和管理后台工具任务.md` |
| 6.5.1 | 上传与挂载文件 | 1790-1796 | 72680-72920 | 186 | `chapters/volcengine/ark-guide/6.5.1 上传与挂载文件.md` |
| 6.5.2 | 持久化记忆 | 1797-1801 | 72921-73086 | 122 | `chapters/volcengine/ark-guide/6.5.2 持久化记忆.md` |
| 6.5.3 | 使用 Dream 整理长期记忆 | 1802-1811 | 73087-73460 | 274 | `chapters/volcengine/ark-guide/6.5.3 使用 Dream 整理长期记忆.md` |
| 6.5.4 | 配置上下文压缩 | 1812-1814 | 73461-73592 | 79 | `chapters/volcengine/ark-guide/6.5.4 配置上下文压缩.md` |
| 6.6.1 | 编排 Multi Agent | 1815-1831 | 73594-74222 | 533 | `chapters/volcengine/ark-guide/6.6.1 编排 Multi Agent.md` |
| 7.1 | 将零代码应用迁移至 Managed Agents | 1832-1839 | 74224-74564 | 239 | `chapters/volcengine/ark-guide/7.1 将零代码应用迁移至 Managed Agents.md` |
| 7.2 | 知识库 | 1840 | 74565-74583 | 10 | `chapters/volcengine/ark-guide/7.2 知识库.md` |
| 8.1.1 | 套餐概览 | 1841-1849 | 74586-74916 | 241 | `chapters/volcengine/ark-guide/8.1.1 套餐概览.md` |
| 8.1.2 | 快速开始 | 1850-1857 | 74917-75157 | 173 | `chapters/volcengine/ark-guide/8.1.2 快速开始.md` |
| 8.1.3.1 | Codex | 1858-1867 | 75159-75438 | 199 | `chapters/volcengine/ark-guide/8.1.3.1 Codex.md` |
| 8.1.3.2 | Claude Code | 1868-1879 | 75439-75815 | 237 | `chapters/volcengine/ark-guide/8.1.3.2 Claude Code.md` |
| 8.1.3.3 | OpenCode | 1880-1895 | 75816-76476 | 577 | `chapters/volcengine/ark-guide/8.1.3.3 OpenCode.md` |
| 8.1.3.4 | OpenClaw | 1896-1914 | 76477-77209 | 602 | `chapters/volcengine/ark-guide/8.1.3.4 OpenClaw.md` |
| 8.1.3.5 | Hermes Agent | 1915-1921 | 77210-77426 | 144 | `chapters/volcengine/ark-guide/8.1.3.5 Hermes Agent.md` |
| 8.1.3.6 | TRAE | 1922-1924 | 77427-77513 | 54 | `chapters/volcengine/ark-guide/8.1.3.6 TRAE.md` |
| 8.1.3.7 | WorkBuddy | 1925-1931 | 77514-77652 | 82 | `chapters/volcengine/ark-guide/8.1.3.7 WorkBuddy.md` |
| 8.1.3.8 | ZCode | 1932-1943 | 77653-78048 | 323 | `chapters/volcengine/ark-guide/8.1.3.8 ZCode.md` |
| 8.1.3.9 | DeepSeek Harness | 1944-1951 | 78049-78253 | 115 | `chapters/volcengine/ark-guide/8.1.3.9 DeepSeek Harness.md` |
| 8.1.3.10 | Pi | 1952-1959 | 78254-78496 | 187 | `chapters/volcengine/ark-guide/8.1.3.10 Pi.md` |
| 8.1.3.11 | OpenViking | 1960-1967 | 78497-78772 | 214 | `chapters/volcengine/ark-guide/8.1.3.11 OpenViking.md` |
| 8.1.3.12 | 其他工具 | 1968-1971 | 78773-78898 | 80 | `chapters/volcengine/ark-guide/8.1.3.12 其他工具.md` |
| 8.1.4.1 | ArkClaw | 1972-1973 | 78900-78961 | 32 | `chapters/volcengine/ark-guide/8.1.4.1 ArkClaw.md` |
| 8.1.4.2 | 记忆增强-Embedding模型 | 1974-1976 | 78962-79077 | 87 | `chapters/volcengine/ark-guide/8.1.4.2 记忆增强-Embedding模型.md` |
| 8.1.5 | Ark CLI：Coding Plan 个人版使用指南 | 1977-1980 | 79078-79170 | 74 | `chapters/volcengine/ark-guide/8.1.5 Ark CLI：Coding Plan 个人版使用指南.md` |
| 8.1.6 | 常见问题 | 1981-1993 | 79171-79635 | 341 | `chapters/volcengine/ark-guide/8.1.6 常见问题.md` |
| 8.1.7.1 | 限时邀请活动 | 1994-1995 | 79637-79703 | 36 | `chapters/volcengine/ark-guide/8.1.7.1 限时邀请活动.md` |
| 8.1.7.2 | Coding Plan Lite & Pro 套餐 2.5 折普惠活动 | 1996-1997 | 79704-79781 | 52 | `chapters/volcengine/ark-guide/8.1.7.2 Coding Plan Lite & Pro 套餐 2.5 折普惠活动.md` |
| 8.1.7.3 | Agent/Coding Plan 指定模型抵扣系数限时折扣活动 | 1998-2000 | 79782-79894 | 88 | `chapters/volcengine/ark-guide/8.1.7.3 Agent-Coding Plan 指定模型抵扣系数限时折扣活动.md` |
| 8.1.7.4 | Coding Plan Pro 套餐赠送 ArkClaw 活动下线公告 | 2001 | 79895-79926 | 21 | `chapters/volcengine/ark-guide/8.1.7.4 Coding Plan Pro 套餐赠送 ArkClaw 活动下线公告.md` |
| 8.1.7.5 | 功能发布公告 | 2002-2006 | 79927-80145 | 189 | `chapters/volcengine/ark-guide/8.1.7.5 功能发布公告.md` |
| 8.1.7.6 | 模型上线公告 | 2007-2013 | 80146-80485 | 314 | `chapters/volcengine/ark-guide/8.1.7.6 模型上线公告.md` |
| 8.1.7.7 | 模型下线公告 | 2014-2021 | 80486-80802 | 247 | `chapters/volcengine/ark-guide/8.1.7.7 模型下线公告.md` |
| 9.1.1.1 | [基础] 构建连续对话的工单分诊助手 | 2022-2036 | 80806-81412 | 527 | `chapters/volcengine/ark-guide/9.1.1.1 [基础] 构建连续对话的工单分诊助手.md` |
| 9.1.1.2 | [基础] 工单分诊 Agent 系统提示词版本管理 | 2037-2043 | 81413-81675 | 193 | `chapters/volcengine/ark-guide/9.1.1.2 [基础] 工单分诊 Agent 系统提示词版本管理.md` |
| 9.1.1.3 | [基础] Custom Tool 使用教程 | 2044-2066 | 81676-82655 | 828 | `chapters/volcengine/ark-guide/9.1.1.3 [基础] Custom Tool 使用教程.md` |
| 9.1.1.4 | [基础] 使用 Viking 知识库检索构建知识问答 Agent | 2067-2074 | 82656-82839 | 106 | `chapters/volcengine/ark-guide/9.1.1.4 [基础] 使用 Viking 知识库检索构建知识问答 Agent.md` |
| 9.1.1.5 | [基础] 在豆包工作中使用 Managed Agents | 2075-2079 | 82840-83038 | 139 | `chapters/volcengine/ark-guide/9.1.1.5 [基础] 在豆包工作中使用 Managed Agents.md` |
| 9.1.1.6 | [基础] 使用 Seedance Managed Agent 生成图片和视频 | 2080-2105 | 83039-84108 | 926 | `chapters/volcengine/ark-guide/9.1.1.6 [基础] 使用 Seedance Managed Agent 生成图片和视频.md` |
| 9.1.1.7 | [进阶] 构建可持续迭代的 AI 研究交付工作台 | 2106-2118 | 84109-84608 | 410 | `chapters/volcengine/ark-guide/9.1.1.7 [进阶] 构建可持续迭代的 AI 研究交付工作台.md` |
| 9.1.1.8 | [进阶] 构建从 CSV 到交互式报告的数据分析 Agent | 2119-2134 | 84609-85225 | 526 | `chapters/volcengine/ark-guide/9.1.1.8 [进阶] 构建从 CSV 到交互式报告的数据分析 Agent.md` |
| 9.1.1.9 | [进阶] 使用 Vaults 让开发 Agent 以用户身份提交 | 2135-2151 | 85226-85892 | 577 | `chapters/volcengine/ark-guide/9.1.1.9 [进阶] 使用 Vaults 让开发 Agent 以用户身份提交.md` |
| 9.1.1.10 | [进阶] 使用 Memory Store 构建有记忆的购物助手 | 2152-2167 | 85893-86491 | 521 | `chapters/volcengine/ark-guide/9.1.1.10 [进阶] 使用 Memory Store 构建有记忆的购物助手.md` |
| 9.1.1.11 | [进阶] 用多智能体团队生成定制销售提案 | 2168-2194 | 86492-87607 | 1005 | `chapters/volcengine/ark-guide/9.1.1.11 [进阶] 用多智能体团队生成定制销售提案.md` |
| 9.1.1.12 | [进阶] 使用 arkcli 构建集成 Vault 与 Memory 的投研 | 2195-2204 | 87608-87961 | 254 | `chapters/volcengine/ark-guide/9.1.1.12 [进阶] 使用 arkcli 构建集成 Vault 与 Memory 的投研.md` |
| 9.1.2 | 快速入门(新手版) | 2205-2208 | 87962-88124 | 96 | `chapters/volcengine/ark-guide/9.1.2 快速入门(新手版).md` |
| 9.1.3 | Seedance 1.0 系列提示词指南 | 2209-2225 | 88125-88470 | 292 | `chapters/volcengine/ark-guide/9.1.3 Seedance 1.0 系列提示词指南.md` |
| 9.1.4 | Seedream 4.0-5.0 提示词指南 | 2226-2237 | 88471-88727 | 197 | `chapters/volcengine/ark-guide/9.1.4 Seedream 4.0-5.0 提示词指南.md` |
| 9.1.5 | Seedream 4.0 助力 Seedance 生视频最佳实践 | 2238-2250 | 88728-88964 | 185 | `chapters/volcengine/ark-guide/9.1.5 Seedream 4.0 助力 Seedance 生视频最佳实践.md` |
| 9.1.6 | RAG（检索增强）解决方案 | 2251-2252 | 88965-89016 | 26 | `chapters/volcengine/ark-guide/9.1.6 RAG（检索增强）解决方案.md` |
| 9.1.7 | 数据回流操作流程 | 2253-2261 | 89017-89131 | 63 | `chapters/volcengine/ark-guide/9.1.7 数据回流操作流程.md` |
| 9.1.8 | 强化学习最佳实践 | 2262-2296 | 89132-90236 | 802 | `chapters/volcengine/ark-guide/9.1.8 强化学习最佳实践.md` |
| 9.1.9 | 如何设置控制台登录保持时间 | 2297 | 90237-90253 | 8 | `chapters/volcengine/ark-guide/9.1.9 如何设置控制台登录保持时间.md` |
| 9.1.10 | 角色扮演场景提示词指南 | 2298-2323 | 90254-91120 | 688 | `chapters/volcengine/ark-guide/9.1.10 角色扮演场景提示词指南.md` |
| 9.1.11 | 机密部署最佳实践 | 2324-2329 | 91121-91258 | 86 | `chapters/volcengine/ark-guide/9.1.11 机密部署最佳实践.md` |
| 9.1.12 | 环境变量配置指南 | 2330-2335 | 91259-91440 | 131 | `chapters/volcengine/ark-guide/9.1.12 环境变量配置指南.md` |
| 9.1.13 | 突发流量处理最佳实践 | 2336-2362 | 91441-92506 | 909 | `chapters/volcengine/ark-guide/9.1.13 突发流量处理最佳实践.md` |
| 9.1.14 | 火山方舟分账最佳实践 | 2363-2371 | 92507-92731 | 108 | `chapters/volcengine/ark-guide/9.1.14 火山方舟分账最佳实践.md` |
| 9.1.15 | 在应用中使用 RTC 实现 AI 实时对话 | 2372-2376 | 92732-92883 | 119 | `chapters/volcengine/ark-guide/9.1.15 在应用中使用 RTC 实现 AI 实时对话.md` |
| 9.1.16 | 通过 TOS 内网预签名 URL 传入文件 | 2377-2379 | 92884-93000 | 93 | `chapters/volcengine/ark-guide/9.1.16 通过 TOS 内网预签名 URL 传入文件.md` |
| 9.1.17 | 用量明细 CSV 解析最佳实践 | 2380-2388 | 93001-93335 | 283 | `chapters/volcengine/ark-guide/9.1.17 用量明细 CSV 解析最佳实践.md` |
