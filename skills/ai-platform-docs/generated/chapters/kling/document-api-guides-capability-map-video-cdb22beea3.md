<!-- Official source: https://klingai.com/document-api/guides/capability-map/video.md -->
<!-- Source SHA-256: e68f5725b2ef6c99f4251607e3f816fa24549a4b0db75e78e95eea1846014364 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://klingai.com/document-api/llms.txt
> Use this file to discover all available pages before exploring further.

# 视频能力地图

> 来源: https://klingai.com/document-api/guides/capability-map/video
> 语言: zh
> 更新日期: 2026-05-19
> 此内容为面向 LLM 优化的 Markdown，已省略页面目录、复制按钮等 UI 控件。

基于现有 Video Models 文档整理，展示不同视频模型、模式与能力支持范围。

## Models

| Model | Description | Input | Generation Range | Resolution |
| --- | --- | --- | --- | --- |
| Kling 3.0 Turbo | 效果稳定出色，性价比更优 | 文本、图片 | 3~15s | 720P、1080P |
| Kling 3.0 | 音画同步升级，主体一致性增强，支持多镜头叙事 | 文本、图片、视频 | 3~15s | 720P、1080P、4K |
| Kling 3.0 Omni | 全能多模态输入，有声角色驱动，直出音画和分镜 | 文本、图片、视频 | 3~15s | 720P、1080P、4K |
| Kling O1 | 大一统视频模型，全能多模态指令，超高一致性 | 文本、图片、视频 | 3~10s | 720P、1080P |
| Kling 2.6 | 音画同步生成，有声音更精彩 | 文本、图片、视频 | 3~10s | 720P、1080P |
| Kling 2.5 Turbo | 超绝想象力，极具性价比 | 文本、图片 | 5s、10s | 720P、1080P |

## Global Capabilities

| Capability | Value | Description |
| --- | --- | --- |
| 数字人 | 不区分模型版本 | 只需一张照片即可生成数字人播报类视频 |
| 对口型 | 不区分模型版本 | 可结合文案或音频，驱动视频中角色的口型 |
| 多模态视频编辑 | 不区分模型版本 | 支持对视频中元素进行标记、替换与增删等编辑操作 |
| 视频生音效 | 不区分模型版本 | 支持为所有可灵模型生成的视频和用户上传的符合视频格式要求的视频添加音效 |
| 文生音效 | 不区分模型版本 | 支持通过输入文本描述（prompt）生成音效 |

## 文生视频

| Capability | Description | Kling 3.0 Turbo | Kling 3.0 | Kling 3.0 Omni | Kling O1 | Kling 2.6 | Kling 2.5 Turbo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 单镜头视频生成 | - | 支持 | 支持 | 支持 | 支持: 时长仅5s、10s | 支持: 时长仅5s、10s，720P仅支持无声视频 | 支持 |
| 多镜头视频生成 | - | 支持 | 支持 | 支持 | 不支持 | 不支持 | 不支持 |
| 音画同出 | - | 支持 | 支持 | 支持 | 不支持 | 支持 | 不支持 |
| 声音控制（人声） | - | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 |

## 图生视频

| Capability | Description | Kling 3.0 Turbo | Kling 3.0 | Kling 3.0 Omni | Kling O1 | Kling 2.6 | Kling 2.5 Turbo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 单镜头视频生成 | - | 支持 | 支持 | 支持 | 支持: 时长仅5s、10s | 支持: 时长仅5s、10s，720P仅支持无声视频 | 支持 |
| 多镜头视频生成 | - | 支持 | 支持 | 支持 | 不支持 | 不支持 | 不支持 |
| 首尾帧 | - | 不支持 | 支持 | 支持 | 支持 | 支持: 仅1080P且仅无声视频 | 支持: 仅支持 1080P |
| 仅尾帧 | - | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 |
| 主体控制 | 视频角色主体+多图主体 | 不支持 | 支持 | 支持 | 支持: 仅多图主体 | 不支持 | 不支持 |
| 音画同出 | - | 支持 | 支持 | 支持 | 不支持 | 支持 | 不支持 |
| 声音控制（人声） | - | 不支持 | 不支持 | 不支持 | 不支持 | 支持: 仅支持时长5s或10s，且1080P视频 | 不支持 |
| 动作控制 | - | 不支持 | 支持: 4K不支持 | 不支持 | 不支持 | 支持 | 不支持 |
| 视频参考 | 特征参考+视频编辑 | 不支持 | 不支持 | 支持 | 支持 | 不支持 | 不支持 |
