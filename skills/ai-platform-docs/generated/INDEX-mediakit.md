# AI MediaKit API 区章节表（mediakit）

来源：《AI MediaKit API 参考》（1040 页）。107 个章节文件，接口级切分：一个接口/任务一个文件；超过 1500 行的按语义块自动再拆为`… - 第N部分`（1 个章节被拆分）。

「页码」是原 PDF 页码范围；「行范围」是中间 MD（`doc/<源文档>.md`）的 1 起始行号，可据此回查原文。章节文件本身已去掉页眉页脚，回查 PDF 时用这两列。文件名即章节标题，日常定位直接 Glob 文件名即可，用不到这两列。

**这张表用来 grep，不要整读。**

| 编号 | 标题 | 页码 | 行范围(源文件) | 行数 | 文件 |
|------|------|------|---------------|------|------|
| 1.1 | 基础概念及准备工作 | 1-4 | 145-295 | 83 | `chapters/volcengine/mediakit/1.1 基础概念及准备工作.md` |
| 2.1 | 提交画质增强（大模型版）任务 API | 5-14 | 297-752 | 405 | `chapters/volcengine/mediakit/2.1 提交画质增强（大模型版）任务 API.md` |
| 2.2 | 提交画质增强（标准版和专业版）任务 API | 15-34 | 753-1756 | 891 | `chapters/volcengine/mediakit/2.2 提交画质增强（标准版和专业版）任务 API.md` |
| 2.3 | 提交画质增强（极速版）任务 API | 35-44 | 1757-2231 | 419 | `chapters/volcengine/mediakit/2.3 提交画质增强（极速版）任务 API.md` |
| 2.4 | 提交字幕擦除（精细化版）任务 API | 45-62 | 2232-3081 | 772 | `chapters/volcengine/mediakit/2.4 提交字幕擦除（精细化版）任务 API.md` |
| 2.5 | 提交字幕擦除（标准版）任务 API | 63-69 | 3082-3400 | 286 | `chapters/volcengine/mediakit/2.5 提交字幕擦除（标准版）任务 API.md` |
| 2.6 | 提交语音转字幕（ASR）任务 API | 70-77 | 3401-3783 | 344 | `chapters/volcengine/mediakit/2.6 提交语音转字幕（ASR）任务 API.md` |
| 2.7 | 提交视频识别字幕（OCR）任务 API | 78-85 | 3784-4117 | 300 | `chapters/volcengine/mediakit/2.7 提交视频识别字幕（OCR）任务 API.md` |
| 2.8 | 提交场景切分任务 API | 86-96 | 4118-4617 | 453 | `chapters/volcengine/mediakit/2.8 提交场景切分任务 API.md` |
| 2.9 | 提交智能语义切片（基础版）任务 API | 97-105 | 4618-5013 | 360 | `chapters/volcengine/mediakit/2.9 提交智能语义切片（基础版）任务 API.md` |
| 2.10 | 提交高光智剪（短剧）任务 API | 106-124 | 5014-5904 | 808 | `chapters/volcengine/mediakit/2.10 提交高光智剪（短剧）任务 API.md` |
| 2.11 | 提交高光智剪（小游戏）任务 API | 125-134 | 5905-6360 | 410 | `chapters/volcengine/mediakit/2.11 提交高光智剪（小游戏）任务 API.md` |
| 2.12 | 提交高光智剪（影视拆条）任务 API | 135-147 | 6361-6974 | 560 | `chapters/volcengine/mediakit/2.12 提交高光智剪（影视拆条）任务 API.md` |
| 2.13 | 提交高光片段提取任务 API | 148-156 | 6975-7335 | 319 | `chapters/volcengine/mediakit/2.13 提交高光片段提取任务 API.md` |
| 2.14 | 提交视频绿幕抠图任务 API | 157-164 | 7336-7709 | 333 | `chapters/volcengine/mediakit/2.14 提交视频绿幕抠图任务 API.md` |
| 2.15 | 提交视频人像抠图任务 API | 165-172 | 7710-8066 | 318 | `chapters/volcengine/mediakit/2.15 提交视频人像抠图任务 API.md` |
| 2.16 | 提交剧情故事线分析任务 API | 173-181 | 8067-8412 | 306 | `chapters/volcengine/mediakit/2.16 提交剧情故事线分析任务 API.md` |
| 2.17 | 提交视频元信息获取任务 API | 182-188 | 8413-8692 | 252 | `chapters/volcengine/mediakit/2.17 提交视频元信息获取任务 API.md` |
| 2.18 | 提交剧本还原任务 API | 189-200 | 8693-9287 | 538 | `chapters/volcengine/mediakit/2.18 提交剧本还原任务 API.md` |
| 2.19 | 提交解说视频生成任务 API | 201-215 | 9288-10004 | 635 | `chapters/volcengine/mediakit/2.19 提交解说视频生成任务 API.md` |
| 2.20 | 提交解说视频生成（短剧行业模型）任务 API | 216-231 | 10005-10770 | 673 | `chapters/volcengine/mediakit/2.20 提交解说视频生成（短剧行业模型）任务 API.md` |
| 2.21 | 提交视频抽帧任务 API | 232-244 | 10771-11382 | 556 | `chapters/volcengine/mediakit/2.21 提交视频抽帧任务 API.md` |
| 2.22 | 提交视频暗水印添加任务 API | 245-252 | 11383-11763 | 339 | `chapters/volcengine/mediakit/2.22 提交视频暗水印添加任务 API.md` |
| 2.23 | 提交视频暗水印提取任务 API | 253-258 | 11764-11992 | 200 | `chapters/volcengine/mediakit/2.23 提交视频暗水印提取任务 API.md` |
| 2.24 | 提交视频转码任务 API | 259-276 | 11993-12886 | 817 | `chapters/volcengine/mediakit/2.24 提交视频转码任务 API.md` |
| 2.25 | 提交极智超清任务 API | 277-293 | 12887-13763 | 799 | `chapters/volcengine/mediakit/2.25 提交极智超清任务 API.md` |
| 2.26 | 提交视频转封装任务 API | 294-301 | 13764-14109 | 311 | `chapters/volcengine/mediakit/2.26 提交视频转封装任务 API.md` |
| 2.27 | 提交视频画质检测 VQScore 任务 API | 302-307 | 14110-14349 | 209 | `chapters/volcengine/mediakit/2.27 提交视频画质检测 VQScore 任务 API.md` |
| 2.28 | 提交视频人脸打码任务 API | 308-315 | 14350-14722 | 334 | `chapters/volcengine/mediakit/2.28 提交视频人脸打码任务 API.md` |
| 2.29 | 提交视频人脸融合（换脸）任务 API | 316-323 | 14723-15101 | 339 | `chapters/volcengine/mediakit/2.29 提交视频人脸融合（换脸）任务 API.md` |
| 2.30 | 提交视频插帧任务 API | 324-330 | 15102-15431 | 297 | `chapters/volcengine/mediakit/2.30 提交视频插帧任务 API.md` |
| 2.31 | 提交视频口型对齐任务 API | 331-339 | 15432-15860 | 386 | `chapters/volcengine/mediakit/2.31 提交视频口型对齐任务 API.md` |
| 2.32 | 提交视频横转竖任务 API | 340-348 | 15861-16221 | 317 | `chapters/volcengine/mediakit/2.32 提交视频横转竖任务 API.md` |
| 2.33 | 提交视频流畅度提升任务 API | 349-358 | 16222-16701 | 426 | `chapters/volcengine/mediakit/2.33 提交视频流畅度提升任务 API.md` |
| 2.34 | 提交智能语义切片（专业版）任务 API | 359-371 | 16702-17316 | 558 | `chapters/volcengine/mediakit/2.34 提交智能语义切片（专业版）任务 API.md` |
| 2.35 | 提交智能精准字幕识别任务 API | 372-383 | 17317-17904 | 501 | `chapters/volcengine/mediakit/2.35 提交智能精准字幕识别任务 API.md` |
| 2.36 | 提交深度动作捕捉任务 API | 384-390 | 17905-18242 | 306 | `chapters/volcengine/mediakit/2.36 提交深度动作捕捉任务 API.md` |
| 2.37 | 提交智能擦除任务 API | 391-403 | 18243-18820 | 516 | `chapters/volcengine/mediakit/2.37 提交智能擦除任务 API.md` |
| 3.1 | 提交图像画质增强任务 API | 404-414 | 18822-19353 | 480 | `chapters/volcengine/mediakit/3.1 提交图像画质增强任务 API.md` |
| 3.2 | 提交图像画质评估任务 API | 415-424 | 19354-19804 | 391 | `chapters/volcengine/mediakit/3.2 提交图像画质评估任务 API.md` |
| 3.3 | 提交图像人脸打码任务 API | 425-430 | 19805-20045 | 216 | `chapters/volcengine/mediakit/3.3 提交图像人脸打码任务 API.md` |
| 3.4 | 提交图像擦除修复任务 API | 431-440 | 20046-20475 | 386 | `chapters/volcengine/mediakit/3.4 提交图像擦除修复任务 API.md` |
| 3.5 | 提交图像背景移除任务 API | 441-449 | 20476-20859 | 347 | `chapters/volcengine/mediakit/3.5 提交图像背景移除任务 API.md` |
| 3.6 | 提交图像智能裁剪任务 API | 450-455 | 20860-21112 | 226 | `chapters/volcengine/mediakit/3.6 提交图像智能裁剪任务 API.md` |
| 3.7 | 提交智能扩图任务 API | 456-461 | 21113-21378 | 243 | `chapters/volcengine/mediakit/3.7 提交智能扩图任务 API.md` |
| 3.8 | 提交集智瘦身任务 API | 462-467 | 21379-21617 | 214 | `chapters/volcengine/mediakit/3.8 提交集智瘦身任务 API.md` |
| 3.9 | 提交电商牛皮癣擦除任务 API | 468-471 | 21618-21784 | 147 | `chapters/volcengine/mediakit/3.9 提交电商牛皮癣擦除任务 API.md` |
| 3.10 | 提交图像元信息获取任务 API | 472-478 | 21785-22094 | 269 | `chapters/volcengine/mediakit/3.10 提交图像元信息获取任务 API.md` |
| 3.11 | 提交图像暗水印添加任务 API | 479-485 | 22095-22405 | 281 | `chapters/volcengine/mediakit/3.11 提交图像暗水印添加任务 API.md` |
| 3.12 | 提交图像暗水印提取任务 API | 486-490 | 22406-22614 | 188 | `chapters/volcengine/mediakit/3.12 提交图像暗水印提取任务 API.md` |
| 3.13.1 | 提交圆角矩形任务 API | 491-496 | 22616-22876 | 233 | `chapters/volcengine/mediakit/3.13.1 提交圆角矩形任务 API.md` |
| 3.13.2 | 提交图像旋转任务 API | 497-501 | 22877-23102 | 200 | `chapters/volcengine/mediakit/3.13.2 提交图像旋转任务 API.md` |
| 3.13.3 | 提交图像翻转任务 API | 502-506 | 23103-23315 | 189 | `chapters/volcengine/mediakit/3.13.3 提交图像翻转任务 API.md` |
| 3.13.4 | 提交图像锐化任务 API | 507-511 | 23316-23530 | 190 | `chapters/volcengine/mediakit/3.13.4 提交图像锐化任务 API.md` |
| 3.13.5 | 提交图像高斯模糊任务 API | 512-516 | 23531-23746 | 193 | `chapters/volcengine/mediakit/3.13.5 提交图像高斯模糊任务 API.md` |
| 3.13.6 | 提交图像打码任务 API | 517-523 | 23747-24057 | 277 | `chapters/volcengine/mediakit/3.13.6 提交图像打码任务 API.md` |
| 3.13.7 | 提交图像添加图文水印任务 API | 524-533 | 24058-24508 | 400 | `chapters/volcengine/mediakit/3.13.7 提交图像添加图文水印任务 API.md` |
| 3.13.8 | 提交图像缩放任务 API | 534-540 | 24509-24837 | 292 | `chapters/volcengine/mediakit/3.13.8 提交图像缩放任务 API.md` |
| 3.13.9 | 提交图像调整任务 API | 541-546 | 24838-25067 | 202 | `chapters/volcengine/mediakit/3.13.9 提交图像调整任务 API.md` |
| 3.13.10 | 提交图像裁剪任务 API | 547-555 | 25068-25470 | 357 | `chapters/volcengine/mediakit/3.13.10 提交图像裁剪任务 API.md` |
| 3.13.11 | 提交图像压缩任务 API | 556-562 | 25471-25760 | 261 | `chapters/volcengine/mediakit/3.13.11 提交图像压缩任务 API.md` |
| 3.13.12 | 提交图像负片任务 API | 563-567 | 25761-25964 | 181 | `chapters/volcengine/mediakit/3.13.12 提交图像负片任务 API.md` |
| 4.1 | 提交 Agent 智能剪辑任务 API | 568-582 | 25966-26659 | 614 | `chapters/volcengine/mediakit/4.1 提交 Agent 智能剪辑任务 API.md` |
| 4.2 | 提交 HyperFrames 云端渲染任务 API | 583-589 | 26660-26979 | 284 | `chapters/volcengine/mediakit/4.2 提交 HyperFrames 云端渲染任务 API.md` |
| 4.3 | 提交多轨道剪辑任务 API | 590-616 | 26980-28270 | 1193 | `chapters/volcengine/mediakit/4.3 提交多轨道剪辑任务 API.md` |
| 4.4 | 提交视频拼接任务 API | 617-625 | 28271-28656 | 346 | `chapters/volcengine/mediakit/4.4 提交视频拼接任务 API.md` |
| 4.5 | 提交音频拼接任务 API | 626-632 | 28657-28962 | 275 | `chapters/volcengine/mediakit/4.5 提交音频拼接任务 API.md` |
| 4.6 | 提交视频裁剪任务 API | 633-640 | 28963-29307 | 311 | `chapters/volcengine/mediakit/4.6 提交视频裁剪任务 API.md` |
| 4.7 | 提交音频裁剪任务 API | 641-647 | 29308-29621 | 285 | `chapters/volcengine/mediakit/4.7 提交音频裁剪任务 API.md` |
| 4.8 | 提交音频提取任务 API | 648-654 | 29622-29927 | 276 | `chapters/volcengine/mediakit/4.8 提交音频提取任务 API.md` |
| 4.9 | 提交音视频合成任务 API | 655-663 | 29928-30360 | 382 | `chapters/volcengine/mediakit/4.9 提交音视频合成任务 API.md` |
| 4.10 | 提交图片转视频任务 API | 664-673 | 30361-30773 | 367 | `chapters/volcengine/mediakit/4.10 提交图片转视频任务 API.md` |
| 4.11 | 提交视频画面翻转任务 API | 674-681 | 30774-31146 | 340 | `chapters/volcengine/mediakit/4.11 提交视频画面翻转任务 API.md` |
| 4.12 | 提交视频画面旋转任务 API | 682-689 | 31147-31495 | 311 | `chapters/volcengine/mediakit/4.12 提交视频画面旋转任务 API.md` |
| 4.13 | 提交视频画面裁剪任务 API | 690-698 | 31496-31898 | 362 | `chapters/volcengine/mediakit/4.13 提交视频画面裁剪任务 API.md` |
| 4.14 | 提交视频画面拼接任务 API | 699-706 | 31899-32268 | 333 | `chapters/volcengine/mediakit/4.14 提交视频画面拼接任务 API.md` |
| 4.15 | 提交视频调速任务 API | 707-713 | 32269-32609 | 308 | `chapters/volcengine/mediakit/4.15 提交视频调速任务 API.md` |
| 4.16 | 提交音频调速任务 API | 714-720 | 32610-32918 | 281 | `chapters/volcengine/mediakit/4.16 提交音频调速任务 API.md` |
| 4.17 | 提交音频混合任务 API | 721-727 | 32919-33228 | 280 | `chapters/volcengine/mediakit/4.17 提交音频混合任务 API.md` |
| 4.18 | 提交视频加字幕任务 API | 728-740 | 33229-33762 | 481 | `chapters/volcengine/mediakit/4.18 提交视频加字幕任务 API.md` |
| 4.19 | 提交视频加图片任务 API | 741-749 | 33763-34188 | 388 | `chapters/volcengine/mediakit/4.19 提交视频加图片任务 API.md` |
| 4.20 | 提交视频声音淡入淡出任务 API | 750-757 | 34189-34535 | 312 | `chapters/volcengine/mediakit/4.20 提交视频声音淡入淡出任务 API.md` |
| 4.21 | 提交音频声音淡入淡出任务 API | 758-764 | 34536-34870 | 304 | `chapters/volcengine/mediakit/4.21 提交音频声音淡入淡出任务 API.md` |
| 4.22 | 提交调整视频音量任务 API | 765-772 | 34871-35224 | 315 | `chapters/volcengine/mediakit/4.22 提交调整视频音量任务 API.md` |
| 4.23 | 提交视频添加滤镜任务 API | 773-779 | 35225-35554 | 294 | `chapters/volcengine/mediakit/4.23 提交视频添加滤镜任务 API.md` |
| 4.24 | 提交视频截取动图任务 API | 780-787 | 35555-35901 | 315 | `chapters/volcengine/mediakit/4.24 提交视频截取动图任务 API.md` |
| 4.25 | 提交视频添加运镜任务 API | 788-794 | 35902-36213 | 275 | `chapters/volcengine/mediakit/4.25 提交视频添加运镜任务 API.md` |
| 4.26 | 提交视频高斯模糊任务 API | 795-803 | 36214-36619 | 363 | `chapters/volcengine/mediakit/4.26 提交视频高斯模糊任务 API.md` |
| 4.27 | 提交文字生成滚屏视频任务 API | 804-814 | 36620-37161 | 466 | `chapters/volcengine/mediakit/4.27 提交文字生成滚屏视频任务 API.md` |
| 4.28 | 提交添加 AIGC 元数据标识任务 API | 815-825 | 37162-37726 | 512 | `chapters/volcengine/mediakit/4.28 提交添加 AIGC 元数据标识任务 API.md` |
| 4.29 | 提交智能剪辑任务 API（旧版） | 826-857 | 37727-38963 | 1137 | `chapters/volcengine/mediakit/4.29 提交智能剪辑任务 API（旧版）.md` |
| 5.1 | 提交人声背景音分离任务 API | 858-868 | 38965-39492 | 471 | `chapters/volcengine/mediakit/5.1 提交人声背景音分离任务 API.md` |
| 5.2 | 提交语音端点识别任务 API | 869-875 | 39493-39786 | 264 | `chapters/volcengine/mediakit/5.2 提交语音端点识别任务 API.md` |
| 5.3 | 提交音频转码任务 API | 876-886 | 39787-40307 | 470 | `chapters/volcengine/mediakit/5.3 提交音频转码任务 API.md` |
| 5.4 | 提交音频元信息获取任务 API | 887-892 | 40308-40556 | 224 | `chapters/volcengine/mediakit/5.4 提交音频元信息获取任务 API.md` |
| 5.5 | 提交音频内容编辑任务 API | 893-903 | 40557-41102 | 490 | `chapters/volcengine/mediakit/5.5 提交音频内容编辑任务 API.md` |
| 6.1 | 提交大模型高光剪辑任务 API | 904-929 | 41104-42356 | 1145 | `chapters/volcengine/mediakit/6.1 提交大模型高光剪辑任务 API.md` |
| 6.2 | 提交视频理解智能策略任务 API | 930-940 | 42357-42904 | 485 | `chapters/volcengine/mediakit/6.2 提交视频理解智能策略任务 API.md` |
| 6.3 | 对话 Chat API - 第1部分 | 941-977 | 42905-44802 | 1725 | `chapters/volcengine/mediakit/6.3 对话 Chat API - 第1部分.md` |
| 6.3 | 对话 Chat API - 第2部分·响应参数 | 978-998 | 44803-45655 | 749 | `chapters/volcengine/mediakit/6.3 对话 Chat API - 第2部分·响应参数.md` |
| 6.4 | MaaS 模型代理 API | 999-1009 | 45656-46156 | 439 | `chapters/volcengine/mediakit/6.4 MaaS 模型代理 API.md` |
| 6.5 | 提交 AIGC 视频质量评估任务 API | 1010-1020 | 46157-46672 | 451 | `chapters/volcengine/mediakit/6.5 提交 AIGC 视频质量评估任务 API.md` |
| 7.1 | 获取媒体上传地址 API | 1021-1024 | 46674-46810 | 105 | `chapters/volcengine/mediakit/7.1 获取媒体上传地址 API.md` |
| 7.2 | 查询任务信息 API | 1025-1029 | 46811-46982 | 143 | `chapters/volcengine/mediakit/7.2 查询任务信息 API.md` |
| 7.3 | 取消异步任务 API | 1030-1033 | 46983-47125 | 123 | `chapters/volcengine/mediakit/7.3 取消异步任务 API.md` |
| 7.4 | 事件回调 | 1034-1037 | 47126-47295 | 134 | `chapters/volcengine/mediakit/7.4 事件回调.md` |
| 7.5 | 错误码 | 1038-1040 | 47296-47436 | 124 | `chapters/volcengine/mediakit/7.5 错误码.md` |
