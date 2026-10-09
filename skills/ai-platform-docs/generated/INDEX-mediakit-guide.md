# AI MediaKit 指南区章节表（mediakit-guide）

来源：《AI MediaKit 文档指南》（889 页）。152 个章节文件，接口级切分：一个接口/任务一个文件；超过 1500 行的按语义块自动再拆为`… - 第N部分`（0 个章节被拆分）。

「页码」是原 PDF 页码范围；「行范围」是中间 MD（`doc/<源文档>.md`）的 1 起始行号，可据此回查原文。章节文件本身已去掉页眉页脚，回查 PDF 时用这两列。文件名即章节标题，日常定位直接 Glob 文件名即可，用不到这两列。

**这张表用来 grep，不要整读。**

| 编号 | 标题 | 页码 | 行范围(源文件) | 行数 | 文件 |
|------|------|------|---------------|------|------|
| 1.1 | 功能发布历史 | --12 | 224-1170 | 742 | `chapters/volcengine/mediakit-guide/1.1 功能发布历史.md` |
| 1.2 | AI MediaKit 查询任务信息 API 查询范围调整公告 | 13 | 1171-1198 | 18 | `chapters/volcengine/mediakit-guide/1.2 AI MediaKit 查询任务信息 API 查询范围调整公告.md` |
| 1.3 | AI MediaKit 输入文件及输出产物存储策略调整公 | 14 | 1199-1231 | 18 | `chapters/volcengine/mediakit-guide/1.3 AI MediaKit 输入文件及输出产物存储策略调整公.md` |
| 2.1 | AI MediaKit 介绍 | 15-26 | 1233-1886 | 602 | `chapters/volcengine/mediakit-guide/2.1 AI MediaKit 介绍.md` |
| 2.2 | 快速入门：视频理解前处理 | 27-33 | 1887-2145 | 224 | `chapters/volcengine/mediakit-guide/2.2 快速入门：视频理解前处理.md` |
| 2.3 | 快速入门：视频生成后处理 | 34-37 | 2146-2270 | 87 | `chapters/volcengine/mediakit-guide/2.3 快速入门：视频生成后处理.md` |
| 2.4 | 计费说明 | 38-39 | 2271-2374 | 69 | `chapters/volcengine/mediakit-guide/2.4 计费说明.md` |
| 3.1.1 | 画质增强（大模型版） | 40-49 | 2377-2665 | 210 | `chapters/volcengine/mediakit-guide/3.1.1 画质增强（大模型版）.md` |
| 3.1.2 | 画质增强（标准版和专业版） | 50-63 | 2666-3144 | 358 | `chapters/volcengine/mediakit-guide/3.1.2 画质增强（标准版和专业版）.md` |
| 3.1.3 | 画质增强（极速版） | 64-69 | 3145-3346 | 157 | `chapters/volcengine/mediakit-guide/3.1.3 画质增强（极速版）.md` |
| 3.1.4 | 字幕擦除 | 70-85 | 3347-3770 | 293 | `chapters/volcengine/mediakit-guide/3.1.4 字幕擦除.md` |
| 3.1.5 | 视频转码 | 86-88 | 3771-3866 | 67 | `chapters/volcengine/mediakit-guide/3.1.5 视频转码.md` |
| 3.1.6 | 极智超清 | 89-91 | 3867-3978 | 81 | `chapters/volcengine/mediakit-guide/3.1.6 极智超清.md` |
| 3.1.7 | 视频暗水印 | 92-97 | 3979-4213 | 136 | `chapters/volcengine/mediakit-guide/3.1.7 视频暗水印.md` |
| 3.1.8 | 场景切分 | 98-102 | 4214-4376 | 111 | `chapters/volcengine/mediakit-guide/3.1.8 场景切分.md` |
| 3.1.9 | 智能语义切片（基础版） | 103-106 | 4377-4529 | 101 | `chapters/volcengine/mediakit-guide/3.1.9 智能语义切片（基础版）.md` |
| 3.1.10 | 智能语义切片（专业版） | 107-111 | 4530-4767 | 167 | `chapters/volcengine/mediakit-guide/3.1.10 智能语义切片（专业版）.md` |
| 3.1.11 | 语音转字幕（ASR） | 112-116 | 4768-4979 | 167 | `chapters/volcengine/mediakit-guide/3.1.11 语音转字幕（ASR）.md` |
| 3.1.12 | 视频识别字幕（OCR） | 117-121 | 4980-5175 | 145 | `chapters/volcengine/mediakit-guide/3.1.12 视频识别字幕（OCR）.md` |
| 3.1.13 | 高光智剪-短剧 | 122-136 | 5176-5712 | 379 | `chapters/volcengine/mediakit-guide/3.1.13 高光智剪-短剧.md` |
| 3.1.14 | 高光智剪-小游戏 | 137-141 | 5713-5894 | 136 | `chapters/volcengine/mediakit-guide/3.1.14 高光智剪-小游戏.md` |
| 3.1.15 | 高光智剪-影视拆条 | 142-146 | 5895-6095 | 143 | `chapters/volcengine/mediakit-guide/3.1.15 高光智剪-影视拆条.md` |
| 3.1.16 | 高光片段提取 | 147-152 | 6096-6293 | 157 | `chapters/volcengine/mediakit-guide/3.1.16 高光片段提取.md` |
| 3.1.17 | 视频抠图 | 153-157 | 6294-6454 | 110 | `chapters/volcengine/mediakit-guide/3.1.17 视频抠图.md` |
| 3.1.18 | 剧情故事线分析 | 158-163 | 6455-6764 | 223 | `chapters/volcengine/mediakit-guide/3.1.18 剧情故事线分析.md` |
| 3.1.19 | 剧本还原 | 164-172 | 6765-7182 | 369 | `chapters/volcengine/mediakit-guide/3.1.19 剧本还原.md` |
| 3.1.20 | 解说视频生成 | 173-182 | 7183-7537 | 272 | `chapters/volcengine/mediakit-guide/3.1.20 解说视频生成.md` |
| 3.1.21 | 解说视频生成（短剧行业模型） | 183-189 | 7538-7814 | 197 | `chapters/volcengine/mediakit-guide/3.1.21 解说视频生成（短剧行业模型）.md` |
| 3.1.22 | 视频抽帧 | 190-195 | 7815-8016 | 143 | `chapters/volcengine/mediakit-guide/3.1.22 视频抽帧.md` |
| 3.1.23 | 视频转封装 | 196-197 | 8017-8096 | 55 | `chapters/volcengine/mediakit-guide/3.1.23 视频转封装.md` |
| 3.1.24 | 视频画质检测 VQScore | 198-200 | 8097-8206 | 81 | `chapters/volcengine/mediakit-guide/3.1.24 视频画质检测 VQScore.md` |
| 3.1.25 | 视频人脸打码 | 201-205 | 8207-8367 | 114 | `chapters/volcengine/mediakit-guide/3.1.25 视频人脸打码.md` |
| 3.1.26 | 视频人脸融合（换脸） | 206-209 | 8368-8520 | 102 | `chapters/volcengine/mediakit-guide/3.1.26 视频人脸融合（换脸）.md` |
| 3.1.27 | 视频插帧 | 210-213 | 8521-8640 | 79 | `chapters/volcengine/mediakit-guide/3.1.27 视频插帧.md` |
| 3.1.28 | 视频口型对齐 | 214-217 | 8641-8793 | 106 | `chapters/volcengine/mediakit-guide/3.1.28 视频口型对齐.md` |
| 3.1.29 | 视频横转竖 | 218-221 | 8794-8929 | 91 | `chapters/volcengine/mediakit-guide/3.1.29 视频横转竖.md` |
| 3.1.30 | 视频流畅度提升 | 222-226 | 8930-9124 | 122 | `chapters/volcengine/mediakit-guide/3.1.30 视频流畅度提升.md` |
| 3.2.1 | 图像画质增强 | 222-233 | 9126-9478 | 277 | `chapters/volcengine/mediakit-guide/3.2.1 图像画质增强.md` |
| 3.2.2 | 图像画质评估 | 234-237 | 9479-9637 | 117 | `chapters/volcengine/mediakit-guide/3.2.2 图像画质评估.md` |
| 3.2.3 | 图像人脸打码 | 238-241 | 9638-9790 | 121 | `chapters/volcengine/mediakit-guide/3.2.3 图像人脸打码.md` |
| 3.2.4 | 图像擦除修复 | 242-246 | 9791-9973 | 131 | `chapters/volcengine/mediakit-guide/3.2.4 图像擦除修复.md` |
| 3.2.5 | 图像背景移除（智能抠图） | 247-249 | 9974-10075 | 70 | `chapters/volcengine/mediakit-guide/3.2.5 图像背景移除（智能抠图）.md` |
| 3.2.6 | 图像文字识别（OCR） | 250-254 | 10076-10269 | 152 | `chapters/volcengine/mediakit-guide/3.2.6 图像文字识别（OCR）.md` |
| 3.2.7 | 图像智能裁剪 | 255-257 | 10270-10361 | 67 | `chapters/volcengine/mediakit-guide/3.2.7 图像智能裁剪.md` |
| 3.2.8 | 智能扩图 | 258-261 | 10362-10471 | 76 | `chapters/volcengine/mediakit-guide/3.2.8 智能扩图.md` |
| 3.2.9 | 集智瘦身 | 262-264 | 10472-10553 | 57 | `chapters/volcengine/mediakit-guide/3.2.9 集智瘦身.md` |
| 3.2.10 | 图像翻译 | 265-271 | 10554-10763 | 174 | `chapters/volcengine/mediakit-guide/3.2.10 图像翻译.md` |
| 3.2.11 | 电商牛皮癣擦除 | 272-274 | 10764-10845 | 60 | `chapters/volcengine/mediakit-guide/3.2.11 电商牛皮癣擦除.md` |
| 3.2.12 | 电商万创（商品场景图生成） | 275-281 | 10846-11088 | 191 | `chapters/volcengine/mediakit-guide/3.2.12 电商万创（商品场景图生成）.md` |
| 3.2.13 | 图像暗水印 | 282-286 | 11089-11262 | 114 | `chapters/volcengine/mediakit-guide/3.2.13 图像暗水印.md` |
| 3.2.14 | 图像基础编辑 | 287-309 | 11263-12033 | 597 | `chapters/volcengine/mediakit-guide/3.2.14 图像基础编辑.md` |
| 3.3.1.1 | 智能剪辑 Vibe Editing | 310-318 | 12036-12401 | 213 | `chapters/volcengine/mediakit-guide/3.3.1.1 智能剪辑 Vibe Editing.md` |
| 3.3.1.2 | Web 智能剪辑 SDK 集成指南 | 319-335 | 12402-13082 | 585 | `chapters/volcengine/mediakit-guide/3.3.1.2 Web 智能剪辑 SDK 集成指南.md` |
| 3.3.2.1 | 多轨道剪辑 | 336-375 | 13084-14631 | 1353 | `chapters/volcengine/mediakit-guide/3.3.2.1 多轨道剪辑.md` |
| 3.3.2.2 | Web 剪辑 SDK 集成指南 | 376-400 | 14632-15672 | 849 | `chapters/volcengine/mediakit-guide/3.3.2.2 Web 剪辑 SDK 集成指南.md` |
| 3.3.2.3 | 音视频拼接 | 401-407 | 15673-15855 | 130 | `chapters/volcengine/mediakit-guide/3.3.2.3 音视频拼接.md` |
| 3.3.2.4 | 音视频裁剪 | 408-411 | 15856-16001 | 104 | `chapters/volcengine/mediakit-guide/3.3.2.4 音视频裁剪.md` |
| 3.3.2.5 | 音视频调速 | 412-415 | 16002-16105 | 71 | `chapters/volcengine/mediakit-guide/3.3.2.5 音视频调速.md` |
| 3.3.2.6 | 音频提取 | 416-419 | 16106-16227 | 84 | `chapters/volcengine/mediakit-guide/3.3.2.6 音频提取.md` |
| 3.3.2.7 | 音视频合成 | 420-424 | 16228-16421 | 140 | `chapters/volcengine/mediakit-guide/3.3.2.7 音视频合成.md` |
| 3.3.2.8 | 音频混合 | 425-428 | 16422-16535 | 79 | `chapters/volcengine/mediakit-guide/3.3.2.8 音频混合.md` |
| 3.3.2.9 | 音量调节与淡入淡出 | 429-433 | 16536-16717 | 133 | `chapters/volcengine/mediakit-guide/3.3.2.9 音量调节与淡入淡出.md` |
| 3.3.2.10 | 图片转视频 | 434-440 | 16718-16944 | 170 | `chapters/volcengine/mediakit-guide/3.3.2.10 图片转视频.md` |
| 3.3.2.11 | 视频画面变换 | 441-446 | 16945-17090 | 103 | `chapters/volcengine/mediakit-guide/3.3.2.11 视频画面变换.md` |
| 3.3.2.12 | 视频添加运镜 | 447-452 | 17091-17240 | 109 | `chapters/volcengine/mediakit-guide/3.3.2.12 视频添加运镜.md` |
| 3.3.2.13 | 视频加字幕 | 453-457 | 17241-17403 | 119 | `chapters/volcengine/mediakit-guide/3.3.2.13 视频加字幕.md` |
| 3.3.2.14 | 视频加图片 | 458-461 | 17404-17510 | 75 | `chapters/volcengine/mediakit-guide/3.3.2.14 视频加图片.md` |
| 3.3.2.15 | 视频添加滤镜 | 462-465 | 17511-17621 | 82 | `chapters/volcengine/mediakit-guide/3.3.2.15 视频添加滤镜.md` |
| 3.3.2.16 | 视频截取动图 | 466-469 | 17622-17750 | 94 | `chapters/volcengine/mediakit-guide/3.3.2.16 视频截取动图.md` |
| 3.3.2.17 | 视频高斯模糊 | 470-474 | 17751-17893 | 102 | `chapters/volcengine/mediakit-guide/3.3.2.17 视频高斯模糊.md` |
| 3.3.2.18 | 文字生成滚屏视频 | 475-479 | 17894-18080 | 115 | `chapters/volcengine/mediakit-guide/3.3.2.18 文字生成滚屏视频.md` |
| 3.3.2.19 | 添加 AIGC 元数据标识 | 480-484 | 18081-18231 | 107 | `chapters/volcengine/mediakit-guide/3.3.2.19 添加 AIGC 元数据标识.md` |
| 3.4.1 | 人声背景音分离 | 485-489 | 18233-18425 | 136 | `chapters/volcengine/mediakit-guide/3.4.1 人声背景音分离.md` |
| 3.4.2 | 语音端点识别 | 490-493 | 18426-18576 | 118 | `chapters/volcengine/mediakit-guide/3.4.2 语音端点识别.md` |
| 3.4.3 | 音频内容编辑 | 494-496 | 18577-18690 | 76 | `chapters/volcengine/mediakit-guide/3.4.3 音频内容编辑.md` |
| 3.4.4 | 音频转码 | 497-501 | 18691-18866 | 125 | `chapters/volcengine/mediakit-guide/3.4.4 音频转码.md` |
| 3.5.1 | 视频理解智能策略 | 502-507 | 18868-19135 | 185 | `chapters/volcengine/mediakit-guide/3.5.1 视频理解智能策略.md` |
| 3.5.2 | 大模型高光剪辑 | 508-514 | 19136-19391 | 191 | `chapters/volcengine/mediakit-guide/3.5.2 大模型高光剪辑.md` |
| 3.5.3 | 视频理解拓展工具 | 515-535 | 19392-20263 | 743 | `chapters/volcengine/mediakit-guide/3.5.3 视频理解拓展工具.md` |
| 3.5.4 | 通过 AI MediaKit 调用图片生成大模型 | 536-538 | 20264-20373 | 77 | `chapters/volcengine/mediakit-guide/3.5.4 通过 AI MediaKit 调用图片生成大模型.md` |
| 3.5.5 | 通过 AI MediaKit 调用视频生成大模型 | 539-541 | 20374-20490 | 84 | `chapters/volcengine/mediakit-guide/3.5.5 通过 AI MediaKit 调用视频生成大模型.md` |
| 3.5.6 | 通过 AI MediaKit 调用音频生成大模型 | 542-544 | 20491-20587 | 68 | `chapters/volcengine/mediakit-guide/3.5.6 通过 AI MediaKit 调用音频生成大模型.md` |
| 3.5.7 | 通过 AI MediaKit 调用语音识别大模型 | 545-547 | 20588-20701 | 80 | `chapters/volcengine/mediakit-guide/3.5.7 通过 AI MediaKit 调用语音识别大模型.md` |
| 3.6.1 | 多源媒体输入与本地上传 | 548-553 | 20703-20893 | 139 | `chapters/volcengine/mediakit-guide/3.6.1 多源媒体输入与本地上传.md` |
| 3.6.2 | 处理产物存储至 VOD 或 TOS | 554-558 | 20894-21069 | 102 | `chapters/volcengine/mediakit-guide/3.6.2 处理产物存储至 VOD 或 TOS.md` |
| 3.7 | 项目与队列管理 | 559-563 | 21070-21222 | 80 | `chapters/volcengine/mediakit-guide/3.7 项目与队列管理.md` |
| 4.1 | AI MediaKit CLI 用户指南 | 564-584 | 21224-21936 | 570 | `chapters/volcengine/mediakit-guide/4.1 AI MediaKit CLI 用户指南.md` |
| 4.2 | AI MediaKit Skill 用户指南 | 585-594 | 21937-22261 | 223 | `chapters/volcengine/mediakit-guide/4.2 AI MediaKit Skill 用户指南.md` |
| 4.3 | AI MediaKit MCP 用户指南 | 595-616 | 22262-23413 | 1056 | `chapters/volcengine/mediakit-guide/4.3 AI MediaKit MCP 用户指南.md` |
| 5.1 | 资源包 | 617-621 | 23415-23650 | 154 | `chapters/volcengine/mediakit-guide/5.1 资源包.md` |
| 5.2 | 剪辑工具计费 | 622-624 | 23651-23757 | 73 | `chapters/volcengine/mediakit-guide/5.2 剪辑工具计费.md` |
| 5.3 | 视频工具计费 | 625-651 | 23758-24948 | 983 | `chapters/volcengine/mediakit-guide/5.3 视频工具计费.md` |
| 5.4 | 音频工具计费 | 652-654 | 24949-25046 | 74 | `chapters/volcengine/mediakit-guide/5.4 音频工具计费.md` |
| 5.5 | 图像工具计费 | 655-659 | 25047-25256 | 138 | `chapters/volcengine/mediakit-guide/5.5 图像工具计费.md` |
| 5.6 | 大模型处理工具计费 | 660 | 25257-25267 | 4 | `chapters/volcengine/mediakit-guide/5.6 大模型处理工具计费.md` |
| 5.7 | 计费常见问题 | 661 | 25268-25302 | 18 | `chapters/volcengine/mediakit-guide/5.7 计费常见问题.md` |
| 6.1 | 常见问题 | 662-664 | 25304-25441 | 117 | `chapters/volcengine/mediakit-guide/6.1 常见问题.md` |
| 7.1 | 视频云服务专用条款 | 665-668 | 25443-25580 | 40 | `chapters/volcengine/mediakit-guide/7.1 视频云服务专用条款.md` |
| 7.2 | 智能处理服务计费结算规则 | 669-670 | 25581-25646 | 30 | `chapters/volcengine/mediakit-guide/7.2 智能处理服务计费结算规则.md` |
| 7.3 | 智能处理服务等级协议 | 671-673 | 25647-25721 | 44 | `chapters/volcengine/mediakit-guide/7.3 智能处理服务等级协议.md` |
| 8.1.1 | 概述 | 674 | 25724-25731 | 6 | `chapters/volcengine/mediakit-guide/8.1.1 概述.md` |
| 8.1.2 | 产品优势 | 675 | 25732-25746 | 9 | `chapters/volcengine/mediakit-guide/8.1.2 产品优势.md` |
| 8.1.3 | 应用场景 | 676 | 25747-25765 | 10 | `chapters/volcengine/mediakit-guide/8.1.3 应用场景.md` |
| 8.1.4 | 产品功能 | 677 | 25766-25788 | 14 | `chapters/volcengine/mediakit-guide/8.1.4 产品功能.md` |
| 8.1.5.1 | 老片修复 | 678-679 | 25790-25833 | 23 | `chapters/volcengine/mediakit-guide/8.1.5.1 老片修复.md` |
| 8.1.5.2 | 大模型视频预处理解决方案 | 680 | 25834-25862 | 12 | `chapters/volcengine/mediakit-guide/8.1.5.2 大模型视频预处理解决方案.md` |
| 8.2.1 | 计费概述 | 681-682 | 25864-25889 | 16 | `chapters/volcengine/mediakit-guide/8.2.1 计费概述.md` |
| 8.2.2.1 | 按量计费 | 683-691 | 25891-26125 | 199 | `chapters/volcengine/mediakit-guide/8.2.2.1 按量计费.md` |
| 8.2.2.2 | 资源包 | 692 | 26126-26162 | 23 | `chapters/volcengine/mediakit-guide/8.2.2.2 资源包.md` |
| 8.3.1 | 快速入门 | 693-702 | 26164-26317 | 97 | `chapters/volcengine/mediakit-guide/8.3.1 快速入门.md` |
| 8.4.1 | 控制台简介 | 703-706 | 26319-26396 | 66 | `chapters/volcengine/mediakit-guide/8.4.1 控制台简介.md` |
| 8.4.2 | 概览 | 707-711 | 26397-26468 | 36 | `chapters/volcengine/mediakit-guide/8.4.2 概览.md` |
| 8.4.3 | 任务管理 | 712-715 | 26469-26579 | 74 | `chapters/volcengine/mediakit-guide/8.4.3 任务管理.md` |
| 8.4.4 | 自动任务触发器 | 716-719 | 26580-26639 | 41 | `chapters/volcengine/mediakit-guide/8.4.4 自动任务触发器.md` |
| 8.4.5.1 | 功能概述 | 720-721 | 26641-26729 | 52 | `chapters/volcengine/mediakit-guide/8.4.5.1 功能概述.md` |
| 8.4.5.2.1 | 基础转码 | 722-736 | 26731-27198 | 388 | `chapters/volcengine/mediakit-guide/8.4.5.2.1 基础转码.md` |
| 8.4.5.2.2 | 极智超清 | 737-745 | 27199-27394 | 149 | `chapters/volcengine/mediakit-guide/8.4.5.2.2 极智超清.md` |
| 8.4.5.3.1 | 精细化擦除 | 746-752 | 27396-27484 | 56 | `chapters/volcengine/mediakit-guide/8.4.5.3.1 精细化擦除.md` |
| 8.4.5.4.1 | 画质检测修复 | 753-760 | 27486-27639 | 113 | `chapters/volcengine/mediakit-guide/8.4.5.4.1 画质检测修复.md` |
| 8.4.5.4.2 | 画质增强 | 761-767 | 27640-27738 | 59 | `chapters/volcengine/mediakit-guide/8.4.5.4.2 画质增强.md` |
| 8.4.5.5.1 | 智能识别剪切 | 768-772 | 27740-27808 | 43 | `chapters/volcengine/mediakit-guide/8.4.5.5.1 智能识别剪切.md` |
| 8.4.5.5.2 | 智能表情合成 | 773-781 | 27809-27936 | 82 | `chapters/volcengine/mediakit-guide/8.4.5.5.2 智能表情合成.md` |
| 8.4.5.5.3 | 智能抠图 | 782-788 | 27937-28014 | 51 | `chapters/volcengine/mediakit-guide/8.4.5.5.3 智能抠图.md` |
| 8.4.6 | 工作流模板 | 789-797 | 28015-28296 | 174 | `chapters/volcengine/mediakit-guide/8.4.6 工作流模板.md` |
| 8.4.7.1 | 统计数据 | 798-804 | 28298-28434 | 59 | `chapters/volcengine/mediakit-guide/8.4.7.1 统计数据.md` |
| 8.4.8 | 系统配置 | 805-807 | 28435-28491 | 38 | `chapters/volcengine/mediakit-guide/8.4.8 系统配置.md` |
| 8.4.9 | 媒体处理输出文件路径 | 808-809 | 28492-28531 | 33 | `chapters/volcengine/mediakit-guide/8.4.9 媒体处理输出文件路径.md` |
| 8.5.1 | 使用说明 | 810 | 28533-28567 | 24 | `chapters/volcengine/mediakit-guide/8.5.1 使用说明.md` |
| 8.5.2.1 | 安装 | 811 | 28569-28585 | 12 | `chapters/volcengine/mediakit-guide/8.5.2.1 安装.md` |
| 8.5.2.2 | 初始化 | 812-813 | 28586-28626 | 30 | `chapters/volcengine/mediakit-guide/8.5.2.2 初始化.md` |
| 8.5.2.3 | 媒体处理任务 | 814-817 | 28627-28754 | 120 | `chapters/volcengine/mediakit-guide/8.5.2.3 媒体处理任务.md` |
| 8.5.3.1 | 安装 | 818 | 28756-28765 | 9 | `chapters/volcengine/mediakit-guide/8.5.3.1 安装.md` |
| 8.5.3.2 | 初始化 | 819-820 | 28766-28811 | 35 | `chapters/volcengine/mediakit-guide/8.5.3.2 初始化.md` |
| 8.5.3.3 | 媒体处理任务 | 821-824 | 28812-28961 | 142 | `chapters/volcengine/mediakit-guide/8.5.3.3 媒体处理任务.md` |
| 8.5.4.1 | 安装 | 825 | 28963-28982 | 16 | `chapters/volcengine/mediakit-guide/8.5.4.1 安装.md` |
| 8.5.4.2 | 初始化 | 826-827 | 28983-29028 | 35 | `chapters/volcengine/mediakit-guide/8.5.4.2 初始化.md` |
| 8.5.4.3 | 媒体处理任务 | 828-832 | 29029-29186 | 148 | `chapters/volcengine/mediakit-guide/8.5.4.3 媒体处理任务.md` |
| 8.5.5.1 | 安装 | 833 | 29188-29201 | 13 | `chapters/volcengine/mediakit-guide/8.5.5.1 安装.md` |
| 8.5.5.2 | 初始化 | 834-835 | 29202-29246 | 34 | `chapters/volcengine/mediakit-guide/8.5.5.2 初始化.md` |
| 8.5.5.3 | 媒体处理任务 | 836-839 | 29247-29387 | 132 | `chapters/volcengine/mediakit-guide/8.5.5.3 媒体处理任务.md` |
| 8.6.1 | API 发布历史 | 840-841 | 29389-29480 | 63 | `chapters/volcengine/mediakit-guide/8.6.1 API 发布历史.md` |
| 8.6.2 | API 概览 | 842 | 29481-29491 | 8 | `chapters/volcengine/mediakit-guide/8.6.2 API 概览.md` |
| 8.6.3 | 调用方法 | 843-845 | 29492-29585 | 72 | `chapters/volcengine/mediakit-guide/8.6.3 调用方法.md` |
| 8.6.4 | 公共错误码 | 846-850 | 29586-29681 | 86 | `chapters/volcengine/mediakit-guide/8.6.4 公共错误码.md` |
| 8.6.5.1 | 媒体处理完成事件 | 851-852 | 29683-29747 | 56 | `chapters/volcengine/mediakit-guide/8.6.5.1 媒体处理完成事件.md` |
| 8.6.6.1 | 提交媒体处理任务 | 853-860 | 29749-30080 | 302 | `chapters/volcengine/mediakit-guide/8.6.6.1 提交媒体处理任务.md` |
| 8.6.6.2 | 查询媒体处理任务 | 861-862 | 30081-30159 | 70 | `chapters/volcengine/mediakit-guide/8.6.6.2 查询媒体处理任务.md` |
| 8.6.6.3 | 取消媒体处理任务 | 863-864 | 30160-30208 | 40 | `chapters/volcengine/mediakit-guide/8.6.6.3 取消媒体处理任务.md` |
| 8.6.6.4 | 任务节点输出定义 | 865-870 | 30209-30414 | 174 | `chapters/volcengine/mediakit-guide/8.6.6.4 任务节点输出定义.md` |
| 8.6.6.5 | 任务输出状态码 | 871 | 30415-30434 | 18 | `chapters/volcengine/mediakit-guide/8.6.6.5 任务输出状态码.md` |
| 8.6.7 | 公共数据结构 | 872-888 | 30435-31182 | 641 | `chapters/volcengine/mediakit-guide/8.6.7 公共数据结构.md` |
| 8.7.1 | 联系我们 | 889 | 31184-31195 | 8 | `chapters/volcengine/mediakit-guide/8.7.1 联系我们.md` |
