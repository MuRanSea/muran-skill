<!-- Official source: https://platform.minimax.cn/docs/api-reference/image-generation-h3-generations.md -->
<!-- Source SHA-256: 689381a86f72dbf0c80fa56737cfff4456aea22b518ee17793abed2f0814eac2 -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.minimaxi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 文生图

> 使用 MiniMax-H3-Image 根据文本描述生成图片，支持 `auto` 或自定义宽高，单次最多生成 10 张。

当前支持模型：`MiniMax-H3-Image`、`MiniMax-H3-Image-Highspeed`，两者参数与限制相同。

> [!WARNING]
>
> 服务端最长等待 600 秒，建议客户端超时不低于 600 秒。本接口不支持幂等：请求发出后，即使客户端超时或断开连接，服务端仍会完成生成并对成功的图片计费；重试会重新生成并计费。使用 OpenAI SDK 时请设置 `max_retries=0`，关闭默认的自动重试。


## OpenAPI

````yaml api-reference/image/generation/api/h3-image-generations.json POST /v1/images/generations
openapi: 3.1.0
info:
  title: MiniMax H3-Image Generations API
  description: MiniMax H3-Image API
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.minimax.cn
security:
  - bearerAuth: []
paths:
  /v1/images/generations:
    post:
      tags:
        - Image
      summary: 文生图
      description: >-
        根据文本描述生成图片，同步返回，支持流式输出。


        当前支持模型：`MiniMax-H3-Image`、`MiniMax-H3-Image-Highspeed`，两者参数与限制相同。


        服务端最长等待 600 秒，建议客户端超时不低于 600
        秒。本接口不支持幂等：请求发出后，即使客户端超时或断开连接，服务端仍会完成生成并对成功的图片计费；重试会重新生成并计费。
      operationId: h3ImageGenerations
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/H3ImageGenerationReq'
      responses:
        '200':
          description: >-
            `stream` 为 `false`（默认）时返回 `application/json`。`stream` 为 `true` 时返回
            `text/event-stream`（SSE），每个事件的 `data` 为 JSON，结构见 `text/event-stream`
            的响应定义，事件说明与完整示例见[流式响应事件](/api-reference/image-generation-h3-streaming)。
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ImagesResponse'
            text/event-stream:
              schema:
                $ref: '#/components/schemas/ImageStreamEvent'
              examples:
                单张成功:
                  summary: 单张成功
                  value:
                    type: image_generation.partial_succeeded
                    created: 1792308690
                    model: MiniMax-H3-Image
                    image_index: 1
                    url: https://example.com/h3-image/output-1.jpg
                    size: 2720x1536
                    output_format: jpeg
                    revised_prompt: 一只橘猫蜷在洒满阳光的窗台上打盹，窗外是模糊的城市街景，暖色调，胶片质感
                单张失败:
                  summary: 单张失败
                  value:
                    type: image_generation.partial_failed
                    created: 1792308691
                    model: MiniMax-H3-Image
                    image_index: 2
                    code: '1027'
                    message: output image failed content safety check
                全部结束:
                  summary: 全部结束
                  value:
                    type: image_generation.completed
                    created: 1792308695
                    model: MiniMax-H3-Image
                    usage:
                      generated_images: 2
                      total_tokens: 13022
                      input_tokens: 4862
                      output_tokens: 8160
                      input_tokens_details:
                        text_tokens: 4862
                        image_tokens: 0
                      output_tokens_details:
                        image_tokens: 8160
                    request_id: 021792308678142a2c883cf675b9804d
                整体失败:
                  summary: 整体失败
                  value:
                    type: error
                    error:
                      type: server_error
                      message: internal error (1000)
                      http_code: '500'
                    usage:
                      generated_images: 0
                      total_tokens: 0
                      input_tokens: 0
                      output_tokens: 0
                      input_tokens_details:
                        text_tokens: 0
                        image_tokens: 0
                      output_tokens_details:
                        image_tokens: 0
                    request_id: 021792308678142a2c883cf675b9804d
        '400':
          $ref: '#/components/responses/Err400'
        '401':
          $ref: '#/components/responses/Err401'
        '402':
          $ref: '#/components/responses/Err402'
          description: |-
            余额或套餐额度不足，错误码见 `error.message` 末尾括号：

            - `1008`：余额不足
            - `2053`：积分不足
            - `2067`：套餐额度已用完，且未开启积分自动消耗
            - `2068`：当前套餐等级不支持该模型
        '422':
          $ref: '#/components/responses/Err422'
        '429':
          $ref: '#/components/responses/Err429'
          description: |-
            触发限流，错误码见 `error.message` 末尾括号：

            - `1002`：超过每分钟生成图片张数（IPM）上限，每个请求按 `n` 张计入
            - `2056`：使用 M Plan 时，套餐用量达到上限
        '500':
          $ref: '#/components/responses/Err500'
components:
  schemas:
    H3ImageGenerationReq:
      type: object
      required:
        - model
        - prompt
      properties:
        model:
          type: string
          description: 模型名称。可选值：`MiniMax-H3-Image`、`MiniMax-H3-Image-Highspeed`，两者参数与限制相同
          enum:
            - MiniMax-H3-Image
            - MiniMax-H3-Image-Highspeed
        prompt:
          type: string
          maxLength: 32000
          description: >-
            图片的文本描述，最长 32000 个字符（按 Unicode 字符计，不含首尾空白），为空或只含空白时返回 400。关闭 Prompt
            增强（`disable_prompt_enhanced` 为 `true`）时，模型只读取约前 4096 个
            token，超出部分不生效。
        disable_prompt_enhanced:
          type: boolean
          default: false
          description: |-
            是否关闭 Prompt 增强，默认 `false`（开启增强），增强结果见 `data[].revised_prompt`。

            设为 `true` 时直接使用原始 `prompt`，输出比例必须由请求给出，二选一：

            - `size` 为 `宽x高`
            - `size` 不传或为 `auto`，`aspect_ratio` 为 `X:Y`（`area` 可不传，默认 `4K`）

            `size` 不是 `宽x高`、且 `aspect_ratio` 不传或为 `auto` 时返回 400。
        'n':
          type: integer
          default: 1
          minimum: 1
          maximum: 10
          description: 生成图片数量，取值范围 [1, 10]，默认 1。
        size:
          type: string
          default: auto
          description: >-
            输出图片尺寸，默认 `auto`，详见[输出尺寸](/guides/image-generation#输出尺寸)。两种写法二选一：


            - `宽x高`：直接指定宽高，如 `2720x1536`，宽、高为正整数。面积（宽 × 高）在 655,360 ~ 20,000,000
            像素之间，宽高比在 1:3 ~ 3:1 之间，均含边界；不满足时返回 400，不会自动缩放或取整。此时不能再传
            `aspect_ratio` 或 `area`（传 `auto` 也不行），否则返回 400

            - `auto` 或不传：宽高由 `aspect_ratio`（默认 `auto`）和 `area`（默认
            `4K`）决定，两者都可以单独传
        aspect_ratio:
          type: string
          default: auto
          example: '16:9'
          description: >-
            输出宽高比，默认 `auto`。


            - `size` 为 `宽x高` 时不能传入（传 `auto` 也不行），否则返回 400

            - `size` 不传或为 `auto`、且 `disable_prompt_enhanced` 为 `true` 时必须传
            `X:Y`，不传或传 `auto` 返回 400


            取值：


            - `auto`：由 Prompt 增强根据内容决定

            - `X:Y`：X、Y 为 1 ~ 300 的整数，宽高比在 1:3 ~ 3:1 之间（含边界），如
            `16:9`、`3:4`、`21:9`、`3:1`
        area:
          type: string
          enum:
            - 1K
            - 2K
            - 4K
          default: 4K
          description: >-
            输出面积档位，默认 `4K`。只能在 `size` 不传或为 `auto` 时传入，`size` 为 `宽x高` 时传入返回 400。


            `1K`、`2K`、`4K` 的目标面积分别为 1024 × 1024、2048 × 2048、4096 × 4096
            像素，宽高由服务端按宽高比计算，如 `2K` 搭配 `16:9` 输出 2720 × 1536。每张的实际宽高见
            `data[].size`。
        output_format:
          type: string
          enum:
            - png
            - jpeg
            - jpg
            - webp
          default: jpeg
          description: >-
            输出图片格式，默认 `jpeg`。可用值：`png`、`jpeg`、`jpg`、`webp`。`jpg` 与 `jpeg`
            等价，响应中的 `output_format` 返回 `jpeg`。
        response_format:
          type: string
          enum:
            - url
            - b64_json
          default: url
          description: >-
            返回形式，默认 `url`。


            - `url`：图片链接，有效期 24 小时，请在有效期内下载并自行保存

            - `b64_json`：Base64 编码的图片数据，不支持流式


            `b64_json` 的总输出面积（`n` × 宽 × 高）上限如下，超出返回 400（`size` 为 `auto` 时每张按
            `area` 对应的面积计，如 `4K` 按 4096 × 4096）：


            | `output_format` | 总面积上限 | 参考 |

            | :--- | :--- | :--- |

            | `png` | 20,000,000 px | 1 张任意尺寸 |

            | `jpeg` / `webp` | 80,000,000 px | 最多 4 张 `4K`，或 10 张 `2K` |
        stream:
          type: boolean
          default: false
          description: >-
            是否流式输出，默认 `false`。开启后响应为 `text/event-stream`（SSE），仅支持
            `response_format` 为 `url`：


            - 每张图片处理完推送一个事件：成功为 `image_generation.partial_succeeded`，失败为
            `image_generation.partial_failed`。事件按完成先后推送，用 `image_index` 对应张序

            - 全部结束后推送 `image_generation.completed`，包含 `usage` 和 `request_id`

            - 响应头返回后，全部图片失败或提交生成前失败时推送 `error` 事件

            - 响应头返回前的错误（参数错误、鉴权失败、限流、余额不足等）仍以普通 HTTP 错误返回，与非流式相同；请先检查 HTTP
            状态码，再按 SSE 解析


            事件结构见[流式响应事件](/api-reference/image-generation-h3-streaming)。
        output_compression:
          type: integer
          minimum: 0
          maximum: 100
          default: 95
          description: >-
            压缩质量，取值范围 [0, 100]，默认 95，数值越大画质越高、文件越大。仅对 `jpeg` / `webp` 生效，输出
            `png` 时忽略；超出取值范围返回 400。
        aigc_watermark:
          type: boolean
          default: false
          description: >-
            是否在图片上添加可见的 AIGC 标识水印，默认 `false`。AIGC
            隐式标识（写在图片文件的元数据中）按合规要求写入，不受该参数控制。
      example:
        model: MiniMax-H3-Image
        prompt: 一只橘猫趴在窗台上晒太阳，午后暖光，胶片质感
        size: 2720x1536
        'n': 2
        response_format: url
    ImagesResponse:
      type: object
      properties:
        created:
          type: integer
          description: 响应生成时间，Unix 时间戳（秒）。
        data:
          type: array
          description: >-
            图片列表，始终为 `n` 项，按张序排列（与流式事件的 `image_index` 一致）。成功的项返回 `url`（或
            `b64_json`）、`size` 和 `revised_prompt`；失败的项（包括未通过内容安全检查的）只返回 `error`。


            只要有 1 张成功，HTTP 状态码就是 200，请逐项检查 `data[].error`；全部失败时返回 402、422 或 500
            的错误响应。只对成功的图片计费。
          items:
            $ref: '#/components/schemas/ImageObject'
        output_format:
          type: string
          enum:
            - png
            - jpeg
            - webp
          description: 生成图片的格式。
        usage:
          $ref: '#/components/schemas/ImageUsage'
        request_id:
          type: string
          description: 请求 ID（即 Trace ID），反馈问题时请提供。
      example:
        created: 1792308678
        data:
          - url: https://example.com/h3-image/output-0.jpg
            size: 2720x1536
            revised_prompt: >-
              午后的暖光透过木质窗框洒在窗台上，一只橘猫侧身趴着晒太阳，眯着眼睛，毛发被阳光勾出金色轮廓，背景是虚化的室内绿植，胶片颗粒质感，柔和的暖色调
          - error:
              code: '1027'
              message: output image failed content safety check
        output_format: jpeg
        usage:
          generated_images: 1
          total_tokens: 7254
          input_tokens: 3174
          output_tokens: 4080
          input_tokens_details:
            text_tokens: 3174
            image_tokens: 0
          output_tokens_details:
            image_tokens: 4080
        request_id: 021792308678142a2c883cf675b9804d
    ImageStreamEvent:
      description: >-
        SSE 事件 `data` 字段的 JSON，为以下 4 种事件之一，按 `type` 区分。每个事件由 `event:` 行与 `data:`
        行组成，事件之间以空行分隔；等待期间每 15 秒推送一行注释 `: keepalive`，可直接忽略。
      oneOf:
        - $ref: '#/components/schemas/ImageStreamPartialSucceeded'
        - $ref: '#/components/schemas/ImageStreamPartialFailed'
        - $ref: '#/components/schemas/ImageStreamCompleted'
        - $ref: '#/components/schemas/ImageStreamError'
    ImageObject:
      type: object
      properties:
        url:
          type: string
          description: 图片链接，`response_format` 为 `url` 时返回，有效期 24 小时。
        b64_json:
          type: string
          description: Base64 编码的图片数据。`response_format` 为 `b64_json` 时返回。
        size:
          type: string
          description: 图片实际尺寸，格式为 `宽x高`。
        revised_prompt:
          type: string
          description: >-
            实际用于生成该图片的 prompt：开启 Prompt 增强时为增强后的结果；`disable_prompt_enhanced` 为
            `true` 时与请求中的 `prompt` 相同。
        error:
          type: object
          description: 该张图片的错误信息，仅失败时返回。
          properties:
            code:
              type: string
              description: >-
                单张失败的错误码。常见取值：`1000` 生成失败，`1001` 等待超时，`1008` 余额不足，`1026` 增强后的
                prompt 未通过内容安全检查，`1027`
                生成的图片未通过内容安全检查。完整列表见[错误码查询列表](/api-reference/errorcode)。
            message:
              type: string
              description: 错误详情。
    ImageUsage:
      type: object
      description: >-
        本次请求的 token 用量，只统计成功的图片，按此计费。`total_tokens` 为 `input_tokens` 与
        `output_tokens` 之和。
      properties:
        generated_images:
          type: integer
          description: 成功生成的图片数量，可能小于 `n`。
        total_tokens:
          type: integer
          description: 总 token 数。
        input_tokens:
          type: integer
          description: 输入 token 数（文本与参考图）。
        output_tokens:
          type: integer
          description: 输出 token 数（生成的图片）。
        input_tokens_details:
          type: object
          properties:
            text_tokens:
              type: integer
              description: 输入文本的 token 数，含 Prompt 增强折算的 token。
            image_tokens:
              type: integer
              description: 输入参考图的 token 数，文生图时为 0。
        output_tokens_details:
          type: object
          properties:
            image_tokens:
              type: integer
              description: 输出图片的 token 数。
    ImageStreamPartialSucceeded:
      type: object
      title: partial_succeeded
      description: 单张图片生成成功，每成功一张推送一次。按完成先后推送，用 `image_index` 对应张序。
      required:
        - type
        - image_index
        - url
      properties:
        type:
          type: string
          enum:
            - image_generation.partial_succeeded
          description: 事件类型，固定为 `image_generation.partial_succeeded`。
        created:
          type: integer
          description: 事件产生时的 Unix 时间戳（秒）。
        model:
          type: string
          description: 模型名称。
        image_index:
          type: integer
          description: 图片序号，从 0 开始，取值范围 [0, n-1]，与非流式响应 `data` 中的位置一致。
        url:
          type: string
          description: 图片链接，有效期 24 小时。
        size:
          type: string
          description: 图片实际尺寸，格式为 `宽x高`。
        output_format:
          type: string
          enum:
            - png
            - jpeg
            - webp
          description: 图片格式：`png`、`jpeg` 或 `webp`。
        revised_prompt:
          type: string
          description: >-
            实际用于生成该图片的 prompt：开启 Prompt 增强时为增强后的结果；`disable_prompt_enhanced` 为
            `true` 时与请求中的 `prompt` 相同。
    ImageStreamPartialFailed:
      type: object
      title: partial_failed
      description: 单张图片生成失败或未通过内容安全检查，其它图片不受影响，会继续推送。
      required:
        - type
        - image_index
        - code
        - message
      properties:
        type:
          type: string
          enum:
            - image_generation.partial_failed
          description: 事件类型，固定为 `image_generation.partial_failed`。
        created:
          type: integer
          description: 事件产生时的 Unix 时间戳（秒）。
        model:
          type: string
          description: 模型名称。
        image_index:
          type: integer
          description: 图片序号，从 0 开始，取值范围 [0, n-1]，与非流式响应 `data` 中的位置一致。
        code:
          type: string
          description: >-
            单张失败的错误码。常见取值：`1000` 生成失败，`1001` 等待超时，`1008` 余额不足，`1026` 增强后的 prompt
            未通过内容安全检查，`1027`
            生成的图片未通过内容安全检查。完整列表见[错误码查询列表](/api-reference/errorcode)。
        message:
          type: string
          description: 错误详情。
    ImageStreamCompleted:
      type: object
      title: completed
      description: 所有图片处理完毕且至少一张成功时推送，是流中的最后一个事件。
      required:
        - type
      properties:
        type:
          type: string
          enum:
            - image_generation.completed
          description: 事件类型，固定为 `image_generation.completed`。
        created:
          type: integer
          description: 事件产生时的 Unix 时间戳（秒）。
        model:
          type: string
          description: 模型名称。
        usage:
          $ref: '#/components/schemas/ImageUsage'
        request_id:
          type: string
          description: 请求 ID（即 Trace ID），反馈问题时请提供。
    ImageStreamError:
      type: object
      title: error
      description: >-
        一张图片都没有生成成功，或响应头返回后、提交生成前请求整体失败时推送，推送后流结束。不计费。不含 `created` 和
        `data`，每张图的失败原因见此前推送的 `partial_failed` 事件。
      required:
        - type
        - error
      properties:
        type:
          type: string
          enum:
            - error
          description: 固定为 `error`。
        error:
          $ref: '#/components/schemas/OaiErrorDetail'
          description: >-
            错误信息，与非流式请求 HTTP 错误响应中的 `error` 字段相同。全部图片失败时，`http_code` 为
            `422`（全部未通过内容安全检查）、`402`（全部因余额不足失败）或 `500`（其他情况）。
        usage:
          $ref: '#/components/schemas/ImageUsage'
          description: 各项均为 0。
        request_id:
          type: string
          description: 请求 ID（即 Trace ID），反馈问题时请提供。
    OaiError:
      type: object
      description: >-
        错误响应，HTTP 状态码即错误码。


        若全部图片均生成失败，额外返回 `created`、`data`（每张的失败原因）与 `usage`：全部因内容安全检查失败时返回
        422，全部因余额不足失败时返回 402，否则返回 500。
      properties:
        type:
          type: string
          description: 固定为 `error`。
          example: error
        error:
          $ref: '#/components/schemas/OaiErrorDetail'
        created:
          type: integer
          description: Unix 时间戳（秒），仅全部图片失败时返回。
        data:
          type: array
          description: 每张图片的失败原因，仅全部图片失败时返回。
          items:
            $ref: '#/components/schemas/ImageObject'
        usage:
          $ref: '#/components/schemas/ImageUsage'
          description: 仅全部图片失败时返回。
        request_id:
          type: string
          description: 请求 ID（即 Trace ID），反馈问题时请提供。
    OaiErrorDetail:
      type: object
      properties:
        type:
          type: string
          description: >-
            错误类型：`bad_request_error`（400）/ `authorized_error`（401）/
            `insufficient_balance_error`（402）/
            `unprocessable_entity_error`（422）/ `rate_limit_error`（429）/
            `server_error`（500）等。
        message:
          type: string
          description: >-
            错误详情，结尾括号内为内部错误码（如 `...
            (2013)`），可查看[错误码查询列表](/api-reference/errorcode)。
        http_code:
          type: string
          description: HTTP 状态码字符串，如 `400`。
  responses:
    Err400:
      description: 参数错误
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/OaiError'
          examples:
            invalid_size:
              summary: 参数错误
              value:
                type: error
                error:
                  type: bad_request_error
                  message: >-
                    invalid params, size 4096x1024: aspect ratio must be within
                    1:3 and 3:1 (2013)
                  http_code: '400'
                request_id: 021792308678142a2c883cf675b9804d
            b64_json:
              summary: b64_json 不满足条件
              value:
                type: error
                error:
                  type: bad_request_error
                  message: >-
                    invalid params, b64_json total output area (n x width x
                    height) 33554432 exceeds 20000000 for png, use url or
                    jpeg/webp instead (2013)
                  http_code: '400'
                request_id: 021792308678142a2c883cf675b9804d
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
            request_id: 021792308678142a2c883cf675b9804d
    Err402:
      description: 余额不足
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
            request_id: 021792308678142a2c883cf675b9804d
    Err422:
      description: 输入涉及敏感内容 / 所有图片都未通过内容安全检查
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/OaiError'
          examples:
            input_sensitive:
              summary: 输入涉及敏感内容
              value:
                type: error
                error:
                  type: unprocessable_entity_error
                  message: 'input content failed safety check: prompt (1026)'
                  http_code: '422'
                request_id: 021792308678142a2c883cf675b9804d
            all_images_failed:
              summary: 所有图片都未通过内容安全检查
              value:
                type: error
                error:
                  type: unprocessable_entity_error
                  message: >-
                    no image generated: all 2 images failed content safety check
                    (1027)
                  http_code: '422'
                created: 1792308678
                data:
                  - error:
                      code: '1027'
                      message: output image failed content safety check
                  - error:
                      code: '1027'
                      message: output image failed content safety check
                usage:
                  generated_images: 0
                  total_tokens: 0
                  input_tokens: 0
                  output_tokens: 0
                  input_tokens_details:
                    text_tokens: 0
                    image_tokens: 0
                  output_tokens_details:
                    image_tokens: 0
                request_id: 021792308678142a2c883cf675b9804d
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
              message: rate limit exceeded(IPM) (1002)
              http_code: '429'
            request_id: 021792308678142a2c883cf675b9804d
    Err500:
      description: 服务端错误
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/OaiError'
          examples:
            server_error:
              summary: 服务端错误
              value:
                type: error
                error:
                  type: server_error
                  message: internal error (1000)
                  http_code: '500'
                request_id: 021792308678142a2c883cf675b9804d
            all_images_failed:
              summary: 一张图片都没有生成成功（含服务端错误）
              value:
                type: error
                error:
                  type: server_error
                  message: 'no image generated: 1 x 1027, 1 x 1000 (1000)'
                  http_code: '500'
                created: 1792308678
                data:
                  - error:
                      code: '1027'
                      message: output image failed content safety check
                  - error:
                      code: '1000'
                      message: image generation failed
                usage:
                  generated_images: 0
                  total_tokens: 0
                  input_tokens: 0
                  output_tokens: 0
                  input_tokens_details:
                    text_tokens: 0
                    image_tokens: 0
                  output_tokens_details:
                    image_tokens: 0
                request_id: 021792308678142a2c883cf675b9804d
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      description: |-
        `HTTP: Bearer Auth`
         - Security Scheme Type: http
         - HTTP Authorization Scheme: Bearer API_key，用于验证账户信息，可在 [账户管理>接口密钥](https://platform.minimax.cn/user-center/basic-information/interface-key) 中查看。

````