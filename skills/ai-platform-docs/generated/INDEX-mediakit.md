# AI MediaKit API 区章节表（mediakit）

来源：《AI MediaKit API 参考》（942 页）。104 个章节文件，接口级切分：一个接口/任务一个文件；超过 1500 行的按语义块自动再拆为`… - 第N部分`（0 个章节被拆分）。

「页码」是原 PDF 页码范围；「行范围」是中间 MD（`doc/<源文档>.md`）的 1 起始行号，可据此回查原文。章节文件本身已去掉页眉页脚，回查 PDF 时用这两列。文件名即章节标题，日常定位直接 Glob 文件名即可，用不到这两列。

**这张表用来 grep，不要整读。**

| 编号 | 标题 | 页码 | 行范围(源文件) | 行数 | 文件 |
|------|------|------|---------------|------|------|
| 1.1 | 基础概念及准备工作 | 1-4 | 143-296 | 85 | `chapters/volcengine/mediakit/1.1 基础概念及准备工作.md` |
| 2.1 | 提交画质增强（大模型版）任务 API | 5-13 | 298-688 | 359 | `chapters/volcengine/mediakit/2.1 提交画质增强（大模型版）任务 API.md` |
| 2.2 | 提交画质增强（标准版和专业版）任务 API | 14-27 | 689-1303 | 571 | `chapters/volcengine/mediakit/2.2 提交画质增强（标准版和专业版）任务 API.md` |
| 2.3 | 提交画质增强（极速版）任务 API | 28-37 | 1304-1725 | 387 | `chapters/volcengine/mediakit/2.3 提交画质增强（极速版）任务 API.md` |
| 2.4 | 提交字幕擦除（精细化版）任务 API | 38-53 | 1726-2416 | 644 | `chapters/volcengine/mediakit/2.4 提交字幕擦除（精细化版）任务 API.md` |
| 2.5 | 提交字幕擦除（标准版）任务 API | 54-60 | 2417-2705 | 266 | `chapters/volcengine/mediakit/2.5 提交字幕擦除（标准版）任务 API.md` |
| 2.6 | 提交语音转字幕（ASR）任务 API | 61-68 | 2706-3029 | 298 | `chapters/volcengine/mediakit/2.6 提交语音转字幕（ASR）任务 API.md` |
| 2.7 | 提交视频识别字幕（OCR）任务 API | 69-75 | 3030-3309 | 263 | `chapters/volcengine/mediakit/2.7 提交视频识别字幕（OCR）任务 API.md` |
| 2.8 | 提交场景切分任务 API | 76-84 | 3310-3728 | 397 | `chapters/volcengine/mediakit/2.8 提交场景切分任务 API.md` |
| 2.9 | 提交智能语义切片（基础版）任务 API | 85-93 | 3729-4099 | 342 | `chapters/volcengine/mediakit/2.9 提交智能语义切片（基础版）任务 API.md` |
| 2.10 | 提交智能语义切片（专业版）任务 API | 94-106 | 4100-4655 | 516 | `chapters/volcengine/mediakit/2.10 提交智能语义切片（专业版）任务 API.md` |
| 2.11 | 提交高光智剪（短剧）任务 API | 107-123 | 4656-5446 | 746 | `chapters/volcengine/mediakit/2.11 提交高光智剪（短剧）任务 API.md` |
| 2.12 | 提交高光智剪（小游戏）任务 API | 124-133 | 5447-5871 | 393 | `chapters/volcengine/mediakit/2.12 提交高光智剪（小游戏）任务 API.md` |
| 2.13 | 提交高光智剪（影视拆条）任务 API | 134-145 | 5872-6410 | 505 | `chapters/volcengine/mediakit/2.13 提交高光智剪（影视拆条）任务 API.md` |
| 2.14 | 提交高光片段提取任务 API | 146-152 | 6411-6704 | 269 | `chapters/volcengine/mediakit/2.14 提交高光片段提取任务 API.md` |
| 2.15 | 提交视频绿幕抠图任务 API | 153-160 | 6705-7044 | 313 | `chapters/volcengine/mediakit/2.15 提交视频绿幕抠图任务 API.md` |
| 2.16 | 提交视频人像抠图任务 API | 161-168 | 7045-7364 | 295 | `chapters/volcengine/mediakit/2.16 提交视频人像抠图任务 API.md` |
| 2.17 | 提交剧情故事线分析任务 API | 169-176 | 7365-7674 | 281 | `chapters/volcengine/mediakit/2.17 提交剧情故事线分析任务 API.md` |
| 2.18 | 提交视频元信息获取任务 API | 177-183 | 7675-7948 | 250 | `chapters/volcengine/mediakit/2.18 提交视频元信息获取任务 API.md` |
| 2.19 | 提交剧本还原任务 API | 184-192 | 7949-8321 | 346 | `chapters/volcengine/mediakit/2.19 提交剧本还原任务 API.md` |
| 2.20 | 提交剧本还原（重绘场景）任务 API | 193-203 | 8322-8822 | 436 | `chapters/volcengine/mediakit/2.20 提交剧本还原（重绘场景）任务 API.md` |
| 2.21 | 提交解说视频生成任务 API | 204-217 | 8823-9437 | 581 | `chapters/volcengine/mediakit/2.21 提交解说视频生成任务 API.md` |
| 2.22 | 提交解说视频生成（短剧行业模型）任务 API | 218-232 | 9438-10112 | 631 | `chapters/volcengine/mediakit/2.22 提交解说视频生成（短剧行业模型）任务 API.md` |
| 2.23 | 提交视频抽帧任务 API | 233-245 | 10113-10687 | 535 | `chapters/volcengine/mediakit/2.23 提交视频抽帧任务 API.md` |
| 2.24 | 提交视频暗水印添加任务 API | 246-253 | 10688-11030 | 315 | `chapters/volcengine/mediakit/2.24 提交视频暗水印添加任务 API.md` |
| 2.25 | 提交视频暗水印提取任务 API | 254-258 | 11031-11226 | 176 | `chapters/volcengine/mediakit/2.25 提交视频暗水印提取任务 API.md` |
| 2.26 | 提交视频转码任务 API | 259-274 | 11227-11997 | 731 | `chapters/volcengine/mediakit/2.26 提交视频转码任务 API.md` |
| 2.27 | 提交极智超清任务 API | 275-291 | 11998-12791 | 747 | `chapters/volcengine/mediakit/2.27 提交极智超清任务 API.md` |
| 2.28 | 提交视频转封装任务 API | 292-298 | 12792-13082 | 272 | `chapters/volcengine/mediakit/2.28 提交视频转封装任务 API.md` |
| 2.29 | 提交视频画质检测 VQScore 任务 API | 299-303 | 13083-13282 | 181 | `chapters/volcengine/mediakit/2.29 提交视频画质检测 VQScore 任务 API.md` |
| 2.30 | 提交视频人脸打码任务 API | 304-311 | 13283-13625 | 316 | `chapters/volcengine/mediakit/2.30 提交视频人脸打码任务 API.md` |
| 2.31 | 提交视频人脸融合（换脸）任务 API | 312-319 | 13626-13965 | 314 | `chapters/volcengine/mediakit/2.31 提交视频人脸融合（换脸）任务 API.md` |
| 2.32 | 提交视频插帧任务 API | 320-326 | 13966-14270 | 280 | `chapters/volcengine/mediakit/2.32 提交视频插帧任务 API.md` |
| 2.33 | 提交视频口型对齐任务 API | 327-334 | 14271-14643 | 347 | `chapters/volcengine/mediakit/2.33 提交视频口型对齐任务 API.md` |
| 2.34 | 提交视频横转竖任务 API | 335-342 | 14644-14965 | 294 | `chapters/volcengine/mediakit/2.34 提交视频横转竖任务 API.md` |
| 2.35 | 提交视频流畅度提升任务 API | 343-352 | 14966-15404 | 405 | `chapters/volcengine/mediakit/2.35 提交视频流畅度提升任务 API.md` |
| 3.1 | 提交图像画质增强任务 API | 353-363 | 15406-15848 | 417 | `chapters/volcengine/mediakit/3.1 提交图像画质增强任务 API.md` |
| 3.2 | 提交图像画质评估任务 API | 364-373 | 15849-16248 | 375 | `chapters/volcengine/mediakit/3.2 提交图像画质评估任务 API.md` |
| 3.3 | 提交图像人脸打码任务 API | 374-379 | 16249-16476 | 214 | `chapters/volcengine/mediakit/3.3 提交图像人脸打码任务 API.md` |
| 3.4 | 提交图像擦除修复任务 API | 380-389 | 16477-16884 | 378 | `chapters/volcengine/mediakit/3.4 提交图像擦除修复任务 API.md` |
| 3.5 | 提交图像背景移除任务 API | 390-397 | 16885-17205 | 300 | `chapters/volcengine/mediakit/3.5 提交图像背景移除任务 API.md` |
| 3.6 | 提交图像文字识别（OCR）任务 API | 398-405 | 17206-17555 | 329 | `chapters/volcengine/mediakit/3.6 提交图像文字识别（OCR）任务 API.md` |
| 3.7 | 提交图像智能裁剪任务 API | 406-411 | 17556-17794 | 223 | `chapters/volcengine/mediakit/3.7 提交图像智能裁剪任务 API.md` |
| 3.8 | 提交智能扩图任务 API | 412-417 | 17795-18052 | 241 | `chapters/volcengine/mediakit/3.8 提交智能扩图任务 API.md` |
| 3.9 | 提交集智瘦身任务 API | 418-423 | 18053-18271 | 204 | `chapters/volcengine/mediakit/3.9 提交集智瘦身任务 API.md` |
| 3.10 | 提交图像翻译任务 API | 424-432 | 18272-18603 | 305 | `chapters/volcengine/mediakit/3.10 提交图像翻译任务 API.md` |
| 3.11 | 提交电商牛皮癣擦除任务 API | 433-436 | 18604-18758 | 141 | `chapters/volcengine/mediakit/3.11 提交电商牛皮癣擦除任务 API.md` |
| 3.12 | 提交电商万创（商品场景图生成）任务 API | 437-448 | 18759-19282 | 490 | `chapters/volcengine/mediakit/3.12 提交电商万创（商品场景图生成）任务 API.md` |
| 3.13 | 提交图像元信息获取任务 API | 449-455 | 19283-19576 | 263 | `chapters/volcengine/mediakit/3.13 提交图像元信息获取任务 API.md` |
| 3.14 | 提交图像暗水印添加任务 API | 456-462 | 19577-19860 | 265 | `chapters/volcengine/mediakit/3.14 提交图像暗水印添加任务 API.md` |
| 3.15 | 提交图像暗水印提取任务 API | 463-467 | 19861-20058 | 183 | `chapters/volcengine/mediakit/3.15 提交图像暗水印提取任务 API.md` |
| 3.16.1 | 提交圆角矩形任务 API | 468-473 | 20060-20304 | 229 | `chapters/volcengine/mediakit/3.16.1 提交圆角矩形任务 API.md` |
| 3.16.2 | 提交图像旋转任务 API | 474-478 | 20305-20516 | 199 | `chapters/volcengine/mediakit/3.16.2 提交图像旋转任务 API.md` |
| 3.16.3 | 提交图像翻转任务 API | 479-483 | 20517-20716 | 188 | `chapters/volcengine/mediakit/3.16.3 提交图像翻转任务 API.md` |
| 3.16.4 | 提交图像锐化任务 API | 484-488 | 20717-20917 | 189 | `chapters/volcengine/mediakit/3.16.4 提交图像锐化任务 API.md` |
| 3.16.5 | 提交图像高斯模糊任务 API | 489-493 | 20918-21123 | 192 | `chapters/volcengine/mediakit/3.16.5 提交图像高斯模糊任务 API.md` |
| 3.16.6 | 提交图像打码任务 API | 494-501 | 21124-21420 | 273 | `chapters/volcengine/mediakit/3.16.6 提交图像打码任务 API.md` |
| 3.16.7 | 提交图像添加图文水印任务 API | 502-511 | 21421-21845 | 400 | `chapters/volcengine/mediakit/3.16.7 提交图像添加图文水印任务 API.md` |
| 3.16.8 | 提交图像缩放任务 API | 512-518 | 21846-22142 | 279 | `chapters/volcengine/mediakit/3.16.8 提交图像缩放任务 API.md` |
| 3.16.9 | 提交图像调整任务 API | 519-524 | 22143-22360 | 202 | `chapters/volcengine/mediakit/3.16.9 提交图像调整任务 API.md` |
| 3.16.10 | 提交图像裁剪任务 API | 525-533 | 22361-22735 | 353 | `chapters/volcengine/mediakit/3.16.10 提交图像裁剪任务 API.md` |
| 3.16.11 | 提交图像压缩任务 API | 534-540 | 22736-23001 | 248 | `chapters/volcengine/mediakit/3.16.11 提交图像压缩任务 API.md` |
| 3.16.12 | 提交图像负片任务 API | 541-545 | 23002-23194 | 180 | `chapters/volcengine/mediakit/3.16.12 提交图像负片任务 API.md` |
| 4.1 | 提交智能剪辑任务 API | 546-579 | 23196-24425 | 1139 | `chapters/volcengine/mediakit/4.1 提交智能剪辑任务 API.md` |
| 4.2 | 提交视频拼接任务 API | 580-588 | 24426-24780 | 327 | `chapters/volcengine/mediakit/4.2 提交视频拼接任务 API.md` |
| 4.3 | 提交音频拼接任务 API | 589-594 | 24781-25056 | 257 | `chapters/volcengine/mediakit/4.3 提交音频拼接任务 API.md` |
| 4.4 | 提交视频裁剪任务 API | 595-601 | 25057-25347 | 271 | `chapters/volcengine/mediakit/4.4 提交视频裁剪任务 API.md` |
| 4.5 | 提交音频裁剪任务 API | 602-608 | 25348-25635 | 268 | `chapters/volcengine/mediakit/4.5 提交音频裁剪任务 API.md` |
| 4.6 | 提交音频提取任务 API | 609-614 | 25636-25911 | 257 | `chapters/volcengine/mediakit/4.6 提交音频提取任务 API.md` |
| 4.7 | 提交音视频合成任务 API | 615-623 | 25912-26294 | 354 | `chapters/volcengine/mediakit/4.7 提交音视频合成任务 API.md` |
| 4.8 | 提交图片转视频任务 API | 624-633 | 26295-26672 | 346 | `chapters/volcengine/mediakit/4.8 提交图片转视频任务 API.md` |
| 4.9 | 提交视频画面翻转任务 API | 634-640 | 26673-26973 | 282 | `chapters/volcengine/mediakit/4.9 提交视频画面翻转任务 API.md` |
| 4.10 | 提交视频画面旋转任务 API | 641-647 | 26974-27262 | 268 | `chapters/volcengine/mediakit/4.10 提交视频画面旋转任务 API.md` |
| 4.11 | 提交视频画面裁剪任务 API | 648-655 | 27263-27600 | 315 | `chapters/volcengine/mediakit/4.11 提交视频画面裁剪任务 API.md` |
| 4.12 | 提交视频画面拼接任务 API | 656-663 | 27601-27938 | 313 | `chapters/volcengine/mediakit/4.12 提交视频画面拼接任务 API.md` |
| 4.13 | 提交视频调速任务 API | 664-670 | 27939-28250 | 289 | `chapters/volcengine/mediakit/4.13 提交视频调速任务 API.md` |
| 4.14 | 提交音频调速任务 API | 671-676 | 28251-28526 | 260 | `chapters/volcengine/mediakit/4.14 提交音频调速任务 API.md` |
| 4.15 | 提交音频混合任务 API | 677-682 | 28527-28807 | 263 | `chapters/volcengine/mediakit/4.15 提交音频混合任务 API.md` |
| 4.16 | 提交视频加字幕任务 API | 683-696 | 28808-29287 | 441 | `chapters/volcengine/mediakit/4.16 提交视频加字幕任务 API.md` |
| 4.17 | 提交视频加图片任务 API | 697-704 | 29288-29659 | 348 | `chapters/volcengine/mediakit/4.17 提交视频加图片任务 API.md` |
| 4.18 | 提交视频声音淡入淡出任务 API | 705-711 | 29660-29975 | 293 | `chapters/volcengine/mediakit/4.18 提交视频声音淡入淡出任务 API.md` |
| 4.19 | 提交音频声音淡入淡出任务 API | 712-718 | 29976-30283 | 286 | `chapters/volcengine/mediakit/4.19 提交音频声音淡入淡出任务 API.md` |
| 4.20 | 提交调整视频音量任务 API | 719-725 | 30284-30601 | 295 | `chapters/volcengine/mediakit/4.20 提交调整视频音量任务 API.md` |
| 4.21 | 提交视频添加滤镜任务 API | 726-732 | 30602-30894 | 272 | `chapters/volcengine/mediakit/4.21 提交视频添加滤镜任务 API.md` |
| 4.22 | 提交视频截取动图任务 API | 733-739 | 30895-31213 | 296 | `chapters/volcengine/mediakit/4.22 提交视频截取动图任务 API.md` |
| 4.23 | 提交视频添加运镜任务 API | 740-746 | 31214-31507 | 269 | `chapters/volcengine/mediakit/4.23 提交视频添加运镜任务 API.md` |
| 4.24 | 提交视频高斯模糊任务 API | 747-755 | 31508-31884 | 343 | `chapters/volcengine/mediakit/4.24 提交视频高斯模糊任务 API.md` |
| 4.25 | 提交文字生成滚屏视频任务 API | 756-766 | 31885-32377 | 434 | `chapters/volcengine/mediakit/4.25 提交文字生成滚屏视频任务 API.md` |
| 4.26 | 提交添加 AIGC 元数据标识任务 API | 767-777 | 32378-32889 | 481 | `chapters/volcengine/mediakit/4.26 提交添加 AIGC 元数据标识任务 API.md` |
| 4.27 | 提交多轨道剪辑任务 API | 778-804 | 32890-34145 | 1168 | `chapters/volcengine/mediakit/4.27 提交多轨道剪辑任务 API.md` |
| 5.1 | 提交人声背景音分离任务 API | 805-815 | 34147-34613 | 436 | `chapters/volcengine/mediakit/5.1 提交人声背景音分离任务 API.md` |
| 5.2 | 提交语音端点识别任务 API | 816-822 | 34614-34896 | 259 | `chapters/volcengine/mediakit/5.2 提交语音端点识别任务 API.md` |
| 5.3 | 提交音频内容编辑任务 API | 823-833 | 34897-35394 | 462 | `chapters/volcengine/mediakit/5.3 提交音频内容编辑任务 API.md` |
| 5.4 | 提交音频转码任务 API | 834-843 | 35395-35870 | 445 | `chapters/volcengine/mediakit/5.4 提交音频转码任务 API.md` |
| 5.5 | 提交音频元信息获取任务 API | 844-849 | 35871-36114 | 223 | `chapters/volcengine/mediakit/5.5 提交音频元信息获取任务 API.md` |
| 6.1 | 提交大模型高光剪辑任务 API | 850-867 | 36116-36902 | 733 | `chapters/volcengine/mediakit/6.1 提交大模型高光剪辑任务 API.md` |
| 6.2 | 提交视频理解智能策略任务 API | 868-876 | 36903-37325 | 384 | `chapters/volcengine/mediakit/6.2 提交视频理解智能策略任务 API.md` |
| 6.3 | 对话 Chat API | 877-904 | 37326-38105 | 591 | `chapters/volcengine/mediakit/6.3 对话 Chat API.md` |
| 6.4 | MaaS 模型代理 API | 905-916 | 38106-38589 | 434 | `chapters/volcengine/mediakit/6.4 MaaS 模型代理 API.md` |
| 6.5 | 提交 AIGC 视频质量评估任务 API | 917-926 | 38590-39059 | 418 | `chapters/volcengine/mediakit/6.5 提交 AIGC 视频质量评估任务 API.md` |
| 7.1 | 查询任务信息 API | 927-931 | 39061-39228 | 145 | `chapters/volcengine/mediakit/7.1 查询任务信息 API.md` |
| 7.2 | 获取媒体上传地址 API | 932-935 | 39229-39364 | 105 | `chapters/volcengine/mediakit/7.2 获取媒体上传地址 API.md` |
| 7.3 | 事件回调 | 936-939 | 39365-39520 | 122 | `chapters/volcengine/mediakit/7.3 事件回调.md` |
| 7.4 | 错误码 | 940-942 | 39521-39651 | 121 | `chapters/volcengine/mediakit/7.4 错误码.md` |
