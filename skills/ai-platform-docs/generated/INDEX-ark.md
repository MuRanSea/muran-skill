# 方舟 API 区章节表（ark）

来源：《火山方舟 API 参考》（1410 页）。202 个章节文件，接口级切分：一个接口/任务一个文件；超过 1500 行的按语义块自动再拆为`… - 第N部分`（5 个章节被拆分）。

「页码」是原 PDF 页码范围；「行范围」是中间 MD（`doc/<源文档>.md`）的 1 起始行号，可据此回查原文。章节文件本身已去掉页眉页脚，回查 PDF 时用这两列。文件名即章节标题，日常定位直接 Glob 文件名即可，用不到这两列。

**这张表用来 grep，不要整读。**

| 编号 | 标题 | 页码 | 行范围(源文件) | 行数 | 文件 |
|------|------|------|---------------|------|------|
| 1.1 | 获取 API Key 并配置 | 1 | 282-316 | 19 | `chapters/volcengine/ark/1.1 获取 API Key 并配置.md` |
| 1.2 | 安装及升级 SDK | 2-7 | 317-472 | 115 | `chapters/volcengine/ark/1.2 安装及升级 SDK.md` |
| 1.3 | Base URL及鉴权 | 8-10 | 473-568 | 68 | `chapters/volcengine/ark/1.3 Base URL及鉴权.md` |
| 2.1 | 对话(Chat) API | 11-42 | 570-1771 | 888 | `chapters/volcengine/ark/2.1 对话(Chat) API.md` |
| 3.1 | 创建 Response - 第1部分 | 43-91 | 1772-3436 | 1410 | `chapters/volcengine/ark/3.1 创建 Response - 第1部分.md` |
| 3.1 | 创建 Response - 第2部分·响应参数 | 92-134 | 3437-4820 | 1210 | `chapters/volcengine/ark/3.1 创建 Response - 第2部分·响应参数.md` |
| 3.2 | 查询 Response 详情 | 135-171 | 4821-5974 | 1062 | `chapters/volcengine/ark/3.2 查询 Response 详情.md` |
| 3.3 | 查询 Response 输入项列表 | 172-200 | 5975-6887 | 831 | `chapters/volcengine/ark/3.3 查询 Response 输入项列表.md` |
| 3.4 | 删除 Response | 201 | 6888-6911 | 19 | `chapters/volcengine/ark/3.4 删除 Response.md` |
| 3.5.1 | Response 生命周期 - 第1部分 | 202-253 | 6912-8610 | 1494 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第1部分.md` |
| 3.5.1 | Response 生命周期 - 第2部分 | 254-305 | 8611-10311 | 1495 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第2部分.md` |
| 3.5.1 | Response 生命周期 - 第3部分 | 306-357 | 10312-12002 | 1489 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第3部分.md` |
| 3.5.1 | Response 生命周期 - 第4部分 | 358-418 | 12003-13990 | 1726 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第4部分.md` |
| 3.5.2 | Output Item 与文本回答 - 第1部分 | 419-469 | 13991-15621 | 1470 | `chapters/volcengine/ark/3.5.2 Output Item 与文本回答 - 第1部分.md` |
| 3.5.2 | Output Item 与文本回答 - 第2部分 | 470-490 | 15622-16249 | 586 | `chapters/volcengine/ark/3.5.2 Output Item 与文本回答 - 第2部分.md` |
| 3.5.3 | 工具调用事件 | 491-527 | 16250-17350 | 1024 | `chapters/volcengine/ark/3.5.3 工具调用事件.md` |
| 3.5.4 | 语音转写与错误事件 | 528-533 | 17351-17523 | 161 | `chapters/volcengine/ark/3.5.4 语音转写与错误事件.md` |
| 4.1 | 创建 Message | 534-553 | 17525-18181 | 569 | `chapters/volcengine/ark/4.1 创建 Message.md` |
| 4.2 | 统计 Messages 请求 token 数 | 554-563 | 18182-18518 | 278 | `chapters/volcengine/ark/4.2 统计 Messages 请求 token 数.md` |
| 5.1 | System One API（beta） | 564-572 | 18520-18794 | 240 | `chapters/volcengine/ark/5.1 System One API（beta）.md` |
| 6.1 | 上传文件 | 573-578 | 18796-19007 | 157 | `chapters/volcengine/ark/6.1 上传文件.md` |
| 6.2 | 查询文件详情 | 579-581 | 19008-19081 | 63 | `chapters/volcengine/ark/6.2 查询文件详情.md` |
| 6.3 | 查询文件列表 | 582-585 | 19082-19216 | 112 | `chapters/volcengine/ark/6.3 查询文件列表.md` |
| 6.4 | 删除文件 | 586 | 19217-19239 | 19 | `chapters/volcengine/ark/6.4 删除文件.md` |
| 6.5 | The file object | 587-589 | 19240-19311 | 57 | `chapters/volcengine/ark/6.5 The file object.md` |
| 7.1 | 创建视频生成任务 | 590-607 | 19313-20177 | 600 | `chapters/volcengine/ark/7.1 创建视频生成任务.md` |
| 7.2 | 查询视频生成任务 | 608-612 | 20178-20332 | 112 | `chapters/volcengine/ark/7.2 查询视频生成任务.md` |
| 7.3 | 查询视频生成任务列表 | 613-618 | 20333-20552 | 164 | `chapters/volcengine/ark/7.3 查询视频生成任务列表.md` |
| 7.4 | 取消或删除视频生成任务 | 619 | 20553-20594 | 38 | `chapters/volcengine/ark/7.4 取消或删除视频生成任务.md` |
| 8.1 | 图片生成 API | 620-637 | 20596-21343 | 520 | `chapters/volcengine/ark/8.1 图片生成 API.md` |
| 8.2 | 图片生成流式响应事件 | 638-643 | 21344-21522 | 156 | `chapters/volcengine/ark/8.2 图片生成流式响应事件.md` |
| 9.1.1 | 创建 3D 生成任务 API | 644-646 | 21525-21629 | 79 | `chapters/volcengine/ark/9.1.1 创建 3D 生成任务 API.md` |
| 9.1.2 | 查询 3D 生成任务 API | 647-648 | 21630-21699 | 52 | `chapters/volcengine/ark/9.1.2 查询 3D 生成任务 API.md` |
| 9.1.3 | 查询 3D 生成任务列表 | 649-652 | 21700-21815 | 87 | `chapters/volcengine/ark/9.1.3 查询 3D 生成任务列表.md` |
| 9.1.4 | 取消或删除 3D 生成任务 | 653 | 21816-21857 | 38 | `chapters/volcengine/ark/9.1.4 取消或删除 3D 生成任务.md` |
| 9.2.1 | 创建3D生成任务 | 654-658 | 21859-22073 | 148 | `chapters/volcengine/ark/9.2.1 创建3D生成任务.md` |
| 9.2.2 | 查询3D生成任务 | 659-660 | 22074-22139 | 48 | `chapters/volcengine/ark/9.2.2 查询3D生成任务.md` |
| 9.2.3 | 查询3D生成任务列表 | 661-663 | 22140-22247 | 81 | `chapters/volcengine/ark/9.2.3 查询3D生成任务列表.md` |
| 9.2.4 | 取消或删除3D生成任务 | 664 | 22248-22282 | 31 | `chapters/volcengine/ark/9.2.4 取消或删除3D生成任务.md` |
| 9.3.1 | 创建3D生成任务 | 665-668 | 22284-22415 | 95 | `chapters/volcengine/ark/9.3.1 创建3D生成任务.md` |
| 9.3.2 | 查询3D生成任务 | 669-670 | 22416-22481 | 48 | `chapters/volcengine/ark/9.3.2 查询3D生成任务.md` |
| 9.3.3 | 查询3D生成任务列表 | 671-673 | 22482-22589 | 81 | `chapters/volcengine/ark/9.3.3 查询3D生成任务列表.md` |
| 9.3.4 | 取消或删除3D生成任务 | 674 | 22590-22624 | 31 | `chapters/volcengine/ark/9.3.4 取消或删除3D生成任务.md` |
| 10.1 | 多模态向量化 API | 675-680 | 22626-22825 | 145 | `chapters/volcengine/ark/10.1 多模态向量化 API.md` |
| 11.1.1 | 创建智能体 | 681-694 | 22828-23319 | 371 | `chapters/volcengine/ark/11.1.1 创建智能体.md` |
| 11.1.2 | 查询智能体列表 | 695-702 | 23320-23580 | 215 | `chapters/volcengine/ark/11.1.2 查询智能体列表.md` |
| 11.1.3 | 查询智能体详情 | 703-709 | 23581-23804 | 180 | `chapters/volcengine/ark/11.1.3 查询智能体详情.md` |
| 11.1.4 | 更新智能体 | 710-724 | 23805-24344 | 389 | `chapters/volcengine/ark/11.1.4 更新智能体.md` |
| 11.1.5 | 删除智能体 | 725 | 24345-24365 | 14 | `chapters/volcengine/ark/11.1.5 删除智能体.md` |
| 11.1.6 | 查询智能体版本列表 | 726-733 | 24366-24615 | 202 | `chapters/volcengine/ark/11.1.6 查询智能体版本列表.md` |
| 11.2.1 | 创建环境 | 734-739 | 24617-24806 | 154 | `chapters/volcengine/ark/11.2.1 创建环境.md` |
| 11.2.2 | 查询环境列表 | 740-743 | 24807-24916 | 99 | `chapters/volcengine/ark/11.2.2 查询环境列表.md` |
| 11.2.3 | 查询环境详情 | 744-746 | 24917-25007 | 80 | `chapters/volcengine/ark/11.2.3 查询环境详情.md` |
| 11.2.4 | 更新环境 | 747-752 | 25008-25215 | 164 | `chapters/volcengine/ark/11.2.4 更新环境.md` |
| 11.2.5 | 删除环境 | 753 | 25216-25238 | 17 | `chapters/volcengine/ark/11.2.5 删除环境.md` |
| 11.2.6.1 | 长轮询拉取待执行 Work | 754-756 | 25240-25330 | 68 | `chapters/volcengine/ark/11.2.6.1 长轮询拉取待执行 Work.md` |
| 11.2.6.2 | 认领 Work | 757-759 | 25331-25403 | 56 | `chapters/volcengine/ark/11.2.6.2 认领 Work.md` |
| 11.2.6.3 | 续租 Work | 760-761 | 25404-25459 | 41 | `chapters/volcengine/ark/11.2.6.3 续租 Work.md` |
| 11.2.6.4 | 查询 Work 队列状态 | 762 | 25460-25492 | 23 | `chapters/volcengine/ark/11.2.6.4 查询 Work 队列状态.md` |
| 11.2.6.5 | 停止 Work | 763-765 | 25493-25565 | 56 | `chapters/volcengine/ark/11.2.6.5 停止 Work.md` |
| 11.2.6.6 | 查询 Work 列表 | 766-768 | 25566-25658 | 76 | `chapters/volcengine/ark/11.2.6.6 查询 Work 列表.md` |
| 11.2.6.7 | 查询 Work 详情 | 769-770 | 25659-25716 | 46 | `chapters/volcengine/ark/11.2.6.7 查询 Work 详情.md` |
| 11.3.1 | 创建会话 | 771-801 | 25718-26772 | 846 | `chapters/volcengine/ark/11.3.1 创建会话.md` |
| 11.3.2 | 查询会话列表 | 802-821 | 26773-27423 | 563 | `chapters/volcengine/ark/11.3.2 查询会话列表.md` |
| 11.3.3 | 查询会话详情 | 822-840 | 27424-28029 | 525 | `chapters/volcengine/ark/11.3.3 查询会话详情.md` |
| 11.3.4 | 更新会话标题和标签 | 841-859 | 28030-28648 | 531 | `chapters/volcengine/ark/11.3.4 更新会话标题和标签.md` |
| 11.3.5 | 升级会话 | 860-886 | 28649-29534 | 749 | `chapters/volcengine/ark/11.3.5 升级会话.md` |
| 11.3.6 | 删除会话 | 887 | 29535-29561 | 20 | `chapters/volcengine/ark/11.3.6 删除会话.md` |
| 11.3.7.1 | 查询会话任务 | 888-891 | 29563-29685 | 93 | `chapters/volcengine/ark/11.3.7.1 查询会话任务.md` |
| 11.3.7.2 | 查询会话任务列表 | 892-895 | 29686-29801 | 88 | `chapters/volcengine/ark/11.3.7.2 查询会话任务列表.md` |
| 11.3.7.3 | 取消会话任务 | 896-897 | 29802-29860 | 31 | `chapters/volcengine/ark/11.3.7.3 取消会话任务.md` |
| 11.3.8.1 | 发送会话事件 | 898-899 | 29862-29908 | 33 | `chapters/volcengine/ark/11.3.8.1 发送会话事件.md` |
| 11.3.8.2 | 查询会话事件列表 | 900-902 | 29909-29975 | 50 | `chapters/volcengine/ark/11.3.8.2 查询会话事件列表.md` |
| 11.3.8.3 | 流式获取会话事件 | 903-904 | 29976-30036 | 34 | `chapters/volcengine/ark/11.3.8.3 流式获取会话事件.md` |
| 11.3.8.4 | 会话事件结构参考 - 第1部分 | 905-963 | 30037-31848 | 1643 | `chapters/volcengine/ark/11.3.8.4 会话事件结构参考 - 第1部分.md` |
| 11.3.9.1 | 添加会话资源 | 964-965 | 31850-31900 | 37 | `chapters/volcengine/ark/11.3.9.1 添加会话资源.md` |
| 11.3.9.2 | 查询会话资源列表 | 966-969 | 31901-32001 | 90 | `chapters/volcengine/ark/11.3.9.2 查询会话资源列表.md` |
| 11.3.9.3 | 查询会话资源 | 970-971 | 32002-32046 | 36 | `chapters/volcengine/ark/11.3.9.3 查询会话资源.md` |
| 11.3.10.1 | 查询线程列表 | 972-974 | 32048-32117 | 56 | `chapters/volcengine/ark/11.3.10.1 查询线程列表.md` |
| 11.3.10.2 | 查询线程详情 | 975-976 | 32118-32166 | 37 | `chapters/volcengine/ark/11.3.10.2 查询线程详情.md` |
| 11.3.10.3 | 查询线程事件列表 | 977-978 | 32167-32228 | 46 | `chapters/volcengine/ark/11.3.10.3 查询线程事件列表.md` |
| 11.3.10.4 | 流式获取线程事件 | 979-980 | 32229-32277 | 29 | `chapters/volcengine/ark/11.3.10.4 流式获取线程事件.md` |
| 11.4.1 | 创建保管库 | 981-982 | 32279-32325 | 36 | `chapters/volcengine/ark/11.4.1 创建保管库.md` |
| 11.4.2 | 查询保管库列表 | 983-984 | 32326-32394 | 55 | `chapters/volcengine/ark/11.4.2 查询保管库列表.md` |
| 11.4.3 | 查询保管库详情 | 985 | 32395-32421 | 24 | `chapters/volcengine/ark/11.4.3 查询保管库详情.md` |
| 11.4.4 | 更新保管库 | 986-987 | 32422-32463 | 33 | `chapters/volcengine/ark/11.4.4 更新保管库.md` |
| 11.4.5 | 删除保管库 | 988 | 32464-32488 | 21 | `chapters/volcengine/ark/11.4.5 删除保管库.md` |
| 11.4.6.1 | 创建凭证 | 989-1001 | 32490-32958 | 358 | `chapters/volcengine/ark/11.4.6.1 创建凭证.md` |
| 11.4.6.2 | 查询凭证列表 | 1002-1008 | 32959-33183 | 182 | `chapters/volcengine/ark/11.4.6.2 查询凭证列表.md` |
| 11.4.6.3 | 查询凭证详情 | 1009-1014 | 33184-33380 | 160 | `chapters/volcengine/ark/11.4.6.3 查询凭证详情.md` |
| 11.4.6.4 | 更新凭证 | 1015-1027 | 33381-33823 | 334 | `chapters/volcengine/ark/11.4.6.4 更新凭证.md` |
| 11.4.6.5 | 删除凭证 | 1028 | 33824-33850 | 21 | `chapters/volcengine/ark/11.4.6.5 删除凭证.md` |
| 11.5.1 | 创建记忆库 | 1029-1031 | 33852-33931 | 61 | `chapters/volcengine/ark/11.5.1 创建记忆库.md` |
| 11.5.2 | 查询记忆库列表 | 1032-1035 | 33932-34036 | 80 | `chapters/volcengine/ark/11.5.2 查询记忆库列表.md` |
| 11.5.3 | 查询记忆库详情 | 1036-1037 | 34037-34098 | 47 | `chapters/volcengine/ark/11.5.3 查询记忆库详情.md` |
| 11.5.4 | 更新记忆库 | 1038-1040 | 34099-34179 | 61 | `chapters/volcengine/ark/11.5.4 更新记忆库.md` |
| 11.5.5 | 删除记忆库 | 1041 | 34180-34205 | 18 | `chapters/volcengine/ark/11.5.5 删除记忆库.md` |
| 11.5.6.1 | 创建记忆 | 1042-1044 | 34207-34273 | 51 | `chapters/volcengine/ark/11.5.6.1 创建记忆.md` |
| 11.5.6.2 | 批量创建记忆 | 1045-1048 | 34274-34393 | 90 | `chapters/volcengine/ark/11.5.6.2 批量创建记忆.md` |
| 11.5.6.3 | 查询记忆列表 | 1049-1051 | 34394-34487 | 70 | `chapters/volcengine/ark/11.5.6.3 查询记忆列表.md` |
| 11.5.6.4 | 查询记忆详情 | 1052-1053 | 34488-34546 | 45 | `chapters/volcengine/ark/11.5.6.4 查询记忆详情.md` |
| 11.5.6.5 | 更新记忆 | 1054-1056 | 34547-34621 | 52 | `chapters/volcengine/ark/11.5.6.5 更新记忆.md` |
| 11.5.6.6 | 删除记忆 | 1057 | 34622-34649 | 18 | `chapters/volcengine/ark/11.5.6.6 删除记忆.md` |
| 11.6.1 | 创建 Dream | 1058-1061 | 34651-34775 | 108 | `chapters/volcengine/ark/11.6.1 创建 Dream.md` |
| 11.6.2 | 查询 Dream 列表 | 1062-1066 | 34776-34915 | 119 | `chapters/volcengine/ark/11.6.2 查询 Dream 列表.md` |
| 11.6.3 | 查询 Dream | 1067-1069 | 34916-35011 | 83 | `chapters/volcengine/ark/11.6.3 查询 Dream.md` |
| 11.6.4 | 取消 Dream | 1070-1072 | 35012-35110 | 84 | `chapters/volcengine/ark/11.6.4 取消 Dream.md` |
| 11.7.1 | 创建技能 | 1073-1074 | 35112-35180 | 49 | `chapters/volcengine/ark/11.7.1 创建技能.md` |
| 11.7.2 | 查询技能列表 | 1075-1077 | 35181-35257 | 61 | `chapters/volcengine/ark/11.7.2 查询技能列表.md` |
| 11.7.3 | 查询技能详情 | 1078-1079 | 35258-35303 | 36 | `chapters/volcengine/ark/11.7.3 查询技能详情.md` |
| 11.7.4 | 设置技能内容保护 | 1080-1081 | 35304-35349 | 37 | `chapters/volcengine/ark/11.7.4 设置技能内容保护.md` |
| 11.7.5 | 删除技能 | 1082 | 35350-35375 | 18 | `chapters/volcengine/ark/11.7.5 删除技能.md` |
| 11.7.6 | 创建新版本的技能 | 1083-1084 | 35376-35435 | 41 | `chapters/volcengine/ark/11.7.6 创建新版本的技能.md` |
| 11.7.7 | 查询技能的版本列表 | 1085-1086 | 35436-35491 | 48 | `chapters/volcengine/ark/11.7.7 查询技能的版本列表.md` |
| 11.7.8 | 查询指定版本的技能 | 1087 | 35492-35521 | 26 | `chapters/volcengine/ark/11.7.8 查询指定版本的技能.md` |
| 11.7.9 | 删除指定版本的技能 | 1088 | 35522-35543 | 17 | `chapters/volcengine/ark/11.7.9 删除指定版本的技能.md` |
| 11.7.10 | 下载指定版本的技能 | 1089 | 35544-35562 | 14 | `chapters/volcengine/ark/11.7.10 下载指定版本的技能.md` |
| 11.7.11 | 扫描 GitHub 技能 | 1090-1091 | 35563-35615 | 43 | `chapters/volcengine/ark/11.7.11 扫描 GitHub 技能.md` |
| 11.7.12 | 导入 GitHub 技能 | 1092-1094 | 35616-35693 | 58 | `chapters/volcengine/ark/11.7.12 导入 GitHub 技能.md` |
| 12.1.1 | 创建批量推理任务 | 1095-1098 | 35696-35776 | 60 | `chapters/volcengine/ark/12.1.1 创建批量推理任务.md` |
| 12.1.2 | 获取批量推理任务列表 | 1099-1104 | 35777-35952 | 152 | `chapters/volcengine/ark/12.1.2 获取批量推理任务列表.md` |
| 12.1.3 | 获取批量推理任务 | 1105-1108 | 35953-36072 | 100 | `chapters/volcengine/ark/12.1.3 获取批量推理任务.md` |
| 12.1.4 | 更新批量推理任务 | 1109 | 36073-36096 | 17 | `chapters/volcengine/ark/12.1.4 更新批量推理任务.md` |
| 12.1.5 | 删除批量推理任务 | 1110 | 36097-36116 | 13 | `chapters/volcengine/ark/12.1.5 删除批量推理任务.md` |
| 12.1.6 | 停止批量推理任务 | 1111 | 36117-36139 | 14 | `chapters/volcengine/ark/12.1.6 停止批量推理任务.md` |
| 12.1.7 | 重启批量推理任务 | 1112 | 36140-36160 | 13 | `chapters/volcengine/ark/12.1.7 重启批量推理任务.md` |
| 12.2 | 批量(Chat) API | 1113-1135 | 36161-36616 | 339 | `chapters/volcengine/ark/12.2 批量(Chat) API.md` |
| 13.1 | 分词 API | 1136-1137 | 36618-36664 | 39 | `chapters/volcengine/ark/13.1 分词 API.md` |
| 14.1.1 | 获取临时 API Key | 1138-1139 | 36667-36703 | 26 | `chapters/volcengine/ark/14.1.1 获取临时 API Key.md` |
| 14.2.1 | 创建个人版套餐 | 1140-1141 | 36705-36762 | 33 | `chapters/volcengine/ark/14.2.1 创建个人版套餐.md` |
| 14.2.2 | 续费个人版套餐 | 1142-1143 | 36763-36808 | 27 | `chapters/volcengine/ark/14.2.2 续费个人版套餐.md` |
| 14.2.3 | 查询个人版套餐 | 1144 | 36809-36836 | 20 | `chapters/volcengine/ark/14.2.3 查询个人版套餐.md` |
| 14.2.4.1 | 查询 Agent Plan 支持的模型列表 | 1145 | 36838-36857 | 14 | `chapters/volcengine/ark/14.2.4.1 查询 Agent Plan 支持的模型列表.md` |
| 14.2.4.2 | 轮换个人版 API Key | 1146 | 36858-36884 | 17 | `chapters/volcengine/ark/14.2.4.2 轮换个人版 API Key.md` |
| 14.2.4.3 | 获取套餐 AFP 额度 | 1147-1149 | 36885-36961 | 66 | `chapters/volcengine/ark/14.2.4.3 获取套餐 AFP 额度.md` |
| 14.2.4.4 | 获取套餐用量详情 | 1150-1151 | 36962-37010 | 39 | `chapters/volcengine/ark/14.2.4.4 获取套餐用量详情.md` |
| 14.2.5.1 | 查询 Coding Plan 支持的模型列表 | 1152 | 37012-37027 | 12 | `chapters/volcengine/ark/14.2.5.1 查询 Coding Plan 支持的模型列表.md` |
| 14.3.1 | 获取基础模型版本列表 | 1153-1155 | 37029-37116 | 72 | `chapters/volcengine/ark/14.3.1 获取基础模型版本列表.md` |
| 14.3.2 | 获取基础模型版本信息 | 1156-1166 | 37117-37440 | 273 | `chapters/volcengine/ark/14.3.2 获取基础模型版本信息.md` |
| 14.3.3 | 获取基础模型列表 | 1167-1172 | 37441-37695 | 186 | `chapters/volcengine/ark/14.3.3 获取基础模型列表.md` |
| 14.3.4 | 获取基础模型信息 | 1173-1176 | 37696-37822 | 93 | `chapters/volcengine/ark/14.3.4 获取基础模型信息.md` |
| 14.4.1 | 批量开通基础模型 | 1177 | 37824-37838 | 11 | `chapters/volcengine/ark/14.4.1 批量开通基础模型.md` |
| 14.4.2 | 启用自动开通新模型 | 1178 | 37839-37850 | 7 | `chapters/volcengine/ark/14.4.2 启用自动开通新模型.md` |
| 14.4.3 | 关闭自动开通新模型 | 1179 | 37851-37862 | 7 | `chapters/volcengine/ark/14.4.3 关闭自动开通新模型.md` |
| 14.4.4 | 查询模型开通详情 | 1180-1184 | 37863-38007 | 131 | `chapters/volcengine/ark/14.4.4 查询模型开通详情.md` |
| 14.4.5 | 查询模型开通列表 | 1185-1190 | 38008-38187 | 163 | `chapters/volcengine/ark/14.4.5 查询模型开通列表.md` |
| 14.5.1 | 批量开通资源 | 1191 | 38189-38207 | 14 | `chapters/volcengine/ark/14.5.1 批量开通资源.md` |
| 14.5.2 | 查询资源开通列表 | 1192-1195 | 38208-38311 | 92 | `chapters/volcengine/ark/14.5.2 查询资源开通列表.md` |
| 14.6.1 | 查询模型限流 | 1196-1199 | 38313-38414 | 91 | `chapters/volcengine/ark/14.6.1 查询模型限流.md` |
| 14.7.1 | 删除定制模型 | 1200 | 38416-38440 | 16 | `chapters/volcengine/ark/14.7.1 删除定制模型.md` |
| 14.7.2 | 获取定制模型信息 | 1201-1204 | 38441-38551 | 97 | `chapters/volcengine/ark/14.7.2 获取定制模型信息.md` |
| 14.7.3 | 更新定制模型 | 1205-1206 | 38552-38586 | 22 | `chapters/volcengine/ark/14.7.3 更新定制模型.md` |
| 14.7.4 | 获取定制模型列表 | 1207-1210 | 38587-38707 | 102 | `chapters/volcengine/ark/14.7.4 获取定制模型列表.md` |
| 14.8.1 | 创建模型调优任务 | 1211-1221 | 38709-39032 | 279 | `chapters/volcengine/ark/14.8.1 创建模型调优任务.md` |
| 14.8.2 | 删除模型调优任务 | 1222 | 39033-39049 | 10 | `chapters/volcengine/ark/14.8.2 删除模型调优任务.md` |
| 14.8.3 | 获取模型调优任务信息 | 1223-1237 | 39050-39511 | 411 | `chapters/volcengine/ark/14.8.3 获取模型调优任务信息.md` |
| 14.8.4 | 查询精调效果指标详细数据 | 1238-1239 | 39512-39557 | 33 | `chapters/volcengine/ark/14.8.4 查询精调效果指标详细数据.md` |
| 14.8.5 | 查询精调效果指标 | 1240 | 39558-39576 | 10 | `chapters/volcengine/ark/14.8.5 查询精调效果指标.md` |
| 14.8.6 | 获取模型调优任务列表 | 1241-1249 | 39577-39851 | 246 | `chapters/volcengine/ark/14.8.6 获取模型调优任务列表.md` |
| 14.8.7 | 重试模型调优任务 | 1250 | 39852-39868 | 9 | `chapters/volcengine/ark/14.8.7 重试模型调优任务.md` |
| 14.8.8 | 停止模型调优任务 | 1251 | 39869-39885 | 10 | `chapters/volcengine/ark/14.8.8 停止模型调优任务.md` |
| 14.8.9 | 更新模型调优任务 | 1252 | 39886-39909 | 14 | `chapters/volcengine/ark/14.8.9 更新模型调优任务.md` |
| 14.9.1 | 开启推理接入点 | 1253 | 39911-39930 | 13 | `chapters/volcengine/ark/14.9.1 开启推理接入点.md` |
| 14.9.2 | 停止推理接入点 | 1254 | 39931-39951 | 11 | `chapters/volcengine/ark/14.9.2 停止推理接入点.md` |
| 14.9.3 | 获取推理接入点列表 | 1255-1260 | 39952-40164 | 168 | `chapters/volcengine/ark/14.9.3 获取推理接入点列表.md` |
| 14.9.4 | 获取推理接入点 | 1261-1264 | 40165-40268 | 88 | `chapters/volcengine/ark/14.9.4 获取推理接入点.md` |
| 14.9.5 | 删除推理接入点 | 1265 | 40269-40288 | 12 | `chapters/volcengine/ark/14.9.5 删除推理接入点.md` |
| 14.9.6 | 更新推理接入点 | 1266-1271 | 40289-40475 | 160 | `chapters/volcengine/ark/14.9.6 更新推理接入点.md` |
| 14.9.7 | 创建推理接入点 | 1272-1279 | 40476-40706 | 192 | `chapters/volcengine/ark/14.9.7 创建推理接入点.md` |
| 14.9.8 | 获取接入点推理应用层加密证书 | 1280-1281 | 40707-40742 | 23 | `chapters/volcengine/ark/14.9.8 获取接入点推理应用层加密证书.md` |
| 14.9.9 | 创建推理接入点滚动升级任务 | 1282-1283 | 40743-40790 | 41 | `chapters/volcengine/ark/14.9.9 创建推理接入点滚动升级任务.md` |
| 14.9.10 | 查询推理接入点滚动升级详情 | 1284-1288 | 40791-40919 | 116 | `chapters/volcengine/ark/14.9.10 查询推理接入点滚动升级详情.md` |
| 14.9.11 | 回滚推理接入点滚动升级 | 1289 | 40920-40937 | 13 | `chapters/volcengine/ark/14.9.11 回滚推理接入点滚动升级.md` |
| 14.9.12 | 取消推理接入点滚动升级 | 1290 | 40938-40955 | 13 | `chapters/volcengine/ark/14.9.12 取消推理接入点滚动升级.md` |
| 14.10.1 | 创建评测任务 | 1291-1295 | 40957-41122 | 131 | `chapters/volcengine/ark/14.10.1 创建评测任务.md` |
| 14.10.2 | 删除评测任务 | 1296 | 41123-41144 | 13 | `chapters/volcengine/ark/14.10.2 删除评测任务.md` |
| 14.10.3 | 获取评测任务 | 1297-1299 | 41145-41226 | 67 | `chapters/volcengine/ark/14.10.3 获取评测任务.md` |
| 14.10.4 | 获取评测任务结果 | 1300-1303 | 41227-41331 | 87 | `chapters/volcengine/ark/14.10.4 获取评测任务结果.md` |
| 14.10.5 | 获取评测任务列表 | 1304-1308 | 41332-41480 | 129 | `chapters/volcengine/ark/14.10.5 获取评测任务列表.md` |
| 14.10.6 | 获取评测任务结果列表 | 1309-1313 | 41481-41624 | 120 | `chapters/volcengine/ark/14.10.6 获取评测任务结果列表.md` |
| 14.10.7 | 停止评测任务 | 1314 | 41625-41646 | 13 | `chapters/volcengine/ark/14.10.7 停止评测任务.md` |
| 14.10.8 | 更新评测任务 | 1315 | 41647-41672 | 18 | `chapters/volcengine/ark/14.10.8 更新评测任务.md` |
| 14.11.1 | 查询推理用量 | 1316-1318 | 41674-41800 | 75 | `chapters/volcengine/ark/14.11.1 查询推理用量.md` |
| 14.11.2 | 查询单请求用量 | 1319-1323 | 41801-41941 | 124 | `chapters/volcengine/ark/14.11.2 查询单请求用量.md` |
| 14.11.3 | 查询异步任务用量 | 1324-1326 | 41942-42014 | 62 | `chapters/volcengine/ark/14.11.3 查询异步任务用量.md` |
| 14.11.4 | 创建用量明细导出任务 | 1327-1328 | 42015-42069 | 33 | `chapters/volcengine/ark/14.11.4 创建用量明细导出任务.md` |
| 14.11.5 | 查询用量明细导出任务状态 | 1329-1331 | 42070-42172 | 71 | `chapters/volcengine/ark/14.11.5 查询用量明细导出任务状态.md` |
| 14.11.6 | 查询模型推理限额 | 1332 | 42173-42200 | 22 | `chapters/volcengine/ark/14.11.6 查询模型推理限额.md` |
| 14.11.7 | 开启模型推理限额 | 1333 | 42201-42225 | 16 | `chapters/volcengine/ark/14.11.7 开启模型推理限额.md` |
| 14.11.8 | 关闭模型推理限额 | 1334 | 42226-42246 | 12 | `chapters/volcengine/ark/14.11.8 关闭模型推理限额.md` |
| 14.12.1 | 创建方舟官方模型产物查询请求 | 1335 | 42248-42266 | 14 | `chapters/volcengine/ark/14.12.1 创建方舟官方模型产物查询请求.md` |
| 14.12.2 | 获取安全审计日志 | 1336-1339 | 42267-42388 | 85 | `chapters/volcengine/ark/14.12.2 获取安全审计日志.md` |
| 14.12.3 | 获取方舟官方产物确认结果 | 1340-1341 | 42389-42420 | 24 | `chapters/volcengine/ark/14.12.3 获取方舟官方产物确认结果.md` |
| 14.13.1 | 上报视频生成模型效果问题 | 1342-1345 | 42422-42547 | 86 | `chapters/volcengine/ark/14.13.1 上报视频生成模型效果问题.md` |
| 14.13.2 | 查询视频生成模型效果问题结果 | 1346-1349 | 42548-42636 | 69 | `chapters/volcengine/ark/14.13.2 查询视频生成模型效果问题结果.md` |
| 14.13.3 | 上报大语言模型效果问题 | 1350-1352 | 42637-42745 | 81 | `chapters/volcengine/ark/14.13.3 上报大语言模型效果问题.md` |
| 14.13.4 | 查询大语言模型效果问题结果 | 1353-1356 | 42746-42863 | 97 | `chapters/volcengine/ark/14.13.4 查询大语言模型效果问题结果.md` |
| 15.1 | 兼容 OpenAI SDK | 1357-1360 | 42865-42981 | 103 | `chapters/volcengine/ark/15.1 兼容 OpenAI SDK.md` |
| 15.2 | 向后兼容性 | 1361 | 42982-43027 | 25 | `chapters/volcengine/ark/15.2 向后兼容性.md` |
| 15.3 | 错误码 - 第1部分 | 1361-1382 | 43028-45011 | 1936 | `chapters/volcengine/ark/15.3 错误码 - 第1部分.md` |
| 15.3 | 错误码 - 第2部分·错误码 | 1383-1392 | 45012-45786 | 751 | `chapters/volcengine/ark/15.3 错误码 - 第2部分·错误码.md` |
| 15.4 | SDK 常见使用示例 | 1393-1410 | 45787-46468 | 611 | `chapters/volcengine/ark/15.4 SDK 常见使用示例.md` |
