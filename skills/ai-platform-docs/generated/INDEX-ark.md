# 方舟 API 区章节表（ark）

来源：《火山方舟 API 参考》（2039 页）。219 个章节文件，接口级切分：一个接口/任务一个文件；超过 1500 行的按语义块自动再拆为`… - 第N部分`（5 个章节被拆分）。

「页码」是原 PDF 页码范围；「行范围」是中间 MD（`doc/<源文档>.md`）的 1 起始行号，可据此回查原文。章节文件本身已去掉页眉页脚，回查 PDF 时用这两列。文件名即章节标题，日常定位直接 Glob 文件名即可，用不到这两列。

**这张表用来 grep，不要整读。**

| 编号 | 标题 | 页码 | 行范围(源文件) | 行数 | 文件 |
|------|------|------|---------------|------|------|
| 1.1 | 获取 API Key 并配置 | 1 | 302-337 | 20 | `chapters/volcengine/ark/1.1 获取 API Key 并配置.md` |
| 1.2 | 安装及升级 SDK | 2-7 | 338-496 | 122 | `chapters/volcengine/ark/1.2 安装及升级 SDK.md` |
| 1.3 | Base URL及鉴权 | 8-10 | 497-592 | 68 | `chapters/volcengine/ark/1.3 Base URL及鉴权.md` |
| 2.1 | 对话(Chat) API | 11-72 | 594-2924 | 1253 | `chapters/volcengine/ark/2.1 对话(Chat) API.md` |
| 3.1 | 创建 Response - 第1部分 | 73-129 | 2925-4613 | 1410 | `chapters/volcengine/ark/3.1 创建 Response - 第1部分.md` |
| 3.1 | 创建 Response - 第2部分·响应参数 | 130-199 | 4614-6970 | 1348 | `chapters/volcengine/ark/3.1 创建 Response - 第2部分·响应参数.md` |
| 3.2 | 查询 Response 详情 | 200-246 | 6971-8304 | 1094 | `chapters/volcengine/ark/3.2 查询 Response 详情.md` |
| 3.3 | 查询 Response 输入项列表 | 247-294 | 8305-9887 | 947 | `chapters/volcengine/ark/3.3 查询 Response 输入项列表.md` |
| 3.4 | 删除 Response | 295-296 | 9888-9961 | 34 | `chapters/volcengine/ark/3.4 删除 Response.md` |
| 3.5.1 | Response 生命周期 - 第1部分 | 297-356 | 9962-11685 | 1505 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第1部分.md` |
| 3.5.1 | Response 生命周期 - 第2部分 | 357-415 | 11686-13382 | 1480 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第2部分.md` |
| 3.5.1 | Response 生命周期 - 第3部分 | 416-475 | 13383-15099 | 1502 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第3部分.md` |
| 3.5.1 | Response 生命周期 - 第4部分 | 476-545 | 15100-17109 | 1732 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第4部分.md` |
| 3.5.2 | Output Item 与文本回答 - 第1部分 | 546-603 | 17110-18761 | 1480 | `chapters/volcengine/ark/3.5.2 Output Item 与文本回答 - 第1部分.md` |
| 3.5.2 | Output Item 与文本回答 - 第2部分 | 604-627 | 18762-19391 | 582 | `chapters/volcengine/ark/3.5.2 Output Item 与文本回答 - 第2部分.md` |
| 3.5.3 | 工具调用事件 | 628-669 | 19392-20502 | 1024 | `chapters/volcengine/ark/3.5.3 工具调用事件.md` |
| 3.5.4 | 语音转写与错误事件 | 670-676 | 20503-20677 | 161 | `chapters/volcengine/ark/3.5.4 语音转写与错误事件.md` |
| 4.1 | 创建 Message | 677-704 | 20679-21459 | 579 | `chapters/volcengine/ark/4.1 创建 Message.md` |
| 4.2 | 统计 Messages 请求 token 数 | 705-717 | 21460-21813 | 282 | `chapters/volcengine/ark/4.2 统计 Messages 请求 token 数.md` |
| 5.1 | System One API（beta） | 718-729 | 21815-22142 | 244 | `chapters/volcengine/ark/5.1 System One API（beta）.md` |
| 6.1 | 上传文件 | 730-742 | 22144-22631 | 206 | `chapters/volcengine/ark/6.1 上传文件.md` |
| 6.2 | 查询文件详情 | 743-747 | 22632-22766 | 75 | `chapters/volcengine/ark/6.2 查询文件详情.md` |
| 6.3 | 查询文件列表 | 748-754 | 22767-22996 | 122 | `chapters/volcengine/ark/6.3 查询文件列表.md` |
| 6.4 | 删除文件 | 755-757 | 22997-23069 | 25 | `chapters/volcengine/ark/6.4 删除文件.md` |
| 6.5 | The file object | 758-761 | 23070-23153 | 60 | `chapters/volcengine/ark/6.5 The file object.md` |
| 7.1 | 创建视频生成任务 | 762-803 | 23155-25031 | 837 | `chapters/volcengine/ark/7.1 创建视频生成任务.md` |
| 7.2 | 查询视频生成任务 | 804-810 | 25032-25262 | 125 | `chapters/volcengine/ark/7.2 查询视频生成任务.md` |
| 7.3 | 查询视频生成任务列表 | 811-821 | 25263-25664 | 203 | `chapters/volcengine/ark/7.3 查询视频生成任务列表.md` |
| 7.4 | 取消或删除视频生成任务 | 822-823 | 25665-25753 | 56 | `chapters/volcengine/ark/7.4 取消或删除视频生成任务.md` |
| 8.1 | 图片生成 API | 824-864 | 25755-27478 | 738 | `chapters/volcengine/ark/8.1 图片生成 API.md` |
| 8.2 | 图片生成流式响应事件 | 865-870 | 27479-27657 | 158 | `chapters/volcengine/ark/8.2 图片生成流式响应事件.md` |
| 9.1.1 | 创建 3D 生成任务 API | 871-876 | 27660-27842 | 102 | `chapters/volcengine/ark/9.1.1 创建 3D 生成任务 API.md` |
| 9.1.2 | 查询 3D 生成任务 API | 877-880 | 27843-27977 | 63 | `chapters/volcengine/ark/9.1.2 查询 3D 生成任务 API.md` |
| 9.1.3 | 查询 3D 生成任务列表 | 881-887 | 27978-28203 | 105 | `chapters/volcengine/ark/9.1.3 查询 3D 生成任务列表.md` |
| 9.1.4 | 取消或删除 3D 生成任务 | 888-889 | 28204-28290 | 52 | `chapters/volcengine/ark/9.1.4 取消或删除 3D 生成任务.md` |
| 9.2.1 | 创建3D生成任务 | 890-896 | 28292-28536 | 152 | `chapters/volcengine/ark/9.2.1 创建3D生成任务.md` |
| 9.2.2 | 查询3D生成任务 | 897-899 | 28537-28616 | 52 | `chapters/volcengine/ark/9.2.2 查询3D生成任务.md` |
| 9.2.3 | 查询3D生成任务列表 | 900-903 | 28617-28742 | 85 | `chapters/volcengine/ark/9.2.3 查询3D生成任务列表.md` |
| 9.2.4 | 取消或删除3D生成任务 | 904-905 | 28743-28787 | 34 | `chapters/volcengine/ark/9.2.4 取消或删除3D生成任务.md` |
| 9.3.1 | 创建3D生成任务 | 906-910 | 28789-28933 | 98 | `chapters/volcengine/ark/9.3.1 创建3D生成任务.md` |
| 9.3.2 | 查询3D生成任务 | 911-913 | 28934-29013 | 51 | `chapters/volcengine/ark/9.3.2 查询3D生成任务.md` |
| 9.3.3 | 查询3D生成任务列表 | 914-917 | 29014-29139 | 86 | `chapters/volcengine/ark/9.3.3 查询3D生成任务列表.md` |
| 9.3.4 | 取消或删除3D生成任务 | 918-919 | 29140-29184 | 34 | `chapters/volcengine/ark/9.3.4 取消或删除3D生成任务.md` |
| 10.1 | 多模态向量化 API | 920-930 | 29186-29604 | 201 | `chapters/volcengine/ark/10.1 多模态向量化 API.md` |
| 11.1.1 | 创建智能体 | 931-949 | 29607-30195 | 406 | `chapters/volcengine/ark/11.1.1 创建智能体.md` |
| 11.1.2 | 查询智能体列表 | 950-960 | 30196-30531 | 238 | `chapters/volcengine/ark/11.1.2 查询智能体列表.md` |
| 11.1.3 | 查询智能体详情 | 961-970 | 30532-30820 | 201 | `chapters/volcengine/ark/11.1.3 查询智能体详情.md` |
| 11.1.4 | 更新智能体 | 971-989 | 30821-31459 | 427 | `chapters/volcengine/ark/11.1.4 更新智能体.md` |
| 11.1.5 | 查询智能体版本列表 | 990-1000 | 31460-31794 | 222 | `chapters/volcengine/ark/11.1.5 查询智能体版本列表.md` |
| 11.1.6 | 归档智能体 | 1001-1009 | 31795-32058 | 203 | `chapters/volcengine/ark/11.1.6 归档智能体.md` |
| 11.1.7 | 删除智能体 | 1010-1011 | 32059-32113 | 21 | `chapters/volcengine/ark/11.1.7 删除智能体.md` |
| 11.2.1 | 创建环境 | 1012-1020 | 32115-32393 | 186 | `chapters/volcengine/ark/11.2.1 创建环境.md` |
| 11.2.2 | 查询环境列表 | 1021-1026 | 32394-32561 | 116 | `chapters/volcengine/ark/11.2.2 查询环境列表.md` |
| 11.2.3 | 查询环境详情 | 1027-1031 | 32562-32708 | 89 | `chapters/volcengine/ark/11.2.3 查询环境详情.md` |
| 11.2.4 | 更新环境 | 1032-1040 | 32709-32992 | 181 | `chapters/volcengine/ark/11.2.4 更新环境.md` |
| 11.2.5 | 归档环境 | 1041-1044 | 32993-33101 | 84 | `chapters/volcengine/ark/11.2.5 归档环境.md` |
| 11.2.6 | 删除环境 | 1045-1046 | 33102-33159 | 25 | `chapters/volcengine/ark/11.2.6 删除环境.md` |
| 11.2.7.1 | 长轮询拉取待执行 Work | 1047-1051 | 33161-33308 | 77 | `chapters/volcengine/ark/11.2.7.1 长轮询拉取待执行 Work.md` |
| 11.2.7.2 | 认领 Work | 1052-1056 | 33309-33453 | 76 | `chapters/volcengine/ark/11.2.7.2 认领 Work.md` |
| 11.2.7.3 | 续租 Work | 1057-1060 | 33454-33567 | 53 | `chapters/volcengine/ark/11.2.7.3 续租 Work.md` |
| 11.2.7.4 | 查询 Work 队列状态 | 1061-1062 | 33568-33635 | 29 | `chapters/volcengine/ark/11.2.7.4 查询 Work 队列状态.md` |
| 11.2.7.5 | 停止 Work | 1063-1067 | 33636-33806 | 90 | `chapters/volcengine/ark/11.2.7.5 停止 Work.md` |
| 11.2.7.6 | 查询 Work 列表 | 1068-1072 | 33807-33966 | 92 | `chapters/volcengine/ark/11.2.7.6 查询 Work 列表.md` |
| 11.2.7.7 | 查询 Work 详情 | 1073-1076 | 33967-34089 | 64 | `chapters/volcengine/ark/11.2.7.7 查询 Work 详情.md` |
| 11.3.1 | 创建会话 | 1077-1115 | 34091-35300 | 905 | `chapters/volcengine/ark/11.3.1 创建会话.md` |
| 11.3.2 | 查询会话列表 | 1116-1141 | 35301-36072 | 602 | `chapters/volcengine/ark/11.3.2 查询会话列表.md` |
| 11.3.3 | 查询会话详情 | 1142-1167 | 36073-36843 | 590 | `chapters/volcengine/ark/11.3.3 查询会话详情.md` |
| 11.3.4 | 更新会话标题和标签 | 1168-1192 | 36844-37588 | 570 | `chapters/volcengine/ark/11.3.4 更新会话标题和标签.md` |
| 11.3.5 | 升级会话 | 1193-1225 | 37589-38560 | 781 | `chapters/volcengine/ark/11.3.5 升级会话.md` |
| 11.3.6 | 归档会话 | 1226-1248 | 38561-39208 | 539 | `chapters/volcengine/ark/11.3.6 归档会话.md` |
| 11.3.7 | 删除会话 | 1249-1250 | 39209-39268 | 27 | `chapters/volcengine/ark/11.3.7 删除会话.md` |
| 11.3.8.1 | 查询会话任务 | 1251-1256 | 39270-39455 | 99 | `chapters/volcengine/ark/11.3.8.1 查询会话任务.md` |
| 11.3.8.2 | 查询会话任务列表 | 1257-1261 | 39456-39626 | 98 | `chapters/volcengine/ark/11.3.8.2 查询会话任务列表.md` |
| 11.3.8.3 | 取消会话任务 | 1262-1264 | 39627-39720 | 36 | `chapters/volcengine/ark/11.3.8.3 取消会话任务.md` |
| 11.3.9.1 | 发送会话事件 | 1265-1268 | 39722-39838 | 53 | `chapters/volcengine/ark/11.3.9.1 发送会话事件.md` |
| 11.3.9.2 | 查询会话事件列表 | 1269-1272 | 39839-39972 | 62 | `chapters/volcengine/ark/11.3.9.2 查询会话事件列表.md` |
| 11.3.9.3 | 流式获取会话事件 | 1273-1277 | 39973-40146 | 50 | `chapters/volcengine/ark/11.3.9.3 流式获取会话事件.md` |
| 11.3.9.4 | 会话事件结构参考 - 第1部分 | 1278-1354 | 40147-42115 | 1748 | `chapters/volcengine/ark/11.3.9.4 会话事件结构参考 - 第1部分.md` |
| 11.3.10.1 | 添加会话资源 | 1355-1358 | 42117-42232 | 51 | `chapters/volcengine/ark/11.3.10.1 添加会话资源.md` |
| 11.3.10.2 | 查询会话资源列表 | 1359-1364 | 42233-42397 | 105 | `chapters/volcengine/ark/11.3.10.2 查询会话资源列表.md` |
| 11.3.10.3 | 查询会话资源 | 1365-1367 | 42398-42492 | 43 | `chapters/volcengine/ark/11.3.10.3 查询会话资源.md` |
| 11.3.11.1 | 查询线程列表 | 1368-1372 | 42494-42633 | 71 | `chapters/volcengine/ark/11.3.11.1 查询线程列表.md` |
| 11.3.11.2 | 查询线程详情 | 1373-1378 | 42634-42818 | 99 | `chapters/volcengine/ark/11.3.11.2 查询线程详情.md` |
| 11.3.11.3 | 查询线程事件列表 | 1379-1382 | 42819-42948 | 57 | `chapters/volcengine/ark/11.3.11.3 查询线程事件列表.md` |
| 11.3.11.4 | 流式获取线程事件 | 1383-1386 | 42949-43083 | 44 | `chapters/volcengine/ark/11.3.11.4 流式获取线程事件.md` |
| 11.4.1 | 创建 Webhook 接入点 | 1387-1390 | 43085-43204 | 64 | `chapters/volcengine/ark/11.4.1 创建 Webhook 接入点.md` |
| 11.4.2 | 查询 Webhook 接入点列表 | 1391-1394 | 43205-43318 | 68 | `chapters/volcengine/ark/11.4.2 查询 Webhook 接入点列表.md` |
| 11.4.3 | 查询 Webhook 接入点详情 | 1395-1397 | 43319-43413 | 53 | `chapters/volcengine/ark/11.4.3 查询 Webhook 接入点详情.md` |
| 11.4.4 | 更新 Webhook 接入点 | 1398-1401 | 43414-43531 | 63 | `chapters/volcengine/ark/11.4.4 更新 Webhook 接入点.md` |
| 11.4.5 | 启用 Webhook 接入点 | 1402-1404 | 43532-43628 | 55 | `chapters/volcengine/ark/11.4.5 启用 Webhook 接入点.md` |
| 11.4.6 | 删除 Webhook 接入点 | 1405 | 43629-43656 | 18 | `chapters/volcengine/ark/11.4.6 删除 Webhook 接入点.md` |
| 11.4.7 | 停用 Webhook 接入点 | 1406-1408 | 43657-43754 | 54 | `chapters/volcengine/ark/11.4.7 停用 Webhook 接入点.md` |
| 11.4.8 | 重置 Webhook 签名密钥 | 1409-1410 | 43755-43789 | 19 | `chapters/volcengine/ark/11.4.8 重置 Webhook 签名密钥.md` |
| 11.4.9 | 发送 Webhook 测试事件 | 1411-1412 | 43790-43834 | 29 | `chapters/volcengine/ark/11.4.9 发送 Webhook 测试事件.md` |
| 11.4.10 | 查询 Webhook 事件详情 | 1413-1414 | 43835-43886 | 35 | `chapters/volcengine/ark/11.4.10 查询 Webhook 事件详情.md` |
| 11.4.11 | 查询 Webhook 事件列表 | 1415-1417 | 43887-43966 | 52 | `chapters/volcengine/ark/11.4.11 查询 Webhook 事件列表.md` |
| 11.4.12 | Webhook 事件结构参考 | 1418-1439 | 43967-44550 | 519 | `chapters/volcengine/ark/11.4.12 Webhook 事件结构参考.md` |
| 11.5.1 | 创建保管库 | 1440-1442 | 44552-44652 | 45 | `chapters/volcengine/ark/11.5.1 创建保管库.md` |
| 11.5.2 | 查询保管库列表 | 1443-1446 | 44653-44772 | 60 | `chapters/volcengine/ark/11.5.2 查询保管库列表.md` |
| 11.5.3 | 查询保管库详情 | 1447-1449 | 44773-44844 | 33 | `chapters/volcengine/ark/11.5.3 查询保管库详情.md` |
| 11.5.4 | 更新保管库 | 1450-1452 | 44845-44948 | 47 | `chapters/volcengine/ark/11.5.4 更新保管库.md` |
| 11.5.5 | 删除保管库 | 1453-1454 | 44949-45005 | 25 | `chapters/volcengine/ark/11.5.5 删除保管库.md` |
| 11.5.6.1 | 创建凭证 | 1455-1470 | 45007-45554 | 376 | `chapters/volcengine/ark/11.5.6.1 创建凭证.md` |
| 11.5.6.2 | 查询凭证列表 | 1471-1479 | 45555-45836 | 188 | `chapters/volcengine/ark/11.5.6.2 查询凭证列表.md` |
| 11.5.6.3 | 查询凭证详情 | 1480-1487 | 45837-46083 | 163 | `chapters/volcengine/ark/11.5.6.3 查询凭证详情.md` |
| 11.5.6.4 | 更新凭证 | 1488-1503 | 46084-46606 | 357 | `chapters/volcengine/ark/11.5.6.4 更新凭证.md` |
| 11.5.6.5 | 删除凭证 | 1504-1505 | 46607-46666 | 30 | `chapters/volcengine/ark/11.5.6.5 删除凭证.md` |
| 11.6.1 | 创建记忆库 | 1506-1510 | 46668-46812 | 72 | `chapters/volcengine/ark/11.6.1 创建记忆库.md` |
| 11.6.2 | 查询记忆库列表 | 1511-1515 | 46813-46971 | 90 | `chapters/volcengine/ark/11.6.2 查询记忆库列表.md` |
| 11.6.3 | 查询记忆库详情 | 1516-1519 | 46972-47089 | 54 | `chapters/volcengine/ark/11.6.3 查询记忆库详情.md` |
| 11.6.4 | 更新记忆库 | 1520-1525 | 47090-47246 | 71 | `chapters/volcengine/ark/11.6.4 更新记忆库.md` |
| 11.6.5 | 删除记忆库 | 1526-1527 | 47247-47307 | 21 | `chapters/volcengine/ark/11.6.5 删除记忆库.md` |
| 11.6.6.1 | 创建记忆 | 1528-1532 | 47309-47444 | 71 | `chapters/volcengine/ark/11.6.6.1 创建记忆.md` |
| 11.6.6.2 | 批量创建记忆 | 1533-1539 | 47445-47688 | 121 | `chapters/volcengine/ark/11.6.6.2 批量创建记忆.md` |
| 11.6.6.3 | 查询记忆列表 | 1540-1544 | 47689-47852 | 87 | `chapters/volcengine/ark/11.6.6.3 查询记忆列表.md` |
| 11.6.6.4 | 查询记忆详情 | 1545-1548 | 47853-47973 | 61 | `chapters/volcengine/ark/11.6.6.4 查询记忆详情.md` |
| 11.6.6.5 | 更新记忆 | 1549-1553 | 47974-48115 | 66 | `chapters/volcengine/ark/11.6.6.5 更新记忆.md` |
| 11.6.6.6 | 删除记忆 | 1554-1555 | 48116-48179 | 25 | `chapters/volcengine/ark/11.6.6.6 删除记忆.md` |
| 11.7.1 | 创建 Dream | 1556-1561 | 48181-48359 | 117 | `chapters/volcengine/ark/11.7.1 创建 Dream.md` |
| 11.7.2 | 查询 Dream 列表 | 1562-1568 | 48360-48586 | 142 | `chapters/volcengine/ark/11.7.2 查询 Dream 列表.md` |
| 11.7.3 | 查询 Dream | 1569-1573 | 48587-48748 | 90 | `chapters/volcengine/ark/11.7.3 查询 Dream.md` |
| 11.7.4 | 取消 Dream | 1574-1579 | 48749-48915 | 93 | `chapters/volcengine/ark/11.7.4 取消 Dream.md` |
| 11.8.1 | 创建技能 | 1580-1583 | 48917-49040 | 61 | `chapters/volcengine/ark/11.8.1 创建技能.md` |
| 11.8.2 | 查询技能列表 | 1584-1587 | 49041-49161 | 68 | `chapters/volcengine/ark/11.8.2 查询技能列表.md` |
| 11.8.3 | 查询技能详情 | 1588-1590 | 49162-49253 | 43 | `chapters/volcengine/ark/11.8.3 查询技能详情.md` |
| 11.8.4 | 设置技能内容保护 | 1591-1593 | 49254-49324 | 43 | `chapters/volcengine/ark/11.8.4 设置技能内容保护.md` |
| 11.8.5 | 删除技能 | 1594-1595 | 49325-49383 | 24 | `chapters/volcengine/ark/11.8.5 删除技能.md` |
| 11.8.6 | 创建新版本的技能 | 1596-1598 | 49384-49485 | 49 | `chapters/volcengine/ark/11.8.6 创建新版本的技能.md` |
| 11.8.7 | 查询技能的版本列表 | 1599-1601 | 49486-49583 | 54 | `chapters/volcengine/ark/11.8.7 查询技能的版本列表.md` |
| 11.8.8 | 查询指定版本的技能 | 1602-1604 | 49584-49655 | 32 | `chapters/volcengine/ark/11.8.8 查询指定版本的技能.md` |
| 11.8.9 | 删除指定版本的技能 | 1605-1606 | 49656-49710 | 22 | `chapters/volcengine/ark/11.8.9 删除指定版本的技能.md` |
| 11.8.10 | 下载指定版本的技能 | 1607-1608 | 49711-49779 | 26 | `chapters/volcengine/ark/11.8.10 下载指定版本的技能.md` |
| 11.8.11 | 扫描 GitHub 技能 | 1609-1611 | 49780-49856 | 48 | `chapters/volcengine/ark/11.8.11 扫描 GitHub 技能.md` |
| 11.8.12 | 导入 GitHub 技能 | 1612-1614 | 49857-49959 | 63 | `chapters/volcengine/ark/11.8.12 导入 GitHub 技能.md` |
| 12.1.1 | 创建批量推理任务 | 1615-1618 | 49962-50042 | 60 | `chapters/volcengine/ark/12.1.1 创建批量推理任务.md` |
| 12.1.2 | 获取批量推理任务列表 | 1619-1626 | 50043-50255 | 165 | `chapters/volcengine/ark/12.1.2 获取批量推理任务列表.md` |
| 12.1.3 | 获取批量推理任务 | 1627-1632 | 50256-50405 | 107 | `chapters/volcengine/ark/12.1.3 获取批量推理任务.md` |
| 12.1.4 | 更新批量推理任务 | 1633-1634 | 50406-50443 | 18 | `chapters/volcengine/ark/12.1.4 更新批量推理任务.md` |
| 12.1.5 | 删除批量推理任务 | 1635-1636 | 50444-50476 | 14 | `chapters/volcengine/ark/12.1.5 删除批量推理任务.md` |
| 12.1.6 | 停止批量推理任务 | 1637-1638 | 50477-50512 | 17 | `chapters/volcengine/ark/12.1.6 停止批量推理任务.md` |
| 12.1.7 | 重启批量推理任务 | 1639-1640 | 50513-50549 | 18 | `chapters/volcengine/ark/12.1.7 重启批量推理任务.md` |
| 12.2 | 批量(Chat) API | 1641-1661 | 50550-51110 | 365 | `chapters/volcengine/ark/12.2 批量(Chat) API.md` |
| 13.1 | 分词 API | 1662-1666 | 51112-51270 | 61 | `chapters/volcengine/ark/13.1 分词 API.md` |
| 14.1.1 | 获取临时 API Key | 1667-1668 | 51273-51322 | 29 | `chapters/volcengine/ark/14.1.1 获取临时 API Key.md` |
| 14.2.1 | 创建个人版套餐 | 1669-1670 | 51324-51385 | 35 | `chapters/volcengine/ark/14.2.1 创建个人版套餐.md` |
| 14.2.2 | 续费个人版套餐 | 1671-1672 | 51386-51434 | 27 | `chapters/volcengine/ark/14.2.2 续费个人版套餐.md` |
| 14.2.3 | 查询个人版套餐 | 1673-1674 | 51435-51477 | 24 | `chapters/volcengine/ark/14.2.3 查询个人版套餐.md` |
| 14.2.4.1 | 查询 Agent Plan 支持的模型列表 | 1675-1676 | 51479-51513 | 16 | `chapters/volcengine/ark/14.2.4.1 查询 Agent Plan 支持的模型列表.md` |
| 14.2.4.2 | 轮换个人版 API Key | 1677-1678 | 51514-51556 | 22 | `chapters/volcengine/ark/14.2.4.2 轮换个人版 API Key.md` |
| 14.2.4.3 | 获取套餐 AFP 额度 | 1679-1682 | 51557-51653 | 69 | `chapters/volcengine/ark/14.2.4.3 获取套餐 AFP 额度.md` |
| 14.2.4.4 | 获取套餐用量详情 | 1683-1685 | 51654-51728 | 43 | `chapters/volcengine/ark/14.2.4.4 获取套餐用量详情.md` |
| 14.2.5.1 | 查询 Coding Plan 支持的模型列表 | 1686 | 51730-51756 | 15 | `chapters/volcengine/ark/14.2.5.1 查询 Coding Plan 支持的模型列表.md` |
| 14.3.1 | 获取基础模型版本列表 | 1687-1690 | 51758-51869 | 77 | `chapters/volcengine/ark/14.3.1 获取基础模型版本列表.md` |
| 14.3.2 | 获取基础模型版本信息 | 1691-1704 | 51870-52252 | 289 | `chapters/volcengine/ark/14.3.2 获取基础模型版本信息.md` |
| 14.3.3 | 获取基础模型列表 | 1705-1712 | 52253-52546 | 195 | `chapters/volcengine/ark/14.3.3 获取基础模型列表.md` |
| 14.3.4 | 获取基础模型信息 | 1713-1717 | 52547-52699 | 97 | `chapters/volcengine/ark/14.3.4 获取基础模型信息.md` |
| 14.4.1 | 批量开通基础模型 | 1718 | 52701-52727 | 13 | `chapters/volcengine/ark/14.4.1 批量开通基础模型.md` |
| 14.4.2 | 启用自动开通新模型 | 1719 | 52728-52752 | 12 | `chapters/volcengine/ark/14.4.2 启用自动开通新模型.md` |
| 14.4.3 | 关闭自动开通新模型 | 1720 | 52753-52777 | 12 | `chapters/volcengine/ark/14.4.3 关闭自动开通新模型.md` |
| 14.4.4 | 查询模型开通详情 | 1721-1727 | 52778-52967 | 152 | `chapters/volcengine/ark/14.4.4 查询模型开通详情.md` |
| 14.4.5 | 查询模型开通列表 | 1728-1735 | 52968-53194 | 186 | `chapters/volcengine/ark/14.4.5 查询模型开通列表.md` |
| 14.5.1 | 批量开通资源 | 1736-1737 | 53196-53229 | 16 | `chapters/volcengine/ark/14.5.1 批量开通资源.md` |
| 14.5.2 | 查询资源开通列表 | 1738-1742 | 53230-53371 | 112 | `chapters/volcengine/ark/14.5.2 查询资源开通列表.md` |
| 14.6.1 | 查询模型限流 | 1743-1747 | 53373-53501 | 99 | `chapters/volcengine/ark/14.6.1 查询模型限流.md` |
| 14.7.1 | 删除定制模型 | 1748-1749 | 53503-53542 | 19 | `chapters/volcengine/ark/14.7.1 删除定制模型.md` |
| 14.7.2 | 获取定制模型信息 | 1750-1755 | 53543-53678 | 102 | `chapters/volcengine/ark/14.7.2 获取定制模型信息.md` |
| 14.7.3 | 更新定制模型 | 1756-1757 | 53679-53726 | 25 | `chapters/volcengine/ark/14.7.3 更新定制模型.md` |
| 14.7.4 | 获取定制模型列表 | 1758-1763 | 53727-53877 | 106 | `chapters/volcengine/ark/14.7.4 获取定制模型列表.md` |
| 14.8.1 | 创建模型调优任务 | 1764-1777 | 53879-54231 | 287 | `chapters/volcengine/ark/14.8.1 创建模型调优任务.md` |
| 14.8.2 | 删除模型调优任务 | 1778 | 54232-54261 | 14 | `chapters/volcengine/ark/14.8.2 删除模型调优任务.md` |
| 14.8.3 | 获取模型调优任务信息 | 1779-1797 | 54262-54765 | 416 | `chapters/volcengine/ark/14.8.3 获取模型调优任务信息.md` |
| 14.8.4 | 查询精调效果指标详细数据 | 1798-1800 | 54766-54837 | 45 | `chapters/volcengine/ark/14.8.4 查询精调效果指标详细数据.md` |
| 14.8.5 | 查询精调效果指标 | 1801-1802 | 54838-54873 | 15 | `chapters/volcengine/ark/14.8.5 查询精调效果指标.md` |
| 14.8.6 | 获取模型调优任务列表 | 1803-1814 | 54874-55188 | 266 | `chapters/volcengine/ark/14.8.6 获取模型调优任务列表.md` |
| 14.8.7 | 重试模型调优任务 | 1815 | 55189-55218 | 13 | `chapters/volcengine/ark/14.8.7 重试模型调优任务.md` |
| 14.8.8 | 停止模型调优任务 | 1816 | 55219-55248 | 14 | `chapters/volcengine/ark/14.8.8 停止模型调优任务.md` |
| 14.8.9 | 更新模型调优任务 | 1817-1818 | 55249-55287 | 16 | `chapters/volcengine/ark/14.8.9 更新模型调优任务.md` |
| 14.9.1 | 开启推理接入点 | 1819-1820 | 55289-55322 | 15 | `chapters/volcengine/ark/14.9.1 开启推理接入点.md` |
| 14.9.2 | 停止推理接入点 | 1821-1822 | 55323-55356 | 13 | `chapters/volcengine/ark/14.9.2 停止推理接入点.md` |
| 14.9.3 | 获取推理接入点列表 | 1823-1830 | 55357-55602 | 177 | `chapters/volcengine/ark/14.9.3 获取推理接入点列表.md` |
| 14.9.4 | 获取推理接入点 | 1831-1835 | 55603-55729 | 91 | `chapters/volcengine/ark/14.9.4 获取推理接入点.md` |
| 14.9.5 | 删除推理接入点 | 1836-1837 | 55730-55762 | 14 | `chapters/volcengine/ark/14.9.5 删除推理接入点.md` |
| 14.9.6 | 更新推理接入点 | 1838-1845 | 55763-55966 | 162 | `chapters/volcengine/ark/14.9.6 更新推理接入点.md` |
| 14.9.7 | 创建推理接入点 | 1846-1855 | 55967-56216 | 196 | `chapters/volcengine/ark/14.9.7 创建推理接入点.md` |
| 14.9.8 | 获取接入点推理应用层加密证书 | 1856-1857 | 56217-56273 | 27 | `chapters/volcengine/ark/14.9.8 获取接入点推理应用层加密证书.md` |
| 14.9.9 | 创建推理接入点滚动升级任务 | 1858-1860 | 56274-56339 | 43 | `chapters/volcengine/ark/14.9.9 创建推理接入点滚动升级任务.md` |
| 14.9.10 | 查询推理接入点滚动升级详情 | 1861-1866 | 56340-56501 | 131 | `chapters/volcengine/ark/14.9.10 查询推理接入点滚动升级详情.md` |
| 14.9.11 | 回滚推理接入点滚动升级 | 1867-1868 | 56502-56534 | 15 | `chapters/volcengine/ark/14.9.11 回滚推理接入点滚动升级.md` |
| 14.9.12 | 取消推理接入点滚动升级 | 1869-1870 | 56535-56567 | 15 | `chapters/volcengine/ark/14.9.12 取消推理接入点滚动升级.md` |
| 14.10.1 | 创建评测任务 | 1871-1877 | 56569-56758 | 137 | `chapters/volcengine/ark/14.10.1 创建评测任务.md` |
| 14.10.2 | 删除评测任务 | 1878-1879 | 56759-56794 | 15 | `chapters/volcengine/ark/14.10.2 删除评测任务.md` |
| 14.10.3 | 获取评测任务 | 1880-1883 | 56795-56897 | 69 | `chapters/volcengine/ark/14.10.3 获取评测任务.md` |
| 14.10.4 | 获取评测任务结果 | 1884-1888 | 56898-57026 | 93 | `chapters/volcengine/ark/14.10.4 获取评测任务结果.md` |
| 14.10.5 | 获取评测任务列表 | 1889-1895 | 57027-57206 | 138 | `chapters/volcengine/ark/14.10.5 获取评测任务列表.md` |
| 14.10.6 | 获取评测任务结果列表 | 1896-1901 | 57207-57377 | 128 | `chapters/volcengine/ark/14.10.6 获取评测任务结果列表.md` |
| 14.10.7 | 停止评测任务 | 1902-1903 | 57378-57412 | 14 | `chapters/volcengine/ark/14.10.7 停止评测任务.md` |
| 14.10.8 | 更新评测任务 | 1904-1905 | 57413-57452 | 20 | `chapters/volcengine/ark/14.10.8 更新评测任务.md` |
| 14.11.1 | 查询推理用量 | 1906-1909 | 57454-57615 | 94 | `chapters/volcengine/ark/14.11.1 查询推理用量.md` |
| 14.11.2 | 查询单请求用量 | 1910-1915 | 57616-57787 | 136 | `chapters/volcengine/ark/14.11.2 查询单请求用量.md` |
| 14.11.3 | 查询异步任务用量 | 1916-1919 | 57788-57879 | 64 | `chapters/volcengine/ark/14.11.3 查询异步任务用量.md` |
| 14.11.4 | 创建用量明细导出任务 | 1920-1922 | 57880-57951 | 36 | `chapters/volcengine/ark/14.11.4 创建用量明细导出任务.md` |
| 14.11.5 | 查询用量明细导出任务状态 | 1923-1926 | 57952-58077 | 78 | `chapters/volcengine/ark/14.11.5 查询用量明细导出任务状态.md` |
| 14.11.6 | 查询模型推理限额 | 1927-1928 | 58078-58120 | 27 | `chapters/volcengine/ark/14.11.6 查询模型推理限额.md` |
| 14.11.7 | 开启模型推理限额 | 1929-1930 | 58121-58161 | 20 | `chapters/volcengine/ark/14.11.7 开启模型推理限额.md` |
| 14.11.8 | 关闭模型推理限额 | 1931-1932 | 58162-58198 | 16 | `chapters/volcengine/ark/14.11.8 关闭模型推理限额.md` |
| 14.12.1 | 创建方舟官方模型产物查询请求 | 1933-1934 | 58200-58234 | 19 | `chapters/volcengine/ark/14.12.1 创建方舟官方模型产物查询请求.md` |
| 14.12.2 | 获取安全审计日志 | 1935-1943 | 58235-58556 | 133 | `chapters/volcengine/ark/14.12.2 获取安全审计日志.md` |
| 14.12.3 | 获取方舟官方产物确认结果 | 1944-1945 | 58557-58603 | 27 | `chapters/volcengine/ark/14.12.3 获取方舟官方产物确认结果.md` |
| 14.13.1 | 上报视频生成模型效果问题 | 1946-1953 | 58605-58865 | 162 | `chapters/volcengine/ark/14.13.1 上报视频生成模型效果问题.md` |
| 14.13.2 | 查询视频生成模型效果问题结果 | 1954-1961 | 58866-59117 | 168 | `chapters/volcengine/ark/14.13.2 查询视频生成模型效果问题结果.md` |
| 14.13.3 | 上报大语言模型效果问题 | 1962-1966 | 59118-59281 | 89 | `chapters/volcengine/ark/14.13.3 上报大语言模型效果问题.md` |
| 14.13.4 | 查询大语言模型效果问题结果 | 1967-1972 | 59282-59448 | 105 | `chapters/volcengine/ark/14.13.4 查询大语言模型效果问题结果.md` |
| 14.13.5 | 上报 3D 生成效果问题 | 1973-1978 | 59449-59660 | 141 | `chapters/volcengine/ark/14.13.5 上报 3D 生成效果问题.md` |
| 14.13.6 | 查询 3D 生成效果问题结果 | 1979-1986 | 59661-59903 | 159 | `chapters/volcengine/ark/14.13.6 查询 3D 生成效果问题结果.md` |
| 15.1 | 兼容 OpenAI SDK | 1987-1990 | 59905-60021 | 103 | `chapters/volcengine/ark/15.1 兼容 OpenAI SDK.md` |
| 15.2 | 向后兼容性 | 1991 | 60022-60067 | 25 | `chapters/volcengine/ark/15.2 向后兼容性.md` |
| 15.3 | 错误码 - 第1部分 | 1991-2013 | 60068-62071 | 1954 | `chapters/volcengine/ark/15.3 错误码 - 第1部分.md` |
| 15.3 | 错误码 - 第2部分·错误码 | 2014-2023 | 62072-62837 | 732 | `chapters/volcengine/ark/15.3 错误码 - 第2部分·错误码.md` |
| 15.4 | SDK 常见使用示例 | 2024-2039 | 62838-63426 | 521 | `chapters/volcengine/ark/15.4 SDK 常见使用示例.md` |
