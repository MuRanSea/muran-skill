<!-- Official source: https://platform.minimax.cn/docs/api-reference/speech-to-text.md -->
<!-- Source SHA-256: 8666563dd1915daaf85bef063f9200da9e4740b528ddea2905eefb0c05c2d3c6 -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.minimaxi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 语音识别

> 使用本接口，将音频文件转写为文本，支持流式返回、说话人分离与字幕导出。



## OpenAPI

````yaml api-reference/speech/speech-to-text/api/openapi.json POST /v1/speech_to_text
openapi: 3.1.0
info:
  title: MiniMax ASR API
  description: MiniMax 语音识别（Speech-to-Text）API，支持一次性返回与流式返回
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.minimax.cn
security:
  - bearerAuth: []
paths:
  /v1/speech_to_text:
    post:
      tags:
        - SpeechToText
      summary: 语音识别
      operationId: speechToText
      parameters:
        - name: Content-Type
          in: header
          required: true
          description: 请求体的媒介类型，固定为 `multipart/form-data`。
          schema:
            type: string
            enum:
              - multipart/form-data
            default: multipart/form-data
        - name: language
          in: header
          required: false
          description: >-
            可选的 [BCP-47
            语言标签](https://www.rfc-editor.org/info/bcp47/)，用于提示音频中的主要语言。不传该请求头或传空值时，启用混合语言识别。


            当前支持：`zh`（中文）、`yue`（粤语）、`en`（英语）、`ja`（日语）、`ko`（韩语）、`th`（泰语）、`vi`（越南语）、`id`（印尼语）、`ms`（马来语）、`fil`（菲律宾语）、`ar`（阿拉伯语）、`tr`（土耳其语）、`fr`（法语）、`de`（德语）、`es`（西班牙语）、`it`（意大利语）、`pt`（葡萄牙语）、`pl`（波兰语）、`ru`（俄语）和
            `uk`（乌克兰语）。
          schema:
            type: string
            default: ''
            example: en
      requestBody:
        required: true
        content:
          multipart/form-data:
            schema:
              type: object
              required:
                - model
                - file
              properties:
                model:
                  type: string
                  description: 本次调用的模型版本。
                  enum:
                    - asr-1.0
                  default: asr-1.0
                  example: asr-1.0
                file:
                  type: string
                  format: binary
                  description: >-
                    待识别的音频文件，填写文件的路径地址。


                    上传的音频文件需遵从以下规范：


                    | 项 | 约束 |

                    | --- | --- |

                    | 格式 | `wav` / `aiff` / `flac` / `alac`(m4a) / `mp3` / `aac`
                    / `opus` / `ogg` |

                    | 时长 | 不超过 **500 秒**；超出会返回 `400` 而不会被截断 |

                    | 大小 | 不超过 **50 MB**；超出返回 `413` |


                    不支持无容器的裸 PCM 数据。


                    语音识别不依赖高采样率与立体声，未压缩的高规格音频容易超过大小上限（如 500 秒 48 kHz 立体声 WAV 约
                    92 MB）。建议先转为单声道 16 kHz，或改用 `mp3` / `aac` / `opus`
                    等压缩格式，识别结果不受影响。
                response_format:
                  type: string
                  description: >-
                    识别结果的返回格式。


                    | 取值 | 返回内容 | 响应类型 |

                    | --- | --- | --- |

                    | `json` | `text` + `duration` | `application/json` |

                    | `verbose_json` | `text` + `duration` + `segments` +
                    `n_speakers`（含说话人分离与时间戳） | `application/json` |

                    | `srt` | SRT 字幕 | `text/plain` |

                    | `vtt` | WebVTT 字幕 | `text/vtt` |


                    `verbose_json` / `srt` / `vtt` 会启用说话人分离与时间戳对齐，因此**不能与
                    `stream=true` 同时使用**。


                    `srt` 的响应体：


                    ```

                    1

                    00:00:00,100 --> 00:00:01,660

                    嘎嘎会，可以，这把稳了。


                    2

                    00:00:02,000 --> 00:00:06,100

                    来检查一下，读下题。

                    ```


                    `vtt` 的响应体：


                    ```

                    WEBVTT


                    00:00:00.100 --> 00:00:01.660

                    嘎嘎会，可以，这把稳了。


                    00:00:02.000 --> 00:00:06.100

                    来检查一下，读下题。

                    ```
                  enum:
                    - json
                    - verbose_json
                    - srt
                    - vtt
                  default: json
                  example: json
                timestamp_level:
                  type: string
                  description: >-
                    时间戳粒度。仅当 `response_format` 为 `verbose_json`、`srt` 或 `vtt`
                    时生效，因为这些格式会启用说话人分离与时间戳对齐。


                    - 空值或 `sentence`（默认）：保持原有句段时间戳，并合并同一分段内相邻且属于同一说话人的文本。

                    - `word`：返回字/词级时间戳，中文按字、英文按词；每个单元仍包含 `speaker`。


                    当 `response_format=json` 时（包括 `stream=true`
                    的情况），该参数可以传入，但会被忽略且不会报错。
                  enum:
                    - ''
                    - sentence
                    - word
                  default: ''
                  example: word
                stream:
                  type: boolean
                  description: >-
                    是否流式返回识别结果。


                    - `false`（默认）：识别完成后一次性返回。

                    - `true`：以 SSE 推送增量文本，响应类型为 `text/event-stream`；此时
                    `response_format` 仅支持 `json`。


                    流式响应以 `data: <json>` 逐行推送，事件之间以空行分隔：


                    ```

                    data: {"index":0,"delta":"实际上","finish":false}


                    data: {"index":1,"delta":"还是商家赚了","finish":false}


                    data: {"index":2,"delta":"","finish":true,"duration":26.325}

                    ```


                    每个事件的 `data` 为 JSON 对象：`index` 为从 `0` 开始递增的事件序号，`delta`
                    为本次新增的识别文本，`finish` 标识是否为终止事件，`duration`
                    为音频时长（单位秒，仅终止事件返回）。客户端应按 `index` 顺序拼接所有 `delta`，并在收到
                    `finish=true` 后结束读取。
                  default: false
                  example: false
      responses:
        '200':
          description: >-
            识别成功。`response_format` 取 `json` 或 `verbose_json` 时返回下列 JSON 结构；取
            `srt` / `vtt` 或 `stream=true` 时的响应体见对应请求参数的说明。
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AsrResp'
              examples:
                json:
                  summary: response_format=json
                  value:
                    text: 实际上还是商家赚了，对他那个冷链的那个运费高。
                    duration: 26.325
                    trace_id: 021785229015510a2c883cf675b9804d
                verbose_json:
                  summary: response_format=verbose_json
                  value:
                    text: 嘎嘎会，可以，这把稳了。来检查一下，读下题。
                    duration: 12.744
                    n_speakers: 2
                    segments:
                      - id: 0
                        start: 0.1
                        end: 1.66
                        speaker: S1
                        text: 嘎嘎会，可以，这把稳了。
                      - id: 1
                        start: 2
                        end: 6.1
                        speaker: S2
                        text: 来检查一下，读下题。
                    trace_id: 021785229015510a2c883cf675b9804d
        '400':
          $ref: '#/components/responses/Err400'
        '401':
          $ref: '#/components/responses/Err401'
        '402':
          $ref: '#/components/responses/Err402'
        '413':
          $ref: '#/components/responses/Err413'
        '422':
          $ref: '#/components/responses/Err422'
        '429':
          $ref: '#/components/responses/Err429'
        '500':
          $ref: '#/components/responses/Err500'
components:
  schemas:
    AsrResp:
      type: object
      properties:
        text:
          type: string
          description: 识别出的完整文本。`verbose_json` 下等于各 `segments[].text` 按时间顺序拼接。
        duration:
          type: number
          description: 输入音频的时长，单位为秒。计费以该时长为准。
        n_speakers:
          type: integer
          description: 识别出的说话人数量。**仅 `response_format=verbose_json` 时返回。**
        segments:
          type: array
          description: >-
            带时间戳的识别单元，每个单元均携带起止时间与说话人标识。粒度由 `timestamp_level` 决定：默认按句段，设为 `word`
            时中文按字、英文按词。**仅 `response_format=verbose_json` 时返回。**
          items:
            $ref: '#/components/schemas/AsrSegment'
        trace_id:
          type: string
          description: 本次请求的追踪 ID，便于排查问题。
    AsrSegment:
      type: object
      properties:
        id:
          type: integer
          description: 该时间戳单元在结果中的序号，从 `0` 开始。
        start:
          type: number
          description: 该单元的起始时间，单位为秒。
        end:
          type: number
          description: 该单元的结束时间，单位为秒。
        speaker:
          type: string
          description: 说话人标识，形如 `S1`、`S2`。同一标识代表同一说话人。
        text:
          type: string
          description: 当前句段、字或词的识别文本。
    OaiError:
      type: object
      description: OpenAI 风格错误响应。出错时 HTTP 状态码为真实错误码（401/400/429/402/422/500…），响应体为该结构。
      properties:
        type:
          type: string
          description: 固定为 `error`。
          example: error
        error:
          $ref: '#/components/schemas/OaiErrorDetail'
        request_id:
          type: string
          description: 请求追踪 ID（便于排查）。
    OaiErrorDetail:
      type: object
      properties:
        type:
          type: string
          description: >-
            错误类型：`authorized_error`(401)/`bad_request_error`(400)/`rate_limit_error`(429)/`insufficient_balance_error`(402)/`unprocessable_entity_error`(422)/`invalid_request_error`(413)/`server_error`(500)
            等。
        message:
          type: string
          description: 错误详情，结尾括号内为内部错误码（如 `... (1004)`）。
        http_code:
          type: string
          description: HTTP 状态码字符串，如 `401`。
  responses:
    Err400:
      description: 参数错误
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/OaiError'
          example:
            type: error
            error:
              type: bad_request_error
              message: >-
                invalid params, audio duration 623.4s exceeds the limit of 500s
                (2013)
              http_code: '400'
            request_id: 021785229015510a2c883cf675b9804d
    Err401:
      description: 鉴权失败
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/OaiError'
          example:
            type: error
            error:
              type: authorized_error
              message: >-
                login fail: Please carry the API secret key in the
                'Authorization' field of the request header (1004)
              http_code: '401'
            request_id: 021785229015510a2c883cf675b9804d
    Err402:
      description: 余额/额度不足
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/OaiError'
          example:
            type: error
            error:
              type: insufficient_balance_error
              message: insufficient balance (1008)
              http_code: '402'
            request_id: 021785229015510a2c883cf675b9804d
    Err413:
      description: 请求体超过大小上限
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/OaiError'
          example:
            type: error
            error:
              type: invalid_request_error
              message: >-
                request body too large: 88200078 bytes exceeds limit of 52428800
                bytes
              http_code: '413'
            request_id: 021785229015510a2c883cf675b9804d
    Err422:
      description: 输入涉及敏感内容
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/OaiError'
          example:
            type: error
            error:
              type: unprocessable_entity_error
              message: audio content contains sensitive content (1026)
              http_code: '422'
            request_id: 021785229015510a2c883cf675b9804d
    Err429:
      description: 触发限流
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/OaiError'
          example:
            type: error
            error:
              type: rate_limit_error
              message: rate limit, please retry later (1002)
              http_code: '429'
            request_id: 021785229015510a2c883cf675b9804d
    Err500:
      description: 服务端错误
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/OaiError'
          example:
            type: error
            error:
              type: server_error
              message: internal error (1000)
              http_code: '500'
            request_id: 021785229015510a2c883cf675b9804d
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: |-
        `HTTP: Bearer Auth`
         - Security Scheme Type: http
         - HTTP Authorization Scheme: Bearer API_key，用于验证账户信息，可在 [账户管理>接口密钥](https://platform.minimax.cn/user-center/basic-information/interface-key) 中查看。

````