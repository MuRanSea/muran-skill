# 方舟 API 区章节表（ark）

来源：《火山方舟 API 参考》（1041 页）。185 个章节文件，接口级切分：一个接口/任务一个文件；超过 1500 行的按语义块自动再拆为`… - 第N部分`（5 个章节被拆分）。

「页码」是原 PDF 页码范围；「行范围」是中间 MD（`doc/<源文档>.md`）的 1 起始行号，可据此回查原文。章节文件本身已去掉页眉页脚，回查 PDF 时用这两列。文件名即章节标题，日常定位直接 Glob 文件名即可，用不到这两列。

**这张表用来 grep，不要整读。**

| 编号 | 标题 | 页码 | 行范围(源文件) | 行数 | 文件 |
|------|------|------|---------------|------|------|
| 1.1 | 获取 API Key 并配置 | 1 | 264-299 | 20 | `chapters/volcengine/ark/1.1 获取 API Key 并配置.md` |
| 1.2 | 安装及升级 SDK | 2-7 | 300-458 | 122 | `chapters/volcengine/ark/1.2 安装及升级 SDK.md` |
| 1.3 | Base URL及鉴权 | 8-10 | 459-554 | 68 | `chapters/volcengine/ark/1.3 Base URL及鉴权.md` |
| 2.1 | 对话(Chat) API | 11-37 | 556-1815 | 925 | `chapters/volcengine/ark/2.1 对话(Chat) API.md` |
| 3.1 | 创建 Response - 第1部分 | 38-76 | 1816-3513 | 1448 | `chapters/volcengine/ark/3.1 创建 Response - 第1部分.md` |
| 3.1 | 创建 Response - 第2部分·响应参数 | 77-108 | 3514-4868 | 1209 | `chapters/volcengine/ark/3.1 创建 Response - 第2部分·响应参数.md` |
| 3.2 | 查询 Response 详情 | 109-135 | 4869-6003 | 1062 | `chapters/volcengine/ark/3.2 查询 Response 详情.md` |
| 3.3 | 查询 Response 输入项列表 | 136-157 | 6004-6902 | 831 | `chapters/volcengine/ark/3.3 查询 Response 输入项列表.md` |
| 3.4 | 删除 Response | 158 | 6903-6926 | 19 | `chapters/volcengine/ark/3.4 删除 Response.md` |
| 3.5.1 | Response 生命周期 - 第1部分 | 159-196 | 6927-8576 | 1474 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第1部分.md` |
| 3.5.1 | Response 生命周期 - 第2部分 | 197-234 | 8577-10240 | 1489 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第2部分.md` |
| 3.5.1 | Response 生命周期 - 第3部分 | 235-272 | 10241-11891 | 1483 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第3部分.md` |
| 3.5.1 | Response 生命周期 - 第4部分 | 273-319 | 11892-13909 | 1778 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第4部分.md` |
| 3.5.2 | Output Item 与文本回答 - 第1部分 | 320-355 | 13910-15484 | 1447 | `chapters/volcengine/ark/3.5.2 Output Item 与文本回答 - 第1部分.md` |
| 3.5.2 | Output Item 与文本回答 - 第2部分 | 356-371 | 15485-16131 | 615 | `chapters/volcengine/ark/3.5.2 Output Item 与文本回答 - 第2部分.md` |
| 3.5.3 | 工具调用事件 | 372-398 | 16132-17212 | 1024 | `chapters/volcengine/ark/3.5.3 工具调用事件.md` |
| 3.5.4 | 语音转写与错误事件 | 399-403 | 17213-17383 | 161 | `chapters/volcengine/ark/3.5.4 语音转写与错误事件.md` |
| 4.1 | 创建 Message | 404-419 | 17385-18029 | 567 | `chapters/volcengine/ark/4.1 创建 Message.md` |
| 4.2 | 统计 Messages 请求 token 数 | 420-427 | 18030-18366 | 282 | `chapters/volcengine/ark/4.2 统计 Messages 请求 token 数.md` |
| 5.1 | 上传文件 | 428-433 | 18368-18582 | 159 | `chapters/volcengine/ark/5.1 上传文件.md` |
| 5.2 | 查询文件详情 | 434-435 | 18583-18650 | 60 | `chapters/volcengine/ark/5.2 查询文件详情.md` |
| 5.3 | 查询文件列表 | 436-439 | 18651-18784 | 112 | `chapters/volcengine/ark/5.3 查询文件列表.md` |
| 5.4 | 删除文件 | 440 | 18785-18807 | 19 | `chapters/volcengine/ark/5.4 删除文件.md` |
| 5.5 | The file object | 441-443 | 18808-18879 | 57 | `chapters/volcengine/ark/5.5 The file object.md` |
| 6.1 | 创建视频生成任务 | 444-460 | 18881-19725 | 591 | `chapters/volcengine/ark/6.1 创建视频生成任务.md` |
| 6.2 | 查询视频生成任务 | 461-464 | 19726-19863 | 103 | `chapters/volcengine/ark/6.2 查询视频生成任务.md` |
| 6.3 | 查询视频生成任务列表 | 465-469 | 19864-20062 | 153 | `chapters/volcengine/ark/6.3 查询视频生成任务列表.md` |
| 6.4 | 取消或删除视频生成任务 | 470 | 20063-20104 | 38 | `chapters/volcengine/ark/6.4 取消或删除视频生成任务.md` |
| 7.1 | 图片生成 API | 471-487 | 20106-20839 | 520 | `chapters/volcengine/ark/7.1 图片生成 API.md` |
| 7.2 | 图片生成流式响应事件 | 488-492 | 20840-21014 | 157 | `chapters/volcengine/ark/7.2 图片生成流式响应事件.md` |
| 8.1.1 | 创建 3D 生成任务 API | 493-496 | 21017-21146 | 100 | `chapters/volcengine/ark/8.1.1 创建 3D 生成任务 API.md` |
| 8.1.2 | 查询 3D 生成任务 API | 497-498 | 21147-21216 | 52 | `chapters/volcengine/ark/8.1.2 查询 3D 生成任务 API.md` |
| 8.1.3 | 查询 3D 生成任务列表 | 499-501 | 21217-21330 | 87 | `chapters/volcengine/ark/8.1.3 查询 3D 生成任务列表.md` |
| 8.1.4 | 取消或删除 3D 生成任务 | 502 | 21331-21372 | 38 | `chapters/volcengine/ark/8.1.4 取消或删除 3D 生成任务.md` |
| 8.2.1 | 创建3D生成任务 | 503-507 | 21374-21588 | 148 | `chapters/volcengine/ark/8.2.1 创建3D生成任务.md` |
| 8.2.2 | 查询3D生成任务 | 508-509 | 21589-21654 | 48 | `chapters/volcengine/ark/8.2.2 查询3D生成任务.md` |
| 8.2.3 | 查询3D生成任务列表 | 510-512 | 21655-21762 | 81 | `chapters/volcengine/ark/8.2.3 查询3D生成任务列表.md` |
| 8.2.4 | 取消或删除3D生成任务 | 513 | 21763-21797 | 31 | `chapters/volcengine/ark/8.2.4 取消或删除3D生成任务.md` |
| 8.3.1 | 创建3D生成任务 | 514-517 | 21799-21930 | 95 | `chapters/volcengine/ark/8.3.1 创建3D生成任务.md` |
| 8.3.2 | 查询3D生成任务 | 518-519 | 21931-21996 | 48 | `chapters/volcengine/ark/8.3.2 查询3D生成任务.md` |
| 8.3.3 | 查询3D生成任务列表 | 520-522 | 21997-22104 | 81 | `chapters/volcengine/ark/8.3.3 查询3D生成任务列表.md` |
| 8.3.4 | 取消或删除3D生成任务 | 523 | 22105-22139 | 31 | `chapters/volcengine/ark/8.3.4 取消或删除3D生成任务.md` |
| 9.1 | 多模态向量化 API | 524-528 | 22141-22339 | 147 | `chapters/volcengine/ark/9.1 多模态向量化 API.md` |
| 10.1 | 创建上下文缓存 API | 529-535 | 22341-22511 | 134 | `chapters/volcengine/ark/10.1 创建上下文缓存 API.md` |
| 10.2 | 上下文缓存对话 API | 536-552 | 22512-23000 | 386 | `chapters/volcengine/ark/10.2 上下文缓存对话 API.md` |
| 11.1.1 | 创建智能体 | 553-560 | 23003-23325 | 245 | `chapters/volcengine/ark/11.1.1 创建智能体.md` |
| 11.1.2 | 查询智能体列表 | 561-565 | 23326-23490 | 135 | `chapters/volcengine/ark/11.1.2 查询智能体列表.md` |
| 11.1.3 | 查询智能体详情 | 566-569 | 23491-23637 | 120 | `chapters/volcengine/ark/11.1.3 查询智能体详情.md` |
| 11.1.4 | 更新智能体 | 570-576 | 23638-23899 | 205 | `chapters/volcengine/ark/11.1.4 更新智能体.md` |
| 11.1.5 | 删除智能体 | 577 | 23900-23917 | 13 | `chapters/volcengine/ark/11.1.5 删除智能体.md` |
| 11.1.6 | 查询智能体版本列表 | 578-582 | 23918-24083 | 138 | `chapters/volcengine/ark/11.1.6 查询智能体版本列表.md` |
| 11.2.1 | 创建环境 | 583-587 | 24085-24293 | 169 | `chapters/volcengine/ark/11.2.1 创建环境.md` |
| 11.2.2 | 查询环境列表 | 588-591 | 24294-24416 | 104 | `chapters/volcengine/ark/11.2.2 查询环境列表.md` |
| 11.2.3 | 查询环境详情 | 592-594 | 24417-24521 | 88 | `chapters/volcengine/ark/11.2.3 查询环境详情.md` |
| 11.2.4 | 更新环境 | 595-599 | 24522-24729 | 168 | `chapters/volcengine/ark/11.2.4 更新环境.md` |
| 11.2.5 | 删除环境 | 600 | 24730-24747 | 14 | `chapters/volcengine/ark/11.2.5 删除环境.md` |
| 11.2.6.1 | 长轮询拉取 work | 601-602 | 24749-24823 | 61 | `chapters/volcengine/ark/11.2.6.1 长轮询拉取 work.md` |
| 11.2.6.2 | 认领 work | 603-604 | 24824-24892 | 57 | `chapters/volcengine/ark/11.2.6.2 认领 work.md` |
| 11.2.6.3 | 查询 work 列表 | 605-607 | 24893-24978 | 74 | `chapters/volcengine/ark/11.2.6.3 查询 work 列表.md` |
| 11.2.6.4 | 查询单个 work | 608-609 | 24979-25042 | 53 | `chapters/volcengine/ark/11.2.6.4 查询单个 work.md` |
| 11.2.6.5 | 心跳续租 | 610-611 | 25043-25078 | 28 | `chapters/volcengine/ark/11.2.6.5 心跳续租.md` |
| 11.2.6.6 | 停止 work | 612-613 | 25079-25147 | 56 | `chapters/volcengine/ark/11.2.6.6 停止 work.md` |
| 11.2.6.7 | 查询队列水位 | 614 | 25148-25171 | 20 | `chapters/volcengine/ark/11.2.6.7 查询队列水位.md` |
| 11.3.1 | 创建会话 | 615-621 | 25173-25458 | 246 | `chapters/volcengine/ark/11.3.1 创建会话.md` |
| 11.3.2 | 查询会话列表 | 622-626 | 25459-25626 | 154 | `chapters/volcengine/ark/11.3.2 查询会话列表.md` |
| 11.3.3 | 查询会话详情 | 627-630 | 25627-25751 | 113 | `chapters/volcengine/ark/11.3.3 查询会话详情.md` |
| 11.3.4 | 更新会话 | 631-633 | 25752-25829 | 68 | `chapters/volcengine/ark/11.3.4 更新会话.md` |
| 11.3.5 | 升级会话 | 634-647 | 25830-26338 | 464 | `chapters/volcengine/ark/11.3.5 升级会话.md` |
| 11.3.6 | 删除会话 | 648 | 26339-26357 | 15 | `chapters/volcengine/ark/11.3.6 删除会话.md` |
| 11.3.7.1 | 发送会话事件 | 649-650 | 26359-26409 | 30 | `chapters/volcengine/ark/11.3.7.1 发送会话事件.md` |
| 11.3.7.2 | 查询会话事件列表 | 651-652 | 26410-26473 | 49 | `chapters/volcengine/ark/11.3.7.2 查询会话事件列表.md` |
| 11.3.7.3 | 流式获取会话事件 | 653-654 | 26474-26517 | 25 | `chapters/volcengine/ark/11.3.7.3 流式获取会话事件.md` |
| 11.3.7.4 | 会话事件结构参考 - 第1部分 | 655-697 | 26518-28183 | 1555 | `chapters/volcengine/ark/11.3.7.4 会话事件结构参考 - 第1部分.md` |
| 11.3.8.1 | 添加会话资源 | 698-699 | 28185-28225 | 31 | `chapters/volcengine/ark/11.3.8.1 添加会话资源.md` |
| 11.3.8.2 | 查询会话资源列表 | 700-701 | 28226-28277 | 45 | `chapters/volcengine/ark/11.3.8.2 查询会话资源列表.md` |
| 11.3.8.3 | 查询会话资源 | 702-703 | 28278-28316 | 32 | `chapters/volcengine/ark/11.3.8.3 查询会话资源.md` |
| 11.3.9.1 | 查询线程列表 | 704-705 | 28318-28381 | 53 | `chapters/volcengine/ark/11.3.9.1 查询线程列表.md` |
| 11.3.9.2 | 查询线程详情 | 706-707 | 28382-28427 | 34 | `chapters/volcengine/ark/11.3.9.2 查询线程详情.md` |
| 11.3.9.3 | 查询线程事件列表 | 708-709 | 28428-28495 | 54 | `chapters/volcengine/ark/11.3.9.3 查询线程事件列表.md` |
| 11.3.9.4 | 流式获取线程事件 | 710 | 28496-28532 | 22 | `chapters/volcengine/ark/11.3.9.4 流式获取线程事件.md` |
| 11.4.1 | 创建保管库 | 711 | 28534-28566 | 28 | `chapters/volcengine/ark/11.4.1 创建保管库.md` |
| 11.4.2 | 查询保管库列表 | 712-713 | 28567-28607 | 36 | `chapters/volcengine/ark/11.4.2 查询保管库列表.md` |
| 11.4.3 | 查询保管库详情 | 714 | 28608-28634 | 23 | `chapters/volcengine/ark/11.4.3 查询保管库详情.md` |
| 11.4.4 | 更新保管库 | 715-716 | 28635-28671 | 29 | `chapters/volcengine/ark/11.4.4 更新保管库.md` |
| 11.4.5 | 删除保管库 | 717 | 28672-28692 | 17 | `chapters/volcengine/ark/11.4.5 删除保管库.md` |
| 11.4.6.1 | 创建凭证 | 718-724 | 28694-28952 | 212 | `chapters/volcengine/ark/11.4.6.1 创建凭证.md` |
| 11.4.6.2 | 查询凭证列表 | 725-728 | 28953-29080 | 109 | `chapters/volcengine/ark/11.4.6.2 查询凭证列表.md` |
| 11.4.6.3 | 查询凭证详情 | 729-731 | 29081-29195 | 95 | `chapters/volcengine/ark/11.4.6.3 查询凭证详情.md` |
| 11.4.6.4 | 更新凭证 | 732-737 | 29196-29442 | 219 | `chapters/volcengine/ark/11.4.6.4 更新凭证.md` |
| 11.4.6.5 | 删除凭证 | 738 | 29443-29465 | 17 | `chapters/volcengine/ark/11.4.6.5 删除凭证.md` |
| 11.5.1 | 创建记忆库 | 739-740 | 29467-29515 | 43 | `chapters/volcengine/ark/11.5.1 创建记忆库.md` |
| 11.5.2 | 查询记忆库列表 | 741-742 | 29516-29582 | 61 | `chapters/volcengine/ark/11.5.2 查询记忆库列表.md` |
| 11.5.3 | 查询记忆库详情 | 743-744 | 29583-29627 | 39 | `chapters/volcengine/ark/11.5.3 查询记忆库详情.md` |
| 11.5.4 | 更新记忆库 | 745-746 | 29628-29679 | 45 | `chapters/volcengine/ark/11.5.4 更新记忆库.md` |
| 11.5.5 | 删除记忆库 | 747 | 29680-29698 | 14 | `chapters/volcengine/ark/11.5.5 删除记忆库.md` |
| 11.5.6.1 | 创建记忆 | 748-749 | 29700-29749 | 43 | `chapters/volcengine/ark/11.5.6.1 创建记忆.md` |
| 11.5.6.2 | 批量创建记忆 | 750-752 | 29750-29851 | 82 | `chapters/volcengine/ark/11.5.6.2 批量创建记忆.md` |
| 11.5.6.3 | 查询记忆列表 | 753-754 | 29852-29918 | 56 | `chapters/volcengine/ark/11.5.6.3 查询记忆列表.md` |
| 11.5.6.4 | 查询记忆详情 | 755-756 | 29919-29967 | 40 | `chapters/volcengine/ark/11.5.6.4 查询记忆详情.md` |
| 11.5.6.5 | 更新记忆 | 757-758 | 29968-30021 | 44 | `chapters/volcengine/ark/11.5.6.5 更新记忆.md` |
| 11.5.6.6 | 删除记忆 | 759 | 30022-30043 | 16 | `chapters/volcengine/ark/11.5.6.6 删除记忆.md` |
| 11.6.1 | 创建技能 | 760-761 | 30045-30094 | 37 | `chapters/volcengine/ark/11.6.1 创建技能.md` |
| 11.6.2 | 查询技能详情 | 762-763 | 30095-30146 | 44 | `chapters/volcengine/ark/11.6.2 查询技能详情.md` |
| 12.1 | 应用(bot) API | 764-776 | 30148-30916 | 537 | `chapters/volcengine/ark/12.1 应用(bot) API.md` |
| 12.2 | 智能体插件 API | 777-781 | 30917-31125 | 195 | `chapters/volcengine/ark/12.2 智能体插件 API.md` |
| 12.3 | 联网插件 数据结构 | 782-784 | 31126-31210 | 79 | `chapters/volcengine/ark/12.3 联网插件 数据结构.md` |
| 12.4 | 知识库插件 数据结构 | 785 | 31211-31233 | 13 | `chapters/volcengine/ark/12.4 知识库插件 数据结构.md` |
| 13.1.1 | 创建批量推理任务 | 786-789 | 31236-31316 | 60 | `chapters/volcengine/ark/13.1.1 创建批量推理任务.md` |
| 13.1.2 | 获取批量推理任务列表 | 790-794 | 31317-31490 | 152 | `chapters/volcengine/ark/13.1.2 获取批量推理任务列表.md` |
| 13.1.3 | 获取批量推理任务 | 795-797 | 31491-31608 | 102 | `chapters/volcengine/ark/13.1.3 获取批量推理任务.md` |
| 13.1.4 | 更新批量推理任务 | 798 | 31609-31632 | 17 | `chapters/volcengine/ark/13.1.4 更新批量推理任务.md` |
| 13.1.5 | 删除批量推理任务 | 799 | 31633-31652 | 13 | `chapters/volcengine/ark/13.1.5 删除批量推理任务.md` |
| 13.1.6 | 停止批量推理任务 | 800 | 31653-31675 | 16 | `chapters/volcengine/ark/13.1.6 停止批量推理任务.md` |
| 13.1.7 | 重启批量推理任务 | 801 | 31676-31696 | 13 | `chapters/volcengine/ark/13.1.7 重启批量推理任务.md` |
| 13.2 | 批量(Chat) API | 802-816 | 31697-32137 | 339 | `chapters/volcengine/ark/13.2 批量(Chat) API.md` |
| 14.1 | 分词 API | 817-818 | 32139-32185 | 39 | `chapters/volcengine/ark/14.1 分词 API.md` |
| 15.1.1 | 获取临时 API Key | 819 | 32188-32222 | 26 | `chapters/volcengine/ark/15.1.1 获取临时 API Key.md` |
| 15.2.1 | 创建个人版套餐 | 820-821 | 32224-32282 | 34 | `chapters/volcengine/ark/15.2.1 创建个人版套餐.md` |
| 15.2.2 | 续费个人版套餐 | 822-823 | 32283-32328 | 27 | `chapters/volcengine/ark/15.2.2 续费个人版套餐.md` |
| 15.2.3 | 查询个人版套餐 | 824 | 32329-32356 | 21 | `chapters/volcengine/ark/15.2.3 查询个人版套餐.md` |
| 15.2.4.1 | 查询 Agent Plan 支持的模型列表 | 825 | 32358-32377 | 14 | `chapters/volcengine/ark/15.2.4.1 查询 Agent Plan 支持的模型列表.md` |
| 15.2.4.2 | 轮换个人版 API Key | 826 | 32378-32404 | 17 | `chapters/volcengine/ark/15.2.4.2 轮换个人版 API Key.md` |
| 15.2.4.3 | 获取套餐 AFP 额度 | 827-828 | 32405-32479 | 66 | `chapters/volcengine/ark/15.2.4.3 获取套餐 AFP 额度.md` |
| 15.2.4.4 | 获取套餐用量详情 | 829-830 | 32480-32528 | 39 | `chapters/volcengine/ark/15.2.4.4 获取套餐用量详情.md` |
| 15.2.5.1 | 查询 Coding Plan 支持的模型列表 | 831 | 32530-32545 | 12 | `chapters/volcengine/ark/15.2.5.1 查询 Coding Plan 支持的模型列表.md` |
| 15.3.1 | 批量开通基础模型 | 832 | 32547-32561 | 11 | `chapters/volcengine/ark/15.3.1 批量开通基础模型.md` |
| 15.3.2 | 启用自动开通新模型 | 833 | 32562-32573 | 7 | `chapters/volcengine/ark/15.3.2 启用自动开通新模型.md` |
| 15.3.3 | 关闭自动开通新模型 | 834 | 32574-32585 | 7 | `chapters/volcengine/ark/15.3.3 关闭自动开通新模型.md` |
| 15.3.4 | 查询模型开通详情 | 835-838 | 32586-32728 | 131 | `chapters/volcengine/ark/15.3.4 查询模型开通详情.md` |
| 15.3.5 | 查询模型开通列表 | 839-843 | 32729-32906 | 163 | `chapters/volcengine/ark/15.3.5 查询模型开通列表.md` |
| 15.4.1 | 批量开通资源 | 844 | 32908-32926 | 14 | `chapters/volcengine/ark/15.4.1 批量开通资源.md` |
| 15.4.2 | 查询资源开通列表 | 845-847 | 32927-33028 | 92 | `chapters/volcengine/ark/15.4.2 查询资源开通列表.md` |
| 15.5.1 | 创建模型调优任务 | 848-855 | 33030-33348 | 281 | `chapters/volcengine/ark/15.5.1 创建模型调优任务.md` |
| 15.5.2 | 删除模型调优任务 | 856 | 33349-33365 | 10 | `chapters/volcengine/ark/15.5.2 删除模型调优任务.md` |
| 15.5.3 | 获取模型调优任务信息 | 857-867 | 33366-33819 | 411 | `chapters/volcengine/ark/15.5.3 获取模型调优任务信息.md` |
| 15.5.4 | 查询精调效果指标详细数据 | 868-869 | 33820-33865 | 33 | `chapters/volcengine/ark/15.5.4 查询精调效果指标详细数据.md` |
| 15.5.5 | 查询精调效果指标 | 870 | 33866-33884 | 10 | `chapters/volcengine/ark/15.5.5 查询精调效果指标.md` |
| 15.5.6 | 获取模型调优任务列表 | 871-877 | 33885-34155 | 246 | `chapters/volcengine/ark/15.5.6 获取模型调优任务列表.md` |
| 15.5.7 | 重试模型调优任务 | 878 | 34156-34172 | 9 | `chapters/volcengine/ark/15.5.7 重试模型调优任务.md` |
| 15.5.8 | 停止模型调优任务 | 879 | 34173-34189 | 10 | `chapters/volcengine/ark/15.5.8 停止模型调优任务.md` |
| 15.5.9 | 更新模型调优任务 | 880 | 34190-34213 | 14 | `chapters/volcengine/ark/15.5.9 更新模型调优任务.md` |
| 15.6.1 | 创建评测任务 | 881-884 | 34215-34380 | 133 | `chapters/volcengine/ark/15.6.1 创建评测任务.md` |
| 15.6.2 | 删除评测任务 | 885 | 34381-34402 | 13 | `chapters/volcengine/ark/15.6.2 删除评测任务.md` |
| 15.6.3 | 获取评测任务 | 886-888 | 34403-34484 | 66 | `chapters/volcengine/ark/15.6.3 获取评测任务.md` |
| 15.6.4 | 获取评测任务结果 | 889-891 | 34485-34587 | 87 | `chapters/volcengine/ark/15.6.4 获取评测任务结果.md` |
| 15.6.5 | 获取评测任务列表 | 892-895 | 34588-34734 | 129 | `chapters/volcengine/ark/15.6.5 获取评测任务列表.md` |
| 15.6.6 | 获取评测任务结果列表 | 896-899 | 34735-34876 | 120 | `chapters/volcengine/ark/15.6.6 获取评测任务结果列表.md` |
| 15.6.7 | 停止评测任务 | 900 | 34877-34898 | 13 | `chapters/volcengine/ark/15.6.7 停止评测任务.md` |
| 15.6.8 | 更新评测任务 | 901 | 34899-34924 | 18 | `chapters/volcengine/ark/15.6.8 更新评测任务.md` |
| 15.7.1 | 开启推理接入点 | 902 | 34926-34946 | 13 | `chapters/volcengine/ark/15.7.1 开启推理接入点.md` |
| 15.7.2 | 停止推理接入点 | 903 | 34947-34967 | 11 | `chapters/volcengine/ark/15.7.2 停止推理接入点.md` |
| 15.7.3 | 获取推理接入点列表 | 904-908 | 34968-35179 | 170 | `chapters/volcengine/ark/15.7.3 获取推理接入点列表.md` |
| 15.7.4 | 获取推理接入点 | 909-911 | 35180-35281 | 88 | `chapters/volcengine/ark/15.7.4 获取推理接入点.md` |
| 15.7.5 | 删除推理接入点 | 912 | 35282-35301 | 12 | `chapters/volcengine/ark/15.7.5 删除推理接入点.md` |
| 15.7.6 | 更新推理接入点 | 913-917 | 35302-35486 | 160 | `chapters/volcengine/ark/15.7.6 更新推理接入点.md` |
| 15.7.7 | 创建推理接入点 | 918-923 | 35487-35714 | 193 | `chapters/volcengine/ark/15.7.7 创建推理接入点.md` |
| 15.7.8 | 获取接入点推理应用层加密证书 | 924-925 | 35715-35750 | 23 | `chapters/volcengine/ark/15.7.8 获取接入点推理应用层加密证书.md` |
| 15.7.9 | 创建推理接入点滚动升级任务 | 926-927 | 35751-35798 | 41 | `chapters/volcengine/ark/15.7.9 创建推理接入点滚动升级任务.md` |
| 15.7.10 | 查询推理接入点滚动升级详情 | 928-931 | 35799-35925 | 116 | `chapters/volcengine/ark/15.7.10 查询推理接入点滚动升级详情.md` |
| 15.7.11 | 回滚推理接入点滚动升级 | 932 | 35926-35943 | 13 | `chapters/volcengine/ark/15.7.11 回滚推理接入点滚动升级.md` |
| 15.7.12 | 取消推理接入点滚动升级 | 933 | 35944-35961 | 13 | `chapters/volcengine/ark/15.7.12 取消推理接入点滚动升级.md` |
| 15.8.1 | 删除定制模型 | 934 | 35963-35988 | 17 | `chapters/volcengine/ark/15.8.1 删除定制模型.md` |
| 15.8.2 | 获取定制模型信息 | 935-937 | 35989-36097 | 97 | `chapters/volcengine/ark/15.8.2 获取定制模型信息.md` |
| 15.8.3 | 更新定制模型 | 938 | 36098-36130 | 22 | `chapters/volcengine/ark/15.8.3 更新定制模型.md` |
| 15.8.4 | 获取定制模型列表 | 939-941 | 36131-36249 | 102 | `chapters/volcengine/ark/15.8.4 获取定制模型列表.md` |
| 15.9.1 | 获取基础模型版本列表 | 942-944 | 36251-36338 | 72 | `chapters/volcengine/ark/15.9.1 获取基础模型版本列表.md` |
| 15.9.2 | 获取基础模型版本信息 | 945-952 | 36339-36656 | 273 | `chapters/volcengine/ark/15.9.2 获取基础模型版本信息.md` |
| 15.9.3 | 获取基础模型列表 | 953-957 | 36657-36901 | 182 | `chapters/volcengine/ark/15.9.3 获取基础模型列表.md` |
| 15.9.4 | 获取基础模型信息 | 958-960 | 36902-37026 | 93 | `chapters/volcengine/ark/15.9.4 获取基础模型信息.md` |
| 15.10.1 | 查询模型限流 | 961-963 | 37028-37127 | 91 | `chapters/volcengine/ark/15.10.1 查询模型限流.md` |
| 15.11.1 | 创建方舟官方模型产物查询请求 | 964 | 37129-37147 | 14 | `chapters/volcengine/ark/15.11.1 创建方舟官方模型产物查询请求.md` |
| 15.11.2 | 获取安全审计日志 | 965-967 | 37148-37267 | 85 | `chapters/volcengine/ark/15.11.2 获取安全审计日志.md` |
| 15.11.3 | 获取方舟官方产物确认结果 | 968 | 37268-37297 | 24 | `chapters/volcengine/ark/15.11.3 获取方舟官方产物确认结果.md` |
| 15.12.1 | 查询推理用量 | 969-971 | 37299-37426 | 75 | `chapters/volcengine/ark/15.12.1 查询推理用量.md` |
| 15.12.2 | 创建用量明细导出任务 | 972-973 | 37427-37479 | 33 | `chapters/volcengine/ark/15.12.2 创建用量明细导出任务.md` |
| 15.12.3 | 查询用量明细导出任务状态 | 974-976 | 37480-37582 | 71 | `chapters/volcengine/ark/15.12.3 查询用量明细导出任务状态.md` |
| 15.13.1 | 上报视频生成模型效果问题 | 977-979 | 37584-37707 | 86 | `chapters/volcengine/ark/15.13.1 上报视频生成模型效果问题.md` |
| 15.13.2 | 查询视频生成模型效果问题结果 | 980-983 | 37708-37796 | 69 | `chapters/volcengine/ark/15.13.2 查询视频生成模型效果问题结果.md` |
| 15.13.3 | 上报大语言模型效果问题 | 984-986 | 37797-37905 | 82 | `chapters/volcengine/ark/15.13.3 上报大语言模型效果问题.md` |
| 15.13.4 | 查询大语言模型效果问题结果 | 987-989 | 37906-38021 | 97 | `chapters/volcengine/ark/15.13.4 查询大语言模型效果问题结果.md` |
| 16.1 | 兼容 OpenAI SDK | 990-993 | 38023-38139 | 103 | `chapters/volcengine/ark/16.1 兼容 OpenAI SDK.md` |
| 16.2 | 向后兼容性 | 994 | 38140-38185 | 25 | `chapters/volcengine/ark/16.2 向后兼容性.md` |
| 16.3 | 错误码 - 第1部分 | 994-1016 | 38186-40143 | 1908 | `chapters/volcengine/ark/16.3 错误码 - 第1部分.md` |
| 16.3 | 错误码 - 第2部分·错误码 | 1017-1024 | 40144-40725 | 552 | `chapters/volcengine/ark/16.3 错误码 - 第2部分·错误码.md` |
| 16.4 | SDK 常见使用示例 | 1025-1041 | 40726-41334 | 538 | `chapters/volcengine/ark/16.4 SDK 常见使用示例.md` |
