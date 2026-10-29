<!-- Official source: https://klingai.com/document-api/api/usage-guide/kling-4-0-prompt-guide.md -->
<!-- Source SHA-256: 71960d0ce3ed1640517eec52a1122c576577fddc1033ca9932bfc673e1cf443c -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://klingai.com/document-api/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling 4.0 视频提示词案例

> 来源: https://klingai.com/document-api/api/usage-guide/kling-4-0-prompt-guide
> 语言: zh
> 当前 Tab: Kling 4.0 视频提示词案例
> 此内容为面向 LLM 优化的 Markdown，已展开页面内 Tab，并省略页面目录、复制按钮等 UI 控件。

::: info-box

本文为 Kling 4.0 视频 使用手册的配套提示词案例，使用手册详细介绍了 Kling 4.0 的模型能力、API任务使用方法、素材要求和提示词写作方法，本文为您提供涵盖 Kling 4.0 不同功能的具体案例，每个案例均附完整提示词与可运行的 API 调用代码，您可直接复制体验，也可结合业务需求调整使用。

## 1 提示词案例

### 1.1 主体与场景参考

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

<div class="guide-case-media-list guide-case-media-list-full">
<div class="guide-case-shot">

<div class="media-wrap image-wrap"><img src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-i-011.1b0d2d26ce00d558.5993c9704714c35c.webp" alt="" /></div>

</div>
</div>

```text
【整体风格】
15秒，写实真人电影质感。傍晚的滨海城市街道连接宴会片场。
自然手持摄影，有明显的脚步起伏、细微不规则晃动和构图修正。甩镜随车辆和人物动作发生，带短暂运动模糊，到达目标后重新落稳。追车和奔跑时运动强烈，宴会段逐渐放缓。
人物有微汗、碎发和衣服褶皱；路面、服装和器材有真实使用痕迹。色彩自然，红色跑车、火光与暖色宴会形成视觉变化。
【人物与车辆】
男演员：
三十岁左右，深色短发、轻微胡茬，体格精干。
驾驶和翻滚时穿完整特工造型：
深炭灰色合身行动上衣，领口闭合；
同色行动长裤；
黑色皮质短靴。
外层服装具有供片场快速换装使用的可撕开接缝，上衣从前中线及两侧打开，外裤沿两条裤腿外侧展开。
白衬衫、黑领结和深蓝西裤预先穿在外层服装里面。
外层保持完整时，人物呈现清楚的深色特工造型。
西服外套由后续两名工作人员帮助穿上。
深蓝西裤裤脚盖住黑色短靴靴筒。
男演员的脸、发型与体格始终一致。
跑车：
红色原创概念跑车，低矮圆润的楔形车身，短车头，弧形座舱，宽后轮拱。
车头是一条横贯式白色灯带，车尾左右各有三枚小圆形尾灯。
车头中央为连续光滑的红色车漆，深灰色轮毂中心为素面金属圆盖。
方向盘中央为完整的黑色皮革表面。
驾驶位侧窗打开，所有镜头保持这套外形与灯组设计。
摩托摄影师：
穿深色工作服和防护头盔，独自站在深蓝运动摩托的两侧特技脚踏上，臀部高于座垫，双手肩扛摄影机，车把空着。
他用双腿和重心控车，上半身补偿颠簸，镜头对准跑车驾驶位。
揭晓时清楚看见他的完整站姿、双脚、摩托与摄影机。
导演：
四十多岁，略带灰发，面部有自然纹理。
穿洗旧的深棕色短款夹克，内搭米色圆领T恤，下穿深色直筒裤。
手持数字秒表，身体与目光主动跟随拍摄。
身旁有场记、摄影助理和灯光人员，近处、身旁与远处的人物和器材形成前后层次。
换装人员：
共六名，穿普通片场工作服。
前四名左侧两人、右侧两人，负责拉开外层特工服。
后两名负责展开并穿好深蓝西服外套。
每个人动作明确，服装取下后由对应工作人员拿在手里。
女伴：
穿香槟金色礼服，手持自己的香槟杯，站在宴会入口内几步远的位置。
侍者：
站在入口一侧，托着香槟杯托盘，供男演员经过时取杯。
【镜头与动作】
00:00—00:03｜追车五镜快切
轮胎特写：后轮抓地，红色跑车加速。
脚部特写：黑色短靴踩下油门。
眼神特写：演员快速判断前方车流，脸随车辆震动。
手部特写：双手利落转动方向盘。
稍宽的侧面镜头：跑车贴着旁车穿过，距离快速缩短再拉开。
前四镜短促，最后一镜稍长，让穿行车流的动作清楚成立。
00:03—00:09｜车内拉出，揭晓摄影师，甩向导演
从副驾驶附近拍驾驶员。
摄影机经过打开的驾驶位侧窗，完整退出车外，再向外拉开。
形成车外侧面大全景：
红色跑车与深蓝摩托平行行驶，摄影师从头到脚完整可见，独自站立，双手肩扛摄影机，镜头正对驾驶员。
跑车绕过前车，摩托同步压弯，随后恢复并行。
摄影机随速度与路面颠簸自然起伏。
车辆掠过导演工作区，镜头顺勢甩向路边。
近处短暂掠过摄影助理的肩膀，镜头落在导演的斜侧中近景。
导演身体前倾，目光追着跑车。
身旁场记记录，远处灯光人员与器材构成有深度的片场背景。
他向前挥手，说：
“Stay with it! Keep going!”
整句在导演出镜期间说完。
00:09—00:12｜跑车爆炸
切跑车侧面的较宽跟拍。
导弹带着尾焰从左后方追入，清楚击中后部车身。
命中点闪光，后部车身随即爆开，火焰、黑烟和碎片向外扩张。
车身被掀起，延续向右的冲势。
手持镜头受冲击短促一震。
00:12—00:14｜画左翻滚入画
切邻近片场地面。
演员穿完整深色特工服，从画面左侧贴地翻滚进入，向中部移动。
左后方保留燃烧火光和升起的烟。
橙色光掠过他的左肩、脸侧与地面。
他收在单膝跪地、单手撑地的英雄姿态，全身可见，衣服沾灰。
镜头随落地动作短促下沉，再重新找到人物。
00:14—00:15｜脸部特写接起跑
切演员面部。
他呼出一口气，脸上有汗和灰，左侧火光闪动。
抬眼锁住前方，肩膀随即抬起，身体开始起跑。
手持镜头有细小晃动，随着起身迅速抬高，接向奔跑。
```

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<button type="button" class="guide-video-poster" data-src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-v-015.f83fe57c92075900.mp4" aria-label="播放视频"><img src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-p-015.87072260fac50780.d1b4e56ed780dabe.webp" alt="" /></button>

API 代码：

```cURL
curl -sS --request POST \
  'https://api-beijing.klingai.com/omni-video/kling-4.0' \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "@image_1 是本案例的参考图；具体应保持的人物或场景信息以素材映射确认结果为准。 【整体风格】 15秒，写实真人电影质感。傍晚的滨海城市街道连接宴会片场。 自然手持摄影，有明显的脚步起伏、细微不规则晃动和构图修正。甩镜随车辆和人物动作发生，带短暂运动模糊，到达目标后重新落稳。追车和奔跑时运动强烈，宴会段逐渐放缓。 人物有微汗、碎发和衣服褶皱；路面、服装和器材有真实使用痕迹。色彩自然，红色跑车、火光与暖色宴会形成视觉变化。 【人物与车辆】 男演员： 三十岁左右，深色短发、轻微胡茬，体格精干。 驾驶和翻滚时穿完整特工造型： 深炭灰色合身行动上衣，领口闭合； 同色行动长裤； 黑色皮质短靴。 外层服装具有供片场快速换装使用的可撕开接缝，上衣从前中线及两侧打开，外裤沿两条裤腿外侧展开。 白衬衫、黑领结和深蓝西裤预先穿在外层服装里面。 外层保持完整时，人物呈现清楚的深色特工造型。 西服外套由后续两名工作人员帮助穿上。 深蓝西裤裤脚盖住黑色短靴靴筒。 男演员的脸、发型与体格始终一致。 跑车： 红色原创概念跑车，低矮圆润的楔形车身，短车头，弧形座舱，宽后轮拱。 车头是一条横贯式白色灯带，车尾左右各有三枚小圆形尾灯。 车头中央为连续光滑的红色车漆，深灰色轮毂中心为素面金属圆盖。 方向盘中央为完整的黑色皮革表面。 驾驶位侧窗打开，所有镜头保持这套外形与灯组设计。 摩托摄影师： 穿深色工作服和防护头盔，独自站在深蓝运动摩托的两侧特技脚踏上，臀部高于座垫，双手肩扛摄影机，车把空着。 他用双腿和重心控车，上半身补偿颠簸，镜头对准跑车驾驶位。 揭晓时清楚看见他的完整站姿、双脚、摩托与摄影机。 导演： 四十多岁，略带灰发，面部有自然纹理。 穿洗旧的深棕色短款夹克，内搭米色圆领T恤，下穿深色直筒裤。 手持数字秒表，身体与目光主动跟随拍摄。 身旁有场记、摄影助理和灯光人员，近处、身旁与远处的人物和器材形成前后层次。 换装人员： 共六名，穿普通片场工作服。 前四名左侧两人、右侧两人，负责拉开外层特工服。 后两名负责展开并穿好深蓝西服外套。 每个人动作明确，服装取下后由对应工作人员拿在手里。 女伴： 穿香槟金色礼服，手持自己的香槟杯，站在宴会入口内几步远的位置。 侍者： 站在入口一侧，托着香槟杯托盘，供男演员经过时取杯。 【镜头与动作】 00:00—00:03｜追车五镜快切 轮胎特写：后轮抓地，红色跑车加速。 脚部特写：黑色短靴踩下油门。 眼神特写：演员快速判断前方车流，脸随车辆震动。 手部特写：双手利落转动方向盘。 稍宽的侧面镜头：跑车贴着旁车穿过，距离快速缩短再拉开。 前四镜短促，最后一镜稍长，让穿行车流的动作清楚成立。 00:03—00:09｜车内拉出，揭晓摄影师，甩向导演 从副驾驶附近拍驾驶员。 摄影机经过打开的驾驶位侧窗，完整退出车外，再向外拉开。 形成车外侧面大全景： 红色跑车与深蓝摩托平行行驶，摄影师从头到脚完整可见，独自站立，双手肩扛摄影机，镜头正对驾驶员。 跑车绕过前车，摩托同步压弯，随后恢复并行。 摄影机随速度与路面颠簸自然起伏。 车辆掠过导演工作区，镜头顺勢甩向路边。 近处短暂掠过摄影助理的肩膀，镜头落在导演的斜侧中近景。 导演身体前倾，目光追着跑车。 身旁场记记录，远处灯光人员与器材构成有深度的片场背景。 他向前挥手，说： “Stay with it! Keep going!” 整句在导演出镜期间说完。 00:09—00:12｜跑车爆炸 切跑车侧面的较宽跟拍。 导弹带着尾焰从左后方追入，清楚击中后部车身。 命中点闪光，后部车身随即爆开，火焰、黑烟和碎片向外扩张。 车身被掀起，延续向右的冲势。 手持镜头受冲击短促一震。 00:12—00:14｜画左翻滚入画 切邻近片场地面。 演员穿完整深色特工服，从画面左侧贴地翻滚进入，向中部移动。 左后方保留燃烧火光和升起的烟。 橙色光掠过他的左肩、脸侧与地面。 他收在单膝跪地、单手撑地的英雄姿态，全身可见，衣服沾灰。 镜头随落地动作短促下沉，再重新找到人物。 00:14—00:15｜脸部特写接起跑 切演员面部。 他呼出一口气，脸上有汗和灰，左侧火光闪动。 抬眼锁住前方，肩膀随即抬起，身体开始起跑。 手持镜头有细小晃动，随着起身迅速抬高，接向奔跑。"
    },
    {
      "type": "refer_image",
      "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch12_1_cast_vehicle_board.jpg",
      "id": "image_1"
    }
  ],
  "settings": {
    "resolution": "1080p",
    "aspect_ratio": "adaptive"
  }
}'
```

### 1.2 动作参考

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

<div class="guide-case-media-list guide-case-media-list-video-full">
<div class="guide-case-shot">

<button type="button" class="guide-video-poster" data-src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-v-016.3a3678d208b3aa43.mp4" aria-label="播放视频"><img src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-p-016.21a0b5ce8eff387f.d3cfe1cb40a0395c.webp" alt="" /></button>

<p>视频1</p>
</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap"><img src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-i-016.e15f59cc63d6ab02.2add50ffcbbf99a5.webp" alt="" /></div>

<p>图片1</p>
</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap"><img src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-i-009.9acc77940efcd8d3.ffc8054c1a3160f6.webp" alt="" /></div>

<p>图片2</p>
</div>
</div>

```text
参考 @视频1 的打斗动作与出招节奏，角色造型来自 @图片1 @图片2
```

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<button type="button" class="guide-video-poster" data-src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-v-019.2561cd167b6fde8e.mp4" aria-label="播放视频"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-p-019.cf68c76a37e91287.15ebf8069dd89946.webp" alt="" /></button>

API 代码：

```cURL
curl -sS --request POST \
  'https://api-beijing.klingai.com/omni-video/kling-4.0' \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "参考 @video_1 的打斗动作与出招节奏，角色造型来自 @image_1 @image_2。"
    },
    {
      "type": "feature_video",
      "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch12_2_fight_motion_source.mp4",
      "id": "video_1"
    },
    {
      "type": "refer_image",
      "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch12_2_dark_hair_fighter_ref.png",
      "id": "image_1"
    },
    {
      "type": "refer_image",
      "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch12_2_silver_hair_fighter_ref.png",
      "id": "image_2"
    }
  ],
  "settings": {
    "resolution": "1080p",
    "aspect_ratio": "adaptive"
  }
}'
```

### 1.3 运镜参考

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

<div class="guide-case-media-list guide-case-media-list-video-full">
<div class="guide-case-shot">

<button type="button" class="guide-video-poster" data-src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-v-010.f1e17d6f421388aa.mp4" aria-label="播放视频"><img src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-p-010.72ab0b48df407eb0.9b1dd5602104ed53.webp" alt="" /></button>

<p>视频1</p>
</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap"><img src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-i-013.2af59253fbf53d04.a2ffa5c46efba4fa.webp" alt="" /></div>

<p>图片1</p>
</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-i-017.9d48f22b4a55896f.03f4fc98351e4d58.webp" alt="" /></div>

<p>图片2</p>
</div>
</div>

```text
参考 @视频1 的运镜轨迹与镜头节奏，主体替换为 @图片1 的汽车，背景替换为@图片2
```

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<button type="button" class="guide-video-poster" data-src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-v-017.eb51d0bd9b362a7e.mp4" aria-label="播放视频"><img src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-p-017.0b611dc3bcf16c7a.fdc58e335ad07cda.webp" alt="" /></button>

API 代码：

```cURL
curl -sS --request POST \
  'https://api-beijing.klingai.com/omni-video/kling-4.0' \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "参考 @video_1 的运镜轨迹与镜头节奏，主体替换为 @image_1 的汽车，背景替换为 @image_2。"
    },
    {
      "type": "feature_video",
      "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch12_3_camera_motion_source.mp4",
      "id": "video_1"
    },
    {
      "type": "refer_image",
      "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch12_3_race_car_ref.png",
      "id": "image_1"
    },
    {
      "type": "refer_image",
      "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch12_3_neon_arena_ref.png",
      "id": "image_2"
    }
  ],
  "settings": {
    "resolution": "1080p",
    "aspect_ratio": "adaptive"
  }
}'
```

### 1.4 分镜表参考

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

<div class="guide-case-media-list">
<div class="guide-case-shot">

<div class="media-wrap image-wrap"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-i-014.b11db9adc74cdb94.c73ab818a8213e2c.webp" alt="" /></div>

<p>图片1</p>
</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-i-012.9ac826fa72bf4c8b.a4da6223abdcf549.webp" alt="" /></div>

<p>图片2</p>
</div>
</div>

```text
严格以附带的分镜表（图片1）为依据，遵循导演已确认的镜头顺序、构图、摄影机运动路径、画面运动方向和情绪递进。呈现分镜画格所描述的最终定格动画画面，不要把分镜表本身拍出来。画面中不得出现铅笔素描质感、分镜网格、标题、中文标签或导演备注栏。

附带的角色设定板（图片2）是确定 BISCUIT（C1）角色形象的唯一依据：他是一只体型小巧、圆滚滚的黏土梗犬，有着蓬乱的棕色毛发，一只耳朵耷拉，另一只耳朵竖起；黑色黏土鼻子很大，双眼圆睁、满怀期待，尾巴短短的。他穿着一套小小的白色黏土宇航服，领口和袖口为橙色；戴着圆形玻璃头盔，头盔正面敞开，让鼻子伸在外面；背着一个装有弯曲天线的小背包，脚穿硕大的月球靴，手里拿着一把比自己还大的黏土叉子。每一帧都必须保持同一只狗、同一套宇航服和同一把叉子的外观一致。C2 是一只体型如巴士般巨大的黏土奶酪鼠，性格友善。

时长15秒，画幅16:9，全程为一个持续展开的主镜头，不出现可见剪辑。唯一一台虚拟摄影机先在他身旁随跳跃起伏，随后与他一起俯冲入洞，从隧道底部向上仰拍，再与他一起冲出洞口，最后升高至极远景。所有景别变化都通过这段连续的摄影机运动完成。

视觉风格：手工黏土定格动画，呈现阿德曼动画的风格。保留清晰可见的指纹、黏土纹理和略微不平整的表面，具有每秒12帧的定格动画顿挫感。采用真实微缩布景的灯光效果和微距摄影般的浅景深。奶酪月球像果冻一样颤动，黑色毡布构成天空，配以锡箔星星和黏土地球。整体温暖、舒适，带着憨趣。

视觉概念：饥饿与勇气。一只小狗，一把巨大的叉子，一颗摇摇晃晃的奶酪月球，以及一位新朋友。

环境：布满孔洞的黄色奶酪月球表面、地表下的奶酪隧道、一艘小巧歪斜的黏土火箭，以及天空中的地球。

音频：除最后三秒响起轻快的大号与尤克里里合奏外，其余时间不使用音乐。音效包括：吱吱作响的黏土脚步声、缓慢低重力跳跃时富有弹性的“啵嘤”声、月球震动时低沉的果冻颤动声、洞口张开时橡胶般的“噗”声、翻滚时的呼啸声、巨鼠响亮的啃咬声和受惊时的尖叫声、爪子慌乱抓挠的声音、如愿吃到奶酪时那一口痛快的咀嚼声、满足的咀嚼声，以及尾巴拍打地面的声音。

情绪指引：L1 好奇 → L3 惊讶 → L4 恐慌 → L5 追逐达到高潮 → L5 第一口奶酪带来的极致幸福 → L1 温馨而满足。

分镜节拍（全程连续，无剪辑）：

0–2秒（P01）：摄影机贴近奶酪表面，以低机位拍摄。Biscuit 从歪斜的小火箭里走出来，将一只爪子踩进奶酪，嗅了嗅，眼睛越睁越大。他肩上扛着叉子，天空中可以看见地球。

2–4.5秒（P02）：摄影机在他身旁随跳跃起伏。他以低重力下缓慢而大幅度的跳跃越过奶酪地表，耳朵上下飞扬。他将叉子扎进一大块楔形奶酪，整片地面顿时像果冻一样颤动，一个巨大的洞口在他脚下张开。

4.5–7秒（P03）：摄影机与他一起俯冲入洞。他爪子里握着叉子，在布满孔洞的奶酪隧道中缓慢翻滚，经过一只正在啃食洞壁、体型如巴士般巨大的黏土奶酪鼠，把对方吓了一跳。

7–9.5秒（P04）：摄影机来到隧道底部，向上仰拍。巨鼠转过身，胡须颤动，追着他沿隧道向上跑。Biscuit 惊慌地在洞壁之间弹来弹去，叉子后面拖着卷曲的奶酪条。

9.5–12秒（P05）：摄影机与他们一起冲出洞口。Biscuit 向上腾起，在空中划出一道缓慢的高弧线，巨鼠的脑袋紧接着从洞口探出。Biscuit 在半空中倒悬着，用叉子舀起一大卷奶酪，送进嘴里，瞬间沉浸在极致的幸福之中。

12–15秒（P06）：摄影机升高，拉至极远景。Biscuit 和巨鼠并排坐在洞口边缘，一起吃着奶酪。火箭停在他们身后，地球缓缓升起，锡箔星星点缀天空。Biscuit 满足地呼出气息，头盔玻璃上蒙起一层雾，尾巴欢快地摇动。大号与尤克里里奏响。保持这一画面。
```

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<button type="button" class="guide-video-poster" data-src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-v-014.4c03cf5e10f8fbee.mp4" aria-label="播放视频"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-p-014.6e3a2aa695c37ba3.5d300d5ecafc3737.webp" alt="" /></button>

API 代码：

```cURL
curl -sS --request POST \
  'https://api-beijing.klingai.com/omni-video/kling-4.0' \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "@image_1 是分镜表，@image_2 是角色设定板。 严格以附带的分镜表（@image_1）为依据，遵循导演已确认的镜头顺序、构图、摄影机运动路径、画面运动方向和情绪递进。呈现分镜画格所描述的最终定格动画画面，不要把分镜表本身拍出来。画面中不得出现铅笔素描质感、分镜网格、标题、中文标签或导演备注栏。  附带的角色设定板（@image_2）是确定 BISCUIT（C1）角色形象的唯一依据：他是一只体型小巧、圆滚滚的黏土梗犬，有着蓬乱的棕色毛发，一只耳朵耷拉，另一只耳朵竖起；黑色黏土鼻子很大，双眼圆睁、满怀期待，尾巴短短的。他穿着一套小小的白色黏土宇航服，领口和袖口为橙色；戴着圆形玻璃头盔，头盔正面敞开，让鼻子伸在外面；背着一个装有弯曲天线的小背包，脚穿硕大的月球靴，手里拿着一把比自己还大的黏土叉子。每一帧都必须保持同一只狗、同一套宇航服和同一把叉子的外观一致。C2 是一只体型如巴士般巨大的黏土奶酪鼠，性格友善。  时长15秒，画幅16:9，全程为一个持续展开的主镜头，不出现可见剪辑。唯一一台虚拟摄影机先在他身旁随跳跃起伏，随后与他一起俯冲入洞，从隧道底部向上仰拍，再与他一起冲出洞口，最后升高至极远景。所有景别变化都通过这段连续的摄影机运动完成。  视觉风格：手工黏土定格动画，呈现阿德曼动画的风格。保留清晰可见的指纹、黏土纹理和略微不平整的表面，具有每秒12帧的定格动画顿挫感。采用真实微缩布景的灯光效果和微距摄影般的浅景深。奶酪月球像果冻一样颤动，黑色毡布构成天空，配以锡箔星星和黏土地球。整体温暖、舒适，带着憨趣。  视觉概念：饥饿与勇气。一只小狗，一把巨大的叉子，一颗摇摇晃晃的奶酪月球，以及一位新朋友。  环境：布满孔洞的黄色奶酪月球表面、地表下的奶酪隧道、一艘小巧歪斜的黏土火箭，以及天空中的地球。  音频：除最后三秒响起轻快的大号与尤克里里合奏外，其余时间不使用音乐。音效包括：吱吱作响的黏土脚步声、缓慢低重力跳跃时富有弹性的“啵嘤”声、月球震动时低沉的果冻颤动声、洞口张开时橡胶般的“噗”声、翻滚时的呼啸声、巨鼠响亮的啃咬声和受惊时的尖叫声、爪子慌乱抓挠的声音、如愿吃到奶酪时那一口痛快的咀嚼声、满足的咀嚼声，以及尾巴拍打地面的声音。  情绪指引：L1 好奇 → L3 惊讶 → L4 恐慌 → L5 追逐达到高潮 → L5 第一口奶酪带来的极致幸福 → L1 温馨而满足。  分镜节拍（全程连续，无剪辑）：  0–2秒（P01）：摄影机贴近奶酪表面，以低机位拍摄。Biscuit 从歪斜的小火箭里走出来，将一只爪子踩进奶酪，嗅了嗅，眼睛越睁越大。他肩上扛着叉子，天空中可以看见地球。  2–4.5秒（P02）：摄影机在他身旁随跳跃起伏。他以低重力下缓慢而大幅度的跳跃越过奶酪地表，耳朵上下飞扬。他将叉子扎进一大块楔形奶酪，整片地面顿时像果冻一样颤动，一个巨大的洞口在他脚下张开。  4.5–7秒（P03）：摄影机与他一起俯冲入洞。他爪子里握着叉子，在布满孔洞的奶酪隧道中缓慢翻滚，经过一只正在啃食洞壁、体型如巴士般巨大的黏土奶酪鼠，把对方吓了一跳。  7–9.5秒（P04）：摄影机来到隧道底部，向上仰拍。巨鼠转过身，胡须颤动，追着他沿隧道向上跑。Biscuit 惊慌地在洞壁之间弹来弹去，叉子后面拖着卷曲的奶酪条。  9.5–12秒（P05）：摄影机与他们一起冲出洞口。Biscuit 向上腾起，在空中划出一道缓慢的高弧线，巨鼠的脑袋紧接着从洞口探出。Biscuit 在半空中倒悬着，用叉子舀起一大卷奶酪，送进嘴里，瞬间沉浸在极致的幸福之中。  12–15秒（P06）：摄影机升高，拉至极远景。Biscuit 和巨鼠并排坐在洞口边缘，一起吃着奶酪。火箭停在他们身后，地球缓缓升起，锡箔星星点缀天空。Biscuit 满足地呼出气息，头盔玻璃上蒙起一层雾，尾巴欢快地摇动。大号与尤克里里奏响。保持这一画面。"
    },
    {
      "type": "refer_image",
      "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch12_4_moon_cheese_storyboard.png",
      "id": "image_1"
    },
    {
      "type": "refer_image",
      "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch12_4_biscuit_character_board.png",
      "id": "image_2"
    }
  ],
  "settings": {
    "resolution": "1080p",
    "aspect_ratio": "adaptive"
  }
}'
```

### 1.5 视频指令编辑

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

<div class="guide-case-media-list guide-case-media-list-full">
<div class="guide-case-shot">

<button type="button" class="guide-video-poster" data-src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-v-012.cc0315aa49c9576e.mp4" aria-label="播放视频"><img src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-p-012.fd57851a6c3718a2.f72a6e010d83900e.webp" alt="" /></button>

<p>视频1</p>
</div>
</div>

```text
编辑@视频1，删除视频中的前景人物，其余保持不变
```

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<button type="button" class="guide-video-poster" data-src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-v-011.d700ab4e2fab2014.mp4" aria-label="播放视频"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-p-011.9a4aa82cdbc622fe.dc768666076375b2.webp" alt="" /></button>

API 代码：

```cURL
curl -sS --request POST \
  'https://api-beijing.klingai.com/omni-video/kling-4.0' \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "编辑 @video_1，删除视频中的前景人物，其余保持不变。"
    },
    {
      "type": "base_video",
      "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch12_5_guitar_foreground_source.mp4",
      "id": "video_1"
    }
  ],
  "settings": {
    "resolution": "1080p",
    "aspect_ratio": "adaptive"
  }
}'
```

### 1.6 视频参考素材编辑

**增加主体**

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

<div class="guide-case-media-list guide-case-media-list-video-full">
<div class="guide-case-shot">

<button type="button" class="guide-video-poster" data-src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-v-013.a3d6ece6f45d952b.mp4" aria-label="播放视频"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-p-013.6e7962a901450b9b.b74c00b1ca8b9773.webp" alt="" /></button>

<p>视频1</p>
</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-i-008.32efa34f29c34fa8.7c883c488b761d4a.webp" alt="" /></div>

<p>主体1 - 正面图</p>
</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-i-010.dd24b8f45d1d2109.098b309778dcfce3.webp" alt="" /></div>

<p>主体1 - 侧面图</p>
</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap"><img src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-i-015.949ee5c08fb9a83c.c0c871aeac01c68f.webp" alt="" /></div>

<p>主体1 - 背面图</p>
</div>
</div>

```text
编辑@视频1，在视频最后箱子再次被打开时，@主体1正躺在里面睡觉。
最后一句台词 “Ah,they're all,old tricks,nothing new.” 改为“Why is there a pig here?”。
```

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<button type="button" class="guide-video-poster" data-src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-v-018.b7b59973200ab37b.mp4" aria-label="播放视频"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-p-018.db4ade6b659f0878.f688c7be51b8620c.webp" alt="" /></button>

API 代码：

##### 第一步：用三视图创建小猪主体

正面图填 frontal_image，侧面图和背面图填 refer_images。此例不绑定音色、回调或标签，不填写无实际值的可选占位字段。创建请求的响应直接显示在终端；保存其中的主体创建任务 ID，随后查询创建结果。

```cURL
curl -sS --request POST \
  'https://api-beijing.klingai.com/v1/general/advanced-custom-elements' \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "element_name": "pink_pig_case_12_6",
  "element_description": "粉色卡通小猪，使用同一只小猪的正面、侧面和背面图片建立主体，用于箱子内新增熟睡小猪的案例。",
  "reference_type": "image_refer",
  "element_image_list": {
    "frontal_image": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch12_6_pink_pig_front_ref.png",
    "refer_images": [
      {
        "image_url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch12_6_pink_pig_side_ref.png"
      },
      {
        "image_url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch12_6_pink_pig_back_ref.png"
      }
    ]
  }
}'
```

##### 查询主体创建结果并取得主体 ID

将下方路径中的 REPLACE_WITH_ELEMENT_CREATION_TASK_ID 替换为创建主体时返回的任务 ID（不是主体 ID）。按所提供说明，也可使用唯一的 external_task_id 二选一查询；本例未设置 external_task_id，使用服务端任务 ID。

```cURL
curl -sS --request GET \
  'https://api-beijing.klingai.com/v1/general/advanced-custom-elements/REPLACE_WITH_ELEMENT_CREATION_TASK_ID' \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header 'Content-Type: application/json'
```

等待主体创建成功，从查询响应取得新建小猪的 element_id，填入第二步的 REPLACE_WITH_PIG_ELEMENT_ID。主体创建任务 ID、主体 element_id、视频任务 ID 是三种不同标识，不可混用。若仍在创建或已失败，不要执行第二步；未取得成功结果时不要重复创建主体。

##### 第二步：使用新建小猪主体编辑视频

```cURL
curl -sS --request POST \
  'https://api-beijing.klingai.com/omni-video/kling-4.0' \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "编辑 @video_1，在视频最后箱子再次被打开时，@element_1 正躺在里面睡觉。最后一句台词“Ah,they‘re all,old tricks,nothing new.”改为“Why is there a pig here?”。"
    },
    {
      "type": "base_video",
      "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch12_6_box_source.mp4",
      "id": "video_1"
    },
    {
      "type": "element",
      "element_id": "REPLACE_WITH_PIG_ELEMENT_ID",
      "id": "element_1"
    }
  ],
  "settings": {
    "resolution": "1080p",
    "aspect_ratio": "adaptive"
  }
}'
```

**人物及场景替换**

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

<div class="guide-case-media-list">
<div class="guide-case-shot">

<button type="button" class="guide-video-poster" data-src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-v-020.79c3a9b47481e578.mp4" aria-label="播放视频"><img src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-p-020.64a03f8fe590c67c.b9c537857240a540.webp" alt="" /></button>

<p>视频1</p>
</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-i-023.9f1edc325ceab418.c23d5f6e6c1d3b25.webp" alt="" /></div>

<p>图片1</p>
</div>
</div>

```text
编辑@视频1，把视频中的环境和人物，整体替换为@图片1 里的内容
```

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<button type="button" class="guide-video-poster" data-src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-v-022.871272fd58f693cd.mp4" aria-label="播放视频"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-p-022.729512c6adb5e11b.70dcaeb88af84521.webp" alt="" /></button>

API 代码：

```cURL
curl -sS --request POST \
  'https://api-beijing.klingai.com/omni-video/kling-4.0' \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "编辑 @video_1，把视频中的环境和人物，整体替换为 @image_1 里的内容。"
    },
    {
      "type": "base_video",
      "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch12_6_scene_swap_source.mp4",
      "id": "video_1"
    },
    {
      "type": "refer_image",
      "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch12_6_red_dress_woman_ref.png",
      "id": "image_1"
    }
  ],
  "settings": {
    "resolution": "1080p",
    "aspect_ratio": "adaptive"
  }
}'
```

**多角色替换**

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

<div class="guide-case-media-list guide-case-media-list-video-full">
<div class="guide-case-shot">

<button type="button" class="guide-video-poster" data-src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-v-028.0a32dba6dbdb9b31.mp4" aria-label="播放视频"><img src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-p-028.e5fa59578dada32e.824d3596e7d8d015.webp" alt="" /></button>

<p>视频1</p>
</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-i-019.b4219ec22489a6db.79225e6b851caf6a.webp" alt="" /></div>

<p>图片1</p>
</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap"><img src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-i-021.665dabb3d4f32dfc.8e5c6d1616289067.webp" alt="" /></div>

<p>图片2</p>
</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-i-024.064cc339c9c720c6.07d1bf5b9cd70799.webp" alt="" /></div>

<p>图片3</p>
</div>
</div>

```text
编辑 @视频1，将视频中从便利店门口依次走出的三位人物，分别替换为：第一位人物：使用 @图片1 的男性身份、脸、深色卷发、白色遮阳帽、白色短袖与黑白条纹内搭、绿色围裙、浅灰宽松牛仔裤和深色运动鞋。第二位人物：使用 @图片2 的女性身份、浅金色短卷发、红色卫衣、绿色围裙、白色长袜和红色鞋。第三位人物：使用 @图片3 的男性身份、浅金色短发、白色厨师帽、黑框眼镜、蓝绿黑图案针织套装、绿色围裙、白色鞋，以及他怀中同一个米白色布偶羊。三位人物的出场顺序、从店内走到门口、停下展示动作、走向镜头并从前景离开的节奏，参考 @视频1 的动作与镜头节奏：第一位轻抬遮阳帽帽檐后走近镜头；第二位在门口自然整理围裙、轻轻招手后走近镜头；第三位抱着布偶羊、扶正眼镜后走近镜头，并在接近镜头时将布偶羊微微举起。将便利店右侧玻璃窗中部的牌子固定一块清晰、稳定、可读的大写字牌：`KLING AI OPEN 24 hours`。文字必须始终拼写正确，不乱码、不变形、不闪烁；牌子固定在玻璃窗内侧，不能遮挡人物。其余完全不变：保持 @视频1 的绿色便利店门框、门口构图、店内货架、灯管、玻璃反射、白天光线、镜头机位、人物走路方向、时长、节奏和画幅。不要新增人物、不要改变店铺结构、不要改变镜头运动、不要出现字幕、logo、水印或额外文字。
```

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<button type="button" class="guide-video-poster" data-src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-v-021.c6d8afac7505b1f9.mp4" aria-label="播放视频"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-p-021.e35633afedff7980.aee88c2bf06d673a.webp" alt="" /></button>

API 代码：

```cURL
curl -sS --request POST \
  'https://api-beijing.klingai.com/omni-video/kling-4.0' \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "编辑 @视频1，将视频中从便利店门口依次走出的三位人物，分别替换为：第一位人物：使用 @图片1 的男性身份、脸、深色卷发、白色遮阳帽、白色短袖与黑白条纹内搭、绿色围裙、浅灰宽松牛仔裤和深色运动鞋。第二位人物：使用 @图片2 的女性身份、浅金色短卷发、红色卫衣、绿色围裙、白色长袜和红色鞋。第三位人物：使用 @图片3 的男性身份、浅金色短发、白色厨师帽、黑框眼镜、蓝绿黑图案针织套装、绿色围裙、白色鞋，以及他怀中同一个米白色布偶羊。三位人物的出场顺序、从店内走到门口、停下展示动作、走向镜头并从前景离开的节奏，参考 @视频1 的动作与镜头节奏：第一位轻抬遮阳帽帽檐后走近镜头；第二位在门口自然整理围裙、轻轻招手后走近镜头；第三位抱着布偶羊、扶正眼镜后走近镜头，并在接近镜头时将布偶羊微微举起。将便利店右侧玻璃窗中部的牌子固定一块清晰、稳定、可读的大写字牌：`KLING AI OPEN 24 hours`。文字必须始终拼写正确，不乱码、不变形、不闪烁；牌子固定在玻璃窗内侧，不能遮挡人物。其余完全不变：保持 @视频1 的绿色便利店门框、门口构图、店内货架、灯管、玻璃反射、白天光线、镜头机位、人物走路方向、时长、节奏和画幅。不要新增人物、不要改变店铺结构、不要改变镜头运动、不要出现字幕、logo、水印或额外文字。"
    },
    {
      "type": "base_video",
      "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch12_6_store_staff_source.mp4",
      "id": "视频1"
    },
    {
      "type": "refer_image",
      "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch12_6_visor_staff_ref.png",
      "id": "图片1"
    },
    {
      "type": "refer_image",
      "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch12_6_red_sweater_staff_ref.png",
      "id": "图片2"
    },
    {
      "type": "refer_image",
      "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch12_6_glasses_staff_ref.png",
      "id": "图片3"
    }
  ],
  "settings": {
    "resolution": "1080p",
    "aspect_ratio": "adaptive"
  }
}'
```

### 1.7 视频风格编辑

指定风格时，采用正向描述加负向排除的写法效果更稳定：

```text
编辑@视频1，将视频风格替换成@图片1的毛毡风格，保持原视频的构图、镜头、动作，只替换风格，不改变人物的服装款式、摩托车造型、场景元素及事件顺序。
```

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

<div class="guide-case-media-list">
<div class="guide-case-shot">

<button type="button" class="guide-video-poster" data-src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-v-023.d3db079330c69774.mp4" aria-label="播放视频"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-p-023.f7d511a744c621b1.01578c31c95d7127.webp" alt="" /></button>

<p>视频1</p>
</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap"><img src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-i-022.0f9f342385e77781.22e48a5492442b42.webp" alt="" /></div>

<p>图片1</p>
</div>
</div>

```text
编辑@视频1，将视频风格替换成@图片1的毛毡风风格，保持原视频的构图、镜头、动作，只替换风格。
```

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<button type="button" class="guide-video-poster" data-src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-v-026.075ab33d6ef6f233.mp4" aria-label="播放视频"><img src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-p-026.b14d452cdc21ec11.78b84ff9a3b61caa.webp" alt="" /></button>

API 代码：

```cURL
curl -sS --request POST \
  'https://api-beijing.klingai.com/omni-video/kling-4.0' \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "编辑 @video_1，将视频风格替换成 @image_1 的毛毡风格，保持原视频的构图、镜头、动作，只替换风格，不改变人物的服装款式、摩托车造型、场景元素及事件顺序。"
    },
    {
      "type": "base_video",
      "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch12_7_cyber_motorcycle_source.mov",
      "id": "video_1"
    },
    {
      "type": "refer_image",
      "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch12_7_felt_picnic_style_ref.png",
      "id": "image_1"
    }
  ],
  "settings": {
    "resolution": "1080p",
    "aspect_ratio": "adaptive"
  }
}'
```

### 1.8 字幕生成

适合品牌广告、产品包装和屏幕界面等需要准确呈现文字的画面。

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

<div class="guide-case-media-list">
<div class="guide-case-shot">

<div class="media-wrap image-wrap"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-i-020.978d3293498c6d64.4b06671319f7d0ac.webp" alt="" /></div>

<p>图片1</p>
</div>
</div>

```text
SCENE CONTEXTEXACT 3 UNIQUE CHARACTERS ACROSS THE VIDEO — NO DUPLICATES.EXT. enchanted counting forest classroom, warm morning. One soft cream cloud teacher teaches the numbers 1, 2, 3 and 4 in four separate shots. Two tiny yellow chick pupils appear only in the number-two shot.3 characters across the video, 5 hard-cut shots, 15s, real time.@Image1: visual-world reference only — handmade clay-and-felt materials, rounded toy-like forms, pastel forest trunks, mossy ground, rainbow colours, warm diffused backlight and shallow storybook depth. Never inherit its existing characters, numerals or composition.LOCATION MAPAll five shots occur on the same circular moss stage inside one enchanted forest classroom.One broad warm-brown tree trunk anchors frame-left; a second tree trunk anchors frame-right. A curved pastel rainbow root crosses the background.The central teaching pedestal remains in the same position in every shot.Camera always stays on the front side of the teaching axis, between 3.0 and 3.3 m from the pedestal.The sun always comes from upper frame-right. Background geometry, material scale and colour palette remain identical after every cut.FIRST FRAME AND SPATIAL BLOCKINGShot 1: the cloud teacher floats centre-left, facing a large red felt numeral 1 on the central pedestal. One red apple is concealed inside the moss below it.Shot 2: the cloud teacher floats centre-left, facing a large amber felt numeral 2. Two yellow chicks begin concealed behind the pedestal.Shot 3: the cloud teacher floats centre-left, facing a large green felt numeral 3. Three blue felt stars begin nested inside the moss.Shot 4: the cloud teacher floats centre-left, facing a large blue felt numeral 4. Four purple clay blocks begin below the pedestal.Shot 5: the cloud teacher floats alone at centre, facing the viewer beneath the rainbow root.Every shot begins mid-gesture with the teacher already pointing toward the active numeral. No empty establishing beat.FORMAT MODEHorizontal 16:9, total 15s, real time, 5 shots connected by clean hard cuts.Shot 1 — 0.00–4.00s: number 1 and one apple.Shot 2 — 4.00–7.08s: number 2 and two chicks.Shot 3 — 7.08–10.21s: number 3 and three stars.Shot 4 — 10.21–13.08s: number 4 and four blocks.Shot 5 — 13.08–15.00s: spoken recap and celebration.Each number receives its own separate shot. Numerals 1, 2, 3 and 4 never share the same teaching frame.No fades, dissolves or split screens.OPTICS35mm equivalent, 54° horizontal FOV, locked across all five shots.Identical natural perspective, camera height, background scale and depth-of-field character after every cut.Focal plane remains on the cloud teacher, active numeral and active quantity.Foreground flowers softly obscure the lower corners. Distant trees dissolve into the same creamy storybook blur.CAMERAEvery shot is operated handheld at approximately 105 cm height from the front side of the teaching axis.World register: gentle SETTLE.Shot 1: slow 10 cm push toward numeral 1.Shot 2: slow 10 cm push toward numeral 2.Shot 3: slow 10 cm push toward numeral 3.Shot 4: slow 10 cm push toward numeral 4.Shot 5: slow 8 cm push toward the celebrating teacher.Visible handheld character throughout: breath sway, micro-roll, late tiny corrections and gentle but obvious handmade shake. Numerals and subtitles remain readable.Camera height, axis and movement speed match across all cuts.Not a gimbal, slider, tripod lock-off, drone or digitally stabilised camera.ACTION TIMING0.00–0.78s: Shot 1 begins. The cloud teacher already points toward the red numeral 1.0.78–1.98s: numeral 1 rises and completes one soft bounce.1.98–4.00s: one red apple rises from the moss and settles beneath numeral 1.4.00–4.86s: hard cut to Shot 2. The amber numeral 2 rises and completes one soft bounce.4.86–7.08s: one yellow chick hops out from the left, then a second chick joins from the right; they touch shoulders and settle together.7.08–8.04s: hard cut to Shot 3. The green numeral 3 rises and completes one soft bounce.8.04–10.21s: two blue felt stars rise together, followed by one additional star; the three stars settle into a clear triangular arrangement.10.21–11.06s: hard cut to Shot 4. The blue numeral 4 rises and completes one soft bounce.11.06–13.08s: three purple blocks assemble first; one additional block clicks into the fourth position.13.08–14.40s: hard cut to Shot 5. Four tiny coloured fireflies pulse sequentially red, amber, green and blue while the teacher points from left to right.14.40–15.00s: the teacher opens both arms; a small clay sun unfolds above the rainbow and releases a brief sparkle burst.PHYSICSThe cloud teacher has the buoyancy of a lightweight stuffed felt puppet, with soft vertical drift and delayed arm movement.Each numeral has padded felt weight: it compresses, rebounds once and settles.The apple lands with soft clay weight. The chicks’ feet squash slightly into the moss. Stars descend with gentle air resistance. Blocks connect with firm edge-to-edge contact.Every quantity remains stable and readable until its shot ends.Hard cuts reset the teaching pedestal cleanly while preserving the same forest, teacher identity, material scale and lighting.LIGHTINGOne identical motivated source in every shot: warm morning sunlight filtering through the trees from upper frame-right.The teacher’s lower-left side remains slightly darker in all five shots.Soft rim light separates the felt fibres from the forest.Protect the cream cloud, pastel numerals and rainbow highlights from clipping.The direction, colour temperature, haze density and exposure remain unchanged across every cut.AUDIOVOICEOVER: the cloud teacher speaks in English with the same warm, clear, medium-high preschool-teacher voice in every shot. Pronunciation is slow, encouraging and rhythmically precise.0.78s: “One.”1.98s: “One means just one.”4.16s: “Two.”4.86s: “Two means one and one together.”7.26s: “Three.”8.04s: “Three means two and one more.”10.32s: “Four.”11.06s: “Four means three and one more.”13.32s: “One, two, three, four.”14.40s: “Great job!”MUSIC: one continuous original children’s instrumental across all cuts, using soft marimba, toy piano, light ukulele, felt-drum taps and gentle handclaps. The same melody, tempo and instrumentation continue seamlessly through every shot. It rises slightly with each new number and ends with a short celebratory flourish.SFX: one soft felt pop for each numeral bounce; one clay plop for the apple; two tiny moss footsteps for the chicks; three sparkle chimes for the stars; four wooden clicks for the blocks; four soft firefly pings during the recap; one bright celebration chime at the end.AMBIENCE: continuous close grass rustle, mid-distance leaves and faint woodland birds. The ambience never resets at the cuts.MIX: narration remains clear and centred. Music ducks beneath every spoken line. Sound effects synchronise exactly with the quantities. Music and ambience remain continuous across every hard cut.SUBTITLESBurned-in English subtitles, bottom-centre inside the title-safe area, positioned 10% above the lower edge.One or two lines maximum. Rounded cream felt subtitle panel with dark chocolate-brown bold lettering, high contrast and stable placement.Subtitles appear and disappear exactly with the matching narration:0.78–1.38s: “ONE.”1.98–3.84s: “ONE MEANS JUST ONE.”4.16–4.66s: “TWO.”4.86–6.82s: “TWO MEANS ONE AND ONE TOGETHER.”7.26–7.78s: “THREE.”8.04–10.16s: “THREE MEANS TWO AND ONE MORE.”10.32–10.80s: “FOUR.”11.06–13.08s: “FOUR MEANS THREE AND ONE MORE.”13.32–14.24s: “ONE, TWO, THREE, FOUR.”14.40–15.00s: “GREAT JOB!”CHARACTER ACTINGCloud teacher: identical body proportions, cream felt texture, tiny arms, dot eyes, rosy cheeks and small smiling mouth in every shot. Uses slow preschool-teaching gestures. The gaze always lands on the active numeral or quantity. The expression gradually changes from patient concentration in Shot 1 to a broad celebratory smile in Shot 5.Shot 1: points with one hand and watches the single apple settle.Shot 2: brings both hands together as the two chicks join.Shot 3: traces a small triangle after the third star appears.Shot 4: raises four soft fingertips after the final block connects.Shot 5: points across four firefly pulses, then opens both arms toward the viewer.Two chick pupils: appear only in Shot 2. The first chick leaves a visible space beside itself; the second fills that space. Both look up at the teacher and blink once after joining.STYLEOne perfectly consistent handmade clay-and-felt stop-motion storybook world across every shot.Rounded silhouettes, tactile fingerprints, plush fibres, softly imperfect surfaces, oversized friendly trees, moss carpet, tiny flowers and pastel rainbow details.Identical teacher model, forest geometry, prop scale, material softness, lens character and lighting direction after every cut.Soft vintage optical character, old-photograph texture, subtle film grain, slight halation and natural motion blur.Colour 60:30:10 = moss green and warm wood / cream and pastel numeral colours / coral-red and sunny-yellow accents.旧照片质感模糊不要锐化.QUALITYThe cloud teacher, active numeral, active quantity and subtitles remain readable in every shot.Numeral shapes are conventional, upright and unambiguous.Subtitle spelling, punctuation and timing match the specified script exactly.Subtitle size, typeface, panel shape and screen position remain identical across all cuts.Soft old-photo resolution, never digitally sharpened.Natural motion blur without ghosting, duplicated limbs, malformed numerals, incorrect quantities or plastic CGI surfaces.POSITIVE CONSTRAINTSNumbers 1, 2, 3 and 4 each receive one separate teaching shot.Only one large numeral appears in each teaching shot.Shot 1 contains exactly one apple.Shot 2 contains exactly two yellow chicks.Shot 3 contains exactly three blue stars.Shot 4 contains exactly four purple blocks.Shot 5 contains only the cloud teacher, four sequential firefly pulses and the final clay sun.The same cloud teacher identity, forest style, light direction, optics, colour palette, music and subtitle design continue across every cut.Speech count: exactly 10 lines.Every subtitle matches its spoken line word for word.A shared 1–4 teaching frame, split screen, incorrect quantity, extra character, style change, lighting change, malformed subtitle or mismatched narration = failed shot.
```

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<button type="button" class="guide-video-poster" data-src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-v-027.d167cab7002aaf1c.mp4" aria-label="播放视频"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-p-027.cebc8790d23ada91.1bf24e7050be71fb.webp" alt="" /></button>

API 代码：

```cURL
curl -sS --request POST \
  'https://api-beijing.klingai.com/omni-video/kling-4.0' \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "SCENE CONTEXTEXACT 3 UNIQUE CHARACTERS ACROSS THE VIDEO — NO DUPLICATES.EXT. enchanted counting forest classroom, warm morning. One soft cream cloud teacher teaches the numbers 1, 2, 3 and 4 in four separate shots. Two tiny yellow chick pupils appear only in the number-two shot.3 characters across the video, 5 hard-cut shots, 15s, real time.@Image1: visual-world reference only — handmade clay-and-felt materials, rounded toy-like forms, pastel forest trunks, mossy ground, rainbow colours, warm diffused backlight and shallow storybook depth. Never inherit its existing characters, numerals or composition.LOCATION MAPAll five shots occur on the same circular moss stage inside one enchanted forest classroom.One broad warm-brown tree trunk anchors frame-left; a second tree trunk anchors frame-right. A curved pastel rainbow root crosses the background.The central teaching pedestal remains in the same position in every shot.Camera always stays on the front side of the teaching axis, between 3.0 and 3.3 m from the pedestal.The sun always comes from upper frame-right. Background geometry, material scale and colour palette remain identical after every cut.FIRST FRAME AND SPATIAL BLOCKINGShot 1: the cloud teacher floats centre-left, facing a large red felt numeral 1 on the central pedestal. One red apple is concealed inside the moss below it.Shot 2: the cloud teacher floats centre-left, facing a large amber felt numeral 2. Two yellow chicks begin concealed behind the pedestal.Shot 3: the cloud teacher floats centre-left, facing a large green felt numeral 3. Three blue felt stars begin nested inside the moss.Shot 4: the cloud teacher floats centre-left, facing a large blue felt numeral 4. Four purple clay blocks begin below the pedestal.Shot 5: the cloud teacher floats alone at centre, facing the viewer beneath the rainbow root.Every shot begins mid-gesture with the teacher already pointing toward the active numeral. No empty establishing beat.FORMAT MODEHorizontal 16:9, total 15s, real time, 5 shots connected by clean hard cuts.Shot 1 — 0.00–4.00s: number 1 and one apple.Shot 2 — 4.00–7.08s: number 2 and two chicks.Shot 3 — 7.08–10.21s: number 3 and three stars.Shot 4 — 10.21–13.08s: number 4 and four blocks.Shot 5 — 13.08–15.00s: spoken recap and celebration.Each number receives its own separate shot. Numerals 1, 2, 3 and 4 never share the same teaching frame.No fades, dissolves or split screens.OPTICS35mm equivalent, 54° horizontal FOV, locked across all five shots.Identical natural perspective, camera height, background scale and depth-of-field character after every cut.Focal plane remains on the cloud teacher, active numeral and active quantity.Foreground flowers softly obscure the lower corners. Distant trees dissolve into the same creamy storybook blur.CAMERAEvery shot is operated handheld at approximately 105 cm height from the front side of the teaching axis.World register: gentle SETTLE.Shot 1: slow 10 cm push toward numeral 1.Shot 2: slow 10 cm push toward numeral 2.Shot 3: slow 10 cm push toward numeral 3.Shot 4: slow 10 cm push toward numeral 4.Shot 5: slow 8 cm push toward the celebrating teacher.Visible handheld character throughout: breath sway, micro-roll, late tiny corrections and gentle but obvious handmade shake. Numerals and subtitles remain readable.Camera height, axis and movement speed match across all cuts.Not a gimbal, slider, tripod lock-off, drone or digitally stabilised camera.ACTION TIMING0.00–0.78s: Shot 1 begins. The cloud teacher already points toward the red numeral 1.0.78–1.98s: numeral 1 rises and completes one soft bounce.1.98–4.00s: one red apple rises from the moss and settles beneath numeral 1.4.00–4.86s: hard cut to Shot 2. The amber numeral 2 rises and completes one soft bounce.4.86–7.08s: one yellow chick hops out from the left, then a second chick joins from the right; they touch shoulders and settle together.7.08–8.04s: hard cut to Shot 3. The green numeral 3 rises and completes one soft bounce.8.04–10.21s: two blue felt stars rise together, followed by one additional star; the three stars settle into a clear triangular arrangement.10.21–11.06s: hard cut to Shot 4. The blue numeral 4 rises and completes one soft bounce.11.06–13.08s: three purple blocks assemble first; one additional block clicks into the fourth position.13.08–14.40s: hard cut to Shot 5. Four tiny coloured fireflies pulse sequentially red, amber, green and blue while the teacher points from left to right.14.40–15.00s: the teacher opens both arms; a small clay sun unfolds above the rainbow and releases a brief sparkle burst.PHYSICSThe cloud teacher has the buoyancy of a lightweight stuffed felt puppet, with soft vertical drift and delayed arm movement.Each numeral has padded felt weight: it compresses, rebounds once and settles.The apple lands with soft clay weight. The chicks’ feet squash slightly into the moss. Stars descend with gentle air resistance. Blocks connect with firm edge-to-edge contact.Every quantity remains stable and readable until its shot ends.Hard cuts reset the teaching pedestal cleanly while preserving the same forest, teacher identity, material scale and lighting.LIGHTINGOne identical motivated source in every shot: warm morning sunlight filtering through the trees from upper frame-right.The teacher’s lower-left side remains slightly darker in all five shots.Soft rim light separates the felt fibres from the forest.Protect the cream cloud, pastel numerals and rainbow highlights from clipping.The direction, colour temperature, haze density and exposure remain unchanged across every cut.AUDIOVOICEOVER: the cloud teacher speaks in English with the same warm, clear, medium-high preschool-teacher voice in every shot. Pronunciation is slow, encouraging and rhythmically precise.0.78s: “One.”1.98s: “One means just one.”4.16s: “Two.”4.86s: “Two means one and one together.”7.26s: “Three.”8.04s: “Three means two and one more.”10.32s: “Four.”11.06s: “Four means three and one more.”13.32s: “One, two, three, four.”14.40s: “Great job!”MUSIC: one continuous original children’s instrumental across all cuts, using soft marimba, toy piano, light ukulele, felt-drum taps and gentle handclaps. The same melody, tempo and instrumentation continue seamlessly through every shot. It rises slightly with each new number and ends with a short celebratory flourish.SFX: one soft felt pop for each numeral bounce; one clay plop for the apple; two tiny moss footsteps for the chicks; three sparkle chimes for the stars; four wooden clicks for the blocks; four soft firefly pings during the recap; one bright celebration chime at the end.AMBIENCE: continuous close grass rustle, mid-distance leaves and faint woodland birds. The ambience never resets at the cuts.MIX: narration remains clear and centred. Music ducks beneath every spoken line. Sound effects synchronise exactly with the quantities. Music and ambience remain continuous across every hard cut.SUBTITLESBurned-in English subtitles, bottom-centre inside the title-safe area, positioned 10% above the lower edge.One or two lines maximum. Rounded cream felt subtitle panel with dark chocolate-brown bold lettering, high contrast and stable placement.Subtitles appear and disappear exactly with the matching narration:0.78–1.38s: “ONE.”1.98–3.84s: “ONE MEANS JUST ONE.”4.16–4.66s: “TWO.”4.86–6.82s: “TWO MEANS ONE AND ONE TOGETHER.”7.26–7.78s: “THREE.”8.04–10.16s: “THREE MEANS TWO AND ONE MORE.”10.32–10.80s: “FOUR.”11.06–13.08s: “FOUR MEANS THREE AND ONE MORE.”13.32–14.24s: “ONE, TWO, THREE, FOUR.”14.40–15.00s: “GREAT JOB!”CHARACTER ACTINGCloud teacher: identical body proportions, cream felt texture, tiny arms, dot eyes, rosy cheeks and small smiling mouth in every shot. Uses slow preschool-teaching gestures. The gaze always lands on the active numeral or quantity. The expression gradually changes from patient concentration in Shot 1 to a broad celebratory smile in Shot 5.Shot 1: points with one hand and watches the single apple settle.Shot 2: brings both hands together as the two chicks join.Shot 3: traces a small triangle after the third star appears.Shot 4: raises four soft fingertips after the final block connects.Shot 5: points across four firefly pulses, then opens both arms toward the viewer.Two chick pupils: appear only in Shot 2. The first chick leaves a visible space beside itself; the second fills that space. Both look up at the teacher and blink once after joining.STYLEOne perfectly consistent handmade clay-and-felt stop-motion storybook world across every shot.Rounded silhouettes, tactile fingerprints, plush fibres, softly imperfect surfaces, oversized friendly trees, moss carpet, tiny flowers and pastel rainbow details.Identical teacher model, forest geometry, prop scale, material softness, lens character and lighting direction after every cut.Soft vintage optical character, old-photograph texture, subtle film grain, slight halation and natural motion blur.Colour 60:30:10 = moss green and warm wood / cream and pastel numeral colours / coral-red and sunny-yellow accents.旧照片质感模糊不要锐化.QUALITYThe cloud teacher, active numeral, active quantity and subtitles remain readable in every shot.Numeral shapes are conventional, upright and unambiguous.Subtitle spelling, punctuation and timing match the specified script exactly.Subtitle size, typeface, panel shape and screen position remain identical across all cuts.Soft old-photo resolution, never digitally sharpened.Natural motion blur without ghosting, duplicated limbs, malformed numerals, incorrect quantities or plastic CGI surfaces.POSITIVE CONSTRAINTSNumbers 1, 2, 3 and 4 each receive one separate teaching shot.Only one large numeral appears in each teaching shot.Shot 1 contains exactly one apple.Shot 2 contains exactly two yellow chicks.Shot 3 contains exactly three blue stars.Shot 4 contains exactly four purple blocks.Shot 5 contains only the cloud teacher, four sequential firefly pulses and the final clay sun.The same cloud teacher identity, forest style, light direction, optics, colour palette, music and subtitle design continue across every cut.Speech count: exactly 10 lines.Every subtitle matches its spoken line word for word.A shared 1–4 teaching frame, split screen, incorrect quantity, extra character, style change, lighting change, malformed subtitle or mismatched narration = failed shot."
    },
    {
      "type": "refer_image",
      "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch12_8_counting_forest_style_ref.png",
      "id": "image_1"
    }
  ],
  "settings": {
    "duration": 22,
    "resolution": "1080p",
    "aspect_ratio": "adaptive"
  }
}'
```

### 1.9 关键帧

##### ① 首帧

写法：@图片1 作为首帧，[后续发生什么]

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

<div class="guide-case-media-list">
<div class="guide-case-shot">

<div class="media-wrap image-wrap"><img src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-i-018.22f8d233ae2ccbd1.b522314bd4ab011d.webp" alt="" /></div>

<p>图片1</p>
</div>
<div class="guide-case-shot">

<button type="button" class="guide-video-poster" data-src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-v-024.12b3ea4b5f9a368e.mp4" aria-label="播放视频"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-p-024.16a28d2c9ebc6bb6.b0fc3474b657772d.webp" alt="" /></button>

<p>视频1</p>
</div>
</div>

```text
@图片1 is the first frame.  @视频1 is the reference for camera, motion, timing and cuts. Recreate  @视频1  shot-for-shot and cut-for-cut, but starting from @图片1 : the rider is SITTING in a black office swivel chair instead of standing on a bike. Same chest-mounted GoPro fisheye POV, same ramp, canyon, river, orange parachute with white ring, airboat and cheering crew, same three jump-cuts and audio as @视频1 . Wherever  @视频1 shows the bike — under the rider on the ramp, shoved away at the cliff, tumbling below in free-fall, and the tiny silhouette during the parachute opening — show the office chair (mesh backrest, padded seat, chrome column, five-spoke base, casters). Before the launch the rider stays seated exactly as in  @图片1 : thighs and knees at the bottom of frame, sneakers on the star base, hands on the armrests. No bicycle, handlebar, tyres or pedals anywhere.
```

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<button type="button" class="guide-video-poster" data-src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-v-025.c71b8cec57ebb857.mp4" aria-label="播放视频"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-p-025.45a70b577a7c8e86.696f48c1a0c15b47.webp" alt="" /></button>

API 代码：

```cURL
curl -sS --request POST \
  'https://api-beijing.klingai.com/omni-video/kling-4.0' \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "Use @image_1 as the exact first frame and seated pose. Recreate @video_1 shot-for-shot, preserving its chest-mounted GoPro fisheye POV, motion, timing, three jump-cuts and original audio. Replace every bicycle appearance with the same black office swivel chair: mesh back, padded seat, armrests, chrome column, five-spoke caster base. Match its presence on the ramp, push-away at the cliff, tumble below during free-fall and tiny silhouette during parachute deployment. Before launch, keep the rider seated: thighs and knees at frame-bottom, sneakers on the chair base, hands on armrests. After separation, preserve the reference rider and object trajectories. Keep the ramp, canyon, river, orange parachute with white ring, airboat and cheering crew unchanged. No bicycle or bicycle parts in any frame."
    },
    {
      "type": "first_frame",
      "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch12_9_canyon_chair_first_frame.png",
      "id": "image_1"
    },
    {
      "type": "feature_video",
      "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch12_9_canyon_jump_source.mp4",
      "id": "video_1"
    }
  ],
  "settings": {
    "resolution": "1080p",
    "aspect_ratio": "adaptive"
  }
}'
```

##### ② 首尾帧

写法：@图片1 作为首帧，@图片2 作为尾帧，生成中间的[过程]

适用情况：变化过程展示、工艺展示、前后对比类内容。

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

<div class="guide-case-media-list">
<div class="guide-case-shot">

<div class="media-wrap image-wrap"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-i-027.28ce7e516ccab32c.83e566b8692238e9.webp" alt="" /></div>

<p>首帧</p>
</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-i-033.77ca9a04f21afed5.86c246c78551a2cd.webp" alt="" /></div>

<p>尾帧</p>
</div>
</div>

```text
SCENE CONTEXTEXACT 1 CHARACTER — NO DUPLICATES.Interior, a worn blacksmith workshop, daytime.The same blacksmith removes the raw material, works it into a greatsword, and returns the completed sword to the original table.15 seconds, six shots. Manufacturing time is compressed through editorial cuts; individual actions retain natural weight and speed.ACTIVE REFERENCES@Image1: exact first-frame anchor. Preserve all five iron blocks, their arrangement, the tabletop, background tools, perspective, and lighting. This image is the starting state of an active pickup shot.@Image2: exact final-frame anchor and finished-sword design. Preserve the blade silhouette, central fuller, angular curved crossguard, spiral metal grip, faceted pommel, diagonal placement, perspective, and background. This composition is reached through a visible physical placement.LOCATION MAPThe worktable fills the foreground. The tool bucket stands behind its left-center edge, the rod rack occupies the rear right, and the anvil stands at the right.The blacksmith works from the left side of the table in both endpoint shots.The camera stays on the original viewer-facing side of the table.During blade-working inserts, the tang points screen-left and the tip points screen-right.The final sword position runs from the upper-left pommel to the lower-right tip.FIRST FRAME AND SPATIAL BLOCKINGAt 0.0 seconds, the frame exactly matches the raw-material reference, with five iron blocks and no hands visible.The same blacksmith immediately reaches in from the left edge.Both gloved hands approach the largest central block from opposite ends, preparing a supported two-handed lift.The blacksmith wears soot-gray sleeves, brown leather gloves, and a narrow dark strap around the right cuff. These details remain identical throughout every shot.FORMAT MODE15 seconds total, six shots.Hard cuts at 3.0, 5.0, 8.0, 10.0, and 11.0 seconds.Cuts compress the omitted manufacturing work and bench clearing.The opening pickup and closing placement each play as continuous physical actions.No fades, dissolves, or object-morph transitions.OPTICSShots 1 and 6: reference-matched elevated three-quarter framing, approximately 63° diagonal field of view and approximately 1.8 meters from the tabletop center.Exact endpoint framing takes priority over estimated optical measurements.Shots 2–5: 40° diagonal field of view, approximately 0.8 meters from the working contact point.Focus follows the hands and metal contact; the workshop background remains softly readable.Each shot holds one fixed field of view.CAMERAA real camera operator holds the camera from the viewer-facing side of the workspace.All shots use handheld SETTLE: visible breathing sway, slight roll, and small delayed corrections.The opening camera holds its position while the iron block leaves the frame.The closing camera holds the empty tabletop composition while the sword enters, then settles into the exact final reference.The blacksmith is the only visible worker; the camera operator remains outside the image.ACTION TIMING0.0–3.0s — TAKE THE IRON.Start on the exact first reference; during 0.0–0.6s, the blacksmith’s matching gloved hands enter from screen-left and grip opposite ends of the largest central block.During 0.6–1.5s, the wrists brace and both hands lift the block clear of the tabletop, exposing the patch of table beneath it.During 1.5–3.0s, the blacksmith carries the supported block out through screen-left; the other four blocks remain resting on the table through the cut.3.0–5.0s — HEAT THE STOCK.Hard cut forward in time to one thick billet already glowing orange among forge coals.The same gray sleeves, brown gloves, and right-cuff strap appear at screen-left as the blacksmith holds long tongs around the billet.A short controlled pull draws the billet toward the forge mouth, with heat shimmer rising above its scaled surface.5.0–8.0s — FORGE THE BLADE.Hard cut forward to an elongated orange-hot blade blank supported on the anvil, tang left and emerging tip right.The same blacksmith braces the tang with left-hand tongs and delivers three deliberate right-hand hammer strikes along the blade flat.Each strike produces local compression, wrist recoil, and a brief scatter of dark scale.8.0–10.0s — FINISH THE METAL.Hard cut forward to a cooled blade with its fuller already formed, held by the same gloved hands against an abrasive wheel.The blacksmith makes one controlled finishing pass along the bevel.A narrow stream of sparks falls from the actual contact point as a brighter strip of metal appears.10.0–11.0s — COMPLETE THE HILT.Hard cut forward to the nearly finished sword supported on a separate assembly bench, its crossguard and spiral metal grip already fitted.The same blacksmith’s left hand braces the grip while the right hand gives the faceted pommel its final tightening turn.The completed sword now has the exact construction and finish required for the final image.11.0–15.0s — PLACE THE FINISHED SWORD.Hard cut to the original worktable, now completely clear; show its empty surface for 0.4 seconds before the same gloved hands carry the completed sword in from screen-left, one hand around the grip and the other supporting the blade flat near its balance point.From 11.4–13.8s, the blacksmith lowers the entire rigid sword diagonally, hilt toward upper-left and tip toward lower-right, easing it onto the tabletop and sliding the supporting hand free as its weight transfers to the table.From 13.8–15.0s, both hands release and withdraw through screen-left; the sword remains motionless in the exact final-reference position as the camera settles onto the final frame.PHYSICSThe raw block retains its shape and mass throughout the pickup.Both hands support it continuously; the forearms tense and the lift accelerates slowly under its weight.The anvil supports the hot blade during forging. Large changes of shape occur across editorial time jumps.The completed sword remains rigid during carrying and placement.The blade-supporting hand has visible clearance to slide free as the sword settles; the hand never passes through the blade or tabletop.Metal contact produces a short scrape and a low, heavy clink, followed by stillness.The same blacksmith clears the remaining raw stock during omitted time before the final shot.LIGHTINGThe original table shots use soft daylight from upper camera-left, matching both references.Retain dark detail in the iron and protect the silver blade highlights.The forge insert uses orange coal glow from below-left as its dominant source.Return to the original neutral daylight before the sword enters the final tabletop shot.AUDIOQuiet workshop air and distant furnace draft form the ambient bed.Opening: leather creaks, a brief iron scrape, and a restrained exertion breath as the heavy block rises.Middle: forge crackle, tong contact, three synchronized hammer impacts, abrasive scraping, and a short fitting sound.Ending: sleeve movement, glove friction against metal, a weighted sword-to-table clink, then quiet workshop ambience.The blacksmith speaks no dialogue.SFX only, no music, no score, no song, no soundtrack.CHARACTER ACTINGOne consistent blacksmith performs every visible action.Soot-gray sleeves, brown leather gloves, and the dark right-cuff strap remain unchanged.Hands work deliberately: brace before lifting, maintain firm tool contact, and reduce speed before lowering the finished sword.The physical rhythm shifts from effort during the raw-block pickup to careful control during the final placement.The face and torso remain outside the crop.STYLEGrounded workshop documentary with tactile iron, worn tools, and convincing manual labor.Soft old-photograph texture, restrained grain, and natural motion blur; no digital sharpening.Charcoal metal and muted brown surfaces dominate, with silver highlights and localized forge orange.The first and last frames preserve the supplied images’ appearance.QUALITYMaintain consistent hands, gloves, sleeve details, metal geometry, and contact shadows.The lifted block reveals the tabletop underneath it.The closing shot visibly establishes the empty tabletop before the sword enters.Keep the full final sword readable, including its tip, guard, grip, and pommel.Avoid duplicate limbs, flickering geometry, and intersecting solid surfaces.POSITIVE CONSTRAINTSThe first frame contains exactly five iron blocks.The largest central block physically leaves the table in the same blacksmith’s two hands.The final shot begins with an empty table.The completed sword enters while visibly supported by that same blacksmith, contacts the tabletop, and remains after both hands withdraw.The last frame matches the finished-sword reference exactly.The opening pickup and final placement each remain continuous, with visible hand-object contact.Exactly one finished sword is present.No text overlays, subtitles, or music.
```

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<button type="button" class="guide-video-poster" data-src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-v-030.7a498f2c5e50a874.mp4" aria-label="播放视频"><img src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-p-030.e430c83637a2bb66.0de7b05e7fed364d.webp" alt="" /></button>

API 代码：

```cURL
curl -sS --request POST \
  'https://api-beijing.klingai.com/image-to-video/kling-4.0' \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "SCENE CONTEXTEXACT 1 CHARACTER — NO DUPLICATES.Interior, a worn blacksmith workshop, daytime.The same blacksmith removes the raw material, works it into a greatsword, and returns the completed sword to the original table.15 seconds, six shots. Manufacturing time is compressed through editorial cuts; individual actions retain natural weight and speed.ACTIVE REFERENCES@Image1: exact first-frame anchor. Preserve all five iron blocks, their arrangement, the tabletop, background tools, perspective, and lighting. This image is the starting state of an active pickup shot.@Image2: exact final-frame anchor and finished-sword design. Preserve the blade silhouette, central fuller, angular curved crossguard, spiral metal grip, faceted pommel, diagonal placement, perspective, and background. This composition is reached through a visible physical placement.LOCATION MAPThe worktable fills the foreground. The tool bucket stands behind its left-center edge, the rod rack occupies the rear right, and the anvil stands at the right.The blacksmith works from the left side of the table in both endpoint shots.The camera stays on the original viewer-facing side of the table.During blade-working inserts, the tang points screen-left and the tip points screen-right.The final sword position runs from the upper-left pommel to the lower-right tip.FIRST FRAME AND SPATIAL BLOCKINGAt 0.0 seconds, the frame exactly matches the raw-material reference, with five iron blocks and no hands visible.The same blacksmith immediately reaches in from the left edge.Both gloved hands approach the largest central block from opposite ends, preparing a supported two-handed lift.The blacksmith wears soot-gray sleeves, brown leather gloves, and a narrow dark strap around the right cuff. These details remain identical throughout every shot.FORMAT MODE15 seconds total, six shots.Hard cuts at 3.0, 5.0, 8.0, 10.0, and 11.0 seconds.Cuts compress the omitted manufacturing work and bench clearing.The opening pickup and closing placement each play as continuous physical actions.No fades, dissolves, or object-morph transitions.OPTICSShots 1 and 6: reference-matched elevated three-quarter framing, approximately 63° diagonal field of view and approximately 1.8 meters from the tabletop center.Exact endpoint framing takes priority over estimated optical measurements.Shots 2–5: 40° diagonal field of view, approximately 0.8 meters from the working contact point.Focus follows the hands and metal contact; the workshop background remains softly readable.Each shot holds one fixed field of view.CAMERAA real camera operator holds the camera from the viewer-facing side of the workspace.All shots use handheld SETTLE: visible breathing sway, slight roll, and small delayed corrections.The opening camera holds its position while the iron block leaves the frame.The closing camera holds the empty tabletop composition while the sword enters, then settles into the exact final reference.The blacksmith is the only visible worker; the camera operator remains outside the image.ACTION TIMING0.0–3.0s — TAKE THE IRON.Start on the exact first reference; during 0.0–0.6s, the blacksmith’s matching gloved hands enter from screen-left and grip opposite ends of the largest central block.During 0.6–1.5s, the wrists brace and both hands lift the block clear of the tabletop, exposing the patch of table beneath it.During 1.5–3.0s, the blacksmith carries the supported block out through screen-left; the other four blocks remain resting on the table through the cut.3.0–5.0s — HEAT THE STOCK.Hard cut forward in time to one thick billet already glowing orange among forge coals.The same gray sleeves, brown gloves, and right-cuff strap appear at screen-left as the blacksmith holds long tongs around the billet.A short controlled pull draws the billet toward the forge mouth, with heat shimmer rising above its scaled surface.5.0–8.0s — FORGE THE BLADE.Hard cut forward to an elongated orange-hot blade blank supported on the anvil, tang left and emerging tip right.The same blacksmith braces the tang with left-hand tongs and delivers three deliberate right-hand hammer strikes along the blade flat.Each strike produces local compression, wrist recoil, and a brief scatter of dark scale.8.0–10.0s — FINISH THE METAL.Hard cut forward to a cooled blade with its fuller already formed, held by the same gloved hands against an abrasive wheel.The blacksmith makes one controlled finishing pass along the bevel.A narrow stream of sparks falls from the actual contact point as a brighter strip of metal appears.10.0–11.0s — COMPLETE THE HILT.Hard cut forward to the nearly finished sword supported on a separate assembly bench, its crossguard and spiral metal grip already fitted.The same blacksmith’s left hand braces the grip while the right hand gives the faceted pommel its final tightening turn.The completed sword now has the exact construction and finish required for the final image.11.0–15.0s — PLACE THE FINISHED SWORD.Hard cut to the original worktable, now completely clear; show its empty surface for 0.4 seconds before the same gloved hands carry the completed sword in from screen-left, one hand around the grip and the other supporting the blade flat near its balance point.From 11.4–13.8s, the blacksmith lowers the entire rigid sword diagonally, hilt toward upper-left and tip toward lower-right, easing it onto the tabletop and sliding the supporting hand free as its weight transfers to the table.From 13.8–15.0s, both hands release and withdraw through screen-left; the sword remains motionless in the exact final-reference position as the camera settles onto the final frame.PHYSICSThe raw block retains its shape and mass throughout the pickup.Both hands support it continuously; the forearms tense and the lift accelerates slowly under its weight.The anvil supports the hot blade during forging. Large changes of shape occur across editorial time jumps.The completed sword remains rigid during carrying and placement.The blade-supporting hand has visible clearance to slide free as the sword settles; the hand never passes through the blade or tabletop.Metal contact produces a short scrape and a low, heavy clink, followed by stillness.The same blacksmith clears the remaining raw stock during omitted time before the final shot.LIGHTINGThe original table shots use soft daylight from upper camera-left, matching both references.Retain dark detail in the iron and protect the silver blade highlights.The forge insert uses orange coal glow from below-left as its dominant source.Return to the original neutral daylight before the sword enters the final tabletop shot.AUDIOQuiet workshop air and distant furnace draft form the ambient bed.Opening: leather creaks, a brief iron scrape, and a restrained exertion breath as the heavy block rises.Middle: forge crackle, tong contact, three synchronized hammer impacts, abrasive scraping, and a short fitting sound.Ending: sleeve movement, glove friction against metal, a weighted sword-to-table clink, then quiet workshop ambience.The blacksmith speaks no dialogue.SFX only, no music, no score, no song, no soundtrack.CHARACTER ACTINGOne consistent blacksmith performs every visible action.Soot-gray sleeves, brown leather gloves, and the dark right-cuff strap remain unchanged.Hands work deliberately: brace before lifting, maintain firm tool contact, and reduce speed before lowering the finished sword.The physical rhythm shifts from effort during the raw-block pickup to careful control during the final placement.The face and torso remain outside the crop.STYLEGrounded workshop documentary with tactile iron, worn tools, and convincing manual labor.Soft old-photograph texture, restrained grain, and natural motion blur; no digital sharpening.Charcoal metal and muted brown surfaces dominate, with silver highlights and localized forge orange.The first and last frames preserve the supplied images’ appearance.QUALITYMaintain consistent hands, gloves, sleeve details, metal geometry, and contact shadows.The lifted block reveals the tabletop underneath it.The closing shot visibly establishes the empty tabletop before the sword enters.Keep the full final sword readable, including its tip, guard, grip, and pommel.Avoid duplicate limbs, flickering geometry, and intersecting solid surfaces.POSITIVE CONSTRAINTSThe first frame contains exactly five iron blocks.The largest central block physically leaves the table in the same blacksmith’s two hands.The final shot begins with an empty table.The completed sword enters while visibly supported by that same blacksmith, contacts the tabletop, and remains after both hands withdraw.The last frame matches the finished-sword reference exactly.The opening pickup and final placement each remain continuous, with visible hand-object contact.Exactly one finished sword is present.No text overlays, subtitles, or music."
    },
    {
      "type": "first_frame",
      "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch12_9_iron_blocks_first_frame.png",
      "id": "Image1"
    },
    {
      "type": "last_frame",
      "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch12_9_greatsword_last_frame.png",
      "id": "Image2"
    }
  ],
  "settings": {
    "duration": 15,
    "resolution": "1080p"
  }
}'
```

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

<div class="guide-case-media-list">
<div class="guide-case-shot">

<div class="media-wrap image-wrap"><img src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-i-026.93fb6135a7799cac.3e43471caa2e5de1.webp" alt="" /></div>

<p>首帧</p>
</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap"><img src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-i-035.e4ca794832022c06.31ed2208758e6131.webp" alt="" /></div>

<p>尾帧</p>
</div>
</div>

```text
生成一支 20 秒横屏 16:9 写实电影感街头逃跑视频。全片是一个连续横向侧面跟拍长镜头，一镜到底，不切镜、不换角度、不换场景。场景发生在曼哈顿风格的繁忙街道。冷调低饱和胶片质感，浅景深，真实手持肩扛稳定器运镜。街道上有餐厅户外座位区、黄色出租车、停靠车辆、报刊架、消火栓、施工脚手架、橱窗玻璃、地铁通风口白色蒸汽、行人和远处密集人流。前景物体不断快速刷过画面，制造遮挡和真实街道纵深。镜头始终与街道平行，向左横向移动，跟随一名年轻女性奔跑。她手里拎着一个塞满东西的大号旅行袋，旅行袋明显很重，随着奔跑滞后摆动，沉沉撞在她腿侧，带得身体微微偏斜。她神情紧张、疲惫，急促喘息，偶尔回头看身后，但画面中不要出现任何追赶者。0–5s：平静街头建立镜头先对准餐厅户外座位区。一位路人正端起咖啡，旁边有金属圆桌、藤编椅、遮阳篷和行人。街道环境音为主：车流、人声、脚步声、远处喇叭。摄影机以很慢的速度向左横移，画面平静。画面右侧边缘逐渐出现女主高速冲入的模糊身影。5–12s：女主冲入，镜头追上她女主从右侧冲入画面，摄影机像被她带动一样迅速加速向左横移并追上她。焦点从街景拉到她脸上，中间允许有轻微过焦和回拉。她全力奔跑，嘴张开喘气，眉头紧锁，下颌绷紧。她两次回头看身后，第二次更明显，露出恐慌和疲惫。她拎着沉重的大号旅行袋，袋子随着每次摆臂滞后晃动，沉沉撞在她腿侧，让她身体微微偏斜。她擦过户外座椅，冲过地铁通风格栅，白色蒸汽被带起，前景行人和街边物体快速刷过画面。12–15s：遮挡与跟丢一辆黄色出租车或一组行人从摄影机和女主之间快速经过，完全遮挡画面约半秒到一秒。遮挡结束后，女主已经不在画面中心。摄影机继续横移但明显减速，短暂失焦，像摄影师在寻找她。镜头扫过路灯杆、行人背影、报刊架、停靠车辆和橱窗反射。15–20s：重新找到女主镜头在人行道中继续寻找，焦点在前景行人、橱窗反射和街边物体之间短暂拉扯，随后在更远处重新捕捉到女主的背影和侧脸。她仍在向左奔跑，但比之前更疲惫。摄影机再次加速追上她，焦点从前景行人拉回她的身体和脸部。她的速度开始下降，呼吸更重，步幅变小，旅行袋越来越沉。她短暂把旅行袋换到另一只手，又立刻换回去，手指紧紧抓住提手，身体被袋子的重量拖得更明显。她冲进人群，逐渐消失镜头重新跟住女主侧面全身。她穿过施工脚手架旁，绿色防护网和金属立柱在前景一根根快速刷过。橱窗玻璃里短暂映出她奔跑的倒影。她脸上有汗，表情从恐慌变成筋疲力尽的坚持。最后她冲进步行街入口的密集人流。画面质感真实街头电影追逐感，冷调低饱和胶片调色，暗部保留细节，高光柔和，细腻胶片颗粒。浅景深，前景和背景在运动中自然虚化。焦点有轻微过焦、回拉和短暂失焦，像真人摄影师手动跟焦。运镜有真实肩扛稳定器质感，带轻微上下浮动、左右摆动、加速和减速惯性，但不要剧烈晃动。负面要求不要切镜、不要跳切、不要闪白、不要叠化、不要慢动作、不要变速、不要字幕、不要水印、不要 UI、不要背景音乐。不要出现追赶者，不要出现三个西装男，不要新增明确反派角色。不要机械轨道感运镜，不要人物滑行，奔跑必须有真实落地重量。不要让旅行袋失去重量感。不要让女主跑得优雅平静。不要肢体穿模，不要人群融合，不要突然换街道、换人物、换服装、换镜头角度。
```

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<button type="button" class="guide-video-poster" data-src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-v-031.ff1b933341450409.mp4" aria-label="播放视频"><img src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-p-031.d5cac570473a2e44.37e816d846157205.webp" alt="" /></button>

API 代码：

```cURL
curl -sS --request POST \
  'https://api-beijing.klingai.com/image-to-video/kling-4.0' \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "生成一支 20 秒横屏 16:9 写实电影感街头逃跑视频。全片是一个连续横向侧面跟拍长镜头，一镜到底，不切镜、不换角度、不换场景。场景发生在曼哈顿风格的繁忙街道。冷调低饱和胶片质感，浅景深，真实手持肩扛稳定器运镜。街道上有餐厅户外座位区、黄色出租车、停靠车辆、报刊架、消火栓、施工脚手架、橱窗玻璃、地铁通风口白色蒸汽、行人和远处密集人流。前景物体不断快速刷过画面，制造遮挡和真实街道纵深。镜头始终与街道平行，向左横向移动，跟随一名年轻女性奔跑。她手里拎着一个塞满东西的大号旅行袋，旅行袋明显很重，随着奔跑滞后摆动，沉沉撞在她腿侧，带得身体微微偏斜。她神情紧张、疲惫，急促喘息，偶尔回头看身后，但画面中不要出现任何追赶者。0–5s：平静街头建立镜头先对准餐厅户外座位区。一位路人正端起咖啡，旁边有金属圆桌、藤编椅、遮阳篷和行人。街道环境音为主：车流、人声、脚步声、远处喇叭。摄影机以很慢的速度向左横移，画面平静。画面右侧边缘逐渐出现女主高速冲入的模糊身影。5–12s：女主冲入，镜头追上她女主从右侧冲入画面，摄影机像被她带动一样迅速加速向左横移并追上她。焦点从街景拉到她脸上，中间允许有轻微过焦和回拉。她全力奔跑，嘴张开喘气，眉头紧锁，下颌绷紧。她两次回头看身后，第二次更明显，露出恐慌和疲惫。她拎着沉重的大号旅行袋，袋子随着每次摆臂滞后晃动，沉沉撞在她腿侧，让她身体微微偏斜。她擦过户外座椅，冲过地铁通风格栅，白色蒸汽被带起，前景行人和街边物体快速刷过画面。12–15s：遮挡与跟丢一辆黄色出租车或一组行人从摄影机和女主之间快速经过，完全遮挡画面约半秒到一秒。遮挡结束后，女主已经不在画面中心。摄影机继续横移但明显减速，短暂失焦，像摄影师在寻找她。镜头扫过路灯杆、行人背影、报刊架、停靠车辆和橱窗反射。15–20s：重新找到女主镜头在人行道中继续寻找，焦点在前景行人、橱窗反射和街边物体之间短暂拉扯，随后在更远处重新捕捉到女主的背影和侧脸。她仍在向左奔跑，但比之前更疲惫。摄影机再次加速追上她，焦点从前景行人拉回她的身体和脸部。她的速度开始下降，呼吸更重，步幅变小，旅行袋越来越沉。她短暂把旅行袋换到另一只手，又立刻换回去，手指紧紧抓住提手，身体被袋子的重量拖得更明显。她冲进人群，逐渐消失镜头重新跟住女主侧面全身。她穿过施工脚手架旁，绿色防护网和金属立柱在前景一根根快速刷过。橱窗玻璃里短暂映出她奔跑的倒影。她脸上有汗，表情从恐慌变成筋疲力尽的坚持。最后她冲进步行街入口的密集人流。画面质感真实街头电影追逐感，冷调低饱和胶片调色，暗部保留细节，高光柔和，细腻胶片颗粒。浅景深，前景和背景在运动中自然虚化。焦点有轻微过焦、回拉和短暂失焦，像真人摄影师手动跟焦。运镜有真实肩扛稳定器质感，带轻微上下浮动、左右摆动、加速和减速惯性，但不要剧烈晃动。负面要求不要切镜、不要跳切、不要闪白、不要叠化、不要慢动作、不要变速、不要字幕、不要水印、不要 UI、不要背景音乐。不要出现追赶者，不要出现三个西装男，不要新增明确反派角色。不要机械轨道感运镜，不要人物滑行，奔跑必须有真实落地重量。不要让旅行袋失去重量感。不要让女主跑得优雅平静。不要肢体穿模，不要人群融合，不要突然换街道、换人物、换服装、换镜头角度。"
    },
    {
      "type": "first_frame",
      "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch12_9_cafe_street_first_frame.png",
      "id": "start"
    },
    {
      "type": "last_frame",
      "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch12_9_street_crowd_last_frame.png",
      "id": "end"
    }
  ],
  "settings": {
    "resolution": "1080p"
  }
}'
```

##### ③ 尾帧

写法：@图片1 作为尾帧，[前面发生什么]

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

<div class="guide-case-media-list">
<div class="guide-case-shot">

<div class="media-wrap image-wrap"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-i-034.b2f314f2702b8278.04c4f8e6ef2a4f7d.webp" alt="" /></div>

<p>图片1</p>
</div>
</div>

```text
以@图片1 作为尾帧、人物服饰、站位、光影和绘画色彩的参考。创作一段15的电影短片：前半段完全是写实真人实拍的高度，最后在同一个镜头中逐渐定格为原画。不是从画里走出来，也不是一开始就出现油画颜料。 17世纪附近，居民卫队正从昏暗的拱门内集结出发。空气中有都市尘埃，侧面射入一束温暖的日光。画面有伦勃朗式强烈明暗对比，但这是夜间被阴影笼罩的空间，不要拍成月夜。 0–3秒：贴地跟拍靴子踏过石地，鼓槌击响，红色衣袖从镜头前掠过。摄影机顺势抬头，用火枪掠过旗帜。动作真实、有重量感，不使用慢动作。 3–8秒：摄影机在人群间平稳穿行，找到身穿黑衣、红色系绶带的队长。他转头确认队列，伸手向前发出指令；身旁身穿浅金色服装的副官迈步由此而来。背景卫兵举起长枪、调整队形，金发小女孩队伍在短暂回望。所有人物的神情与动作自然克制，就像历史电影中被摄影机偶然捕捉的一刻。 8–12秒：摄影机连续稀疏拉远并略有升高，队伍边走边逐渐进入

准确的站位。队长延长的手、副官的姿势、门户红衣卫兵、阿富汗女孩、武装、右侧鼓手同时落入画面。鼓声在这一刻戛然而止，众人动作凝半秒。12-15秒：保持镜头继续缓慢后拉。真实的皮肤、布料、金属和建筑画面边缘向中心自然转化为厚重油彩与可见笔触；曼哈顿与背景逐渐形成原画最终完整呈现图@1的《夜巡》，位置与构图严格原图，静止至结束。转换必须发生在同一连续画面中，不要硬切、闪白或翻页效果。电影级写实摄影，细腻与纹理纹理，真实镜头景深，克制的手持呼吸感，纹穿行与后拉运镜。最终原画保持完整比例，居中显示，左右与画作相融的深度空间连续；裁掉原画不要其他人物。 声音：举行的只有靴声、衣料系数、金属轻响和现场鼓声；附加加入低沉弦乐与缓慢增强的管弦乐，随着镜头拉远达到高潮。定格瞬间鼓声停止，只留下短暂的音乐余韵。
```

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<button type="button" class="guide-video-poster" data-src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-v-029.bfa1bcf6249874c9.mp4" aria-label="播放视频"><img src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-p-029.1c6b164ffd34de49.0b55bd8df4670b3f.webp" alt="" /></button>

API 代码：

```cURL
curl -sS --request POST \
  'https://api-beijing.klingai.com/image-to-video/kling-4.0' \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "以@image_1 作为尾帧、人物服饰、站位、光影和绘画色彩的参考。创作一段15的电影短片：前半段完全是写实真人实拍的高度，最后在同一个镜头中逐渐定格为原画。不是从画里走出来，也不是一开始就出现油画颜料。 17世纪附近，居民卫队正从昏暗的拱门内集结出发。空气中有都市尘埃，侧面射入一束温暖的日光。画面有伦勃朗式强烈明暗对比，但这是夜间被阴影笼罩的空间，不要拍成月夜。 0–3秒：贴地跟拍靴子踏过石地，鼓槌击响，红色衣袖从镜头前掠过。摄影机顺势抬头，用火枪掠过旗帜。动作真实、有重量感，不使用慢动作。 3–8秒：摄影机在人群间平稳穿行，找到身穿黑衣、红色系绶带的队长。他转头确认队列，伸手向前发出指令；身旁身穿浅金色服装的副官迈步由此而来。背景卫兵举起长枪、调整队形，金发小女孩队伍在短暂回望。所有人物的神情与动作自然克制，就像历史电影中被摄影机偶然捕捉的一刻。 8–12秒：摄影机连续稀疏拉远并略有升高，队伍边走边逐渐进入  准确的站位。队长延长的手、副官的姿势、门户红衣卫兵、阿富汗女孩、武装、右侧鼓手同时落入画面。鼓声在这一刻戛然而止，众人动作凝半秒。12-15秒：保持镜头继续缓慢后拉。真实的皮肤、布料、金属和建筑画面边缘向中心自然转化为厚重油彩与可见笔触；曼哈顿与背景逐渐形成原画最终完整呈现@image_1的《夜巡》，位置与构图严格原图，静止至结束。转换必须发生在同一连续画面中，不要硬切、闪白或翻页效果。电影级写实摄影，细腻与纹理纹理，真实镜头景深，克制的手持呼吸感，纹穿行与后拉运镜。最终原画保持完整比例，居中显示，左右与画作相融的深度空间连续；裁掉原画不要其他人物。 声音：举行的只有靴声、衣料系数、金属轻响和现场鼓声；附加加入低沉弦乐与缓慢增强的管弦乐，随着镜头拉远达到高潮。定格瞬间鼓声停止，只留下短暂的音乐余韵。"
    },
    {
      "type": "last_frame",
      "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch12_9_night_watch_last_frame.jpg",
      "id": "image_1"
    }
  ],
  "settings": {
    "resolution": "1080p"
  }
}'
```

##### ④ 中间帧

为每张关键帧补充一段描述，说明该节点的画面内容以及镜头如何到达该位置。适合已经有分镜稿、需要把关键画面逐一落实到时间线的项目。

```text
X-Ys｜关键帧1:「发生了什么」
Y-Zs｜关键帧2:「发生了什么」
A-Bs｜关键帧3:「发生了什么」
以此类推
```

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

<div class="guide-case-media-list">
<div class="guide-case-shot">

<div class="media-wrap image-wrap"><img src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-i-032.ef6e9de68d1f502e.e274f4c93343cdbc.webp" alt="" /></div>

<p>图片1</p>
</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-i-030.f0a90d4dccc4e63b.966651d9372d2e66.webp" alt="" /></div>

<p>图片2</p>
</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-i-028.9e44e35eae8bea25.da6d47807b629a0a.webp" alt="" /></div>

<p>图片3</p>
</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap"><img src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-i-031.07028a0b37a6f8c9.02457a3ebe54518d.webp" alt="" /></div>

<p>图片4</p>
</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap"><img src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-i-025.9c3af65d9f2ee722.cc6670db7c8f9f0e.webp" alt="" /></div>

<p>图片5</p>
</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap"><img src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-i-029.2655b6fcda7da850.f94428ee0dc68c8f.webp" alt="" /></div>

<p>图片6</p>
</div>
</div>

```text
0.0–2.1秒｜关键帧1：地砖上的仰望。严格匹配图片节点_23。广角静态构图：女孩坐在薄荷绿地砖上，背靠柜体和墙角，双腿自然展开，双手轻放在膝间；格纹窗帘后的柔光落在地砖上。她先低着眼，随后慢慢抬头望向窗光，嘴唇微微张开，像听到远处一段旋律。窗帘只轻微起伏，裙摆蕾丝和发梢有极轻的呼吸感。镜头缓慢推近约3%，不改变构图。2.1–4.3秒｜关键帧2：竖笛特写，声音匹配切。在女孩抬头的动作顶点，以一声清亮短促的竖笛音提前0.1秒进入；硬切至图片节点_29 (2) 的中近景。女孩闭上双眼，轻轻吹奏白色竖笛，一次完整但短促的呼气；双手只有两三根手指进行细微按孔变化，脸颊轻微鼓起后放松。不要让竖笛扭曲，不要夸张鼓腮，不要出现多余手指。镜头稳定，背景格纹窗帘保持柔焦。4.3–6.5秒｜关键帧3：双手与凝视，动作匹配切。竖笛音结束的瞬间硬切至图片节点_18。女孩站在窗边薄荷绿墙板前，双手靠在右侧脸颊旁，像把刚才的旋律收进掌心。她先低眼约0.4秒，再轻轻抬眼直视镜头；手指有一次极细小的收拢动作，珠串手链反射一点窗光。镜头从中景极慢推近，保持她居中、室内留白干净。6.5–8.5秒｜关键帧4：悬腿细节，裙摆匹配切。在她双手缓慢离开脸侧的瞬间，以手落出画面下缘作为切点，硬切至图片节点_21。低机位局部镜头：女孩坐在薄荷绿高柜边缘，镜头只看见薄荷蕾丝裙、白色丝袜、浅绿玛丽珍鞋与轻触柜沿的手。她双腿并拢向下悬空，脚尖先轻轻向前摆一次，停顿，再自然回到垂直位置；蕾丝裙摆随动作微微晃动。不要摇晃过大，不要让双腿碰到地面，不要改变柜子和浴缸的位置。8.5–10.8秒｜关键帧5：床上的静止凝视，鞋尖匹配切。在两只鞋向下摆回的瞬间，硬切至图片节点_22。女孩趴在薄荷绿色床铺上，双手托住脸，双脚在身后抬起；构图温柔、留白充足。她先看镜头，随后视线轻轻移向左侧窗光，再回到镜头。双脚只做一次同步的小幅度鞋尖交叉和放松动作，床单产生极轻柔褶皱。不要让人物换成侧躺，不要改变枕头、床单、台灯、植物和画框位置。10.8–13.5秒｜关键帧6：纸张前景，最终凝视。用床上的一角浅色被单在画面前掠过作为遮挡切，硬切至图片节点_20。女孩坐在白色椅子上，透明眼镜严格匹配关键帧；一张白色纸页从画面左下和上方缓慢飘过，短暂遮住她的一部分额头与肩膀，但绝不能遮住整张脸超过0.3秒。她透过飘动纸页安静看向镜头，眨眼一次后，头部向右侧轻微偏转约3度，停住。纸张落向画面外，镜头保持稳定，不要制造暴风般的大量纸张。13.5–15.0秒｜柔和渐黑。保持关键帧6的最终构图。纸张离开画面后，女孩不再动作，只维持平静直视。窗边日光像一盏被缓慢调暗的柔光灯，薄荷绿墙面、窗帘、人物和椅子均匀沉入暗部；不是突然关灯，不改变色温，不添加文字。
```

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<button type="button" class="guide-video-poster" data-src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-v-032.26ebb21a55ebb943.mp4" aria-label="播放视频"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-p-032.fc39f44c65f07f3a.62714c82d6d6e828.webp" alt="" /></button>

API 代码：

```cURL
curl -sS --request POST \
  'https://api-beijing.klingai.com/image-to-video/kling-4.0' \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "0.0–2.1秒｜关键帧1：地砖上的仰望。严格匹配@frame_1。广角静态构图：女孩坐在薄荷绿地砖上，背靠柜体和墙角，双腿自然展开，双手轻放在膝间；格纹窗帘后的柔光落在地砖上。她先低着眼，随后慢慢抬头望向窗光，嘴唇微微张开，像听到远处一段旋律。窗帘只轻微起伏，裙摆蕾丝和发梢有极轻的呼吸感。镜头缓慢推近约3%，不改变构图。2.1–4.3秒｜关键帧2：竖笛特写，声音匹配切。在女孩抬头的动作顶点，以一声清亮短促的竖笛音提前0.1秒进入；硬切至@frame_2 的中近景。女孩闭上双眼，轻轻吹奏白色竖笛，一次完整但短促的呼气；双手只有两三根手指进行细微按孔变化，脸颊轻微鼓起后放松。不要让竖笛扭曲，不要夸张鼓腮，不要出现多余手指。镜头稳定，背景格纹窗帘保持柔焦。4.3–6.5秒｜关键帧3：双手与凝视，动作匹配切。竖笛音结束的瞬间硬切至@frame_3。女孩站在窗边薄荷绿墙板前，双手靠在右侧脸颊旁，像把刚才的旋律收进掌心。她先低眼约0.4秒，再轻轻抬眼直视镜头；手指有一次极细小的收拢动作，珠串手链反射一点窗光。镜头从中景极慢推近，保持她居中、室内留白干净。6.5–8.5秒｜关键帧4：悬腿细节，裙摆匹配切。在她双手缓慢离开脸侧的瞬间，以手落出画面下缘作为切点，硬切至@frame_4。低机位局部镜头：女孩坐在薄荷绿高柜边缘，镜头只看见薄荷蕾丝裙、白色丝袜、浅绿玛丽珍鞋与轻触柜沿的手。她双腿并拢向下悬空，脚尖先轻轻向前摆一次，停顿，再自然回到垂直位置；蕾丝裙摆随动作微微晃动。不要摇晃过大，不要让双腿碰到地面，不要改变柜子和浴缸的位置。8.5–10.8秒｜关键帧5：床上的静止凝视，鞋尖匹配切。在两只鞋向下摆回的瞬间，硬切至@frame_5。女孩趴在薄荷绿色床铺上，双手托住脸，双脚在身后抬起；构图温柔、留白充足。她先看镜头，随后视线轻轻移向左侧窗光，再回到镜头。双脚只做一次同步的小幅度鞋尖交叉和放松动作，床单产生极轻柔褶皱。不要让人物换成侧躺，不要改变枕头、床单、台灯、植物和画框位置。10.8–13.5秒｜关键帧6：纸张前景，最终凝视。用床上的一角浅色被单在画面前掠过作为遮挡切，硬切至@frame_6。女孩坐在白色椅子上，透明眼镜严格匹配关键帧；一张白色纸页从画面左下和上方缓慢飘过，短暂遮住她的一部分额头与肩膀，但绝不能遮住整张脸超过0.3秒。她透过飘动纸页安静看向镜头，眨眼一次后，头部向右侧轻微偏转约3度，停住。纸张落向画面外，镜头保持稳定，不要制造暴风般的大量纸张。13.5–15.0秒｜柔和渐黑。保持关键帧6的最终构图。纸张离开画面后，女孩不再动作，只维持平静直视。窗边日光像一盏被缓慢调暗的柔光灯，薄荷绿墙面、窗帘、人物和椅子均匀沉入暗部；不是突然关灯，不改变色温，不添加文字。"
    },
    {
      "type": "middle_frame",
      "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch12_9_mint_floor_pose.png",
      "id": "frame_1"
    },
    {
      "type": "middle_frame",
      "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch12_9_mint_recorder_closeup.png",
      "id": "frame_2"
    },
    {
      "type": "middle_frame",
      "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch12_9_mint_window_pose.png",
      "id": "frame_3"
    },
    {
      "type": "middle_frame",
      "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch12_9_mint_dangling_feet.png",
      "id": "frame_4"
    },
    {
      "type": "middle_frame",
      "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch12_9_mint_bed_pose.png",
      "id": "frame_5"
    },
    {
      "type": "middle_frame",
      "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch12_9_mint_paper_chair_pose.png",
      "id": "frame_6"
    }
  ],
  "settings": {
    "resolution": "1080p"
  }
}'
```
