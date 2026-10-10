# 方舟 API 区章节表（ark）

来源：《火山方舟 API 参考》（1065 页）。192 个章节文件，接口级切分：一个接口/任务一个文件；超过 1500 行的按语义块自动再拆为`… - 第N部分`（5 个章节被拆分）。

「页码」是原 PDF 页码范围；「行范围」是中间 MD（`doc/<源文档>.md`）的 1 起始行号，可据此回查原文。章节文件本身已去掉页眉页脚，回查 PDF 时用这两列。文件名即章节标题，日常定位直接 Glob 文件名即可，用不到这两列。

**这张表用来 grep，不要整读。**

| 编号 | 标题 | 页码 | 行范围(源文件) | 行数 | 文件 |
|------|------|------|---------------|------|------|
| 1.1 | 获取 API Key 并配置 | 1 | 269-304 | 20 | `chapters/volcengine/ark/1.1 获取 API Key 并配置.md` |
| 1.2 | 安装及升级 SDK | 2-7 | 305-463 | 122 | `chapters/volcengine/ark/1.2 安装及升级 SDK.md` |
| 1.3 | Base URL及鉴权 | 8-10 | 464-559 | 68 | `chapters/volcengine/ark/1.3 Base URL及鉴权.md` |
| 2.1 | 对话(Chat) API | 11-37 | 561-1802 | 916 | `chapters/volcengine/ark/2.1 对话(Chat) API.md` |
| 3.1 | 创建 Response - 第1部分 | 38-76 | 1803-3484 | 1441 | `chapters/volcengine/ark/3.1 创建 Response - 第1部分.md` |
| 3.1 | 创建 Response - 第2部分·响应参数 | 77-108 | 3485-4839 | 1209 | `chapters/volcengine/ark/3.1 创建 Response - 第2部分·响应参数.md` |
| 3.2 | 查询 Response 详情 | 109-135 | 4840-5974 | 1062 | `chapters/volcengine/ark/3.2 查询 Response 详情.md` |
| 3.3 | 查询 Response 输入项列表 | 136-157 | 5975-6873 | 831 | `chapters/volcengine/ark/3.3 查询 Response 输入项列表.md` |
| 3.4 | 删除 Response | 158 | 6874-6897 | 19 | `chapters/volcengine/ark/3.4 删除 Response.md` |
| 3.5.1 | Response 生命周期 - 第1部分 | 159-196 | 6898-8547 | 1474 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第1部分.md` |
| 3.5.1 | Response 生命周期 - 第2部分 | 197-234 | 8548-10211 | 1489 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第2部分.md` |
| 3.5.1 | Response 生命周期 - 第3部分 | 235-272 | 10212-11862 | 1483 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第3部分.md` |
| 3.5.1 | Response 生命周期 - 第4部分 | 273-319 | 11863-13880 | 1778 | `chapters/volcengine/ark/3.5.1 Response 生命周期 - 第4部分.md` |
| 3.5.2 | Output Item 与文本回答 - 第1部分 | 320-355 | 13881-15455 | 1447 | `chapters/volcengine/ark/3.5.2 Output Item 与文本回答 - 第1部分.md` |
| 3.5.2 | Output Item 与文本回答 - 第2部分 | 356-371 | 15456-16102 | 615 | `chapters/volcengine/ark/3.5.2 Output Item 与文本回答 - 第2部分.md` |
| 3.5.3 | 工具调用事件 | 372-398 | 16103-17183 | 1024 | `chapters/volcengine/ark/3.5.3 工具调用事件.md` |
| 3.5.4 | 语音转写与错误事件 | 399-403 | 17184-17354 | 161 | `chapters/volcengine/ark/3.5.4 语音转写与错误事件.md` |
| 4.1 | 创建 Message | 404-419 | 17356-17997 | 564 | `chapters/volcengine/ark/4.1 创建 Message.md` |
| 4.2 | 统计 Messages 请求 token 数 | 420-427 | 17998-18331 | 279 | `chapters/volcengine/ark/4.2 统计 Messages 请求 token 数.md` |
| 5.1 | 上传文件 | 428-433 | 18333-18547 | 159 | `chapters/volcengine/ark/5.1 上传文件.md` |
| 5.2 | 查询文件详情 | 434-435 | 18548-18615 | 60 | `chapters/volcengine/ark/5.2 查询文件详情.md` |
| 5.3 | 查询文件列表 | 436-439 | 18616-18746 | 109 | `chapters/volcengine/ark/5.3 查询文件列表.md` |
| 5.4 | 删除文件 | 440 | 18747-18769 | 19 | `chapters/volcengine/ark/5.4 删除文件.md` |
| 5.5 | The file object | 441-443 | 18770-18841 | 57 | `chapters/volcengine/ark/5.5 The file object.md` |
| 6.1 | 创建视频生成任务 | 444-460 | 18843-19715 | 613 | `chapters/volcengine/ark/6.1 创建视频生成任务.md` |
| 6.2 | 查询视频生成任务 | 461-464 | 19716-19856 | 105 | `chapters/volcengine/ark/6.2 查询视频生成任务.md` |
| 6.3 | 查询视频生成任务列表 | 465-469 | 19857-20059 | 156 | `chapters/volcengine/ark/6.3 查询视频生成任务列表.md` |
| 6.4 | 取消或删除视频生成任务 | 470 | 20060-20101 | 38 | `chapters/volcengine/ark/6.4 取消或删除视频生成任务.md` |
| 7.1 | 图片生成 API | 471-487 | 20103-20856 | 530 | `chapters/volcengine/ark/7.1 图片生成 API.md` |
| 7.2 | 图片生成流式响应事件 | 488-492 | 20857-21033 | 158 | `chapters/volcengine/ark/7.2 图片生成流式响应事件.md` |
| 8.1.1 | 创建 3D 生成任务 API | 493-495 | 21036-21139 | 80 | `chapters/volcengine/ark/8.1.1 创建 3D 生成任务 API.md` |
| 8.1.2 | 查询 3D 生成任务 API | 496-497 | 21140-21209 | 52 | `chapters/volcengine/ark/8.1.2 查询 3D 生成任务 API.md` |
| 8.1.3 | 查询 3D 生成任务列表 | 498-500 | 21210-21323 | 87 | `chapters/volcengine/ark/8.1.3 查询 3D 生成任务列表.md` |
| 8.1.4 | 取消或删除 3D 生成任务 | 501 | 21324-21365 | 38 | `chapters/volcengine/ark/8.1.4 取消或删除 3D 生成任务.md` |
| 8.2.1 | 创建3D生成任务 | 502-506 | 21367-21581 | 148 | `chapters/volcengine/ark/8.2.1 创建3D生成任务.md` |
| 8.2.2 | 查询3D生成任务 | 507-508 | 21582-21647 | 48 | `chapters/volcengine/ark/8.2.2 查询3D生成任务.md` |
| 8.2.3 | 查询3D生成任务列表 | 509-511 | 21648-21755 | 81 | `chapters/volcengine/ark/8.2.3 查询3D生成任务列表.md` |
| 8.2.4 | 取消或删除3D生成任务 | 512 | 21756-21790 | 31 | `chapters/volcengine/ark/8.2.4 取消或删除3D生成任务.md` |
| 8.3.1 | 创建3D生成任务 | 513-516 | 21792-21923 | 95 | `chapters/volcengine/ark/8.3.1 创建3D生成任务.md` |
| 8.3.2 | 查询3D生成任务 | 517-518 | 21924-21989 | 48 | `chapters/volcengine/ark/8.3.2 查询3D生成任务.md` |
| 8.3.3 | 查询3D生成任务列表 | 519-521 | 21990-22097 | 81 | `chapters/volcengine/ark/8.3.3 查询3D生成任务列表.md` |
| 8.3.4 | 取消或删除3D生成任务 | 522 | 22098-22132 | 31 | `chapters/volcengine/ark/8.3.4 取消或删除3D生成任务.md` |
| 9.1 | 多模态向量化 API | 523-527 | 22134-22332 | 147 | `chapters/volcengine/ark/9.1 多模态向量化 API.md` |
| 10.1.1 | 创建智能体 | 528-536 | 22335-22737 | 320 | `chapters/volcengine/ark/10.1.1 创建智能体.md` |
| 10.1.2 | 查询智能体列表 | 537-542 | 22738-22971 | 195 | `chapters/volcengine/ark/10.1.2 查询智能体列表.md` |
| 10.1.3 | 查询智能体详情 | 543-547 | 22972-23169 | 161 | `chapters/volcengine/ark/10.1.3 查询智能体详情.md` |
| 10.1.4 | 更新智能体 | 548-557 | 23170-23628 | 344 | `chapters/volcengine/ark/10.1.4 更新智能体.md` |
| 10.1.5 | 删除智能体 | 558 | 23629-23649 | 14 | `chapters/volcengine/ark/10.1.5 删除智能体.md` |
| 10.1.6 | 查询智能体版本列表 | 559-564 | 23650-23872 | 183 | `chapters/volcengine/ark/10.1.6 查询智能体版本列表.md` |
| 10.2.1 | 创建环境 | 565-569 | 23874-24049 | 144 | `chapters/volcengine/ark/10.2.1 创建环境.md` |
| 10.2.2 | 查询环境列表 | 570-572 | 24050-24153 | 95 | `chapters/volcengine/ark/10.2.2 查询环境列表.md` |
| 10.2.3 | 查询环境详情 | 573-575 | 24154-24240 | 76 | `chapters/volcengine/ark/10.2.3 查询环境详情.md` |
| 10.2.4 | 更新环境 | 576-580 | 24241-24440 | 158 | `chapters/volcengine/ark/10.2.4 更新环境.md` |
| 10.2.5 | 删除环境 | 581 | 24441-24463 | 19 | `chapters/volcengine/ark/10.2.5 删除环境.md` |
| 10.2.6.1 | 长轮询拉取待执行 Work | 582-584 | 24465-24556 | 69 | `chapters/volcengine/ark/10.2.6.1 长轮询拉取待执行 Work.md` |
| 10.2.6.2 | 认领 Work | 585-586 | 24557-24627 | 56 | `chapters/volcengine/ark/10.2.6.2 认领 Work.md` |
| 10.2.6.3 | 续租 Work | 587-588 | 24628-24683 | 41 | `chapters/volcengine/ark/10.2.6.3 续租 Work.md` |
| 10.2.6.4 | 查询 Work 队列状态 | 589 | 24684-24716 | 23 | `chapters/volcengine/ark/10.2.6.4 查询 Work 队列状态.md` |
| 10.2.6.5 | 停止 Work | 590-591 | 24717-24787 | 56 | `chapters/volcengine/ark/10.2.6.5 停止 Work.md` |
| 10.2.6.6 | 查询 Work 列表 | 592-594 | 24788-24880 | 77 | `chapters/volcengine/ark/10.2.6.6 查询 Work 列表.md` |
| 10.2.6.7 | 查询 Work 详情 | 595-596 | 24881-24938 | 46 | `chapters/volcengine/ark/10.2.6.7 查询 Work 详情.md` |
| 10.3.1 | 创建会话 | 597-613 | 24940-25650 | 604 | `chapters/volcengine/ark/10.3.1 创建会话.md` |
| 10.3.2 | 查询会话列表 | 614-626 | 25651-26197 | 487 | `chapters/volcengine/ark/10.3.2 查询会话列表.md` |
| 10.3.3 | 查询会话详情 | 627-638 | 26198-26704 | 452 | `chapters/volcengine/ark/10.3.3 查询会话详情.md` |
| 10.3.4 | 更新会话标题和标签 | 639-650 | 26705-27223 | 458 | `chapters/volcengine/ark/10.3.4 更新会话标题和标签.md` |
| 10.3.5 | 升级会话 | 651-664 | 27224-27805 | 511 | `chapters/volcengine/ark/10.3.5 升级会话.md` |
| 10.3.6 | 删除会话 | 665 | 27806-27832 | 20 | `chapters/volcengine/ark/10.3.6 删除会话.md` |
| 10.3.7.1 | 发送会话事件 | 666-667 | 27834-27880 | 33 | `chapters/volcengine/ark/10.3.7.1 发送会话事件.md` |
| 10.3.7.2 | 查询会话事件列表 | 668-669 | 27881-27945 | 50 | `chapters/volcengine/ark/10.3.7.2 查询会话事件列表.md` |
| 10.3.7.3 | 流式获取会话事件 | 670-671 | 27946-27997 | 32 | `chapters/volcengine/ark/10.3.7.3 流式获取会话事件.md` |
| 10.3.7.4 | 会话事件结构参考 - 第1部分 | 672-716 | 27998-29778 | 1641 | `chapters/volcengine/ark/10.3.7.4 会话事件结构参考 - 第1部分.md` |
| 10.3.8.1 | 添加会话资源 | 717-718 | 29780-29832 | 41 | `chapters/volcengine/ark/10.3.8.1 添加会话资源.md` |
| 10.3.8.2 | 查询会话资源列表 | 719-721 | 29833-29924 | 85 | `chapters/volcengine/ark/10.3.8.2 查询会话资源列表.md` |
| 10.3.8.3 | 查询会话资源 | 722 | 29925-29942 | 13 | `chapters/volcengine/ark/10.3.8.3 查询会话资源.md` |
| 10.3.9.1 | 查询线程列表 | 723-724 | 29944-30011 | 56 | `chapters/volcengine/ark/10.3.9.1 查询线程列表.md` |
| 10.3.9.2 | 查询线程详情 | 725-726 | 30012-30060 | 37 | `chapters/volcengine/ark/10.3.9.2 查询线程详情.md` |
| 10.3.9.3 | 查询线程事件列表 | 727-728 | 30061-30123 | 47 | `chapters/volcengine/ark/10.3.9.3 查询线程事件列表.md` |
| 10.3.9.4 | 流式获取线程事件 | 729-730 | 30124-30172 | 30 | `chapters/volcengine/ark/10.3.9.4 流式获取线程事件.md` |
| 10.4.1 | 创建保管库 | 731-732 | 30174-30208 | 28 | `chapters/volcengine/ark/10.4.1 创建保管库.md` |
| 10.4.2 | 查询保管库列表 | 733-734 | 30209-30263 | 45 | `chapters/volcengine/ark/10.4.2 查询保管库列表.md` |
| 10.4.3 | 查询保管库详情 | 735 | 30264-30290 | 24 | `chapters/volcengine/ark/10.4.3 查询保管库详情.md` |
| 10.4.4 | 更新保管库 | 736-737 | 30291-30332 | 33 | `chapters/volcengine/ark/10.4.4 更新保管库.md` |
| 10.4.5 | 删除保管库 | 738 | 30333-30357 | 21 | `chapters/volcengine/ark/10.4.5 删除保管库.md` |
| 10.4.6.1 | 创建凭证 | 739-747 | 30359-30733 | 290 | `chapters/volcengine/ark/10.4.6.1 创建凭证.md` |
| 10.4.6.2 | 查询凭证列表 | 748-752 | 30734-30917 | 153 | `chapters/volcengine/ark/10.4.6.2 查询凭证列表.md` |
| 10.4.6.3 | 查询凭证详情 | 753-756 | 30918-31073 | 131 | `chapters/volcengine/ark/10.4.6.3 查询凭证详情.md` |
| 10.4.6.4 | 更新凭证 | 757-764 | 31074-31419 | 271 | `chapters/volcengine/ark/10.4.6.4 更新凭证.md` |
| 10.4.6.5 | 删除凭证 | 765 | 31420-31446 | 21 | `chapters/volcengine/ark/10.4.6.5 删除凭证.md` |
| 10.5.1 | 创建记忆库 | 766-767 | 31448-31508 | 52 | `chapters/volcengine/ark/10.5.1 创建记忆库.md` |
| 10.5.2 | 查询记忆库列表 | 768-769 | 31509-31591 | 66 | `chapters/volcengine/ark/10.5.2 查询记忆库列表.md` |
| 10.5.3 | 查询记忆库详情 | 770-771 | 31592-31637 | 37 | `chapters/volcengine/ark/10.5.3 查询记忆库详情.md` |
| 10.5.4 | 更新记忆库 | 772-773 | 31638-31700 | 51 | `chapters/volcengine/ark/10.5.4 更新记忆库.md` |
| 10.5.5 | 删除记忆库 | 774 | 31701-31726 | 17 | `chapters/volcengine/ark/10.5.5 删除记忆库.md` |
| 10.5.6.1 | 创建记忆 | 775-776 | 31728-31793 | 52 | `chapters/volcengine/ark/10.5.6.1 创建记忆.md` |
| 10.5.6.2 | 批量创建记忆 | 777-779 | 31794-31908 | 89 | `chapters/volcengine/ark/10.5.6.2 批量创建记忆.md` |
| 10.5.6.3 | 查询记忆列表 | 780-782 | 31909-32000 | 69 | `chapters/volcengine/ark/10.5.6.3 查询记忆列表.md` |
| 10.5.6.4 | 查询记忆详情 | 783-784 | 32001-32059 | 45 | `chapters/volcengine/ark/10.5.6.4 查询记忆详情.md` |
| 10.5.6.5 | 更新记忆 | 785-786 | 32060-32130 | 52 | `chapters/volcengine/ark/10.5.6.5 更新记忆.md` |
| 10.5.6.6 | 删除记忆 | 787 | 32131-32159 | 18 | `chapters/volcengine/ark/10.5.6.6 删除记忆.md` |
| 10.6.1 | 创建技能 | 788-789 | 32161-32229 | 49 | `chapters/volcengine/ark/10.6.1 创建技能.md` |
| 10.6.2 | 查询技能列表 | 790-791 | 32230-32304 | 61 | `chapters/volcengine/ark/10.6.2 查询技能列表.md` |
| 10.6.3 | 查询技能详情 | 792-793 | 32305-32350 | 36 | `chapters/volcengine/ark/10.6.3 查询技能详情.md` |
| 10.6.4 | 设置技能内容保护 | 794-795 | 32351-32396 | 37 | `chapters/volcengine/ark/10.6.4 设置技能内容保护.md` |
| 10.6.5 | 删除技能 | 796 | 32397-32422 | 18 | `chapters/volcengine/ark/10.6.5 删除技能.md` |
| 10.6.6 | 创建新版本的技能 | 797-798 | 32423-32482 | 41 | `chapters/volcengine/ark/10.6.6 创建新版本的技能.md` |
| 10.6.7 | 查询技能的版本列表 | 799-800 | 32483-32538 | 48 | `chapters/volcengine/ark/10.6.7 查询技能的版本列表.md` |
| 10.6.8 | 查询指定版本的技能 | 801 | 32539-32568 | 26 | `chapters/volcengine/ark/10.6.8 查询指定版本的技能.md` |
| 10.6.9 | 删除指定版本的技能 | 802 | 32569-32590 | 17 | `chapters/volcengine/ark/10.6.9 删除指定版本的技能.md` |
| 10.6.10 | 下载指定版本的技能 | 803 | 32591-32609 | 14 | `chapters/volcengine/ark/10.6.10 下载指定版本的技能.md` |
| 10.6.11 | 扫描 GitHub 技能 | 804-805 | 32610-32662 | 43 | `chapters/volcengine/ark/10.6.11 扫描 GitHub 技能.md` |
| 10.6.12 | 导入 GitHub 技能 | 806-807 | 32663-32738 | 58 | `chapters/volcengine/ark/10.6.12 导入 GitHub 技能.md` |
| 11.1.1 | 创建批量推理任务 | 808-811 | 32741-32821 | 60 | `chapters/volcengine/ark/11.1.1 创建批量推理任务.md` |
| 11.1.2 | 获取批量推理任务列表 | 812-816 | 32822-32995 | 152 | `chapters/volcengine/ark/11.1.2 获取批量推理任务列表.md` |
| 11.1.3 | 获取批量推理任务 | 817-819 | 32996-33113 | 102 | `chapters/volcengine/ark/11.1.3 获取批量推理任务.md` |
| 11.1.4 | 更新批量推理任务 | 820 | 33114-33137 | 17 | `chapters/volcengine/ark/11.1.4 更新批量推理任务.md` |
| 11.1.5 | 删除批量推理任务 | 821 | 33138-33157 | 13 | `chapters/volcengine/ark/11.1.5 删除批量推理任务.md` |
| 11.1.6 | 停止批量推理任务 | 822 | 33158-33180 | 16 | `chapters/volcengine/ark/11.1.6 停止批量推理任务.md` |
| 11.1.7 | 重启批量推理任务 | 823 | 33181-33201 | 13 | `chapters/volcengine/ark/11.1.7 重启批量推理任务.md` |
| 11.2 | 批量(Chat) API | 824-838 | 33202-33642 | 339 | `chapters/volcengine/ark/11.2 批量(Chat) API.md` |
| 12.1 | 分词 API | 839-840 | 33644-33690 | 39 | `chapters/volcengine/ark/12.1 分词 API.md` |
| 13.1.1 | 获取临时 API Key | 841 | 33693-33727 | 26 | `chapters/volcengine/ark/13.1.1 获取临时 API Key.md` |
| 13.2.1 | 创建个人版套餐 | 842-843 | 33729-33787 | 34 | `chapters/volcengine/ark/13.2.1 创建个人版套餐.md` |
| 13.2.2 | 续费个人版套餐 | 844-845 | 33788-33833 | 27 | `chapters/volcengine/ark/13.2.2 续费个人版套餐.md` |
| 13.2.3 | 查询个人版套餐 | 846 | 33834-33861 | 21 | `chapters/volcengine/ark/13.2.3 查询个人版套餐.md` |
| 13.2.4.1 | 查询 Agent Plan 支持的模型列表 | 847 | 33863-33882 | 14 | `chapters/volcengine/ark/13.2.4.1 查询 Agent Plan 支持的模型列表.md` |
| 13.2.4.2 | 轮换个人版 API Key | 848 | 33883-33909 | 17 | `chapters/volcengine/ark/13.2.4.2 轮换个人版 API Key.md` |
| 13.2.4.3 | 获取套餐 AFP 额度 | 849-850 | 33910-33984 | 66 | `chapters/volcengine/ark/13.2.4.3 获取套餐 AFP 额度.md` |
| 13.2.4.4 | 获取套餐用量详情 | 851-852 | 33985-34033 | 39 | `chapters/volcengine/ark/13.2.4.4 获取套餐用量详情.md` |
| 13.2.5.1 | 查询 Coding Plan 支持的模型列表 | 853 | 34035-34050 | 12 | `chapters/volcengine/ark/13.2.5.1 查询 Coding Plan 支持的模型列表.md` |
| 13.3.1 | 获取基础模型版本列表 | 854-856 | 34052-34139 | 72 | `chapters/volcengine/ark/13.3.1 获取基础模型版本列表.md` |
| 13.3.2 | 获取基础模型版本信息 | 857-864 | 34140-34457 | 273 | `chapters/volcengine/ark/13.3.2 获取基础模型版本信息.md` |
| 13.3.3 | 获取基础模型列表 | 865-869 | 34458-34702 | 182 | `chapters/volcengine/ark/13.3.3 获取基础模型列表.md` |
| 13.3.4 | 获取基础模型信息 | 870-872 | 34703-34827 | 93 | `chapters/volcengine/ark/13.3.4 获取基础模型信息.md` |
| 13.4.1 | 批量开通基础模型 | 873 | 34829-34843 | 11 | `chapters/volcengine/ark/13.4.1 批量开通基础模型.md` |
| 13.4.2 | 启用自动开通新模型 | 874 | 34844-34855 | 7 | `chapters/volcengine/ark/13.4.2 启用自动开通新模型.md` |
| 13.4.3 | 关闭自动开通新模型 | 875 | 34856-34867 | 7 | `chapters/volcengine/ark/13.4.3 关闭自动开通新模型.md` |
| 13.4.4 | 查询模型开通详情 | 876-879 | 34868-35010 | 131 | `chapters/volcengine/ark/13.4.4 查询模型开通详情.md` |
| 13.4.5 | 查询模型开通列表 | 880-884 | 35011-35188 | 163 | `chapters/volcengine/ark/13.4.5 查询模型开通列表.md` |
| 13.5.1 | 批量开通资源 | 885 | 35190-35208 | 14 | `chapters/volcengine/ark/13.5.1 批量开通资源.md` |
| 13.5.2 | 查询资源开通列表 | 886-888 | 35209-35310 | 92 | `chapters/volcengine/ark/13.5.2 查询资源开通列表.md` |
| 13.6.1 | 查询模型限流 | 889-891 | 35312-35411 | 91 | `chapters/volcengine/ark/13.6.1 查询模型限流.md` |
| 13.7.1 | 删除定制模型 | 892 | 35413-35438 | 17 | `chapters/volcengine/ark/13.7.1 删除定制模型.md` |
| 13.7.2 | 获取定制模型信息 | 893-895 | 35439-35547 | 97 | `chapters/volcengine/ark/13.7.2 获取定制模型信息.md` |
| 13.7.3 | 更新定制模型 | 896 | 35548-35580 | 22 | `chapters/volcengine/ark/13.7.3 更新定制模型.md` |
| 13.7.4 | 获取定制模型列表 | 897-899 | 35581-35699 | 102 | `chapters/volcengine/ark/13.7.4 获取定制模型列表.md` |
| 13.8.1 | 创建模型调优任务 | 900-907 | 35701-36019 | 281 | `chapters/volcengine/ark/13.8.1 创建模型调优任务.md` |
| 13.8.2 | 删除模型调优任务 | 908 | 36020-36036 | 10 | `chapters/volcengine/ark/13.8.2 删除模型调优任务.md` |
| 13.8.3 | 获取模型调优任务信息 | 909-919 | 36037-36490 | 411 | `chapters/volcengine/ark/13.8.3 获取模型调优任务信息.md` |
| 13.8.4 | 查询精调效果指标详细数据 | 920-921 | 36491-36536 | 33 | `chapters/volcengine/ark/13.8.4 查询精调效果指标详细数据.md` |
| 13.8.5 | 查询精调效果指标 | 922 | 36537-36555 | 10 | `chapters/volcengine/ark/13.8.5 查询精调效果指标.md` |
| 13.8.6 | 获取模型调优任务列表 | 923-929 | 36556-36826 | 246 | `chapters/volcengine/ark/13.8.6 获取模型调优任务列表.md` |
| 13.8.7 | 重试模型调优任务 | 930 | 36827-36843 | 9 | `chapters/volcengine/ark/13.8.7 重试模型调优任务.md` |
| 13.8.8 | 停止模型调优任务 | 931 | 36844-36860 | 10 | `chapters/volcengine/ark/13.8.8 停止模型调优任务.md` |
| 13.8.9 | 更新模型调优任务 | 932 | 36861-36884 | 14 | `chapters/volcengine/ark/13.8.9 更新模型调优任务.md` |
| 13.9.1 | 开启推理接入点 | 933 | 36886-36906 | 13 | `chapters/volcengine/ark/13.9.1 开启推理接入点.md` |
| 13.9.2 | 停止推理接入点 | 934 | 36907-36927 | 11 | `chapters/volcengine/ark/13.9.2 停止推理接入点.md` |
| 13.9.3 | 获取推理接入点列表 | 935-939 | 36928-37139 | 170 | `chapters/volcengine/ark/13.9.3 获取推理接入点列表.md` |
| 13.9.4 | 获取推理接入点 | 940-942 | 37140-37241 | 88 | `chapters/volcengine/ark/13.9.4 获取推理接入点.md` |
| 13.9.5 | 删除推理接入点 | 943 | 37242-37261 | 12 | `chapters/volcengine/ark/13.9.5 删除推理接入点.md` |
| 13.9.6 | 更新推理接入点 | 944-948 | 37262-37446 | 160 | `chapters/volcengine/ark/13.9.6 更新推理接入点.md` |
| 13.9.7 | 创建推理接入点 | 949-954 | 37447-37674 | 193 | `chapters/volcengine/ark/13.9.7 创建推理接入点.md` |
| 13.9.8 | 获取接入点推理应用层加密证书 | 955-956 | 37675-37710 | 23 | `chapters/volcengine/ark/13.9.8 获取接入点推理应用层加密证书.md` |
| 13.9.9 | 创建推理接入点滚动升级任务 | 957-958 | 37711-37758 | 41 | `chapters/volcengine/ark/13.9.9 创建推理接入点滚动升级任务.md` |
| 13.9.10 | 查询推理接入点滚动升级详情 | 959-962 | 37759-37885 | 116 | `chapters/volcengine/ark/13.9.10 查询推理接入点滚动升级详情.md` |
| 13.9.11 | 回滚推理接入点滚动升级 | 963 | 37886-37903 | 13 | `chapters/volcengine/ark/13.9.11 回滚推理接入点滚动升级.md` |
| 13.9.12 | 取消推理接入点滚动升级 | 964 | 37904-37921 | 13 | `chapters/volcengine/ark/13.9.12 取消推理接入点滚动升级.md` |
| 13.10.1 | 创建评测任务 | 965-968 | 37923-38088 | 133 | `chapters/volcengine/ark/13.10.1 创建评测任务.md` |
| 13.10.2 | 删除评测任务 | 969 | 38089-38110 | 13 | `chapters/volcengine/ark/13.10.2 删除评测任务.md` |
| 13.10.3 | 获取评测任务 | 970-972 | 38111-38192 | 66 | `chapters/volcengine/ark/13.10.3 获取评测任务.md` |
| 13.10.4 | 获取评测任务结果 | 973-975 | 38193-38295 | 87 | `chapters/volcengine/ark/13.10.4 获取评测任务结果.md` |
| 13.10.5 | 获取评测任务列表 | 976-979 | 38296-38442 | 129 | `chapters/volcengine/ark/13.10.5 获取评测任务列表.md` |
| 13.10.6 | 获取评测任务结果列表 | 980-983 | 38443-38584 | 120 | `chapters/volcengine/ark/13.10.6 获取评测任务结果列表.md` |
| 13.10.7 | 停止评测任务 | 984 | 38585-38606 | 13 | `chapters/volcengine/ark/13.10.7 停止评测任务.md` |
| 13.10.8 | 更新评测任务 | 985 | 38607-38632 | 18 | `chapters/volcengine/ark/13.10.8 更新评测任务.md` |
| 13.11.1 | 查询推理用量 | 986-988 | 38634-38761 | 75 | `chapters/volcengine/ark/13.11.1 查询推理用量.md` |
| 13.11.2 | 创建用量明细导出任务 | 989-990 | 38762-38814 | 33 | `chapters/volcengine/ark/13.11.2 创建用量明细导出任务.md` |
| 13.11.3 | 查询用量明细导出任务状态 | 991-993 | 38815-38917 | 71 | `chapters/volcengine/ark/13.11.3 查询用量明细导出任务状态.md` |
| 13.11.4 | 查询模型推理限额 | 994 | 38918-38945 | 22 | `chapters/volcengine/ark/13.11.4 查询模型推理限额.md` |
| 13.11.5 | 开启模型推理限额 | 995 | 38946-38970 | 16 | `chapters/volcengine/ark/13.11.5 开启模型推理限额.md` |
| 13.11.6 | 关闭模型推理限额 | 996 | 38971-38991 | 12 | `chapters/volcengine/ark/13.11.6 关闭模型推理限额.md` |
| 13.12.1 | 创建方舟官方模型产物查询请求 | 997 | 38993-39011 | 14 | `chapters/volcengine/ark/13.12.1 创建方舟官方模型产物查询请求.md` |
| 13.12.2 | 获取安全审计日志 | 998-1000 | 39012-39131 | 85 | `chapters/volcengine/ark/13.12.2 获取安全审计日志.md` |
| 13.12.3 | 获取方舟官方产物确认结果 | 1001 | 39132-39161 | 24 | `chapters/volcengine/ark/13.12.3 获取方舟官方产物确认结果.md` |
| 13.13.1 | 上报视频生成模型效果问题 | 1002-1004 | 39163-39286 | 86 | `chapters/volcengine/ark/13.13.1 上报视频生成模型效果问题.md` |
| 13.13.2 | 查询视频生成模型效果问题结果 | 1005-1008 | 39287-39375 | 69 | `chapters/volcengine/ark/13.13.2 查询视频生成模型效果问题结果.md` |
| 13.13.3 | 上报大语言模型效果问题 | 1009-1011 | 39376-39484 | 82 | `chapters/volcengine/ark/13.13.3 上报大语言模型效果问题.md` |
| 13.13.4 | 查询大语言模型效果问题结果 | 1012-1014 | 39485-39600 | 97 | `chapters/volcengine/ark/13.13.4 查询大语言模型效果问题结果.md` |
| 14.1 | 兼容 OpenAI SDK | 1015-1018 | 39602-39718 | 103 | `chapters/volcengine/ark/14.1 兼容 OpenAI SDK.md` |
| 14.2 | 向后兼容性 | 1019 | 39719-39764 | 25 | `chapters/volcengine/ark/14.2 向后兼容性.md` |
| 14.3 | 错误码 - 第1部分 | 1019-1041 | 39765-41729 | 1915 | `chapters/volcengine/ark/14.3 错误码 - 第1部分.md` |
| 14.3 | 错误码 - 第2部分·错误码 | 1042-1049 | 41730-42328 | 569 | `chapters/volcengine/ark/14.3 错误码 - 第2部分·错误码.md` |
| 14.4 | SDK 常见使用示例 | 1050-1065 | 42329-42917 | 521 | `chapters/volcengine/ark/14.4 SDK 常见使用示例.md` |
