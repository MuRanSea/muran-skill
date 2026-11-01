# 方舟 API 区章节表（ark）

来源：《火山方舟 API 参考》（2037 页）。219 个章节文件，接口级切分：一个接口/任务一个文件；超过 1500 行的按语义块自动再拆为`… - 第N部分`（5 个章节被拆分）。

「页码」是原 PDF 页码范围；「行范围」是中间 MD（`doc/<源文档>.md`）的 1 起始行号，可据此回查原文。章节文件本身已去掉页眉页脚，回查 PDF 时用这两列。文件名即章节标题，日常定位直接 Glob 文件名即可，用不到这两列。

**这张表用来 grep，不要整读。**

| 编号 | 标题 | 页码 | 行范围(源文件) | 行数 | 文件 |
|------|------|------|---------------|------|------|
| 1.1 | 获取 API Key 并配置 | 1 | 302-337 | 20 | `chapters/volcengine/ark/1.1 获取 API Key 并配置.md` |
| 1.2 | 安装及升级 SDK | 2-7 | 338-496 | 122 | `chapters/volcengine/ark/1.2 安装及升级 SDK.md` |
| 1.3 | Base URL及鉴权 | 8-10 | 497-592 | 68 | `chapters/volcengine/ark/1.3 Base URL及鉴权.md` |
| 2.1 | 对话(Chat) API | 11-71 | 594-2914 | 1246 | `chapters/volcengine/ark/2.1 对话(Chat) API.md` |
| 3.1 | 创建 Response - 第1部分 | 72-128 | 2915-4591 | 1405 | `chapters/volcengine/ark/3.1 创建 Response - 第1部分.md` |
| 3.1 | 创建 Response - 第2部分·响应参数 | 129-197 | 4592-6945 | 1351 | `chapters/volcengine/ark/3.1 创建 Response - 第2部分·响应参数.md` |
| 3.2 | 查询 Response 详情 | 198-244 | 6946-8279 | 1094 | `chapters/volcengine/ark/3.2 查询 Response 详情.md` |
| 3.3 | 查询 Response 输入项列表 | 245-292 | 8280-9862 | 947 | `chapters/volcengine/ark/3.3 查询 Response 输入项列表.md` |
| 3.4 | 删除 Response | 293-294 | 9863-9936 | 34 | `chapters/volcengine/ark/3.4 删除 Response.md` |
| 3.5.1 | Response 生命周期 - 第1部分 | 295-354 | 9937-11660 | 1505 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第1部分.md` |
| 3.5.1 | Response 生命周期 - 第2部分 | 355-413 | 11661-13357 | 1480 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第2部分.md` |
| 3.5.1 | Response 生命周期 - 第3部分 | 414-473 | 13358-15074 | 1502 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第3部分.md` |
| 3.5.1 | Response 生命周期 - 第4部分 | 474-543 | 15075-17084 | 1732 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第4部分.md` |
| 3.5.2 | Output Item 与文本回答 - 第1部分 | 544-601 | 17085-18736 | 1480 | `chapters/volcengine/ark/3.5.2 Output Item 与文本回答 - 第1部分.md` |
| 3.5.2 | Output Item 与文本回答 - 第2部分 | 602-625 | 18737-19366 | 582 | `chapters/volcengine/ark/3.5.2 Output Item 与文本回答 - 第2部分.md` |
| 3.5.3 | 工具调用事件 | 626-667 | 19367-20477 | 1024 | `chapters/volcengine/ark/3.5.3 工具调用事件.md` |
| 3.5.4 | 语音转写与错误事件 | 668-674 | 20478-20652 | 161 | `chapters/volcengine/ark/3.5.4 语音转写与错误事件.md` |
| 4.1 | 创建 Message | 675-702 | 20654-21434 | 579 | `chapters/volcengine/ark/4.1 创建 Message.md` |
| 4.2 | 统计 Messages 请求 token 数 | 703-715 | 21435-21788 | 282 | `chapters/volcengine/ark/4.2 统计 Messages 请求 token 数.md` |
| 5.1 | System One API（beta） | 716-727 | 21790-22117 | 244 | `chapters/volcengine/ark/5.1 System One API（beta）.md` |
| 6.1 | 上传文件 | 728-740 | 22119-22606 | 206 | `chapters/volcengine/ark/6.1 上传文件.md` |
| 6.2 | 查询文件详情 | 741-745 | 22607-22741 | 75 | `chapters/volcengine/ark/6.2 查询文件详情.md` |
| 6.3 | 查询文件列表 | 746-752 | 22742-22971 | 122 | `chapters/volcengine/ark/6.3 查询文件列表.md` |
| 6.4 | 删除文件 | 753-755 | 22972-23044 | 25 | `chapters/volcengine/ark/6.4 删除文件.md` |
| 6.5 | The file object | 756-759 | 23045-23128 | 60 | `chapters/volcengine/ark/6.5 The file object.md` |
| 7.1 | 创建视频生成任务 | 760-801 | 23130-25006 | 837 | `chapters/volcengine/ark/7.1 创建视频生成任务.md` |
| 7.2 | 查询视频生成任务 | 802-808 | 25007-25237 | 125 | `chapters/volcengine/ark/7.2 查询视频生成任务.md` |
| 7.3 | 查询视频生成任务列表 | 809-819 | 25238-25639 | 203 | `chapters/volcengine/ark/7.3 查询视频生成任务列表.md` |
| 7.4 | 取消或删除视频生成任务 | 820-821 | 25640-25728 | 56 | `chapters/volcengine/ark/7.4 取消或删除视频生成任务.md` |
| 8.1 | 图片生成 API | 822-862 | 25730-27453 | 738 | `chapters/volcengine/ark/8.1 图片生成 API.md` |
| 8.2 | 图片生成流式响应事件 | 863-868 | 27454-27632 | 158 | `chapters/volcengine/ark/8.2 图片生成流式响应事件.md` |
| 9.1.1 | 创建 3D 生成任务 API | 869-874 | 27635-27817 | 102 | `chapters/volcengine/ark/9.1.1 创建 3D 生成任务 API.md` |
| 9.1.2 | 查询 3D 生成任务 API | 875-878 | 27818-27952 | 63 | `chapters/volcengine/ark/9.1.2 查询 3D 生成任务 API.md` |
| 9.1.3 | 查询 3D 生成任务列表 | 879-885 | 27953-28178 | 105 | `chapters/volcengine/ark/9.1.3 查询 3D 生成任务列表.md` |
| 9.1.4 | 取消或删除 3D 生成任务 | 886-887 | 28179-28265 | 52 | `chapters/volcengine/ark/9.1.4 取消或删除 3D 生成任务.md` |
| 9.2.1 | 创建3D生成任务 | 888-894 | 28267-28511 | 152 | `chapters/volcengine/ark/9.2.1 创建3D生成任务.md` |
| 9.2.2 | 查询3D生成任务 | 895-897 | 28512-28591 | 52 | `chapters/volcengine/ark/9.2.2 查询3D生成任务.md` |
| 9.2.3 | 查询3D生成任务列表 | 898-901 | 28592-28717 | 85 | `chapters/volcengine/ark/9.2.3 查询3D生成任务列表.md` |
| 9.2.4 | 取消或删除3D生成任务 | 902-903 | 28718-28762 | 34 | `chapters/volcengine/ark/9.2.4 取消或删除3D生成任务.md` |
| 9.3.1 | 创建3D生成任务 | 904-908 | 28764-28908 | 98 | `chapters/volcengine/ark/9.3.1 创建3D生成任务.md` |
| 9.3.2 | 查询3D生成任务 | 909-911 | 28909-28988 | 51 | `chapters/volcengine/ark/9.3.2 查询3D生成任务.md` |
| 9.3.3 | 查询3D生成任务列表 | 912-915 | 28989-29114 | 86 | `chapters/volcengine/ark/9.3.3 查询3D生成任务列表.md` |
| 9.3.4 | 取消或删除3D生成任务 | 916-917 | 29115-29159 | 34 | `chapters/volcengine/ark/9.3.4 取消或删除3D生成任务.md` |
| 10.1 | 多模态向量化 API | 918-928 | 29161-29579 | 201 | `chapters/volcengine/ark/10.1 多模态向量化 API.md` |
| 11.1.1 | 创建智能体 | 929-947 | 29582-30170 | 406 | `chapters/volcengine/ark/11.1.1 创建智能体.md` |
| 11.1.2 | 查询智能体列表 | 948-958 | 30171-30506 | 238 | `chapters/volcengine/ark/11.1.2 查询智能体列表.md` |
| 11.1.3 | 查询智能体详情 | 959-968 | 30507-30795 | 201 | `chapters/volcengine/ark/11.1.3 查询智能体详情.md` |
| 11.1.4 | 更新智能体 | 969-987 | 30796-31434 | 427 | `chapters/volcengine/ark/11.1.4 更新智能体.md` |
| 11.1.5 | 查询智能体版本列表 | 988-998 | 31435-31769 | 222 | `chapters/volcengine/ark/11.1.5 查询智能体版本列表.md` |
| 11.1.6 | 归档智能体 | 999-1007 | 31770-32033 | 203 | `chapters/volcengine/ark/11.1.6 归档智能体.md` |
| 11.1.7 | 删除智能体 | 1008-1009 | 32034-32088 | 21 | `chapters/volcengine/ark/11.1.7 删除智能体.md` |
| 11.2.1 | 创建环境 | 1010-1018 | 32090-32368 | 186 | `chapters/volcengine/ark/11.2.1 创建环境.md` |
| 11.2.2 | 查询环境列表 | 1019-1024 | 32369-32536 | 116 | `chapters/volcengine/ark/11.2.2 查询环境列表.md` |
| 11.2.3 | 查询环境详情 | 1025-1029 | 32537-32683 | 89 | `chapters/volcengine/ark/11.2.3 查询环境详情.md` |
| 11.2.4 | 更新环境 | 1030-1038 | 32684-32967 | 181 | `chapters/volcengine/ark/11.2.4 更新环境.md` |
| 11.2.5 | 归档环境 | 1039-1042 | 32968-33076 | 84 | `chapters/volcengine/ark/11.2.5 归档环境.md` |
| 11.2.6 | 删除环境 | 1043-1044 | 33077-33134 | 25 | `chapters/volcengine/ark/11.2.6 删除环境.md` |
| 11.2.7.1 | 长轮询拉取待执行 Work | 1045-1049 | 33136-33283 | 77 | `chapters/volcengine/ark/11.2.7.1 长轮询拉取待执行 Work.md` |
| 11.2.7.2 | 认领 Work | 1050-1054 | 33284-33428 | 76 | `chapters/volcengine/ark/11.2.7.2 认领 Work.md` |
| 11.2.7.3 | 续租 Work | 1055-1058 | 33429-33542 | 53 | `chapters/volcengine/ark/11.2.7.3 续租 Work.md` |
| 11.2.7.4 | 查询 Work 队列状态 | 1059-1060 | 33543-33610 | 29 | `chapters/volcengine/ark/11.2.7.4 查询 Work 队列状态.md` |
| 11.2.7.5 | 停止 Work | 1061-1065 | 33611-33781 | 90 | `chapters/volcengine/ark/11.2.7.5 停止 Work.md` |
| 11.2.7.6 | 查询 Work 列表 | 1066-1070 | 33782-33941 | 92 | `chapters/volcengine/ark/11.2.7.6 查询 Work 列表.md` |
| 11.2.7.7 | 查询 Work 详情 | 1071-1074 | 33942-34064 | 64 | `chapters/volcengine/ark/11.2.7.7 查询 Work 详情.md` |
| 11.3.1 | 创建会话 | 1075-1113 | 34066-35275 | 905 | `chapters/volcengine/ark/11.3.1 创建会话.md` |
| 11.3.2 | 查询会话列表 | 1114-1139 | 35276-36047 | 602 | `chapters/volcengine/ark/11.3.2 查询会话列表.md` |
| 11.3.3 | 查询会话详情 | 1140-1165 | 36048-36818 | 590 | `chapters/volcengine/ark/11.3.3 查询会话详情.md` |
| 11.3.4 | 更新会话标题和标签 | 1166-1190 | 36819-37563 | 570 | `chapters/volcengine/ark/11.3.4 更新会话标题和标签.md` |
| 11.3.5 | 升级会话 | 1191-1223 | 37564-38535 | 781 | `chapters/volcengine/ark/11.3.5 升级会话.md` |
| 11.3.6 | 归档会话 | 1224-1246 | 38536-39183 | 539 | `chapters/volcengine/ark/11.3.6 归档会话.md` |
| 11.3.7 | 删除会话 | 1247-1248 | 39184-39243 | 27 | `chapters/volcengine/ark/11.3.7 删除会话.md` |
| 11.3.8.1 | 查询会话任务 | 1249-1254 | 39245-39430 | 99 | `chapters/volcengine/ark/11.3.8.1 查询会话任务.md` |
| 11.3.8.2 | 查询会话任务列表 | 1255-1259 | 39431-39601 | 98 | `chapters/volcengine/ark/11.3.8.2 查询会话任务列表.md` |
| 11.3.8.3 | 取消会话任务 | 1260-1262 | 39602-39695 | 36 | `chapters/volcengine/ark/11.3.8.3 取消会话任务.md` |
| 11.3.9.1 | 发送会话事件 | 1263-1266 | 39697-39813 | 53 | `chapters/volcengine/ark/11.3.9.1 发送会话事件.md` |
| 11.3.9.2 | 查询会话事件列表 | 1267-1270 | 39814-39947 | 62 | `chapters/volcengine/ark/11.3.9.2 查询会话事件列表.md` |
| 11.3.9.3 | 流式获取会话事件 | 1271-1275 | 39948-40121 | 50 | `chapters/volcengine/ark/11.3.9.3 流式获取会话事件.md` |
| 11.3.9.4 | 会话事件结构参考 - 第1部分 | 1276-1352 | 40122-42090 | 1748 | `chapters/volcengine/ark/11.3.9.4 会话事件结构参考 - 第1部分.md` |
| 11.3.10.1 | 添加会话资源 | 1353-1356 | 42092-42207 | 51 | `chapters/volcengine/ark/11.3.10.1 添加会话资源.md` |
| 11.3.10.2 | 查询会话资源列表 | 1357-1362 | 42208-42372 | 105 | `chapters/volcengine/ark/11.3.10.2 查询会话资源列表.md` |
| 11.3.10.3 | 查询会话资源 | 1363-1365 | 42373-42467 | 43 | `chapters/volcengine/ark/11.3.10.3 查询会话资源.md` |
| 11.3.11.1 | 查询线程列表 | 1366-1370 | 42469-42608 | 71 | `chapters/volcengine/ark/11.3.11.1 查询线程列表.md` |
| 11.3.11.2 | 查询线程详情 | 1371-1376 | 42609-42793 | 99 | `chapters/volcengine/ark/11.3.11.2 查询线程详情.md` |
| 11.3.11.3 | 查询线程事件列表 | 1377-1380 | 42794-42923 | 57 | `chapters/volcengine/ark/11.3.11.3 查询线程事件列表.md` |
| 11.3.11.4 | 流式获取线程事件 | 1381-1384 | 42924-43058 | 44 | `chapters/volcengine/ark/11.3.11.4 流式获取线程事件.md` |
| 11.4.1 | 创建 Webhook 接入点 | 1385-1388 | 43060-43179 | 64 | `chapters/volcengine/ark/11.4.1 创建 Webhook 接入点.md` |
| 11.4.2 | 查询 Webhook 接入点列表 | 1389-1392 | 43180-43293 | 68 | `chapters/volcengine/ark/11.4.2 查询 Webhook 接入点列表.md` |
| 11.4.3 | 查询 Webhook 接入点详情 | 1393-1395 | 43294-43388 | 53 | `chapters/volcengine/ark/11.4.3 查询 Webhook 接入点详情.md` |
| 11.4.4 | 更新 Webhook 接入点 | 1396-1399 | 43389-43506 | 63 | `chapters/volcengine/ark/11.4.4 更新 Webhook 接入点.md` |
| 11.4.5 | 启用 Webhook 接入点 | 1400-1402 | 43507-43603 | 55 | `chapters/volcengine/ark/11.4.5 启用 Webhook 接入点.md` |
| 11.4.6 | 删除 Webhook 接入点 | 1403 | 43604-43631 | 18 | `chapters/volcengine/ark/11.4.6 删除 Webhook 接入点.md` |
| 11.4.7 | 停用 Webhook 接入点 | 1404-1406 | 43632-43729 | 54 | `chapters/volcengine/ark/11.4.7 停用 Webhook 接入点.md` |
| 11.4.8 | 重置 Webhook 签名密钥 | 1407-1408 | 43730-43764 | 19 | `chapters/volcengine/ark/11.4.8 重置 Webhook 签名密钥.md` |
| 11.4.9 | 发送 Webhook 测试事件 | 1409-1410 | 43765-43809 | 29 | `chapters/volcengine/ark/11.4.9 发送 Webhook 测试事件.md` |
| 11.4.10 | 查询 Webhook 事件详情 | 1411-1412 | 43810-43861 | 35 | `chapters/volcengine/ark/11.4.10 查询 Webhook 事件详情.md` |
| 11.4.11 | 查询 Webhook 事件列表 | 1413-1415 | 43862-43941 | 52 | `chapters/volcengine/ark/11.4.11 查询 Webhook 事件列表.md` |
| 11.4.12 | Webhook 事件结构参考 | 1416-1437 | 43942-44525 | 519 | `chapters/volcengine/ark/11.4.12 Webhook 事件结构参考.md` |
| 11.5.1 | 创建保管库 | 1438-1440 | 44527-44627 | 45 | `chapters/volcengine/ark/11.5.1 创建保管库.md` |
| 11.5.2 | 查询保管库列表 | 1441-1444 | 44628-44747 | 60 | `chapters/volcengine/ark/11.5.2 查询保管库列表.md` |
| 11.5.3 | 查询保管库详情 | 1445-1447 | 44748-44819 | 33 | `chapters/volcengine/ark/11.5.3 查询保管库详情.md` |
| 11.5.4 | 更新保管库 | 1448-1450 | 44820-44923 | 47 | `chapters/volcengine/ark/11.5.4 更新保管库.md` |
| 11.5.5 | 删除保管库 | 1451-1452 | 44924-44980 | 25 | `chapters/volcengine/ark/11.5.5 删除保管库.md` |
| 11.5.6.1 | 创建凭证 | 1453-1468 | 44982-45529 | 376 | `chapters/volcengine/ark/11.5.6.1 创建凭证.md` |
| 11.5.6.2 | 查询凭证列表 | 1469-1477 | 45530-45811 | 188 | `chapters/volcengine/ark/11.5.6.2 查询凭证列表.md` |
| 11.5.6.3 | 查询凭证详情 | 1478-1485 | 45812-46058 | 163 | `chapters/volcengine/ark/11.5.6.3 查询凭证详情.md` |
| 11.5.6.4 | 更新凭证 | 1486-1501 | 46059-46581 | 357 | `chapters/volcengine/ark/11.5.6.4 更新凭证.md` |
| 11.5.6.5 | 删除凭证 | 1502-1503 | 46582-46641 | 30 | `chapters/volcengine/ark/11.5.6.5 删除凭证.md` |
| 11.6.1 | 创建记忆库 | 1504-1508 | 46643-46787 | 72 | `chapters/volcengine/ark/11.6.1 创建记忆库.md` |
| 11.6.2 | 查询记忆库列表 | 1509-1513 | 46788-46946 | 90 | `chapters/volcengine/ark/11.6.2 查询记忆库列表.md` |
| 11.6.3 | 查询记忆库详情 | 1514-1517 | 46947-47064 | 54 | `chapters/volcengine/ark/11.6.3 查询记忆库详情.md` |
| 11.6.4 | 更新记忆库 | 1518-1523 | 47065-47221 | 71 | `chapters/volcengine/ark/11.6.4 更新记忆库.md` |
| 11.6.5 | 删除记忆库 | 1524-1525 | 47222-47282 | 21 | `chapters/volcengine/ark/11.6.5 删除记忆库.md` |
| 11.6.6.1 | 创建记忆 | 1526-1530 | 47284-47419 | 71 | `chapters/volcengine/ark/11.6.6.1 创建记忆.md` |
| 11.6.6.2 | 批量创建记忆 | 1531-1537 | 47420-47663 | 121 | `chapters/volcengine/ark/11.6.6.2 批量创建记忆.md` |
| 11.6.6.3 | 查询记忆列表 | 1538-1542 | 47664-47827 | 87 | `chapters/volcengine/ark/11.6.6.3 查询记忆列表.md` |
| 11.6.6.4 | 查询记忆详情 | 1543-1546 | 47828-47948 | 61 | `chapters/volcengine/ark/11.6.6.4 查询记忆详情.md` |
| 11.6.6.5 | 更新记忆 | 1547-1551 | 47949-48090 | 66 | `chapters/volcengine/ark/11.6.6.5 更新记忆.md` |
| 11.6.6.6 | 删除记忆 | 1552-1553 | 48091-48154 | 25 | `chapters/volcengine/ark/11.6.6.6 删除记忆.md` |
| 11.7.1 | 创建 Dream | 1554-1559 | 48156-48334 | 117 | `chapters/volcengine/ark/11.7.1 创建 Dream.md` |
| 11.7.2 | 查询 Dream 列表 | 1560-1566 | 48335-48561 | 142 | `chapters/volcengine/ark/11.7.2 查询 Dream 列表.md` |
| 11.7.3 | 查询 Dream | 1567-1571 | 48562-48723 | 90 | `chapters/volcengine/ark/11.7.3 查询 Dream.md` |
| 11.7.4 | 取消 Dream | 1572-1577 | 48724-48890 | 93 | `chapters/volcengine/ark/11.7.4 取消 Dream.md` |
| 11.8.1 | 创建技能 | 1578-1581 | 48892-49015 | 61 | `chapters/volcengine/ark/11.8.1 创建技能.md` |
| 11.8.2 | 查询技能列表 | 1582-1585 | 49016-49136 | 68 | `chapters/volcengine/ark/11.8.2 查询技能列表.md` |
| 11.8.3 | 查询技能详情 | 1586-1588 | 49137-49228 | 43 | `chapters/volcengine/ark/11.8.3 查询技能详情.md` |
| 11.8.4 | 设置技能内容保护 | 1589-1591 | 49229-49299 | 43 | `chapters/volcengine/ark/11.8.4 设置技能内容保护.md` |
| 11.8.5 | 删除技能 | 1592-1593 | 49300-49358 | 24 | `chapters/volcengine/ark/11.8.5 删除技能.md` |
| 11.8.6 | 创建新版本的技能 | 1594-1596 | 49359-49460 | 49 | `chapters/volcengine/ark/11.8.6 创建新版本的技能.md` |
| 11.8.7 | 查询技能的版本列表 | 1597-1599 | 49461-49558 | 54 | `chapters/volcengine/ark/11.8.7 查询技能的版本列表.md` |
| 11.8.8 | 查询指定版本的技能 | 1600-1602 | 49559-49630 | 32 | `chapters/volcengine/ark/11.8.8 查询指定版本的技能.md` |
| 11.8.9 | 删除指定版本的技能 | 1603-1604 | 49631-49685 | 22 | `chapters/volcengine/ark/11.8.9 删除指定版本的技能.md` |
| 11.8.10 | 下载指定版本的技能 | 1605-1606 | 49686-49754 | 26 | `chapters/volcengine/ark/11.8.10 下载指定版本的技能.md` |
| 11.8.11 | 扫描 GitHub 技能 | 1607-1609 | 49755-49831 | 48 | `chapters/volcengine/ark/11.8.11 扫描 GitHub 技能.md` |
| 11.8.12 | 导入 GitHub 技能 | 1610-1612 | 49832-49934 | 63 | `chapters/volcengine/ark/11.8.12 导入 GitHub 技能.md` |
| 12.1.1 | 创建批量推理任务 | 1613-1616 | 49937-50017 | 60 | `chapters/volcengine/ark/12.1.1 创建批量推理任务.md` |
| 12.1.2 | 获取批量推理任务列表 | 1617-1624 | 50018-50230 | 165 | `chapters/volcengine/ark/12.1.2 获取批量推理任务列表.md` |
| 12.1.3 | 获取批量推理任务 | 1625-1630 | 50231-50380 | 107 | `chapters/volcengine/ark/12.1.3 获取批量推理任务.md` |
| 12.1.4 | 更新批量推理任务 | 1631-1632 | 50381-50418 | 18 | `chapters/volcengine/ark/12.1.4 更新批量推理任务.md` |
| 12.1.5 | 删除批量推理任务 | 1633-1634 | 50419-50451 | 14 | `chapters/volcengine/ark/12.1.5 删除批量推理任务.md` |
| 12.1.6 | 停止批量推理任务 | 1635-1636 | 50452-50487 | 17 | `chapters/volcengine/ark/12.1.6 停止批量推理任务.md` |
| 12.1.7 | 重启批量推理任务 | 1637-1638 | 50488-50524 | 18 | `chapters/volcengine/ark/12.1.7 重启批量推理任务.md` |
| 12.2 | 批量(Chat) API | 1639-1659 | 50525-51085 | 365 | `chapters/volcengine/ark/12.2 批量(Chat) API.md` |
| 13.1 | 分词 API | 1660-1664 | 51087-51245 | 61 | `chapters/volcengine/ark/13.1 分词 API.md` |
| 14.1.1 | 获取临时 API Key | 1665-1666 | 51248-51297 | 29 | `chapters/volcengine/ark/14.1.1 获取临时 API Key.md` |
| 14.2.1 | 创建个人版套餐 | 1667-1668 | 51299-51360 | 35 | `chapters/volcengine/ark/14.2.1 创建个人版套餐.md` |
| 14.2.2 | 续费个人版套餐 | 1669-1670 | 51361-51409 | 27 | `chapters/volcengine/ark/14.2.2 续费个人版套餐.md` |
| 14.2.3 | 查询个人版套餐 | 1671-1672 | 51410-51452 | 24 | `chapters/volcengine/ark/14.2.3 查询个人版套餐.md` |
| 14.2.4.1 | 查询 Agent Plan 支持的模型列表 | 1673-1674 | 51454-51488 | 16 | `chapters/volcengine/ark/14.2.4.1 查询 Agent Plan 支持的模型列表.md` |
| 14.2.4.2 | 轮换个人版 API Key | 1675-1676 | 51489-51531 | 22 | `chapters/volcengine/ark/14.2.4.2 轮换个人版 API Key.md` |
| 14.2.4.3 | 获取套餐 AFP 额度 | 1677-1680 | 51532-51628 | 69 | `chapters/volcengine/ark/14.2.4.3 获取套餐 AFP 额度.md` |
| 14.2.4.4 | 获取套餐用量详情 | 1681-1683 | 51629-51703 | 43 | `chapters/volcengine/ark/14.2.4.4 获取套餐用量详情.md` |
| 14.2.5.1 | 查询 Coding Plan 支持的模型列表 | 1684 | 51705-51731 | 15 | `chapters/volcengine/ark/14.2.5.1 查询 Coding Plan 支持的模型列表.md` |
| 14.3.1 | 获取基础模型版本列表 | 1685-1688 | 51733-51844 | 77 | `chapters/volcengine/ark/14.3.1 获取基础模型版本列表.md` |
| 14.3.2 | 获取基础模型版本信息 | 1689-1702 | 51845-52227 | 289 | `chapters/volcengine/ark/14.3.2 获取基础模型版本信息.md` |
| 14.3.3 | 获取基础模型列表 | 1703-1710 | 52228-52521 | 195 | `chapters/volcengine/ark/14.3.3 获取基础模型列表.md` |
| 14.3.4 | 获取基础模型信息 | 1711-1715 | 52522-52674 | 97 | `chapters/volcengine/ark/14.3.4 获取基础模型信息.md` |
| 14.4.1 | 批量开通基础模型 | 1716 | 52676-52702 | 13 | `chapters/volcengine/ark/14.4.1 批量开通基础模型.md` |
| 14.4.2 | 启用自动开通新模型 | 1717 | 52703-52727 | 12 | `chapters/volcengine/ark/14.4.2 启用自动开通新模型.md` |
| 14.4.3 | 关闭自动开通新模型 | 1718 | 52728-52752 | 12 | `chapters/volcengine/ark/14.4.3 关闭自动开通新模型.md` |
| 14.4.4 | 查询模型开通详情 | 1719-1725 | 52753-52942 | 152 | `chapters/volcengine/ark/14.4.4 查询模型开通详情.md` |
| 14.4.5 | 查询模型开通列表 | 1726-1733 | 52943-53169 | 186 | `chapters/volcengine/ark/14.4.5 查询模型开通列表.md` |
| 14.5.1 | 批量开通资源 | 1734-1735 | 53171-53204 | 16 | `chapters/volcengine/ark/14.5.1 批量开通资源.md` |
| 14.5.2 | 查询资源开通列表 | 1736-1740 | 53205-53346 | 112 | `chapters/volcengine/ark/14.5.2 查询资源开通列表.md` |
| 14.6.1 | 查询模型限流 | 1741-1745 | 53348-53476 | 99 | `chapters/volcengine/ark/14.6.1 查询模型限流.md` |
| 14.7.1 | 删除定制模型 | 1746-1747 | 53478-53517 | 19 | `chapters/volcengine/ark/14.7.1 删除定制模型.md` |
| 14.7.2 | 获取定制模型信息 | 1748-1753 | 53518-53653 | 102 | `chapters/volcengine/ark/14.7.2 获取定制模型信息.md` |
| 14.7.3 | 更新定制模型 | 1754-1755 | 53654-53701 | 25 | `chapters/volcengine/ark/14.7.3 更新定制模型.md` |
| 14.7.4 | 获取定制模型列表 | 1756-1761 | 53702-53852 | 106 | `chapters/volcengine/ark/14.7.4 获取定制模型列表.md` |
| 14.8.1 | 创建模型调优任务 | 1762-1775 | 53854-54206 | 287 | `chapters/volcengine/ark/14.8.1 创建模型调优任务.md` |
| 14.8.2 | 删除模型调优任务 | 1776 | 54207-54236 | 14 | `chapters/volcengine/ark/14.8.2 删除模型调优任务.md` |
| 14.8.3 | 获取模型调优任务信息 | 1777-1795 | 54237-54740 | 416 | `chapters/volcengine/ark/14.8.3 获取模型调优任务信息.md` |
| 14.8.4 | 查询精调效果指标详细数据 | 1796-1798 | 54741-54812 | 45 | `chapters/volcengine/ark/14.8.4 查询精调效果指标详细数据.md` |
| 14.8.5 | 查询精调效果指标 | 1799-1800 | 54813-54848 | 15 | `chapters/volcengine/ark/14.8.5 查询精调效果指标.md` |
| 14.8.6 | 获取模型调优任务列表 | 1801-1812 | 54849-55163 | 266 | `chapters/volcengine/ark/14.8.6 获取模型调优任务列表.md` |
| 14.8.7 | 重试模型调优任务 | 1813 | 55164-55193 | 13 | `chapters/volcengine/ark/14.8.7 重试模型调优任务.md` |
| 14.8.8 | 停止模型调优任务 | 1814 | 55194-55223 | 14 | `chapters/volcengine/ark/14.8.8 停止模型调优任务.md` |
| 14.8.9 | 更新模型调优任务 | 1815-1816 | 55224-55262 | 16 | `chapters/volcengine/ark/14.8.9 更新模型调优任务.md` |
| 14.9.1 | 开启推理接入点 | 1817-1818 | 55264-55297 | 15 | `chapters/volcengine/ark/14.9.1 开启推理接入点.md` |
| 14.9.2 | 停止推理接入点 | 1819-1820 | 55298-55331 | 13 | `chapters/volcengine/ark/14.9.2 停止推理接入点.md` |
| 14.9.3 | 获取推理接入点列表 | 1821-1828 | 55332-55577 | 177 | `chapters/volcengine/ark/14.9.3 获取推理接入点列表.md` |
| 14.9.4 | 获取推理接入点 | 1829-1833 | 55578-55704 | 91 | `chapters/volcengine/ark/14.9.4 获取推理接入点.md` |
| 14.9.5 | 删除推理接入点 | 1834-1835 | 55705-55737 | 14 | `chapters/volcengine/ark/14.9.5 删除推理接入点.md` |
| 14.9.6 | 更新推理接入点 | 1836-1843 | 55738-55941 | 162 | `chapters/volcengine/ark/14.9.6 更新推理接入点.md` |
| 14.9.7 | 创建推理接入点 | 1844-1853 | 55942-56191 | 196 | `chapters/volcengine/ark/14.9.7 创建推理接入点.md` |
| 14.9.8 | 获取接入点推理应用层加密证书 | 1854-1855 | 56192-56248 | 27 | `chapters/volcengine/ark/14.9.8 获取接入点推理应用层加密证书.md` |
| 14.9.9 | 创建推理接入点滚动升级任务 | 1856-1858 | 56249-56314 | 43 | `chapters/volcengine/ark/14.9.9 创建推理接入点滚动升级任务.md` |
| 14.9.10 | 查询推理接入点滚动升级详情 | 1859-1864 | 56315-56476 | 131 | `chapters/volcengine/ark/14.9.10 查询推理接入点滚动升级详情.md` |
| 14.9.11 | 回滚推理接入点滚动升级 | 1865-1866 | 56477-56509 | 15 | `chapters/volcengine/ark/14.9.11 回滚推理接入点滚动升级.md` |
| 14.9.12 | 取消推理接入点滚动升级 | 1867-1868 | 56510-56542 | 15 | `chapters/volcengine/ark/14.9.12 取消推理接入点滚动升级.md` |
| 14.10.1 | 创建评测任务 | 1869-1875 | 56544-56733 | 137 | `chapters/volcengine/ark/14.10.1 创建评测任务.md` |
| 14.10.2 | 删除评测任务 | 1876-1877 | 56734-56769 | 15 | `chapters/volcengine/ark/14.10.2 删除评测任务.md` |
| 14.10.3 | 获取评测任务 | 1878-1881 | 56770-56872 | 69 | `chapters/volcengine/ark/14.10.3 获取评测任务.md` |
| 14.10.4 | 获取评测任务结果 | 1882-1886 | 56873-57001 | 93 | `chapters/volcengine/ark/14.10.4 获取评测任务结果.md` |
| 14.10.5 | 获取评测任务列表 | 1887-1893 | 57002-57181 | 138 | `chapters/volcengine/ark/14.10.5 获取评测任务列表.md` |
| 14.10.6 | 获取评测任务结果列表 | 1894-1899 | 57182-57352 | 128 | `chapters/volcengine/ark/14.10.6 获取评测任务结果列表.md` |
| 14.10.7 | 停止评测任务 | 1900-1901 | 57353-57387 | 14 | `chapters/volcengine/ark/14.10.7 停止评测任务.md` |
| 14.10.8 | 更新评测任务 | 1902-1903 | 57388-57427 | 20 | `chapters/volcengine/ark/14.10.8 更新评测任务.md` |
| 14.11.1 | 查询推理用量 | 1904-1907 | 57429-57590 | 94 | `chapters/volcengine/ark/14.11.1 查询推理用量.md` |
| 14.11.2 | 查询单请求用量 | 1908-1913 | 57591-57762 | 136 | `chapters/volcengine/ark/14.11.2 查询单请求用量.md` |
| 14.11.3 | 查询异步任务用量 | 1914-1917 | 57763-57854 | 64 | `chapters/volcengine/ark/14.11.3 查询异步任务用量.md` |
| 14.11.4 | 创建用量明细导出任务 | 1918-1920 | 57855-57926 | 36 | `chapters/volcengine/ark/14.11.4 创建用量明细导出任务.md` |
| 14.11.5 | 查询用量明细导出任务状态 | 1921-1924 | 57927-58052 | 78 | `chapters/volcengine/ark/14.11.5 查询用量明细导出任务状态.md` |
| 14.11.6 | 查询模型推理限额 | 1925-1926 | 58053-58095 | 27 | `chapters/volcengine/ark/14.11.6 查询模型推理限额.md` |
| 14.11.7 | 开启模型推理限额 | 1927-1928 | 58096-58136 | 20 | `chapters/volcengine/ark/14.11.7 开启模型推理限额.md` |
| 14.11.8 | 关闭模型推理限额 | 1929-1930 | 58137-58173 | 16 | `chapters/volcengine/ark/14.11.8 关闭模型推理限额.md` |
| 14.12.1 | 创建方舟官方模型产物查询请求 | 1931-1932 | 58175-58209 | 19 | `chapters/volcengine/ark/14.12.1 创建方舟官方模型产物查询请求.md` |
| 14.12.2 | 获取安全审计日志 | 1933-1941 | 58210-58531 | 133 | `chapters/volcengine/ark/14.12.2 获取安全审计日志.md` |
| 14.12.3 | 获取方舟官方产物确认结果 | 1942-1943 | 58532-58578 | 27 | `chapters/volcengine/ark/14.12.3 获取方舟官方产物确认结果.md` |
| 14.13.1 | 上报视频生成模型效果问题 | 1944-1951 | 58580-58840 | 162 | `chapters/volcengine/ark/14.13.1 上报视频生成模型效果问题.md` |
| 14.13.2 | 查询视频生成模型效果问题结果 | 1952-1959 | 58841-59092 | 168 | `chapters/volcengine/ark/14.13.2 查询视频生成模型效果问题结果.md` |
| 14.13.3 | 上报大语言模型效果问题 | 1960-1964 | 59093-59256 | 89 | `chapters/volcengine/ark/14.13.3 上报大语言模型效果问题.md` |
| 14.13.4 | 查询大语言模型效果问题结果 | 1965-1970 | 59257-59423 | 105 | `chapters/volcengine/ark/14.13.4 查询大语言模型效果问题结果.md` |
| 14.13.5 | 上报 3D 生成效果问题 | 1971-1976 | 59424-59635 | 141 | `chapters/volcengine/ark/14.13.5 上报 3D 生成效果问题.md` |
| 14.13.6 | 查询 3D 生成效果问题结果 | 1977-1984 | 59636-59878 | 159 | `chapters/volcengine/ark/14.13.6 查询 3D 生成效果问题结果.md` |
| 15.1 | 兼容 OpenAI SDK | 1985-1988 | 59880-59996 | 103 | `chapters/volcengine/ark/15.1 兼容 OpenAI SDK.md` |
| 15.2 | 向后兼容性 | 1989 | 59997-60042 | 25 | `chapters/volcengine/ark/15.2 向后兼容性.md` |
| 15.3 | 错误码 - 第1部分 | 1989-2011 | 60043-62046 | 1954 | `chapters/volcengine/ark/15.3 错误码 - 第1部分.md` |
| 15.3 | 错误码 - 第2部分·错误码 | 2012-2021 | 62047-62812 | 732 | `chapters/volcengine/ark/15.3 错误码 - 第2部分·错误码.md` |
| 15.4 | SDK 常见使用示例 | 2022-2037 | 62813-63401 | 521 | `chapters/volcengine/ark/15.4 SDK 常见使用示例.md` |
