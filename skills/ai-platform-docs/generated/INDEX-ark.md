# 方舟 API 区章节表（ark）

来源：《火山方舟 API 参考》（1393 页）。199 个章节文件，接口级切分：一个接口/任务一个文件；超过 1500 行的按语义块自动再拆为`… - 第N部分`（5 个章节被拆分）。

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
| 11.1.1 | 创建智能体 | 678-691 | 22849-23340 | 371 | `chapters/volcengine/ark/11.1.1 创建智能体.md` |
| 11.1.2 | 查询智能体列表 | 692-699 | 23341-23601 | 215 | `chapters/volcengine/ark/11.1.2 查询智能体列表.md` |
| 11.1.3 | 查询智能体详情 | 700-706 | 23602-23825 | 180 | `chapters/volcengine/ark/11.1.3 查询智能体详情.md` |
| 11.1.4 | 更新智能体 | 707-721 | 23826-24365 | 389 | `chapters/volcengine/ark/11.1.4 更新智能体.md` |
| 11.1.5 | 删除智能体 | 722 | 24366-24386 | 14 | `chapters/volcengine/ark/11.1.5 删除智能体.md` |
| 11.1.6 | 查询智能体版本列表 | 723-730 | 24387-24636 | 202 | `chapters/volcengine/ark/11.1.6 查询智能体版本列表.md` |
| 11.2.1 | 创建环境 | 731-736 | 24638-24827 | 154 | `chapters/volcengine/ark/11.2.1 创建环境.md` |
| 11.2.2 | 查询环境列表 | 737-740 | 24828-24937 | 99 | `chapters/volcengine/ark/11.2.2 查询环境列表.md` |
| 11.2.3 | 查询环境详情 | 741-743 | 24938-25028 | 80 | `chapters/volcengine/ark/11.2.3 查询环境详情.md` |
| 11.2.4 | 更新环境 | 744-749 | 25029-25236 | 164 | `chapters/volcengine/ark/11.2.4 更新环境.md` |
| 11.2.5 | 删除环境 | 750 | 25237-25259 | 17 | `chapters/volcengine/ark/11.2.5 删除环境.md` |
| 11.2.6.1 | 长轮询拉取待执行 Work | 751-753 | 25261-25351 | 68 | `chapters/volcengine/ark/11.2.6.1 长轮询拉取待执行 Work.md` |
| 11.2.6.2 | 认领 Work | 754-756 | 25352-25424 | 56 | `chapters/volcengine/ark/11.2.6.2 认领 Work.md` |
| 11.2.6.3 | 续租 Work | 757-758 | 25425-25480 | 41 | `chapters/volcengine/ark/11.2.6.3 续租 Work.md` |
| 11.2.6.4 | 查询 Work 队列状态 | 759 | 25481-25513 | 23 | `chapters/volcengine/ark/11.2.6.4 查询 Work 队列状态.md` |
| 11.2.6.5 | 停止 Work | 760-762 | 25514-25586 | 56 | `chapters/volcengine/ark/11.2.6.5 停止 Work.md` |
| 11.2.6.6 | 查询 Work 列表 | 763-765 | 25587-25679 | 76 | `chapters/volcengine/ark/11.2.6.6 查询 Work 列表.md` |
| 11.2.6.7 | 查询 Work 详情 | 766-767 | 25680-25737 | 46 | `chapters/volcengine/ark/11.2.6.7 查询 Work 详情.md` |
| 11.3.1 | 创建会话 | 768-798 | 25739-26789 | 844 | `chapters/volcengine/ark/11.3.1 创建会话.md` |
| 11.3.2 | 查询会话列表 | 799-818 | 26790-27436 | 561 | `chapters/volcengine/ark/11.3.2 查询会话列表.md` |
| 11.3.3 | 查询会话详情 | 819-837 | 27437-28039 | 523 | `chapters/volcengine/ark/11.3.3 查询会话详情.md` |
| 11.3.4 | 更新会话标题和标签 | 838-856 | 28040-28654 | 529 | `chapters/volcengine/ark/11.3.4 更新会话标题和标签.md` |
| 11.3.5 | 升级会话 | 857-882 | 28655-29534 | 747 | `chapters/volcengine/ark/11.3.5 升级会话.md` |
| 11.3.6 | 删除会话 | 883 | 29535-29561 | 20 | `chapters/volcengine/ark/11.3.6 删除会话.md` |
| 11.3.7.1 | 发送会话事件 | 884-885 | 29563-29609 | 33 | `chapters/volcengine/ark/11.3.7.1 发送会话事件.md` |
| 11.3.7.2 | 查询会话事件列表 | 886-888 | 29610-29676 | 50 | `chapters/volcengine/ark/11.3.7.2 查询会话事件列表.md` |
| 11.3.7.3 | 流式获取会话事件 | 889-890 | 29677-29737 | 34 | `chapters/volcengine/ark/11.3.7.3 流式获取会话事件.md` |
| 11.3.7.4 | 会话事件结构参考 - 第1部分 | 891-949 | 29738-31554 | 1648 | `chapters/volcengine/ark/11.3.7.4 会话事件结构参考 - 第1部分.md` |
| 11.3.8.1 | 添加会话资源 | 950-951 | 31556-31606 | 37 | `chapters/volcengine/ark/11.3.8.1 添加会话资源.md` |
| 11.3.8.2 | 查询会话资源列表 | 952-955 | 31607-31703 | 88 | `chapters/volcengine/ark/11.3.8.2 查询会话资源列表.md` |
| 11.3.8.3 | 查询会话资源 | 956-957 | 31704-31748 | 36 | `chapters/volcengine/ark/11.3.8.3 查询会话资源.md` |
| 11.3.9.1 | 查询线程列表 | 958-960 | 31750-31819 | 56 | `chapters/volcengine/ark/11.3.9.1 查询线程列表.md` |
| 11.3.9.2 | 查询线程详情 | 961-962 | 31820-31868 | 37 | `chapters/volcengine/ark/11.3.9.2 查询线程详情.md` |
| 11.3.9.3 | 查询线程事件列表 | 963-964 | 31869-31930 | 46 | `chapters/volcengine/ark/11.3.9.3 查询线程事件列表.md` |
| 11.3.9.4 | 流式获取线程事件 | 965-966 | 31931-31979 | 29 | `chapters/volcengine/ark/11.3.9.4 流式获取线程事件.md` |
| 11.4.1 | 创建保管库 | 967-968 | 31981-32027 | 36 | `chapters/volcengine/ark/11.4.1 创建保管库.md` |
| 11.4.2 | 查询保管库列表 | 969-970 | 32028-32096 | 55 | `chapters/volcengine/ark/11.4.2 查询保管库列表.md` |
| 11.4.3 | 查询保管库详情 | 971 | 32097-32123 | 24 | `chapters/volcengine/ark/11.4.3 查询保管库详情.md` |
| 11.4.4 | 更新保管库 | 972-973 | 32124-32165 | 33 | `chapters/volcengine/ark/11.4.4 更新保管库.md` |
| 11.4.5 | 删除保管库 | 974 | 32166-32190 | 21 | `chapters/volcengine/ark/11.4.5 删除保管库.md` |
| 11.4.6.1 | 创建凭证 | 975-987 | 32192-32660 | 358 | `chapters/volcengine/ark/11.4.6.1 创建凭证.md` |
| 11.4.6.2 | 查询凭证列表 | 988-994 | 32661-32885 | 182 | `chapters/volcengine/ark/11.4.6.2 查询凭证列表.md` |
| 11.4.6.3 | 查询凭证详情 | 995-1000 | 32886-33082 | 160 | `chapters/volcengine/ark/11.4.6.3 查询凭证详情.md` |
| 11.4.6.4 | 更新凭证 | 1001-1013 | 33083-33525 | 334 | `chapters/volcengine/ark/11.4.6.4 更新凭证.md` |
| 11.4.6.5 | 删除凭证 | 1014 | 33526-33552 | 21 | `chapters/volcengine/ark/11.4.6.5 删除凭证.md` |
| 11.5.1 | 创建记忆库 | 1015-1017 | 33554-33633 | 61 | `chapters/volcengine/ark/11.5.1 创建记忆库.md` |
| 11.5.2 | 查询记忆库列表 | 1018-1021 | 33634-33738 | 80 | `chapters/volcengine/ark/11.5.2 查询记忆库列表.md` |
| 11.5.3 | 查询记忆库详情 | 1022-1023 | 33739-33800 | 47 | `chapters/volcengine/ark/11.5.3 查询记忆库详情.md` |
| 11.5.4 | 更新记忆库 | 1024-1026 | 33801-33881 | 61 | `chapters/volcengine/ark/11.5.4 更新记忆库.md` |
| 11.5.5 | 删除记忆库 | 1027 | 33882-33907 | 18 | `chapters/volcengine/ark/11.5.5 删除记忆库.md` |
| 11.5.6.1 | 创建记忆 | 1028-1030 | 33909-33975 | 51 | `chapters/volcengine/ark/11.5.6.1 创建记忆.md` |
| 11.5.6.2 | 批量创建记忆 | 1031-1034 | 33976-34095 | 90 | `chapters/volcengine/ark/11.5.6.2 批量创建记忆.md` |
| 11.5.6.3 | 查询记忆列表 | 1035-1037 | 34096-34189 | 70 | `chapters/volcengine/ark/11.5.6.3 查询记忆列表.md` |
| 11.5.6.4 | 查询记忆详情 | 1038-1039 | 34190-34248 | 45 | `chapters/volcengine/ark/11.5.6.4 查询记忆详情.md` |
| 11.5.6.5 | 更新记忆 | 1040-1042 | 34249-34323 | 52 | `chapters/volcengine/ark/11.5.6.5 更新记忆.md` |
| 11.5.6.6 | 删除记忆 | 1043 | 34324-34351 | 18 | `chapters/volcengine/ark/11.5.6.6 删除记忆.md` |
| 11.6.1 | 创建 Dream | 1044-1047 | 34353-34477 | 108 | `chapters/volcengine/ark/11.6.1 创建 Dream.md` |
| 11.6.2 | 查询 Dream 列表 | 1048-1052 | 34478-34617 | 119 | `chapters/volcengine/ark/11.6.2 查询 Dream 列表.md` |
| 11.6.3 | 查询 Dream | 1053-1055 | 34618-34713 | 83 | `chapters/volcengine/ark/11.6.3 查询 Dream.md` |
| 11.6.4 | 取消 Dream | 1056-1059 | 34714-34814 | 84 | `chapters/volcengine/ark/11.6.4 取消 Dream.md` |
| 11.7.1 | 创建技能 | 1060-1061 | 34816-34884 | 49 | `chapters/volcengine/ark/11.7.1 创建技能.md` |
| 11.7.2 | 查询技能列表 | 1062-1064 | 34885-34961 | 61 | `chapters/volcengine/ark/11.7.2 查询技能列表.md` |
| 11.7.3 | 查询技能详情 | 1065-1066 | 34962-35007 | 36 | `chapters/volcengine/ark/11.7.3 查询技能详情.md` |
| 11.7.4 | 设置技能内容保护 | 1067-1068 | 35008-35053 | 37 | `chapters/volcengine/ark/11.7.4 设置技能内容保护.md` |
| 11.7.5 | 删除技能 | 1069 | 35054-35079 | 18 | `chapters/volcengine/ark/11.7.5 删除技能.md` |
| 11.7.6 | 创建新版本的技能 | 1070-1071 | 35080-35139 | 41 | `chapters/volcengine/ark/11.7.6 创建新版本的技能.md` |
| 11.7.7 | 查询技能的版本列表 | 1072-1073 | 35140-35195 | 48 | `chapters/volcengine/ark/11.7.7 查询技能的版本列表.md` |
| 11.7.8 | 查询指定版本的技能 | 1074-1075 | 35196-35227 | 26 | `chapters/volcengine/ark/11.7.8 查询指定版本的技能.md` |
| 11.7.9 | 删除指定版本的技能 | 1076 | 35228-35249 | 17 | `chapters/volcengine/ark/11.7.9 删除指定版本的技能.md` |
| 11.7.10 | 下载指定版本的技能 | 1077 | 35250-35268 | 14 | `chapters/volcengine/ark/11.7.10 下载指定版本的技能.md` |
| 11.7.11 | 扫描 GitHub 技能 | 1078-1079 | 35269-35321 | 43 | `chapters/volcengine/ark/11.7.11 扫描 GitHub 技能.md` |
| 11.7.12 | 导入 GitHub 技能 | 1080-1082 | 35322-35399 | 58 | `chapters/volcengine/ark/11.7.12 导入 GitHub 技能.md` |
| 12.1.1 | 创建批量推理任务 | 1083-1086 | 35402-35482 | 60 | `chapters/volcengine/ark/12.1.1 创建批量推理任务.md` |
| 12.1.2 | 获取批量推理任务列表 | 1087-1092 | 35483-35658 | 152 | `chapters/volcengine/ark/12.1.2 获取批量推理任务列表.md` |
| 12.1.3 | 获取批量推理任务 | 1093-1096 | 35659-35778 | 100 | `chapters/volcengine/ark/12.1.3 获取批量推理任务.md` |
| 12.1.4 | 更新批量推理任务 | 1097 | 35779-35802 | 17 | `chapters/volcengine/ark/12.1.4 更新批量推理任务.md` |
| 12.1.5 | 删除批量推理任务 | 1098 | 35803-35822 | 13 | `chapters/volcengine/ark/12.1.5 删除批量推理任务.md` |
| 12.1.6 | 停止批量推理任务 | 1099 | 35823-35845 | 14 | `chapters/volcengine/ark/12.1.6 停止批量推理任务.md` |
| 12.1.7 | 重启批量推理任务 | 1100 | 35846-35866 | 13 | `chapters/volcengine/ark/12.1.7 重启批量推理任务.md` |
| 12.2 | 批量(Chat) API | 1101-1118 | 35867-36335 | 352 | `chapters/volcengine/ark/12.2 批量(Chat) API.md` |
| 13.1 | 分词 API | 1119-1120 | 36337-36383 | 39 | `chapters/volcengine/ark/13.1 分词 API.md` |
| 14.1.1 | 获取临时 API Key | 1121-1122 | 36386-36422 | 26 | `chapters/volcengine/ark/14.1.1 获取临时 API Key.md` |
| 14.2.1 | 创建个人版套餐 | 1123-1124 | 36424-36481 | 33 | `chapters/volcengine/ark/14.2.1 创建个人版套餐.md` |
| 14.2.2 | 续费个人版套餐 | 1125-1126 | 36482-36527 | 27 | `chapters/volcengine/ark/14.2.2 续费个人版套餐.md` |
| 14.2.3 | 查询个人版套餐 | 1127 | 36528-36555 | 20 | `chapters/volcengine/ark/14.2.3 查询个人版套餐.md` |
| 14.2.4.1 | 查询 Agent Plan 支持的模型列表 | 1128 | 36557-36576 | 14 | `chapters/volcengine/ark/14.2.4.1 查询 Agent Plan 支持的模型列表.md` |
| 14.2.4.2 | 轮换个人版 API Key | 1129 | 36577-36603 | 17 | `chapters/volcengine/ark/14.2.4.2 轮换个人版 API Key.md` |
| 14.2.4.3 | 获取套餐 AFP 额度 | 1130-1132 | 36604-36680 | 66 | `chapters/volcengine/ark/14.2.4.3 获取套餐 AFP 额度.md` |
| 14.2.4.4 | 获取套餐用量详情 | 1133-1134 | 36681-36729 | 39 | `chapters/volcengine/ark/14.2.4.4 获取套餐用量详情.md` |
| 14.2.5.1 | 查询 Coding Plan 支持的模型列表 | 1135 | 36731-36746 | 12 | `chapters/volcengine/ark/14.2.5.1 查询 Coding Plan 支持的模型列表.md` |
| 14.3.1 | 获取基础模型版本列表 | 1136-1138 | 36748-36835 | 72 | `chapters/volcengine/ark/14.3.1 获取基础模型版本列表.md` |
| 14.3.2 | 获取基础模型版本信息 | 1139-1149 | 36836-37159 | 273 | `chapters/volcengine/ark/14.3.2 获取基础模型版本信息.md` |
| 14.3.3 | 获取基础模型列表 | 1150-1155 | 37160-37414 | 186 | `chapters/volcengine/ark/14.3.3 获取基础模型列表.md` |
| 14.3.4 | 获取基础模型信息 | 1156-1159 | 37415-37541 | 93 | `chapters/volcengine/ark/14.3.4 获取基础模型信息.md` |
| 14.4.1 | 批量开通基础模型 | 1160 | 37543-37557 | 11 | `chapters/volcengine/ark/14.4.1 批量开通基础模型.md` |
| 14.4.2 | 启用自动开通新模型 | 1161 | 37558-37569 | 7 | `chapters/volcengine/ark/14.4.2 启用自动开通新模型.md` |
| 14.4.3 | 关闭自动开通新模型 | 1162 | 37570-37581 | 7 | `chapters/volcengine/ark/14.4.3 关闭自动开通新模型.md` |
| 14.4.4 | 查询模型开通详情 | 1163-1167 | 37582-37726 | 131 | `chapters/volcengine/ark/14.4.4 查询模型开通详情.md` |
| 14.4.5 | 查询模型开通列表 | 1168-1173 | 37727-37906 | 163 | `chapters/volcengine/ark/14.4.5 查询模型开通列表.md` |
| 14.5.1 | 批量开通资源 | 1174 | 37908-37926 | 14 | `chapters/volcengine/ark/14.5.1 批量开通资源.md` |
| 14.5.2 | 查询资源开通列表 | 1175-1178 | 37927-38030 | 92 | `chapters/volcengine/ark/14.5.2 查询资源开通列表.md` |
| 14.6.1 | 查询模型限流 | 1179-1182 | 38032-38133 | 91 | `chapters/volcengine/ark/14.6.1 查询模型限流.md` |
| 14.7.1 | 删除定制模型 | 1183 | 38135-38159 | 16 | `chapters/volcengine/ark/14.7.1 删除定制模型.md` |
| 14.7.2 | 获取定制模型信息 | 1184-1187 | 38160-38270 | 97 | `chapters/volcengine/ark/14.7.2 获取定制模型信息.md` |
| 14.7.3 | 更新定制模型 | 1188-1189 | 38271-38305 | 22 | `chapters/volcengine/ark/14.7.3 更新定制模型.md` |
| 14.7.4 | 获取定制模型列表 | 1190-1193 | 38306-38426 | 102 | `chapters/volcengine/ark/14.7.4 获取定制模型列表.md` |
| 14.8.1 | 创建模型调优任务 | 1194-1204 | 38428-38751 | 279 | `chapters/volcengine/ark/14.8.1 创建模型调优任务.md` |
| 14.8.2 | 删除模型调优任务 | 1205 | 38752-38768 | 10 | `chapters/volcengine/ark/14.8.2 删除模型调优任务.md` |
| 14.8.3 | 获取模型调优任务信息 | 1206-1220 | 38769-39230 | 411 | `chapters/volcengine/ark/14.8.3 获取模型调优任务信息.md` |
| 14.8.4 | 查询精调效果指标详细数据 | 1221-1222 | 39231-39276 | 33 | `chapters/volcengine/ark/14.8.4 查询精调效果指标详细数据.md` |
| 14.8.5 | 查询精调效果指标 | 1223 | 39277-39295 | 10 | `chapters/volcengine/ark/14.8.5 查询精调效果指标.md` |
| 14.8.6 | 获取模型调优任务列表 | 1224-1232 | 39296-39570 | 246 | `chapters/volcengine/ark/14.8.6 获取模型调优任务列表.md` |
| 14.8.7 | 重试模型调优任务 | 1233 | 39571-39587 | 9 | `chapters/volcengine/ark/14.8.7 重试模型调优任务.md` |
| 14.8.8 | 停止模型调优任务 | 1234 | 39588-39604 | 10 | `chapters/volcengine/ark/14.8.8 停止模型调优任务.md` |
| 14.8.9 | 更新模型调优任务 | 1235 | 39605-39628 | 14 | `chapters/volcengine/ark/14.8.9 更新模型调优任务.md` |
| 14.9.1 | 开启推理接入点 | 1236 | 39630-39649 | 13 | `chapters/volcengine/ark/14.9.1 开启推理接入点.md` |
| 14.9.2 | 停止推理接入点 | 1237 | 39650-39670 | 11 | `chapters/volcengine/ark/14.9.2 停止推理接入点.md` |
| 14.9.3 | 获取推理接入点列表 | 1238-1243 | 39671-39883 | 168 | `chapters/volcengine/ark/14.9.3 获取推理接入点列表.md` |
| 14.9.4 | 获取推理接入点 | 1244-1247 | 39884-39987 | 88 | `chapters/volcengine/ark/14.9.4 获取推理接入点.md` |
| 14.9.5 | 删除推理接入点 | 1248 | 39988-40007 | 12 | `chapters/volcengine/ark/14.9.5 删除推理接入点.md` |
| 14.9.6 | 更新推理接入点 | 1249-1254 | 40008-40194 | 160 | `chapters/volcengine/ark/14.9.6 更新推理接入点.md` |
| 14.9.7 | 创建推理接入点 | 1255-1262 | 40195-40425 | 192 | `chapters/volcengine/ark/14.9.7 创建推理接入点.md` |
| 14.9.8 | 获取接入点推理应用层加密证书 | 1263-1264 | 40426-40461 | 23 | `chapters/volcengine/ark/14.9.8 获取接入点推理应用层加密证书.md` |
| 14.9.9 | 创建推理接入点滚动升级任务 | 1265-1266 | 40462-40509 | 41 | `chapters/volcengine/ark/14.9.9 创建推理接入点滚动升级任务.md` |
| 14.9.10 | 查询推理接入点滚动升级详情 | 1267-1271 | 40510-40638 | 116 | `chapters/volcengine/ark/14.9.10 查询推理接入点滚动升级详情.md` |
| 14.9.11 | 回滚推理接入点滚动升级 | 1272 | 40639-40656 | 13 | `chapters/volcengine/ark/14.9.11 回滚推理接入点滚动升级.md` |
| 14.9.12 | 取消推理接入点滚动升级 | 1273 | 40657-40674 | 13 | `chapters/volcengine/ark/14.9.12 取消推理接入点滚动升级.md` |
| 14.10.1 | 创建评测任务 | 1274-1278 | 40676-40841 | 131 | `chapters/volcengine/ark/14.10.1 创建评测任务.md` |
| 14.10.2 | 删除评测任务 | 1279 | 40842-40863 | 13 | `chapters/volcengine/ark/14.10.2 删除评测任务.md` |
| 14.10.3 | 获取评测任务 | 1280-1282 | 40864-40945 | 67 | `chapters/volcengine/ark/14.10.3 获取评测任务.md` |
| 14.10.4 | 获取评测任务结果 | 1283-1286 | 40946-41050 | 87 | `chapters/volcengine/ark/14.10.4 获取评测任务结果.md` |
| 14.10.5 | 获取评测任务列表 | 1287-1291 | 41051-41199 | 129 | `chapters/volcengine/ark/14.10.5 获取评测任务列表.md` |
| 14.10.6 | 获取评测任务结果列表 | 1292-1296 | 41200-41343 | 120 | `chapters/volcengine/ark/14.10.6 获取评测任务结果列表.md` |
| 14.10.7 | 停止评测任务 | 1297 | 41344-41365 | 13 | `chapters/volcengine/ark/14.10.7 停止评测任务.md` |
| 14.10.8 | 更新评测任务 | 1298 | 41366-41391 | 18 | `chapters/volcengine/ark/14.10.8 更新评测任务.md` |
| 14.11.1 | 查询推理用量 | 1299-1301 | 41393-41519 | 75 | `chapters/volcengine/ark/14.11.1 查询推理用量.md` |
| 14.11.2 | 查询单请求用量 | 1302-1306 | 41520-41660 | 124 | `chapters/volcengine/ark/14.11.2 查询单请求用量.md` |
| 14.11.3 | 查询异步任务用量 | 1307-1309 | 41661-41733 | 62 | `chapters/volcengine/ark/14.11.3 查询异步任务用量.md` |
| 14.11.4 | 创建用量明细导出任务 | 1310-1311 | 41734-41788 | 33 | `chapters/volcengine/ark/14.11.4 创建用量明细导出任务.md` |
| 14.11.5 | 查询用量明细导出任务状态 | 1312-1314 | 41789-41891 | 71 | `chapters/volcengine/ark/14.11.5 查询用量明细导出任务状态.md` |
| 14.11.6 | 查询模型推理限额 | 1315 | 41892-41919 | 22 | `chapters/volcengine/ark/14.11.6 查询模型推理限额.md` |
| 14.11.7 | 开启模型推理限额 | 1316 | 41920-41944 | 16 | `chapters/volcengine/ark/14.11.7 开启模型推理限额.md` |
| 14.11.8 | 关闭模型推理限额 | 1317 | 41945-41965 | 12 | `chapters/volcengine/ark/14.11.8 关闭模型推理限额.md` |
| 14.12.1 | 创建方舟官方模型产物查询请求 | 1318 | 41967-41985 | 14 | `chapters/volcengine/ark/14.12.1 创建方舟官方模型产物查询请求.md` |
| 14.12.2 | 获取安全审计日志 | 1319-1322 | 41986-42107 | 85 | `chapters/volcengine/ark/14.12.2 获取安全审计日志.md` |
| 14.12.3 | 获取方舟官方产物确认结果 | 1323-1324 | 42108-42139 | 24 | `chapters/volcengine/ark/14.12.3 获取方舟官方产物确认结果.md` |
| 14.13.1 | 上报视频生成模型效果问题 | 1325-1328 | 42141-42266 | 86 | `chapters/volcengine/ark/14.13.1 上报视频生成模型效果问题.md` |
| 14.13.2 | 查询视频生成模型效果问题结果 | 1329-1332 | 42267-42355 | 69 | `chapters/volcengine/ark/14.13.2 查询视频生成模型效果问题结果.md` |
| 14.13.3 | 上报大语言模型效果问题 | 1333-1335 | 42356-42464 | 81 | `chapters/volcengine/ark/14.13.3 上报大语言模型效果问题.md` |
| 14.13.4 | 查询大语言模型效果问题结果 | 1336-1339 | 42465-42582 | 97 | `chapters/volcengine/ark/14.13.4 查询大语言模型效果问题结果.md` |
| 15.1 | 兼容 OpenAI SDK | 1340-1343 | 42584-42700 | 103 | `chapters/volcengine/ark/15.1 兼容 OpenAI SDK.md` |
| 15.2 | 向后兼容性 | 1344 | 42701-42746 | 25 | `chapters/volcengine/ark/15.2 向后兼容性.md` |
| 15.3 | 错误码 - 第1部分 | 1344-1365 | 42747-44730 | 1936 | `chapters/volcengine/ark/15.3 错误码 - 第1部分.md` |
| 15.3 | 错误码 - 第2部分·错误码 | 1366-1375 | 44731-45505 | 751 | `chapters/volcengine/ark/15.3 错误码 - 第2部分·错误码.md` |
| 15.4 | SDK 常见使用示例 | 1376-1393 | 45506-46187 | 611 | `chapters/volcengine/ark/15.4 SDK 常见使用示例.md` |
