# 方舟 API 区章节表（ark）

来源：《火山方舟 API 参考》（1392 页）。199 个章节文件，接口级切分：一个接口/任务一个文件；超过 1500 行的按语义块自动再拆为`… - 第N部分`（5 个章节被拆分）。

「页码」是原 PDF 页码范围；「行范围」是中间 MD（`doc/<源文档>.md`）的 1 起始行号，可据此回查原文。章节文件本身已去掉页眉页脚，回查 PDF 时用这两列。文件名即章节标题，日常定位直接 Glob 文件名即可，用不到这两列。

**这张表用来 grep，不要整读。**

| 编号 | 标题 | 页码 | 行范围(源文件) | 行数 | 文件 |
|------|------|------|---------------|------|------|
| 1.1 | 获取 API Key 并配置 | 1 | 278-312 | 19 | `chapters/volcengine/ark/1.1 获取 API Key 并配置.md` |
| 1.2 | 安装及升级 SDK | 2-7 | 313-468 | 115 | `chapters/volcengine/ark/1.2 安装及升级 SDK.md` |
| 1.3 | Base URL及鉴权 | 8-10 | 469-564 | 68 | `chapters/volcengine/ark/1.3 Base URL及鉴权.md` |
| 2.1 | 对话(Chat) API | 11-42 | 566-1767 | 891 | `chapters/volcengine/ark/2.1 对话(Chat) API.md` |
| 3.1 | 创建 Response - 第1部分 | 43-91 | 1768-3455 | 1428 | `chapters/volcengine/ark/3.1 创建 Response - 第1部分.md` |
| 3.1 | 创建 Response - 第2部分·响应参数 | 92-134 | 3456-4841 | 1211 | `chapters/volcengine/ark/3.1 创建 Response - 第2部分·响应参数.md` |
| 3.2 | 查询 Response 详情 | 135-171 | 4842-5996 | 1062 | `chapters/volcengine/ark/3.2 查询 Response 详情.md` |
| 3.3 | 查询 Response 输入项列表 | 172-200 | 5997-6909 | 831 | `chapters/volcengine/ark/3.3 查询 Response 输入项列表.md` |
| 3.4 | 删除 Response | 201 | 6910-6933 | 19 | `chapters/volcengine/ark/3.4 删除 Response.md` |
| 3.5.1 | Response 生命周期 - 第1部分 | 202-253 | 6934-8644 | 1505 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第1部分.md` |
| 3.5.1 | Response 生命周期 - 第2部分 | 254-304 | 8645-10329 | 1479 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第2部分.md` |
| 3.5.1 | Response 生命周期 - 第3部分 | 305-356 | 10330-12034 | 1502 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第3部分.md` |
| 3.5.1 | Response 生命周期 - 第4部分 | 357-415 | 12035-14012 | 1719 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第4部分.md` |
| 3.5.2 | Output Item 与文本回答 - 第1部分 | 416-466 | 14013-15643 | 1470 | `chapters/volcengine/ark/3.5.2 Output Item 与文本回答 - 第1部分.md` |
| 3.5.2 | Output Item 与文本回答 - 第2部分 | 467-487 | 15644-16271 | 586 | `chapters/volcengine/ark/3.5.2 Output Item 与文本回答 - 第2部分.md` |
| 3.5.3 | 工具调用事件 | 488-524 | 16272-17372 | 1024 | `chapters/volcengine/ark/3.5.3 工具调用事件.md` |
| 3.5.4 | 语音转写与错误事件 | 525-530 | 17373-17545 | 161 | `chapters/volcengine/ark/3.5.4 语音转写与错误事件.md` |
| 4.1 | 创建 Message | 531-550 | 17547-18203 | 569 | `chapters/volcengine/ark/4.1 创建 Message.md` |
| 4.2 | 统计 Messages 请求 token 数 | 551-560 | 18204-18540 | 278 | `chapters/volcengine/ark/4.2 统计 Messages 请求 token 数.md` |
| 5.1 | System One API（beta） | 561-569 | 18542-18816 | 240 | `chapters/volcengine/ark/5.1 System One API（beta）.md` |
| 6.1 | 上传文件 | 570-575 | 18818-19029 | 157 | `chapters/volcengine/ark/6.1 上传文件.md` |
| 6.2 | 查询文件详情 | 576-578 | 19030-19103 | 63 | `chapters/volcengine/ark/6.2 查询文件详情.md` |
| 6.3 | 查询文件列表 | 579-582 | 19104-19238 | 112 | `chapters/volcengine/ark/6.3 查询文件列表.md` |
| 6.4 | 删除文件 | 583 | 19239-19261 | 19 | `chapters/volcengine/ark/6.4 删除文件.md` |
| 6.5 | The file object | 584-586 | 19262-19333 | 57 | `chapters/volcengine/ark/6.5 The file object.md` |
| 7.1 | 创建视频生成任务 | 587-604 | 19335-20199 | 600 | `chapters/volcengine/ark/7.1 创建视频生成任务.md` |
| 7.2 | 查询视频生成任务 | 605-609 | 20200-20354 | 112 | `chapters/volcengine/ark/7.2 查询视频生成任务.md` |
| 7.3 | 查询视频生成任务列表 | 610-615 | 20355-20574 | 164 | `chapters/volcengine/ark/7.3 查询视频生成任务列表.md` |
| 7.4 | 取消或删除视频生成任务 | 616 | 20575-20616 | 38 | `chapters/volcengine/ark/7.4 取消或删除视频生成任务.md` |
| 8.1 | 图片生成 API | 617-634 | 20618-21365 | 520 | `chapters/volcengine/ark/8.1 图片生成 API.md` |
| 8.2 | 图片生成流式响应事件 | 635-640 | 21366-21544 | 156 | `chapters/volcengine/ark/8.2 图片生成流式响应事件.md` |
| 9.1.1 | 创建 3D 生成任务 API | 641-643 | 21547-21650 | 80 | `chapters/volcengine/ark/9.1.1 创建 3D 生成任务 API.md` |
| 9.1.2 | 查询 3D 生成任务 API | 644-645 | 21651-21720 | 52 | `chapters/volcengine/ark/9.1.2 查询 3D 生成任务 API.md` |
| 9.1.3 | 查询 3D 生成任务列表 | 646-649 | 21721-21836 | 87 | `chapters/volcengine/ark/9.1.3 查询 3D 生成任务列表.md` |
| 9.1.4 | 取消或删除 3D 生成任务 | 650 | 21837-21878 | 38 | `chapters/volcengine/ark/9.1.4 取消或删除 3D 生成任务.md` |
| 9.2.1 | 创建3D生成任务 | 651-655 | 21880-22094 | 148 | `chapters/volcengine/ark/9.2.1 创建3D生成任务.md` |
| 9.2.2 | 查询3D生成任务 | 656-657 | 22095-22160 | 48 | `chapters/volcengine/ark/9.2.2 查询3D生成任务.md` |
| 9.2.3 | 查询3D生成任务列表 | 658-660 | 22161-22268 | 81 | `chapters/volcengine/ark/9.2.3 查询3D生成任务列表.md` |
| 9.2.4 | 取消或删除3D生成任务 | 661 | 22269-22303 | 31 | `chapters/volcengine/ark/9.2.4 取消或删除3D生成任务.md` |
| 9.3.1 | 创建3D生成任务 | 662-665 | 22305-22436 | 95 | `chapters/volcengine/ark/9.3.1 创建3D生成任务.md` |
| 9.3.2 | 查询3D生成任务 | 666-667 | 22437-22502 | 48 | `chapters/volcengine/ark/9.3.2 查询3D生成任务.md` |
| 9.3.3 | 查询3D生成任务列表 | 668-670 | 22503-22610 | 81 | `chapters/volcengine/ark/9.3.3 查询3D生成任务列表.md` |
| 9.3.4 | 取消或删除3D生成任务 | 671 | 22611-22645 | 31 | `chapters/volcengine/ark/9.3.4 取消或删除3D生成任务.md` |
| 10.1 | 多模态向量化 API | 672-677 | 22647-22846 | 145 | `chapters/volcengine/ark/10.1 多模态向量化 API.md` |
| 11.1.1 | 创建智能体 | 678-691 | 22849-23339 | 375 | `chapters/volcengine/ark/11.1.1 创建智能体.md` |
| 11.1.2 | 查询智能体列表 | 692-699 | 23340-23600 | 215 | `chapters/volcengine/ark/11.1.2 查询智能体列表.md` |
| 11.1.3 | 查询智能体详情 | 700-706 | 23601-23824 | 180 | `chapters/volcengine/ark/11.1.3 查询智能体详情.md` |
| 11.1.4 | 更新智能体 | 707-720 | 23825-24360 | 387 | `chapters/volcengine/ark/11.1.4 更新智能体.md` |
| 11.1.5 | 删除智能体 | 721 | 24361-24381 | 14 | `chapters/volcengine/ark/11.1.5 删除智能体.md` |
| 11.1.6 | 查询智能体版本列表 | 722-729 | 24382-24631 | 202 | `chapters/volcengine/ark/11.1.6 查询智能体版本列表.md` |
| 11.2.1 | 创建环境 | 730-735 | 24633-24811 | 145 | `chapters/volcengine/ark/11.2.1 创建环境.md` |
| 11.2.2 | 查询环境列表 | 736-739 | 24812-24918 | 95 | `chapters/volcengine/ark/11.2.2 查询环境列表.md` |
| 11.2.3 | 查询环境详情 | 740-742 | 24919-25006 | 76 | `chapters/volcengine/ark/11.2.3 查询环境详情.md` |
| 11.2.4 | 更新环境 | 743-748 | 25007-25208 | 155 | `chapters/volcengine/ark/11.2.4 更新环境.md` |
| 11.2.5 | 删除环境 | 749 | 25209-25231 | 17 | `chapters/volcengine/ark/11.2.5 删除环境.md` |
| 11.2.6.1 | 长轮询拉取待执行 Work | 750-752 | 25233-25323 | 68 | `chapters/volcengine/ark/11.2.6.1 长轮询拉取待执行 Work.md` |
| 11.2.6.2 | 认领 Work | 753-755 | 25324-25396 | 56 | `chapters/volcengine/ark/11.2.6.2 认领 Work.md` |
| 11.2.6.3 | 续租 Work | 756-757 | 25397-25452 | 41 | `chapters/volcengine/ark/11.2.6.3 续租 Work.md` |
| 11.2.6.4 | 查询 Work 队列状态 | 758 | 25453-25485 | 23 | `chapters/volcengine/ark/11.2.6.4 查询 Work 队列状态.md` |
| 11.2.6.5 | 停止 Work | 759-761 | 25486-25558 | 56 | `chapters/volcengine/ark/11.2.6.5 停止 Work.md` |
| 11.2.6.6 | 查询 Work 列表 | 762-764 | 25559-25651 | 76 | `chapters/volcengine/ark/11.2.6.6 查询 Work 列表.md` |
| 11.2.6.7 | 查询 Work 详情 | 765-766 | 25652-25709 | 46 | `chapters/volcengine/ark/11.2.6.7 查询 Work 详情.md` |
| 11.3.1 | 创建会话 | 767-797 | 25711-26761 | 844 | `chapters/volcengine/ark/11.3.1 创建会话.md` |
| 11.3.2 | 查询会话列表 | 798-817 | 26762-27408 | 561 | `chapters/volcengine/ark/11.3.2 查询会话列表.md` |
| 11.3.3 | 查询会话详情 | 818-836 | 27409-28011 | 523 | `chapters/volcengine/ark/11.3.3 查询会话详情.md` |
| 11.3.4 | 更新会话标题和标签 | 837-855 | 28012-28626 | 529 | `chapters/volcengine/ark/11.3.4 更新会话标题和标签.md` |
| 11.3.5 | 升级会话 | 856-881 | 28627-29506 | 747 | `chapters/volcengine/ark/11.3.5 升级会话.md` |
| 11.3.6 | 删除会话 | 882 | 29507-29533 | 20 | `chapters/volcengine/ark/11.3.6 删除会话.md` |
| 11.3.7.1 | 发送会话事件 | 883-884 | 29535-29581 | 33 | `chapters/volcengine/ark/11.3.7.1 发送会话事件.md` |
| 11.3.7.2 | 查询会话事件列表 | 885-887 | 29582-29648 | 50 | `chapters/volcengine/ark/11.3.7.2 查询会话事件列表.md` |
| 11.3.7.3 | 流式获取会话事件 | 888-889 | 29649-29709 | 34 | `chapters/volcengine/ark/11.3.7.3 流式获取会话事件.md` |
| 11.3.7.4 | 会话事件结构参考 - 第1部分 | 890-948 | 29710-31530 | 1649 | `chapters/volcengine/ark/11.3.7.4 会话事件结构参考 - 第1部分.md` |
| 11.3.8.1 | 添加会话资源 | 949-950 | 31532-31582 | 37 | `chapters/volcengine/ark/11.3.8.1 添加会话资源.md` |
| 11.3.8.2 | 查询会话资源列表 | 951-954 | 31583-31679 | 88 | `chapters/volcengine/ark/11.3.8.2 查询会话资源列表.md` |
| 11.3.8.3 | 查询会话资源 | 955-956 | 31680-31724 | 36 | `chapters/volcengine/ark/11.3.8.3 查询会话资源.md` |
| 11.3.9.1 | 查询线程列表 | 957-959 | 31726-31795 | 56 | `chapters/volcengine/ark/11.3.9.1 查询线程列表.md` |
| 11.3.9.2 | 查询线程详情 | 960-961 | 31796-31844 | 37 | `chapters/volcengine/ark/11.3.9.2 查询线程详情.md` |
| 11.3.9.3 | 查询线程事件列表 | 962-963 | 31845-31906 | 46 | `chapters/volcengine/ark/11.3.9.3 查询线程事件列表.md` |
| 11.3.9.4 | 流式获取线程事件 | 964-965 | 31907-31955 | 29 | `chapters/volcengine/ark/11.3.9.4 流式获取线程事件.md` |
| 11.4.1 | 创建保管库 | 966-967 | 31957-32003 | 36 | `chapters/volcengine/ark/11.4.1 创建保管库.md` |
| 11.4.2 | 查询保管库列表 | 968-969 | 32004-32072 | 55 | `chapters/volcengine/ark/11.4.2 查询保管库列表.md` |
| 11.4.3 | 查询保管库详情 | 970 | 32073-32099 | 24 | `chapters/volcengine/ark/11.4.3 查询保管库详情.md` |
| 11.4.4 | 更新保管库 | 971-972 | 32100-32141 | 33 | `chapters/volcengine/ark/11.4.4 更新保管库.md` |
| 11.4.5 | 删除保管库 | 973 | 32142-32166 | 21 | `chapters/volcengine/ark/11.4.5 删除保管库.md` |
| 11.4.6.1 | 创建凭证 | 974-986 | 32168-32636 | 358 | `chapters/volcengine/ark/11.4.6.1 创建凭证.md` |
| 11.4.6.2 | 查询凭证列表 | 987-993 | 32637-32861 | 182 | `chapters/volcengine/ark/11.4.6.2 查询凭证列表.md` |
| 11.4.6.3 | 查询凭证详情 | 994-999 | 32862-33058 | 160 | `chapters/volcengine/ark/11.4.6.3 查询凭证详情.md` |
| 11.4.6.4 | 更新凭证 | 1000-1012 | 33059-33501 | 334 | `chapters/volcengine/ark/11.4.6.4 更新凭证.md` |
| 11.4.6.5 | 删除凭证 | 1013 | 33502-33528 | 21 | `chapters/volcengine/ark/11.4.6.5 删除凭证.md` |
| 11.5.1 | 创建记忆库 | 1014-1016 | 33530-33609 | 61 | `chapters/volcengine/ark/11.5.1 创建记忆库.md` |
| 11.5.2 | 查询记忆库列表 | 1017-1020 | 33610-33714 | 80 | `chapters/volcengine/ark/11.5.2 查询记忆库列表.md` |
| 11.5.3 | 查询记忆库详情 | 1021-1022 | 33715-33776 | 47 | `chapters/volcengine/ark/11.5.3 查询记忆库详情.md` |
| 11.5.4 | 更新记忆库 | 1023-1025 | 33777-33857 | 61 | `chapters/volcengine/ark/11.5.4 更新记忆库.md` |
| 11.5.5 | 删除记忆库 | 1026 | 33858-33883 | 18 | `chapters/volcengine/ark/11.5.5 删除记忆库.md` |
| 11.5.6.1 | 创建记忆 | 1027-1029 | 33885-33951 | 51 | `chapters/volcengine/ark/11.5.6.1 创建记忆.md` |
| 11.5.6.2 | 批量创建记忆 | 1030-1033 | 33952-34071 | 90 | `chapters/volcengine/ark/11.5.6.2 批量创建记忆.md` |
| 11.5.6.3 | 查询记忆列表 | 1034-1036 | 34072-34165 | 70 | `chapters/volcengine/ark/11.5.6.3 查询记忆列表.md` |
| 11.5.6.4 | 查询记忆详情 | 1037-1038 | 34166-34224 | 45 | `chapters/volcengine/ark/11.5.6.4 查询记忆详情.md` |
| 11.5.6.5 | 更新记忆 | 1039-1041 | 34225-34299 | 52 | `chapters/volcengine/ark/11.5.6.5 更新记忆.md` |
| 11.5.6.6 | 删除记忆 | 1042 | 34300-34327 | 18 | `chapters/volcengine/ark/11.5.6.6 删除记忆.md` |
| 11.6.1 | 创建 Dream | 1043-1046 | 34329-34453 | 108 | `chapters/volcengine/ark/11.6.1 创建 Dream.md` |
| 11.6.2 | 查询 Dream 列表 | 1047-1051 | 34454-34593 | 119 | `chapters/volcengine/ark/11.6.2 查询 Dream 列表.md` |
| 11.6.3 | 查询 Dream | 1052-1054 | 34594-34689 | 83 | `chapters/volcengine/ark/11.6.3 查询 Dream.md` |
| 11.6.4 | 取消 Dream | 1055-1058 | 34690-34790 | 84 | `chapters/volcengine/ark/11.6.4 取消 Dream.md` |
| 11.7.1 | 创建技能 | 1059-1060 | 34792-34860 | 49 | `chapters/volcengine/ark/11.7.1 创建技能.md` |
| 11.7.2 | 查询技能列表 | 1061-1063 | 34861-34937 | 61 | `chapters/volcengine/ark/11.7.2 查询技能列表.md` |
| 11.7.3 | 查询技能详情 | 1064-1065 | 34938-34983 | 36 | `chapters/volcengine/ark/11.7.3 查询技能详情.md` |
| 11.7.4 | 设置技能内容保护 | 1066-1067 | 34984-35029 | 37 | `chapters/volcengine/ark/11.7.4 设置技能内容保护.md` |
| 11.7.5 | 删除技能 | 1068 | 35030-35055 | 18 | `chapters/volcengine/ark/11.7.5 删除技能.md` |
| 11.7.6 | 创建新版本的技能 | 1069-1070 | 35056-35115 | 41 | `chapters/volcengine/ark/11.7.6 创建新版本的技能.md` |
| 11.7.7 | 查询技能的版本列表 | 1071-1072 | 35116-35171 | 48 | `chapters/volcengine/ark/11.7.7 查询技能的版本列表.md` |
| 11.7.8 | 查询指定版本的技能 | 1073-1074 | 35172-35203 | 26 | `chapters/volcengine/ark/11.7.8 查询指定版本的技能.md` |
| 11.7.9 | 删除指定版本的技能 | 1075 | 35204-35225 | 17 | `chapters/volcengine/ark/11.7.9 删除指定版本的技能.md` |
| 11.7.10 | 下载指定版本的技能 | 1076 | 35226-35244 | 14 | `chapters/volcengine/ark/11.7.10 下载指定版本的技能.md` |
| 11.7.11 | 扫描 GitHub 技能 | 1077-1078 | 35245-35297 | 43 | `chapters/volcengine/ark/11.7.11 扫描 GitHub 技能.md` |
| 11.7.12 | 导入 GitHub 技能 | 1079-1081 | 35298-35375 | 58 | `chapters/volcengine/ark/11.7.12 导入 GitHub 技能.md` |
| 12.1.1 | 创建批量推理任务 | 1082-1085 | 35378-35458 | 60 | `chapters/volcengine/ark/12.1.1 创建批量推理任务.md` |
| 12.1.2 | 获取批量推理任务列表 | 1086-1091 | 35459-35634 | 152 | `chapters/volcengine/ark/12.1.2 获取批量推理任务列表.md` |
| 12.1.3 | 获取批量推理任务 | 1092-1095 | 35635-35754 | 100 | `chapters/volcengine/ark/12.1.3 获取批量推理任务.md` |
| 12.1.4 | 更新批量推理任务 | 1096 | 35755-35778 | 17 | `chapters/volcengine/ark/12.1.4 更新批量推理任务.md` |
| 12.1.5 | 删除批量推理任务 | 1097 | 35779-35798 | 13 | `chapters/volcengine/ark/12.1.5 删除批量推理任务.md` |
| 12.1.6 | 停止批量推理任务 | 1098 | 35799-35821 | 14 | `chapters/volcengine/ark/12.1.6 停止批量推理任务.md` |
| 12.1.7 | 重启批量推理任务 | 1099 | 35822-35842 | 13 | `chapters/volcengine/ark/12.1.7 重启批量推理任务.md` |
| 12.2 | 批量(Chat) API | 1100-1117 | 35843-36311 | 352 | `chapters/volcengine/ark/12.2 批量(Chat) API.md` |
| 13.1 | 分词 API | 1118-1119 | 36313-36359 | 39 | `chapters/volcengine/ark/13.1 分词 API.md` |
| 14.1.1 | 获取临时 API Key | 1120-1121 | 36362-36398 | 26 | `chapters/volcengine/ark/14.1.1 获取临时 API Key.md` |
| 14.2.1 | 创建个人版套餐 | 1122-1123 | 36400-36457 | 33 | `chapters/volcengine/ark/14.2.1 创建个人版套餐.md` |
| 14.2.2 | 续费个人版套餐 | 1124-1125 | 36458-36503 | 27 | `chapters/volcengine/ark/14.2.2 续费个人版套餐.md` |
| 14.2.3 | 查询个人版套餐 | 1126 | 36504-36531 | 20 | `chapters/volcengine/ark/14.2.3 查询个人版套餐.md` |
| 14.2.4.1 | 查询 Agent Plan 支持的模型列表 | 1127 | 36533-36552 | 14 | `chapters/volcengine/ark/14.2.4.1 查询 Agent Plan 支持的模型列表.md` |
| 14.2.4.2 | 轮换个人版 API Key | 1128 | 36553-36579 | 17 | `chapters/volcengine/ark/14.2.4.2 轮换个人版 API Key.md` |
| 14.2.4.3 | 获取套餐 AFP 额度 | 1129-1131 | 36580-36656 | 66 | `chapters/volcengine/ark/14.2.4.3 获取套餐 AFP 额度.md` |
| 14.2.4.4 | 获取套餐用量详情 | 1132-1133 | 36657-36705 | 39 | `chapters/volcengine/ark/14.2.4.4 获取套餐用量详情.md` |
| 14.2.5.1 | 查询 Coding Plan 支持的模型列表 | 1134 | 36707-36722 | 12 | `chapters/volcengine/ark/14.2.5.1 查询 Coding Plan 支持的模型列表.md` |
| 14.3.1 | 获取基础模型版本列表 | 1135-1137 | 36724-36811 | 72 | `chapters/volcengine/ark/14.3.1 获取基础模型版本列表.md` |
| 14.3.2 | 获取基础模型版本信息 | 1138-1148 | 36812-37135 | 273 | `chapters/volcengine/ark/14.3.2 获取基础模型版本信息.md` |
| 14.3.3 | 获取基础模型列表 | 1149-1154 | 37136-37390 | 186 | `chapters/volcengine/ark/14.3.3 获取基础模型列表.md` |
| 14.3.4 | 获取基础模型信息 | 1155-1158 | 37391-37517 | 93 | `chapters/volcengine/ark/14.3.4 获取基础模型信息.md` |
| 14.4.1 | 批量开通基础模型 | 1159 | 37519-37533 | 11 | `chapters/volcengine/ark/14.4.1 批量开通基础模型.md` |
| 14.4.2 | 启用自动开通新模型 | 1160 | 37534-37545 | 7 | `chapters/volcengine/ark/14.4.2 启用自动开通新模型.md` |
| 14.4.3 | 关闭自动开通新模型 | 1161 | 37546-37557 | 7 | `chapters/volcengine/ark/14.4.3 关闭自动开通新模型.md` |
| 14.4.4 | 查询模型开通详情 | 1162-1166 | 37558-37702 | 131 | `chapters/volcengine/ark/14.4.4 查询模型开通详情.md` |
| 14.4.5 | 查询模型开通列表 | 1167-1172 | 37703-37882 | 163 | `chapters/volcengine/ark/14.4.5 查询模型开通列表.md` |
| 14.5.1 | 批量开通资源 | 1173 | 37884-37902 | 14 | `chapters/volcengine/ark/14.5.1 批量开通资源.md` |
| 14.5.2 | 查询资源开通列表 | 1174-1177 | 37903-38006 | 92 | `chapters/volcengine/ark/14.5.2 查询资源开通列表.md` |
| 14.6.1 | 查询模型限流 | 1178-1181 | 38008-38109 | 91 | `chapters/volcengine/ark/14.6.1 查询模型限流.md` |
| 14.7.1 | 删除定制模型 | 1182 | 38111-38135 | 16 | `chapters/volcengine/ark/14.7.1 删除定制模型.md` |
| 14.7.2 | 获取定制模型信息 | 1183-1186 | 38136-38246 | 97 | `chapters/volcengine/ark/14.7.2 获取定制模型信息.md` |
| 14.7.3 | 更新定制模型 | 1187-1188 | 38247-38281 | 22 | `chapters/volcengine/ark/14.7.3 更新定制模型.md` |
| 14.7.4 | 获取定制模型列表 | 1189-1192 | 38282-38402 | 102 | `chapters/volcengine/ark/14.7.4 获取定制模型列表.md` |
| 14.8.1 | 创建模型调优任务 | 1193-1203 | 38404-38727 | 279 | `chapters/volcengine/ark/14.8.1 创建模型调优任务.md` |
| 14.8.2 | 删除模型调优任务 | 1204 | 38728-38744 | 10 | `chapters/volcengine/ark/14.8.2 删除模型调优任务.md` |
| 14.8.3 | 获取模型调优任务信息 | 1205-1219 | 38745-39206 | 411 | `chapters/volcengine/ark/14.8.3 获取模型调优任务信息.md` |
| 14.8.4 | 查询精调效果指标详细数据 | 1220-1221 | 39207-39252 | 33 | `chapters/volcengine/ark/14.8.4 查询精调效果指标详细数据.md` |
| 14.8.5 | 查询精调效果指标 | 1222 | 39253-39271 | 10 | `chapters/volcengine/ark/14.8.5 查询精调效果指标.md` |
| 14.8.6 | 获取模型调优任务列表 | 1223-1231 | 39272-39546 | 246 | `chapters/volcengine/ark/14.8.6 获取模型调优任务列表.md` |
| 14.8.7 | 重试模型调优任务 | 1232 | 39547-39563 | 9 | `chapters/volcengine/ark/14.8.7 重试模型调优任务.md` |
| 14.8.8 | 停止模型调优任务 | 1233 | 39564-39580 | 10 | `chapters/volcengine/ark/14.8.8 停止模型调优任务.md` |
| 14.8.9 | 更新模型调优任务 | 1234 | 39581-39604 | 14 | `chapters/volcengine/ark/14.8.9 更新模型调优任务.md` |
| 14.9.1 | 开启推理接入点 | 1235 | 39606-39625 | 13 | `chapters/volcengine/ark/14.9.1 开启推理接入点.md` |
| 14.9.2 | 停止推理接入点 | 1236 | 39626-39646 | 11 | `chapters/volcengine/ark/14.9.2 停止推理接入点.md` |
| 14.9.3 | 获取推理接入点列表 | 1237-1242 | 39647-39859 | 168 | `chapters/volcengine/ark/14.9.3 获取推理接入点列表.md` |
| 14.9.4 | 获取推理接入点 | 1243-1246 | 39860-39963 | 88 | `chapters/volcengine/ark/14.9.4 获取推理接入点.md` |
| 14.9.5 | 删除推理接入点 | 1247 | 39964-39983 | 12 | `chapters/volcengine/ark/14.9.5 删除推理接入点.md` |
| 14.9.6 | 更新推理接入点 | 1248-1253 | 39984-40170 | 160 | `chapters/volcengine/ark/14.9.6 更新推理接入点.md` |
| 14.9.7 | 创建推理接入点 | 1254-1261 | 40171-40401 | 192 | `chapters/volcengine/ark/14.9.7 创建推理接入点.md` |
| 14.9.8 | 获取接入点推理应用层加密证书 | 1262-1263 | 40402-40437 | 23 | `chapters/volcengine/ark/14.9.8 获取接入点推理应用层加密证书.md` |
| 14.9.9 | 创建推理接入点滚动升级任务 | 1264-1265 | 40438-40485 | 41 | `chapters/volcengine/ark/14.9.9 创建推理接入点滚动升级任务.md` |
| 14.9.10 | 查询推理接入点滚动升级详情 | 1266-1270 | 40486-40614 | 116 | `chapters/volcengine/ark/14.9.10 查询推理接入点滚动升级详情.md` |
| 14.9.11 | 回滚推理接入点滚动升级 | 1271 | 40615-40632 | 13 | `chapters/volcengine/ark/14.9.11 回滚推理接入点滚动升级.md` |
| 14.9.12 | 取消推理接入点滚动升级 | 1272 | 40633-40650 | 13 | `chapters/volcengine/ark/14.9.12 取消推理接入点滚动升级.md` |
| 14.10.1 | 创建评测任务 | 1273-1277 | 40652-40817 | 131 | `chapters/volcengine/ark/14.10.1 创建评测任务.md` |
| 14.10.2 | 删除评测任务 | 1278 | 40818-40839 | 13 | `chapters/volcengine/ark/14.10.2 删除评测任务.md` |
| 14.10.3 | 获取评测任务 | 1279-1281 | 40840-40921 | 67 | `chapters/volcengine/ark/14.10.3 获取评测任务.md` |
| 14.10.4 | 获取评测任务结果 | 1282-1285 | 40922-41026 | 87 | `chapters/volcengine/ark/14.10.4 获取评测任务结果.md` |
| 14.10.5 | 获取评测任务列表 | 1286-1290 | 41027-41175 | 129 | `chapters/volcengine/ark/14.10.5 获取评测任务列表.md` |
| 14.10.6 | 获取评测任务结果列表 | 1291-1295 | 41176-41319 | 120 | `chapters/volcengine/ark/14.10.6 获取评测任务结果列表.md` |
| 14.10.7 | 停止评测任务 | 1296 | 41320-41341 | 13 | `chapters/volcengine/ark/14.10.7 停止评测任务.md` |
| 14.10.8 | 更新评测任务 | 1297 | 41342-41367 | 18 | `chapters/volcengine/ark/14.10.8 更新评测任务.md` |
| 14.11.1 | 查询推理用量 | 1298-1300 | 41369-41495 | 75 | `chapters/volcengine/ark/14.11.1 查询推理用量.md` |
| 14.11.2 | 查询单请求用量 | 1301-1305 | 41496-41636 | 124 | `chapters/volcengine/ark/14.11.2 查询单请求用量.md` |
| 14.11.3 | 查询异步任务用量 | 1306-1308 | 41637-41709 | 62 | `chapters/volcengine/ark/14.11.3 查询异步任务用量.md` |
| 14.11.4 | 创建用量明细导出任务 | 1309-1310 | 41710-41764 | 33 | `chapters/volcengine/ark/14.11.4 创建用量明细导出任务.md` |
| 14.11.5 | 查询用量明细导出任务状态 | 1311-1313 | 41765-41867 | 71 | `chapters/volcengine/ark/14.11.5 查询用量明细导出任务状态.md` |
| 14.11.6 | 查询模型推理限额 | 1314 | 41868-41895 | 22 | `chapters/volcengine/ark/14.11.6 查询模型推理限额.md` |
| 14.11.7 | 开启模型推理限额 | 1315 | 41896-41920 | 16 | `chapters/volcengine/ark/14.11.7 开启模型推理限额.md` |
| 14.11.8 | 关闭模型推理限额 | 1316 | 41921-41941 | 12 | `chapters/volcengine/ark/14.11.8 关闭模型推理限额.md` |
| 14.12.1 | 创建方舟官方模型产物查询请求 | 1317 | 41943-41961 | 14 | `chapters/volcengine/ark/14.12.1 创建方舟官方模型产物查询请求.md` |
| 14.12.2 | 获取安全审计日志 | 1318-1321 | 41962-42083 | 85 | `chapters/volcengine/ark/14.12.2 获取安全审计日志.md` |
| 14.12.3 | 获取方舟官方产物确认结果 | 1322-1323 | 42084-42115 | 24 | `chapters/volcengine/ark/14.12.3 获取方舟官方产物确认结果.md` |
| 14.13.1 | 上报视频生成模型效果问题 | 1324-1327 | 42117-42242 | 86 | `chapters/volcengine/ark/14.13.1 上报视频生成模型效果问题.md` |
| 14.13.2 | 查询视频生成模型效果问题结果 | 1328-1331 | 42243-42331 | 69 | `chapters/volcengine/ark/14.13.2 查询视频生成模型效果问题结果.md` |
| 14.13.3 | 上报大语言模型效果问题 | 1332-1334 | 42332-42440 | 81 | `chapters/volcengine/ark/14.13.3 上报大语言模型效果问题.md` |
| 14.13.4 | 查询大语言模型效果问题结果 | 1335-1338 | 42441-42558 | 97 | `chapters/volcengine/ark/14.13.4 查询大语言模型效果问题结果.md` |
| 15.1 | 兼容 OpenAI SDK | 1339-1342 | 42560-42676 | 103 | `chapters/volcengine/ark/15.1 兼容 OpenAI SDK.md` |
| 15.2 | 向后兼容性 | 1343 | 42677-42722 | 25 | `chapters/volcengine/ark/15.2 向后兼容性.md` |
| 15.3 | 错误码 - 第1部分 | 1343-1364 | 42723-44706 | 1936 | `chapters/volcengine/ark/15.3 错误码 - 第1部分.md` |
| 15.3 | 错误码 - 第2部分·错误码 | 1365-1374 | 44707-45481 | 751 | `chapters/volcengine/ark/15.3 错误码 - 第2部分·错误码.md` |
| 15.4 | SDK 常见使用示例 | 1375-1392 | 45482-46163 | 611 | `chapters/volcengine/ark/15.4 SDK 常见使用示例.md` |
