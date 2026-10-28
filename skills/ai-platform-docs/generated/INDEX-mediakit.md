# AI MediaKit API 区章节表（mediakit）

来源：《AI MediaKit API 参考》（951 页）。106 个章节文件，接口级切分：一个接口/任务一个文件；超过 1500 行的按语义块自动再拆为`… - 第N部分`（0 个章节被拆分）。

「页码」是原 PDF 页码范围；「行范围」是中间 MD（`doc/<源文档>.md`）的 1 起始行号，可据此回查原文。章节文件本身已去掉页眉页脚，回查 PDF 时用这两列。文件名即章节标题，日常定位直接 Glob 文件名即可，用不到这两列。

**这张表用来 grep，不要整读。**

| 编号 | 标题 | 页码 | 行范围(源文件) | 行数 | 文件 |
|------|------|------|---------------|------|------|
| 1.1 | 基础概念及准备工作 | 1-4 | 145-298 | 85 | `chapters/volcengine/mediakit/1.1 基础概念及准备工作.md` |
| 2.1 | 提交画质增强（大模型版）任务 API | 5-13 | 300-690 | 359 | `chapters/volcengine/mediakit/2.1 提交画质增强（大模型版）任务 API.md` |
| 2.2 | 提交画质增强（标准版和专业版）任务 API | 14-27 | 691-1305 | 571 | `chapters/volcengine/mediakit/2.2 提交画质增强（标准版和专业版）任务 API.md` |
| 2.3 | 提交画质增强（极速版）任务 API | 28-37 | 1306-1727 | 387 | `chapters/volcengine/mediakit/2.3 提交画质增强（极速版）任务 API.md` |
| 2.4 | 提交字幕擦除（精细化版）任务 API | 38-53 | 1728-2418 | 644 | `chapters/volcengine/mediakit/2.4 提交字幕擦除（精细化版）任务 API.md` |
| 2.5 | 提交字幕擦除（标准版）任务 API | 54-60 | 2419-2707 | 266 | `chapters/volcengine/mediakit/2.5 提交字幕擦除（标准版）任务 API.md` |
| 2.6 | 提交语音转字幕（ASR）任务 API | 61-68 | 2708-3031 | 298 | `chapters/volcengine/mediakit/2.6 提交语音转字幕（ASR）任务 API.md` |
| 2.7 | 提交视频识别字幕（OCR）任务 API | 69-75 | 3032-3311 | 263 | `chapters/volcengine/mediakit/2.7 提交视频识别字幕（OCR）任务 API.md` |
| 2.8 | 提交场景切分任务 API | 76-84 | 3312-3730 | 397 | `chapters/volcengine/mediakit/2.8 提交场景切分任务 API.md` |
| 2.9 | 提交智能语义切片（基础版）任务 API | 85-93 | 3731-4101 | 342 | `chapters/volcengine/mediakit/2.9 提交智能语义切片（基础版）任务 API.md` |
| 2.10 | 提交智能语义切片（专业版）任务 API | 94-106 | 4102-4657 | 516 | `chapters/volcengine/mediakit/2.10 提交智能语义切片（专业版）任务 API.md` |
| 2.11 | 提交高光智剪（短剧）任务 API | 107-123 | 4658-5448 | 746 | `chapters/volcengine/mediakit/2.11 提交高光智剪（短剧）任务 API.md` |
| 2.12 | 提交高光智剪（小游戏）任务 API | 124-133 | 5449-5873 | 393 | `chapters/volcengine/mediakit/2.12 提交高光智剪（小游戏）任务 API.md` |
| 2.13 | 提交高光智剪（影视拆条）任务 API | 134-145 | 5874-6412 | 505 | `chapters/volcengine/mediakit/2.13 提交高光智剪（影视拆条）任务 API.md` |
| 2.14 | 提交高光片段提取任务 API | 146-152 | 6413-6706 | 269 | `chapters/volcengine/mediakit/2.14 提交高光片段提取任务 API.md` |
| 2.15 | 提交视频绿幕抠图任务 API | 153-160 | 6707-7046 | 313 | `chapters/volcengine/mediakit/2.15 提交视频绿幕抠图任务 API.md` |
| 2.16 | 提交视频人像抠图任务 API | 161-168 | 7047-7366 | 295 | `chapters/volcengine/mediakit/2.16 提交视频人像抠图任务 API.md` |
| 2.17 | 提交剧情故事线分析任务 API | 169-176 | 7367-7676 | 281 | `chapters/volcengine/mediakit/2.17 提交剧情故事线分析任务 API.md` |
| 2.18 | 提交视频元信息获取任务 API | 177-183 | 7677-7950 | 250 | `chapters/volcengine/mediakit/2.18 提交视频元信息获取任务 API.md` |
| 2.19 | 提交剧本还原任务 API | 184-192 | 7951-8323 | 346 | `chapters/volcengine/mediakit/2.19 提交剧本还原任务 API.md` |
| 2.20 | 提交剧本还原（重绘场景）任务 API | 193-203 | 8324-8824 | 436 | `chapters/volcengine/mediakit/2.20 提交剧本还原（重绘场景）任务 API.md` |
| 2.21 | 提交解说视频生成任务 API | 204-217 | 8825-9439 | 581 | `chapters/volcengine/mediakit/2.21 提交解说视频生成任务 API.md` |
| 2.22 | 提交解说视频生成（短剧行业模型）任务 API | 218-232 | 9440-10114 | 631 | `chapters/volcengine/mediakit/2.22 提交解说视频生成（短剧行业模型）任务 API.md` |
| 2.23 | 提交视频抽帧任务 API | 233-245 | 10115-10689 | 535 | `chapters/volcengine/mediakit/2.23 提交视频抽帧任务 API.md` |
| 2.24 | 提交视频暗水印添加任务 API | 246-253 | 10690-11032 | 315 | `chapters/volcengine/mediakit/2.24 提交视频暗水印添加任务 API.md` |
| 2.25 | 提交视频暗水印提取任务 API | 254-258 | 11033-11251 | 197 | `chapters/volcengine/mediakit/2.25 提交视频暗水印提取任务 API.md` |
| 2.26 | 提交视频转码任务 API | 259-275 | 11252-12063 | 766 | `chapters/volcengine/mediakit/2.26 提交视频转码任务 API.md` |
| 2.27 | 提交极智超清任务 API | 276-292 | 12064-12857 | 747 | `chapters/volcengine/mediakit/2.27 提交极智超清任务 API.md` |
| 2.28 | 提交视频转封装任务 API | 293-299 | 12858-13148 | 272 | `chapters/volcengine/mediakit/2.28 提交视频转封装任务 API.md` |
| 2.29 | 提交视频画质检测 VQScore 任务 API | 300-304 | 13149-13376 | 207 | `chapters/volcengine/mediakit/2.29 提交视频画质检测 VQScore 任务 API.md` |
| 2.30 | 提交视频人脸打码任务 API | 305-312 | 13377-13719 | 316 | `chapters/volcengine/mediakit/2.30 提交视频人脸打码任务 API.md` |
| 2.31 | 提交视频人脸融合（换脸）任务 API | 313-320 | 13720-14059 | 314 | `chapters/volcengine/mediakit/2.31 提交视频人脸融合（换脸）任务 API.md` |
| 2.32 | 提交视频插帧任务 API | 321-327 | 14060-14364 | 280 | `chapters/volcengine/mediakit/2.32 提交视频插帧任务 API.md` |
| 2.33 | 提交视频口型对齐任务 API | 328-335 | 14365-14737 | 347 | `chapters/volcengine/mediakit/2.33 提交视频口型对齐任务 API.md` |
| 2.34 | 提交视频横转竖任务 API | 336-343 | 14738-15059 | 294 | `chapters/volcengine/mediakit/2.34 提交视频横转竖任务 API.md` |
| 2.35 | 提交视频流畅度提升任务 API | 344-353 | 15060-15498 | 405 | `chapters/volcengine/mediakit/2.35 提交视频流畅度提升任务 API.md` |
| 2.36 | 提交深度动作捕捉任务 API | 354-358 | 15499-15736 | 218 | `chapters/volcengine/mediakit/2.36 提交深度动作捕捉任务 API.md` |
| 3.1 | 提交图像画质增强任务 API | 359-368 | 15738-16174 | 413 | `chapters/volcengine/mediakit/3.1 提交图像画质增强任务 API.md` |
| 3.2 | 提交图像画质评估任务 API | 369-377 | 16175-16571 | 374 | `chapters/volcengine/mediakit/3.2 提交图像画质评估任务 API.md` |
| 3.3 | 提交图像人脸打码任务 API | 378-383 | 16572-16800 | 215 | `chapters/volcengine/mediakit/3.3 提交图像人脸打码任务 API.md` |
| 3.4 | 提交图像擦除修复任务 API | 384-393 | 16801-17208 | 378 | `chapters/volcengine/mediakit/3.4 提交图像擦除修复任务 API.md` |
| 3.5 | 提交图像背景移除任务 API | 394-401 | 17209-17529 | 300 | `chapters/volcengine/mediakit/3.5 提交图像背景移除任务 API.md` |
| 3.6 | 提交图像文字识别（OCR）任务 API | 402-409 | 17530-17879 | 329 | `chapters/volcengine/mediakit/3.6 提交图像文字识别（OCR）任务 API.md` |
| 3.7 | 提交图像智能裁剪任务 API | 410-415 | 17880-18118 | 223 | `chapters/volcengine/mediakit/3.7 提交图像智能裁剪任务 API.md` |
| 3.8 | 提交智能扩图任务 API | 416-421 | 18119-18376 | 241 | `chapters/volcengine/mediakit/3.8 提交智能扩图任务 API.md` |
| 3.9 | 提交集智瘦身任务 API | 422-427 | 18377-18595 | 204 | `chapters/volcengine/mediakit/3.9 提交集智瘦身任务 API.md` |
| 3.10 | 提交图像翻译任务 API | 428-436 | 18596-18927 | 305 | `chapters/volcengine/mediakit/3.10 提交图像翻译任务 API.md` |
| 3.11 | 提交电商牛皮癣擦除任务 API | 437-440 | 18928-19082 | 141 | `chapters/volcengine/mediakit/3.11 提交电商牛皮癣擦除任务 API.md` |
| 3.12 | 提交电商万创（商品场景图生成）任务 API | 441-452 | 19083-19606 | 490 | `chapters/volcengine/mediakit/3.12 提交电商万创（商品场景图生成）任务 API.md` |
| 3.13 | 提交图像元信息获取任务 API | 453-459 | 19607-19900 | 263 | `chapters/volcengine/mediakit/3.13 提交图像元信息获取任务 API.md` |
| 3.14 | 提交图像暗水印添加任务 API | 460-466 | 19901-20184 | 265 | `chapters/volcengine/mediakit/3.14 提交图像暗水印添加任务 API.md` |
| 3.15 | 提交图像暗水印提取任务 API | 467-471 | 20185-20382 | 183 | `chapters/volcengine/mediakit/3.15 提交图像暗水印提取任务 API.md` |
| 3.16.1 | 提交圆角矩形任务 API | 472-477 | 20384-20628 | 229 | `chapters/volcengine/mediakit/3.16.1 提交圆角矩形任务 API.md` |
| 3.16.2 | 提交图像旋转任务 API | 478-482 | 20629-20840 | 199 | `chapters/volcengine/mediakit/3.16.2 提交图像旋转任务 API.md` |
| 3.16.3 | 提交图像翻转任务 API | 483-487 | 20841-21040 | 188 | `chapters/volcengine/mediakit/3.16.3 提交图像翻转任务 API.md` |
| 3.16.4 | 提交图像锐化任务 API | 488-492 | 21041-21241 | 189 | `chapters/volcengine/mediakit/3.16.4 提交图像锐化任务 API.md` |
| 3.16.5 | 提交图像高斯模糊任务 API | 493-497 | 21242-21447 | 192 | `chapters/volcengine/mediakit/3.16.5 提交图像高斯模糊任务 API.md` |
| 3.16.6 | 提交图像打码任务 API | 498-505 | 21448-21744 | 273 | `chapters/volcengine/mediakit/3.16.6 提交图像打码任务 API.md` |
| 3.16.7 | 提交图像添加图文水印任务 API | 506-515 | 21745-22169 | 400 | `chapters/volcengine/mediakit/3.16.7 提交图像添加图文水印任务 API.md` |
| 3.16.8 | 提交图像缩放任务 API | 516-522 | 22170-22466 | 279 | `chapters/volcengine/mediakit/3.16.8 提交图像缩放任务 API.md` |
| 3.16.9 | 提交图像调整任务 API | 523-528 | 22467-22684 | 202 | `chapters/volcengine/mediakit/3.16.9 提交图像调整任务 API.md` |
| 3.16.10 | 提交图像裁剪任务 API | 529-537 | 22685-23059 | 353 | `chapters/volcengine/mediakit/3.16.10 提交图像裁剪任务 API.md` |
| 3.16.11 | 提交图像压缩任务 API | 538-544 | 23060-23325 | 248 | `chapters/volcengine/mediakit/3.16.11 提交图像压缩任务 API.md` |
| 3.16.12 | 提交图像负片任务 API | 545-549 | 23326-23518 | 180 | `chapters/volcengine/mediakit/3.16.12 提交图像负片任务 API.md` |
| 4.1 | 提交智能剪辑任务 API | 550-583 | 23520-24749 | 1139 | `chapters/volcengine/mediakit/4.1 提交智能剪辑任务 API.md` |
| 4.2 | 提交视频拼接任务 API | 584-592 | 24750-25104 | 327 | `chapters/volcengine/mediakit/4.2 提交视频拼接任务 API.md` |
| 4.3 | 提交音频拼接任务 API | 593-598 | 25105-25380 | 257 | `chapters/volcengine/mediakit/4.3 提交音频拼接任务 API.md` |
| 4.4 | 提交视频裁剪任务 API | 599-605 | 25381-25671 | 271 | `chapters/volcengine/mediakit/4.4 提交视频裁剪任务 API.md` |
| 4.5 | 提交音频裁剪任务 API | 606-612 | 25672-25959 | 268 | `chapters/volcengine/mediakit/4.5 提交音频裁剪任务 API.md` |
| 4.6 | 提交音频提取任务 API | 613-618 | 25960-26235 | 257 | `chapters/volcengine/mediakit/4.6 提交音频提取任务 API.md` |
| 4.7 | 提交音视频合成任务 API | 619-627 | 26236-26618 | 354 | `chapters/volcengine/mediakit/4.7 提交音视频合成任务 API.md` |
| 4.8 | 提交图片转视频任务 API | 628-637 | 26619-26996 | 346 | `chapters/volcengine/mediakit/4.8 提交图片转视频任务 API.md` |
| 4.9 | 提交视频画面翻转任务 API | 638-644 | 26997-27297 | 282 | `chapters/volcengine/mediakit/4.9 提交视频画面翻转任务 API.md` |
| 4.10 | 提交视频画面旋转任务 API | 645-651 | 27298-27586 | 268 | `chapters/volcengine/mediakit/4.10 提交视频画面旋转任务 API.md` |
| 4.11 | 提交视频画面裁剪任务 API | 652-659 | 27587-27924 | 315 | `chapters/volcengine/mediakit/4.11 提交视频画面裁剪任务 API.md` |
| 4.12 | 提交视频画面拼接任务 API | 660-667 | 27925-28262 | 313 | `chapters/volcengine/mediakit/4.12 提交视频画面拼接任务 API.md` |
| 4.13 | 提交视频调速任务 API | 668-674 | 28263-28574 | 289 | `chapters/volcengine/mediakit/4.13 提交视频调速任务 API.md` |
| 4.14 | 提交音频调速任务 API | 675-680 | 28575-28850 | 260 | `chapters/volcengine/mediakit/4.14 提交音频调速任务 API.md` |
| 4.15 | 提交音频混合任务 API | 681-686 | 28851-29131 | 263 | `chapters/volcengine/mediakit/4.15 提交音频混合任务 API.md` |
| 4.16 | 提交视频加字幕任务 API | 687-700 | 29132-29611 | 441 | `chapters/volcengine/mediakit/4.16 提交视频加字幕任务 API.md` |
| 4.17 | 提交视频加图片任务 API | 701-708 | 29612-29983 | 348 | `chapters/volcengine/mediakit/4.17 提交视频加图片任务 API.md` |
| 4.18 | 提交视频声音淡入淡出任务 API | 709-715 | 29984-30299 | 293 | `chapters/volcengine/mediakit/4.18 提交视频声音淡入淡出任务 API.md` |
| 4.19 | 提交音频声音淡入淡出任务 API | 716-722 | 30300-30607 | 286 | `chapters/volcengine/mediakit/4.19 提交音频声音淡入淡出任务 API.md` |
| 4.20 | 提交调整视频音量任务 API | 723-729 | 30608-30925 | 295 | `chapters/volcengine/mediakit/4.20 提交调整视频音量任务 API.md` |
| 4.21 | 提交视频添加滤镜任务 API | 730-736 | 30926-31218 | 272 | `chapters/volcengine/mediakit/4.21 提交视频添加滤镜任务 API.md` |
| 4.22 | 提交视频截取动图任务 API | 737-743 | 31219-31537 | 296 | `chapters/volcengine/mediakit/4.22 提交视频截取动图任务 API.md` |
| 4.23 | 提交视频添加运镜任务 API | 744-750 | 31538-31831 | 269 | `chapters/volcengine/mediakit/4.23 提交视频添加运镜任务 API.md` |
| 4.24 | 提交视频高斯模糊任务 API | 751-759 | 31832-32208 | 343 | `chapters/volcengine/mediakit/4.24 提交视频高斯模糊任务 API.md` |
| 4.25 | 提交文字生成滚屏视频任务 API | 760-769 | 32209-32701 | 437 | `chapters/volcengine/mediakit/4.25 提交文字生成滚屏视频任务 API.md` |
| 4.26 | 提交添加 AIGC 元数据标识任务 API | 770-780 | 32702-33213 | 481 | `chapters/volcengine/mediakit/4.26 提交添加 AIGC 元数据标识任务 API.md` |
| 4.27 | 提交多轨道剪辑任务 API | 781-807 | 33214-34469 | 1168 | `chapters/volcengine/mediakit/4.27 提交多轨道剪辑任务 API.md` |
| 4.28 | 提交 HyperFrames 云端渲染任务 API | 808-814 | 34470-34773 | 279 | `chapters/volcengine/mediakit/4.28 提交 HyperFrames 云端渲染任务 API.md` |
| 5.1 | 提交人声背景音分离任务 API | 815-824 | 34775-35238 | 435 | `chapters/volcengine/mediakit/5.1 提交人声背景音分离任务 API.md` |
| 5.2 | 提交语音端点识别任务 API | 825-831 | 35239-35521 | 259 | `chapters/volcengine/mediakit/5.2 提交语音端点识别任务 API.md` |
| 5.3 | 提交音频转码任务 API | 832-841 | 35522-35997 | 445 | `chapters/volcengine/mediakit/5.3 提交音频转码任务 API.md` |
| 5.4 | 提交音频元信息获取任务 API | 842-847 | 35998-36241 | 223 | `chapters/volcengine/mediakit/5.4 提交音频元信息获取任务 API.md` |
| 5.5 | 提交音频内容编辑任务 API | 848-858 | 36242-36739 | 462 | `chapters/volcengine/mediakit/5.5 提交音频内容编辑任务 API.md` |
| 6.1 | 提交大模型高光剪辑任务 API | 859-876 | 36741-37536 | 742 | `chapters/volcengine/mediakit/6.1 提交大模型高光剪辑任务 API.md` |
| 6.2 | 提交视频理解智能策略任务 API | 877-885 | 37537-37959 | 384 | `chapters/volcengine/mediakit/6.2 提交视频理解智能策略任务 API.md` |
| 6.3 | 对话 Chat API | 886-913 | 37960-38739 | 591 | `chapters/volcengine/mediakit/6.3 对话 Chat API.md` |
| 6.4 | MaaS 模型代理 API | 914-925 | 38740-39223 | 434 | `chapters/volcengine/mediakit/6.4 MaaS 模型代理 API.md` |
| 6.5 | 提交 AIGC 视频质量评估任务 API | 926-935 | 39224-39693 | 418 | `chapters/volcengine/mediakit/6.5 提交 AIGC 视频质量评估任务 API.md` |
| 7.1 | 获取媒体上传地址 API | 936-939 | 39695-39831 | 108 | `chapters/volcengine/mediakit/7.1 获取媒体上传地址 API.md` |
| 7.2 | 查询任务信息 API | 940-944 | 39832-39998 | 143 | `chapters/volcengine/mediakit/7.2 查询任务信息 API.md` |
| 7.3 | 事件回调 | 945-948 | 39999-40154 | 122 | `chapters/volcengine/mediakit/7.3 事件回调.md` |
| 7.4 | 错误码 | 949-951 | 40155-40285 | 121 | `chapters/volcengine/mediakit/7.4 错误码.md` |
