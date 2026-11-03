---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/goal.md
type: official-doc
author: Anthropic (Claude Code docs)
published: undated (v2.1.234-2.1.269 features)
accessed: 2026-10-29
reliability: high (official doc, full page read)
---
# /goal: keep working toward a completion condition
## Key claims
- `/goal <condition>` = session-scoped prompt-based Stop hook; after every turn a small fast model (Haiku class) judges: not yet met / met / impossible. Evaluator "doesn't run commands or read files independently"; it judges only what Claude surfaced in the conversation. Condition up to 4,000 chars; bound with "or stop after 20 turns".
- Works with `-p` (runs loop to completion; use `--output-format stream-json --verbose` or it looks stuck), desktop and Remote Control. Restored on `--resume` but turn count/timer/token baseline reset.
- Errors that clear the goal: auth failure (when CC manages creds), exhausted credit balance, context overflow auto-compaction can't clear, model unavailable. Other errors: retry (overloaded/dropped connection; after 3 automatic retries the goal pauses) or pause (rate limit, claude.ai usage limit, hook ended the turn); if the session is waiting for usage reset, work resumes then.
- No-progress guard: no tool use for several turns => loop stops with a warning and returns control.
- Background work defers evaluation; check-ins after 30 min of waiting (then 1 h, then every 2 h; max 3 idle check-ins; `CLAUDE_CODE_GOAL_CHECKIN_MINUTES`, 0 turns off check-ins and retries).
- `/loop` = time-triggered, `/goal` = condition-triggered, Stop hook = your own logic.
## Quotable
> completion is decided by a fresh model rather than the one doing the work.

## Used by
[[topic-anthropic-agent-guidance]], [[topic-llm-judge-and-adversarial-verification]], [[topic-long-running-always-on-agents]], [[topic-multi-agent-failure-modes]]
