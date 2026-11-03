---
tags: [manager-kb, source]
url: https://github.com/disler/claude-code-hooks-mastery
type: repo
author: disler (IndyDevDan)
published: undated (README read 2026-10-29; covers 13 hook events incl. Setup, PermissionRequest)
accessed: 2026-10-29
reliability: med (popular practitioner demo repo; code read, not run)
---
# disler/claude-code-hooks-mastery
## Key claims
- Demonstrates all 13 hook events with UV single-file Python scripts (inline dependency headers) under `.claude/hooks/`, logging every event as JSON under `logs/`; security-blocks `rm -rf` and `.env` access in PreToolUse; UserPromptSubmit validation + context injection; PreCompact transcript backup; SessionStart loads git status/issues; PermissionRequest auto-allows read-only ops; TTS notifications on Stop/Notification (the Notification/Stop-to-audio pattern parallels Roman's Telegram voice replies).
- Builder/Validator pairing as "team": `team/builder.md` (all tools; PostToolUse ruff+ty validators block on lint/type errors) and `team/validator.md` (frontmatter `model: opus`, `disallowedTools: Write, Edit, NotebookEdit`, "ONE task", reads acceptance criteria via TaskGet, runs read-only checks, must emit a pass/fail report with Checks Performed / Files Inspected / Commands Run / Issues Found). Stated rationale: "This two-agent pairing increases compute to increase trust that work was delivered correctly."
- `/plan_w_team` is a "self-validating" command: its frontmatter declares Stop hooks that run validators (a script that checks a new spec file exists in `specs/` and `--contains` required headings, e.g. '## Task Description'); on failure the validator's message tells the agent exactly what to do and "Do not stop until ..." so it keeps working. Same mechanism could gate worker reports (RESULT:/VERIFIED: present).
- Templated meta-prompts: a command that emits plans in a fixed vetted format ("template meta prompt") so output shape is predictable.
- Repo also ships an output-styles collection and custom status lines (not read in detail).
- Caveat: validators in the sample exit 1 on failure in their docstring; per the official hooks reference only exit 2 (or JSON decision) blocks a Stop hook, so copy the pattern, not the exit codes.
## Quotable
> "This two-agent pairing increases compute to increase trust that work was delivered correctly."

## Used by
[[topic-claude-code-features]]
