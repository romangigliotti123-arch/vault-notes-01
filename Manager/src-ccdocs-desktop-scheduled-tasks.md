---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/desktop-scheduled-tasks.md
type: official-doc
author: Anthropic (Claude Code docs)
published: undated
accessed: 2026-10-29
reliability: high (official doc)
---
# Desktop scheduled tasks (local)
## Key claims
- Local tasks "only fire while the app is open and your computer is awake"; if the computer sleeps through the time, the run is skipped; "Keep computer awake" setting exists.
- Missed runs: on app start/wake, Desktop starts exactly ONE catch-up run for the most recently missed time within the last 7 days and discards older ones. Doc advises guardrails in the prompt ("If it's after 5pm, skip the review...").
- Each task has own permission mode; Manual-mode tasks stall until approved; "Run now" after creating to pre-approve tools. Stored at `~/.claude/scheduled-tasks/<task-name>/SKILL.md` (frontmatter name/description, prompt as body); schedule/model/folder are NOT in that file. A task can reschedule itself via `update_scheduled_task`.
- History list shows skipped runs with the reason (asleep, previous run still in progress, other tasks running). Deterministic stagger delay of a few minutes.
- Worktree option isolates each run's files.

## Used by
[[topic-long-running-always-on-agents]]
