# 方舟 API 区章节表（ark）

来源：《火山方舟 API 参考》（1343 页）。230 个章节文件，接口级切分：一个接口/任务一个文件；超过 1500 行的按语义块自动再拆为`… - 第N部分`（5 个章节被拆分）。

「页码」是原 PDF 页码范围；「行范围」是中间 MD（`doc/<源文档>.md`）的 1 起始行号，可据此回查原文。章节文件本身已去掉页眉页脚，回查 PDF 时用这两列。文件名即章节标题，日常定位直接 Glob 文件名即可，用不到这两列。

**这张表用来 grep，不要整读。**

| 编号 | 标题 | 页码 | 行范围(源文件) | 行数 | 文件 |
|------|------|------|---------------|------|------|
| 1.1 | 获取 API Key 并配置 | 1 | 314-349 | 19 | `chapters/volcengine/ark/1.1 获取 API Key 并配置.md` |
| 1.2 | 安装及升级 SDK | 2-7 | 350-508 | 122 | `chapters/volcengine/ark/1.2 安装及升级 SDK.md` |
| 1.3 | Base URL 及鉴权 | 8-10 | 509-604 | 68 | `chapters/volcengine/ark/1.3 Base URL 及鉴权.md` |
| 2.1 | 对话(Chat) API | 11-42 | 606-2084 | 1091 | `chapters/volcengine/ark/2.1 对话(Chat) API.md` |
| 2.2.1 | 创建 Response - 第1部分 | 43-81 | 2085-3789 | 1439 | `chapters/volcengine/ark/2.2.1 创建 Response - 第1部分.md` |
| 2.2.1 | 创建 Response - 第2部分·响应参数 | 82-114 | 3790-5193 | 1239 | `chapters/volcengine/ark/2.2.1 创建 Response - 第2部分·响应参数.md` |
| 2.2.2 | 查询 Response 详情 | 115-141 | 5194-6331 | 1064 | `chapters/volcengine/ark/2.2.2 查询 Response 详情.md` |
| 2.2.3 | 查询 Response 输入项列表 | 142-163 | 6332-7264 | 847 | `chapters/volcengine/ark/2.2.3 查询 Response 输入项列表.md` |
| 2.2.4 | 删除 Response | 164 | 7265-7288 | 19 | `chapters/volcengine/ark/2.2.4 删除 Response.md` |
| 2.2.5.1 | Response 生命周期 - 第1部分 | 165-203 | 7289-8986 | 1506 | `chapters/volcengine/ark/2.2.5.1 Response 生命周期 - 第1部分.md` |
| 2.2.5.1 | Response 生命周期 - 第2部分 | 204-241 | 8987-10646 | 1475 | `chapters/volcengine/ark/2.2.5.1 Response 生命周期 - 第2部分.md` |
| 2.2.5.1 | Response 生命周期 - 第3部分 | 242-280 | 10647-12342 | 1510 | `chapters/volcengine/ark/2.2.5.1 Response 生命周期 - 第3部分.md` |
| 2.2.5.1 | Response 生命周期 - 第4部分 | 281-330 | 12343-14491 | 1873 | `chapters/volcengine/ark/2.2.5.1 Response 生命周期 - 第4部分.md` |
| 2.2.5.2 | Output Item 与文本回答 - 第1部分 | 331-366 | 14492-16066 | 1447 | `chapters/volcengine/ark/2.2.5.2 Output Item 与文本回答 - 第1部分.md` |
| 2.2.5.2 | Output Item 与文本回答 - 第2部分 | 367-382 | 16067-16713 | 615 | `chapters/volcengine/ark/2.2.5.2 Output Item 与文本回答 - 第2部分.md` |
| 2.2.5.3 | 工具调用事件 | 383-410 | 16714-17796 | 1024 | `chapters/volcengine/ark/2.2.5.3 工具调用事件.md` |
| 2.2.5.4 | 语音转写与错误事件 | 411-415 | 17797-17967 | 161 | `chapters/volcengine/ark/2.2.5.4 语音转写与错误事件.md` |
| 2.3.1 | 创建 Message | 416-432 | 17969-18644 | 584 | `chapters/volcengine/ark/2.3.1 创建 Message.md` |
| 2.3.2 | 统计 Messages 请求 token 数 | 433-441 | 18645-18985 | 279 | `chapters/volcengine/ark/2.3.2 统计 Messages 请求 token 数.md` |
| 3.1 | 创建视频生成任务 | 442-457 | 18987-19732 | 511 | `chapters/volcengine/ark/3.1 创建视频生成任务.md` |
| 3.2 | 查询视频生成任务 | 458-461 | 19733-19890 | 116 | `chapters/volcengine/ark/3.2 查询视频生成任务.md` |
| 3.3 | 查询视频生成任务列表 | 462-466 | 19891-20113 | 168 | `chapters/volcengine/ark/3.3 查询视频生成任务列表.md` |
| 3.4 | 取消或删除视频生成任务 | 467 | 20114-20159 | 42 | `chapters/volcengine/ark/3.4 取消或删除视频生成任务.md` |
| 4.1 | 图片生成 API | 468-487 | 20161-21114 | 661 | `chapters/volcengine/ark/4.1 图片生成 API.md` |
| 4.2 | 图片生成流式响应事件 | 488-491 | 21115-21249 | 124 | `chapters/volcengine/ark/4.2 图片生成流式响应事件.md` |
| 5.1.1 | 创建智能体 | 492-505 | 21252-21879 | 477 | `chapters/volcengine/ark/5.1.1 创建智能体.md` |
| 5.1.2 | 查询智能体列表 | 506-513 | 21880-22212 | 274 | `chapters/volcengine/ark/5.1.2 查询智能体列表.md` |
| 5.1.3 | 查询智能体详情 | 514-520 | 22213-22499 | 232 | `chapters/volcengine/ark/5.1.3 查询智能体详情.md` |
| 5.1.4 | 更新智能体 | 521-535 | 22500-23179 | 499 | `chapters/volcengine/ark/5.1.4 更新智能体.md` |
| 5.1.5 | 查询智能体版本列表 | 536-542 | 23180-23487 | 250 | `chapters/volcengine/ark/5.1.5 查询智能体版本列表.md` |
| 5.1.6 | 归档智能体 | 543-549 | 23488-23777 | 235 | `chapters/volcengine/ark/5.1.6 归档智能体.md` |
| 5.1.7 | 删除智能体 | 550 | 23778-23801 | 16 | `chapters/volcengine/ark/5.1.7 删除智能体.md` |
| 5.2.1 | 创建环境 | 551-557 | 23803-24090 | 215 | `chapters/volcengine/ark/5.2.1 创建环境.md` |
| 5.2.2 | 查询环境列表 | 558-561 | 24091-24240 | 129 | `chapters/volcengine/ark/5.2.2 查询环境列表.md` |
| 5.2.3 | 查询环境详情 | 562-565 | 24241-24366 | 104 | `chapters/volcengine/ark/5.2.3 查询环境详情.md` |
| 5.2.4 | 更新环境 | 566-573 | 24367-24690 | 232 | `chapters/volcengine/ark/5.2.4 更新环境.md` |
| 5.2.5 | 归档环境 | 574-577 | 24691-24817 | 104 | `chapters/volcengine/ark/5.2.5 归档环境.md` |
| 5.2.6 | 删除环境 | 578 | 24818-24842 | 16 | `chapters/volcengine/ark/5.2.6 删除环境.md` |
| 5.2.7.1 | 长轮询拉取待执行 Work | 579-581 | 24844-24950 | 77 | `chapters/volcengine/ark/5.2.7.1 长轮询拉取待执行 Work.md` |
| 5.2.7.2 | 认领 Work | 582-584 | 24951-25038 | 64 | `chapters/volcengine/ark/5.2.7.2 认领 Work.md` |
| 5.2.7.3 | 续租 Work | 585-586 | 25039-25105 | 47 | `chapters/volcengine/ark/5.2.7.3 续租 Work.md` |
| 5.2.7.4 | 查询 Work 队列状态 | 587 | 25106-25138 | 23 | `chapters/volcengine/ark/5.2.7.4 查询 Work 队列状态.md` |
| 5.2.7.5 | 停止 Work | 588-590 | 25139-25243 | 75 | `chapters/volcengine/ark/5.2.7.5 停止 Work.md` |
| 5.2.7.6 | 查询 Work 列表 | 591-593 | 25244-25351 | 86 | `chapters/volcengine/ark/5.2.7.6 查询 Work 列表.md` |
| 5.2.7.7 | 查询 Work 详情 | 594-595 | 25352-25424 | 54 | `chapters/volcengine/ark/5.2.7.7 查询 Work 详情.md` |
| 5.3.1 | 创建会话 | 596-629 | 25426-26902 | 1191 | `chapters/volcengine/ark/5.3.1 创建会话.md` |
| 5.3.2 | 查询会话列表 | 630-651 | 26903-27836 | 796 | `chapters/volcengine/ark/5.3.2 查询会话列表.md` |
| 5.3.3 | 查询会话详情 | 652-672 | 27837-28757 | 789 | `chapters/volcengine/ark/5.3.3 查询会话详情.md` |
| 5.3.4 | 更新会话标题和标签 | 673-693 | 28758-29649 | 758 | `chapters/volcengine/ark/5.3.4 更新会话标题和标签.md` |
| 5.3.5 | 升级会话 | 694-721 | 29650-30869 | 1010 | `chapters/volcengine/ark/5.3.5 升级会话.md` |
| 5.3.6 | 归档会话 | 722-743 | 30870-31801 | 792 | `chapters/volcengine/ark/5.3.6 归档会话.md` |
| 5.3.7 | 删除会话 | 744 | 31802-31828 | 19 | `chapters/volcengine/ark/5.3.7 删除会话.md` |
| 5.3.8.1 | 查询会话任务 | 745-749 | 31830-32017 | 156 | `chapters/volcengine/ark/5.3.8.1 查询会话任务.md` |
| 5.3.8.2 | 查询会话任务列表 | 750-752 | 32018-32131 | 88 | `chapters/volcengine/ark/5.3.8.2 查询会话任务列表.md` |
| 5.3.8.3 | 取消会话任务 | 753-754 | 32132-32190 | 31 | `chapters/volcengine/ark/5.3.8.3 取消会话任务.md` |
| 5.3.9.1 | 发送会话事件 | 755-756 | 32192-32256 | 42 | `chapters/volcengine/ark/5.3.9.1 发送会话事件.md` |
| 5.3.9.2 | 查询会话事件列表 | 757-759 | 32257-32343 | 58 | `chapters/volcengine/ark/5.3.9.2 查询会话事件列表.md` |
| 5.3.9.3 | 流式获取会话事件 | 760-761 | 32344-32419 | 41 | `chapters/volcengine/ark/5.3.9.3 流式获取会话事件.md` |
| 5.3.9.4 | 会话事件结构参考 - 第1部分 | 762-811 | 32420-34395 | 1787 | `chapters/volcengine/ark/5.3.9.4 会话事件结构参考 - 第1部分.md` |
| 5.3.10.1 | 添加会话资源 | 812-813 | 34397-34449 | 41 | `chapters/volcengine/ark/5.3.10.1 添加会话资源.md` |
| 5.3.10.2 | 查询会话资源列表 | 814-816 | 34450-34562 | 100 | `chapters/volcengine/ark/5.3.10.2 查询会话资源列表.md` |
| 5.3.10.3 | 查询会话资源 | 817-818 | 34563-34607 | 36 | `chapters/volcengine/ark/5.3.10.3 查询会话资源.md` |
| 5.3.11.1 | 查询线程列表 | 819-822 | 34609-34738 | 104 | `chapters/volcengine/ark/5.3.11.1 查询线程列表.md` |
| 5.3.11.2 | 查询线程详情 | 823-825 | 34739-34836 | 79 | `chapters/volcengine/ark/5.3.11.2 查询线程详情.md` |
| 5.3.11.3 | 查询线程事件列表 | 826-827 | 34837-34899 | 47 | `chapters/volcengine/ark/5.3.11.3 查询线程事件列表.md` |
| 5.3.11.4 | 流式获取线程事件 | 828-829 | 34900-34948 | 30 | `chapters/volcengine/ark/5.3.11.4 流式获取线程事件.md` |
| 5.4.1 | 创建 Webhook 接入点 | 830-832 | 34950-35049 | 61 | `chapters/volcengine/ark/5.4.1 创建 Webhook 接入点.md` |
| 5.4.2 | 查询 Webhook 接入点列表 | 833-835 | 35050-35147 | 66 | `chapters/volcengine/ark/5.4.2 查询 Webhook 接入点列表.md` |
| 5.4.3 | 查询 Webhook 接入点详情 | 836-837 | 35148-35226 | 51 | `chapters/volcengine/ark/5.4.3 查询 Webhook 接入点详情.md` |
| 5.4.4 | 更新 Webhook 接入点 | 838-840 | 35227-35326 | 59 | `chapters/volcengine/ark/5.4.4 更新 Webhook 接入点.md` |
| 5.4.5 | 启用 Webhook 接入点 | 841-842 | 35327-35407 | 51 | `chapters/volcengine/ark/5.4.5 启用 Webhook 接入点.md` |
| 5.4.6 | 删除 Webhook 接入点 | 843 | 35408-35427 | 15 | `chapters/volcengine/ark/5.4.6 删除 Webhook 接入点.md` |
| 5.4.7 | 停用 Webhook 接入点 | 844-845 | 35428-35509 | 51 | `chapters/volcengine/ark/5.4.7 停用 Webhook 接入点.md` |
| 5.4.8 | 重置 Webhook 签名密钥 | 846 | 35510-35533 | 16 | `chapters/volcengine/ark/5.4.8 重置 Webhook 签名密钥.md` |
| 5.4.9 | 发送 Webhook 测试事件 | 847 | 35534-35566 | 26 | `chapters/volcengine/ark/5.4.9 发送 Webhook 测试事件.md` |
| 5.4.10 | 查询 Webhook 事件详情 | 848-849 | 35567-35626 | 46 | `chapters/volcengine/ark/5.4.10 查询 Webhook 事件详情.md` |
| 5.4.11 | 查询 Webhook 事件列表 | 850-852 | 35627-35714 | 64 | `chapters/volcengine/ark/5.4.11 查询 Webhook 事件列表.md` |
| 5.4.12 | Webhook 事件结构参考 | 853-867 | 35715-36284 | 519 | `chapters/volcengine/ark/5.4.12 Webhook 事件结构参考.md` |
| 5.5.1 | 创建保管库 | 868-869 | 36286-36332 | 36 | `chapters/volcengine/ark/5.5.1 创建保管库.md` |
| 5.5.2 | 查询保管库列表 | 870-871 | 36333-36410 | 60 | `chapters/volcengine/ark/5.5.2 查询保管库列表.md` |
| 5.5.3 | 查询保管库详情 | 872 | 36411-36443 | 28 | `chapters/volcengine/ark/5.5.3 查询保管库详情.md` |
| 5.5.4 | 更新保管库 | 873-874 | 36444-36491 | 37 | `chapters/volcengine/ark/5.5.4 更新保管库.md` |
| 5.5.5 | 删除保管库 | 875 | 36492-36516 | 21 | `chapters/volcengine/ark/5.5.5 删除保管库.md` |
| 5.5.6.1 | 创建凭证 | 876-885 | 36518-36987 | 364 | `chapters/volcengine/ark/5.5.6.1 创建凭证.md` |
| 5.5.6.2 | 查询凭证列表 | 886-890 | 36988-37211 | 185 | `chapters/volcengine/ark/5.5.6.2 查询凭证列表.md` |
| 5.5.6.3 | 查询凭证详情 | 891-895 | 37212-37409 | 163 | `chapters/volcengine/ark/5.5.6.3 查询凭证详情.md` |
| 5.5.6.4 | 更新凭证 | 896-905 | 37410-37853 | 340 | `chapters/volcengine/ark/5.5.6.4 更新凭证.md` |
| 5.5.6.5 | 删除凭证 | 906 | 37854-37880 | 21 | `chapters/volcengine/ark/5.5.6.5 删除凭证.md` |
| 5.6.1 | 创建记忆库 | 907-909 | 37882-37961 | 61 | `chapters/volcengine/ark/5.6.1 创建记忆库.md` |
| 5.6.2 | 查询记忆库列表 | 910-912 | 37962-38064 | 80 | `chapters/volcengine/ark/5.6.2 查询记忆库列表.md` |
| 5.6.3 | 查询记忆库详情 | 913-914 | 38065-38126 | 47 | `chapters/volcengine/ark/5.6.3 查询记忆库详情.md` |
| 5.6.4 | 更新记忆库 | 915-917 | 38127-38207 | 61 | `chapters/volcengine/ark/5.6.4 更新记忆库.md` |
| 5.6.5 | 删除记忆库 | 918 | 38208-38233 | 17 | `chapters/volcengine/ark/5.6.5 删除记忆库.md` |
| 5.6.6.1 | 创建记忆 | 919-920 | 38235-38299 | 51 | `chapters/volcengine/ark/5.6.6.1 创建记忆.md` |
| 5.6.6.2 | 批量创建记忆 | 921-923 | 38300-38417 | 90 | `chapters/volcengine/ark/5.6.6.2 批量创建记忆.md` |
| 5.6.6.3 | 查询记忆列表 | 924-926 | 38418-38511 | 70 | `chapters/volcengine/ark/5.6.6.3 查询记忆列表.md` |
| 5.6.6.4 | 查询记忆详情 | 927-928 | 38512-38570 | 45 | `chapters/volcengine/ark/5.6.6.4 查询记忆详情.md` |
| 5.6.6.5 | 更新记忆 | 929-930 | 38571-38643 | 51 | `chapters/volcengine/ark/5.6.6.5 更新记忆.md` |
| 5.6.6.6 | 删除记忆 | 931 | 38644-38672 | 18 | `chapters/volcengine/ark/5.6.6.6 删除记忆.md` |
| 5.7.1 | 创建 Dream | 932-935 | 38674-38798 | 108 | `chapters/volcengine/ark/5.7.1 创建 Dream.md` |
| 5.7.2 | 查询 Dream 列表 | 936-939 | 38799-38936 | 119 | `chapters/volcengine/ark/5.7.2 查询 Dream 列表.md` |
| 5.7.3 | 查询 Dream | 940-942 | 38937-39032 | 83 | `chapters/volcengine/ark/5.7.3 查询 Dream.md` |
| 5.7.4 | 取消 Dream | 943-945 | 39033-39131 | 84 | `chapters/volcengine/ark/5.7.4 取消 Dream.md` |
| 5.8.1 | 创建技能 | 946-947 | 39133-39201 | 49 | `chapters/volcengine/ark/5.8.1 创建技能.md` |
| 5.8.2 | 查询技能列表 | 948-949 | 39202-39276 | 61 | `chapters/volcengine/ark/5.8.2 查询技能列表.md` |
| 5.8.3 | 查询技能详情 | 950-951 | 39277-39322 | 36 | `chapters/volcengine/ark/5.8.3 查询技能详情.md` |
| 5.8.4 | 设置技能内容保护 | 952-953 | 39323-39368 | 37 | `chapters/volcengine/ark/5.8.4 设置技能内容保护.md` |
| 5.8.5 | 删除技能 | 954 | 39369-39394 | 18 | `chapters/volcengine/ark/5.8.5 删除技能.md` |
| 5.8.6 | 创建新版本的技能 | 955-956 | 39395-39454 | 41 | `chapters/volcengine/ark/5.8.6 创建新版本的技能.md` |
| 5.8.7 | 查询技能的版本列表 | 957-958 | 39455-39510 | 48 | `chapters/volcengine/ark/5.8.7 查询技能的版本列表.md` |
| 5.8.8 | 查询指定版本的技能 | 959 | 39511-39540 | 26 | `chapters/volcengine/ark/5.8.8 查询指定版本的技能.md` |
| 5.8.9 | 删除指定版本的技能 | 960 | 39541-39562 | 17 | `chapters/volcengine/ark/5.8.9 删除指定版本的技能.md` |
| 5.8.10 | 下载指定版本的技能 | 961 | 39563-39581 | 14 | `chapters/volcengine/ark/5.8.10 下载指定版本的技能.md` |
| 5.8.11 | 扫描 GitHub 技能 | 962-963 | 39582-39634 | 43 | `chapters/volcengine/ark/5.8.11 扫描 GitHub 技能.md` |
| 5.8.12 | 导入 GitHub 技能 | 964-965 | 39635-39710 | 58 | `chapters/volcengine/ark/5.8.12 导入 GitHub 技能.md` |
| 5.9.1 | 创建 Deployment | 966-971 | 39712-39950 | 197 | `chapters/volcengine/ark/5.9.1 创建 Deployment.md` |
| 5.9.2 | 更新 Deployment | 972-977 | 39951-40193 | 201 | `chapters/volcengine/ark/5.9.2 更新 Deployment.md` |
| 5.9.3 | 查询 Deployment 详情 | 978-981 | 40194-40332 | 116 | `chapters/volcengine/ark/5.9.3 查询 Deployment 详情.md` |
| 5.9.4 | 查询 Deployment 列表 | 982-986 | 40333-40512 | 152 | `chapters/volcengine/ark/5.9.4 查询 Deployment 列表.md` |
| 5.9.5 | 恢复 Deployment | 987-990 | 40513-40653 | 116 | `chapters/volcengine/ark/5.9.5 恢复 Deployment.md` |
| 5.9.6 | 暂停 Deployment | 991-994 | 40654-40793 | 117 | `chapters/volcengine/ark/5.9.6 暂停 Deployment.md` |
| 5.9.7 | 归档 Deployment | 995-998 | 40794-40933 | 116 | `chapters/volcengine/ark/5.9.7 归档 Deployment.md` |
| 5.9.8 | 立即运行 Deployment | 999-1000 | 40934-40990 | 47 | `chapters/volcengine/ark/5.9.8 立即运行 Deployment.md` |
| 5.9.9 | 查询 Deployment Run 列表 | 1001-1003 | 40991-41079 | 71 | `chapters/volcengine/ark/5.9.9 查询 Deployment Run 列表.md` |
| 5.9.10 | 查询 Deployment Run 详情 | 1004-1005 | 41080-41136 | 46 | `chapters/volcengine/ark/5.9.10 查询 Deployment Run 详情.md` |
| 6.1 | 上传文件 | 1006-1011 | 41138-41363 | 165 | `chapters/volcengine/ark/6.1 上传文件.md` |
| 6.2 | 查询文件详情 | 1012-1014 | 41364-41447 | 67 | `chapters/volcengine/ark/6.2 查询文件详情.md` |
| 6.3 | 查询文件列表 | 1015-1018 | 41448-41592 | 116 | `chapters/volcengine/ark/6.3 查询文件列表.md` |
| 6.4 | 删除文件 | 1019 | 41593-41615 | 19 | `chapters/volcengine/ark/6.4 删除文件.md` |
| 6.5 | The file object | 1020-1022 | 41616-41687 | 57 | `chapters/volcengine/ark/6.5 The file object.md` |
| 7.1 | Models API | 1023-1026 | 41689-41822 | 123 | `chapters/volcengine/ark/7.1 Models API.md` |
| 8.1 | System One API（beta） | 1027-1034 | 41824-42096 | 240 | `chapters/volcengine/ark/8.1 System One API（beta）.md` |
| 9.1.1 | 创建 3D 生成任务 API | 1035-1037 | 42099-42203 | 79 | `chapters/volcengine/ark/9.1.1 创建 3D 生成任务 API.md` |
| 9.1.2 | 查询 3D 生成任务 API | 1038-1039 | 42204-42273 | 52 | `chapters/volcengine/ark/9.1.2 查询 3D 生成任务 API.md` |
| 9.1.3 | 查询 3D 生成任务列表 | 1040-1042 | 42274-42387 | 87 | `chapters/volcengine/ark/9.1.3 查询 3D 生成任务列表.md` |
| 9.1.4 | 取消或删除 3D 生成任务 | 1043 | 42388-42429 | 38 | `chapters/volcengine/ark/9.1.4 取消或删除 3D 生成任务.md` |
| 9.2.1 | 创建 3D 生成任务 | 1044-1048 | 42431-42645 | 148 | `chapters/volcengine/ark/9.2.1 创建 3D 生成任务.md` |
| 9.2.2 | 查询 3D 生成任务 | 1049-1050 | 42646-42711 | 48 | `chapters/volcengine/ark/9.2.2 查询 3D 生成任务.md` |
| 9.2.3 | 查询 3D 生成任务列表 | 1051-1053 | 42712-42819 | 81 | `chapters/volcengine/ark/9.2.3 查询 3D 生成任务列表.md` |
| 9.2.4 | 取消或删除 3D 生成任务 | 1054 | 42820-42854 | 31 | `chapters/volcengine/ark/9.2.4 取消或删除 3D 生成任务.md` |
| 9.3.1 | 创建 3D 生成任务 | 1055-1058 | 42856-42987 | 95 | `chapters/volcengine/ark/9.3.1 创建 3D 生成任务.md` |
| 9.3.2 | 查询 3D 生成任务 | 1059-1060 | 42988-43053 | 48 | `chapters/volcengine/ark/9.3.2 查询 3D 生成任务.md` |
| 9.3.3 | 查询 3D 生成任务列表 | 1061-1063 | 43054-43161 | 81 | `chapters/volcengine/ark/9.3.3 查询 3D 生成任务列表.md` |
| 9.3.4 | 取消或删除 3D 生成任务 | 1064 | 43162-43196 | 31 | `chapters/volcengine/ark/9.3.4 取消或删除 3D 生成任务.md` |
| 10.1 | 多模态向量化 API | 1065-1069 | 43198-43396 | 147 | `chapters/volcengine/ark/10.1 多模态向量化 API.md` |
| 11.1 | 分词 API | 1070-1071 | 43398-43444 | 39 | `chapters/volcengine/ark/11.1 分词 API.md` |
| 12.1.1 | 获取临时 API Key | 1072 | 43447-43481 | 26 | `chapters/volcengine/ark/12.1.1 获取临时 API Key.md` |
| 12.2.1 | 创建个人版套餐 | 1073-1074 | 43483-43541 | 34 | `chapters/volcengine/ark/12.2.1 创建个人版套餐.md` |
| 12.2.2 | 续费个人版套餐 | 1075-1076 | 43542-43587 | 27 | `chapters/volcengine/ark/12.2.2 续费个人版套餐.md` |
| 12.2.3 | 查询个人版套餐 | 1077 | 43588-43615 | 21 | `chapters/volcengine/ark/12.2.3 查询个人版套餐.md` |
| 12.2.4.1 | 查询 Agent Plan 支持的模型列表 | 1078 | 43617-43636 | 14 | `chapters/volcengine/ark/12.2.4.1 查询 Agent Plan 支持的模型列表.md` |
| 12.2.4.2 | 轮换个人版 API Key | 1079 | 43637-43663 | 17 | `chapters/volcengine/ark/12.2.4.2 轮换个人版 API Key.md` |
| 12.2.4.3 | 获取套餐 AFP 额度 | 1080-1081 | 43664-43738 | 66 | `chapters/volcengine/ark/12.2.4.3 获取套餐 AFP 额度.md` |
| 12.2.4.4 | 获取套餐用量详情 | 1082-1083 | 43739-43787 | 39 | `chapters/volcengine/ark/12.2.4.4 获取套餐用量详情.md` |
| 12.2.5.1 | 查询 Coding Plan 支持的模型列表 | 1084 | 43789-43804 | 12 | `chapters/volcengine/ark/12.2.5.1 查询 Coding Plan 支持的模型列表.md` |
| 12.3.1 | 获取基础模型版本列表 | 1085-1087 | 43806-43893 | 72 | `chapters/volcengine/ark/12.3.1 获取基础模型版本列表.md` |
| 12.3.2 | 获取基础模型版本信息 | 1088-1095 | 43894-44211 | 273 | `chapters/volcengine/ark/12.3.2 获取基础模型版本信息.md` |
| 12.3.3 | 获取基础模型列表 | 1096-1100 | 44212-44464 | 186 | `chapters/volcengine/ark/12.3.3 获取基础模型列表.md` |
| 12.3.4 | 获取基础模型信息 | 1101-1103 | 44465-44589 | 93 | `chapters/volcengine/ark/12.3.4 获取基础模型信息.md` |
| 12.4.1 | 批量开通基础模型 | 1104 | 44591-44605 | 11 | `chapters/volcengine/ark/12.4.1 批量开通基础模型.md` |
| 12.4.2 | 启用自动开通新模型 | 1105 | 44606-44617 | 7 | `chapters/volcengine/ark/12.4.2 启用自动开通新模型.md` |
| 12.4.3 | 关闭自动开通新模型 | 1106 | 44618-44629 | 7 | `chapters/volcengine/ark/12.4.3 关闭自动开通新模型.md` |
| 12.4.4 | 查询模型开通详情 | 1107-1110 | 44630-44772 | 131 | `chapters/volcengine/ark/12.4.4 查询模型开通详情.md` |
| 12.4.5 | 查询模型开通列表 | 1111-1115 | 44773-44950 | 163 | `chapters/volcengine/ark/12.4.5 查询模型开通列表.md` |
| 12.4.6 | 查询模型价格 | 1116-1120 | 44951-45152 | 156 | `chapters/volcengine/ark/12.4.6 查询模型价格.md` |
| 12.5.1 | 批量开通资源 | 1121 | 45154-45172 | 14 | `chapters/volcengine/ark/12.5.1 批量开通资源.md` |
| 12.5.2 | 查询资源开通列表 | 1122-1124 | 45173-45274 | 92 | `chapters/volcengine/ark/12.5.2 查询资源开通列表.md` |
| 12.6.1 | 查询模型限流 | 1125-1127 | 45276-45375 | 91 | `chapters/volcengine/ark/12.6.1 查询模型限流.md` |
| 12.7.1 | 删除定制模型 | 1128 | 45377-45402 | 17 | `chapters/volcengine/ark/12.7.1 删除定制模型.md` |
| 12.7.2 | 获取定制模型信息 | 1129-1131 | 45403-45511 | 97 | `chapters/volcengine/ark/12.7.2 获取定制模型信息.md` |
| 12.7.3 | 更新定制模型 | 1132 | 45512-45544 | 22 | `chapters/volcengine/ark/12.7.3 更新定制模型.md` |
| 12.7.4 | 获取定制模型列表 | 1133-1135 | 45545-45663 | 102 | `chapters/volcengine/ark/12.7.4 获取定制模型列表.md` |
| 12.8.1 | 创建模型调优任务 | 1136-1143 | 45665-45983 | 281 | `chapters/volcengine/ark/12.8.1 创建模型调优任务.md` |
| 12.8.2 | 删除模型调优任务 | 1144 | 45984-46000 | 10 | `chapters/volcengine/ark/12.8.2 删除模型调优任务.md` |
| 12.8.3 | 获取模型调优任务信息 | 1145-1155 | 46001-46454 | 411 | `chapters/volcengine/ark/12.8.3 获取模型调优任务信息.md` |
| 12.8.4 | 查询精调效果指标详细数据 | 1156-1157 | 46455-46500 | 32 | `chapters/volcengine/ark/12.8.4 查询精调效果指标详细数据.md` |
| 12.8.5 | 查询精调效果指标 | 1158 | 46501-46519 | 10 | `chapters/volcengine/ark/12.8.5 查询精调效果指标.md` |
| 12.8.6 | 获取模型调优任务列表 | 1159-1165 | 46520-46790 | 246 | `chapters/volcengine/ark/12.8.6 获取模型调优任务列表.md` |
| 12.8.7 | 重试模型调优任务 | 1166 | 46791-46807 | 9 | `chapters/volcengine/ark/12.8.7 重试模型调优任务.md` |
| 12.8.8 | 停止模型调优任务 | 1167 | 46808-46824 | 10 | `chapters/volcengine/ark/12.8.8 停止模型调优任务.md` |
| 12.8.9 | 更新模型调优任务 | 1168 | 46825-46848 | 14 | `chapters/volcengine/ark/12.8.9 更新模型调优任务.md` |
| 12.9.1 | 开启推理接入点 | 1169 | 46850-46870 | 13 | `chapters/volcengine/ark/12.9.1 开启推理接入点.md` |
| 12.9.2 | 停止推理接入点 | 1170 | 46871-46891 | 11 | `chapters/volcengine/ark/12.9.2 停止推理接入点.md` |
| 12.9.3 | 获取推理接入点列表 | 1171-1175 | 46892-47103 | 170 | `chapters/volcengine/ark/12.9.3 获取推理接入点列表.md` |
| 12.9.4 | 获取推理接入点 | 1176-1178 | 47104-47205 | 88 | `chapters/volcengine/ark/12.9.4 获取推理接入点.md` |
| 12.9.5 | 删除推理接入点 | 1179 | 47206-47225 | 12 | `chapters/volcengine/ark/12.9.5 删除推理接入点.md` |
| 12.9.6 | 更新推理接入点 | 1180-1184 | 47226-47410 | 160 | `chapters/volcengine/ark/12.9.6 更新推理接入点.md` |
| 12.9.7 | 创建推理接入点 | 1185-1190 | 47411-47638 | 193 | `chapters/volcengine/ark/12.9.7 创建推理接入点.md` |
| 12.9.8 | 获取接入点推理应用层加密证书 | 1191-1192 | 47639-47674 | 23 | `chapters/volcengine/ark/12.9.8 获取接入点推理应用层加密证书.md` |
| 12.9.9 | 创建推理接入点滚动升级任务 | 1193-1194 | 47675-47722 | 41 | `chapters/volcengine/ark/12.9.9 创建推理接入点滚动升级任务.md` |
| 12.9.10 | 查询推理接入点滚动升级详情 | 1195-1198 | 47723-47849 | 116 | `chapters/volcengine/ark/12.9.10 查询推理接入点滚动升级详情.md` |
| 12.9.11 | 回滚推理接入点滚动升级 | 1199 | 47850-47867 | 13 | `chapters/volcengine/ark/12.9.11 回滚推理接入点滚动升级.md` |
| 12.9.12 | 取消推理接入点滚动升级 | 1200 | 47868-47885 | 13 | `chapters/volcengine/ark/12.9.12 取消推理接入点滚动升级.md` |
| 12.10.1 | 创建批量推理任务 | 1201-1202 | 47887-47963 | 59 | `chapters/volcengine/ark/12.10.1 创建批量推理任务.md` |
| 12.10.2 | 获取批量推理任务列表 | 1203-1207 | 47964-48137 | 152 | `chapters/volcengine/ark/12.10.2 获取批量推理任务列表.md` |
| 12.10.3 | 获取批量推理任务 | 1208-1210 | 48138-48255 | 102 | `chapters/volcengine/ark/12.10.3 获取批量推理任务.md` |
| 12.10.4 | 更新批量推理任务 | 1211 | 48256-48279 | 17 | `chapters/volcengine/ark/12.10.4 更新批量推理任务.md` |
| 12.10.5 | 删除批量推理任务 | 1212 | 48280-48299 | 13 | `chapters/volcengine/ark/12.10.5 删除批量推理任务.md` |
| 12.10.6 | 停止批量推理任务 | 1213 | 48300-48322 | 16 | `chapters/volcengine/ark/12.10.6 停止批量推理任务.md` |
| 12.10.7 | 重启批量推理任务 | 1214 | 48323-48343 | 13 | `chapters/volcengine/ark/12.10.7 重启批量推理任务.md` |
| 12.11.1 | 创建评测任务 | 1215-1218 | 48345-48510 | 133 | `chapters/volcengine/ark/12.11.1 创建评测任务.md` |
| 12.11.2 | 删除评测任务 | 1219 | 48511-48532 | 13 | `chapters/volcengine/ark/12.11.2 删除评测任务.md` |
| 12.11.3 | 获取评测任务 | 1220-1222 | 48533-48614 | 66 | `chapters/volcengine/ark/12.11.3 获取评测任务.md` |
| 12.11.4 | 获取评测任务结果 | 1223-1225 | 48615-48717 | 87 | `chapters/volcengine/ark/12.11.4 获取评测任务结果.md` |
| 12.11.5 | 获取评测任务列表 | 1226-1229 | 48718-48864 | 129 | `chapters/volcengine/ark/12.11.5 获取评测任务列表.md` |
| 12.11.6 | 获取评测任务结果列表 | 1230-1233 | 48865-49006 | 120 | `chapters/volcengine/ark/12.11.6 获取评测任务结果列表.md` |
| 12.11.7 | 停止评测任务 | 1234 | 49007-49028 | 13 | `chapters/volcengine/ark/12.11.7 停止评测任务.md` |
| 12.11.8 | 更新评测任务 | 1235 | 49029-49054 | 18 | `chapters/volcengine/ark/12.11.8 更新评测任务.md` |
| 12.12.1 | 查询推理用量 | 1236-1238 | 49056-49183 | 75 | `chapters/volcengine/ark/12.12.1 查询推理用量.md` |
| 12.12.2 | 查询单请求用量 | 1239-1242 | 49184-49322 | 124 | `chapters/volcengine/ark/12.12.2 查询单请求用量.md` |
| 12.12.3 | 查询异步任务用量 | 1243-1244 | 49323-49393 | 62 | `chapters/volcengine/ark/12.12.3 查询异步任务用量.md` |
| 12.12.4 | 创建用量明细导出任务 | 1245-1246 | 49394-49448 | 33 | `chapters/volcengine/ark/12.12.4 创建用量明细导出任务.md` |
| 12.12.5 | 查询用量明细导出任务状态 | 1247-1249 | 49449-49551 | 71 | `chapters/volcengine/ark/12.12.5 查询用量明细导出任务状态.md` |
| 12.12.6 | 查询模型推理限额 | 1250 | 49552-49579 | 22 | `chapters/volcengine/ark/12.12.6 查询模型推理限额.md` |
| 12.12.7 | 开启模型推理限额 | 1251 | 49580-49604 | 16 | `chapters/volcengine/ark/12.12.7 开启模型推理限额.md` |
| 12.12.8 | 关闭模型推理限额 | 1252 | 49605-49625 | 12 | `chapters/volcengine/ark/12.12.8 关闭模型推理限额.md` |
| 12.13.1 | 创建方舟官方模型产物查询请求 | 1253 | 49627-49645 | 14 | `chapters/volcengine/ark/12.13.1 创建方舟官方模型产物查询请求.md` |
| 12.13.2 | 获取安全审计日志 | 1254-1256 | 49646-49765 | 85 | `chapters/volcengine/ark/12.13.2 获取安全审计日志.md` |
| 12.13.3 | 获取方舟官方产物确认结果 | 1257 | 49766-49795 | 24 | `chapters/volcengine/ark/12.13.3 获取方舟官方产物确认结果.md` |
| 12.14.1 | 上报视频生成模型效果问题 | 1258-1267 | 49797-50247 | 344 | `chapters/volcengine/ark/12.14.1 上报视频生成模型效果问题.md` |
| 12.14.2 | 查询视频生成模型效果问题结果 | 1268-1273 | 50248-50457 | 163 | `chapters/volcengine/ark/12.14.2 查询视频生成模型效果问题结果.md` |
| 12.14.3 | 上报大语言模型效果问题 | 1274-1276 | 50458-50576 | 87 | `chapters/volcengine/ark/12.14.3 上报大语言模型效果问题.md` |
| 12.14.4 | 查询大语言模型效果问题结果 | 1277-1280 | 50577-50704 | 102 | `chapters/volcengine/ark/12.14.4 查询大语言模型效果问题结果.md` |
| 12.14.5 | 上报 3D 生成效果问题 | 1281-1285 | 50705-50888 | 134 | `chapters/volcengine/ark/12.14.5 上报 3D 生成效果问题.md` |
| 12.14.6 | 查询 3D 生成效果问题结果 | 1286-1290 | 50889-51083 | 152 | `chapters/volcengine/ark/12.14.6 查询 3D 生成效果问题结果.md` |
| 13.1 | 兼容 OpenAI SDK | 1291-1294 | 51085-51201 | 103 | `chapters/volcengine/ark/13.1 兼容 OpenAI SDK.md` |
| 13.2 | 向后兼容性 | 1295 | 51202-51247 | 25 | `chapters/volcengine/ark/13.2 向后兼容性.md` |
| 13.3 | 错误码 - 第1部分 | 1295-1317 | 51248-53251 | 1954 | `chapters/volcengine/ark/13.3 错误码 - 第1部分.md` |
| 13.3 | 错误码 - 第2部分·错误码 | 1318-1327 | 53252-54017 | 732 | `chapters/volcengine/ark/13.3 错误码 - 第2部分·错误码.md` |
| 13.4 | SDK 常见使用示例 | 1328-1343 | 54018-54606 | 521 | `chapters/volcengine/ark/13.4 SDK 常见使用示例.md` |
