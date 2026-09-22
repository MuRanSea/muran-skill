---
name: grill-me
description: A relentless interview to sharpen a plan or design.
disable-model-invocation: true
---

Call the Skill tool with "grilling".


## Harness compatibility

When these instructions say to call the Skill tool, use your agent’s native skill loader. If it has no such tool, read the named skill’s `SKILL.md` from the sibling skill directory (resolve paths from this skill directory, not the project working directory). Use available native tools with equivalent behavior. If subagents are unavailable, perform the passes sequentially and disclose that they were not independent.

This skill is intended for explicit user invocation. Harnesses that ignore `disable-model-invocation` should follow this intent; this text is not a runtime permission control.
