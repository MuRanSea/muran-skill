# 方舟 API 区章节表（ark）

来源：《火山方舟 API 参考》（1108 页）。198 个章节文件，接口级切分：一个接口/任务一个文件；超过 1500 行的按语义块自动再拆为`… - 第N部分`（5 个章节被拆分）。

「页码」是原 PDF 页码范围；「行范围」是中间 MD（`doc/<源文档>.md`）的 1 起始行号，可据此回查原文。章节文件本身已去掉页眉页脚，回查 PDF 时用这两列。文件名即章节标题，日常定位直接 Glob 文件名即可，用不到这两列。

**这张表用来 grep，不要整读。**

| 编号 | 标题 | 页码 | 行范围(源文件) | 行数 | 文件 |
|------|------|------|---------------|------|------|
| 1.1 | 获取 API Key 并配置 | 1 | 276-311 | 20 | `chapters/volcengine/ark/1.1 获取 API Key 并配置.md` |
| 1.2 | 安装及升级 SDK | 2-7 | 312-470 | 122 | `chapters/volcengine/ark/1.2 安装及升级 SDK.md` |
| 1.3 | Base URL及鉴权 | 8-10 | 471-566 | 68 | `chapters/volcengine/ark/1.3 Base URL及鉴权.md` |
| 2.1 | 对话(Chat) API | 11-37 | 568-1811 | 917 | `chapters/volcengine/ark/2.1 对话(Chat) API.md` |
| 3.1 | 创建 Response - 第1部分 | 38-76 | 1812-3495 | 1442 | `chapters/volcengine/ark/3.1 创建 Response - 第1部分.md` |
| 3.1 | 创建 Response - 第2部分·响应参数 | 77-108 | 3496-4850 | 1209 | `chapters/volcengine/ark/3.1 创建 Response - 第2部分·响应参数.md` |
| 3.2 | 查询 Response 详情 | 109-135 | 4851-5985 | 1062 | `chapters/volcengine/ark/3.2 查询 Response 详情.md` |
| 3.3 | 查询 Response 输入项列表 | 136-157 | 5986-6884 | 831 | `chapters/volcengine/ark/3.3 查询 Response 输入项列表.md` |
| 3.4 | 删除 Response | 158 | 6885-6908 | 19 | `chapters/volcengine/ark/3.4 删除 Response.md` |
| 3.5.1 | Response 生命周期 - 第1部分 | 159-196 | 6909-8558 | 1474 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第1部分.md` |
| 3.5.1 | Response 生命周期 - 第2部分 | 197-234 | 8559-10222 | 1489 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第2部分.md` |
| 3.5.1 | Response 生命周期 - 第3部分 | 235-272 | 10223-11873 | 1483 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第3部分.md` |
| 3.5.1 | Response 生命周期 - 第4部分 | 273-319 | 11874-13891 | 1778 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第4部分.md` |
| 3.5.2 | Output Item 与文本回答 - 第1部分 | 320-355 | 13892-15466 | 1447 | `chapters/volcengine/ark/3.5.2 Output Item 与文本回答 - 第1部分.md` |
| 3.5.2 | Output Item 与文本回答 - 第2部分 | 356-371 | 15467-16113 | 615 | `chapters/volcengine/ark/3.5.2 Output Item 与文本回答 - 第2部分.md` |
| 3.5.3 | 工具调用事件 | 372-398 | 16114-17194 | 1024 | `chapters/volcengine/ark/3.5.3 工具调用事件.md` |
| 3.5.4 | 语音转写与错误事件 | 399-403 | 17195-17365 | 161 | `chapters/volcengine/ark/3.5.4 语音转写与错误事件.md` |
| 4.1 | 创建 Message | 404-419 | 17367-18008 | 564 | `chapters/volcengine/ark/4.1 创建 Message.md` |
| 4.2 | 统计 Messages 请求 token 数 | 420-427 | 18009-18342 | 279 | `chapters/volcengine/ark/4.2 统计 Messages 请求 token 数.md` |
| 5.1 | 上传文件 | 428-433 | 18344-18558 | 159 | `chapters/volcengine/ark/5.1 上传文件.md` |
| 5.2 | 查询文件详情 | 434-435 | 18559-18630 | 63 | `chapters/volcengine/ark/5.2 查询文件详情.md` |
| 5.3 | 查询文件列表 | 436-439 | 18631-18765 | 112 | `chapters/volcengine/ark/5.3 查询文件列表.md` |
| 5.4 | 删除文件 | 440 | 18766-18788 | 19 | `chapters/volcengine/ark/5.4 删除文件.md` |
| 5.5 | The file object | 441-443 | 18789-18860 | 57 | `chapters/volcengine/ark/5.5 The file object.md` |
| 6.1 | 创建视频生成任务 | 444-460 | 18862-19734 | 613 | `chapters/volcengine/ark/6.1 创建视频生成任务.md` |
| 6.2 | 查询视频生成任务 | 461-464 | 19735-19875 | 105 | `chapters/volcengine/ark/6.2 查询视频生成任务.md` |
| 6.3 | 查询视频生成任务列表 | 465-469 | 19876-20078 | 156 | `chapters/volcengine/ark/6.3 查询视频生成任务列表.md` |
| 6.4 | 取消或删除视频生成任务 | 470 | 20079-20120 | 38 | `chapters/volcengine/ark/6.4 取消或删除视频生成任务.md` |
| 7.1 | 图片生成 API | 471-487 | 20122-20875 | 531 | `chapters/volcengine/ark/7.1 图片生成 API.md` |
| 7.2 | 图片生成流式响应事件 | 488-492 | 20876-21052 | 158 | `chapters/volcengine/ark/7.2 图片生成流式响应事件.md` |
| 8.1.1 | 创建 3D 生成任务 API | 493-495 | 21055-21158 | 80 | `chapters/volcengine/ark/8.1.1 创建 3D 生成任务 API.md` |
| 8.1.2 | 查询 3D 生成任务 API | 496-497 | 21159-21228 | 52 | `chapters/volcengine/ark/8.1.2 查询 3D 生成任务 API.md` |
| 8.1.3 | 查询 3D 生成任务列表 | 498-500 | 21229-21342 | 87 | `chapters/volcengine/ark/8.1.3 查询 3D 生成任务列表.md` |
| 8.1.4 | 取消或删除 3D 生成任务 | 501 | 21343-21384 | 38 | `chapters/volcengine/ark/8.1.4 取消或删除 3D 生成任务.md` |
| 8.2.1 | 创建3D生成任务 | 502-506 | 21386-21600 | 148 | `chapters/volcengine/ark/8.2.1 创建3D生成任务.md` |
| 8.2.2 | 查询3D生成任务 | 507-508 | 21601-21666 | 48 | `chapters/volcengine/ark/8.2.2 查询3D生成任务.md` |
| 8.2.3 | 查询3D生成任务列表 | 509-511 | 21667-21774 | 81 | `chapters/volcengine/ark/8.2.3 查询3D生成任务列表.md` |
| 8.2.4 | 取消或删除3D生成任务 | 512 | 21775-21809 | 31 | `chapters/volcengine/ark/8.2.4 取消或删除3D生成任务.md` |
| 8.3.1 | 创建3D生成任务 | 513-516 | 21811-21942 | 95 | `chapters/volcengine/ark/8.3.1 创建3D生成任务.md` |
| 8.3.2 | 查询3D生成任务 | 517-518 | 21943-22008 | 48 | `chapters/volcengine/ark/8.3.2 查询3D生成任务.md` |
| 8.3.3 | 查询3D生成任务列表 | 519-521 | 22009-22116 | 81 | `chapters/volcengine/ark/8.3.3 查询3D生成任务列表.md` |
| 8.3.4 | 取消或删除3D生成任务 | 522 | 22117-22151 | 31 | `chapters/volcengine/ark/8.3.4 取消或删除3D生成任务.md` |
| 9.1 | 多模态向量化 API | 523-527 | 22153-22351 | 147 | `chapters/volcengine/ark/9.1 多模态向量化 API.md` |
| 10.1.1 | 创建智能体 | 528-538 | 22354-22830 | 372 | `chapters/volcengine/ark/10.1.1 创建智能体.md` |
| 10.1.2 | 查询智能体列表 | 539-544 | 22831-23087 | 215 | `chapters/volcengine/ark/10.1.2 查询智能体列表.md` |
| 10.1.3 | 查询智能体详情 | 545-550 | 23088-23309 | 180 | `chapters/volcengine/ark/10.1.3 查询智能体详情.md` |
| 10.1.4 | 更新智能体 | 551-562 | 23310-23833 | 384 | `chapters/volcengine/ark/10.1.4 更新智能体.md` |
| 10.1.5 | 删除智能体 | 563 | 23834-23854 | 14 | `chapters/volcengine/ark/10.1.5 删除智能体.md` |
| 10.1.6 | 查询智能体版本列表 | 564-569 | 23855-24100 | 202 | `chapters/volcengine/ark/10.1.6 查询智能体版本列表.md` |
| 10.2.1 | 创建环境 | 570-574 | 24102-24278 | 144 | `chapters/volcengine/ark/10.2.1 创建环境.md` |
| 10.2.2 | 查询环境列表 | 575-577 | 24279-24383 | 95 | `chapters/volcengine/ark/10.2.2 查询环境列表.md` |
| 10.2.3 | 查询环境详情 | 578-580 | 24384-24471 | 76 | `chapters/volcengine/ark/10.2.3 查询环境详情.md` |
| 10.2.4 | 更新环境 | 581-585 | 24472-24671 | 156 | `chapters/volcengine/ark/10.2.4 更新环境.md` |
| 10.2.5 | 删除环境 | 586 | 24672-24694 | 19 | `chapters/volcengine/ark/10.2.5 删除环境.md` |
| 10.2.6.1 | 长轮询拉取待执行 Work | 587-589 | 24696-24787 | 69 | `chapters/volcengine/ark/10.2.6.1 长轮询拉取待执行 Work.md` |
| 10.2.6.2 | 认领 Work | 590-591 | 24788-24858 | 56 | `chapters/volcengine/ark/10.2.6.2 认领 Work.md` |
| 10.2.6.3 | 续租 Work | 592-593 | 24859-24914 | 41 | `chapters/volcengine/ark/10.2.6.3 续租 Work.md` |
| 10.2.6.4 | 查询 Work 队列状态 | 594 | 24915-24947 | 23 | `chapters/volcengine/ark/10.2.6.4 查询 Work 队列状态.md` |
| 10.2.6.5 | 停止 Work | 595-596 | 24948-25018 | 56 | `chapters/volcengine/ark/10.2.6.5 停止 Work.md` |
| 10.2.6.6 | 查询 Work 列表 | 597-599 | 25019-25111 | 77 | `chapters/volcengine/ark/10.2.6.6 查询 Work 列表.md` |
| 10.2.6.7 | 查询 Work 详情 | 600-601 | 25112-25169 | 46 | `chapters/volcengine/ark/10.2.6.7 查询 Work 详情.md` |
| 10.3.1 | 创建会话 | 602-624 | 25171-26163 | 809 | `chapters/volcengine/ark/10.3.1 创建会话.md` |
| 10.3.2 | 查询会话列表 | 625-638 | 26164-26761 | 527 | `chapters/volcengine/ark/10.3.2 查询会话列表.md` |
| 10.3.3 | 查询会话详情 | 639-651 | 26762-27319 | 492 | `chapters/volcengine/ark/10.3.3 查询会话详情.md` |
| 10.3.4 | 更新会话标题和标签 | 652-664 | 27320-27889 | 498 | `chapters/volcengine/ark/10.3.4 更新会话标题和标签.md` |
| 10.3.5 | 升级会话 | 665-679 | 27890-28522 | 551 | `chapters/volcengine/ark/10.3.5 升级会话.md` |
| 10.3.6 | 删除会话 | 680 | 28523-28549 | 20 | `chapters/volcengine/ark/10.3.6 删除会话.md` |
| 10.3.7.1 | 发送会话事件 | 681-682 | 28551-28597 | 33 | `chapters/volcengine/ark/10.3.7.1 发送会话事件.md` |
| 10.3.7.2 | 查询会话事件列表 | 683-684 | 28598-28662 | 50 | `chapters/volcengine/ark/10.3.7.2 查询会话事件列表.md` |
| 10.3.7.3 | 流式获取会话事件 | 685-686 | 28663-28723 | 35 | `chapters/volcengine/ark/10.3.7.3 流式获取会话事件.md` |
| 10.3.7.4 | 会话事件结构参考 - 第1部分 | 687-732 | 28724-30519 | 1653 | `chapters/volcengine/ark/10.3.7.4 会话事件结构参考 - 第1部分.md` |
| 10.3.8.1 | 添加会话资源 | 733-734 | 30521-30573 | 41 | `chapters/volcengine/ark/10.3.8.1 添加会话资源.md` |
| 10.3.8.2 | 查询会话资源列表 | 735-737 | 30574-30665 | 85 | `chapters/volcengine/ark/10.3.8.2 查询会话资源列表.md` |
| 10.3.8.3 | 查询会话资源 | 738 | 30666-30683 | 13 | `chapters/volcengine/ark/10.3.8.3 查询会话资源.md` |
| 10.3.9.1 | 查询线程列表 | 739-740 | 30685-30752 | 56 | `chapters/volcengine/ark/10.3.9.1 查询线程列表.md` |
| 10.3.9.2 | 查询线程详情 | 741-742 | 30753-30801 | 37 | `chapters/volcengine/ark/10.3.9.2 查询线程详情.md` |
| 10.3.9.3 | 查询线程事件列表 | 743-744 | 30802-30864 | 47 | `chapters/volcengine/ark/10.3.9.3 查询线程事件列表.md` |
| 10.3.9.4 | 流式获取线程事件 | 745-746 | 30865-30913 | 30 | `chapters/volcengine/ark/10.3.9.4 流式获取线程事件.md` |
| 10.4.1 | 创建保管库 | 747-748 | 30915-30949 | 28 | `chapters/volcengine/ark/10.4.1 创建保管库.md` |
| 10.4.2 | 查询保管库列表 | 749-750 | 30950-31004 | 45 | `chapters/volcengine/ark/10.4.2 查询保管库列表.md` |
| 10.4.3 | 查询保管库详情 | 751 | 31005-31031 | 24 | `chapters/volcengine/ark/10.4.3 查询保管库详情.md` |
| 10.4.4 | 更新保管库 | 752-753 | 31032-31073 | 33 | `chapters/volcengine/ark/10.4.4 更新保管库.md` |
| 10.4.5 | 删除保管库 | 754 | 31074-31098 | 21 | `chapters/volcengine/ark/10.4.5 删除保管库.md` |
| 10.4.6.1 | 创建凭证 | 755-764 | 31100-31563 | 358 | `chapters/volcengine/ark/10.4.6.1 创建凭证.md` |
| 10.4.6.2 | 查询凭证列表 | 765-769 | 31564-31784 | 182 | `chapters/volcengine/ark/10.4.6.2 查询凭证列表.md` |
| 10.4.6.3 | 查询凭证详情 | 770-774 | 31785-31979 | 160 | `chapters/volcengine/ark/10.4.6.3 查询凭证详情.md` |
| 10.4.6.4 | 更新凭证 | 775-784 | 31980-32416 | 334 | `chapters/volcengine/ark/10.4.6.4 更新凭证.md` |
| 10.4.6.5 | 删除凭证 | 785 | 32417-32443 | 21 | `chapters/volcengine/ark/10.4.6.5 删除凭证.md` |
| 10.5.1 | 创建记忆库 | 786-788 | 32445-32522 | 59 | `chapters/volcengine/ark/10.5.1 创建记忆库.md` |
| 10.5.2 | 查询记忆库列表 | 789-791 | 32523-32622 | 77 | `chapters/volcengine/ark/10.5.2 查询记忆库列表.md` |
| 10.5.3 | 查询记忆库详情 | 792-793 | 32623-32682 | 45 | `chapters/volcengine/ark/10.5.3 查询记忆库详情.md` |
| 10.5.4 | 更新记忆库 | 794-796 | 32683-32761 | 59 | `chapters/volcengine/ark/10.5.4 更新记忆库.md` |
| 10.5.5 | 删除记忆库 | 797 | 32762-32787 | 17 | `chapters/volcengine/ark/10.5.5 删除记忆库.md` |
| 10.5.6.1 | 创建记忆 | 798-799 | 32789-32853 | 51 | `chapters/volcengine/ark/10.5.6.1 创建记忆.md` |
| 10.5.6.2 | 批量创建记忆 | 800-802 | 32854-32968 | 89 | `chapters/volcengine/ark/10.5.6.2 批量创建记忆.md` |
| 10.5.6.3 | 查询记忆列表 | 803-805 | 32969-33060 | 69 | `chapters/volcengine/ark/10.5.6.3 查询记忆列表.md` |
| 10.5.6.4 | 查询记忆详情 | 806-807 | 33061-33119 | 45 | `chapters/volcengine/ark/10.5.6.4 查询记忆详情.md` |
| 10.5.6.5 | 更新记忆 | 808-809 | 33120-33190 | 51 | `chapters/volcengine/ark/10.5.6.5 更新记忆.md` |
| 10.5.6.6 | 删除记忆 | 810 | 33191-33219 | 18 | `chapters/volcengine/ark/10.5.6.6 删除记忆.md` |
| 10.6.1 | 创建 Dream | 811-814 | 33221-33345 | 108 | `chapters/volcengine/ark/10.6.1 创建 Dream.md` |
| 10.6.2 | 查询 Dream 列表 | 815-818 | 33346-33483 | 119 | `chapters/volcengine/ark/10.6.2 查询 Dream 列表.md` |
| 10.6.3 | 查询 Dream | 819-821 | 33484-33579 | 83 | `chapters/volcengine/ark/10.6.3 查询 Dream.md` |
| 10.6.4 | 取消 Dream | 822-824 | 33580-33678 | 84 | `chapters/volcengine/ark/10.6.4 取消 Dream.md` |
| 10.7.1 | 创建技能 | 825-826 | 33680-33748 | 49 | `chapters/volcengine/ark/10.7.1 创建技能.md` |
| 10.7.2 | 查询技能列表 | 827-828 | 33749-33823 | 61 | `chapters/volcengine/ark/10.7.2 查询技能列表.md` |
| 10.7.3 | 查询技能详情 | 829-830 | 33824-33869 | 36 | `chapters/volcengine/ark/10.7.3 查询技能详情.md` |
| 10.7.4 | 设置技能内容保护 | 831-832 | 33870-33915 | 37 | `chapters/volcengine/ark/10.7.4 设置技能内容保护.md` |
| 10.7.5 | 删除技能 | 833 | 33916-33941 | 18 | `chapters/volcengine/ark/10.7.5 删除技能.md` |
| 10.7.6 | 创建新版本的技能 | 834-835 | 33942-34001 | 41 | `chapters/volcengine/ark/10.7.6 创建新版本的技能.md` |
| 10.7.7 | 查询技能的版本列表 | 836-837 | 34002-34057 | 48 | `chapters/volcengine/ark/10.7.7 查询技能的版本列表.md` |
| 10.7.8 | 查询指定版本的技能 | 838 | 34058-34087 | 26 | `chapters/volcengine/ark/10.7.8 查询指定版本的技能.md` |
| 10.7.9 | 删除指定版本的技能 | 839 | 34088-34109 | 17 | `chapters/volcengine/ark/10.7.9 删除指定版本的技能.md` |
| 10.7.10 | 下载指定版本的技能 | 840 | 34110-34128 | 14 | `chapters/volcengine/ark/10.7.10 下载指定版本的技能.md` |
| 10.7.11 | 扫描 GitHub 技能 | 841-842 | 34129-34181 | 43 | `chapters/volcengine/ark/10.7.11 扫描 GitHub 技能.md` |
| 10.7.12 | 导入 GitHub 技能 | 843-844 | 34182-34257 | 58 | `chapters/volcengine/ark/10.7.12 导入 GitHub 技能.md` |
| 11.1.1 | 创建批量推理任务 | 845-848 | 34260-34340 | 60 | `chapters/volcengine/ark/11.1.1 创建批量推理任务.md` |
| 11.1.2 | 获取批量推理任务列表 | 849-853 | 34341-34514 | 152 | `chapters/volcengine/ark/11.1.2 获取批量推理任务列表.md` |
| 11.1.3 | 获取批量推理任务 | 854-856 | 34515-34632 | 102 | `chapters/volcengine/ark/11.1.3 获取批量推理任务.md` |
| 11.1.4 | 更新批量推理任务 | 857 | 34633-34656 | 17 | `chapters/volcengine/ark/11.1.4 更新批量推理任务.md` |
| 11.1.5 | 删除批量推理任务 | 858 | 34657-34676 | 13 | `chapters/volcengine/ark/11.1.5 删除批量推理任务.md` |
| 11.1.6 | 停止批量推理任务 | 859 | 34677-34699 | 16 | `chapters/volcengine/ark/11.1.6 停止批量推理任务.md` |
| 11.1.7 | 重启批量推理任务 | 860 | 34700-34720 | 13 | `chapters/volcengine/ark/11.1.7 重启批量推理任务.md` |
| 11.2 | 批量(Chat) API | 861-875 | 34721-35161 | 339 | `chapters/volcengine/ark/11.2 批量(Chat) API.md` |
| 12.1 | 分词 API | 876-877 | 35163-35209 | 39 | `chapters/volcengine/ark/12.1 分词 API.md` |
| 13.1.1 | 获取临时 API Key | 878 | 35212-35246 | 26 | `chapters/volcengine/ark/13.1.1 获取临时 API Key.md` |
| 13.2.1 | 创建个人版套餐 | 879-880 | 35248-35306 | 34 | `chapters/volcengine/ark/13.2.1 创建个人版套餐.md` |
| 13.2.2 | 续费个人版套餐 | 881-882 | 35307-35352 | 27 | `chapters/volcengine/ark/13.2.2 续费个人版套餐.md` |
| 13.2.3 | 查询个人版套餐 | 883 | 35353-35380 | 21 | `chapters/volcengine/ark/13.2.3 查询个人版套餐.md` |
| 13.2.4.1 | 查询 Agent Plan 支持的模型列表 | 884 | 35382-35401 | 14 | `chapters/volcengine/ark/13.2.4.1 查询 Agent Plan 支持的模型列表.md` |
| 13.2.4.2 | 轮换个人版 API Key | 885 | 35402-35428 | 17 | `chapters/volcengine/ark/13.2.4.2 轮换个人版 API Key.md` |
| 13.2.4.3 | 获取套餐 AFP 额度 | 886-887 | 35429-35503 | 66 | `chapters/volcengine/ark/13.2.4.3 获取套餐 AFP 额度.md` |
| 13.2.4.4 | 获取套餐用量详情 | 888-889 | 35504-35552 | 39 | `chapters/volcengine/ark/13.2.4.4 获取套餐用量详情.md` |
| 13.2.5.1 | 查询 Coding Plan 支持的模型列表 | 890 | 35554-35569 | 12 | `chapters/volcengine/ark/13.2.5.1 查询 Coding Plan 支持的模型列表.md` |
| 13.3.1 | 获取基础模型版本列表 | 891-893 | 35571-35658 | 72 | `chapters/volcengine/ark/13.3.1 获取基础模型版本列表.md` |
| 13.3.2 | 获取基础模型版本信息 | 894-901 | 35659-35976 | 273 | `chapters/volcengine/ark/13.3.2 获取基础模型版本信息.md` |
| 13.3.3 | 获取基础模型列表 | 902-906 | 35977-36221 | 182 | `chapters/volcengine/ark/13.3.3 获取基础模型列表.md` |
| 13.3.4 | 获取基础模型信息 | 907-909 | 36222-36346 | 93 | `chapters/volcengine/ark/13.3.4 获取基础模型信息.md` |
| 13.4.1 | 批量开通基础模型 | 910 | 36348-36362 | 11 | `chapters/volcengine/ark/13.4.1 批量开通基础模型.md` |
| 13.4.2 | 启用自动开通新模型 | 911 | 36363-36374 | 7 | `chapters/volcengine/ark/13.4.2 启用自动开通新模型.md` |
| 13.4.3 | 关闭自动开通新模型 | 912 | 36375-36386 | 7 | `chapters/volcengine/ark/13.4.3 关闭自动开通新模型.md` |
| 13.4.4 | 查询模型开通详情 | 913-916 | 36387-36529 | 131 | `chapters/volcengine/ark/13.4.4 查询模型开通详情.md` |
| 13.4.5 | 查询模型开通列表 | 917-921 | 36530-36707 | 163 | `chapters/volcengine/ark/13.4.5 查询模型开通列表.md` |
| 13.5.1 | 批量开通资源 | 922 | 36709-36727 | 14 | `chapters/volcengine/ark/13.5.1 批量开通资源.md` |
| 13.5.2 | 查询资源开通列表 | 923-925 | 36728-36829 | 92 | `chapters/volcengine/ark/13.5.2 查询资源开通列表.md` |
| 13.6.1 | 查询模型限流 | 926-928 | 36831-36930 | 91 | `chapters/volcengine/ark/13.6.1 查询模型限流.md` |
| 13.7.1 | 删除定制模型 | 929 | 36932-36957 | 17 | `chapters/volcengine/ark/13.7.1 删除定制模型.md` |
| 13.7.2 | 获取定制模型信息 | 930-932 | 36958-37066 | 97 | `chapters/volcengine/ark/13.7.2 获取定制模型信息.md` |
| 13.7.3 | 更新定制模型 | 933 | 37067-37099 | 22 | `chapters/volcengine/ark/13.7.3 更新定制模型.md` |
| 13.7.4 | 获取定制模型列表 | 934-936 | 37100-37218 | 102 | `chapters/volcengine/ark/13.7.4 获取定制模型列表.md` |
| 13.8.1 | 创建模型调优任务 | 937-944 | 37220-37538 | 281 | `chapters/volcengine/ark/13.8.1 创建模型调优任务.md` |
| 13.8.2 | 删除模型调优任务 | 945 | 37539-37555 | 10 | `chapters/volcengine/ark/13.8.2 删除模型调优任务.md` |
| 13.8.3 | 获取模型调优任务信息 | 946-956 | 37556-38009 | 411 | `chapters/volcengine/ark/13.8.3 获取模型调优任务信息.md` |
| 13.8.4 | 查询精调效果指标详细数据 | 957-958 | 38010-38055 | 33 | `chapters/volcengine/ark/13.8.4 查询精调效果指标详细数据.md` |
| 13.8.5 | 查询精调效果指标 | 959 | 38056-38074 | 10 | `chapters/volcengine/ark/13.8.5 查询精调效果指标.md` |
| 13.8.6 | 获取模型调优任务列表 | 960-966 | 38075-38345 | 246 | `chapters/volcengine/ark/13.8.6 获取模型调优任务列表.md` |
| 13.8.7 | 重试模型调优任务 | 967 | 38346-38362 | 9 | `chapters/volcengine/ark/13.8.7 重试模型调优任务.md` |
| 13.8.8 | 停止模型调优任务 | 968 | 38363-38379 | 10 | `chapters/volcengine/ark/13.8.8 停止模型调优任务.md` |
| 13.8.9 | 更新模型调优任务 | 969 | 38380-38403 | 14 | `chapters/volcengine/ark/13.8.9 更新模型调优任务.md` |
| 13.9.1 | 开启推理接入点 | 970 | 38405-38425 | 13 | `chapters/volcengine/ark/13.9.1 开启推理接入点.md` |
| 13.9.2 | 停止推理接入点 | 971 | 38426-38446 | 11 | `chapters/volcengine/ark/13.9.2 停止推理接入点.md` |
| 13.9.3 | 获取推理接入点列表 | 972-976 | 38447-38658 | 170 | `chapters/volcengine/ark/13.9.3 获取推理接入点列表.md` |
| 13.9.4 | 获取推理接入点 | 977-979 | 38659-38760 | 88 | `chapters/volcengine/ark/13.9.4 获取推理接入点.md` |
| 13.9.5 | 删除推理接入点 | 980 | 38761-38780 | 12 | `chapters/volcengine/ark/13.9.5 删除推理接入点.md` |
| 13.9.6 | 更新推理接入点 | 981-985 | 38781-38965 | 160 | `chapters/volcengine/ark/13.9.6 更新推理接入点.md` |
| 13.9.7 | 创建推理接入点 | 986-991 | 38966-39193 | 193 | `chapters/volcengine/ark/13.9.7 创建推理接入点.md` |
| 13.9.8 | 获取接入点推理应用层加密证书 | 992-993 | 39194-39229 | 23 | `chapters/volcengine/ark/13.9.8 获取接入点推理应用层加密证书.md` |
| 13.9.9 | 创建推理接入点滚动升级任务 | 994-995 | 39230-39277 | 41 | `chapters/volcengine/ark/13.9.9 创建推理接入点滚动升级任务.md` |
| 13.9.10 | 查询推理接入点滚动升级详情 | 996-999 | 39278-39404 | 116 | `chapters/volcengine/ark/13.9.10 查询推理接入点滚动升级详情.md` |
| 13.9.11 | 回滚推理接入点滚动升级 | 1000 | 39405-39422 | 13 | `chapters/volcengine/ark/13.9.11 回滚推理接入点滚动升级.md` |
| 13.9.12 | 取消推理接入点滚动升级 | 1001 | 39423-39440 | 13 | `chapters/volcengine/ark/13.9.12 取消推理接入点滚动升级.md` |
| 13.10.1 | 创建评测任务 | 1002-1005 | 39442-39607 | 133 | `chapters/volcengine/ark/13.10.1 创建评测任务.md` |
| 13.10.2 | 删除评测任务 | 1006 | 39608-39629 | 13 | `chapters/volcengine/ark/13.10.2 删除评测任务.md` |
| 13.10.3 | 获取评测任务 | 1007-1009 | 39630-39711 | 66 | `chapters/volcengine/ark/13.10.3 获取评测任务.md` |
| 13.10.4 | 获取评测任务结果 | 1010-1012 | 39712-39814 | 87 | `chapters/volcengine/ark/13.10.4 获取评测任务结果.md` |
| 13.10.5 | 获取评测任务列表 | 1013-1016 | 39815-39961 | 129 | `chapters/volcengine/ark/13.10.5 获取评测任务列表.md` |
| 13.10.6 | 获取评测任务结果列表 | 1017-1020 | 39962-40103 | 120 | `chapters/volcengine/ark/13.10.6 获取评测任务结果列表.md` |
| 13.10.7 | 停止评测任务 | 1021 | 40104-40125 | 13 | `chapters/volcengine/ark/13.10.7 停止评测任务.md` |
| 13.10.8 | 更新评测任务 | 1022 | 40126-40151 | 18 | `chapters/volcengine/ark/13.10.8 更新评测任务.md` |
| 13.11.1 | 查询推理用量 | 1023-1025 | 40153-40280 | 75 | `chapters/volcengine/ark/13.11.1 查询推理用量.md` |
| 13.11.2 | 查询单请求用量 | 1026-1029 | 40281-40419 | 124 | `chapters/volcengine/ark/13.11.2 查询单请求用量.md` |
| 13.11.3 | 查询异步任务用量 | 1030-1031 | 40420-40490 | 62 | `chapters/volcengine/ark/13.11.3 查询异步任务用量.md` |
| 13.11.4 | 创建用量明细导出任务 | 1032-1033 | 40491-40545 | 33 | `chapters/volcengine/ark/13.11.4 创建用量明细导出任务.md` |
| 13.11.5 | 查询用量明细导出任务状态 | 1034-1036 | 40546-40648 | 71 | `chapters/volcengine/ark/13.11.5 查询用量明细导出任务状态.md` |
| 13.11.6 | 查询模型推理限额 | 1037 | 40649-40676 | 22 | `chapters/volcengine/ark/13.11.6 查询模型推理限额.md` |
| 13.11.7 | 开启模型推理限额 | 1038 | 40677-40701 | 16 | `chapters/volcengine/ark/13.11.7 开启模型推理限额.md` |
| 13.11.8 | 关闭模型推理限额 | 1039 | 40702-40722 | 12 | `chapters/volcengine/ark/13.11.8 关闭模型推理限额.md` |
| 13.12.1 | 创建方舟官方模型产物查询请求 | 1040 | 40724-40742 | 14 | `chapters/volcengine/ark/13.12.1 创建方舟官方模型产物查询请求.md` |
| 13.12.2 | 获取安全审计日志 | 1041-1043 | 40743-40862 | 85 | `chapters/volcengine/ark/13.12.2 获取安全审计日志.md` |
| 13.12.3 | 获取方舟官方产物确认结果 | 1044 | 40863-40892 | 24 | `chapters/volcengine/ark/13.12.3 获取方舟官方产物确认结果.md` |
| 13.13.1 | 上报视频生成模型效果问题 | 1045-1047 | 40894-41017 | 86 | `chapters/volcengine/ark/13.13.1 上报视频生成模型效果问题.md` |
| 13.13.2 | 查询视频生成模型效果问题结果 | 1048-1051 | 41018-41106 | 69 | `chapters/volcengine/ark/13.13.2 查询视频生成模型效果问题结果.md` |
| 13.13.3 | 上报大语言模型效果问题 | 1052-1054 | 41107-41215 | 82 | `chapters/volcengine/ark/13.13.3 上报大语言模型效果问题.md` |
| 13.13.4 | 查询大语言模型效果问题结果 | 1055-1057 | 41216-41331 | 97 | `chapters/volcengine/ark/13.13.4 查询大语言模型效果问题结果.md` |
| 14.1 | 兼容 OpenAI SDK | 1058-1061 | 41333-41449 | 103 | `chapters/volcengine/ark/14.1 兼容 OpenAI SDK.md` |
| 14.2 | 向后兼容性 | 1062 | 41450-41495 | 25 | `chapters/volcengine/ark/14.2 向后兼容性.md` |
| 14.3 | 错误码 - 第1部分 | 1062-1084 | 41496-43460 | 1915 | `chapters/volcengine/ark/14.3 错误码 - 第1部分.md` |
| 14.3 | 错误码 - 第2部分·错误码 | 1085-1092 | 43461-44059 | 569 | `chapters/volcengine/ark/14.3 错误码 - 第2部分·错误码.md` |
| 14.4 | SDK 常见使用示例 | 1093-1108 | 44060-44648 | 521 | `chapters/volcengine/ark/14.4 SDK 常见使用示例.md` |
