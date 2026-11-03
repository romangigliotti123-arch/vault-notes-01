---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/scheduled-tasks.md (+ goal.md, routines.md)
type: official-doc
author: Anthropic (Claude Code docs)
published: undated (current docs, matches Claude Code 2.1.312; fetched raw .md)
accessed: 2026-10-29
reliability: high (official, raw markdown)
---
# /loop, session-scoped cron, /goal and routines (Claude Code docs)
## Key claims
- Three scheduling options: Cloud routines (runs without your machine; fresh clone, no local files; min interval 1 hour; auto mode by default), Desktop scheduled tasks (your machine, no open session needed, needs the Desktop app), `/loop` (session-scoped, needs open session, min 1 minute). `/loop` is a bundled skill; prompt-only form lets Claude pick a 1 min-1 h delay each iteration and may use the Monitor tool instead of polling ("often more token-efficient and responsive"). Bare `/loop` runs a built-in maintenance prompt or `.claude/loop.md` / `~/.claude/loop.md` (truncated at 25,000 bytes; edits apply next iteration).
- Underlying tools `CronCreate/CronList/CronDelete`; 50 tasks per session; recurring tasks EXPIRE after 7 days (fire once more then delete); jitter up to half the gap, max 30 min (use off-:00 minutes for one-shots); tasks fire only while Claude is running AND idle; no catch-up for missed fires; self-paced `/loop` is not restored on resume; `CLAUDE_CODE_DISABLE_CRON=1` disables the scheduler. A scheduled fire runs only skills Claude may invoke itself (not `disable-model-invocation`, not built-in commands).
- In a background session a self-paced loop stops if its wakeup comes due while the process is down; fallback wakeup ~20 min if an iteration neither reschedules nor stops.
- `/goal <condition>` = session-scoped prompt-based Stop hook: after every turn a small fast model judges the condition from what is in the transcript (it runs no tools); verdicts not-met / met / impossible; condition up to 4,000 chars; put a bound inside it ("or stop after 20 turns"); works in `-p` (`claude -p "/goal ..."` loops to completion; use `--output-format stream-json --verbose` to see progress), in Remote Control and Desktop; restored on resume (counters reset); evaluation is deferred while subagents/background commands run, with check-ins after 30 min then doubling (`CLAUDE_CODE_GOAL_CHECKIN_MINUTES`; 0 disables check-ins and auto-retries); stops after several turns with no tool use; a goal does not change permission mode ("run /goal in auto mode to run unattended").
- Auto-retry/pause behaviour: 3 automatic retries for transient API errors, then pause; usage-limit errors pause the goal and resume if auto-continue at limit reset is active (`autoContinueAtUsageLimit`, default true, v2.1.234+; user/managed scope).
- Routines (cloud): triggers = schedule, API, GitHub event; need claude.ai login; run in auto mode with no permission prompts; branch protection recommended; per-run effort level selectable in the model picker (2.1.312). Not usable for tasks needing local files/hosts.
## Quotable
> "`/goal` adds a separate evaluator that checks your condition after every turn, so completion is decided by a fresh model rather than the one doing the work."
> "Recurring tasks automatically expire 7 days after creation."

## Used by
[[topic-claude-code-features]]
