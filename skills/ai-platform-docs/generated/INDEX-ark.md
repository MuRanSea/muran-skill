# 方舟 API 区章节表（ark）

来源：《火山方舟 API 参考》（1392 页）。199 个章节文件，接口级切分：一个接口/任务一个文件；超过 1500 行的按语义块自动再拆为`… - 第N部分`（5 个章节被拆分）。

「页码」是原 PDF 页码范围；「行范围」是中间 MD（`doc/<源文档>.md`）的 1 起始行号，可据此回查原文。章节文件本身已去掉页眉页脚，回查 PDF 时用这两列。文件名即章节标题，日常定位直接 Glob 文件名即可，用不到这两列。

**这张表用来 grep，不要整读。**

| 编号 | 标题 | 页码 | 行范围(源文件) | 行数 | 文件 |
|------|------|------|---------------|------|------|
| 1.1 | 获取 API Key 并配置 | 1 | 278-312 | 19 | `chapters/volcengine/ark/1.1 获取 API Key 并配置.md` |
| 1.2 | 安装及升级 SDK | 2-7 | 313-468 | 115 | `chapters/volcengine/ark/1.2 安装及升级 SDK.md` |
| 1.3 | Base URL及鉴权 | 8-10 | 469-564 | 68 | `chapters/volcengine/ark/1.3 Base URL及鉴权.md` |
| 2.1 | 对话(Chat) API | 11-41 | 566-1754 | 885 | `chapters/volcengine/ark/2.1 对话(Chat) API.md` |
| 3.1 | 创建 Response - 第1部分 | 42-90 | 1755-3440 | 1428 | `chapters/volcengine/ark/3.1 创建 Response - 第1部分.md` |
| 3.1 | 创建 Response - 第2部分·响应参数 | 91-133 | 3441-4826 | 1211 | `chapters/volcengine/ark/3.1 创建 Response - 第2部分·响应参数.md` |
| 3.2 | 查询 Response 详情 | 134-170 | 4827-5981 | 1062 | `chapters/volcengine/ark/3.2 查询 Response 详情.md` |
| 3.3 | 查询 Response 输入项列表 | 171-199 | 5982-6894 | 831 | `chapters/volcengine/ark/3.3 查询 Response 输入项列表.md` |
| 3.4 | 删除 Response | 200 | 6895-6918 | 19 | `chapters/volcengine/ark/3.4 删除 Response.md` |
| 3.5.1 | Response 生命周期 - 第1部分 | 201-252 | 6919-8629 | 1505 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第1部分.md` |
| 3.5.1 | Response 生命周期 - 第2部分 | 253-303 | 8630-10314 | 1479 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第2部分.md` |
| 3.5.1 | Response 生命周期 - 第3部分 | 304-355 | 10315-12019 | 1502 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第3部分.md` |
| 3.5.1 | Response 生命周期 - 第4部分 | 356-414 | 12020-13997 | 1719 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第4部分.md` |
| 3.5.2 | Output Item 与文本回答 - 第1部分 | 415-465 | 13998-15628 | 1470 | `chapters/volcengine/ark/3.5.2 Output Item 与文本回答 - 第1部分.md` |
| 3.5.2 | Output Item 与文本回答 - 第2部分 | 466-486 | 15629-16256 | 586 | `chapters/volcengine/ark/3.5.2 Output Item 与文本回答 - 第2部分.md` |
| 3.5.3 | 工具调用事件 | 487-523 | 16257-17357 | 1024 | `chapters/volcengine/ark/3.5.3 工具调用事件.md` |
| 3.5.4 | 语音转写与错误事件 | 524-529 | 17358-17530 | 161 | `chapters/volcengine/ark/3.5.4 语音转写与错误事件.md` |
| 4.1 | 创建 Message | 530-549 | 17532-18181 | 564 | `chapters/volcengine/ark/4.1 创建 Message.md` |
| 4.2 | 统计 Messages 请求 token 数 | 550-559 | 18182-18518 | 278 | `chapters/volcengine/ark/4.2 统计 Messages 请求 token 数.md` |
| 5.1 | System One API（beta） | 560-568 | 18520-18794 | 240 | `chapters/volcengine/ark/5.1 System One API（beta）.md` |
| 6.1 | 上传文件 | 569-574 | 18796-19007 | 157 | `chapters/volcengine/ark/6.1 上传文件.md` |
| 6.2 | 查询文件详情 | 575-577 | 19008-19081 | 63 | `chapters/volcengine/ark/6.2 查询文件详情.md` |
| 6.3 | 查询文件列表 | 578-581 | 19082-19216 | 112 | `chapters/volcengine/ark/6.3 查询文件列表.md` |
| 6.4 | 删除文件 | 582 | 19217-19239 | 19 | `chapters/volcengine/ark/6.4 删除文件.md` |
| 6.5 | The file object | 583-585 | 19240-19311 | 57 | `chapters/volcengine/ark/6.5 The file object.md` |
| 7.1 | 创建视频生成任务 | 586-603 | 19313-20177 | 600 | `chapters/volcengine/ark/7.1 创建视频生成任务.md` |
| 7.2 | 查询视频生成任务 | 604-607 | 20178-20318 | 105 | `chapters/volcengine/ark/7.2 查询视频生成任务.md` |
| 7.3 | 查询视频生成任务列表 | 608-613 | 20319-20523 | 156 | `chapters/volcengine/ark/7.3 查询视频生成任务列表.md` |
| 7.4 | 取消或删除视频生成任务 | 614 | 20524-20565 | 38 | `chapters/volcengine/ark/7.4 取消或删除视频生成任务.md` |
| 8.1 | 图片生成 API | 615-632 | 20567-21314 | 520 | `chapters/volcengine/ark/8.1 图片生成 API.md` |
| 8.2 | 图片生成流式响应事件 | 633-638 | 21315-21493 | 156 | `chapters/volcengine/ark/8.2 图片生成流式响应事件.md` |
| 9.1.1 | 创建 3D 生成任务 API | 639-641 | 21496-21599 | 80 | `chapters/volcengine/ark/9.1.1 创建 3D 生成任务 API.md` |
| 9.1.2 | 查询 3D 生成任务 API | 642-643 | 21600-21669 | 52 | `chapters/volcengine/ark/9.1.2 查询 3D 生成任务 API.md` |
| 9.1.3 | 查询 3D 生成任务列表 | 644-647 | 21670-21785 | 87 | `chapters/volcengine/ark/9.1.3 查询 3D 生成任务列表.md` |
| 9.1.4 | 取消或删除 3D 生成任务 | 648 | 21786-21827 | 38 | `chapters/volcengine/ark/9.1.4 取消或删除 3D 生成任务.md` |
| 9.2.1 | 创建3D生成任务 | 649-653 | 21829-22043 | 148 | `chapters/volcengine/ark/9.2.1 创建3D生成任务.md` |
| 9.2.2 | 查询3D生成任务 | 654-655 | 22044-22109 | 48 | `chapters/volcengine/ark/9.2.2 查询3D生成任务.md` |
| 9.2.3 | 查询3D生成任务列表 | 656-658 | 22110-22217 | 81 | `chapters/volcengine/ark/9.2.3 查询3D生成任务列表.md` |
| 9.2.4 | 取消或删除3D生成任务 | 659 | 22218-22252 | 31 | `chapters/volcengine/ark/9.2.4 取消或删除3D生成任务.md` |
| 9.3.1 | 创建3D生成任务 | 660-663 | 22254-22385 | 95 | `chapters/volcengine/ark/9.3.1 创建3D生成任务.md` |
| 9.3.2 | 查询3D生成任务 | 664-665 | 22386-22451 | 48 | `chapters/volcengine/ark/9.3.2 查询3D生成任务.md` |
| 9.3.3 | 查询3D生成任务列表 | 666-668 | 22452-22559 | 81 | `chapters/volcengine/ark/9.3.3 查询3D生成任务列表.md` |
| 9.3.4 | 取消或删除3D生成任务 | 669 | 22560-22594 | 31 | `chapters/volcengine/ark/9.3.4 取消或删除3D生成任务.md` |
| 10.1 | 多模态向量化 API | 670-675 | 22596-22795 | 145 | `chapters/volcengine/ark/10.1 多模态向量化 API.md` |
| 11.1.1 | 创建智能体 | 676-689 | 22798-23288 | 375 | `chapters/volcengine/ark/11.1.1 创建智能体.md` |
| 11.1.2 | 查询智能体列表 | 690-697 | 23289-23549 | 215 | `chapters/volcengine/ark/11.1.2 查询智能体列表.md` |
| 11.1.3 | 查询智能体详情 | 698-704 | 23550-23773 | 180 | `chapters/volcengine/ark/11.1.3 查询智能体详情.md` |
| 11.1.4 | 更新智能体 | 705-718 | 23774-24309 | 387 | `chapters/volcengine/ark/11.1.4 更新智能体.md` |
| 11.1.5 | 删除智能体 | 719 | 24310-24330 | 14 | `chapters/volcengine/ark/11.1.5 删除智能体.md` |
| 11.1.6 | 查询智能体版本列表 | 720-727 | 24331-24580 | 202 | `chapters/volcengine/ark/11.1.6 查询智能体版本列表.md` |
| 11.2.1 | 创建环境 | 728-733 | 24582-24760 | 145 | `chapters/volcengine/ark/11.2.1 创建环境.md` |
| 11.2.2 | 查询环境列表 | 734-737 | 24761-24867 | 95 | `chapters/volcengine/ark/11.2.2 查询环境列表.md` |
| 11.2.3 | 查询环境详情 | 738-740 | 24868-24955 | 76 | `chapters/volcengine/ark/11.2.3 查询环境详情.md` |
| 11.2.4 | 更新环境 | 741-746 | 24956-25157 | 155 | `chapters/volcengine/ark/11.2.4 更新环境.md` |
| 11.2.5 | 删除环境 | 747 | 25158-25180 | 17 | `chapters/volcengine/ark/11.2.5 删除环境.md` |
| 11.2.6.1 | 长轮询拉取待执行 Work | 748-750 | 25182-25272 | 69 | `chapters/volcengine/ark/11.2.6.1 长轮询拉取待执行 Work.md` |
| 11.2.6.2 | 认领 Work | 751-753 | 25273-25345 | 56 | `chapters/volcengine/ark/11.2.6.2 认领 Work.md` |
| 11.2.6.3 | 续租 Work | 754-755 | 25346-25401 | 41 | `chapters/volcengine/ark/11.2.6.3 续租 Work.md` |
| 11.2.6.4 | 查询 Work 队列状态 | 756-757 | 25402-25436 | 23 | `chapters/volcengine/ark/11.2.6.4 查询 Work 队列状态.md` |
| 11.2.6.5 | 停止 Work | 758-760 | 25437-25509 | 56 | `chapters/volcengine/ark/11.2.6.5 停止 Work.md` |
| 11.2.6.6 | 查询 Work 列表 | 761-763 | 25510-25602 | 76 | `chapters/volcengine/ark/11.2.6.6 查询 Work 列表.md` |
| 11.2.6.7 | 查询 Work 详情 | 764-765 | 25603-25660 | 46 | `chapters/volcengine/ark/11.2.6.7 查询 Work 详情.md` |
| 11.3.1 | 创建会话 | 766-796 | 25662-26712 | 844 | `chapters/volcengine/ark/11.3.1 创建会话.md` |
| 11.3.2 | 查询会话列表 | 797-816 | 26713-27359 | 561 | `chapters/volcengine/ark/11.3.2 查询会话列表.md` |
| 11.3.3 | 查询会话详情 | 817-835 | 27360-27962 | 523 | `chapters/volcengine/ark/11.3.3 查询会话详情.md` |
| 11.3.4 | 更新会话标题和标签 | 836-854 | 27963-28577 | 529 | `chapters/volcengine/ark/11.3.4 更新会话标题和标签.md` |
| 11.3.5 | 升级会话 | 855-880 | 28578-29457 | 747 | `chapters/volcengine/ark/11.3.5 升级会话.md` |
| 11.3.6 | 删除会话 | 881 | 29458-29484 | 20 | `chapters/volcengine/ark/11.3.6 删除会话.md` |
| 11.3.7.1 | 发送会话事件 | 882-883 | 29486-29532 | 33 | `chapters/volcengine/ark/11.3.7.1 发送会话事件.md` |
| 11.3.7.2 | 查询会话事件列表 | 884-886 | 29533-29599 | 50 | `chapters/volcengine/ark/11.3.7.2 查询会话事件列表.md` |
| 11.3.7.3 | 流式获取会话事件 | 887-888 | 29600-29660 | 34 | `chapters/volcengine/ark/11.3.7.3 流式获取会话事件.md` |
| 11.3.7.4 | 会话事件结构参考 - 第1部分 | 889-947 | 29661-31481 | 1649 | `chapters/volcengine/ark/11.3.7.4 会话事件结构参考 - 第1部分.md` |
| 11.3.8.1 | 添加会话资源 | 948-949 | 31483-31533 | 37 | `chapters/volcengine/ark/11.3.8.1 添加会话资源.md` |
| 11.3.8.2 | 查询会话资源列表 | 950-953 | 31534-31630 | 88 | `chapters/volcengine/ark/11.3.8.2 查询会话资源列表.md` |
| 11.3.8.3 | 查询会话资源 | 954-955 | 31631-31675 | 36 | `chapters/volcengine/ark/11.3.8.3 查询会话资源.md` |
| 11.3.9.1 | 查询线程列表 | 956-958 | 31677-31746 | 56 | `chapters/volcengine/ark/11.3.9.1 查询线程列表.md` |
| 11.3.9.2 | 查询线程详情 | 959-960 | 31747-31795 | 37 | `chapters/volcengine/ark/11.3.9.2 查询线程详情.md` |
| 11.3.9.3 | 查询线程事件列表 | 961-962 | 31796-31857 | 46 | `chapters/volcengine/ark/11.3.9.3 查询线程事件列表.md` |
| 11.3.9.4 | 流式获取线程事件 | 963-964 | 31858-31906 | 29 | `chapters/volcengine/ark/11.3.9.4 流式获取线程事件.md` |
| 11.4.1 | 创建保管库 | 965-966 | 31908-31954 | 36 | `chapters/volcengine/ark/11.4.1 创建保管库.md` |
| 11.4.2 | 查询保管库列表 | 967-968 | 31955-32023 | 55 | `chapters/volcengine/ark/11.4.2 查询保管库列表.md` |
| 11.4.3 | 查询保管库详情 | 969 | 32024-32050 | 24 | `chapters/volcengine/ark/11.4.3 查询保管库详情.md` |
| 11.4.4 | 更新保管库 | 970-971 | 32051-32092 | 33 | `chapters/volcengine/ark/11.4.4 更新保管库.md` |
| 11.4.5 | 删除保管库 | 972 | 32093-32117 | 21 | `chapters/volcengine/ark/11.4.5 删除保管库.md` |
| 11.4.6.1 | 创建凭证 | 973-985 | 32119-32587 | 358 | `chapters/volcengine/ark/11.4.6.1 创建凭证.md` |
| 11.4.6.2 | 查询凭证列表 | 986-992 | 32588-32812 | 182 | `chapters/volcengine/ark/11.4.6.2 查询凭证列表.md` |
| 11.4.6.3 | 查询凭证详情 | 993-998 | 32813-33009 | 160 | `chapters/volcengine/ark/11.4.6.3 查询凭证详情.md` |
| 11.4.6.4 | 更新凭证 | 999-1011 | 33010-33452 | 334 | `chapters/volcengine/ark/11.4.6.4 更新凭证.md` |
| 11.4.6.5 | 删除凭证 | 1012 | 33453-33479 | 21 | `chapters/volcengine/ark/11.4.6.5 删除凭证.md` |
| 11.5.1 | 创建记忆库 | 1013-1015 | 33481-33560 | 61 | `chapters/volcengine/ark/11.5.1 创建记忆库.md` |
| 11.5.2 | 查询记忆库列表 | 1016-1019 | 33561-33665 | 80 | `chapters/volcengine/ark/11.5.2 查询记忆库列表.md` |
| 11.5.3 | 查询记忆库详情 | 1020-1021 | 33666-33727 | 47 | `chapters/volcengine/ark/11.5.3 查询记忆库详情.md` |
| 11.5.4 | 更新记忆库 | 1022-1024 | 33728-33808 | 61 | `chapters/volcengine/ark/11.5.4 更新记忆库.md` |
| 11.5.5 | 删除记忆库 | 1025 | 33809-33834 | 18 | `chapters/volcengine/ark/11.5.5 删除记忆库.md` |
| 11.5.6.1 | 创建记忆 | 1026-1028 | 33836-33902 | 51 | `chapters/volcengine/ark/11.5.6.1 创建记忆.md` |
| 11.5.6.2 | 批量创建记忆 | 1029-1032 | 33903-34022 | 90 | `chapters/volcengine/ark/11.5.6.2 批量创建记忆.md` |
| 11.5.6.3 | 查询记忆列表 | 1033-1035 | 34023-34116 | 70 | `chapters/volcengine/ark/11.5.6.3 查询记忆列表.md` |
| 11.5.6.4 | 查询记忆详情 | 1036-1037 | 34117-34175 | 45 | `chapters/volcengine/ark/11.5.6.4 查询记忆详情.md` |
| 11.5.6.5 | 更新记忆 | 1038-1040 | 34176-34250 | 52 | `chapters/volcengine/ark/11.5.6.5 更新记忆.md` |
| 11.5.6.6 | 删除记忆 | 1041 | 34251-34278 | 18 | `chapters/volcengine/ark/11.5.6.6 删除记忆.md` |
| 11.6.1 | 创建 Dream | 1042-1045 | 34280-34404 | 108 | `chapters/volcengine/ark/11.6.1 创建 Dream.md` |
| 11.6.2 | 查询 Dream 列表 | 1046-1050 | 34405-34544 | 119 | `chapters/volcengine/ark/11.6.2 查询 Dream 列表.md` |
| 11.6.3 | 查询 Dream | 1051-1053 | 34545-34640 | 83 | `chapters/volcengine/ark/11.6.3 查询 Dream.md` |
| 11.6.4 | 取消 Dream | 1054-1057 | 34641-34741 | 84 | `chapters/volcengine/ark/11.6.4 取消 Dream.md` |
| 11.7.1 | 创建技能 | 1058-1059 | 34743-34811 | 49 | `chapters/volcengine/ark/11.7.1 创建技能.md` |
| 11.7.2 | 查询技能列表 | 1060-1062 | 34812-34888 | 61 | `chapters/volcengine/ark/11.7.2 查询技能列表.md` |
| 11.7.3 | 查询技能详情 | 1063-1064 | 34889-34934 | 36 | `chapters/volcengine/ark/11.7.3 查询技能详情.md` |
| 11.7.4 | 设置技能内容保护 | 1065-1066 | 34935-34980 | 37 | `chapters/volcengine/ark/11.7.4 设置技能内容保护.md` |
| 11.7.5 | 删除技能 | 1067 | 34981-35006 | 18 | `chapters/volcengine/ark/11.7.5 删除技能.md` |
| 11.7.6 | 创建新版本的技能 | 1068-1069 | 35007-35066 | 41 | `chapters/volcengine/ark/11.7.6 创建新版本的技能.md` |
| 11.7.7 | 查询技能的版本列表 | 1070-1071 | 35067-35122 | 48 | `chapters/volcengine/ark/11.7.7 查询技能的版本列表.md` |
| 11.7.8 | 查询指定版本的技能 | 1072-1073 | 35123-35154 | 26 | `chapters/volcengine/ark/11.7.8 查询指定版本的技能.md` |
| 11.7.9 | 删除指定版本的技能 | 1074 | 35155-35176 | 17 | `chapters/volcengine/ark/11.7.9 删除指定版本的技能.md` |
| 11.7.10 | 下载指定版本的技能 | 1075 | 35177-35195 | 14 | `chapters/volcengine/ark/11.7.10 下载指定版本的技能.md` |
| 11.7.11 | 扫描 GitHub 技能 | 1076-1077 | 35196-35248 | 43 | `chapters/volcengine/ark/11.7.11 扫描 GitHub 技能.md` |
| 11.7.12 | 导入 GitHub 技能 | 1078-1080 | 35249-35326 | 58 | `chapters/volcengine/ark/11.7.12 导入 GitHub 技能.md` |
| 12.1.1 | 创建批量推理任务 | 1081-1084 | 35329-35409 | 60 | `chapters/volcengine/ark/12.1.1 创建批量推理任务.md` |
| 12.1.2 | 获取批量推理任务列表 | 1085-1090 | 35410-35585 | 152 | `chapters/volcengine/ark/12.1.2 获取批量推理任务列表.md` |
| 12.1.3 | 获取批量推理任务 | 1091-1094 | 35586-35705 | 100 | `chapters/volcengine/ark/12.1.3 获取批量推理任务.md` |
| 12.1.4 | 更新批量推理任务 | 1095 | 35706-35729 | 17 | `chapters/volcengine/ark/12.1.4 更新批量推理任务.md` |
| 12.1.5 | 删除批量推理任务 | 1096 | 35730-35749 | 13 | `chapters/volcengine/ark/12.1.5 删除批量推理任务.md` |
| 12.1.6 | 停止批量推理任务 | 1097 | 35750-35772 | 14 | `chapters/volcengine/ark/12.1.6 停止批量推理任务.md` |
| 12.1.7 | 重启批量推理任务 | 1098 | 35773-35793 | 13 | `chapters/volcengine/ark/12.1.7 重启批量推理任务.md` |
| 12.2 | 批量(Chat) API | 1099-1116 | 35794-36262 | 352 | `chapters/volcengine/ark/12.2 批量(Chat) API.md` |
| 13.1 | 分词 API | 1117-1118 | 36264-36310 | 39 | `chapters/volcengine/ark/13.1 分词 API.md` |
| 14.1.1 | 获取临时 API Key | 1119-1120 | 36313-36349 | 26 | `chapters/volcengine/ark/14.1.1 获取临时 API Key.md` |
| 14.2.1 | 创建个人版套餐 | 1121-1122 | 36351-36408 | 33 | `chapters/volcengine/ark/14.2.1 创建个人版套餐.md` |
| 14.2.2 | 续费个人版套餐 | 1123-1124 | 36409-36454 | 27 | `chapters/volcengine/ark/14.2.2 续费个人版套餐.md` |
| 14.2.3 | 查询个人版套餐 | 1125 | 36455-36482 | 20 | `chapters/volcengine/ark/14.2.3 查询个人版套餐.md` |
| 14.2.4.1 | 查询 Agent Plan 支持的模型列表 | 1126 | 36484-36503 | 14 | `chapters/volcengine/ark/14.2.4.1 查询 Agent Plan 支持的模型列表.md` |
| 14.2.4.2 | 轮换个人版 API Key | 1127 | 36504-36530 | 17 | `chapters/volcengine/ark/14.2.4.2 轮换个人版 API Key.md` |
| 14.2.4.3 | 获取套餐 AFP 额度 | 1128-1130 | 36531-36607 | 66 | `chapters/volcengine/ark/14.2.4.3 获取套餐 AFP 额度.md` |
| 14.2.4.4 | 获取套餐用量详情 | 1131-1132 | 36608-36656 | 39 | `chapters/volcengine/ark/14.2.4.4 获取套餐用量详情.md` |
| 14.2.5.1 | 查询 Coding Plan 支持的模型列表 | 1133 | 36658-36673 | 12 | `chapters/volcengine/ark/14.2.5.1 查询 Coding Plan 支持的模型列表.md` |
| 14.3.1 | 获取基础模型版本列表 | 1134-1136 | 36675-36762 | 72 | `chapters/volcengine/ark/14.3.1 获取基础模型版本列表.md` |
| 14.3.2 | 获取基础模型版本信息 | 1137-1147 | 36763-37086 | 273 | `chapters/volcengine/ark/14.3.2 获取基础模型版本信息.md` |
| 14.3.3 | 获取基础模型列表 | 1148-1154 | 37087-37335 | 182 | `chapters/volcengine/ark/14.3.3 获取基础模型列表.md` |
| 14.3.4 | 获取基础模型信息 | 1155-1158 | 37336-37462 | 93 | `chapters/volcengine/ark/14.3.4 获取基础模型信息.md` |
| 14.4.1 | 批量开通基础模型 | 1159 | 37464-37478 | 11 | `chapters/volcengine/ark/14.4.1 批量开通基础模型.md` |
| 14.4.2 | 启用自动开通新模型 | 1160 | 37479-37490 | 7 | `chapters/volcengine/ark/14.4.2 启用自动开通新模型.md` |
| 14.4.3 | 关闭自动开通新模型 | 1161 | 37491-37502 | 7 | `chapters/volcengine/ark/14.4.3 关闭自动开通新模型.md` |
| 14.4.4 | 查询模型开通详情 | 1162-1166 | 37503-37647 | 131 | `chapters/volcengine/ark/14.4.4 查询模型开通详情.md` |
| 14.4.5 | 查询模型开通列表 | 1167-1172 | 37648-37827 | 163 | `chapters/volcengine/ark/14.4.5 查询模型开通列表.md` |
| 14.5.1 | 批量开通资源 | 1173 | 37829-37847 | 14 | `chapters/volcengine/ark/14.5.1 批量开通资源.md` |
| 14.5.2 | 查询资源开通列表 | 1174-1177 | 37848-37951 | 92 | `chapters/volcengine/ark/14.5.2 查询资源开通列表.md` |
| 14.6.1 | 查询模型限流 | 1178-1181 | 37953-38054 | 91 | `chapters/volcengine/ark/14.6.1 查询模型限流.md` |
| 14.7.1 | 删除定制模型 | 1182 | 38056-38080 | 16 | `chapters/volcengine/ark/14.7.1 删除定制模型.md` |
| 14.7.2 | 获取定制模型信息 | 1183-1186 | 38081-38191 | 97 | `chapters/volcengine/ark/14.7.2 获取定制模型信息.md` |
| 14.7.3 | 更新定制模型 | 1187-1188 | 38192-38226 | 22 | `chapters/volcengine/ark/14.7.3 更新定制模型.md` |
| 14.7.4 | 获取定制模型列表 | 1189-1192 | 38227-38347 | 102 | `chapters/volcengine/ark/14.7.4 获取定制模型列表.md` |
| 14.8.1 | 创建模型调优任务 | 1193-1203 | 38349-38672 | 279 | `chapters/volcengine/ark/14.8.1 创建模型调优任务.md` |
| 14.8.2 | 删除模型调优任务 | 1204 | 38673-38689 | 10 | `chapters/volcengine/ark/14.8.2 删除模型调优任务.md` |
| 14.8.3 | 获取模型调优任务信息 | 1205-1219 | 38690-39151 | 411 | `chapters/volcengine/ark/14.8.3 获取模型调优任务信息.md` |
| 14.8.4 | 查询精调效果指标详细数据 | 1220-1221 | 39152-39197 | 33 | `chapters/volcengine/ark/14.8.4 查询精调效果指标详细数据.md` |
| 14.8.5 | 查询精调效果指标 | 1222 | 39198-39216 | 10 | `chapters/volcengine/ark/14.8.5 查询精调效果指标.md` |
| 14.8.6 | 获取模型调优任务列表 | 1223-1231 | 39217-39491 | 246 | `chapters/volcengine/ark/14.8.6 获取模型调优任务列表.md` |
| 14.8.7 | 重试模型调优任务 | 1232 | 39492-39508 | 9 | `chapters/volcengine/ark/14.8.7 重试模型调优任务.md` |
| 14.8.8 | 停止模型调优任务 | 1233 | 39509-39525 | 10 | `chapters/volcengine/ark/14.8.8 停止模型调优任务.md` |
| 14.8.9 | 更新模型调优任务 | 1234 | 39526-39549 | 14 | `chapters/volcengine/ark/14.8.9 更新模型调优任务.md` |
| 14.9.1 | 开启推理接入点 | 1235 | 39551-39570 | 13 | `chapters/volcengine/ark/14.9.1 开启推理接入点.md` |
| 14.9.2 | 停止推理接入点 | 1236 | 39571-39591 | 11 | `chapters/volcengine/ark/14.9.2 停止推理接入点.md` |
| 14.9.3 | 获取推理接入点列表 | 1237-1242 | 39592-39804 | 168 | `chapters/volcengine/ark/14.9.3 获取推理接入点列表.md` |
| 14.9.4 | 获取推理接入点 | 1243-1246 | 39805-39908 | 88 | `chapters/volcengine/ark/14.9.4 获取推理接入点.md` |
| 14.9.5 | 删除推理接入点 | 1247 | 39909-39928 | 12 | `chapters/volcengine/ark/14.9.5 删除推理接入点.md` |
| 14.9.6 | 更新推理接入点 | 1248-1253 | 39929-40115 | 160 | `chapters/volcengine/ark/14.9.6 更新推理接入点.md` |
| 14.9.7 | 创建推理接入点 | 1254-1261 | 40116-40346 | 192 | `chapters/volcengine/ark/14.9.7 创建推理接入点.md` |
| 14.9.8 | 获取接入点推理应用层加密证书 | 1262-1263 | 40347-40382 | 23 | `chapters/volcengine/ark/14.9.8 获取接入点推理应用层加密证书.md` |
| 14.9.9 | 创建推理接入点滚动升级任务 | 1264-1265 | 40383-40430 | 41 | `chapters/volcengine/ark/14.9.9 创建推理接入点滚动升级任务.md` |
| 14.9.10 | 查询推理接入点滚动升级详情 | 1266-1270 | 40431-40559 | 116 | `chapters/volcengine/ark/14.9.10 查询推理接入点滚动升级详情.md` |
| 14.9.11 | 回滚推理接入点滚动升级 | 1271 | 40560-40577 | 13 | `chapters/volcengine/ark/14.9.11 回滚推理接入点滚动升级.md` |
| 14.9.12 | 取消推理接入点滚动升级 | 1272 | 40578-40595 | 13 | `chapters/volcengine/ark/14.9.12 取消推理接入点滚动升级.md` |
| 14.10.1 | 创建评测任务 | 1273-1277 | 40597-40762 | 131 | `chapters/volcengine/ark/14.10.1 创建评测任务.md` |
| 14.10.2 | 删除评测任务 | 1278 | 40763-40784 | 13 | `chapters/volcengine/ark/14.10.2 删除评测任务.md` |
| 14.10.3 | 获取评测任务 | 1279-1281 | 40785-40866 | 67 | `chapters/volcengine/ark/14.10.3 获取评测任务.md` |
| 14.10.4 | 获取评测任务结果 | 1282-1285 | 40867-40971 | 87 | `chapters/volcengine/ark/14.10.4 获取评测任务结果.md` |
| 14.10.5 | 获取评测任务列表 | 1286-1290 | 40972-41120 | 129 | `chapters/volcengine/ark/14.10.5 获取评测任务列表.md` |
| 14.10.6 | 获取评测任务结果列表 | 1291-1295 | 41121-41264 | 120 | `chapters/volcengine/ark/14.10.6 获取评测任务结果列表.md` |
| 14.10.7 | 停止评测任务 | 1296 | 41265-41286 | 13 | `chapters/volcengine/ark/14.10.7 停止评测任务.md` |
| 14.10.8 | 更新评测任务 | 1297 | 41287-41312 | 18 | `chapters/volcengine/ark/14.10.8 更新评测任务.md` |
| 14.11.1 | 查询推理用量 | 1298-1300 | 41314-41440 | 75 | `chapters/volcengine/ark/14.11.1 查询推理用量.md` |
| 14.11.2 | 查询单请求用量 | 1301-1305 | 41441-41581 | 124 | `chapters/volcengine/ark/14.11.2 查询单请求用量.md` |
| 14.11.3 | 查询异步任务用量 | 1306-1308 | 41582-41654 | 62 | `chapters/volcengine/ark/14.11.3 查询异步任务用量.md` |
| 14.11.4 | 创建用量明细导出任务 | 1309-1310 | 41655-41709 | 33 | `chapters/volcengine/ark/14.11.4 创建用量明细导出任务.md` |
| 14.11.5 | 查询用量明细导出任务状态 | 1311-1313 | 41710-41812 | 71 | `chapters/volcengine/ark/14.11.5 查询用量明细导出任务状态.md` |
| 14.11.6 | 查询模型推理限额 | 1314 | 41813-41840 | 22 | `chapters/volcengine/ark/14.11.6 查询模型推理限额.md` |
| 14.11.7 | 开启模型推理限额 | 1315 | 41841-41865 | 16 | `chapters/volcengine/ark/14.11.7 开启模型推理限额.md` |
| 14.11.8 | 关闭模型推理限额 | 1316 | 41866-41886 | 12 | `chapters/volcengine/ark/14.11.8 关闭模型推理限额.md` |
| 14.12.1 | 创建方舟官方模型产物查询请求 | 1317 | 41888-41906 | 14 | `chapters/volcengine/ark/14.12.1 创建方舟官方模型产物查询请求.md` |
| 14.12.2 | 获取安全审计日志 | 1318-1321 | 41907-42028 | 85 | `chapters/volcengine/ark/14.12.2 获取安全审计日志.md` |
| 14.12.3 | 获取方舟官方产物确认结果 | 1322-1323 | 42029-42060 | 24 | `chapters/volcengine/ark/14.12.3 获取方舟官方产物确认结果.md` |
| 14.13.1 | 上报视频生成模型效果问题 | 1324-1327 | 42062-42187 | 86 | `chapters/volcengine/ark/14.13.1 上报视频生成模型效果问题.md` |
| 14.13.2 | 查询视频生成模型效果问题结果 | 1328-1331 | 42188-42276 | 69 | `chapters/volcengine/ark/14.13.2 查询视频生成模型效果问题结果.md` |
| 14.13.3 | 上报大语言模型效果问题 | 1332-1334 | 42277-42385 | 81 | `chapters/volcengine/ark/14.13.3 上报大语言模型效果问题.md` |
| 14.13.4 | 查询大语言模型效果问题结果 | 1335-1338 | 42386-42503 | 97 | `chapters/volcengine/ark/14.13.4 查询大语言模型效果问题结果.md` |
| 15.1 | 兼容 OpenAI SDK | 1339-1342 | 42505-42621 | 103 | `chapters/volcengine/ark/15.1 兼容 OpenAI SDK.md` |
| 15.2 | 向后兼容性 | 1343 | 42622-42667 | 25 | `chapters/volcengine/ark/15.2 向后兼容性.md` |
| 15.3 | 错误码 - 第1部分 | 1343-1364 | 42668-44651 | 1936 | `chapters/volcengine/ark/15.3 错误码 - 第1部分.md` |
| 15.3 | 错误码 - 第2部分·错误码 | 1365-1374 | 44652-45426 | 751 | `chapters/volcengine/ark/15.3 错误码 - 第2部分·错误码.md` |
| 15.4 | SDK 常见使用示例 | 1375-1392 | 45427-46108 | 611 | `chapters/volcengine/ark/15.4 SDK 常见使用示例.md` |
