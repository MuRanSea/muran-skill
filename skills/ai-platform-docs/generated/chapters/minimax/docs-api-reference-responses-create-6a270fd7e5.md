<!-- Official source: https://platform.minimax.cn/docs/api-reference/responses-create.md -->
<!-- Source SHA-256: 4fb78e02136b74a7746293aba3cc1294af47cc9beb908ce230dc064b7b4d87c4 -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.minimaxi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 对话生成

> OpenAI Responses API 兼容的主接口调用MiniMax 模型，生成模型回复，支持流式与非流式。

export const ResponsesReturnValues = ({label}) => {
  const marker = useRef(null);
  useEffect(() => {
    const root = marker.current?.closest("#content-container");
    if (!root) return;
    const fixedFields = new Set(["response-object", "response-parallel-tool-calls", "response-store", "response-truncation"]);
    const hiddenRows = new Map();
    const updateLabels = () => {
      root.querySelectorAll('[id^="response-"]').forEach(heading => {
        const field = heading.closest(".primitive-param-field");
        field?.querySelectorAll(".whitespace-pre-wrap.prose-sm").forEach(row => {
          if (fixedFields.has(heading.id) && row.querySelectorAll("code").length === 1) {
            if (!hiddenRows.has(row)) hiddenRows.set(row, row.hidden);
            row.hidden = true;
          }
          row.childNodes.forEach(node => {
            if (node.nodeType === Node.TEXT_NODE && (/^(可用选项|Available options)$/).test(node.textContent.trim())) {
              node.textContent = label;
            }
          });
        });
      });
    };
    updateLabels();
    const observer = new MutationObserver(updateLabels);
    observer.observe(root, {
      childList: true,
      subtree: true,
      characterData: true
    });
    return () => {
      observer.disconnect();
      hiddenRows.forEach((hidden, row) => {
        row.hidden = hidden;
      });
    };
  }, [label]);
  return <span ref={marker} hidden />;
};

<ResponsesReturnValues label="可能的返回值" />


## OpenAPI

````yaml api-reference/text/api/openapi-responses.json POST /v1/responses
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
  /v1/responses:
    post:
      tags:
        - Responses
      summary: 对话生成
      operationId: createResponse
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
              $ref: '#/components/schemas/CreateResponseReq'
            examples:
              深度思考:
                value:
                  model: MiniMax-M3.1-Flash
                  reasoning:
                    effort: max
                  input: 9.11 和 9.9 哪个更大？
              图片理解:
                value:
                  model: MiniMax-M3.1-Flash
                  reasoning:
                    effort: max
                  input:
                    - role: user
                      content:
                        - type: input_text
                          text: 这张图片的内容是什么？
                        - type: input_image
                          image_url: >-
                            https://filecdn.minimax.chat/public/fe9d04da-f60e-444d-a2e0-18ae743add33.jpeg
              视频理解:
                value:
                  model: MiniMax-M3.1-Flash
                  reasoning:
                    effort: max
                  input:
                    - role: user
                      content:
                        - type: input_text
                          text: 这个视频里发生了什么？
                        - type: input_video
                          video_url: >-
                            https://filecdn.minimax.chat/public/ee8c1648-21f1-41b7-8397-65022d22ffe5.mp4
              流式:
                value:
                  model: MiniMax-M3.1-Flash
                  reasoning:
                    effort: max
                  input:
                    - role: user
                      content:
                        - type: input_text
                          text: 这张图片的内容是什么？
                        - type: input_image
                          image_url: >-
                            https://filecdn.minimax.chat/public/fe9d04da-f60e-444d-a2e0-18ae743add33.jpeg
                  stream: true
              工具调用:
                value:
                  model: MiniMax-M3.1-Flash
                  reasoning:
                    effort: max
                  input: 旧金山现在天气怎么样？
                  tools:
                    - type: function
                      name: get_weather
                      description: Get the current weather for a given location.
                      parameters:
                        type: object
                        properties:
                          location:
                            type: string
                            description: The city and state/country, e.g. San Francisco, US
                        required:
                          - location
        required: true
      responses:
        '200':
          description: 成功响应
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateResponseResp'
              examples:
                深度思考:
                  value:
                    id: 07229fa4ff19f5b74ad4581cad3af46c
                    object: response
                    created_at: 1792240804
                    model: MiniMax-M3.1-Flash
                    status: completed
                    output:
                      - id: 07229fa4ff19f5b74ad4581cad3af46c_rs
                        type: reasoning
                        status: completed
                        summary: []
                        content:
                          - type: reasoning_text
                            text: >-
                              We need answer Chinese. Need determine 9.11 vs
                              9.9. Decimal comparison: 9.9 = 9.90 > 9.11. User
                              asks which larger. Need concise maybe explain.
                              Ensure not date ambiguity? They ask 9.11 and 9.9
                              likely decimals. Answer 9.9 larger. Chinese.
                      - id: 07229fa4ff19f5b74ad4581cad3af46c_msg
                        type: message
                        status: completed
                        role: assistant
                        content:
                          - type: output_text
                            text: |-
                              9.9 更大。

                              因为把小数位补齐：9.9 = 9.90，而 9.90 > 9.11。
                            annotations: []
                    output_text: |-
                      9.9 更大。

                      因为把小数位补齐：9.9 = 9.90，而 9.90 > 9.11。
                    usage:
                      input_tokens: 216
                      output_tokens: 107
                      total_tokens: 323
                      input_tokens_details:
                        cached_tokens: 189
                      output_tokens_details:
                        reasoning_tokens: 75
                    error: null
                    incomplete_details: null
                    instructions: null
                    metadata: {}
                    tools: null
                    tool_choice: auto
                    temperature: 1
                    top_p: 0.95
                    text:
                      format:
                        type: text
                    reasoning:
                      effort: max
                      summary: null
                    max_output_tokens: null
                    parallel_tool_calls: true
                    previous_response_id: null
                    conversation: null
                    store: false
                    service_tier: null
                    safety_identifier: null
                    truncation: disabled
                图片理解:
                  value:
                    id: 07229fa4f4b7aa2578eef43416353b1e
                    object: response
                    created_at: 1792240804
                    model: MiniMax-M3.1-Flash
                    status: completed
                    output:
                      - id: 07229fa4f4b7aa2578eef43416353b1e_rs
                        type: reasoning
                        status: completed
                        summary: []
                        content:
                          - type: reasoning_text
                            text: >-
                              We need answer Chinese. Need describe image. We
                              can identify generic child, no sensitive. Need
                              maybe mention close-up portrait of young girl
                              smiling, curly brown hair bangs, green/hazel eyes,
                              white lace dress, warm soft lighting, blurred
                              brown-gray background. Since user asks content.
                              Need concise. Ensure not infer identity. Let's
                              craft.
                      - id: 07229fa4f4b7aa2578eef43416353b1e_msg
                        type: message
                        status: completed
                        role: assistant
                        content:
                          - type: output_text
                            text: >-
                              这是一张小女孩的暖调人像特写。她留着棕色卷发和齐刘海，睁着绿色或棕绿色的眼睛，面带微笑，身穿带蕾丝领口和肩部装饰的白色连衣裙。背景呈柔和的棕灰色虚化，光线温暖自然。
                            annotations: []
                    output_text: >-
                      这是一张小女孩的暖调人像特写。她留着棕色卷发和齐刘海，睁着绿色或棕绿色的眼睛，面带微笑，身穿带蕾丝领口和肩部装饰的白色连衣裙。背景呈柔和的棕灰色虚化，光线温暖自然。
                    usage:
                      input_tokens: 1407
                      output_tokens: 127
                      total_tokens: 1534
                      input_tokens_details:
                        cached_tokens: 1405
                      output_tokens_details:
                        reasoning_tokens: 70
                    error: null
                    incomplete_details: null
                    instructions: null
                    metadata: {}
                    tools: null
                    tool_choice: auto
                    temperature: 1
                    top_p: 0.95
                    text:
                      format:
                        type: text
                    reasoning:
                      effort: max
                      summary: null
                    max_output_tokens: null
                    parallel_tool_calls: true
                    previous_response_id: null
                    conversation: null
                    store: false
                    service_tier: null
                    safety_identifier: null
                    truncation: disabled
                视频理解:
                  value:
                    id: 07229fa44741487d6937e3789ea56819
                    object: response
                    created_at: 1792240804
                    model: MiniMax-M3.1-Flash
                    status: completed
                    output:
                      - id: 07229fa44741487d6937e3789ea56819_rs
                        type: reasoning
                        status: completed
                        summary: []
                        content:
                          - type: reasoning_text
                            text: >-
                              We need answer in Chinese likely describe video.
                              Need inspect sequence. We have frames 0-5.5 sec.
                              It's a generated/edited video perhaps cat in
                              Olympic diving venue, running along diving
                              board/platform, leaps into pool, splash. Need
                              accurately state. Let's parse details.


                              At 0: cat (Asian? wildcat-looking domestic cat,
                              spotted/striped) walking on narrow turquoise
                              diving board/beam over pool in Olympic stadium.
                              Background Olympic rings, crowds, purple signage
                              "Lausanne 2024" perhaps. Camera tracks as cat
                              runs. At ~2.5 sec cat leaps, paws extended, flying
                              over diving platform, rotates/dives headfirst into
                              pool around 4 sec, splash at 4.5, ripples. Need
                              mention no visible injury perhaps. User asks
                              "这个视频里发生了什么？" likely concise Chinese description.
                              We should avoid overclaiming exact
                              venue/competition or whether real. Say video
                              depicts a cat walking/running along diving
                              platform in an Olympic-themed swimming/diving
                              arena, then jumps and dives into pool causing
                              splash, ending with ripples. Maybe note it appears
                              AI-generated due image/video artifacts/watermarks
                              MiniMax/Hailuo AI. Should we mention? Could be
                              useful but not needed. Need answer natural.


                              Let's formulate:
                              "视频中，一只带斑纹的猫在类似奥运会跳水馆的跳板/池边窄台上向前奔跑，背景有奥运五环和观众。跑到尽头后纵身跃起，身体在空中翻转，随后头朝下扎入泳池，激起大片水花；最后水面只剩涟漪和逐渐消散的水花。"
                              Maybe if question wants event summary. Include
                              duration ~5.5 sec. Need perhaps mention cat lands
                              in diving pool, not necessarily headfirst? Frame
                              3.5 body vertical head down, yes.


                              Let's answer Chinese.
                      - id: 07229fa44741487d6937e3789ea56819_msg
                        type: message
                        status: completed
                        role: assistant
                        content:
                          - type: output_text
                            text: >-
                              视频里，一只带斑纹的猫沿着奥运跳水馆池边的窄平台向前奔跑，背景有奥运五环和观众。跑到尽头后，它纵身跃起，在空中翻转后头朝下跳入泳池，激起一大片水花，最后水面只剩下逐渐扩散的涟漪。
                            annotations: []
                    output_text: >-
                      视频里，一只带斑纹的猫沿着奥运跳水馆池边的窄平台向前奔跑，背景有奥运五环和观众。跑到尽头后，它纵身跃起，在空中翻转后头朝下跳入泳池，激起一大片水花，最后水面只剩下逐渐扩散的涟漪。
                    usage:
                      input_tokens: 2285
                      output_tokens: 430
                      total_tokens: 2715
                      input_tokens_details:
                        cached_tokens: 2283
                      output_tokens_details:
                        reasoning_tokens: 369
                    error: null
                    incomplete_details: null
                    instructions: null
                    metadata: {}
                    tools: null
                    tool_choice: auto
                    temperature: 1
                    top_p: 0.95
                    text:
                      format:
                        type: text
                    reasoning:
                      effort: max
                      summary: null
                    max_output_tokens: null
                    parallel_tool_calls: true
                    previous_response_id: null
                    conversation: null
                    store: false
                    service_tier: null
                    safety_identifier: null
                    truncation: disabled
                流式:
                  value:
                    - type: response.created
                      sequence_number: 0
                      response:
                        id: 07229fa479c585e3683008175f57bd8f
                        object: response
                        created_at: 1792240804
                        model: MiniMax-M3.1-Flash
                        status: in_progress
                        output: []
                        output_text: null
                        usage: null
                        error: null
                        incomplete_details: null
                        instructions: null
                        metadata: {}
                        tools: null
                        tool_choice: auto
                        temperature: 1
                        top_p: 0.95
                        text:
                          format:
                            type: text
                        reasoning:
                          effort: max
                          summary: null
                        max_output_tokens: null
                        parallel_tool_calls: true
                        previous_response_id: null
                        conversation: null
                        store: false
                        service_tier: null
                        safety_identifier: null
                        truncation: disabled
                    - type: response.in_progress
                      sequence_number: 1
                      response:
                        id: 07229fa479c585e3683008175f57bd8f
                        object: response
                        created_at: 1792240804
                        model: MiniMax-M3.1-Flash
                        status: in_progress
                        output: []
                        output_text: null
                        usage: null
                        error: null
                        incomplete_details: null
                        instructions: null
                        metadata: {}
                        tools: null
                        tool_choice: auto
                        temperature: 1
                        top_p: 0.95
                        text:
                          format:
                            type: text
                        reasoning:
                          effort: max
                          summary: null
                        max_output_tokens: null
                        parallel_tool_calls: true
                        previous_response_id: null
                        conversation: null
                        store: false
                        service_tier: null
                        safety_identifier: null
                        truncation: disabled
                    - type: response.output_item.added
                      sequence_number: 2
                      item:
                        id: 07229fa479c585e3683008175f57bd8f_rs
                        type: reasoning
                        status: in_progress
                        summary: []
                        content: []
                      output_index: 0
                    - type: response.content_part.added
                      sequence_number: 3
                      part:
                        type: reasoning_text
                        text: ''
                      output_index: 0
                      content_index: 0
                      item_id: 07229fa479c585e3683008175f57bd8f_rs
                    - type: response.reasoning_text.delta
                      sequence_number: 4
                      output_index: 0
                      content_index: 0
                      item_id: 07229fa479c585e3683008175f57bd8f_rs
                      delta: We need answer
                    - type: response.reasoning_text.delta
                      sequence_number: 5
                      output_index: 0
                      content_index: 0
                      item_id: 07229fa479c585e3683008175f57bd8f_rs
                      delta: ' Chinese describe image. Need be careful child, identity unknown. Need content: close-up portrait of young girl, brown'
                    - type: response.reasoning_text.delta
                      sequence_number: 6
                      output_index: 0
                      content_index: 0
                      item_id: 07229fa479c585e3683008175f57bd8f_rs
                      delta: ' wavy hair bangs, looking camera slight smile, cream lace dress, warm golden light, neutral blurred'
                    - type: response.reasoning_text.delta
                      sequence_number: 7
                      output_index: 0
                      content_index: 0
                      item_id: 07229fa479c585e3683008175f57bd8f_rs
                      delta: ' background. We should not infer ethnicity perhaps. concise. Maybe mention eyes green/hazel. Need answer in'
                    - type: response.reasoning_text.delta
                      sequence_number: 8
                      output_index: 0
                      content_index: 0
                      item_id: 07229fa479c585e3683008175f57bd8f_rs
                      delta: ' Chinese.'
                    - type: response.reasoning_text.done
                      sequence_number: 9
                      output_index: 0
                      content_index: 0
                      item_id: 07229fa479c585e3683008175f57bd8f_rs
                      text: >-
                        We need answer Chinese describe image. Need be careful
                        child, identity unknown. Need content: close-up portrait
                        of young girl, brown wavy hair bangs, looking camera
                        slight smile, cream lace dress, warm golden light,
                        neutral blurred background. We should not infer
                        ethnicity perhaps. concise. Maybe mention eyes
                        green/hazel. Need answer in Chinese.
                    - type: response.content_part.done
                      sequence_number: 10
                      part:
                        type: reasoning_text
                        text: >-
                          We need answer Chinese describe image. Need be careful
                          child, identity unknown. Need content: close-up
                          portrait of young girl, brown wavy hair bangs, looking
                          camera slight smile, cream lace dress, warm golden
                          light, neutral blurred background. We should not infer
                          ethnicity perhaps. concise. Maybe mention eyes
                          green/hazel. Need answer in Chinese.
                      output_index: 0
                      content_index: 0
                      item_id: 07229fa479c585e3683008175f57bd8f_rs
                    - type: response.output_item.done
                      sequence_number: 11
                      item:
                        id: 07229fa479c585e3683008175f57bd8f_rs
                        type: reasoning
                        status: completed
                        summary: []
                        content:
                          - type: reasoning_text
                            text: >-
                              We need answer Chinese describe image. Need be
                              careful child, identity unknown. Need content:
                              close-up portrait of young girl, brown wavy hair
                              bangs, looking camera slight smile, cream lace
                              dress, warm golden light, neutral blurred
                              background. We should not infer ethnicity perhaps.
                              concise. Maybe mention eyes green/hazel. Need
                              answer in Chinese.
                      output_index: 0
                    - type: response.output_item.added
                      sequence_number: 12
                      item:
                        type: message
                        status: in_progress
                        role: assistant
                        content: []
                        id: 07229fa479c585e3683008175f57bd8f_msg_1
                      output_index: 1
                    - type: response.content_part.added
                      sequence_number: 13
                      part:
                        type: output_text
                        text: ''
                        annotations: []
                      output_index: 1
                      content_index: 0
                      item_id: 07229fa479c585e3683008175f57bd8f_msg_1
                    - type: response.output_text.delta
                      sequence_number: 14
                      output_index: 1
                      content_index: 0
                      item_id: 07229fa479c585e3683008175f57bd8f_msg_1
                      delta: 这是一张小女孩的暖色调肖像特写。她留着棕色卷发
                    - type: response.output_text.delta
                      sequence_number: 15
                      output_index: 1
                      content_index: 0
                      item_id: 07229fa479c585e3683008175f57bd8f_msg_1
                      delta: 和齐刘海，穿着带蕾丝边的米白色连衣裙，微微笑着看向镜头。画面
                    - type: response.output_text.delta
                      sequence_number: 16
                      output_index: 1
                      content_index: 0
                      item_id: 07229fa479c585e3683008175f57bd8f_msg_1
                      delta: 采用柔和的侧光与浅景深，背景呈棕灰色虚化，整体温馨
                    - type: response.output_text.delta
                      sequence_number: 17
                      output_index: 1
                      content_index: 0
                      item_id: 07229fa479c585e3683008175f57bd8f_msg_1
                      delta: 自然。
                    - type: response.output_text.done
                      sequence_number: 18
                      output_index: 1
                      content_index: 0
                      item_id: 07229fa479c585e3683008175f57bd8f_msg_1
                      text: >-
                        这是一张小女孩的暖色调肖像特写。她留着棕色卷发和齐刘海，穿着带蕾丝边的米白色连衣裙，微微笑着看向镜头。画面采用柔和的侧光与浅景深，背景呈棕灰色虚化，整体温馨自然。
                    - type: response.content_part.done
                      sequence_number: 19
                      part:
                        type: output_text
                        text: >-
                          这是一张小女孩的暖色调肖像特写。她留着棕色卷发和齐刘海，穿着带蕾丝边的米白色连衣裙，微微笑着看向镜头。画面采用柔和的侧光与浅景深，背景呈棕灰色虚化，整体温馨自然。
                        annotations: []
                      output_index: 1
                      content_index: 0
                      item_id: 07229fa479c585e3683008175f57bd8f_msg_1
                    - type: response.output_item.done
                      sequence_number: 20
                      item:
                        id: 07229fa479c585e3683008175f57bd8f_msg_1
                        type: message
                        status: completed
                        role: assistant
                        content:
                          - type: output_text
                            text: >-
                              这是一张小女孩的暖色调肖像特写。她留着棕色卷发和齐刘海，穿着带蕾丝边的米白色连衣裙，微微笑着看向镜头。画面采用柔和的侧光与浅景深，背景呈棕灰色虚化，整体温馨自然。
                            annotations: []
                      output_index: 1
                    - type: response.completed
                      sequence_number: 21
                      response:
                        id: 07229fa479c585e3683008175f57bd8f
                        object: response
                        created_at: 1792240804
                        model: MiniMax-M3.1-Flash
                        status: completed
                        output:
                          - id: 07229fa479c585e3683008175f57bd8f_rs
                            type: reasoning
                            status: completed
                            summary: []
                            content:
                              - type: reasoning_text
                                text: >-
                                  We need answer Chinese describe image. Need be
                                  careful child, identity unknown. Need content:
                                  close-up portrait of young girl, brown wavy
                                  hair bangs, looking camera slight smile, cream
                                  lace dress, warm golden light, neutral blurred
                                  background. We should not infer ethnicity
                                  perhaps. concise. Maybe mention eyes
                                  green/hazel. Need answer in Chinese.
                          - id: 07229fa479c585e3683008175f57bd8f_msg_1
                            type: message
                            status: completed
                            role: assistant
                            content:
                              - type: output_text
                                text: >-
                                  这是一张小女孩的暖色调肖像特写。她留着棕色卷发和齐刘海，穿着带蕾丝边的米白色连衣裙，微微笑着看向镜头。画面采用柔和的侧光与浅景深，背景呈棕灰色虚化，整体温馨自然。
                                annotations: []
                        output_text: >-
                          这是一张小女孩的暖色调肖像特写。她留着棕色卷发和齐刘海，穿着带蕾丝边的米白色连衣裙，微微笑着看向镜头。画面采用柔和的侧光与浅景深，背景呈棕灰色虚化，整体温馨自然。
                        usage:
                          input_tokens: 1407
                          output_tokens: 121
                          total_tokens: 1528
                          input_tokens_details:
                            cached_tokens: 1405
                          output_tokens_details:
                            reasoning_tokens: 70
                        error: null
                        incomplete_details: null
                        instructions: null
                        metadata: {}
                        tools: null
                        tool_choice: auto
                        temperature: 1
                        top_p: 0.95
                        text:
                          format:
                            type: text
                        reasoning:
                          effort: max
                          summary: null
                        max_output_tokens: null
                        parallel_tool_calls: true
                        previous_response_id: null
                        conversation: null
                        store: false
                        service_tier: null
                        safety_identifier: null
                        truncation: disabled
                工具调用:
                  value:
                    id: 07229fa434e87bfb6278664eb2616841
                    object: response
                    created_at: 1792240804
                    model: MiniMax-M3.1-Flash
                    status: completed
                    output:
                      - id: 07229fa434e87bfb6278664eb2616841_rs
                        type: reasoning
                        status: completed
                        summary: []
                        content:
                          - type: reasoning_text
                            text: >-
                              The user asks in Chinese: "What's the current
                              weather in San Francisco?" I should call the
                              weather tool.
                      - id: 07229fa434e87bfb6278664eb2616841_fc_0
                        type: function_call
                        status: completed
                        call_id: call_function_f5xolsmpgj3i_1
                        name: get_weather
                        arguments: '{"location": "San Francisco, US"}'
                    output_text: null
                    usage:
                      input_tokens: 463
                      output_tokens: 54
                      total_tokens: 517
                      input_tokens_details:
                        cached_tokens: 229
                      output_tokens_details:
                        reasoning_tokens: 24
                    error: null
                    incomplete_details: null
                    instructions: null
                    metadata: {}
                    tools:
                      - type: function
                        name: get_weather
                        description: Get the current weather for a given location.
                        parameters:
                          type: object
                          properties:
                            location:
                              type: string
                              description: >-
                                The city and state/country, e.g. San Francisco,
                                US
                          required:
                            - location
                    tool_choice: auto
                    temperature: 1
                    top_p: 0.95
                    text:
                      format:
                        type: text
                    reasoning:
                      effort: max
                      summary: null
                    max_output_tokens: null
                    parallel_tool_calls: true
                    previous_response_id: null
                    conversation: null
                    store: false
                    service_tier: null
                    safety_identifier: null
                    truncation: disabled
            text/event-stream:
              schema:
                type: object
                description: 流式响应（SSE）。每个事件的 `data` 为 JSON，`type` 字段标识事件类型。
              examples:
                流式:
                  value:
                    - type: response.created
                      sequence_number: 0
                      response:
                        id: 07229fa479c585e3683008175f57bd8f
                        object: response
                        created_at: 1792240804
                        model: MiniMax-M3.1-Flash
                        status: in_progress
                        output: []
                        output_text: null
                        usage: null
                        error: null
                        incomplete_details: null
                        instructions: null
                        metadata: {}
                        tools: null
                        tool_choice: auto
                        temperature: 1
                        top_p: 0.95
                        text:
                          format:
                            type: text
                        reasoning:
                          effort: max
                          summary: null
                        max_output_tokens: null
                        parallel_tool_calls: true
                        previous_response_id: null
                        conversation: null
                        store: false
                        service_tier: null
                        safety_identifier: null
                        truncation: disabled
                    - type: response.in_progress
                      sequence_number: 1
                      response:
                        id: 07229fa479c585e3683008175f57bd8f
                        object: response
                        created_at: 1792240804
                        model: MiniMax-M3.1-Flash
                        status: in_progress
                        output: []
                        output_text: null
                        usage: null
                        error: null
                        incomplete_details: null
                        instructions: null
                        metadata: {}
                        tools: null
                        tool_choice: auto
                        temperature: 1
                        top_p: 0.95
                        text:
                          format:
                            type: text
                        reasoning:
                          effort: max
                          summary: null
                        max_output_tokens: null
                        parallel_tool_calls: true
                        previous_response_id: null
                        conversation: null
                        store: false
                        service_tier: null
                        safety_identifier: null
                        truncation: disabled
                    - type: response.output_item.added
                      sequence_number: 2
                      item:
                        id: 07229fa479c585e3683008175f57bd8f_rs
                        type: reasoning
                        status: in_progress
                        summary: []
                        content: []
                      output_index: 0
                    - type: response.content_part.added
                      sequence_number: 3
                      part:
                        type: reasoning_text
                        text: ''
                      output_index: 0
                      content_index: 0
                      item_id: 07229fa479c585e3683008175f57bd8f_rs
                    - type: response.reasoning_text.delta
                      sequence_number: 4
                      output_index: 0
                      content_index: 0
                      item_id: 07229fa479c585e3683008175f57bd8f_rs
                      delta: We need answer
                    - type: response.reasoning_text.delta
                      sequence_number: 5
                      output_index: 0
                      content_index: 0
                      item_id: 07229fa479c585e3683008175f57bd8f_rs
                      delta: ' Chinese describe image. Need be careful child, identity unknown. Need content: close-up portrait of young girl, brown'
                    - type: response.reasoning_text.delta
                      sequence_number: 6
                      output_index: 0
                      content_index: 0
                      item_id: 07229fa479c585e3683008175f57bd8f_rs
                      delta: ' wavy hair bangs, looking camera slight smile, cream lace dress, warm golden light, neutral blurred'
                    - type: response.reasoning_text.delta
                      sequence_number: 7
                      output_index: 0
                      content_index: 0
                      item_id: 07229fa479c585e3683008175f57bd8f_rs
                      delta: ' background. We should not infer ethnicity perhaps. concise. Maybe mention eyes green/hazel. Need answer in'
                    - type: response.reasoning_text.delta
                      sequence_number: 8
                      output_index: 0
                      content_index: 0
                      item_id: 07229fa479c585e3683008175f57bd8f_rs
                      delta: ' Chinese.'
                    - type: response.reasoning_text.done
                      sequence_number: 9
                      output_index: 0
                      content_index: 0
                      item_id: 07229fa479c585e3683008175f57bd8f_rs
                      text: >-
                        We need answer Chinese describe image. Need be careful
                        child, identity unknown. Need content: close-up portrait
                        of young girl, brown wavy hair bangs, looking camera
                        slight smile, cream lace dress, warm golden light,
                        neutral blurred background. We should not infer
                        ethnicity perhaps. concise. Maybe mention eyes
                        green/hazel. Need answer in Chinese.
                    - type: response.content_part.done
                      sequence_number: 10
                      part:
                        type: reasoning_text
                        text: >-
                          We need answer Chinese describe image. Need be careful
                          child, identity unknown. Need content: close-up
                          portrait of young girl, brown wavy hair bangs, looking
                          camera slight smile, cream lace dress, warm golden
                          light, neutral blurred background. We should not infer
                          ethnicity perhaps. concise. Maybe mention eyes
                          green/hazel. Need answer in Chinese.
                      output_index: 0
                      content_index: 0
                      item_id: 07229fa479c585e3683008175f57bd8f_rs
                    - type: response.output_item.done
                      sequence_number: 11
                      item:
                        id: 07229fa479c585e3683008175f57bd8f_rs
                        type: reasoning
                        status: completed
                        summary: []
                        content:
                          - type: reasoning_text
                            text: >-
                              We need answer Chinese describe image. Need be
                              careful child, identity unknown. Need content:
                              close-up portrait of young girl, brown wavy hair
                              bangs, looking camera slight smile, cream lace
                              dress, warm golden light, neutral blurred
                              background. We should not infer ethnicity perhaps.
                              concise. Maybe mention eyes green/hazel. Need
                              answer in Chinese.
                      output_index: 0
                    - type: response.output_item.added
                      sequence_number: 12
                      item:
                        type: message
                        status: in_progress
                        role: assistant
                        content: []
                        id: 07229fa479c585e3683008175f57bd8f_msg_1
                      output_index: 1
                    - type: response.content_part.added
                      sequence_number: 13
                      part:
                        type: output_text
                        text: ''
                        annotations: []
                      output_index: 1
                      content_index: 0
                      item_id: 07229fa479c585e3683008175f57bd8f_msg_1
                    - type: response.output_text.delta
                      sequence_number: 14
                      output_index: 1
                      content_index: 0
                      item_id: 07229fa479c585e3683008175f57bd8f_msg_1
                      delta: 这是一张小女孩的暖色调肖像特写。她留着棕色卷发
                    - type: response.output_text.delta
                      sequence_number: 15
                      output_index: 1
                      content_index: 0
                      item_id: 07229fa479c585e3683008175f57bd8f_msg_1
                      delta: 和齐刘海，穿着带蕾丝边的米白色连衣裙，微微笑着看向镜头。画面
                    - type: response.output_text.delta
                      sequence_number: 16
                      output_index: 1
                      content_index: 0
                      item_id: 07229fa479c585e3683008175f57bd8f_msg_1
                      delta: 采用柔和的侧光与浅景深，背景呈棕灰色虚化，整体温馨
                    - type: response.output_text.delta
                      sequence_number: 17
                      output_index: 1
                      content_index: 0
                      item_id: 07229fa479c585e3683008175f57bd8f_msg_1
                      delta: 自然。
                    - type: response.output_text.done
                      sequence_number: 18
                      output_index: 1
                      content_index: 0
                      item_id: 07229fa479c585e3683008175f57bd8f_msg_1
                      text: >-
                        这是一张小女孩的暖色调肖像特写。她留着棕色卷发和齐刘海，穿着带蕾丝边的米白色连衣裙，微微笑着看向镜头。画面采用柔和的侧光与浅景深，背景呈棕灰色虚化，整体温馨自然。
                    - type: response.content_part.done
                      sequence_number: 19
                      part:
                        type: output_text
                        text: >-
                          这是一张小女孩的暖色调肖像特写。她留着棕色卷发和齐刘海，穿着带蕾丝边的米白色连衣裙，微微笑着看向镜头。画面采用柔和的侧光与浅景深，背景呈棕灰色虚化，整体温馨自然。
                        annotations: []
                      output_index: 1
                      content_index: 0
                      item_id: 07229fa479c585e3683008175f57bd8f_msg_1
                    - type: response.output_item.done
                      sequence_number: 20
                      item:
                        id: 07229fa479c585e3683008175f57bd8f_msg_1
                        type: message
                        status: completed
                        role: assistant
                        content:
                          - type: output_text
                            text: >-
                              这是一张小女孩的暖色调肖像特写。她留着棕色卷发和齐刘海，穿着带蕾丝边的米白色连衣裙，微微笑着看向镜头。画面采用柔和的侧光与浅景深，背景呈棕灰色虚化，整体温馨自然。
                            annotations: []
                      output_index: 1
                    - type: response.completed
                      sequence_number: 21
                      response:
                        id: 07229fa479c585e3683008175f57bd8f
                        object: response
                        created_at: 1792240804
                        model: MiniMax-M3.1-Flash
                        status: completed
                        output:
                          - id: 07229fa479c585e3683008175f57bd8f_rs
                            type: reasoning
                            status: completed
                            summary: []
                            content:
                              - type: reasoning_text
                                text: >-
                                  We need answer Chinese describe image. Need be
                                  careful child, identity unknown. Need content:
                                  close-up portrait of young girl, brown wavy
                                  hair bangs, looking camera slight smile, cream
                                  lace dress, warm golden light, neutral blurred
                                  background. We should not infer ethnicity
                                  perhaps. concise. Maybe mention eyes
                                  green/hazel. Need answer in Chinese.
                          - id: 07229fa479c585e3683008175f57bd8f_msg_1
                            type: message
                            status: completed
                            role: assistant
                            content:
                              - type: output_text
                                text: >-
                                  这是一张小女孩的暖色调肖像特写。她留着棕色卷发和齐刘海，穿着带蕾丝边的米白色连衣裙，微微笑着看向镜头。画面采用柔和的侧光与浅景深，背景呈棕灰色虚化，整体温馨自然。
                                annotations: []
                        output_text: >-
                          这是一张小女孩的暖色调肖像特写。她留着棕色卷发和齐刘海，穿着带蕾丝边的米白色连衣裙，微微笑着看向镜头。画面采用柔和的侧光与浅景深，背景呈棕灰色虚化，整体温馨自然。
                        usage:
                          input_tokens: 1407
                          output_tokens: 121
                          total_tokens: 1528
                          input_tokens_details:
                            cached_tokens: 1405
                          output_tokens_details:
                            reasoning_tokens: 70
                        error: null
                        incomplete_details: null
                        instructions: null
                        metadata: {}
                        tools: null
                        tool_choice: auto
                        temperature: 1
                        top_p: 0.95
                        text:
                          format:
                            type: text
                        reasoning:
                          effort: max
                          summary: null
                        max_output_tokens: null
                        parallel_tool_calls: true
                        previous_response_id: null
                        conversation: null
                        store: false
                        service_tier: null
                        safety_identifier: null
                        truncation: disabled
components:
  schemas:
    CreateResponseReq:
      type: object
      required:
        - model
        - input
      properties:
        model:
          type: string
          description: 调用的模型名称，如 `MiniMax-M3.1-Flash`
          example: MiniMax-M3.1-Flash
        service_tier:
          type: string
          description: >-
            请求准入服务层级。支持的取值为 `standard` 和 `priority`。省略时默认使用
            `standard`。`priority`
            的[价格](https://platform.minimax.cn/docs/pricing/overview#models/text)为
            `standard` 的 1.5
            倍，并会确保请求获得优先准入，使其排在其他请求之前处理，从而带来更快响应并减少失败。`MiniMax-M3.1-Flash`
            不支持该字段。
          enum:
            - standard
            - priority
          default: standard
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
        max_output_tokens:
          type: integer
          description: >-
            最大输出 token 数。推理 token 也计入此上限，设置过小会导致 `status` 为 `incomplete` 且
            `output` 中没有 `message` 项。
        temperature:
          type: number
          format: float
          description: 采样温度，取值范围 (0, 1]
          default: 1
          minimum: 0
          maximum: 1
        top_p:
          type: number
          format: float
          description: 核采样，取值范围 (0, 1]
          default: 0.95
          minimum: 0
          maximum: 1
        stream:
          type: boolean
          description: 设置为 `true` 启用 SSE 流式响应
          default: false
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
        metadata:
          type: object
          description: 请求元数据，key-value 均为字符串
          additionalProperties:
            type: string
        prompt_cache_key:
          type: string
          description: Prompt 缓存路由标识
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

            - M2.x 模型：推理无法关闭，传入 `effort: "none"` 会被接收但不生效。
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
    CreateResponseResp:
      type: object
      properties:
        id:
          type: string
          description: 响应 ID
          example: abc123
        object:
          type: string
          enum:
            - response
          description: 对象类型，固定为 `response`
        created_at:
          type: integer
          description: 响应创建时间（Unix 秒）
        model:
          type: string
          description: 实际处理请求的模型名称
          example: MiniMax-M3.1-Flash
        status:
          type: string
          enum:
            - completed
            - incomplete
            - failed
          description: 响应状态
        output:
          type: array
          description: 模型输出列表
          items:
            $ref: '#/components/schemas/OutputItem'
        output_text:
          type: string
          nullable: true
          description: 便捷字段：所有文本输出拼接后的结果
        usage:
          $ref: '#/components/schemas/Usage'
        error:
          type: object
          nullable: true
          description: 错误信息，仅在 `status=failed` 时返回
          properties:
            code:
              type: string
              description: 错误码
            message:
              type: string
              description: 人类可读的错误描述
        incomplete_details:
          type: object
          nullable: true
          description: 未完成原因，仅在 `status=incomplete` 时返回
          properties:
            reason:
              type: string
              enum:
                - max_output_tokens
                - content_filter
        parallel_tool_calls:
          type: boolean
          description: 请求中暂不支持该参数，传入后将被忽略，响应中固定返回 **`true`**。
        store:
          type: boolean
          description: 请求中暂不支持该参数，传入后将被忽略，响应中固定返回 **`false`**。
        truncation:
          type: string
          enum:
            - disabled
          description: 请求中暂不支持该参数，传入后将被忽略，响应中固定返回 **`disabled`**。
        previous_response_id:
          type: string
          nullable: true
          description: 请求中暂不支持该参数，传入后将被忽略，响应中固定返回 **`null`**。
        conversation:
          type: object
          nullable: true
          description: 请求中暂不支持该参数，传入后将被忽略，响应中固定返回 **`null`**。
        service_tier:
          type: string
          nullable: true
          description: >-
            本次请求实际生效的服务层级，取值为 `standard` 或 `priority`。`MiniMax-M3.1-Flash`
            不支持该字段，响应中返回 **`null`**。
        safety_identifier:
          type: string
          nullable: true
          description: 请求中暂不支持该参数，传入后将被忽略，响应中固定返回 **`null`**。
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
          description: 消息内容，可以是字符串或多模态片段数组（仅当 `type` 为 `message` 时使用）
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
    OutputItem:
      oneOf:
        - title: Message
          type: object
          properties:
            id:
              type: string
              description: '`<id>_msg` 格式'
            type:
              type: string
              enum:
                - message
            status:
              type: string
              enum:
                - completed
            role:
              type: string
              enum:
                - assistant
            content:
              type: array
              items:
                type: object
                properties:
                  type:
                    type: string
                    enum:
                      - output_text
                  text:
                    type: string
                    description: 模型生成的文本
                  annotations:
                    type: array
                    description: 引用标注
        - title: Reasoning
          type: object
          description: 思维链输出（仅开启推理时返回）
          properties:
            id:
              type: string
              description: '`<id>_rs` 格式'
            type:
              type: string
              enum:
                - reasoning
            status:
              type: string
              enum:
                - completed
            summary:
              type: array
              description: 思维链摘要
            content:
              type: array
              items:
                type: object
                properties:
                  type:
                    type: string
                    enum:
                      - reasoning_text
                  text:
                    type: string
                    description: 思维链文本
        - title: Function Call
          type: object
          description: 工具调用
          properties:
            id:
              type: string
              description: '`<id>_fc_<index>` 格式'
            type:
              type: string
              enum:
                - function_call
            status:
              type: string
              enum:
                - completed
            call_id:
              type: string
              description: 工具调用 ID，用于关联 `function_call_output`
            name:
              type: string
              description: 函数名称
            arguments:
              type: string
              description: 函数参数的 JSON 字符串
    Usage:
      type: object
      properties:
        input_tokens:
          type: integer
          description: 输入 token 数
        input_tokens_details:
          type: object
          properties:
            cached_tokens:
              type: integer
              description: Prompt 缓存命中的 token 数
        output_tokens:
          type: integer
          description: 输出 token 数
        output_tokens_details:
          type: object
          properties:
            reasoning_tokens:
              type: integer
              description: 思维链消耗的 token 数（仅开启推理时计入）
        total_tokens:
          type: integer
          description: 总 token 数
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
                  description: 视频链接或 Base64 编码，大文件建议使用 File API 上传
                fps:
                  type: number
                  format: float
                  default: 1
                  minimum: 0.2
                  maximum: 5
                  description: 抽帧频率
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