# 方舟 API 区章节表（ark）

来源：《火山方舟 API 参考》（1092 页）。196 个章节文件，接口级切分：一个接口/任务一个文件；超过 1500 行的按语义块自动再拆为`… - 第N部分`（5 个章节被拆分）。

「页码」是原 PDF 页码范围；「行范围」是中间 MD（`doc/<源文档>.md`）的 1 起始行号，可据此回查原文。章节文件本身已去掉页眉页脚，回查 PDF 时用这两列。文件名即章节标题，日常定位直接 Glob 文件名即可，用不到这两列。

**这张表用来 grep，不要整读。**

| 编号 | 标题 | 页码 | 行范围(源文件) | 行数 | 文件 |
|------|------|------|---------------|------|------|
| 1.1 | 获取 API Key 并配置 | 1 | 274-309 | 20 | `chapters/volcengine/ark/1.1 获取 API Key 并配置.md` |
| 1.2 | 安装及升级 SDK | 2-7 | 310-468 | 122 | `chapters/volcengine/ark/1.2 安装及升级 SDK.md` |
| 1.3 | Base URL及鉴权 | 8-10 | 469-564 | 68 | `chapters/volcengine/ark/1.3 Base URL及鉴权.md` |
| 2.1 | 对话(Chat) API | 11-37 | 566-1807 | 916 | `chapters/volcengine/ark/2.1 对话(Chat) API.md` |
| 3.1 | 创建 Response - 第1部分 | 38-76 | 1808-3489 | 1441 | `chapters/volcengine/ark/3.1 创建 Response - 第1部分.md` |
| 3.1 | 创建 Response - 第2部分·响应参数 | 77-108 | 3490-4844 | 1209 | `chapters/volcengine/ark/3.1 创建 Response - 第2部分·响应参数.md` |
| 3.2 | 查询 Response 详情 | 109-135 | 4845-5979 | 1062 | `chapters/volcengine/ark/3.2 查询 Response 详情.md` |
| 3.3 | 查询 Response 输入项列表 | 136-157 | 5980-6878 | 831 | `chapters/volcengine/ark/3.3 查询 Response 输入项列表.md` |
| 3.4 | 删除 Response | 158 | 6879-6902 | 19 | `chapters/volcengine/ark/3.4 删除 Response.md` |
| 3.5.1 | Response 生命周期 - 第1部分 | 159-196 | 6903-8552 | 1474 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第1部分.md` |
| 3.5.1 | Response 生命周期 - 第2部分 | 197-234 | 8553-10216 | 1489 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第2部分.md` |
| 3.5.1 | Response 生命周期 - 第3部分 | 235-272 | 10217-11867 | 1483 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第3部分.md` |
| 3.5.1 | Response 生命周期 - 第4部分 | 273-319 | 11868-13885 | 1778 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第4部分.md` |
| 3.5.2 | Output Item 与文本回答 - 第1部分 | 320-355 | 13886-15460 | 1447 | `chapters/volcengine/ark/3.5.2 Output Item 与文本回答 - 第1部分.md` |
| 3.5.2 | Output Item 与文本回答 - 第2部分 | 356-371 | 15461-16107 | 615 | `chapters/volcengine/ark/3.5.2 Output Item 与文本回答 - 第2部分.md` |
| 3.5.3 | 工具调用事件 | 372-398 | 16108-17188 | 1024 | `chapters/volcengine/ark/3.5.3 工具调用事件.md` |
| 3.5.4 | 语音转写与错误事件 | 399-403 | 17189-17359 | 161 | `chapters/volcengine/ark/3.5.4 语音转写与错误事件.md` |
| 4.1 | 创建 Message | 404-419 | 17361-18002 | 564 | `chapters/volcengine/ark/4.1 创建 Message.md` |
| 4.2 | 统计 Messages 请求 token 数 | 420-427 | 18003-18336 | 279 | `chapters/volcengine/ark/4.2 统计 Messages 请求 token 数.md` |
| 5.1 | 上传文件 | 428-433 | 18338-18552 | 159 | `chapters/volcengine/ark/5.1 上传文件.md` |
| 5.2 | 查询文件详情 | 434-435 | 18553-18620 | 60 | `chapters/volcengine/ark/5.2 查询文件详情.md` |
| 5.3 | 查询文件列表 | 436-439 | 18621-18751 | 109 | `chapters/volcengine/ark/5.3 查询文件列表.md` |
| 5.4 | 删除文件 | 440 | 18752-18774 | 19 | `chapters/volcengine/ark/5.4 删除文件.md` |
| 5.5 | The file object | 441-443 | 18775-18846 | 57 | `chapters/volcengine/ark/5.5 The file object.md` |
| 6.1 | 创建视频生成任务 | 444-460 | 18848-19720 | 613 | `chapters/volcengine/ark/6.1 创建视频生成任务.md` |
| 6.2 | 查询视频生成任务 | 461-464 | 19721-19861 | 105 | `chapters/volcengine/ark/6.2 查询视频生成任务.md` |
| 6.3 | 查询视频生成任务列表 | 465-469 | 19862-20064 | 156 | `chapters/volcengine/ark/6.3 查询视频生成任务列表.md` |
| 6.4 | 取消或删除视频生成任务 | 470 | 20065-20106 | 38 | `chapters/volcengine/ark/6.4 取消或删除视频生成任务.md` |
| 7.1 | 图片生成 API | 471-487 | 20108-20862 | 531 | `chapters/volcengine/ark/7.1 图片生成 API.md` |
| 7.2 | 图片生成流式响应事件 | 488-492 | 20863-21039 | 158 | `chapters/volcengine/ark/7.2 图片生成流式响应事件.md` |
| 8.1.1 | 创建 3D 生成任务 API | 493-495 | 21042-21145 | 80 | `chapters/volcengine/ark/8.1.1 创建 3D 生成任务 API.md` |
| 8.1.2 | 查询 3D 生成任务 API | 496-497 | 21146-21215 | 52 | `chapters/volcengine/ark/8.1.2 查询 3D 生成任务 API.md` |
| 8.1.3 | 查询 3D 生成任务列表 | 498-500 | 21216-21329 | 87 | `chapters/volcengine/ark/8.1.3 查询 3D 生成任务列表.md` |
| 8.1.4 | 取消或删除 3D 生成任务 | 501 | 21330-21371 | 38 | `chapters/volcengine/ark/8.1.4 取消或删除 3D 生成任务.md` |
| 8.2.1 | 创建3D生成任务 | 502-506 | 21373-21587 | 148 | `chapters/volcengine/ark/8.2.1 创建3D生成任务.md` |
| 8.2.2 | 查询3D生成任务 | 507-508 | 21588-21653 | 48 | `chapters/volcengine/ark/8.2.2 查询3D生成任务.md` |
| 8.2.3 | 查询3D生成任务列表 | 509-511 | 21654-21761 | 81 | `chapters/volcengine/ark/8.2.3 查询3D生成任务列表.md` |
| 8.2.4 | 取消或删除3D生成任务 | 512 | 21762-21796 | 31 | `chapters/volcengine/ark/8.2.4 取消或删除3D生成任务.md` |
| 8.3.1 | 创建3D生成任务 | 513-516 | 21798-21929 | 95 | `chapters/volcengine/ark/8.3.1 创建3D生成任务.md` |
| 8.3.2 | 查询3D生成任务 | 517-518 | 21930-21995 | 48 | `chapters/volcengine/ark/8.3.2 查询3D生成任务.md` |
| 8.3.3 | 查询3D生成任务列表 | 519-521 | 21996-22103 | 81 | `chapters/volcengine/ark/8.3.3 查询3D生成任务列表.md` |
| 8.3.4 | 取消或删除3D生成任务 | 522 | 22104-22138 | 31 | `chapters/volcengine/ark/8.3.4 取消或删除3D生成任务.md` |
| 9.1 | 多模态向量化 API | 523-527 | 22140-22338 | 147 | `chapters/volcengine/ark/9.1 多模态向量化 API.md` |
| 10.1.1 | 创建智能体 | 528-538 | 22341-22824 | 375 | `chapters/volcengine/ark/10.1.1 创建智能体.md` |
| 10.1.2 | 查询智能体列表 | 539-544 | 22825-23083 | 215 | `chapters/volcengine/ark/10.1.2 查询智能体列表.md` |
| 10.1.3 | 查询智能体详情 | 545-550 | 23084-23307 | 180 | `chapters/volcengine/ark/10.1.3 查询智能体详情.md` |
| 10.1.4 | 更新智能体 | 551-562 | 23308-23838 | 387 | `chapters/volcengine/ark/10.1.4 更新智能体.md` |
| 10.1.5 | 删除智能体 | 563 | 23839-23859 | 14 | `chapters/volcengine/ark/10.1.5 删除智能体.md` |
| 10.1.6 | 查询智能体版本列表 | 564-569 | 23860-24107 | 202 | `chapters/volcengine/ark/10.1.6 查询智能体版本列表.md` |
| 10.2.1 | 创建环境 | 570-574 | 24109-24285 | 144 | `chapters/volcengine/ark/10.2.1 创建环境.md` |
| 10.2.2 | 查询环境列表 | 575-577 | 24286-24390 | 95 | `chapters/volcengine/ark/10.2.2 查询环境列表.md` |
| 10.2.3 | 查询环境详情 | 578-580 | 24391-24478 | 76 | `chapters/volcengine/ark/10.2.3 查询环境详情.md` |
| 10.2.4 | 更新环境 | 581-585 | 24479-24678 | 156 | `chapters/volcengine/ark/10.2.4 更新环境.md` |
| 10.2.5 | 删除环境 | 586 | 24679-24701 | 19 | `chapters/volcengine/ark/10.2.5 删除环境.md` |
| 10.2.6.1 | 长轮询拉取待执行 Work | 587-589 | 24703-24794 | 69 | `chapters/volcengine/ark/10.2.6.1 长轮询拉取待执行 Work.md` |
| 10.2.6.2 | 认领 Work | 590-591 | 24795-24865 | 56 | `chapters/volcengine/ark/10.2.6.2 认领 Work.md` |
| 10.2.6.3 | 续租 Work | 592-593 | 24866-24921 | 41 | `chapters/volcengine/ark/10.2.6.3 续租 Work.md` |
| 10.2.6.4 | 查询 Work 队列状态 | 594 | 24922-24954 | 23 | `chapters/volcengine/ark/10.2.6.4 查询 Work 队列状态.md` |
| 10.2.6.5 | 停止 Work | 595-596 | 24955-25025 | 56 | `chapters/volcengine/ark/10.2.6.5 停止 Work.md` |
| 10.2.6.6 | 查询 Work 列表 | 597-599 | 25026-25118 | 77 | `chapters/volcengine/ark/10.2.6.6 查询 Work 列表.md` |
| 10.2.6.7 | 查询 Work 详情 | 600-601 | 25119-25176 | 46 | `chapters/volcengine/ark/10.2.6.7 查询 Work 详情.md` |
| 10.3.1 | 创建会话 | 602-619 | 25178-25935 | 640 | `chapters/volcengine/ark/10.3.1 创建会话.md` |
| 10.3.2 | 查询会话列表 | 620-633 | 25936-26528 | 523 | `chapters/volcengine/ark/10.3.2 查询会话列表.md` |
| 10.3.3 | 查询会话详情 | 634-646 | 26529-27081 | 488 | `chapters/volcengine/ark/10.3.3 查询会话详情.md` |
| 10.3.4 | 更新会话标题和标签 | 647-659 | 27082-27646 | 494 | `chapters/volcengine/ark/10.3.4 更新会话标题和标签.md` |
| 10.3.5 | 升级会话 | 660-674 | 27647-28274 | 547 | `chapters/volcengine/ark/10.3.5 升级会话.md` |
| 10.3.6 | 删除会话 | 675 | 28275-28301 | 20 | `chapters/volcengine/ark/10.3.6 删除会话.md` |
| 10.3.7.1 | 发送会话事件 | 676-677 | 28303-28349 | 33 | `chapters/volcengine/ark/10.3.7.1 发送会话事件.md` |
| 10.3.7.2 | 查询会话事件列表 | 678-679 | 28350-28414 | 50 | `chapters/volcengine/ark/10.3.7.2 查询会话事件列表.md` |
| 10.3.7.3 | 流式获取会话事件 | 680-681 | 28415-28466 | 32 | `chapters/volcengine/ark/10.3.7.3 流式获取会话事件.md` |
| 10.3.7.4 | 会话事件结构参考 - 第1部分 | 682-726 | 28467-30247 | 1641 | `chapters/volcengine/ark/10.3.7.4 会话事件结构参考 - 第1部分.md` |
| 10.3.8.1 | 添加会话资源 | 727-728 | 30249-30301 | 41 | `chapters/volcengine/ark/10.3.8.1 添加会话资源.md` |
| 10.3.8.2 | 查询会话资源列表 | 729-731 | 30302-30393 | 85 | `chapters/volcengine/ark/10.3.8.2 查询会话资源列表.md` |
| 10.3.8.3 | 查询会话资源 | 732 | 30394-30411 | 13 | `chapters/volcengine/ark/10.3.8.3 查询会话资源.md` |
| 10.3.9.1 | 查询线程列表 | 733-734 | 30413-30480 | 56 | `chapters/volcengine/ark/10.3.9.1 查询线程列表.md` |
| 10.3.9.2 | 查询线程详情 | 735-736 | 30481-30529 | 37 | `chapters/volcengine/ark/10.3.9.2 查询线程详情.md` |
| 10.3.9.3 | 查询线程事件列表 | 737-738 | 30530-30592 | 47 | `chapters/volcengine/ark/10.3.9.3 查询线程事件列表.md` |
| 10.3.9.4 | 流式获取线程事件 | 739-740 | 30593-30641 | 30 | `chapters/volcengine/ark/10.3.9.4 流式获取线程事件.md` |
| 10.4.1 | 创建保管库 | 741-742 | 30643-30677 | 28 | `chapters/volcengine/ark/10.4.1 创建保管库.md` |
| 10.4.2 | 查询保管库列表 | 743-744 | 30678-30732 | 45 | `chapters/volcengine/ark/10.4.2 查询保管库列表.md` |
| 10.4.3 | 查询保管库详情 | 745 | 30733-30759 | 24 | `chapters/volcengine/ark/10.4.3 查询保管库详情.md` |
| 10.4.4 | 更新保管库 | 746-747 | 30760-30801 | 33 | `chapters/volcengine/ark/10.4.4 更新保管库.md` |
| 10.4.5 | 删除保管库 | 748 | 30802-30826 | 21 | `chapters/volcengine/ark/10.4.5 删除保管库.md` |
| 10.4.6.1 | 创建凭证 | 749-757 | 30828-31202 | 290 | `chapters/volcengine/ark/10.4.6.1 创建凭证.md` |
| 10.4.6.2 | 查询凭证列表 | 758-762 | 31203-31386 | 153 | `chapters/volcengine/ark/10.4.6.2 查询凭证列表.md` |
| 10.4.6.3 | 查询凭证详情 | 763-766 | 31387-31542 | 131 | `chapters/volcengine/ark/10.4.6.3 查询凭证详情.md` |
| 10.4.6.4 | 更新凭证 | 767-774 | 31543-31888 | 271 | `chapters/volcengine/ark/10.4.6.4 更新凭证.md` |
| 10.4.6.5 | 删除凭证 | 775 | 31889-31915 | 21 | `chapters/volcengine/ark/10.4.6.5 删除凭证.md` |
| 10.5.1 | 创建记忆库 | 776-778 | 31917-31994 | 59 | `chapters/volcengine/ark/10.5.1 创建记忆库.md` |
| 10.5.2 | 查询记忆库列表 | 779-781 | 31995-32094 | 77 | `chapters/volcengine/ark/10.5.2 查询记忆库列表.md` |
| 10.5.3 | 查询记忆库详情 | 782-783 | 32095-32154 | 45 | `chapters/volcengine/ark/10.5.3 查询记忆库详情.md` |
| 10.5.4 | 更新记忆库 | 784-786 | 32155-32233 | 59 | `chapters/volcengine/ark/10.5.4 更新记忆库.md` |
| 10.5.5 | 删除记忆库 | 787 | 32234-32259 | 17 | `chapters/volcengine/ark/10.5.5 删除记忆库.md` |
| 10.5.6.1 | 创建记忆 | 788-789 | 32261-32325 | 51 | `chapters/volcengine/ark/10.5.6.1 创建记忆.md` |
| 10.5.6.2 | 批量创建记忆 | 790-792 | 32326-32440 | 89 | `chapters/volcengine/ark/10.5.6.2 批量创建记忆.md` |
| 10.5.6.3 | 查询记忆列表 | 793-795 | 32441-32532 | 69 | `chapters/volcengine/ark/10.5.6.3 查询记忆列表.md` |
| 10.5.6.4 | 查询记忆详情 | 796-797 | 32533-32591 | 45 | `chapters/volcengine/ark/10.5.6.4 查询记忆详情.md` |
| 10.5.6.5 | 更新记忆 | 798-799 | 32592-32662 | 51 | `chapters/volcengine/ark/10.5.6.5 更新记忆.md` |
| 10.5.6.6 | 删除记忆 | 800 | 32663-32691 | 18 | `chapters/volcengine/ark/10.5.6.6 删除记忆.md` |
| 10.6.1 | 创建 Dream | 801-804 | 32693-32817 | 108 | `chapters/volcengine/ark/10.6.1 创建 Dream.md` |
| 10.6.2 | 查询 Dream 列表 | 805-808 | 32818-32955 | 119 | `chapters/volcengine/ark/10.6.2 查询 Dream 列表.md` |
| 10.6.3 | 查询 Dream | 809-811 | 32956-33051 | 83 | `chapters/volcengine/ark/10.6.3 查询 Dream.md` |
| 10.6.4 | 取消 Dream | 812-814 | 33052-33150 | 84 | `chapters/volcengine/ark/10.6.4 取消 Dream.md` |
| 10.7.1 | 创建技能 | 815-816 | 33152-33220 | 49 | `chapters/volcengine/ark/10.7.1 创建技能.md` |
| 10.7.2 | 查询技能列表 | 817-818 | 33221-33295 | 61 | `chapters/volcengine/ark/10.7.2 查询技能列表.md` |
| 10.7.3 | 查询技能详情 | 819-820 | 33296-33341 | 36 | `chapters/volcengine/ark/10.7.3 查询技能详情.md` |
| 10.7.4 | 设置技能内容保护 | 821-822 | 33342-33387 | 37 | `chapters/volcengine/ark/10.7.4 设置技能内容保护.md` |
| 10.7.5 | 删除技能 | 823 | 33388-33413 | 18 | `chapters/volcengine/ark/10.7.5 删除技能.md` |
| 10.7.6 | 创建新版本的技能 | 824-825 | 33414-33473 | 41 | `chapters/volcengine/ark/10.7.6 创建新版本的技能.md` |
| 10.7.7 | 查询技能的版本列表 | 826-827 | 33474-33529 | 48 | `chapters/volcengine/ark/10.7.7 查询技能的版本列表.md` |
| 10.7.8 | 查询指定版本的技能 | 828 | 33530-33559 | 26 | `chapters/volcengine/ark/10.7.8 查询指定版本的技能.md` |
| 10.7.9 | 删除指定版本的技能 | 829 | 33560-33581 | 17 | `chapters/volcengine/ark/10.7.9 删除指定版本的技能.md` |
| 10.7.10 | 下载指定版本的技能 | 830 | 33582-33600 | 14 | `chapters/volcengine/ark/10.7.10 下载指定版本的技能.md` |
| 10.7.11 | 扫描 GitHub 技能 | 831-832 | 33601-33653 | 43 | `chapters/volcengine/ark/10.7.11 扫描 GitHub 技能.md` |
| 10.7.12 | 导入 GitHub 技能 | 833-834 | 33654-33729 | 58 | `chapters/volcengine/ark/10.7.12 导入 GitHub 技能.md` |
| 11.1.1 | 创建批量推理任务 | 835-838 | 33732-33812 | 60 | `chapters/volcengine/ark/11.1.1 创建批量推理任务.md` |
| 11.1.2 | 获取批量推理任务列表 | 839-843 | 33813-33986 | 152 | `chapters/volcengine/ark/11.1.2 获取批量推理任务列表.md` |
| 11.1.3 | 获取批量推理任务 | 844-846 | 33987-34104 | 102 | `chapters/volcengine/ark/11.1.3 获取批量推理任务.md` |
| 11.1.4 | 更新批量推理任务 | 847 | 34105-34128 | 17 | `chapters/volcengine/ark/11.1.4 更新批量推理任务.md` |
| 11.1.5 | 删除批量推理任务 | 848 | 34129-34148 | 13 | `chapters/volcengine/ark/11.1.5 删除批量推理任务.md` |
| 11.1.6 | 停止批量推理任务 | 849 | 34149-34171 | 16 | `chapters/volcengine/ark/11.1.6 停止批量推理任务.md` |
| 11.1.7 | 重启批量推理任务 | 850 | 34172-34192 | 13 | `chapters/volcengine/ark/11.1.7 重启批量推理任务.md` |
| 11.2 | 批量(Chat) API | 851-865 | 34193-34633 | 339 | `chapters/volcengine/ark/11.2 批量(Chat) API.md` |
| 12.1 | 分词 API | 866-867 | 34635-34681 | 39 | `chapters/volcengine/ark/12.1 分词 API.md` |
| 13.1.1 | 获取临时 API Key | 868 | 34684-34718 | 26 | `chapters/volcengine/ark/13.1.1 获取临时 API Key.md` |
| 13.2.1 | 创建个人版套餐 | 869-870 | 34720-34778 | 34 | `chapters/volcengine/ark/13.2.1 创建个人版套餐.md` |
| 13.2.2 | 续费个人版套餐 | 871-872 | 34779-34824 | 27 | `chapters/volcengine/ark/13.2.2 续费个人版套餐.md` |
| 13.2.3 | 查询个人版套餐 | 873 | 34825-34852 | 21 | `chapters/volcengine/ark/13.2.3 查询个人版套餐.md` |
| 13.2.4.1 | 查询 Agent Plan 支持的模型列表 | 874 | 34854-34873 | 14 | `chapters/volcengine/ark/13.2.4.1 查询 Agent Plan 支持的模型列表.md` |
| 13.2.4.2 | 轮换个人版 API Key | 875 | 34874-34900 | 17 | `chapters/volcengine/ark/13.2.4.2 轮换个人版 API Key.md` |
| 13.2.4.3 | 获取套餐 AFP 额度 | 876-877 | 34901-34975 | 66 | `chapters/volcengine/ark/13.2.4.3 获取套餐 AFP 额度.md` |
| 13.2.4.4 | 获取套餐用量详情 | 878-879 | 34976-35024 | 39 | `chapters/volcengine/ark/13.2.4.4 获取套餐用量详情.md` |
| 13.2.5.1 | 查询 Coding Plan 支持的模型列表 | 880 | 35026-35041 | 12 | `chapters/volcengine/ark/13.2.5.1 查询 Coding Plan 支持的模型列表.md` |
| 13.3.1 | 获取基础模型版本列表 | 881-883 | 35043-35130 | 72 | `chapters/volcengine/ark/13.3.1 获取基础模型版本列表.md` |
| 13.3.2 | 获取基础模型版本信息 | 884-891 | 35131-35448 | 273 | `chapters/volcengine/ark/13.3.2 获取基础模型版本信息.md` |
| 13.3.3 | 获取基础模型列表 | 892-896 | 35449-35693 | 182 | `chapters/volcengine/ark/13.3.3 获取基础模型列表.md` |
| 13.3.4 | 获取基础模型信息 | 897-899 | 35694-35818 | 93 | `chapters/volcengine/ark/13.3.4 获取基础模型信息.md` |
| 13.4.1 | 批量开通基础模型 | 900 | 35820-35834 | 11 | `chapters/volcengine/ark/13.4.1 批量开通基础模型.md` |
| 13.4.2 | 启用自动开通新模型 | 901 | 35835-35846 | 7 | `chapters/volcengine/ark/13.4.2 启用自动开通新模型.md` |
| 13.4.3 | 关闭自动开通新模型 | 902 | 35847-35858 | 7 | `chapters/volcengine/ark/13.4.3 关闭自动开通新模型.md` |
| 13.4.4 | 查询模型开通详情 | 903-906 | 35859-36001 | 131 | `chapters/volcengine/ark/13.4.4 查询模型开通详情.md` |
| 13.4.5 | 查询模型开通列表 | 907-911 | 36002-36179 | 163 | `chapters/volcengine/ark/13.4.5 查询模型开通列表.md` |
| 13.5.1 | 批量开通资源 | 912 | 36181-36199 | 14 | `chapters/volcengine/ark/13.5.1 批量开通资源.md` |
| 13.5.2 | 查询资源开通列表 | 913-915 | 36200-36301 | 92 | `chapters/volcengine/ark/13.5.2 查询资源开通列表.md` |
| 13.6.1 | 查询模型限流 | 916-918 | 36303-36402 | 91 | `chapters/volcengine/ark/13.6.1 查询模型限流.md` |
| 13.7.1 | 删除定制模型 | 919 | 36404-36429 | 17 | `chapters/volcengine/ark/13.7.1 删除定制模型.md` |
| 13.7.2 | 获取定制模型信息 | 920-922 | 36430-36538 | 97 | `chapters/volcengine/ark/13.7.2 获取定制模型信息.md` |
| 13.7.3 | 更新定制模型 | 923 | 36539-36571 | 22 | `chapters/volcengine/ark/13.7.3 更新定制模型.md` |
| 13.7.4 | 获取定制模型列表 | 924-926 | 36572-36690 | 102 | `chapters/volcengine/ark/13.7.4 获取定制模型列表.md` |
| 13.8.1 | 创建模型调优任务 | 927-934 | 36692-37010 | 281 | `chapters/volcengine/ark/13.8.1 创建模型调优任务.md` |
| 13.8.2 | 删除模型调优任务 | 935 | 37011-37027 | 10 | `chapters/volcengine/ark/13.8.2 删除模型调优任务.md` |
| 13.8.3 | 获取模型调优任务信息 | 936-946 | 37028-37481 | 411 | `chapters/volcengine/ark/13.8.3 获取模型调优任务信息.md` |
| 13.8.4 | 查询精调效果指标详细数据 | 947-948 | 37482-37527 | 33 | `chapters/volcengine/ark/13.8.4 查询精调效果指标详细数据.md` |
| 13.8.5 | 查询精调效果指标 | 949 | 37528-37546 | 10 | `chapters/volcengine/ark/13.8.5 查询精调效果指标.md` |
| 13.8.6 | 获取模型调优任务列表 | 950-956 | 37547-37817 | 246 | `chapters/volcengine/ark/13.8.6 获取模型调优任务列表.md` |
| 13.8.7 | 重试模型调优任务 | 957 | 37818-37834 | 9 | `chapters/volcengine/ark/13.8.7 重试模型调优任务.md` |
| 13.8.8 | 停止模型调优任务 | 958 | 37835-37851 | 10 | `chapters/volcengine/ark/13.8.8 停止模型调优任务.md` |
| 13.8.9 | 更新模型调优任务 | 959 | 37852-37875 | 14 | `chapters/volcengine/ark/13.8.9 更新模型调优任务.md` |
| 13.9.1 | 开启推理接入点 | 960 | 37877-37897 | 13 | `chapters/volcengine/ark/13.9.1 开启推理接入点.md` |
| 13.9.2 | 停止推理接入点 | 961 | 37898-37918 | 11 | `chapters/volcengine/ark/13.9.2 停止推理接入点.md` |
| 13.9.3 | 获取推理接入点列表 | 962-966 | 37919-38130 | 170 | `chapters/volcengine/ark/13.9.3 获取推理接入点列表.md` |
| 13.9.4 | 获取推理接入点 | 967-969 | 38131-38232 | 88 | `chapters/volcengine/ark/13.9.4 获取推理接入点.md` |
| 13.9.5 | 删除推理接入点 | 970 | 38233-38252 | 12 | `chapters/volcengine/ark/13.9.5 删除推理接入点.md` |
| 13.9.6 | 更新推理接入点 | 971-975 | 38253-38437 | 160 | `chapters/volcengine/ark/13.9.6 更新推理接入点.md` |
| 13.9.7 | 创建推理接入点 | 976-981 | 38438-38665 | 193 | `chapters/volcengine/ark/13.9.7 创建推理接入点.md` |
| 13.9.8 | 获取接入点推理应用层加密证书 | 982-983 | 38666-38701 | 23 | `chapters/volcengine/ark/13.9.8 获取接入点推理应用层加密证书.md` |
| 13.9.9 | 创建推理接入点滚动升级任务 | 984-985 | 38702-38749 | 41 | `chapters/volcengine/ark/13.9.9 创建推理接入点滚动升级任务.md` |
| 13.9.10 | 查询推理接入点滚动升级详情 | 986-989 | 38750-38876 | 116 | `chapters/volcengine/ark/13.9.10 查询推理接入点滚动升级详情.md` |
| 13.9.11 | 回滚推理接入点滚动升级 | 990 | 38877-38894 | 13 | `chapters/volcengine/ark/13.9.11 回滚推理接入点滚动升级.md` |
| 13.9.12 | 取消推理接入点滚动升级 | 991 | 38895-38912 | 13 | `chapters/volcengine/ark/13.9.12 取消推理接入点滚动升级.md` |
| 13.10.1 | 创建评测任务 | 992-995 | 38914-39079 | 133 | `chapters/volcengine/ark/13.10.1 创建评测任务.md` |
| 13.10.2 | 删除评测任务 | 996 | 39080-39101 | 13 | `chapters/volcengine/ark/13.10.2 删除评测任务.md` |
| 13.10.3 | 获取评测任务 | 997-999 | 39102-39183 | 66 | `chapters/volcengine/ark/13.10.3 获取评测任务.md` |
| 13.10.4 | 获取评测任务结果 | 1000-1002 | 39184-39286 | 87 | `chapters/volcengine/ark/13.10.4 获取评测任务结果.md` |
| 13.10.5 | 获取评测任务列表 | 1003-1006 | 39287-39433 | 129 | `chapters/volcengine/ark/13.10.5 获取评测任务列表.md` |
| 13.10.6 | 获取评测任务结果列表 | 1007-1010 | 39434-39575 | 120 | `chapters/volcengine/ark/13.10.6 获取评测任务结果列表.md` |
| 13.10.7 | 停止评测任务 | 1011 | 39576-39597 | 13 | `chapters/volcengine/ark/13.10.7 停止评测任务.md` |
| 13.10.8 | 更新评测任务 | 1012 | 39598-39623 | 18 | `chapters/volcengine/ark/13.10.8 更新评测任务.md` |
| 13.11.1 | 查询推理用量 | 1013-1015 | 39625-39752 | 75 | `chapters/volcengine/ark/13.11.1 查询推理用量.md` |
| 13.11.2 | 创建用量明细导出任务 | 1016-1017 | 39753-39805 | 33 | `chapters/volcengine/ark/13.11.2 创建用量明细导出任务.md` |
| 13.11.3 | 查询用量明细导出任务状态 | 1018-1020 | 39806-39908 | 71 | `chapters/volcengine/ark/13.11.3 查询用量明细导出任务状态.md` |
| 13.11.4 | 查询模型推理限额 | 1021 | 39909-39936 | 22 | `chapters/volcengine/ark/13.11.4 查询模型推理限额.md` |
| 13.11.5 | 开启模型推理限额 | 1022 | 39937-39961 | 16 | `chapters/volcengine/ark/13.11.5 开启模型推理限额.md` |
| 13.11.6 | 关闭模型推理限额 | 1023 | 39962-39982 | 12 | `chapters/volcengine/ark/13.11.6 关闭模型推理限额.md` |
| 13.12.1 | 创建方舟官方模型产物查询请求 | 1024 | 39984-40002 | 14 | `chapters/volcengine/ark/13.12.1 创建方舟官方模型产物查询请求.md` |
| 13.12.2 | 获取安全审计日志 | 1025-1027 | 40003-40122 | 85 | `chapters/volcengine/ark/13.12.2 获取安全审计日志.md` |
| 13.12.3 | 获取方舟官方产物确认结果 | 1028 | 40123-40152 | 24 | `chapters/volcengine/ark/13.12.3 获取方舟官方产物确认结果.md` |
| 13.13.1 | 上报视频生成模型效果问题 | 1029-1031 | 40154-40277 | 86 | `chapters/volcengine/ark/13.13.1 上报视频生成模型效果问题.md` |
| 13.13.2 | 查询视频生成模型效果问题结果 | 1032-1035 | 40278-40366 | 69 | `chapters/volcengine/ark/13.13.2 查询视频生成模型效果问题结果.md` |
| 13.13.3 | 上报大语言模型效果问题 | 1036-1038 | 40367-40475 | 82 | `chapters/volcengine/ark/13.13.3 上报大语言模型效果问题.md` |
| 13.13.4 | 查询大语言模型效果问题结果 | 1039-1041 | 40476-40591 | 97 | `chapters/volcengine/ark/13.13.4 查询大语言模型效果问题结果.md` |
| 14.1 | 兼容 OpenAI SDK | 1042-1045 | 40593-40709 | 103 | `chapters/volcengine/ark/14.1 兼容 OpenAI SDK.md` |
| 14.2 | 向后兼容性 | 1046 | 40710-40755 | 25 | `chapters/volcengine/ark/14.2 向后兼容性.md` |
| 14.3 | 错误码 - 第1部分 | 1046-1068 | 40756-42720 | 1915 | `chapters/volcengine/ark/14.3 错误码 - 第1部分.md` |
| 14.3 | 错误码 - 第2部分·错误码 | 1069-1076 | 42721-43319 | 569 | `chapters/volcengine/ark/14.3 错误码 - 第2部分·错误码.md` |
| 14.4 | SDK 常见使用示例 | 1077-1092 | 43320-43908 | 521 | `chapters/volcengine/ark/14.4 SDK 常见使用示例.md` |
