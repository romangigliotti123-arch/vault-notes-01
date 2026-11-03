---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/hooks.md ; /interactive-mode.md ; /goal.md ; /commands.md
type: official-doc
author: Anthropic
published: undated (docs fetched 2026-10-29)
accessed: 2026-10-29
reliability: high (official docs, raw markdown, grep-read)
---
# Claude Code docs: Notification hook types, session recap, /goal, status commands
## Key claims
- `Notification` hook matcher types: `permission_prompt` (fires only after the prompt has waited ~6 s; each keystroke defers it), `idle_prompt` ("Claude finished responding about 60 seconds ago and you haven't typed since"; suppressed while a background subagent still runs), `auth_success`, `elicitation_*`, `agent_needs_input` and `agent_completed` (background sessions, only while agent view is open in a terminal), `quota_auto_resume_*`. `PermissionRequest` hook fires immediately when a tool asks permission.
- Session recap: one-line recap generated after >=3 min away and >=3 turns; `/recap` on demand; both capped at 400 characters; never in non-interactive mode; `/recap` text works from phone.
- `/goal <condition>`: after every turn a separate evaluator model checks the condition; Claude keeps working until met/impossible/error. "completion is decided by a fresh model rather than the one doing the work". Alternatives: `/loop` (time interval), Stop hook (own script). Auto mode and /goal are complementary (per-tool prompts vs per-turn prompts).
- Commands that run immediately even while Claude is responding: `/status`, `/tasks`, `/usage`. Other messages sent mid-turn are queued and run after the current turn finishes. `/btw` = side question without adding to history. `/tasks` lists background work incl. finished subagents.
- Usage limit: in interactive sessions Claude waits and continues automatically after the limit resets (v2.1.234+), per interactive-mode.md; RC doc says plan accordingly for RC sessions (see manager-setup.md).
## Quotable
> Claude finished responding about 60 seconds ago and you haven't typed since

## Used by
[[topic-remote-mobile-ux]]
