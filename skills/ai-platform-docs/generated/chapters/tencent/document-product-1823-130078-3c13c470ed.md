<!-- Official source: https://cloud.tencent.com/document/product/1823/130078 -->
<!-- Source SHA-256: 2184cbec40a65061e529c5755a28a8536700e7a52785bc96dd9918e726a71b2c -->

# API 使用说明

官方来源：https://cloud.tencent.com/document/product/1823/130078
最近更新时间：2026-10-26 11:28:30

## 概述

大模型服务平台 TokenHub 兼容 **OpenAI API、Anthropic API 协议**，可直接使用 OpenAI SDK 快速接入。

## 接口域名

针对不同的地域，平台提供了不同的接入地址，以便于为您提供最稳定的接入。默认接入地址如下：

**注意：**

请根据服务开通的地域选择对应的接口地址，不支持跨地域、跨站点调用服务。

| 地域 | 接口地址 | 资源调度范围 |
| --- | --- | --- |
| 广州 | `https://tokenhub.tencentmaas.com` | 中国大陆 |
| 新加坡 | `https://tokenhub-intl.tencentmaas.com` | 全球 |

同时平台提供了备用接入地址以确保异常情况下用户能顺利接入，当默认地址不可用时，您可以尝试切换为以下接入地址：

| 地域 | 接口地址 | 资源调度范围 |
| --- | --- | --- |
| 广州 | `https://tokenhub.tencentmaas.cn` | 中国大陆 |
| 新加坡 | `https://tokenhub-intl.tencentmaas.cn` | 全球 |

## 鉴权方式

使用 [API KEY](https://console.cloud.tencent.com/tokenhub/apikey) 通过 `Authorization: Bearer` Header 鉴权。

## 查询模型列表

您可以通过 `GET /v1/models` 接口查询当前平台支持的模型范围。该接口兼容 OpenAI API 协议，返回平台当前可调用的全部模型列表及其状态，模型 ID 即为调用推理接口时 `model` 参数需传入的值。

**注意：**

调用 `/v1/models` 需在请求头中传入 API KEY 进行鉴权（`Authorization: Bearer <API KEY>`）；未携带认证信息或 API KEY 无效时，接口将返回 HTTP 401 错误。

### 请求示例

```bash
curl https://tokenhub.tencentmaas.com/v1/models \\
  -H "Authorization: Bearer $TOKENHUB_API_KEY"
```

### 响应示例

```json
{
    "object": "list",
    "data": [
        {
            "id": "hy3",
            "object": "model",
            "name": "Hy3",
            "created": 1783267200,
            "status": "online"
        },
        {
            "id": "deepseek-v4-pro",
            "object": "model",
            "name": "DeepSeek-V4-Pro",
            "created": 1776960000,
            "status": "online"
        }
    ]
}
```

### 响应参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| object | String | 固定为 `list`，表示返回的是模型列表。 |
| data | Array | 模型对象数组，每个元素代表一个可用模型。 |
| data[].id | String | 模型 ID，调用推理接口时 `model` 参数需传入该值。 |
| data[].object | String | 对象类型，固定为 `model`。 |
| data[].name | String | 模型展示名称。 |
| data[].created | Integer | 模型创建时间（Unix 时间戳，单位：秒）。 |
| data[].status | String | 模型状态，如 `online`（在线）、`pre-offline`（即将下线）。 |

## 模型调用方式

<table><colgroup><col/><col/><col/></colgroup><tbody><tr><td><div>模型名称</div></td><td><div>model 参数值</div></td><td><div>API 调用指引</div></td></tr><tr><td><div>Hy4 preview</div></td><td><div>hy4-preview</div></td><td rowspan="35"><div>详细调用参数可参见 <a href="https://cloud.tencent.com/document/product/1823/130079">语言模型调用概览</a>。</div></td></tr><tr><td><div>Hy3</div></td><td><div>hy3</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>Hy-MT2-Pro</div></td><td><div>hy-mt2-pro</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>Hy-MT2-Plus</div></td><td><div>hy-mt2-plus</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>Hy-MT2-Lite</div></td><td><div>hy-mt2-lite</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>Hy-Role-Latest</div></td><td><div>hunyuan-role-latest</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>Hy-Role</div></td><td><div>hy-role</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>DeepSeek-V4.1-Flash-1017 原厂直供</div></td><td><div>deepseek/deepseek-flash</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>DeepSeek-V4-Flash 0731 正式版 原厂直供</div></td><td><div>deepseek-v4-flash-202605</div><div>deepseek/deepseek-v4-flash-0731</div><div>deepseek/deepseek-v4-flash</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>DeepSeek-V4-Pro 0813 正式版 原厂直供</div></td><td><div>deepseek-v4-pro-202606</div><div>deepseek/deepseek-v4-pro-0813</div><div>deepseek/deepseek-v4-pro</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>DeepSeek-V4-Flash-Vision-Exp 原厂直供</div></td><td><div>deepseek/deepseek-v4-flash-vision-exp</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>DeepSeek-V4-Flash 0731 正式版</div></td><td><div>deepseek-v4-flash-0731</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>DeepSeek-V4-Pro 0813 正式版</div></td><td><div>deepseek-v4-pro-0813</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>DeepSeek-V4-Flash</div></td><td><div>deepseek-v4-flash</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>DeepSeek-V4-Pro</div></td><td><div>deepseek-v4-pro</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>GLM-5.3</div></td><td><div>glm-5.3</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>GLM-5.3-Flash</div></td><td><div>glm-5.3-flash</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>GLM-5.3-FlashX</div></td><td><div>glm-5.3-flashx</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>GLM-5.2</div></td><td><div>glm-5.2</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>GLM-5V-Turbo</div></td><td><div>glm-5v-turbo</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td colspan="1" rowspan="1"><div>Kimi K3.1 Pro HighSpeed</div></td><td colspan="1" rowspan="1"><div>kimi-k3.1-pro-highspeed</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td colspan="1" rowspan="1"><div>Kimi K3.1 Pro</div></td><td colspan="1" rowspan="1"><div>kimi-k3.1-pro</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>Kimi K3</div></td><td><div>kimi-k3</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>Kimi K2.8 Preview</div></td><td><div>kimi-k2.8-preview</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>Kimi K2.7 Code HighSpeed</div></td><td><div>kimi-k2.7-code-highspeed</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>Kimi K2.7 Code</div></td><td><div>kimi-k2.7-code</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>Kimi-K2.6</div></td><td><div>kimi-k2.6</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td colspan="1" rowspan="1"><div>MiniMax-M3.1-Flash</div></td><td colspan="1" rowspan="1"><div>minimax-m3.1-flash</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>MiniMax-M3</div></td><td><div>minimax-m3</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>MiniMax-M2.7</div></td><td><div>minimax-m2.7</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>Qwen3.5 Flash</div></td><td><div>qwen3.5-flash</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>Qwen3.5 Plus</div></td><td><div>qwen3.5-plus</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>MiMo-V2.6-Pro</div></td><td><div>mimo-v2.6-pro</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>MiMo-V2.6-Flash</div></td><td><div>mimo-v2.6-flash</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>MiMo-V2.5-Pro</div></td><td><div>mimo-v2.5-pro</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>Hy-Image-3.0</div></td><td><div>hy-image-v3</div></td><td rowspan="2"><div>详细调用参数可参见 <a href="https://cloud.tencent.com/document/product/1823/135744">图像生成模型调用概览</a>。</div></td></tr><tr><td><div>Vidu-Image-q2</div></td><td><div>vidu-image-q2</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>Hy-Video-v1.5</div></td><td><div>hy-video-v1.5</div></td><td rowspan="4"><div>详细调用参数可参见 <a href="https://cloud.tencent.com/document/product/1823/135738">视频生成模型调用概览</a>。</div></td></tr><tr><td><div>PixVerse-Video-v6</div></td><td><div>pixverse-video-v6.0</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>Kling-Video-V3</div></td><td><div>kling-video-v3</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>MiniMax-Video-H3</div></td><td><div>minimax-video-h3</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>HY-3D-3.0</div></td><td><div>hy-3d-3.0</div></td><td rowspan="3"><div>详细调用参数可参见 <a href="https://cloud.tencent.com/document/product/1823/130082">3D 生成</a>。</div></td></tr><tr><td><div>HY-3D-3.1</div></td><td><div>hy-3d-3.1</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>HY-3D-Express</div></td><td><div>hy-3d-express</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>YT-VITA</div></td><td><div>youtu-vita</div></td><td rowspan="4"><div>详细调用参数可参见 <a href="https://cloud.tencent.com/document/product/1823/130988">多模态理解</a>。</div></td></tr><tr><td><div>HY-Vision-2.0-Instruct</div></td><td><div>hy-vision-2.0-instruct</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>HY-Vision-1.5-Thinking</div></td><td><div>hunyuan-t1-vision-20250916</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>HY-Vision-Video</div></td><td><div>hunyuan-turbos-vision-video-20250728</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>Kinfra-Text-Embedding-0.6b</div></td><td><div>kinfra-text-embedding-0.6b</div></td><td rowspan="4"><div>详细调用参数可参见 <a href="https://cloud.tencent.com/document/product/1823/133515">向量模型</a>。</div></td></tr><tr><td><div>Kinfra-Text-Embedding-4b</div></td><td><div>kinfra-text-embedding-4b</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>Kinfra-VL-Embedding-2b</div></td><td><div>kinfra-vl-embedding-2b</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>Kinfra-VL-Embedding-8b</div></td><td><div>kinfra-vl-embedding-8b</div></td><td colspan="0" rowspan="0"><div></div></td></tr></tbody></table>

## 异常处理

API 报错请参见 [API 错误码说明](https://cloud.tencent.com/document/product/1823/131595)。
