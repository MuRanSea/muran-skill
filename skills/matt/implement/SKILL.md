---
name: implement
description: "Implement a piece of work based on a spec or set of tickets."
disable-model-invocation: true
---

Implement the work described by the user in the spec or tickets.

If the user passes a ticket reference, fetch it from the issue tracker and state its title before starting. If the reference is ambiguous, ask.

Call the Skill tool with "tdd" where possible, at pre-agreed seams.

Run typechecking regularly, single test files regularly, and the full test suite once at the end.

Once done, call the Skill tool with "code-review" to review the work.

Commit your work to the current branch.


## Harness compatibility

When these instructions say to call the Skill tool, use your agent’s native skill loader. If it has no such tool, read the named skill’s `SKILL.md` from the sibling skill directory (resolve paths from this skill directory, not the project working directory). Use available native tools with equivalent behavior. If subagents are unavailable, perform the passes sequentially and disclose that they were not independent.

This skill is intended for explicit user invocation. Harnesses that ignore `disable-model-invocation` should follow this intent; this text is not a runtime permission control.
