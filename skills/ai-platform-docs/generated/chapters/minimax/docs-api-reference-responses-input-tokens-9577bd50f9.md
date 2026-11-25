<!-- Official source: https://platform.minimax.cn/docs/api-reference/responses-input-tokens.md -->
<!-- Source SHA-256: 85a5ff375579811b8cd86dcd569562ea5e61523e74ec6e386de278495b59a33b -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.minimaxi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Token 估算

> 估算请求的输入 token 数，不真正调用模型生成。常用于在调用主接口前评估请求成本与是否触发上下文长度上限。



## OpenAPI

````yaml api-reference/text/api/openapi-responses.json POST /v1/responses/input_tokens
openapi: 3.1.0
info:
  title: MiniMax Responses API
  description: MiniMax OpenAI Responses API 兼容接口，支持对话生成和 Token 估算
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.minimax.cn
security:
  - bearerAuth: []
paths:
  /v1/responses/input_tokens:
    post:
      tags:
        - Responses
      summary: Token 估算
      operationId: estimateInputTokens
      parameters:
        - name: Content-Type
          in: header
          required: true
          description: 请求体的媒介类型，请设置为 `application/json`，确保请求数据的格式为 JSON
          schema:
            type: string
            enum:
              - application/json
            default: application/json
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/EstimateInputTokensReq'
            examples:
              Request:
                value:
                  model: MiniMax-M3.1-Flash
                  input: >-
                    请帮我写一封邮件，邀请团队成员参加下周三下午 3
                    点的项目复盘会议，说明会议议程，并提醒大家提前准备各自负责模块的进展总结和遇到的问题。
        required: true
      responses:
        '200':
          description: 成功响应
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EstimateInputTokensResp'
              examples:
                Response:
                  value:
                    object: response.input_tokens
                    input_tokens: 235
components:
  schemas:
    EstimateInputTokensReq:
      type: object
      required:
        - model
        - input
      properties:
        model:
          type: string
          description: 调用的模型名称，如 `MiniMax-M3.1-Flash`
          example: MiniMax-M3.1-Flash
        input:
          description: 对话内容，支持简单文本或完整对话历史数组
          oneOf:
            - type: string
              description: 简单文本输入
            - type: array
              description: 完整对话历史
              items:
                $ref: '#/components/schemas/InputItem'
        instructions:
          type: string
          description: 系统指令
        tools:
          type: array
          description: 工具列表
          items:
            $ref: '#/components/schemas/Tool'
        tool_choice:
          type: string
          enum:
            - auto
          description: 工具选择策略：`auto` 表示由模型自动判断是否调用工具
        text:
          type: object
          description: 输出格式控制
          properties:
            format:
              type: object
              properties:
                type:
                  type: string
                  enum:
                    - text
                  default: text
                  description: 输出格式类型
        reasoning:
          type: object
          description: >-
            推理控制。默认值随模型不同，因此未在 schema 层声明统一默认值。

            - `MiniMax-M3.1-Flash`：推理始终开启，省略 `reasoning` 时也会推理。`effort` 可取
            `low`、`medium`、`high`、`xhigh` 或 `max`，并且确实会调节推理深度；省略时默认使用 `max`
            档位。传入 `effort: "none"` 会返回 HTTP 400。

            - `MiniMax-M3`：默认关闭推理；将 `effort` 设为非 `none` 值可开启推理，但不会调节推理深度。
          properties:
            effort:
              type: string
              enum:
                - minimal
                - low
                - medium
                - high
                - xhigh
                - max
                - none
          required: []
    EstimateInputTokensResp:
      type: object
      required:
        - object
        - input_tokens
      properties:
        object:
          type: string
          enum:
            - response.input_tokens
          description: 对象类型，固定为 `response.input_tokens`
        input_tokens:
          type: integer
          description: 估算的输入 token 数
    InputItem:
      type: object
      description: >-
        对话历史条目。`type` 字段决定具体形态：`message`（默认）/ `function_call` /
        `function_call_output` / `reasoning`
      properties:
        type:
          type: string
          enum:
            - message
            - function_call
            - function_call_output
            - reasoning
          default: message
          description: 条目类型
        role:
          type: string
          enum:
            - user
            - assistant
            - system
            - developer
            - tool
          description: 消息角色（仅当 `type` 为 `message` 时使用）
        content:
          description: >-
            消息内容，可以是字符串或多模态片段数组（仅当 `type` 为 `message` 时使用）


            **多模态输入限制**（适用于 `MiniMax-M3.1-Flash` 和 `MiniMax-M3`）

            - URL / Base64 方式传入：视频文件 ≤ 50 MB，图片文件 ≤ 10 MB，请求体 ≤ 64 MB。

            - 使用 Files API 上传：以 `mm_file://{file_id}` 形式引用，单个视频最大 512 MB。

            - 单次请求的 `input`（含历史轮次）累计最多 200 张图片、20 个视频。

            - 图片和视频的宽、高须大于 0，宽高比不超过 200:1。

            - 视频必须包含视频轨（纯音频文件不支持），时长大于 0 且不超过 30 分钟。

            - 抽帧数按 `round(时长 × fps / 2) × 2` 计算，须不少于 2 且不超过视频实际总帧数；`时长 × fps` 小于
            1 时一定无法满足，`fps` 高于视频本身的帧率时通常也无法满足。

            - 视频像素总量 `缩放后单帧宽 × 缩放后单帧高 × 抽帧数 / 2` 不超过 301,056,000。单帧按 `detail` 或
            `max_long_side_pixel` 缩放，长边上限：`low` 504、`default` 672、`high` 1288。
          oneOf:
            - type: string
            - type: array
              items:
                $ref: '#/components/schemas/ContentPart'
        call_id:
          type: string
          description: 工具调用 ID（仅当 `type` 为 `function_call` 或 `function_call_output` 时使用）
        name:
          type: string
          description: 函数名（仅当 `type` 为 `function_call` 时使用）
        arguments:
          type: string
          description: 函数参数的 JSON 字符串（仅当 `type` 为 `function_call` 时使用）
        output:
          description: 工具返回结果（仅当 `type` 为 `function_call_output` 时使用）
          oneOf:
            - type: string
            - type: array
              items:
                $ref: '#/components/schemas/ContentPart'
        summary:
          type: array
          description: 思维链段落数组（仅当 `type` 为 `reasoning` 时使用）
          items:
            type: object
            properties:
              type:
                type: string
                enum:
                  - summary_text
              text:
                type: string
                description: 思维链文本
    Tool:
      type: object
      required:
        - type
        - name
      properties:
        type:
          type: string
          enum:
            - function
          description: 工具类型
        name:
          type: string
          description: 函数名称
        description:
          type: string
          description: 函数说明，用于模型判断何时调用
        parameters:
          type: object
          description: 函数参数定义，使用 JSON Schema 格式
    ContentPart:
      type: object
      required:
        - type
      description: 消息内容片段
      properties:
        type:
          type: string
          enum:
            - input_text
            - output_text
            - input_image
            - input_video
          description: |-
            内容片段类型：
            - `input_text` / `output_text`: 文本片段
            - `input_image`: 图片输入
            - `input_video`: 视频输入
        text:
          type: string
          description: 文本内容（当 `type` 为 `input_text` / `output_text` 时）
        image_url:
          description: 图片输入（当 `type` 为 `input_image` 时）。支持的格式：JPEG、PNG、GIF、WEBP
          oneOf:
            - type: string
            - type: object
              required:
                - url
              properties:
                url:
                  type: string
                  description: 图片链接或 Base64 编码
                detail:
                  type: string
                  enum:
                    - low
                    - default
                    - high
                  default: default
                  description: 图片理解的精细度档位
        video_url:
          description: 视频输入（当 `type` 为 `input_video` 时）。支持的格式：MP4、AVI、MOV、MKV
          oneOf:
            - type: string
            - type: object
              required:
                - url
              properties:
                url:
                  type: string
                  description: >-
                    视频 URL、Base64 data URL，或形如 `mm_file://{file_id}` 的 Files API
                    引用。`file_id`
                    需先通过[文件上传](/api-reference/file-management-upload)接口上传视频后获取。
                fps:
                  type: number
                  format: float
                  default: 2
                  minimum: 0.2
                  maximum: 5
                  description: 视频抽帧频率，默认值为 2，范围 [0.2, 5]。
                detail:
                  type: string
                  enum:
                    - low
                    - default
                    - high
                  default: default
                  description: 视频理解的精细度档位
                max_long_side_pixel:
                  type: integer
                  description: 视频帧最长边的像素约束
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: |-
        `HTTP: Bearer Auth`
         - Security Scheme Type: http
         - HTTP Authorization Scheme: Bearer API_key，用于验证账户信息，可在 [账户管理>接口密钥](https://platform.minimax.cn/user-center/basic-information/interface-key) 中查看

````