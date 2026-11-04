# 方舟指南区章节表（ark-guide）

来源：《火山方舟 文档指南》（2407 页）。178 个章节文件，接口级切分：一个接口/任务一个文件；超过 1500 行的按语义块自动再拆为`… - 第N部分`（10 个章节被拆分）。

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
| 2.2 | Seed-Evolving | 99-103 | 5662-5850 | 120 | `chapters/volcengine/ark-guide/2.2 Seed-Evolving.md` |
| 2.3 | DeepSeek-V4.1-Flash（升级 1017） | 104-115 | 5851-6442 | 504 | `chapters/volcengine/ark-guide/2.3 DeepSeek-V4.1-Flash（升级 1017）.md` |
| 3.1 | 文本生成 | 116-129 | 6444-7003 | 474 | `chapters/volcengine/ark-guide/3.1 文本生成.md` |
| 3.2.1 | 图片理解 - 第1部分 | 130-168 | 7004-8635 | 1426 | `chapters/volcengine/ark-guide/3.2.1 图片理解 - 第1部分.md` |
| 3.2.1 | 图片理解 - 第2部分·代码示例 | 169-194 | 8636-9688 | 902 | `chapters/volcengine/ark-guide/3.2.1 图片理解 - 第2部分·代码示例.md` |
| 3.2.2 | 视频理解 - 第1部分 | 195-235 | 9689-11380 | 1494 | `chapters/volcengine/ark-guide/3.2.2 视频理解 - 第1部分.md` |
| 3.2.2 | 视频理解 - 第2部分 | 236-248 | 11381-11931 | 484 | `chapters/volcengine/ark-guide/3.2.2 视频理解 - 第2部分.md` |
| 3.2.3 | 文档理解 | 249-277 | 11932-13118 | 1051 | `chapters/volcengine/ark-guide/3.2.3 文档理解.md` |
| 3.2.4 | 音频理解 - 第1部分 | 278-331 | 13119-15335 | 1903 | `chapters/volcengine/ark-guide/3.2.4 音频理解 - 第1部分.md` |
| 3.3.1 | Doubao Seedance 2.5 教程 - 第1部分 | 332-373 | 15336-17131 | 1494 | `chapters/volcengine/ark-guide/3.3.1 Doubao Seedance 2.5 教程 - 第1部分.md` |
| 3.3.1 | Doubao Seedance 2.5 教程 - 第2部分 | 374-414 | 17132-18855 | 1384 | `chapters/volcengine/ark-guide/3.3.1 Doubao Seedance 2.5 教程 - 第2部分.md` |
| 3.3.2 | Doubao Seedance 2.5 提示词指南 | 415-483 | 18856-20441 | 939 | `chapters/volcengine/ark-guide/3.3.2 Doubao Seedance 2.5 提示词指南.md` |
| 3.3.3 | Doubao Seedance 2.0 系列教程 - 第1部分 | 484-532 | 20442-22443 | 1738 | `chapters/volcengine/ark-guide/3.3.3 Doubao Seedance 2.0 系列教程 - 第1部分.md` |
| 3.3.4 | Doubao Seedance 2.0 系列提示词指南 | 533-582 | 22444-23241 | 512 | `chapters/volcengine/ark-guide/3.3.4 Doubao Seedance 2.0 系列提示词指南.md` |
| 3.3.5 | 视频生成教程 - 第1部分 | 583-622 | 23242-24922 | 1532 | `chapters/volcengine/ark-guide/3.3.5 视频生成教程 - 第1部分.md` |
| 3.3.5 | 视频生成教程 - 第2部分 | 623-642 | 24923-25708 | 644 | `chapters/volcengine/ark-guide/3.3.5 视频生成教程 - 第2部分.md` |
| 3.3.6 | Doubao Seedance 便利创作含肖像视频 | 643-661 | 25709-26451 | 652 | `chapters/volcengine/ark-guide/3.3.6 Doubao Seedance 便利创作含肖像视频.md` |
| 3.4.1 | Doubao Seedream 5.0 pro / flash 教程 | 662-692 | 26453-27575 | 939 | `chapters/volcengine/ark-guide/3.4.1 Doubao Seedream 5.0 pro - flash 教程.md` |
| 3.4.2 | Doubao Seedream 5.0 pro / flash 实现交互编辑指南 | 693-702 | 27576-27943 | 298 | `chapters/volcengine/ark-guide/3.4.2 Doubao Seedream 5.0 pro - flash 实现交互编辑指南.md` |
| 3.4.3 | 图片生成教程 - 第1部分 | 703-745 | 27944-29631 | 1482 | `chapters/volcengine/ark-guide/3.4.3 图片生成教程 - 第1部分.md` |
| 3.4.3 | 图片生成教程 - 第2部分 | 746-761 | 29632-30422 | 681 | `chapters/volcengine/ark-guide/3.4.3 图片生成教程 - 第2部分.md` |
| 3.5 | 决策评估（beta） | 762-772 | 30423-30893 | 404 | `chapters/volcengine/ark-guide/3.5 决策评估（beta）.md` |
| 3.6.1 | 3D 生成 | 773-782 | 30895-31306 | 350 | `chapters/volcengine/ark-guide/3.6.1 3D 生成.md` |
| 3.6.2 | 向量化 | 783-806 | 31307-32347 | 856 | `chapters/volcengine/ark-guide/3.6.2 向量化.md` |
| 3.7.1 | 工具概述 | 807-813 | 32349-32643 | 257 | `chapters/volcengine/ark-guide/3.7.1 工具概述.md` |
| 3.7.2 | 豆包助手 | 807-834 | 32644-33590 | 783 | `chapters/volcengine/ark-guide/3.7.2 豆包助手.md` |
| 3.7.3 | 联网搜索工具 | 835-853 | 33591-34384 | 656 | `chapters/volcengine/ark-guide/3.7.3 联网搜索工具.md` |
| 3.7.4 | Image Process（图像处理） | 854-880 | 34385-35384 | 906 | `chapters/volcengine/ark-guide/3.7.4 Image Process（图像处理）.md` |
| 3.7.5 | 私域知识库搜索 Knowledge Search | 881-886 | 35385-35572 | 146 | `chapters/volcengine/ark-guide/3.7.5 私域知识库搜索 Knowledge Search.md` |
| 3.7.6 | 云部署 MCP / Remote MCP | 887-903 | 35573-36220 | 580 | `chapters/volcengine/ark-guide/3.7.6 云部署 MCP - Remote MCP.md` |
| 3.7.7 | Function Calling（函数调用） - 第1部分 | 904-947 | 36221-38023 | 1567 | `chapters/volcengine/ark-guide/3.7.7 Function Calling（函数调用） - 第1部分.md` |
| 3.7.8 | Apply Patch（代码补丁工具） | 948-964 | 38024-38764 | 321 | `chapters/volcengine/ark-guide/3.7.8 Apply Patch（代码补丁工具）.md` |
| 3.8.1 | 深度思考 | 965-988 | 38766-39840 | 947 | `chapters/volcengine/ark-guide/3.8.1 深度思考.md` |
| 3.8.2 | 上下文管理 | 989-1020 | 39841-41199 | 1187 | `chapters/volcengine/ark-guide/3.8.2 上下文管理.md` |
| 3.8.3 | 流式输出 | 1021-1046 | 41200-42326 | 999 | `chapters/volcengine/ark-guide/3.8.3 流式输出.md` |
| 3.8.4 | 续写模式 | 1047-1055 | 42327-42751 | 379 | `chapters/volcengine/ark-guide/3.8.4 续写模式.md` |
| 3.8.5 | 上下文缓存 | 1056-1088 | 42752-44139 | 1156 | `chapters/volcengine/ark-guide/3.8.5 上下文缓存.md` |
| 3.8.6 | 文件输入(Files API) | 1089-1124 | 44140-45548 | 1270 | `chapters/volcengine/ark-guide/3.8.6 文件输入(Files API).md` |
| 3.8.7 | GUI Agent 能力 | 1125-1135 | 45549-45946 | 317 | `chapters/volcengine/ark-guide/3.8.7 GUI Agent 能力.md` |
| 3.8.8 | 视觉定位 Grounding | 1136-1142 | 45947-46190 | 223 | `chapters/volcengine/ark-guide/3.8.8 视觉定位 Grounding.md` |
| 3.8.9 | 提示词工程 | 1143-1147 | 46191-46408 | 152 | `chapters/volcengine/ark-guide/3.8.9 提示词工程.md` |
| 3.8.10 | 结构化输出(beta) | 1148-1170 | 46409-47326 | 818 | `chapters/volcengine/ark-guide/3.8.10 结构化输出(beta).md` |
| 3.9.1 | 迁移至 Responses API | 1171-1183 | 47328-48024 | 618 | `chapters/volcengine/ark-guide/3.9.1 迁移至 Responses API.md` |
| 3.9.2 | 文本生成 | 1184-1221 | 48025-49551 | 1331 | `chapters/volcengine/ark-guide/3.9.2 文本生成.md` |
| 3.9.3 | 深度思考 | 1222-1244 | 49552-50592 | 847 | `chapters/volcengine/ark-guide/3.9.3 深度思考.md` |
| 3.9.4 | 多模态理解 | 1245-1272 | 50593-51749 | 1039 | `chapters/volcengine/ark-guide/3.9.4 多模态理解.md` |
| 3.9.5 | 工具调用 | 1273-1284 | 51750-52268 | 458 | `chapters/volcengine/ark-guide/3.9.5 工具调用.md` |
| 3.9.6 | 结构化输出(beta) | 1285-1293 | 52269-52625 | 320 | `chapters/volcengine/ark-guide/3.9.6 结构化输出(beta).md` |
| 3.9.7 | 上下文编辑 | 1294-1299 | 52626-52875 | 218 | `chapters/volcengine/ark-guide/3.9.7 上下文编辑.md` |
| 3.10.1 | Codex | 1300-1308 | 52877-53095 | 165 | `chapters/volcengine/ark-guide/3.10.1 Codex.md` |
| 3.10.2 | Claude Code | 1309-1316 | 53096-53349 | 176 | `chapters/volcengine/ark-guide/3.10.2 Claude Code.md` |
| 3.10.3 | OpenCode | 1317-1320 | 53350-53489 | 106 | `chapters/volcengine/ark-guide/3.10.3 OpenCode.md` |
| 3.10.4 | OpenClaw | 1321-1326 | 53490-53686 | 155 | `chapters/volcengine/ark-guide/3.10.4 OpenClaw.md` |
| 3.10.5 | Hermes Agent | 1327-1330 | 53687-53803 | 84 | `chapters/volcengine/ark-guide/3.10.5 Hermes Agent.md` |
| 3.10.6 | TRAE | 1331-1333 | 53804-53857 | 30 | `chapters/volcengine/ark-guide/3.10.6 TRAE.md` |
| 3.10.7 | WorkBuddy | 1334-1337 | 53858-53919 | 42 | `chapters/volcengine/ark-guide/3.10.7 WorkBuddy.md` |
| 3.10.8 | ZCode | 1338-1342 | 53920-54060 | 114 | `chapters/volcengine/ark-guide/3.10.8 ZCode.md` |
| 3.10.9 | DeepSeek Harness | 1343-1348 | 54061-54218 | 90 | `chapters/volcengine/ark-guide/3.10.9 DeepSeek Harness.md` |
| 3.10.10 | Pi | 1349-1351 | 54219-54318 | 78 | `chapters/volcengine/ark-guide/3.10.10 Pi.md` |
| 3.10.11 | 其他工具 | 1352-1355 | 54319-54458 | 103 | `chapters/volcengine/ark-guide/3.10.11 其他工具.md` |
| 4.1 | 推理方式概述 | 1352-1360 | 54460-55104 | 574 | `chapters/volcengine/ark-guide/4.1 推理方式概述.md` |
| 4.2 | 在线推理（常规） | 1361-1362 | 55105-55167 | 43 | `chapters/volcengine/ark-guide/4.2 在线推理（常规）.md` |
| 4.3 | 在线推理（低延迟） | 1363-1368 | 55168-55370 | 117 | `chapters/volcengine/ark-guide/4.3 在线推理（低延迟）.md` |
| 4.4 | 在线推理（低优） | 1369-1376 | 55371-55664 | 183 | `chapters/volcengine/ark-guide/4.4 在线推理（低优）.md` |
| 4.5 | 在线推理（TPM 保障包） | 1377-1384 | 55665-55935 | 187 | `chapters/volcengine/ark-guide/4.5 在线推理（TPM 保障包）.md` |
| 4.6.1 | 模型单元概述 | 1385-1386 | 55937-56024 | 46 | `chapters/volcengine/ark-guide/4.6.1 模型单元概述.md` |
| 4.6.2 | 创建模型单元 | 1387-1389 | 56025-56128 | 62 | `chapters/volcengine/ark-guide/4.6.2 创建模型单元.md` |
| 4.6.3 | 管理模型单元 | 1390 | 56129-56159 | 17 | `chapters/volcengine/ark-guide/4.6.3 管理模型单元.md` |
| 4.7 | 批量推理 | 1391-1424 | 56160-57650 | 1224 | `chapters/volcengine/ark-guide/4.7 批量推理.md` |
| 4.8.1 | 智能模型路由 | 1425-1429 | 57652-57800 | 85 | `chapters/volcengine/ark-guide/4.8.1 智能模型路由.md` |
| 4.8.2 | 使用 MLP 推理服务 | 1430-1436 | 57801-58062 | 196 | `chapters/volcengine/ark-guide/4.8.2 使用 MLP 推理服务.md` |
| 4.8.3 | 使用自定义模型进行推理 | 1437-1439 | 58063-58196 | 75 | `chapters/volcengine/ark-guide/4.8.3 使用自定义模型进行推理.md` |
| 5.1.1 | 模型精调概述 | 1440-1445 | 58199-58577 | 322 | `chapters/volcengine/ark-guide/5.1.1 模型精调概述.md` |
| 5.1.2 | 有监督微调最佳实践 | 1446-1459 | 58578-59195 | 207 | `chapters/volcengine/ark-guide/5.1.2 有监督微调最佳实践.md` |
| 5.1.3 | 直接偏好优化最佳实践 | 1460-1469 | 59196-59628 | 292 | `chapters/volcengine/ark-guide/5.1.3 直接偏好优化最佳实践.md` |
| 5.1.4 | 强化学习最佳实践 | 1470-1497 | 59629-60727 | 865 | `chapters/volcengine/ark-guide/5.1.4 强化学习最佳实践.md` |
| 5.1.5 | Plugin 异常处理 | 1498-1500 | 60728-60869 | 99 | `chapters/volcengine/ark-guide/5.1.5 Plugin 异常处理.md` |
| 5.1.6 | 精调 SDK 使用指南 | 1498-1534 | 60870-62463 | 1332 | `chapters/volcengine/ark-guide/5.1.6 精调 SDK 使用指南.md` |
| 5.1.7.1 | 格式总览 | 1535-1536 | 62465-62518 | 38 | `chapters/volcengine/ark-guide/5.1.7.1 格式总览.md` |
| 5.1.7.2 | 语言及多模态理解模型精调数据格式 - 第1部分 | 1535-1583 | 62519-64780 | 1936 | `chapters/volcengine/ark-guide/5.1.7.2 语言及多模态理解模型精调数据格式 - 第1部分.md` |
| 5.1.7.2 | 语言及多模态理解模型精调数据格式 - 第2部分·注意事项 | 1584-1585 | 64781-64873 | 60 | `chapters/volcengine/ark-guide/5.1.7.2 语言及多模态理解模型精调数据格式 - 第2部分·注意事项.md` |
| 5.1.7.3 | 图片生成模型精调数据格式 | 1586-1593 | 64874-65224 | 293 | `chapters/volcengine/ark-guide/5.1.7.3 图片生成模型精调数据格式.md` |
| 5.1.7.4 | 视频生成模型精调数据格式 | 1594-1596 | 65225-65321 | 88 | `chapters/volcengine/ark-guide/5.1.7.4 视频生成模型精调数据格式.md` |
| 5.1.8 | 管理自定义模型 | 1597-1599 | 65322-65412 | 54 | `chapters/volcengine/ark-guide/5.1.8 管理自定义模型.md` |
| 5.2.1 | 创建模型评测任务 | 1600-1605 | 65414-65479 | 31 | `chapters/volcengine/ark-guide/5.2.1 创建模型评测任务.md` |
| 5.2.2 | 查看并管理模型评测任务 | 1606-1608 | 65480-65499 | 11 | `chapters/volcengine/ark-guide/5.2.2 查看并管理模型评测任务.md` |
| 5.2.3 | 评测数据集格式说明 | 1609-1625 | 65500-66403 | 833 | `chapters/volcengine/ark-guide/5.2.3 评测数据集格式说明.md` |
| 5.2.4.1 | 人工评测作业 | 1626-1635 | 66405-66458 | 28 | `chapters/volcengine/ark-guide/5.2.4.1 人工评测作业.md` |
| 5.2.4.2 | 查看评测报告 | 1636-1640 | 66459-66568 | 61 | `chapters/volcengine/ark-guide/5.2.4.2 查看评测报告.md` |
| 5.3.1 | 数据集介绍 | 1641-1646 | 66570-66680 | 74 | `chapters/volcengine/ark-guide/5.3.1 数据集介绍.md` |
| 5.3.2 | 共享数据集 | 1647-1652 | 66681-66727 | 24 | `chapters/volcengine/ark-guide/5.3.2 共享数据集.md` |
| 6.1.1 | 概述 | 1653-1656 | 66730-66891 | 117 | `chapters/volcengine/ark-guide/6.1.1 概述.md` |
| 6.1.2 | 快速入门（代码） | 1657-1672 | 66892-67548 | 596 | `chapters/volcengine/ark-guide/6.1.2 快速入门（代码）.md` |
| 6.1.3 | 快速入门（控制台） | 1673-1675 | 67549-67647 | 57 | `chapters/volcengine/ark-guide/6.1.3 快速入门（控制台）.md` |
| 6.2.1 | Agent | 1676-1682 | 67649-67914 | 213 | `chapters/volcengine/ark-guide/6.2.1 Agent.md` |
| 6.2.2 | Skills | 1683-1687 | 67915-68063 | 107 | `chapters/volcengine/ark-guide/6.2.2 Skills.md` |
| 6.2.3 | MCP | 1688-1691 | 68064-68218 | 127 | `chapters/volcengine/ark-guide/6.2.3 MCP.md` |
| 6.2.4 | Tools | 1692-1706 | 68219-68862 | 490 | `chapters/volcengine/ark-guide/6.2.4 Tools.md` |
| 6.2.5 | 工具权限策略 | 1707-1710 | 68863-69018 | 135 | `chapters/volcengine/ark-guide/6.2.5 工具权限策略.md` |
| 6.2.6 | 模型支持的参数列表 | 1711-1713 | 69019-69181 | 140 | `chapters/volcengine/ark-guide/6.2.6 模型支持的参数列表.md` |
| 6.3.1 | 配置云环境 | 1714-1720 | 69183-69462 | 217 | `chapters/volcengine/ark-guide/6.3.1 配置云环境.md` |
| 6.3.2 | 云沙箱参考 | 1721-1724 | 69463-69618 | 128 | `chapters/volcengine/ark-guide/6.3.2 云沙箱参考.md` |
| 6.3.3.1 | 自托管环境概述 | 1725-1729 | 69620-69835 | 126 | `chapters/volcengine/ark-guide/6.3.3.1 自托管环境概述.md` |
| 6.3.3.2 | 配置并运行自托管环境 | 1730-1744 | 69836-70420 | 476 | `chapters/volcengine/ark-guide/6.3.3.2 配置并运行自托管环境.md` |
| 6.3.3.3 | 自托管环境安全说明 | 1745-1751 | 70421-70715 | 186 | `chapters/volcengine/ark-guide/6.3.3.3 自托管环境安全说明.md` |
| 6.4.1 | 启动 Session | 1752-1766 | 70717-71342 | 509 | `chapters/volcengine/ark-guide/6.4.1 启动 Session.md` |
| 6.4.2 | 管理 Session | 1767-1773 | 71343-71624 | 208 | `chapters/volcengine/ark-guide/6.4.2 管理 Session.md` |
| 6.4.3 | Session 事件流 | 1774-1795 | 71625-72525 | 736 | `chapters/volcengine/ark-guide/6.4.3 Session 事件流.md` |
| 6.4.4 | 使用 Webhook 接收事件通知 | 1796-1808 | 72526-73040 | 387 | `chapters/volcengine/ark-guide/6.4.4 使用 Webhook 接收事件通知.md` |
| 6.4.5 | 使用 Vaults 认证 | 1809-1816 | 73041-73385 | 246 | `chapters/volcengine/ark-guide/6.4.5 使用 Vaults 认证.md` |
| 6.4.6 | 运行和管理后台工具任务 | 1817-1822 | 73386-73615 | 155 | `chapters/volcengine/ark-guide/6.4.6 运行和管理后台工具任务.md` |
| 6.5.1 | 上传与挂载文件 | 1823-1829 | 73617-73860 | 189 | `chapters/volcengine/ark-guide/6.5.1 上传与挂载文件.md` |
| 6.5.2 | 持久化记忆 | 1830-1834 | 73861-74026 | 122 | `chapters/volcengine/ark-guide/6.5.2 持久化记忆.md` |
| 6.5.3 | 使用 Dream 整理长期记忆 | 1835-1844 | 74027-74400 | 274 | `chapters/volcengine/ark-guide/6.5.3 使用 Dream 整理长期记忆.md` |
| 6.5.4 | 配置上下文压缩 | 1845-1847 | 74401-74532 | 79 | `chapters/volcengine/ark-guide/6.5.4 配置上下文压缩.md` |
| 6.6.1 | 编排 Multi Agent | 1848-1864 | 74534-75162 | 533 | `chapters/volcengine/ark-guide/6.6.1 编排 Multi Agent.md` |
| 7.1 | 将零代码应用迁移至 Managed Agents | 1865-1872 | 75164-75504 | 239 | `chapters/volcengine/ark-guide/7.1 将零代码应用迁移至 Managed Agents.md` |
| 7.2 | 知识库 | 1873 | 75505-75523 | 10 | `chapters/volcengine/ark-guide/7.2 知识库.md` |
| 8.1.1 | 套餐概览 | 1874-1882 | 75526-75856 | 241 | `chapters/volcengine/ark-guide/8.1.1 套餐概览.md` |
| 8.1.2 | 快速开始 | 1883-1889 | 75857-76099 | 172 | `chapters/volcengine/ark-guide/8.1.2 快速开始.md` |
| 8.1.3.1 | Codex | 1890-1898 | 76101-76332 | 169 | `chapters/volcengine/ark-guide/8.1.3.1 Codex.md` |
| 8.1.3.2 | Claude Code | 1899-1907 | 76333-76645 | 216 | `chapters/volcengine/ark-guide/8.1.3.2 Claude Code.md` |
| 8.1.3.3 | OpenCode | 1908-1921 | 76646-77265 | 552 | `chapters/volcengine/ark-guide/8.1.3.3 OpenCode.md` |
| 8.1.3.4 | OpenClaw | 1922-1940 | 77266-77972 | 589 | `chapters/volcengine/ark-guide/8.1.3.4 OpenClaw.md` |
| 8.1.3.5 | Hermes Agent | 1941-1946 | 77973-78190 | 147 | `chapters/volcengine/ark-guide/8.1.3.5 Hermes Agent.md` |
| 8.1.3.6 | TRAE | 1947-1948 | 78191-78228 | 20 | `chapters/volcengine/ark-guide/8.1.3.6 TRAE.md` |
| 8.1.3.7 | WorkBuddy | 1949-1954 | 78229-78359 | 78 | `chapters/volcengine/ark-guide/8.1.3.7 WorkBuddy.md` |
| 8.1.3.8 | ZCode | 1955-1964 | 78360-78744 | 320 | `chapters/volcengine/ark-guide/8.1.3.8 ZCode.md` |
| 8.1.3.9 | DeepSeek Harness | 1965-1972 | 78745-78937 | 108 | `chapters/volcengine/ark-guide/8.1.3.9 DeepSeek Harness.md` |
| 8.1.3.10 | Pi | 1973-1978 | 78938-79153 | 175 | `chapters/volcengine/ark-guide/8.1.3.10 Pi.md` |
| 8.1.3.11 | OpenViking | 1979-1985 | 79154-79378 | 178 | `chapters/volcengine/ark-guide/8.1.3.11 OpenViking.md` |
| 8.1.3.12 | 其他工具 | 1986-1989 | 79379-79505 | 86 | `chapters/volcengine/ark-guide/8.1.3.12 其他工具.md` |
| 8.1.4.1 | ArkClaw | 1990-1991 | 79507-79568 | 32 | `chapters/volcengine/ark-guide/8.1.4.1 ArkClaw.md` |
| 8.1.4.2 | 记忆增强-Embedding模型 | 1992-1994 | 79569-79684 | 87 | `chapters/volcengine/ark-guide/8.1.4.2 记忆增强-Embedding模型.md` |
| 8.1.5 | Ark CLI：Coding Plan 个人版使用指南 | 1995-1998 | 79685-79776 | 73 | `chapters/volcengine/ark-guide/8.1.5 Ark CLI：Coding Plan 个人版使用指南.md` |
| 8.1.6 | 常见问题 | 1999-2011 | 79777-80241 | 341 | `chapters/volcengine/ark-guide/8.1.6 常见问题.md` |
| 8.1.7.1 | 限时邀请活动 | 2012-2013 | 80243-80309 | 36 | `chapters/volcengine/ark-guide/8.1.7.1 限时邀请活动.md` |
| 8.1.7.2 | Coding Plan Lite & Pro 套餐 2.5 折普惠活动 | 2014-2015 | 80310-80387 | 52 | `chapters/volcengine/ark-guide/8.1.7.2 Coding Plan Lite & Pro 套餐 2.5 折普惠活动.md` |
| 8.1.7.3 | Agent/Coding Plan 指定模型抵扣系数限时折扣活动 | 2016-2018 | 80388-80499 | 87 | `chapters/volcengine/ark-guide/8.1.7.3 Agent-Coding Plan 指定模型抵扣系数限时折扣活动.md` |
| 8.1.7.4 | Coding Plan Pro 套餐赠送 ArkClaw 活动下线公告 | 2019 | 80500-80531 | 21 | `chapters/volcengine/ark-guide/8.1.7.4 Coding Plan Pro 套餐赠送 ArkClaw 活动下线公告.md` |
| 8.1.7.5 | 功能发布公告 | 2020-2024 | 80532-80750 | 189 | `chapters/volcengine/ark-guide/8.1.7.5 功能发布公告.md` |
| 8.1.7.6 | 模型上线公告 | 2025-2031 | 80751-81090 | 314 | `chapters/volcengine/ark-guide/8.1.7.6 模型上线公告.md` |
| 8.1.7.7 | 模型下线公告 | 2032-2039 | 81091-81407 | 247 | `chapters/volcengine/ark-guide/8.1.7.7 模型下线公告.md` |
| 9.1.1.1 | [基础] 构建连续对话的工单分诊助手 | 2040-2054 | 81411-82017 | 527 | `chapters/volcengine/ark-guide/9.1.1.1 [基础] 构建连续对话的工单分诊助手.md` |
| 9.1.1.2 | [基础] 工单分诊 Agent 系统提示词版本管理 | 2055-2061 | 82018-82280 | 193 | `chapters/volcengine/ark-guide/9.1.1.2 [基础] 工单分诊 Agent 系统提示词版本管理.md` |
| 9.1.1.3 | [基础] Custom Tool 使用教程 | 2062-2084 | 82281-83260 | 828 | `chapters/volcengine/ark-guide/9.1.1.3 [基础] Custom Tool 使用教程.md` |
| 9.1.1.4 | [基础] 使用 Viking 知识库检索构建知识问答 Agent | 2085-2092 | 83261-83444 | 106 | `chapters/volcengine/ark-guide/9.1.1.4 [基础] 使用 Viking 知识库检索构建知识问答 Agent.md` |
| 9.1.1.5 | [基础] 在豆包工作中使用 Managed Agents | 2093-2097 | 83445-83643 | 139 | `chapters/volcengine/ark-guide/9.1.1.5 [基础] 在豆包工作中使用 Managed Agents.md` |
| 9.1.1.6 | [基础] 使用 Seedance Managed Agent 生成图片和视频 | 2098-2123 | 83644-84713 | 926 | `chapters/volcengine/ark-guide/9.1.1.6 [基础] 使用 Seedance Managed Agent 生成图片和视频.md` |
| 9.1.1.7 | [进阶] 构建可持续迭代的 AI 研究交付工作台 | 2124-2136 | 84714-85213 | 410 | `chapters/volcengine/ark-guide/9.1.1.7 [进阶] 构建可持续迭代的 AI 研究交付工作台.md` |
| 9.1.1.8 | [进阶] 构建从 CSV 到交互式报告的数据分析 Agent | 2137-2152 | 85214-85830 | 526 | `chapters/volcengine/ark-guide/9.1.1.8 [进阶] 构建从 CSV 到交互式报告的数据分析 Agent.md` |
| 9.1.1.9 | [进阶] 使用 Vaults 让开发 Agent 以用户身份提交 | 2153-2169 | 85831-86497 | 577 | `chapters/volcengine/ark-guide/9.1.1.9 [进阶] 使用 Vaults 让开发 Agent 以用户身份提交.md` |
| 9.1.1.10 | [进阶] 使用 Memory Store 构建有记忆的购物助手 | 2170-2185 | 86498-87096 | 521 | `chapters/volcengine/ark-guide/9.1.1.10 [进阶] 使用 Memory Store 构建有记忆的购物助手.md` |
| 9.1.1.11 | [进阶] 用多智能体团队生成定制销售提案 | 2186-2212 | 87097-88212 | 1005 | `chapters/volcengine/ark-guide/9.1.1.11 [进阶] 用多智能体团队生成定制销售提案.md` |
| 9.1.1.12 | [进阶] 使用 arkcli 构建集成 Vault 与 Memory 的投研 | 2213-2222 | 88213-88566 | 254 | `chapters/volcengine/ark-guide/9.1.1.12 [进阶] 使用 arkcli 构建集成 Vault 与 Memory 的投研.md` |
| 9.1.2 | 快速入门(新手版) | 2223-2226 | 88567-88729 | 96 | `chapters/volcengine/ark-guide/9.1.2 快速入门(新手版).md` |
| 9.1.3 | Seedance 1.0 系列提示词指南 | 2227-2243 | 88730-89075 | 292 | `chapters/volcengine/ark-guide/9.1.3 Seedance 1.0 系列提示词指南.md` |
| 9.1.4 | Seedream 4.0-5.0 提示词指南 | 2244-2255 | 89076-89332 | 197 | `chapters/volcengine/ark-guide/9.1.4 Seedream 4.0-5.0 提示词指南.md` |
| 9.1.5 | Seedream 4.0 助力 Seedance 生视频最佳实践 | 2256-2268 | 89333-89569 | 185 | `chapters/volcengine/ark-guide/9.1.5 Seedream 4.0 助力 Seedance 生视频最佳实践.md` |
| 9.1.6 | RAG（检索增强）解决方案 | 2269-2270 | 89570-89621 | 26 | `chapters/volcengine/ark-guide/9.1.6 RAG（检索增强）解决方案.md` |
| 9.1.7 | 数据回流操作流程 | 2271-2279 | 89622-89736 | 63 | `chapters/volcengine/ark-guide/9.1.7 数据回流操作流程.md` |
| 9.1.8 | 强化学习最佳实践 | 2280-2314 | 89737-90841 | 802 | `chapters/volcengine/ark-guide/9.1.8 强化学习最佳实践.md` |
| 9.1.9 | 如何设置控制台登录保持时间 | 2315 | 90842-90858 | 8 | `chapters/volcengine/ark-guide/9.1.9 如何设置控制台登录保持时间.md` |
| 9.1.10 | 角色扮演场景提示词指南 | 2316-2341 | 90859-91725 | 688 | `chapters/volcengine/ark-guide/9.1.10 角色扮演场景提示词指南.md` |
| 9.1.11 | 机密部署最佳实践 | 2342-2347 | 91726-91863 | 86 | `chapters/volcengine/ark-guide/9.1.11 机密部署最佳实践.md` |
| 9.1.12 | 环境变量配置指南 | 2348-2353 | 91864-92045 | 131 | `chapters/volcengine/ark-guide/9.1.12 环境变量配置指南.md` |
| 9.1.13 | 突发流量处理最佳实践 | 2354-2380 | 92046-93115 | 911 | `chapters/volcengine/ark-guide/9.1.13 突发流量处理最佳实践.md` |
| 9.1.14 | 火山方舟分账最佳实践 | 2381-2389 | 93116-93340 | 108 | `chapters/volcengine/ark-guide/9.1.14 火山方舟分账最佳实践.md` |
| 9.1.15 | 在应用中使用 RTC 实现 AI 实时对话 | 2390-2394 | 93341-93492 | 119 | `chapters/volcengine/ark-guide/9.1.15 在应用中使用 RTC 实现 AI 实时对话.md` |
| 9.1.16 | 通过 TOS 内网预签名 URL 传入文件 | 2395-2397 | 93493-93609 | 93 | `chapters/volcengine/ark-guide/9.1.16 通过 TOS 内网预签名 URL 传入文件.md` |
| 9.1.17 | 用量明细 CSV 解析最佳实践 | 2398-2407 | 93610-93997 | 331 | `chapters/volcengine/ark-guide/9.1.17 用量明细 CSV 解析最佳实践.md` |
