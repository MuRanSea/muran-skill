# 方舟 API 区章节表（ark）

来源：《火山方舟 API 参考》（1486 页）。202 个章节文件，接口级切分：一个接口/任务一个文件；超过 1500 行的按语义块自动再拆为`… - 第N部分`（5 个章节被拆分）。

「页码」是原 PDF 页码范围；「行范围」是中间 MD（`doc/<源文档>.md`）的 1 起始行号，可据此回查原文。章节文件本身已去掉页眉页脚，回查 PDF 时用这两列。文件名即章节标题，日常定位直接 Glob 文件名即可，用不到这两列。

**这张表用来 grep，不要整读。**

| 编号 | 标题 | 页码 | 行范围(源文件) | 行数 | 文件 |
|------|------|------|---------------|------|------|
| 1.1 | 获取 API Key 并配置 | 1 | 282-316 | 19 | `chapters/volcengine/ark/1.1 获取 API Key 并配置.md` |
| 1.2 | 安装及升级 SDK | 2-7 | 317-472 | 115 | `chapters/volcengine/ark/1.2 安装及升级 SDK.md` |
| 1.3 | Base URL及鉴权 | 8-10 | 473-568 | 68 | `chapters/volcengine/ark/1.3 Base URL及鉴权.md` |
| 2.1 | 对话(Chat) API | 11-66 | 570-2885 | 1249 | `chapters/volcengine/ark/2.1 对话(Chat) API.md` |
| 3.1 | 创建 Response - 第1部分 | 67-115 | 2886-4551 | 1410 | `chapters/volcengine/ark/3.1 创建 Response - 第1部分.md` |
| 3.1 | 创建 Response - 第2部分·响应参数 | 116-178 | 4552-6893 | 1344 | `chapters/volcengine/ark/3.1 创建 Response - 第2部分·响应参数.md` |
| 3.2 | 查询 Response 详情 | 179-215 | 6894-8047 | 1062 | `chapters/volcengine/ark/3.2 查询 Response 详情.md` |
| 3.3 | 查询 Response 输入项列表 | 216-244 | 8048-8960 | 831 | `chapters/volcengine/ark/3.3 查询 Response 输入项列表.md` |
| 3.4 | 删除 Response | 245 | 8961-8984 | 19 | `chapters/volcengine/ark/3.4 删除 Response.md` |
| 3.5.1 | Response 生命周期 - 第1部分 | 246-297 | 8985-10683 | 1494 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第1部分.md` |
| 3.5.1 | Response 生命周期 - 第2部分 | 298-349 | 10684-12384 | 1495 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第2部分.md` |
| 3.5.1 | Response 生命周期 - 第3部分 | 350-401 | 12385-14075 | 1489 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第3部分.md` |
| 3.5.1 | Response 生命周期 - 第4部分 | 402-462 | 14076-16063 | 1726 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第4部分.md` |
| 3.5.2 | Output Item 与文本回答 - 第1部分 | 463-513 | 16064-17694 | 1470 | `chapters/volcengine/ark/3.5.2 Output Item 与文本回答 - 第1部分.md` |
| 3.5.2 | Output Item 与文本回答 - 第2部分 | 514-534 | 17695-18322 | 586 | `chapters/volcengine/ark/3.5.2 Output Item 与文本回答 - 第2部分.md` |
| 3.5.3 | 工具调用事件 | 535-571 | 18323-19423 | 1024 | `chapters/volcengine/ark/3.5.3 工具调用事件.md` |
| 3.5.4 | 语音转写与错误事件 | 572-577 | 19424-19596 | 161 | `chapters/volcengine/ark/3.5.4 语音转写与错误事件.md` |
| 4.1 | 创建 Message | 578-597 | 19598-20254 | 569 | `chapters/volcengine/ark/4.1 创建 Message.md` |
| 4.2 | 统计 Messages 请求 token 数 | 598-607 | 20255-20591 | 278 | `chapters/volcengine/ark/4.2 统计 Messages 请求 token 数.md` |
| 5.1 | System One API（beta） | 608-616 | 20593-20867 | 240 | `chapters/volcengine/ark/5.1 System One API（beta）.md` |
| 6.1 | 上传文件 | 617-622 | 20869-21080 | 157 | `chapters/volcengine/ark/6.1 上传文件.md` |
| 6.2 | 查询文件详情 | 623-625 | 21081-21154 | 63 | `chapters/volcengine/ark/6.2 查询文件详情.md` |
| 6.3 | 查询文件列表 | 626-629 | 21155-21289 | 112 | `chapters/volcengine/ark/6.3 查询文件列表.md` |
| 6.4 | 删除文件 | 630 | 21290-21312 | 19 | `chapters/volcengine/ark/6.4 删除文件.md` |
| 6.5 | The file object | 631-633 | 21313-21384 | 57 | `chapters/volcengine/ark/6.5 The file object.md` |
| 7.1 | 创建视频生成任务 | 634-673 | 21386-23241 | 828 | `chapters/volcengine/ark/7.1 创建视频生成任务.md` |
| 7.2 | 查询视频生成任务 | 674-678 | 23242-23396 | 112 | `chapters/volcengine/ark/7.2 查询视频生成任务.md` |
| 7.3 | 查询视频生成任务列表 | 679-684 | 23397-23616 | 164 | `chapters/volcengine/ark/7.3 查询视频生成任务列表.md` |
| 7.4 | 取消或删除视频生成任务 | 685 | 23617-23658 | 38 | `chapters/volcengine/ark/7.4 取消或删除视频生成任务.md` |
| 8.1 | 图片生成 API | 686-703 | 23660-24407 | 520 | `chapters/volcengine/ark/8.1 图片生成 API.md` |
| 8.2 | 图片生成流式响应事件 | 704-709 | 24408-24586 | 156 | `chapters/volcengine/ark/8.2 图片生成流式响应事件.md` |
| 9.1.1 | 创建 3D 生成任务 API | 710-712 | 24589-24693 | 79 | `chapters/volcengine/ark/9.1.1 创建 3D 生成任务 API.md` |
| 9.1.2 | 查询 3D 生成任务 API | 713-714 | 24694-24763 | 52 | `chapters/volcengine/ark/9.1.2 查询 3D 生成任务 API.md` |
| 9.1.3 | 查询 3D 生成任务列表 | 715-718 | 24764-24879 | 87 | `chapters/volcengine/ark/9.1.3 查询 3D 生成任务列表.md` |
| 9.1.4 | 取消或删除 3D 生成任务 | 719 | 24880-24921 | 38 | `chapters/volcengine/ark/9.1.4 取消或删除 3D 生成任务.md` |
| 9.2.1 | 创建3D生成任务 | 720-724 | 24923-25137 | 148 | `chapters/volcengine/ark/9.2.1 创建3D生成任务.md` |
| 9.2.2 | 查询3D生成任务 | 725-726 | 25138-25203 | 48 | `chapters/volcengine/ark/9.2.2 查询3D生成任务.md` |
| 9.2.3 | 查询3D生成任务列表 | 727-729 | 25204-25311 | 81 | `chapters/volcengine/ark/9.2.3 查询3D生成任务列表.md` |
| 9.2.4 | 取消或删除3D生成任务 | 730 | 25312-25346 | 31 | `chapters/volcengine/ark/9.2.4 取消或删除3D生成任务.md` |
| 9.3.1 | 创建3D生成任务 | 731-734 | 25348-25479 | 95 | `chapters/volcengine/ark/9.3.1 创建3D生成任务.md` |
| 9.3.2 | 查询3D生成任务 | 735-736 | 25480-25545 | 48 | `chapters/volcengine/ark/9.3.2 查询3D生成任务.md` |
| 9.3.3 | 查询3D生成任务列表 | 737-739 | 25546-25653 | 81 | `chapters/volcengine/ark/9.3.3 查询3D生成任务列表.md` |
| 9.3.4 | 取消或删除3D生成任务 | 740 | 25654-25688 | 31 | `chapters/volcengine/ark/9.3.4 取消或删除3D生成任务.md` |
| 10.1 | 多模态向量化 API | 741-746 | 25690-25889 | 145 | `chapters/volcengine/ark/10.1 多模态向量化 API.md` |
| 11.1.1 | 创建智能体 | 747-760 | 25892-26383 | 371 | `chapters/volcengine/ark/11.1.1 创建智能体.md` |
| 11.1.2 | 查询智能体列表 | 761-768 | 26384-26644 | 215 | `chapters/volcengine/ark/11.1.2 查询智能体列表.md` |
| 11.1.3 | 查询智能体详情 | 769-775 | 26645-26868 | 180 | `chapters/volcengine/ark/11.1.3 查询智能体详情.md` |
| 11.1.4 | 更新智能体 | 776-790 | 26869-27408 | 389 | `chapters/volcengine/ark/11.1.4 更新智能体.md` |
| 11.1.5 | 删除智能体 | 791 | 27409-27429 | 14 | `chapters/volcengine/ark/11.1.5 删除智能体.md` |
| 11.1.6 | 查询智能体版本列表 | 792-799 | 27430-27679 | 202 | `chapters/volcengine/ark/11.1.6 查询智能体版本列表.md` |
| 11.2.1 | 创建环境 | 800-805 | 27681-27870 | 154 | `chapters/volcengine/ark/11.2.1 创建环境.md` |
| 11.2.2 | 查询环境列表 | 806-809 | 27871-27980 | 99 | `chapters/volcengine/ark/11.2.2 查询环境列表.md` |
| 11.2.3 | 查询环境详情 | 810-812 | 27981-28071 | 80 | `chapters/volcengine/ark/11.2.3 查询环境详情.md` |
| 11.2.4 | 更新环境 | 813-818 | 28072-28279 | 164 | `chapters/volcengine/ark/11.2.4 更新环境.md` |
| 11.2.5 | 删除环境 | 819 | 28280-28302 | 17 | `chapters/volcengine/ark/11.2.5 删除环境.md` |
| 11.2.6.1 | 长轮询拉取待执行 Work | 820-822 | 28304-28394 | 68 | `chapters/volcengine/ark/11.2.6.1 长轮询拉取待执行 Work.md` |
| 11.2.6.2 | 认领 Work | 823-825 | 28395-28467 | 56 | `chapters/volcengine/ark/11.2.6.2 认领 Work.md` |
| 11.2.6.3 | 续租 Work | 826-827 | 28468-28523 | 41 | `chapters/volcengine/ark/11.2.6.3 续租 Work.md` |
| 11.2.6.4 | 查询 Work 队列状态 | 828 | 28524-28556 | 23 | `chapters/volcengine/ark/11.2.6.4 查询 Work 队列状态.md` |
| 11.2.6.5 | 停止 Work | 829-831 | 28557-28629 | 56 | `chapters/volcengine/ark/11.2.6.5 停止 Work.md` |
| 11.2.6.6 | 查询 Work 列表 | 832-834 | 28630-28722 | 76 | `chapters/volcengine/ark/11.2.6.6 查询 Work 列表.md` |
| 11.2.6.7 | 查询 Work 详情 | 835-836 | 28723-28780 | 46 | `chapters/volcengine/ark/11.2.6.7 查询 Work 详情.md` |
| 11.3.1 | 创建会话 | 837-867 | 28782-29836 | 846 | `chapters/volcengine/ark/11.3.1 创建会话.md` |
| 11.3.2 | 查询会话列表 | 868-887 | 29837-30487 | 563 | `chapters/volcengine/ark/11.3.2 查询会话列表.md` |
| 11.3.3 | 查询会话详情 | 888-909 | 30488-31215 | 564 | `chapters/volcengine/ark/11.3.3 查询会话详情.md` |
| 11.3.4 | 更新会话标题和标签 | 910-928 | 31216-31834 | 531 | `chapters/volcengine/ark/11.3.4 更新会话标题和标签.md` |
| 11.3.5 | 升级会话 | 929-955 | 31835-32720 | 749 | `chapters/volcengine/ark/11.3.5 升级会话.md` |
| 11.3.6 | 删除会话 | 956 | 32721-32747 | 20 | `chapters/volcengine/ark/11.3.6 删除会话.md` |
| 11.3.7.1 | 查询会话任务 | 957-960 | 32749-32871 | 93 | `chapters/volcengine/ark/11.3.7.1 查询会话任务.md` |
| 11.3.7.2 | 查询会话任务列表 | 961-964 | 32872-32987 | 88 | `chapters/volcengine/ark/11.3.7.2 查询会话任务列表.md` |
| 11.3.7.3 | 取消会话任务 | 965-966 | 32988-33046 | 31 | `chapters/volcengine/ark/11.3.7.3 取消会话任务.md` |
| 11.3.8.1 | 发送会话事件 | 967-968 | 33048-33094 | 33 | `chapters/volcengine/ark/11.3.8.1 发送会话事件.md` |
| 11.3.8.2 | 查询会话事件列表 | 969-971 | 33095-33161 | 50 | `chapters/volcengine/ark/11.3.8.2 查询会话事件列表.md` |
| 11.3.8.3 | 流式获取会话事件 | 972-975 | 33162-33333 | 49 | `chapters/volcengine/ark/11.3.8.3 流式获取会话事件.md` |
| 11.3.8.4 | 会话事件结构参考 - 第1部分 | 976-1036 | 33334-35206 | 1693 | `chapters/volcengine/ark/11.3.8.4 会话事件结构参考 - 第1部分.md` |
| 11.3.9.1 | 添加会话资源 | 1037-1038 | 35208-35258 | 37 | `chapters/volcengine/ark/11.3.9.1 添加会话资源.md` |
| 11.3.9.2 | 查询会话资源列表 | 1039-1042 | 35259-35359 | 90 | `chapters/volcengine/ark/11.3.9.2 查询会话资源列表.md` |
| 11.3.9.3 | 查询会话资源 | 1043-1044 | 35360-35404 | 36 | `chapters/volcengine/ark/11.3.9.3 查询会话资源.md` |
| 11.3.10.1 | 查询线程列表 | 1045-1047 | 35406-35475 | 56 | `chapters/volcengine/ark/11.3.10.1 查询线程列表.md` |
| 11.3.10.2 | 查询线程详情 | 1048-1052 | 35476-35658 | 99 | `chapters/volcengine/ark/11.3.10.2 查询线程详情.md` |
| 11.3.10.3 | 查询线程事件列表 | 1053-1054 | 35659-35720 | 46 | `chapters/volcengine/ark/11.3.10.3 查询线程事件列表.md` |
| 11.3.10.4 | 流式获取线程事件 | 1055-1056 | 35721-35769 | 29 | `chapters/volcengine/ark/11.3.10.4 流式获取线程事件.md` |
| 11.4.1 | 创建保管库 | 1057-1058 | 35771-35817 | 36 | `chapters/volcengine/ark/11.4.1 创建保管库.md` |
| 11.4.2 | 查询保管库列表 | 1059-1060 | 35818-35886 | 55 | `chapters/volcengine/ark/11.4.2 查询保管库列表.md` |
| 11.4.3 | 查询保管库详情 | 1061 | 35887-35913 | 24 | `chapters/volcengine/ark/11.4.3 查询保管库详情.md` |
| 11.4.4 | 更新保管库 | 1062-1063 | 35914-35955 | 33 | `chapters/volcengine/ark/11.4.4 更新保管库.md` |
| 11.4.5 | 删除保管库 | 1064 | 35956-35980 | 21 | `chapters/volcengine/ark/11.4.5 删除保管库.md` |
| 11.4.6.1 | 创建凭证 | 1065-1077 | 35982-36450 | 358 | `chapters/volcengine/ark/11.4.6.1 创建凭证.md` |
| 11.4.6.2 | 查询凭证列表 | 1078-1084 | 36451-36675 | 182 | `chapters/volcengine/ark/11.4.6.2 查询凭证列表.md` |
| 11.4.6.3 | 查询凭证详情 | 1085-1090 | 36676-36872 | 160 | `chapters/volcengine/ark/11.4.6.3 查询凭证详情.md` |
| 11.4.6.4 | 更新凭证 | 1091-1103 | 36873-37315 | 334 | `chapters/volcengine/ark/11.4.6.4 更新凭证.md` |
| 11.4.6.5 | 删除凭证 | 1104 | 37316-37342 | 21 | `chapters/volcengine/ark/11.4.6.5 删除凭证.md` |
| 11.5.1 | 创建记忆库 | 1105-1107 | 37344-37423 | 61 | `chapters/volcengine/ark/11.5.1 创建记忆库.md` |
| 11.5.2 | 查询记忆库列表 | 1108-1111 | 37424-37528 | 80 | `chapters/volcengine/ark/11.5.2 查询记忆库列表.md` |
| 11.5.3 | 查询记忆库详情 | 1112-1113 | 37529-37590 | 47 | `chapters/volcengine/ark/11.5.3 查询记忆库详情.md` |
| 11.5.4 | 更新记忆库 | 1114-1116 | 37591-37671 | 61 | `chapters/volcengine/ark/11.5.4 更新记忆库.md` |
| 11.5.5 | 删除记忆库 | 1117 | 37672-37697 | 18 | `chapters/volcengine/ark/11.5.5 删除记忆库.md` |
| 11.5.6.1 | 创建记忆 | 1118-1120 | 37699-37765 | 51 | `chapters/volcengine/ark/11.5.6.1 创建记忆.md` |
| 11.5.6.2 | 批量创建记忆 | 1121-1124 | 37766-37885 | 90 | `chapters/volcengine/ark/11.5.6.2 批量创建记忆.md` |
| 11.5.6.3 | 查询记忆列表 | 1125-1127 | 37886-37979 | 70 | `chapters/volcengine/ark/11.5.6.3 查询记忆列表.md` |
| 11.5.6.4 | 查询记忆详情 | 1128-1129 | 37980-38038 | 45 | `chapters/volcengine/ark/11.5.6.4 查询记忆详情.md` |
| 11.5.6.5 | 更新记忆 | 1130-1132 | 38039-38113 | 52 | `chapters/volcengine/ark/11.5.6.5 更新记忆.md` |
| 11.5.6.6 | 删除记忆 | 1133 | 38114-38141 | 18 | `chapters/volcengine/ark/11.5.6.6 删除记忆.md` |
| 11.6.1 | 创建 Dream | 1134-1137 | 38143-38267 | 108 | `chapters/volcengine/ark/11.6.1 创建 Dream.md` |
| 11.6.2 | 查询 Dream 列表 | 1138-1142 | 38268-38407 | 119 | `chapters/volcengine/ark/11.6.2 查询 Dream 列表.md` |
| 11.6.3 | 查询 Dream | 1143-1145 | 38408-38503 | 83 | `chapters/volcengine/ark/11.6.3 查询 Dream.md` |
| 11.6.4 | 取消 Dream | 1146-1148 | 38504-38602 | 84 | `chapters/volcengine/ark/11.6.4 取消 Dream.md` |
| 11.7.1 | 创建技能 | 1149-1150 | 38604-38672 | 49 | `chapters/volcengine/ark/11.7.1 创建技能.md` |
| 11.7.2 | 查询技能列表 | 1151-1153 | 38673-38749 | 61 | `chapters/volcengine/ark/11.7.2 查询技能列表.md` |
| 11.7.3 | 查询技能详情 | 1154-1155 | 38750-38795 | 36 | `chapters/volcengine/ark/11.7.3 查询技能详情.md` |
| 11.7.4 | 设置技能内容保护 | 1156-1157 | 38796-38841 | 37 | `chapters/volcengine/ark/11.7.4 设置技能内容保护.md` |
| 11.7.5 | 删除技能 | 1158 | 38842-38867 | 18 | `chapters/volcengine/ark/11.7.5 删除技能.md` |
| 11.7.6 | 创建新版本的技能 | 1159-1160 | 38868-38927 | 41 | `chapters/volcengine/ark/11.7.6 创建新版本的技能.md` |
| 11.7.7 | 查询技能的版本列表 | 1161-1162 | 38928-38983 | 48 | `chapters/volcengine/ark/11.7.7 查询技能的版本列表.md` |
| 11.7.8 | 查询指定版本的技能 | 1163 | 38984-39013 | 26 | `chapters/volcengine/ark/11.7.8 查询指定版本的技能.md` |
| 11.7.9 | 删除指定版本的技能 | 1164 | 39014-39035 | 17 | `chapters/volcengine/ark/11.7.9 删除指定版本的技能.md` |
| 11.7.10 | 下载指定版本的技能 | 1165 | 39036-39054 | 14 | `chapters/volcengine/ark/11.7.10 下载指定版本的技能.md` |
| 11.7.11 | 扫描 GitHub 技能 | 1166-1167 | 39055-39107 | 43 | `chapters/volcengine/ark/11.7.11 扫描 GitHub 技能.md` |
| 11.7.12 | 导入 GitHub 技能 | 1168-1170 | 39108-39185 | 58 | `chapters/volcengine/ark/11.7.12 导入 GitHub 技能.md` |
| 12.1.1 | 创建批量推理任务 | 1171-1174 | 39188-39268 | 60 | `chapters/volcengine/ark/12.1.1 创建批量推理任务.md` |
| 12.1.2 | 获取批量推理任务列表 | 1175-1180 | 39269-39444 | 152 | `chapters/volcengine/ark/12.1.2 获取批量推理任务列表.md` |
| 12.1.3 | 获取批量推理任务 | 1181-1184 | 39445-39564 | 100 | `chapters/volcengine/ark/12.1.3 获取批量推理任务.md` |
| 12.1.4 | 更新批量推理任务 | 1185 | 39565-39588 | 17 | `chapters/volcengine/ark/12.1.4 更新批量推理任务.md` |
| 12.1.5 | 删除批量推理任务 | 1186 | 39589-39608 | 13 | `chapters/volcengine/ark/12.1.5 删除批量推理任务.md` |
| 12.1.6 | 停止批量推理任务 | 1187 | 39609-39631 | 14 | `chapters/volcengine/ark/12.1.6 停止批量推理任务.md` |
| 12.1.7 | 重启批量推理任务 | 1188 | 39632-39652 | 13 | `chapters/volcengine/ark/12.1.7 重启批量推理任务.md` |
| 12.2 | 批量(Chat) API | 1189-1211 | 39653-40108 | 339 | `chapters/volcengine/ark/12.2 批量(Chat) API.md` |
| 13.1 | 分词 API | 1212-1213 | 40110-40156 | 39 | `chapters/volcengine/ark/13.1 分词 API.md` |
| 14.1.1 | 获取临时 API Key | 1214-1215 | 40159-40195 | 26 | `chapters/volcengine/ark/14.1.1 获取临时 API Key.md` |
| 14.2.1 | 创建个人版套餐 | 1216-1217 | 40197-40254 | 33 | `chapters/volcengine/ark/14.2.1 创建个人版套餐.md` |
| 14.2.2 | 续费个人版套餐 | 1218-1219 | 40255-40300 | 27 | `chapters/volcengine/ark/14.2.2 续费个人版套餐.md` |
| 14.2.3 | 查询个人版套餐 | 1220 | 40301-40328 | 20 | `chapters/volcengine/ark/14.2.3 查询个人版套餐.md` |
| 14.2.4.1 | 查询 Agent Plan 支持的模型列表 | 1221 | 40330-40349 | 14 | `chapters/volcengine/ark/14.2.4.1 查询 Agent Plan 支持的模型列表.md` |
| 14.2.4.2 | 轮换个人版 API Key | 1222 | 40350-40376 | 17 | `chapters/volcengine/ark/14.2.4.2 轮换个人版 API Key.md` |
| 14.2.4.3 | 获取套餐 AFP 额度 | 1223-1225 | 40377-40453 | 66 | `chapters/volcengine/ark/14.2.4.3 获取套餐 AFP 额度.md` |
| 14.2.4.4 | 获取套餐用量详情 | 1226-1227 | 40454-40502 | 39 | `chapters/volcengine/ark/14.2.4.4 获取套餐用量详情.md` |
| 14.2.5.1 | 查询 Coding Plan 支持的模型列表 | 1228 | 40504-40519 | 12 | `chapters/volcengine/ark/14.2.5.1 查询 Coding Plan 支持的模型列表.md` |
| 14.3.1 | 获取基础模型版本列表 | 1229-1231 | 40521-40608 | 72 | `chapters/volcengine/ark/14.3.1 获取基础模型版本列表.md` |
| 14.3.2 | 获取基础模型版本信息 | 1232-1242 | 40609-40932 | 273 | `chapters/volcengine/ark/14.3.2 获取基础模型版本信息.md` |
| 14.3.3 | 获取基础模型列表 | 1243-1248 | 40933-41187 | 186 | `chapters/volcengine/ark/14.3.3 获取基础模型列表.md` |
| 14.3.4 | 获取基础模型信息 | 1249-1252 | 41188-41314 | 93 | `chapters/volcengine/ark/14.3.4 获取基础模型信息.md` |
| 14.4.1 | 批量开通基础模型 | 1253 | 41316-41330 | 11 | `chapters/volcengine/ark/14.4.1 批量开通基础模型.md` |
| 14.4.2 | 启用自动开通新模型 | 1254 | 41331-41342 | 7 | `chapters/volcengine/ark/14.4.2 启用自动开通新模型.md` |
| 14.4.3 | 关闭自动开通新模型 | 1255 | 41343-41354 | 7 | `chapters/volcengine/ark/14.4.3 关闭自动开通新模型.md` |
| 14.4.4 | 查询模型开通详情 | 1256-1260 | 41355-41499 | 131 | `chapters/volcengine/ark/14.4.4 查询模型开通详情.md` |
| 14.4.5 | 查询模型开通列表 | 1261-1266 | 41500-41679 | 163 | `chapters/volcengine/ark/14.4.5 查询模型开通列表.md` |
| 14.5.1 | 批量开通资源 | 1267 | 41681-41699 | 14 | `chapters/volcengine/ark/14.5.1 批量开通资源.md` |
| 14.5.2 | 查询资源开通列表 | 1268-1271 | 41700-41803 | 92 | `chapters/volcengine/ark/14.5.2 查询资源开通列表.md` |
| 14.6.1 | 查询模型限流 | 1272-1275 | 41805-41906 | 91 | `chapters/volcengine/ark/14.6.1 查询模型限流.md` |
| 14.7.1 | 删除定制模型 | 1276 | 41908-41932 | 16 | `chapters/volcengine/ark/14.7.1 删除定制模型.md` |
| 14.7.2 | 获取定制模型信息 | 1277-1280 | 41933-42043 | 97 | `chapters/volcengine/ark/14.7.2 获取定制模型信息.md` |
| 14.7.3 | 更新定制模型 | 1281-1282 | 42044-42078 | 22 | `chapters/volcengine/ark/14.7.3 更新定制模型.md` |
| 14.7.4 | 获取定制模型列表 | 1283-1286 | 42079-42199 | 102 | `chapters/volcengine/ark/14.7.4 获取定制模型列表.md` |
| 14.8.1 | 创建模型调优任务 | 1287-1297 | 42201-42524 | 279 | `chapters/volcengine/ark/14.8.1 创建模型调优任务.md` |
| 14.8.2 | 删除模型调优任务 | 1298 | 42525-42541 | 10 | `chapters/volcengine/ark/14.8.2 删除模型调优任务.md` |
| 14.8.3 | 获取模型调优任务信息 | 1299-1313 | 42542-43003 | 411 | `chapters/volcengine/ark/14.8.3 获取模型调优任务信息.md` |
| 14.8.4 | 查询精调效果指标详细数据 | 1314-1315 | 43004-43049 | 33 | `chapters/volcengine/ark/14.8.4 查询精调效果指标详细数据.md` |
| 14.8.5 | 查询精调效果指标 | 1316 | 43050-43068 | 10 | `chapters/volcengine/ark/14.8.5 查询精调效果指标.md` |
| 14.8.6 | 获取模型调优任务列表 | 1317-1325 | 43069-43343 | 246 | `chapters/volcengine/ark/14.8.6 获取模型调优任务列表.md` |
| 14.8.7 | 重试模型调优任务 | 1326 | 43344-43360 | 9 | `chapters/volcengine/ark/14.8.7 重试模型调优任务.md` |
| 14.8.8 | 停止模型调优任务 | 1327 | 43361-43377 | 10 | `chapters/volcengine/ark/14.8.8 停止模型调优任务.md` |
| 14.8.9 | 更新模型调优任务 | 1328 | 43378-43401 | 14 | `chapters/volcengine/ark/14.8.9 更新模型调优任务.md` |
| 14.9.1 | 开启推理接入点 | 1329 | 43403-43422 | 13 | `chapters/volcengine/ark/14.9.1 开启推理接入点.md` |
| 14.9.2 | 停止推理接入点 | 1330 | 43423-43443 | 11 | `chapters/volcengine/ark/14.9.2 停止推理接入点.md` |
| 14.9.3 | 获取推理接入点列表 | 1331-1336 | 43444-43656 | 168 | `chapters/volcengine/ark/14.9.3 获取推理接入点列表.md` |
| 14.9.4 | 获取推理接入点 | 1337-1340 | 43657-43760 | 88 | `chapters/volcengine/ark/14.9.4 获取推理接入点.md` |
| 14.9.5 | 删除推理接入点 | 1341 | 43761-43780 | 12 | `chapters/volcengine/ark/14.9.5 删除推理接入点.md` |
| 14.9.6 | 更新推理接入点 | 1342-1347 | 43781-43967 | 160 | `chapters/volcengine/ark/14.9.6 更新推理接入点.md` |
| 14.9.7 | 创建推理接入点 | 1348-1355 | 43968-44198 | 192 | `chapters/volcengine/ark/14.9.7 创建推理接入点.md` |
| 14.9.8 | 获取接入点推理应用层加密证书 | 1356-1357 | 44199-44234 | 23 | `chapters/volcengine/ark/14.9.8 获取接入点推理应用层加密证书.md` |
| 14.9.9 | 创建推理接入点滚动升级任务 | 1358-1359 | 44235-44282 | 41 | `chapters/volcengine/ark/14.9.9 创建推理接入点滚动升级任务.md` |
| 14.9.10 | 查询推理接入点滚动升级详情 | 1360-1364 | 44283-44411 | 116 | `chapters/volcengine/ark/14.9.10 查询推理接入点滚动升级详情.md` |
| 14.9.11 | 回滚推理接入点滚动升级 | 1365 | 44412-44429 | 13 | `chapters/volcengine/ark/14.9.11 回滚推理接入点滚动升级.md` |
| 14.9.12 | 取消推理接入点滚动升级 | 1366 | 44430-44447 | 13 | `chapters/volcengine/ark/14.9.12 取消推理接入点滚动升级.md` |
| 14.10.1 | 创建评测任务 | 1367-1371 | 44449-44614 | 131 | `chapters/volcengine/ark/14.10.1 创建评测任务.md` |
| 14.10.2 | 删除评测任务 | 1372 | 44615-44636 | 13 | `chapters/volcengine/ark/14.10.2 删除评测任务.md` |
| 14.10.3 | 获取评测任务 | 1373-1375 | 44637-44718 | 67 | `chapters/volcengine/ark/14.10.3 获取评测任务.md` |
| 14.10.4 | 获取评测任务结果 | 1376-1379 | 44719-44823 | 87 | `chapters/volcengine/ark/14.10.4 获取评测任务结果.md` |
| 14.10.5 | 获取评测任务列表 | 1380-1384 | 44824-44972 | 129 | `chapters/volcengine/ark/14.10.5 获取评测任务列表.md` |
| 14.10.6 | 获取评测任务结果列表 | 1385-1389 | 44973-45116 | 120 | `chapters/volcengine/ark/14.10.6 获取评测任务结果列表.md` |
| 14.10.7 | 停止评测任务 | 1390 | 45117-45138 | 13 | `chapters/volcengine/ark/14.10.7 停止评测任务.md` |
| 14.10.8 | 更新评测任务 | 1391 | 45139-45164 | 18 | `chapters/volcengine/ark/14.10.8 更新评测任务.md` |
| 14.11.1 | 查询推理用量 | 1392-1394 | 45166-45292 | 75 | `chapters/volcengine/ark/14.11.1 查询推理用量.md` |
| 14.11.2 | 查询单请求用量 | 1395-1399 | 45293-45433 | 124 | `chapters/volcengine/ark/14.11.2 查询单请求用量.md` |
| 14.11.3 | 查询异步任务用量 | 1400-1402 | 45434-45506 | 62 | `chapters/volcengine/ark/14.11.3 查询异步任务用量.md` |
| 14.11.4 | 创建用量明细导出任务 | 1403-1404 | 45507-45561 | 33 | `chapters/volcengine/ark/14.11.4 创建用量明细导出任务.md` |
| 14.11.5 | 查询用量明细导出任务状态 | 1405-1407 | 45562-45664 | 71 | `chapters/volcengine/ark/14.11.5 查询用量明细导出任务状态.md` |
| 14.11.6 | 查询模型推理限额 | 1408 | 45665-45692 | 22 | `chapters/volcengine/ark/14.11.6 查询模型推理限额.md` |
| 14.11.7 | 开启模型推理限额 | 1409 | 45693-45717 | 16 | `chapters/volcengine/ark/14.11.7 开启模型推理限额.md` |
| 14.11.8 | 关闭模型推理限额 | 1410 | 45718-45738 | 12 | `chapters/volcengine/ark/14.11.8 关闭模型推理限额.md` |
| 14.12.1 | 创建方舟官方模型产物查询请求 | 1411 | 45740-45758 | 14 | `chapters/volcengine/ark/14.12.1 创建方舟官方模型产物查询请求.md` |
| 14.12.2 | 获取安全审计日志 | 1412-1415 | 45759-45880 | 85 | `chapters/volcengine/ark/14.12.2 获取安全审计日志.md` |
| 14.12.3 | 获取方舟官方产物确认结果 | 1416-1417 | 45881-45912 | 24 | `chapters/volcengine/ark/14.12.3 获取方舟官方产物确认结果.md` |
| 14.13.1 | 上报视频生成模型效果问题 | 1418-1421 | 45914-46039 | 86 | `chapters/volcengine/ark/14.13.1 上报视频生成模型效果问题.md` |
| 14.13.2 | 查询视频生成模型效果问题结果 | 1422-1425 | 46040-46128 | 69 | `chapters/volcengine/ark/14.13.2 查询视频生成模型效果问题结果.md` |
| 14.13.3 | 上报大语言模型效果问题 | 1426-1428 | 46129-46237 | 81 | `chapters/volcengine/ark/14.13.3 上报大语言模型效果问题.md` |
| 14.13.4 | 查询大语言模型效果问题结果 | 1429-1432 | 46238-46355 | 97 | `chapters/volcengine/ark/14.13.4 查询大语言模型效果问题结果.md` |
| 15.1 | 兼容 OpenAI SDK | 1433-1436 | 46357-46473 | 103 | `chapters/volcengine/ark/15.1 兼容 OpenAI SDK.md` |
| 15.2 | 向后兼容性 | 1437 | 46474-46519 | 25 | `chapters/volcengine/ark/15.2 向后兼容性.md` |
| 15.3 | 错误码 - 第1部分 | 1437-1458 | 46520-48503 | 1936 | `chapters/volcengine/ark/15.3 错误码 - 第1部分.md` |
| 15.3 | 错误码 - 第2部分·错误码 | 1459-1468 | 48504-49278 | 751 | `chapters/volcengine/ark/15.3 错误码 - 第2部分·错误码.md` |
| 15.4 | SDK 常见使用示例 | 1469-1486 | 49279-49960 | 611 | `chapters/volcengine/ark/15.4 SDK 常见使用示例.md` |
