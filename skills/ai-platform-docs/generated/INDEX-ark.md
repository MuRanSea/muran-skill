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
| 7.4 | 取消或删除视频生成任务 | 820-821 | 25635-25723 | 56 | `chapters/volcengine/ark/7.4 取消或删除视频生成任务.md` |
| 8.1 | 图片生成 API | 822-862 | 25725-27448 | 738 | `chapters/volcengine/ark/8.1 图片生成 API.md` |
| 8.2 | 图片生成流式响应事件 | 863-868 | 27449-27627 | 158 | `chapters/volcengine/ark/8.2 图片生成流式响应事件.md` |
| 9.1.1 | 创建 3D 生成任务 API | 869-874 | 27630-27812 | 102 | `chapters/volcengine/ark/9.1.1 创建 3D 生成任务 API.md` |
| 9.1.2 | 查询 3D 生成任务 API | 875-878 | 27813-27947 | 63 | `chapters/volcengine/ark/9.1.2 查询 3D 生成任务 API.md` |
| 9.1.3 | 查询 3D 生成任务列表 | 879-885 | 27948-28173 | 105 | `chapters/volcengine/ark/9.1.3 查询 3D 生成任务列表.md` |
| 9.1.4 | 取消或删除 3D 生成任务 | 886-887 | 28174-28260 | 52 | `chapters/volcengine/ark/9.1.4 取消或删除 3D 生成任务.md` |
| 9.2.1 | 创建3D生成任务 | 888-894 | 28262-28506 | 152 | `chapters/volcengine/ark/9.2.1 创建3D生成任务.md` |
| 9.2.2 | 查询3D生成任务 | 895-897 | 28507-28586 | 52 | `chapters/volcengine/ark/9.2.2 查询3D生成任务.md` |
| 9.2.3 | 查询3D生成任务列表 | 898-901 | 28587-28712 | 85 | `chapters/volcengine/ark/9.2.3 查询3D生成任务列表.md` |
| 9.2.4 | 取消或删除3D生成任务 | 902-903 | 28713-28757 | 34 | `chapters/volcengine/ark/9.2.4 取消或删除3D生成任务.md` |
| 9.3.1 | 创建3D生成任务 | 904-908 | 28759-28903 | 98 | `chapters/volcengine/ark/9.3.1 创建3D生成任务.md` |
| 9.3.2 | 查询3D生成任务 | 909-911 | 28904-28983 | 51 | `chapters/volcengine/ark/9.3.2 查询3D生成任务.md` |
| 9.3.3 | 查询3D生成任务列表 | 912-915 | 28984-29109 | 86 | `chapters/volcengine/ark/9.3.3 查询3D生成任务列表.md` |
| 9.3.4 | 取消或删除3D生成任务 | 916-917 | 29110-29154 | 34 | `chapters/volcengine/ark/9.3.4 取消或删除3D生成任务.md` |
| 10.1 | 多模态向量化 API | 918-928 | 29156-29574 | 201 | `chapters/volcengine/ark/10.1 多模态向量化 API.md` |
| 11.1.1 | 创建智能体 | 929-947 | 29577-30165 | 406 | `chapters/volcengine/ark/11.1.1 创建智能体.md` |
| 11.1.2 | 查询智能体列表 | 948-958 | 30166-30501 | 238 | `chapters/volcengine/ark/11.1.2 查询智能体列表.md` |
| 11.1.3 | 查询智能体详情 | 959-968 | 30502-30790 | 201 | `chapters/volcengine/ark/11.1.3 查询智能体详情.md` |
| 11.1.4 | 更新智能体 | 969-987 | 30791-31429 | 427 | `chapters/volcengine/ark/11.1.4 更新智能体.md` |
| 11.1.5 | 查询智能体版本列表 | 988-998 | 31430-31764 | 222 | `chapters/volcengine/ark/11.1.5 查询智能体版本列表.md` |
| 11.1.6 | 删除智能体 | 999-1000 | 31765-31819 | 21 | `chapters/volcengine/ark/11.1.6 删除智能体.md` |
| 11.2.1 | 创建环境 | 1001-1009 | 31821-32099 | 186 | `chapters/volcengine/ark/11.2.1 创建环境.md` |
| 11.2.2 | 查询环境列表 | 1010-1015 | 32100-32267 | 116 | `chapters/volcengine/ark/11.2.2 查询环境列表.md` |
| 11.2.3 | 查询环境详情 | 1016-1020 | 32268-32414 | 89 | `chapters/volcengine/ark/11.2.3 查询环境详情.md` |
| 11.2.4 | 更新环境 | 1021-1029 | 32415-32698 | 181 | `chapters/volcengine/ark/11.2.4 更新环境.md` |
| 11.2.5 | 删除环境 | 1030-1031 | 32699-32756 | 25 | `chapters/volcengine/ark/11.2.5 删除环境.md` |
| 11.2.6.1 | 长轮询拉取待执行 Work | 1032-1036 | 32758-32905 | 77 | `chapters/volcengine/ark/11.2.6.1 长轮询拉取待执行 Work.md` |
| 11.2.6.2 | 认领 Work | 1037-1041 | 32906-33050 | 76 | `chapters/volcengine/ark/11.2.6.2 认领 Work.md` |
| 11.2.6.3 | 续租 Work | 1042-1045 | 33051-33164 | 53 | `chapters/volcengine/ark/11.2.6.3 续租 Work.md` |
| 11.2.6.4 | 查询 Work 队列状态 | 1046-1047 | 33165-33232 | 29 | `chapters/volcengine/ark/11.2.6.4 查询 Work 队列状态.md` |
| 11.2.6.5 | 停止 Work | 1048-1052 | 33233-33403 | 90 | `chapters/volcengine/ark/11.2.6.5 停止 Work.md` |
| 11.2.6.6 | 查询 Work 列表 | 1053-1057 | 33404-33563 | 92 | `chapters/volcengine/ark/11.2.6.6 查询 Work 列表.md` |
| 11.2.6.7 | 查询 Work 详情 | 1058-1061 | 33564-33686 | 64 | `chapters/volcengine/ark/11.2.6.7 查询 Work 详情.md` |
| 11.3.1 | 创建会话 | 1062-1100 | 33688-34897 | 905 | `chapters/volcengine/ark/11.3.1 创建会话.md` |
| 11.3.2 | 查询会话列表 | 1101-1126 | 34898-35669 | 602 | `chapters/volcengine/ark/11.3.2 查询会话列表.md` |
| 11.3.3 | 查询会话详情 | 1127-1152 | 35670-36440 | 590 | `chapters/volcengine/ark/11.3.3 查询会话详情.md` |
| 11.3.4 | 更新会话标题和标签 | 1153-1177 | 36441-37185 | 570 | `chapters/volcengine/ark/11.3.4 更新会话标题和标签.md` |
| 11.3.5 | 升级会话 | 1178-1210 | 37186-38157 | 781 | `chapters/volcengine/ark/11.3.5 升级会话.md` |
| 11.3.6 | 删除会话 | 1211-1212 | 38158-38217 | 27 | `chapters/volcengine/ark/11.3.6 删除会话.md` |
| 11.3.7.1 | 查询会话任务 | 1213-1218 | 38219-38404 | 99 | `chapters/volcengine/ark/11.3.7.1 查询会话任务.md` |
| 11.3.7.2 | 查询会话任务列表 | 1219-1223 | 38405-38575 | 98 | `chapters/volcengine/ark/11.3.7.2 查询会话任务列表.md` |
| 11.3.7.3 | 取消会话任务 | 1224-1226 | 38576-38669 | 36 | `chapters/volcengine/ark/11.3.7.3 取消会话任务.md` |
| 11.3.8.1 | 发送会话事件 | 1227-1230 | 38671-38787 | 53 | `chapters/volcengine/ark/11.3.8.1 发送会话事件.md` |
| 11.3.8.2 | 查询会话事件列表 | 1231-1234 | 38788-38921 | 62 | `chapters/volcengine/ark/11.3.8.2 查询会话事件列表.md` |
| 11.3.8.3 | 流式获取会话事件 | 1235-1239 | 38922-39095 | 50 | `chapters/volcengine/ark/11.3.8.3 流式获取会话事件.md` |
| 11.3.8.4 | 会话事件结构参考 - 第1部分 | 1240-1316 | 39096-41064 | 1748 | `chapters/volcengine/ark/11.3.8.4 会话事件结构参考 - 第1部分.md` |
| 11.3.9.1 | 添加会话资源 | 1317-1320 | 41066-41181 | 51 | `chapters/volcengine/ark/11.3.9.1 添加会话资源.md` |
| 11.3.9.2 | 查询会话资源列表 | 1321-1326 | 41182-41346 | 105 | `chapters/volcengine/ark/11.3.9.2 查询会话资源列表.md` |
| 11.3.9.3 | 查询会话资源 | 1327-1329 | 41347-41441 | 43 | `chapters/volcengine/ark/11.3.9.3 查询会话资源.md` |
| 11.3.10.1 | 查询线程列表 | 1330-1334 | 41443-41582 | 71 | `chapters/volcengine/ark/11.3.10.1 查询线程列表.md` |
| 11.3.10.2 | 查询线程详情 | 1335-1340 | 41583-41767 | 99 | `chapters/volcengine/ark/11.3.10.2 查询线程详情.md` |
| 11.3.10.3 | 查询线程事件列表 | 1341-1344 | 41768-41897 | 57 | `chapters/volcengine/ark/11.3.10.3 查询线程事件列表.md` |
| 11.3.10.4 | 流式获取线程事件 | 1345-1348 | 41898-42032 | 44 | `chapters/volcengine/ark/11.3.10.4 流式获取线程事件.md` |
| 11.4.1 | 创建 Webhook 接入点 | 1349-1352 | 42034-42153 | 64 | `chapters/volcengine/ark/11.4.1 创建 Webhook 接入点.md` |
| 11.4.2 | 查询 Webhook 接入点列表 | 1353-1356 | 42154-42267 | 68 | `chapters/volcengine/ark/11.4.2 查询 Webhook 接入点列表.md` |
| 11.4.3 | 查询 Webhook 接入点详情 | 1357-1359 | 42268-42362 | 53 | `chapters/volcengine/ark/11.4.3 查询 Webhook 接入点详情.md` |
| 11.4.4 | 更新 Webhook 接入点 | 1360-1363 | 42363-42480 | 63 | `chapters/volcengine/ark/11.4.4 更新 Webhook 接入点.md` |
| 11.4.5 | 启用 Webhook 接入点 | 1364-1366 | 42481-42577 | 55 | `chapters/volcengine/ark/11.4.5 启用 Webhook 接入点.md` |
| 11.4.6 | 删除 Webhook 接入点 | 1367 | 42578-42605 | 18 | `chapters/volcengine/ark/11.4.6 删除 Webhook 接入点.md` |
| 11.4.7 | 停用 Webhook 接入点 | 1368-1370 | 42606-42703 | 54 | `chapters/volcengine/ark/11.4.7 停用 Webhook 接入点.md` |
| 11.4.8 | 重置 Webhook 签名密钥 | 1371-1372 | 42704-42738 | 19 | `chapters/volcengine/ark/11.4.8 重置 Webhook 签名密钥.md` |
| 11.4.9 | 发送 Webhook 测试事件 | 1373-1374 | 42739-42783 | 29 | `chapters/volcengine/ark/11.4.9 发送 Webhook 测试事件.md` |
| 11.4.10 | 查询 Webhook 事件详情 | 1375-1376 | 42784-42835 | 35 | `chapters/volcengine/ark/11.4.10 查询 Webhook 事件详情.md` |
| 11.4.11 | 查询 Webhook 事件列表 | 1377-1379 | 42836-42915 | 52 | `chapters/volcengine/ark/11.4.11 查询 Webhook 事件列表.md` |
| 11.4.12 | Webhook 事件结构参考 | 1380-1401 | 42916-43499 | 519 | `chapters/volcengine/ark/11.4.12 Webhook 事件结构参考.md` |
| 11.5.1 | 创建保管库 | 1402-1404 | 43501-43601 | 45 | `chapters/volcengine/ark/11.5.1 创建保管库.md` |
| 11.5.2 | 查询保管库列表 | 1405-1408 | 43602-43721 | 60 | `chapters/volcengine/ark/11.5.2 查询保管库列表.md` |
| 11.5.3 | 查询保管库详情 | 1409-1411 | 43722-43793 | 33 | `chapters/volcengine/ark/11.5.3 查询保管库详情.md` |
| 11.5.4 | 更新保管库 | 1412-1414 | 43794-43897 | 47 | `chapters/volcengine/ark/11.5.4 更新保管库.md` |
| 11.5.5 | 删除保管库 | 1415-1416 | 43898-43954 | 25 | `chapters/volcengine/ark/11.5.5 删除保管库.md` |
| 11.5.6.1 | 创建凭证 | 1417-1432 | 43956-44503 | 376 | `chapters/volcengine/ark/11.5.6.1 创建凭证.md` |
| 11.5.6.2 | 查询凭证列表 | 1433-1441 | 44504-44785 | 188 | `chapters/volcengine/ark/11.5.6.2 查询凭证列表.md` |
| 11.5.6.3 | 查询凭证详情 | 1442-1449 | 44786-45032 | 163 | `chapters/volcengine/ark/11.5.6.3 查询凭证详情.md` |
| 11.5.6.4 | 更新凭证 | 1450-1465 | 45033-45555 | 357 | `chapters/volcengine/ark/11.5.6.4 更新凭证.md` |
| 11.5.6.5 | 删除凭证 | 1466-1467 | 45556-45615 | 30 | `chapters/volcengine/ark/11.5.6.5 删除凭证.md` |
| 11.6.1 | 创建记忆库 | 1468-1472 | 45617-45761 | 72 | `chapters/volcengine/ark/11.6.1 创建记忆库.md` |
| 11.6.2 | 查询记忆库列表 | 1473-1477 | 45762-45920 | 90 | `chapters/volcengine/ark/11.6.2 查询记忆库列表.md` |
| 11.6.3 | 查询记忆库详情 | 1478-1481 | 45921-46038 | 54 | `chapters/volcengine/ark/11.6.3 查询记忆库详情.md` |
| 11.6.4 | 更新记忆库 | 1482-1487 | 46039-46195 | 71 | `chapters/volcengine/ark/11.6.4 更新记忆库.md` |
| 11.6.5 | 删除记忆库 | 1488-1489 | 46196-46256 | 21 | `chapters/volcengine/ark/11.6.5 删除记忆库.md` |
| 11.6.6.1 | 创建记忆 | 1490-1494 | 46258-46393 | 71 | `chapters/volcengine/ark/11.6.6.1 创建记忆.md` |
| 11.6.6.2 | 批量创建记忆 | 1495-1501 | 46394-46637 | 121 | `chapters/volcengine/ark/11.6.6.2 批量创建记忆.md` |
| 11.6.6.3 | 查询记忆列表 | 1502-1506 | 46638-46801 | 87 | `chapters/volcengine/ark/11.6.6.3 查询记忆列表.md` |
| 11.6.6.4 | 查询记忆详情 | 1507-1510 | 46802-46922 | 61 | `chapters/volcengine/ark/11.6.6.4 查询记忆详情.md` |
| 11.6.6.5 | 更新记忆 | 1511-1515 | 46923-47064 | 66 | `chapters/volcengine/ark/11.6.6.5 更新记忆.md` |
| 11.6.6.6 | 删除记忆 | 1516-1517 | 47065-47128 | 25 | `chapters/volcengine/ark/11.6.6.6 删除记忆.md` |
| 11.7.1 | 创建 Dream | 1518-1523 | 47130-47308 | 117 | `chapters/volcengine/ark/11.7.1 创建 Dream.md` |
| 11.7.2 | 查询 Dream 列表 | 1524-1530 | 47309-47535 | 142 | `chapters/volcengine/ark/11.7.2 查询 Dream 列表.md` |
| 11.7.3 | 查询 Dream | 1531-1535 | 47536-47697 | 90 | `chapters/volcengine/ark/11.7.3 查询 Dream.md` |
| 11.7.4 | 取消 Dream | 1536-1541 | 47698-47864 | 93 | `chapters/volcengine/ark/11.7.4 取消 Dream.md` |
| 11.8.1 | 创建技能 | 1542-1545 | 47866-47989 | 61 | `chapters/volcengine/ark/11.8.1 创建技能.md` |
| 11.8.2 | 查询技能列表 | 1546-1549 | 47990-48110 | 68 | `chapters/volcengine/ark/11.8.2 查询技能列表.md` |
| 11.8.3 | 查询技能详情 | 1550-1552 | 48111-48202 | 43 | `chapters/volcengine/ark/11.8.3 查询技能详情.md` |
| 11.8.4 | 设置技能内容保护 | 1553-1555 | 48203-48273 | 43 | `chapters/volcengine/ark/11.8.4 设置技能内容保护.md` |
| 11.8.5 | 删除技能 | 1556-1557 | 48274-48332 | 24 | `chapters/volcengine/ark/11.8.5 删除技能.md` |
| 11.8.6 | 创建新版本的技能 | 1558-1560 | 48333-48434 | 49 | `chapters/volcengine/ark/11.8.6 创建新版本的技能.md` |
| 11.8.7 | 查询技能的版本列表 | 1561-1563 | 48435-48532 | 54 | `chapters/volcengine/ark/11.8.7 查询技能的版本列表.md` |
| 11.8.8 | 查询指定版本的技能 | 1564-1566 | 48533-48604 | 32 | `chapters/volcengine/ark/11.8.8 查询指定版本的技能.md` |
| 11.8.9 | 删除指定版本的技能 | 1567-1568 | 48605-48659 | 22 | `chapters/volcengine/ark/11.8.9 删除指定版本的技能.md` |
| 11.8.10 | 下载指定版本的技能 | 1569-1570 | 48660-48728 | 26 | `chapters/volcengine/ark/11.8.10 下载指定版本的技能.md` |
| 11.8.11 | 扫描 GitHub 技能 | 1571-1573 | 48729-48805 | 48 | `chapters/volcengine/ark/11.8.11 扫描 GitHub 技能.md` |
| 11.8.12 | 导入 GitHub 技能 | 1574-1576 | 48806-48908 | 63 | `chapters/volcengine/ark/11.8.12 导入 GitHub 技能.md` |
| 12.1.1 | 创建批量推理任务 | 1577-1580 | 48911-48991 | 60 | `chapters/volcengine/ark/12.1.1 创建批量推理任务.md` |
| 12.1.2 | 获取批量推理任务列表 | 1581-1588 | 48992-49204 | 165 | `chapters/volcengine/ark/12.1.2 获取批量推理任务列表.md` |
| 12.1.3 | 获取批量推理任务 | 1589-1594 | 49205-49354 | 107 | `chapters/volcengine/ark/12.1.3 获取批量推理任务.md` |
| 12.1.4 | 更新批量推理任务 | 1595-1596 | 49355-49392 | 18 | `chapters/volcengine/ark/12.1.4 更新批量推理任务.md` |
| 12.1.5 | 删除批量推理任务 | 1597-1598 | 49393-49425 | 14 | `chapters/volcengine/ark/12.1.5 删除批量推理任务.md` |
| 12.1.6 | 停止批量推理任务 | 1599-1600 | 49426-49461 | 17 | `chapters/volcengine/ark/12.1.6 停止批量推理任务.md` |
| 12.1.7 | 重启批量推理任务 | 1601-1602 | 49462-49498 | 18 | `chapters/volcengine/ark/12.1.7 重启批量推理任务.md` |
| 12.2 | 批量(Chat) API | 1603-1623 | 49499-50059 | 365 | `chapters/volcengine/ark/12.2 批量(Chat) API.md` |
| 13.1 | 分词 API | 1624-1628 | 50061-50219 | 61 | `chapters/volcengine/ark/13.1 分词 API.md` |
| 14.1.1 | 获取临时 API Key | 1629-1630 | 50222-50271 | 29 | `chapters/volcengine/ark/14.1.1 获取临时 API Key.md` |
| 14.2.1 | 创建个人版套餐 | 1631-1632 | 50273-50334 | 35 | `chapters/volcengine/ark/14.2.1 创建个人版套餐.md` |
| 14.2.2 | 续费个人版套餐 | 1633-1634 | 50335-50383 | 27 | `chapters/volcengine/ark/14.2.2 续费个人版套餐.md` |
| 14.2.3 | 查询个人版套餐 | 1635-1636 | 50384-50426 | 24 | `chapters/volcengine/ark/14.2.3 查询个人版套餐.md` |
| 14.2.4.1 | 查询 Agent Plan 支持的模型列表 | 1637-1638 | 50428-50462 | 16 | `chapters/volcengine/ark/14.2.4.1 查询 Agent Plan 支持的模型列表.md` |
| 14.2.4.2 | 轮换个人版 API Key | 1639-1640 | 50463-50505 | 22 | `chapters/volcengine/ark/14.2.4.2 轮换个人版 API Key.md` |
| 14.2.4.3 | 获取套餐 AFP 额度 | 1641-1644 | 50506-50602 | 69 | `chapters/volcengine/ark/14.2.4.3 获取套餐 AFP 额度.md` |
| 14.2.4.4 | 获取套餐用量详情 | 1645-1647 | 50603-50677 | 43 | `chapters/volcengine/ark/14.2.4.4 获取套餐用量详情.md` |
| 14.2.5.1 | 查询 Coding Plan 支持的模型列表 | 1648 | 50679-50705 | 15 | `chapters/volcengine/ark/14.2.5.1 查询 Coding Plan 支持的模型列表.md` |
| 14.3.1 | 获取基础模型版本列表 | 1649-1652 | 50707-50818 | 77 | `chapters/volcengine/ark/14.3.1 获取基础模型版本列表.md` |
| 14.3.2 | 获取基础模型版本信息 | 1653-1666 | 50819-51201 | 289 | `chapters/volcengine/ark/14.3.2 获取基础模型版本信息.md` |
| 14.3.3 | 获取基础模型列表 | 1667-1674 | 51202-51495 | 195 | `chapters/volcengine/ark/14.3.3 获取基础模型列表.md` |
| 14.3.4 | 获取基础模型信息 | 1675-1679 | 51496-51648 | 97 | `chapters/volcengine/ark/14.3.4 获取基础模型信息.md` |
| 14.4.1 | 批量开通基础模型 | 1680 | 51650-51676 | 13 | `chapters/volcengine/ark/14.4.1 批量开通基础模型.md` |
| 14.4.2 | 启用自动开通新模型 | 1681 | 51677-51701 | 12 | `chapters/volcengine/ark/14.4.2 启用自动开通新模型.md` |
| 14.4.3 | 关闭自动开通新模型 | 1682 | 51702-51726 | 12 | `chapters/volcengine/ark/14.4.3 关闭自动开通新模型.md` |
| 14.4.4 | 查询模型开通详情 | 1683-1689 | 51727-51916 | 152 | `chapters/volcengine/ark/14.4.4 查询模型开通详情.md` |
| 14.4.5 | 查询模型开通列表 | 1690-1697 | 51917-52143 | 186 | `chapters/volcengine/ark/14.4.5 查询模型开通列表.md` |
| 14.5.1 | 批量开通资源 | 1698-1699 | 52145-52178 | 16 | `chapters/volcengine/ark/14.5.1 批量开通资源.md` |
| 14.5.2 | 查询资源开通列表 | 1700-1704 | 52179-52320 | 112 | `chapters/volcengine/ark/14.5.2 查询资源开通列表.md` |
| 14.6.1 | 查询模型限流 | 1705-1709 | 52322-52450 | 99 | `chapters/volcengine/ark/14.6.1 查询模型限流.md` |
| 14.7.1 | 删除定制模型 | 1710-1711 | 52452-52491 | 19 | `chapters/volcengine/ark/14.7.1 删除定制模型.md` |
| 14.7.2 | 获取定制模型信息 | 1712-1717 | 52492-52627 | 102 | `chapters/volcengine/ark/14.7.2 获取定制模型信息.md` |
| 14.7.3 | 更新定制模型 | 1718-1719 | 52628-52675 | 25 | `chapters/volcengine/ark/14.7.3 更新定制模型.md` |
| 14.7.4 | 获取定制模型列表 | 1720-1725 | 52676-52826 | 106 | `chapters/volcengine/ark/14.7.4 获取定制模型列表.md` |
| 14.8.1 | 创建模型调优任务 | 1726-1739 | 52828-53180 | 287 | `chapters/volcengine/ark/14.8.1 创建模型调优任务.md` |
| 14.8.2 | 删除模型调优任务 | 1740 | 53181-53210 | 14 | `chapters/volcengine/ark/14.8.2 删除模型调优任务.md` |
| 14.8.3 | 获取模型调优任务信息 | 1741-1759 | 53211-53714 | 416 | `chapters/volcengine/ark/14.8.3 获取模型调优任务信息.md` |
| 14.8.4 | 查询精调效果指标详细数据 | 1760-1762 | 53715-53786 | 45 | `chapters/volcengine/ark/14.8.4 查询精调效果指标详细数据.md` |
| 14.8.5 | 查询精调效果指标 | 1763-1764 | 53787-53822 | 15 | `chapters/volcengine/ark/14.8.5 查询精调效果指标.md` |
| 14.8.6 | 获取模型调优任务列表 | 1765-1776 | 53823-54137 | 266 | `chapters/volcengine/ark/14.8.6 获取模型调优任务列表.md` |
| 14.8.7 | 重试模型调优任务 | 1777 | 54138-54167 | 13 | `chapters/volcengine/ark/14.8.7 重试模型调优任务.md` |
| 14.8.8 | 停止模型调优任务 | 1778 | 54168-54197 | 14 | `chapters/volcengine/ark/14.8.8 停止模型调优任务.md` |
| 14.8.9 | 更新模型调优任务 | 1779-1780 | 54198-54236 | 16 | `chapters/volcengine/ark/14.8.9 更新模型调优任务.md` |
| 14.9.1 | 开启推理接入点 | 1781-1782 | 54238-54271 | 15 | `chapters/volcengine/ark/14.9.1 开启推理接入点.md` |
| 14.9.2 | 停止推理接入点 | 1783-1784 | 54272-54305 | 13 | `chapters/volcengine/ark/14.9.2 停止推理接入点.md` |
| 14.9.3 | 获取推理接入点列表 | 1785-1792 | 54306-54551 | 177 | `chapters/volcengine/ark/14.9.3 获取推理接入点列表.md` |
| 14.9.4 | 获取推理接入点 | 1793-1797 | 54552-54678 | 91 | `chapters/volcengine/ark/14.9.4 获取推理接入点.md` |
| 14.9.5 | 删除推理接入点 | 1798-1799 | 54679-54711 | 14 | `chapters/volcengine/ark/14.9.5 删除推理接入点.md` |
| 14.9.6 | 更新推理接入点 | 1800-1807 | 54712-54915 | 162 | `chapters/volcengine/ark/14.9.6 更新推理接入点.md` |
| 14.9.7 | 创建推理接入点 | 1808-1817 | 54916-55165 | 196 | `chapters/volcengine/ark/14.9.7 创建推理接入点.md` |
| 14.9.8 | 获取接入点推理应用层加密证书 | 1818-1819 | 55166-55222 | 27 | `chapters/volcengine/ark/14.9.8 获取接入点推理应用层加密证书.md` |
| 14.9.9 | 创建推理接入点滚动升级任务 | 1820-1822 | 55223-55288 | 43 | `chapters/volcengine/ark/14.9.9 创建推理接入点滚动升级任务.md` |
| 14.9.10 | 查询推理接入点滚动升级详情 | 1823-1828 | 55289-55450 | 131 | `chapters/volcengine/ark/14.9.10 查询推理接入点滚动升级详情.md` |
| 14.9.11 | 回滚推理接入点滚动升级 | 1829-1830 | 55451-55483 | 15 | `chapters/volcengine/ark/14.9.11 回滚推理接入点滚动升级.md` |
| 14.9.12 | 取消推理接入点滚动升级 | 1831-1832 | 55484-55516 | 15 | `chapters/volcengine/ark/14.9.12 取消推理接入点滚动升级.md` |
| 14.10.1 | 创建评测任务 | 1833-1839 | 55518-55707 | 137 | `chapters/volcengine/ark/14.10.1 创建评测任务.md` |
| 14.10.2 | 删除评测任务 | 1840-1841 | 55708-55743 | 15 | `chapters/volcengine/ark/14.10.2 删除评测任务.md` |
| 14.10.3 | 获取评测任务 | 1842-1845 | 55744-55846 | 69 | `chapters/volcengine/ark/14.10.3 获取评测任务.md` |
| 14.10.4 | 获取评测任务结果 | 1846-1850 | 55847-55975 | 93 | `chapters/volcengine/ark/14.10.4 获取评测任务结果.md` |
| 14.10.5 | 获取评测任务列表 | 1851-1857 | 55976-56155 | 138 | `chapters/volcengine/ark/14.10.5 获取评测任务列表.md` |
| 14.10.6 | 获取评测任务结果列表 | 1858-1863 | 56156-56326 | 128 | `chapters/volcengine/ark/14.10.6 获取评测任务结果列表.md` |
| 14.10.7 | 停止评测任务 | 1864-1865 | 56327-56361 | 14 | `chapters/volcengine/ark/14.10.7 停止评测任务.md` |
| 14.10.8 | 更新评测任务 | 1866-1867 | 56362-56401 | 20 | `chapters/volcengine/ark/14.10.8 更新评测任务.md` |
| 14.11.1 | 查询推理用量 | 1868-1871 | 56403-56564 | 94 | `chapters/volcengine/ark/14.11.1 查询推理用量.md` |
| 14.11.2 | 查询单请求用量 | 1872-1877 | 56565-56736 | 136 | `chapters/volcengine/ark/14.11.2 查询单请求用量.md` |
| 14.11.3 | 查询异步任务用量 | 1878-1881 | 56737-56828 | 64 | `chapters/volcengine/ark/14.11.3 查询异步任务用量.md` |
| 14.11.4 | 创建用量明细导出任务 | 1882-1884 | 56829-56900 | 36 | `chapters/volcengine/ark/14.11.4 创建用量明细导出任务.md` |
| 14.11.5 | 查询用量明细导出任务状态 | 1885-1888 | 56901-57026 | 78 | `chapters/volcengine/ark/14.11.5 查询用量明细导出任务状态.md` |
| 14.11.6 | 查询模型推理限额 | 1889-1890 | 57027-57069 | 27 | `chapters/volcengine/ark/14.11.6 查询模型推理限额.md` |
| 14.11.7 | 开启模型推理限额 | 1891-1892 | 57070-57110 | 20 | `chapters/volcengine/ark/14.11.7 开启模型推理限额.md` |
| 14.11.8 | 关闭模型推理限额 | 1893-1894 | 57111-57147 | 16 | `chapters/volcengine/ark/14.11.8 关闭模型推理限额.md` |
| 14.12.1 | 创建方舟官方模型产物查询请求 | 1895-1896 | 57149-57183 | 19 | `chapters/volcengine/ark/14.12.1 创建方舟官方模型产物查询请求.md` |
| 14.12.2 | 获取安全审计日志 | 1897-1905 | 57184-57505 | 133 | `chapters/volcengine/ark/14.12.2 获取安全审计日志.md` |
| 14.12.3 | 获取方舟官方产物确认结果 | 1906-1907 | 57506-57552 | 27 | `chapters/volcengine/ark/14.12.3 获取方舟官方产物确认结果.md` |
| 14.13.1 | 上报视频生成模型效果问题 | 1908-1915 | 57554-57814 | 162 | `chapters/volcengine/ark/14.13.1 上报视频生成模型效果问题.md` |
| 14.13.2 | 查询视频生成模型效果问题结果 | 1916-1923 | 57815-58066 | 168 | `chapters/volcengine/ark/14.13.2 查询视频生成模型效果问题结果.md` |
| 14.13.3 | 上报大语言模型效果问题 | 1924-1928 | 58067-58230 | 89 | `chapters/volcengine/ark/14.13.3 上报大语言模型效果问题.md` |
| 14.13.4 | 查询大语言模型效果问题结果 | 1929-1934 | 58231-58397 | 105 | `chapters/volcengine/ark/14.13.4 查询大语言模型效果问题结果.md` |
| 14.13.5 | 上报 3D 生成效果问题 | 1935-1940 | 58398-58609 | 141 | `chapters/volcengine/ark/14.13.5 上报 3D 生成效果问题.md` |
| 14.13.6 | 查询 3D 生成效果问题结果 | 1941-1948 | 58610-58852 | 159 | `chapters/volcengine/ark/14.13.6 查询 3D 生成效果问题结果.md` |
| 15.1 | 兼容 OpenAI SDK | 1949-1952 | 58854-58970 | 103 | `chapters/volcengine/ark/15.1 兼容 OpenAI SDK.md` |
| 15.2 | 向后兼容性 | 1953 | 58971-59016 | 25 | `chapters/volcengine/ark/15.2 向后兼容性.md` |
| 15.3 | 错误码 - 第1部分 | 1953-1975 | 59017-61020 | 1954 | `chapters/volcengine/ark/15.3 错误码 - 第1部分.md` |
| 15.3 | 错误码 - 第2部分·错误码 | 1976-1985 | 61021-61786 | 732 | `chapters/volcengine/ark/15.3 错误码 - 第2部分·错误码.md` |
| 15.4 | SDK 常见使用示例 | 1986-2001 | 61787-62375 | 521 | `chapters/volcengine/ark/15.4 SDK 常见使用示例.md` |
