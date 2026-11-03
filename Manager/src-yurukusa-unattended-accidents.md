---
tags: [manager-kb, source]
url: https://dev.to/yurukusa/i-let-claude-code-run-unattended-for-108-hours-heres-every-accident-that-happened-51cm
type: practitioner-blog
author: Yurukusa
published: undated (page: "Posted on Mar 11", edited Aug 12; year not shown, author joined Feb 2026)
accessed: 2026-10-29
reliability: low-med (self-reported anecdotes; vendor of a setup tool)
---
# "I let Claude Code run unattended for 108 hours: every accident"
## Key claims
- Seven incidents: agent deleted src/ during "cleanup" (twice); sub-agent looped on an external API ($8 in one hour, noticed next morning); fix-check-fail repeated 20 times with "fixed" each time; pushed to main without review; context filled and agent restarted the task from scratch (3 h overwritten); PUT without prior GET blanked an article (twice); idle watchdog hit a rate limit and logged "RATE_LIMIT" every 15 s indefinitely.
- Mitigations the author credits with "70% of the accidents": PreToolUse hook blocking destructive commands (rm -rf, git reset --hard, push --force); CLAUDE.md rule "retry up to 3 times, then log the blocker to a pending file and move to the next task"; a `mission.md` saved before compaction.
- "Claude Code's default setup assumes a human is sitting next to it."

## Used by
[[topic-agent-security]], [[topic-long-running-always-on-agents]]
