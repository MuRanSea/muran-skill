<!-- Official source: https://klingai.com/document-api/api/usage-guide/kling-image-4-0.md -->
<!-- Source SHA-256: c5fc43218ae67bbfc54a02c09448ae67c9fabb9a2e180c2e145a8df01963b598 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://klingai.com/document-api/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling Image 4.0 使用手册

> 来源: https://klingai.com/document-api/api/usage-guide/kling-image-4-0
> 语言: zh
> 当前 Tab: Kling Image 4.0 使用手册
> 此内容为面向 LLM 优化的 Markdown，已展开页面内 Tab，并省略页面目录、复制按钮等 UI 控件。

::: info-box

Kling Image 4.0 是面向图片创作的生成模型，支持文字描述、单图与多图参考、关联组图以及电商详情和网页设计长图，可用于角色设定、摄影、海报、商品素材、贺卡及演示页面创作。

本文介绍模型能力、API任务、输入要求、输出规格与提示词写法，帮助您从文字和参考素材开始，完成图片生成。

## 1 模型调用条件

调用 Kling Image 4.0 模型前，请确保您满足以下任一条件：

- 购买旗舰版资源包（[前往购买](https://klingai.com/dev/pricing?scrollTo=image)）
- 账户现金余额 > 0元，可留咨沟通充值（[前往留咨](https://klingai.com/document-api/api/usage-guide/kling-image-4-0#business-consult)）

## 2 使用前必读

### 2.1 任务类型与限制

先区分“独立图片”“有关联的组图”和“一张长页面”。文生图与参考图创作共用普通图片接口，通过 contents 表达输入、通过 settings 表达输出；长图使用独立接口。

| 对比项   | 独立图片                         | 关联组图                         | 长图                                                                          |
| -------- | -------------------------------- | -------------------------------- | ----------------------------------------------------------------------------- |
| 适合任务 | 照片、海报、单张角色设定图       | 分镜、成套角色、商品组图、演示页 | 电商详情页、网页视觉                                                          |
| 创建接口 | POST /image-generation/kling-4.0 | POST /image-generation/kling-4.0 | POST /long-image-generation/kling-4.0                                         |
| 模式参数 | result_type=single               | result_type=series               | skill=ecommerce / webpage                                                     |
| 张数     | n：1—9，默认1                    | series_amount：2—10或auto，默认4 | 固定一张完整长图                                                              |
| 分辨率   | 2k / 4k / 8k，默认2k             | 2k / 4k / 8k，默认2k             | 1k / 2k，默认1k                                                               |
| 参考素材 | 图片与多图主体合计≤10            | 图片与多图主体合计≤10            | 生成电商详情页必须提供1—3张图，网页设计可以输入一张风格参考图和一张主体参考图 |

三视图、四宫格、九宫格如果排在同一张画面内，仍应使用single。只有希望得到多张独立且相互关联的画面时，才选择series；series下n无效。

### 2.2 配置方法

#### 普通图片与关联组图

- 调用 /image-generation/kling-4.0。
- 在 contents 添加 type="prompt"，完整提示词写入 text。
- 有参考图时添加 type="refer_image"，通过 url 提供公开可访问的图片URL或合法Base64。
- 为引用素材设置任务内唯一的 id，提示词使用 @id。未显式引用的素材仍会作为参考生效。
- 根据任务设置 result_type、张数、resolution 和 aspect_ratio。

提示词示例：

> 人物身份参考 @person，服装参考 @outfit，配饰参考 @accessory。保留人物五官、服装颜色与关键设计细节，生成一张自然光街头穿搭照片。

普通图还支持 type="element"，以 element_id 引用通过图片定制的多图主体，数量与参考图片共用10个名额。请使用 Image 接口支持的输入素材类型。

#### 电商详情与网页长图

调用 /long-image-generation/kling-4.0，使用同样的prompt与refer_image结构。settings.skill必填：电商为ecommerce、网页视觉为webpage；电商必须提供1—3张图，网页设计可以输入一张风格参考图和一张主体参考图。电商可设置length，网页不支持length。每次只返回一张长图，不返回内部配图、HTML或可编辑设计文件。

### 2.3 报错机制

创建任务成功不等于生成已完成。同步响应检查code、message和request_id，再根据`data.id`查询；生成失败时检查任务status和message。鉴权、字段值、图片访问性、素材规格及额度分别排查，保留request_id便于定位；不要对未知结果的创建请求自动连发重试。

## 3 新手入门

### 第一步：准备账号与 API Key

在[开发者控制台](https://klingai.com/dev/api-key)创建新 API Key，在同一终端设置环境变量。下面为Bash/zsh写法，Windows可在兼容终端中运行或按环境调整。

```bash
export KLING_API_KEY="替换为你自己的API_Key"
```

### 第二步：创建图片任务

以下示例使用文字描述创建一张图片。提交后，请保存响应中的任务 ID，用于查询生成进度和获取结果。

```cURL
curl --request POST \
  --url "https://api-beijing.klingai.com/image-generation/kling-4.0" \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header "Content-Type: application/json" \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "温馨客厅里的橘猫随手拍，一只胖瘦适中的成年橘色虎斑猫端正坐在深灰色布艺沙发上，身体朝向镜头，脑袋微微歪向一侧，睁着绿色眼睛好奇地看着拍摄者。橘猫毛发短而细密，脸颊圆润，鼻子粉红，胡须清晰。旁边放着米白色毛绒抱枕，前景铺着带黄色和深蓝色图案的柔软毯子。背景是一扇明亮的大窗户，可以看到室外住宅和树木，左侧隐约露出圆形墙镜、绿植和客厅家具。白天自然光从窗边照进来，猫咪边缘带有柔和轮廓光。竖版中景，iPhone室内实拍感，温暖日常，真实毛发纹理。"
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

| 参数                  | 作用         | 本例         |
| --------------------- | ------------ | ------------ |
| contents[].type       | 输入类别     | prompt       |
| contents[].text       | 完整画面描述 | 橘猫客厅随拍 |
| settings.result_type  | 输出模式     | single       |
| settings.n            | 独立图片张数 | 1            |
| settings.resolution   | 清晰度       | 2k           |
| settings.aspect_ratio | 宽高比       | 3:4          |

响应示例（字段结构示意，ID为占位）：

```json
{
    "code": 0,
    "message": "SUCCEED",
    "request_id": "example-request-id",
    "data": {
        "id": "example-task-id",
        "status": "submitted",
        "create_time": 1790000000000,
        "update_time": 1790000000000
    }
}
```

### 第三步：查询任务状态

将真实创建结果中的`data.id`填入查询地址。task_ids与external_task_ids只能选一种；GET参数在URL中，不发送JSON请求体。可以通过回调机制替代持续轮询，避免过密查询。

```cURL
curl --request GET \
  --url "https://api-beijing.klingai.com/tasks?task_ids=替换为真实任务ID" \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header "Content-Type: application/json"
```

| status     | 含义     | 下一步                                    |
| ---------- | -------- | ----------------------------------------- |
| submitted  | 已提交   | 等待进入处理                              |
| processing | 处理中   | 稍后查询或等待回调                        |
| succeeded  | 生成成功 | 读取outputs并下载                         |
| failed     | 生成失败 | 检查message与输入，必要时凭request_id排查 |

### 第四步：获取图片

查询返回的data是数组；匹配目标任务，成功后读取outputs[].url。组图共享group_id并按组内顺序返回，不按文件名重排。下方仅展示单图结构示意，URL不是可下载的真实结果。

```json
{
    "code": 0,
    "message": "SUCCEED",
    "request_id": "example-query-id",
    "data": [
        {
            "id": "example-task-id",
            "status": "succeeded",
            "message": "",
            "outputs": [
                {
                    "type": "image",
                    "url": "https://example.com/result.png"
                }
            ]
        }
    ]
}
```

生成结果链接为防盗链格式，结果图片在30天后清理，请及时下载转存。回调配置通过options.callback_url指定，通知协议详见[Callback协议](https://klingai.com/document-api/api/get-started/callbacks)。

## 4 Kling Image 4.0 最新能力

### 4.1 原生相机真实感

通过具体动作、生活环境、拍摄距离和自然光线组织画面，适合手机随拍、纪实摄影与电影静帧。真实感并不要求每一处都清晰或明亮，适度遮挡、景深和不均匀光照也是画面信息。

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-001.ff6a91097516a327.webp" alt="" loading="lazy" /></div>

### 4.2 文字表现与复杂排版

支持在提示词中指定主标题、副标题、小字、字形与位置，用于海报、封面和品牌视觉。单张图片支持最多 2,000 字的文字生成；实际呈现效果受语种、字体、文字密度和布局影响。生成后，请校对专有名词、数字、标点与小字。

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-002.9a59ba7bd75ea13e.webp" alt="" loading="lazy" /></div>

### 4.3 原生 8K

普通单图与组图支持2k、4k、8k。长图技能的清晰度单独限定为1k、2k，不能沿用普通图的8k参数。

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-003.3b21f9de0eb373b0.webp" alt="" loading="lazy" /></div>

### 4.4 连贯组图与多素材一致性

一次提示词可组织2—10张关联画面，通过逐张描述与一致性要求，制作分镜、角色设定、商品素材或演示页。角色图、服装图、商品图和风格图可分别分工，不应只笼统写‘参考所有图片’。

<div class="guide-case-media-list guide-image-grid" style="--shot-ratio: 1.778">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-004.15bd99a3db40857e.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-005.28d60ee71a3cc1e2.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-006.372ed7c92461b571.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-007.b508bbdff2a7d411.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-008.cd2821291eb6b765.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-009.90af2d2c638b4e16.webp" alt="" loading="lazy" /></div>

</div>
</div>

### 4.5 字体与风格引导

支持在 prompt 中指定字体。只需在提示词中补充“字体为：XXX体”，例如“字体为：长风手书体”。当前模型支持的字体清单见第 6.8 节。

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-010.69100390ca0bf007.webp" alt="" loading="lazy" /></div>

### 4.6 页面级长图

电商详情和网页设计使用长图接口，由内容模块形成一张完整页面视觉。

<div class="media-wrap image-wrap guide-image is-long"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-011.6511a59b6056e737.webp" alt="" loading="lazy" /></div>

## 5 能力概述

### 5.1 模型与输出规格

| 项目     | 普通单图/组图                                                                               | 长图                                                                                                       |
| -------- | ------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| 模型路径 | image-generation/kling-4.0                                                                  | long-image-generation/kling-4.0                                                                            |
| 清晰度   | 2k、4k、8k                                                                                  | 1k、2k                                                                                                     |
| 比例     | auto及8种固定比例                                                                           | 没有普通图aspect_ratio配置项                                                                               |
| 输入文字 | 纯英文≤50,000字符；纯非英文≤21,000字符；混合输入：英文字符数/50000 + 非英文字符数/21000 ≤ 1 | prompt 必填；纯英文≤166,000字符；纯非英文≤71,000字符；混合输入：英文字符数/166000 + 非英文字符数/71000 ≤ 1 |
| 图片输入 | JPG/JPEG/PNG，≤30MB，双边≥300px，比例2:5—5:2                                                | 相同图片规格；生成电商详情页必须提供1—3张图，网页设计可以输入一张风格参考图和一张主体参考图                |
| 输出形态 | 单图或多张关联组图                                                                          | 每次一张完整长图                                                                                           |

### 5.2 典型创作能力

| 创作目标         | 任务方式                   | 提示词重点                       |
| ---------------- | -------------------------- | -------------------------------- |
| 生活照片与纪实   | single                     | 人物状态、场景、光线和拍摄方式   |
| 角色多视图设定   | single或series，按页数决定 | 视角顺序、布局、角色特征         |
| 故事分镜         | series                     | 总张数、逐张静帧、统一角色与风格 |
| 风格/配色转绘    | single＋多图参考           | 风格来源与主体来源分离           |
| 商品与穿搭       | single或series＋参考       | 商品结构、服装细节及模特身份     |
| 海报/主视觉/贺卡 | single                     | 逐字文案、字形、层级与位置       |
| 电商/网页页面    | 长图ecommerce或webpage     | 商品事实、模块顺序、品牌与文案   |
| 演示页面         | series                     | 页数、逐页内容和整套视觉系统     |

## 6 特色能力与使用方法

### 6.1 文生图

用文字描述主体正在做什么、身处什么环境，以及画面如何被拍摄或设计。真实感图片可以从“主体＋动作或状态＋具体场景＋拍摄方式”开始。

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

```text
温馨客厅里的橘猫随手拍，一只胖瘦适中的成年橘色虎斑猫端正坐在深灰色布艺沙发上，身体朝向镜头，脑袋微微歪向一侧，睁着绿色眼睛好奇地看着拍摄者。橘猫毛发短而细密，脸颊圆润，鼻子粉红，胡须清晰。旁边放着米白色毛绒抱枕，前景铺着带黄色和深蓝色图案的柔软毯子。背景是一扇明亮的大窗户，可以看到室外住宅和树木，左侧隐约露出圆形墙镜、绿植和客厅家具。白天自然光从窗边照进来，猫咪边缘带有柔和轮廓光。竖版中景，iPhone室内实拍感，温暖日常，真实毛发纹理。
```

<p class="guide-case-note">仅提示词，无参考图。</p>

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<div class="guide-case-media-list guide-case-media-list-full">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-012.61945ff123ca6f08.webp" alt="" loading="lazy" /></div>

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
      "text": "温馨客厅里的橘猫随手拍，一只胖瘦适中的成年橘色虎斑猫端正坐在深灰色布艺沙发上，身体朝向镜头，脑袋微微歪向一侧，睁着绿色眼睛好奇地看着拍摄者。橘猫毛发短而细密，脸颊圆润，鼻子粉红，胡须清晰。旁边放着米白色毛绒抱枕，前景铺着带黄色和深蓝色图案的柔软毯子。背景是一扇明亮的大窗户，可以看到室外住宅和树木，左侧隐约露出圆形墙镜、绿植和客厅家具。白天自然光从窗边照进来，猫咪边缘带有柔和轮廓光。竖版中景，iPhone室内实拍感，温暖日常，真实毛发纹理。"
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

### 6.2 单图参考

基于一张参考图生成新的画面，可用于角色多视图、姿态变化等创作。说明需要改变的视角和布局，以及需要保持一致的外貌、服饰等特征。

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

<div class="guide-case-media-list guide-case-media-list-full">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-013.a259f11a59ed0a89.webp" alt="" loading="lazy" /></div>

<p>参考图</p>
</div>
</div>

```text
根据@character 中的人物外观，生成一张纯白色背景的同一角色的标准三视图（正面全身、侧面全身、背面全身），画面左侧为角色高清面部特写，右侧整齐排列三个全身视角，角色五官、发型、服饰、外形、画面风格在所有视图中完全一致。
```

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<div class="guide-case-media-list guide-case-media-list-full">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-014.d7ce80369d16a084.webp" alt="" loading="lazy" /></div>

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
      "text": "根据@character 中的人物外观，生成一张纯白色背景的同一角色的标准三视图（正面全身、侧面全身、背面全身），画面左侧为角色高清面部特写，右侧整齐排列三个全身视角，角色五官、发型、服饰、外形、画面风格在所有视图中完全一致。"
    },
    {
      "type": "refer_image",
      "url": "https://p1-kling.klingai.com/kcdn/cdn-kcdn112452/tutorials/kling-image-4-0/api-examples-20261110/character.png",
      "id": "character"
    }
  ],
  "settings": {
    "result_type": "single",
    "n": 1,
    "resolution": "2k",
    "aspect_ratio": "16:9"
  }
}'
```

### 6.3 多图参考

将多张参考图中的人物、服饰、商品或场景组合到新画面中。逐一说明每张图的用途和需要保留的特征，例如人物来自哪张图、服装与配饰来自哪些图。

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

### 6.4 分镜组图

用一次描述生成一组连贯的分镜画面，保持角色、服装、场景和道具一致。按顺序说明每张分镜的动作、景别和机位，每张呈现一个明确瞬间。

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

<div class="guide-case-media-list" style="--shot-ratio: 1.333">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-020.6c89e9ba230912d6.webp" alt="" loading="lazy" /></div>

<p>参考图</p>
</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-021.e8963ad3a6ac757b.webp" alt="" loading="lazy" /></div>

<p>参考图</p>
</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-022.d08ee8213f2115bf.webp" alt="" loading="lazy" /></div>

<p>参考图</p>
</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-023.11bf6cebd21b7eb7.webp" alt="" loading="lazy" /></div>

<p>参考图</p>
</div>
</div>

```text
生成四张连贯的写实仙侠短剧分镜，9:16 竖向，每张为独立画面，不拼图。女主参考 @heroine，男主参考 @hero，场景参考 @peach_forest，桃花外形参考 @peach_blossom。第1张：女主从桃树后探出身子，微笑看向男主。第2张：女主将一朵桃花插在男主的发饰旁。第3张：男主、女主在桃树下相握着手，轻轻对视。第4张：女主倚在男主肩旁，男主发饰上的桃花仍在。保持同一角色的五官、发型、服饰，以及桃花林场景与画面风格一致。
```

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<div class="guide-case-media-list" style="--shot-ratio: 0.565">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-024.9810033b96962ca4.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-025.22c8be6b28f6172f.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-026.5cca448fb2573e83.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-027.6018f73dbc861a96.webp" alt="" loading="lazy" /></div>

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
      "text": "生成四张连贯的写实仙侠短剧分镜，9:16 竖向，每张为独立画面，不拼图。女主参考 @heroine，男主参考 @hero，场景参考 @peach_forest，桃花外形参考 @peach_blossom。第1张：女主从桃树后探出身子，微笑看向男主。第2张：女主将一朵桃花插在男主的发饰旁。第3张：男主、女主在桃树下相握着手，轻轻对视。第4张：女主倚在男主肩旁，男主发饰上的桃花仍在。保持同一角色的五官、发型、服饰，以及桃花林场景与画面风格一致。"
    },
    {
      "type": "refer_image",
      "url": "https://p1-kling.klingai.com/kcdn/cdn-kcdn112452/tutorials/kling-image-4-0/api-examples-20261110/heroine.png",
      "id": "heroine"
    },
    {
      "type": "refer_image",
      "url": "https://p1-kling.klingai.com/kcdn/cdn-kcdn112452/tutorials/kling-image-4-0/api-examples-20261110/hero.png",
      "id": "hero"
    },
    {
      "type": "refer_image",
      "url": "https://p1-kling.klingai.com/kcdn/cdn-kcdn112452/tutorials/kling-image-4-0/api-examples-20261110/peach_forest.png",
      "id": "peach_forest"
    },
    {
      "type": "refer_image",
      "url": "https://p1-kling.klingai.com/kcdn/cdn-kcdn112452/tutorials/kling-image-4-0/api-examples-20261110/peach_blossom.png",
      "id": "peach_blossom"
    }
  ],
  "settings": {
    "result_type": "series",
    "series_amount": 4,
    "resolution": "2k",
    "aspect_ratio": "9:16"
  }
}'
```

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

<div class="guide-case-media-list guide-case-media-list-full">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-028.b6df53c9151bd515.webp" alt="" loading="lazy" /></div>

<p>@ref_1 · 动作片主角</p>
</div>
</div>

```text
参考素材职责：@ref_1：动作片主角。
黄昏工业废墟，暖金逆光、冷灰阴影、浓烟与火光，粗粝胶片质感，强纵深、强冲击、快节奏的画面动作和带有微微颠簸的画面，整个环境充满了爆炸、枪声的战场背景音。呈现主角闯入战火的压迫感。01｜抵达 · 主角持枪抵达，捕捉军靴触地、屈膝落稳的瞬间。衣角被旋翼风掀起，尘土包围身体，背景仍是同一段破墙。02｜冲向沙袋 · 侧面中景，主角持枪冲向几步外的沙袋。前方墙面被击中，碎屑横飞，身体前倾、步伐迅猛，直升机在左后方尘幕中隐去。03｜进入战斗 · 侧面中景，主角在沙袋后，一手撑住袋沿。弹着点在外侧炸出砂尘，碎石掠过前景，捕捉身体刚刚收进掩体的紧迫瞬间。04｜探身开火 · 中近景，主角从同一沙袋边缘探出上身射击，短促枪口火光照亮侧脸。远处厂房闪出火力，近处扬尘喷溅，人物与枪身形成有力斜线。05｜火线压低 · 紧凑近景，承接射击，主角迅速收低身体，肩膀贴住沙袋。砂粒从头盔旁飞过，脸上汗水混着灰尘，眼神紧绷；背景爆闪照亮半边面孔。06｜近处爆炸 · 超宽低机位，沙袋外的废弃车辆爆炸，火焰、黑烟与土浪轰然升起。主角蜷低在前景，手臂护住头部，逆向飞散的碎屑构成全片冲击峰值。07｜烟中起身 · 侧面中景，承接爆炸，主角撑住沙袋起身，转向身后几步外的厂房门洞。烟尘卷过肩背，车辆仍在燃烧，火光勾亮他孤身一人的轮廓。08｜闪入门洞 · 从门洞内向外看，主角弯腰跨入，肩背贴住门侧墙壁，步枪收在身前。门外火星与砂尘掠过，冷暗室内与炽亮战场形成强烈反差。09｜门边反击 · 中近景，承接贴墙姿态，主角从门框边侧身开火。枪口闪光撕开昏暗，映亮汗尘覆盖的脸；门外浓烟与火光翻涌，以孤身迎战的动作收尾
```

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<div class="guide-case-media-list guide-case-media-list-thirds" style="--shot-ratio: 1.770">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-029.99493a8934699715.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-030.c47c878a484a2492.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-031.6bc039e78df9b9da.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-032.faa79d1e6964e94c.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-033.f3cd470efc759655.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-034.bd6dd27088032ea8.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-035.8141b4c1a8b99885.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-036.167791f7d7e3e428.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-037.6032948115610847.webp" alt="" loading="lazy" /></div>

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
      "text": "参考素材职责：@ref_1：动作片主角。\n黄昏工业废墟，暖金逆光、冷灰阴影、浓烟与火光，粗粝胶片质感，强纵深、强冲击、快节奏的画面动作和带有微微颠簸的画面，整个环境充满了爆炸、枪声的战场背景音。呈现主角闯入战火的压迫感。01｜抵达 · 主角持枪抵达，捕捉军靴触地、屈膝落稳的瞬间。衣角被旋翼风掀起，尘土包围身体，背景仍是同一段破墙。02｜冲向沙袋 · 侧面中景，主角持枪冲向几步外的沙袋。前方墙面被击中，碎屑横飞，身体前倾、步伐迅猛，直升机在左后方尘幕中隐去。03｜进入战斗 · 侧面中景，主角在沙袋后，一手撑住袋沿。弹着点在外侧炸出砂尘，碎石掠过前景，捕捉身体刚刚收进掩体的紧迫瞬间。04｜探身开火 · 中近景，主角从同一沙袋边缘探出上身射击，短促枪口火光照亮侧脸。远处厂房闪出火力，近处扬尘喷溅，人物与枪身形成有力斜线。05｜火线压低 · 紧凑近景，承接射击，主角迅速收低身体，肩膀贴住沙袋。砂粒从头盔旁飞过，脸上汗水混着灰尘，眼神紧绷；背景爆闪照亮半边面孔。06｜近处爆炸 · 超宽低机位，沙袋外的废弃车辆爆炸，火焰、黑烟与土浪轰然升起。主角蜷低在前景，手臂护住头部，逆向飞散的碎屑构成全片冲击峰值。07｜烟中起身 · 侧面中景，承接爆炸，主角撑住沙袋起身，转向身后几步外的厂房门洞。烟尘卷过肩背，车辆仍在燃烧，火光勾亮他孤身一人的轮廓。08｜闪入门洞 · 从门洞内向外看，主角弯腰跨入，肩背贴住门侧墙壁，步枪收在身前。门外火星与砂尘掠过，冷暗室内与炽亮战场形成强烈反差。09｜门边反击 · 中近景，承接贴墙姿态，主角从门框边侧身开火。枪口闪光撕开昏暗，映亮汗尘覆盖的脸；门外浓烟与火光翻涌，以孤身迎战的动作收尾"
    },
    {
      "type": "refer_image",
      "url": "https://p1-kling.klingai.com/kcdn/cdn-kcdn112452/tutorials/kling-image-4-0/api-examples-20261110/ref_6124598575989755167.png",
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

### 6.5 场景组图

参考核心场景资产，生成同一视觉风格下的不同场景。描述需要扩展的场景，并说明要保持一致的美术风格、建筑语言和色调。

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

<div class="guide-case-media-list guide-case-media-list-full">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-038.88f33daa1b898127.webp" alt="" loading="lazy" /></div>

<p>参考图</p>
</div>
</div>

```text
参考 @campus_style 中的画面艺术设计风格，生成六张不同的校园场景图，依次为教室、走廊、学校大门、操场、楼梯间、学校天台。保持统一的画面艺术设计风格、建筑语言和色调，每张都是单张场景图，不拼图。
```

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<div class="guide-case-media-list guide-case-media-list-thirds" style="--shot-ratio: 1.778">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-039.b4be0c7155b307c6.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-040.8a00164e9026f458.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-041.b664b616b346ab79.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-042.53a5808fc688927f.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-043.040bcad9e13da621.webp" alt="" loading="lazy" /></div>

</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-044.575b94aa2a594b5c.webp" alt="" loading="lazy" /></div>

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
      "text": "参考 @campus_style 中的画面艺术设计风格，生成六张不同的校园场景图，依次为教室、走廊、学校大门、操场、楼梯间、学校天台。保持统一的画面艺术设计风格、建筑语言和色调，每张都是单张场景图，不拼图。"
    },
    {
      "type": "refer_image",
      "url": "https://p1-kling.klingai.com/kcdn/cdn-kcdn112452/tutorials/kling-image-4-0/api-examples-20261110/campus_style.png",
      "id": "campus_style"
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

### 6.6 商品组图

围绕同一商品生成不同角度、细节和使用场景的成套图片。逐张说明展示内容，并保持商品的形状、颜色、结构、Logo 和包装标识一致。

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

### 6.7 文字排版与海报

支持在图片中生成文字及排版，可用于海报、封面和品牌视觉。直接给出需要呈现的文案，并说明文字的层级、位置、字形和颜色。

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

### 6.8 字体设置

支持在图片中指定字体。将字体名称写在对应文案旁，例如“字体为：长风手书体”，并说明文字位置和排版要求。当前模型支持的字体清单见：[字体清单](https://docs.qingque.cn/d/home/eZQBi9wz9wFtSbAdf1PP-WMjL?identityId=2V7wEGHyc5r)。

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

```text
生成一组四页的儿童连环画，讲述小狐狸寻找春天的故事。每页是一张独立的完整画面，不拼图、不使用四宫格。全套采用温暖清新的水彩童书插画风格，色调柔和，画面简洁，四页中的小狐狸始终保持橘红色毛发、白色胸口、绿色围巾和小挎包。每页底部留出清晰的故事概要区，文字不要遮挡主体，四页概要均使用同一种字体，字体为：长风手书体。
第1页：早晨，小狐狸背着小挎包站在森林路口，望着远处的小山和嫩绿色树芽。页底文字：“小狐狸出发了，它想找到春天。”
第2页：小狐狸蹲在溪水旁，观察石头边刚刚冒出的嫩芽，阳光映在水面上。页底文字：“溪水唱着歌，嫩芽探出了头。”
第3页：小狐狸走过开满小花的草地，一只蝴蝶在它鼻尖前飞舞，小狐狸露出惊喜的表情。页底文字：“花开了，蝴蝶也来迎接它。”
第4页：小狐狸坐在盛开的树下，与小兔一起分享野餐，远处的森林明亮而温暖。页底文字：“原来，春天就在我们的身边。”
```

<p class="guide-case-note">仅提示词，无参考图。</p>

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<div class="guide-case-media-list" style="--shot-ratio: 0.743">
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-049.0ba27a22e1e35810.webp" alt="" loading="lazy" /></div>

<p>第 1 页</p>
</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-050.15a01d58fd4d9265.webp" alt="" loading="lazy" /></div>

<p>第 2 页</p>
</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-051.bec42b08f07429ef.webp" alt="" loading="lazy" /></div>

<p>第 3 页</p>
</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap guide-image"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/image4-manual-zh-052.feca656cf1d52a35.webp" alt="" loading="lazy" /></div>

<p>第 4 页</p>

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
      "text": "生成一组四页的儿童连环画，讲述小狐狸寻找春天的故事。每页是一张独立的完整画面，不拼图、不使用四宫格。全套采用温暖清新的水彩童书插画风格，色调柔和，画面简洁，四页中的小狐狸始终保持橘红色毛发、白色胸口、绿色围巾和小挎包。每页底部留出清晰的故事概要区，文字不要遮挡主体，四页概要均使用同一种字体，字体为：长风手书体。\n第1页：早晨，小狐狸背着小挎包站在森林路口，望着远处的小山和嫩绿色树芽。页底文字：“小狐狸出发了，它想找到春天。”\n第2页：小狐狸蹲在溪水旁，观察石头边刚刚冒出的嫩芽，阳光映在水面上。页底文字：“溪水唱着歌，嫩芽探出了头。”\n第3页：小狐狸走过开满小花的草地，一只蝴蝶在它鼻尖前飞舞，小狐狸露出惊喜的表情。页底文字：“花开了，蝴蝶也来迎接它。”\n第4页：小狐狸坐在盛开的树下，与小兔一起分享野餐，远处的森林明亮而温暖。页底文字：“原来，春天就在我们的身边。”"
    }
  ],
  "settings": {
    "result_type": "series",
    "series_amount": 4,
    "resolution": "2k",
    "aspect_ratio": "3:4"
  }
}'
```

### 6.9 风格、配色与画面处理

根据参考图调整画面的风格、配色或质感。区分主体参考与风格参考，说明需要改变的效果，以及需要保留的主体特征。

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

### 6.10 电商详情长图

基于商品参考图生成完整的电商详情长图。提供页面语言、商品卖点和内容模块，并保持商品外观与标识一致。

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

### 6.11 网页设计长图

根据页面用途、品牌风格和内容结构生成完整的网页设计长图。输出为图片，不包含网页代码或交互功能。

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

## 7 自定义图片输出规格

以下JSON是配置片段，不是完整可调用请求。请与contents合并，并使用对应创建接口。

### 7.1 分辨率

| 任务          | 枚举         | 默认 | 说明                           |
| ------------- | ------------ | ---- | ------------------------------ |
| 普通图/组图   | 2k / 4k / 8k | 2k   | 原生图片档位，不是逐张指定像素 |
| 电商/网页长图 | 1k / 2k      | 1k   | 不支持4k或8k                   |

```json
{
    "settings": {
        "result_type": "single",
        "n": 1,
        "resolution": "8k",
        "aspect_ratio": "3:4"
    }
}
```

resolution 指定图片清晰度档位，不用于设置任意宽度或高度；请结合 aspect_ratio 配置画面比例。

### 7.2 宽高比

| 用途        | 可选值                                          |
| ----------- | ----------------------------------------------- |
| 普通图/组图 | auto、16:9、9:16、1:1、4:3、3:4、3:2、2:3、21:9 |
| 长图        | 依技能生成页面，不使用普通图aspect_ratio字段    |

auto根据传入内容智能选择。强制某个受支持比例时，参数与提示词意图保持一致；不支持4:7等任意固定比值。

### 7.3 单图张数与组图张数

```json
{
    "settings": {
        "result_type": "single",
        "n": 3,
        "resolution": "2k",
        "aspect_ratio": "auto"
    }
}
```

上例生成3张独立图片，不代表3张连续叙事。关联组图使用下面的配置，数量为2—10或auto；auto根据内容决定张数，并占用与实际张数对应的并发量。

```json
{
    "settings": {
        "result_type": "series",
        "series_amount": 6,
        "resolution": "2k",
        "aspect_ratio": "16:9"
    }
}
```

### 7.4 长图技能与长度

| skill     | length         | 含义                         |
| --------- | -------------- | ---------------------------- |
| ecommerce | short          | 约2—5个内容模块，最终1张图   |
| ecommerce | medium（默认） | 约6—10个内容模块，最终1张图  |
| ecommerce | long           | 约11—18个内容模块，最终1张图 |
| webpage   | 不支持         | 设置无效，不传此字段         |

```json
{
    "settings": {
        "skill": "ecommerce",
        "length": "medium",
        "resolution": "2k"
    }
}
```

### 7.5 水印与通用配置

options.watermark_info.enabled控制是否同时生成含水印结果；watermark_url按配置返回。options.callback_url指定回调，options.external_task_id为用户自定义唯一任务ID，不覆盖系统`data.id`。具体协议与可选字段详见API说明。

```json
{
    "options": {
        "watermark_info": {
            "enabled": true
        }
    }
}
```

## 8 提示词技巧与写作建议

### 8.1 基础写作

使用“主体＋动作/状态＋环境＋构图＋光线/风格”。主体决定画什么，动作提供瞬间，环境建立空间，构图与光线决定怎么呈现。先写重要信息，再补可见细节，避免所有信息权重相同。

### 8.2 结构化提示词

复杂图片可按目标风格、主体与保留特征、材质、光影、构图、文字与限制分段；长提示词不是越长越好，重复和矛盾会干扰控制。

| 段落       | 建议说明                                 |
| ---------- | ---------------------------------------- |
| 目标风格   | 明确摄影/插画/版画等流派，避免只写高级感 |
| 主体与保留 | 人物身份、商品结构、服饰关键点           |
| 画面       | 动作、场景、空间关系和景别               |
| 材质/光照  | 具体纹理、光源方向、明暗关系             |
| 文字/排版  | 逐字文案、字体特征、大小层级与位置       |
| 限制       | 不拼图、无额外人物、不改变商品标识等     |

### 8.3 参考类任务与多素材映射

给每张图独立ID，并显式定义用途。‘参考@style的配色，主体来自@person’比‘参考这两张图’明确；不需要继承的角色、背景、服装也应说明。未显式引用的素材仍生效，不要添加与目标无关的图。

### 8.4 图片修改与保留范围

通过参考图与提示词描述希望修改和保留的内容。分别说明人物身份、服饰、背景和风格的要求，减少相互冲突的描述。参考图创作会重新生成画面，不保证对原图进行像素级无损编辑。

### 8.5 组图与逐张静帧

先写总张数与整套风格，再编号描述每张画面，最后列出一致性约束。将连续情节拆成每张图片能够呈现的静态瞬间。多视图排在同一页时使用 single，多张独立画面使用 series。

### 8.6 负向控制

将不希望出现的内容直接写入提示词，例如不拼图、不增加其他人物、不改变 Logo、不要让文字覆盖面部。避免大量宽泛描述；负向要求与正向描述冲突时，应先消除矛盾。

### 8.7 进阶写作

用明确视觉参考替代泛化风格：例如瑞士国际主义网格强调对齐和阅读顺序，复古手工版画强调刀痕与油墨，冷光时尚编辑摄影强调材料、轮廓和克制留白。商品和演示页的价格、规格、工艺数字与品牌故事需核实，不能因为生成了文字就当作真实事实。

## 9 使用限制

### 9.1 参考素材

| 项目           | 要求                                                                          |
| -------------- | ----------------------------------------------------------------------------- |
| 图片格式       | JPG、JPEG、PNG                                                                |
| 单图体积       | 不超过30MB                                                                    |
| 输入宽高       | 宽和高均≥300px                                                                |
| 输入比例       | 2:5—5:2                                                                       |
| 普通图素材数量 | 参考图与通过图片定制的主体合计≤10                                             |
| 长图素材数量   | 生成电商详情页必须提供1—3张图，网页设计可以输入一张风格参考图和一张主体参考图 |
| URL与ID        | URL必须公开可访问或有效Base64；任务内ID唯一                                   |

### 9.2 提示词与输出边界

提示词长度按英文与非英文字符分别计算。单图/组图生成：纯英文不超过 50,000 字符，纯非英文不超过 21,000 字符；混合输入需满足：英文字符数/50000 + 非英文字符数/21000 ≤ 1。长图生成：纯英文不超过 166,000 字符，纯非英文不超过 71,000 字符；混合输入需满足：英文字符数/166000 + 非英文字符数/71000 ≤ 1。文字呈现效果受语种、字体、字形、文字密度和布局影响，生成后需检查准确性与可读性。长图仅支持 1k、2k，且每次输出一张完整图片；

单图的多格排版不等于独立组图，输入素材数量也不等于输出图片数量。独立图片张数由 n 指定，关联组图张数由 series_amount 指定；输出结果以任务查询返回为准。

## 10 常见问题

### 10.1 素材与能力

| 问题                           | 说明                                                                                          |
| ------------------------------ | --------------------------------------------------------------------------------------------- |
| 没有参考图能生成吗？           | 普通图片可以，仅传prompt；电商长图必须有商品图。                                              |
| 文生图与图生图要用不同接口吗？ | 普通图共用image-generation，通过contents区分输入。                                            |
| 为什么三视图不是series？       | 若多个视角在同一张设定页中，就是single；多名角色各一页才是series。                            |
| 为什么填n没有改变组图张数？    | series下n无效，应设置series_amount。                                                          |
| 长图的long是不是多张？         | 不是，最终仍1张，long表示约11—18个内容模块。                                                  |
| 能返回HTML或PPTX吗？           | 不能，网页与演示页都是图片，需要另行开发或制作文件。                                          |
| 字体怎么选？                   | 在 prompt 中补充“字体为：XXX体”，例如“字体为：长风手书体”。支持的字体清单见第 6.8 节。        |
| 有精确像素表吗？               | 通过 resolution 选择清晰度档位，通过 aspect_ratio 选择比例；当前 API 不提供任意宽高像素配置。 |

### 10.2 提示词与结果优化

| 现象                 | 优先检查                                               |
| -------------------- | ------------------------------------------------------ |
| 角色或服装不一致     | 素材职责、引用ID和保留项是否明确，是否有矛盾外貌描述   |
| 文字不正确或小字难读 | 文案是否逐字给出，内容是否过密，字体装饰是否影响辨识   |
| 组图变成拼贴         | 是否明确每张独立画面、不拼图，并选择series             |
| 比例与预期不同       | 是否选择合法枚举，参数与prompt是否冲突                 |
| 商品细节或卖点偏差   | 参考图是否清晰，产品事实是否明确，生成文案是否人工核实 |
| 参考链接无法使用     | 不要传内网签名链接，检查公网可访问性、规格和有效期     |
