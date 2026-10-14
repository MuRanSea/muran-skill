<!-- Official source: https://cloud.tencent.com/document/product/1823/135744 -->
<!-- Source SHA-256: a707936e02ea7d96fd0f37b21aaf1b388f1a644753cc11121b06a55a77f9ad41 -->

# 图像生成模型调用概览

官方来源：https://cloud.tencent.com/document/product/1823/135744
最近更新时间：2026-10-13 15:50:31

## 概述

大模型服务平台 TokenHub 图片生成模型提供**文生图、参考生图、图片编辑**等能力，覆盖混元、Vidu 等系列模型。本文为各模型的快速导航与选型指引。

**说明：**

各接口的详细参数、请求示例与返回字段请跳转对应调用指南查阅。计费说明请参见 [TokenHub 模型价格说明](https://cloud.tencent.com/document/product/1823/130055)。

## 模型列表

### 混元系列

详情请参见 [Hy 生图调用指南](https://cloud.tencent.com/document/product/1823/135745)。

<table><colgroup><col/><col/><col/><col/><col/></colgroup><tbody><tr><td><div>模型名称</div></td><td><div>model 参数值</div></td><td><div>支持能力</div></td><td><div>接口类型</div></td><td><div>简要说明</div></td></tr><tr><td><div>Hy-Image-3.0</div></td><td><div><code>hy-image-v3</code></div></td><td><div>文生图/参考生图</div></td><td><div>同步</div></td><td><div>支持 prompt 自动改写、37 组预设尺寸、自定义水印脚注。</div></td></tr><tr><td><div>Hy-Image-3.5-preview</div></td><td><div><code>hy-image-v3.5-preview</code></div></td><td colspan="1" rowspan="1"><div>文生图/参考生图/多轮编辑</div></td><td colspan="1" rowspan="1"><div>同步</div></td><td colspan="1" rowspan="1"><div>支持多模态输入、多轮编辑上下文、外部搜索增强、按面积档位自动决定尺寸。</div></td></tr></tbody></table>

### WAND 系列

详情请参考 [WAND 生图调用指南](https://cloud.tencent.com/document/product/1823/137203)。

<table><colgroup><col/><col/><col/><col/><col/><col/></colgroup><tbody><tr><td><div><b>模型名称</b></div></td><td><div><b>model 参数值</b></div></td><td><div><b>支持能力</b></div></td><td><div><b>提示词上限</b></div></td><td><div><b>分辨率</b></div></td><td><div><b>画面宽高比</b></div></td></tr><tr><td><div>WAND-Vega-Image-1.0-Lite</div></td><td><div>wand-vega-image-lite</div></td><td><div>文生图/参考生图</div></td><td><div>2000字符</div></td><td><div>1K / 2K / 4K</div></td><td colspan="1" rowspan="3"><div>支持 1:1、2:3、3:2、3:4、4:3、9:16、16:9、21:9 常见尺寸</div></td></tr><tr><td><div>WAND-Vega-Image-1.0-Flash</div></td><td><div>wand-vega-image-flash</div></td><td><div>文生图/参考生图</div></td><td><div>2000字符</div></td><td><div>1K / 2K / 4K</div></td><td colspan="0" rowspan="0"><div></div></td></tr><tr><td><div>WAND-Vega-Image-1.0-Pro</div></td><td><div>wand-vega-image-pro</div></td><td><div>文生图/参考生图</div></td><td><div>2000字符</div></td><td><div>1K / 2K / 4K</div></td><td colspan="0" rowspan="0"><div><h2></h2></div></td></tr></tbody></table>

### Vidu 系列

详情请参见 [Vidu 生图调用指南](https://cloud.tencent.com/document/product/1823/135746)。

| 模型名称 | model 参数值 | 支持能力 | 接口类型 | 简要说明 |
| --- | --- | --- | --- | --- |
| Vidu-Image-q2 | `vidu-image-q2` | 参考生图 / 文生图 / 图片编辑 | 异步 | 支持 0~7 张参考图保持主体一致，1080p / 2K / 4K 超清直出。 |

### Seedream 系列

详情请参见 [Seedream 生图调用指南](https://cloud.tencent.com/document/product/1823/136609)。

<table><colgroup><col/><col/><col/><col/><col/></colgroup><tbody><tr><td><div>模型名称</div></td><td><div>model 参数值</div></td><td><div>支持能力</div></td><td><div>接口类型</div></td><td><div>简要说明</div></td></tr><tr><td colspan="1" rowspan="1"><div>Seedream-Image-v5.0-pro</div></td><td colspan="1" rowspan="1"><div><code>seedream-image-v5.0-pro</code></div></td><td colspan="1" rowspan="1"><div>参考生图 / 文生图</div></td><td><div>同步</div></td><td><div>旗舰高精度生图，精准坐标编辑</div></td></tr><tr><td colspan="1" rowspan="1"><div>Seedream-Image-v5.0-lite</div></td><td colspan="1" rowspan="1"><div><code>seedream-image-v5.0-lite</code></div></td><td><div>参考生图 / 文生图</div></td><td><div>同步</div></td><td><div>轻量快速，联网实时检索，高性价比生图</div></td></tr><tr><td><div>Seedream-Image-v5.0-flash</div></td><td><div><code>seedream-image-v5.0-flash</code></div></td><td><div>参考生图 / 文生图</div></td><td><div>同步</div></td><td><div>高速生图模型，出图更快、价格更低</div></td></tr></tbody></table>

### Kling 系列

详情请参见 [Kling 生图调用指南](https://cloud.tencent.com/document/product/1823/138803)。

<table><tbody><tr><td colspan="1" rowspan="1"><div>模型名称</div></td><td colspan="1" rowspan="1"><div>model 参数值</div></td><td colspan="1" rowspan="1"><div>支持能力</div></td><td colspan="1" rowspan="1"><div>提示词上限</div></td><td colspan="1" rowspan="1"><div>分辨率</div></td></tr><tr><td colspan="1" rowspan="1"><div>Kling-Image-v3</div></td><td colspan="1" rowspan="1"><div><code>kling-image-v3</code></div></td><td colspan="1" rowspan="1"><div>文生图 / 图生图（单图参考）</div></td><td colspan="1" rowspan="1"><div>2500 字符</div></td><td colspan="1" rowspan="1"><div>1K / 2K</div></td></tr><tr><td colspan="1" rowspan="1"><div>Kling-Image-o1</div></td><td colspan="1" rowspan="1"><div><code>kling-image-o1</code></div></td><td colspan="1" rowspan="1"><div>文生图 / 图生图（多图参考）</div></td><td colspan="1" rowspan="1"><div>2500 字符</div></td><td colspan="1" rowspan="1"><div>1K / 2K</div></td></tr><tr><td colspan="1" rowspan="1"><div>Kling-Image-v3-omni</div></td><td colspan="1" rowspan="1"><div><code>kling-image-v3-omni</code></div></td><td colspan="1" rowspan="1"><div>文生图 / 图生图（多图参考）/ 系列组图</div></td><td colspan="1" rowspan="1"><div>2500 字符</div></td><td colspan="1" rowspan="1"><div>1K / 2K / 4K</div></td></tr></tbody></table>
