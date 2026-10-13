<!-- Official source: https://cloud.tencent.com/document/product/1823/130660 -->
<!-- Source SHA-256: 04f1df93d0be3f8c23dbd8be32bf04ca6facad21b889efce1e749816236607ae -->

# Token Plan 企业版快速入门

官方来源：https://cloud.tencent.com/document/product/1823/130660
最近更新时间：2026-09-03 15:45:00

本文介绍如何购买 Token Plan 企业版套餐，创建 API Key 并且快速验证模型调用，以及在龙虾或者编程工具中使用。

## 步骤一：购买 Token Plan 企业版套餐

1. 登录大模型服务平台 TokenHub 控制台，前往 [Token Plan 企业版购买页](https://console.cloud.tencent.com/tokenhub/tokenplan-e/buy)，选择适合您的订阅套餐。

2. 根据您选购的套餐类型，配置如下套餐参数：

2.1 如果您要购买专业套餐：

| **配置项** | **是否必填** | **说明** | **举例** |
| --- | --- | --- | --- |
| 月额度 | 是 | 支持自定义积分规格，最终价格及规则请以 [控制台](https://console.cloud.tencent.com/tokenhub/tokenplan-e/buy?type=pro) 为准。 | 100,000 积分 |
| 套餐名称 | 是 | 自定义套餐名称，便于区分管理（如“研发团队套餐”、“产品线 A 套餐”等）。 | 研发团队套餐 |
| 购买时长 | 是 | 可选择 1 至 12 个月。 | 1 个月 |
| 自动续费 | 否 | 按需开启。开启后，套餐到期会自动扣除下一个月的套餐费用。 | 否 |

2.2 如果您要购买轻享套餐：

| **配置项** | **是否必填** | **说明** | **举例** |
| --- | --- | --- | --- |
| 月 Token 数 | 是 | 支持自定义规格，最终价格及规则请以 [控制台](https://console.cloud.tencent.com/tokenhub/tokenplan-e/buy?type=lite) 为准。 | 50,000,000 tokens |
| 套餐名称 | 是 | 自定义套餐名称，便于区分管理（如“研发团队套餐”、“产品线 A 套餐”等）。 | 研发团队套餐 |
| 购买时长 | 是 | 选择 1 至 12 个月。 | 1 个月 |
| 自动续费 | 否 | 按需开启。开启后，套餐到期会自动扣除下一个月的套餐费用。 | 否 |

3. 确认配置信息与费用总计，勾选服务条款，单击**立即购买**完成支付。

## 步骤二：获取 API Key

购买套餐后，需要创建并复制 API Key，来获取模型调用凭证。

1. 在 [我的套餐](https://console.cloud.tencent.com/tokenhub/tokenplan-e) 列表中，选择套餐 > **管理 API Key**，进入 API Key 管理页面。

![](https://qcloudimg.tencent-cloud.cn/image/document/e83cf11055e5c722a432e2bb501dee57.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/e83cf11055e5c722a432e2bb501dee57.png)

2. 单击**创建 API Key**。

![](https://qcloudimg.tencent-cloud.cn/image/document/6395037ddba3ce5ad0182a63691a9a4e.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/6395037ddba3ce5ad0182a63691a9a4e.png)

3. 填写 API Key 配置，并单击**确定**生成 API Key：

| **字段** | **是否必填** | **说明** | **举例** |
| --- | --- | --- | --- |
| 复用已有 Key | 否 | 下拉选择当前套餐下已创建的 Key，选中后自动回填该 Key 的配置（模型选择、独占额度、总额度上限、TPM 限制）到下方表单，便于快速创建同配置的新 Key。Key 名称不回填，需重新输入。  选择“不复用”则从空白开始配置。 | 不复用 |
| Key 名称 | 是 | 为 Key 自定义命名，便于识别用途和归属（如“员工001”、“客服 Bot”）。  命名规则：**只能包含中文、字母、数字、下划线、连字符，以中文或字母开头，以中文或字母或数字结尾，长度 2~50 个字符**。 | 员工001 |
| 创建数量 | 是 | 本次创建的 Key 数量，范围 1~10。系统会自动在 Key 名称后追加序号（如“员工001-1”、“员工001-2”）。批量创建时，所有 Key 共享相同的配置参数。 | 1 |
| 模型选择 | 是 | 选择该 Key 可以调用的模型，支持多选。可选模型包括 Auto 智能路由、GLM-5、Kimi-K2.5、MiniMax-M2.5。  未勾选的模型，该 Key 调用时将返回无权限错误。 | Auto 智能路由 |
| 独占额度 | 是 | 为该 Key 预留的专属额度（单位：积分/tokens），仅该 Key 可使用，其他 Key 无法占用。设为 0 表示不预留专属额度，该 Key 仅使用共享池。输入值不得超过当前可分配的独占额度（页面会提示“当前最大可配置 X 额度”）。 | 0 |
| 总额度上限 | 是 | 该 Key 在本计费周期内最多可使用的额度总量（独占 + 共享部分之和）。提供两种模式：  同套餐包上限（默认）：上限等于套餐包的总额度，即该 Key 理论上可使用整个额度池（实际受共享池竞争限制）。  自定义上限：手动输入一个具体数值，限制该 Key 的最大可用额度，适合需要严格控制单 Key 成本的场景。 | 同套餐包上限 |
| TPM 限制 | 是 | 该 Key 每分钟可处理的最大 Token 数（Tokens Per Minute），用于控制调用速率，防止单个 Key 过度占用带宽。提供两种模式：  同套餐包上限（默认）：TPM 上限与套餐包级别一致。  自定义上限：手动输入值，不可超过套餐包级 TPM 上限。 | 同套餐包上限 |

4. 对已创建好的 API Key 单击**复制**，即可获得 API Key。

![](https://qcloudimg.tencent-cloud.cn/image/document/285e4f2cafa134a3d5aaac01bbae70df.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/285e4f2cafa134a3d5aaac01bbae70df.png)

## 步骤三：快速验证模型调用

获取 API Key 后您可在命令行终端通过 cURL 简单验证连通性：

`$your_api_key` 替换为您在上一步中创建并复制的 API Key。

`$model_id` 替换为您想测试的模型 ID，不同套餐可用模型列表不一样，详见：[专业套餐可用模型](https://cloud.tencent.com/document/product/1823/130659#cde5404a-a7bb-4d53-acba-6e3b1b6b8264)、[轻享套餐可用模型](https://cloud.tencent.com/document/product/1823/131173#b18f9f4d-fad3-49a9-a38e-2ef38854fa19)。例如 `auto`。

验证示例如下：

广州

新加坡

```bash
curl --location 'https://tokenhub.tencentmaas.com/plan/v3/chat/completions' \\
--header 'Authorization: Bearer $your_api_key' \\
--header 'Content-Type: application/json' \\
--data '{
  "model": "$model_id",
  "messages": [
    {
      "role": "user",
      "content": "写一首关于春天的诗"
    }
  ],
  "stream": false
}'
```

**返回结果示例**

```json
{
    "id": "********-****-****-****-************",
    "object": "chat.completion",
    "model": "auto",
    "created": *******,
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "**春日漫步**\\n\\n春风拂面柳絮轻，  \\n桃红李白映湖光。  \\n碧草如烟铺小径，  \\n燕舞蜂歌映日晴。  \\n翠鸟鸣枝声细细，  \\n清泉石上映星光。  \\n万物苏醒歌盛世，  \\n人间四月尽芳菲。",
                "reasoning_content": "The user is speaking Chinese: \\"写一首关于春天的诗\\" which translates to \\"Write a poem about spring\\". So we need to comply, providing a poem about spring in Chinese.\\n\\nWe should generate a Chinese poem. There's no policy conflict. The user wants a poem about spring. That is fine.\\n\\nWe should produce a poem in Chinese, maybe a classical style or free verse. The user is Chinese, likely wants a Chinese poem.\\n\\nThe policy: There's no disallowed content. So just comply.\\n\\nWe could produce a 5- or 7-character per line poem, e.g., a \\"七绝\\" or a \\"五律\\". Or a free verse. Let's produce a short Chinese poem with vivid imagery. The poem might be 4-8 lines. Should be about spring. Use imagery of blossoming, birds, gentle breezes, green grass, etc.\\n\\nThus we can output something like:\\n\\n春风拂面柳絮轻，  \\n桃红李白映湖光。  \\n碧草如烟铺小径，  \\n燕舞蜂歌映日晴。  \\n\\nThat's a four-line poem with 7 characters each maybe? Let's count: \\"春风拂面柳絮轻\\" has 7 characters: 春风 (2) 拂 (1) 面 (1) 柳 (1) 絮 (1) 轻 (1) - it's 7? Actually Chinese characters: 春(1) 风2 拂3 面4 柳5 絮6 轻7. Yes 7. Then second line \\"桃红李白映湖光\\" also 7. Third line \\"碧草如烟铺小径\\" also 7. Fourth line \\"燕舞蜂歌映日晴\\" also 7. Good.\\n\\nAlternatively, maybe do a 5- or 7-line poem in a more modern style. But the user just said \\"写一首关于春天的诗\\", so either is fine.\\n\\nWe can also add a title: \\"春之韵\\".\\n\\nLet's provide a short poem: \\"春风拂面柳絮轻，桃红李白映湖光，碧草如烟铺小径，燕舞蜂歌映日晴\\". Possibly add more lines to fill up to 8 lines: \\"翠鸟鸣枝声细细，清泉石上映星光，万物苏醒歌盛世，人间四月尽芳菲\\". That would be 8 lines of 7 characters each (if we maintain 7 characters each). Let's see: \\"翠鸟鸣枝声细细\\" - characters: 翠1 鸟2 鸣3 枝4 声5 细6 细7: yes 7. \\"清泉石上映星光\\" - 清1 泉2 石3 上4 映5 星6 光7. \\"万物苏醒歌盛世\\" - 万1 物2 苏3 醒4 歌5 盛6 世7. \\"人间四月尽芳菲\\" - 人1 间2 三3 月4 尽5 芳6 菲7. Good. Then that is 8 lines of 7 characters each, forming a \\"七绝\\" variant. Actually it's 8 lines, maybe a \\"七律\\" (seven-character regulated verse) but 8 lines is okay.\\n\\nWe can present the poem with a title \\"春日漫步\\". Then provide the poem.\\n\\nWe should be mindful of possible Chinese punctuation. Use Chinese punctuation: \\"，\\" and \\"。\\" or just line breaks.\\n\\nWe can give a note: It's a classical style poem, describing spring scenery.\\n\\nTherefore answer: a poem.\\n\\nWill respond in Chinese, as the user wrote in Chinese. Provide the poem. That's it.\\n\\nNow output."
            },
            "finish_reason": "stop"
        }
    ],
    "usage": {
        "prompt_tokens": 46,
        "completion_tokens": 813,
        "total_tokens": 859,
        "prompt_tokens_details": {
            "cached_tokens": 0
        },
        "completion_tokens_details": {
            "reasoning_tokens": 748
        }
    }
}
```

```bash
curl --location 'https://tokenhub-intl.tencentmaas.com/plan/v3/chat/completions' \\
--header 'Authorization: Bearer $your_api_key' \\
--header 'Content-Type: application/json' \\
--data '{
  "model": "$model_id",
  "messages": [
    {
      "role": "user",
      "content": "写一首关于春天的诗"
    }
  ],
  "stream": false
}'
```

**返回结果示例**

```json
{
    "id": "********-****-****-****-************",
    "object": "chat.completion",
    "model": "auto",
    "created": *******,
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "**春日漫步**\\n\\n春风拂面柳絮轻，  \\n桃红李白映湖光。  \\n碧草如烟铺小径，  \\n燕舞蜂歌映日晴。  \\n翠鸟鸣枝声细细，  \\n清泉石上映星光。  \\n万物苏醒歌盛世，  \\n人间四月尽芳菲。",
                "reasoning_content": "The user is speaking Chinese: \\"写一首关于春天的诗\\" which translates to \\"Write a poem about spring\\". So we need to comply, providing a poem about spring in Chinese.\\n\\nWe should generate a Chinese poem. There's no policy conflict. The user wants a poem about spring. That is fine.\\n\\nWe should produce a poem in Chinese, maybe a classical style or free verse. The user is Chinese, likely wants a Chinese poem.\\n\\nThe policy: There's no disallowed content. So just comply.\\n\\nWe could produce a 5- or 7-character per line poem, e.g., a \\"七绝\\" or a \\"五律\\". Or a free verse. Let's produce a short Chinese poem with vivid imagery. The poem might be 4-8 lines. Should be about spring. Use imagery of blossoming, birds, gentle breezes, green grass, etc.\\n\\nThus we can output something like:\\n\\n春风拂面柳絮轻，  \\n桃红李白映湖光。  \\n碧草如烟铺小径，  \\n燕舞蜂歌映日晴。  \\n\\nThat's a four-line poem with 7 characters each maybe? Let's count: \\"春风拂面柳絮轻\\" has 7 characters: 春风 (2) 拂 (1) 面 (1) 柳 (1) 絮 (1) 轻 (1) - it's 7? Actually Chinese characters: 春(1) 风2 拂3 面4 柳5 絮6 轻7. Yes 7. Then second line \\"桃红李白映湖光\\" also 7. Third line \\"碧草如烟铺小径\\" also 7. Fourth line \\"燕舞蜂歌映日晴\\" also 7. Good.\\n\\nAlternatively, maybe do a 5- or 7-line poem in a more modern style. But the user just said \\"写一首关于春天的诗\\", so either is fine.\\n\\nWe can also add a title: \\"春之韵\\".\\n\\nLet's provide a short poem: \\"春风拂面柳絮轻，桃红李白映湖光，碧草如烟铺小径，燕舞蜂歌映日晴\\". Possibly add more lines to fill up to 8 lines: \\"翠鸟鸣枝声细细，清泉石上映星光，万物苏醒歌盛世，人间四月尽芳菲\\". That would be 8 lines of 7 characters each (if we maintain 7 characters each). Let's see: \\"翠鸟鸣枝声细细\\" - characters: 翠1 鸟2 鸣3 枝4 声5 细6 细7: yes 7. \\"清泉石上映星光\\" - 清1 泉2 石3 上4 映5 星6 光7. \\"万物苏醒歌盛世\\" - 万1 物2 苏3 醒4 歌5 盛6 世7. \\"人间四月尽芳菲\\" - 人1 间2 三3 月4 尽5 芳6 菲7. Good. Then that is 8 lines of 7 characters each, forming a \\"七绝\\" variant. Actually it's 8 lines, maybe a \\"七律\\" (seven-character regulated verse) but 8 lines is okay.\\n\\nWe can present the poem with a title \\"春日漫步\\". Then provide the poem.\\n\\nWe should be mindful of possible Chinese punctuation. Use Chinese punctuation: \\"，\\" and \\"。\\" or just line breaks.\\n\\nWe can give a note: It's a classical style poem, describing spring scenery.\\n\\nTherefore answer: a poem.\\n\\nWill respond in Chinese, as the user wrote in Chinese. Provide the poem. That's it.\\n\\nNow output."
            },
            "finish_reason": "stop"
        }
    ],
    "usage": {
        "prompt_tokens": 46,
        "completion_tokens": 813,
        "total_tokens": 859,
        "prompt_tokens_details": {
            "cached_tokens": 0
        },
        "completion_tokens_details": {
            "reasoning_tokens": 748
        }
    }
}
```

## 步骤四：配置 AI 工具

Token Plan 企业版兼容热门的龙虾工具和 AI 编码工具，您可以根据自己的偏好选择，将 URL、API Key 和具体的模型配置到工具中，就能使用大模型服务。

<table><colgroup><col/><col/><col/></colgroup><tbody><tr><td colspan="3" rowspan="1"><div><b>龙虾工具</b></div></td><td colspan="0" rowspan="0"><div></div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div><b></b><a href="https://cloud.tencent.com/document/product/1823/130671"><b>OpenClaw</b></a></div><div>开源、自托管个人 AI 助手</div></td><td><div><b></b><a href="https://cloud.tencent.com/document/product/1823/130673"><b>WorkBuddy</b></a></div><div>腾讯云全场景 AI 桌面智能体</div></td><td colspan="1" rowspan="1"><div><b></b><a href="https://cloud.tencent.com/document/product/1823/130674"><b>CoPaw</b></a></div><div>开源 AI 智能体</div></td></tr><tr><td><div><b></b><a href="https://cloud.tencent.com/document/product/1823/130672"><b>AutoClaw</b></a></div><div>本地 AI 智能体</div></td><td><div><b></b><a href="https://cloud.tencent.com/document/product/1823/131062"><b>QClaw</b></a></div><div>腾讯电脑管家本地化 AI 助手</div></td><td colspan="1" rowspan="1"><div><b></b><a href="https://cloud.tencent.com/document/product/1823/136045"><b>DeepSeek Harness</b></a></div><div>开源、本地运行的 AI Agent 框架</div></td></tr></tbody></table>

<table><colgroup><col/><col/><col/></colgroup><tbody><tr><td colspan="3" rowspan="1"><div><b>编程工具</b></div></td><td colspan="0" rowspan="0"><div></div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td colspan="1" rowspan="1"><div><b></b><a href="https://cloud.tencent.com/document/product/1823/130663"><b>CodeBuddy</b></a></div><div>基于腾讯云 AI 技术的智能编程工具</div></td><td colspan="1" rowspan="1"><div><b></b><a href="https://cloud.tencent.com/document/product/1823/130664"><b>OpenCode</b></a></div><div>开源 AI 编程代理工具</div></td><td colspan="1" rowspan="1"><div><b></b><a href="https://cloud.tencent.com/document/product/1823/130670"><b>Kilo Code</b></a></div><div>轻量高性能编程工具</div></td></tr><tr><td colspan="1" rowspan="1"><div><b></b><a href="https://cloud.tencent.com/document/product/1823/130667"><b>Cline</b></a></div><div>VSCode 扩展，代码补全和调试</div></td><td colspan="1" rowspan="1"><div><b></b><a href="https://cloud.tencent.com/document/product/1823/130668"><b>Cursor</b></a></div><div>AI 原生代码编辑器</div></td><td colspan="1" rowspan="1"><div><b></b><a href="https://cloud.tencent.com/document/product/1823/130669"><b>Kilo CLI</b></a></div><div>轻量高性能编程工具命令行</div></td></tr><tr><td colspan="1" rowspan="1"><div><b></b><a href="https://cloud.tencent.com/document/product/1823/130665"><b>Claude Code</b></a></div><div>AI 终端编程助手，支持自然语言编程</div></td><td colspan="1" rowspan="1"><div><b></b><a href="https://cloud.tencent.com/document/product/1823/130666"><b>Codex</b></a></div><div>OpenAI 推出的智能编程代理</div></td><td colspan="1" rowspan="1"><div><b></b><a href="https://cloud.tencent.com/document/product/1823/135395"><b>TRAE</b></a></div><div>深度融合 AI 能力的开发工具</div></td></tr><tr><td><div><b></b><a href="https://cloud.tencent.com/document/product/1823/136605"><b>CC Switch</b></a></div><div>统一管理多个 AI 编程工具</div></td><td><div>-</div></td><td><div>-</div></td></tr></tbody></table>
