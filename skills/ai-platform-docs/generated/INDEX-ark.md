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
| 11.2.6.1 | 长轮询拉取待执行 Work | 1032-1036 | 32718-32865 | 77 | `chapters/volcengine/ark/11.2.6.1 长轮询拉取待执行 Work.md` |
| 11.2.6.2 | 认领 Work | 1037-1041 | 32866-33010 | 76 | `chapters/volcengine/ark/11.2.6.2 认领 Work.md` |
| 11.2.6.3 | 续租 Work | 1042-1045 | 33011-33124 | 53 | `chapters/volcengine/ark/11.2.6.3 续租 Work.md` |
| 11.2.6.4 | 查询 Work 队列状态 | 1046-1047 | 33125-33192 | 29 | `chapters/volcengine/ark/11.2.6.4 查询 Work 队列状态.md` |
| 11.2.6.5 | 停止 Work | 1048-1052 | 33193-33363 | 90 | `chapters/volcengine/ark/11.2.6.5 停止 Work.md` |
| 11.2.6.6 | 查询 Work 列表 | 1053-1057 | 33364-33523 | 92 | `chapters/volcengine/ark/11.2.6.6 查询 Work 列表.md` |
| 11.2.6.7 | 查询 Work 详情 | 1058-1061 | 33524-33646 | 64 | `chapters/volcengine/ark/11.2.6.7 查询 Work 详情.md` |
| 11.3.1 | 创建会话 | 1062-1100 | 33648-34852 | 903 | `chapters/volcengine/ark/11.3.1 创建会话.md` |
| 11.3.2 | 查询会话列表 | 1101-1126 | 34853-35613 | 596 | `chapters/volcengine/ark/11.3.2 查询会话列表.md` |
| 11.3.3 | 查询会话详情 | 1127-1152 | 35614-36381 | 588 | `chapters/volcengine/ark/11.3.3 查询会话详情.md` |
| 11.3.4 | 更新会话标题和标签 | 1153-1177 | 36382-37120 | 567 | `chapters/volcengine/ark/11.3.4 更新会话标题和标签.md` |
| 11.3.5 | 升级会话 | 1178-1210 | 37121-38087 | 778 | `chapters/volcengine/ark/11.3.5 升级会话.md` |
| 11.3.6 | 删除会话 | 1211-1212 | 38088-38147 | 26 | `chapters/volcengine/ark/11.3.6 删除会话.md` |
| 11.3.7.1 | 查询会话任务 | 1213-1218 | 38149-38334 | 99 | `chapters/volcengine/ark/11.3.7.1 查询会话任务.md` |
| 11.3.7.2 | 查询会话任务列表 | 1219-1223 | 38335-38505 | 98 | `chapters/volcengine/ark/11.3.7.2 查询会话任务列表.md` |
| 11.3.7.3 | 取消会话任务 | 1224-1226 | 38506-38599 | 36 | `chapters/volcengine/ark/11.3.7.3 取消会话任务.md` |
| 11.3.8.1 | 发送会话事件 | 1227-1230 | 38601-38717 | 53 | `chapters/volcengine/ark/11.3.8.1 发送会话事件.md` |
| 11.3.8.2 | 查询会话事件列表 | 1231-1234 | 38718-38851 | 62 | `chapters/volcengine/ark/11.3.8.2 查询会话事件列表.md` |
| 11.3.8.3 | 流式获取会话事件 | 1235-1239 | 38852-39025 | 50 | `chapters/volcengine/ark/11.3.8.3 流式获取会话事件.md` |
| 11.3.8.4 | 会话事件结构参考 - 第1部分 | 1240-1316 | 39026-40994 | 1748 | `chapters/volcengine/ark/11.3.8.4 会话事件结构参考 - 第1部分.md` |
| 11.3.9.1 | 添加会话资源 | 1317-1320 | 40996-41111 | 51 | `chapters/volcengine/ark/11.3.9.1 添加会话资源.md` |
| 11.3.9.2 | 查询会话资源列表 | 1321-1326 | 41112-41276 | 105 | `chapters/volcengine/ark/11.3.9.2 查询会话资源列表.md` |
| 11.3.9.3 | 查询会话资源 | 1327-1329 | 41277-41371 | 43 | `chapters/volcengine/ark/11.3.9.3 查询会话资源.md` |
| 11.3.10.1 | 查询线程列表 | 1330-1334 | 41373-41512 | 71 | `chapters/volcengine/ark/11.3.10.1 查询线程列表.md` |
| 11.3.10.2 | 查询线程详情 | 1335-1340 | 41513-41697 | 99 | `chapters/volcengine/ark/11.3.10.2 查询线程详情.md` |
| 11.3.10.3 | 查询线程事件列表 | 1341-1344 | 41698-41827 | 57 | `chapters/volcengine/ark/11.3.10.3 查询线程事件列表.md` |
| 11.3.10.4 | 流式获取线程事件 | 1345-1348 | 41828-41962 | 44 | `chapters/volcengine/ark/11.3.10.4 流式获取线程事件.md` |
| 11.4.1 | 创建 Webhook 接入点 | 1349-1352 | 41964-42083 | 64 | `chapters/volcengine/ark/11.4.1 创建 Webhook 接入点.md` |
| 11.4.2 | 查询 Webhook 接入点列表 | 1353-1356 | 42084-42197 | 68 | `chapters/volcengine/ark/11.4.2 查询 Webhook 接入点列表.md` |
| 11.4.3 | 查询 Webhook 接入点详情 | 1357-1359 | 42198-42292 | 53 | `chapters/volcengine/ark/11.4.3 查询 Webhook 接入点详情.md` |
| 11.4.4 | 更新 Webhook 接入点 | 1360-1363 | 42293-42410 | 63 | `chapters/volcengine/ark/11.4.4 更新 Webhook 接入点.md` |
| 11.4.5 | 启用 Webhook 接入点 | 1364-1366 | 42411-42507 | 55 | `chapters/volcengine/ark/11.4.5 启用 Webhook 接入点.md` |
| 11.4.6 | 删除 Webhook 接入点 | 1367 | 42508-42535 | 18 | `chapters/volcengine/ark/11.4.6 删除 Webhook 接入点.md` |
| 11.4.7 | 停用 Webhook 接入点 | 1368-1370 | 42536-42633 | 54 | `chapters/volcengine/ark/11.4.7 停用 Webhook 接入点.md` |
| 11.4.8 | 重置 Webhook 签名密钥 | 1371-1372 | 42634-42668 | 19 | `chapters/volcengine/ark/11.4.8 重置 Webhook 签名密钥.md` |
| 11.4.9 | 发送 Webhook 测试事件 | 1373-1374 | 42669-42713 | 29 | `chapters/volcengine/ark/11.4.9 发送 Webhook 测试事件.md` |
| 11.4.10 | 查询 Webhook 事件详情 | 1375-1376 | 42714-42765 | 35 | `chapters/volcengine/ark/11.4.10 查询 Webhook 事件详情.md` |
| 11.4.11 | 查询 Webhook 事件列表 | 1377-1379 | 42766-42845 | 52 | `chapters/volcengine/ark/11.4.11 查询 Webhook 事件列表.md` |
| 11.4.12 | Webhook 事件结构参考 | 1380-1401 | 42846-43429 | 519 | `chapters/volcengine/ark/11.4.12 Webhook 事件结构参考.md` |
| 11.5.1 | 创建保管库 | 1402-1404 | 43431-43531 | 45 | `chapters/volcengine/ark/11.5.1 创建保管库.md` |
| 11.5.2 | 查询保管库列表 | 1405-1408 | 43532-43651 | 60 | `chapters/volcengine/ark/11.5.2 查询保管库列表.md` |
| 11.5.3 | 查询保管库详情 | 1409-1411 | 43652-43723 | 33 | `chapters/volcengine/ark/11.5.3 查询保管库详情.md` |
| 11.5.4 | 更新保管库 | 1412-1414 | 43724-43827 | 47 | `chapters/volcengine/ark/11.5.4 更新保管库.md` |
| 11.5.5 | 删除保管库 | 1415-1416 | 43828-43884 | 25 | `chapters/volcengine/ark/11.5.5 删除保管库.md` |
| 11.5.6.1 | 创建凭证 | 1417-1432 | 43886-44433 | 376 | `chapters/volcengine/ark/11.5.6.1 创建凭证.md` |
| 11.5.6.2 | 查询凭证列表 | 1433-1441 | 44434-44715 | 188 | `chapters/volcengine/ark/11.5.6.2 查询凭证列表.md` |
| 11.5.6.3 | 查询凭证详情 | 1442-1449 | 44716-44962 | 163 | `chapters/volcengine/ark/11.5.6.3 查询凭证详情.md` |
| 11.5.6.4 | 更新凭证 | 1450-1465 | 44963-45485 | 357 | `chapters/volcengine/ark/11.5.6.4 更新凭证.md` |
| 11.5.6.5 | 删除凭证 | 1466-1467 | 45486-45545 | 30 | `chapters/volcengine/ark/11.5.6.5 删除凭证.md` |
| 11.6.1 | 创建记忆库 | 1468-1472 | 45547-45691 | 72 | `chapters/volcengine/ark/11.6.1 创建记忆库.md` |
| 11.6.2 | 查询记忆库列表 | 1473-1477 | 45692-45850 | 90 | `chapters/volcengine/ark/11.6.2 查询记忆库列表.md` |
| 11.6.3 | 查询记忆库详情 | 1478-1481 | 45851-45968 | 54 | `chapters/volcengine/ark/11.6.3 查询记忆库详情.md` |
| 11.6.4 | 更新记忆库 | 1482-1487 | 45969-46125 | 71 | `chapters/volcengine/ark/11.6.4 更新记忆库.md` |
| 11.6.5 | 删除记忆库 | 1488-1489 | 46126-46186 | 21 | `chapters/volcengine/ark/11.6.5 删除记忆库.md` |
| 11.6.6.1 | 创建记忆 | 1490-1494 | 46188-46323 | 71 | `chapters/volcengine/ark/11.6.6.1 创建记忆.md` |
| 11.6.6.2 | 批量创建记忆 | 1495-1501 | 46324-46567 | 121 | `chapters/volcengine/ark/11.6.6.2 批量创建记忆.md` |
| 11.6.6.3 | 查询记忆列表 | 1502-1506 | 46568-46731 | 87 | `chapters/volcengine/ark/11.6.6.3 查询记忆列表.md` |
| 11.6.6.4 | 查询记忆详情 | 1507-1510 | 46732-46852 | 61 | `chapters/volcengine/ark/11.6.6.4 查询记忆详情.md` |
| 11.6.6.5 | 更新记忆 | 1511-1515 | 46853-46994 | 66 | `chapters/volcengine/ark/11.6.6.5 更新记忆.md` |
| 11.6.6.6 | 删除记忆 | 1516-1517 | 46995-47058 | 25 | `chapters/volcengine/ark/11.6.6.6 删除记忆.md` |
| 11.7.1 | 创建 Dream | 1518-1523 | 47060-47238 | 117 | `chapters/volcengine/ark/11.7.1 创建 Dream.md` |
| 11.7.2 | 查询 Dream 列表 | 1524-1530 | 47239-47465 | 142 | `chapters/volcengine/ark/11.7.2 查询 Dream 列表.md` |
| 11.7.3 | 查询 Dream | 1531-1535 | 47466-47627 | 90 | `chapters/volcengine/ark/11.7.3 查询 Dream.md` |
| 11.7.4 | 取消 Dream | 1536-1541 | 47628-47794 | 93 | `chapters/volcengine/ark/11.7.4 取消 Dream.md` |
| 11.8.1 | 创建技能 | 1542-1545 | 47796-47919 | 61 | `chapters/volcengine/ark/11.8.1 创建技能.md` |
| 11.8.2 | 查询技能列表 | 1546-1549 | 47920-48040 | 68 | `chapters/volcengine/ark/11.8.2 查询技能列表.md` |
| 11.8.3 | 查询技能详情 | 1550-1552 | 48041-48132 | 43 | `chapters/volcengine/ark/11.8.3 查询技能详情.md` |
| 11.8.4 | 设置技能内容保护 | 1553-1555 | 48133-48203 | 43 | `chapters/volcengine/ark/11.8.4 设置技能内容保护.md` |
| 11.8.5 | 删除技能 | 1556-1557 | 48204-48262 | 24 | `chapters/volcengine/ark/11.8.5 删除技能.md` |
| 11.8.6 | 创建新版本的技能 | 1558-1560 | 48263-48364 | 49 | `chapters/volcengine/ark/11.8.6 创建新版本的技能.md` |
| 11.8.7 | 查询技能的版本列表 | 1561-1563 | 48365-48462 | 54 | `chapters/volcengine/ark/11.8.7 查询技能的版本列表.md` |
| 11.8.8 | 查询指定版本的技能 | 1564-1566 | 48463-48534 | 32 | `chapters/volcengine/ark/11.8.8 查询指定版本的技能.md` |
| 11.8.9 | 删除指定版本的技能 | 1567-1568 | 48535-48589 | 22 | `chapters/volcengine/ark/11.8.9 删除指定版本的技能.md` |
| 11.8.10 | 下载指定版本的技能 | 1569-1570 | 48590-48658 | 26 | `chapters/volcengine/ark/11.8.10 下载指定版本的技能.md` |
| 11.8.11 | 扫描 GitHub 技能 | 1571-1573 | 48659-48735 | 48 | `chapters/volcengine/ark/11.8.11 扫描 GitHub 技能.md` |
| 11.8.12 | 导入 GitHub 技能 | 1574-1576 | 48736-48838 | 63 | `chapters/volcengine/ark/11.8.12 导入 GitHub 技能.md` |
| 12.1.1 | 创建批量推理任务 | 1577-1580 | 48841-48921 | 60 | `chapters/volcengine/ark/12.1.1 创建批量推理任务.md` |
| 12.1.2 | 获取批量推理任务列表 | 1581-1588 | 48922-49134 | 165 | `chapters/volcengine/ark/12.1.2 获取批量推理任务列表.md` |
| 12.1.3 | 获取批量推理任务 | 1589-1594 | 49135-49284 | 107 | `chapters/volcengine/ark/12.1.3 获取批量推理任务.md` |
| 12.1.4 | 更新批量推理任务 | 1595-1596 | 49285-49322 | 18 | `chapters/volcengine/ark/12.1.4 更新批量推理任务.md` |
| 12.1.5 | 删除批量推理任务 | 1597-1598 | 49323-49355 | 14 | `chapters/volcengine/ark/12.1.5 删除批量推理任务.md` |
| 12.1.6 | 停止批量推理任务 | 1599-1600 | 49356-49391 | 17 | `chapters/volcengine/ark/12.1.6 停止批量推理任务.md` |
| 12.1.7 | 重启批量推理任务 | 1601-1602 | 49392-49428 | 18 | `chapters/volcengine/ark/12.1.7 重启批量推理任务.md` |
| 12.2 | 批量(Chat) API | 1603-1623 | 49429-49989 | 365 | `chapters/volcengine/ark/12.2 批量(Chat) API.md` |
| 13.1 | 分词 API | 1624-1628 | 49991-50149 | 61 | `chapters/volcengine/ark/13.1 分词 API.md` |
| 14.1.1 | 获取临时 API Key | 1629-1630 | 50152-50201 | 29 | `chapters/volcengine/ark/14.1.1 获取临时 API Key.md` |
| 14.2.1 | 创建个人版套餐 | 1631-1632 | 50203-50264 | 35 | `chapters/volcengine/ark/14.2.1 创建个人版套餐.md` |
| 14.2.2 | 续费个人版套餐 | 1633-1634 | 50265-50313 | 27 | `chapters/volcengine/ark/14.2.2 续费个人版套餐.md` |
| 14.2.3 | 查询个人版套餐 | 1635-1636 | 50314-50356 | 24 | `chapters/volcengine/ark/14.2.3 查询个人版套餐.md` |
| 14.2.4.1 | 查询 Agent Plan 支持的模型列表 | 1637-1638 | 50358-50392 | 16 | `chapters/volcengine/ark/14.2.4.1 查询 Agent Plan 支持的模型列表.md` |
| 14.2.4.2 | 轮换个人版 API Key | 1639-1640 | 50393-50435 | 22 | `chapters/volcengine/ark/14.2.4.2 轮换个人版 API Key.md` |
| 14.2.4.3 | 获取套餐 AFP 额度 | 1641-1644 | 50436-50532 | 69 | `chapters/volcengine/ark/14.2.4.3 获取套餐 AFP 额度.md` |
| 14.2.4.4 | 获取套餐用量详情 | 1645-1647 | 50533-50607 | 43 | `chapters/volcengine/ark/14.2.4.4 获取套餐用量详情.md` |
| 14.2.5.1 | 查询 Coding Plan 支持的模型列表 | 1648 | 50609-50635 | 15 | `chapters/volcengine/ark/14.2.5.1 查询 Coding Plan 支持的模型列表.md` |
| 14.3.1 | 获取基础模型版本列表 | 1649-1652 | 50637-50748 | 77 | `chapters/volcengine/ark/14.3.1 获取基础模型版本列表.md` |
| 14.3.2 | 获取基础模型版本信息 | 1653-1666 | 50749-51131 | 289 | `chapters/volcengine/ark/14.3.2 获取基础模型版本信息.md` |
| 14.3.3 | 获取基础模型列表 | 1667-1674 | 51132-51425 | 195 | `chapters/volcengine/ark/14.3.3 获取基础模型列表.md` |
| 14.3.4 | 获取基础模型信息 | 1675-1679 | 51426-51578 | 97 | `chapters/volcengine/ark/14.3.4 获取基础模型信息.md` |
| 14.4.1 | 批量开通基础模型 | 1680 | 51580-51606 | 13 | `chapters/volcengine/ark/14.4.1 批量开通基础模型.md` |
| 14.4.2 | 启用自动开通新模型 | 1681 | 51607-51631 | 12 | `chapters/volcengine/ark/14.4.2 启用自动开通新模型.md` |
| 14.4.3 | 关闭自动开通新模型 | 1682 | 51632-51656 | 12 | `chapters/volcengine/ark/14.4.3 关闭自动开通新模型.md` |
| 14.4.4 | 查询模型开通详情 | 1683-1689 | 51657-51846 | 152 | `chapters/volcengine/ark/14.4.4 查询模型开通详情.md` |
| 14.4.5 | 查询模型开通列表 | 1690-1697 | 51847-52073 | 186 | `chapters/volcengine/ark/14.4.5 查询模型开通列表.md` |
| 14.5.1 | 批量开通资源 | 1698-1699 | 52075-52108 | 16 | `chapters/volcengine/ark/14.5.1 批量开通资源.md` |
| 14.5.2 | 查询资源开通列表 | 1700-1704 | 52109-52250 | 112 | `chapters/volcengine/ark/14.5.2 查询资源开通列表.md` |
| 14.6.1 | 查询模型限流 | 1705-1709 | 52252-52380 | 99 | `chapters/volcengine/ark/14.6.1 查询模型限流.md` |
| 14.7.1 | 删除定制模型 | 1710-1711 | 52382-52421 | 19 | `chapters/volcengine/ark/14.7.1 删除定制模型.md` |
| 14.7.2 | 获取定制模型信息 | 1712-1717 | 52422-52557 | 102 | `chapters/volcengine/ark/14.7.2 获取定制模型信息.md` |
| 14.7.3 | 更新定制模型 | 1718-1719 | 52558-52605 | 25 | `chapters/volcengine/ark/14.7.3 更新定制模型.md` |
| 14.7.4 | 获取定制模型列表 | 1720-1725 | 52606-52756 | 106 | `chapters/volcengine/ark/14.7.4 获取定制模型列表.md` |
| 14.8.1 | 创建模型调优任务 | 1726-1739 | 52758-53110 | 287 | `chapters/volcengine/ark/14.8.1 创建模型调优任务.md` |
| 14.8.2 | 删除模型调优任务 | 1740 | 53111-53140 | 14 | `chapters/volcengine/ark/14.8.2 删除模型调优任务.md` |
| 14.8.3 | 获取模型调优任务信息 | 1741-1759 | 53141-53644 | 416 | `chapters/volcengine/ark/14.8.3 获取模型调优任务信息.md` |
| 14.8.4 | 查询精调效果指标详细数据 | 1760-1762 | 53645-53716 | 45 | `chapters/volcengine/ark/14.8.4 查询精调效果指标详细数据.md` |
| 14.8.5 | 查询精调效果指标 | 1763-1764 | 53717-53752 | 15 | `chapters/volcengine/ark/14.8.5 查询精调效果指标.md` |
| 14.8.6 | 获取模型调优任务列表 | 1765-1776 | 53753-54067 | 266 | `chapters/volcengine/ark/14.8.6 获取模型调优任务列表.md` |
| 14.8.7 | 重试模型调优任务 | 1777 | 54068-54097 | 13 | `chapters/volcengine/ark/14.8.7 重试模型调优任务.md` |
| 14.8.8 | 停止模型调优任务 | 1778 | 54098-54127 | 14 | `chapters/volcengine/ark/14.8.8 停止模型调优任务.md` |
| 14.8.9 | 更新模型调优任务 | 1779-1780 | 54128-54166 | 16 | `chapters/volcengine/ark/14.8.9 更新模型调优任务.md` |
| 14.9.1 | 开启推理接入点 | 1781-1782 | 54168-54201 | 15 | `chapters/volcengine/ark/14.9.1 开启推理接入点.md` |
| 14.9.2 | 停止推理接入点 | 1783-1784 | 54202-54235 | 13 | `chapters/volcengine/ark/14.9.2 停止推理接入点.md` |
| 14.9.3 | 获取推理接入点列表 | 1785-1792 | 54236-54481 | 177 | `chapters/volcengine/ark/14.9.3 获取推理接入点列表.md` |
| 14.9.4 | 获取推理接入点 | 1793-1797 | 54482-54608 | 91 | `chapters/volcengine/ark/14.9.4 获取推理接入点.md` |
| 14.9.5 | 删除推理接入点 | 1798-1799 | 54609-54641 | 14 | `chapters/volcengine/ark/14.9.5 删除推理接入点.md` |
| 14.9.6 | 更新推理接入点 | 1800-1807 | 54642-54845 | 162 | `chapters/volcengine/ark/14.9.6 更新推理接入点.md` |
| 14.9.7 | 创建推理接入点 | 1808-1817 | 54846-55095 | 196 | `chapters/volcengine/ark/14.9.7 创建推理接入点.md` |
| 14.9.8 | 获取接入点推理应用层加密证书 | 1818-1819 | 55096-55152 | 27 | `chapters/volcengine/ark/14.9.8 获取接入点推理应用层加密证书.md` |
| 14.9.9 | 创建推理接入点滚动升级任务 | 1820-1822 | 55153-55218 | 43 | `chapters/volcengine/ark/14.9.9 创建推理接入点滚动升级任务.md` |
| 14.9.10 | 查询推理接入点滚动升级详情 | 1823-1828 | 55219-55380 | 131 | `chapters/volcengine/ark/14.9.10 查询推理接入点滚动升级详情.md` |
| 14.9.11 | 回滚推理接入点滚动升级 | 1829-1830 | 55381-55413 | 15 | `chapters/volcengine/ark/14.9.11 回滚推理接入点滚动升级.md` |
| 14.9.12 | 取消推理接入点滚动升级 | 1831-1832 | 55414-55446 | 15 | `chapters/volcengine/ark/14.9.12 取消推理接入点滚动升级.md` |
| 14.10.1 | 创建评测任务 | 1833-1839 | 55448-55637 | 137 | `chapters/volcengine/ark/14.10.1 创建评测任务.md` |
| 14.10.2 | 删除评测任务 | 1840-1841 | 55638-55673 | 15 | `chapters/volcengine/ark/14.10.2 删除评测任务.md` |
| 14.10.3 | 获取评测任务 | 1842-1845 | 55674-55776 | 69 | `chapters/volcengine/ark/14.10.3 获取评测任务.md` |
| 14.10.4 | 获取评测任务结果 | 1846-1850 | 55777-55905 | 93 | `chapters/volcengine/ark/14.10.4 获取评测任务结果.md` |
| 14.10.5 | 获取评测任务列表 | 1851-1857 | 55906-56085 | 138 | `chapters/volcengine/ark/14.10.5 获取评测任务列表.md` |
| 14.10.6 | 获取评测任务结果列表 | 1858-1863 | 56086-56256 | 128 | `chapters/volcengine/ark/14.10.6 获取评测任务结果列表.md` |
| 14.10.7 | 停止评测任务 | 1864-1865 | 56257-56291 | 14 | `chapters/volcengine/ark/14.10.7 停止评测任务.md` |
| 14.10.8 | 更新评测任务 | 1866-1867 | 56292-56331 | 20 | `chapters/volcengine/ark/14.10.8 更新评测任务.md` |
| 14.11.1 | 查询推理用量 | 1868-1871 | 56333-56494 | 94 | `chapters/volcengine/ark/14.11.1 查询推理用量.md` |
| 14.11.2 | 查询单请求用量 | 1872-1877 | 56495-56666 | 136 | `chapters/volcengine/ark/14.11.2 查询单请求用量.md` |
| 14.11.3 | 查询异步任务用量 | 1878-1881 | 56667-56758 | 64 | `chapters/volcengine/ark/14.11.3 查询异步任务用量.md` |
| 14.11.4 | 创建用量明细导出任务 | 1882-1884 | 56759-56830 | 36 | `chapters/volcengine/ark/14.11.4 创建用量明细导出任务.md` |
| 14.11.5 | 查询用量明细导出任务状态 | 1885-1888 | 56831-56956 | 78 | `chapters/volcengine/ark/14.11.5 查询用量明细导出任务状态.md` |
| 14.11.6 | 查询模型推理限额 | 1889-1890 | 56957-56999 | 27 | `chapters/volcengine/ark/14.11.6 查询模型推理限额.md` |
| 14.11.7 | 开启模型推理限额 | 1891-1892 | 57000-57040 | 20 | `chapters/volcengine/ark/14.11.7 开启模型推理限额.md` |
| 14.11.8 | 关闭模型推理限额 | 1893-1894 | 57041-57077 | 16 | `chapters/volcengine/ark/14.11.8 关闭模型推理限额.md` |
| 14.12.1 | 创建方舟官方模型产物查询请求 | 1895-1896 | 57079-57113 | 19 | `chapters/volcengine/ark/14.12.1 创建方舟官方模型产物查询请求.md` |
| 14.12.2 | 获取安全审计日志 | 1897-1905 | 57114-57435 | 133 | `chapters/volcengine/ark/14.12.2 获取安全审计日志.md` |
| 14.12.3 | 获取方舟官方产物确认结果 | 1906-1907 | 57436-57482 | 27 | `chapters/volcengine/ark/14.12.3 获取方舟官方产物确认结果.md` |
| 14.13.1 | 上报视频生成模型效果问题 | 1908-1915 | 57484-57744 | 162 | `chapters/volcengine/ark/14.13.1 上报视频生成模型效果问题.md` |
| 14.13.2 | 查询视频生成模型效果问题结果 | 1916-1923 | 57745-57996 | 168 | `chapters/volcengine/ark/14.13.2 查询视频生成模型效果问题结果.md` |
| 14.13.3 | 上报大语言模型效果问题 | 1924-1928 | 57997-58160 | 89 | `chapters/volcengine/ark/14.13.3 上报大语言模型效果问题.md` |
| 14.13.4 | 查询大语言模型效果问题结果 | 1929-1934 | 58161-58327 | 105 | `chapters/volcengine/ark/14.13.4 查询大语言模型效果问题结果.md` |
| 14.13.5 | 上报 3D 生成效果问题 | 1935-1940 | 58328-58539 | 141 | `chapters/volcengine/ark/14.13.5 上报 3D 生成效果问题.md` |
| 14.13.6 | 查询 3D 生成效果问题结果 | 1941-1948 | 58540-58782 | 159 | `chapters/volcengine/ark/14.13.6 查询 3D 生成效果问题结果.md` |
| 15.1 | 兼容 OpenAI SDK | 1949-1952 | 58784-58900 | 103 | `chapters/volcengine/ark/15.1 兼容 OpenAI SDK.md` |
| 15.2 | 向后兼容性 | 1953 | 58901-58946 | 25 | `chapters/volcengine/ark/15.2 向后兼容性.md` |
| 15.3 | 错误码 - 第1部分 | 1953-1975 | 58947-60951 | 1955 | `chapters/volcengine/ark/15.3 错误码 - 第1部分.md` |
| 15.3 | 错误码 - 第2部分·错误码 | 1976-1985 | 60952-61713 | 727 | `chapters/volcengine/ark/15.3 错误码 - 第2部分·错误码.md` |
| 15.4 | SDK 常见使用示例 | 1986-2001 | 61714-62302 | 521 | `chapters/volcengine/ark/15.4 SDK 常见使用示例.md` |
