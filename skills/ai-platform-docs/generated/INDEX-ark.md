# 方舟 API 区章节表（ark）

来源：《火山方舟 API 参考》（1066 页）。192 个章节文件，接口级切分：一个接口/任务一个文件；超过 1500 行的按语义块自动再拆为`… - 第N部分`（5 个章节被拆分）。

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
| 6.1 | 创建视频生成任务 | 444-460 | 18842-19714 | 613 | `chapters/volcengine/ark/6.1 创建视频生成任务.md` |
| 6.2 | 查询视频生成任务 | 461-464 | 19715-19855 | 105 | `chapters/volcengine/ark/6.2 查询视频生成任务.md` |
| 6.3 | 查询视频生成任务列表 | 465-469 | 19856-20058 | 156 | `chapters/volcengine/ark/6.3 查询视频生成任务列表.md` |
| 6.4 | 取消或删除视频生成任务 | 470 | 20059-20100 | 38 | `chapters/volcengine/ark/6.4 取消或删除视频生成任务.md` |
| 7.1 | 图片生成 API | 471-487 | 20102-20855 | 530 | `chapters/volcengine/ark/7.1 图片生成 API.md` |
| 7.2 | 图片生成流式响应事件 | 488-492 | 20856-21032 | 158 | `chapters/volcengine/ark/7.2 图片生成流式响应事件.md` |
| 8.1.1 | 创建 3D 生成任务 API | 493-495 | 21035-21138 | 80 | `chapters/volcengine/ark/8.1.1 创建 3D 生成任务 API.md` |
| 8.1.2 | 查询 3D 生成任务 API | 496-497 | 21139-21208 | 52 | `chapters/volcengine/ark/8.1.2 查询 3D 生成任务 API.md` |
| 8.1.3 | 查询 3D 生成任务列表 | 498-500 | 21209-21322 | 87 | `chapters/volcengine/ark/8.1.3 查询 3D 生成任务列表.md` |
| 8.1.4 | 取消或删除 3D 生成任务 | 501 | 21323-21364 | 38 | `chapters/volcengine/ark/8.1.4 取消或删除 3D 生成任务.md` |
| 8.2.1 | 创建3D生成任务 | 502-506 | 21366-21580 | 148 | `chapters/volcengine/ark/8.2.1 创建3D生成任务.md` |
| 8.2.2 | 查询3D生成任务 | 507-508 | 21581-21646 | 48 | `chapters/volcengine/ark/8.2.2 查询3D生成任务.md` |
| 8.2.3 | 查询3D生成任务列表 | 509-511 | 21647-21754 | 81 | `chapters/volcengine/ark/8.2.3 查询3D生成任务列表.md` |
| 8.2.4 | 取消或删除3D生成任务 | 512 | 21755-21789 | 31 | `chapters/volcengine/ark/8.2.4 取消或删除3D生成任务.md` |
| 8.3.1 | 创建3D生成任务 | 513-516 | 21791-21922 | 95 | `chapters/volcengine/ark/8.3.1 创建3D生成任务.md` |
| 8.3.2 | 查询3D生成任务 | 517-518 | 21923-21988 | 48 | `chapters/volcengine/ark/8.3.2 查询3D生成任务.md` |
| 8.3.3 | 查询3D生成任务列表 | 519-521 | 21989-22096 | 81 | `chapters/volcengine/ark/8.3.3 查询3D生成任务列表.md` |
| 8.3.4 | 取消或删除3D生成任务 | 522 | 22097-22131 | 31 | `chapters/volcengine/ark/8.3.4 取消或删除3D生成任务.md` |
| 9.1 | 多模态向量化 API | 523-527 | 22133-22331 | 147 | `chapters/volcengine/ark/9.1 多模态向量化 API.md` |
| 10.1.1 | 创建智能体 | 528-536 | 22334-22736 | 320 | `chapters/volcengine/ark/10.1.1 创建智能体.md` |
| 10.1.2 | 查询智能体列表 | 537-542 | 22737-22970 | 195 | `chapters/volcengine/ark/10.1.2 查询智能体列表.md` |
| 10.1.3 | 查询智能体详情 | 543-547 | 22971-23168 | 161 | `chapters/volcengine/ark/10.1.3 查询智能体详情.md` |
| 10.1.4 | 更新智能体 | 548-557 | 23169-23627 | 344 | `chapters/volcengine/ark/10.1.4 更新智能体.md` |
| 10.1.5 | 删除智能体 | 558 | 23628-23648 | 14 | `chapters/volcengine/ark/10.1.5 删除智能体.md` |
| 10.1.6 | 查询智能体版本列表 | 559-564 | 23649-23871 | 183 | `chapters/volcengine/ark/10.1.6 查询智能体版本列表.md` |
| 10.2.1 | 创建环境 | 565-569 | 23873-24048 | 144 | `chapters/volcengine/ark/10.2.1 创建环境.md` |
| 10.2.2 | 查询环境列表 | 570-572 | 24049-24152 | 95 | `chapters/volcengine/ark/10.2.2 查询环境列表.md` |
| 10.2.3 | 查询环境详情 | 573-575 | 24153-24239 | 76 | `chapters/volcengine/ark/10.2.3 查询环境详情.md` |
| 10.2.4 | 更新环境 | 576-580 | 24240-24439 | 158 | `chapters/volcengine/ark/10.2.4 更新环境.md` |
| 10.2.5 | 删除环境 | 581 | 24440-24462 | 19 | `chapters/volcengine/ark/10.2.5 删除环境.md` |
| 10.2.6.1 | 长轮询拉取待执行 Work | 582-584 | 24464-24555 | 69 | `chapters/volcengine/ark/10.2.6.1 长轮询拉取待执行 Work.md` |
| 10.2.6.2 | 认领 Work | 585-586 | 24556-24626 | 56 | `chapters/volcengine/ark/10.2.6.2 认领 Work.md` |
| 10.2.6.3 | 续租 Work | 587-588 | 24627-24682 | 41 | `chapters/volcengine/ark/10.2.6.3 续租 Work.md` |
| 10.2.6.4 | 查询 Work 队列状态 | 589 | 24683-24715 | 23 | `chapters/volcengine/ark/10.2.6.4 查询 Work 队列状态.md` |
| 10.2.6.5 | 停止 Work | 590-591 | 24716-24786 | 56 | `chapters/volcengine/ark/10.2.6.5 停止 Work.md` |
| 10.2.6.6 | 查询 Work 列表 | 592-594 | 24787-24879 | 77 | `chapters/volcengine/ark/10.2.6.6 查询 Work 列表.md` |
| 10.2.6.7 | 查询 Work 详情 | 595-596 | 24880-24937 | 46 | `chapters/volcengine/ark/10.2.6.7 查询 Work 详情.md` |
| 10.3.1 | 创建会话 | 597-613 | 24939-25649 | 604 | `chapters/volcengine/ark/10.3.1 创建会话.md` |
| 10.3.2 | 查询会话列表 | 614-626 | 25650-26196 | 487 | `chapters/volcengine/ark/10.3.2 查询会话列表.md` |
| 10.3.3 | 查询会话详情 | 627-638 | 26197-26703 | 452 | `chapters/volcengine/ark/10.3.3 查询会话详情.md` |
| 10.3.4 | 更新会话标题和标签 | 639-650 | 26704-27222 | 458 | `chapters/volcengine/ark/10.3.4 更新会话标题和标签.md` |
| 10.3.5 | 升级会话 | 651-664 | 27223-27804 | 511 | `chapters/volcengine/ark/10.3.5 升级会话.md` |
| 10.3.6 | 删除会话 | 665 | 27805-27831 | 20 | `chapters/volcengine/ark/10.3.6 删除会话.md` |
| 10.3.7.1 | 发送会话事件 | 666-667 | 27833-27879 | 33 | `chapters/volcengine/ark/10.3.7.1 发送会话事件.md` |
| 10.3.7.2 | 查询会话事件列表 | 668-669 | 27880-27944 | 50 | `chapters/volcengine/ark/10.3.7.2 查询会话事件列表.md` |
| 10.3.7.3 | 流式获取会话事件 | 670-671 | 27945-27996 | 33 | `chapters/volcengine/ark/10.3.7.3 流式获取会话事件.md` |
| 10.3.7.4 | 会话事件结构参考 - 第1部分 | 672-716 | 27997-29777 | 1641 | `chapters/volcengine/ark/10.3.7.4 会话事件结构参考 - 第1部分.md` |
| 10.3.8.1 | 添加会话资源 | 717-718 | 29779-29831 | 41 | `chapters/volcengine/ark/10.3.8.1 添加会话资源.md` |
| 10.3.8.2 | 查询会话资源列表 | 719-721 | 29832-29923 | 85 | `chapters/volcengine/ark/10.3.8.2 查询会话资源列表.md` |
| 10.3.8.3 | 查询会话资源 | 722 | 29924-29941 | 13 | `chapters/volcengine/ark/10.3.8.3 查询会话资源.md` |
| 10.3.9.1 | 查询线程列表 | 723-724 | 29943-30010 | 56 | `chapters/volcengine/ark/10.3.9.1 查询线程列表.md` |
| 10.3.9.2 | 查询线程详情 | 725-726 | 30011-30059 | 37 | `chapters/volcengine/ark/10.3.9.2 查询线程详情.md` |
| 10.3.9.3 | 查询线程事件列表 | 727-728 | 30060-30122 | 47 | `chapters/volcengine/ark/10.3.9.3 查询线程事件列表.md` |
| 10.3.9.4 | 流式获取线程事件 | 729-730 | 30123-30171 | 30 | `chapters/volcengine/ark/10.3.9.4 流式获取线程事件.md` |
| 10.4.1 | 创建保管库 | 731-732 | 30173-30207 | 28 | `chapters/volcengine/ark/10.4.1 创建保管库.md` |
| 10.4.2 | 查询保管库列表 | 733-734 | 30208-30262 | 45 | `chapters/volcengine/ark/10.4.2 查询保管库列表.md` |
| 10.4.3 | 查询保管库详情 | 735 | 30263-30289 | 24 | `chapters/volcengine/ark/10.4.3 查询保管库详情.md` |
| 10.4.4 | 更新保管库 | 736-737 | 30290-30331 | 33 | `chapters/volcengine/ark/10.4.4 更新保管库.md` |
| 10.4.5 | 删除保管库 | 738 | 30332-30356 | 21 | `chapters/volcengine/ark/10.4.5 删除保管库.md` |
| 10.4.6.1 | 创建凭证 | 739-747 | 30358-30732 | 290 | `chapters/volcengine/ark/10.4.6.1 创建凭证.md` |
| 10.4.6.2 | 查询凭证列表 | 748-752 | 30733-30916 | 153 | `chapters/volcengine/ark/10.4.6.2 查询凭证列表.md` |
| 10.4.6.3 | 查询凭证详情 | 753-756 | 30917-31072 | 131 | `chapters/volcengine/ark/10.4.6.3 查询凭证详情.md` |
| 10.4.6.4 | 更新凭证 | 757-764 | 31073-31418 | 271 | `chapters/volcengine/ark/10.4.6.4 更新凭证.md` |
| 10.4.6.5 | 删除凭证 | 765 | 31419-31445 | 21 | `chapters/volcengine/ark/10.4.6.5 删除凭证.md` |
| 10.5.1 | 创建记忆库 | 766-767 | 31447-31507 | 52 | `chapters/volcengine/ark/10.5.1 创建记忆库.md` |
| 10.5.2 | 查询记忆库列表 | 768-769 | 31508-31590 | 66 | `chapters/volcengine/ark/10.5.2 查询记忆库列表.md` |
| 10.5.3 | 查询记忆库详情 | 770-771 | 31591-31636 | 37 | `chapters/volcengine/ark/10.5.3 查询记忆库详情.md` |
| 10.5.4 | 更新记忆库 | 772-773 | 31637-31699 | 51 | `chapters/volcengine/ark/10.5.4 更新记忆库.md` |
| 10.5.5 | 删除记忆库 | 774 | 31700-31725 | 17 | `chapters/volcengine/ark/10.5.5 删除记忆库.md` |
| 10.5.6.1 | 创建记忆 | 775-776 | 31727-31792 | 52 | `chapters/volcengine/ark/10.5.6.1 创建记忆.md` |
| 10.5.6.2 | 批量创建记忆 | 777-779 | 31793-31907 | 89 | `chapters/volcengine/ark/10.5.6.2 批量创建记忆.md` |
| 10.5.6.3 | 查询记忆列表 | 780-782 | 31908-31999 | 69 | `chapters/volcengine/ark/10.5.6.3 查询记忆列表.md` |
| 10.5.6.4 | 查询记忆详情 | 783-784 | 32000-32058 | 45 | `chapters/volcengine/ark/10.5.6.4 查询记忆详情.md` |
| 10.5.6.5 | 更新记忆 | 785-786 | 32059-32129 | 52 | `chapters/volcengine/ark/10.5.6.5 更新记忆.md` |
| 10.5.6.6 | 删除记忆 | 787 | 32130-32158 | 18 | `chapters/volcengine/ark/10.5.6.6 删除记忆.md` |
| 10.6.1 | 创建技能 | 788-789 | 32160-32228 | 49 | `chapters/volcengine/ark/10.6.1 创建技能.md` |
| 10.6.2 | 查询技能列表 | 790-791 | 32229-32303 | 61 | `chapters/volcengine/ark/10.6.2 查询技能列表.md` |
| 10.6.3 | 查询技能详情 | 792-793 | 32304-32349 | 36 | `chapters/volcengine/ark/10.6.3 查询技能详情.md` |
| 10.6.4 | 设置技能内容保护 | 794-795 | 32350-32395 | 37 | `chapters/volcengine/ark/10.6.4 设置技能内容保护.md` |
| 10.6.5 | 删除技能 | 796 | 32396-32421 | 18 | `chapters/volcengine/ark/10.6.5 删除技能.md` |
| 10.6.6 | 创建新版本的技能 | 797-798 | 32422-32481 | 41 | `chapters/volcengine/ark/10.6.6 创建新版本的技能.md` |
| 10.6.7 | 查询技能的版本列表 | 799-800 | 32482-32537 | 48 | `chapters/volcengine/ark/10.6.7 查询技能的版本列表.md` |
| 10.6.8 | 查询指定版本的技能 | 801 | 32538-32567 | 26 | `chapters/volcengine/ark/10.6.8 查询指定版本的技能.md` |
| 10.6.9 | 删除指定版本的技能 | 802 | 32568-32589 | 17 | `chapters/volcengine/ark/10.6.9 删除指定版本的技能.md` |
| 10.6.10 | 下载指定版本的技能 | 803 | 32590-32608 | 14 | `chapters/volcengine/ark/10.6.10 下载指定版本的技能.md` |
| 10.6.11 | 扫描 GitHub 技能 | 804-805 | 32609-32661 | 43 | `chapters/volcengine/ark/10.6.11 扫描 GitHub 技能.md` |
| 10.6.12 | 导入 GitHub 技能 | 806-807 | 32662-32737 | 58 | `chapters/volcengine/ark/10.6.12 导入 GitHub 技能.md` |
| 11.1.1 | 创建批量推理任务 | 808-811 | 32740-32820 | 60 | `chapters/volcengine/ark/11.1.1 创建批量推理任务.md` |
| 11.1.2 | 获取批量推理任务列表 | 812-816 | 32821-32994 | 152 | `chapters/volcengine/ark/11.1.2 获取批量推理任务列表.md` |
| 11.1.3 | 获取批量推理任务 | 817-819 | 32995-33112 | 102 | `chapters/volcengine/ark/11.1.3 获取批量推理任务.md` |
| 11.1.4 | 更新批量推理任务 | 820 | 33113-33136 | 17 | `chapters/volcengine/ark/11.1.4 更新批量推理任务.md` |
| 11.1.5 | 删除批量推理任务 | 821 | 33137-33156 | 13 | `chapters/volcengine/ark/11.1.5 删除批量推理任务.md` |
| 11.1.6 | 停止批量推理任务 | 822 | 33157-33179 | 16 | `chapters/volcengine/ark/11.1.6 停止批量推理任务.md` |
| 11.1.7 | 重启批量推理任务 | 823 | 33180-33200 | 13 | `chapters/volcengine/ark/11.1.7 重启批量推理任务.md` |
| 11.2 | 批量(Chat) API | 824-838 | 33201-33641 | 339 | `chapters/volcengine/ark/11.2 批量(Chat) API.md` |
| 12.1 | 分词 API | 839-840 | 33643-33689 | 39 | `chapters/volcengine/ark/12.1 分词 API.md` |
| 13.1.1 | 获取临时 API Key | 841 | 33692-33726 | 26 | `chapters/volcengine/ark/13.1.1 获取临时 API Key.md` |
| 13.2.1 | 创建个人版套餐 | 842-843 | 33728-33786 | 34 | `chapters/volcengine/ark/13.2.1 创建个人版套餐.md` |
| 13.2.2 | 续费个人版套餐 | 844-845 | 33787-33832 | 27 | `chapters/volcengine/ark/13.2.2 续费个人版套餐.md` |
| 13.2.3 | 查询个人版套餐 | 846 | 33833-33860 | 21 | `chapters/volcengine/ark/13.2.3 查询个人版套餐.md` |
| 13.2.4.1 | 查询 Agent Plan 支持的模型列表 | 847 | 33862-33881 | 14 | `chapters/volcengine/ark/13.2.4.1 查询 Agent Plan 支持的模型列表.md` |
| 13.2.4.2 | 轮换个人版 API Key | 848 | 33882-33908 | 17 | `chapters/volcengine/ark/13.2.4.2 轮换个人版 API Key.md` |
| 13.2.4.3 | 获取套餐 AFP 额度 | 849-850 | 33909-33983 | 66 | `chapters/volcengine/ark/13.2.4.3 获取套餐 AFP 额度.md` |
| 13.2.4.4 | 获取套餐用量详情 | 851-852 | 33984-34032 | 39 | `chapters/volcengine/ark/13.2.4.4 获取套餐用量详情.md` |
| 13.2.5.1 | 查询 Coding Plan 支持的模型列表 | 853 | 34034-34049 | 12 | `chapters/volcengine/ark/13.2.5.1 查询 Coding Plan 支持的模型列表.md` |
| 13.3.1 | 获取基础模型版本列表 | 854-856 | 34051-34138 | 72 | `chapters/volcengine/ark/13.3.1 获取基础模型版本列表.md` |
| 13.3.2 | 获取基础模型版本信息 | 857-864 | 34139-34456 | 273 | `chapters/volcengine/ark/13.3.2 获取基础模型版本信息.md` |
| 13.3.3 | 获取基础模型列表 | 865-869 | 34457-34701 | 182 | `chapters/volcengine/ark/13.3.3 获取基础模型列表.md` |
| 13.3.4 | 获取基础模型信息 | 870-872 | 34702-34826 | 93 | `chapters/volcengine/ark/13.3.4 获取基础模型信息.md` |
| 13.4.1 | 批量开通基础模型 | 873 | 34828-34842 | 11 | `chapters/volcengine/ark/13.4.1 批量开通基础模型.md` |
| 13.4.2 | 启用自动开通新模型 | 874 | 34843-34854 | 7 | `chapters/volcengine/ark/13.4.2 启用自动开通新模型.md` |
| 13.4.3 | 关闭自动开通新模型 | 875 | 34855-34866 | 7 | `chapters/volcengine/ark/13.4.3 关闭自动开通新模型.md` |
| 13.4.4 | 查询模型开通详情 | 876-879 | 34867-35009 | 131 | `chapters/volcengine/ark/13.4.4 查询模型开通详情.md` |
| 13.4.5 | 查询模型开通列表 | 880-884 | 35010-35187 | 163 | `chapters/volcengine/ark/13.4.5 查询模型开通列表.md` |
| 13.5.1 | 批量开通资源 | 885 | 35189-35207 | 14 | `chapters/volcengine/ark/13.5.1 批量开通资源.md` |
| 13.5.2 | 查询资源开通列表 | 886-888 | 35208-35309 | 92 | `chapters/volcengine/ark/13.5.2 查询资源开通列表.md` |
| 13.6.1 | 查询模型限流 | 889-891 | 35311-35410 | 91 | `chapters/volcengine/ark/13.6.1 查询模型限流.md` |
| 13.7.1 | 删除定制模型 | 892 | 35412-35437 | 17 | `chapters/volcengine/ark/13.7.1 删除定制模型.md` |
| 13.7.2 | 获取定制模型信息 | 893-895 | 35438-35546 | 97 | `chapters/volcengine/ark/13.7.2 获取定制模型信息.md` |
| 13.7.3 | 更新定制模型 | 896 | 35547-35579 | 22 | `chapters/volcengine/ark/13.7.3 更新定制模型.md` |
| 13.7.4 | 获取定制模型列表 | 897-899 | 35580-35698 | 102 | `chapters/volcengine/ark/13.7.4 获取定制模型列表.md` |
| 13.8.1 | 创建模型调优任务 | 900-907 | 35700-36018 | 281 | `chapters/volcengine/ark/13.8.1 创建模型调优任务.md` |
| 13.8.2 | 删除模型调优任务 | 908 | 36019-36035 | 10 | `chapters/volcengine/ark/13.8.2 删除模型调优任务.md` |
| 13.8.3 | 获取模型调优任务信息 | 909-919 | 36036-36489 | 411 | `chapters/volcengine/ark/13.8.3 获取模型调优任务信息.md` |
| 13.8.4 | 查询精调效果指标详细数据 | 920-921 | 36490-36535 | 33 | `chapters/volcengine/ark/13.8.4 查询精调效果指标详细数据.md` |
| 13.8.5 | 查询精调效果指标 | 922 | 36536-36554 | 10 | `chapters/volcengine/ark/13.8.5 查询精调效果指标.md` |
| 13.8.6 | 获取模型调优任务列表 | 923-929 | 36555-36825 | 246 | `chapters/volcengine/ark/13.8.6 获取模型调优任务列表.md` |
| 13.8.7 | 重试模型调优任务 | 930 | 36826-36842 | 9 | `chapters/volcengine/ark/13.8.7 重试模型调优任务.md` |
| 13.8.8 | 停止模型调优任务 | 931 | 36843-36859 | 10 | `chapters/volcengine/ark/13.8.8 停止模型调优任务.md` |
| 13.8.9 | 更新模型调优任务 | 932 | 36860-36883 | 14 | `chapters/volcengine/ark/13.8.9 更新模型调优任务.md` |
| 13.9.1 | 开启推理接入点 | 933 | 36885-36905 | 13 | `chapters/volcengine/ark/13.9.1 开启推理接入点.md` |
| 13.9.2 | 停止推理接入点 | 934 | 36906-36926 | 11 | `chapters/volcengine/ark/13.9.2 停止推理接入点.md` |
| 13.9.3 | 获取推理接入点列表 | 935-939 | 36927-37138 | 170 | `chapters/volcengine/ark/13.9.3 获取推理接入点列表.md` |
| 13.9.4 | 获取推理接入点 | 940-942 | 37139-37240 | 88 | `chapters/volcengine/ark/13.9.4 获取推理接入点.md` |
| 13.9.5 | 删除推理接入点 | 943 | 37241-37260 | 12 | `chapters/volcengine/ark/13.9.5 删除推理接入点.md` |
| 13.9.6 | 更新推理接入点 | 944-948 | 37261-37445 | 160 | `chapters/volcengine/ark/13.9.6 更新推理接入点.md` |
| 13.9.7 | 创建推理接入点 | 949-954 | 37446-37673 | 193 | `chapters/volcengine/ark/13.9.7 创建推理接入点.md` |
| 13.9.8 | 获取接入点推理应用层加密证书 | 955-956 | 37674-37709 | 23 | `chapters/volcengine/ark/13.9.8 获取接入点推理应用层加密证书.md` |
| 13.9.9 | 创建推理接入点滚动升级任务 | 957-958 | 37710-37757 | 41 | `chapters/volcengine/ark/13.9.9 创建推理接入点滚动升级任务.md` |
| 13.9.10 | 查询推理接入点滚动升级详情 | 959-962 | 37758-37884 | 116 | `chapters/volcengine/ark/13.9.10 查询推理接入点滚动升级详情.md` |
| 13.9.11 | 回滚推理接入点滚动升级 | 963 | 37885-37902 | 13 | `chapters/volcengine/ark/13.9.11 回滚推理接入点滚动升级.md` |
| 13.9.12 | 取消推理接入点滚动升级 | 964 | 37903-37920 | 13 | `chapters/volcengine/ark/13.9.12 取消推理接入点滚动升级.md` |
| 13.10.1 | 创建评测任务 | 965-968 | 37922-38087 | 133 | `chapters/volcengine/ark/13.10.1 创建评测任务.md` |
| 13.10.2 | 删除评测任务 | 969 | 38088-38109 | 13 | `chapters/volcengine/ark/13.10.2 删除评测任务.md` |
| 13.10.3 | 获取评测任务 | 970-972 | 38110-38191 | 66 | `chapters/volcengine/ark/13.10.3 获取评测任务.md` |
| 13.10.4 | 获取评测任务结果 | 973-975 | 38192-38294 | 87 | `chapters/volcengine/ark/13.10.4 获取评测任务结果.md` |
| 13.10.5 | 获取评测任务列表 | 976-979 | 38295-38441 | 129 | `chapters/volcengine/ark/13.10.5 获取评测任务列表.md` |
| 13.10.6 | 获取评测任务结果列表 | 980-983 | 38442-38583 | 120 | `chapters/volcengine/ark/13.10.6 获取评测任务结果列表.md` |
| 13.10.7 | 停止评测任务 | 984 | 38584-38605 | 13 | `chapters/volcengine/ark/13.10.7 停止评测任务.md` |
| 13.10.8 | 更新评测任务 | 985 | 38606-38631 | 18 | `chapters/volcengine/ark/13.10.8 更新评测任务.md` |
| 13.11.1 | 查询推理用量 | 986-988 | 38633-38760 | 75 | `chapters/volcengine/ark/13.11.1 查询推理用量.md` |
| 13.11.2 | 创建用量明细导出任务 | 989-990 | 38761-38813 | 33 | `chapters/volcengine/ark/13.11.2 创建用量明细导出任务.md` |
| 13.11.3 | 查询用量明细导出任务状态 | 991-993 | 38814-38916 | 71 | `chapters/volcengine/ark/13.11.3 查询用量明细导出任务状态.md` |
| 13.11.4 | 查询模型推理限额 | 994 | 38917-38944 | 22 | `chapters/volcengine/ark/13.11.4 查询模型推理限额.md` |
| 13.11.5 | 开启模型推理限额 | 995 | 38945-38969 | 16 | `chapters/volcengine/ark/13.11.5 开启模型推理限额.md` |
| 13.11.6 | 关闭模型推理限额 | 996 | 38970-38990 | 12 | `chapters/volcengine/ark/13.11.6 关闭模型推理限额.md` |
| 13.12.1 | 创建方舟官方模型产物查询请求 | 997 | 38992-39010 | 14 | `chapters/volcengine/ark/13.12.1 创建方舟官方模型产物查询请求.md` |
| 13.12.2 | 获取安全审计日志 | 998-1000 | 39011-39130 | 85 | `chapters/volcengine/ark/13.12.2 获取安全审计日志.md` |
| 13.12.3 | 获取方舟官方产物确认结果 | 1001 | 39131-39160 | 24 | `chapters/volcengine/ark/13.12.3 获取方舟官方产物确认结果.md` |
| 13.13.1 | 上报视频生成模型效果问题 | 1002-1004 | 39162-39285 | 86 | `chapters/volcengine/ark/13.13.1 上报视频生成模型效果问题.md` |
| 13.13.2 | 查询视频生成模型效果问题结果 | 1005-1008 | 39286-39374 | 69 | `chapters/volcengine/ark/13.13.2 查询视频生成模型效果问题结果.md` |
| 13.13.3 | 上报大语言模型效果问题 | 1009-1011 | 39375-39483 | 82 | `chapters/volcengine/ark/13.13.3 上报大语言模型效果问题.md` |
| 13.13.4 | 查询大语言模型效果问题结果 | 1012-1014 | 39484-39599 | 97 | `chapters/volcengine/ark/13.13.4 查询大语言模型效果问题结果.md` |
| 14.1 | 兼容 OpenAI SDK | 1015-1018 | 39601-39717 | 103 | `chapters/volcengine/ark/14.1 兼容 OpenAI SDK.md` |
| 14.2 | 向后兼容性 | 1019 | 39718-39763 | 25 | `chapters/volcengine/ark/14.2 向后兼容性.md` |
| 14.3 | 错误码 - 第1部分 | 1019-1041 | 39764-41728 | 1915 | `chapters/volcengine/ark/14.3 错误码 - 第1部分.md` |
| 14.3 | 错误码 - 第2部分·错误码 | 1042-1049 | 41729-42327 | 569 | `chapters/volcengine/ark/14.3 错误码 - 第2部分·错误码.md` |
| 14.4 | SDK 常见使用示例 | 1050-1066 | 42328-42936 | 538 | `chapters/volcengine/ark/14.4 SDK 常见使用示例.md` |
