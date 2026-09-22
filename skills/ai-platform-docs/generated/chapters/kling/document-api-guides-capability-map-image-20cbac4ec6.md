<!-- Official source: https://klingai.com/document-api/guides/capability-map/image.md -->
<!-- Source SHA-256: c035ebe70c06f5b43d8954d3423f0cce105c25446e5e91c297cb41cac6df4b7a -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://klingai.com/document-api/llms.txt
> Use this file to discover all available pages before exploring further.

# 图片能力地图

> 来源: https://klingai.com/document-api/guides/capability-map/image
> 语言: zh
> 更新日期: 2026-05-19
> 此内容为面向 LLM 优化的 Markdown，已省略页面目录、复制按钮等 UI 控件。

基于现有 Image Models 文档整理，展示不同图片模型、比例与能力支持范围。

## Models

| Model | Description | Input | Generation Range | Resolution |
| --- | --- | --- | --- | --- |
| Kling Image 3.0 | 强化一致性，自由多参考图，全面效果升级 | 文本、图片 | 16:9、9:16、1:1、4:3、3:4、3:2、2:3、21:9 | 1K, 2K |
| Kling Image 3.0 Omni | 强化叙事感、直出2K/4K超高清图、系列组图生成 | 文本、图片 | 16:9、9:16、1:1、4:3、3:4、3:2、2:3、21:9、auto | 1K, 2K, 4K |
| Kling Image O1 | 高特征一致性，精准细节修改，风格迁移准确 | 文本、图片 | 16:9、9:16、1:1、4:3、3:4、3:2、2:3、21:9、auto | 1K, 2K |
| Kling Image 2.1 | 指令遵循强，文字强化，出图稳定 | 文本、图片 | 16:9、9:16、1:1、4:3、3:4、3:2、2:3、21:9 | 1K, 2K |

## Global Capabilities

| Capability | Value | Description |
| --- | --- | --- |
| 扩图 | 不区分模型版本 | 可基于已有图片扩展内容 |

## 文生图

| Capability | Description | Kling Image 3.0 | Kling Image 3.0 Omni | Kling Image O1 | Kling Image 2.1 |
| --- | --- | --- | --- | --- | --- |
| 单图生成 | - | 支持 | 支持: 长宽比不支持auto | 支持 | 支持 |

## 图生图

| Capability | Description | Kling Image 3.0 | Kling Image 3.0 Omni | Kling Image O1 | Kling Image 2.1 |
| --- | --- | --- | --- | --- | --- |
| 单图生成 | - | 支持 | 支持 | 支持 | 支持 |
| 组图生成 | - | 不支持 | 支持 | 不支持 | 支持 |
| 多图参考图 | - | 不支持 | 支持 | 支持 | 支持 |
| 角色特征参考 | - | 不支持 | 不支持 | 不支持 | 支持 |
| 人脸特征参考 | - | 不支持 | 不支持 | 不支持 | 支持 |
| 风格训练 | - | 不支持 | 不支持 | 不支持 | 不支持 |
| 主体控制 | - | 支持: 仅多图主体 | 支持: 仅多图主体 | 支持: 仅多图主体 | 不支持 |
