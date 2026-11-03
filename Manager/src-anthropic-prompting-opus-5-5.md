---
tags: [manager-kb, source]
url: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5
type: official-doc
author: Anthropic
published: undated
accessed: 2026-10-29
reliability: high (official; sections read: Unattended agentic runs, Time signals)
---
# Prompting Claude Opus 5.5 (unattended runs, time signals)
## Key claims
- Unattended loops: Opus 5.5 keeps the user updated and "some of those updates end the turn with text rather than a tool call". An unattended loop that treats a text-only end_turn as completion stops there. "Treat a text-only end of turn as a report rather than as proof the task is done."
- Remedy: keep the task parts in a checklist the model updates (to-do tool or file); if a turn ends with items open and no blocker stated, send a short user message naming them; or state a completion condition up front and have a smaller model check each end of turn; "stop after two or three automatic continuations on the same task" so a stuck run ends and can be reviewed.
- If something the model started is still running (background command, subagent), do not treat the task as done: wait for it and return its output as the next user message.
- A system-prompt addition naming the specific early-stop patterns (summary that announces next step instead of doing it; offer to continue unless user prefers; list of decisions that block nothing; "good place to report") reduces stops. Keep your own confirmation step for risky actions. Expect somewhat more tool calls/tokens.
- Time signals for multi-agent harnesses: give a time budget, e.g. line `elapsed 340s / 1200s` after each message; in Anthropic's evals of small agent teams, budgets made teams finish considerably sooner at comparable quality; the budget is advisory, "keep your own timeout"; under time pressure the model may search/verify a little less.
## Quotable
> "Treat a text-only end of turn as a report rather than as proof the task is done."

## Used by
[[topic-anthropic-agent-guidance]], [[topic-brief-prompt-engineering]], [[topic-context-engineering]], [[topic-multi-agent-failure-modes]], [[topic-report-formats-and-verification]]
