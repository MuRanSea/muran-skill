<!-- Official source: https://klingai.com/document-api/api/usage-guide/kling-image-4-0-prompt-guide.md -->
<!-- Source SHA-256: 22b29975d2fc9083ad6a0f62cad9469d46fa5e87d665c2bcdf9099fab5551c80 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://klingai.com/document-api/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling Image 4.0 提示词案例

> 来源: https://klingai.com/document-api/api/usage-guide/kling-image-4-0-prompt-guide
> 语言: zh
> 当前 Tab: Kling Image 4.0 提示词案例
> 此内容为面向 LLM 优化的 Markdown，已展开页面内 Tab，并省略页面目录、复制按钮等 UI 控件。

本文为 Kling 4.0 图片使用手册的配套提示词案例，使用手册详细介绍了 Kling 4.0图片的模型能力、API任务使用方法、素材要求和提示词写作方法，本文为您提供涵盖 Kling 4.0 图片不同功能的具体案例，每个案例均附完整提示词与可运行的 API 调用代码，您可直接复制体验，也可结合业务需求调整使用。

## 1 内容创作

### 1️⃣ 原生真实感

提示词写法：【主体】＋【正在发生的动作／状态】＋【具体场景】＋【手机拍摄方式】。可按需要补充自然光线、衣物或材质细节，并使用“前置自拍”“朋友后置拍摄”“手机直出”“生活感随拍”等拍摄描述。

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

```text
一名年轻东亚女生站在深秋公园的浅蓝灰色金属护栏旁，黑色齐刘海短发自然垂落，头戴白底红色波点针织头巾，红色系带垂落在胸前，身穿宽松奶白色针织毛衣、深灰色百褶短裙和白色过膝袜，肩上背着白色红波点布包。女生双手撑着金属栏杆，上半身探出栏杆，右腿的小腿翘起来，动作俏皮可爱。身体朝向画面右侧，头部向左上方转动，抬头望向树梢，露出明亮自然的笑容，黑色短发随着动作轻轻扬起，神态轻松、俏皮。
竖版中远景环境人像，摄影机位于人物侧前方，略微俯拍，人物位于画面中下部偏左位置，身体呈自然倾斜姿态。金属栏杆从画面左下方延伸至右侧远处，形成纵深透视。画面上方保留大量交错的深色树枝和鲜艳枫叶，背景是浓密的橙红色、金黄色枫树林，左侧隐约可见蓝色湖水，地面铺满深红褐色落叶，背景环境清晰可辨。明亮秋日阳光从人物左前方照射，脸部受到直接照明，皮肤明亮通透，头发边缘有轻微暖金色高光，毛衣呈柔和奶白色，树叶在阳光下呈现通透的橙红色。复古日系胶片快照，广角镜头，较深景深，明显胶片颗粒与轻微噪点，暖色调，红橙色枫叶与蓝绿色阴影形成冷暖撞色，整体反差偏高，画面边缘轻微失焦，带有胶片扫描质感和自然曝光偏差，像朋友在秋日旅行途中抓拍的照片，明媚、自由、轻盈，充满青春电影感。
```

<p class="guide-case-note">仅提示词，无参考图。</p>

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<div class="guide-case-media-list guide-case-media-list-full">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-001.ff6a91097516a327.webp" alt="" loading="lazy" /></div>

</div>
</div>

API 代码：

```cURL
curl --request POST \
  --url "https://api-beijing.klingai.com/image-generation/kling-4.0" \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header "Content-Type: application/json" \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "一名年轻东亚女生站在深秋公园的浅蓝灰色金属护栏旁，黑色齐刘海短发自然垂落，头戴白底红色波点针织头巾，红色系带垂落在胸前，身穿宽松奶白色针织毛衣、深灰色百褶短裙和白色过膝袜，肩上背着白色红波点布包。女生双手撑着金属栏杆，上半身探出栏杆，右腿的小腿翘起来，动作俏皮可爱。身体朝向画面右侧，头部向左上方转动，抬头望向树梢，露出明亮自然的笑容，黑色短发随着动作轻轻扬起，神态轻松、俏皮。\n竖版中远景环境人像，摄影机位于人物侧前方，略微俯拍，人物位于画面中下部偏左位置，身体呈自然倾斜姿态。金属栏杆从画面左下方延伸至右侧远处，形成纵深透视。画面上方保留大量交错的深色树枝和鲜艳枫叶，背景是浓密的橙红色、金黄色枫树林，左侧隐约可见蓝色湖水，地面铺满深红褐色落叶，背景环境清晰可辨。明亮秋日阳光从人物左前方照射，脸部受到直接照明，皮肤明亮通透，头发边缘有轻微暖金色高光，毛衣呈柔和奶白色，树叶在阳光下呈现通透的橙红色。复古日系胶片快照，广角镜头，较深景深，明显胶片颗粒与轻微噪点，暖色调，红橙色枫叶与蓝绿色阴影形成冷暖撞色，整体反差偏高，画面边缘轻微失焦，带有胶片扫描质感和自然曝光偏差，像朋友在秋日旅行途中抓拍的照片，明媚、自由、轻盈，充满青春电影感。"
    }
  ],
  "settings": {
    "result_type": "single",
    "n": 1,
    "resolution": "2k",
    "aspect_ratio": "auto"
  }
}'
```

### 2️⃣ 角色创作

#### 角色设计·单图生成

提示词写法：【年龄】＋【身份背景】＋【体型】＋【面部特征】＋【发型】＋【穿着配饰】＋【气质与表情】。根据用途补充【动作与道具】、【背景】及【全身／半身／特写构图】；幻想角色可增加【物种特征与身体结构】。

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

```text
周会珍，46岁，县城歌厅前领班。身材丰润，短卷发染成酒红色，常穿亮色针织衫、豹纹丝巾和夸张耳环。性格泼辣、爱笑、嘴碎，见谁都熟，遇事绝不吃亏。真实人物的正面半身摄影，背景是灰色斑驳墙面简约室内。
```

<p class="guide-case-note">仅提示词，无参考图。</p>

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<div class="guide-case-media-list guide-case-media-list-full">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-zh-002.e1837892b3bfc57d.webp" alt="" loading="lazy" /></div>

</div>
</div>

API 代码：

```cURL
curl --request POST \
  --url "https://api-beijing.klingai.com/image-generation/kling-4.0" \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header "Content-Type: application/json" \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "周会珍，46岁，县城歌厅前领班。身材丰润，短卷发染成酒红色，常穿亮色针织衫、豹纹丝巾和夸张耳环。性格泼辣、爱笑、嘴碎，见谁都熟，遇事绝不吃亏。真实人物的正面半身摄影，背景是灰色斑驳墙面简约室内。"
    }
  ],
  "settings": {
    "result_type": "single",
    "n": 1,
    "resolution": "2k",
    "aspect_ratio": "auto"
  }
}'
```

#### 角色多视图·单图生成

提示词写法：参考【输入图】中的角色，生成一张角色多视图设定图，包含【正面、侧面、背面等全身视角】与【面部特写视角】。按【布局要求】排列在同一张图片中，使用【背景与布光】，保持各视角的外貌、发型、服饰和身体比例一致。

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

<div class="guide-case-media-list guide-case-media-list-full">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-003.c6e6aedef01c177c.webp" alt="" loading="lazy" /></div>

<p>@ref_1 · 角色身份与外观参考</p>
</div>
</div>

```text
参考素材职责：@ref_1：角色身份与外观参考。
生成图中角色的多视图参考图，纯白背景，无阴影，布光均匀。画面排版：左侧全身三视图依次为正面全身、侧面全身、背面全身；右侧上下排列面部正面特写和面部侧面特写。保持整个画面背景为纯色简约背景，比例精准，对称构图，无多余装饰和线条，区域之间无缝衔接。
```

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<div class="guide-case-media-list guide-case-media-list-full">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-004.096642e2fa5372bc.webp" alt="" loading="lazy" /></div>

</div>
</div>

API 代码：

```cURL
curl --request POST \
  --url "https://api-beijing.klingai.com/image-generation/kling-4.0" \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header "Content-Type: application/json" \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "参考素材职责：@ref_1：角色身份与外观参考。\n生成图中角色的多视图参考图，纯白背景，无阴影，布光均匀。画面排版：左侧全身三视图依次为正面全身、侧面全身、背面全身；右侧上下排列面部正面特写和面部侧面特写。保持整个画面背景为纯色简约背景，比例精准，对称构图，无多余装饰和线条，区域之间无缝衔接。"
    },
    {
      "type": "refer_image",
      "url": "https://p1-kling.klingai.com/kcdn/cdn-kcdn112452/tutorials/kling-image-4-0/api-examples-20261110/ref_-3977339680444001418.png",
      "id": "ref_1"
    }
  ],
  "settings": {
    "result_type": "single",
    "n": 1,
    "resolution": "2k",
    "aspect_ratio": "auto"
  }
}'
```

#### 卡司合照·单图生成

提示词写法：参考【输入图】的画面艺术设计风格，在同一张图片中生成【人数】名不同角色的合照。角色1：【描述】；角色2：【描述】；角色3：【描述】……按【并排站位／分格布局】安排人物，补充【动作互动与场景】，保持整体风格统一、各角色特征有区别。

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

<div class="guide-case-media-list guide-case-media-list-full">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-zh-005.c4dec1781c646792.webp" alt="" loading="lazy" /></div>

<p>@ref_1 · 画面/角色艺术风格及三视图形式参考</p>
</div>
</div>

```text
参考素材职责：@ref_1：画面/角色艺术风格及三视图形式参考。
参考图中的画面艺术设计风格，生成一组不同角色的四宫格。
```

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<div class="guide-case-media-list guide-case-media-list-full">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-zh-006.edeceb62a507ed19.webp" alt="" loading="lazy" /></div>

</div>
</div>

API 代码：

```cURL
curl --request POST \
  --url "https://api-beijing.klingai.com/image-generation/kling-4.0" \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header "Content-Type: application/json" \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "参考素材职责：@ref_1：画面/角色艺术风格及三视图形式参考。\n参考图中的画面艺术设计风格，生成一组不同角色的四宫格。"
    },
    {
      "type": "refer_image",
      "url": "https://p1-kling.klingai.com/kcdn/cdn-kcdn112452/tutorials/kling-image-4-0/api-examples-20261110/ref_9029810809747074506.png",
      "id": "ref_1"
    }
  ],
  "settings": {
    "result_type": "single",
    "n": 1,
    "resolution": "2k",
    "aspect_ratio": "auto"
  }
}'
```

#### 三视图角色·组图生成

提示词写法：参考【输入图】的特写和三视图形式，生成与该角色成套成组的【人数】名其他角色。角色1：【描述】；角色2：【描述】；角色3：【描述】……每名角色输出一张独立设定图，包含【特写与三视图布局】，保持整组画风、背景和排版一致。

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

<div class="guide-case-media-list guide-case-media-list-full">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-025.f09cd915e8c2a98b.webp" alt="" loading="lazy" /></div>

<p>@ref_1 · 画面/角色艺术风格及三视图形式参考</p>
</div>
</div>

```text
参考素材职责：@ref_1：画面/角色艺术风格及三视图形式参考。
请参考该角色的特写和三视图形式，生成与该角色成套成组的三名其他角色。
角色1:二十多岁、身材纤细修长的成年白人女性，浅肤色，浅灰蓝色眼睛，椭圆脸，自然浅色眉毛，鼻梁挺直，嘴唇自然微微闭合。浅金色带灰调的头发，在脑后盘成松散凌乱的发髻，额前与两侧垂落几缕微卷碎发。保留轻微雀斑、毛孔和真实皮肤纹理，淡妆，表情平静、疏离、略带慵懒感。穿深酒红色无袖长连衣裙，圆领，小盖肩式宽肩线，柔软哑光面料，腰腹处有自然垂坠的斜向褶皱，裙身偏直筒，下摆至小腿下段、脚踝上方。颈部松松环绕一条浅樱粉色长围巾，围巾平整柔软、无图案，长尾从肩后垂落至背部腰际。脚穿黑色圆头平底芭蕾鞋，不添加其他醒目配饰。
角色2:二十多岁的成年白人女性，纤细修长，浅肤色，略带灰绿色的浅色眼睛，浓密自然的深棕色眉毛，挺直鼻梁，轮廓清晰的自然嘴唇。深棕色头发在脑后扎成松散的低位发髻，头顶蓬松，两侧散落不规则微卷碎发。自然淡妆，保留轻微雀斑、真实毛孔和皮肤细节，表情冷静、自信、略带疏离。穿深巧克力棕色皮革短夹克，宽松廓形，较高的立领，肩部有肩袢，前中金属拉链，腰部有收紧的弹性下摆，长袖宽松，袖口收束。皮革带柔和光泽与真实细碎褶皱，不是亮面漆皮。夹克敞开，内搭奶油白色贴身高领针织衫。下穿黑色高腰宽腿长裤，裤管宽大、垂坠，裤脚接近地面，局部覆盖黑色尖头鞋。
角色3:人物为四十多岁至五十岁左右的中年黑人男性，深棕色皮肤，中等偏修长体型，肩膀自然宽阔，深棕色眼睛。短黑色紧密卷发，顶部稍长，两侧渐短。修剪整齐的短胡须与胡髭，下巴和下颌胡须有明显银灰色，形成自然黑灰混合的胡须层次。保留额头细纹、眼周纹理、毛孔及真实肤色变化。表情沉稳、温和、坚定，嘴唇自然闭合。
穿炭黑色哑光毛呢质感休闲外套，长度至臀部附近，平翻领，前中纽扣，胸前单个贴袋，长袖，直身宽松版型。外套敞开，内搭灰白底、细黑色小方格衬衫，领口解开，衬衫下摆自然露出。颈部佩戴细棕色长绳项链，胸前有银色几何金属吊坠。下穿炭黑色直筒长裤，脚穿深棕近黑色系带皮鞋，鞋底边缘带棕色层次。服装无品牌标识。
```

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<div class="guide-case-media-list guide-case-media-list-full guide-case-media-list-stack" style="--shot-ratio: 1.777">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-zh-008.fbeecd2c7f65fb67.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-zh-009.1cb73d3d88b94307.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-zh-010.d0a2335888f6a3cb.webp" alt="" loading="lazy" /></div>

</div>
</div>

API 代码：

```cURL
curl --request POST \
  --url "https://api-beijing.klingai.com/image-generation/kling-4.0" \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header "Content-Type: application/json" \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "参考素材职责：@ref_1：画面/角色艺术风格及三视图形式参考。\n请参考该角色的特写和三视图形式，生成与该角色成套成组的三名其他角色。\n角色1:二十多岁、身材纤细修长的成年白人女性，浅肤色，浅灰蓝色眼睛，椭圆脸，自然浅色眉毛，鼻梁挺直，嘴唇自然微微闭合。浅金色带灰调的头发，在脑后盘成松散凌乱的发髻，额前与两侧垂落几缕微卷碎发。保留轻微雀斑、毛孔和真实皮肤纹理，淡妆，表情平静、疏离、略带慵懒感。穿深酒红色无袖长连衣裙，圆领，小盖肩式宽肩线，柔软哑光面料，腰腹处有自然垂坠的斜向褶皱，裙身偏直筒，下摆至小腿下段、脚踝上方。颈部松松环绕一条浅樱粉色长围巾，围巾平整柔软、无图案，长尾从肩后垂落至背部腰际。脚穿黑色圆头平底芭蕾鞋，不添加其他醒目配饰。\n角色2:二十多岁的成年白人女性，纤细修长，浅肤色，略带灰绿色的浅色眼睛，浓密自然的深棕色眉毛，挺直鼻梁，轮廓清晰的自然嘴唇。深棕色头发在脑后扎成松散的低位发髻，头顶蓬松，两侧散落不规则微卷碎发。自然淡妆，保留轻微雀斑、真实毛孔和皮肤细节，表情冷静、自信、略带疏离。穿深巧克力棕色皮革短夹克，宽松廓形，较高的立领，肩部有肩袢，前中金属拉链，腰部有收紧的弹性下摆，长袖宽松，袖口收束。皮革带柔和光泽与真实细碎褶皱，不是亮面漆皮。夹克敞开，内搭奶油白色贴身高领针织衫。下穿黑色高腰宽腿长裤，裤管宽大、垂坠，裤脚接近地面，局部覆盖黑色尖头鞋。\n角色3:人物为四十多岁至五十岁左右的中年黑人男性，深棕色皮肤，中等偏修长体型，肩膀自然宽阔，深棕色眼睛。短黑色紧密卷发，顶部稍长，两侧渐短。修剪整齐的短胡须与胡髭，下巴和下颌胡须有明显银灰色，形成自然黑灰混合的胡须层次。保留额头细纹、眼周纹理、毛孔及真实肤色变化。表情沉稳、温和、坚定，嘴唇自然闭合。\n穿炭黑色哑光毛呢质感休闲外套，长度至臀部附近，平翻领，前中纽扣，胸前单个贴袋，长袖，直身宽松版型。外套敞开，内搭灰白底、细黑色小方格衬衫，领口解开，衬衫下摆自然露出。颈部佩戴细棕色长绳项链，胸前有银色几何金属吊坠。下穿炭黑色直筒长裤，脚穿深棕近黑色系带皮鞋，鞋底边缘带棕色层次。服装无品牌标识。"
    },
    {
      "type": "refer_image",
      "url": "https://p1-kling.klingai.com/kcdn/cdn-kcdn112452/tutorials/kling-image-4-0/api-examples-20261110/ref_7269315860580644084.png",
      "id": "ref_1"
    }
  ],
  "settings": {
    "result_type": "series",
    "series_amount": 3,
    "resolution": "2k",
    "aspect_ratio": "auto"
  }
}'
```

#### 群像生成

提示词写法：【人数与群体身份】＋【人物差异】＋【站位布局】＋【动作互动】＋【场景】。需要细化时，逐人填写【位置、辨识特征、穿着、动作、表情／视线】，再补充【拍摄视角、景深、统一光影与色调】；明确所有人物呈现在同一张图片中。

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

```text
五位年轻东亚学生穿着统一的夏季校服，在铁路和公路旁的空旷道路上朝镜头奔跑。人物约高中生年龄，两男三女，青春自然，头发被风吹起，脸上带着灿烂笑容。校服以白色短袖衬衫、深蓝条纹领带、灰色针织背心、深色长裤或蓝灰格纹百褶裙为主，女生穿白色过膝袜和黑色皮鞋。
前景右侧女性一边跑一边用手扶头发，身体向前倾；中央女生双手举着黑色书包放在头顶，开心大笑；另一位女生齐刘海扎着高马尾，穿灰色背心和格纹裙；后方两个男生也面带笑容追赶。人物动作幅度大，姿态各不相同，充满放学后追逐嬉闹的感觉。
场景位于城市边缘的铁路沿线，背景密集分布电线杆、铁路接触网、限速标志、护栏和远处城市建筑。道路呈倾斜透视线向远方延伸。竖构图，全身群像，中远景，轻微低机位，镜头稍微倾斜，带抓拍感。晴天自然光，整体胶片色调，轻微过曝和颗粒感，像2000年代青春电影或校园写真。
```

<p class="guide-case-note">仅提示词，无参考图。</p>

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<div class="guide-case-media-list guide-case-media-list-full">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-zh-011.528c687513e75d44.webp" alt="" loading="lazy" /></div>

</div>
</div>

API 代码：

```cURL
curl --request POST \
  --url "https://api-beijing.klingai.com/image-generation/kling-4.0" \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header "Content-Type: application/json" \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "五位年轻东亚学生穿着统一的夏季校服，在铁路和公路旁的空旷道路上朝镜头奔跑。人物约高中生年龄，两男三女，青春自然，头发被风吹起，脸上带着灿烂笑容。校服以白色短袖衬衫、深蓝条纹领带、灰色针织背心、深色长裤或蓝灰格纹百褶裙为主，女生穿白色过膝袜和黑色皮鞋。\n前景右侧女性一边跑一边用手扶头发，身体向前倾；中央女生双手举着黑色书包放在头顶，开心大笑；另一位女生齐刘海扎着高马尾，穿灰色背心和格纹裙；后方两个男生也面带笑容追赶。人物动作幅度大，姿态各不相同，充满放学后追逐嬉闹的感觉。\n场景位于城市边缘的铁路沿线，背景密集分布电线杆、铁路接触网、限速标志、护栏和远处城市建筑。道路呈倾斜透视线向远方延伸。竖构图，全身群像，中远景，轻微低机位，镜头稍微倾斜，带抓拍感。晴天自然光，整体胶片色调，轻微过曝和颗粒感，像2000年代青春电影或校园写真。"
    }
  ],
  "settings": {
    "result_type": "single",
    "n": 1,
    "resolution": "2k",
    "aspect_ratio": "auto"
  }
}'
```

### 3️⃣ 纪实摄影

提示词写法：【人物身份】＋【外貌与穿着特征】＋【具体行为／互动】＋【生活场景】。补充【拍摄视角、现场光线与成像质感】，用正在发生的可见动作表达人物状态，避免只用“真实”“有故事感”等抽象描述。

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

```text
3:4竖幅，冬日傍晚拥挤的街头热食摊，机位在摊位桌面附近、平视略低，近距离纪实抓拍。画面下方是一排被边框裁切的金属锅、碗和盛满白色包子的圆形蒸笼；左侧前景，戴黑色帽子、穿暗红棕色厚外套的摊主侧身低头，右手持长柄勺伸向中央的大锅。右下方主体是一名戴黑针织帽、裹酒红围巾和深色外套的中老年顾客，双手捧着一只白色包子，低头看着手中的食物；他的身后还有几位戴冬帽、穿厚外套的顾客，逐渐消失在画面中部的暗影里。大股真实蒸汽从画面左下方与中央锅口升起，斜向左上及中央扩散，遮挡部分背景，但摊主和右侧顾客的脸仍可辨认。太阳是画面右上区域一颗小而明亮的圆形光斑，低角度橙金色逆光穿透蒸汽，让蒸汽边缘发亮；人物正面仍偏暗，保留深阴影，右后方街道冷蓝
```

<p class="guide-case-note">仅提示词，无参考图。</p>

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<div class="guide-case-media-list guide-case-media-list-full">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-zh-012.3f798717994a8ec5.webp" alt="" loading="lazy" /></div>

</div>
</div>

API 代码：

```cURL
curl --request POST \
  --url "https://api-beijing.klingai.com/image-generation/kling-4.0" \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header "Content-Type: application/json" \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "3:4竖幅，冬日傍晚拥挤的街头热食摊，机位在摊位桌面附近、平视略低，近距离纪实抓拍。画面下方是一排被边框裁切的金属锅、碗和盛满白色包子的圆形蒸笼；左侧前景，戴黑色帽子、穿暗红棕色厚外套的摊主侧身低头，右手持长柄勺伸向中央的大锅。右下方主体是一名戴黑针织帽、裹酒红围巾和深色外套的中老年顾客，双手捧着一只白色包子，低头看着手中的食物；他的身后还有几位戴冬帽、穿厚外套的顾客，逐渐消失在画面中部的暗影里。大股真实蒸汽从画面左下方与中央锅口升起，斜向左上及中央扩散，遮挡部分背景，但摊主和右侧顾客的脸仍可辨认。太阳是画面右上区域一颗小而明亮的圆形光斑，低角度橙金色逆光穿透蒸汽，让蒸汽边缘发亮；人物正面仍偏暗，保留深阴影，右后方街道冷蓝"
    }
  ],
  "settings": {
    "result_type": "single",
    "n": 1,
    "resolution": "2k",
    "aspect_ratio": "3:4"
  }
}'
```

### 4️⃣ 叙事感

提示词写法：【视觉风格】＋【环境】＋【主体】＋【动作／神态】＋【构图】＋【机位角度】＋【焦点】＋【光线】＋【细节质感】＋【色调】＋【情绪氛围】。描述一个明确的故事瞬间，并用人物动作、视线、空间关系和道具呈现情绪。

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

```text
电影级 35mm 胶片摄影的画面风格，带有细腻颗粒纹理和经典好莱坞悬疑片质感。画面像是捕捉到一场紧张棋局中，人物俯身审视棋盘、与对手进行心理博弈的瞬间。主体是一位浅金色卷发年轻女性，苍白肤色，面部带有雀斑，淡色嘴唇，浅蓝绿色眼眸，佩戴银色环形耳环，身穿黑色带白色圆点装饰的衣物。她身体前倾，面部极度靠近镜头，呈现俯视棋盘的对弈姿态，神情紧张警觉，仿佛正在观察棋局中的关键一步。

环境是暖色调室内空间，前景为国际象棋棋盘与棋子，棋盘格纹理隐约可见，背景有柔和的暖色光斑。画面采用荷兰角机位，整体向左倾斜 45 度，构图具有不稳定感和悬疑张力。摄影机从棋子之间向上仰拍人物面部，形成极近距离低角度仰拍的窥视视角，人物仿佛正俯身审视棋局。人物面部位于画面中上部，占据画面 50% 以上；前景国际象棋棋子占据画面底部及左右边缘约 45% 区域，被极度虚化和放大，形成天然画框；背景暖色光斑进一步虚化缩小，强化人物、道具与空间之间的透视层次。

光线为柔和温暖的侧顶光，从画面右上方斜射，在人物面部形成自然明暗过渡，鼻尖和颧骨处带有明显高光，棋子顶部有微弱反光。画面突出人物面部雀斑、皮肤纹理、浅金色卷发、银色耳环冷光、黑色波点衣物质感，以及前景棋子产生的真实折射与柔焦效果。景深极浅，焦点精确锁定在人物右眼及鼻梁区域，左眼、嘴唇和前景棋子均呈现柔和虚化。整体色彩以浓郁的琥珀色、焦糖棕和暖橙为主，棋子为黑白色，肤色偏暖白，黑色衣物与银色饰品形成冷点对比。高光处微微过曝，阴影浓郁且暖调过渡自然，整体氛围紧张、对弈、心理博弈、悬疑、复古暖调、权力角力，呈现沉浸式智力对决的窥视感。
```

<p class="guide-case-note">仅提示词，无参考图。</p>

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<div class="guide-case-media-list guide-case-media-list-full">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-013.12682e665bffe9ae.webp" alt="" loading="lazy" /></div>

</div>
</div>

API 代码：

```cURL
curl --request POST \
  --url "https://api-beijing.klingai.com/image-generation/kling-4.0" \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header "Content-Type: application/json" \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "电影级 35mm 胶片摄影的画面风格，带有细腻颗粒纹理和经典好莱坞悬疑片质感。画面像是捕捉到一场紧张棋局中，人物俯身审视棋盘、与对手进行心理博弈的瞬间。主体是一位浅金色卷发年轻女性，苍白肤色，面部带有雀斑，淡色嘴唇，浅蓝绿色眼眸，佩戴银色环形耳环，身穿黑色带白色圆点装饰的衣物。她身体前倾，面部极度靠近镜头，呈现俯视棋盘的对弈姿态，神情紧张警觉，仿佛正在观察棋局中的关键一步。\n\n环境是暖色调室内空间，前景为国际象棋棋盘与棋子，棋盘格纹理隐约可见，背景有柔和的暖色光斑。画面采用荷兰角机位，整体向左倾斜 45 度，构图具有不稳定感和悬疑张力。摄影机从棋子之间向上仰拍人物面部，形成极近距离低角度仰拍的窥视视角，人物仿佛正俯身审视棋局。人物面部位于画面中上部，占据画面 50% 以上；前景国际象棋棋子占据画面底部及左右边缘约 45% 区域，被极度虚化和放大，形成天然画框；背景暖色光斑进一步虚化缩小，强化人物、道具与空间之间的透视层次。\n\n光线为柔和温暖的侧顶光，从画面右上方斜射，在人物面部形成自然明暗过渡，鼻尖和颧骨处带有明显高光，棋子顶部有微弱反光。画面突出人物面部雀斑、皮肤纹理、浅金色卷发、银色耳环冷光、黑色波点衣物质感，以及前景棋子产生的真实折射与柔焦效果。景深极浅，焦点精确锁定在人物右眼及鼻梁区域，左眼、嘴唇和前景棋子均呈现柔和虚化。整体色彩以浓郁的琥珀色、焦糖棕和暖橙为主，棋子为黑白色，肤色偏暖白，黑色衣物与银色饰品形成冷点对比。高光处微微过曝，阴影浓郁且暖调过渡自然，整体氛围紧张、对弈、心理博弈、悬疑、复古暖调、权力角力，呈现沉浸式智力对决的窥视感。"
    }
  ],
  "settings": {
    "result_type": "single",
    "n": 1,
    "resolution": "2k",
    "aspect_ratio": "auto"
  }
}'
```

### 5️⃣ 风格化

提示词写法：【目标风格】＋【主体与保留特征】＋【造型与材质】＋【色彩与光影】＋【环境与构图】。明确需要保留的身份、结构、动作或标识，以及风格化程度；可选择【水彩／油画／黏土／毛毡／剪纸／像素等风格】，不限定具体人物或题材。

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

```text
【目标风格】
梦幻日系时尚插画，融合柔焦摄影、粉彩绘画与超现实童话意象；细腻绒感笔触叠加轻微颗粒，呈现明亮、轻盈、充满春日生命力的氛围。以清晰的人物轮廓搭配具有方向性的背景拖影，营造奔跑时世界从身旁流过的感觉。
【保留特征】
少女朝左迈步、身体微微前倾的侧面全身姿态，低头闭眼，面颊泛红，黑色长发向右扬起。保留柠檬黄渔夫帽、同色宽松毛绒连帽上衣、白色飘逸长裙、白蓝运动鞋与白色单肩包；周围环绕半透明粉白游鱼、白色雏菊与鲜绿草叶。
【造型与材质】
渔夫帽柔软圆润，荧光浅黄色上衣具有蓬松细密的绒毛、宽大袖口和浅色抽绳；白色长裙轻薄柔软，随步伐展开层叠褶皱。运动鞋呈现厚底与蓝色局部装饰，肩包简洁柔软。游鱼拥有乳白至淡粉的半透明身体、轻纱般舒展的鱼鳍与尾部，部分贴近镜头，形成柔软朦胧的前景遮挡。
【色彩与光影】
以矢车菊蓝和钴蓝铺陈背景，搭配明亮柠檬黄、嫩草绿、纯白与樱花粉，形成鲜艳而柔和的色彩关系。采用明亮漫射日光，人物肤色温润，衣物高光轻柔泛白；鱼群边缘带有朦胧透光感，整体呈现粉彩般的柔亮质感，暗部保持通透。
【环境与构图】
纵向全身构图，9:16。少女居于中央，双腿迈开，裙摆与发丝共同强化行进动势。蓝色背景、绿色草地、散落雏菊与粉白鱼群交织成流动的幻想空间，背景纹理沿左下至右上方向拉伸。近景大鱼从画面边缘切入，远景小鱼与花朵疏密交错，形成包围主体的空间层次；人物面部与主要服装细节保持可辨，画面无文字。
```

<p class="guide-case-note">仅提示词，无参考图。</p>

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<div class="guide-case-media-list guide-case-media-list-full">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-014.86b74a5bd4b0ef35.webp" alt="" loading="lazy" /></div>

</div>
</div>

API 代码：

```cURL
curl --request POST \
  --url "https://api-beijing.klingai.com/image-generation/kling-4.0" \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header "Content-Type: application/json" \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "【目标风格】\n梦幻日系时尚插画，融合柔焦摄影、粉彩绘画与超现实童话意象；细腻绒感笔触叠加轻微颗粒，呈现明亮、轻盈、充满春日生命力的氛围。以清晰的人物轮廓搭配具有方向性的背景拖影，营造奔跑时世界从身旁流过的感觉。\n【保留特征】\n少女朝左迈步、身体微微前倾的侧面全身姿态，低头闭眼，面颊泛红，黑色长发向右扬起。保留柠檬黄渔夫帽、同色宽松毛绒连帽上衣、白色飘逸长裙、白蓝运动鞋与白色单肩包；周围环绕半透明粉白游鱼、白色雏菊与鲜绿草叶。\n【造型与材质】\n渔夫帽柔软圆润，荧光浅黄色上衣具有蓬松细密的绒毛、宽大袖口和浅色抽绳；白色长裙轻薄柔软，随步伐展开层叠褶皱。运动鞋呈现厚底与蓝色局部装饰，肩包简洁柔软。游鱼拥有乳白至淡粉的半透明身体、轻纱般舒展的鱼鳍与尾部，部分贴近镜头，形成柔软朦胧的前景遮挡。\n【色彩与光影】\n以矢车菊蓝和钴蓝铺陈背景，搭配明亮柠檬黄、嫩草绿、纯白与樱花粉，形成鲜艳而柔和的色彩关系。采用明亮漫射日光，人物肤色温润，衣物高光轻柔泛白；鱼群边缘带有朦胧透光感，整体呈现粉彩般的柔亮质感，暗部保持通透。\n【环境与构图】\n纵向全身构图，9:16。少女居于中央，双腿迈开，裙摆与发丝共同强化行进动势。蓝色背景、绿色草地、散落雏菊与粉白鱼群交织成流动的幻想空间，背景纹理沿左下至右上方向拉伸。近景大鱼从画面边缘切入，远景小鱼与花朵疏密交错，形成包围主体的空间层次；人物面部与主要服装细节保持可辨，画面无文字。"
    }
  ],
  "settings": {
    "result_type": "single",
    "n": 1,
    "resolution": "2k",
    "aspect_ratio": "9:16"
  }
}'
```

### 6️⃣ 分镜组图

#### 动画分镜·组图生成

提示词写法：生成【张数】张【动画风格】的独立分镜图，画面比例为【比例】。主角为【角色描述／角色参考图】，整体场景与氛围为【描述】。第1张：【动作、表情、环境与景别】；第2张：【描述】；第3张：【描述】……保持角色外貌、服装、道具和画风一致，每张呈现一个明确瞬间，不合并成拼图。

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

<div class="guide-case-media-list guide-case-media-list-full">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-015.464fee1d449c25c6.webp" alt="" loading="lazy" /></div>

<p>@ref_1 · 机器人主角</p>
</div>
</div>

```text
参考素材职责：@ref_1：机器人主角。
动画电影分镜第1张：冰雪淹没了曾经繁华的都市火车站，人类早已消失，机器人手中拿着一个生命光球，看着眼前荒废覆雪的列车。第2张：机器人艰难的顶着风雪前行，他抱着光球，穿过被雪掩埋的街道。第3张：暴风雪骤然加剧。它焦急的迎着风雪半跪蹲下，努力将光球护在胸口。第4张远景：风雪中，它艰难的向一座荒废的温室走去。第5张特写，机器人手中光球的特写，进入温室后，风雪暂时被隔绝，机器人看向手中的光球，担心它是否安全。第6张中景：机器人在温室中，风雪被暂时隔绝在温室外，第一株嫩芽破土而出，光球照亮了嫩芽，完成护送。第7张：小机器人打开门走出门外，不可置信的看着生机蔓延开来，鲜花和植被逐渐驱散了寒冬，一半世界依然是冰雪，另一半则有了绿意。第8张：冰雪完全退去，原来的高架、楼群与街道仍在，却已被植物和鲜花覆盖。小机器人仰望着周围的生命奇迹。第9张：小机器人坐在绿意盎然的废墟上，手上握着一枝花，花上有一只蝴蝶。
```

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<div class="guide-case-media-list guide-case-media-list-thirds" style="--shot-ratio: 1.778">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-016.38b26442906074f0.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-017.925596d3fa895635.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-018.4669097ea3f778fd.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-019.7cab8394257ebc65.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-020.cd6bb70f353565ad.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-021.2a675dd95cf60e41.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-022.f5f9c6f16c2785d0.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-023.0036e12751236d43.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-024.c216486d6294fdb4.webp" alt="" loading="lazy" /></div>

</div>
</div>

API 代码：

```cURL
curl --request POST \
  --url "https://api-beijing.klingai.com/image-generation/kling-4.0" \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header "Content-Type: application/json" \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "参考素材职责：@ref_1：机器人主角。\n动画电影分镜第1张：冰雪淹没了曾经繁华的都市火车站，人类早已消失，机器人手中拿着一个生命光球，看着眼前荒废覆雪的列车。第2张：机器人艰难的顶着风雪前行，他抱着光球，穿过被雪掩埋的街道。第3张：暴风雪骤然加剧。它焦急的迎着风雪半跪蹲下，努力将光球护在胸口。第4张远景：风雪中，它艰难的向一座荒废的温室走去。第5张特写，机器人手中光球的特写，进入温室后，风雪暂时被隔绝，机器人看向手中的光球，担心它是否安全。第6张中景：机器人在温室中，风雪被暂时隔绝在温室外，第一株嫩芽破土而出，光球照亮了嫩芽，完成护送。第7张：小机器人打开门走出门外，不可置信的看着生机蔓延开来，鲜花和植被逐渐驱散了寒冬，一半世界依然是冰雪，另一半则有了绿意。第8张：冰雪完全退去，原来的高架、楼群与街道仍在，却已被植物和鲜花覆盖。小机器人仰望着周围的生命奇迹。第9张：小机器人坐在绿意盎然的废墟上，手上握着一枝花，花上有一只蝴蝶。"
    },
    {
      "type": "refer_image",
      "url": "https://p1-kling.klingai.com/kcdn/cdn-kcdn112452/tutorials/kling-image-4-0/api-examples-20261110/ref_2602961555005807078.png",
      "id": "ref_1"
    }
  ],
  "settings": {
    "result_type": "series",
    "series_amount": 9,
    "resolution": "2k",
    "aspect_ratio": "16:9"
  }
}'
```

#### 影视分镜·组图生成

提示词写法：生成【张数】张【影视类型与视觉风格】的独立电影分镜，画面比例为【比例】。人物为【角色描述／角色参考图】，场景为【场景描述／场景参考图】。按顺序列出每张的【动作、神态、景别、机位与光影】，保持人物、服装、道具和场景连续，不合并成拼图。

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

<div class="guide-case-media-list guide-case-media-list-full">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-025.f09cd915e8c2a98b.webp" alt="" loading="lazy" /></div>

<p>@ref_1 · 女主</p>
</div>
</div>

```text
参考素材职责：@ref_1：女主。
法式浪漫歌舞片电影分镜图。全部镜头发生在巴黎街道的一段连续舞蹈中：奶油色石砌建筑、酒红色咖啡馆遮阳篷、深绿色路灯、浅灰石板人行道，背景只有少量不遮挡女主角的远处行人；景别变化通过合理切镜完成。
展示了女主在街头进行优雅而有活力的舞蹈，一套完整而轻盈优雅的小步舞。
```

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<div class="guide-case-media-list guide-case-media-list-thirds" style="--shot-ratio: 1.778">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-026.ee75508ec5798aa2.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-027.70aed3b92dcc689c.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-028.5eede3ec413d7e86.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-029.675b657be44d2053.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-030.25482ead13c54ddd.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-031.dac431516f91f0b0.webp" alt="" loading="lazy" /></div>

</div>
</div>

API 代码：

```cURL
curl --request POST \
  --url "https://api-beijing.klingai.com/image-generation/kling-4.0" \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header "Content-Type: application/json" \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "参考素材职责：@ref_1：女主。\n法式浪漫歌舞片电影分镜图。全部镜头发生在巴黎街道的一段连续舞蹈中：奶油色石砌建筑、酒红色咖啡馆遮阳篷、深绿色路灯、浅灰石板人行道，背景只有少量不遮挡女主角的远处行人；景别变化通过合理切镜完成。\n展示了女主在街头进行优雅而有活力的舞蹈，一套完整而轻盈优雅的小步舞。"
    },
    {
      "type": "refer_image",
      "url": "https://p1-kling.klingai.com/kcdn/cdn-kcdn112452/tutorials/kling-image-4-0/api-examples-20261110/ref_7269315860580644084.png",
      "id": "ref_1"
    }
  ],
  "settings": {
    "result_type": "series",
    "series_amount": 6,
    "resolution": "2k",
    "aspect_ratio": "16:9"
  }
}'
```

### 7️⃣ 场景组图

提示词写法：参考【输入图】的画面艺术设计风格，生成一组【张数】张不同的场景图，围绕【目标场景1、目标场景2、目标场景3……】。逐张说明【地貌／建筑、昼夜、天气与构图】，保持整组画风、色调和空间语言一致，每张输出一处完整场景。

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

<div class="guide-case-media-list guide-case-media-list-full">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-032.ca11974b42920558.webp" alt="" loading="lazy" /></div>

<p>@ref_1 · 场景艺术设计风格参考</p>
</div>
</div>

```text
参考素材职责：@ref_1：场景艺术设计风格参考。
参考图中的画面艺术设计风格，生成一组不同的场景图，围绕山、海洋、平原、森林、沙漠、洞穴
```

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<div class="guide-case-media-list guide-case-media-list-thirds" style="--shot-ratio: 1.778">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-033.410b479a5f58ae2b.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-034.234ef0602079ffed.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-035.5f49002cac22447f.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-036.9afdaebdb2cb0227.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-037.9db3044c3e79e637.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-038.bc8041ac07acdfa2.webp" alt="" loading="lazy" /></div>

</div>
</div>

API 代码：

```cURL
curl --request POST \
  --url "https://api-beijing.klingai.com/image-generation/kling-4.0" \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header "Content-Type: application/json" \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "参考素材职责：@ref_1：场景艺术设计风格参考。\n参考图中的画面艺术设计风格，生成一组不同的场景图，围绕山、海洋、平原、森林、沙漠、洞穴"
    },
    {
      "type": "refer_image",
      "url": "https://p1-kling.klingai.com/kcdn/cdn-kcdn112452/tutorials/kling-image-4-0/api-examples-20261110/ref_-2392878985869669832.png",
      "id": "ref_1"
    }
  ],
  "settings": {
    "result_type": "series",
    "series_amount": 6,
    "resolution": "2k",
    "aspect_ratio": "auto"
  }
}'
```

## 2 社媒运营

### 1️⃣ 海报／封面生成

#### 文字排版与海报生成

提示词写法：生成一张【画面比例】的【海报／封面用途】，使用【主要配色】。主体为【人物／商品／景物】，背景为【描述】，在【位置】为文字留白。主标题写“【标题】”，使用【字体／字形、颜色与排列方式】；副标题写“【副标题】”，放在【位置】；补充“【信息】”。明确【文案语言】及各级文字的大小、对齐与阅读顺序。

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

```text
画面以大面积的排版文字为视觉中心，背景为户外的沙漠风景，整体配色以棕黄色为主，呈现出构图较好的中心构图。画面正中偏下占据主要位置的是白色超大号粗体手写体中文标题"百日出行"与"夏计划"分两行居中排列，字间距和行间距紧凑，笔画边缘呈毛糙的蜡笔或粉笔质感，部分笔画有连笔和变形。主标题左侧是黄色小号粗体黑体数字日期"07.01"与"08.31"，中间有黄色横线分隔。右上角为黄色小号黑体正文"37°C"与"summer"分两行右对齐排列，下方带有一个黄色的太阳图标。画面左下角为黄色小号粗体黑体宣传标语"我们自由"与"呼吸着37°C的夏天"分两行左对齐排列。背景的沙漠在白天自然光与太阳光的45度斜侧光照射下，连绵起伏的沙丘表面带有风吹过的波浪状纹理，向阳面的亮黄色与背阴面的深棕色形成高对比度的暖色调硬光光影。画面偏左上方有一名身穿橙色上衣与深色短裤、头戴帽子的人物，双臂向两侧张开，身体向后倾斜呈站立姿态。画面右上方带有一个黄色的笑脸涂鸦图案，由一条白线连接至画面左侧。这是一张非写实、极简主义风格的数字排版拼贴艺术平面设计品牌海报。
```

<p class="guide-case-note">仅提示词，无参考图。</p>

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<div class="guide-case-media-list guide-case-media-list-full">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-048.3f5ee024d9fa2664.webp" alt="" loading="lazy" /></div>

</div>
</div>

API 代码：

```cURL
curl --request POST \
  --url "https://api-beijing.klingai.com/image-generation/kling-4.0" \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header "Content-Type: application/json" \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "画面以大面积的排版文字为视觉中心，背景为户外的沙漠风景，整体配色以棕黄色为主，呈现出构图较好的中心构图。画面正中偏下占据主要位置的是白色超大号粗体手写体中文标题\"百日出行\"与\"夏计划\"分两行居中排列，字间距和行间距紧凑，笔画边缘呈毛糙的蜡笔或粉笔质感，部分笔画有连笔和变形。主标题左侧是黄色小号粗体黑体数字日期\"07.01\"与\"08.31\"，中间有黄色横线分隔。右上角为黄色小号黑体正文\"37°C\"与\"summer\"分两行右对齐排列，下方带有一个黄色的太阳图标。画面左下角为黄色小号粗体黑体宣传标语\"我们自由\"与\"呼吸着37°C的夏天\"分两行左对齐排列。背景的沙漠在白天自然光与太阳光的45度斜侧光照射下，连绵起伏的沙丘表面带有风吹过的波浪状纹理，向阳面的亮黄色与背阴面的深棕色形成高对比度的暖色调硬光光影。画面偏左上方有一名身穿橙色上衣与深色短裤、头戴帽子的人物，双臂向两侧张开，身体向后倾斜呈站立姿态。画面右上方带有一个黄色的笑脸涂鸦图案，由一条白线连接至画面左侧。这是一张非写实、极简主义风格的数字排版拼贴艺术平面设计品牌海报。"
    }
  ],
  "settings": {
    "result_type": "single",
    "n": 1,
    "resolution": "2k",
    "aspect_ratio": "auto"
  }
}'
```

### 2️⃣ 品牌主视觉生成

提示词写法：【宣传主题／视觉风格】＋【主视觉创意】＋【主体描述】＋【场景与构图】＋【材质细节】＋【光影／色彩】＋【宣传文案】＋【字体与排版】＋【画面质感】。逐字给出【品牌名、标题与标语】，说明产品与文字的布局关系；使用商品参考图时，明确需要保持的外观与标识。

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

```text
一台深灰色金属边框的电子平板设备斜立放置在画面中心偏左位置，其屏幕内流动着银灰色与淡蓝色的抽象流体纹理，具有丝绸般的褶皱感与金属光泽，中心点缀着一颗带有明显高光反射的晶莹椭圆形水泡。在侧逆光与人工霓虹灯的共同照射下，平板左侧边缘散发出强烈的蓝色冷光带，与背景深邃黑色空间中垂直上升的蓝色光束共同构建出高对比度的未来科技风视觉效果。主体后方衬托着巨大的半透明灰色字母 "Ultra"，背景中隐约分布着呈矩阵排列的微小灰色编码文字水印。平整的深蓝色镜面地板质感细腻光滑，清晰地倒映出平板底部的轮廓以及周边的蓝色光晕。画面采用中心构图与对角线构图，构图较好，整体影调偏暗，软光与体积照明的应用增强了视觉中心感。画面上方中央水平排列着白色粗黑体标题 "KLING AI Ultra"，其中 "KLING AI" 部分比 "Ultra" 略粗，其下方紧随浅金色的副标题 "搭载新一代可灵视觉生成引擎"；右上角蓝色圆角正方形容器中心印有白色字母 "K"；画面底部中央则分布着两行白色超小号黑体文字 "KLING AI 全新创作体验发布" 与 "CREATE BEYOND LIMITS"，所有文字块沿画面中心轴线垂直分布，呈现出极简主义的商业广告风。
```

<p class="guide-case-note">仅提示词，无参考图。</p>

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<div class="guide-case-media-list guide-case-media-list-full">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-002.9a59ba7bd75ea13e.webp" alt="" loading="lazy" /></div>

</div>
</div>

API 代码：

```cURL
curl --request POST \
  --url "https://api-beijing.klingai.com/image-generation/kling-4.0" \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header "Content-Type: application/json" \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "一台深灰色金属边框的电子平板设备斜立放置在画面中心偏左位置，其屏幕内流动着银灰色与淡蓝色的抽象流体纹理，具有丝绸般的褶皱感与金属光泽，中心点缀着一颗带有明显高光反射的晶莹椭圆形水泡。在侧逆光与人工霓虹灯的共同照射下，平板左侧边缘散发出强烈的蓝色冷光带，与背景深邃黑色空间中垂直上升的蓝色光束共同构建出高对比度的未来科技风视觉效果。主体后方衬托着巨大的半透明灰色字母 \"Ultra\"，背景中隐约分布着呈矩阵排列的微小灰色编码文字水印。平整的深蓝色镜面地板质感细腻光滑，清晰地倒映出平板底部的轮廓以及周边的蓝色光晕。画面采用中心构图与对角线构图，构图较好，整体影调偏暗，软光与体积照明的应用增强了视觉中心感。画面上方中央水平排列着白色粗黑体标题 \"KLING AI Ultra\"，其中 \"KLING AI\" 部分比 \"Ultra\" 略粗，其下方紧随浅金色的副标题 \"搭载新一代可灵视觉生成引擎\"；右上角蓝色圆角正方形容器中心印有白色字母 \"K\"；画面底部中央则分布着两行白色超小号黑体文字 \"KLING AI 全新创作体验发布\" 与 \"CREATE BEYOND LIMITS\"，所有文字块沿画面中心轴线垂直分布，呈现出极简主义的商业广告风。"
    }
  ],
  "settings": {
    "result_type": "single",
    "n": 1,
    "resolution": "2k",
    "aspect_ratio": "auto"
  }
}'
```

## 3 电商营销

### 1️⃣ 商品展示图

#### 商品展示·单图生成

提示词写法：【图片类型／视觉风格】＋【商品主体／商品参考图】＋【摆放与互动关系】＋【场景与道具】＋【构图】＋【材质细节】＋【光影】＋【色彩】＋【画面质感与氛围】。明确需要保留的商品形状、颜色、结构和标识，说明道具如何衬托商品，不遮挡关键部位。

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

<div class="guide-case-media-list guide-case-media-list-full">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-041.5bd590bdff428a30.webp" alt="" loading="lazy" /></div>

<p>@ref_1 · 香水商品参考</p>
</div>
</div>

```text
参考素材职责：@ref_1：香水商品参考。
画面正中央的米白色陶瓷高脚托盘上放置着一组静物组合，托盘表面光滑，边缘带有向下的卷边设计，底部点缀着金色细边装饰。托盘中央斜放着一瓶细长长方形的磨砂玻璃香水，瓶身色彩从上至下由浅粉色渐变为透明，顶部配有棕色圆柱形木质瓶盖。香水瓶正面的白色方形标签逆时针倾斜约15度，上面印有黑色的无衬线字体，细致大号字符的 "Kling"字体为冷雅衬线体 位于上方，下方是较细小的 "IMAGE" 和 "Pro"。香水瓶右侧依偎着两块表面粗糙且带有纹理的不规则棕色石头。石头上方斜插着一根细长的干枯植物茎秆，顶端开着一朵黄色球形花序，整体长度较长。在香水瓶与植物茎秆之间，夹着一个布满细碎亮片的半透明粉红色塑料花朵，有清晰的花瓣和花蕊。香水瓶和石头交界处绽放着一朵星形展开的白色小花。背景为纯色渐变，从底部的深红色向上逐渐过渡为浅米黄色。整个近景画面在摄影棚人工暖光的正面漫射照明下，展现出低对比度的高调光影调，大面积留白的中心构图突出了静物的质感与造型，构图较好。
```

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<div class="guide-case-media-list guide-case-media-list-full">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-042.61478737c4fc1e33.webp" alt="" loading="lazy" /></div>

</div>
</div>

API 代码：

```cURL
curl --request POST \
  --url "https://api-beijing.klingai.com/image-generation/kling-4.0" \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header "Content-Type: application/json" \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "参考素材职责：@ref_1：香水商品参考。\n画面正中央的米白色陶瓷高脚托盘上放置着一组静物组合，托盘表面光滑，边缘带有向下的卷边设计，底部点缀着金色细边装饰。托盘中央斜放着一瓶细长长方形的磨砂玻璃香水，瓶身色彩从上至下由浅粉色渐变为透明，顶部配有棕色圆柱形木质瓶盖。香水瓶正面的白色方形标签逆时针倾斜约15度，上面印有黑色的无衬线字体，细致大号字符的 \"Kling\"字体为冷雅衬线体 位于上方，下方是较细小的 \"IMAGE\" 和 \"Pro\"。香水瓶右侧依偎着两块表面粗糙且带有纹理的不规则棕色石头。石头上方斜插着一根细长的干枯植物茎秆，顶端开着一朵黄色球形花序，整体长度较长。在香水瓶与植物茎秆之间，夹着一个布满细碎亮片的半透明粉红色塑料花朵，有清晰的花瓣和花蕊。香水瓶和石头交界处绽放着一朵星形展开的白色小花。背景为纯色渐变，从底部的深红色向上逐渐过渡为浅米黄色。整个近景画面在摄影棚人工暖光的正面漫射照明下，展现出低对比度的高调光影调，大面积留白的中心构图突出了静物的质感与造型，构图较好。"
    },
    {
      "type": "refer_image",
      "url": "https://p1-kling.klingai.com/kcdn/cdn-kcdn112452/tutorials/kling-image-4-0/api-examples-20261110/ref_-5830599535845822989.png",
      "id": "ref_1"
    }
  ],
  "settings": {
    "result_type": "single",
    "n": 1,
    "resolution": "2k",
    "aspect_ratio": "auto"
  }
}'
```

#### 商品展示·组图生成

提示词写法：参考【商品图】生成一组【张数／由模型规划数量】张商品展示图，整体风格为【描述】。第1张：【场景或角度】；第2张：【场景或角度】；第3张：【场景或角度】……可包含主图、结构、细节、使用场景和配件展示。保持商品形状、颜色、结构、Logo与包装标识一致；如使用模特参考图，另行说明人物职责。

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

<div class="guide-case-media-list" style="--shot-ratio: 0.684">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-045.163c783a7d490ed7.webp" alt="" loading="lazy" /></div>

<p>@ref_1 · 男人模特</p>
</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-046.c563bc52dab8fd33.webp" alt="" loading="lazy" /></div>

<p>@ref_2 · 冲浪板商品</p>
</div>
</div>

```text
以@ref_2这块复古蓝白红条纹冲浪板为主体，@ref_1这个男人为模特，规划一组完整电商产品组图：包含纯色背景正面主图、侧面与底部结构展示、板面纹理与尾鳍细节特写、尺寸与材质信息图、冲浪者海上实拍、沙滩与车载户外场景图及配件收纳展示，整体采用清爽海岸蓝与暖沙色调，突出复古设计、轻盈耐用、稳定操控和专业运动质感。不要拼图，每一张都是单图。
```

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<div class="guide-case-media-list guide-case-media-list-full">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-047.1a5bb82689f51688.webp" alt="" loading="lazy" /></div>

</div>
</div>

此处展示部分效果；组图张数以 series_amount 配置和任务返回结果为准。

API 代码：

```cURL
curl --request POST \
  --url "https://api-beijing.klingai.com/image-generation/kling-4.0" \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header "Content-Type: application/json" \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "以@ref_2这块复古蓝白红条纹冲浪板为主体，@ref_1这个男人为模特，规划一组完整电商产品组图：包含纯色背景正面主图、侧面与底部结构展示、板面纹理与尾鳍细节特写、尺寸与材质信息图、冲浪者海上实拍、沙滩与车载户外场景图及配件收纳展示，整体采用清爽海岸蓝与暖沙色调，突出复古设计、轻盈耐用、稳定操控和专业运动质感。不要拼图，每一张都是单图。"
    },
    {
      "type": "refer_image",
      "url": "https://p1-kling.klingai.com/kcdn/cdn-kcdn112452/tutorials/kling-image-4-0/api-examples-20261110/surfer.png",
      "id": "ref_1"
    },
    {
      "type": "refer_image",
      "url": "https://p1-kling.klingai.com/kcdn/cdn-kcdn112452/tutorials/kling-image-4-0/api-examples-20261110/surfboard.png",
      "id": "ref_2"
    }
  ],
  "settings": {
    "result_type": "series",
    "series_amount": "auto",
    "resolution": "2k",
    "aspect_ratio": "auto"
  }
}'
```

### 2️⃣ 模特衣服试穿

#### 虚拟试穿·多图参考

提示词写法：使用【人物参考图】中的人物，穿着【服装参考图】中的服装，搭配【配饰参考图】中的配饰，处于【场景描述／场景参考图】。保留【人物身份特征】及服装的颜色、版型、材质、图案和关键细节，补充【穿搭关系】、【姿势／神态】和【全身／半身构图】，逐一说明各参考图的用途。

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

<div class="guide-case-media-list" style="--shot-ratio: 0.777">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-015.747ec8a71858114a.webp" alt="" loading="lazy" /></div>

<p>@ref_1 · 人物身份</p>
</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-016.f22ec0121d97658d.webp" alt="" loading="lazy" /></div>

<p>@ref_2 · 服装平铺</p>
</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-017.122fc687077b5438.webp" alt="" loading="lazy" /></div>

<p>@ref_3 · 包袋与饰品</p>
</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-018.04657851ece7005b.webp" alt="" loading="lazy" /></div>

<p>@ref_4 · 街道背景</p>
</div>
</div>

```text
参考素材职责：@ref_1：人物身份；@ref_2：服装平铺；@ref_3：包袋与饰品；@ref_4：街道背景。
人物穿着图中的所有服饰，走在街道上
```

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<div class="guide-case-media-list guide-case-media-list-full">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-019.701fa3f9ea6ac727.webp" alt="" loading="lazy" /></div>

</div>
</div>

API 代码：

```cURL
curl --request POST \
  --url "https://api-beijing.klingai.com/image-generation/kling-4.0" \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header "Content-Type: application/json" \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "参考素材职责：@ref_1：人物身份；@ref_2：服装平铺；@ref_3：包袋与饰品；@ref_4：街道背景。\n人物穿着图中的所有服饰，走在街道上"
    },
    {
      "type": "refer_image",
      "url": "https://p1-kling.klingai.com/kcdn/cdn-kcdn112452/tutorials/kling-image-4-0/api-examples-20261110/outfit_ref_1.png",
      "id": "ref_1"
    },
    {
      "type": "refer_image",
      "url": "https://p1-kling.klingai.com/kcdn/cdn-kcdn112452/tutorials/kling-image-4-0/api-examples-20261110/outfit_ref_2.png",
      "id": "ref_2"
    },
    {
      "type": "refer_image",
      "url": "https://p1-kling.klingai.com/kcdn/cdn-kcdn112452/tutorials/kling-image-4-0/api-examples-20261110/outfit_ref_3.png",
      "id": "ref_3"
    },
    {
      "type": "refer_image",
      "url": "https://p1-kling.klingai.com/kcdn/cdn-kcdn112452/tutorials/kling-image-4-0/api-examples-20261110/outfit_ref_4.png",
      "id": "ref_4"
    }
  ],
  "settings": {
    "result_type": "single",
    "n": 1,
    "resolution": "2k",
    "aspect_ratio": "auto"
  }
}'
```

### 3️⃣ 营销传播

#### 电商详情页长图

提示词写法：参考【商品图】，生成一张【页面语言】的【商品品类】电商详情长图。商品为【外观与已核实信息】，主要卖点为【卖点1、卖点2……】；按【主视觉、功能卖点、材质／工艺、规格参数、使用场景等模块】组织页面。补充【逐模块文案、视觉风格与排版要求】，保持商品外观与标识一致。

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

<div class="guide-case-media-list guide-case-media-list-full">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-056.25d46ec347886d10.webp" alt="" loading="lazy" /></div>

<p>@ref_1 · 红色带盖铸铁锅商品</p>
</div>
</div>

```text
参考素材职责：@ref_1：红色带盖铸铁锅商品。
给我生成一个铸铁锅的电商详情页
```

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<div class="guide-case-media-list guide-case-media-list-full">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image is-long"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-057.a75f4a5368dc814b.webp" alt="" loading="lazy" /></div>

</div>
</div>

API 代码：

```cURL
curl --request POST \
  --url "https://api-beijing.klingai.com/long-image-generation/kling-4.0" \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header "Content-Type: application/json" \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "参考素材职责：@ref_1：红色带盖铸铁锅商品。\n给我生成一个铸铁锅的电商详情页"
    },
    {
      "type": "refer_image",
      "url": "https://p1-kling.klingai.com/kcdn/cdn-kcdn112452/tutorials/kling-image-4-0/api-examples-20261110/cast_iron_pot.png",
      "id": "ref_1"
    }
  ],
  "settings": {
    "skill": "ecommerce",
    "length": "medium",
    "resolution": "2k"
  }
}'
```

#### 产品网站图

提示词写法：为【品牌／产品／主体】生成一张【页面语言】的【品牌官网／网店／产品介绍页等网站类型】设计长图，视觉风格为【描述】。按【导航、首屏、内容区、行动按钮、页脚等结构】组织页面，给出【标题、正文与按钮文案】，补充【配色、字体、图片布局和留白要求】。

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

```text
生成一个陶瓷制造商品牌网店网页
```

<p class="guide-case-note">仅提示词，无参考图。</p>

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<div class="guide-case-media-list guide-case-media-list-full">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image is-long"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-058.8ec75970d04a724b.webp" alt="" loading="lazy" /></div>

</div>
</div>

API 代码：

```cURL
curl --request POST \
  --url "https://api-beijing.klingai.com/long-image-generation/kling-4.0" \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header "Content-Type: application/json" \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "生成一个陶瓷制造商品牌网店网页"
    }
  ],
  "settings": {
    "skill": "webpage",
    "resolution": "2k"
  }
}'
```

## 4 大众玩法

### 1️⃣ 人物写真

提示词写法：【人物】＋【穿着配饰】＋【情绪化表情与动作】＋【场景】。补充【光影、色调、构图与成像质感】；使用人物参考图时说明需要保留的身份特征。双人写真进一步写清【前后位置、身体距离、接触方式与视线关系】。

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

```text
一名年轻东亚女生站在深秋公园的浅蓝灰色金属护栏旁，黑色齐刘海短发自然垂落，头戴白底红色波点针织头巾，红色系带垂落在胸前，身穿宽松奶白色针织毛衣、深灰色百褶短裙和白色过膝袜，肩上背着白色红波点布包。女生双手撑着金属栏杆，上半身探出栏杆，右腿的小腿翘起来，动作俏皮可爱。身体朝向画面右侧，头部向左上方转动，抬头望向树梢，露出明亮自然的笑容，黑色短发随着动作轻轻扬起，神态轻松、俏皮。
竖版中远景环境人像，摄影机位于人物侧前方，略微俯拍，人物位于画面中下部偏左位置，身体呈自然倾斜姿态。金属栏杆从画面左下方延伸至右侧远处，形成纵深透视。画面上方保留大量交错的深色树枝和鲜艳枫叶，背景是浓密的橙红色、金黄色枫树林，左侧隐约可见蓝色湖水，地面铺满深红褐色落叶，背景环境清晰可辨。明亮秋日阳光从人物左前方照射，脸部受到直接照明，皮肤明亮通透，头发边缘有轻微暖金色高光，毛衣呈柔和奶白色，树叶在阳光下呈现通透的橙红色。复古日系胶片快照，广角镜头，较深景深，明显胶片颗粒与轻微噪点，暖色调，红橙色枫叶与蓝绿色阴影形成冷暖撞色，整体反差偏高，画面边缘轻微失焦，带有胶片扫描质感和自然曝光偏差，像朋友在秋日旅行途中抓拍的照片，明媚、自由、轻盈，充满青春电影感。
```

<p class="guide-case-note">仅提示词，无参考图。</p>

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<div class="guide-case-media-list guide-case-media-list-full">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-001.ff6a91097516a327.webp" alt="" loading="lazy" /></div>

</div>
</div>

API 代码：

```cURL
curl --request POST \
  --url "https://api-beijing.klingai.com/image-generation/kling-4.0" \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header "Content-Type: application/json" \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "一名年轻东亚女生站在深秋公园的浅蓝灰色金属护栏旁，黑色齐刘海短发自然垂落，头戴白底红色波点针织头巾，红色系带垂落在胸前，身穿宽松奶白色针织毛衣、深灰色百褶短裙和白色过膝袜，肩上背着白色红波点布包。女生双手撑着金属栏杆，上半身探出栏杆，右腿的小腿翘起来，动作俏皮可爱。身体朝向画面右侧，头部向左上方转动，抬头望向树梢，露出明亮自然的笑容，黑色短发随着动作轻轻扬起，神态轻松、俏皮。\n竖版中远景环境人像，摄影机位于人物侧前方，略微俯拍，人物位于画面中下部偏左位置，身体呈自然倾斜姿态。金属栏杆从画面左下方延伸至右侧远处，形成纵深透视。画面上方保留大量交错的深色树枝和鲜艳枫叶，背景是浓密的橙红色、金黄色枫树林，左侧隐约可见蓝色湖水，地面铺满深红褐色落叶，背景环境清晰可辨。明亮秋日阳光从人物左前方照射，脸部受到直接照明，皮肤明亮通透，头发边缘有轻微暖金色高光，毛衣呈柔和奶白色，树叶在阳光下呈现通透的橙红色。复古日系胶片快照，广角镜头，较深景深，明显胶片颗粒与轻微噪点，暖色调，红橙色枫叶与蓝绿色阴影形成冷暖撞色，整体反差偏高，画面边缘轻微失焦，带有胶片扫描质感和自然曝光偏差，像朋友在秋日旅行途中抓拍的照片，明媚、自由、轻盈，充满青春电影感。"
    }
  ],
  "settings": {
    "result_type": "single",
    "n": 1,
    "resolution": "2k",
    "aspect_ratio": "auto"
  }
}'
```

### 2️⃣ 风格参考

#### 风格与配色迁移

提示词写法：参考【风格图】的【风格、配色与质感特点】，为【主体图】生成对应效果。保留主体的【形状、结构、关键部件与标识】，仅调整【需要迁移的色彩、光影或材质效果】；需要参考文字与排版时，另行给出【文案与布局要求】。

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

<div class="guide-case-media-list" style="--shot-ratio: 0.750">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-053.734d7d0924941b23.webp" alt="" loading="lazy" /></div>

<p>@ref_1 · 蓝色X光风格与配色</p>
</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-054.13f34f2a5fa28379.webp" alt="" loading="lazy" /></div>

<p>@ref_2 · 粉色旅行包主体</p>
</div>
</div>

```text
参考@ref_1的x光照射风格和配色，给@ref_2进行风格转化，参考文字和排版一致
```

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<div class="guide-case-media-list guide-case-media-list-full">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-055.a11dfb7ffd42e41d.webp" alt="" loading="lazy" /></div>

</div>
</div>

API 代码：

```cURL
curl --request POST \
  --url "https://api-beijing.klingai.com/image-generation/kling-4.0" \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header "Content-Type: application/json" \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "参考@ref_1的x光照射风格和配色，给@ref_2进行风格转化，参考文字和排版一致"
    },
    {
      "type": "refer_image",
      "url": "https://p1-kling.klingai.com/kcdn/cdn-kcdn112452/tutorials/kling-image-4-0/api-examples-20261110/style_input.png",
      "id": "ref_1"
    },
    {
      "type": "refer_image",
      "url": "https://p1-kling.klingai.com/kcdn/cdn-kcdn112452/tutorials/kling-image-4-0/api-examples-20261110/xray_style.png",
      "id": "ref_2"
    }
  ],
  "settings": {
    "result_type": "single",
    "n": 1,
    "resolution": "2k",
    "aspect_ratio": "auto"
  }
}'
```

#### 绘画风格转绘

提示词写法：将【主体图】按照【风格参考图】的绘画风格转绘，要求画面细节丰富、风格响应准确。保留【人物身份、动作、主体结构或其他关键特征】，画面比例为【比例】；按需要说明【笔触、线条、材质、背景是否一并转换】。

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

<div class="guide-case-media-list" style="--shot-ratio: 1.059">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-058.47d8d8c684efbd93.webp" alt="" loading="lazy" /></div>

<p>@ref_1 · 绘画风格</p>
</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-059.30a40eda507204eb.webp" alt="" loading="lazy" /></div>

<p>@ref_2 · 女性面部主体</p>
</div>
</div>

```text
把@ref_2按照@ref_1的风格转绘，要求画面细节丰富，风格响应准确，3:4画幅尺寸
```

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<div class="guide-case-media-list guide-case-media-list-full">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-060.08df1087820ba93c.webp" alt="" loading="lazy" /></div>

</div>
</div>

API 代码：

```cURL
curl --request POST \
  --url "https://api-beijing.klingai.com/image-generation/kling-4.0" \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header "Content-Type: application/json" \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "把@ref_2按照@ref_1的风格转绘，要求画面细节丰富，风格响应准确，3:4画幅尺寸"
    },
    {
      "type": "refer_image",
      "url": "https://p1-kling.klingai.com/kcdn/cdn-kcdn112452/tutorials/kling-image-4-0/api-examples-20261110/ref_-2257508069206203136.png",
      "id": "ref_1"
    },
    {
      "type": "refer_image",
      "url": "https://p1-kling.klingai.com/kcdn/cdn-kcdn112452/tutorials/kling-image-4-0/api-examples-20261110/ref_5387406207519161726.png",
      "id": "ref_2"
    }
  ],
  "settings": {
    "result_type": "single",
    "n": 1,
    "resolution": "2k",
    "aspect_ratio": "3:4"
  }
}'
```

#### 动作、光影与质感复刻

提示词写法：使用【人物图】中的人物，参考【效果图】的【动作、身体朝向、构图、光影、滤镜与质感】生成新画面。保留【人物身份、面部特征、发型和需要保留的服饰】，说明哪些效果需要复刻、哪些内容保持不变，不将人物替换为效果图中的人物。

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

<div class="guide-case-media-list" style="--shot-ratio: 0.743">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-061.082eb7463a9f0c04.webp" alt="" loading="lazy" /></div>

<p>@ref_1 · 姿势光影与质感</p>
</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-062.bf40258bd5cd9684.webp" alt="" loading="lazy" /></div>

<p>@ref_2 · 人物主体</p>
</div>
</div>

```text
人物@ref_2完全复刻@ref_1的图片效果，包括动作滤镜以及质感
```

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<div class="guide-case-media-list guide-case-media-list-full">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-063.3287ca96728066c0.webp" alt="" loading="lazy" /></div>

</div>
</div>

API 代码：

```cURL
curl --request POST \
  --url "https://api-beijing.klingai.com/image-generation/kling-4.0" \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header "Content-Type: application/json" \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "人物@ref_2完全复刻@ref_1的图片效果，包括动作滤镜以及质感"
    },
    {
      "type": "refer_image",
      "url": "https://p1-kling.klingai.com/kcdn/cdn-kcdn112452/tutorials/kling-image-4-0/api-examples-20261110/ref_5336452827380069132.png",
      "id": "ref_1"
    },
    {
      "type": "refer_image",
      "url": "https://p1-kling.klingai.com/kcdn/cdn-kcdn112452/tutorials/kling-image-4-0/api-examples-20261110/ref_1552508722112523252.png",
      "id": "ref_2"
    }
  ],
  "settings": {
    "result_type": "single",
    "n": 1,
    "resolution": "2k",
    "aspect_ratio": "auto"
  }
}'
```

### 3️⃣ 节日贺卡生成

提示词写法：参考【风格图】的【视觉风格】，制作一张【节日／用途】贺卡。主文案为“【祝福语】”，使用【文案语言】，补充【背景、配色、装饰与排版要求】。如使用人物或家庭照片，另行引用【人物参考图】，保持身份一致，并说明照片与节日装饰的布局关系。

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

<div class="guide-case-media-list" style="--shot-ratio: 0.743">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-064.5e352afc5b6cc358.webp" alt="" loading="lazy" /></div>

<p>@ref_1 · 拼贴风格</p>
</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-065.d82b63dbbecb0a42.webp" alt="" loading="lazy" /></div>

<p>@ref_2 · 唯一家庭身份</p>
</div>
</div>

```text
Use @ref_1 as the visual style reference and @ref_2 as the only family identity reference. Create a warm handmade Christmas greeting card in a vintage cut-paper collage and scrapbook style.

Preserve the exact identity of the family from @ref_2: the mother, father, and child, including their facial features, hairstyles, skin tones, expressions, family relationship, clothing, and recognizable appearance. Do not add or remove any family members. Carefully cut the family out from the original background and place the family photograph in the center of the card as a colorful printed family photo. Keep the original natural colors of the family photo, including realistic skin tones, hair colors, clothing colors, and facial details. Do not convert the family photo to black and white, grayscale, monochrome, or faded sepia. The family photo must remain clear, warm, vivid, and recognizable.

Place the colorful family photo inside a large red or burgundy Christmas heart, Christmas wreath, or handmade irregular paper frame. Give the photo irregular torn-paper edges, a soft cream border, subtle paper shadows, visible glue or tape marks, and a slightly tilted scrapbook placement. The photo should look like a real colorful family photograph pasted onto a handmade Christmas card, while preserving the original family atmosphere and natural smiles.

Use an off-white aged paper background with visible paper fibers, light creases, imperfect edges, handmade cutting marks, vintage printing grain, distressed ink, slight color misregistration, and tactile paper texture. Surround the family photo with festive handmade collage elements: red and dark green stars, gold stars, pine branches, holly leaves, red berries, snowflakes, candy canes, Christmas lights, bells, ribbons, gift boxes, stockings, gingerbread cookies, Santa hats, snowmen, and a small Christmas tree. Every decorative element should look like a paper cutout, fabric patch, vintage magazine illustration, or hand-painted scrapbook piece, not glossy 3D icons.

At the top or upper area of the card, create handmade collage lettering that reads:
“MERRY CHRISTMAS”

Use mismatched cut-paper letters with different paper textures, colors, sizes, and typefaces. The phrase must remain clearly readable. Place the following Christmas message in a clean, elegant handwritten or vintage printed text block, preferably on a cream paper note or parchment-like collage panel so that all words remain legible:

“Dear Oliver,

Wishing you a very Merry Christmas and a happy, healthy New Year.
May you stay well, feel happy, and enjoy many warm and peaceful moments with your loved ones.

With warmest wishes,
Emily”

Keep the wording exactly as provided. Do not rewrite, omit, paraphrase, duplicate, or replace the text. Use tasteful dark green, burgundy, or charcoal lettering with good spacing and strong contrast against the light paper panel. The message should feel personal, warm, sincere, and suitable for a family Christmas greeting card.

Follow the composition of @ref_1: a central colorful family photograph, surrounded by handmade Christmas decorations, cutout shapes, stars, leaves, ornaments, and scrapbook lettering. Keep the composition charming, slightly asymmetrical, tactile, playful, nostalgic, and carefully balanced. The colorful family photo must remain the main emotional focus, while the Christmas decorations and message support the composition without covering the faces.

Color palette: warm cream, muted red, burgundy, forest green, dark green, mustard gold, pale blue, bright natural photo colors, and charcoal black. Vintage 1970s–1990s handmade Christmas card aesthetic, retro scrapbook poster, screen-print texture, faded surrounding ink, colorful family photo collage, cut-paper collage, warm family holiday greeting card, nostalgic handmade design, collectible Christmas card, vertical format, highly detailed.
```

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<div class="guide-case-media-list guide-case-media-list-full">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-066.3325ca39540a8106.webp" alt="" loading="lazy" /></div>

</div>
</div>

API 代码：

```cURL
curl --request POST \
  --url "https://api-beijing.klingai.com/image-generation/kling-4.0" \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header "Content-Type: application/json" \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "Use @ref_1 as the visual style reference and @ref_2 as the only family identity reference. Create a warm handmade Christmas greeting card in a vintage cut-paper collage and scrapbook style.\n\nPreserve the exact identity of the family from @ref_2: the mother, father, and child, including their facial features, hairstyles, skin tones, expressions, family relationship, clothing, and recognizable appearance. Do not add or remove any family members. Carefully cut the family out from the original background and place the family photograph in the center of the card as a colorful printed family photo. Keep the original natural colors of the family photo, including realistic skin tones, hair colors, clothing colors, and facial details. Do not convert the family photo to black and white, grayscale, monochrome, or faded sepia. The family photo must remain clear, warm, vivid, and recognizable.\n\nPlace the colorful family photo inside a large red or burgundy Christmas heart, Christmas wreath, or handmade irregular paper frame. Give the photo irregular torn-paper edges, a soft cream border, subtle paper shadows, visible glue or tape marks, and a slightly tilted scrapbook placement. The photo should look like a real colorful family photograph pasted onto a handmade Christmas card, while preserving the original family atmosphere and natural smiles.\n\nUse an off-white aged paper background with visible paper fibers, light creases, imperfect edges, handmade cutting marks, vintage printing grain, distressed ink, slight color misregistration, and tactile paper texture. Surround the family photo with festive handmade collage elements: red and dark green stars, gold stars, pine branches, holly leaves, red berries, snowflakes, candy canes, Christmas lights, bells, ribbons, gift boxes, stockings, gingerbread cookies, Santa hats, snowmen, and a small Christmas tree. Every decorative element should look like a paper cutout, fabric patch, vintage magazine illustration, or hand-painted scrapbook piece, not glossy 3D icons.\n\nAt the top or upper area of the card, create handmade collage lettering that reads:\n“MERRY CHRISTMAS”\n\nUse mismatched cut-paper letters with different paper textures, colors, sizes, and typefaces. The phrase must remain clearly readable. Place the following Christmas message in a clean, elegant handwritten or vintage printed text block, preferably on a cream paper note or parchment-like collage panel so that all words remain legible:\n\n“Dear Oliver,\n\nWishing you a very Merry Christmas and a happy, healthy New Year.\nMay you stay well, feel happy, and enjoy many warm and peaceful moments with your loved ones.\n\nWith warmest wishes,\nEmily”\n\nKeep the wording exactly as provided. Do not rewrite, omit, paraphrase, duplicate, or replace the text. Use tasteful dark green, burgundy, or charcoal lettering with good spacing and strong contrast against the light paper panel. The message should feel personal, warm, sincere, and suitable for a family Christmas greeting card.\n\nFollow the composition of @ref_1: a central colorful family photograph, surrounded by handmade Christmas decorations, cutout shapes, stars, leaves, ornaments, and scrapbook lettering. Keep the composition charming, slightly asymmetrical, tactile, playful, nostalgic, and carefully balanced. The colorful family photo must remain the main emotional focus, while the Christmas decorations and message support the composition without covering the faces.\n\nColor palette: warm cream, muted red, burgundy, forest green, dark green, mustard gold, pale blue, bright natural photo colors, and charcoal black. Vintage 1970s–1990s handmade Christmas card aesthetic, retro scrapbook poster, screen-print texture, faded surrounding ink, colorful family photo collage, cut-paper collage, warm family holiday greeting card, nostalgic handmade design, collectible Christmas card, vertical format, highly detailed."
    },
    {
      "type": "refer_image",
      "url": "https://p1-kling.klingai.com/kcdn/cdn-kcdn112452/tutorials/kling-image-4-0/api-examples-20261110/ref_3885055675500939882.png",
      "id": "ref_1"
    },
    {
      "type": "refer_image",
      "url": "https://p1-kling.klingai.com/kcdn/cdn-kcdn112452/tutorials/kling-image-4-0/api-examples-20261110/ref_-2319974293355923273.png",
      "id": "ref_2"
    }
  ],
  "settings": {
    "result_type": "single",
    "n": 1,
    "resolution": "2k",
    "aspect_ratio": "auto"
  }
}'
```

## 5 打工人福音

### 1️⃣ PPT组图生成

提示词写法：生成【页数】页【画面比例】的演示页面图片，主题为【主题】，面向【受众】，语言为【文案语言】，整体风格为【视觉风格】。可提供逐页大纲：第1页：【标题、文案与布局】；第2页：【内容要求】；第3页：【内容要求】……未提供大纲时按主题安排各页内容。保持配色、字体、标题样式与主体设计一致，每页独立成图。

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

```text
=== SLIDE 1 · COVER ===
premium tech keynote style, deep space black studio background, cinematic rim lighting, minimal sans-serif typography in pearl white with generous negative space, professional presentation slide, 16:9 widescreen, flagship smartphone floating at a dramatic three-quarter angle, grade-five titanium frame with brushed metal texture, polished ceramic back panel, circular halo camera module ringed with fine metallic ridges, soft warm amber and violet aurora gradient glow blooming behind the device, subtle floor reflection beneath, Slide title: AETHER ONE, Subtitle: Light, made personal. Introducing the most luminous device we have ever built, sophisticated monochrome palette of deep black pearl white and silver titanium with warm amber and violet aurora accents, avoid generic tech blue colors, high-end industrial design visual, ultra high resolution, cinematic color grading, sharp typography
=== SLIDE 2 · DESIGN PHILOSOPHY ===
premium tech keynote style, deep space black studio background, cinematic rim lighting, minimal sans-serif typography in pearl white with generous negative space, professional presentation slide, 16:9 widescreen, a single beam of white light passing through darkness and spreading into a full spectrum across the stage, giant statement typography floating over a soft amber-and-violet gradient, one thin golden hairline crossing the frame, Slide title: Everything begins with light., Subtitle: Design philosophy, sophisticated monochrome palette of deep black pearl white and silver titanium with warm amber and violet aurora accents, avoid generic tech blue colors, high-end industrial design visual, ultra high resolution, cinematic color grading, sharp typography
=== SLIDE 3 · AETHER A2 CHIP ===
premium tech keynote style, deep space black studio background, cinematic rim lighting, minimal sans-serif typography in pearl white with generous negative space, professional presentation slide, 16:9 widescreen, the Aether A2 chip die floating above the stage like a tiny city of light, golden circuit veins glowing across the silicon, exploded layers suspended beneath, thin light beams connecting each layer, Slide title: Aether A2. The engine of light., Subtitle: Built on a second-generation 3-nanometer process, sophisticated monochrome palette of deep black pearl white and silver titanium with warm amber and violet aurora accents, avoid generic tech blue colors, high-end industrial design visual, ultra high resolution, cinematic color grading, sharp typography
=== SLIDE 4 · LUMINOUS DISPLAY ===
premium tech keynote style, deep space black studio background, cinematic rim lighting, minimal sans-serif typography in pearl white with generous negative space, professional presentation slide, 16:9 widescreen, the display panel floating upright in the dark, the screen glowing with a live color spectrum, light washing across the studio floor, a thin beam tracing the panel edges, Slide title: Luminous. By name. By nature., Subtitle: A 6.9-inch LTPO OLED that reaches 3,000 nits, sophisticated monochrome palette of deep black pearl white and silver titanium with warm amber and violet aurora accents, avoid generic tech blue colors, high-end industrial design visual, ultra high resolution, cinematic color grading, sharp typography
=== SLIDE 5 · HALO CAMERA ===
premium tech keynote style, deep space black studio background, cinematic rim lighting, minimal sans-serif typography in pearl white with generous negative space, professional presentation slide, 16:9 widescreen, exploded view of the Halo camera module suspended in darkness, lens stack separated into floating elements, beams of light entering the main lens, soft night-city bokeh glowing behind, Slide title: Halo. Light, composed., Subtitle: A professional imaging system, sophisticated monochrome palette of deep black pearl white and silver titanium with warm amber and violet aurora accents, avoid generic tech blue colors, high-end industrial design visual, ultra high resolution, cinematic color grading, sharp typography
=== SLIDE 6 · BATTERY & CHARGING ===
premium tech keynote style, deep space black studio background, cinematic rim lighting, minimal sans-serif typography in pearl white with generous negative space, professional presentation slide, 16:9 widescreen, a glowing ring of amber light encircling the device, charging pulses rippling outward like a slow heartbeat, a soft energy wave spreading across the dark floor, Slide title: All day. Then some., Subtitle: A 5,300-milliampere-hour silicon-carbon battery with 85-watt HyperCharge — endurance that keeps up with your light, sophisticated monochrome palette of deep black pearl white and silver titanium with warm amber and violet aurora accents, avoid generic tech blue colors, high-end industrial design visual, ultra high resolution, cinematic color grading, sharp typography
=== SLIDE 7 · AETHEROS & AI ===
premium tech keynote style, deep space black studio background, cinematic rim lighting, minimal sans-serif typography in pearl white with generous negative space, professional presentation slide, 16:9 widescreen, translucent interface panels floating in layered dark space, small glowing nodes connected by fine threads of light, a soft aurora haze behind the panels, Slide title: AetherOS 12. Intelligence, at home., Subtitle: Rebuilt around the Aether A2 neural engine, sophisticated monochrome palette of deep black pearl white and silver titanium with warm amber and violet aurora accents, avoid generic tech blue colors, high-end industrial design visual, ultra high resolution, cinematic color grading, sharp typography
=== SLIDE 8 · PRICING & CLOSING ===
premium tech keynote style, deep space black studio background, cinematic rim lighting, minimal sans-serif typography in pearl white with generous negative space, professional presentation slide, 16:9 widescreen, the full device lineup floating in a row at three-quarter angles, soft golden horizon light rising behind the row, faint pricing lines glowing beneath each device, Slide title: AETHER ONE., Subtitle: Light, made personal. From 999 dollars — pre-orders open this Friday, in stores October the twenty-eighth, sophisticated monochrome palette of deep black pearl white and silver titanium with warm amber and violet aurora accents, avoid generic tech blue colors, high-end industrial design visual, ultra high resolution, cinematic color grading, sharp typography
```

<p class="guide-case-note">仅提示词，无参考图。</p>

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<div class="guide-case-media-list guide-case-media-list-thirds" style="--shot-ratio: 1.771">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-067.c9f3fc70d3c9e7ed.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-068.624c22e1d60bbeb6.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-069.e1dc561f015d4d05.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-070.c5cf9bbd87b2415b.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-071.02d626eec7457a28.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-072.7ad486633e5cca34.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-073.837eb7ec15c8b16a.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-prompt-en-074.485536b2bf511578.webp" alt="" loading="lazy" /></div>

</div>
</div>

API 代码：

```cURL
curl --request POST \
  --url "https://api-beijing.klingai.com/image-generation/kling-4.0" \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header "Content-Type: application/json" \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "=== SLIDE 1 · COVER ===\npremium tech keynote style, deep space black studio background, cinematic rim lighting, minimal sans-serif typography in pearl white with generous negative space, professional presentation slide, 16:9 widescreen, flagship smartphone floating at a dramatic three-quarter angle, grade-five titanium frame with brushed metal texture, polished ceramic back panel, circular halo camera module ringed with fine metallic ridges, soft warm amber and violet aurora gradient glow blooming behind the device, subtle floor reflection beneath, Slide title: AETHER ONE, Subtitle: Light, made personal. Introducing the most luminous device we have ever built, sophisticated monochrome palette of deep black pearl white and silver titanium with warm amber and violet aurora accents, avoid generic tech blue colors, high-end industrial design visual, ultra high resolution, cinematic color grading, sharp typography\n=== SLIDE 2 · DESIGN PHILOSOPHY ===\npremium tech keynote style, deep space black studio background, cinematic rim lighting, minimal sans-serif typography in pearl white with generous negative space, professional presentation slide, 16:9 widescreen, a single beam of white light passing through darkness and spreading into a full spectrum across the stage, giant statement typography floating over a soft amber-and-violet gradient, one thin golden hairline crossing the frame, Slide title: Everything begins with light., Subtitle: Design philosophy, sophisticated monochrome palette of deep black pearl white and silver titanium with warm amber and violet aurora accents, avoid generic tech blue colors, high-end industrial design visual, ultra high resolution, cinematic color grading, sharp typography\n=== SLIDE 3 · AETHER A2 CHIP ===\npremium tech keynote style, deep space black studio background, cinematic rim lighting, minimal sans-serif typography in pearl white with generous negative space, professional presentation slide, 16:9 widescreen, the Aether A2 chip die floating above the stage like a tiny city of light, golden circuit veins glowing across the silicon, exploded layers suspended beneath, thin light beams connecting each layer, Slide title: Aether A2. The engine of light., Subtitle: Built on a second-generation 3-nanometer process, sophisticated monochrome palette of deep black pearl white and silver titanium with warm amber and violet aurora accents, avoid generic tech blue colors, high-end industrial design visual, ultra high resolution, cinematic color grading, sharp typography\n=== SLIDE 4 · LUMINOUS DISPLAY ===\npremium tech keynote style, deep space black studio background, cinematic rim lighting, minimal sans-serif typography in pearl white with generous negative space, professional presentation slide, 16:9 widescreen, the display panel floating upright in the dark, the screen glowing with a live color spectrum, light washing across the studio floor, a thin beam tracing the panel edges, Slide title: Luminous. By name. By nature., Subtitle: A 6.9-inch LTPO OLED that reaches 3,000 nits, sophisticated monochrome palette of deep black pearl white and silver titanium with warm amber and violet aurora accents, avoid generic tech blue colors, high-end industrial design visual, ultra high resolution, cinematic color grading, sharp typography\n=== SLIDE 5 · HALO CAMERA ===\npremium tech keynote style, deep space black studio background, cinematic rim lighting, minimal sans-serif typography in pearl white with generous negative space, professional presentation slide, 16:9 widescreen, exploded view of the Halo camera module suspended in darkness, lens stack separated into floating elements, beams of light entering the main lens, soft night-city bokeh glowing behind, Slide title: Halo. Light, composed., Subtitle: A professional imaging system, sophisticated monochrome palette of deep black pearl white and silver titanium with warm amber and violet aurora accents, avoid generic tech blue colors, high-end industrial design visual, ultra high resolution, cinematic color grading, sharp typography\n=== SLIDE 6 · BATTERY & CHARGING ===\npremium tech keynote style, deep space black studio background, cinematic rim lighting, minimal sans-serif typography in pearl white with generous negative space, professional presentation slide, 16:9 widescreen, a glowing ring of amber light encircling the device, charging pulses rippling outward like a slow heartbeat, a soft energy wave spreading across the dark floor, Slide title: All day. Then some., Subtitle: A 5,300-milliampere-hour silicon-carbon battery with 85-watt HyperCharge — endurance that keeps up with your light, sophisticated monochrome palette of deep black pearl white and silver titanium with warm amber and violet aurora accents, avoid generic tech blue colors, high-end industrial design visual, ultra high resolution, cinematic color grading, sharp typography\n=== SLIDE 7 · AETHEROS & AI ===\npremium tech keynote style, deep space black studio background, cinematic rim lighting, minimal sans-serif typography in pearl white with generous negative space, professional presentation slide, 16:9 widescreen, translucent interface panels floating in layered dark space, small glowing nodes connected by fine threads of light, a soft aurora haze behind the panels, Slide title: AetherOS 12. Intelligence, at home., Subtitle: Rebuilt around the Aether A2 neural engine, sophisticated monochrome palette of deep black pearl white and silver titanium with warm amber and violet aurora accents, avoid generic tech blue colors, high-end industrial design visual, ultra high resolution, cinematic color grading, sharp typography\n=== SLIDE 8 · PRICING & CLOSING ===\npremium tech keynote style, deep space black studio background, cinematic rim lighting, minimal sans-serif typography in pearl white with generous negative space, professional presentation slide, 16:9 widescreen, the full device lineup floating in a row at three-quarter angles, soft golden horizon light rising behind the row, faint pricing lines glowing beneath each device, Slide title: AETHER ONE., Subtitle: Light, made personal. From 999 dollars — pre-orders open this Friday, in stores October the twenty-eighth, sophisticated monochrome palette of deep black pearl white and silver titanium with warm amber and violet aurora accents, avoid generic tech blue colors, high-end industrial design visual, ultra high resolution, cinematic color grading, sharp typography"
    }
  ],
  "settings": {
    "result_type": "series",
    "series_amount": 8,
    "resolution": "2k",
    "aspect_ratio": "16:9"
  }
}'
```
