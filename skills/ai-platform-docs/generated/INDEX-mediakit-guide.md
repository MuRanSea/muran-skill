# AI MediaKit 指南区章节表（mediakit-guide）

来源：《AI MediaKit 文档指南》（932 页）。154 个章节文件，接口级切分：一个接口/任务一个文件；超过 1500 行的按语义块自动再拆为`… - 第N部分`（0 个章节被拆分）。

「页码」是原 PDF 页码范围；「行范围」是中间 MD（`doc/<源文档>.md`）的 1 起始行号，可据此回查原文。章节文件本身已去掉页眉页脚，回查 PDF 时用这两列。文件名即章节标题，日常定位直接 Glob 文件名即可，用不到这两列。

**这张表用来 grep，不要整读。**

| 编号 | 标题 | 页码 | 行范围(源文件) | 行数 | 文件 |
|------|------|------|---------------|------|------|
| 1.1 | 功能发布历史 | 1-12 | 226-927 | 679 | `chapters/volcengine/mediakit-guide/1.1 功能发布历史.md` |
| 1.2 | AI MediaKit 查询任务信息 API 查询范围调整公告 | 13 | 928-955 | 18 | `chapters/volcengine/mediakit-guide/1.2 AI MediaKit 查询任务信息 API 查询范围调整公告.md` |
| 1.3 | AI MediaKit 输入文件及输出产物存储策略调整公 | 14 | 956-988 | 18 | `chapters/volcengine/mediakit-guide/1.3 AI MediaKit 输入文件及输出产物存储策略调整公.md` |
| 2.1 | AI MediaKit 介绍 | 15-26 | 990-1640 | 601 | `chapters/volcengine/mediakit-guide/2.1 AI MediaKit 介绍.md` |
| 2.2 | 快速入门：视频理解前处理 | 27-34 | 1641-1932 | 257 | `chapters/volcengine/mediakit-guide/2.2 快速入门：视频理解前处理.md` |
| 2.3 | 快速入门：视频生成后处理 | 35-38 | 1933-2056 | 86 | `chapters/volcengine/mediakit-guide/2.3 快速入门：视频生成后处理.md` |
| 2.4 | 计费说明 | 39-40 | 2057-2149 | 68 | `chapters/volcengine/mediakit-guide/2.4 计费说明.md` |
| 3.1.1 | 画质增强（大模型版） | 41-50 | 2152-2437 | 207 | `chapters/volcengine/mediakit-guide/3.1.1 画质增强（大模型版）.md` |
| 3.1.2 | 画质增强（标准版和专业版） | 51-66 | 2438-2911 | 353 | `chapters/volcengine/mediakit-guide/3.1.2 画质增强（标准版和专业版）.md` |
| 3.1.3 | 画质增强（极速版） | 67-72 | 2912-3107 | 155 | `chapters/volcengine/mediakit-guide/3.1.3 画质增强（极速版）.md` |
| 3.1.4 | 字幕擦除 | 73-89 | 3108-3551 | 315 | `chapters/volcengine/mediakit-guide/3.1.4 字幕擦除.md` |
| 3.1.5 | 视频转码 | 90-92 | 3552-3646 | 67 | `chapters/volcengine/mediakit-guide/3.1.5 视频转码.md` |
| 3.1.6 | 极智超清 | 93-96 | 3647-3760 | 80 | `chapters/volcengine/mediakit-guide/3.1.6 极智超清.md` |
| 3.1.7 | 视频暗水印 | 97-102 | 3761-3986 | 133 | `chapters/volcengine/mediakit-guide/3.1.7 视频暗水印.md` |
| 3.1.8 | 场景切分 | 103-107 | 3987-4146 | 112 | `chapters/volcengine/mediakit-guide/3.1.8 场景切分.md` |
| 3.1.9 | 智能语义切片（基础版） | 108-111 | 4147-4296 | 101 | `chapters/volcengine/mediakit-guide/3.1.9 智能语义切片（基础版）.md` |
| 3.1.10 | 智能语义切片（专业版） | 112-116 | 4297-4527 | 166 | `chapters/volcengine/mediakit-guide/3.1.10 智能语义切片（专业版）.md` |
| 3.1.11 | 语音转字幕（ASR） | 117-121 | 4528-4728 | 160 | `chapters/volcengine/mediakit-guide/3.1.11 语音转字幕（ASR）.md` |
| 3.1.12 | 视频识别字幕（OCR） | 122-126 | 4729-4905 | 130 | `chapters/volcengine/mediakit-guide/3.1.12 视频识别字幕（OCR）.md` |
| 3.1.13 | 高光智剪-短剧 | 127-141 | 4906-5430 | 379 | `chapters/volcengine/mediakit-guide/3.1.13 高光智剪-短剧.md` |
| 3.1.14 | 高光智剪-小游戏 | 142-146 | 5431-5607 | 136 | `chapters/volcengine/mediakit-guide/3.1.14 高光智剪-小游戏.md` |
| 3.1.15 | 高光智剪-影视拆条 | 147-151 | 5608-5800 | 141 | `chapters/volcengine/mediakit-guide/3.1.15 高光智剪-影视拆条.md` |
| 3.1.16 | 高光片段提取 | 152-157 | 5801-5988 | 154 | `chapters/volcengine/mediakit-guide/3.1.16 高光片段提取.md` |
| 3.1.17 | 视频抠图 | 158-162 | 5989-6146 | 110 | `chapters/volcengine/mediakit-guide/3.1.17 视频抠图.md` |
| 3.1.18 | 剧情故事线分析 | 163-169 | 6147-6451 | 223 | `chapters/volcengine/mediakit-guide/3.1.18 剧情故事线分析.md` |
| 3.1.19 | 剧本还原 | 170-178 | 6452-6864 | 367 | `chapters/volcengine/mediakit-guide/3.1.19 剧本还原.md` |
| 3.1.20 | 解说视频生成 | 179-188 | 6865-7204 | 262 | `chapters/volcengine/mediakit-guide/3.1.20 解说视频生成.md` |
| 3.1.21 | 解说视频生成（短剧行业模型） | 189-195 | 7205-7469 | 193 | `chapters/volcengine/mediakit-guide/3.1.21 解说视频生成（短剧行业模型）.md` |
| 3.1.22 | 视频抽帧 | 196-201 | 7470-7669 | 143 | `chapters/volcengine/mediakit-guide/3.1.22 视频抽帧.md` |
| 3.1.23 | 视频转封装 | 202-203 | 7670-7749 | 55 | `chapters/volcengine/mediakit-guide/3.1.23 视频转封装.md` |
| 3.1.24 | 视频画质检测 VQScore | 204-206 | 7750-7856 | 81 | `chapters/volcengine/mediakit-guide/3.1.24 视频画质检测 VQScore.md` |
| 3.1.25 | 视频人脸打码 | 207-211 | 7857-8012 | 114 | `chapters/volcengine/mediakit-guide/3.1.25 视频人脸打码.md` |
| 3.1.26 | 视频人脸融合（换脸） | 212-215 | 8013-8151 | 98 | `chapters/volcengine/mediakit-guide/3.1.26 视频人脸融合（换脸）.md` |
| 3.1.27 | 视频插帧 | 216-219 | 8152-8269 | 79 | `chapters/volcengine/mediakit-guide/3.1.27 视频插帧.md` |
| 3.1.28 | 视频口型对齐 | 220-224 | 8270-8420 | 108 | `chapters/volcengine/mediakit-guide/3.1.28 视频口型对齐.md` |
| 3.1.29 | 视频横转竖 | 225-228 | 8421-8548 | 91 | `chapters/volcengine/mediakit-guide/3.1.29 视频横转竖.md` |
| 3.1.30 | 视频流畅度提升 | 229-233 | 8549-8739 | 123 | `chapters/volcengine/mediakit-guide/3.1.30 视频流畅度提升.md` |
| 3.2.1 | 图像画质增强 | 234-240 | 8741-9038 | 266 | `chapters/volcengine/mediakit-guide/3.2.1 图像画质增强.md` |
| 3.2.2 | 图像画质评估 | 241-244 | 9039-9190 | 114 | `chapters/volcengine/mediakit-guide/3.2.2 图像画质评估.md` |
| 3.2.3 | 图像人脸打码 | 245-248 | 9191-9336 | 120 | `chapters/volcengine/mediakit-guide/3.2.3 图像人脸打码.md` |
| 3.2.4 | 图像擦除修复 | 249-253 | 9337-9512 | 127 | `chapters/volcengine/mediakit-guide/3.2.4 图像擦除修复.md` |
| 3.2.5 | 图像背景移除（智能抠图） | 254-256 | 9513-9605 | 67 | `chapters/volcengine/mediakit-guide/3.2.5 图像背景移除（智能抠图）.md` |
| 3.2.6 | 图像文字识别（OCR） | 257-261 | 9606-9790 | 152 | `chapters/volcengine/mediakit-guide/3.2.6 图像文字识别（OCR）.md` |
| 3.2.7 | 图像智能裁剪 | 262-264 | 9791-9877 | 66 | `chapters/volcengine/mediakit-guide/3.2.7 图像智能裁剪.md` |
| 3.2.8 | 智能扩图 | 265-268 | 9878-9981 | 74 | `chapters/volcengine/mediakit-guide/3.2.8 智能扩图.md` |
| 3.2.9 | 集智瘦身 | 269-271 | 9982-10057 | 55 | `chapters/volcengine/mediakit-guide/3.2.9 集智瘦身.md` |
| 3.2.10 | 图像翻译 | 272-278 | 10058-10262 | 173 | `chapters/volcengine/mediakit-guide/3.2.10 图像翻译.md` |
| 3.2.11 | 电商牛皮癣擦除 | 279-281 | 10263-10337 | 57 | `chapters/volcengine/mediakit-guide/3.2.11 电商牛皮癣擦除.md` |
| 3.2.12 | 电商万创（商品场景图生成） | 282-288 | 10338-10574 | 189 | `chapters/volcengine/mediakit-guide/3.2.12 电商万创（商品场景图生成）.md` |
| 3.2.13 | 图像暗水印 | 289-292 | 10575-10740 | 111 | `chapters/volcengine/mediakit-guide/3.2.13 图像暗水印.md` |
| 3.2.14 | 图像基础编辑 | 293-315 | 10741-11498 | 594 | `chapters/volcengine/mediakit-guide/3.2.14 图像基础编辑.md` |
| 3.3.1.1 | 智能剪辑 Vibe Editing | 316-324 | 11501-11825 | 207 | `chapters/volcengine/mediakit-guide/3.3.1.1 智能剪辑 Vibe Editing.md` |
| 3.3.1.2 | Web 智能剪辑 SDK 集成指南 | 325-356 | 11826-13337 | 1319 | `chapters/volcengine/mediakit-guide/3.3.1.2 Web 智能剪辑 SDK 集成指南.md` |
| 3.3.2.1 | 多轨道剪辑 | 357-399 | 13339-14891 | 1352 | `chapters/volcengine/mediakit-guide/3.3.2.1 多轨道剪辑.md` |
| 3.3.2.2 | Web 剪辑 SDK 集成指南 | 400-433 | 14892-16326 | 1220 | `chapters/volcengine/mediakit-guide/3.3.2.2 Web 剪辑 SDK 集成指南.md` |
| 3.3.2.3 | 音视频拼接 | 434-440 | 16327-16499 | 128 | `chapters/volcengine/mediakit-guide/3.3.2.3 音视频拼接.md` |
| 3.3.2.4 | 音视频裁剪 | 441-444 | 16500-16639 | 102 | `chapters/volcengine/mediakit-guide/3.3.2.4 音视频裁剪.md` |
| 3.3.2.5 | 音视频调速 | 445-448 | 16640-16743 | 71 | `chapters/volcengine/mediakit-guide/3.3.2.5 音视频调速.md` |
| 3.3.2.6 | 音频提取 | 449-451 | 16744-16861 | 84 | `chapters/volcengine/mediakit-guide/3.3.2.6 音频提取.md` |
| 3.3.2.7 | 音视频合成 | 452-456 | 16862-17050 | 140 | `chapters/volcengine/mediakit-guide/3.3.2.7 音视频合成.md` |
| 3.3.2.8 | 音频混合 | 457-459 | 17051-17159 | 79 | `chapters/volcengine/mediakit-guide/3.3.2.8 音频混合.md` |
| 3.3.2.9 | 音量调节与淡入淡出 | 460-464 | 17160-17338 | 133 | `chapters/volcengine/mediakit-guide/3.3.2.9 音量调节与淡入淡出.md` |
| 3.3.2.10 | 图片转视频 | 465-471 | 17339-17562 | 170 | `chapters/volcengine/mediakit-guide/3.3.2.10 图片转视频.md` |
| 3.3.2.11 | 视频画面变换 | 472-477 | 17563-17702 | 102 | `chapters/volcengine/mediakit-guide/3.3.2.11 视频画面变换.md` |
| 3.3.2.12 | 视频添加运镜 | 478-483 | 17703-17848 | 109 | `chapters/volcengine/mediakit-guide/3.3.2.12 视频添加运镜.md` |
| 3.3.2.13 | 视频加字幕 | 484-488 | 17849-18010 | 118 | `chapters/volcengine/mediakit-guide/3.3.2.13 视频加字幕.md` |
| 3.3.2.14 | 视频加图片 | 489-492 | 18011-18117 | 75 | `chapters/volcengine/mediakit-guide/3.3.2.14 视频加图片.md` |
| 3.3.2.15 | 视频添加滤镜 | 493-496 | 18118-18228 | 82 | `chapters/volcengine/mediakit-guide/3.3.2.15 视频添加滤镜.md` |
| 3.3.2.16 | 视频截取动图 | 497-500 | 18229-18351 | 94 | `chapters/volcengine/mediakit-guide/3.3.2.16 视频截取动图.md` |
| 3.3.2.17 | 视频高斯模糊 | 501-505 | 18352-18494 | 102 | `chapters/volcengine/mediakit-guide/3.3.2.17 视频高斯模糊.md` |
| 3.3.2.18 | 文字生成滚屏视频 | 506-510 | 18495-18681 | 115 | `chapters/volcengine/mediakit-guide/3.3.2.18 文字生成滚屏视频.md` |
| 3.3.2.19 | 添加 AIGC 元数据标识 | 511-514 | 18682-18824 | 107 | `chapters/volcengine/mediakit-guide/3.3.2.19 添加 AIGC 元数据标识.md` |
| 3.3.2.20 | HyperFrames 云端渲染 | 515-518 | 18825-18981 | 110 | `chapters/volcengine/mediakit-guide/3.3.2.20 HyperFrames 云端渲染.md` |
| 3.4.1 | 人声背景音分离 | 519-523 | 18983-19175 | 136 | `chapters/volcengine/mediakit-guide/3.4.1 人声背景音分离.md` |
| 3.4.2 | 语音端点识别 | 524-527 | 19176-19326 | 118 | `chapters/volcengine/mediakit-guide/3.4.2 语音端点识别.md` |
| 3.4.3 | 音频内容编辑 | 528-530 | 19327-19440 | 76 | `chapters/volcengine/mediakit-guide/3.4.3 音频内容编辑.md` |
| 3.4.4 | 音频转码 | 531-535 | 19441-19611 | 122 | `chapters/volcengine/mediakit-guide/3.4.4 音频转码.md` |
| 3.5.1 | 视频理解智能策略 | 536-541 | 19613-19875 | 184 | `chapters/volcengine/mediakit-guide/3.5.1 视频理解智能策略.md` |
| 3.5.2 | 大模型高光剪辑 | 542-548 | 19876-20127 | 189 | `chapters/volcengine/mediakit-guide/3.5.2 大模型高光剪辑.md` |
| 3.5.3 | 视频理解拓展工具 | 549-571 | 20128-21067 | 814 | `chapters/volcengine/mediakit-guide/3.5.3 视频理解拓展工具.md` |
| 3.5.4 | AIGC 视频生成质量评估 | 572-577 | 21068-21327 | 184 | `chapters/volcengine/mediakit-guide/3.5.4 AIGC 视频生成质量评估.md` |
| 3.5.5 | 通过 AI MediaKit 调用图片生成大模型 | 578-580 | 21328-21436 | 76 | `chapters/volcengine/mediakit-guide/3.5.5 通过 AI MediaKit 调用图片生成大模型.md` |
| 3.5.6 | 通过 AI MediaKit 调用视频生成大模型 | 581-583 | 21437-21553 | 84 | `chapters/volcengine/mediakit-guide/3.5.6 通过 AI MediaKit 调用视频生成大模型.md` |
| 3.5.7 | 通过 AI MediaKit 调用音频生成大模型 | 584-586 | 21554-21650 | 68 | `chapters/volcengine/mediakit-guide/3.5.7 通过 AI MediaKit 调用音频生成大模型.md` |
| 3.5.8 | 通过 AI MediaKit 调用语音识别大模型 | 587-589 | 21651-21763 | 79 | `chapters/volcengine/mediakit-guide/3.5.8 通过 AI MediaKit 调用语音识别大模型.md` |
| 3.6.1 | 多源媒体输入与本地上传 | 590-594 | 21765-21952 | 136 | `chapters/volcengine/mediakit-guide/3.6.1 多源媒体输入与本地上传.md` |
| 3.6.2 | 处理产物存储至 VOD 或 TOS | 595-599 | 21953-22129 | 102 | `chapters/volcengine/mediakit-guide/3.6.2 处理产物存储至 VOD 或 TOS.md` |
| 3.7 | 按项目或 API Key 分账 | 600-605 | 22130-22312 | 115 | `chapters/volcengine/mediakit-guide/3.7 按项目或 API Key 分账.md` |
| 4.1 | AI MediaKit CLI 用户指南 | 606-627 | 22314-23016 | 562 | `chapters/volcengine/mediakit-guide/4.1 AI MediaKit CLI 用户指南.md` |
| 4.2 | AI MediaKit Skill 用户指南 | 628-636 | 23017-23338 | 222 | `chapters/volcengine/mediakit-guide/4.2 AI MediaKit Skill 用户指南.md` |
| 4.3 | AI MediaKit MCP 用户指南 | 637-659 | 23339-24488 | 1053 | `chapters/volcengine/mediakit-guide/4.3 AI MediaKit MCP 用户指南.md` |
| 5.1 | 资源包 | 660-664 | 24490-24702 | 154 | `chapters/volcengine/mediakit-guide/5.1 资源包.md` |
| 5.2 | 剪辑工具计费 | 665-667 | 24703-24803 | 71 | `chapters/volcengine/mediakit-guide/5.2 剪辑工具计费.md` |
| 5.3 | 视频工具计费 | 668-694 | 24804-25884 | 935 | `chapters/volcengine/mediakit-guide/5.3 视频工具计费.md` |
| 5.4 | 音频工具计费 | 695-697 | 25885-25971 | 71 | `chapters/volcengine/mediakit-guide/5.4 音频工具计费.md` |
| 5.5 | 图像工具计费 | 698-702 | 25972-26178 | 139 | `chapters/volcengine/mediakit-guide/5.5 图像工具计费.md` |
| 5.6 | 大模型处理工具计费 | 703 | 26179-26189 | 4 | `chapters/volcengine/mediakit-guide/5.6 大模型处理工具计费.md` |
| 5.7 | 计费常见问题 | 704 | 26190-26224 | 18 | `chapters/volcengine/mediakit-guide/5.7 计费常见问题.md` |
| 6.1 | 常见问题 | 705-707 | 26226-26363 | 117 | `chapters/volcengine/mediakit-guide/6.1 常见问题.md` |
| 7.1 | 视频云服务专用条款 | 708-711 | 26365-26502 | 40 | `chapters/volcengine/mediakit-guide/7.1 视频云服务专用条款.md` |
| 7.2 | 智能处理服务计费结算规则 | 712-713 | 26503-26568 | 30 | `chapters/volcengine/mediakit-guide/7.2 智能处理服务计费结算规则.md` |
| 7.3 | 智能处理服务等级协议 | 714-716 | 26569-26643 | 44 | `chapters/volcengine/mediakit-guide/7.3 智能处理服务等级协议.md` |
| 8.1.1 | 概述 | 717 | 26646-26653 | 6 | `chapters/volcengine/mediakit-guide/8.1.1 概述.md` |
| 8.1.2 | 产品优势 | 718 | 26654-26668 | 9 | `chapters/volcengine/mediakit-guide/8.1.2 产品优势.md` |
| 8.1.3 | 应用场景 | 719 | 26669-26687 | 10 | `chapters/volcengine/mediakit-guide/8.1.3 应用场景.md` |
| 8.1.4 | 产品功能 | 720 | 26688-26710 | 14 | `chapters/volcengine/mediakit-guide/8.1.4 产品功能.md` |
| 8.1.5.1 | 老片修复 | 721-722 | 26712-26755 | 23 | `chapters/volcengine/mediakit-guide/8.1.5.1 老片修复.md` |
| 8.1.5.2 | 大模型视频预处理解决方案 | 723 | 26756-26784 | 12 | `chapters/volcengine/mediakit-guide/8.1.5.2 大模型视频预处理解决方案.md` |
| 8.2.1 | 计费概述 | 724-725 | 26786-26811 | 16 | `chapters/volcengine/mediakit-guide/8.2.1 计费概述.md` |
| 8.2.2.1 | 按量计费 | 726-734 | 26813-27047 | 199 | `chapters/volcengine/mediakit-guide/8.2.2.1 按量计费.md` |
| 8.2.2.2 | 资源包 | 735 | 27048-27084 | 23 | `chapters/volcengine/mediakit-guide/8.2.2.2 资源包.md` |
| 8.3.1 | 快速入门 | 736-745 | 27086-27239 | 97 | `chapters/volcengine/mediakit-guide/8.3.1 快速入门.md` |
| 8.4.1 | 控制台简介 | 746-749 | 27241-27318 | 66 | `chapters/volcengine/mediakit-guide/8.4.1 控制台简介.md` |
| 8.4.2 | 概览 | 750-754 | 27319-27390 | 36 | `chapters/volcengine/mediakit-guide/8.4.2 概览.md` |
| 8.4.3 | 任务管理 | 755-758 | 27391-27501 | 74 | `chapters/volcengine/mediakit-guide/8.4.3 任务管理.md` |
| 8.4.4 | 自动任务触发器 | 759-762 | 27502-27561 | 41 | `chapters/volcengine/mediakit-guide/8.4.4 自动任务触发器.md` |
| 8.4.5.1 | 功能概述 | 763-764 | 27563-27651 | 52 | `chapters/volcengine/mediakit-guide/8.4.5.1 功能概述.md` |
| 8.4.5.2.1 | 基础转码 | 765-779 | 27653-28120 | 388 | `chapters/volcengine/mediakit-guide/8.4.5.2.1 基础转码.md` |
| 8.4.5.2.2 | 极智超清 | 780-788 | 28121-28316 | 149 | `chapters/volcengine/mediakit-guide/8.4.5.2.2 极智超清.md` |
| 8.4.5.3.1 | 精细化擦除 | 789-795 | 28318-28406 | 56 | `chapters/volcengine/mediakit-guide/8.4.5.3.1 精细化擦除.md` |
| 8.4.5.4.1 | 画质检测修复 | 796-803 | 28408-28561 | 113 | `chapters/volcengine/mediakit-guide/8.4.5.4.1 画质检测修复.md` |
| 8.4.5.4.2 | 画质增强 | 804-810 | 28562-28660 | 59 | `chapters/volcengine/mediakit-guide/8.4.5.4.2 画质增强.md` |
| 8.4.5.5.1 | 智能识别剪切 | 811-815 | 28662-28730 | 43 | `chapters/volcengine/mediakit-guide/8.4.5.5.1 智能识别剪切.md` |
| 8.4.5.5.2 | 智能表情合成 | 816-824 | 28731-28858 | 82 | `chapters/volcengine/mediakit-guide/8.4.5.5.2 智能表情合成.md` |
| 8.4.5.5.3 | 智能抠图 | 825-831 | 28859-28936 | 51 | `chapters/volcengine/mediakit-guide/8.4.5.5.3 智能抠图.md` |
| 8.4.6 | 工作流模板 | 832-840 | 28937-29218 | 174 | `chapters/volcengine/mediakit-guide/8.4.6 工作流模板.md` |
| 8.4.7.1 | 统计数据 | 841-847 | 29220-29356 | 59 | `chapters/volcengine/mediakit-guide/8.4.7.1 统计数据.md` |
| 8.4.8 | 系统配置 | 848-850 | 29357-29413 | 38 | `chapters/volcengine/mediakit-guide/8.4.8 系统配置.md` |
| 8.4.9 | 媒体处理输出文件路径 | 851-852 | 29414-29453 | 33 | `chapters/volcengine/mediakit-guide/8.4.9 媒体处理输出文件路径.md` |
| 8.5.1 | 使用说明 | 853 | 29455-29489 | 24 | `chapters/volcengine/mediakit-guide/8.5.1 使用说明.md` |
| 8.5.2.1 | 安装 | 854 | 29491-29507 | 12 | `chapters/volcengine/mediakit-guide/8.5.2.1 安装.md` |
| 8.5.2.2 | 初始化 | 855-856 | 29508-29548 | 30 | `chapters/volcengine/mediakit-guide/8.5.2.2 初始化.md` |
| 8.5.2.3 | 媒体处理任务 | 857-860 | 29549-29676 | 120 | `chapters/volcengine/mediakit-guide/8.5.2.3 媒体处理任务.md` |
| 8.5.3.1 | 安装 | 861 | 29678-29687 | 9 | `chapters/volcengine/mediakit-guide/8.5.3.1 安装.md` |
| 8.5.3.2 | 初始化 | 862-863 | 29688-29733 | 35 | `chapters/volcengine/mediakit-guide/8.5.3.2 初始化.md` |
| 8.5.3.3 | 媒体处理任务 | 864-867 | 29734-29883 | 142 | `chapters/volcengine/mediakit-guide/8.5.3.3 媒体处理任务.md` |
| 8.5.4.1 | 安装 | 868 | 29885-29904 | 16 | `chapters/volcengine/mediakit-guide/8.5.4.1 安装.md` |
| 8.5.4.2 | 初始化 | 869-870 | 29905-29950 | 35 | `chapters/volcengine/mediakit-guide/8.5.4.2 初始化.md` |
| 8.5.4.3 | 媒体处理任务 | 871-875 | 29951-30108 | 148 | `chapters/volcengine/mediakit-guide/8.5.4.3 媒体处理任务.md` |
| 8.5.5.1 | 安装 | 876 | 30110-30123 | 13 | `chapters/volcengine/mediakit-guide/8.5.5.1 安装.md` |
| 8.5.5.2 | 初始化 | 877-878 | 30124-30168 | 34 | `chapters/volcengine/mediakit-guide/8.5.5.2 初始化.md` |
| 8.5.5.3 | 媒体处理任务 | 879-882 | 30169-30309 | 132 | `chapters/volcengine/mediakit-guide/8.5.5.3 媒体处理任务.md` |
| 8.6.1 | API 发布历史 | 883-884 | 30311-30402 | 63 | `chapters/volcengine/mediakit-guide/8.6.1 API 发布历史.md` |
| 8.6.2 | API 概览 | 885 | 30403-30413 | 8 | `chapters/volcengine/mediakit-guide/8.6.2 API 概览.md` |
| 8.6.3 | 调用方法 | 886-888 | 30414-30507 | 72 | `chapters/volcengine/mediakit-guide/8.6.3 调用方法.md` |
| 8.6.4 | 公共错误码 | 889-893 | 30508-30603 | 86 | `chapters/volcengine/mediakit-guide/8.6.4 公共错误码.md` |
| 8.6.5.1 | 媒体处理完成事件 | 894-895 | 30605-30669 | 56 | `chapters/volcengine/mediakit-guide/8.6.5.1 媒体处理完成事件.md` |
| 8.6.6.1 | 提交媒体处理任务 | 896-903 | 30671-31002 | 302 | `chapters/volcengine/mediakit-guide/8.6.6.1 提交媒体处理任务.md` |
| 8.6.6.2 | 查询媒体处理任务 | 904-905 | 31003-31081 | 70 | `chapters/volcengine/mediakit-guide/8.6.6.2 查询媒体处理任务.md` |
| 8.6.6.3 | 取消媒体处理任务 | 906-907 | 31082-31130 | 40 | `chapters/volcengine/mediakit-guide/8.6.6.3 取消媒体处理任务.md` |
| 8.6.6.4 | 任务节点输出定义 | 908-913 | 31131-31336 | 174 | `chapters/volcengine/mediakit-guide/8.6.6.4 任务节点输出定义.md` |
| 8.6.6.5 | 任务输出状态码 | 914 | 31337-31356 | 18 | `chapters/volcengine/mediakit-guide/8.6.6.5 任务输出状态码.md` |
| 8.6.7 | 公共数据结构 | 915-931 | 31357-32104 | 641 | `chapters/volcengine/mediakit-guide/8.6.7 公共数据结构.md` |
| 8.7.1 | 联系我们 | 932 | 32106-32117 | 8 | `chapters/volcengine/mediakit-guide/8.7.1 联系我们.md` |
