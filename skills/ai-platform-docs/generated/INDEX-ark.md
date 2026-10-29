# 方舟 API 区章节表（ark）

来源：《火山方舟 API 参考》（2001 页）。216 个章节文件，接口级切分：一个接口/任务一个文件；超过 1500 行的按语义块自动再拆为`… - 第N部分`（5 个章节被拆分）。

「页码」是原 PDF 页码范围；「行范围」是中间 MD（`doc/<源文档>.md`）的 1 起始行号，可据此回查原文。章节文件本身已去掉页眉页脚，回查 PDF 时用这两列。文件名即章节标题，日常定位直接 Glob 文件名即可，用不到这两列。

**这张表用来 grep，不要整读。**

| 编号 | 标题 | 页码 | 行范围(源文件) | 行数 | 文件 |
|------|------|------|---------------|------|------|
| 1.1 | 获取 API Key 并配置 | 1 | 297-332 | 20 | `chapters/volcengine/ark/1.1 获取 API Key 并配置.md` |
| 1.2 | 安装及升级 SDK | 2-7 | 333-491 | 122 | `chapters/volcengine/ark/1.2 安装及升级 SDK.md` |
| 1.3 | Base URL及鉴权 | 8-10 | 492-587 | 68 | `chapters/volcengine/ark/1.3 Base URL及鉴权.md` |
| 2.1 | 对话(Chat) API | 11-71 | 589-2909 | 1246 | `chapters/volcengine/ark/2.1 对话(Chat) API.md` |
| 3.1 | 创建 Response - 第1部分 | 72-128 | 2910-4586 | 1405 | `chapters/volcengine/ark/3.1 创建 Response - 第1部分.md` |
| 3.1 | 创建 Response - 第2部分·响应参数 | 129-197 | 4587-6940 | 1351 | `chapters/volcengine/ark/3.1 创建 Response - 第2部分·响应参数.md` |
| 3.2 | 查询 Response 详情 | 198-244 | 6941-8274 | 1094 | `chapters/volcengine/ark/3.2 查询 Response 详情.md` |
| 3.3 | 查询 Response 输入项列表 | 245-292 | 8275-9857 | 947 | `chapters/volcengine/ark/3.3 查询 Response 输入项列表.md` |
| 3.4 | 删除 Response | 293-294 | 9858-9931 | 34 | `chapters/volcengine/ark/3.4 删除 Response.md` |
| 3.5.1 | Response 生命周期 - 第1部分 | 295-354 | 9932-11655 | 1505 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第1部分.md` |
| 3.5.1 | Response 生命周期 - 第2部分 | 355-413 | 11656-13352 | 1480 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第2部分.md` |
| 3.5.1 | Response 生命周期 - 第3部分 | 414-473 | 13353-15069 | 1502 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第3部分.md` |
| 3.5.1 | Response 生命周期 - 第4部分 | 474-543 | 15070-17079 | 1732 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第4部分.md` |
| 3.5.2 | Output Item 与文本回答 - 第1部分 | 544-601 | 17080-18731 | 1480 | `chapters/volcengine/ark/3.5.2 Output Item 与文本回答 - 第1部分.md` |
| 3.5.2 | Output Item 与文本回答 - 第2部分 | 602-625 | 18732-19361 | 582 | `chapters/volcengine/ark/3.5.2 Output Item 与文本回答 - 第2部分.md` |
| 3.5.3 | 工具调用事件 | 626-667 | 19362-20472 | 1024 | `chapters/volcengine/ark/3.5.3 工具调用事件.md` |
| 3.5.4 | 语音转写与错误事件 | 668-674 | 20473-20647 | 161 | `chapters/volcengine/ark/3.5.4 语音转写与错误事件.md` |
| 4.1 | 创建 Message | 675-702 | 20649-21429 | 579 | `chapters/volcengine/ark/4.1 创建 Message.md` |
| 4.2 | 统计 Messages 请求 token 数 | 703-715 | 21430-21783 | 282 | `chapters/volcengine/ark/4.2 统计 Messages 请求 token 数.md` |
| 5.1 | System One API（beta） | 716-727 | 21785-22112 | 244 | `chapters/volcengine/ark/5.1 System One API（beta）.md` |
| 6.1 | 上传文件 | 728-740 | 22114-22601 | 206 | `chapters/volcengine/ark/6.1 上传文件.md` |
| 6.2 | 查询文件详情 | 741-745 | 22602-22736 | 75 | `chapters/volcengine/ark/6.2 查询文件详情.md` |
| 6.3 | 查询文件列表 | 746-752 | 22737-22966 | 122 | `chapters/volcengine/ark/6.3 查询文件列表.md` |
| 6.4 | 删除文件 | 753-755 | 22967-23039 | 25 | `chapters/volcengine/ark/6.4 删除文件.md` |
| 6.5 | The file object | 756-759 | 23040-23123 | 60 | `chapters/volcengine/ark/6.5 The file object.md` |
| 7.1 | 创建视频生成任务 | 760-801 | 23125-25001 | 837 | `chapters/volcengine/ark/7.1 创建视频生成任务.md` |
| 7.2 | 查询视频生成任务 | 802-808 | 25002-25232 | 125 | `chapters/volcengine/ark/7.2 查询视频生成任务.md` |
| 7.3 | 查询视频生成任务列表 | 809-819 | 25233-25634 | 203 | `chapters/volcengine/ark/7.3 查询视频生成任务列表.md` |
| 7.4 | 取消或删除视频生成任务 | 820-821 | 25635-25721 | 50 | `chapters/volcengine/ark/7.4 取消或删除视频生成任务.md` |
| 8.1 | 图片生成 API | 822-862 | 25723-27446 | 738 | `chapters/volcengine/ark/8.1 图片生成 API.md` |
| 8.2 | 图片生成流式响应事件 | 863-868 | 27447-27625 | 158 | `chapters/volcengine/ark/8.2 图片生成流式响应事件.md` |
| 9.1.1 | 创建 3D 生成任务 API | 869-874 | 27628-27810 | 102 | `chapters/volcengine/ark/9.1.1 创建 3D 生成任务 API.md` |
| 9.1.2 | 查询 3D 生成任务 API | 875-878 | 27811-27945 | 63 | `chapters/volcengine/ark/9.1.2 查询 3D 生成任务 API.md` |
| 9.1.3 | 查询 3D 生成任务列表 | 879-885 | 27946-28171 | 105 | `chapters/volcengine/ark/9.1.3 查询 3D 生成任务列表.md` |
| 9.1.4 | 取消或删除 3D 生成任务 | 886-887 | 28172-28258 | 52 | `chapters/volcengine/ark/9.1.4 取消或删除 3D 生成任务.md` |
| 9.2.1 | 创建3D生成任务 | 888-894 | 28260-28504 | 152 | `chapters/volcengine/ark/9.2.1 创建3D生成任务.md` |
| 9.2.2 | 查询3D生成任务 | 895-897 | 28505-28584 | 52 | `chapters/volcengine/ark/9.2.2 查询3D生成任务.md` |
| 9.2.3 | 查询3D生成任务列表 | 898-901 | 28585-28710 | 85 | `chapters/volcengine/ark/9.2.3 查询3D生成任务列表.md` |
| 9.2.4 | 取消或删除3D生成任务 | 902-903 | 28711-28755 | 34 | `chapters/volcengine/ark/9.2.4 取消或删除3D生成任务.md` |
| 9.3.1 | 创建3D生成任务 | 904-908 | 28757-28901 | 98 | `chapters/volcengine/ark/9.3.1 创建3D生成任务.md` |
| 9.3.2 | 查询3D生成任务 | 909-911 | 28902-28981 | 51 | `chapters/volcengine/ark/9.3.2 查询3D生成任务.md` |
| 9.3.3 | 查询3D生成任务列表 | 912-915 | 28982-29107 | 86 | `chapters/volcengine/ark/9.3.3 查询3D生成任务列表.md` |
| 9.3.4 | 取消或删除3D生成任务 | 916-917 | 29108-29152 | 34 | `chapters/volcengine/ark/9.3.4 取消或删除3D生成任务.md` |
| 10.1 | 多模态向量化 API | 918-928 | 29154-29572 | 201 | `chapters/volcengine/ark/10.1 多模态向量化 API.md` |
| 11.1.1 | 创建智能体 | 929-947 | 29575-30161 | 405 | `chapters/volcengine/ark/11.1.1 创建智能体.md` |
| 11.1.2 | 查询智能体列表 | 948-958 | 30162-30491 | 234 | `chapters/volcengine/ark/11.1.2 查询智能体列表.md` |
| 11.1.3 | 查询智能体详情 | 959-968 | 30492-30778 | 199 | `chapters/volcengine/ark/11.1.3 查询智能体详情.md` |
| 11.1.4 | 更新智能体 | 969-987 | 30779-31413 | 425 | `chapters/volcengine/ark/11.1.4 更新智能体.md` |
| 11.1.5 | 删除智能体 | 988-989 | 31414-31465 | 19 | `chapters/volcengine/ark/11.1.5 删除智能体.md` |
| 11.1.6 | 查询智能体版本列表 | 990-1000 | 31466-31797 | 220 | `chapters/volcengine/ark/11.1.6 查询智能体版本列表.md` |
| 11.2.1 | 创建环境 | 1001-1009 | 31799-32074 | 184 | `chapters/volcengine/ark/11.2.1 创建环境.md` |
| 11.2.2 | 查询环境列表 | 1010-1015 | 32075-32235 | 111 | `chapters/volcengine/ark/11.2.2 查询环境列表.md` |
| 11.2.3 | 查询环境详情 | 1016-1020 | 32236-32379 | 87 | `chapters/volcengine/ark/11.2.3 查询环境详情.md` |
| 11.2.4 | 更新环境 | 1021-1029 | 32380-32660 | 179 | `chapters/volcengine/ark/11.2.4 更新环境.md` |
| 11.2.5 | 删除环境 | 1030-1031 | 32661-32716 | 27 | `chapters/volcengine/ark/11.2.5 删除环境.md` |
| 11.2.6.1 | 长轮询拉取待执行 Work | 1032-1036 | 32718-32880 | 85 | `chapters/volcengine/ark/11.2.6.1 长轮询拉取待执行 Work.md` |
| 11.2.6.2 | 认领 Work | 1037-1041 | 32881-33025 | 76 | `chapters/volcengine/ark/11.2.6.2 认领 Work.md` |
| 11.2.6.3 | 续租 Work | 1042-1045 | 33026-33139 | 53 | `chapters/volcengine/ark/11.2.6.3 续租 Work.md` |
| 11.2.6.4 | 查询 Work 队列状态 | 1046-1047 | 33140-33207 | 29 | `chapters/volcengine/ark/11.2.6.4 查询 Work 队列状态.md` |
| 11.2.6.5 | 停止 Work | 1048-1052 | 33208-33378 | 90 | `chapters/volcengine/ark/11.2.6.5 停止 Work.md` |
| 11.2.6.6 | 查询 Work 列表 | 1053-1057 | 33379-33538 | 92 | `chapters/volcengine/ark/11.2.6.6 查询 Work 列表.md` |
| 11.2.6.7 | 查询 Work 详情 | 1058-1061 | 33539-33661 | 64 | `chapters/volcengine/ark/11.2.6.7 查询 Work 详情.md` |
| 11.3.1 | 创建会话 | 1062-1100 | 33663-34867 | 903 | `chapters/volcengine/ark/11.3.1 创建会话.md` |
| 11.3.2 | 查询会话列表 | 1101-1126 | 34868-35628 | 596 | `chapters/volcengine/ark/11.3.2 查询会话列表.md` |
| 11.3.3 | 查询会话详情 | 1127-1152 | 35629-36396 | 588 | `chapters/volcengine/ark/11.3.3 查询会话详情.md` |
| 11.3.4 | 更新会话标题和标签 | 1153-1177 | 36397-37135 | 567 | `chapters/volcengine/ark/11.3.4 更新会话标题和标签.md` |
| 11.3.5 | 升级会话 | 1178-1210 | 37136-38102 | 778 | `chapters/volcengine/ark/11.3.5 升级会话.md` |
| 11.3.6 | 删除会话 | 1211-1212 | 38103-38162 | 26 | `chapters/volcengine/ark/11.3.6 删除会话.md` |
| 11.3.7.1 | 查询会话任务 | 1213-1218 | 38164-38349 | 99 | `chapters/volcengine/ark/11.3.7.1 查询会话任务.md` |
| 11.3.7.2 | 查询会话任务列表 | 1219-1223 | 38350-38520 | 98 | `chapters/volcengine/ark/11.3.7.2 查询会话任务列表.md` |
| 11.3.7.3 | 取消会话任务 | 1224-1226 | 38521-38614 | 36 | `chapters/volcengine/ark/11.3.7.3 取消会话任务.md` |
| 11.3.8.1 | 发送会话事件 | 1227-1230 | 38616-38732 | 53 | `chapters/volcengine/ark/11.3.8.1 发送会话事件.md` |
| 11.3.8.2 | 查询会话事件列表 | 1231-1234 | 38733-38866 | 62 | `chapters/volcengine/ark/11.3.8.2 查询会话事件列表.md` |
| 11.3.8.3 | 流式获取会话事件 | 1235-1239 | 38867-39040 | 50 | `chapters/volcengine/ark/11.3.8.3 流式获取会话事件.md` |
| 11.3.8.4 | 会话事件结构参考 - 第1部分 | 1240-1316 | 39041-41009 | 1748 | `chapters/volcengine/ark/11.3.8.4 会话事件结构参考 - 第1部分.md` |
| 11.3.9.1 | 添加会话资源 | 1317-1320 | 41011-41126 | 51 | `chapters/volcengine/ark/11.3.9.1 添加会话资源.md` |
| 11.3.9.2 | 查询会话资源列表 | 1321-1326 | 41127-41291 | 105 | `chapters/volcengine/ark/11.3.9.2 查询会话资源列表.md` |
| 11.3.9.3 | 查询会话资源 | 1327-1329 | 41292-41386 | 43 | `chapters/volcengine/ark/11.3.9.3 查询会话资源.md` |
| 11.3.10.1 | 查询线程列表 | 1330-1334 | 41388-41527 | 71 | `chapters/volcengine/ark/11.3.10.1 查询线程列表.md` |
| 11.3.10.2 | 查询线程详情 | 1335-1340 | 41528-41712 | 99 | `chapters/volcengine/ark/11.3.10.2 查询线程详情.md` |
| 11.3.10.3 | 查询线程事件列表 | 1341-1344 | 41713-41842 | 57 | `chapters/volcengine/ark/11.3.10.3 查询线程事件列表.md` |
| 11.3.10.4 | 流式获取线程事件 | 1345-1348 | 41843-41977 | 44 | `chapters/volcengine/ark/11.3.10.4 流式获取线程事件.md` |
| 11.4.1 | 创建 Webhook 接入点 | 1349-1352 | 41979-42098 | 64 | `chapters/volcengine/ark/11.4.1 创建 Webhook 接入点.md` |
| 11.4.2 | 查询 Webhook 接入点列表 | 1353-1356 | 42099-42212 | 68 | `chapters/volcengine/ark/11.4.2 查询 Webhook 接入点列表.md` |
| 11.4.3 | 查询 Webhook 接入点详情 | 1357-1359 | 42213-42307 | 53 | `chapters/volcengine/ark/11.4.3 查询 Webhook 接入点详情.md` |
| 11.4.4 | 更新 Webhook 接入点 | 1360-1363 | 42308-42425 | 63 | `chapters/volcengine/ark/11.4.4 更新 Webhook 接入点.md` |
| 11.4.5 | 启用 Webhook 接入点 | 1364-1366 | 42426-42522 | 55 | `chapters/volcengine/ark/11.4.5 启用 Webhook 接入点.md` |
| 11.4.6 | 删除 Webhook 接入点 | 1367 | 42523-42550 | 18 | `chapters/volcengine/ark/11.4.6 删除 Webhook 接入点.md` |
| 11.4.7 | 停用 Webhook 接入点 | 1368-1370 | 42551-42648 | 54 | `chapters/volcengine/ark/11.4.7 停用 Webhook 接入点.md` |
| 11.4.8 | 重置 Webhook 签名密钥 | 1371-1372 | 42649-42683 | 19 | `chapters/volcengine/ark/11.4.8 重置 Webhook 签名密钥.md` |
| 11.4.9 | 发送 Webhook 测试事件 | 1373-1374 | 42684-42728 | 29 | `chapters/volcengine/ark/11.4.9 发送 Webhook 测试事件.md` |
| 11.4.10 | 查询 Webhook 事件详情 | 1375-1376 | 42729-42780 | 35 | `chapters/volcengine/ark/11.4.10 查询 Webhook 事件详情.md` |
| 11.4.11 | 查询 Webhook 事件列表 | 1377-1379 | 42781-42860 | 52 | `chapters/volcengine/ark/11.4.11 查询 Webhook 事件列表.md` |
| 11.4.12 | Webhook 事件结构参考 | 1380-1401 | 42861-43444 | 519 | `chapters/volcengine/ark/11.4.12 Webhook 事件结构参考.md` |
| 11.5.1 | 创建保管库 | 1402-1404 | 43446-43546 | 45 | `chapters/volcengine/ark/11.5.1 创建保管库.md` |
| 11.5.2 | 查询保管库列表 | 1405-1408 | 43547-43666 | 60 | `chapters/volcengine/ark/11.5.2 查询保管库列表.md` |
| 11.5.3 | 查询保管库详情 | 1409-1411 | 43667-43738 | 33 | `chapters/volcengine/ark/11.5.3 查询保管库详情.md` |
| 11.5.4 | 更新保管库 | 1412-1414 | 43739-43842 | 47 | `chapters/volcengine/ark/11.5.4 更新保管库.md` |
| 11.5.5 | 删除保管库 | 1415-1416 | 43843-43899 | 25 | `chapters/volcengine/ark/11.5.5 删除保管库.md` |
| 11.5.6.1 | 创建凭证 | 1417-1432 | 43901-44448 | 376 | `chapters/volcengine/ark/11.5.6.1 创建凭证.md` |
| 11.5.6.2 | 查询凭证列表 | 1433-1441 | 44449-44730 | 188 | `chapters/volcengine/ark/11.5.6.2 查询凭证列表.md` |
| 11.5.6.3 | 查询凭证详情 | 1442-1449 | 44731-44977 | 163 | `chapters/volcengine/ark/11.5.6.3 查询凭证详情.md` |
| 11.5.6.4 | 更新凭证 | 1450-1465 | 44978-45500 | 357 | `chapters/volcengine/ark/11.5.6.4 更新凭证.md` |
| 11.5.6.5 | 删除凭证 | 1466-1467 | 45501-45560 | 30 | `chapters/volcengine/ark/11.5.6.5 删除凭证.md` |
| 11.6.1 | 创建记忆库 | 1468-1472 | 45562-45706 | 72 | `chapters/volcengine/ark/11.6.1 创建记忆库.md` |
| 11.6.2 | 查询记忆库列表 | 1473-1477 | 45707-45865 | 90 | `chapters/volcengine/ark/11.6.2 查询记忆库列表.md` |
| 11.6.3 | 查询记忆库详情 | 1478-1481 | 45866-45983 | 54 | `chapters/volcengine/ark/11.6.3 查询记忆库详情.md` |
| 11.6.4 | 更新记忆库 | 1482-1487 | 45984-46140 | 71 | `chapters/volcengine/ark/11.6.4 更新记忆库.md` |
| 11.6.5 | 删除记忆库 | 1488-1489 | 46141-46201 | 21 | `chapters/volcengine/ark/11.6.5 删除记忆库.md` |
| 11.6.6.1 | 创建记忆 | 1490-1494 | 46203-46338 | 71 | `chapters/volcengine/ark/11.6.6.1 创建记忆.md` |
| 11.6.6.2 | 批量创建记忆 | 1495-1501 | 46339-46582 | 121 | `chapters/volcengine/ark/11.6.6.2 批量创建记忆.md` |
| 11.6.6.3 | 查询记忆列表 | 1502-1506 | 46583-46746 | 87 | `chapters/volcengine/ark/11.6.6.3 查询记忆列表.md` |
| 11.6.6.4 | 查询记忆详情 | 1507-1510 | 46747-46867 | 61 | `chapters/volcengine/ark/11.6.6.4 查询记忆详情.md` |
| 11.6.6.5 | 更新记忆 | 1511-1515 | 46868-47009 | 66 | `chapters/volcengine/ark/11.6.6.5 更新记忆.md` |
| 11.6.6.6 | 删除记忆 | 1516-1517 | 47010-47073 | 25 | `chapters/volcengine/ark/11.6.6.6 删除记忆.md` |
| 11.7.1 | 创建 Dream | 1518-1523 | 47075-47253 | 117 | `chapters/volcengine/ark/11.7.1 创建 Dream.md` |
| 11.7.2 | 查询 Dream 列表 | 1524-1530 | 47254-47480 | 142 | `chapters/volcengine/ark/11.7.2 查询 Dream 列表.md` |
| 11.7.3 | 查询 Dream | 1531-1535 | 47481-47642 | 90 | `chapters/volcengine/ark/11.7.3 查询 Dream.md` |
| 11.7.4 | 取消 Dream | 1536-1541 | 47643-47809 | 93 | `chapters/volcengine/ark/11.7.4 取消 Dream.md` |
| 11.8.1 | 创建技能 | 1542-1545 | 47811-47934 | 61 | `chapters/volcengine/ark/11.8.1 创建技能.md` |
| 11.8.2 | 查询技能列表 | 1546-1549 | 47935-48055 | 68 | `chapters/volcengine/ark/11.8.2 查询技能列表.md` |
| 11.8.3 | 查询技能详情 | 1550-1552 | 48056-48147 | 43 | `chapters/volcengine/ark/11.8.3 查询技能详情.md` |
| 11.8.4 | 设置技能内容保护 | 1553-1555 | 48148-48218 | 43 | `chapters/volcengine/ark/11.8.4 设置技能内容保护.md` |
| 11.8.5 | 删除技能 | 1556-1557 | 48219-48277 | 24 | `chapters/volcengine/ark/11.8.5 删除技能.md` |
| 11.8.6 | 创建新版本的技能 | 1558-1560 | 48278-48379 | 49 | `chapters/volcengine/ark/11.8.6 创建新版本的技能.md` |
| 11.8.7 | 查询技能的版本列表 | 1561-1563 | 48380-48477 | 54 | `chapters/volcengine/ark/11.8.7 查询技能的版本列表.md` |
| 11.8.8 | 查询指定版本的技能 | 1564-1566 | 48478-48549 | 32 | `chapters/volcengine/ark/11.8.8 查询指定版本的技能.md` |
| 11.8.9 | 删除指定版本的技能 | 1567-1568 | 48550-48604 | 22 | `chapters/volcengine/ark/11.8.9 删除指定版本的技能.md` |
| 11.8.10 | 下载指定版本的技能 | 1569-1570 | 48605-48673 | 26 | `chapters/volcengine/ark/11.8.10 下载指定版本的技能.md` |
| 11.8.11 | 扫描 GitHub 技能 | 1571-1573 | 48674-48750 | 48 | `chapters/volcengine/ark/11.8.11 扫描 GitHub 技能.md` |
| 11.8.12 | 导入 GitHub 技能 | 1574-1576 | 48751-48853 | 63 | `chapters/volcengine/ark/11.8.12 导入 GitHub 技能.md` |
| 12.1.1 | 创建批量推理任务 | 1577-1580 | 48856-48936 | 60 | `chapters/volcengine/ark/12.1.1 创建批量推理任务.md` |
| 12.1.2 | 获取批量推理任务列表 | 1581-1588 | 48937-49149 | 165 | `chapters/volcengine/ark/12.1.2 获取批量推理任务列表.md` |
| 12.1.3 | 获取批量推理任务 | 1589-1594 | 49150-49299 | 107 | `chapters/volcengine/ark/12.1.3 获取批量推理任务.md` |
| 12.1.4 | 更新批量推理任务 | 1595-1596 | 49300-49337 | 18 | `chapters/volcengine/ark/12.1.4 更新批量推理任务.md` |
| 12.1.5 | 删除批量推理任务 | 1597-1598 | 49338-49370 | 14 | `chapters/volcengine/ark/12.1.5 删除批量推理任务.md` |
| 12.1.6 | 停止批量推理任务 | 1599-1600 | 49371-49406 | 17 | `chapters/volcengine/ark/12.1.6 停止批量推理任务.md` |
| 12.1.7 | 重启批量推理任务 | 1601-1602 | 49407-49443 | 18 | `chapters/volcengine/ark/12.1.7 重启批量推理任务.md` |
| 12.2 | 批量(Chat) API | 1603-1623 | 49444-50004 | 365 | `chapters/volcengine/ark/12.2 批量(Chat) API.md` |
| 13.1 | 分词 API | 1624-1628 | 50006-50164 | 61 | `chapters/volcengine/ark/13.1 分词 API.md` |
| 14.1.1 | 获取临时 API Key | 1629-1630 | 50167-50216 | 29 | `chapters/volcengine/ark/14.1.1 获取临时 API Key.md` |
| 14.2.1 | 创建个人版套餐 | 1631-1632 | 50218-50279 | 35 | `chapters/volcengine/ark/14.2.1 创建个人版套餐.md` |
| 14.2.2 | 续费个人版套餐 | 1633-1634 | 50280-50328 | 27 | `chapters/volcengine/ark/14.2.2 续费个人版套餐.md` |
| 14.2.3 | 查询个人版套餐 | 1635-1636 | 50329-50371 | 24 | `chapters/volcengine/ark/14.2.3 查询个人版套餐.md` |
| 14.2.4.1 | 查询 Agent Plan 支持的模型列表 | 1637-1638 | 50373-50407 | 16 | `chapters/volcengine/ark/14.2.4.1 查询 Agent Plan 支持的模型列表.md` |
| 14.2.4.2 | 轮换个人版 API Key | 1639-1640 | 50408-50450 | 22 | `chapters/volcengine/ark/14.2.4.2 轮换个人版 API Key.md` |
| 14.2.4.3 | 获取套餐 AFP 额度 | 1641-1644 | 50451-50547 | 69 | `chapters/volcengine/ark/14.2.4.3 获取套餐 AFP 额度.md` |
| 14.2.4.4 | 获取套餐用量详情 | 1645-1647 | 50548-50622 | 43 | `chapters/volcengine/ark/14.2.4.4 获取套餐用量详情.md` |
| 14.2.5.1 | 查询 Coding Plan 支持的模型列表 | 1648 | 50624-50650 | 15 | `chapters/volcengine/ark/14.2.5.1 查询 Coding Plan 支持的模型列表.md` |
| 14.3.1 | 获取基础模型版本列表 | 1649-1652 | 50652-50763 | 77 | `chapters/volcengine/ark/14.3.1 获取基础模型版本列表.md` |
| 14.3.2 | 获取基础模型版本信息 | 1653-1666 | 50764-51146 | 289 | `chapters/volcengine/ark/14.3.2 获取基础模型版本信息.md` |
| 14.3.3 | 获取基础模型列表 | 1667-1674 | 51147-51440 | 195 | `chapters/volcengine/ark/14.3.3 获取基础模型列表.md` |
| 14.3.4 | 获取基础模型信息 | 1675-1679 | 51441-51593 | 97 | `chapters/volcengine/ark/14.3.4 获取基础模型信息.md` |
| 14.4.1 | 批量开通基础模型 | 1680 | 51595-51621 | 13 | `chapters/volcengine/ark/14.4.1 批量开通基础模型.md` |
| 14.4.2 | 启用自动开通新模型 | 1681 | 51622-51646 | 12 | `chapters/volcengine/ark/14.4.2 启用自动开通新模型.md` |
| 14.4.3 | 关闭自动开通新模型 | 1682 | 51647-51671 | 12 | `chapters/volcengine/ark/14.4.3 关闭自动开通新模型.md` |
| 14.4.4 | 查询模型开通详情 | 1683-1689 | 51672-51861 | 152 | `chapters/volcengine/ark/14.4.4 查询模型开通详情.md` |
| 14.4.5 | 查询模型开通列表 | 1690-1697 | 51862-52088 | 186 | `chapters/volcengine/ark/14.4.5 查询模型开通列表.md` |
| 14.5.1 | 批量开通资源 | 1698-1699 | 52090-52123 | 16 | `chapters/volcengine/ark/14.5.1 批量开通资源.md` |
| 14.5.2 | 查询资源开通列表 | 1700-1704 | 52124-52265 | 112 | `chapters/volcengine/ark/14.5.2 查询资源开通列表.md` |
| 14.6.1 | 查询模型限流 | 1705-1709 | 52267-52395 | 99 | `chapters/volcengine/ark/14.6.1 查询模型限流.md` |
| 14.7.1 | 删除定制模型 | 1710-1711 | 52397-52436 | 19 | `chapters/volcengine/ark/14.7.1 删除定制模型.md` |
| 14.7.2 | 获取定制模型信息 | 1712-1717 | 52437-52572 | 102 | `chapters/volcengine/ark/14.7.2 获取定制模型信息.md` |
| 14.7.3 | 更新定制模型 | 1718-1719 | 52573-52620 | 25 | `chapters/volcengine/ark/14.7.3 更新定制模型.md` |
| 14.7.4 | 获取定制模型列表 | 1720-1725 | 52621-52771 | 106 | `chapters/volcengine/ark/14.7.4 获取定制模型列表.md` |
| 14.8.1 | 创建模型调优任务 | 1726-1739 | 52773-53125 | 287 | `chapters/volcengine/ark/14.8.1 创建模型调优任务.md` |
| 14.8.2 | 删除模型调优任务 | 1740 | 53126-53155 | 14 | `chapters/volcengine/ark/14.8.2 删除模型调优任务.md` |
| 14.8.3 | 获取模型调优任务信息 | 1741-1759 | 53156-53659 | 416 | `chapters/volcengine/ark/14.8.3 获取模型调优任务信息.md` |
| 14.8.4 | 查询精调效果指标详细数据 | 1760-1762 | 53660-53731 | 45 | `chapters/volcengine/ark/14.8.4 查询精调效果指标详细数据.md` |
| 14.8.5 | 查询精调效果指标 | 1763-1764 | 53732-53767 | 15 | `chapters/volcengine/ark/14.8.5 查询精调效果指标.md` |
| 14.8.6 | 获取模型调优任务列表 | 1765-1776 | 53768-54082 | 266 | `chapters/volcengine/ark/14.8.6 获取模型调优任务列表.md` |
| 14.8.7 | 重试模型调优任务 | 1777 | 54083-54112 | 13 | `chapters/volcengine/ark/14.8.7 重试模型调优任务.md` |
| 14.8.8 | 停止模型调优任务 | 1778 | 54113-54142 | 14 | `chapters/volcengine/ark/14.8.8 停止模型调优任务.md` |
| 14.8.9 | 更新模型调优任务 | 1779-1780 | 54143-54181 | 16 | `chapters/volcengine/ark/14.8.9 更新模型调优任务.md` |
| 14.9.1 | 开启推理接入点 | 1781-1782 | 54183-54216 | 15 | `chapters/volcengine/ark/14.9.1 开启推理接入点.md` |
| 14.9.2 | 停止推理接入点 | 1783-1784 | 54217-54250 | 13 | `chapters/volcengine/ark/14.9.2 停止推理接入点.md` |
| 14.9.3 | 获取推理接入点列表 | 1785-1792 | 54251-54496 | 177 | `chapters/volcengine/ark/14.9.3 获取推理接入点列表.md` |
| 14.9.4 | 获取推理接入点 | 1793-1797 | 54497-54623 | 91 | `chapters/volcengine/ark/14.9.4 获取推理接入点.md` |
| 14.9.5 | 删除推理接入点 | 1798-1799 | 54624-54656 | 14 | `chapters/volcengine/ark/14.9.5 删除推理接入点.md` |
| 14.9.6 | 更新推理接入点 | 1800-1807 | 54657-54860 | 162 | `chapters/volcengine/ark/14.9.6 更新推理接入点.md` |
| 14.9.7 | 创建推理接入点 | 1808-1817 | 54861-55110 | 196 | `chapters/volcengine/ark/14.9.7 创建推理接入点.md` |
| 14.9.8 | 获取接入点推理应用层加密证书 | 1818-1819 | 55111-55167 | 27 | `chapters/volcengine/ark/14.9.8 获取接入点推理应用层加密证书.md` |
| 14.9.9 | 创建推理接入点滚动升级任务 | 1820-1822 | 55168-55233 | 43 | `chapters/volcengine/ark/14.9.9 创建推理接入点滚动升级任务.md` |
| 14.9.10 | 查询推理接入点滚动升级详情 | 1823-1828 | 55234-55395 | 131 | `chapters/volcengine/ark/14.9.10 查询推理接入点滚动升级详情.md` |
| 14.9.11 | 回滚推理接入点滚动升级 | 1829-1830 | 55396-55428 | 15 | `chapters/volcengine/ark/14.9.11 回滚推理接入点滚动升级.md` |
| 14.9.12 | 取消推理接入点滚动升级 | 1831-1832 | 55429-55461 | 15 | `chapters/volcengine/ark/14.9.12 取消推理接入点滚动升级.md` |
| 14.10.1 | 创建评测任务 | 1833-1839 | 55463-55652 | 137 | `chapters/volcengine/ark/14.10.1 创建评测任务.md` |
| 14.10.2 | 删除评测任务 | 1840-1841 | 55653-55688 | 15 | `chapters/volcengine/ark/14.10.2 删除评测任务.md` |
| 14.10.3 | 获取评测任务 | 1842-1845 | 55689-55791 | 69 | `chapters/volcengine/ark/14.10.3 获取评测任务.md` |
| 14.10.4 | 获取评测任务结果 | 1846-1850 | 55792-55920 | 93 | `chapters/volcengine/ark/14.10.4 获取评测任务结果.md` |
| 14.10.5 | 获取评测任务列表 | 1851-1857 | 55921-56100 | 138 | `chapters/volcengine/ark/14.10.5 获取评测任务列表.md` |
| 14.10.6 | 获取评测任务结果列表 | 1858-1863 | 56101-56271 | 128 | `chapters/volcengine/ark/14.10.6 获取评测任务结果列表.md` |
| 14.10.7 | 停止评测任务 | 1864-1865 | 56272-56306 | 14 | `chapters/volcengine/ark/14.10.7 停止评测任务.md` |
| 14.10.8 | 更新评测任务 | 1866-1867 | 56307-56346 | 20 | `chapters/volcengine/ark/14.10.8 更新评测任务.md` |
| 14.11.1 | 查询推理用量 | 1868-1871 | 56348-56509 | 94 | `chapters/volcengine/ark/14.11.1 查询推理用量.md` |
| 14.11.2 | 查询单请求用量 | 1872-1877 | 56510-56681 | 136 | `chapters/volcengine/ark/14.11.2 查询单请求用量.md` |
| 14.11.3 | 查询异步任务用量 | 1878-1881 | 56682-56773 | 64 | `chapters/volcengine/ark/14.11.3 查询异步任务用量.md` |
| 14.11.4 | 创建用量明细导出任务 | 1882-1884 | 56774-56845 | 36 | `chapters/volcengine/ark/14.11.4 创建用量明细导出任务.md` |
| 14.11.5 | 查询用量明细导出任务状态 | 1885-1888 | 56846-56971 | 78 | `chapters/volcengine/ark/14.11.5 查询用量明细导出任务状态.md` |
| 14.11.6 | 查询模型推理限额 | 1889-1890 | 56972-57014 | 27 | `chapters/volcengine/ark/14.11.6 查询模型推理限额.md` |
| 14.11.7 | 开启模型推理限额 | 1891-1892 | 57015-57055 | 20 | `chapters/volcengine/ark/14.11.7 开启模型推理限额.md` |
| 14.11.8 | 关闭模型推理限额 | 1893-1894 | 57056-57092 | 16 | `chapters/volcengine/ark/14.11.8 关闭模型推理限额.md` |
| 14.12.1 | 创建方舟官方模型产物查询请求 | 1895-1896 | 57094-57128 | 19 | `chapters/volcengine/ark/14.12.1 创建方舟官方模型产物查询请求.md` |
| 14.12.2 | 获取安全审计日志 | 1897-1905 | 57129-57450 | 133 | `chapters/volcengine/ark/14.12.2 获取安全审计日志.md` |
| 14.12.3 | 获取方舟官方产物确认结果 | 1906-1907 | 57451-57497 | 27 | `chapters/volcengine/ark/14.12.3 获取方舟官方产物确认结果.md` |
| 14.13.1 | 上报视频生成模型效果问题 | 1908-1915 | 57499-57759 | 162 | `chapters/volcengine/ark/14.13.1 上报视频生成模型效果问题.md` |
| 14.13.2 | 查询视频生成模型效果问题结果 | 1916-1923 | 57760-58011 | 168 | `chapters/volcengine/ark/14.13.2 查询视频生成模型效果问题结果.md` |
| 14.13.3 | 上报大语言模型效果问题 | 1924-1928 | 58012-58175 | 89 | `chapters/volcengine/ark/14.13.3 上报大语言模型效果问题.md` |
| 14.13.4 | 查询大语言模型效果问题结果 | 1929-1934 | 58176-58342 | 105 | `chapters/volcengine/ark/14.13.4 查询大语言模型效果问题结果.md` |
| 14.13.5 | 上报 3D 生成效果问题 | 1935-1940 | 58343-58554 | 141 | `chapters/volcengine/ark/14.13.5 上报 3D 生成效果问题.md` |
| 14.13.6 | 查询 3D 生成效果问题结果 | 1941-1948 | 58555-58797 | 159 | `chapters/volcengine/ark/14.13.6 查询 3D 生成效果问题结果.md` |
| 15.1 | 兼容 OpenAI SDK | 1949-1952 | 58799-58915 | 103 | `chapters/volcengine/ark/15.1 兼容 OpenAI SDK.md` |
| 15.2 | 向后兼容性 | 1953 | 58916-58961 | 25 | `chapters/volcengine/ark/15.2 向后兼容性.md` |
| 15.3 | 错误码 - 第1部分 | 1953-1975 | 58962-60966 | 1955 | `chapters/volcengine/ark/15.3 错误码 - 第1部分.md` |
| 15.3 | 错误码 - 第2部分·错误码 | 1976-1985 | 60967-61728 | 727 | `chapters/volcengine/ark/15.3 错误码 - 第2部分·错误码.md` |
| 15.4 | SDK 常见使用示例 | 1986-2001 | 61729-62317 | 521 | `chapters/volcengine/ark/15.4 SDK 常见使用示例.md` |
