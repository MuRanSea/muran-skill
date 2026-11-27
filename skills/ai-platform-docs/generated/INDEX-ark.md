# 方舟 API 区章节表（ark）

来源：《火山方舟 API 参考》（1400 页）。241 个章节文件，接口级切分：一个接口/任务一个文件；超过 1500 行的按语义块自动再拆为`… - 第N部分`（5 个章节被拆分）。

「页码」是原 PDF 页码范围；「行范围」是中间 MD（`doc/<源文档>.md`）的 1 起始行号，可据此回查原文。章节文件本身已去掉页眉页脚，回查 PDF 时用这两列。文件名即章节标题，日常定位直接 Glob 文件名即可，用不到这两列。

**这张表用来 grep，不要整读。**

| 编号 | 标题 | 页码 | 行范围(源文件) | 行数 | 文件 |
|------|------|------|---------------|------|------|
| 1.1 | 获取 API Key 并配置 | 1 | 325-360 | 19 | `chapters/volcengine/ark/1.1 获取 API Key 并配置.md` |
| 1.2 | 安装及升级 SDK | 2-7 | 361-519 | 122 | `chapters/volcengine/ark/1.2 安装及升级 SDK.md` |
| 1.3 | Base URL 及鉴权 | 8-10 | 520-615 | 68 | `chapters/volcengine/ark/1.3 Base URL 及鉴权.md` |
| 2.1 | 对话(Chat) API | 11-42 | 617-2095 | 1091 | `chapters/volcengine/ark/2.1 对话(Chat) API.md` |
| 2.2.1 | 创建 Response - 第1部分 | 43-85 | 2096-3973 | 1589 | `chapters/volcengine/ark/2.2.1 创建 Response - 第1部分.md` |
| 2.2.1 | 创建 Response - 第2部分·响应参数 | 86-121 | 3974-5535 | 1380 | `chapters/volcengine/ark/2.2.1 创建 Response - 第2部分·响应参数.md` |
| 2.2.2 | 查询 Response 详情 | 122-152 | 5536-6833 | 1205 | `chapters/volcengine/ark/2.2.2 查询 Response 详情.md` |
| 2.2.3 | 查询 Response 输入项列表 | 153-177 | 6834-7877 | 945 | `chapters/volcengine/ark/2.2.3 查询 Response 输入项列表.md` |
| 2.2.4 | 删除 Response | 178 | 7878-7901 | 19 | `chapters/volcengine/ark/2.2.4 删除 Response.md` |
| 2.2.5.1 | Response 生命周期 - 第1部分 | 179-216 | 7902-9560 | 1466 | `chapters/volcengine/ark/2.2.5.1 Response 生命周期 - 第1部分.md` |
| 2.2.5.1 | Response 生命周期 - 第2部分 | 217-254 | 9561-11228 | 1476 | `chapters/volcengine/ark/2.2.5.1 Response 生命周期 - 第2部分.md` |
| 2.2.5.1 | Response 生命周期 - 第3部分 | 255-292 | 11229-12898 | 1479 | `chapters/volcengine/ark/2.2.5.1 Response 生命周期 - 第3部分.md` |
| 2.2.5.1 | Response 生命周期 - 第4部分 | 293-330 | 12899-14575 | 1474 | `chapters/volcengine/ark/2.2.5.1 Response 生命周期 - 第4部分.md` |
| 2.2.5.1 | Response 生命周期 - 第5部分 | 331-361 | 14576-15923 | 1184 | `chapters/volcengine/ark/2.2.5.1 Response 生命周期 - 第5部分.md` |
| 2.2.5.2 | Output Item 与文本回答 - 第1部分 | 362-397 | 15924-17521 | 1454 | `chapters/volcengine/ark/2.2.5.2 Output Item 与文本回答 - 第1部分.md` |
| 2.2.5.2 | Output Item 与文本回答 - 第2部分 | 398-417 | 17522-18361 | 796 | `chapters/volcengine/ark/2.2.5.2 Output Item 与文本回答 - 第2部分.md` |
| 2.2.5.3 | 工具调用事件 | 418-445 | 18362-19444 | 1024 | `chapters/volcengine/ark/2.2.5.3 工具调用事件.md` |
| 2.2.5.4 | 语音转写与错误事件 | 446-450 | 19445-19615 | 161 | `chapters/volcengine/ark/2.2.5.4 语音转写与错误事件.md` |
| 2.3.1 | 创建 Message | 451-467 | 19617-20292 | 584 | `chapters/volcengine/ark/2.3.1 创建 Message.md` |
| 2.3.2 | 统计 Messages 请求 token 数 | 468-476 | 20293-20633 | 279 | `chapters/volcengine/ark/2.3.2 统计 Messages 请求 token 数.md` |
| 3.1 | 创建视频生成任务 | 477-492 | 20635-21370 | 504 | `chapters/volcengine/ark/3.1 创建视频生成任务.md` |
| 3.2 | 查询视频生成任务 | 493-496 | 21371-21526 | 114 | `chapters/volcengine/ark/3.2 查询视频生成任务.md` |
| 3.3 | 查询视频生成任务列表 | 497-501 | 21527-21746 | 165 | `chapters/volcengine/ark/3.3 查询视频生成任务列表.md` |
| 3.4 | 取消或删除视频生成任务 | 502 | 21747-21792 | 42 | `chapters/volcengine/ark/3.4 取消或删除视频生成任务.md` |
| 4.1 | 图片生成 API | 503-522 | 21794-22747 | 661 | `chapters/volcengine/ark/4.1 图片生成 API.md` |
| 4.2 | 图片生成流式响应事件 | 523-526 | 22748-22882 | 124 | `chapters/volcengine/ark/4.2 图片生成流式响应事件.md` |
| 5.1.1 | 创建智能体 | 527-540 | 22885-23512 | 477 | `chapters/volcengine/ark/5.1.1 创建智能体.md` |
| 5.1.2 | 查询智能体列表 | 541-548 | 23513-23845 | 274 | `chapters/volcengine/ark/5.1.2 查询智能体列表.md` |
| 5.1.3 | 查询智能体详情 | 549-555 | 23846-24132 | 232 | `chapters/volcengine/ark/5.1.3 查询智能体详情.md` |
| 5.1.4 | 更新智能体 | 556-570 | 24133-24812 | 499 | `chapters/volcengine/ark/5.1.4 更新智能体.md` |
| 5.1.5 | 查询智能体版本列表 | 571-577 | 24813-25120 | 250 | `chapters/volcengine/ark/5.1.5 查询智能体版本列表.md` |
| 5.1.6 | 归档智能体 | 578-584 | 25121-25410 | 235 | `chapters/volcengine/ark/5.1.6 归档智能体.md` |
| 5.1.7 | 删除智能体 | 585 | 25411-25434 | 16 | `chapters/volcengine/ark/5.1.7 删除智能体.md` |
| 5.2.1 | 创建环境 | 586-592 | 25436-25723 | 215 | `chapters/volcengine/ark/5.2.1 创建环境.md` |
| 5.2.2 | 查询环境列表 | 593-596 | 25724-25873 | 129 | `chapters/volcengine/ark/5.2.2 查询环境列表.md` |
| 5.2.3 | 查询环境详情 | 597-600 | 25874-25999 | 104 | `chapters/volcengine/ark/5.2.3 查询环境详情.md` |
| 5.2.4 | 更新环境 | 601-608 | 26000-26323 | 232 | `chapters/volcengine/ark/5.2.4 更新环境.md` |
| 5.2.5 | 归档环境 | 609-612 | 26324-26450 | 104 | `chapters/volcengine/ark/5.2.5 归档环境.md` |
| 5.2.6 | 删除环境 | 613 | 26451-26475 | 16 | `chapters/volcengine/ark/5.2.6 删除环境.md` |
| 5.2.7.1 | 长轮询拉取待执行 Work | 614-616 | 26477-26583 | 77 | `chapters/volcengine/ark/5.2.7.1 长轮询拉取待执行 Work.md` |
| 5.2.7.2 | 认领 Work | 617-619 | 26584-26671 | 64 | `chapters/volcengine/ark/5.2.7.2 认领 Work.md` |
| 5.2.7.3 | 续租 Work | 620-621 | 26672-26738 | 47 | `chapters/volcengine/ark/5.2.7.3 续租 Work.md` |
| 5.2.7.4 | 查询 Work 队列状态 | 622 | 26739-26771 | 23 | `chapters/volcengine/ark/5.2.7.4 查询 Work 队列状态.md` |
| 5.2.7.5 | 停止 Work | 623-625 | 26772-26876 | 75 | `chapters/volcengine/ark/5.2.7.5 停止 Work.md` |
| 5.2.7.6 | 查询 Work 列表 | 626-628 | 26877-26984 | 86 | `chapters/volcengine/ark/5.2.7.6 查询 Work 列表.md` |
| 5.2.7.7 | 查询 Work 详情 | 629-630 | 26985-27057 | 54 | `chapters/volcengine/ark/5.2.7.7 查询 Work 详情.md` |
| 5.3.1 | 创建会话 | 631-664 | 27059-28535 | 1190 | `chapters/volcengine/ark/5.3.1 创建会话.md` |
| 5.3.2 | 查询会话列表 | 665-686 | 28536-29469 | 796 | `chapters/volcengine/ark/5.3.2 查询会话列表.md` |
| 5.3.3 | 查询会话详情 | 687-707 | 29470-30390 | 789 | `chapters/volcengine/ark/5.3.3 查询会话详情.md` |
| 5.3.4 | 更新会话标题和标签 | 708-728 | 30391-31282 | 758 | `chapters/volcengine/ark/5.3.4 更新会话标题和标签.md` |
| 5.3.5 | 升级会话 | 729-756 | 31283-32502 | 1010 | `chapters/volcengine/ark/5.3.5 升级会话.md` |
| 5.3.6 | 归档会话 | 757-778 | 32503-33434 | 792 | `chapters/volcengine/ark/5.3.6 归档会话.md` |
| 5.3.7 | 删除会话 | 779 | 33435-33461 | 19 | `chapters/volcengine/ark/5.3.7 删除会话.md` |
| 5.3.8.1 | 查询会话任务 | 780-784 | 33463-33650 | 156 | `chapters/volcengine/ark/5.3.8.1 查询会话任务.md` |
| 5.3.8.2 | 查询会话任务列表 | 785-787 | 33651-33764 | 88 | `chapters/volcengine/ark/5.3.8.2 查询会话任务列表.md` |
| 5.3.8.3 | 取消会话任务 | 788-789 | 33765-33823 | 31 | `chapters/volcengine/ark/5.3.8.3 取消会话任务.md` |
| 5.3.9.1 | 发送会话事件 | 790-791 | 33825-33889 | 42 | `chapters/volcengine/ark/5.3.9.1 发送会话事件.md` |
| 5.3.9.2 | 查询会话事件列表 | 792-794 | 33890-33976 | 58 | `chapters/volcengine/ark/5.3.9.2 查询会话事件列表.md` |
| 5.3.9.3 | 流式获取会话事件 | 795-796 | 33977-34052 | 41 | `chapters/volcengine/ark/5.3.9.3 流式获取会话事件.md` |
| 5.3.9.4 | 会话事件结构参考 - 第1部分 | 797-846 | 34053-36028 | 1787 | `chapters/volcengine/ark/5.3.9.4 会话事件结构参考 - 第1部分.md` |
| 5.3.10.1 | 添加会话资源 | 847-848 | 36030-36082 | 41 | `chapters/volcengine/ark/5.3.10.1 添加会话资源.md` |
| 5.3.10.2 | 查询会话资源列表 | 849-851 | 36083-36195 | 100 | `chapters/volcengine/ark/5.3.10.2 查询会话资源列表.md` |
| 5.3.10.3 | 查询会话资源 | 852-853 | 36196-36240 | 36 | `chapters/volcengine/ark/5.3.10.3 查询会话资源.md` |
| 5.3.11.1 | 查询线程列表 | 854-857 | 36242-36371 | 104 | `chapters/volcengine/ark/5.3.11.1 查询线程列表.md` |
| 5.3.11.2 | 查询线程详情 | 858-860 | 36372-36469 | 79 | `chapters/volcengine/ark/5.3.11.2 查询线程详情.md` |
| 5.3.11.3 | 查询线程事件列表 | 861-862 | 36470-36532 | 47 | `chapters/volcengine/ark/5.3.11.3 查询线程事件列表.md` |
| 5.3.11.4 | 流式获取线程事件 | 863-864 | 36533-36581 | 30 | `chapters/volcengine/ark/5.3.11.4 流式获取线程事件.md` |
| 5.4.1 | 创建 Webhook 接入点 | 865-867 | 36583-36682 | 61 | `chapters/volcengine/ark/5.4.1 创建 Webhook 接入点.md` |
| 5.4.2 | 查询 Webhook 接入点列表 | 868-870 | 36683-36780 | 66 | `chapters/volcengine/ark/5.4.2 查询 Webhook 接入点列表.md` |
| 5.4.3 | 查询 Webhook 接入点详情 | 871-872 | 36781-36859 | 51 | `chapters/volcengine/ark/5.4.3 查询 Webhook 接入点详情.md` |
| 5.4.4 | 更新 Webhook 接入点 | 873-875 | 36860-36959 | 59 | `chapters/volcengine/ark/5.4.4 更新 Webhook 接入点.md` |
| 5.4.5 | 启用 Webhook 接入点 | 876-877 | 36960-37040 | 51 | `chapters/volcengine/ark/5.4.5 启用 Webhook 接入点.md` |
| 5.4.6 | 删除 Webhook 接入点 | 878 | 37041-37060 | 15 | `chapters/volcengine/ark/5.4.6 删除 Webhook 接入点.md` |
| 5.4.7 | 停用 Webhook 接入点 | 879-880 | 37061-37142 | 51 | `chapters/volcengine/ark/5.4.7 停用 Webhook 接入点.md` |
| 5.4.8 | 重置 Webhook 签名密钥 | 881 | 37143-37166 | 16 | `chapters/volcengine/ark/5.4.8 重置 Webhook 签名密钥.md` |
| 5.4.9 | 发送 Webhook 测试事件 | 882 | 37167-37199 | 26 | `chapters/volcengine/ark/5.4.9 发送 Webhook 测试事件.md` |
| 5.4.10 | 查询 Webhook 事件详情 | 883-884 | 37200-37259 | 46 | `chapters/volcengine/ark/5.4.10 查询 Webhook 事件详情.md` |
| 5.4.11 | 查询 Webhook 事件列表 | 885-887 | 37260-37347 | 64 | `chapters/volcengine/ark/5.4.11 查询 Webhook 事件列表.md` |
| 5.4.12 | Webhook 事件结构参考 | 888-902 | 37348-37917 | 519 | `chapters/volcengine/ark/5.4.12 Webhook 事件结构参考.md` |
| 5.5.1 | 创建保管库 | 903-904 | 37919-37965 | 36 | `chapters/volcengine/ark/5.5.1 创建保管库.md` |
| 5.5.2 | 查询保管库列表 | 905-906 | 37966-38043 | 60 | `chapters/volcengine/ark/5.5.2 查询保管库列表.md` |
| 5.5.3 | 查询保管库详情 | 907 | 38044-38076 | 28 | `chapters/volcengine/ark/5.5.3 查询保管库详情.md` |
| 5.5.4 | 更新保管库 | 908-909 | 38077-38124 | 37 | `chapters/volcengine/ark/5.5.4 更新保管库.md` |
| 5.5.5 | 删除保管库 | 910 | 38125-38149 | 21 | `chapters/volcengine/ark/5.5.5 删除保管库.md` |
| 5.5.6.1 | 创建凭证 | 911-920 | 38151-38620 | 364 | `chapters/volcengine/ark/5.5.6.1 创建凭证.md` |
| 5.5.6.2 | 查询凭证列表 | 921-925 | 38621-38844 | 185 | `chapters/volcengine/ark/5.5.6.2 查询凭证列表.md` |
| 5.5.6.3 | 查询凭证详情 | 926-930 | 38845-39042 | 163 | `chapters/volcengine/ark/5.5.6.3 查询凭证详情.md` |
| 5.5.6.4 | 更新凭证 | 931-940 | 39043-39486 | 340 | `chapters/volcengine/ark/5.5.6.4 更新凭证.md` |
| 5.5.6.5 | 删除凭证 | 941 | 39487-39513 | 21 | `chapters/volcengine/ark/5.5.6.5 删除凭证.md` |
| 5.6.1 | 创建记忆库 | 942-944 | 39515-39594 | 61 | `chapters/volcengine/ark/5.6.1 创建记忆库.md` |
| 5.6.2 | 查询记忆库列表 | 945-947 | 39595-39697 | 80 | `chapters/volcengine/ark/5.6.2 查询记忆库列表.md` |
| 5.6.3 | 查询记忆库详情 | 948-949 | 39698-39759 | 47 | `chapters/volcengine/ark/5.6.3 查询记忆库详情.md` |
| 5.6.4 | 更新记忆库 | 950-952 | 39760-39840 | 61 | `chapters/volcengine/ark/5.6.4 更新记忆库.md` |
| 5.6.5 | 删除记忆库 | 953 | 39841-39866 | 17 | `chapters/volcengine/ark/5.6.5 删除记忆库.md` |
| 5.6.6.1 | 创建记忆 | 954-955 | 39868-39932 | 51 | `chapters/volcengine/ark/5.6.6.1 创建记忆.md` |
| 5.6.6.2 | 批量创建记忆 | 956-958 | 39933-40050 | 90 | `chapters/volcengine/ark/5.6.6.2 批量创建记忆.md` |
| 5.6.6.3 | 查询记忆列表 | 959-961 | 40051-40144 | 70 | `chapters/volcengine/ark/5.6.6.3 查询记忆列表.md` |
| 5.6.6.4 | 查询记忆详情 | 962-963 | 40145-40203 | 45 | `chapters/volcengine/ark/5.6.6.4 查询记忆详情.md` |
| 5.6.6.5 | 更新记忆 | 964-965 | 40204-40276 | 51 | `chapters/volcengine/ark/5.6.6.5 更新记忆.md` |
| 5.6.6.6 | 删除记忆 | 966 | 40277-40305 | 18 | `chapters/volcengine/ark/5.6.6.6 删除记忆.md` |
| 5.7.1 | 创建 Dream | 967-970 | 40307-40431 | 108 | `chapters/volcengine/ark/5.7.1 创建 Dream.md` |
| 5.7.2 | 查询 Dream 列表 | 971-974 | 40432-40569 | 119 | `chapters/volcengine/ark/5.7.2 查询 Dream 列表.md` |
| 5.7.3 | 查询 Dream | 975-977 | 40570-40665 | 83 | `chapters/volcengine/ark/5.7.3 查询 Dream.md` |
| 5.7.4 | 取消 Dream | 978-980 | 40666-40764 | 84 | `chapters/volcengine/ark/5.7.4 取消 Dream.md` |
| 5.8.1 | 创建技能 | 981-982 | 40766-40834 | 49 | `chapters/volcengine/ark/5.8.1 创建技能.md` |
| 5.8.2 | 查询技能列表 | 983-984 | 40835-40909 | 61 | `chapters/volcengine/ark/5.8.2 查询技能列表.md` |
| 5.8.3 | 查询技能详情 | 985-986 | 40910-40955 | 36 | `chapters/volcengine/ark/5.8.3 查询技能详情.md` |
| 5.8.4 | 设置技能内容保护 | 987-988 | 40956-41001 | 37 | `chapters/volcengine/ark/5.8.4 设置技能内容保护.md` |
| 5.8.5 | 删除技能 | 989 | 41002-41027 | 18 | `chapters/volcengine/ark/5.8.5 删除技能.md` |
| 5.8.6 | 创建新版本的技能 | 990-991 | 41028-41087 | 41 | `chapters/volcengine/ark/5.8.6 创建新版本的技能.md` |
| 5.8.7 | 查询技能的版本列表 | 992-993 | 41088-41143 | 48 | `chapters/volcengine/ark/5.8.7 查询技能的版本列表.md` |
| 5.8.8 | 查询指定版本的技能 | 994 | 41144-41173 | 26 | `chapters/volcengine/ark/5.8.8 查询指定版本的技能.md` |
| 5.8.9 | 删除指定版本的技能 | 995 | 41174-41195 | 17 | `chapters/volcengine/ark/5.8.9 删除指定版本的技能.md` |
| 5.8.10 | 下载指定版本的技能 | 996 | 41196-41214 | 14 | `chapters/volcengine/ark/5.8.10 下载指定版本的技能.md` |
| 5.8.11 | 扫描 GitHub 技能 | 997-998 | 41215-41267 | 43 | `chapters/volcengine/ark/5.8.11 扫描 GitHub 技能.md` |
| 5.8.12 | 导入 GitHub 技能 | 999-1000 | 41268-41343 | 58 | `chapters/volcengine/ark/5.8.12 导入 GitHub 技能.md` |
| 5.9.1 | 创建 Deployment | 1001-1006 | 41345-41583 | 197 | `chapters/volcengine/ark/5.9.1 创建 Deployment.md` |
| 5.9.2 | 更新 Deployment | 1007-1012 | 41584-41826 | 201 | `chapters/volcengine/ark/5.9.2 更新 Deployment.md` |
| 5.9.3 | 查询 Deployment 详情 | 1013-1016 | 41827-41965 | 116 | `chapters/volcengine/ark/5.9.3 查询 Deployment 详情.md` |
| 5.9.4 | 查询 Deployment 列表 | 1017-1021 | 41966-42145 | 152 | `chapters/volcengine/ark/5.9.4 查询 Deployment 列表.md` |
| 5.9.5 | 恢复 Deployment | 1022-1025 | 42146-42286 | 116 | `chapters/volcengine/ark/5.9.5 恢复 Deployment.md` |
| 5.9.6 | 暂停 Deployment | 1026-1029 | 42287-42426 | 117 | `chapters/volcengine/ark/5.9.6 暂停 Deployment.md` |
| 5.9.7 | 归档 Deployment | 1030-1033 | 42427-42566 | 116 | `chapters/volcengine/ark/5.9.7 归档 Deployment.md` |
| 5.9.8 | 立即运行 Deployment | 1034-1035 | 42567-42623 | 47 | `chapters/volcengine/ark/5.9.8 立即运行 Deployment.md` |
| 5.9.9 | 查询 Deployment Run 列表 | 1036-1038 | 42624-42712 | 71 | `chapters/volcengine/ark/5.9.9 查询 Deployment Run 列表.md` |
| 5.9.10 | 查询 Deployment Run 详情 | 1039-1040 | 42713-42769 | 46 | `chapters/volcengine/ark/5.9.10 查询 Deployment Run 详情.md` |
| 6.1 | 上传文件 | 1041-1046 | 42771-42996 | 165 | `chapters/volcengine/ark/6.1 上传文件.md` |
| 6.2 | 查询文件详情 | 1047-1049 | 42997-43080 | 67 | `chapters/volcengine/ark/6.2 查询文件详情.md` |
| 6.3 | 查询文件列表 | 1050-1053 | 43081-43225 | 116 | `chapters/volcengine/ark/6.3 查询文件列表.md` |
| 6.4 | 删除文件 | 1054 | 43226-43248 | 19 | `chapters/volcengine/ark/6.4 删除文件.md` |
| 6.5 | The file object | 1055-1057 | 43249-43320 | 57 | `chapters/volcengine/ark/6.5 The file object.md` |
| 7.1 | Models API | 1058-1061 | 43322-43455 | 123 | `chapters/volcengine/ark/7.1 Models API.md` |
| 8.1 | System One API（beta） | 1062-1069 | 43457-43729 | 240 | `chapters/volcengine/ark/8.1 System One API（beta）.md` |
| 9.1.1 | 创建 3D 生成任务 API | 1070-1072 | 43732-43836 | 79 | `chapters/volcengine/ark/9.1.1 创建 3D 生成任务 API.md` |
| 9.1.2 | 查询 3D 生成任务 API | 1073-1074 | 43837-43906 | 52 | `chapters/volcengine/ark/9.1.2 查询 3D 生成任务 API.md` |
| 9.1.3 | 查询 3D 生成任务列表 | 1075-1077 | 43907-44020 | 87 | `chapters/volcengine/ark/9.1.3 查询 3D 生成任务列表.md` |
| 9.1.4 | 取消或删除 3D 生成任务 | 1078 | 44021-44062 | 38 | `chapters/volcengine/ark/9.1.4 取消或删除 3D 生成任务.md` |
| 9.2.1 | 创建 3D 生成任务 | 1079-1083 | 44064-44278 | 148 | `chapters/volcengine/ark/9.2.1 创建 3D 生成任务.md` |
| 9.2.2 | 查询 3D 生成任务 | 1084-1085 | 44279-44344 | 48 | `chapters/volcengine/ark/9.2.2 查询 3D 生成任务.md` |
| 9.2.3 | 查询 3D 生成任务列表 | 1086-1088 | 44345-44452 | 81 | `chapters/volcengine/ark/9.2.3 查询 3D 生成任务列表.md` |
| 9.2.4 | 取消或删除 3D 生成任务 | 1089 | 44453-44487 | 31 | `chapters/volcengine/ark/9.2.4 取消或删除 3D 生成任务.md` |
| 9.3.1 | 创建 3D 生成任务 | 1090-1093 | 44489-44620 | 95 | `chapters/volcengine/ark/9.3.1 创建 3D 生成任务.md` |
| 9.3.2 | 查询 3D 生成任务 | 1094-1095 | 44621-44686 | 48 | `chapters/volcengine/ark/9.3.2 查询 3D 生成任务.md` |
| 9.3.3 | 查询 3D 生成任务列表 | 1096-1098 | 44687-44794 | 81 | `chapters/volcengine/ark/9.3.3 查询 3D 生成任务列表.md` |
| 9.3.4 | 取消或删除 3D 生成任务 | 1099 | 44795-44829 | 31 | `chapters/volcengine/ark/9.3.4 取消或删除 3D 生成任务.md` |
| 10.1 | 多模态向量化 API | 1100-1104 | 44831-45029 | 147 | `chapters/volcengine/ark/10.1 多模态向量化 API.md` |
| 11.1 | 分词 API | 1105-1106 | 45031-45077 | 39 | `chapters/volcengine/ark/11.1 分词 API.md` |
| 12.1.1 | 获取临时 API Key | 1107 | 45080-45114 | 26 | `chapters/volcengine/ark/12.1.1 获取临时 API Key.md` |
| 12.2.1 | 创建个人版套餐 | 1108-1109 | 45116-45174 | 34 | `chapters/volcengine/ark/12.2.1 创建个人版套餐.md` |
| 12.2.2 | 续费个人版套餐 | 1110-1111 | 45175-45220 | 27 | `chapters/volcengine/ark/12.2.2 续费个人版套餐.md` |
| 12.2.3 | 查询个人版套餐 | 1112 | 45221-45248 | 21 | `chapters/volcengine/ark/12.2.3 查询个人版套餐.md` |
| 12.2.4.1 | 查询 Agent Plan 支持的模型列表 | 1113 | 45250-45269 | 14 | `chapters/volcengine/ark/12.2.4.1 查询 Agent Plan 支持的模型列表.md` |
| 12.2.4.2 | 轮换个人版 API Key | 1114 | 45270-45296 | 17 | `chapters/volcengine/ark/12.2.4.2 轮换个人版 API Key.md` |
| 12.2.4.3 | 获取套餐 AFP 额度 | 1115-1116 | 45297-45371 | 66 | `chapters/volcengine/ark/12.2.4.3 获取套餐 AFP 额度.md` |
| 12.2.4.4 | 获取套餐用量详情 | 1117-1118 | 45372-45420 | 39 | `chapters/volcengine/ark/12.2.4.4 获取套餐用量详情.md` |
| 12.2.5.1 | 查询 Coding Plan 支持的模型列表 | 1119 | 45422-45437 | 12 | `chapters/volcengine/ark/12.2.5.1 查询 Coding Plan 支持的模型列表.md` |
| 12.2.6.1 | 创建企业版席位 | 1120-1121 | 45439-45510 | 44 | `chapters/volcengine/ark/12.2.6.1 创建企业版席位.md` |
| 12.2.6.2 | 续费企业版席位 | 1122-1123 | 45511-45549 | 29 | `chapters/volcengine/ark/12.2.6.2 续费企业版席位.md` |
| 12.2.6.3 | 批量绑定企业版席位 | 1124-1125 | 45550-45593 | 32 | `chapters/volcengine/ark/12.2.6.3 批量绑定企业版席位.md` |
| 12.2.6.4 | 批量更新企业版席位 API Key | 1126 | 45594-45627 | 25 | `chapters/volcengine/ark/12.2.6.4 批量更新企业版席位 API Key.md` |
| 12.2.6.5 | 获取单个/多个席位的 AFP 额度用量 | 1127-1129 | 45628-45719 | 80 | `chapters/volcengine/ark/12.2.6.5 获取单个-多个席位的 AFP 额度用量.md` |
| 12.2.6.6 | 查询席位 AFP 额度用量列表 | 1130-1133 | 45720-45853 | 114 | `chapters/volcengine/ark/12.2.6.6 查询席位 AFP 额度用量列表.md` |
| 12.2.6.7 | 获取单个/多个席位的模型调用数据明细 | 1134-1135 | 45854-45922 | 58 | `chapters/volcengine/ark/12.2.6.7 获取单个-多个席位的模型调用数据明细.md` |
| 12.2.6.8 | 创建共享包 | 1136-1137 | 45923-45995 | 51 | `chapters/volcengine/ark/12.2.6.8 创建共享包.md` |
| 12.2.6.9 | 续费共享包 | 1138-1139 | 45996-46054 | 39 | `chapters/volcengine/ark/12.2.6.9 续费共享包.md` |
| 12.2.6.10 | 查询共享包订阅信息 | 1140-1141 | 46055-46117 | 47 | `chapters/volcengine/ark/12.2.6.10 查询共享包订阅信息.md` |
| 12.3.1 | 获取基础模型版本列表 | 1142-1144 | 46119-46206 | 72 | `chapters/volcengine/ark/12.3.1 获取基础模型版本列表.md` |
| 12.3.2 | 获取基础模型版本信息 | 1145-1152 | 46207-46524 | 273 | `chapters/volcengine/ark/12.3.2 获取基础模型版本信息.md` |
| 12.3.3 | 获取基础模型列表 | 1153-1157 | 46525-46777 | 186 | `chapters/volcengine/ark/12.3.3 获取基础模型列表.md` |
| 12.3.4 | 获取基础模型信息 | 1158-1160 | 46778-46902 | 93 | `chapters/volcengine/ark/12.3.4 获取基础模型信息.md` |
| 12.4.1 | 批量开通基础模型 | 1161 | 46904-46918 | 11 | `chapters/volcengine/ark/12.4.1 批量开通基础模型.md` |
| 12.4.2 | 启用自动开通新模型 | 1162 | 46919-46930 | 7 | `chapters/volcengine/ark/12.4.2 启用自动开通新模型.md` |
| 12.4.3 | 关闭自动开通新模型 | 1163 | 46931-46942 | 7 | `chapters/volcengine/ark/12.4.3 关闭自动开通新模型.md` |
| 12.4.4 | 查询模型开通详情 | 1164-1167 | 46943-47085 | 131 | `chapters/volcengine/ark/12.4.4 查询模型开通详情.md` |
| 12.4.5 | 查询模型开通列表 | 1168-1172 | 47086-47263 | 163 | `chapters/volcengine/ark/12.4.5 查询模型开通列表.md` |
| 12.4.6 | 查询模型价格 | 1173-1177 | 47264-47465 | 156 | `chapters/volcengine/ark/12.4.6 查询模型价格.md` |
| 12.5.1 | 批量开通资源 | 1178 | 47467-47485 | 14 | `chapters/volcengine/ark/12.5.1 批量开通资源.md` |
| 12.5.2 | 查询资源开通列表 | 1179-1181 | 47486-47587 | 92 | `chapters/volcengine/ark/12.5.2 查询资源开通列表.md` |
| 12.6.1 | 查询模型限流 | 1182-1184 | 47589-47688 | 91 | `chapters/volcengine/ark/12.6.1 查询模型限流.md` |
| 12.7.1 | 删除定制模型 | 1185 | 47690-47715 | 17 | `chapters/volcengine/ark/12.7.1 删除定制模型.md` |
| 12.7.2 | 获取定制模型信息 | 1186-1188 | 47716-47824 | 97 | `chapters/volcengine/ark/12.7.2 获取定制模型信息.md` |
| 12.7.3 | 更新定制模型 | 1189 | 47825-47857 | 22 | `chapters/volcengine/ark/12.7.3 更新定制模型.md` |
| 12.7.4 | 获取定制模型列表 | 1190-1192 | 47858-47976 | 102 | `chapters/volcengine/ark/12.7.4 获取定制模型列表.md` |
| 12.8.1 | 创建模型调优任务 | 1193-1200 | 47978-48296 | 281 | `chapters/volcengine/ark/12.8.1 创建模型调优任务.md` |
| 12.8.2 | 删除模型调优任务 | 1201 | 48297-48313 | 10 | `chapters/volcengine/ark/12.8.2 删除模型调优任务.md` |
| 12.8.3 | 获取模型调优任务信息 | 1202-1212 | 48314-48767 | 411 | `chapters/volcengine/ark/12.8.3 获取模型调优任务信息.md` |
| 12.8.4 | 查询精调效果指标详细数据 | 1213-1214 | 48768-48813 | 32 | `chapters/volcengine/ark/12.8.4 查询精调效果指标详细数据.md` |
| 12.8.5 | 查询精调效果指标 | 1215 | 48814-48832 | 10 | `chapters/volcengine/ark/12.8.5 查询精调效果指标.md` |
| 12.8.6 | 获取模型调优任务列表 | 1216-1222 | 48833-49103 | 246 | `chapters/volcengine/ark/12.8.6 获取模型调优任务列表.md` |
| 12.8.7 | 重试模型调优任务 | 1223 | 49104-49120 | 9 | `chapters/volcengine/ark/12.8.7 重试模型调优任务.md` |
| 12.8.8 | 停止模型调优任务 | 1224 | 49121-49137 | 10 | `chapters/volcengine/ark/12.8.8 停止模型调优任务.md` |
| 12.8.9 | 更新模型调优任务 | 1225 | 49138-49161 | 14 | `chapters/volcengine/ark/12.8.9 更新模型调优任务.md` |
| 12.9.1 | 开启推理接入点 | 1226 | 49163-49183 | 13 | `chapters/volcengine/ark/12.9.1 开启推理接入点.md` |
| 12.9.2 | 停止推理接入点 | 1227 | 49184-49204 | 11 | `chapters/volcengine/ark/12.9.2 停止推理接入点.md` |
| 12.9.3 | 获取推理接入点列表 | 1228-1232 | 49205-49416 | 170 | `chapters/volcengine/ark/12.9.3 获取推理接入点列表.md` |
| 12.9.4 | 获取推理接入点 | 1233-1235 | 49417-49518 | 88 | `chapters/volcengine/ark/12.9.4 获取推理接入点.md` |
| 12.9.5 | 删除推理接入点 | 1236 | 49519-49538 | 12 | `chapters/volcengine/ark/12.9.5 删除推理接入点.md` |
| 12.9.6 | 更新推理接入点 | 1237-1241 | 49539-49723 | 160 | `chapters/volcengine/ark/12.9.6 更新推理接入点.md` |
| 12.9.7 | 创建推理接入点 | 1242-1247 | 49724-49951 | 193 | `chapters/volcengine/ark/12.9.7 创建推理接入点.md` |
| 12.9.8 | 获取接入点推理应用层加密证书 | 1248-1249 | 49952-49987 | 23 | `chapters/volcengine/ark/12.9.8 获取接入点推理应用层加密证书.md` |
| 12.9.9 | 创建推理接入点滚动升级任务 | 1250-1251 | 49988-50035 | 41 | `chapters/volcengine/ark/12.9.9 创建推理接入点滚动升级任务.md` |
| 12.9.10 | 查询推理接入点滚动升级详情 | 1252-1255 | 50036-50162 | 116 | `chapters/volcengine/ark/12.9.10 查询推理接入点滚动升级详情.md` |
| 12.9.11 | 回滚推理接入点滚动升级 | 1256 | 50163-50180 | 13 | `chapters/volcengine/ark/12.9.11 回滚推理接入点滚动升级.md` |
| 12.9.12 | 取消推理接入点滚动升级 | 1257 | 50181-50198 | 13 | `chapters/volcengine/ark/12.9.12 取消推理接入点滚动升级.md` |
| 12.10.1 | 创建批量推理任务 | 1258-1259 | 50200-50276 | 59 | `chapters/volcengine/ark/12.10.1 创建批量推理任务.md` |
| 12.10.2 | 获取批量推理任务列表 | 1260-1264 | 50277-50450 | 152 | `chapters/volcengine/ark/12.10.2 获取批量推理任务列表.md` |
| 12.10.3 | 获取批量推理任务 | 1265-1267 | 50451-50568 | 102 | `chapters/volcengine/ark/12.10.3 获取批量推理任务.md` |
| 12.10.4 | 更新批量推理任务 | 1268 | 50569-50592 | 17 | `chapters/volcengine/ark/12.10.4 更新批量推理任务.md` |
| 12.10.5 | 删除批量推理任务 | 1269 | 50593-50612 | 13 | `chapters/volcengine/ark/12.10.5 删除批量推理任务.md` |
| 12.10.6 | 停止批量推理任务 | 1270 | 50613-50635 | 16 | `chapters/volcengine/ark/12.10.6 停止批量推理任务.md` |
| 12.10.7 | 重启批量推理任务 | 1271 | 50636-50656 | 13 | `chapters/volcengine/ark/12.10.7 重启批量推理任务.md` |
| 12.11.1 | 创建评测任务 | 1272-1275 | 50658-50823 | 133 | `chapters/volcengine/ark/12.11.1 创建评测任务.md` |
| 12.11.2 | 删除评测任务 | 1276 | 50824-50845 | 13 | `chapters/volcengine/ark/12.11.2 删除评测任务.md` |
| 12.11.3 | 获取评测任务 | 1277-1279 | 50846-50927 | 66 | `chapters/volcengine/ark/12.11.3 获取评测任务.md` |
| 12.11.4 | 获取评测任务结果 | 1280-1282 | 50928-51030 | 87 | `chapters/volcengine/ark/12.11.4 获取评测任务结果.md` |
| 12.11.5 | 获取评测任务列表 | 1283-1286 | 51031-51177 | 129 | `chapters/volcengine/ark/12.11.5 获取评测任务列表.md` |
| 12.11.6 | 获取评测任务结果列表 | 1287-1290 | 51178-51319 | 120 | `chapters/volcengine/ark/12.11.6 获取评测任务结果列表.md` |
| 12.11.7 | 停止评测任务 | 1291 | 51320-51341 | 13 | `chapters/volcengine/ark/12.11.7 停止评测任务.md` |
| 12.11.8 | 更新评测任务 | 1292 | 51342-51367 | 18 | `chapters/volcengine/ark/12.11.8 更新评测任务.md` |
| 12.12.1 | 查询推理用量 | 1293-1295 | 51369-51496 | 75 | `chapters/volcengine/ark/12.12.1 查询推理用量.md` |
| 12.12.2 | 查询单请求用量 | 1296-1299 | 51497-51635 | 124 | `chapters/volcengine/ark/12.12.2 查询单请求用量.md` |
| 12.12.3 | 查询异步任务用量 | 1300-1301 | 51636-51706 | 62 | `chapters/volcengine/ark/12.12.3 查询异步任务用量.md` |
| 12.12.4 | 创建用量明细导出任务 | 1302-1303 | 51707-51761 | 33 | `chapters/volcengine/ark/12.12.4 创建用量明细导出任务.md` |
| 12.12.5 | 查询用量明细导出任务状态 | 1304-1306 | 51762-51864 | 71 | `chapters/volcengine/ark/12.12.5 查询用量明细导出任务状态.md` |
| 12.12.6 | 查询模型推理限额 | 1307 | 51865-51892 | 22 | `chapters/volcengine/ark/12.12.6 查询模型推理限额.md` |
| 12.12.7 | 开启模型推理限额 | 1308 | 51893-51917 | 16 | `chapters/volcengine/ark/12.12.7 开启模型推理限额.md` |
| 12.12.8 | 关闭模型推理限额 | 1309 | 51918-51938 | 12 | `chapters/volcengine/ark/12.12.8 关闭模型推理限额.md` |
| 12.13.1 | 创建方舟官方模型产物查询请求 | 1310 | 51940-51958 | 14 | `chapters/volcengine/ark/12.13.1 创建方舟官方模型产物查询请求.md` |
| 12.13.2 | 获取安全审计日志 | 1311-1313 | 51959-52078 | 85 | `chapters/volcengine/ark/12.13.2 获取安全审计日志.md` |
| 12.13.3 | 获取方舟官方产物确认结果 | 1314 | 52079-52108 | 24 | `chapters/volcengine/ark/12.13.3 获取方舟官方产物确认结果.md` |
| 12.14.1 | 上报视频生成模型效果问题 | 1315-1324 | 52110-52560 | 344 | `chapters/volcengine/ark/12.14.1 上报视频生成模型效果问题.md` |
| 12.14.2 | 查询视频生成模型效果问题结果 | 1325-1330 | 52561-52770 | 163 | `chapters/volcengine/ark/12.14.2 查询视频生成模型效果问题结果.md` |
| 12.14.3 | 上报大语言模型效果问题 | 1331-1333 | 52771-52889 | 87 | `chapters/volcengine/ark/12.14.3 上报大语言模型效果问题.md` |
| 12.14.4 | 查询大语言模型效果问题结果 | 1334-1337 | 52890-53017 | 102 | `chapters/volcengine/ark/12.14.4 查询大语言模型效果问题结果.md` |
| 12.14.5 | 上报 3D 生成效果问题 | 1338-1342 | 53018-53201 | 134 | `chapters/volcengine/ark/12.14.5 上报 3D 生成效果问题.md` |
| 12.14.6 | 查询 3D 生成效果问题结果 | 1343-1347 | 53202-53396 | 152 | `chapters/volcengine/ark/12.14.6 查询 3D 生成效果问题结果.md` |
| 13.1 | 兼容 OpenAI SDK | 1348-1351 | 53398-53514 | 103 | `chapters/volcengine/ark/13.1 兼容 OpenAI SDK.md` |
| 13.2 | 向后兼容性 | 1352 | 53515-53560 | 25 | `chapters/volcengine/ark/13.2 向后兼容性.md` |
| 13.3 | 错误码 - 第1部分 | 1352-1374 | 53561-55564 | 1954 | `chapters/volcengine/ark/13.3 错误码 - 第1部分.md` |
| 13.3 | 错误码 - 第2部分·错误码 | 1375-1384 | 55565-56330 | 732 | `chapters/volcengine/ark/13.3 错误码 - 第2部分·错误码.md` |
| 13.4 | SDK 常见使用示例 | 1385-1400 | 56331-56919 | 521 | `chapters/volcengine/ark/13.4 SDK 常见使用示例.md` |
