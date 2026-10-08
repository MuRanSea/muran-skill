<!-- Official source: https://platform.minimax.cn/docs/api-reference/speech-t2a-websocket-bidi.md -->
<!-- Source SHA-256: 847ef787f9996e7ffd1aaea665ea4d83c1dace9dd0851f5de524172f68b1b383 -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.minimaxi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 双向流式语音合成

> 通过 WebSocket 连接按任意粒度（含逐字）流式发送文本，由服务端自动攒句合成，适合对接大模型流式输出。

## 与 `/ws/v1/t2a_v2` 的区别

本接口面向**文本流式输入**场景：把大模型的流式输出直接逐 token 转成语音。

| | [`/ws/v1/t2a_v2`](/docs/api-reference/speech-t2a-websocket) | `/ws/v1/t2a_v2_bidi`（本接口） |
| - | - | - |
| 攒句责任 | **客户端**自行判断句子边界 | **服务端**自动攒句 |
| 逐字发送文本 | 每个字触发一次合成，音频碎裂 | 攒成完整句子后再合成 |
| 打断 | 不支持，只能断开连接 | `task_cancel`，打断后可继续 |
| 句边界事件 | 无 | `sentence_start` / `sentence_end` |
| `task_finish` | 立即关闭连接 | 先合成缓冲区残留再关闭 |
| 催出残留但不结束会话 | 无 | `task_flush` |

`task_start` 的音色、音频、发音字典等参数与 `/ws/v1/t2a_v2` **完全一致**，已有接入可直接复用。

## 事件流程

1. 建立连接，收到 `connected_success`
2. 发送 `task_start`，收到 `task_started`
3. 发送 `task_continue`（**可按任意粒度，包括单个字符**），服务端攒句后开始合成
   * 每句合成开始返回 `sentence_start`
   * 音频通过 `task_continued` 分块返回
   * 该句结束返回 `sentence_end`
4. 需要打断时发送 `task_cancel`，收到 `task_canceled` 后可继续发送 `task_continue`
5. 一轮说完、希望立刻拿到尾句音频时发送 `task_flush`，收到 `task_flushed` 后会话继续
6. 发送 `task_finish`，服务端合成完残留文本后返回 `task_finished` 并关闭连接

<Note>
  三层结束语义不要混用：`is_final` 表示本次请求的音频结束，`sentence_end` 表示当前句结束，`task_finished` 表示整个会话结束。
</Note>

<Note>
  一条连接同时只能有一个合成会话。任务已开始后重复发送 `task_start` 会返回 `2206`（事件顺序非法）并关闭连接。
</Note>

## 攒句与延迟

服务端按标点判断句子边界，因此**你发送的文本中的标点会直接影响音频的自然度**：

| 文本情况 | 服务端行为 |
| - | - |
| 以句末标点（`。！？…!?.` 及换行）结尾 | **立即**送去合成，不引入额外延迟 |
| 出现次级标点（`，、；：,;:`） | 已攒文本达到一定长度才切句，避免切出过短的碎片 |
| 长文本完全没有标点 | 达到长度上限时强制切断，此时句边界与语义无关，听感会断裂 |
| 尾部不带标点，但已攒够长度 | 等待一个短暂的静默窗口后兜底送出 |
| 尾部不带标点且很短 | **继续等待**，不会为了低延迟把半个词送去合成 |

<Warning>
  最后一条对多轮对话场景有实际影响。

  如果一轮说完时残留的文本既很短、又不带句末标点，它不会被那个短静默窗口立刻送出，而要等一个更长的兜底窗口。有两个办法避免这段等待：**给最后一片文本补上句末标点**，或者**发送 `task_flush`** 主动催出。

  注意不能用 `task_finish` 代替——它会关闭连接，在一条连接上跑多轮对话时用不了。
</Warning>

<Warning>
  如果你的程序在转发大模型输出前会清洗文本，**请保留原始标点**。缺少标点会让服务端退化为按长度机械切分，停顿位置与语义不符，音频明显不自然。
</Warning>

<Note>
  上游（如大模型）出现较长停顿时，音频中会出现相应的空白，这无法避免。服务端不会为了填补空白而把攒了一半的句子提前送出——那样只会让听众先听到半个词再等待。
</Note>

## 连接保活

连接空闲超过约 120 秒会被服务端关闭并返回 `2201`。「空闲」指服务端既没有收到上行事件，也没有在下发音频。

<Warning>
  服务端**不会主动发送** WebSocket ping 帧。如果你的会话存在较长静默期（例如等待用户说话），请由客户端定期发送 ping —— 服务端会回复 pong 并刷新活跃时间。仅靠 TCP 连接存活不足以避免 `2201`。
</Warning>

## 发送速率与重试

收到 `2205` 表示服务端排队待合成的文本过多，通常是发送速度超过了合成速度。

<Note>
  `2205` **不是配额限流**，也是软失败：连接和会话都不会关闭。稍后重新发送该条 `task_continue` 即可，**不需要重连、也不需要重新 `task_start`**。
</Note>

单条 `task_continue` 文本超过 10,000 字符会返回 `2204`，该条被跳过，连接与会话同样保持。


## AsyncAPI

````yaml api-reference/speech/t2a/api/asyncapi-bidi.json t2a_v2_bidi_websocket
id: t2a_v2_bidi_websocket
title: T2a_v2_bidi_websocket
description: ''
servers:
  - id: production
    protocol: wss
    host: api.minimax.cn
    bindings: []
    variables: []
address: /ws/v1/t2a_v2_bidi
parameters: []
bindings: []
operations:
  - &ref_3
    id: sendMessage
    title: Send message
    description: ''
    type: receive
    messages:
      - &ref_5
        id: send_task_start
        contentType: application/json
        payload:
          - name: 任务开始
            description: |-
              发送`任务开始`事件则正式开始合成任务，当服务端返回的 `task_started` 事件时，标志着任务已成功开始。
              只有在接收到该事件后，才能向服务器发送 `task_continue` 事件或 `task_finish` 事件。
            type: object
            properties:
              - name: event
                type: string
                description: 控制发送的指令，当前环节应填写： `task_start`
                enumValues:
                  - task_start
                required: true
              - name: model
                type: string
                description: 请求的模型版本
                enumValues:
                  - speech-2.8-hd
                  - speech-2.8-turbo
                  - speech-2.6-hd
                  - speech-2.6-turbo
                  - speech-02-hd
                  - speech-02-turbo
                  - speech-01-hd
                  - speech-01-turbo
                required: true
              - name: voice_setting
                type: object
                required: true
                properties:
                  - name: voice_id
                    type: string
                    description: "合成音频的音色编号。若需要设置混合音色，请设置 timbre_weights 参数，本参数设置为空值。支持系统音色、复刻音色以及文生音色三种类型，以下是部分最新的系统音色（ID），可查看 [系统音色列表](/faq/system-voice-id) 或使用 [查询可用音色 API](/api-reference/voice-management-get) 查询系统支持的全部音色\n\n - **中文**:\n\t- moss_audio_ce44fc67-7ce3-11f0-8de5-96e35d26fb85\n\t- moss_audio_aaa1346a-7ce7-11f0-8e61-2e6e3c7ee85d\n\t- Chinese (Mandarin)_Lyrical_Voice\n\t- Chinese (Mandarin)_HK_Flight_Attendant\n- **英文**:\n\t- English_Graceful_Lady\n\t- English_Insightful_Speaker\n\t- English_radiant_girl\n\t- English_Persuasive_Man\n\t- moss_audio_6dc281eb-713c-11f0-a447-9613c873494c\n\t- moss_audio_570551b1-735c-11f0-b236-0adeeecad052\n\t- moss_audio_ad5baf92-735f-11f0-8263-fe5a2fe98ec8\n\t- English_Lucky_Robot\n- **日文**:\n\t- Japanese_Whisper_Belle\n\t- moss_audio_24875c4a-7be4-11f0-9359-4e72c55db738\n\t- moss_audio_7f4ee608-78ea-11f0-bb73-1e2a4cfcd245\n\t- moss_audio_c1a6a3ac-7be6-11f0-8e8e-36b92fbb4f95"
                    required: true
                  - name: speed
                    type: number
                    description: 合成音频的语速，取值越大，语速越快。取值范围 `[0.5,2]`，默认值为1.0
                    required: false
                  - name: vol
                    type: number
                    description: 合成音频的音量，取值越大，音量越高。取值范围 `(0,10]`，默认值为 1.0
                    required: false
                  - name: pitch
                    type: integer
                    description: 合成音频的语调，取值范围 `[-12,12]`，默认值为 0，其中 0 为原音色输出
                    required: false
                  - name: emotion
                    type: string
                    description: "控制合成语音的情绪，参数范围 `[\"happy\", \"sad\", \"angry\", \"fearful\", \"disgusted\", \"surprised\", \"calm\", \"fluent\", \"whisper\"]`，分别对应 8 种情绪：高兴，悲伤，愤怒，害怕，厌恶，惊讶，中性，生动，低语 \r\n- 模型会根据输入文本自动匹配合适的情绪，一般无需手动指定  \r\n- 该参数仅对 `speech-2.8-hd`, `speech-2.8-turbo`, `speech-2.6-hd`, `speech-2.6-turbo`, `speech-02-hd`, `speech-02-turbo`, `speech-01-hd`, `speech-01-turbo` 模型生效 \r\n- 选项 `fluent`, `whisper` 仅对 `speech-2.6-turbo`, `speech-2.6-hd` 模型生效，`speech-2.8-hd`, `speech-2.8-turbo` 模型不支持 `whisper`"
                    enumValues:
                      - happy
                      - sad
                      - angry
                      - fearful
                      - disgusted
                      - surprised
                      - calm
                      - fluent
                      - whisper
                    required: false
                  - name: english_normalization
                    type: boolean
                    description: 该参数支持英语文本规范化，可提升数字阅读场景的性能，但会略微增加延迟，默认值为 `false`
                    required: false
                  - name: latex_read
                    type: boolean
                    description: >-
                      控制是否朗读 latex 公式，默认为 `false`

                      **需注意**:

                      - 仅支持中文，开启该参数后，`language_boost` 参数会被设置为 `Chinese`

                      - 请求中的公式需要在公式的首尾加上 `$$`

                      - 请求中公式若有 `"\"`，需转义成 `"\\"`.


                      示例：一元二次方程根的基本公式

                      ![The quadratic
                      formula](https://filecdn.minimax.chat/public/d6f62e9a-cd3f-4f55-a237-257eef531683.png)


                      应表示为 `$$x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}$$`
                    required: false
              - name: audio_setting
                type: object
                required: false
                properties:
                  - name: sample_rate
                    type: integer
                    description: >-
                      生成音频的采样率。可选范围 `[8000，16000，22050，24000，32000，44100]`，默认为
                      `32000`
                    required: false
                  - name: bitrate
                    type: integer
                    description: >-
                      生成音频的比特率。可选范围 `[32000，64000，128000，256000]`，默认值为
                      `128000`。该参数仅对 `mp3` 格式的音频生效
                    required: false
                  - name: format
                    type: string
                    description: >-
                      生成音频的格式。`pcmu_raw` 与 `pcmu_wav` 为 G.711 μ-law 编码（采样率 8
                      kHz；`pcmu_raw` 为无文件头裸数据，`pcmu_wav` 封装在 WAV 容器中）。`opus` 为
                      Ogg/Opus 编码；流式模式下音频 chunk 需按到达顺序拼接后再解码
                    enumValues:
                      - mp3
                      - pcm
                      - flac
                      - wav
                      - pcmu_raw
                      - pcmu_wav
                      - opus
                    required: false
                  - name: channel
                    type: integer
                    description: 生成音频的声道数。可选范围：`[1,2]`，其中 `1` 为单声道，`2` 为双声道，默认值为 1
                    required: false
              - name: pronunciation_dict
                type: object
                required: false
                properties:
                  - name: tone
                    type: array
                    description: |-
                      定义需要特殊标注的文字或符号对应的注音或发音替换规则。在中文文本中，声调用数字表示：
                      一声为 1，二声为 2，三声为 3，四声为 4，轻声为 5
                      示例如下：
                      `["燕少飞/(yan4)(shao3)(fei1)", "omg/oh my god"]`
                    required: false
                    properties:
                      - name: item
                        type: string
                        required: false
              - name: timbre_weights
                type: object
                required: false
                properties:
                  - name: voice_id
                    type: string
                    description: >-
                      合成音频的音色编号，须和weight参数同步填写。支持系统音色、复刻音色以及文生音色三种类型。系统支持的全部音色可查看
                      [系统音色列表](/faq/system-voice-id)，也可使用 [查询可用音色
                      API](/api-reference/voice-management-get) 查询系统支持的全部音色
                    required: false
                  - name: weight
                    type: integer
                    description: >-
                      合成音频各音色所占的权重，须与 voice_id 同步填写。可选值范围为[1, 100]，最多支持 4
                      种音色混合，单一音色取值占比越高，合成音色与该音色相似度越高.


                      ```json dark

                      "timbre_weights": [
                        {
                          "voice_id": "female-chengshu",
                          "weight": 30
                        },
                        {
                          "voice_id": "female-tianmei",
                          "weight": 70
                        }
                      ]

                      ```
                    required: false
              - name: language_boost
                type: string
                description: >-
                  是否增强对指定的小语种和方言的识别能力，设置后可以提升在指定小语种/方言场景下的语音表现。默认值为
                  `null`，如果不明确小语种类型，可设置为 `auto`，模型将自主判断小语种类型

                  可选值范围： 

                  [`Chinese`, `Chinese,Yue`, `English`, `Arabic`, `Russian`,
                  `Spanish`, `French`, `Portuguese`, `German`, `Turkish`,
                  `Dutch`, `Ukrainian`, `Vietnamese`, `Indonesian`, `Japanese`,
                  `Italian`, `Korean`, `Thai`, `Polish`, `Romanian`, `Greek`,
                  `Czech`, `Finnish`, `Hindi`, `Bulgarian`, `Danish`, `Hebrew`,
                  `Malay`, `Persian`, `Slovak`, `Swedish`, `Croatian`,
                  `Filipino`, `Hungarian`, `Norwegian`, `Slovenian`, `Catalan`,
                  `Nynorsk`, `Tamil`, `Afrikaans`, `auto`]


                  注意：speech-01 和 speech-02 系列模型暂不支持 Persian、Filipino、Tamil
                  这三个语种。
                enumValues:
                  - Chinese
                  - Chinese,Yue
                  - English
                  - Arabic
                  - Russian
                  - Spanish
                  - French
                  - Portuguese
                  - German
                  - Turkish
                  - Dutch
                  - Ukrainian
                  - Vietnamese
                  - Indonesian
                  - Japanese
                  - Italian
                  - Korean
                  - Thai
                  - Polish
                  - Romanian
                  - Greek
                  - Czech
                  - Finnish
                  - Hindi
                  - Bulgarian
                  - Danish
                  - Hebrew
                  - Malay
                  - Persian
                  - Slovak
                  - Swedish
                  - Croatian
                  - Filipino
                  - Hungarian
                  - Norwegian
                  - Slovenian
                  - Catalan
                  - Nynorsk
                  - Tamil
                  - Afrikaans
                  - auto
                required: false
              - name: voice_modify
                type: object
                description: 声音效果器设置
                required: false
                properties:
                  - name: pitch
                    type: integer
                    description: >-
                      音高调整（低沉/明亮），范围 [-100,100]，数值接近 -100，声音更低沉；接近 100，声音更明亮


                      ![pitch
                      adjustment](https://filecdn.minimax.chat/public/5d210c47-4236-4e81-893b-16cc1ef0302d.png)
                    required: false
                  - name: intensity
                    type: integer
                    description: >-
                      强度调整（力量感/柔和），范围 [-100,100]，数值接近 -100，声音更刚劲；接近 100，声音更轻柔


                      ![intensity
                      adjustment](https://filecdn.minimax.chat/public/862d493e-71d5-4d1f-b7c3-9ac51890631b.png)
                    required: false
                  - name: timbre
                    type: integer
                    description: >-
                      音色调整（磁性/清脆），范围 [-100,100]，数值接近 -100，声音更浑厚；数值接近 100，声音更清脆


                      ![timbre
                      adjustment](https://filecdn.minimax.chat/public/5f0e6cae-363a-452b-8d42-fbc4ef5a0510.png)
                    required: false
                  - name: sound_effects
                    type: string
                    description: |-
                      音效设置，单次仅能选择一种，可选值：
                      1. spacious_echo（空旷回音）
                      2. auditorium_echo（礼堂广播）
                      3. lofi_telephone（电话失真）
                      4. robotic（电音）
                    enumValues:
                      - spacious_echo
                      - auditorium_echo
                      - lofi_telephone
                      - robotic
                    required: false
              - name: subtitle_enable
                type: boolean
                description: >-
                  控制是否开启字幕服务，默认值为 `false`。仅对 `speech-2.8-hd`,
                  `speech-2.8-turbo`, `speech-2.6-hd`, `speech-2.6-turbo`,
                  `speech-02-hd`, `speech-02-turbo`, `speech-01-hd`,
                  `speech-01-turbo` 模型有效
                required: false
              - name: subtitle_type
                type: string
                description: >-
                  字幕粒度，默认值为 `sentence`。可选值：

                  - `sentence`：句级别时间戳

                  - `word`：词级别时间戳

                  - `word_streaming`：流式优化的词级别时间戳


                  字幕通过 `task_continued` 事件的 `data.subtitle` 随音频下发，不提供字幕文件：

                  - `sentence` / `word`：每个分段只在该分段最后一个音频片段中返回一次完整字幕，`sentence` 不含
                  `timestamped_words`

                  - `word_streaming`：每个音频片段都返回当前分段截至目前的累计字幕（`timestamped_words`
                  与 `time_end` 持续增长），客户端应以最新一条覆盖同一分段的旧结果；`text_begin`
                  变化表示进入下一个分段


                  `is_final` 为 `true` 的消息不含字幕，请在每条 `task_continued` 消息中检查
                  `data.subtitle`


                  双向模式下服务端按句合成，每句（一组 `sentence_start` … `sentence_end`）独立计时：字幕中的
                  `time_begin` / `time_end` 与 `text_begin` / `text_end` 均相对当前句，从
                  0 开始
                enumValues:
                  - sentence
                  - word
                  - word_streaming
                required: false
              - name: continuous_sound
                type: boolean
                description: |-
                  控制模型侧文本切分策略，仅对 `speech-2.8-hd`、`speech-2.8-turbo` 模型有效。
                  - `true`：模型侧不切分文本，连续推理生成音频（长文本韵律更自然）
                  - `false`：模型侧切分文本，并发推理生成音频（延迟更低）

                  默认值为 `false`
                required: false
              - name: session_id
                type: string
                description: >-
                  会话 id，由客户端生成，用于标识本次合成会话。可不传，不传时服务端使用 `connect_id`
                  兜底。该字段仅作透传回显，便于客户端串联自己的会话上下文
                required: false
        headers: []
        jsonPayloadSchema:
          type: object
          required:
            - event
            - model
            - voice_setting
          properties:
            event:
              type: string
              enum:
                - task_start
              default:
                - task_start
              description: 控制发送的指令，当前环节应填写： `task_start`
              x-parser-schema-id: <anonymous-schema-7>
            model:
              type: string
              description: 请求的模型版本
              enum:
                - speech-2.8-hd
                - speech-2.8-turbo
                - speech-2.6-hd
                - speech-2.6-turbo
                - speech-02-hd
                - speech-02-turbo
                - speech-01-hd
                - speech-01-turbo
              x-parser-schema-id: <anonymous-schema-8>
            voice_setting:
              type: object
              required:
                - voice_id
              properties:
                voice_id:
                  type: string
                  description: "合成音频的音色编号。若需要设置混合音色，请设置 timbre_weights 参数，本参数设置为空值。支持系统音色、复刻音色以及文生音色三种类型，以下是部分最新的系统音色（ID），可查看 [系统音色列表](/faq/system-voice-id) 或使用 [查询可用音色 API](/api-reference/voice-management-get) 查询系统支持的全部音色\n\n - **中文**:\n\t- moss_audio_ce44fc67-7ce3-11f0-8de5-96e35d26fb85\n\t- moss_audio_aaa1346a-7ce7-11f0-8e61-2e6e3c7ee85d\n\t- Chinese (Mandarin)_Lyrical_Voice\n\t- Chinese (Mandarin)_HK_Flight_Attendant\n- **英文**:\n\t- English_Graceful_Lady\n\t- English_Insightful_Speaker\n\t- English_radiant_girl\n\t- English_Persuasive_Man\n\t- moss_audio_6dc281eb-713c-11f0-a447-9613c873494c\n\t- moss_audio_570551b1-735c-11f0-b236-0adeeecad052\n\t- moss_audio_ad5baf92-735f-11f0-8263-fe5a2fe98ec8\n\t- English_Lucky_Robot\n- **日文**:\n\t- Japanese_Whisper_Belle\n\t- moss_audio_24875c4a-7be4-11f0-9359-4e72c55db738\n\t- moss_audio_7f4ee608-78ea-11f0-bb73-1e2a4cfcd245\n\t- moss_audio_c1a6a3ac-7be6-11f0-8e8e-36b92fbb4f95"
                  x-parser-schema-id: <anonymous-schema-9>
                speed:
                  type: number
                  format: float
                  description: 合成音频的语速，取值越大，语速越快。取值范围 `[0.5,2]`，默认值为1.0
                  minimum: 0.5
                  maximum: 2
                  default: 1
                  x-parser-schema-id: <anonymous-schema-10>
                vol:
                  type: number
                  format: float
                  description: 合成音频的音量，取值越大，音量越高。取值范围 `(0,10]`，默认值为 1.0
                  exclusiveMinimum: 0
                  maximum: 10
                  default: 1
                  x-parser-schema-id: <anonymous-schema-11>
                pitch:
                  type: integer
                  description: 合成音频的语调，取值范围 `[-12,12]`，默认值为 0，其中 0 为原音色输出
                  minimum: -12
                  maximum: 12
                  default: 0
                  x-parser-schema-id: <anonymous-schema-12>
                emotion:
                  type: string
                  description: "控制合成语音的情绪，参数范围 `[\"happy\", \"sad\", \"angry\", \"fearful\", \"disgusted\", \"surprised\", \"calm\", \"fluent\", \"whisper\"]`，分别对应 8 种情绪：高兴，悲伤，愤怒，害怕，厌恶，惊讶，中性，生动，低语 \r\n- 模型会根据输入文本自动匹配合适的情绪，一般无需手动指定  \r\n- 该参数仅对 `speech-2.8-hd`, `speech-2.8-turbo`, `speech-2.6-hd`, `speech-2.6-turbo`, `speech-02-hd`, `speech-02-turbo`, `speech-01-hd`, `speech-01-turbo` 模型生效 \r\n- 选项 `fluent`, `whisper` 仅对 `speech-2.6-turbo`, `speech-2.6-hd` 模型生效，`speech-2.8-hd`, `speech-2.8-turbo` 模型不支持 `whisper`"
                  enum:
                    - happy
                    - sad
                    - angry
                    - fearful
                    - disgusted
                    - surprised
                    - calm
                    - fluent
                    - whisper
                  x-parser-schema-id: <anonymous-schema-13>
                english_normalization:
                  type: boolean
                  description: 该参数支持英语文本规范化，可提升数字阅读场景的性能，但会略微增加延迟，默认值为 `false`
                  default: false
                  x-parser-schema-id: <anonymous-schema-14>
                latex_read:
                  type: boolean
                  description: >-
                    控制是否朗读 latex 公式，默认为 `false`

                    **需注意**:

                    - 仅支持中文，开启该参数后，`language_boost` 参数会被设置为 `Chinese`

                    - 请求中的公式需要在公式的首尾加上 `$$`

                    - 请求中公式若有 `"\"`，需转义成 `"\\"`.


                    示例：一元二次方程根的基本公式

                    ![The quadratic
                    formula](https://filecdn.minimax.chat/public/d6f62e9a-cd3f-4f55-a237-257eef531683.png)


                    应表示为 `$$x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}$$`
                  default: false
                  x-parser-schema-id: <anonymous-schema-15>
              x-parser-schema-id: VoiceSetting
            audio_setting:
              type: object
              properties:
                sample_rate:
                  type: integer
                  format: int64
                  description: >-
                    生成音频的采样率。可选范围 `[8000，16000，22050，24000，32000，44100]`，默认为
                    `32000`
                  x-parser-schema-id: <anonymous-schema-16>
                bitrate:
                  type: integer
                  format: int64
                  description: >-
                    生成音频的比特率。可选范围 `[32000，64000，128000，256000]`，默认值为
                    `128000`。该参数仅对 `mp3` 格式的音频生效
                  x-parser-schema-id: <anonymous-schema-17>
                format:
                  type: string
                  description: >-
                    生成音频的格式。`pcmu_raw` 与 `pcmu_wav` 为 G.711 μ-law 编码（采样率 8
                    kHz；`pcmu_raw` 为无文件头裸数据，`pcmu_wav` 封装在 WAV 容器中）。`opus` 为
                    Ogg/Opus 编码；流式模式下音频 chunk 需按到达顺序拼接后再解码
                  enum:
                    - mp3
                    - pcm
                    - flac
                    - wav
                    - pcmu_raw
                    - pcmu_wav
                    - opus
                  default: mp3
                  x-parser-schema-id: <anonymous-schema-18>
                channel:
                  type: integer
                  format: int64
                  description: 生成音频的声道数。可选范围：`[1,2]`，其中 `1` 为单声道，`2` 为双声道，默认值为 1
                  x-parser-schema-id: <anonymous-schema-19>
              x-parser-schema-id: AudioSetting
            pronunciation_dict:
              type: object
              properties:
                tone:
                  type: array
                  items:
                    type: string
                    x-parser-schema-id: <anonymous-schema-21>
                  description: |-
                    定义需要特殊标注的文字或符号对应的注音或发音替换规则。在中文文本中，声调用数字表示：
                    一声为 1，二声为 2，三声为 3，四声为 4，轻声为 5
                    示例如下：
                    `["燕少飞/(yan4)(shao3)(fei1)", "omg/oh my god"]`
                  x-parser-schema-id: <anonymous-schema-20>
              x-parser-schema-id: PronunciationDict
            timbre_weights:
              type: object
              properties:
                voice_id:
                  type: string
                  description: >-
                    合成音频的音色编号，须和weight参数同步填写。支持系统音色、复刻音色以及文生音色三种类型。系统支持的全部音色可查看
                    [系统音色列表](/faq/system-voice-id)，也可使用 [查询可用音色
                    API](/api-reference/voice-management-get) 查询系统支持的全部音色
                  x-parser-schema-id: <anonymous-schema-22>
                weight:
                  type: integer
                  format: int64
                  description: >-
                    合成音频各音色所占的权重，须与 voice_id 同步填写。可选值范围为[1, 100]，最多支持 4
                    种音色混合，单一音色取值占比越高，合成音色与该音色相似度越高.


                    ```json dark

                    "timbre_weights": [
                      {
                        "voice_id": "female-chengshu",
                        "weight": 30
                      },
                      {
                        "voice_id": "female-tianmei",
                        "weight": 70
                      }
                    ]

                    ```
                  minimum: 1
                  maximum: 100
                  x-parser-schema-id: <anonymous-schema-23>
              x-parser-schema-id: TimbreWeights
            language_boost:
              type: string
              description: >-
                是否增强对指定的小语种和方言的识别能力，设置后可以提升在指定小语种/方言场景下的语音表现。默认值为
                `null`，如果不明确小语种类型，可设置为 `auto`，模型将自主判断小语种类型

                可选值范围： 

                [`Chinese`, `Chinese,Yue`, `English`, `Arabic`, `Russian`,
                `Spanish`, `French`, `Portuguese`, `German`, `Turkish`, `Dutch`,
                `Ukrainian`, `Vietnamese`, `Indonesian`, `Japanese`, `Italian`,
                `Korean`, `Thai`, `Polish`, `Romanian`, `Greek`, `Czech`,
                `Finnish`, `Hindi`, `Bulgarian`, `Danish`, `Hebrew`, `Malay`,
                `Persian`, `Slovak`, `Swedish`, `Croatian`, `Filipino`,
                `Hungarian`, `Norwegian`, `Slovenian`, `Catalan`, `Nynorsk`,
                `Tamil`, `Afrikaans`, `auto`]


                注意：speech-01 和 speech-02 系列模型暂不支持 Persian、Filipino、Tamil 这三个语种。
              enum:
                - Chinese
                - Chinese,Yue
                - English
                - Arabic
                - Russian
                - Spanish
                - French
                - Portuguese
                - German
                - Turkish
                - Dutch
                - Ukrainian
                - Vietnamese
                - Indonesian
                - Japanese
                - Italian
                - Korean
                - Thai
                - Polish
                - Romanian
                - Greek
                - Czech
                - Finnish
                - Hindi
                - Bulgarian
                - Danish
                - Hebrew
                - Malay
                - Persian
                - Slovak
                - Swedish
                - Croatian
                - Filipino
                - Hungarian
                - Norwegian
                - Slovenian
                - Catalan
                - Nynorsk
                - Tamil
                - Afrikaans
                - auto
              x-parser-schema-id: <anonymous-schema-24>
            voice_modify:
              type: object
              description: 声音效果器设置
              properties:
                pitch:
                  type: integer
                  description: >-
                    音高调整（低沉/明亮），范围 [-100,100]，数值接近 -100，声音更低沉；接近 100，声音更明亮


                    ![pitch
                    adjustment](https://filecdn.minimax.chat/public/5d210c47-4236-4e81-893b-16cc1ef0302d.png)
                  minimum: -100
                  maximum: 100
                  x-parser-schema-id: <anonymous-schema-25>
                intensity:
                  type: integer
                  description: >-
                    强度调整（力量感/柔和），范围 [-100,100]，数值接近 -100，声音更刚劲；接近 100，声音更轻柔


                    ![intensity
                    adjustment](https://filecdn.minimax.chat/public/862d493e-71d5-4d1f-b7c3-9ac51890631b.png)
                  minimum: -100
                  maximum: 100
                  x-parser-schema-id: <anonymous-schema-26>
                timbre:
                  type: integer
                  description: >-
                    音色调整（磁性/清脆），范围 [-100,100]，数值接近 -100，声音更浑厚；数值接近 100，声音更清脆


                    ![timbre
                    adjustment](https://filecdn.minimax.chat/public/5f0e6cae-363a-452b-8d42-fbc4ef5a0510.png)
                  minimum: -100
                  maximum: 100
                  x-parser-schema-id: <anonymous-schema-27>
                sound_effects:
                  type: string
                  description: |-
                    音效设置，单次仅能选择一种，可选值：
                    1. spacious_echo（空旷回音）
                    2. auditorium_echo（礼堂广播）
                    3. lofi_telephone（电话失真）
                    4. robotic（电音）
                  enum:
                    - spacious_echo
                    - auditorium_echo
                    - lofi_telephone
                    - robotic
                  x-parser-schema-id: <anonymous-schema-28>
              x-parser-schema-id: VoiceModify
            subtitle_enable:
              type: boolean
              description: >-
                控制是否开启字幕服务，默认值为 `false`。仅对 `speech-2.8-hd`, `speech-2.8-turbo`,
                `speech-2.6-hd`, `speech-2.6-turbo`, `speech-02-hd`,
                `speech-02-turbo`, `speech-01-hd`, `speech-01-turbo` 模型有效
              default: false
              x-parser-schema-id: <anonymous-schema-29>
            subtitle_type:
              type: string
              description: >-
                字幕粒度，默认值为 `sentence`。可选值：

                - `sentence`：句级别时间戳

                - `word`：词级别时间戳

                - `word_streaming`：流式优化的词级别时间戳


                字幕通过 `task_continued` 事件的 `data.subtitle` 随音频下发，不提供字幕文件：

                - `sentence` / `word`：每个分段只在该分段最后一个音频片段中返回一次完整字幕，`sentence` 不含
                `timestamped_words`

                - `word_streaming`：每个音频片段都返回当前分段截至目前的累计字幕（`timestamped_words` 与
                `time_end` 持续增长），客户端应以最新一条覆盖同一分段的旧结果；`text_begin` 变化表示进入下一个分段


                `is_final` 为 `true` 的消息不含字幕，请在每条 `task_continued` 消息中检查
                `data.subtitle`


                双向模式下服务端按句合成，每句（一组 `sentence_start` … `sentence_end`）独立计时：字幕中的
                `time_begin` / `time_end` 与 `text_begin` / `text_end` 均相对当前句，从 0
                开始
              enum:
                - sentence
                - word
                - word_streaming
              default: sentence
              x-parser-schema-id: <anonymous-schema-30>
            continuous_sound:
              type: boolean
              description: |-
                控制模型侧文本切分策略，仅对 `speech-2.8-hd`、`speech-2.8-turbo` 模型有效。
                - `true`：模型侧不切分文本，连续推理生成音频（长文本韵律更自然）
                - `false`：模型侧切分文本，并发推理生成音频（延迟更低）

                默认值为 `false`
              default: false
              x-parser-schema-id: <anonymous-schema-31>
            session_id:
              type: string
              description: >-
                会话 id，由客户端生成，用于标识本次合成会话。可不传，不传时服务端使用 `connect_id`
                兜底。该字段仅作透传回显，便于客户端串联自己的会话上下文
              x-parser-schema-id: <anonymous-schema-32>
          x-parser-schema-id: SendTaskStartEvent
        title: 任务开始
        description: |-
          发送`任务开始`事件则正式开始合成任务，当服务端返回的 `task_started` 事件时，标志着任务已成功开始。
          只有在接收到该事件后，才能向服务器发送 `task_continue` 事件或 `task_finish` 事件。
        example: |-
          {
            "event": "task_start",
            "model": "speech-2.8-turbo",
            "language_boost": "Chinese",
            "voice_setting": {
              "voice_id": "male-qn-qingse",
              "speed": 1,
              "vol": 1,
              "pitch": 0
            },
            "pronunciation_dict": {
              "tone": [
                "处理/(chu3)(li3)",
                "危险/dangerous"
              ]
            },
            "audio_setting": {
              "sample_rate": 32000,
              "bitrate": 128000,
              "format": "mp3",
              "channel": 1
            },
            "session_id": "my-session-001"
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: send_task_start
      - &ref_6
        id: send_task_continue
        contentType: application/json
        payload:
          - name: 任务继续
            description: >-
              当收到服务端返回的 `task_started` 事件后，任务正式开始，可通过发送 `task_continue`
              事件发送要合成的文本。


              与 `/ws/v1/t2a_v2`
              的关键区别：**本接口的文本不会一条一次合成**，而是进入服务端的攒句缓冲，按下列规则成句后才送去合成，因此可以安全地按逐字/逐
              token 粒度发送：

              - 遇到句末标点（`。！？…；!?.` 及换行）立即合成

              - 遇到次级标点（`，、：,;:`）且已攒够长度时合成

              - 累计长度达到上限时强制切分

              - 停止发送超过一定时间后，自动合成缓冲区中的残留文本


              纯空白文本会被静默丢弃，不会返回错误。

              当最后一次收到服务端返回结果后超过 120s 没有发送新事件时，WebSocket 连接自动断开。
            type: object
            properties:
              - name: event
                type: string
                description: 表示会话事件类型，当前环节应填写 `task_continue`
                enumValues:
                  - task_continue
                required: true
              - name: text
                type: string
                description: >-
                  需要合成语音的文本，长度限制小于 10,000 字符。


                  **可按任意粒度发送**（包括单个字符），服务端会自动攒句，无需客户端自行判断句子边界。


                  - 段落切换用换行符标记

                  - 停顿控制：支持自定义文本之间的语音时间间隔。使用方式：在文本中增加 `<#x#>` 标记，`x`
                  为停顿时长（单位：秒），范围 **[0.01,
                  99.99]**，最多保留两位小数。文本间隔时间需设置在两个可以语音发音的文本之间，不可连续使用多个停顿标记

                  - 语气词标签：仅当模型选择 `speech-2.8-hd` 或 `speech-2.8-turbo`
                  时，支持在文本中插入语气词标签。支持的语气词：`(laughs)`（笑声）、`(chuckle)`（轻笑）、`(coughs)`（咳嗽）、`(clear-throat)`（清嗓子）、`(groans)`（呻吟）、`(breath)`（正常换气）、`(pant)`（喘气）、`(inhale)`（吸气）、`(exhale)`（呼气）、`(gasps)`（倒吸气）、`(sniffs)`（吸鼻子）、`(sighs)`（叹气）、`(snorts)`（喷鼻息）、`(burps)`（打嗝）、`(lip-smacking)`（咂嘴）、`(humming)`（哼唱）、`(hissing)`（嘶嘶声）、`(emm)`（嗯）、`(sneezes)`（喷嚏）
                required: true
        headers: []
        jsonPayloadSchema:
          type: object
          required:
            - event
            - text
          properties:
            event:
              type: string
              description: 表示会话事件类型，当前环节应填写 `task_continue`
              enum:
                - task_continue
              default:
                - task_continue
              x-parser-schema-id: <anonymous-schema-39>
            text:
              type: string
              description: >-
                需要合成语音的文本，长度限制小于 10,000 字符。


                **可按任意粒度发送**（包括单个字符），服务端会自动攒句，无需客户端自行判断句子边界。


                - 段落切换用换行符标记

                - 停顿控制：支持自定义文本之间的语音时间间隔。使用方式：在文本中增加 `<#x#>` 标记，`x`
                为停顿时长（单位：秒），范围 **[0.01,
                99.99]**，最多保留两位小数。文本间隔时间需设置在两个可以语音发音的文本之间，不可连续使用多个停顿标记

                - 语气词标签：仅当模型选择 `speech-2.8-hd` 或 `speech-2.8-turbo`
                时，支持在文本中插入语气词标签。支持的语气词：`(laughs)`（笑声）、`(chuckle)`（轻笑）、`(coughs)`（咳嗽）、`(clear-throat)`（清嗓子）、`(groans)`（呻吟）、`(breath)`（正常换气）、`(pant)`（喘气）、`(inhale)`（吸气）、`(exhale)`（呼气）、`(gasps)`（倒吸气）、`(sniffs)`（吸鼻子）、`(sighs)`（叹气）、`(snorts)`（喷鼻息）、`(burps)`（打嗝）、`(lip-smacking)`（咂嘴）、`(humming)`（哼唱）、`(hissing)`（嘶嘶声）、`(emm)`（嗯）、`(sneezes)`（喷嚏）
              x-parser-schema-id: <anonymous-schema-40>
          x-parser-schema-id: SendTaskContinueEvent
        title: 任务继续
        description: >-
          当收到服务端返回的 `task_started` 事件后，任务正式开始，可通过发送 `task_continue` 事件发送要合成的文本。


          与 `/ws/v1/t2a_v2`
          的关键区别：**本接口的文本不会一条一次合成**，而是进入服务端的攒句缓冲，按下列规则成句后才送去合成，因此可以安全地按逐字/逐 token
          粒度发送：

          - 遇到句末标点（`。！？…；!?.` 及换行）立即合成

          - 遇到次级标点（`，、：,;:`）且已攒够长度时合成

          - 累计长度达到上限时强制切分

          - 停止发送超过一定时间后，自动合成缓冲区中的残留文本


          纯空白文本会被静默丢弃，不会返回错误。

          当最后一次收到服务端返回结果后超过 120s 没有发送新事件时，WebSocket 连接自动断开。
        example: |-
          {
            "event": "task_continue",
            "text": "真正的危险不是计算机开始像人一样思考(sighs)，而是人开始像计算机一样思考。计算机只是可以帮我们处理一些简单事务。"
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: send_task_continue
      - &ref_7
        id: send_task_cancel
        contentType: application/json
        payload:
          - name: 打断合成
            description: >-
              发送 `task_cancel` 事件可立即打断当前合成：服务端会丢弃攒句缓冲区中尚未合成的文本、中断正在进行的合成，并返回
              `task_canceled` 事件。


              已经发送给客户端的音频不会撤回。


              打断后会话回到 `task_started` 状态，**可以继续发送 `task_continue`
              继续合成**，无需重建连接。适用于实时对话中用户插话打断的场景。
            type: object
            properties:
              - name: event
                type: string
                description: 表示会话事件类型，当前环节应填写 `task_cancel`
                enumValues:
                  - task_cancel
                required: true
        headers: []
        jsonPayloadSchema:
          type: object
          required:
            - event
          properties:
            event:
              type: string
              enum:
                - task_cancel
              default:
                - task_cancel
              description: 表示会话事件类型，当前环节应填写 `task_cancel`
              x-parser-schema-id: <anonymous-schema-89>
          x-parser-schema-id: SendTaskCancelEvent
        title: 打断合成
        description: >-
          发送 `task_cancel` 事件可立即打断当前合成：服务端会丢弃攒句缓冲区中尚未合成的文本、中断正在进行的合成，并返回
          `task_canceled` 事件。


          已经发送给客户端的音频不会撤回。


          打断后会话回到 `task_started` 状态，**可以继续发送 `task_continue`
          继续合成**，无需重建连接。适用于实时对话中用户插话打断的场景。
        example: |-
          {
            "event": "task_cancel"
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: send_task_cancel
      - &ref_8
        id: send_task_flush
        contentType: application/json
        payload:
          - name: 催出残留（不结束会话）
            description: >-
              发送 `task_flush` 事件，让服务端立即把攒句缓冲区里剩余的文本送去合成，但**不结束会话、不关闭连接**。合成完毕后返回
              `task_flushed`。


              适用场景：一轮说完了，而最后一片文本很短又不带句末标点。这种残留不会被静默窗口立刻送出（那是为了避免在词中间切开），需要等一个更长的兜底窗口。发
              `task_flush` 可以立刻拿到这段音频。


              与 `task_finish` 的区别：`task_finish`
              会关闭连接，因此在一条连接上进行多轮对话时无法用它催出某一轮的尾句；`task_flush` 之后会话仍处于
              `task_started` 状态，可以继续发送 `task_continue`。


              缓冲区恰好为空时也会正常返回 `task_flushed`，不算错误。
            type: object
            properties:
              - name: event
                type: string
                description: 表示会话事件类型，当前环节应填写 `task_flush`
                enumValues:
                  - task_flush
                required: true
        headers: []
        jsonPayloadSchema:
          type: object
          required:
            - event
          properties:
            event:
              type: string
              enum:
                - task_flush
              default:
                - task_flush
              description: 表示会话事件类型，当前环节应填写 `task_flush`
              x-parser-schema-id: <anonymous-schema-73>
          x-parser-schema-id: SendTaskFlushEvent
        title: 催出残留（不结束会话）
        description: >-
          发送 `task_flush` 事件，让服务端立即把攒句缓冲区里剩余的文本送去合成，但**不结束会话、不关闭连接**。合成完毕后返回
          `task_flushed`。


          适用场景：一轮说完了，而最后一片文本很短又不带句末标点。这种残留不会被静默窗口立刻送出（那是为了避免在词中间切开），需要等一个更长的兜底窗口。发
          `task_flush` 可以立刻拿到这段音频。


          与 `task_finish` 的区别：`task_finish`
          会关闭连接，因此在一条连接上进行多轮对话时无法用它催出某一轮的尾句；`task_flush` 之后会话仍处于 `task_started`
          状态，可以继续发送 `task_continue`。


          缓冲区恰好为空时也会正常返回 `task_flushed`，不算错误。
        example: |-
          {
            "event": "task_flush"
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: send_task_flush
      - &ref_9
        id: send_task_finish
        contentType: application/json
        payload:
          - name: 任务结束
            description: >-
              服务端收到 `task_finish` 事件后，会先把攒句缓冲区中剩余的文本送去合成，等全部音频返回后才回复
              `task_finished` 并关闭连接。


              因此**最后一句不完整的文本也不会丢失**，无需客户端在结束前补一个标点。
            type: object
            properties:
              - name: event
                type: string
                description: 表示会话事件类型，当前环节应填写 `task_finish`
                enumValues:
                  - task_finish
                required: true
        headers: []
        jsonPayloadSchema:
          type: object
          required:
            - event
          properties:
            event:
              type: string
              enum:
                - task_finish
              default:
                - task_finish
              description: 表示会话事件类型，当前环节应填写 `task_finish`
              x-parser-schema-id: <anonymous-schema-78>
          x-parser-schema-id: SendTaskFinishEvent
        title: 任务结束
        description: >-
          服务端收到 `task_finish` 事件后，会先把攒句缓冲区中剩余的文本送去合成，等全部音频返回后才回复 `task_finished`
          并关闭连接。


          因此**最后一句不完整的文本也不会丢失**，无需客户端在结束前补一个标点。
        example: |-
          {
            "event": "task_finish"
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: send_task_finish
    bindings: []
    extensions: &ref_2
      - id: x-parser-unique-object-id
        value: t2a_v2_bidi_websocket
  - &ref_4
    id: receiveMessage
    title: Receive message
    type: send
    messages:
      - &ref_10
        id: receive_connected_success
        contentType: application/json
        payload:
          - name: 建连成功
            description: 成功建立连接后会返回 `connected_success` 事件
            type: object
            properties:
              - name: session_id
                type: string
                description: 表示整个会话的 id
                required: false
              - name: event
                type: string
                description: 表示会话事件类型，建连成功后会返回`connected_success`
                required: false
              - name: trace_id
                type: string
                description: 表示会话中单次请求的 id，用于在咨询/反馈时帮助定位问题
                required: false
              - name: base_resp
                type: object
                required: false
                properties:
                  - name: status_code
                    type: integer
                    description: |-
                      状态码，`0`代表建连成功.
                      更多状态码信息请参考 [错误码查询列表](/api-reference/errorcode)
                    required: false
                  - name: status_msg
                    type: string
                    description: 该请求对应的状态码和详情
                    required: false
              - name: connect_id
                type: string
                description: >-
                  表示当前 WebSocket 连接的 id。与 `session_id` 区分：一个连接对应一个
                  `connect_id`，`session_id` 标识连接内的合成会话
                required: false
        headers: []
        jsonPayloadSchema:
          type: object
          properties:
            session_id:
              type: string
              description: 表示整个会话的 id
              x-parser-schema-id: <anonymous-schema-1>
            event:
              type: string
              const: connected_success
              description: 表示会话事件类型，建连成功后会返回`connected_success`
              x-parser-schema-id: <anonymous-schema-2>
            trace_id:
              type: string
              description: 表示会话中单次请求的 id，用于在咨询/反馈时帮助定位问题
              x-parser-schema-id: <anonymous-schema-3>
            base_resp: &ref_0
              type: object
              properties:
                status_code:
                  type: integer
                  description: |-
                    状态码，`0`代表建连成功.
                    更多状态码信息请参考 [错误码查询列表](/api-reference/errorcode)
                  x-parser-schema-id: <anonymous-schema-4>
                status_msg:
                  type: string
                  description: 该请求对应的状态码和详情
                  x-parser-schema-id: <anonymous-schema-5>
              x-parser-schema-id: BaseResp
            connect_id:
              type: string
              description: >-
                表示当前 WebSocket 连接的 id。与 `session_id` 区分：一个连接对应一个
                `connect_id`，`session_id` 标识连接内的合成会话
              x-parser-schema-id: <anonymous-schema-6>
          x-parser-schema-id: ReceiveConnectedSuccessEvent
        title: 建连成功
        description: 成功建立连接后会返回 `connected_success` 事件
        example: |-
          {
            "session_id": "xxxx",
            "event": "connected_success",
            "trace_id": "0303a2882bf18235ae7a809ae0f3cca7",
            "base_resp": {
              "status_code": 0,
              "status_msg": "success"
            },
            "connect_id": "301871346491491"
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: receive_connected_success
      - &ref_11
        id: receive_task_started
        contentType: application/json
        payload:
          - name: 任务开始
            description: 服务端返回 `task_started` 事件，标志着任务已成功开始
            type: object
            properties:
              - name: session_id
                type: string
                description: 表示整个会话的 id
                required: false
              - name: event
                type: string
                description: 表示会话事件类型，当前环节成功后会返回 `task_started`
                required: false
              - name: trace_id
                type: string
                description: 表示会话中单次请求的 id，用于在咨询/反馈时帮助定位问题
                required: false
              - name: base_resp
                type: object
                description: 该请求对应的状态码和详情
                required: false
                properties:
                  - name: status_code
                    type: integer
                    description: |-
                      状态码。
                      - 0: 表示发送成功
                      - 2202: 表示非法事件
                      更多内容可查看 [错误码查询列表](/api-reference/errorcode) 了解详情
                    required: false
                  - name: status_msg
                    type: string
                    description: 状态详情
                    required: false
              - name: connect_id
                type: string
                description: >-
                  表示当前 WebSocket 连接的 id。与 `session_id` 区分：一个连接对应一个
                  `connect_id`，`session_id` 标识连接内的合成会话
                required: false
        headers: []
        jsonPayloadSchema:
          type: object
          properties:
            session_id:
              type: string
              description: 表示整个会话的 id
              x-parser-schema-id: <anonymous-schema-33>
            event:
              type: string
              const: 表示会话事件类型，当前环节成功后会返回 `task_started`
              x-parser-schema-id: <anonymous-schema-34>
            trace_id:
              type: string
              description: 表示会话中单次请求的 id，用于在咨询/反馈时帮助定位问题
              x-parser-schema-id: <anonymous-schema-35>
            base_resp: &ref_1
              type: object
              description: 该请求对应的状态码和详情
              properties:
                status_code:
                  type: integer
                  description: |-
                    状态码。
                    - 0: 表示发送成功
                    - 2202: 表示非法事件
                    更多内容可查看 [错误码查询列表](/api-reference/errorcode) 了解详情
                  x-parser-schema-id: <anonymous-schema-36>
                status_msg:
                  type: string
                  description: 状态详情
                  x-parser-schema-id: <anonymous-schema-37>
              x-parser-schema-id: TaskStartFinishBaseResp
            connect_id:
              type: string
              description: >-
                表示当前 WebSocket 连接的 id。与 `session_id` 区分：一个连接对应一个
                `connect_id`，`session_id` 标识连接内的合成会话
              x-parser-schema-id: <anonymous-schema-38>
          x-parser-schema-id: ReceiveTaskStartedEvent
        title: 任务开始
        description: 服务端返回 `task_started` 事件，标志着任务已成功开始
        example: |-
          {
            "session_id": "xxxx",
            "event": "task_started",
            "trace_id": "0303a2882bf18235ae7a809ae0f3cca7",
            "base_resp": {
              "status_code": 0,
              "status_msg": "success"
            },
            "connect_id": "301871346491491"
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: receive_task_started
      - &ref_12
        id: receive_sentence_start
        contentType: application/json
        payload:
          - name: 分句开始合成
            description: >-
              服务端攒够一个句子并开始合成时返回 `sentence_start` 事件。随后该句的音频通过 `task_continued`
              事件分块返回，直到 `sentence_end`。


              可用它统计服务端实际把文本攒成了多少句
            type: object
            properties:
              - name: session_id
                type: string
                description: 表示整个会话的 id
                required: false
              - name: connect_id
                type: string
                description: >-
                  表示当前 WebSocket 连接的 id。与 `session_id` 区分：一个连接对应一个
                  `connect_id`，`session_id` 标识连接内的合成会话
                required: false
              - name: event
                type: string
                description: 表示会话事件类型，分句开始合成时会返回 `sentence_start`
                required: false
              - name: trace_id
                type: string
                description: 表示会话中单次请求的 id，用于在咨询/反馈时帮助定位问题
                required: false
              - name: base_resp
                type: object
                required: false
                properties:
                  - name: status_code
                    type: integer
                    description: |-
                      状态码，`0`代表建连成功.
                      更多状态码信息请参考 [错误码查询列表](/api-reference/errorcode)
                    required: false
                  - name: status_msg
                    type: string
                    description: 该请求对应的状态码和详情
                    required: false
        headers: []
        jsonPayloadSchema:
          type: object
          properties:
            session_id:
              type: string
              description: 表示整个会话的 id
              x-parser-schema-id: <anonymous-schema-94>
            connect_id:
              type: string
              description: >-
                表示当前 WebSocket 连接的 id。与 `session_id` 区分：一个连接对应一个
                `connect_id`，`session_id` 标识连接内的合成会话
              x-parser-schema-id: <anonymous-schema-95>
            event:
              type: string
              const: sentence_start
              description: 表示会话事件类型，分句开始合成时会返回 `sentence_start`
              x-parser-schema-id: <anonymous-schema-96>
            trace_id:
              type: string
              description: 表示会话中单次请求的 id，用于在咨询/反馈时帮助定位问题
              x-parser-schema-id: <anonymous-schema-97>
            base_resp: *ref_0
          x-parser-schema-id: ReceiveSentenceStartEvent
        title: 分句开始合成
        description: >-
          服务端攒够一个句子并开始合成时返回 `sentence_start` 事件。随后该句的音频通过 `task_continued`
          事件分块返回，直到 `sentence_end`。


          可用它统计服务端实际把文本攒成了多少句
        example: |-
          {
            "session_id": "my-session-001",
            "connect_id": "301871346491491",
            "event": "sentence_start",
            "trace_id": "0303a2882bf18235ae7a809ae0f3cca7",
            "base_resp": {
              "status_code": 0,
              "status_msg": "success"
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: receive_sentence_start
      - &ref_13
        id: receive_task_continued
        contentType: application/json
        payload:
          - name: 任务继续
            description: 服务端返回 `task_continued` 事件，标志着任务已成功继续
            type: object
            properties:
              - name: data
                type: object
                description: '`data` 可能返回为 `null`，参考示例代码时，注意进行非空判断'
                required: false
                properties:
                  - name: audio
                    type: string
                    description: 合成后的音频片段，采用 `hex` 编码，按照输入定义的格式进行生成（mp3/pcm/flac）
                    required: false
                  - name: subtitle
                    type: object
                    description: >-
                      开启字幕时返回，携带当前分段的字幕，随对应的音频片段下发，返回时机见 `task_start` 的
                      `subtitle_type`。`is_final` 为 `true` 的消息不含该字段
                    required: false
                    properties:
                      - name: text
                        type: string
                        description: 分段文本
                        required: false
                      - name: text_begin
                        type: integer
                        description: 分段在本次合成文本中的起始字符位置（含）
                        required: false
                      - name: text_end
                        type: integer
                        description: 分段在本次合成文本中的结束字符位置（不含）
                        required: false
                      - name: time_begin
                        type: number
                        description: 分段起始时间，单位毫秒，相对本次合成音频的起点
                        required: false
                      - name: time_end
                        type: number
                        description: 分段结束时间，单位毫秒，相对本次合成音频的起点
                        required: false
                      - name: timestamped_words
                        type: array
                        description: >-
                          词级时间戳，仅 `subtitle_type` 为 `word` / `word_streaming`
                          时返回，`sentence` 时为 `null`
                        required: false
                        properties:
                          - name: word
                            type: string
                            description: 词文本
                            required: false
                          - name: word_begin
                            type: integer
                            description: 该词在本次合成文本中的起始字符位置（含）
                            required: false
                          - name: word_end
                            type: integer
                            description: 该词在本次合成文本中的结束字符位置（不含）
                            required: false
                          - name: time_begin
                            type: number
                            description: 该词起始时间，单位毫秒
                            required: false
                          - name: time_end
                            type: number
                            description: 该词结束时间，单位毫秒
                            required: false
              - name: trace_id
                type: string
                description: 表示会话中单次请求的 id，用于在咨询/反馈时帮助定位问题。
                required: false
              - name: session_id
                type: string
                description: 表示整个会话的 id。
                required: false
              - name: event
                type: string
                description: 表示会话类型，当前环节成功后会返回 task_continued`
                required: false
              - name: is_final
                type: boolean
                description: 该请求返回是否完结
                required: false
              - name: extra_info
                type: object
                description: 相关额外信息
                required: false
                properties:
                  - name: audio_length
                    type: integer
                    description: 音频时长，精确到毫秒
                    required: false
                  - name: audio_sample_rate
                    type: integer
                    description: 音频采样率
                    required: false
                  - name: audio_size
                    type: integer
                    description: 音频文件大小，单位为字节
                    required: false
                  - name: bitrate
                    type: integer
                    description: 音频比特率
                    required: false
                  - name: audio_format
                    type: string
                    description: 生成音频文件的格式。取值范围 mp3/pcm/flac
                    required: false
                  - name: audio_channel
                    type: integer
                    description: 生成音频声道数。1：单声道，2：双声道
                    required: false
                  - name: invisible_character_ratio
                    type: integer
                    description: 非法字符占比。非法字符不超过 10%（包含 10%），音频会正常生成并返回非法字符占比，超过进行报错
                    required: false
                  - name: usage_characters
                    type: integer
                    description: 计费字符数。本次语音生成的计费字符数
                    required: false
                  - name: usage_voice_count
                    type: integer
                    description: 本次请求计费的音色数量（音色首次使用时计费），仅在产生音色费用时返回
                    required: false
                  - name: word_count
                    type: integer
                    description: 合成文本的字符数（含标点和空格），仅供参考，不用于计费；计费字符数请以 `usage_characters` 为准
                    required: false
              - name: base_resp
                type: object
                description: 本次请求的状态码和详情
                required: false
                properties:
                  - name: status_code
                    type: integer
                    description: >-
                      状态码

                      - 0: 请求结果正常

                      - 1000: 未知错误

                      - 1001: 请求超时

                      - 1002: 触发限流

                      - 1004: 鉴权失败

                      - 1039: 触发 TPM 限流

                      - 1042: 非法字符超过 10%

                      - 2013: 输入参数信息不正常

                      - 2201: 连接空闲超时，被服务端关闭（见接口说明的「连接保活」一节）

                      - 2202: 非法事件

                      - 2204: 单条 `task_continue` 文本超过 10,000 字符，该条被跳过；连接与会话保持

                      - 2205: 排队待合成的文本过多（发送速度超过合成速度）。**这不是配额限流**：连接与会话均保持，稍后重发该条
                      `task_continue` 即可，不要重连或重新 `task_start`

                      - 2206: 事件顺序非法（如已开始任务后重复发送 `task_start`）


                      注意：本接口对纯空白文本会静默丢弃，不会返回 `2203`。

                      更多内容可查看 [错误码查询列表](/api-reference/errorcode) 了解详情
                    required: false
                  - name: status_msg
                    type: string
                    description: 状态详情
                    required: false
              - name: connect_id
                type: string
                description: >-
                  表示当前 WebSocket 连接的 id。与 `session_id` 区分：一个连接对应一个
                  `connect_id`，`session_id` 标识连接内的合成会话
                required: false
        headers: []
        jsonPayloadSchema:
          type: object
          properties:
            data:
              type: object
              description: '`data` 可能返回为 `null`，参考示例代码时，注意进行非空判断'
              properties:
                audio:
                  type: string
                  description: 合成后的音频片段，采用 `hex` 编码，按照输入定义的格式进行生成（mp3/pcm/flac）
                  x-parser-schema-id: <anonymous-schema-42>
                subtitle:
                  type: object
                  description: >-
                    开启字幕时返回，携带当前分段的字幕，随对应的音频片段下发，返回时机见 `task_start` 的
                    `subtitle_type`。`is_final` 为 `true` 的消息不含该字段
                  properties:
                    text:
                      type: string
                      description: 分段文本
                      x-parser-schema-id: <anonymous-schema-44>
                    text_begin:
                      type: integer
                      format: int64
                      description: 分段在本次合成文本中的起始字符位置（含）
                      x-parser-schema-id: <anonymous-schema-45>
                    text_end:
                      type: integer
                      format: int64
                      description: 分段在本次合成文本中的结束字符位置（不含）
                      x-parser-schema-id: <anonymous-schema-46>
                    time_begin:
                      type: number
                      description: 分段起始时间，单位毫秒，相对本次合成音频的起点
                      x-parser-schema-id: <anonymous-schema-47>
                    time_end:
                      type: number
                      description: 分段结束时间，单位毫秒，相对本次合成音频的起点
                      x-parser-schema-id: <anonymous-schema-48>
                    timestamped_words:
                      type: array
                      description: >-
                        词级时间戳，仅 `subtitle_type` 为 `word` / `word_streaming`
                        时返回，`sentence` 时为 `null`
                      items:
                        type: object
                        properties:
                          word:
                            type: string
                            description: 词文本
                            x-parser-schema-id: <anonymous-schema-51>
                          word_begin:
                            type: integer
                            format: int64
                            description: 该词在本次合成文本中的起始字符位置（含）
                            x-parser-schema-id: <anonymous-schema-52>
                          word_end:
                            type: integer
                            format: int64
                            description: 该词在本次合成文本中的结束字符位置（不含）
                            x-parser-schema-id: <anonymous-schema-53>
                          time_begin:
                            type: number
                            description: 该词起始时间，单位毫秒
                            x-parser-schema-id: <anonymous-schema-54>
                          time_end:
                            type: number
                            description: 该词结束时间，单位毫秒
                            x-parser-schema-id: <anonymous-schema-55>
                        x-parser-schema-id: <anonymous-schema-50>
                      x-parser-schema-id: <anonymous-schema-49>
                  x-parser-schema-id: <anonymous-schema-43>
              x-parser-schema-id: <anonymous-schema-41>
            trace_id:
              type: string
              description: 表示会话中单次请求的 id，用于在咨询/反馈时帮助定位问题。
              x-parser-schema-id: <anonymous-schema-56>
            session_id:
              type: string
              description: 表示整个会话的 id。
              x-parser-schema-id: <anonymous-schema-57>
            event:
              type: string
              description: 表示会话类型，当前环节成功后会返回 task_continued`
              x-parser-schema-id: <anonymous-schema-58>
            is_final:
              type: boolean
              description: 该请求返回是否完结
              x-parser-schema-id: <anonymous-schema-59>
            extra_info:
              type: object
              description: 相关额外信息
              properties:
                audio_length:
                  type: integer
                  format: int64
                  description: 音频时长，精确到毫秒
                  x-parser-schema-id: <anonymous-schema-60>
                audio_sample_rate:
                  type: integer
                  format: int64
                  description: 音频采样率
                  x-parser-schema-id: <anonymous-schema-61>
                audio_size:
                  type: integer
                  format: int64
                  description: 音频文件大小，单位为字节
                  x-parser-schema-id: <anonymous-schema-62>
                bitrate:
                  type: integer
                  format: int64
                  description: 音频比特率
                  x-parser-schema-id: <anonymous-schema-63>
                audio_format:
                  type: string
                  description: 生成音频文件的格式。取值范围 mp3/pcm/flac
                  x-parser-schema-id: <anonymous-schema-64>
                audio_channel:
                  type: integer
                  format: int64
                  description: 生成音频声道数。1：单声道，2：双声道
                  x-parser-schema-id: <anonymous-schema-65>
                invisible_character_ratio:
                  type: integer
                  format: float
                  description: 非法字符占比。非法字符不超过 10%（包含 10%），音频会正常生成并返回非法字符占比，超过进行报错
                  x-parser-schema-id: <anonymous-schema-66>
                usage_characters:
                  type: integer
                  format: int64
                  description: 计费字符数。本次语音生成的计费字符数
                  x-parser-schema-id: <anonymous-schema-67>
                usage_voice_count:
                  type: integer
                  format: int64
                  description: 本次请求计费的音色数量（音色首次使用时计费），仅在产生音色费用时返回
                  x-parser-schema-id: <anonymous-schema-68>
                word_count:
                  type: integer
                  format: int64
                  description: 合成文本的字符数（含标点和空格），仅供参考，不用于计费；计费字符数请以 `usage_characters` 为准
                  x-parser-schema-id: <anonymous-schema-69>
              x-parser-schema-id: ExtraInfo
            base_resp:
              type: object
              description: 本次请求的状态码和详情
              properties:
                status_code:
                  type: integer
                  description: >-
                    状态码

                    - 0: 请求结果正常

                    - 1000: 未知错误

                    - 1001: 请求超时

                    - 1002: 触发限流

                    - 1004: 鉴权失败

                    - 1039: 触发 TPM 限流

                    - 1042: 非法字符超过 10%

                    - 2013: 输入参数信息不正常

                    - 2201: 连接空闲超时，被服务端关闭（见接口说明的「连接保活」一节）

                    - 2202: 非法事件

                    - 2204: 单条 `task_continue` 文本超过 10,000 字符，该条被跳过；连接与会话保持

                    - 2205: 排队待合成的文本过多（发送速度超过合成速度）。**这不是配额限流**：连接与会话均保持，稍后重发该条
                    `task_continue` 即可，不要重连或重新 `task_start`

                    - 2206: 事件顺序非法（如已开始任务后重复发送 `task_start`）


                    注意：本接口对纯空白文本会静默丢弃，不会返回 `2203`。

                    更多内容可查看 [错误码查询列表](/api-reference/errorcode) 了解详情
                  x-parser-schema-id: <anonymous-schema-70>
                status_msg:
                  type: string
                  description: 状态详情
                  x-parser-schema-id: <anonymous-schema-71>
              x-parser-schema-id: TaskContinueBaseResp
            connect_id:
              type: string
              description: >-
                表示当前 WebSocket 连接的 id。与 `session_id` 区分：一个连接对应一个
                `connect_id`，`session_id` 标识连接内的合成会话
              x-parser-schema-id: <anonymous-schema-72>
          x-parser-schema-id: ReceiveTaskContinuedEvent
        title: 任务继续
        description: 服务端返回 `task_continued` 事件，标志着任务已成功继续
        example: |-
          {
            "data": {
              "audio": "xxx"
            },
            "extra_info": {
              "audio_channel": 1,
              "audio_format": "mp3",
              "audio_length": 9914,
              "audio_sample_rate": 32000,
              "audio_size": 157869,
              "bitrate": 128000,
              "invisible_character_ratio": 0,
              "usage_characters": 158,
              "word_count": 158
            },
            "is_final": true,
            "session_id": "301871346491491",
            "trace_id": "04ee3794e2c9e4a6d5f99e77742f06fd",
            "base_resp": {
              "status_code": 0,
              "status_msg": "success"
            },
            "connect_id": "301871346491491"
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: receive_task_continued
      - &ref_14
        id: receive_sentence_end
        contentType: application/json
        payload:
          - name: 分句合成结束
            description: >-
              服务端返回 `sentence_end` 事件，表示当前句子的音频已全部返回。


              注意三层结束语义的区别：`is_final` 表示本次请求的音频结束，`sentence_end`
              表示当前句结束，`task_finished` 表示整个会话结束
            type: object
            properties:
              - name: session_id
                type: string
                description: 表示整个会话的 id
                required: false
              - name: connect_id
                type: string
                description: >-
                  表示当前 WebSocket 连接的 id。与 `session_id` 区分：一个连接对应一个
                  `connect_id`，`session_id` 标识连接内的合成会话
                required: false
              - name: event
                type: string
                description: 表示会话事件类型，分句合成结束时会返回 `sentence_end`
                required: false
              - name: trace_id
                type: string
                description: 表示会话中单次请求的 id，用于在咨询/反馈时帮助定位问题
                required: false
              - name: base_resp
                type: object
                required: false
                properties:
                  - name: status_code
                    type: integer
                    description: |-
                      状态码，`0`代表建连成功.
                      更多状态码信息请参考 [错误码查询列表](/api-reference/errorcode)
                    required: false
                  - name: status_msg
                    type: string
                    description: 该请求对应的状态码和详情
                    required: false
        headers: []
        jsonPayloadSchema:
          type: object
          properties:
            session_id:
              type: string
              description: 表示整个会话的 id
              x-parser-schema-id: <anonymous-schema-98>
            connect_id:
              type: string
              description: >-
                表示当前 WebSocket 连接的 id。与 `session_id` 区分：一个连接对应一个
                `connect_id`，`session_id` 标识连接内的合成会话
              x-parser-schema-id: <anonymous-schema-99>
            event:
              type: string
              const: sentence_end
              description: 表示会话事件类型，分句合成结束时会返回 `sentence_end`
              x-parser-schema-id: <anonymous-schema-100>
            trace_id:
              type: string
              description: 表示会话中单次请求的 id，用于在咨询/反馈时帮助定位问题
              x-parser-schema-id: <anonymous-schema-101>
            base_resp: *ref_0
          x-parser-schema-id: ReceiveSentenceEndEvent
        title: 分句合成结束
        description: >-
          服务端返回 `sentence_end` 事件，表示当前句子的音频已全部返回。


          注意三层结束语义的区别：`is_final` 表示本次请求的音频结束，`sentence_end`
          表示当前句结束，`task_finished` 表示整个会话结束
        example: |-
          {
            "session_id": "my-session-001",
            "connect_id": "301871346491491",
            "event": "sentence_end",
            "trace_id": "0303a2882bf18235ae7a809ae0f3cca7",
            "base_resp": {
              "status_code": 0,
              "status_msg": "success"
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: receive_sentence_end
      - &ref_15
        id: receive_task_canceled
        contentType: application/json
        payload:
          - name: 打断成功
            description: 服务端返回 `task_canceled` 事件，表示打断已生效。此后可继续发送 `task_continue`
            type: object
            properties:
              - name: session_id
                type: string
                description: 表示整个会话的 id
                required: false
              - name: connect_id
                type: string
                description: >-
                  表示当前 WebSocket 连接的 id。与 `session_id` 区分：一个连接对应一个
                  `connect_id`，`session_id` 标识连接内的合成会话
                required: false
              - name: event
                type: string
                description: 表示会话事件类型，打断成功后会返回 `task_canceled`
                required: false
              - name: trace_id
                type: string
                description: 表示会话中单次请求的 id，用于在咨询/反馈时帮助定位问题
                required: false
              - name: base_resp
                type: object
                required: false
                properties:
                  - name: status_code
                    type: integer
                    description: |-
                      状态码，`0`代表建连成功.
                      更多状态码信息请参考 [错误码查询列表](/api-reference/errorcode)
                    required: false
                  - name: status_msg
                    type: string
                    description: 该请求对应的状态码和详情
                    required: false
        headers: []
        jsonPayloadSchema:
          type: object
          properties:
            session_id:
              type: string
              description: 表示整个会话的 id
              x-parser-schema-id: <anonymous-schema-90>
            connect_id:
              type: string
              description: >-
                表示当前 WebSocket 连接的 id。与 `session_id` 区分：一个连接对应一个
                `connect_id`，`session_id` 标识连接内的合成会话
              x-parser-schema-id: <anonymous-schema-91>
            event:
              type: string
              const: task_canceled
              description: 表示会话事件类型，打断成功后会返回 `task_canceled`
              x-parser-schema-id: <anonymous-schema-92>
            trace_id:
              type: string
              description: 表示会话中单次请求的 id，用于在咨询/反馈时帮助定位问题
              x-parser-schema-id: <anonymous-schema-93>
            base_resp: *ref_0
          x-parser-schema-id: ReceiveTaskCanceledEvent
        title: 打断成功
        description: 服务端返回 `task_canceled` 事件，表示打断已生效。此后可继续发送 `task_continue`
        example: |-
          {
            "session_id": "my-session-001",
            "connect_id": "301871346491491",
            "event": "task_canceled",
            "trace_id": "0303a2882bf18235ae7a809ae0f3cca7",
            "base_resp": {
              "status_code": 0,
              "status_msg": "success"
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: receive_task_canceled
      - &ref_16
        id: receive_task_flushed
        contentType: application/json
        payload:
          - name: 残留已送出
            description: >-
              服务端返回 `task_flushed`，表示本次 `task_flush` 请求的音频已全部下发完毕。该事件排在本次 flush
              产生的音频帧之后，收到它即可认为这一轮的音频结束。此后可继续发送 `task_continue`。
            type: object
            properties:
              - name: session_id
                type: string
                description: 表示整个会话的 id
                required: false
              - name: connect_id
                type: string
                description: >-
                  表示当前 WebSocket 连接的 id。与 `session_id` 区分：一个连接对应一个
                  `connect_id`，`session_id` 标识连接内的合成会话
                required: false
              - name: event
                type: string
                description: 表示会话事件类型，残留送出完毕后会返回 `task_flushed`
                required: false
              - name: trace_id
                type: string
                description: 表示会话中单次请求的 id，用于在咨询/反馈时帮助定位问题
                required: false
              - name: base_resp
                type: object
                required: false
                properties:
                  - name: status_code
                    type: integer
                    description: |-
                      状态码，`0`代表建连成功.
                      更多状态码信息请参考 [错误码查询列表](/api-reference/errorcode)
                    required: false
                  - name: status_msg
                    type: string
                    description: 该请求对应的状态码和详情
                    required: false
        headers: []
        jsonPayloadSchema:
          type: object
          properties:
            session_id:
              type: string
              description: 表示整个会话的 id
              x-parser-schema-id: <anonymous-schema-74>
            connect_id:
              type: string
              description: >-
                表示当前 WebSocket 连接的 id。与 `session_id` 区分：一个连接对应一个
                `connect_id`，`session_id` 标识连接内的合成会话
              x-parser-schema-id: <anonymous-schema-75>
            event:
              type: string
              const: task_flushed
              description: 表示会话事件类型，残留送出完毕后会返回 `task_flushed`
              x-parser-schema-id: <anonymous-schema-76>
            trace_id:
              type: string
              description: 表示会话中单次请求的 id，用于在咨询/反馈时帮助定位问题
              x-parser-schema-id: <anonymous-schema-77>
            base_resp: *ref_0
          x-parser-schema-id: ReceiveTaskFlushedEvent
        title: 残留已送出
        description: >-
          服务端返回 `task_flushed`，表示本次 `task_flush` 请求的音频已全部下发完毕。该事件排在本次 flush
          产生的音频帧之后，收到它即可认为这一轮的音频结束。此后可继续发送 `task_continue`。
        example: |-
          {
            "session_id": "my-session-001",
            "connect_id": "301871346491491",
            "event": "task_flushed",
            "trace_id": "0303a2882bf18235ae7a809ae0f3cca7",
            "base_resp": {
              "status_code": 0,
              "status_msg": "success"
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: receive_task_flushed
      - &ref_17
        id: receive_task_finished
        contentType: application/json
        payload:
          - name: 任务结束
            description: 服务端返回 `task_finished` 事件，标志着任务已成功结束
            type: object
            properties:
              - name: trace_id
                type: string
                description: 表示会话中单次请求的 id，用于在咨询/反馈时帮助定位问题
                required: false
              - name: session_id
                type: string
                description: 表示整个会话的 id
                required: false
              - name: event
                type: string
                description: 表示会话类型，当前环节成功后会返回 `task_finished`
                required: false
              - name: base_resp
                type: object
                description: 该请求对应的状态码和详情
                required: false
                properties:
                  - name: status_code
                    type: integer
                    description: |-
                      状态码。
                      - 0: 表示发送成功
                      - 2202: 表示非法事件
                      更多内容可查看 [错误码查询列表](/api-reference/errorcode) 了解详情
                    required: false
                  - name: status_msg
                    type: string
                    description: 状态详情
                    required: false
              - name: connect_id
                type: string
                description: >-
                  表示当前 WebSocket 连接的 id。与 `session_id` 区分：一个连接对应一个
                  `connect_id`，`session_id` 标识连接内的合成会话
                required: false
        headers: []
        jsonPayloadSchema:
          type: object
          properties:
            trace_id:
              type: string
              description: 表示会话中单次请求的 id，用于在咨询/反馈时帮助定位问题
              x-parser-schema-id: <anonymous-schema-79>
            session_id:
              type: string
              description: 表示整个会话的 id
              x-parser-schema-id: <anonymous-schema-80>
            event:
              type: string
              description: 表示会话类型，当前环节成功后会返回 `task_finished`
              x-parser-schema-id: <anonymous-schema-81>
            base_resp: *ref_1
            connect_id:
              type: string
              description: >-
                表示当前 WebSocket 连接的 id。与 `session_id` 区分：一个连接对应一个
                `connect_id`，`session_id` 标识连接内的合成会话
              x-parser-schema-id: <anonymous-schema-82>
          x-parser-schema-id: ReceiveTaskFinishedEvent
        title: 任务结束
        description: 服务端返回 `task_finished` 事件，标志着任务已成功结束
        example: |-
          {
            "session_id": "xxxx",
            "event": "task_finished",
            "trace_id": "0303a2882bf18235ae7a809ae0f3cca7",
            "base_resp": {
              "status_code": 0,
              "status_msg": "success"
            },
            "connect_id": "301871346491491"
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: receive_task_finished
      - &ref_18
        id: receive_task_failed
        contentType: application/json
        payload:
          - name: 任务失败
            description: 如果接收到 `task_failed` 事件，表示任务失败。此时需要关闭 WebSocket 连接并处理错误。
            type: object
            properties:
              - name: trace_id
                type: string
                description: 表示会话中单次请求的 id，用于在咨询/反馈时帮助定位问题
                required: false
              - name: session_id
                type: string
                description: 表示整个会话的 id
                required: false
              - name: event
                type: string
                description: 表示会话类型，任务失败会返回 `task_failed`
                required: false
              - name: base_resp
                type: object
                description: 本次请求的状态码和详情
                required: false
                properties:
                  - name: status_code
                    type: integer
                    description: |-
                      状态码
                      - `1000`: 未知错误
                      - `1001`: 超时
                      - `1002`: 触发限流
                      - `1004`: 鉴权失败
                      - `1039`: 触发 TPM 限流
                      - `1042`: 非法字符超过 10%
                      - `2013`: 输入参数信息不正常
                      - `2201`: 连接空闲超时，被服务端关闭（见接口说明的「连接保活」一节）
                      更多内容可查看 [错误码查询列表](/api-reference/errorcode) 了解详情
                    required: false
                  - name: status_msg
                    type: string
                    description: 状态详情
                    required: false
              - name: connect_id
                type: string
                description: >-
                  表示当前 WebSocket 连接的 id。与 `session_id` 区分：一个连接对应一个
                  `connect_id`，`session_id` 标识连接内的合成会话
                required: false
        headers: []
        jsonPayloadSchema:
          type: object
          properties:
            trace_id:
              type: string
              description: 表示会话中单次请求的 id，用于在咨询/反馈时帮助定位问题
              x-parser-schema-id: <anonymous-schema-83>
            session_id:
              type: string
              description: 表示整个会话的 id
              x-parser-schema-id: <anonymous-schema-84>
            event:
              type: string
              description: 表示会话类型，任务失败会返回 `task_failed`
              x-parser-schema-id: <anonymous-schema-85>
            base_resp:
              type: object
              description: 本次请求的状态码和详情
              properties:
                status_code:
                  type: integer
                  description: |-
                    状态码
                    - `1000`: 未知错误
                    - `1001`: 超时
                    - `1002`: 触发限流
                    - `1004`: 鉴权失败
                    - `1039`: 触发 TPM 限流
                    - `1042`: 非法字符超过 10%
                    - `2013`: 输入参数信息不正常
                    - `2201`: 连接空闲超时，被服务端关闭（见接口说明的「连接保活」一节）
                    更多内容可查看 [错误码查询列表](/api-reference/errorcode) 了解详情
                  x-parser-schema-id: <anonymous-schema-86>
                status_msg:
                  type: string
                  description: 状态详情
                  x-parser-schema-id: <anonymous-schema-87>
              x-parser-schema-id: TaskFailedBaseResp
            connect_id:
              type: string
              description: >-
                表示当前 WebSocket 连接的 id。与 `session_id` 区分：一个连接对应一个
                `connect_id`，`session_id` 标识连接内的合成会话
              x-parser-schema-id: <anonymous-schema-88>
          x-parser-schema-id: ReceiveTaskFailedEvent
        title: 任务失败
        description: 如果接收到 `task_failed` 事件，表示任务失败。此时需要关闭 WebSocket 连接并处理错误。
        example: |-
          {
            "session_id": "xxxx",
            "event": "task_failed",
            "trace_id": "0303a2882bf18235ae7a809ae0f3cca7",
            "base_resp": {
              "status_code": 1004,
              "status_msg": "XXXXXXX"
            },
            "connect_id": "301871346491491"
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: receive_task_failed
    bindings: []
    extensions: *ref_2
sendOperations:
  - *ref_3
receiveOperations:
  - *ref_4
sendMessages:
  - *ref_5
  - *ref_6
  - *ref_7
  - *ref_8
  - *ref_9
receiveMessages:
  - *ref_10
  - *ref_11
  - *ref_12
  - *ref_13
  - *ref_14
  - *ref_15
  - *ref_16
  - *ref_17
  - *ref_18
extensions:
  - id: x-parser-unique-object-id
    value: t2a_v2_bidi_websocket
securitySchemes: []

````