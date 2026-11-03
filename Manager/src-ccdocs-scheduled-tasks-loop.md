---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/scheduled-tasks.md
type: official-doc
author: Anthropic (Claude Code docs)
published: undated (docs for Claude Code ~2.1.31x)
accessed: 2026-10-29
reliability: high (official doc, full page fetched)
---
# Run prompts on a schedule (/loop, CronCreate)
## Key claims
- Session-scoped scheduling: `/loop`, `CronCreate/CronList/CronDelete`. "Tasks only fire while Claude Code is running and idle." Closing the terminal stops them.
- Three scheduling options compared: Cloud (min interval 1 h, no machine needed), Desktop (needs app open + computer awake, min 1 min if Claude sets it, 1 h in forms), `/loop` (needs open session, min 1 min).
- Recurring tasks auto-expire after 7 days (fire once more then delete). Up to 50 tasks per session.
- Jitter: recurring tasks run late by up to half the gap (max 30 min); `*/5 * * * *` runs 4m45s after the previous (cache-TTL aware).
- "No catch-up for missed fires": if due while Claude is busy, fires once when idle, not once per missed interval. After `--resume`, a recurring task does not fire for runs missed while the session was not running.
- Self-paced `/loop` (no interval): Claude picks 1 min to 1 h each iteration; if an iteration neither reschedules nor stops, a fallback wakeup ~20 min later is scheduled and then the loop ends. Self-paced loop is NOT restored on `--resume`; in a background session it stops if the wakeup comes due while the process is down (e.g. crash).
- Bare `/loop` runs a built-in maintenance prompt (continue unfinished work, tend PR, cleanup passes) or `~/.claude/loop.md` (truncated at 25,000 bytes). "irreversible actions such as pushing or deleting only proceed when they continue something the transcript already authorized."
- Background Bash commands and monitors are not restarted on resume. Monitor tool streams script output lines back (avoids polling).
- `CLAUDE_CODE_DISABLE_CRON=1` disables the scheduler.
## Quotable
> Tasks only fire while Claude Code is running and idle. Closing the terminal or letting the session exit stops them firing.
> No catch-up for missed fires.

## Used by
[[topic-context-window-management]], [[topic-long-running-always-on-agents]]
