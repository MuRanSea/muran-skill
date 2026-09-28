# AI MediaKit API 区章节表（mediakit）

来源：《AI MediaKit API 参考》（931 页）。102 个章节文件，接口级切分：一个接口/任务一个文件；超过 1500 行的按语义块自动再拆为`… - 第N部分`（0 个章节被拆分）。

「页码」是原 PDF 页码范围；「行范围」是中间 MD（`doc/<源文档>.md`）的 1 起始行号，可据此回查原文。章节文件本身已去掉页眉页脚，回查 PDF 时用这两列。文件名即章节标题，日常定位直接 Glob 文件名即可，用不到这两列。

**这张表用来 grep，不要整读。**

| 编号 | 标题 | 页码 | 行范围(源文件) | 行数 | 文件 |
|------|------|------|---------------|------|------|
| 1.1 | 基础概念及准备工作 | 1-4 | 139-288 | 84 | `chapters/volcengine/mediakit/1.1 基础概念及准备工作.md` |
| 2.1 | 提交画质增强（大模型版）任务 API | 5-14 | 290-745 | 405 | `chapters/volcengine/mediakit/2.1 提交画质增强（大模型版）任务 API.md` |
| 2.2 | 提交画质增强（标准版和专业版）任务 API | 15-28 | 746-1458 | 628 | `chapters/volcengine/mediakit/2.2 提交画质增强（标准版和专业版）任务 API.md` |
| 2.3 | 提交画质增强（极速版）任务 API | 29-38 | 1459-1933 | 419 | `chapters/volcengine/mediakit/2.3 提交画质增强（极速版）任务 API.md` |
| 2.4 | 提交字幕擦除（精细化版）任务 API | 39-55 | 1934-2722 | 717 | `chapters/volcengine/mediakit/2.4 提交字幕擦除（精细化版）任务 API.md` |
| 2.5 | 提交字幕擦除（标准版）任务 API | 56-62 | 2723-3041 | 286 | `chapters/volcengine/mediakit/2.5 提交字幕擦除（标准版）任务 API.md` |
| 2.6 | 提交语音转字幕（ASR）任务 API | 63-70 | 3042-3394 | 313 | `chapters/volcengine/mediakit/2.6 提交语音转字幕（ASR）任务 API.md` |
| 2.7 | 提交视频识别字幕（OCR）任务 API | 71-78 | 3395-3702 | 276 | `chapters/volcengine/mediakit/2.7 提交视频识别字幕（OCR）任务 API.md` |
| 2.8 | 提交场景切分任务 API | 79-86 | 3703-4068 | 330 | `chapters/volcengine/mediakit/2.8 提交场景切分任务 API.md` |
| 2.9 | 提交智能语义切片（基础版）任务 API | 87-95 | 4069-4464 | 360 | `chapters/volcengine/mediakit/2.9 提交智能语义切片（基础版）任务 API.md` |
| 2.10 | 提交智能语义切片（专业版）任务 API | 96-108 | 4465-5079 | 558 | `chapters/volcengine/mediakit/2.10 提交智能语义切片（专业版）任务 API.md` |
| 2.11 | 提交高光智剪（短剧）任务 API | 109-126 | 5080-5937 | 781 | `chapters/volcengine/mediakit/2.11 提交高光智剪（短剧）任务 API.md` |
| 2.12 | 提交高光智剪（小游戏）任务 API | 127-136 | 5938-6393 | 410 | `chapters/volcengine/mediakit/2.12 提交高光智剪（小游戏）任务 API.md` |
| 2.13 | 提交高光智剪（影视拆条）任务 API | 137-148 | 6394-6978 | 534 | `chapters/volcengine/mediakit/2.13 提交高光智剪（影视拆条）任务 API.md` |
| 2.14 | 提交高光片段提取任务 API | 149-156 | 6979-7314 | 298 | `chapters/volcengine/mediakit/2.14 提交高光片段提取任务 API.md` |
| 2.15 | 提交视频绿幕抠图任务 API | 157-164 | 7315-7688 | 333 | `chapters/volcengine/mediakit/2.15 提交视频绿幕抠图任务 API.md` |
| 2.16 | 提交视频人像抠图任务 API | 165-172 | 7689-8045 | 318 | `chapters/volcengine/mediakit/2.16 提交视频人像抠图任务 API.md` |
| 2.17 | 提交剧情故事线分析任务 API | 173-180 | 8046-8363 | 283 | `chapters/volcengine/mediakit/2.17 提交剧情故事线分析任务 API.md` |
| 2.18 | 提交视频元信息获取任务 API | 181-187 | 8364-8643 | 252 | `chapters/volcengine/mediakit/2.18 提交视频元信息获取任务 API.md` |
| 2.19 | 提交剧本还原任务 API | 188-196 | 8644-9080 | 396 | `chapters/volcengine/mediakit/2.19 提交剧本还原任务 API.md` |
| 2.20 | 提交剧本还原（重绘场景）任务 API | 197-207 | 9081-9599 | 440 | `chapters/volcengine/mediakit/2.20 提交剧本还原（重绘场景）任务 API.md` |
| 2.21 | 提交解说视频生成任务 API | 208-221 | 9600-10285 | 611 | `chapters/volcengine/mediakit/2.21 提交解说视频生成任务 API.md` |
| 2.22 | 提交解说视频生成（短剧行业模型）任务 API | 222-237 | 10286-11048 | 670 | `chapters/volcengine/mediakit/2.22 提交解说视频生成（短剧行业模型）任务 API.md` |
| 2.23 | 提交视频抽帧任务 API | 238-248 | 11049-11560 | 464 | `chapters/volcengine/mediakit/2.23 提交视频抽帧任务 API.md` |
| 2.24 | 提交视频暗水印添加任务 API | 249-256 | 11561-11941 | 339 | `chapters/volcengine/mediakit/2.24 提交视频暗水印添加任务 API.md` |
| 2.25 | 提交视频暗水印提取任务 API | 257-261 | 11942-12141 | 177 | `chapters/volcengine/mediakit/2.25 提交视频暗水印提取任务 API.md` |
| 2.26 | 提交视频转码任务 API | 262-278 | 12142-12990 | 776 | `chapters/volcengine/mediakit/2.26 提交视频转码任务 API.md` |
| 2.27 | 提交极智超清任务 API | 279-295 | 12991-13867 | 799 | `chapters/volcengine/mediakit/2.27 提交极智超清任务 API.md` |
| 2.28 | 提交视频转封装任务 API | 296-302 | 13868-14183 | 288 | `chapters/volcengine/mediakit/2.28 提交视频转封装任务 API.md` |
| 2.29 | 提交视频画质检测 VQScore 任务 API | 303-307 | 14184-14392 | 182 | `chapters/volcengine/mediakit/2.29 提交视频画质检测 VQScore 任务 API.md` |
| 2.30 | 提交视频人脸打码任务 API | 308-315 | 14393-14769 | 337 | `chapters/volcengine/mediakit/2.30 提交视频人脸打码任务 API.md` |
| 2.31 | 提交视频人脸融合（换脸）任务 API | 316-323 | 14770-15148 | 339 | `chapters/volcengine/mediakit/2.31 提交视频人脸融合（换脸）任务 API.md` |
| 2.32 | 提交视频插帧任务 API | 324-330 | 15149-15478 | 297 | `chapters/volcengine/mediakit/2.32 提交视频插帧任务 API.md` |
| 2.33 | 提交视频口型对齐任务 API | 331-339 | 15479-15907 | 386 | `chapters/volcengine/mediakit/2.33 提交视频口型对齐任务 API.md` |
| 2.34 | 提交视频横转竖任务 API | 340-348 | 15908-16268 | 317 | `chapters/volcengine/mediakit/2.34 提交视频横转竖任务 API.md` |
| 2.35 | 提交视频流畅度提升任务 API | 349-358 | 16269-16748 | 427 | `chapters/volcengine/mediakit/2.35 提交视频流畅度提升任务 API.md` |
| 3.1 | 提交图像画质增强任务 API | 359-370 | 16750-17284 | 481 | `chapters/volcengine/mediakit/3.1 提交图像画质增强任务 API.md` |
| 3.2 | 提交图像画质评估任务 API | 371-380 | 17285-17736 | 392 | `chapters/volcengine/mediakit/3.2 提交图像画质评估任务 API.md` |
| 3.3 | 提交图像人脸打码任务 API | 381-386 | 17737-17977 | 216 | `chapters/volcengine/mediakit/3.3 提交图像人脸打码任务 API.md` |
| 3.4 | 提交图像擦除修复任务 API | 387-396 | 17978-18407 | 386 | `chapters/volcengine/mediakit/3.4 提交图像擦除修复任务 API.md` |
| 3.5 | 提交图像背景移除任务 API | 397-405 | 18408-18791 | 347 | `chapters/volcengine/mediakit/3.5 提交图像背景移除任务 API.md` |
| 3.6 | 提交图像文字识别（OCR）任务 API | 406-414 | 18792-19189 | 364 | `chapters/volcengine/mediakit/3.6 提交图像文字识别（OCR）任务 API.md` |
| 3.7 | 提交图像智能裁剪任务 API | 415-420 | 19190-19442 | 226 | `chapters/volcengine/mediakit/3.7 提交图像智能裁剪任务 API.md` |
| 3.8 | 提交智能扩图任务 API | 421-426 | 19443-19708 | 243 | `chapters/volcengine/mediakit/3.8 提交智能扩图任务 API.md` |
| 3.9 | 提交集智瘦身任务 API | 427-432 | 19709-19947 | 214 | `chapters/volcengine/mediakit/3.9 提交集智瘦身任务 API.md` |
| 3.10 | 提交图像翻译任务 API | 433-441 | 19948-20297 | 313 | `chapters/volcengine/mediakit/3.10 提交图像翻译任务 API.md` |
| 3.11 | 提交电商牛皮癣擦除任务 API | 442-445 | 20298-20464 | 147 | `chapters/volcengine/mediakit/3.11 提交电商牛皮癣擦除任务 API.md` |
| 3.12 | 提交电商万创（商品场景图生成）任务 API | 446-457 | 20465-21016 | 504 | `chapters/volcengine/mediakit/3.12 提交电商万创（商品场景图生成）任务 API.md` |
| 3.13 | 提交图像元信息获取任务 API | 458-464 | 21017-21326 | 269 | `chapters/volcengine/mediakit/3.13 提交图像元信息获取任务 API.md` |
| 3.14 | 提交图像暗水印添加任务 API | 465-471 | 21327-21637 | 281 | `chapters/volcengine/mediakit/3.14 提交图像暗水印添加任务 API.md` |
| 3.15 | 提交图像暗水印提取任务 API | 472-476 | 21638-21846 | 188 | `chapters/volcengine/mediakit/3.15 提交图像暗水印提取任务 API.md` |
| 3.16.1 | 提交圆角矩形任务 API | 477-482 | 21848-22108 | 233 | `chapters/volcengine/mediakit/3.16.1 提交圆角矩形任务 API.md` |
| 3.16.2 | 提交图像旋转任务 API | 483-487 | 22109-22334 | 200 | `chapters/volcengine/mediakit/3.16.2 提交图像旋转任务 API.md` |
| 3.16.3 | 提交图像翻转任务 API | 488-492 | 22335-22547 | 189 | `chapters/volcengine/mediakit/3.16.3 提交图像翻转任务 API.md` |
| 3.16.4 | 提交图像锐化任务 API | 493-497 | 22548-22762 | 190 | `chapters/volcengine/mediakit/3.16.4 提交图像锐化任务 API.md` |
| 3.16.5 | 提交图像高斯模糊任务 API | 498-502 | 22763-22978 | 193 | `chapters/volcengine/mediakit/3.16.5 提交图像高斯模糊任务 API.md` |
| 3.16.6 | 提交图像打码任务 API | 503-509 | 22979-23289 | 277 | `chapters/volcengine/mediakit/3.16.6 提交图像打码任务 API.md` |
| 3.16.7 | 提交图像添加图文水印任务 API | 510-519 | 23290-23740 | 400 | `chapters/volcengine/mediakit/3.16.7 提交图像添加图文水印任务 API.md` |
| 3.16.8 | 提交图像缩放任务 API | 520-526 | 23741-24069 | 292 | `chapters/volcengine/mediakit/3.16.8 提交图像缩放任务 API.md` |
| 3.16.9 | 提交图像调整任务 API | 527-532 | 24070-24299 | 202 | `chapters/volcengine/mediakit/3.16.9 提交图像调整任务 API.md` |
| 3.16.10 | 提交图像裁剪任务 API | 533-541 | 24300-24698 | 353 | `chapters/volcengine/mediakit/3.16.10 提交图像裁剪任务 API.md` |
| 3.16.11 | 提交图像压缩任务 API | 542-548 | 24699-24988 | 261 | `chapters/volcengine/mediakit/3.16.11 提交图像压缩任务 API.md` |
| 3.16.12 | 提交图像负片任务 API | 549-553 | 24989-25192 | 181 | `chapters/volcengine/mediakit/3.16.12 提交图像负片任务 API.md` |
| 4.1 | 提交智能剪辑任务 API | 554-585 | 25194-26426 | 1137 | `chapters/volcengine/mediakit/4.1 提交智能剪辑任务 API.md` |
| 4.2 | 提交视频拼接任务 API | 586-594 | 26427-26812 | 346 | `chapters/volcengine/mediakit/4.2 提交视频拼接任务 API.md` |
| 4.3 | 提交音频拼接任务 API | 595-601 | 26813-27118 | 275 | `chapters/volcengine/mediakit/4.3 提交音频拼接任务 API.md` |
| 4.4 | 提交视频裁剪任务 API | 602-608 | 27119-27436 | 288 | `chapters/volcengine/mediakit/4.4 提交视频裁剪任务 API.md` |
| 4.5 | 提交音频裁剪任务 API | 609-615 | 27437-27750 | 285 | `chapters/volcengine/mediakit/4.5 提交音频裁剪任务 API.md` |
| 4.6 | 提交音频提取任务 API | 616-622 | 27751-28056 | 276 | `chapters/volcengine/mediakit/4.6 提交音频提取任务 API.md` |
| 4.7 | 提交音视频合成任务 API | 623-631 | 28057-28489 | 382 | `chapters/volcengine/mediakit/4.7 提交音视频合成任务 API.md` |
| 4.8 | 提交图片转视频任务 API | 632-641 | 28490-28902 | 367 | `chapters/volcengine/mediakit/4.8 提交图片转视频任务 API.md` |
| 4.9 | 提交视频画面翻转任务 API | 642-648 | 28903-29249 | 318 | `chapters/volcengine/mediakit/4.9 提交视频画面翻转任务 API.md` |
| 4.10 | 提交视频画面旋转任务 API | 649-655 | 29250-29570 | 287 | `chapters/volcengine/mediakit/4.10 提交视频画面旋转任务 API.md` |
| 4.11 | 提交视频画面裁剪任务 API | 656-664 | 29571-29949 | 341 | `chapters/volcengine/mediakit/4.11 提交视频画面裁剪任务 API.md` |
| 4.12 | 提交视频画面拼接任务 API | 665-672 | 29950-30319 | 333 | `chapters/volcengine/mediakit/4.12 提交视频画面拼接任务 API.md` |
| 4.13 | 提交视频调速任务 API | 673-679 | 30320-30660 | 308 | `chapters/volcengine/mediakit/4.13 提交视频调速任务 API.md` |
| 4.14 | 提交音频调速任务 API | 680-686 | 30661-30969 | 281 | `chapters/volcengine/mediakit/4.14 提交音频调速任务 API.md` |
| 4.15 | 提交音频混合任务 API | 687-693 | 30970-31279 | 280 | `chapters/volcengine/mediakit/4.15 提交音频混合任务 API.md` |
| 4.16 | 提交视频加字幕任务 API | 694-706 | 31280-31813 | 481 | `chapters/volcengine/mediakit/4.16 提交视频加字幕任务 API.md` |
| 4.17 | 提交视频加图片任务 API | 707-715 | 31814-32239 | 388 | `chapters/volcengine/mediakit/4.17 提交视频加图片任务 API.md` |
| 4.18 | 提交视频声音淡入淡出任务 API | 716-723 | 32240-32586 | 312 | `chapters/volcengine/mediakit/4.18 提交视频声音淡入淡出任务 API.md` |
| 4.19 | 提交音频声音淡入淡出任务 API | 724-730 | 32587-32921 | 304 | `chapters/volcengine/mediakit/4.19 提交音频声音淡入淡出任务 API.md` |
| 4.20 | 提交调整视频音量任务 API | 731-738 | 32922-33275 | 315 | `chapters/volcengine/mediakit/4.20 提交调整视频音量任务 API.md` |
| 4.21 | 提交视频添加滤镜任务 API | 739-745 | 33276-33605 | 294 | `chapters/volcengine/mediakit/4.21 提交视频添加滤镜任务 API.md` |
| 4.22 | 提交视频截取动图任务 API | 746-753 | 33606-33952 | 315 | `chapters/volcengine/mediakit/4.22 提交视频截取动图任务 API.md` |
| 4.23 | 提交视频添加运镜任务 API | 754-760 | 33953-34264 | 275 | `chapters/volcengine/mediakit/4.23 提交视频添加运镜任务 API.md` |
| 4.24 | 提交视频高斯模糊任务 API | 761-769 | 34265-34670 | 363 | `chapters/volcengine/mediakit/4.24 提交视频高斯模糊任务 API.md` |
| 4.25 | 提交文字生成滚屏视频任务 API | 770-780 | 34671-35212 | 466 | `chapters/volcengine/mediakit/4.25 提交文字生成滚屏视频任务 API.md` |
| 4.26 | 提交添加 AIGC 元数据标识任务 API | 781-791 | 35213-35777 | 512 | `chapters/volcengine/mediakit/4.26 提交添加 AIGC 元数据标识任务 API.md` |
| 4.27 | 提交多轨道剪辑任务 API | 792-818 | 35778-37068 | 1193 | `chapters/volcengine/mediakit/4.27 提交多轨道剪辑任务 API.md` |
| 5.1 | 提交人声背景音分离任务 API | 819-829 | 37070-37599 | 474 | `chapters/volcengine/mediakit/5.1 提交人声背景音分离任务 API.md` |
| 5.2 | 提交语音端点识别任务 API | 830-836 | 37600-37893 | 264 | `chapters/volcengine/mediakit/5.2 提交语音端点识别任务 API.md` |
| 5.3 | 提交音频转码任务 API | 837-847 | 37894-38414 | 470 | `chapters/volcengine/mediakit/5.3 提交音频转码任务 API.md` |
| 5.4 | 提交音频元信息获取任务 API | 848-853 | 38415-38663 | 224 | `chapters/volcengine/mediakit/5.4 提交音频元信息获取任务 API.md` |
| 5.5 | 提交音频内容编辑任务 API | 854-863 | 38664-39159 | 449 | `chapters/volcengine/mediakit/5.5 提交音频内容编辑任务 API.md` |
| 6.1 | 提交大模型高光剪辑任务 API | 864-881 | 39161-40028 | 790 | `chapters/volcengine/mediakit/6.1 提交大模型高光剪辑任务 API.md` |
| 6.2 | 提交视频理解智能策略任务 API | 882-890 | 40029-40471 | 392 | `chapters/volcengine/mediakit/6.2 提交视频理解智能策略任务 API.md` |
| 6.3 | 对话 Chat API | 891-915 | 40472-41246 | 592 | `chapters/volcengine/mediakit/6.3 对话 Chat API.md` |
| 7.1 | 查询任务信息 API | 916-920 | 41248-41417 | 144 | `chapters/volcengine/mediakit/7.1 查询任务信息 API.md` |
| 7.2 | 获取媒体上传地址 API | 921-924 | 41418-41554 | 104 | `chapters/volcengine/mediakit/7.2 获取媒体上传地址 API.md` |
| 7.3 | 事件回调 | 925-928 | 41555-41712 | 122 | `chapters/volcengine/mediakit/7.3 事件回调.md` |
| 7.4 | 错误码 | 929-931 | 41713-41853 | 124 | `chapters/volcengine/mediakit/7.4 错误码.md` |
