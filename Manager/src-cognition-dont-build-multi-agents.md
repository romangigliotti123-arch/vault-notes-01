---
tags: [manager-kb, source]
url: https://cognition.com/blog/dont-build-multi-agents
type: eng-blog
author: Walden Yan (Cognition)
published: 2025 (exact date not shown in fetch)
accessed: 2026-10-29
reliability: med (practitioner, strong opinion, 1 product)
---
# Don't Build Multi-Agents (Cognition)
## Key claims
- Principle 1: "Share context, and share full agent traces, not just individual messages." Passing only the subtask text loses what earlier turns and tool calls implied.
- Principle 2: "Actions carry implicit decisions, and conflicting decisions carry bad results." Parallel subagents make unstated assumptions that clash.
- Flappy Bird example: parent splits into two subtasks; one subagent builds a Super-Mario-like background, other a bird that moves wrongly; the merge step must reconcile incompatible work. Copying the original task text to each subagent does not fully fix it.
- Default recommendation: single-threaded linear agent; for long tasks add a context-compression model that condenses history into key details, events, decisions (hard to get right).
- Claude Code subagents are cited as the safe form: they answer narrow questions, do not write code in parallel with the main agent, and keep investigation out of main history.
- Edit-apply split (big model writes instructions, small model applies) caused errors from ambiguity; single model doing both is now typical.
## Quotable
> "Actions carry implicit decisions, and conflicting decisions carry bad results."
## Note
Fetched via WebFetch summary (model-summarised); principle wordings quoted as returned. Date not shown in fetch; widely dated June 2025.

## Used by
[[topic-anthropic-agent-guidance]], [[topic-brief-prompt-engineering]], [[topic-context-engineering]], [[topic-context-window-management]], [[topic-model-effort-routing-cost]], [[topic-multi-agent-failure-modes]], [[topic-multi-agent-frameworks]], [[topic-orchestration-patterns]], [[topic-report-formats-and-verification]]
