# AI MediaKit 指南区章节表（mediakit-guide）

来源：《AI MediaKit 文档指南》（955 页）。155 个章节文件，接口级切分：一个接口/任务一个文件；超过 1500 行的按语义块自动再拆为`… - 第N部分`（2 个章节被拆分）。

「页码」是原 PDF 页码范围；「行范围」是中间 MD（`doc/<源文档>.md`）的 1 起始行号，可据此回查原文。章节文件本身已去掉页眉页脚，回查 PDF 时用这两列。文件名即章节标题，日常定位直接 Glob 文件名即可，用不到这两列。

**这张表用来 grep，不要整读。**

| 编号 | 标题 | 页码 | 行范围(源文件) | 行数 | 文件 |
|------|------|------|---------------|------|------|
| 1.1 | 功能发布历史 | 1-14 | 227-1323 | 865 | `chapters/volcengine/mediakit-guide/1.1 功能发布历史.md` |
| 1.2 | AI MediaKit 查询任务信息 API 查询范围调整公告 | 15 | 1324-1351 | 18 | `chapters/volcengine/mediakit-guide/1.2 AI MediaKit 查询任务信息 API 查询范围调整公告.md` |
| 1.3 | AI MediaKit 输入文件及输出产物存储策略调整公 | 16 | 1352-1385 | 18 | `chapters/volcengine/mediakit-guide/1.3 AI MediaKit 输入文件及输出产物存储策略调整公.md` |
| 2.1 | AI MediaKit 介绍 | 17-29 | 1387-2139 | 699 | `chapters/volcengine/mediakit-guide/2.1 AI MediaKit 介绍.md` |
| 2.2 | 快速入门：视频理解前处理 | 30-36 | 2140-2398 | 224 | `chapters/volcengine/mediakit-guide/2.2 快速入门：视频理解前处理.md` |
| 2.3 | 快速入门：视频生成后处理 | 37-40 | 2399-2523 | 87 | `chapters/volcengine/mediakit-guide/2.3 快速入门：视频生成后处理.md` |
| 2.4 | 计费说明 | 41-42 | 2524-2627 | 69 | `chapters/volcengine/mediakit-guide/2.4 计费说明.md` |
| 3.1.1 | 画质增强（大模型版） | 43-52 | 2630-2918 | 210 | `chapters/volcengine/mediakit-guide/3.1.1 画质增强（大模型版）.md` |
| 3.1.2 | 画质增强（标准版和专业版） | 53-69 | 2919-3472 | 407 | `chapters/volcengine/mediakit-guide/3.1.2 画质增强（标准版和专业版）.md` |
| 3.1.3 | 画质增强（极速版） | 70-75 | 3473-3674 | 157 | `chapters/volcengine/mediakit-guide/3.1.3 画质增强（极速版）.md` |
| 3.1.4 | 字幕擦除 | 76-91 | 3675-4125 | 314 | `chapters/volcengine/mediakit-guide/3.1.4 字幕擦除.md` |
| 3.1.5 | 视频转码 | 92-94 | 4126-4221 | 67 | `chapters/volcengine/mediakit-guide/3.1.5 视频转码.md` |
| 3.1.6 | 极智超清 | 95-97 | 4222-4333 | 81 | `chapters/volcengine/mediakit-guide/3.1.6 极智超清.md` |
| 3.1.7 | 视频暗水印 | 98-103 | 4334-4568 | 136 | `chapters/volcengine/mediakit-guide/3.1.7 视频暗水印.md` |
| 3.1.8 | 场景切分 | 104-108 | 4569-4731 | 111 | `chapters/volcengine/mediakit-guide/3.1.8 场景切分.md` |
| 3.1.9 | 智能语义切片（基础版） | 109-112 | 4732-4884 | 101 | `chapters/volcengine/mediakit-guide/3.1.9 智能语义切片（基础版）.md` |
| 3.1.10 | 语音转字幕（ASR） | 113-118 | 4885-5108 | 176 | `chapters/volcengine/mediakit-guide/3.1.10 语音转字幕（ASR）.md` |
| 3.1.11 | 视频识别字幕（OCR） | 119-123 | 5109-5304 | 145 | `chapters/volcengine/mediakit-guide/3.1.11 视频识别字幕（OCR）.md` |
| 3.1.12 | 高光智剪-短剧 | 124-138 | 5305-5841 | 379 | `chapters/volcengine/mediakit-guide/3.1.12 高光智剪-短剧.md` |
| 3.1.13 | 高光智剪-小游戏 | 139-143 | 5842-6023 | 136 | `chapters/volcengine/mediakit-guide/3.1.13 高光智剪-小游戏.md` |
| 3.1.14 | 高光智剪-影视拆条 | 144-148 | 6024-6224 | 143 | `chapters/volcengine/mediakit-guide/3.1.14 高光智剪-影视拆条.md` |
| 3.1.15 | 高光片段提取 | 149-154 | 6225-6422 | 157 | `chapters/volcengine/mediakit-guide/3.1.15 高光片段提取.md` |
| 3.1.16 | 视频抠图 | 155-159 | 6423-6583 | 110 | `chapters/volcengine/mediakit-guide/3.1.16 视频抠图.md` |
| 3.1.17 | 剧情故事线分析 | 160-165 | 6584-6893 | 223 | `chapters/volcengine/mediakit-guide/3.1.17 剧情故事线分析.md` |
| 3.1.18 | 剧本还原 | 166-175 | 6894-7361 | 396 | `chapters/volcengine/mediakit-guide/3.1.18 剧本还原.md` |
| 3.1.19 | 解说视频生成 | 176-185 | 7362-7716 | 272 | `chapters/volcengine/mediakit-guide/3.1.19 解说视频生成.md` |
| 3.1.20 | 解说视频生成（短剧行业模型） | 186-192 | 7717-7993 | 197 | `chapters/volcengine/mediakit-guide/3.1.20 解说视频生成（短剧行业模型）.md` |
| 3.1.21 | 视频抽帧 | 193-198 | 7994-8195 | 143 | `chapters/volcengine/mediakit-guide/3.1.21 视频抽帧.md` |
| 3.1.22 | 视频转封装 | 199-200 | 8196-8275 | 55 | `chapters/volcengine/mediakit-guide/3.1.22 视频转封装.md` |
| 3.1.23 | 视频画质检测 VQScore | 201-203 | 8276-8385 | 81 | `chapters/volcengine/mediakit-guide/3.1.23 视频画质检测 VQScore.md` |
| 3.1.24 | 视频人脸打码 | 204-208 | 8386-8544 | 113 | `chapters/volcengine/mediakit-guide/3.1.24 视频人脸打码.md` |
| 3.1.25 | 视频人脸融合（换脸） | 209-212 | 8545-8697 | 102 | `chapters/volcengine/mediakit-guide/3.1.25 视频人脸融合（换脸）.md` |
| 3.1.26 | 视频插帧 | 213-216 | 8698-8817 | 79 | `chapters/volcengine/mediakit-guide/3.1.26 视频插帧.md` |
| 3.1.27 | 智能语义切片（专业版） | 217-221 | 8818-9055 | 167 | `chapters/volcengine/mediakit-guide/3.1.27 智能语义切片（专业版）.md` |
| 3.1.28 | 视频口型对齐 | 222-225 | 9056-9208 | 106 | `chapters/volcengine/mediakit-guide/3.1.28 视频口型对齐.md` |
| 3.1.29 | 视频横转竖 | 226-229 | 9209-9344 | 91 | `chapters/volcengine/mediakit-guide/3.1.29 视频横转竖.md` |
| 3.1.30 | 视频流畅度提升 | 230-234 | 9345-9539 | 122 | `chapters/volcengine/mediakit-guide/3.1.30 视频流畅度提升.md` |
| 3.1.31 | 智能精准字幕识别 | 235-240 | 9540-9789 | 184 | `chapters/volcengine/mediakit-guide/3.1.31 智能精准字幕识别.md` |
| 3.1.32 | 深度动作捕捉 | 241-246 | 9790-9941 | 98 | `chapters/volcengine/mediakit-guide/3.1.32 深度动作捕捉.md` |
| 3.1.33 | 智能擦除 | 247-252 | 9942-10154 | 150 | `chapters/volcengine/mediakit-guide/3.1.33 智能擦除.md` |
| 3.2.1 | 图像画质增强 | 247-259 | 10156-10508 | 277 | `chapters/volcengine/mediakit-guide/3.2.1 图像画质增强.md` |
| 3.2.2 | 图像画质评估 | 260-263 | 10509-10667 | 117 | `chapters/volcengine/mediakit-guide/3.2.2 图像画质评估.md` |
| 3.2.3 | 图像人脸打码 | 264-267 | 10668-10820 | 121 | `chapters/volcengine/mediakit-guide/3.2.3 图像人脸打码.md` |
| 3.2.4 | 图像擦除修复 | 268-272 | 10821-11003 | 131 | `chapters/volcengine/mediakit-guide/3.2.4 图像擦除修复.md` |
| 3.2.5 | 图像背景移除（智能抠图） | 273-275 | 11004-11105 | 70 | `chapters/volcengine/mediakit-guide/3.2.5 图像背景移除（智能抠图）.md` |
| 3.2.6 | 图像智能裁剪 | 276-278 | 11106-11197 | 67 | `chapters/volcengine/mediakit-guide/3.2.6 图像智能裁剪.md` |
| 3.2.7 | 智能扩图 | 279-282 | 11198-11307 | 76 | `chapters/volcengine/mediakit-guide/3.2.7 智能扩图.md` |
| 3.2.8 | 集智瘦身 | 283-285 | 11308-11389 | 57 | `chapters/volcengine/mediakit-guide/3.2.8 集智瘦身.md` |
| 3.2.9 | 电商牛皮癣擦除 | 286-288 | 11390-11471 | 60 | `chapters/volcengine/mediakit-guide/3.2.9 电商牛皮癣擦除.md` |
| 3.2.10 | 图像基础编辑 | 289-311 | 11472-12242 | 597 | `chapters/volcengine/mediakit-guide/3.2.10 图像基础编辑.md` |
| 3.2.11 | 图像暗水印 | 312-316 | 12243-12416 | 114 | `chapters/volcengine/mediakit-guide/3.2.11 图像暗水印.md` |
| 3.3.1.1 | 智能剪辑 Vibe Editing | 317-326 | 12419-12804 | 234 | `chapters/volcengine/mediakit-guide/3.3.1.1 智能剪辑 Vibe Editing.md` |
| 3.3.1.2 | Web 智能剪辑 SDK 集成指南 - 第1部分 | 327-364 | 12805-14576 | 1538 | `chapters/volcengine/mediakit-guide/3.3.1.2 Web 智能剪辑 SDK 集成指南 - 第1部分.md` |
| 3.3.2.1 | 多轨道剪辑 | 365-404 | 14578-16125 | 1353 | `chapters/volcengine/mediakit-guide/3.3.2.1 多轨道剪辑.md` |
| 3.3.2.2 | Web 剪辑 SDK 集成指南 - 第1部分 | 405-446 | 16126-17924 | 1525 | `chapters/volcengine/mediakit-guide/3.3.2.2 Web 剪辑 SDK 集成指南 - 第1部分.md` |
| 3.3.2.3 | HyperFrames 云端渲染 | 447-450 | 17925-18081 | 110 | `chapters/volcengine/mediakit-guide/3.3.2.3 HyperFrames 云端渲染.md` |
| 3.3.2.4 | 音视频拼接 | 451-457 | 18082-18264 | 130 | `chapters/volcengine/mediakit-guide/3.3.2.4 音视频拼接.md` |
| 3.3.2.5 | 音视频裁剪 | 458-461 | 18265-18410 | 104 | `chapters/volcengine/mediakit-guide/3.3.2.5 音视频裁剪.md` |
| 3.3.2.6 | 音视频调速 | 462-465 | 18411-18514 | 71 | `chapters/volcengine/mediakit-guide/3.3.2.6 音视频调速.md` |
| 3.3.2.7 | 音频提取 | 466-469 | 18515-18636 | 84 | `chapters/volcengine/mediakit-guide/3.3.2.7 音频提取.md` |
| 3.3.2.8 | 音视频合成 | 470-474 | 18637-18830 | 140 | `chapters/volcengine/mediakit-guide/3.3.2.8 音视频合成.md` |
| 3.3.2.9 | 音频混合 | 475-478 | 18831-18944 | 79 | `chapters/volcengine/mediakit-guide/3.3.2.9 音频混合.md` |
| 3.3.2.10 | 音量调节与淡入淡出 | 479-483 | 18945-19126 | 133 | `chapters/volcengine/mediakit-guide/3.3.2.10 音量调节与淡入淡出.md` |
| 3.3.2.11 | 图片转视频 | 484-490 | 19127-19353 | 170 | `chapters/volcengine/mediakit-guide/3.3.2.11 图片转视频.md` |
| 3.3.2.12 | 视频加字幕 | 491-495 | 19354-19516 | 119 | `chapters/volcengine/mediakit-guide/3.3.2.12 视频加字幕.md` |
| 3.3.2.13 | 视频加图片 | 496-499 | 19517-19623 | 75 | `chapters/volcengine/mediakit-guide/3.3.2.13 视频加图片.md` |
| 3.3.2.14 | 视频添加滤镜 | 500-503 | 19624-19734 | 82 | `chapters/volcengine/mediakit-guide/3.3.2.14 视频添加滤镜.md` |
| 3.3.2.15 | 视频添加运镜 | 504-509 | 19735-19884 | 109 | `chapters/volcengine/mediakit-guide/3.3.2.15 视频添加运镜.md` |
| 3.3.2.16 | 视频截取动图 | 510-513 | 19885-20013 | 94 | `chapters/volcengine/mediakit-guide/3.3.2.16 视频截取动图.md` |
| 3.3.2.17 | 视频高斯模糊 | 514-518 | 20014-20156 | 102 | `chapters/volcengine/mediakit-guide/3.3.2.17 视频高斯模糊.md` |
| 3.3.2.18 | 文字生成滚屏视频 | 519-523 | 20157-20343 | 115 | `chapters/volcengine/mediakit-guide/3.3.2.18 文字生成滚屏视频.md` |
| 3.3.2.19 | 视频画面变换 | 524-529 | 20344-20489 | 103 | `chapters/volcengine/mediakit-guide/3.3.2.19 视频画面变换.md` |
| 3.3.2.20 | 添加 AIGC 元数据标识 | 530-534 | 20490-20640 | 107 | `chapters/volcengine/mediakit-guide/3.3.2.20 添加 AIGC 元数据标识.md` |
| 3.4.1 | 人声背景音分离 | 535-539 | 20642-20842 | 140 | `chapters/volcengine/mediakit-guide/3.4.1 人声背景音分离.md` |
| 3.4.2 | 语音端点识别 | 540-543 | 20843-20993 | 118 | `chapters/volcengine/mediakit-guide/3.4.2 语音端点识别.md` |
| 3.4.3 | 音频转码 | 544-548 | 20994-21169 | 125 | `chapters/volcengine/mediakit-guide/3.4.3 音频转码.md` |
| 3.4.4 | 音频内容编辑 | 549-551 | 21170-21283 | 76 | `chapters/volcengine/mediakit-guide/3.4.4 音频内容编辑.md` |
| 3.5.1 | 视频理解拓展工具 | 552-572 | 21285-22157 | 744 | `chapters/volcengine/mediakit-guide/3.5.1 视频理解拓展工具.md` |
| 3.5.2 | 视频理解智能策略 | 573-579 | 22158-22459 | 206 | `chapters/volcengine/mediakit-guide/3.5.2 视频理解智能策略.md` |
| 3.5.3 | 大模型高光剪辑 | 580-586 | 22460-22751 | 212 | `chapters/volcengine/mediakit-guide/3.5.3 大模型高光剪辑.md` |
| 3.5.4 | 通过 AI MediaKit 调用图片生成大模型 | 587-589 | 22752-22861 | 77 | `chapters/volcengine/mediakit-guide/3.5.4 通过 AI MediaKit 调用图片生成大模型.md` |
| 3.5.5 | 通过 AI MediaKit 调用视频生成大模型 | 590-592 | 22862-22978 | 84 | `chapters/volcengine/mediakit-guide/3.5.5 通过 AI MediaKit 调用视频生成大模型.md` |
| 3.5.6 | 通过 AI MediaKit 调用音频生成大模型 | 593-595 | 22979-23075 | 68 | `chapters/volcengine/mediakit-guide/3.5.6 通过 AI MediaKit 调用音频生成大模型.md` |
| 3.5.7 | 通过 AI MediaKit 调用语音识别大模型 | 596-598 | 23076-23190 | 80 | `chapters/volcengine/mediakit-guide/3.5.7 通过 AI MediaKit 调用语音识别大模型.md` |
| 3.5.8 | AIGC 视频生成质量评估 | 599-605 | 23191-23476 | 205 | `chapters/volcengine/mediakit-guide/3.5.8 AIGC 视频生成质量评估.md` |
| 3.6.1 | 多源媒体输入与本地上传 | 606-611 | 23478-23671 | 140 | `chapters/volcengine/mediakit-guide/3.6.1 多源媒体输入与本地上传.md` |
| 3.6.2 | 处理产物存储至 VOD 或 TOS | 612-616 | 23672-23849 | 102 | `chapters/volcengine/mediakit-guide/3.6.2 处理产物存储至 VOD 或 TOS.md` |
| 3.7 | 按项目或 API Key 分账 | 617-622 | 23850-24033 | 116 | `chapters/volcengine/mediakit-guide/3.7 按项目或 API Key 分账.md` |
| 3.8 | 通过子账号与项目授权实现业务间隔离 | 623-628 | 24034-24234 | 120 | `chapters/volcengine/mediakit-guide/3.8 通过子账号与项目授权实现业务间隔离.md` |
| 4.1 | AI MediaKit CLI 用户指南 | 629-648 | 24236-24938 | 566 | `chapters/volcengine/mediakit-guide/4.1 AI MediaKit CLI 用户指南.md` |
| 4.2 | AI MediaKit Skill 用户指南 | 649-658 | 24939-25263 | 223 | `chapters/volcengine/mediakit-guide/4.2 AI MediaKit Skill 用户指南.md` |
| 4.3 | AI MediaKit MCP 用户指南 | 659-680 | 25264-26405 | 1046 | `chapters/volcengine/mediakit-guide/4.3 AI MediaKit MCP 用户指南.md` |
| 5.1 | 资源包 | 681-686 | 26407-26676 | 183 | `chapters/volcengine/mediakit-guide/5.1 资源包.md` |
| 5.2 | 剪辑工具计费 | 687-689 | 26677-26783 | 73 | `chapters/volcengine/mediakit-guide/5.2 剪辑工具计费.md` |
| 5.3 | 视频工具计费 | 690-718 | 26784-28066 | 1038 | `chapters/volcengine/mediakit-guide/5.3 视频工具计费.md` |
| 5.4 | 音频工具计费 | 719-721 | 28067-28164 | 74 | `chapters/volcengine/mediakit-guide/5.4 音频工具计费.md` |
| 5.5 | 图像工具计费 | 722-725 | 28165-28313 | 97 | `chapters/volcengine/mediakit-guide/5.5 图像工具计费.md` |
| 5.6 | 大模型处理工具计费 | 726 | 28314-28324 | 4 | `chapters/volcengine/mediakit-guide/5.6 大模型处理工具计费.md` |
| 5.7 | 计费常见问题 | 727 | 28325-28359 | 18 | `chapters/volcengine/mediakit-guide/5.7 计费常见问题.md` |
| 6.1 | 常见问题 | 728-730 | 28361-28498 | 117 | `chapters/volcengine/mediakit-guide/6.1 常见问题.md` |
| 7.1 | 视频云服务专用条款 | 731-734 | 28500-28637 | 40 | `chapters/volcengine/mediakit-guide/7.1 视频云服务专用条款.md` |
| 7.2 | 智能处理服务计费结算规则 | 735-736 | 28638-28703 | 30 | `chapters/volcengine/mediakit-guide/7.2 智能处理服务计费结算规则.md` |
| 7.3 | 智能处理服务等级协议 | 737-739 | 28704-28778 | 44 | `chapters/volcengine/mediakit-guide/7.3 智能处理服务等级协议.md` |
| 8.1.1 | 概述 | 740 | 28781-28788 | 6 | `chapters/volcengine/mediakit-guide/8.1.1 概述.md` |
| 8.1.2 | 产品优势 | 741 | 28789-28803 | 9 | `chapters/volcengine/mediakit-guide/8.1.2 产品优势.md` |
| 8.1.3 | 应用场景 | 742 | 28804-28822 | 10 | `chapters/volcengine/mediakit-guide/8.1.3 应用场景.md` |
| 8.1.4 | 产品功能 | 743 | 28823-28845 | 14 | `chapters/volcengine/mediakit-guide/8.1.4 产品功能.md` |
| 8.1.5.1 | 老片修复 | 744-745 | 28847-28890 | 23 | `chapters/volcengine/mediakit-guide/8.1.5.1 老片修复.md` |
| 8.1.5.2 | 大模型视频预处理解决方案 | 746 | 28891-28919 | 12 | `chapters/volcengine/mediakit-guide/8.1.5.2 大模型视频预处理解决方案.md` |
| 8.2.1 | 计费概述 | 747-748 | 28921-28946 | 16 | `chapters/volcengine/mediakit-guide/8.2.1 计费概述.md` |
| 8.2.2.1 | 按量计费 | 749-757 | 28948-29182 | 199 | `chapters/volcengine/mediakit-guide/8.2.2.1 按量计费.md` |
| 8.2.2.2 | 资源包 | 758 | 29183-29219 | 23 | `chapters/volcengine/mediakit-guide/8.2.2.2 资源包.md` |
| 8.3.1 | 快速入门 | 759-768 | 29221-29374 | 97 | `chapters/volcengine/mediakit-guide/8.3.1 快速入门.md` |
| 8.4.1 | 控制台简介 | 769-772 | 29376-29453 | 66 | `chapters/volcengine/mediakit-guide/8.4.1 控制台简介.md` |
| 8.4.2 | 概览 | 773-777 | 29454-29525 | 36 | `chapters/volcengine/mediakit-guide/8.4.2 概览.md` |
| 8.4.3 | 任务管理 | 778-781 | 29526-29636 | 74 | `chapters/volcengine/mediakit-guide/8.4.3 任务管理.md` |
| 8.4.4 | 自动任务触发器 | 782-785 | 29637-29696 | 41 | `chapters/volcengine/mediakit-guide/8.4.4 自动任务触发器.md` |
| 8.4.5.1 | 功能概述 | 786-787 | 29698-29786 | 52 | `chapters/volcengine/mediakit-guide/8.4.5.1 功能概述.md` |
| 8.4.5.2.1 | 基础转码 | 788-802 | 29788-30255 | 388 | `chapters/volcengine/mediakit-guide/8.4.5.2.1 基础转码.md` |
| 8.4.5.2.2 | 极智超清 | 803-811 | 30256-30451 | 149 | `chapters/volcengine/mediakit-guide/8.4.5.2.2 极智超清.md` |
| 8.4.5.3.1 | 精细化擦除 | 812-818 | 30453-30541 | 56 | `chapters/volcengine/mediakit-guide/8.4.5.3.1 精细化擦除.md` |
| 8.4.5.4.1 | 画质检测修复 | 819-826 | 30543-30696 | 113 | `chapters/volcengine/mediakit-guide/8.4.5.4.1 画质检测修复.md` |
| 8.4.5.4.2 | 画质增强 | 827-833 | 30697-30795 | 59 | `chapters/volcengine/mediakit-guide/8.4.5.4.2 画质增强.md` |
| 8.4.5.5.1 | 智能识别剪切 | 834-838 | 30797-30865 | 43 | `chapters/volcengine/mediakit-guide/8.4.5.5.1 智能识别剪切.md` |
| 8.4.5.5.2 | 智能表情合成 | 839-847 | 30866-30993 | 82 | `chapters/volcengine/mediakit-guide/8.4.5.5.2 智能表情合成.md` |
| 8.4.5.5.3 | 智能抠图 | 848-854 | 30994-31071 | 51 | `chapters/volcengine/mediakit-guide/8.4.5.5.3 智能抠图.md` |
| 8.4.6 | 工作流模板 | 855-863 | 31072-31353 | 174 | `chapters/volcengine/mediakit-guide/8.4.6 工作流模板.md` |
| 8.4.7.1 | 统计数据 | 864-870 | 31355-31491 | 59 | `chapters/volcengine/mediakit-guide/8.4.7.1 统计数据.md` |
| 8.4.8 | 系统配置 | 871-873 | 31492-31548 | 38 | `chapters/volcengine/mediakit-guide/8.4.8 系统配置.md` |
| 8.4.9 | 媒体处理输出文件路径 | 874-875 | 31549-31588 | 33 | `chapters/volcengine/mediakit-guide/8.4.9 媒体处理输出文件路径.md` |
| 8.5.1 | 使用说明 | 876 | 31590-31624 | 24 | `chapters/volcengine/mediakit-guide/8.5.1 使用说明.md` |
| 8.5.2.1 | 安装 | 877 | 31626-31642 | 12 | `chapters/volcengine/mediakit-guide/8.5.2.1 安装.md` |
| 8.5.2.2 | 初始化 | 878-879 | 31643-31683 | 30 | `chapters/volcengine/mediakit-guide/8.5.2.2 初始化.md` |
| 8.5.2.3 | 媒体处理任务 | 880-883 | 31684-31811 | 120 | `chapters/volcengine/mediakit-guide/8.5.2.3 媒体处理任务.md` |
| 8.5.3.1 | 安装 | 884 | 31813-31822 | 9 | `chapters/volcengine/mediakit-guide/8.5.3.1 安装.md` |
| 8.5.3.2 | 初始化 | 885-886 | 31823-31868 | 35 | `chapters/volcengine/mediakit-guide/8.5.3.2 初始化.md` |
| 8.5.3.3 | 媒体处理任务 | 887-890 | 31869-32018 | 142 | `chapters/volcengine/mediakit-guide/8.5.3.3 媒体处理任务.md` |
| 8.5.4.1 | 安装 | 891 | 32020-32039 | 16 | `chapters/volcengine/mediakit-guide/8.5.4.1 安装.md` |
| 8.5.4.2 | 初始化 | 892-893 | 32040-32085 | 35 | `chapters/volcengine/mediakit-guide/8.5.4.2 初始化.md` |
| 8.5.4.3 | 媒体处理任务 | 894-898 | 32086-32243 | 148 | `chapters/volcengine/mediakit-guide/8.5.4.3 媒体处理任务.md` |
| 8.5.5.1 | 安装 | 899 | 32245-32258 | 13 | `chapters/volcengine/mediakit-guide/8.5.5.1 安装.md` |
| 8.5.5.2 | 初始化 | 900-901 | 32259-32303 | 34 | `chapters/volcengine/mediakit-guide/8.5.5.2 初始化.md` |
| 8.5.5.3 | 媒体处理任务 | 902-905 | 32304-32444 | 132 | `chapters/volcengine/mediakit-guide/8.5.5.3 媒体处理任务.md` |
| 8.6.1 | API 发布历史 | 906-907 | 32446-32537 | 63 | `chapters/volcengine/mediakit-guide/8.6.1 API 发布历史.md` |
| 8.6.2 | API 概览 | 908 | 32538-32548 | 8 | `chapters/volcengine/mediakit-guide/8.6.2 API 概览.md` |
| 8.6.3 | 调用方法 | 909-911 | 32549-32642 | 72 | `chapters/volcengine/mediakit-guide/8.6.3 调用方法.md` |
| 8.6.4 | 公共错误码 | 912-916 | 32643-32738 | 86 | `chapters/volcengine/mediakit-guide/8.6.4 公共错误码.md` |
| 8.6.5.1 | 媒体处理完成事件 | 917-918 | 32740-32804 | 56 | `chapters/volcengine/mediakit-guide/8.6.5.1 媒体处理完成事件.md` |
| 8.6.6.1 | 提交媒体处理任务 | 919-926 | 32806-33137 | 302 | `chapters/volcengine/mediakit-guide/8.6.6.1 提交媒体处理任务.md` |
| 8.6.6.2 | 查询媒体处理任务 | 927-928 | 33138-33216 | 70 | `chapters/volcengine/mediakit-guide/8.6.6.2 查询媒体处理任务.md` |
| 8.6.6.3 | 取消媒体处理任务 | 929-930 | 33217-33265 | 40 | `chapters/volcengine/mediakit-guide/8.6.6.3 取消媒体处理任务.md` |
| 8.6.6.4 | 任务节点输出定义 | 931-936 | 33266-33471 | 174 | `chapters/volcengine/mediakit-guide/8.6.6.4 任务节点输出定义.md` |
| 8.6.6.5 | 任务输出状态码 | 937 | 33472-33491 | 18 | `chapters/volcengine/mediakit-guide/8.6.6.5 任务输出状态码.md` |
| 8.6.7 | 公共数据结构 | 938-954 | 33492-34239 | 641 | `chapters/volcengine/mediakit-guide/8.6.7 公共数据结构.md` |
| 8.7.1 | 联系我们 | 955 | 34241-34252 | 8 | `chapters/volcengine/mediakit-guide/8.7.1 联系我们.md` |
