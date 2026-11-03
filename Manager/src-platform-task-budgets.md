---
tags: [manager-kb, source]
url: https://platform.claude.com/docs/en/build-with-claude/task-budgets
type: official-doc
author: Anthropic (Claude Developer Platform docs)
published: undated (beta header task-budgets-2026-03-13)
accessed: 2026-10-29
reliability: high (official)
---
# Task budgets (advisory token countdown for an agent loop)
## Key claims
- Gives the model a running countdown over a full agentic loop (thinking + tool calls + tool results + output); model uses it to prioritise and finish gracefully. Advisory, not enforced ("a soft hint, not a hard cap"); `max_tokens` remains the hard per-request cap. Minimum 20,000 tokens.
- A budget that is clearly too small "can cause refusal-like behavior": the model may decline, scope down aggressively or stop early. Size against measured p99 per-task spend.
- Complements effort: effort = depth per step; task budget = breadth of total work.
- Does NOT apply to Claude Code or Cowork ("Task budgets are not supported on Claude Code or Cowork surfaces"); in Managed Agents use session budgets instead. Supported on Opus 5/5.5, Sonnet 5.5, Haiku 5.5, Fable/Mythos 5.x; not Sonnet 5.
- Do not mutate the budget client-side each request (invalidates prompt cache; under-reporting makes the model finish early).
- Relevance: the analogue for a Claude Code manager is `--max-turns`, `--max-budget-usd`, `maxTurns` in agent files, and an explicit "stop after N turns" clause in /goal.
## Quotable
> "A budget that is too small for the task can cause refusal-like behavior."

## Used by
[[topic-anthropic-agent-guidance]]
