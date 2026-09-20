---
name: handoff
description: Compact the current conversation into a handoff document for another agent to pick up.
argument-hint: "What will the next session be used for?"
disable-model-invocation: true
---

Write a handoff document summarising the current conversation so a fresh agent can continue the work. Save to the temporary directory of the user's OS - not the current workspace.

Include a "suggested skills" section in the document, naming which skills the next agent should call the Skill tool for.

Do not duplicate content already captured in other artifacts (specs, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead.

Redact any sensitive information, such as API keys, passwords, or personally identifiable information.

If the user passed arguments, treat them as a description of what the next session will focus on and tailor the doc accordingly.


## Harness compatibility

When these instructions say to call the Skill tool, use your agent’s native skill loader. If it has no such tool, read the named skill’s `SKILL.md` from the sibling skill directory (resolve paths from this skill directory, not the project working directory). Use available native tools with equivalent behavior. If subagents are unavailable, perform the passes sequentially and disclose that they were not independent.

This skill is intended for explicit user invocation. Harnesses that ignore `disable-model-invocation` should follow this intent; this text is not a runtime permission control.
