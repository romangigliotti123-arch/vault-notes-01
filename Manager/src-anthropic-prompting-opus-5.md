---
tags: [manager-kb, source]
url: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5
type: official-doc
author: Anthropic
published: undated
accessed: 2026-10-29
reliability: high (official)
---
# Prompting Claude Opus 5
## Key claims
- Opus 5 "performs best when given the complete task specification up front and left to run."
- Reviews: "If your review prompt says 'only report high-severity issues' or 'be conservative,' the model might follow that instruction literally and report less; ask it to report everything and filter in a separate pass instead."
- Effort does not reliably shorten visible responses; prompt for conciseness. Narration cadence snippet: "Before your first tool call, say in one sentence what you're about to do... When you finish, lead with the outcome: your first sentence should answer 'what happened' or 'what did you find'". Positive examples of the wanted style beat prohibitions.
- Written deliverables are longer: add "Match the length of written documents to what the task needs... do not pad with filler sections, redundant summaries, or boilerplate."
- Over-verification: "If your prompt contains explicit verification instructions ('include a final verification step for any non-trivial task,' 'use a subagent to verify'), remove them"; same for "double-check your answer".
- Scope snippet: "Deliver what was asked, at the scope intended. Make routine judgment calls yourself, and check in only when different readings of the request would lead to materially different work. If the request seems mistaken or a better approach exists, say so in a sentence and continue with the task as asked rather than quietly narrowing, widening, or transforming it."
- Subagent control: delegates more readily than prior models; give explicit guidance or deterministic caps (`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`, `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`, `max_budget_usd`). Snippet: "Delegate to a subagent only for large tasks that are genuinely independent and parallelizable... Do not delegate work you can finish yourself in a handful of tool calls, and do not use subagents to verify or double-check your own work. If one subagent can complete the task, use one rather than several."
- Self-correction: limit narrated corrections to those that change the user's code, conclusions or decisions.
- Asking the model to reproduce its reasoning verbatim can trigger `reasoning_extraction` refusals; ask for a short explanation or summary of actions.
- Strong at "effective writer-verifier patterns" in subagent teams.
## Quotable
> "instructions like these cause over-verification on Claude Opus 5, and removing them reduces wasted tokens with no loss in quality."

## Used by
[[topic-anthropic-agent-guidance]], [[topic-brief-prompt-engineering]], [[topic-context-engineering]], [[topic-report-formats-and-verification]]
