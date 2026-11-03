---
tags: [manager-kb, source]
url: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5
type: official-doc
author: Anthropic (Claude Developer Platform docs)
published: undated (Opus 5 page; Opus 5.5 page links here for subagent control)
accessed: 2026-10-29
reliability: high (official)
---
# Prompting Claude Opus 5 (orchestration-relevant parts)
## Key claims
- Strong at long-horizon agentic work; "performs best when given the complete task specification up front and left to run". "coordinates teams of subagents well, with effective writer-verifier patterns and few cases of agents overwriting each other's work."
- Effort: default `high`; "use `low` and `medium` liberally as your primary control for token cost and response time wherever quality holds, and step up to `xhigh` for demanding coding and agentic work." Re-run effort sweeps per model.
- Verbosity: effort controls thinking, not visible length; lowering effort "without reliably shortening the visible response". Prompt for length explicitly. Narrates a lot during agentic work: prescribe cadence, e.g. "Before your first tool call, say in one sentence what you're about to do... When you finish, lead with the outcome". Written deliverables run long: "Match the length of written documents to what the task needs".
- Over-verification: "Claude Opus 5 verifies its own work without being told to. If your prompt contains explicit verification instructions ('include a final verification step', 'use a subagent to verify'), remove them" - they waste tokens with no quality gain; same for "double-check your answer".
- Scope: can expand a task; constrain with "Deliver what was asked, at the scope intended. Make routine judgment calls yourself, and check in only when different readings of the request would lead to materially different work. If the request seems mistaken or a better approach exists, say so in a sentence and continue..."
- Subagent spawning: "delegates to subagents more readily than prior models... it multiplies cost and time when applied to small tasks." Damping prompt: "Delegate to a subagent only for large tasks that are genuinely independent and parallelizable... Do not delegate work you can finish yourself in a handful of tool calls, and do not use subagents to verify or double-check your own work. If one subagent can complete the task, use one rather than several, and keep spawn counts low." Deterministic caps: `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`, `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`, SDK `max_budget_usd`. Custom/omitted system prompt gets no built-in delegation instruction.
- Code review prompts: "only report high-severity issues"/"be conservative" is followed literally and under-reports; ask for everything, filter in a separate pass.
- Prompts asking the model to write its reasoning verbatim may hit `reasoning_extraction` refusals; ask for a short explanation instead.
## Quotable
> "Delegate to a subagent only for large tasks that are genuinely independent and parallelizable"
> "instructions like these cause over-verification on Claude Opus 5, and removing them reduces wasted tokens with no loss in quality."

## Used by
[[topic-anthropic-agent-guidance]], [[topic-context-engineering]]
