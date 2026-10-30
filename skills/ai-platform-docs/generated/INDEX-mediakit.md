# AI MediaKit API 区章节表（mediakit）

来源：《AI MediaKit API 参考》（999 页）。106 个章节文件，接口级切分：一个接口/任务一个文件；超过 1500 行的按语义块自动再拆为`… - 第N部分`（0 个章节被拆分）。

「页码」是原 PDF 页码范围；「行范围」是中间 MD（`doc/<源文档>.md`）的 1 起始行号，可据此回查原文。章节文件本身已去掉页眉页脚，回查 PDF 时用这两列。文件名即章节标题，日常定位直接 Glob 文件名即可，用不到这两列。

**这张表用来 grep，不要整读。**

| 编号 | 标题 | 页码 | 行范围(源文件) | 行数 | 文件 |
|------|------|------|---------------|------|------|
| 1.1 | 基础概念及准备工作 | 1-4 | 145-298 | 86 | `chapters/volcengine/mediakit/1.1 基础概念及准备工作.md` |
| 2.1 | 提交画质增强（大模型版）任务 API | 5-14 | 300-755 | 405 | `chapters/volcengine/mediakit/2.1 提交画质增强（大模型版）任务 API.md` |
| 2.2 | 提交画质增强（标准版和专业版）任务 API | 15-29 | 756-1487 | 646 | `chapters/volcengine/mediakit/2.2 提交画质增强（标准版和专业版）任务 API.md` |
| 2.3 | 提交画质增强（极速版）任务 API | 30-39 | 1488-1962 | 419 | `chapters/volcengine/mediakit/2.3 提交画质增强（极速版）任务 API.md` |
| 2.4 | 提交字幕擦除（精细化版）任务 API | 40-56 | 1963-2776 | 742 | `chapters/volcengine/mediakit/2.4 提交字幕擦除（精细化版）任务 API.md` |
| 2.5 | 提交字幕擦除（标准版）任务 API | 57-63 | 2777-3095 | 286 | `chapters/volcengine/mediakit/2.5 提交字幕擦除（标准版）任务 API.md` |
| 2.6 | 提交语音转字幕（ASR）任务 API | 64-71 | 3096-3448 | 313 | `chapters/volcengine/mediakit/2.6 提交语音转字幕（ASR）任务 API.md` |
| 2.7 | 提交视频识别字幕（OCR）任务 API | 72-79 | 3449-3782 | 300 | `chapters/volcengine/mediakit/2.7 提交视频识别字幕（OCR）任务 API.md` |
| 2.8 | 提交场景切分任务 API | 80-90 | 3783-4282 | 453 | `chapters/volcengine/mediakit/2.8 提交场景切分任务 API.md` |
| 2.9 | 提交智能语义切片（基础版）任务 API | 91-99 | 4283-4678 | 360 | `chapters/volcengine/mediakit/2.9 提交智能语义切片（基础版）任务 API.md` |
| 2.10 | 提交智能语义切片（专业版）任务 API | 100-112 | 4679-5293 | 558 | `chapters/volcengine/mediakit/2.10 提交智能语义切片（专业版）任务 API.md` |
| 2.11 | 提交高光智剪（短剧）任务 API | 113-131 | 5294-6184 | 808 | `chapters/volcengine/mediakit/2.11 提交高光智剪（短剧）任务 API.md` |
| 2.12 | 提交高光智剪（小游戏）任务 API | 132-141 | 6185-6640 | 410 | `chapters/volcengine/mediakit/2.12 提交高光智剪（小游戏）任务 API.md` |
| 2.13 | 提交高光智剪（影视拆条）任务 API | 142-154 | 6641-7254 | 560 | `chapters/volcengine/mediakit/2.13 提交高光智剪（影视拆条）任务 API.md` |
| 2.14 | 提交高光片段提取任务 API | 155-163 | 7255-7615 | 319 | `chapters/volcengine/mediakit/2.14 提交高光片段提取任务 API.md` |
| 2.15 | 提交视频绿幕抠图任务 API | 164-171 | 7616-7989 | 333 | `chapters/volcengine/mediakit/2.15 提交视频绿幕抠图任务 API.md` |
| 2.16 | 提交视频人像抠图任务 API | 172-179 | 7990-8346 | 318 | `chapters/volcengine/mediakit/2.16 提交视频人像抠图任务 API.md` |
| 2.17 | 提交剧情故事线分析任务 API | 180-188 | 8347-8692 | 306 | `chapters/volcengine/mediakit/2.17 提交剧情故事线分析任务 API.md` |
| 2.18 | 提交视频元信息获取任务 API | 189-195 | 8693-8972 | 252 | `chapters/volcengine/mediakit/2.18 提交视频元信息获取任务 API.md` |
| 2.19 | 提交剧本还原任务 API | 196-204 | 8973-9409 | 396 | `chapters/volcengine/mediakit/2.19 提交剧本还原任务 API.md` |
| 2.20 | 提交剧本还原（重绘场景）任务 API | 205-215 | 9410-9928 | 440 | `chapters/volcengine/mediakit/2.20 提交剧本还原（重绘场景）任务 API.md` |
| 2.21 | 提交解说视频生成任务 API | 216-230 | 9929-10645 | 635 | `chapters/volcengine/mediakit/2.21 提交解说视频生成任务 API.md` |
| 2.22 | 提交解说视频生成（短剧行业模型）任务 API | 231-246 | 10646-11408 | 670 | `chapters/volcengine/mediakit/2.22 提交解说视频生成（短剧行业模型）任务 API.md` |
| 2.23 | 提交视频抽帧任务 API | 247-259 | 11409-12020 | 556 | `chapters/volcengine/mediakit/2.23 提交视频抽帧任务 API.md` |
| 2.24 | 提交视频暗水印添加任务 API | 260-267 | 12021-12401 | 339 | `chapters/volcengine/mediakit/2.24 提交视频暗水印添加任务 API.md` |
| 2.25 | 提交视频暗水印提取任务 API | 268-273 | 12402-12630 | 200 | `chapters/volcengine/mediakit/2.25 提交视频暗水印提取任务 API.md` |
| 2.26 | 提交视频转码任务 API | 274-291 | 12631-13524 | 817 | `chapters/volcengine/mediakit/2.26 提交视频转码任务 API.md` |
| 2.27 | 提交极智超清任务 API | 292-308 | 13525-14401 | 799 | `chapters/volcengine/mediakit/2.27 提交极智超清任务 API.md` |
| 2.28 | 提交视频转封装任务 API | 309-316 | 14402-14747 | 311 | `chapters/volcengine/mediakit/2.28 提交视频转封装任务 API.md` |
| 2.29 | 提交视频画质检测 VQScore 任务 API | 317-322 | 14748-14987 | 209 | `chapters/volcengine/mediakit/2.29 提交视频画质检测 VQScore 任务 API.md` |
| 2.30 | 提交视频人脸打码任务 API | 323-330 | 14988-15364 | 337 | `chapters/volcengine/mediakit/2.30 提交视频人脸打码任务 API.md` |
| 2.31 | 提交视频人脸融合（换脸）任务 API | 331-338 | 15365-15743 | 339 | `chapters/volcengine/mediakit/2.31 提交视频人脸融合（换脸）任务 API.md` |
| 2.32 | 提交视频插帧任务 API | 339-345 | 15744-16073 | 297 | `chapters/volcengine/mediakit/2.32 提交视频插帧任务 API.md` |
| 2.33 | 提交视频口型对齐任务 API | 346-354 | 16074-16502 | 386 | `chapters/volcengine/mediakit/2.33 提交视频口型对齐任务 API.md` |
| 2.34 | 提交视频横转竖任务 API | 355-363 | 16503-16863 | 317 | `chapters/volcengine/mediakit/2.34 提交视频横转竖任务 API.md` |
| 2.35 | 提交视频流畅度提升任务 API | 364-373 | 16864-17343 | 426 | `chapters/volcengine/mediakit/2.35 提交视频流畅度提升任务 API.md` |
| 2.36 | 提交深度动作捕捉任务 API | 374-379 | 17344-17590 | 221 | `chapters/volcengine/mediakit/2.36 提交深度动作捕捉任务 API.md` |
| 3.1 | 提交图像画质增强任务 API | 380-390 | 17592-18123 | 480 | `chapters/volcengine/mediakit/3.1 提交图像画质增强任务 API.md` |
| 3.2 | 提交图像画质评估任务 API | 391-400 | 18124-18574 | 391 | `chapters/volcengine/mediakit/3.2 提交图像画质评估任务 API.md` |
| 3.3 | 提交图像人脸打码任务 API | 401-406 | 18575-18815 | 216 | `chapters/volcengine/mediakit/3.3 提交图像人脸打码任务 API.md` |
| 3.4 | 提交图像擦除修复任务 API | 407-416 | 18816-19245 | 386 | `chapters/volcengine/mediakit/3.4 提交图像擦除修复任务 API.md` |
| 3.5 | 提交图像背景移除任务 API | 417-425 | 19246-19629 | 347 | `chapters/volcengine/mediakit/3.5 提交图像背景移除任务 API.md` |
| 3.6 | 提交图像文字识别（OCR）任务 API | 426-434 | 19630-20027 | 364 | `chapters/volcengine/mediakit/3.6 提交图像文字识别（OCR）任务 API.md` |
| 3.7 | 提交图像智能裁剪任务 API | 435-440 | 20028-20280 | 226 | `chapters/volcengine/mediakit/3.7 提交图像智能裁剪任务 API.md` |
| 3.8 | 提交智能扩图任务 API | 441-446 | 20281-20546 | 243 | `chapters/volcengine/mediakit/3.8 提交智能扩图任务 API.md` |
| 3.9 | 提交集智瘦身任务 API | 447-452 | 20547-20785 | 214 | `chapters/volcengine/mediakit/3.9 提交集智瘦身任务 API.md` |
| 3.10 | 提交图像翻译任务 API | 453-461 | 20786-21135 | 313 | `chapters/volcengine/mediakit/3.10 提交图像翻译任务 API.md` |
| 3.11 | 提交电商牛皮癣擦除任务 API | 462-465 | 21136-21302 | 147 | `chapters/volcengine/mediakit/3.11 提交电商牛皮癣擦除任务 API.md` |
| 3.12 | 提交电商万创（商品场景图生成）任务 API | 466-477 | 21303-21854 | 504 | `chapters/volcengine/mediakit/3.12 提交电商万创（商品场景图生成）任务 API.md` |
| 3.13 | 提交图像元信息获取任务 API | 478-484 | 21855-22164 | 269 | `chapters/volcengine/mediakit/3.13 提交图像元信息获取任务 API.md` |
| 3.14 | 提交图像暗水印添加任务 API | 485-491 | 22165-22475 | 281 | `chapters/volcengine/mediakit/3.14 提交图像暗水印添加任务 API.md` |
| 3.15 | 提交图像暗水印提取任务 API | 492-496 | 22476-22684 | 188 | `chapters/volcengine/mediakit/3.15 提交图像暗水印提取任务 API.md` |
| 3.16.1 | 提交圆角矩形任务 API | 497-502 | 22686-22946 | 233 | `chapters/volcengine/mediakit/3.16.1 提交圆角矩形任务 API.md` |
| 3.16.2 | 提交图像旋转任务 API | 503-507 | 22947-23172 | 200 | `chapters/volcengine/mediakit/3.16.2 提交图像旋转任务 API.md` |
| 3.16.3 | 提交图像翻转任务 API | 508-512 | 23173-23385 | 189 | `chapters/volcengine/mediakit/3.16.3 提交图像翻转任务 API.md` |
| 3.16.4 | 提交图像锐化任务 API | 513-517 | 23386-23600 | 190 | `chapters/volcengine/mediakit/3.16.4 提交图像锐化任务 API.md` |
| 3.16.5 | 提交图像高斯模糊任务 API | 518-522 | 23601-23816 | 193 | `chapters/volcengine/mediakit/3.16.5 提交图像高斯模糊任务 API.md` |
| 3.16.6 | 提交图像打码任务 API | 523-529 | 23817-24127 | 277 | `chapters/volcengine/mediakit/3.16.6 提交图像打码任务 API.md` |
| 3.16.7 | 提交图像添加图文水印任务 API | 530-539 | 24128-24578 | 400 | `chapters/volcengine/mediakit/3.16.7 提交图像添加图文水印任务 API.md` |
| 3.16.8 | 提交图像缩放任务 API | 540-546 | 24579-24907 | 292 | `chapters/volcengine/mediakit/3.16.8 提交图像缩放任务 API.md` |
| 3.16.9 | 提交图像调整任务 API | 547-552 | 24908-25137 | 202 | `chapters/volcengine/mediakit/3.16.9 提交图像调整任务 API.md` |
| 3.16.10 | 提交图像裁剪任务 API | 553-561 | 25138-25540 | 357 | `chapters/volcengine/mediakit/3.16.10 提交图像裁剪任务 API.md` |
| 3.16.11 | 提交图像压缩任务 API | 562-568 | 25541-25830 | 261 | `chapters/volcengine/mediakit/3.16.11 提交图像压缩任务 API.md` |
| 3.16.12 | 提交图像负片任务 API | 569-573 | 25831-26034 | 181 | `chapters/volcengine/mediakit/3.16.12 提交图像负片任务 API.md` |
| 4.1 | 提交智能剪辑任务 API | 574-606 | 26036-27266 | 1136 | `chapters/volcengine/mediakit/4.1 提交智能剪辑任务 API.md` |
| 4.2 | 提交视频拼接任务 API | 607-615 | 27267-27652 | 346 | `chapters/volcengine/mediakit/4.2 提交视频拼接任务 API.md` |
| 4.3 | 提交音频拼接任务 API | 616-622 | 27653-27958 | 275 | `chapters/volcengine/mediakit/4.3 提交音频拼接任务 API.md` |
| 4.4 | 提交视频裁剪任务 API | 623-630 | 27959-28303 | 311 | `chapters/volcengine/mediakit/4.4 提交视频裁剪任务 API.md` |
| 4.5 | 提交音频裁剪任务 API | 631-637 | 28304-28617 | 285 | `chapters/volcengine/mediakit/4.5 提交音频裁剪任务 API.md` |
| 4.6 | 提交音频提取任务 API | 638-644 | 28618-28923 | 276 | `chapters/volcengine/mediakit/4.6 提交音频提取任务 API.md` |
| 4.7 | 提交音视频合成任务 API | 645-653 | 28924-29356 | 382 | `chapters/volcengine/mediakit/4.7 提交音视频合成任务 API.md` |
| 4.8 | 提交图片转视频任务 API | 654-663 | 29357-29769 | 367 | `chapters/volcengine/mediakit/4.8 提交图片转视频任务 API.md` |
| 4.9 | 提交视频画面翻转任务 API | 664-671 | 29770-30142 | 340 | `chapters/volcengine/mediakit/4.9 提交视频画面翻转任务 API.md` |
| 4.10 | 提交视频画面旋转任务 API | 672-679 | 30143-30491 | 311 | `chapters/volcengine/mediakit/4.10 提交视频画面旋转任务 API.md` |
| 4.11 | 提交视频画面裁剪任务 API | 680-688 | 30492-30894 | 362 | `chapters/volcengine/mediakit/4.11 提交视频画面裁剪任务 API.md` |
| 4.12 | 提交视频画面拼接任务 API | 689-696 | 30895-31264 | 333 | `chapters/volcengine/mediakit/4.12 提交视频画面拼接任务 API.md` |
| 4.13 | 提交视频调速任务 API | 697-703 | 31265-31605 | 308 | `chapters/volcengine/mediakit/4.13 提交视频调速任务 API.md` |
| 4.14 | 提交音频调速任务 API | 704-710 | 31606-31914 | 281 | `chapters/volcengine/mediakit/4.14 提交音频调速任务 API.md` |
| 4.15 | 提交音频混合任务 API | 711-717 | 31915-32224 | 280 | `chapters/volcengine/mediakit/4.15 提交音频混合任务 API.md` |
| 4.16 | 提交视频加字幕任务 API | 718-730 | 32225-32758 | 481 | `chapters/volcengine/mediakit/4.16 提交视频加字幕任务 API.md` |
| 4.17 | 提交视频加图片任务 API | 731-739 | 32759-33184 | 388 | `chapters/volcengine/mediakit/4.17 提交视频加图片任务 API.md` |
| 4.18 | 提交视频声音淡入淡出任务 API | 740-747 | 33185-33531 | 312 | `chapters/volcengine/mediakit/4.18 提交视频声音淡入淡出任务 API.md` |
| 4.19 | 提交音频声音淡入淡出任务 API | 748-754 | 33532-33866 | 304 | `chapters/volcengine/mediakit/4.19 提交音频声音淡入淡出任务 API.md` |
| 4.20 | 提交调整视频音量任务 API | 755-762 | 33867-34220 | 315 | `chapters/volcengine/mediakit/4.20 提交调整视频音量任务 API.md` |
| 4.21 | 提交视频添加滤镜任务 API | 763-769 | 34221-34550 | 294 | `chapters/volcengine/mediakit/4.21 提交视频添加滤镜任务 API.md` |
| 4.22 | 提交视频截取动图任务 API | 770-777 | 34551-34897 | 315 | `chapters/volcengine/mediakit/4.22 提交视频截取动图任务 API.md` |
| 4.23 | 提交视频添加运镜任务 API | 778-784 | 34898-35209 | 275 | `chapters/volcengine/mediakit/4.23 提交视频添加运镜任务 API.md` |
| 4.24 | 提交视频高斯模糊任务 API | 785-793 | 35210-35615 | 363 | `chapters/volcengine/mediakit/4.24 提交视频高斯模糊任务 API.md` |
| 4.25 | 提交文字生成滚屏视频任务 API | 794-804 | 35616-36157 | 466 | `chapters/volcengine/mediakit/4.25 提交文字生成滚屏视频任务 API.md` |
| 4.26 | 提交添加 AIGC 元数据标识任务 API | 805-815 | 36158-36722 | 512 | `chapters/volcengine/mediakit/4.26 提交添加 AIGC 元数据标识任务 API.md` |
| 4.27 | 提交多轨道剪辑任务 API | 816-842 | 36723-38013 | 1193 | `chapters/volcengine/mediakit/4.27 提交多轨道剪辑任务 API.md` |
| 4.28 | 提交 HyperFrames 云端渲染任务 API | 843-849 | 38014-38333 | 284 | `chapters/volcengine/mediakit/4.28 提交 HyperFrames 云端渲染任务 API.md` |
| 5.1 | 提交人声背景音分离任务 API | 850-860 | 38335-38862 | 471 | `chapters/volcengine/mediakit/5.1 提交人声背景音分离任务 API.md` |
| 5.2 | 提交语音端点识别任务 API | 861-867 | 38863-39156 | 264 | `chapters/volcengine/mediakit/5.2 提交语音端点识别任务 API.md` |
| 5.3 | 提交音频转码任务 API | 868-878 | 39157-39677 | 470 | `chapters/volcengine/mediakit/5.3 提交音频转码任务 API.md` |
| 5.4 | 提交音频元信息获取任务 API | 879-884 | 39678-39926 | 224 | `chapters/volcengine/mediakit/5.4 提交音频元信息获取任务 API.md` |
| 5.5 | 提交音频内容编辑任务 API | 885-895 | 39927-40472 | 490 | `chapters/volcengine/mediakit/5.5 提交音频内容编辑任务 API.md` |
| 6.1 | 提交大模型高光剪辑任务 API | 896-915 | 40474-41451 | 886 | `chapters/volcengine/mediakit/6.1 提交大模型高光剪辑任务 API.md` |
| 6.2 | 提交视频理解智能策略任务 API | 916-924 | 41452-41894 | 392 | `chapters/volcengine/mediakit/6.2 提交视频理解智能策略任务 API.md` |
| 6.3 | 对话 Chat API | 925-962 | 41895-43006 | 654 | `chapters/volcengine/mediakit/6.3 对话 Chat API.md` |
| 6.4 | MaaS 模型代理 API | 963-973 | 43007-43507 | 439 | `chapters/volcengine/mediakit/6.4 MaaS 模型代理 API.md` |
| 6.5 | 提交 AIGC 视频质量评估任务 API | 974-983 | 43508-44002 | 429 | `chapters/volcengine/mediakit/6.5 提交 AIGC 视频质量评估任务 API.md` |
| 7.1 | 获取媒体上传地址 API | 984-987 | 44004-44140 | 105 | `chapters/volcengine/mediakit/7.1 获取媒体上传地址 API.md` |
| 7.2 | 查询任务信息 API | 988-992 | 44141-44314 | 145 | `chapters/volcengine/mediakit/7.2 查询任务信息 API.md` |
| 7.3 | 事件回调 | 993-996 | 44315-44472 | 122 | `chapters/volcengine/mediakit/7.3 事件回调.md` |
| 7.4 | 错误码 | 997-999 | 44473-44613 | 124 | `chapters/volcengine/mediakit/7.4 错误码.md` |
