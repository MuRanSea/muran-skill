<!-- Official source: https://klingai.com/document-api/api/usage-guide/kling-4-0.md -->
<!-- Source SHA-256: aaf52dbcd401d3c7e29b12d47752729d26715e71f59db8dc21c1432082a1ccba -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://klingai.com/document-api/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling 4.0 视频使用手册

> 来源: https://klingai.com/document-api/api/usage-guide/kling-4-0
> 语言: zh
> 当前 Tab: Kling 4.0 视频使用手册
> 此内容为面向 LLM 优化的 Markdown，已展开页面内 Tab，并省略页面目录、复制按钮等 UI 控件。

::: info-box

Kling 4.0 是原生多模态视频创作模型，支持最长 30 秒原生生成、全能参考和最多 10 张关键帧输入，具备更稳定的复杂动态表现、更强的全能参考一致性，以及更完整连贯、精准可控的叙事能力，让创作者能够将创作构思与多元素材高效转化为完整、可控的视频成片。可用于影视、短剧、游戏、动画、广告及 MV 等创作场景。

本文介绍 Kling 4.0 的模型能力、API任务使用方法、素材要求和提示词写作方法，帮助您从创意描述与参考素材开始，完成视频生成和编辑。

## 1 模型调用条件

调用 Kling 4.0 模型前，请确保您满足以下任一条件：

- 购买旗舰版资源包（[前往购买](https://klingai.com/dev/pricing?scrollTo=video-package)）
- 账户现金余额 > 0元，可留咨沟通充值（[前往留咨](#business-consult)）

## 2 使用前必读

### 2.1 任务类型与限制

Kling 4.0 在创作端提供“全能参考”和“关键帧”两个一级入口。全能参考为默认入口，适合组合素材、参考已有内容或从一句创意开始；关键帧入口用于定义指定时刻的画面节点。在API侧，提供3个API 接口，全能参考、图生视频和文生视频；

| **对比项**          | **全能参考**                               | **图生视频**                               | **文生视频**                     |
| ------------------- | ------------------------------------------ | ------------------------------------------ | -------------------------------- |
| 适用情况            | 有图像、视频等素材需要参考，或仅有创意方向 | 画面节点已经确定，需要控制其在成片中的呈现 | 仅有文本，需要生成视频的场景     |
| 控制对象            | 外观、风格、动作、镜头等生成内容           | 时间轴上指定节点的画面                     | 按照文本内容生成内容             |
| 处理方式            | 对用户指令进行意图分类与模型路由           | 不接入意图分类，输入指向同一链路           | 不接入意图分类，输入指向同一链路 |
| 可上传素材          | 文本、图片、视频、音色                     | 文本、图片                                 | 仅文本                           |
| 对应 API 接口及字段 | /omni-video/kling-4.0                      | /image-to-video/kling-4.0                  | /text-to-video/kling-4.0         |

全能参考入口可以完成文生视频、关键帧生视频、全能参考生视频等能力。

| **任务**       | **使用说明**                               | **能力边界**                                                           |
| -------------- | ------------------------------------------ | ---------------------------------------------------------------------- |
| 文生视频       | 通过文字描述主体和希望发生的事件           | 文本不超过 8000 tokens                                                 |
| 全能参考生视频 | 组合不同素材，明确各素材的职责             | 图片、视频、音色、主体合计最多 15 个                                   |
| 视频编辑       | 明确指定待编辑视频、修改对象与保留范围     | 最多输入 5 段视频，其中 1 段为主视频；单段 3–30 秒，总时长不超过 30 秒 |
| 关键帧生视频   | 使用首帧、尾帧、首尾帧或中间帧定义画面节点 | 最多 10 张图片；关键帧独立入口不支持另传参考素材                       |

### 2.2 配置方法

#### 全能参考

通过图片、视频、主体或音色提供参考信息，生成视频。不同素材可分别用于指定人物外观、动作、运镜、场景或声音。对于全能参考生成类任务，推荐按以下方式配置：

- 调用 /omni-video/kling-4.0 接口。
- 在 contents 中添加 type 为 prompt 的对象，将提示词填写到 text。
- 根据素材用途，添加对应的输入对象：
    - **图片参考**：type 设置为 refer_image，通过 url 传入图片。
    - **动作、运镜等视频参考**：type 设置为 feature_video，通过 url 传入视频。
    - **主体参考**：type 设置为 element，通过 element_id 指定主体。
    - **音色参考**：type 设置为 voice，通过 voice_id 指定音色。
- 为素材设置本次任务内不重复的 id，在提示词中通过 @id 指定各素材的作用。例如，id 为 image_1 的图片，在提示词中写作 @image_1。
- 根据输出要求设置 settings：resolution 支持 720p、1080p，默认 1080p。aspect_ratio 支持 21:9、16:9、9:16、1:1、adaptive，默认 adaptive。若传入adaptive 时，模型会识别并遵循 Prompt 中的比例意图。duration 支持 **3–30 秒的整数**，未传入时优先识别 Prompt 中的时长意图，无明确意图时采用 base_video的时长，未提供 base_video 时，默认 **10 秒**。

**提示词示例：**

> 参考 @video_1 的运镜轨迹与镜头节奏，主体使用 @image_1 中的汽车，背景使用 @image_2 中的街道。仅参考视频的运镜，不沿用其中的人物和场景。

说明：可灵通过接口路径及 contents 中的素材类型表达输入用途。如希望参考视频中的运镜、动作或风格等特征生成新视频，应使用 feature_video；若希望对原视频进行内容增加、删除、修改，或调整背景、风格等，应使用 base_video指定待编辑视频，并在 Prompt 中说明需要修改和保留的内容。具体示例可参考第 6 章和[Kling 4.0 视频 提示词案例](https://klingai.com/document-api/api/usage-guide/kling-4-0-prompt-guide#1-提示词案例)。

#### 视频编辑

对已有视频进行定向修改，例如增加、替换或删除主体，修改人物、背景或视觉风格。

对于明确的视频编辑类任务，推荐按以下方式配置：

- 调用 /omni-video/kling-4.0 接口。
- 在 contents 中添加 **一个** type 为 base_video 的对象，通过 url 传入待编辑视频，并设置 id，例如 video_1。
- 如需提供替换对象、目标风格或其他参考信息，可继续添加 refer_image、element 等对应类型的素材。
- 在 type 为 prompt 的对象中，通过 text 明确说明：**编辑哪个视频、修改什么、保留什么**。
- 按当前接口支持范围配置输出参数。settings.duration 支持 **3–30 秒的整数**。

**提示词示例：**

> 编辑 @video_1，将视频中的人物替换为 @image_1 中的人物，保持原视频的动作、构图和镜头运动，其余保持不变。

说明：每次请求最多包含一个 base_video。参考视频、待编辑视频与视频角色主体共用视频数量和时长额度，合计最多 **5 段、30 秒**。

#### 首帧、尾帧与多关键帧生视频

使用图片定义视频的起始画面、结束画面或中间画面节点，并通过提示词描述节点之间的动作与过渡。

对于仅使用图片关键帧的任务，推荐按以下方式配置：

- 调用 /image-to-video/kling-4.0 接口。
- 在 contents 中，根据图片的用途设置 type：
    - **首帧**：first_frame。
    - **尾帧**：last_frame。
    - **中间帧**：middle_frame。
- 通过各对象的 url 传入图片，并设置不重复的 id，便于在提示词中引用。图片合计最多 **10 张**。
- 在 type 为 prompt 的对象中，使用 text 描述画面内容、动作过程和节点之间的衔接。
- 通过 settings.duration 设置 **3–30 秒**的整数时长，通过 settings.resolution 选择 720p 或 1080p。专用图生接口当前未提供独立的 aspect_ratio 字段，不要额外传入。

**首尾帧提示词示例：**

> @start 为首帧，@end 为尾帧。生成15秒的视频，展示铁匠将原料锻造成成品的过程，采用真实纪录片风格，最终画面与尾帧一致。

说明：如果除了关键帧，还需要输入动作参考视频、主体或音色，应使用 /omni-video/kling-4.0 接口，并按对应素材类型配置。不能向专用图生接口直接添加这些参考类型。

### 2.3 报错机制

视频生成采用异步任务机制，报错分为以下两种情况：

• **同步报错（提交任务时）**：创建接口直接返回错误。请根据响应中的 code 和 message 排查，修正后重新提交，[错误码详情](https://klingai.com/document-api/api/get-started/error-codes)。

• **异步报错（任务创建后）**：已获得任务 ID，但查询到任务状态为 failed。请查看该任务的返回 message，了解失败原因。

**获得任务 ID 仅表示任务已创建；任务状态为 succeeded 才表示生成成功。** 等待期间请查询原任务，不要重复提交创建任务。

## 3 新手入门

本节面向第一次调用可灵 API 的用户。你将通过 **准备 API Key → 创建任务 → 查询状态 → 获取视频** 四个步骤，生成一段 5 秒的视频。整个过程无需安装 SDK、配置 Python 环境或下载示例包，也无需提前准备图片、视频素材。如果你已经非常熟悉可灵API的调用，可跳过本章节，直接参考后续章节的丰富示例。如果希望先体验视频生成效果，可以使用平台已有的在线体验功能。

**使用说明：** 本教程分别提供 macOS 和 Windows 的命令示例。本文所有示例均使用 Bash 语法，并通过 cURL 调用 API。每一步只需执行与你的操作系统对应的代码，并始终在同一个终端窗口中完成操作。

##### 第一步：准备账号与 API Key

开始前，请完成以下准备：

- **登录开发者平台**：访问 [可灵 AI 开发者平台](https://klingai.com/dev)，登录账号。
- **准备 API 资源**：前往 [资源包页面](https://klingai.com/dev/pricing?scrollTo=video-package)，选择适合的视频生成 API 资源包。首次联调可查看页面是否提供试用资源。
- **获取 API Key**：进入 [开发者控制台](https://klingai.com/dev/api-key)，点击「新建 API Key」，创建并妥善保存密钥。

账号、资源包及鉴权步骤依据[可灵快速入门文档](https://klingai.com/document-api/guides/get-started/quick-start)。请确保账号具有 Kling 4.0 模型的调用权限及足够的可用额度。本教程将创建真实的视频生成任务，并按照平台计费规则扣费。准备好 API Key 后，根据操作系统打开终端并执行以下命令。

**macOS**

按 Command + 空格，搜索并打开「终端」（Terminal），输入以下命令并按回车，进入 Bash：

```bash
bash
```

**Windows**

前往 Git for Windows 官网，下载并安装 Git for Windows，其中包含 Git Bash。

安装完成后，从开始菜单打开 Git Bash。后续所有命令都在这个 Git Bash 窗口中运行，请勿使用 PowerShell 或命令提示符（CMD）。

**配置 API Key**

以下命令适用于 macOS 的 Bash 和 Windows 的 Git Bash。请在刚才打开的窗口中执行：

```bash
read -r -s -p "请输入 API Key，按回车确认：" KLING_API_KEY
printf '\n'
export KLING_API_KEY
```

出现提示后，粘贴 API Key 并按回车。输入过程中不会显示字符，这是正常现象。

API Key 仅在当前终端会话中生效。请保持此窗口打开，并在同一窗口中继续完成创建任务、查询状态和获取视频等操作。关闭窗口后，需要重新打开 Bash 或 Git Bash 并配置 API Key。请勿向他人分享 API Key。

后续步骤在两个操作系统中使用相同命令，无需切换代码版本。本教程统一使用北京区域 API 地址 https://api-beijing.klingai.com。如果使用海外区域，请替换为对应区域的API 地址，并确保创建任务和查询任务使用同一区域。

##### 第二步：创建视频任务

在刚才的终端窗口中，复制并运行以下命令，创建一个文生视频任务。

首次体验可直接使用示例内容，无需修改提示词或其他参数。

```cURL
curl -sS --request POST \
  'https://api-beijing.klingai.com/text-to-video/kling-4.0' \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data-raw '{
    "prompt": "清晨的海边，一只白色海鸥掠过海面，镜头缓慢推进，传来自然的海浪声。",
    "settings": {
      "duration": 5,
      "resolution": "720p",
      "aspect_ratio": "16:9"
    }
  }'
```

**参数说明**

| 参数                  | 本示例取值         | 作用                   |
| --------------------- | ------------------ | ---------------------- |
| prompt                | 海边海鸥的场景描述 | 描述希望生成的视频内容 |
| settings.duration     | 5                  | 生成 5 秒视频          |
| settings.resolution   | "720p"             | 输出 720p 清晰度       |
| settings.aspect_ratio | "16:9"             | 输出横屏视频           |

创建成功后，终端将返回 JSON 响应，示例如下：

```json
{
    "code": 0,
    "message": "SUCCEED",
    "request_id": "1ceedbc3-55b4-4e3d-926f-6964422f5962",
    "data": {
        "id": "943539593730219878",
        "status": "submitted",
        "message": "",
        "create_time": 1792993723982,
        "update_time": 1792993723982
    }
}
```

以上为响应结构示例，任务 ID、请求 ID 和时间戳以实际返回结果为准。

**重点关注以下两个字段：**

- code：返回 0 表示创建请求成功。
- data.id：系统分配的任务 ID，用于后续查询生成进度。

请**复制并保存 data.id 的值**，下一步需要使用。注意不要将 request_id 误认为任务 ID。

创建任务成功并不代表视频已经生成完成。此时任务可能仍在排队或处理中，暂时没有视频下载链接属于正常情况。

如果创建失败，请先根据接口返回的错误码排查问题，不要继续后续步骤。

##### 第三步：查询任务状态

视频生成需要一定时间。创建任务后，可以通过任务 ID 查询生成进度。

仍在刚才的终端窗口中，复制并执行以下命令。根据提示输入第二步返回的任务 ID，按回车确认。

```bash
printf '请输入任务 ID，按回车确认：'
read -r KLING_TASK_ID

curl -sS --request GET \
  "https://api-beijing.klingai.com/tasks?task_ids=${KLING_TASK_ID}" \
  --header "Authorization: Bearer ${KLING_API_KEY}"
```

查询成功后，接口返回的 data 是任务信息数组。找到 id 与当前任务 ID 一致的对象，查看其中的 status 字段。

**任务状态说明**

| status     | 状态说明             | 下一步操作             |
| ---------- | -------------------- | ---------------------- |
| submitted  | 任务已提交，等待处理 | 稍后重新查询           |
| processing | 视频正在生成         | 稍后重新查询           |
| succeeded  | 视频生成成功         | 进入第四步             |
| failed     | 视频生成失败         | 查看任务返回的错误信息 |

例如，任务仍在生成时，可能返回：

```json
{
    "code": 0,
    "message": "SUCCEED",
    "data": [
        {
            "id": "943539593730219878",
            "status": "processing",
            "message": ""
        }
    ]
}
```

以上仅展示关键字段，实际响应可能包含其他信息，具体查看API文档。

如果任务尚未完成，建议约 **1分钟后重新执行本步骤**，使用同一个任务 ID 查询。

##### 第四步：获取视频

当任务状态变为 succeeded，表示视频已生成成功。

此时，查询响应中的 outputs 将包含生成结果。找到 type 为 video 的对象，读取其中的 url 字段。

成功响应示例（仅展示关键字段）：

```json
{
    "code": 0,
    "message": "SUCCEED",
    "data": [
        {
            "id": "943539593730219878",
            "status": "succeeded",
            "outputs": [
                {
                    "type": "video",
                    "url": "https://example.com/generated-video.mp4"
                }
            ]
        }
    ]
}
```

以上 URL 仅为示意地址，不能用于下载实际生成结果。

**查看或下载视频：**

- 复制实际响应中 outputs 对应的完整 url，不包含两侧双引号。
- 将 URL 粘贴到浏览器地址栏并打开。
- 查看生成的视频，并将其下载保存到本地。

**注意：** 视频下载链接具有有效期，请在生成成功后及时下载，并保存到自己的存储空间。如果链接失效，可重新查询任务，确认接口是否返回可用的下载地址。

**恭喜，你已完成第一次可灵 API 调用！**

通过以上四步，你已经成功创建视频生成任务、查询生成状态，并获取生成结果。

接下来，你可以尝试：

- 修改 prompt，生成不同场景的视频。
- 根据模型支持的参数范围，调整视频时长、清晰度和画幅比例。
- 使用图片或其他参考素材，体验更多视频生成能力。

如需更多示例，请查看第6章节和[Kling 4.0 视频 提示词案例](https://klingai.com/document-api/api/usage-guide/kling-4-0-prompt-guide#1-提示词案例)。当然也可以在准备自己的提示词和参考素材后，可参考本文第 2 章确定任务方式，按第 8 章声明素材职责，并参考[Kling 4.0 视频 提示词案例](https://klingai.com/document-api/api/usage-guide/kling-4-0-prompt-guide#1-提示词案例)的提示词模板，准备生成

## 4 Kling4.0最新能力

### 4.1 视听表现

1. Kling 4.0 提升了大幅度动态、连续动作与复杂运镜的稳定性，支持高品质音频和双通道立体声，使声音、对白与表演更自然地同步。
1. 支持 21:9 超宽画幅。
1. 1080p、4K 的 10-bit HDR 输出【即将上线】。

### 4.2 全能参考

单次任务可组合图片、视频、主体与音色等最多 15 项参考素材。其中图片最多 10 张、视频最多 5 段且总时长不超过 30 秒、主体最多 7 个且视频主体最多 3 个。不同参考可分别提供角色外观、动作、镜头、场景或声音信息。

### 4.3 长叙事与关键帧

单次原生生成最长 30 秒，支持长镜头和连续叙事。最多输入 10 张关键帧，通过预设画面节点控制人物状态、场景变化与情节推进。提示词长度上限提升至 8000 tokens。

### 4.4 多语种与多元风格

支持中文、英语、日语、韩语、西班牙语、葡萄牙语、德语、法语、印地语等语言，以及多种口音与方言。画面文字支持上述多语种、Emoji 和 Logo。视觉风格覆盖电影感影像、复古 DV、动画、毛毡、奇幻、赛博等。

### 4.5 Kling 4.0 Flash【即将上线】

Kling 4.0 Flash 面向高频创意尝试和短视频创作，单次生成最长 20 秒，最高支持 720p，暂不支持首尾帧及多关键帧。

### 4.6 视频续拍【即将上线】

上传视频后支持多次续拍，最长可延展至 2 分钟。

## 5 能力概述

### 5.1 模型与输出规格

| **功能/参数项** | **Kling 4.0**                                | **Kling 4.0 flash（即将上线）**              |
| --------------- | -------------------------------------------- | -------------------------------------------- |
| 一级入口        | 全能参考 / 关键帧 / 长视频                   | 全能参考 / 关键帧                            |
| 生成时长        | 3-30s                                        | 3-20s                                        |
| 生成模式        | 720p / 1080p / 4K / 4K HDR（即将上线）       | 720p                                         |
| 首尾帧          | 支持                                         | 不支持                                       |
| 多关键帧        | 支持                                         | 不支持                                       |
| 音色克隆        | 支持                                         | 不支持                                       |
| 主体绑定音色    | 支持                                         | 不支持                                       |
| 输入视频        | 单个视频时长：3-30s<br>视频合计总时长：3-30s | 单个视频时长：3-20s<br>视频合计总时长：3-20s |

### 5.2 全能参考典型能力清单

::: container guide-capability-table

| **任务类型** | **能力**                   | **使用方式**                                                 |
| ------------ | -------------------------- | ------------------------------------------------------------ |
| 参考生视频   | 人物与多角色参考           | 声明每张图片对应的人物，以及需要保持的面孔、发型、服装等特征 |
| 参考生视频   | 动作参考                   | 从参考视频提取动作与节奏，角色造型来自指定图片               |
| 参考生视频   | 运镜参考                   | 从参考视频提取镜头轨迹与节奏，另行指定主体和场景             |
| 参考生视频   | 构图参考                   | 明确需要保持哪张图片的构图                                   |
| 参考生视频   | 分镜表参考                 | 用图片提供角色设计、镜头顺序、取景与摄影机路径等信息         |
| 参考生视频   | 音色参考                   | 指定说话人的音色；不支持上传背景音乐或音效                   |
| 编辑视频     | 增加、替换、删除元素       | 明确待编辑视频、修改对象和保留范围                           |
| 编辑视频     | 风格修改                   | 用文字或图片指定新风格，写明需要保留的构图、动作和事件顺序   |
| 关键帧       | 首帧、尾帧、首尾帧、中间帧 | 定义关键画面节点，补充动作和过渡                             |
| 延长视频     | 视频续拍                   | 即将上线；                                                   |

## 6 特色能力与使用方法

### 6.1 简短指令生成

只有一句创意也可以开始。写出主体和希望发生的事件，模型可扩写简单指令，补全剧情、场景调度与运镜；描述足够清晰时，则按已有描述执行。

::::: container guide-case guide-case-brief

:::: container guide-case-input

<p class="guide-case-label">输入</p>

::: container guide-case-brief-body

An old man ranting about AI.

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<button type="button" class="guide-video-poster" data-src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-v-001.6de5a1824460045b.mp4" aria-label="播放视频"><img src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-p-001.c462a6306eed11fb.52407e68998db5f0.webp" alt="" /></button>

API 代码示例：

```cURL
curl --request POST \
  'https://api-beijing.klingai.com/text-to-video/kling-4.0' \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "prompt": "An old man ranting about AI.",
  "settings": {
    "duration": 15,
    "resolution": "1080p",
    "aspect_ratio": "16:9"
  }
}'
```

### 6.2 多模态参考

人物外观、动作、镜头、空间关系与音色可以来自不同素材。提示词需要说明每份素材提供什么，以及最终如何组合。

| **参考维度** | **写法**                                                                      |
| ------------ | ----------------------------------------------------------------------------- |
| 动作参考     | 参考 @视频1 的打斗动作与出招节奏，角色造型来自 @图片1 @图片2                  |
| 运镜参考     | 参考 @视频1 的运镜轨迹与镜头节奏，主体替换为 @图片1 的汽车，背景替换为 @图片2 |
| 构图参考     | 参考 @图片1 的构图，严格保持                                                  |

构图参考

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

<div class="guide-case-media-list">
<div class="guide-case-shot">

<div class="media-wrap image-wrap"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-i-001.d2290b254ab70b73.716123ce14ad28fd.webp" alt="" /></div>

<p>图片1</p>
</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-i-002.53b2476ca1d709df.88f4fd138387376a.webp" alt="" /></div>

<p>图片2</p>
</div>
</div>

```text
镜头1:5s。参考图片1 中的构图，生成一个月明星稀的夜晚，白色散发着月光的巨大的莲花，散发星星点点的白光和金点光，在天空中盛开，并占了画面大部分，一个身穿白色古装、外披金色纱衣的绝色美人，抬手看着远处的巨大莲花，风吹过，吹起她的裙摆，她有两根白色又细又长的发带，随风飞舞，黑色瀑布般的长发，她的身体被月光照耀着镶着一层银白色的光边，就像仙女一样。这朵巨大莲花就像是巨大月亮一样的存在，莲花虽大，但看起来距离人物是远的，人物更小，但是距离镜头更近，能感受到明显的景深差距，构图差距，图1中人物的头发、发带、衣服随风飘荡着，人物的飘动非常自然、真实，摆动。仙气十足，空中的莲花微微颤动像是在呼吸，每片叶子上下浮动，有流着点点星光的水流慢慢的、细水长流的、轻轻的从每一片叶片上留下来，金色光点慢慢的来回移动，莲花在一呼一吸的发光，镜头向右平移，但人物不动，景深变化，莲花可以看出由于镜头变化而微微改动。

镜头2:5s。参考图片2中的花和人物姿势的构图，生成一个月明星稀的夜晚，一朵巨大的墨色莲花盛开在一个水面上，莲花中心空出一片区域，足够躺着一个身穿浅淡青色衣服的绝色美女，她悠闲地姿势，翘着二郎腿，动作舒畅惬意，双手交叠在脑后，像是在小憩打盹，莲花看起来顺着河流在飘，巨大的莲花几乎充满画面，莲花本身散发着光芒、光芒照应在画面上，莲花中心光照着有近乎透明的美感，镀上一点白色的边，还有一点金色散发着，视觉主体是黑色绝美的莲花，人物占画面比例不算大。从上往下垂直俯拍，画面聚集了星星点点的萤火虫，散在整个画面中，女人微微摇晃着，自在的摆手，风吹过她的裙摆、头发都在轻轻摆动，非常自然的动态效果，巨大的莲花散发着光芒，莲花的光芒一亮一暗像人的呼吸，金色的点点是萤火虫，萤火虫朝着相同方向慢慢飞动，水流在不断流动，莲花向画面左侧流动.镜头逐渐拉远。

背景音乐：古典、优雅、仙境一般的古筝和笛子的合奏，中国传统美感
```

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<button type="button" class="guide-video-poster" data-src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-v-002.37e480c081dbbd9e.mp4" aria-label="播放视频"><img src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-p-002.35243c43bb20c34c.2269bc05714ff6c5.webp" alt="" /></button>

```cURL
curl --request POST \
  'https://api-beijing.klingai.com/omni-video/kling-4.0' \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "镜头1:5s。参考@image_1 中的构图，生成一个月明星稀的夜晚，白色散发着月光的巨大的莲花，散发星星点点的白光和金点光，在天空中盛开，并占了画面大部分，一个身穿白色古装、外披金色纱衣的绝色美人，抬手看着远处的巨大莲花，风吹过，吹起她的裙摆，她有两根白色又细又长的发带，随风飞舞，黑色瀑布般的长发，她的身体被月光照耀着镶着一层银白色的光边，就像仙女一样。这朵巨大莲花就像是巨大月亮一样的存在，莲花虽大，但看起来距离人物是远的，人物更小，但是距离镜头更近，能感受到明显的景深差距，构图差距，@image_1中人物的头发、发带、衣服随风飘荡着，人物的飘动非常自然、真实，摆动。仙气十足，空中的莲花微微颤动像是在呼吸，每片叶子上下浮动，有流着点点星光的水流慢慢的、细水长流的、轻轻的从每一片叶片上留下来，金色光点慢慢的来回移动，莲花在一呼一吸的发光，镜头向右平移，但人物不动，景深变化，莲花可以看出由于镜头变化而微微改动。\n\n镜头2:5s。参考@image_2中的花和人物姿势的构图，生成一个月明星稀的夜晚，一朵巨大的墨色莲花盛开在一个水面上，莲花中心空出一片区域，足够躺着一个身穿浅淡青色衣服的绝色美女，她悠闲地姿势，翘着二郎腿，动作舒畅惬意，双手交叠在脑后，像是在小憩打盹，莲花看起来顺着河流在飘，巨大的莲花几乎充满画面，莲花本身散发着光芒、光芒照应在画面上，莲花中心光照着有近乎透明的美感，镀上一点白色的边，还有一点金色散发着，视觉主体是黑色绝美的莲花，人物占画面比例不算大。从上往下垂直俯拍，画面聚集了星星点点的萤火虫，散在整个画面中，女人微微摇晃着，自在的摆手，风吹过她的裙摆、头发都在轻轻摆动，非常自然的动态效果，巨大的莲花散发着光芒，莲花的光芒一亮一暗像人的呼吸，金色的点点是萤火虫，萤火虫朝着相同方向慢慢飞动，水流在不断流动，莲花向画面左侧流动.镜头逐渐拉远。\n\n背景音乐：古典、优雅、仙境一般的古筝和笛子的合奏，中国传统美感"
    },
    {
      "type": "refer_image",
      "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch6_2_lotus_distance_sketch.png",
      "id": "image_1"
    },
    {
      "type": "refer_image",
      "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch6_2_lotus_pose_sketch.png",
      "id": "image_2"
    }
  ],
  "settings": {
    "duration": 10,
    "resolution": "1080p",
    "aspect_ratio": "adaptive"
  }
}'
```

### 6.3 30 秒视频生成

Kling 4.0 支持单次生成 3–30 秒视频。智能分镜默认开启，模型根据内容组织镜头与节奏，适用于有完整故事线的短片和多镜头广告。

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

<div class="guide-case-media-list">
<div class="guide-case-shot">

<div class="media-wrap image-wrap"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-i-004.c065ed5143990b02.a9c8a5eb314afe33.webp" alt="" /></div>

<p>图片1</p>
</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap"><img src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-i-003.c556e087c9f65659.944d04f6a2baebd2.webp" alt="" /></div>

<p>图片2</p>
</div>
</div>

```text
1. SCENE CONTEXTEXACTLY 1 DRAGON — NO DUPLICATES.A 30-second, six-shot dark-fantasy action sequence. A colossal dragon roars, launches from a mountain pinnacle, accelerates toward a burning coastal city, dives between its towers and performs a devastating aerial fire attack. Epic scale, very fast pacing, real-time motion.2. ACTIVE REFERENCES

 controls the burning coastal city, Gothic architecture, harbour, mountain horizon, existing fires, smoke columns, storm clouds and lighting.

 controls the dragon’s identity, black-grey scales, red-brown wing membranes, horns, dorsal spines, four legs, two wings, long tail and opening rocky pinnacle.3. LOCATION MAPThe pinnacle overlooks the coastal city. The harbour lies screen-left, the central castle lies ahead, and the densest burning district lies centre-right. Direction of travel always runs from the mountain toward the city centre. Cameras remain behind, below or on the dragon’s left side without reversing the travel axis.4. FIRST FRAME AND SPATIAL BLOCKINGThe dragon is already crouched on the pinnacle, wings spread, hind legs compressed and head aimed toward the city. Its jaws open for one roar. Fires flicker below, connected smoke columns bend with the wind and the entire storm ceiling visibly moves.5. FORMAT MODESix shots with hard cuts:SHOT 1 — 0.0–4.0s: roar and launch.SHOT 2 — 4.0–9.0s: high-speed pursuit toward the harbour.SHOT 3 — 9.0–13.5s: low flight across the water toward the city.SHOT 4 — 13.5–19.0s: first fire attack between towers.SHOT 5 — 19.0–25.0s: banking pursuit and sweeping fire attack.SHOT 6 — 25.0–30.0s: dragon climbs above the burning city.Cuts are motivated by wing wipes, smoke wipes and close architectural passes. No fades or dissolves.6. OPTICSSHOT 1: 24mm, 74° horizontal FOV, low-angle environmental wide.SHOT 2: 18mm, 90° FOV, rear pursuit perspective.SHOT 3: 24mm, 74° FOV, low water-level chase.SHOT 4: 28mm, 65° FOV, roof-height tracking.SHOT 5: 24mm, 74° FOV, close side-rear pursuit.SHOT 6: 18mm, 90° FOV, monumental aerial wide.Moderate-deep focus. Strong natural motion blur on wing tips, water, smoke, embers and nearby buildings.7. CAMERAAll cameras have obvious physical handheld instability.SHOT 1 rapidly tilts upward as the dragon launches; wing pressure violently jolts the operator.SHOT 2 follows 12 metres behind the tail with intense wind buffeting and rapid vertical vibration.SHOT 3 races just above the water behind the dragon; waves and burning boats whip past the frame edges.SHOT 4 tracks through the street canyon at roof height.SHOT 5 follows the dragon through a hard bank, nearly losing framing as towers pass dangerously close.SHOT 6 pursues upward, then settles into a wide view of the devastated city.No smooth floating or mechanically perfect movement.8. ACTION TIMING0.0–0.8s: The dragon releases one thunderous roar, neck extended and eyes fixed on the city.0.8–2.0s: Hind legs drive into the pinnacle; claws fracture the rock.2.0–4.0s: The dragon launches and performs two powerful wing strokes. Dust and stone explode backward.4.0–6.5s: Hard cut behind the dragon already accelerating at high speed.6.5–9.0s: It folds its legs beneath its body and dives toward the harbour. Smoke streams across its wings.9.0–11.5s: The dragon skims rapidly above rough water. Wing tips nearly touch the waves.11.5–13.5s: It passes burning ships and climbs over the sea wall. A tower wipes across the lens.13.5–15.0s: Hard cut inside the city. The dragon bursts through smoke between Gothic towers.15.0–19.0s: It releases one continuous orange-white fire jet, sweeping across the left row of rooftops while maintaining full speed.19.0–21.5s: The dragon snaps into a hard right bank around the central tower; the tail swings with delayed inertia.21.5–25.0s: Its connected fire stream sweeps across the avenue and strikes the right-side tower. Burning masonry and embers fall behind it.25.0–27.0s: The dragon stops breathing fire, beats its wings powerfully and climbs above the rooftops.27.0–30.0s: It ascends into the storm light and glides over the burning city. The camera widens to reveal spreading flames, smoke columns and the harbour below.9. PHYSICSThe dragon has immense believable mass despite its speed. Wing strokes originate in the shoulders; membranes stretch under aerodynamic load. The torso, legs and tail react with delayed inertia. Wing wakes tear openings through smoke, disturb water and buffet nearby fires. Fire emerges only from the open mouth as a pressure-driven stream with a white-hot core, orange turbulent edges and visible heat distortion. Buildings ignite progressively at visible impact points. Debris follows gravity and the dragon’s wake.10. LIGHTINGCold storm daylight enters from upper-left. Existing fires provide orange underlight beneath the dragon. The fire stream becomes a moving motivated key light, casting travelling highlights over scales, towers and smoke. Sunbeams break through the clouds during the final climb. Preserve detail in the flame core and keep the dragon’s silhouette readable.11. AUDIONo dialogue.Synchronized dragon roar, claw scraping, rock fracture, leather-wing thunder, violent wind, wave impacts, burning ships, collapsing masonry, ember hiss and pressurised fire blasts.Epic original score: rapid war drums, low brass ostinato and urgent strings begin immediately. Wordless low choir enters at launch. Percussion accelerates during the chase. Full orchestra strikes with each fire attack, then expands into a dark triumphant finale during the ascent. Roar, wings and fire remain louder than the music.12. CHARACTER ACTINGThe dragon acts with focused predatory intent. Its eyes remain locked on its flight path and successive building targets. During acceleration, its head lowers and shoulders drive aggressively. Inside the city, the neck deliberately guides the fire stream while the tail controls each bank. In the final shot, its chest opens and posture changes from attacking aggression to airborne dominance.13. STYLEGrand apocalyptic dark-fantasy cinema, aggressive pursuit photography, monumental scale and battlefield energy. Charcoal and storm blue occupy 60% of the palette, smoke-brown stone 30%, and fire orange 10%. Weathered 35mm film texture with old-photograph softness, organic grain and no digital sharpening.14. QUALITYConsistent dragon identity and anatomy through every cut: one head, two wings, four legs and one tail. Stable city architecture, coherent wing cycles, attached mouth fire, volumetric smoke and physically connected destruction. Natural fast-motion blur without ghost copies, anatomy mutation or detached flames.15. POSITIVE CONSTRAINTSExactly one dragon remains visible throughout the sequence. It launches before 2 seconds, reaches the harbour by 9 seconds, enters the city at 13.5 seconds and completes two fast fire-attack passes before climbing away. Every shot preserves the mountain-to-city direction. Strong camera shake communicates extreme speed while the dragon remains readable. City fires continuously emit smoke, clouds visibly travel across the sky, and new destruction appears only where the connected fire stream strikes.
```

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<button type="button" class="guide-video-poster" data-src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-v-004.f21ef3e96c0ee1e4.mp4" aria-label="播放视频"><img src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-p-004.559a4e9c9a5a4d73.17784587d1bbaaee.webp" alt="" /></button>

```cURL
curl -sS --request POST \
  'https://api-beijing.klingai.com/omni-video/kling-4.0' \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "Use @city for the city and @dragon for the dragon identity.\n30s, six shots, dark-fantasy cinema. Exactly one colossal dragon throughout: one head, four legs, two wings, one tail. Its appearance 100% matches the dragon reference. Use the city reference for architecture and geography.\n0–4s: Low rear-left wide. The crouching dragon roars, launches before 2s and scatters rock with powerful wingbeats.\n4–9s: Rear pursuit as it accelerates downhill toward the harbour.\n9–13.5s: Skim above water past burning ships, then climb over the sea wall.\n13.5–19s: Track above a broad avenue. From 15s, a mouth-connected fire jet ignites the left rooftops in sequence.\n19–25s: Stop firing and bank right around the central tower. At 21.5s, a second jet strikes the right-side tower; masonry falls behind.\n25–30s: Stop firing, climb and glide. Widen to reveal the burning city and harbour.\nKeep cameras behind or left of the dragon, wing clearance visible and destruction tied to flame impacts. Heavy wingbeats, trailing tail inertia, disturbed smoke. Cold storm light, orange firelight, organic film grain. Camera buffeting settles for the finale.\nSynchronized roar, wings, wind, fire and masonry over urgent drums, brass and wordless choir. No dialogue or text."
    },
    {
      "type": "refer_image",
      "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch6_3_burning_city_ref.png",
      "id": "city"
    },
    {
      "type": "refer_image",
      "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch6_3_dragon_character_ref.png",
      "id": "dragon"
    }
  ],
  "settings": {
    "duration": 30,
    "resolution": "1080p",
    "aspect_ratio": "adaptive"
  }
}'
```

### 6.4 视频编辑

可定向修改已有视频中的角色表情与动作、机位与运镜、风格或背景。说明修改内容时，同时写明需要保留的部分。

| **修改维度**   | **写法**                                                                                                                   |
| -------------- | -------------------------------------------------------------------------------------------------------------------------- |
| 增加主体       | 编辑 @视频1，在视频最后箱子再次被打开时，@主体1 正躺在里面睡觉                                                             |
| 人物与场景替换 | 编辑 @视频1 中的环境和人物，整体替换为 @图片1                                                                              |
| 多角色替换     | 编辑 @视频1，将从便利店门口依次走出的三位人物，分别替换为第一位 @图片1、第二位 @图片2、第三位 @图片3，并分别描述新主体外表 |
| 删除元素       | 删除 @视频1 中的前景人物，其余保持不变                                                                                     |
| 风格修改       | 编辑 @视频1，将视频中的柯基犬替换成 3D 像素风格的柯基犬，保持其动作                                                        |

**风格修改**

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

<div class="guide-case-media-list">
<div class="guide-case-shot">

<button type="button" class="guide-video-poster" data-src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-v-005.78afc62e31c998f8.mp4" aria-label="播放视频"><img src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-p-005.270ffa2083d6965b.559f85d985016a76.webp" alt="" /></button>

<p>视频1</p>
</div>
</div>

```text
编辑@视频1 中那只在雪地里蹦跳的三色柯基幼犬，替换为3D方块像素风格的柯基：整个身体由方块拼成——长方体的身子、方块脑袋、两只竖起的方形三角耳、四条短短的方柱腿、一小截方块尾巴，所有边缘都是硬直角，没有任何圆弧；表面是16×16像素的低分辨率贴图，颜色沿用原来柯基的三色分布——黄褐色身体、背部黑色鞍状色块、白色脸中线、白围脖、白胸、白爪，眼睛是两个黑色方点，鼻子是一个黑方块，舌头是一小块粉色像素；受光面亮、侧面暗，是平涂的方块明暗，没有毛发质感和柔和过渡。体型与原来的柯基一致，不放大不缩小。方块柯基逐帧沿用原来柯基的位置、动作和运动轨迹：站在门廊边、跳进深雪消失、雪面留坑、探出方块脑袋、一次次腾空往前跳并陷进雪里、最后坐在雪坑里；跳跃时身体和腿像游戏里的生物动画一样只做整块的摆动，不弯曲。它陷进雪里的深度、蹬起的雪、身上落的雪、投在雪面上的影子都跟随方块身体；被雪盖住后再出现时仍是同一只方块柯基，贴图一致。注意：只有柯基变成方块风格，木门廊、雪地、木栅栏、树林、灰白天空全部保持真实实拍画面，不做任何方块化或像素化。画面里只有这一只动物，任何一帧都不再出现真实毛发的柯基。声音与原片完全一致，不新增任何声音。手持机位和运镜保持不变。其他保持不变。
```

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<button type="button" class="guide-video-poster" data-src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-v-003.cb00c3c4742ff6b7.mp4" aria-label="播放视频"><img src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-p-003.85c4ffe41421e349.f70b86ee0f017c4f.webp" alt="" /></button>

视频编辑时，可以设置duration参数，如未设置该参数，模型会follow原视频长度。如果设置duration参数，优先follow输入的duration参数。

```cURL
curl --request POST \
  'https://api-beijing.klingai.com/omni-video/kling-4.0' \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "编辑@视频1 中那只在雪地里蹦跳的三色柯基幼犬，替换为3D方块像素风格的柯基：整个身体由方块拼成——长方体的身子、方块脑袋、两只竖起的方形三角耳、四条短短的方柱腿、一小截方块尾巴，所有边缘都是硬直角，没有任何圆弧；表面是16×16像素的低分辨率贴图，颜色沿用原来柯基的三色分布——黄褐色身体、背部黑色鞍状色块、白色脸中线、白围脖、白胸、白爪，眼睛是两个黑色方点，鼻子是一个黑方块，舌头是一小块粉色像素；受光面亮、侧面暗，是平涂的方块明暗，没有毛发质感和柔和过渡。体型与原来的柯基一致，不放大不缩小。方块柯基逐帧沿用原来柯基的位置、动作和运动轨迹：站在门廊边、跳进深雪消失、雪面留坑、探出方块脑袋、一次次腾空往前跳并陷进雪里、最后坐在雪坑里；跳跃时身体和腿像游戏里的生物动画一样只做整块的摆动，不弯曲。它陷进雪里的深度、蹬起的雪、身上落的雪、投在雪面上的影子都跟随方块身体；被雪盖住后再出现时仍是同一只方块柯基，贴图一致。注意：只有柯基变成方块风格，木门廊、雪地、木栅栏、树林、灰白天空全部保持真实实拍画面，不做任何方块化或像素化。画面里只有这一只动物，任何一帧都不再出现真实毛发的柯基。声音与原片完全一致，不新增任何声音。手持机位和运镜保持不变。其他保持不变。"
    },
    {
      "type": "base_video",
      "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch6_4_snow_corgi_source.mp4",
      "id": "视频1"
    }
  ],
  "settings": {
    "resolution": "1080p",
    "aspect_ratio": "adaptive"
  }
}'
```

### 6.5 爆款视频复刻

可以借用参考视频的叙事节奏、镜头构图或呈现方式，再替换角色、商品与场景。提示词需要说清借用与替换的部分。本次重点介绍社媒爆款与效果广告场景；参考片段与目标内容在节奏和镜头结构上越接近，通常越容易获得预期效果。

将 @视频1 里的主体替换成 @图片1，其余保持不变。

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

<div class="guide-case-media-list">
<div class="guide-case-shot">

<button type="button" class="guide-video-poster" data-src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-v-007.778ee8312de53712.mp4" aria-label="播放视频"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-p-007.616c96b66109dcb0.77d27b3c4e7d1764.webp" alt="" /></button>

<p>视频1</p>
</div>
<div class="guide-case-shot">

<div class="media-wrap image-wrap"><img src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-i-007.ca289700747c3fbd.9eb6aaf6b66692f4.webp" alt="" /></div>

<p>图片1</p>
</div>
</div>

```text
将 @视频1 里的主体替换成 @图片1，其余保持不变
```

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<button type="button" class="guide-video-poster" data-src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-v-008.96253122981d0dee.mp4" aria-label="播放视频"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-p-008.00b2b22eb36bb923.739e512104999a6f.webp" alt="" /></button>

API 代码示例：

```cURL
curl -sS --request POST \
  'https://api-beijing.klingai.com/omni-video/kling-4.0' \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "将@video_1里的主体替换成 @image_1，其余保持不变。"
    },
    {
      "type": "base_video",
      "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch6_5_viral_pet_source.mov",
      "id": "video_1"
    },
    {
      "type": "refer_image",
      "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch6_5_fluffy_cat_ref.png",
      "id": "image_1"
    }
  ],
  "settings": {
    "resolution": "1080p",
    "aspect_ratio": "adaptive"
  }
}'
```

### 6.6 多语言与音色

声音输出为双通道立体声。需要特定语种时，直接用该语种撰写引号中的台词；需要更具体的说话方式时，可补充年龄、音色、语速和情绪。

| **项目** | **支持范围**                                                   |
| -------- | -------------------------------------------------------------- |
| 语种     | 中文、英语、日语、韩语、西班牙语、葡萄牙语、德语、法语、印地语 |
| 中文方言 | 四川话、粤语                                                   |
| 中文口音 | 北京、东北、中国台湾                                           |
| 英文口音 | 美式、英式、印度                                               |

音频输入仅支持音色参考，用于指定说话人的音色。背景音乐和音效由模型根据画面生成，在提示词的声音部分描述即可。

【适合口播广告、多语种内容，以及需要突出地域口音的剧情演绎】

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

<div class="guide-case-media-list">
<div class="guide-case-shot">

<div class="media-wrap image-wrap"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-i-005.299bb54318af604a.112e6658b0c09849.webp" alt="" /></div>

<p>图片1</p>
</div>
</div>

```text
场景：三人位于明亮、整洁的虚构城市旅游咨询中心。全程色调保持一致。游客站在画面左侧，翻译员站在中间，旅游工作人员站在右侧。咨询台上放着城市地图和路线示意图。背景文字和地图文字模糊不可读，不出现真实品牌、机构名称、logo 或水印。剧情与对白：0–3 秒：三人中景。西班牙女性游客看向中间的翻译员，举起手中的地图，用自然、清晰、偏慢的西班牙语说：“¿Dónde está la estación de metro más cercana?”游客说完后停顿约 0.5 秒，翻译员转向旅游服务工作人员，用中文翻译：“她想知道最近的地铁站在哪里。”3–7 秒：镜头切到翻译员和旅游服务工作人员。旅游服务工作人员看向地图（不用给地图特写），用自然、清晰的中文回答：“沿这条路直走，步行大约五分钟就能到。”工作人员说完后停顿约 0.5 秒，翻译员确认理解后转向游客。7–11 秒：翻译员用自然、清晰、偏慢的西班牙语翻译工作人员的回答：“La estación de metro está a unos cinco minutos a pie. Siga recto por esta calle.”翻译员说话时指向地图路线，游客认真查看地图。11–15 秒：镜头回到三人中景。西班牙游客理解后微笑点头，用西班牙语说：“Muchas gracias.”三人保持自然的服务交流状态，画面结束。声音要求：- 西班牙游客只说西班牙语；- 中国旅游服务工作人员只说中文；- 中国翻译员先说中文，再说西班牙语；- 三个人使用不同的声音；- 每个人说话时，其他人保持安静，不要抢话或同时说话；- 所有对白必须有清晰人声，人物口型与对应语言同步；- 西班牙语发音自然、标准，不要生成英语发音；- 语速偏慢，句子之间保留自然停顿；- 保留轻微旅游咨询中心环境声，不添加背景音乐，环境音不能盖住对白。镜头设计：开头用三人中景交代人物关系；游客说话时切到游客和翻译员的双人近景；翻译员转述时切到翻译员与工作人员；工作人员回答时加入地图路线特写；翻译员用西班牙语翻译时回到翻译员与游客；结尾回到三人中景。人物位置、视线方向和服装保持连续，不要突然换人或改变空间关系。画面风格：真实、自然、专业的旅游服务纪录片风格，明亮干净，人物表情自然，动作克制，像机场或城市游客服务中心的真实交流场景。
```

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<button type="button" class="guide-video-poster" data-src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-v-006.0c7343dba0034c6f.mp4" aria-label="播放视频"><img src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-p-006.218bd0c70d7fe5d2.c92ba79e2fadafba.webp" alt="" /></button>

API 代码示例：

```cURL
curl -sS --request POST \
  'https://api-beijing.klingai.com/text-to-video/kling-4.0' \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "prompt": "场景：三人位于明亮、整洁的虚构城市旅游咨询中心。全程色调保持一致。游客站在画面左侧，翻译员站在中间，旅游工作人员站在右侧。咨询台上放着城市地图和路线示意图。背景文字和地图文字模糊不可读，不出现真实品牌、机构名称、logo 或水印。剧情与对白：0–3 秒：三人中景。西班牙女性游客看向中间的翻译员，举起手中的地图，用自然、清晰、偏慢的西班牙语说：“¿Dónde está la estación de metro más cercana?”游客说完后停顿约 0.5 秒，翻译员转向旅游服务工作人员，用中文翻译：“她想知道最近的地铁站在哪里。”3–7 秒：镜头切到翻译员和旅游服务工作人员。旅游服务工作人员看向地图（不用给地图特写），用自然、清晰的中文回答：“沿这条路直走，步行大约五分钟就能到。”工作人员说完后停顿约 0.5 秒，翻译员确认理解后转向游客。7–11 秒：翻译员用自然、清晰、偏慢的西班牙语翻译工作人员的回答：“La estación de metro está a unos cinco minutos a pie. Siga recto por esta calle.”翻译员说话时指向地图路线，游客认真查看地图。11–15 秒：镜头回到三人中景。西班牙游客理解后微笑点头，用西班牙语说：“Muchas gracias.”三人保持自然的服务交流状态，画面结束。声音要求：- 西班牙游客只说西班牙语；- 中国旅游服务工作人员只说中文；- 中国翻译员先说中文，再说西班牙语；- 三个人使用不同的声音；- 每个人说话时，其他人保持安静，不要抢话或同时说话；- 所有对白必须有清晰人声，人物口型与对应语言同步；- 西班牙语发音自然、标准，不要生成英语发音；- 语速偏慢，句子之间保留自然停顿；- 保留轻微旅游咨询中心环境声，不添加背景音乐，环境音不能盖住对白。镜头设计：开头用三人中景交代人物关系；游客说话时切到游客和翻译员的双人近景；翻译员转述时切到翻译员与工作人员；工作人员回答时加入地图路线特写；翻译员用西班牙语翻译时回到翻译员与游客；结尾回到三人中景。人物位置、视线方向和服装保持连续，不要突然换人或改变空间关系。画面风格：真实、自然、专业的旅游服务纪录片风格，明亮干净，人物表情自然，动作克制，像机场或城市游客服务中心的真实交流场景。",
  "settings": {
    "resolution": "1080p",
    "aspect_ratio": "16:9"
  }
}'
```

::::: container guide-case

:::: container guide-case-input

<p class="guide-case-label">输入</p>

<div class="guide-case-media-list">
<div class="guide-case-shot">

<div class="media-wrap image-wrap"><img src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/fashion-showroom-reference.34d8658d4f3de1f6.9e15500add5d00c4.webp" alt="" /></div>

<p>图片1</p>
</div>
</div>

```text
1. SCENE CONTEXTEXACT 1 HUMAN CHARACTER — NO DUPLICATES.A woman enthusiastically presents the black Kling cropped puffer jacket she is wearing inside a minimalist fashion showroom. She maintains warm, confident eye contact with the camera while demonstrating the collar, chest logo, quilted construction, cropped silhouette, and pockets. One continuous 15-second vertical fashion shot.2. ACTIVE REFERENCES@image1 controls the woman’s exact identity, straight brown hair, blue eyes, small earrings, black Kling cropped puffer jacket, high collar, silver zipper, white chest logo, quilted panels, elastic cuffs, side pockets, loose blue jeans, black belt, showroom racks, window, and vertical composition. Preserve every detail exactly.3. LOCATION MAPThe woman remains centered between two clothing racks. The left rack stays behind frame-left, the second rack remains in the rear-right, and the large window stays on frame-right. The camera remains directly in front of her and moves only slightly toward her left side.4. FIRST FRAME AND SPATIAL BLOCKINGMatch the reference composition. She stands in a relaxed three-quarter position with both arms resting naturally beside her body. The complete jacket, waistline, belt, and upper jeans remain visible. Her head turns toward the camera and her eyes lock naturally onto the lens.5. FORMAT MODEOne uninterrupted 15-second vertical 9:16 shot. No cuts, fades, dissolves, speed ramps, wardrobe transformations, location changes, or duplicated poses.6. OPTICS50mm equivalent lens with a 40° horizontal field of view. Medium fashion framing keeps her eyes, facial expression, collar, logo, zipper, sleeves, hem, pockets, and waistline readable. Moderate depth of field softly separates her from the clothing racks.7. CAMERAA human operator stands approximately two and a half meters away at chest height and performs one slow handheld clockwise arc of less than one meter. Breathing drift, small footsteps, slight roll, and delayed reframing remain visible. The camera never becomes mechanically stabilized or crops out the jacket hem.8. ACTION TIMING0.0–2.0s: She finds the lens, takes a light anticipatory breath, and forms a genuine welcoming smile.2.0–5.5s: While beginning her sentence, she touches the structured collar and follows the zipper downward with her fingertips, keeping her eyes on the lens.5.5–8.5s: Her voice becomes more animated as her hand pauses beside the white Kling logo and her free hand opens in a small expressive gesture.8.5–11.5s: She turns into a three-quarter side profile, slips both hands into the pockets, and looks back toward the lens with a confident smile.11.5–15.0s: She faces forward again, relaxes her shoulders, and finishes the presentation with bright eyes and a warm, satisfied expression.9. PHYSICSThe padded jacket compresses naturally beneath her fingertips and recovers after release. Quilted panels retain consistent volume. Sleeves bend and crease at the elbows, while the cropped hem shifts during her turn and settles under gravity. Hair and earrings respond with small delayed movement.10. LIGHTINGSoft daylight from the large window on frame-right is the single motivated key source. It creates restrained highlights across her eyes, hair, black fabric, silver zipper, and cheekbones while preserving detail in the quilted panels. Ceiling track lights remain subtle background practicals.11. AUDIOLayered showroom ambience: quiet room tone, distant ventilation, soft jacket rustle, zipper contact, jeans movement, and restrained footsteps. In a sincere, emotionally engaged English voice, she says: “I honestly love this Kling jacket—the cropped fit feels so confident, and it goes with everything.” Begin with warm appreciation, emphasize “love” and “confident,” then finish with an audible smile. Her lips, breath, expression, and garment gestures synchronize exactly with the sentence. SFX only, no music, no score, no song, no soundtrack.12. CHARACTER ACTINGShe speaks as someone genuinely excited by how the jacket makes her feel. Her eyes stay connected to the lens with living highlights and irregular natural blinks. Her eyebrows lift slightly on “love,” her cheeks rise on “confident,” and her final smile reaches both eyes. She never looks down at the garment while speaking; her hands locate each feature naturally through touch. INNER, UNSPOKEN: “This feels completely like me.”13. STYLEMinimal contemporary fashion content captured by an imperfect human companion. Clearly handheld intimacy, old-photograph softness, organic film grain, restrained contrast, natural fabric texture, gentle window halation, and no digital sharpening. Color balance: 60% black and charcoal, 25% cool white showroom tones, 15% faded blue denim and natural skin.14. QUALITYThe woman’s identity, eye color, hairstyle, earrings, jacket geometry, quilted panels, collar, zipper, cuffs, pockets, jeans, and belt remain consistent. The white Kling wordmark remains correctly spelled, stable, and attached to the same chest position. Eyes, lips, hands, fingers, sleeves, and fabric folds remain anatomically coherent.15. POSITIVE CONSTRAINTSExactly one woman wears exactly one black Kling jacket throughout the shot. She maintains direct lens connection while speaking and looks back toward the lens during the side pose. She speaks exactly one emotional English passage and performs one continuous garment presentation. The jacket remains fully zipped and its logo stays visible during front-facing moments. Add no second person, clothing change, subtitle, price, promotional overlay, mirror reflection, music, or runway movement. A flat emotionless delivery, wandering eyeline, malformed wordmark, changing jacket length, extra limb, or fabric passing through her body equals a failed shot.
```

:::: container guide-case-output

<p class="guide-case-label">输出</p>

<button type="button" class="guide-video-poster" data-src="https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-v-009.3140838b9e7acdf6.mp4" aria-label="播放视频"><img src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/zh-p-009.027b31dae20e273c.50afc6708587fff3.webp" alt="" /></button>

API 代码示例：

```cURL
curl -sS --request POST \
  'https://api-beijing.klingai.com/omni-video/kling-4.0' \
  --header "Authorization: Bearer ${KLING_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "contents": [
    {
      "type": "prompt",
      "text": "15s, 9:16, one continuous handheld shot of exactly one woman presenting her jacket.\n@image_1 defines her identity, outfit and showroom. Her appearance 100% matches the reference. Preserve the fully zipped black Kling cropped puffer, white chest logo, silver zipper, quilting, blue jeans and belt.\nKeep her head, entire jacket and waistline visible. Gentle handheld drift with a small arc toward her left; soft window light from frame-right.\n0–2s: Meet the lens and smile.\n2–8s: Touch the collar, trace beside the closed zipper, then indicate the logo.\n8–12s: Turn slightly sideways, hands in pockets, face toward the lens.\n12–15s: Face forward and smile.\nWhile demonstrating, say exactly:\n“I honestly love this Kling jacket—the cropped fit feels so confident, and it goes with everything.”\nWarm natural English, accurate lip sync, quiet room tone and fabric rustle. Clear face and garment detail, natural fabric movement, stable correctly spelled logo. No cuts, extra people, wardrobe changes, music, subtitles or overlays.\nUse @speaker as the voice of the woman for the exact English dialogue above."
    },
    {
      "type": "refer_image",
      "url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-tob-release-note/ch6_6_jacket_model_ref.png",
      "id": "image_1"
    },
    {
      "type": "voice",
      "voice_id": "829826751244537879",
      "id": "speaker"
    }
  ],
  "settings": {
    "duration": 15,
    "resolution": "1080p",
    "aspect_ratio": "adaptive"
  }
}'
```

### 6.7 文字生成

画面文字支持中、英、日、韩、西、葡、德、法、印地等语言，以及 Emoji 与 Logo。字幕也可以直接写进提示词，同时说明字号、对齐方式、停留时间和是否与对白同步。

### 6.8 风格化生成

可通过提示词控制画面材质、光影与氛围，使用电影感影像、复古 DV、动画、毛毡、奇幻、赛博等视觉风格。指定动画风格时，明确采用的质感，并排除与其冲突的写实质感。

编辑 @视频1，将视频风格替换成 @图片1 的毛毡风格，保持原视频的构图、镜头、动作，只替换风格，不改变人物的服装款式、摩托车造型、场景元素及事件顺序。

### 6.9 关键帧控制

关键帧用于定义时间线上的画面节点。未使用关键帧时，画面变化的顺序与时机由模型决定；使用后，用户可指定关键时刻的画面。

| **控制对象** | **示意**                                 |
| ------------ | ---------------------------------------- |
| 角色动作     | 第 3 秒抬手，第 7 秒转身                 |
| 角色出入画   | 角色 B 在第 6 秒进门                     |
| 场景变化     | 第 5 秒天色转暗，第 10 秒下雨            |
| 构图变化     | 在指定秒数内从大远景转到特写             |
| 状态演进     | 从 A 状态到 B 状态，中间经过哪些画面节点 |

首帧、尾帧、首尾帧与中间帧模板见[Kling 4.0 视频 提示词案例-第1.9节](https://klingai.com/document-api/api/usage-guide/kling-4-0-prompt-guide#1.9-关键帧)。

### 6.10 视频续拍

即将上线。支持多次续拍、最长延展至 2 分钟。

## 7 自定义视频输出规格

通过 API 参数控制输出视频的分辨率、宽高比、时长，以及是否同时生成含水印的结果。

- settings.resolution：指定输出视频的分辨率。
- settings.aspect_ratio：指定输出视频的宽高比。
- settings.duration：指定输出视频的时长。
- options.watermark_info.enabled：指定是否同时生成含水印的结果。

以下以 **Kling 4.0 全能参考接口 /omni-video/kling-4.0** 为例。示例仅展示相关配置，使用时需与 contents 等参数合并为完整请求。

### 7.1 分辨率与动态范围

Kling 4.0 支持 720p、1080p、4K 三档输出。4K输出即将上线，同时1080p、4K 的 10-bit HDR 输出即将上线。通过 settings.resolution 指定输出视频的分辨率。默认值：1080p；可选值：720p、1080p

```json
{
    "settings": {
        "resolution": "1080p"
    }
}
```

### 7.2 宽高比

全能参考的创作端选项为 21:9、16:9、1:1、9:16、智能，默认智能。关键帧入口上传图片后，比例跟随第一张关键帧。通过 settings.aspect_ratio 指定输出视频的宽高比。默认值：adaptive，可选值：21:9、16:9、9:16、1:1、adaptive

传入明确的比例值时，以参数值为准，优先于 Prompt 中的比例要求。

```json
{
    "settings": {
        "aspect_ratio": "16:9"
    }
}
```

**自动适配规则**

aspect_ratio未传入明确比例，或将其设置为 adaptive 时，模型按以下优先级确定输出比例：

1. **Prompt 中的比例意图**：例如“生成一段 9:16 的竖屏视频”。
1. **待编辑视频的比例**：若未识别到明确的比例意图，优先采用 base_video 的比例。
1. **关键帧图片的比例**：未提供 base_video 时，采用关键帧图片的比例；存在多张关键帧时优先采用首帧，无首帧时采用第一张关键帧图片。
1. **其他输入视频的比例**：未提供待编辑视频和关键帧图片时，参考其他输入视频的比例。
1. **默认比例**：以上均不适用时，使用 16:9。

### 7.3 视频时长

Kling 4.0 单次生成 3–30 秒。创作端以 1 秒为单位调整，默认 10 秒。Kling 4.0 Flash 单次最长 20 秒。

通过 settings.duration 指定生成视频的时长，单位为秒。非必填；取值范围：3–30 秒的整数。

传入 duration 时，以参数值为准，优先于 Prompt 中的时长要求。

```json
{
    "settings": {
        "duration": 10
    }
}
```

**未传入时的适配规则**

1. **优先识别 Prompt 中的时长意图**：例如“生成一段 15 秒的视频”。
1. **采用待编辑视频的时长**：若未识别到明确的时长意图，且提供了 base_video，则采用该视频的时长。
1. **使用默认时长**：若未识别到明确的时长意图，且未提供 base_video，则使用 **10 秒**。

例如，希望通过 Prompt 指定“15 秒、9:16”时，可省略 duration，并将 aspect_ratio 设置为 adaptive：

```json
{
    "contents": [
        {
            "type": "prompt",
            "text": "生成一段15秒、9:16的竖屏视频：清晨的海边，一只海鸥掠过海面，镜头缓慢向前推进。"
        }
    ],
    "settings": {
        "resolution": "1080p",
        "aspect_ratio": "adaptive"
    }
}
```

### 7.4 水印

通过 options.watermark_info.enabled 控制是否同时生成含水印的视频结果。

- true：同时生成含水印的结果。
- false（默认）：不额外生成含水印的结果。

```json
{
    "options": {
        "watermark_info": {
            "enabled": true
        }
    }
}
```

任务成功后，可从视频输出对象的 url 获取常规结果。

## 8 提示词技巧与写作建议

### 8.1 基础写作

采用描述性语言，减少抽象词汇和泛化的否定表述。写清画面中实际可见的特征，减少模型的猜测。

| **不推荐的表达**           | **推荐的描述**                                       |
| -------------------------- | ---------------------------------------------------- |
| 高级质感                   | 侧逆光勾出物体边缘，背景虚化，表面可见细微磨砂颗粒   |
| 年代感                     | 墙面泛黄，家具边角磨损，暖色白炽灯                   |
| 中产家庭的厨房             | 木纹橱柜，台面上放着电饭煲与调味罐，冰箱门贴着便利贴 |
| 不要展示主体正面，在打电话 | 主体侧面，在打电话                                   |

先用一句话写清主体、场景、动作和情绪，再补充真正影响结果的镜头、时序、声音和保留条件。

### 8.2 结构化提示词

【素材职责】

@图片1 是\_\_\_，保持其\_\_\_一致；

@图片2 是\_\_\_，保持其\_\_\_一致；

参考 @视频1 的\_\_\_。

【整体设定】

场景与质感\_\_\_，视觉风格\_\_\_，镜头基调\_\_\_。

【分段事件】

0–Xs：\_\_\_（画面、动作、情绪）

X–Ys：\_\_\_（镜头如何运动、细节补充）

Y–结尾：\_\_\_（收尾画面）

【声音】

谁说什么或旁白\_\_\_；环境声\_\_\_；配乐\_\_\_；音效\_\_\_。

### 8.3参考类任务与多素材映射

素材按上传顺序编号，例如 @图片1、@图片2、@视频1。每份素材都需要声明用途；仅提供编号而不说明职责时，模型会自行推测素材用途。

@图片1 是本场景，保持其空间结构、陈设与光线；

@图片2 是女主角，保持其面孔、发型与服装；

女主角在该场景中走向窗边，停下，回头。

多份素材分别提供人物、动作、镜头或声音时，逐一说明作用范围，并明确不应带入的部分。素材较多时，核对每个 @编号是否引用正确。

### 8.4编辑类任务

编辑提示词包含三个部分：待编辑的视频、具体修改、需要保留的内容。

编辑 @视频1，将\_\_\_改为\_\_\_，其余保持不变。

“编辑”与“参考”表达不同意图。需要修改原视频本身时，明确使用“编辑”；仅写“参考”可能进入参考生成。

### 8.5 首尾帧与关键帧

首帧写清后续事件，尾帧写清到达最终画面之前发生的过程；首尾帧同时给出起点与终点。中间帧为每张图片补充节点内容和镜头如何到达该位置。

关键帧独立入口仅支持图片，不支持上传其他参考素材。

### 8.6 时间轴与分段事件

建议采用分段时间与关键帧节点组织事件。例如：

X–Ys｜关键帧1：\_\_\_（发生了什么）

Y–Zs｜关键帧2：\_\_\_（发生了什么）

A–Bs｜关键帧3：\_\_\_（发生了什么）

每段写清画面、动作、情绪和镜头运动，以及与相邻节点的衔接。生成时长的创作端设置步长为 1 秒；

### 8.7 负向控制

优先正向描述想要的画面。特别提醒：模型可能默认添加字幕和背景音乐，不需要时应明确写出“无字幕”“无背景音乐”。

风格化任务中，可用正向风格描述与针对性的排除条件共同限定质感。例如，指定动画风格时排除写实质感。不要将否定词扩展为与任务无关的长清单。

### 8.8 进阶写作

**镜头语言**

可描述推、拉、摇、移、跟拍、环绕等镜头运动，并结合具体画面节点说明景别变化与转场。使用参考视频控制运镜时，明确只参考哪部分镜头轨迹和节奏，再说明替换的主体与场景。

**动作与表情**

用可观察的动作描述人物状态与情绪，写清事件如何推进。需要指定动作节点时，结合关键帧描述，例如第 3 秒抬手、第 7 秒转身。

**多宫格分镜与故事板**

分镜表参考写法包括：用图片提供角色设计，并将分镜表作为镜头顺序、取景、摄影机路径、画面方向和情绪变化的参考。提示词中说明需要生成完成态画面，避免把网格、标题栏或中文标注当成成片内容。

**声音与语种**

写清谁说什么，并补充语速、情绪、音色、环境声、配乐与音效。特定语种的台词直接使用该语种撰写。上传音色只用于指定说话人的音色，背景音乐和音效通过提示词描述。

**字幕与画面文字**

写明具体文字内容、位置、对齐、停留时间和是否同步对白。

## 9 使用限制

### 9.1 全能参考输入

| **输入类型** | **数量与规格**                                                                 |
| ------------ | ------------------------------------------------------------------------------ |
| 文本         | 不超过 8000 tokens                                                             |
| 图片         | 最多 10 张；单张不超过 30 MB；长宽比 2:5–5:2                                   |
| 视频         | 最多 5 段；单段 3–30 秒；总时长不超过 30 秒；单段不超过 300 MB；长宽比 2:5–5:2 |
| 音色         | 单次最多 3 个；创建音色的音频长 5–30 秒；文件不超过 50 MB                      |
| 主体         | 最多 7 个，其中视频主体最多 3 个；创建视频主体的素材长 3–8 秒                  |
| 合计         | 图片、视频、音色、主体合计最多 15 个                                           |

参考视频、编辑视频和视频主体共用视频额度，合计最多 5 段、总时长不超过 30 秒。已上传 5 个参考视频后，不能再添加视频主体。

音频输入只支持音色参考，不支持上传背景音乐或音效。

## 10 常见问题

### 10.1 素材与能力

**素材总量如何计算**

图片、视频、音色、主体合计最多 15 个，各类型同时受自身上限约束。素材较多时，优先保留最影响画面与节奏的部分。

**已上传 5 个参考视频后能否添加视频主体**

不能。参考视频、编辑视频和视频主体共用 5 段、30 秒的视频额度。

**是否支持上传背景音乐或音效**

不支持。音频输入仅支持音色参考。背景音乐与音效在提示词中描述，由模型根据画面生成。

**是否需要手动开启音效与分镜**

创作端音画同步与智能分镜无开关，默认开启。API 也同样默认开启。

**提示词长度上限是多少**

8000 tokens。为便于开发者统计输入长度并进行校验，API 端将这一限制换算为字符数，如为纯英文，内容长度不超过26,000个字符；如为纯非英文，内容长度不能超过11,000个字符；如为英文&非英文混合输入，需保持英文字符数 ÷ 26,000 + 非英文字符数 ÷ 11,000 ≤ 1。

### 10.2提示词优化

**生成结果与预期不符时如何调整**

先检查每份素材是否声明职责，再检查是否使用了“高级感”“电影感”等抽象词。将其改成具体光线、材质、构图与动作描述。素材较多时，还需核对编号与作用范围。

**提示词是否越长越好**

不必追求长度。先写清主体、场景、动作与情绪，再补充镜头、时序、声音和保留条件。复刻视频时，选择节奏、构图和运镜接近目标的参考片段。
