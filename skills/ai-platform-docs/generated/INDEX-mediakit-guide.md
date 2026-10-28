# AI MediaKit 指南区章节表（mediakit-guide）

来源：《AI MediaKit 文档指南》（937 页）。155 个章节文件，接口级切分：一个接口/任务一个文件；超过 1500 行的按语义块自动再拆为`… - 第N部分`（0 个章节被拆分）。

「页码」是原 PDF 页码范围；「行范围」是中间 MD（`doc/<源文档>.md`）的 1 起始行号，可据此回查原文。章节文件本身已去掉页眉页脚，回查 PDF 时用这两列。文件名即章节标题，日常定位直接 Glob 文件名即可，用不到这两列。

**这张表用来 grep，不要整读。**

| 编号 | 标题 | 页码 | 行范围(源文件) | 行数 | 文件 |
|------|------|------|---------------|------|------|
| 1.1 | 功能发布历史 | 1-12 | 227-953 | 704 | `chapters/volcengine/mediakit-guide/1.1 功能发布历史.md` |
| 1.2 | AI MediaKit 查询任务信息 API 查询范围调整公告 | 13 | 954-981 | 18 | `chapters/volcengine/mediakit-guide/1.2 AI MediaKit 查询任务信息 API 查询范围调整公告.md` |
| 1.3 | AI MediaKit 输入文件及输出产物存储策略调整公 | 14 | 982-1014 | 18 | `chapters/volcengine/mediakit-guide/1.3 AI MediaKit 输入文件及输出产物存储策略调整公.md` |
| 2.1 | AI MediaKit 介绍 | 15-28 | 1016-1802 | 733 | `chapters/volcengine/mediakit-guide/2.1 AI MediaKit 介绍.md` |
| 2.2 | 快速入门：视频理解前处理 | 29-36 | 1803-2094 | 257 | `chapters/volcengine/mediakit-guide/2.2 快速入门：视频理解前处理.md` |
| 2.3 | 快速入门：视频生成后处理 | 37-40 | 2095-2218 | 86 | `chapters/volcengine/mediakit-guide/2.3 快速入门：视频生成后处理.md` |
| 2.4 | 计费说明 | 41-42 | 2219-2311 | 68 | `chapters/volcengine/mediakit-guide/2.4 计费说明.md` |
| 3.1.1 | 画质增强（大模型版） | 43-52 | 2314-2599 | 207 | `chapters/volcengine/mediakit-guide/3.1.1 画质增强（大模型版）.md` |
| 3.1.2 | 画质增强（标准版和专业版） | 53-68 | 2600-3073 | 353 | `chapters/volcengine/mediakit-guide/3.1.2 画质增强（标准版和专业版）.md` |
| 3.1.3 | 画质增强（极速版） | 69-74 | 3074-3269 | 155 | `chapters/volcengine/mediakit-guide/3.1.3 画质增强（极速版）.md` |
| 3.1.4 | 字幕擦除 | 75-91 | 3270-3713 | 315 | `chapters/volcengine/mediakit-guide/3.1.4 字幕擦除.md` |
| 3.1.5 | 视频转码 | 92-94 | 3714-3808 | 67 | `chapters/volcengine/mediakit-guide/3.1.5 视频转码.md` |
| 3.1.6 | 极智超清 | 95-98 | 3809-3922 | 80 | `chapters/volcengine/mediakit-guide/3.1.6 极智超清.md` |
| 3.1.7 | 视频暗水印 | 99-104 | 3923-4148 | 133 | `chapters/volcengine/mediakit-guide/3.1.7 视频暗水印.md` |
| 3.1.8 | 场景切分 | 105-109 | 4149-4308 | 112 | `chapters/volcengine/mediakit-guide/3.1.8 场景切分.md` |
| 3.1.9 | 智能语义切片（基础版） | 110-113 | 4309-4458 | 101 | `chapters/volcengine/mediakit-guide/3.1.9 智能语义切片（基础版）.md` |
| 3.1.10 | 智能语义切片（专业版） | 114-118 | 4459-4689 | 166 | `chapters/volcengine/mediakit-guide/3.1.10 智能语义切片（专业版）.md` |
| 3.1.11 | 语音转字幕（ASR） | 119-123 | 4690-4890 | 160 | `chapters/volcengine/mediakit-guide/3.1.11 语音转字幕（ASR）.md` |
| 3.1.12 | 视频识别字幕（OCR） | 124-128 | 4891-5067 | 130 | `chapters/volcengine/mediakit-guide/3.1.12 视频识别字幕（OCR）.md` |
| 3.1.13 | 高光智剪-短剧 | 129-143 | 5068-5592 | 379 | `chapters/volcengine/mediakit-guide/3.1.13 高光智剪-短剧.md` |
| 3.1.14 | 高光智剪-小游戏 | 144-148 | 5593-5769 | 136 | `chapters/volcengine/mediakit-guide/3.1.14 高光智剪-小游戏.md` |
| 3.1.15 | 高光智剪-影视拆条 | 149-153 | 5770-5962 | 141 | `chapters/volcengine/mediakit-guide/3.1.15 高光智剪-影视拆条.md` |
| 3.1.16 | 高光片段提取 | 154-159 | 5963-6150 | 154 | `chapters/volcengine/mediakit-guide/3.1.16 高光片段提取.md` |
| 3.1.17 | 视频抠图 | 160-164 | 6151-6308 | 110 | `chapters/volcengine/mediakit-guide/3.1.17 视频抠图.md` |
| 3.1.18 | 剧情故事线分析 | 165-171 | 6309-6613 | 223 | `chapters/volcengine/mediakit-guide/3.1.18 剧情故事线分析.md` |
| 3.1.19 | 剧本还原 | 172-180 | 6614-7026 | 367 | `chapters/volcengine/mediakit-guide/3.1.19 剧本还原.md` |
| 3.1.20 | 解说视频生成 | 181-190 | 7027-7366 | 262 | `chapters/volcengine/mediakit-guide/3.1.20 解说视频生成.md` |
| 3.1.21 | 解说视频生成（短剧行业模型） | 191-197 | 7367-7631 | 193 | `chapters/volcengine/mediakit-guide/3.1.21 解说视频生成（短剧行业模型）.md` |
| 3.1.22 | 视频抽帧 | 198-203 | 7632-7831 | 143 | `chapters/volcengine/mediakit-guide/3.1.22 视频抽帧.md` |
| 3.1.23 | 视频转封装 | 204-205 | 7832-7911 | 55 | `chapters/volcengine/mediakit-guide/3.1.23 视频转封装.md` |
| 3.1.24 | 视频画质检测 VQScore | 206-208 | 7912-8018 | 81 | `chapters/volcengine/mediakit-guide/3.1.24 视频画质检测 VQScore.md` |
| 3.1.25 | 视频人脸打码 | 209-213 | 8019-8174 | 114 | `chapters/volcengine/mediakit-guide/3.1.25 视频人脸打码.md` |
| 3.1.26 | 视频人脸融合（换脸） | 214-217 | 8175-8313 | 98 | `chapters/volcengine/mediakit-guide/3.1.26 视频人脸融合（换脸）.md` |
| 3.1.27 | 视频插帧 | 218-221 | 8314-8431 | 79 | `chapters/volcengine/mediakit-guide/3.1.27 视频插帧.md` |
| 3.1.28 | 视频口型对齐 | 222-226 | 8432-8582 | 108 | `chapters/volcengine/mediakit-guide/3.1.28 视频口型对齐.md` |
| 3.1.29 | 视频横转竖 | 227-230 | 8583-8710 | 91 | `chapters/volcengine/mediakit-guide/3.1.29 视频横转竖.md` |
| 3.1.30 | 视频流畅度提升 | 231-235 | 8711-8901 | 123 | `chapters/volcengine/mediakit-guide/3.1.30 视频流畅度提升.md` |
| 3.1.31 | 深度动作捕捉 | 236-239 | 8902-9045 | 98 | `chapters/volcengine/mediakit-guide/3.1.31 深度动作捕捉.md` |
| 3.2.1 | 图像画质增强 | 240-246 | 9047-9344 | 266 | `chapters/volcengine/mediakit-guide/3.2.1 图像画质增强.md` |
| 3.2.2 | 图像画质评估 | 247-250 | 9345-9496 | 114 | `chapters/volcengine/mediakit-guide/3.2.2 图像画质评估.md` |
| 3.2.3 | 图像人脸打码 | 251-254 | 9497-9642 | 120 | `chapters/volcengine/mediakit-guide/3.2.3 图像人脸打码.md` |
| 3.2.4 | 图像擦除修复 | 255-259 | 9643-9818 | 127 | `chapters/volcengine/mediakit-guide/3.2.4 图像擦除修复.md` |
| 3.2.5 | 图像背景移除（智能抠图） | 260-262 | 9819-9911 | 67 | `chapters/volcengine/mediakit-guide/3.2.5 图像背景移除（智能抠图）.md` |
| 3.2.6 | 图像文字识别（OCR） | 263-267 | 9912-10096 | 152 | `chapters/volcengine/mediakit-guide/3.2.6 图像文字识别（OCR）.md` |
| 3.2.7 | 图像智能裁剪 | 268-270 | 10097-10183 | 66 | `chapters/volcengine/mediakit-guide/3.2.7 图像智能裁剪.md` |
| 3.2.8 | 智能扩图 | 271-274 | 10184-10287 | 74 | `chapters/volcengine/mediakit-guide/3.2.8 智能扩图.md` |
| 3.2.9 | 集智瘦身 | 275-277 | 10288-10363 | 55 | `chapters/volcengine/mediakit-guide/3.2.9 集智瘦身.md` |
| 3.2.10 | 图像翻译 | 278-284 | 10364-10568 | 173 | `chapters/volcengine/mediakit-guide/3.2.10 图像翻译.md` |
| 3.2.11 | 电商牛皮癣擦除 | 285-287 | 10569-10643 | 57 | `chapters/volcengine/mediakit-guide/3.2.11 电商牛皮癣擦除.md` |
| 3.2.12 | 电商万创（商品场景图生成） | 288-294 | 10644-10880 | 189 | `chapters/volcengine/mediakit-guide/3.2.12 电商万创（商品场景图生成）.md` |
| 3.2.13 | 图像暗水印 | 295-298 | 10881-11046 | 111 | `chapters/volcengine/mediakit-guide/3.2.13 图像暗水印.md` |
| 3.2.14 | 图像基础编辑 | 299-321 | 11047-11804 | 594 | `chapters/volcengine/mediakit-guide/3.2.14 图像基础编辑.md` |
| 3.3.1.1 | 智能剪辑 Vibe Editing | 322-330 | 11807-12131 | 207 | `chapters/volcengine/mediakit-guide/3.3.1.1 智能剪辑 Vibe Editing.md` |
| 3.3.1.2 | Web 智能剪辑 SDK 集成指南 | 331-362 | 12132-13643 | 1319 | `chapters/volcengine/mediakit-guide/3.3.1.2 Web 智能剪辑 SDK 集成指南.md` |
| 3.3.2.1 | 多轨道剪辑 | 363-405 | 13645-15197 | 1352 | `chapters/volcengine/mediakit-guide/3.3.2.1 多轨道剪辑.md` |
| 3.3.2.2 | Web 剪辑 SDK 集成指南 | 406-439 | 15198-16632 | 1220 | `chapters/volcengine/mediakit-guide/3.3.2.2 Web 剪辑 SDK 集成指南.md` |
| 3.3.2.3 | 音视频拼接 | 440-446 | 16633-16805 | 128 | `chapters/volcengine/mediakit-guide/3.3.2.3 音视频拼接.md` |
| 3.3.2.4 | 音视频裁剪 | 447-450 | 16806-16945 | 102 | `chapters/volcengine/mediakit-guide/3.3.2.4 音视频裁剪.md` |
| 3.3.2.5 | 音视频调速 | 451-454 | 16946-17049 | 71 | `chapters/volcengine/mediakit-guide/3.3.2.5 音视频调速.md` |
| 3.3.2.6 | 音频提取 | 455-457 | 17050-17167 | 84 | `chapters/volcengine/mediakit-guide/3.3.2.6 音频提取.md` |
| 3.3.2.7 | 音视频合成 | 458-462 | 17168-17356 | 140 | `chapters/volcengine/mediakit-guide/3.3.2.7 音视频合成.md` |
| 3.3.2.8 | 音频混合 | 463-465 | 17357-17465 | 79 | `chapters/volcengine/mediakit-guide/3.3.2.8 音频混合.md` |
| 3.3.2.9 | 音量调节与淡入淡出 | 466-470 | 17466-17644 | 133 | `chapters/volcengine/mediakit-guide/3.3.2.9 音量调节与淡入淡出.md` |
| 3.3.2.10 | 图片转视频 | 471-477 | 17645-17868 | 170 | `chapters/volcengine/mediakit-guide/3.3.2.10 图片转视频.md` |
| 3.3.2.11 | 视频画面变换 | 478-483 | 17869-18008 | 102 | `chapters/volcengine/mediakit-guide/3.3.2.11 视频画面变换.md` |
| 3.3.2.12 | 视频添加运镜 | 484-489 | 18009-18154 | 109 | `chapters/volcengine/mediakit-guide/3.3.2.12 视频添加运镜.md` |
| 3.3.2.13 | 视频加字幕 | 490-494 | 18155-18316 | 118 | `chapters/volcengine/mediakit-guide/3.3.2.13 视频加字幕.md` |
| 3.3.2.14 | 视频加图片 | 495-498 | 18317-18423 | 75 | `chapters/volcengine/mediakit-guide/3.3.2.14 视频加图片.md` |
| 3.3.2.15 | 视频添加滤镜 | 499-502 | 18424-18534 | 82 | `chapters/volcengine/mediakit-guide/3.3.2.15 视频添加滤镜.md` |
| 3.3.2.16 | 视频截取动图 | 503-506 | 18535-18657 | 94 | `chapters/volcengine/mediakit-guide/3.3.2.16 视频截取动图.md` |
| 3.3.2.17 | 视频高斯模糊 | 507-511 | 18658-18800 | 102 | `chapters/volcengine/mediakit-guide/3.3.2.17 视频高斯模糊.md` |
| 3.3.2.18 | 文字生成滚屏视频 | 512-516 | 18801-18987 | 115 | `chapters/volcengine/mediakit-guide/3.3.2.18 文字生成滚屏视频.md` |
| 3.3.2.19 | 添加 AIGC 元数据标识 | 517-520 | 18988-19130 | 107 | `chapters/volcengine/mediakit-guide/3.3.2.19 添加 AIGC 元数据标识.md` |
| 3.3.2.20 | HyperFrames 云端渲染 | 521-524 | 19131-19287 | 110 | `chapters/volcengine/mediakit-guide/3.3.2.20 HyperFrames 云端渲染.md` |
| 3.4.1 | 人声背景音分离 | 525-529 | 19289-19489 | 140 | `chapters/volcengine/mediakit-guide/3.4.1 人声背景音分离.md` |
| 3.4.2 | 语音端点识别 | 530-533 | 19490-19640 | 118 | `chapters/volcengine/mediakit-guide/3.4.2 语音端点识别.md` |
| 3.4.3 | 音频转码 | 534-538 | 19641-19811 | 122 | `chapters/volcengine/mediakit-guide/3.4.3 音频转码.md` |
| 3.4.4 | 音频内容编辑 | 539-541 | 19812-19925 | 76 | `chapters/volcengine/mediakit-guide/3.4.4 音频内容编辑.md` |
| 3.5.1 | 视频理解智能策略 | 542-547 | 19927-20189 | 184 | `chapters/volcengine/mediakit-guide/3.5.1 视频理解智能策略.md` |
| 3.5.2 | 大模型高光剪辑 | 548-554 | 20190-20441 | 189 | `chapters/volcengine/mediakit-guide/3.5.2 大模型高光剪辑.md` |
| 3.5.3 | 视频理解拓展工具 | 555-577 | 20442-21381 | 814 | `chapters/volcengine/mediakit-guide/3.5.3 视频理解拓展工具.md` |
| 3.5.4 | AIGC 视频生成质量评估 | 578-583 | 21382-21641 | 184 | `chapters/volcengine/mediakit-guide/3.5.4 AIGC 视频生成质量评估.md` |
| 3.5.5 | 通过 AI MediaKit 调用图片生成大模型 | 584-586 | 21642-21750 | 76 | `chapters/volcengine/mediakit-guide/3.5.5 通过 AI MediaKit 调用图片生成大模型.md` |
| 3.5.6 | 通过 AI MediaKit 调用视频生成大模型 | 587-589 | 21751-21867 | 84 | `chapters/volcengine/mediakit-guide/3.5.6 通过 AI MediaKit 调用视频生成大模型.md` |
| 3.5.7 | 通过 AI MediaKit 调用音频生成大模型 | 590-592 | 21868-21964 | 68 | `chapters/volcengine/mediakit-guide/3.5.7 通过 AI MediaKit 调用音频生成大模型.md` |
| 3.5.8 | 通过 AI MediaKit 调用语音识别大模型 | 593-595 | 21965-22077 | 79 | `chapters/volcengine/mediakit-guide/3.5.8 通过 AI MediaKit 调用语音识别大模型.md` |
| 3.6.1 | 多源媒体输入与本地上传 | 596-600 | 22079-22266 | 136 | `chapters/volcengine/mediakit-guide/3.6.1 多源媒体输入与本地上传.md` |
| 3.6.2 | 处理产物存储至 VOD 或 TOS | 601-605 | 22267-22443 | 102 | `chapters/volcengine/mediakit-guide/3.6.2 处理产物存储至 VOD 或 TOS.md` |
| 3.7 | 按项目或 API Key 分账 | 606-611 | 22444-22626 | 115 | `chapters/volcengine/mediakit-guide/3.7 按项目或 API Key 分账.md` |
| 4.1 | AI MediaKit CLI 用户指南 | 612-633 | 22628-23330 | 562 | `chapters/volcengine/mediakit-guide/4.1 AI MediaKit CLI 用户指南.md` |
| 4.2 | AI MediaKit Skill 用户指南 | 634-642 | 23331-23652 | 222 | `chapters/volcengine/mediakit-guide/4.2 AI MediaKit Skill 用户指南.md` |
| 4.3 | AI MediaKit MCP 用户指南 | 643-665 | 23653-24802 | 1053 | `chapters/volcengine/mediakit-guide/4.3 AI MediaKit MCP 用户指南.md` |
| 5.1 | 资源包 | 666-670 | 24804-25016 | 154 | `chapters/volcengine/mediakit-guide/5.1 资源包.md` |
| 5.2 | 剪辑工具计费 | 671-673 | 25017-25117 | 71 | `chapters/volcengine/mediakit-guide/5.2 剪辑工具计费.md` |
| 5.3 | 视频工具计费 | 674-699 | 25118-26215 | 952 | `chapters/volcengine/mediakit-guide/5.3 视频工具计费.md` |
| 5.4 | 音频工具计费 | 700-702 | 26216-26302 | 71 | `chapters/volcengine/mediakit-guide/5.4 音频工具计费.md` |
| 5.5 | 图像工具计费 | 703-707 | 26303-26509 | 139 | `chapters/volcengine/mediakit-guide/5.5 图像工具计费.md` |
| 5.6 | 大模型处理工具计费 | 708 | 26510-26520 | 4 | `chapters/volcengine/mediakit-guide/5.6 大模型处理工具计费.md` |
| 5.7 | 计费常见问题 | 709 | 26521-26555 | 18 | `chapters/volcengine/mediakit-guide/5.7 计费常见问题.md` |
| 6.1 | 常见问题 | 710-712 | 26557-26694 | 117 | `chapters/volcengine/mediakit-guide/6.1 常见问题.md` |
| 7.1 | 视频云服务专用条款 | 713-716 | 26696-26833 | 40 | `chapters/volcengine/mediakit-guide/7.1 视频云服务专用条款.md` |
| 7.2 | 智能处理服务计费结算规则 | 717-718 | 26834-26899 | 30 | `chapters/volcengine/mediakit-guide/7.2 智能处理服务计费结算规则.md` |
| 7.3 | 智能处理服务等级协议 | 719-721 | 26900-26974 | 44 | `chapters/volcengine/mediakit-guide/7.3 智能处理服务等级协议.md` |
| 8.1.1 | 概述 | 722 | 26977-26984 | 6 | `chapters/volcengine/mediakit-guide/8.1.1 概述.md` |
| 8.1.2 | 产品优势 | 723 | 26985-26999 | 9 | `chapters/volcengine/mediakit-guide/8.1.2 产品优势.md` |
| 8.1.3 | 应用场景 | 724 | 27000-27018 | 10 | `chapters/volcengine/mediakit-guide/8.1.3 应用场景.md` |
| 8.1.4 | 产品功能 | 725 | 27019-27041 | 14 | `chapters/volcengine/mediakit-guide/8.1.4 产品功能.md` |
| 8.1.5.1 | 老片修复 | 726-727 | 27043-27086 | 23 | `chapters/volcengine/mediakit-guide/8.1.5.1 老片修复.md` |
| 8.1.5.2 | 大模型视频预处理解决方案 | 728 | 27087-27115 | 12 | `chapters/volcengine/mediakit-guide/8.1.5.2 大模型视频预处理解决方案.md` |
| 8.2.1 | 计费概述 | 729-730 | 27117-27142 | 16 | `chapters/volcengine/mediakit-guide/8.2.1 计费概述.md` |
| 8.2.2.1 | 按量计费 | 731-739 | 27144-27378 | 199 | `chapters/volcengine/mediakit-guide/8.2.2.1 按量计费.md` |
| 8.2.2.2 | 资源包 | 740 | 27379-27415 | 23 | `chapters/volcengine/mediakit-guide/8.2.2.2 资源包.md` |
| 8.3.1 | 快速入门 | 741-750 | 27417-27570 | 97 | `chapters/volcengine/mediakit-guide/8.3.1 快速入门.md` |
| 8.4.1 | 控制台简介 | 751-754 | 27572-27649 | 66 | `chapters/volcengine/mediakit-guide/8.4.1 控制台简介.md` |
| 8.4.2 | 概览 | 755-759 | 27650-27721 | 36 | `chapters/volcengine/mediakit-guide/8.4.2 概览.md` |
| 8.4.3 | 任务管理 | 760-763 | 27722-27832 | 74 | `chapters/volcengine/mediakit-guide/8.4.3 任务管理.md` |
| 8.4.4 | 自动任务触发器 | 764-767 | 27833-27892 | 41 | `chapters/volcengine/mediakit-guide/8.4.4 自动任务触发器.md` |
| 8.4.5.1 | 功能概述 | 768-769 | 27894-27982 | 52 | `chapters/volcengine/mediakit-guide/8.4.5.1 功能概述.md` |
| 8.4.5.2.1 | 基础转码 | 770-784 | 27984-28451 | 388 | `chapters/volcengine/mediakit-guide/8.4.5.2.1 基础转码.md` |
| 8.4.5.2.2 | 极智超清 | 785-793 | 28452-28647 | 149 | `chapters/volcengine/mediakit-guide/8.4.5.2.2 极智超清.md` |
| 8.4.5.3.1 | 精细化擦除 | 794-800 | 28649-28737 | 56 | `chapters/volcengine/mediakit-guide/8.4.5.3.1 精细化擦除.md` |
| 8.4.5.4.1 | 画质检测修复 | 801-808 | 28739-28892 | 113 | `chapters/volcengine/mediakit-guide/8.4.5.4.1 画质检测修复.md` |
| 8.4.5.4.2 | 画质增强 | 809-815 | 28893-28991 | 59 | `chapters/volcengine/mediakit-guide/8.4.5.4.2 画质增强.md` |
| 8.4.5.5.1 | 智能识别剪切 | 816-820 | 28993-29061 | 43 | `chapters/volcengine/mediakit-guide/8.4.5.5.1 智能识别剪切.md` |
| 8.4.5.5.2 | 智能表情合成 | 821-829 | 29062-29189 | 82 | `chapters/volcengine/mediakit-guide/8.4.5.5.2 智能表情合成.md` |
| 8.4.5.5.3 | 智能抠图 | 830-836 | 29190-29267 | 51 | `chapters/volcengine/mediakit-guide/8.4.5.5.3 智能抠图.md` |
| 8.4.6 | 工作流模板 | 837-845 | 29268-29549 | 174 | `chapters/volcengine/mediakit-guide/8.4.6 工作流模板.md` |
| 8.4.7.1 | 统计数据 | 846-852 | 29551-29687 | 59 | `chapters/volcengine/mediakit-guide/8.4.7.1 统计数据.md` |
| 8.4.8 | 系统配置 | 853-855 | 29688-29744 | 38 | `chapters/volcengine/mediakit-guide/8.4.8 系统配置.md` |
| 8.4.9 | 媒体处理输出文件路径 | 856-857 | 29745-29784 | 33 | `chapters/volcengine/mediakit-guide/8.4.9 媒体处理输出文件路径.md` |
| 8.5.1 | 使用说明 | 858 | 29786-29820 | 24 | `chapters/volcengine/mediakit-guide/8.5.1 使用说明.md` |
| 8.5.2.1 | 安装 | 859 | 29822-29838 | 12 | `chapters/volcengine/mediakit-guide/8.5.2.1 安装.md` |
| 8.5.2.2 | 初始化 | 860-861 | 29839-29879 | 30 | `chapters/volcengine/mediakit-guide/8.5.2.2 初始化.md` |
| 8.5.2.3 | 媒体处理任务 | 862-865 | 29880-30007 | 120 | `chapters/volcengine/mediakit-guide/8.5.2.3 媒体处理任务.md` |
| 8.5.3.1 | 安装 | 866 | 30009-30018 | 9 | `chapters/volcengine/mediakit-guide/8.5.3.1 安装.md` |
| 8.5.3.2 | 初始化 | 867-868 | 30019-30064 | 35 | `chapters/volcengine/mediakit-guide/8.5.3.2 初始化.md` |
| 8.5.3.3 | 媒体处理任务 | 869-872 | 30065-30214 | 142 | `chapters/volcengine/mediakit-guide/8.5.3.3 媒体处理任务.md` |
| 8.5.4.1 | 安装 | 873 | 30216-30235 | 16 | `chapters/volcengine/mediakit-guide/8.5.4.1 安装.md` |
| 8.5.4.2 | 初始化 | 874-875 | 30236-30281 | 35 | `chapters/volcengine/mediakit-guide/8.5.4.2 初始化.md` |
| 8.5.4.3 | 媒体处理任务 | 876-880 | 30282-30439 | 148 | `chapters/volcengine/mediakit-guide/8.5.4.3 媒体处理任务.md` |
| 8.5.5.1 | 安装 | 881 | 30441-30454 | 13 | `chapters/volcengine/mediakit-guide/8.5.5.1 安装.md` |
| 8.5.5.2 | 初始化 | 882-883 | 30455-30499 | 34 | `chapters/volcengine/mediakit-guide/8.5.5.2 初始化.md` |
| 8.5.5.3 | 媒体处理任务 | 884-887 | 30500-30640 | 132 | `chapters/volcengine/mediakit-guide/8.5.5.3 媒体处理任务.md` |
| 8.6.1 | API 发布历史 | 888-889 | 30642-30733 | 63 | `chapters/volcengine/mediakit-guide/8.6.1 API 发布历史.md` |
| 8.6.2 | API 概览 | 890 | 30734-30744 | 8 | `chapters/volcengine/mediakit-guide/8.6.2 API 概览.md` |
| 8.6.3 | 调用方法 | 891-893 | 30745-30838 | 72 | `chapters/volcengine/mediakit-guide/8.6.3 调用方法.md` |
| 8.6.4 | 公共错误码 | 894-898 | 30839-30934 | 86 | `chapters/volcengine/mediakit-guide/8.6.4 公共错误码.md` |
| 8.6.5.1 | 媒体处理完成事件 | 899-900 | 30936-31000 | 56 | `chapters/volcengine/mediakit-guide/8.6.5.1 媒体处理完成事件.md` |
| 8.6.6.1 | 提交媒体处理任务 | 901-908 | 31002-31333 | 302 | `chapters/volcengine/mediakit-guide/8.6.6.1 提交媒体处理任务.md` |
| 8.6.6.2 | 查询媒体处理任务 | 909-910 | 31334-31412 | 70 | `chapters/volcengine/mediakit-guide/8.6.6.2 查询媒体处理任务.md` |
| 8.6.6.3 | 取消媒体处理任务 | 911-912 | 31413-31461 | 40 | `chapters/volcengine/mediakit-guide/8.6.6.3 取消媒体处理任务.md` |
| 8.6.6.4 | 任务节点输出定义 | 913-918 | 31462-31667 | 174 | `chapters/volcengine/mediakit-guide/8.6.6.4 任务节点输出定义.md` |
| 8.6.6.5 | 任务输出状态码 | 919 | 31668-31687 | 18 | `chapters/volcengine/mediakit-guide/8.6.6.5 任务输出状态码.md` |
| 8.6.7 | 公共数据结构 | 920-936 | 31688-32435 | 641 | `chapters/volcengine/mediakit-guide/8.6.7 公共数据结构.md` |
| 8.7.1 | 联系我们 | 937 | 32437-32448 | 8 | `chapters/volcengine/mediakit-guide/8.7.1 联系我们.md` |
