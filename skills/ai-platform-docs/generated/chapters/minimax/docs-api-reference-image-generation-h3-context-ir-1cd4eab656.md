<!-- Official source: https://platform.minimax.cn/docs/api-reference/image-generation-h3-context-ir.md -->
<!-- Source SHA-256: f24c3c997eb1d1e1abda5f1bc1058ed5a7429b8939207d451211c3562ce03fc5 -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.minimaxi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# H3-Image-Context-IR

> 单独调用 MiniMax-H3-Image 的 Prompt 增强，同步返回增强后的 prompt，不生成图片。

> [!WARNING]
>
> 本接口只返回增强后的 prompt，不会生成图片。

本接口与[文生图](https://platform.minimaxi.com/docs/api-reference/image-generation-h3-generations.md)、[图片编辑](https://platform.minimaxi.com/docs/api-reference/image-generation-h3-edits.md)内置的 Prompt 增强相同：不传 `images` 时按文生图增强，传入参考图时按图片编辑增强。可用于预览和修改增强结果，或在自己的工作流中分步调用。

当前支持模型：`MiniMax-H3-Image`；`MiniMax-H3-Image-Highspeed` 不支持本接口，传入返回 400。服务端最长等待 600 秒，建议客户端超时不低于 600 秒。

> [!NOTE]
>
> **计费**：Prompt 增强调用模型的输入、输出与思考 token 按单价折算为等价的输入文字 token，计入 `usage.input_tokens`，不单独计输出。请求失败（含未通过内容安全检查）不计费。

> [!NOTE]
>
> **分两步生成**：文生图可将 `revised_prompt` 作为[文生图](https://platform.minimaxi.com/docs/api-reference/image-generation-h3-generations.md)请求的 `prompt`，设置 `disable_prompt_enhanced: true`，并传入响应中的 `aspect_ratio`（或自行指定 `size` / `aspect_ratio`），生成请求不再计 Prompt 增强的费用。图片编辑始终开启 Prompt 增强，将结果传给图片编辑接口时会再次增强并计费。


## OpenAPI

````yaml api-reference/image/generation/api/h3-image-context-ir.json POST /v1/h3_image_context_ir
openapi: 3.1.0
info:
  title: MiniMax H3-Image Context IR API
  description: MiniMax H3-Image API
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.minimax.cn
security:
  - bearerAuth: []
paths:
  /v1/h3_image_context_ir:
    post:
      tags:
        - Image
      summary: H3-Image-Context-IR
      description: >-
        单独调用 MiniMax-H3-Image 的 Prompt 增强，同步返回增强后的 prompt，不生成图片。


        - 不传 `images`：按文生图增强

        - 传 `images`（1 ~ 16 张）：结合参考图按图片编辑增强


        当前支持模型：`MiniMax-H3-Image`；`MiniMax-H3-Image-Highspeed` 不支持本接口，传入返回
        400。通常数秒内返回，服务端最长等待 600 秒，建议客户端超时不低于 600 秒。
      operationId: h3ImageContextIR
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/H3ImageContextIRReq'
            examples:
              t2i:
                summary: 文生图增强
                value:
                  model: MiniMax-H3-Image
                  prompt: 一只橘猫趴在窗台上晒太阳，午后暖光，胶片质感
              edit:
                summary: 图片编辑增强
                value:
                  model: MiniMax-H3-Image
                  prompt: 把图1里的猫换成图2里的柴犬，保持背景不变
                  images:
                    - image_url: https://example.com/cat.jpg
                    - image_url: https://example.com/dog.png
                  aspect_ratio: auto
      responses:
        '200':
          description: 增强成功，返回增强后的 prompt。
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/H3ImageContextIRResponse'
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

            - `1002`：超过每分钟请求数（RPM）上限
            - `2056`：使用 M Plan 时，套餐用量达到上限
        '500':
          $ref: '#/components/responses/Err500'
components:
  schemas:
    H3ImageContextIRReq:
      type: object
      required:
        - model
        - prompt
      properties:
        model:
          type: string
          description: 模型名称。可选值：`MiniMax-H3-Image`
          enum:
            - MiniMax-H3-Image
        prompt:
          type: string
          maxLength: 32000
          description: 需要增强的文本描述，最长 32000 个字符（按 Unicode 字符计，不含首尾空白），为空或只含空白时返回 400。
        images:
          type: array
          minItems: 1
          maxItems: 16
          description: >-
            参考图列表，1 ~ 16 张。传入时结合参考图按图片编辑增强，不传时按文生图增强。


            **参考图限制**（请求体总大小 ≤ 64 MiB，Base64 编码后的大小约为原文件的 4/3；超过该上限时请改用公网 URL 或
            `mm_file://`）


            | 项 | 限制 |

            | :--- | :--- |

            | 格式 | JPG、JPEG、PNG、WEBP、HEIC、HEIF |

            | 单文件大小 | ≤ 64 MiB |

            | 宽高范围 | [128, 8192] px |

            | 长宽比（长边/短边） | ≤ 4:1 |

            | 数量 | 1 ~ 16 |
          items:
            $ref: '#/components/schemas/ImageInput'
        size:
          type: string
          default: auto
          description: >-
            目标输出尺寸，默认
            `auto`。写法与生成接口相同，两种写法二选一，详见[输出尺寸](/guides/image-generation#输出尺寸)。


            - `宽x高`：如 `2720x1536`，图片编辑增强按该宽高的比例描述画面。面积与宽高比的限制同生成接口，不满足时返回
            400；此时不能再传 `aspect_ratio` 或 `area`（传 `auto` 也不行），否则返回 400

            - `auto` 或不传：比例由 `aspect_ratio` 决定


            尺寸参数只影响图片编辑增强，文生图增强不读取尺寸参数。
        aspect_ratio:
          type: string
          default: auto
          example: '16:9'
          description: >-
            目标宽高比，默认 `auto`。只能在 `size` 不传或为 `auto` 时传入，`size` 为 `宽x高` 时传入返回 400。


            - `auto`：由 Prompt 增强决定，结果见响应中的 `aspect_ratio`

            - `X:Y`：X、Y 为 1 ~ 300 的整数，宽高比在 1:3 ~ 3:1 之间（含边界），如
            `16:9`、`3:4`。图片编辑增强按该比例描述画面，响应不返回 `aspect_ratio`
        area:
          type: string
          enum:
            - 1K
            - 2K
            - 4K
          default: 4K
          description: >-
            面积档位，可选 `1K`、`2K`、`4K`，默认 `4K`。只能在 `size` 不传或为 `auto` 时传入，`size` 为
            `宽x高` 时传入返回 400。不影响增强结果，便于与生成请求使用同一组参数。
    H3ImageContextIRResponse:
      type: object
      properties:
        created:
          type: integer
          description: 响应生成时间，Unix 时间戳（秒）。
        revised_prompt:
          type: string
          description: 增强后的 prompt。
        aspect_ratio:
          type: string
          example: '3:2'
          description: >-
            Prompt 增强给出的宽高比，格式为 `X:Y`，在 1:3 ~ 3:1 之间。仅当比例由增强决定（`size` 不传或为
            `auto`，且 `aspect_ratio` 不传或为 `auto`）时返回。
        usage:
          $ref: '#/components/schemas/H3ImageContextIRUsage'
        request_id:
          type: string
          description: 请求 ID（即 Trace ID），反馈问题时请提供。
      example:
        created: 1794023743
        revised_prompt: >-
          一只橘色虎斑猫慵懒地趴在木质窗台上晒太阳，午后暖金色的阳光从窗外斜射进来，在猫毛和窗台上形成柔和的光斑，背景的窗帘与室内陈设略微虚化，整体呈现温暖的胶片质感，颗粒细腻、色调偏暖。
        aspect_ratio: '3:2'
        usage:
          total_tokens: 3489
          input_tokens: 3489
        request_id: 021792308678142a2c883cf675b9804d
    ImageInput:
      type: object
      description: 单张参考图。
      required:
        - image_url
      properties:
        image_url:
          type: string
          description: >-
            图片地址,支持:公网 URL;`mm_file://{file_id}`(引用已上传文件,file_id
            通过[文件上传](/api-reference/file-management-upload)接口以 `purpose` 为
            `image_generation_input` 上传获得);`data:image/<格式>;base64,<Base64>`
            data URI(`<格式>` 小写)。
    H3ImageContextIRUsage:
      type: object
      description: 本次请求的 token 用量，用于计费。Prompt 增强的成本统一折算为输入文字 token，不单独计输出。
      properties:
        total_tokens:
          type: integer
          description: 总 token 数，与 `input_tokens` 相同。
        input_tokens:
          type: integer
          description: >-
            输入文字 token 数。Prompt 增强调用模型的输入、输出与思考 token 按单价折算为等价的输入文字
            token，口径与生成接口 `usage.input_tokens_details.text_tokens` 中 Prompt
            增强的部分相同。
    OaiError:
      type: object
      description: 错误响应，HTTP 状态码即错误码。请求失败时不计费。
      properties:
        type:
          type: string
          description: 固定为 `error`。
          example: error
        error:
          $ref: '#/components/schemas/OaiErrorDetail'
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
          example:
            type: error
            error:
              type: bad_request_error
              message: invalid params, area must be one of 1K, 2K, 4K (2013)
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
      description: 输入或增强结果涉及敏感内容
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
            revised_prompt_sensitive:
              summary: 增强结果未通过内容安全检查
              value:
                type: error
                error:
                  type: unprocessable_entity_error
                  message: 'input content failed safety check: revised_prompt (1026)'
                  http_code: '422'
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
              message: rate limit exceeded(RPM) (1002)
              http_code: '429'
            request_id: 021792308678142a2c883cf675b9804d
    Err500:
      description: 服务端错误
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/OaiError'
          examples:
            timeout:
              summary: Prompt 增强超时
              value:
                type: error
                error:
                  type: server_error
                  message: request timeout, prompt rewrite timed out (1001)
                  http_code: '500'
                request_id: 021792308678142a2c883cf675b9804d
            server_error:
              summary: 服务端错误
              value:
                type: error
                error:
                  type: server_error
                  message: system error, prompt rewrite failed (1033)
                  http_code: '500'
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