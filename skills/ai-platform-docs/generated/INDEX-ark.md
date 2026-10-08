# 方舟 API 区章节表（ark）

来源：《火山方舟 API 参考》（1068 页）。192 个章节文件，接口级切分：一个接口/任务一个文件；超过 1500 行的按语义块自动再拆为`… - 第N部分`（5 个章节被拆分）。

「页码」是原 PDF 页码范围；「行范围」是中间 MD（`doc/<源文档>.md`）的 1 起始行号，可据此回查原文。章节文件本身已去掉页眉页脚，回查 PDF 时用这两列。文件名即章节标题，日常定位直接 Glob 文件名即可，用不到这两列。

**这张表用来 grep，不要整读。**

| 编号 | 标题 | 页码 | 行范围(源文件) | 行数 | 文件 |
|------|------|------|---------------|------|------|
| 1.1 | 获取 API Key 并配置 | 1 | 269-304 | 20 | `chapters/volcengine/ark/1.1 获取 API Key 并配置.md` |
| 1.2 | 安装及升级 SDK | 2-7 | 305-463 | 122 | `chapters/volcengine/ark/1.2 安装及升级 SDK.md` |
| 1.3 | Base URL及鉴权 | 8-10 | 464-559 | 68 | `chapters/volcengine/ark/1.3 Base URL及鉴权.md` |
| 2.1 | 对话(Chat) API | 11-37 | 561-1801 | 916 | `chapters/volcengine/ark/2.1 对话(Chat) API.md` |
| 3.1 | 创建 Response - 第1部分 | 38-76 | 1802-3483 | 1441 | `chapters/volcengine/ark/3.1 创建 Response - 第1部分.md` |
| 3.1 | 创建 Response - 第2部分·响应参数 | 77-108 | 3484-4838 | 1209 | `chapters/volcengine/ark/3.1 创建 Response - 第2部分·响应参数.md` |
| 3.2 | 查询 Response 详情 | 109-135 | 4839-5973 | 1062 | `chapters/volcengine/ark/3.2 查询 Response 详情.md` |
| 3.3 | 查询 Response 输入项列表 | 136-157 | 5974-6872 | 831 | `chapters/volcengine/ark/3.3 查询 Response 输入项列表.md` |
| 3.4 | 删除 Response | 158 | 6873-6896 | 19 | `chapters/volcengine/ark/3.4 删除 Response.md` |
| 3.5.1 | Response 生命周期 - 第1部分 | 159-196 | 6897-8546 | 1474 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第1部分.md` |
| 3.5.1 | Response 生命周期 - 第2部分 | 197-234 | 8547-10210 | 1489 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第2部分.md` |
| 3.5.1 | Response 生命周期 - 第3部分 | 235-272 | 10211-11861 | 1483 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第3部分.md` |
| 3.5.1 | Response 生命周期 - 第4部分 | 273-319 | 11862-13879 | 1778 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第4部分.md` |
| 3.5.2 | Output Item 与文本回答 - 第1部分 | 320-355 | 13880-15454 | 1447 | `chapters/volcengine/ark/3.5.2 Output Item 与文本回答 - 第1部分.md` |
| 3.5.2 | Output Item 与文本回答 - 第2部分 | 356-371 | 15455-16101 | 615 | `chapters/volcengine/ark/3.5.2 Output Item 与文本回答 - 第2部分.md` |
| 3.5.3 | 工具调用事件 | 372-398 | 16102-17182 | 1024 | `chapters/volcengine/ark/3.5.3 工具调用事件.md` |
| 3.5.4 | 语音转写与错误事件 | 399-403 | 17183-17353 | 161 | `chapters/volcengine/ark/3.5.4 语音转写与错误事件.md` |
| 4.1 | 创建 Message | 404-419 | 17355-17996 | 564 | `chapters/volcengine/ark/4.1 创建 Message.md` |
| 4.2 | 统计 Messages 请求 token 数 | 420-427 | 17997-18330 | 279 | `chapters/volcengine/ark/4.2 统计 Messages 请求 token 数.md` |
| 5.1 | 上传文件 | 428-433 | 18332-18546 | 159 | `chapters/volcengine/ark/5.1 上传文件.md` |
| 5.2 | 查询文件详情 | 434-435 | 18547-18614 | 60 | `chapters/volcengine/ark/5.2 查询文件详情.md` |
| 5.3 | 查询文件列表 | 436-439 | 18615-18745 | 109 | `chapters/volcengine/ark/5.3 查询文件列表.md` |
| 5.4 | 删除文件 | 440 | 18746-18768 | 19 | `chapters/volcengine/ark/5.4 删除文件.md` |
| 5.5 | The file object | 441-443 | 18769-18840 | 57 | `chapters/volcengine/ark/5.5 The file object.md` |
| 6.1 | 创建视频生成任务 | 444-460 | 18842-19716 | 609 | `chapters/volcengine/ark/6.1 创建视频生成任务.md` |
| 6.2 | 查询视频生成任务 | 461-464 | 19717-19857 | 105 | `chapters/volcengine/ark/6.2 查询视频生成任务.md` |
| 6.3 | 查询视频生成任务列表 | 465-469 | 19858-20060 | 156 | `chapters/volcengine/ark/6.3 查询视频生成任务列表.md` |
| 6.4 | 取消或删除视频生成任务 | 470 | 20061-20102 | 38 | `chapters/volcengine/ark/6.4 取消或删除视频生成任务.md` |
| 7.1 | 图片生成 API | 471-487 | 20104-20857 | 530 | `chapters/volcengine/ark/7.1 图片生成 API.md` |
| 7.2 | 图片生成流式响应事件 | 488-492 | 20858-21034 | 158 | `chapters/volcengine/ark/7.2 图片生成流式响应事件.md` |
| 8.1.1 | 创建 3D 生成任务 API | 493-495 | 21037-21140 | 80 | `chapters/volcengine/ark/8.1.1 创建 3D 生成任务 API.md` |
| 8.1.2 | 查询 3D 生成任务 API | 496-497 | 21141-21210 | 52 | `chapters/volcengine/ark/8.1.2 查询 3D 生成任务 API.md` |
| 8.1.3 | 查询 3D 生成任务列表 | 498-500 | 21211-21324 | 87 | `chapters/volcengine/ark/8.1.3 查询 3D 生成任务列表.md` |
| 8.1.4 | 取消或删除 3D 生成任务 | 501 | 21325-21366 | 38 | `chapters/volcengine/ark/8.1.4 取消或删除 3D 生成任务.md` |
| 8.2.1 | 创建3D生成任务 | 502-506 | 21368-21582 | 148 | `chapters/volcengine/ark/8.2.1 创建3D生成任务.md` |
| 8.2.2 | 查询3D生成任务 | 507-508 | 21583-21648 | 48 | `chapters/volcengine/ark/8.2.2 查询3D生成任务.md` |
| 8.2.3 | 查询3D生成任务列表 | 509-511 | 21649-21756 | 81 | `chapters/volcengine/ark/8.2.3 查询3D生成任务列表.md` |
| 8.2.4 | 取消或删除3D生成任务 | 512 | 21757-21791 | 31 | `chapters/volcengine/ark/8.2.4 取消或删除3D生成任务.md` |
| 8.3.1 | 创建3D生成任务 | 513-516 | 21793-21924 | 95 | `chapters/volcengine/ark/8.3.1 创建3D生成任务.md` |
| 8.3.2 | 查询3D生成任务 | 517-518 | 21925-21990 | 48 | `chapters/volcengine/ark/8.3.2 查询3D生成任务.md` |
| 8.3.3 | 查询3D生成任务列表 | 519-521 | 21991-22098 | 81 | `chapters/volcengine/ark/8.3.3 查询3D生成任务列表.md` |
| 8.3.4 | 取消或删除3D生成任务 | 522 | 22099-22133 | 31 | `chapters/volcengine/ark/8.3.4 取消或删除3D生成任务.md` |
| 9.1 | 多模态向量化 API | 523-527 | 22135-22333 | 147 | `chapters/volcengine/ark/9.1 多模态向量化 API.md` |
| 10.1.1 | 创建智能体 | 528-536 | 22336-22738 | 320 | `chapters/volcengine/ark/10.1.1 创建智能体.md` |
| 10.1.2 | 查询智能体列表 | 537-542 | 22739-22972 | 195 | `chapters/volcengine/ark/10.1.2 查询智能体列表.md` |
| 10.1.3 | 查询智能体详情 | 543-547 | 22973-23170 | 161 | `chapters/volcengine/ark/10.1.3 查询智能体详情.md` |
| 10.1.4 | 更新智能体 | 548-557 | 23171-23629 | 344 | `chapters/volcengine/ark/10.1.4 更新智能体.md` |
| 10.1.5 | 删除智能体 | 558 | 23630-23648 | 13 | `chapters/volcengine/ark/10.1.5 删除智能体.md` |
| 10.1.6 | 查询智能体版本列表 | 559-564 | 23649-23871 | 183 | `chapters/volcengine/ark/10.1.6 查询智能体版本列表.md` |
| 10.2.1 | 创建环境 | 565-569 | 23873-24048 | 144 | `chapters/volcengine/ark/10.2.1 创建环境.md` |
| 10.2.2 | 查询环境列表 | 570-572 | 24049-24152 | 95 | `chapters/volcengine/ark/10.2.2 查询环境列表.md` |
| 10.2.3 | 查询环境详情 | 573-575 | 24153-24239 | 76 | `chapters/volcengine/ark/10.2.3 查询环境详情.md` |
| 10.2.4 | 更新环境 | 576-580 | 24240-24439 | 158 | `chapters/volcengine/ark/10.2.4 更新环境.md` |
| 10.2.5 | 删除环境 | 581 | 24440-24462 | 19 | `chapters/volcengine/ark/10.2.5 删除环境.md` |
| 10.2.6.1 | 长轮询拉取待执行 work | 582-584 | 24464-24541 | 60 | `chapters/volcengine/ark/10.2.6.1 长轮询拉取待执行 work.md` |
| 10.2.6.2 | 认领 work | 585-586 | 24542-24604 | 51 | `chapters/volcengine/ark/10.2.6.2 认领 work.md` |
| 10.2.6.3 | 查询 work 列表 | 587-589 | 24605-24695 | 76 | `chapters/volcengine/ark/10.2.6.3 查询 work 列表.md` |
| 10.2.6.4 | 查询 Work 详情 | 590-591 | 24696-24750 | 45 | `chapters/volcengine/ark/10.2.6.4 查询 Work 详情.md` |
| 10.2.6.5 | 心跳续租 | 592-593 | 24751-24804 | 37 | `chapters/volcengine/ark/10.2.6.5 心跳续租.md` |
| 10.2.6.6 | 停止 work | 594-595 | 24805-24869 | 52 | `chapters/volcengine/ark/10.2.6.6 停止 work.md` |
| 10.2.6.7 | 查询 Work 队列状态 | 596 | 24870-24898 | 19 | `chapters/volcengine/ark/10.2.6.7 查询 Work 队列状态.md` |
| 10.3.1 | 创建会话 | 597-613 | 24900-25596 | 588 | `chapters/volcengine/ark/10.3.1 创建会话.md` |
| 10.3.2 | 查询会话列表 | 614-626 | 25597-26129 | 471 | `chapters/volcengine/ark/10.3.2 查询会话列表.md` |
| 10.3.3 | 查询会话详情 | 627-638 | 26130-26622 | 436 | `chapters/volcengine/ark/10.3.3 查询会话详情.md` |
| 10.3.4 | 更新会话标题和标签 | 639-650 | 26623-27126 | 442 | `chapters/volcengine/ark/10.3.4 更新会话标题和标签.md` |
| 10.3.5 | 升级会话 | 651-663 | 27127-27692 | 495 | `chapters/volcengine/ark/10.3.5 升级会话.md` |
| 10.3.6 | 删除会话 | 664 | 27693-27719 | 20 | `chapters/volcengine/ark/10.3.6 删除会话.md` |
| 10.3.7.1 | 发送会话事件 | 665-666 | 27721-27767 | 33 | `chapters/volcengine/ark/10.3.7.1 发送会话事件.md` |
| 10.3.7.2 | 查询会话事件列表 | 667-668 | 27768-27832 | 50 | `chapters/volcengine/ark/10.3.7.2 查询会话事件列表.md` |
| 10.3.7.3 | 流式获取会话事件 | 669-670 | 27833-27879 | 29 | `chapters/volcengine/ark/10.3.7.3 流式获取会话事件.md` |
| 10.3.7.4 | 会话事件结构参考 - 第1部分 | 671-718 | 27880-29772 | 1742 | `chapters/volcengine/ark/10.3.7.4 会话事件结构参考 - 第1部分.md` |
| 10.3.8.1 | 添加会话资源 | 719-720 | 29774-29826 | 41 | `chapters/volcengine/ark/10.3.8.1 添加会话资源.md` |
| 10.3.8.2 | 查询会话资源列表 | 721-723 | 29827-29918 | 85 | `chapters/volcengine/ark/10.3.8.2 查询会话资源列表.md` |
| 10.3.8.3 | 查询会话资源 | 724 | 29919-29936 | 13 | `chapters/volcengine/ark/10.3.8.3 查询会话资源.md` |
| 10.3.9.1 | 查询线程列表 | 725-726 | 29938-30005 | 56 | `chapters/volcengine/ark/10.3.9.1 查询线程列表.md` |
| 10.3.9.2 | 查询线程详情 | 727-728 | 30006-30054 | 37 | `chapters/volcengine/ark/10.3.9.2 查询线程详情.md` |
| 10.3.9.3 | 查询线程事件列表 | 729-730 | 30055-30114 | 44 | `chapters/volcengine/ark/10.3.9.3 查询线程事件列表.md` |
| 10.3.9.4 | 流式获取线程事件 | 731-732 | 30115-30161 | 28 | `chapters/volcengine/ark/10.3.9.4 流式获取线程事件.md` |
| 10.4.1 | 创建保管库 | 733-734 | 30163-30197 | 28 | `chapters/volcengine/ark/10.4.1 创建保管库.md` |
| 10.4.2 | 查询保管库列表 | 735-736 | 30198-30252 | 45 | `chapters/volcengine/ark/10.4.2 查询保管库列表.md` |
| 10.4.3 | 查询保管库详情 | 737 | 30253-30279 | 24 | `chapters/volcengine/ark/10.4.3 查询保管库详情.md` |
| 10.4.4 | 更新保管库 | 738-739 | 30280-30321 | 33 | `chapters/volcengine/ark/10.4.4 更新保管库.md` |
| 10.4.5 | 删除保管库 | 740 | 30322-30346 | 21 | `chapters/volcengine/ark/10.4.5 删除保管库.md` |
| 10.4.6.1 | 创建凭证 | 741-749 | 30348-30722 | 290 | `chapters/volcengine/ark/10.4.6.1 创建凭证.md` |
| 10.4.6.2 | 查询凭证列表 | 750-754 | 30723-30906 | 153 | `chapters/volcengine/ark/10.4.6.2 查询凭证列表.md` |
| 10.4.6.3 | 查询凭证详情 | 755-758 | 30907-31062 | 131 | `chapters/volcengine/ark/10.4.6.3 查询凭证详情.md` |
| 10.4.6.4 | 更新凭证 | 759-766 | 31063-31408 | 271 | `chapters/volcengine/ark/10.4.6.4 更新凭证.md` |
| 10.4.6.5 | 删除凭证 | 767 | 31409-31435 | 21 | `chapters/volcengine/ark/10.4.6.5 删除凭证.md` |
| 10.5.1 | 创建记忆库 | 768-769 | 31437-31497 | 52 | `chapters/volcengine/ark/10.5.1 创建记忆库.md` |
| 10.5.2 | 查询记忆库列表 | 770-771 | 31498-31571 | 61 | `chapters/volcengine/ark/10.5.2 查询记忆库列表.md` |
| 10.5.3 | 查询记忆库详情 | 772-773 | 31572-31617 | 37 | `chapters/volcengine/ark/10.5.3 查询记忆库详情.md` |
| 10.5.4 | 更新记忆库 | 774-775 | 31618-31680 | 51 | `chapters/volcengine/ark/10.5.4 更新记忆库.md` |
| 10.5.5 | 删除记忆库 | 776 | 31681-31706 | 17 | `chapters/volcengine/ark/10.5.5 删除记忆库.md` |
| 10.5.6.1 | 创建记忆 | 777-778 | 31708-31773 | 52 | `chapters/volcengine/ark/10.5.6.1 创建记忆.md` |
| 10.5.6.2 | 批量创建记忆 | 779-781 | 31774-31888 | 89 | `chapters/volcengine/ark/10.5.6.2 批量创建记忆.md` |
| 10.5.6.3 | 查询记忆列表 | 782-784 | 31889-31977 | 67 | `chapters/volcengine/ark/10.5.6.3 查询记忆列表.md` |
| 10.5.6.4 | 查询记忆详情 | 785-786 | 31978-32033 | 42 | `chapters/volcengine/ark/10.5.6.4 查询记忆详情.md` |
| 10.5.6.5 | 更新记忆 | 787-788 | 32034-32104 | 52 | `chapters/volcengine/ark/10.5.6.5 更新记忆.md` |
| 10.5.6.6 | 删除记忆 | 789 | 32105-32133 | 18 | `chapters/volcengine/ark/10.5.6.6 删除记忆.md` |
| 10.6.1 | 创建技能 | 790-791 | 32135-32203 | 49 | `chapters/volcengine/ark/10.6.1 创建技能.md` |
| 10.6.2 | 查询技能列表 | 792-793 | 32204-32278 | 61 | `chapters/volcengine/ark/10.6.2 查询技能列表.md` |
| 10.6.3 | 查询技能详情 | 794-795 | 32279-32321 | 34 | `chapters/volcengine/ark/10.6.3 查询技能详情.md` |
| 10.6.4 | 设置技能内容保护 | 796-797 | 32322-32367 | 37 | `chapters/volcengine/ark/10.6.4 设置技能内容保护.md` |
| 10.6.5 | 删除技能 | 798 | 32368-32393 | 18 | `chapters/volcengine/ark/10.6.5 删除技能.md` |
| 10.6.6 | 创建新版本的技能 | 799-800 | 32394-32453 | 41 | `chapters/volcengine/ark/10.6.6 创建新版本的技能.md` |
| 10.6.7 | 查询技能的版本列表 | 801-802 | 32454-32509 | 48 | `chapters/volcengine/ark/10.6.7 查询技能的版本列表.md` |
| 10.6.8 | 查询指定版本的技能 | 803 | 32510-32539 | 26 | `chapters/volcengine/ark/10.6.8 查询指定版本的技能.md` |
| 10.6.9 | 删除指定版本的技能 | 804 | 32540-32561 | 17 | `chapters/volcengine/ark/10.6.9 删除指定版本的技能.md` |
| 10.6.10 | 下载指定版本的技能 | 805 | 32562-32580 | 14 | `chapters/volcengine/ark/10.6.10 下载指定版本的技能.md` |
| 10.6.11 | 扫描 GitHub 技能 | 806-807 | 32581-32633 | 43 | `chapters/volcengine/ark/10.6.11 扫描 GitHub 技能.md` |
| 10.6.12 | 导入 GitHub 技能 | 808-809 | 32634-32705 | 55 | `chapters/volcengine/ark/10.6.12 导入 GitHub 技能.md` |
| 11.1.1 | 创建批量推理任务 | 810-813 | 32708-32788 | 60 | `chapters/volcengine/ark/11.1.1 创建批量推理任务.md` |
| 11.1.2 | 获取批量推理任务列表 | 814-818 | 32789-32962 | 152 | `chapters/volcengine/ark/11.1.2 获取批量推理任务列表.md` |
| 11.1.3 | 获取批量推理任务 | 819-821 | 32963-33080 | 102 | `chapters/volcengine/ark/11.1.3 获取批量推理任务.md` |
| 11.1.4 | 更新批量推理任务 | 822 | 33081-33104 | 17 | `chapters/volcengine/ark/11.1.4 更新批量推理任务.md` |
| 11.1.5 | 删除批量推理任务 | 823 | 33105-33124 | 13 | `chapters/volcengine/ark/11.1.5 删除批量推理任务.md` |
| 11.1.6 | 停止批量推理任务 | 824 | 33125-33147 | 16 | `chapters/volcengine/ark/11.1.6 停止批量推理任务.md` |
| 11.1.7 | 重启批量推理任务 | 825 | 33148-33168 | 13 | `chapters/volcengine/ark/11.1.7 重启批量推理任务.md` |
| 11.2 | 批量(Chat) API | 826-840 | 33169-33609 | 339 | `chapters/volcengine/ark/11.2 批量(Chat) API.md` |
| 12.1 | 分词 API | 841-842 | 33611-33657 | 39 | `chapters/volcengine/ark/12.1 分词 API.md` |
| 13.1.1 | 获取临时 API Key | 843 | 33660-33694 | 26 | `chapters/volcengine/ark/13.1.1 获取临时 API Key.md` |
| 13.2.1 | 创建个人版套餐 | 844-845 | 33696-33754 | 34 | `chapters/volcengine/ark/13.2.1 创建个人版套餐.md` |
| 13.2.2 | 续费个人版套餐 | 846-847 | 33755-33800 | 27 | `chapters/volcengine/ark/13.2.2 续费个人版套餐.md` |
| 13.2.3 | 查询个人版套餐 | 848 | 33801-33828 | 21 | `chapters/volcengine/ark/13.2.3 查询个人版套餐.md` |
| 13.2.4.1 | 查询 Agent Plan 支持的模型列表 | 849 | 33830-33849 | 14 | `chapters/volcengine/ark/13.2.4.1 查询 Agent Plan 支持的模型列表.md` |
| 13.2.4.2 | 轮换个人版 API Key | 850 | 33850-33876 | 17 | `chapters/volcengine/ark/13.2.4.2 轮换个人版 API Key.md` |
| 13.2.4.3 | 获取套餐 AFP 额度 | 851-852 | 33877-33951 | 66 | `chapters/volcengine/ark/13.2.4.3 获取套餐 AFP 额度.md` |
| 13.2.4.4 | 获取套餐用量详情 | 853-854 | 33952-34000 | 39 | `chapters/volcengine/ark/13.2.4.4 获取套餐用量详情.md` |
| 13.2.5.1 | 查询 Coding Plan 支持的模型列表 | 855 | 34002-34017 | 12 | `chapters/volcengine/ark/13.2.5.1 查询 Coding Plan 支持的模型列表.md` |
| 13.3.1 | 获取基础模型版本列表 | 856-858 | 34019-34106 | 72 | `chapters/volcengine/ark/13.3.1 获取基础模型版本列表.md` |
| 13.3.2 | 获取基础模型版本信息 | 859-866 | 34107-34424 | 273 | `chapters/volcengine/ark/13.3.2 获取基础模型版本信息.md` |
| 13.3.3 | 获取基础模型列表 | 867-871 | 34425-34669 | 182 | `chapters/volcengine/ark/13.3.3 获取基础模型列表.md` |
| 13.3.4 | 获取基础模型信息 | 872-874 | 34670-34794 | 93 | `chapters/volcengine/ark/13.3.4 获取基础模型信息.md` |
| 13.4.1 | 批量开通基础模型 | 875 | 34796-34810 | 11 | `chapters/volcengine/ark/13.4.1 批量开通基础模型.md` |
| 13.4.2 | 启用自动开通新模型 | 876 | 34811-34822 | 7 | `chapters/volcengine/ark/13.4.2 启用自动开通新模型.md` |
| 13.4.3 | 关闭自动开通新模型 | 877 | 34823-34834 | 7 | `chapters/volcengine/ark/13.4.3 关闭自动开通新模型.md` |
| 13.4.4 | 查询模型开通详情 | 878-881 | 34835-34977 | 131 | `chapters/volcengine/ark/13.4.4 查询模型开通详情.md` |
| 13.4.5 | 查询模型开通列表 | 882-886 | 34978-35155 | 163 | `chapters/volcengine/ark/13.4.5 查询模型开通列表.md` |
| 13.5.1 | 批量开通资源 | 887 | 35157-35175 | 14 | `chapters/volcengine/ark/13.5.1 批量开通资源.md` |
| 13.5.2 | 查询资源开通列表 | 888-890 | 35176-35277 | 92 | `chapters/volcengine/ark/13.5.2 查询资源开通列表.md` |
| 13.6.1 | 查询模型限流 | 891-893 | 35279-35378 | 91 | `chapters/volcengine/ark/13.6.1 查询模型限流.md` |
| 13.7.1 | 删除定制模型 | 894 | 35380-35405 | 17 | `chapters/volcengine/ark/13.7.1 删除定制模型.md` |
| 13.7.2 | 获取定制模型信息 | 895-897 | 35406-35514 | 97 | `chapters/volcengine/ark/13.7.2 获取定制模型信息.md` |
| 13.7.3 | 更新定制模型 | 898 | 35515-35547 | 22 | `chapters/volcengine/ark/13.7.3 更新定制模型.md` |
| 13.7.4 | 获取定制模型列表 | 899-901 | 35548-35666 | 102 | `chapters/volcengine/ark/13.7.4 获取定制模型列表.md` |
| 13.8.1 | 创建模型调优任务 | 902-909 | 35668-35986 | 281 | `chapters/volcengine/ark/13.8.1 创建模型调优任务.md` |
| 13.8.2 | 删除模型调优任务 | 910 | 35987-36003 | 10 | `chapters/volcengine/ark/13.8.2 删除模型调优任务.md` |
| 13.8.3 | 获取模型调优任务信息 | 911-921 | 36004-36457 | 411 | `chapters/volcengine/ark/13.8.3 获取模型调优任务信息.md` |
| 13.8.4 | 查询精调效果指标详细数据 | 922-923 | 36458-36503 | 33 | `chapters/volcengine/ark/13.8.4 查询精调效果指标详细数据.md` |
| 13.8.5 | 查询精调效果指标 | 924 | 36504-36522 | 10 | `chapters/volcengine/ark/13.8.5 查询精调效果指标.md` |
| 13.8.6 | 获取模型调优任务列表 | 925-931 | 36523-36793 | 246 | `chapters/volcengine/ark/13.8.6 获取模型调优任务列表.md` |
| 13.8.7 | 重试模型调优任务 | 932 | 36794-36810 | 9 | `chapters/volcengine/ark/13.8.7 重试模型调优任务.md` |
| 13.8.8 | 停止模型调优任务 | 933 | 36811-36827 | 10 | `chapters/volcengine/ark/13.8.8 停止模型调优任务.md` |
| 13.8.9 | 更新模型调优任务 | 934 | 36828-36851 | 14 | `chapters/volcengine/ark/13.8.9 更新模型调优任务.md` |
| 13.9.1 | 开启推理接入点 | 935 | 36853-36873 | 13 | `chapters/volcengine/ark/13.9.1 开启推理接入点.md` |
| 13.9.2 | 停止推理接入点 | 936 | 36874-36894 | 11 | `chapters/volcengine/ark/13.9.2 停止推理接入点.md` |
| 13.9.3 | 获取推理接入点列表 | 937-941 | 36895-37106 | 170 | `chapters/volcengine/ark/13.9.3 获取推理接入点列表.md` |
| 13.9.4 | 获取推理接入点 | 942-944 | 37107-37208 | 88 | `chapters/volcengine/ark/13.9.4 获取推理接入点.md` |
| 13.9.5 | 删除推理接入点 | 945 | 37209-37228 | 12 | `chapters/volcengine/ark/13.9.5 删除推理接入点.md` |
| 13.9.6 | 更新推理接入点 | 946-950 | 37229-37413 | 160 | `chapters/volcengine/ark/13.9.6 更新推理接入点.md` |
| 13.9.7 | 创建推理接入点 | 951-956 | 37414-37641 | 193 | `chapters/volcengine/ark/13.9.7 创建推理接入点.md` |
| 13.9.8 | 获取接入点推理应用层加密证书 | 957-958 | 37642-37677 | 23 | `chapters/volcengine/ark/13.9.8 获取接入点推理应用层加密证书.md` |
| 13.9.9 | 创建推理接入点滚动升级任务 | 959-960 | 37678-37725 | 41 | `chapters/volcengine/ark/13.9.9 创建推理接入点滚动升级任务.md` |
| 13.9.10 | 查询推理接入点滚动升级详情 | 961-964 | 37726-37852 | 116 | `chapters/volcengine/ark/13.9.10 查询推理接入点滚动升级详情.md` |
| 13.9.11 | 回滚推理接入点滚动升级 | 965 | 37853-37870 | 13 | `chapters/volcengine/ark/13.9.11 回滚推理接入点滚动升级.md` |
| 13.9.12 | 取消推理接入点滚动升级 | 966 | 37871-37888 | 13 | `chapters/volcengine/ark/13.9.12 取消推理接入点滚动升级.md` |
| 13.10.1 | 创建评测任务 | 967-970 | 37890-38055 | 133 | `chapters/volcengine/ark/13.10.1 创建评测任务.md` |
| 13.10.2 | 删除评测任务 | 971 | 38056-38077 | 13 | `chapters/volcengine/ark/13.10.2 删除评测任务.md` |
| 13.10.3 | 获取评测任务 | 972-974 | 38078-38159 | 66 | `chapters/volcengine/ark/13.10.3 获取评测任务.md` |
| 13.10.4 | 获取评测任务结果 | 975-977 | 38160-38262 | 87 | `chapters/volcengine/ark/13.10.4 获取评测任务结果.md` |
| 13.10.5 | 获取评测任务列表 | 978-981 | 38263-38409 | 129 | `chapters/volcengine/ark/13.10.5 获取评测任务列表.md` |
| 13.10.6 | 获取评测任务结果列表 | 982-985 | 38410-38551 | 120 | `chapters/volcengine/ark/13.10.6 获取评测任务结果列表.md` |
| 13.10.7 | 停止评测任务 | 986 | 38552-38573 | 13 | `chapters/volcengine/ark/13.10.7 停止评测任务.md` |
| 13.10.8 | 更新评测任务 | 987 | 38574-38599 | 18 | `chapters/volcengine/ark/13.10.8 更新评测任务.md` |
| 13.11.1 | 查询推理用量 | 988-990 | 38601-38728 | 75 | `chapters/volcengine/ark/13.11.1 查询推理用量.md` |
| 13.11.2 | 创建用量明细导出任务 | 991-992 | 38729-38781 | 33 | `chapters/volcengine/ark/13.11.2 创建用量明细导出任务.md` |
| 13.11.3 | 查询用量明细导出任务状态 | 993-995 | 38782-38884 | 71 | `chapters/volcengine/ark/13.11.3 查询用量明细导出任务状态.md` |
| 13.11.4 | 查询模型推理限额 | 996 | 38885-38912 | 22 | `chapters/volcengine/ark/13.11.4 查询模型推理限额.md` |
| 13.11.5 | 开启模型推理限额 | 997 | 38913-38937 | 16 | `chapters/volcengine/ark/13.11.5 开启模型推理限额.md` |
| 13.11.6 | 关闭模型推理限额 | 998 | 38938-38958 | 12 | `chapters/volcengine/ark/13.11.6 关闭模型推理限额.md` |
| 13.12.1 | 创建方舟官方模型产物查询请求 | 999 | 38960-38978 | 14 | `chapters/volcengine/ark/13.12.1 创建方舟官方模型产物查询请求.md` |
| 13.12.2 | 获取安全审计日志 | 1000-1002 | 38979-39098 | 85 | `chapters/volcengine/ark/13.12.2 获取安全审计日志.md` |
| 13.12.3 | 获取方舟官方产物确认结果 | 1003 | 39099-39128 | 24 | `chapters/volcengine/ark/13.12.3 获取方舟官方产物确认结果.md` |
| 13.13.1 | 上报视频生成模型效果问题 | 1004-1006 | 39130-39253 | 86 | `chapters/volcengine/ark/13.13.1 上报视频生成模型效果问题.md` |
| 13.13.2 | 查询视频生成模型效果问题结果 | 1007-1010 | 39254-39342 | 69 | `chapters/volcengine/ark/13.13.2 查询视频生成模型效果问题结果.md` |
| 13.13.3 | 上报大语言模型效果问题 | 1011-1013 | 39343-39451 | 82 | `chapters/volcengine/ark/13.13.3 上报大语言模型效果问题.md` |
| 13.13.4 | 查询大语言模型效果问题结果 | 1014-1016 | 39452-39567 | 97 | `chapters/volcengine/ark/13.13.4 查询大语言模型效果问题结果.md` |
| 14.1 | 兼容 OpenAI SDK | 1017-1020 | 39569-39685 | 103 | `chapters/volcengine/ark/14.1 兼容 OpenAI SDK.md` |
| 14.2 | 向后兼容性 | 1021 | 39686-39731 | 25 | `chapters/volcengine/ark/14.2 向后兼容性.md` |
| 14.3 | 错误码 - 第1部分 | 1021-1043 | 39732-41691 | 1910 | `chapters/volcengine/ark/14.3 错误码 - 第1部分.md` |
| 14.3 | 错误码 - 第2部分·错误码 | 1044-1051 | 41692-42303 | 582 | `chapters/volcengine/ark/14.3 错误码 - 第2部分·错误码.md` |
| 14.4 | SDK 常见使用示例 | 1052-1068 | 42304-42912 | 538 | `chapters/volcengine/ark/14.4 SDK 常见使用示例.md` |
