# 方舟 API 区章节表（ark）

来源：《火山方舟 API 参考》（1402 页）。241 个章节文件，接口级切分：一个接口/任务一个文件；超过 1500 行的按语义块自动再拆为`… - 第N部分`（5 个章节被拆分）。

「页码」是原 PDF 页码范围；「行范围」是中间 MD（`doc/<源文档>.md`）的 1 起始行号，可据此回查原文。章节文件本身已去掉页眉页脚，回查 PDF 时用这两列。文件名即章节标题，日常定位直接 Glob 文件名即可，用不到这两列。

**这张表用来 grep，不要整读。**

| 编号 | 标题 | 页码 | 行范围(源文件) | 行数 | 文件 |
|------|------|------|---------------|------|------|
| 1.1 | 获取 API Key 并配置 | 1 | 325-360 | 19 | `chapters/volcengine/ark/1.1 获取 API Key 并配置.md` |
| 1.2 | 安装及升级 SDK | 2-7 | 361-519 | 122 | `chapters/volcengine/ark/1.2 安装及升级 SDK.md` |
| 1.3 | Base URL 及鉴权 | 8-10 | 520-615 | 68 | `chapters/volcengine/ark/1.3 Base URL 及鉴权.md` |
| 2.1 | 对话(Chat) API | 11-42 | 617-2095 | 1091 | `chapters/volcengine/ark/2.1 对话(Chat) API.md` |
| 2.2.1 | 创建 Response - 第1部分 | 43-84 | 2096-3953 | 1578 | `chapters/volcengine/ark/2.2.1 创建 Response - 第1部分.md` |
| 2.2.1 | 创建 Response - 第2部分·响应参数 | 85-121 | 3954-5525 | 1382 | `chapters/volcengine/ark/2.2.1 创建 Response - 第2部分·响应参数.md` |
| 2.2.2 | 查询 Response 详情 | 122-152 | 5526-6823 | 1205 | `chapters/volcengine/ark/2.2.2 查询 Response 详情.md` |
| 2.2.3 | 查询 Response 输入项列表 | 153-177 | 6824-7858 | 937 | `chapters/volcengine/ark/2.2.3 查询 Response 输入项列表.md` |
| 2.2.4 | 删除 Response | 178 | 7859-7882 | 19 | `chapters/volcengine/ark/2.2.4 删除 Response.md` |
| 2.2.5.1 | Response 生命周期 - 第1部分 | 179-216 | 7883-9541 | 1466 | `chapters/volcengine/ark/2.2.5.1 Response 生命周期 - 第1部分.md` |
| 2.2.5.1 | Response 生命周期 - 第2部分 | 217-254 | 9542-11209 | 1476 | `chapters/volcengine/ark/2.2.5.1 Response 生命周期 - 第2部分.md` |
| 2.2.5.1 | Response 生命周期 - 第3部分 | 255-292 | 11210-12879 | 1479 | `chapters/volcengine/ark/2.2.5.1 Response 生命周期 - 第3部分.md` |
| 2.2.5.1 | Response 生命周期 - 第4部分 | 293-330 | 12880-14556 | 1474 | `chapters/volcengine/ark/2.2.5.1 Response 生命周期 - 第4部分.md` |
| 2.2.5.1 | Response 生命周期 - 第5部分 | 331-361 | 14557-15904 | 1184 | `chapters/volcengine/ark/2.2.5.1 Response 生命周期 - 第5部分.md` |
| 2.2.5.2 | Output Item 与文本回答 - 第1部分 | 362-397 | 15905-17502 | 1454 | `chapters/volcengine/ark/2.2.5.2 Output Item 与文本回答 - 第1部分.md` |
| 2.2.5.2 | Output Item 与文本回答 - 第2部分 | 398-417 | 17503-18342 | 796 | `chapters/volcengine/ark/2.2.5.2 Output Item 与文本回答 - 第2部分.md` |
| 2.2.5.3 | 工具调用事件 | 418-445 | 18343-19425 | 1024 | `chapters/volcengine/ark/2.2.5.3 工具调用事件.md` |
| 2.2.5.4 | 语音转写与错误事件 | 446-450 | 19426-19596 | 161 | `chapters/volcengine/ark/2.2.5.4 语音转写与错误事件.md` |
| 2.3.1 | 创建 Message | 451-467 | 19598-20273 | 584 | `chapters/volcengine/ark/2.3.1 创建 Message.md` |
| 2.3.2 | 统计 Messages 请求 token 数 | 468-476 | 20274-20614 | 279 | `chapters/volcengine/ark/2.3.2 统计 Messages 请求 token 数.md` |
| 3.1 | 创建视频生成任务 | 477-492 | 20616-21351 | 504 | `chapters/volcengine/ark/3.1 创建视频生成任务.md` |
| 3.2 | 查询视频生成任务 | 493-496 | 21352-21507 | 114 | `chapters/volcengine/ark/3.2 查询视频生成任务.md` |
| 3.3 | 查询视频生成任务列表 | 497-501 | 21508-21727 | 165 | `chapters/volcengine/ark/3.3 查询视频生成任务列表.md` |
| 3.4 | 取消或删除视频生成任务 | 502 | 21728-21773 | 42 | `chapters/volcengine/ark/3.4 取消或删除视频生成任务.md` |
| 4.1 | 图片生成 API | 503-522 | 21775-22730 | 661 | `chapters/volcengine/ark/4.1 图片生成 API.md` |
| 4.2 | 图片生成流式响应事件 | 523-526 | 22731-22865 | 124 | `chapters/volcengine/ark/4.2 图片生成流式响应事件.md` |
| 5.1.1 | 创建智能体 | 527-540 | 22868-23495 | 477 | `chapters/volcengine/ark/5.1.1 创建智能体.md` |
| 5.1.2 | 查询智能体列表 | 541-548 | 23496-23828 | 274 | `chapters/volcengine/ark/5.1.2 查询智能体列表.md` |
| 5.1.3 | 查询智能体详情 | 549-555 | 23829-24115 | 232 | `chapters/volcengine/ark/5.1.3 查询智能体详情.md` |
| 5.1.4 | 更新智能体 | 556-570 | 24116-24795 | 499 | `chapters/volcengine/ark/5.1.4 更新智能体.md` |
| 5.1.5 | 查询智能体版本列表 | 571-577 | 24796-25103 | 250 | `chapters/volcengine/ark/5.1.5 查询智能体版本列表.md` |
| 5.1.6 | 归档智能体 | 578-584 | 25104-25393 | 235 | `chapters/volcengine/ark/5.1.6 归档智能体.md` |
| 5.1.7 | 删除智能体 | 585 | 25394-25417 | 16 | `chapters/volcengine/ark/5.1.7 删除智能体.md` |
| 5.2.1 | 创建环境 | 586-592 | 25419-25706 | 215 | `chapters/volcengine/ark/5.2.1 创建环境.md` |
| 5.2.2 | 查询环境列表 | 593-596 | 25707-25856 | 129 | `chapters/volcengine/ark/5.2.2 查询环境列表.md` |
| 5.2.3 | 查询环境详情 | 597-600 | 25857-25982 | 104 | `chapters/volcengine/ark/5.2.3 查询环境详情.md` |
| 5.2.4 | 更新环境 | 601-608 | 25983-26306 | 232 | `chapters/volcengine/ark/5.2.4 更新环境.md` |
| 5.2.5 | 归档环境 | 609-612 | 26307-26433 | 104 | `chapters/volcengine/ark/5.2.5 归档环境.md` |
| 5.2.6 | 删除环境 | 613 | 26434-26458 | 16 | `chapters/volcengine/ark/5.2.6 删除环境.md` |
| 5.2.7.1 | 长轮询拉取待执行 Work | 614-616 | 26460-26566 | 77 | `chapters/volcengine/ark/5.2.7.1 长轮询拉取待执行 Work.md` |
| 5.2.7.2 | 认领 Work | 617-619 | 26567-26654 | 64 | `chapters/volcengine/ark/5.2.7.2 认领 Work.md` |
| 5.2.7.3 | 续租 Work | 620-621 | 26655-26721 | 47 | `chapters/volcengine/ark/5.2.7.3 续租 Work.md` |
| 5.2.7.4 | 查询 Work 队列状态 | 622 | 26722-26754 | 23 | `chapters/volcengine/ark/5.2.7.4 查询 Work 队列状态.md` |
| 5.2.7.5 | 停止 Work | 623-625 | 26755-26859 | 75 | `chapters/volcengine/ark/5.2.7.5 停止 Work.md` |
| 5.2.7.6 | 查询 Work 列表 | 626-628 | 26860-26967 | 86 | `chapters/volcengine/ark/5.2.7.6 查询 Work 列表.md` |
| 5.2.7.7 | 查询 Work 详情 | 629-630 | 26968-27040 | 54 | `chapters/volcengine/ark/5.2.7.7 查询 Work 详情.md` |
| 5.3.1 | 创建会话 | 631-664 | 27042-28518 | 1190 | `chapters/volcengine/ark/5.3.1 创建会话.md` |
| 5.3.2 | 查询会话列表 | 665-686 | 28519-29452 | 796 | `chapters/volcengine/ark/5.3.2 查询会话列表.md` |
| 5.3.3 | 查询会话详情 | 687-707 | 29453-30373 | 789 | `chapters/volcengine/ark/5.3.3 查询会话详情.md` |
| 5.3.4 | 更新会话标题和标签 | 708-728 | 30374-31265 | 758 | `chapters/volcengine/ark/5.3.4 更新会话标题和标签.md` |
| 5.3.5 | 升级会话 | 729-756 | 31266-32485 | 1010 | `chapters/volcengine/ark/5.3.5 升级会话.md` |
| 5.3.6 | 归档会话 | 757-778 | 32486-33417 | 792 | `chapters/volcengine/ark/5.3.6 归档会话.md` |
| 5.3.7 | 删除会话 | 779 | 33418-33444 | 19 | `chapters/volcengine/ark/5.3.7 删除会话.md` |
| 5.3.8.1 | 查询会话任务 | 780-784 | 33446-33633 | 156 | `chapters/volcengine/ark/5.3.8.1 查询会话任务.md` |
| 5.3.8.2 | 查询会话任务列表 | 785-787 | 33634-33747 | 88 | `chapters/volcengine/ark/5.3.8.2 查询会话任务列表.md` |
| 5.3.8.3 | 取消会话任务 | 788-789 | 33748-33806 | 31 | `chapters/volcengine/ark/5.3.8.3 取消会话任务.md` |
| 5.3.9.1 | 发送会话事件 | 790-791 | 33808-33872 | 42 | `chapters/volcengine/ark/5.3.9.1 发送会话事件.md` |
| 5.3.9.2 | 查询会话事件列表 | 792-794 | 33873-33959 | 58 | `chapters/volcengine/ark/5.3.9.2 查询会话事件列表.md` |
| 5.3.9.3 | 流式获取会话事件 | 795-796 | 33960-34035 | 41 | `chapters/volcengine/ark/5.3.9.3 流式获取会话事件.md` |
| 5.3.9.4 | 会话事件结构参考 - 第1部分 | 797-846 | 34036-36011 | 1787 | `chapters/volcengine/ark/5.3.9.4 会话事件结构参考 - 第1部分.md` |
| 5.3.10.1 | 添加会话资源 | 847-848 | 36013-36065 | 41 | `chapters/volcengine/ark/5.3.10.1 添加会话资源.md` |
| 5.3.10.2 | 查询会话资源列表 | 849-851 | 36066-36178 | 100 | `chapters/volcengine/ark/5.3.10.2 查询会话资源列表.md` |
| 5.3.10.3 | 查询会话资源 | 852-853 | 36179-36223 | 36 | `chapters/volcengine/ark/5.3.10.3 查询会话资源.md` |
| 5.3.11.1 | 查询线程列表 | 854-857 | 36225-36354 | 104 | `chapters/volcengine/ark/5.3.11.1 查询线程列表.md` |
| 5.3.11.2 | 查询线程详情 | 858-860 | 36355-36452 | 79 | `chapters/volcengine/ark/5.3.11.2 查询线程详情.md` |
| 5.3.11.3 | 查询线程事件列表 | 861-862 | 36453-36515 | 47 | `chapters/volcengine/ark/5.3.11.3 查询线程事件列表.md` |
| 5.3.11.4 | 流式获取线程事件 | 863-864 | 36516-36564 | 30 | `chapters/volcengine/ark/5.3.11.4 流式获取线程事件.md` |
| 5.4.1 | 创建 Webhook 接入点 | 865-867 | 36566-36665 | 61 | `chapters/volcengine/ark/5.4.1 创建 Webhook 接入点.md` |
| 5.4.2 | 查询 Webhook 接入点列表 | 868-870 | 36666-36763 | 66 | `chapters/volcengine/ark/5.4.2 查询 Webhook 接入点列表.md` |
| 5.4.3 | 查询 Webhook 接入点详情 | 871-872 | 36764-36842 | 51 | `chapters/volcengine/ark/5.4.3 查询 Webhook 接入点详情.md` |
| 5.4.4 | 更新 Webhook 接入点 | 873-875 | 36843-36942 | 59 | `chapters/volcengine/ark/5.4.4 更新 Webhook 接入点.md` |
| 5.4.5 | 启用 Webhook 接入点 | 876-877 | 36943-37023 | 51 | `chapters/volcengine/ark/5.4.5 启用 Webhook 接入点.md` |
| 5.4.6 | 删除 Webhook 接入点 | 878 | 37024-37043 | 15 | `chapters/volcengine/ark/5.4.6 删除 Webhook 接入点.md` |
| 5.4.7 | 停用 Webhook 接入点 | 879-880 | 37044-37125 | 51 | `chapters/volcengine/ark/5.4.7 停用 Webhook 接入点.md` |
| 5.4.8 | 重置 Webhook 签名密钥 | 881 | 37126-37149 | 16 | `chapters/volcengine/ark/5.4.8 重置 Webhook 签名密钥.md` |
| 5.4.9 | 发送 Webhook 测试事件 | 882 | 37150-37182 | 26 | `chapters/volcengine/ark/5.4.9 发送 Webhook 测试事件.md` |
| 5.4.10 | 查询 Webhook 事件详情 | 883-884 | 37183-37242 | 46 | `chapters/volcengine/ark/5.4.10 查询 Webhook 事件详情.md` |
| 5.4.11 | 查询 Webhook 事件列表 | 885-887 | 37243-37330 | 64 | `chapters/volcengine/ark/5.4.11 查询 Webhook 事件列表.md` |
| 5.4.12 | Webhook 事件结构参考 | 888-902 | 37331-37900 | 519 | `chapters/volcengine/ark/5.4.12 Webhook 事件结构参考.md` |
| 5.5.1 | 创建保管库 | 903-904 | 37902-37948 | 36 | `chapters/volcengine/ark/5.5.1 创建保管库.md` |
| 5.5.2 | 查询保管库列表 | 905-906 | 37949-38026 | 60 | `chapters/volcengine/ark/5.5.2 查询保管库列表.md` |
| 5.5.3 | 查询保管库详情 | 907 | 38027-38059 | 28 | `chapters/volcengine/ark/5.5.3 查询保管库详情.md` |
| 5.5.4 | 更新保管库 | 908-909 | 38060-38107 | 37 | `chapters/volcengine/ark/5.5.4 更新保管库.md` |
| 5.5.5 | 删除保管库 | 910 | 38108-38132 | 21 | `chapters/volcengine/ark/5.5.5 删除保管库.md` |
| 5.5.6.1 | 创建凭证 | 911-920 | 38134-38603 | 364 | `chapters/volcengine/ark/5.5.6.1 创建凭证.md` |
| 5.5.6.2 | 查询凭证列表 | 921-925 | 38604-38827 | 185 | `chapters/volcengine/ark/5.5.6.2 查询凭证列表.md` |
| 5.5.6.3 | 查询凭证详情 | 926-930 | 38828-39025 | 163 | `chapters/volcengine/ark/5.5.6.3 查询凭证详情.md` |
| 5.5.6.4 | 更新凭证 | 931-940 | 39026-39469 | 340 | `chapters/volcengine/ark/5.5.6.4 更新凭证.md` |
| 5.5.6.5 | 删除凭证 | 941 | 39470-39496 | 21 | `chapters/volcengine/ark/5.5.6.5 删除凭证.md` |
| 5.6.1 | 创建记忆库 | 942-944 | 39498-39577 | 61 | `chapters/volcengine/ark/5.6.1 创建记忆库.md` |
| 5.6.2 | 查询记忆库列表 | 945-947 | 39578-39680 | 80 | `chapters/volcengine/ark/5.6.2 查询记忆库列表.md` |
| 5.6.3 | 查询记忆库详情 | 948-949 | 39681-39742 | 47 | `chapters/volcengine/ark/5.6.3 查询记忆库详情.md` |
| 5.6.4 | 更新记忆库 | 950-952 | 39743-39823 | 61 | `chapters/volcengine/ark/5.6.4 更新记忆库.md` |
| 5.6.5 | 删除记忆库 | 953 | 39824-39849 | 17 | `chapters/volcengine/ark/5.6.5 删除记忆库.md` |
| 5.6.6.1 | 创建记忆 | 954-955 | 39851-39915 | 51 | `chapters/volcengine/ark/5.6.6.1 创建记忆.md` |
| 5.6.6.2 | 批量创建记忆 | 956-958 | 39916-40033 | 90 | `chapters/volcengine/ark/5.6.6.2 批量创建记忆.md` |
| 5.6.6.3 | 查询记忆列表 | 959-961 | 40034-40127 | 70 | `chapters/volcengine/ark/5.6.6.3 查询记忆列表.md` |
| 5.6.6.4 | 查询记忆详情 | 962-963 | 40128-40186 | 45 | `chapters/volcengine/ark/5.6.6.4 查询记忆详情.md` |
| 5.6.6.5 | 更新记忆 | 964-965 | 40187-40259 | 51 | `chapters/volcengine/ark/5.6.6.5 更新记忆.md` |
| 5.6.6.6 | 删除记忆 | 966 | 40260-40288 | 18 | `chapters/volcengine/ark/5.6.6.6 删除记忆.md` |
| 5.7.1 | 创建 Dream | 967-970 | 40290-40414 | 108 | `chapters/volcengine/ark/5.7.1 创建 Dream.md` |
| 5.7.2 | 查询 Dream 列表 | 971-974 | 40415-40552 | 119 | `chapters/volcengine/ark/5.7.2 查询 Dream 列表.md` |
| 5.7.3 | 查询 Dream | 975-977 | 40553-40648 | 83 | `chapters/volcengine/ark/5.7.3 查询 Dream.md` |
| 5.7.4 | 取消 Dream | 978-980 | 40649-40747 | 84 | `chapters/volcengine/ark/5.7.4 取消 Dream.md` |
| 5.8.1 | 创建技能 | 981-982 | 40749-40817 | 49 | `chapters/volcengine/ark/5.8.1 创建技能.md` |
| 5.8.2 | 查询技能列表 | 983-984 | 40818-40892 | 61 | `chapters/volcengine/ark/5.8.2 查询技能列表.md` |
| 5.8.3 | 查询技能详情 | 985-986 | 40893-40938 | 36 | `chapters/volcengine/ark/5.8.3 查询技能详情.md` |
| 5.8.4 | 设置技能内容保护 | 987-988 | 40939-40984 | 37 | `chapters/volcengine/ark/5.8.4 设置技能内容保护.md` |
| 5.8.5 | 删除技能 | 989 | 40985-41010 | 18 | `chapters/volcengine/ark/5.8.5 删除技能.md` |
| 5.8.6 | 创建新版本的技能 | 990-991 | 41011-41070 | 41 | `chapters/volcengine/ark/5.8.6 创建新版本的技能.md` |
| 5.8.7 | 查询技能的版本列表 | 992-993 | 41071-41126 | 48 | `chapters/volcengine/ark/5.8.7 查询技能的版本列表.md` |
| 5.8.8 | 查询指定版本的技能 | 994 | 41127-41156 | 26 | `chapters/volcengine/ark/5.8.8 查询指定版本的技能.md` |
| 5.8.9 | 删除指定版本的技能 | 995 | 41157-41178 | 17 | `chapters/volcengine/ark/5.8.9 删除指定版本的技能.md` |
| 5.8.10 | 下载指定版本的技能 | 996 | 41179-41197 | 14 | `chapters/volcengine/ark/5.8.10 下载指定版本的技能.md` |
| 5.8.11 | 扫描 GitHub 技能 | 997-998 | 41198-41250 | 43 | `chapters/volcengine/ark/5.8.11 扫描 GitHub 技能.md` |
| 5.8.12 | 导入 GitHub 技能 | 999-1000 | 41251-41326 | 58 | `chapters/volcengine/ark/5.8.12 导入 GitHub 技能.md` |
| 5.9.1 | 创建 Deployment | 1001-1006 | 41328-41566 | 197 | `chapters/volcengine/ark/5.9.1 创建 Deployment.md` |
| 5.9.2 | 更新 Deployment | 1007-1012 | 41567-41809 | 201 | `chapters/volcengine/ark/5.9.2 更新 Deployment.md` |
| 5.9.3 | 查询 Deployment 详情 | 1013-1016 | 41810-41948 | 116 | `chapters/volcengine/ark/5.9.3 查询 Deployment 详情.md` |
| 5.9.4 | 查询 Deployment 列表 | 1017-1021 | 41949-42128 | 152 | `chapters/volcengine/ark/5.9.4 查询 Deployment 列表.md` |
| 5.9.5 | 恢复 Deployment | 1022-1025 | 42129-42269 | 116 | `chapters/volcengine/ark/5.9.5 恢复 Deployment.md` |
| 5.9.6 | 暂停 Deployment | 1026-1029 | 42270-42409 | 117 | `chapters/volcengine/ark/5.9.6 暂停 Deployment.md` |
| 5.9.7 | 归档 Deployment | 1030-1033 | 42410-42549 | 116 | `chapters/volcengine/ark/5.9.7 归档 Deployment.md` |
| 5.9.8 | 立即运行 Deployment | 1034-1035 | 42550-42606 | 47 | `chapters/volcengine/ark/5.9.8 立即运行 Deployment.md` |
| 5.9.9 | 查询 Deployment Run 列表 | 1036-1038 | 42607-42695 | 71 | `chapters/volcengine/ark/5.9.9 查询 Deployment Run 列表.md` |
| 5.9.10 | 查询 Deployment Run 详情 | 1039-1040 | 42696-42752 | 46 | `chapters/volcengine/ark/5.9.10 查询 Deployment Run 详情.md` |
| 6.1 | 上传文件 | 1041-1046 | 42754-42979 | 165 | `chapters/volcengine/ark/6.1 上传文件.md` |
| 6.2 | 查询文件详情 | 1047-1049 | 42980-43063 | 67 | `chapters/volcengine/ark/6.2 查询文件详情.md` |
| 6.3 | 查询文件列表 | 1050-1053 | 43064-43208 | 116 | `chapters/volcengine/ark/6.3 查询文件列表.md` |
| 6.4 | 删除文件 | 1054 | 43209-43231 | 19 | `chapters/volcengine/ark/6.4 删除文件.md` |
| 6.5 | The file object | 1055-1057 | 43232-43303 | 57 | `chapters/volcengine/ark/6.5 The file object.md` |
| 7.1 | Models API | 1058-1061 | 43305-43438 | 123 | `chapters/volcengine/ark/7.1 Models API.md` |
| 8.1 | System One API（beta） | 1062-1069 | 43440-43712 | 240 | `chapters/volcengine/ark/8.1 System One API（beta）.md` |
| 9.1.1 | 创建 3D 生成任务 API | 1070-1072 | 43715-43819 | 79 | `chapters/volcengine/ark/9.1.1 创建 3D 生成任务 API.md` |
| 9.1.2 | 查询 3D 生成任务 API | 1073-1074 | 43820-43889 | 52 | `chapters/volcengine/ark/9.1.2 查询 3D 生成任务 API.md` |
| 9.1.3 | 查询 3D 生成任务列表 | 1075-1077 | 43890-44003 | 87 | `chapters/volcengine/ark/9.1.3 查询 3D 生成任务列表.md` |
| 9.1.4 | 取消或删除 3D 生成任务 | 1078 | 44004-44045 | 38 | `chapters/volcengine/ark/9.1.4 取消或删除 3D 生成任务.md` |
| 9.2.1 | 创建 3D 生成任务 | 1079-1083 | 44047-44261 | 148 | `chapters/volcengine/ark/9.2.1 创建 3D 生成任务.md` |
| 9.2.2 | 查询 3D 生成任务 | 1084-1085 | 44262-44327 | 48 | `chapters/volcengine/ark/9.2.2 查询 3D 生成任务.md` |
| 9.2.3 | 查询 3D 生成任务列表 | 1086-1088 | 44328-44435 | 81 | `chapters/volcengine/ark/9.2.3 查询 3D 生成任务列表.md` |
| 9.2.4 | 取消或删除 3D 生成任务 | 1089 | 44436-44470 | 31 | `chapters/volcengine/ark/9.2.4 取消或删除 3D 生成任务.md` |
| 9.3.1 | 创建 3D 生成任务 | 1090-1093 | 44472-44603 | 95 | `chapters/volcengine/ark/9.3.1 创建 3D 生成任务.md` |
| 9.3.2 | 查询 3D 生成任务 | 1094-1095 | 44604-44669 | 48 | `chapters/volcengine/ark/9.3.2 查询 3D 生成任务.md` |
| 9.3.3 | 查询 3D 生成任务列表 | 1096-1098 | 44670-44777 | 81 | `chapters/volcengine/ark/9.3.3 查询 3D 生成任务列表.md` |
| 9.3.4 | 取消或删除 3D 生成任务 | 1099 | 44778-44812 | 31 | `chapters/volcengine/ark/9.3.4 取消或删除 3D 生成任务.md` |
| 10.1 | 多模态向量化 API | 1100-1104 | 44814-45012 | 147 | `chapters/volcengine/ark/10.1 多模态向量化 API.md` |
| 11.1 | 分词 API | 1105-1106 | 45014-45060 | 39 | `chapters/volcengine/ark/11.1 分词 API.md` |
| 12.1.1 | 获取临时 API Key | 1107 | 45063-45097 | 26 | `chapters/volcengine/ark/12.1.1 获取临时 API Key.md` |
| 12.2.1 | 创建个人版套餐 | 1108-1109 | 45099-45157 | 34 | `chapters/volcengine/ark/12.2.1 创建个人版套餐.md` |
| 12.2.2 | 续费个人版套餐 | 1110-1111 | 45158-45203 | 27 | `chapters/volcengine/ark/12.2.2 续费个人版套餐.md` |
| 12.2.3 | 查询个人版套餐 | 1112 | 45204-45231 | 21 | `chapters/volcengine/ark/12.2.3 查询个人版套餐.md` |
| 12.2.4.1 | 查询 Agent Plan 支持的模型列表 | 1113 | 45233-45252 | 14 | `chapters/volcengine/ark/12.2.4.1 查询 Agent Plan 支持的模型列表.md` |
| 12.2.4.2 | 轮换个人版 API Key | 1114 | 45253-45279 | 17 | `chapters/volcengine/ark/12.2.4.2 轮换个人版 API Key.md` |
| 12.2.4.3 | 获取套餐 AFP 额度 | 1115-1116 | 45280-45354 | 66 | `chapters/volcengine/ark/12.2.4.3 获取套餐 AFP 额度.md` |
| 12.2.4.4 | 获取套餐用量详情 | 1117-1118 | 45355-45403 | 39 | `chapters/volcengine/ark/12.2.4.4 获取套餐用量详情.md` |
| 12.2.5.1 | 查询 Coding Plan 支持的模型列表 | 1119 | 45405-45420 | 12 | `chapters/volcengine/ark/12.2.5.1 查询 Coding Plan 支持的模型列表.md` |
| 12.2.6.1 | 创建企业版席位 | 1120-1121 | 45422-45493 | 44 | `chapters/volcengine/ark/12.2.6.1 创建企业版席位.md` |
| 12.2.6.2 | 续费企业版席位 | 1122-1123 | 45494-45532 | 29 | `chapters/volcengine/ark/12.2.6.2 续费企业版席位.md` |
| 12.2.6.3 | 批量绑定企业版席位 | 1124-1125 | 45533-45576 | 32 | `chapters/volcengine/ark/12.2.6.3 批量绑定企业版席位.md` |
| 12.2.6.4 | 批量更新企业版席位 API Key | 1126 | 45577-45610 | 25 | `chapters/volcengine/ark/12.2.6.4 批量更新企业版席位 API Key.md` |
| 12.2.6.5 | 获取单个/多个席位的 AFP 额度用量 | 1127-1129 | 45611-45702 | 80 | `chapters/volcengine/ark/12.2.6.5 获取单个-多个席位的 AFP 额度用量.md` |
| 12.2.6.6 | 查询席位 AFP 额度用量列表 | 1130-1133 | 45703-45836 | 114 | `chapters/volcengine/ark/12.2.6.6 查询席位 AFP 额度用量列表.md` |
| 12.2.6.7 | 获取单个/多个席位的模型调用数据明细 | 1134-1135 | 45837-45905 | 58 | `chapters/volcengine/ark/12.2.6.7 获取单个-多个席位的模型调用数据明细.md` |
| 12.2.6.8 | 创建共享包 | 1136-1137 | 45906-45978 | 51 | `chapters/volcengine/ark/12.2.6.8 创建共享包.md` |
| 12.2.6.9 | 续费共享包 | 1138-1139 | 45979-46037 | 39 | `chapters/volcengine/ark/12.2.6.9 续费共享包.md` |
| 12.2.6.10 | 查询共享包订阅信息 | 1140-1141 | 46038-46100 | 47 | `chapters/volcengine/ark/12.2.6.10 查询共享包订阅信息.md` |
| 12.3.1 | 获取基础模型版本列表 | 1142-1144 | 46102-46189 | 72 | `chapters/volcengine/ark/12.3.1 获取基础模型版本列表.md` |
| 12.3.2 | 获取基础模型版本信息 | 1145-1152 | 46190-46507 | 273 | `chapters/volcengine/ark/12.3.2 获取基础模型版本信息.md` |
| 12.3.3 | 获取基础模型列表 | 1153-1157 | 46508-46760 | 186 | `chapters/volcengine/ark/12.3.3 获取基础模型列表.md` |
| 12.3.4 | 获取基础模型信息 | 1158-1160 | 46761-46885 | 93 | `chapters/volcengine/ark/12.3.4 获取基础模型信息.md` |
| 12.4.1 | 批量开通基础模型 | 1161 | 46887-46901 | 11 | `chapters/volcengine/ark/12.4.1 批量开通基础模型.md` |
| 12.4.2 | 启用自动开通新模型 | 1162 | 46902-46913 | 7 | `chapters/volcengine/ark/12.4.2 启用自动开通新模型.md` |
| 12.4.3 | 关闭自动开通新模型 | 1163 | 46914-46925 | 7 | `chapters/volcengine/ark/12.4.3 关闭自动开通新模型.md` |
| 12.4.4 | 查询模型开通详情 | 1164-1167 | 46926-47068 | 131 | `chapters/volcengine/ark/12.4.4 查询模型开通详情.md` |
| 12.4.5 | 查询模型开通列表 | 1168-1172 | 47069-47246 | 163 | `chapters/volcengine/ark/12.4.5 查询模型开通列表.md` |
| 12.4.6 | 查询模型价格 | 1173-1177 | 47247-47448 | 156 | `chapters/volcengine/ark/12.4.6 查询模型价格.md` |
| 12.5.1 | 批量开通资源 | 1178 | 47450-47468 | 14 | `chapters/volcengine/ark/12.5.1 批量开通资源.md` |
| 12.5.2 | 查询资源开通列表 | 1179-1181 | 47469-47570 | 92 | `chapters/volcengine/ark/12.5.2 查询资源开通列表.md` |
| 12.6.1 | 查询模型限流 | 1182-1184 | 47572-47671 | 91 | `chapters/volcengine/ark/12.6.1 查询模型限流.md` |
| 12.7.1 | 删除定制模型 | 1185 | 47673-47698 | 17 | `chapters/volcengine/ark/12.7.1 删除定制模型.md` |
| 12.7.2 | 获取定制模型信息 | 1186-1188 | 47699-47807 | 97 | `chapters/volcengine/ark/12.7.2 获取定制模型信息.md` |
| 12.7.3 | 更新定制模型 | 1189 | 47808-47840 | 22 | `chapters/volcengine/ark/12.7.3 更新定制模型.md` |
| 12.7.4 | 获取定制模型列表 | 1190-1192 | 47841-47959 | 102 | `chapters/volcengine/ark/12.7.4 获取定制模型列表.md` |
| 12.8.1 | 创建模型调优任务 | 1193-1200 | 47961-48279 | 281 | `chapters/volcengine/ark/12.8.1 创建模型调优任务.md` |
| 12.8.2 | 删除模型调优任务 | 1201 | 48280-48296 | 10 | `chapters/volcengine/ark/12.8.2 删除模型调优任务.md` |
| 12.8.3 | 获取模型调优任务信息 | 1202-1212 | 48297-48750 | 411 | `chapters/volcengine/ark/12.8.3 获取模型调优任务信息.md` |
| 12.8.4 | 查询精调效果指标详细数据 | 1213-1214 | 48751-48796 | 32 | `chapters/volcengine/ark/12.8.4 查询精调效果指标详细数据.md` |
| 12.8.5 | 查询精调效果指标 | 1215 | 48797-48815 | 10 | `chapters/volcengine/ark/12.8.5 查询精调效果指标.md` |
| 12.8.6 | 获取模型调优任务列表 | 1216-1222 | 48816-49086 | 246 | `chapters/volcengine/ark/12.8.6 获取模型调优任务列表.md` |
| 12.8.7 | 重试模型调优任务 | 1223 | 49087-49103 | 9 | `chapters/volcengine/ark/12.8.7 重试模型调优任务.md` |
| 12.8.8 | 停止模型调优任务 | 1224 | 49104-49120 | 10 | `chapters/volcengine/ark/12.8.8 停止模型调优任务.md` |
| 12.8.9 | 更新模型调优任务 | 1225 | 49121-49144 | 14 | `chapters/volcengine/ark/12.8.9 更新模型调优任务.md` |
| 12.9.1 | 开启推理接入点 | 1226 | 49146-49166 | 13 | `chapters/volcengine/ark/12.9.1 开启推理接入点.md` |
| 12.9.2 | 停止推理接入点 | 1227 | 49167-49187 | 11 | `chapters/volcengine/ark/12.9.2 停止推理接入点.md` |
| 12.9.3 | 获取推理接入点列表 | 1228-1232 | 49188-49399 | 170 | `chapters/volcengine/ark/12.9.3 获取推理接入点列表.md` |
| 12.9.4 | 获取推理接入点 | 1233-1235 | 49400-49501 | 88 | `chapters/volcengine/ark/12.9.4 获取推理接入点.md` |
| 12.9.5 | 删除推理接入点 | 1236 | 49502-49521 | 12 | `chapters/volcengine/ark/12.9.5 删除推理接入点.md` |
| 12.9.6 | 更新推理接入点 | 1237-1241 | 49522-49706 | 160 | `chapters/volcengine/ark/12.9.6 更新推理接入点.md` |
| 12.9.7 | 创建推理接入点 | 1242-1247 | 49707-49934 | 193 | `chapters/volcengine/ark/12.9.7 创建推理接入点.md` |
| 12.9.8 | 获取接入点推理应用层加密证书 | 1248-1249 | 49935-49970 | 23 | `chapters/volcengine/ark/12.9.8 获取接入点推理应用层加密证书.md` |
| 12.9.9 | 创建推理接入点滚动升级任务 | 1250-1251 | 49971-50018 | 41 | `chapters/volcengine/ark/12.9.9 创建推理接入点滚动升级任务.md` |
| 12.9.10 | 查询推理接入点滚动升级详情 | 1252-1255 | 50019-50145 | 116 | `chapters/volcengine/ark/12.9.10 查询推理接入点滚动升级详情.md` |
| 12.9.11 | 回滚推理接入点滚动升级 | 1256 | 50146-50163 | 13 | `chapters/volcengine/ark/12.9.11 回滚推理接入点滚动升级.md` |
| 12.9.12 | 取消推理接入点滚动升级 | 1257 | 50164-50181 | 13 | `chapters/volcengine/ark/12.9.12 取消推理接入点滚动升级.md` |
| 12.10.1 | 创建批量推理任务 | 1258-1259 | 50183-50259 | 59 | `chapters/volcengine/ark/12.10.1 创建批量推理任务.md` |
| 12.10.2 | 获取批量推理任务列表 | 1260-1264 | 50260-50433 | 152 | `chapters/volcengine/ark/12.10.2 获取批量推理任务列表.md` |
| 12.10.3 | 获取批量推理任务 | 1265-1267 | 50434-50551 | 102 | `chapters/volcengine/ark/12.10.3 获取批量推理任务.md` |
| 12.10.4 | 更新批量推理任务 | 1268 | 50552-50575 | 17 | `chapters/volcengine/ark/12.10.4 更新批量推理任务.md` |
| 12.10.5 | 删除批量推理任务 | 1269 | 50576-50595 | 13 | `chapters/volcengine/ark/12.10.5 删除批量推理任务.md` |
| 12.10.6 | 停止批量推理任务 | 1270 | 50596-50618 | 16 | `chapters/volcengine/ark/12.10.6 停止批量推理任务.md` |
| 12.10.7 | 重启批量推理任务 | 1271 | 50619-50639 | 13 | `chapters/volcengine/ark/12.10.7 重启批量推理任务.md` |
| 12.11.1 | 创建评测任务 | 1272-1275 | 50641-50806 | 133 | `chapters/volcengine/ark/12.11.1 创建评测任务.md` |
| 12.11.2 | 删除评测任务 | 1276 | 50807-50828 | 13 | `chapters/volcengine/ark/12.11.2 删除评测任务.md` |
| 12.11.3 | 获取评测任务 | 1277-1279 | 50829-50910 | 66 | `chapters/volcengine/ark/12.11.3 获取评测任务.md` |
| 12.11.4 | 获取评测任务结果 | 1280-1282 | 50911-51013 | 87 | `chapters/volcengine/ark/12.11.4 获取评测任务结果.md` |
| 12.11.5 | 获取评测任务列表 | 1283-1286 | 51014-51160 | 129 | `chapters/volcengine/ark/12.11.5 获取评测任务列表.md` |
| 12.11.6 | 获取评测任务结果列表 | 1287-1290 | 51161-51302 | 120 | `chapters/volcengine/ark/12.11.6 获取评测任务结果列表.md` |
| 12.11.7 | 停止评测任务 | 1291 | 51303-51324 | 13 | `chapters/volcengine/ark/12.11.7 停止评测任务.md` |
| 12.11.8 | 更新评测任务 | 1292 | 51325-51350 | 18 | `chapters/volcengine/ark/12.11.8 更新评测任务.md` |
| 12.12.1 | 查询推理用量 | 1293-1296 | 51352-51497 | 87 | `chapters/volcengine/ark/12.12.1 查询推理用量.md` |
| 12.12.2 | 查询单请求用量 | 1297-1300 | 51498-51636 | 124 | `chapters/volcengine/ark/12.12.2 查询单请求用量.md` |
| 12.12.3 | 查询异步任务用量 | 1301-1302 | 51637-51707 | 62 | `chapters/volcengine/ark/12.12.3 查询异步任务用量.md` |
| 12.12.4 | 创建用量明细导出任务 | 1303-1304 | 51708-51762 | 33 | `chapters/volcengine/ark/12.12.4 创建用量明细导出任务.md` |
| 12.12.5 | 查询用量明细导出任务状态 | 1305-1307 | 51763-51865 | 71 | `chapters/volcengine/ark/12.12.5 查询用量明细导出任务状态.md` |
| 12.12.6 | 查询模型推理限额 | 1308 | 51866-51893 | 22 | `chapters/volcengine/ark/12.12.6 查询模型推理限额.md` |
| 12.12.7 | 开启模型推理限额 | 1309 | 51894-51918 | 16 | `chapters/volcengine/ark/12.12.7 开启模型推理限额.md` |
| 12.12.8 | 关闭模型推理限额 | 1310 | 51919-51939 | 12 | `chapters/volcengine/ark/12.12.8 关闭模型推理限额.md` |
| 12.13.1 | 创建方舟官方模型产物查询请求 | 1311 | 51941-51959 | 14 | `chapters/volcengine/ark/12.13.1 创建方舟官方模型产物查询请求.md` |
| 12.13.2 | 获取安全审计日志 | 1312-1314 | 51960-52079 | 85 | `chapters/volcengine/ark/12.13.2 获取安全审计日志.md` |
| 12.13.3 | 获取方舟官方产物确认结果 | 1315 | 52080-52109 | 24 | `chapters/volcengine/ark/12.13.3 获取方舟官方产物确认结果.md` |
| 12.14.1 | 上报视频生成模型效果问题 | 1316-1325 | 52111-52561 | 344 | `chapters/volcengine/ark/12.14.1 上报视频生成模型效果问题.md` |
| 12.14.2 | 查询视频生成模型效果问题结果 | 1326-1332 | 52562-52847 | 229 | `chapters/volcengine/ark/12.14.2 查询视频生成模型效果问题结果.md` |
| 12.14.3 | 上报大语言模型效果问题 | 1333-1335 | 52848-52966 | 87 | `chapters/volcengine/ark/12.14.3 上报大语言模型效果问题.md` |
| 12.14.4 | 查询大语言模型效果问题结果 | 1336-1339 | 52967-53094 | 102 | `chapters/volcengine/ark/12.14.4 查询大语言模型效果问题结果.md` |
| 12.14.5 | 上报 3D 生成效果问题 | 1340-1344 | 53095-53278 | 134 | `chapters/volcengine/ark/12.14.5 上报 3D 生成效果问题.md` |
| 12.14.6 | 查询 3D 生成效果问题结果 | 1345-1349 | 53279-53469 | 148 | `chapters/volcengine/ark/12.14.6 查询 3D 生成效果问题结果.md` |
| 13.1 | 兼容 OpenAI SDK | 1350-1353 | 53471-53587 | 103 | `chapters/volcengine/ark/13.1 兼容 OpenAI SDK.md` |
| 13.2 | 向后兼容性 | 1354 | 53588-53633 | 25 | `chapters/volcengine/ark/13.2 向后兼容性.md` |
| 13.3 | 错误码 - 第1部分 | 1354-1376 | 53634-55637 | 1954 | `chapters/volcengine/ark/13.3 错误码 - 第1部分.md` |
| 13.3 | 错误码 - 第2部分·错误码 | 1377-1386 | 55638-56403 | 732 | `chapters/volcengine/ark/13.3 错误码 - 第2部分·错误码.md` |
| 13.4 | SDK 常见使用示例 | 1387-1402 | 56404-56992 | 521 | `chapters/volcengine/ark/13.4 SDK 常见使用示例.md` |
