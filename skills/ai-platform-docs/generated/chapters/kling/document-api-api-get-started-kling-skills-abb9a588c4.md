<!-- Official source: https://klingai.com/document-api/api/get-started/kling-skills.md -->
<!-- Source SHA-256: b3f3cd778f70c32f2b231a9b1a9cdbba2a69928491f670901a4dc449651d931c -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://klingai.com/document-api/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling Skills

> 来源: https://klingai.com/document-api/api/get-started/kling-skills
> 语言: zh
> 当前 Tab: Kling Skills
> 此内容为面向 LLM 优化的 Markdown，已展开页面内 Tab，并省略页面目录、复制按钮等 UI 控件。

更新日期：2026年10月28日

---

::: info-box

KlingAI API 官方 skill，开发者可以在第三方Agent中使用Kling AI Skill进行视频生成、图片生成和主体管理等，支持Openclaw、Claude Code、Cursor、Codex、Copilot、Opencode等工具。根据用户意图自动选择子命令 video / image / element，智能路由到对应 API 端点。

---

<SkillCard icon="K" color="#2261f5" title="Kling AI Skill" clawHubButton="true" clawHubUrl="https://clawhub.ai/klingai-dev/klingai" buyButton="true" buyUrl="https://klingai.com/dev/pricing?scrollTo=video-package" buyText="购买资源包">
    <ul style="font-size: 12px !important;">
        <li style="font-size: 12px !important;">视频生成支持模型：kling-3.0 / kling-3.0-turbo / kling-3.0-omni / kling-2.6 / kling-2.5-turbo / kling-o1</li>
        <li style="font-size: 12px !important;">图片生成支持模型：kling-v3 / kling-v3-omni / kling-v2-1 / kling-image-o1</li>
        <li style="font-size: 12px !important;">主体/角色管理 -- 创建可复用的角色、跨视频保持人物一致性</li>
    </ul>
</SkillCard>

---

## 使用指南

<div style="width: 60%; min-width: 600px;">
<video src="https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/videos/kling_skill_zh.721d69809dd5ba6b.mp4" controls width="100%"></video>
</div>

## Skill 接入说明

---

### 下载地址

[https://clawhub.ai/klingai-dev/klingai](https://clawhub.ai/klingai-dev/klingai)

### 环境要求：

\*Node.js 18+，无其他依赖。

### 认证方式：

- 安装skill时将提供url链接，使用可灵账号完成一键绑定（推荐）
- 手动获取 api-key 后通过指令绑定：
  `node kling.mjs account --import-credentials --api_key "<API_KEY>"`

### 区域：

未设置 KLING_API_BASE 时，脚本自动探测中国/全球端点并缓存。可通过设置 KLING_API_BASE 强制指定区域。

## 注意事项

- 每次提交均会产生费用，意图不明确时请先确认再提交
- 视频生成通常需要 1–5 分钟，图片约 20–60 秒，主体创建约 30 秒–2 分钟
- 生成资源保留 30 天，请及时下载保存
- 支持中英文双语交互，自动检测用户语言
