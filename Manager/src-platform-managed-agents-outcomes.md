---
tags: [manager-kb, source]
url: https://platform.claude.com/docs/en/managed-agents/define-outcomes
type: official-doc
author: Anthropic (Claude Managed Agents docs)
published: undated (beta; header managed-agents-2026-04-01; secondary sources say public beta 2026-05-06)
accessed: 2026-10-29
reliability: high (official doc read in full)
---
# Managed Agents: Define outcomes (rubric + separate grader)
## Key claims
- The harness provisions a grader that "uses a separate context window to avoid being influenced by the main agent's implementation choices"; returns which criteria passed/failed, handed back to the agent for the next iteration. Rubric is required, a markdown doc of explicit, gradeable criteria ("The CSV contains a price column with numeric values" not "The data looks good"); the grader scores each criterion independently, "vague criteria produce noisy evaluations". No rubric? Give a known-good artifact and have Claude derive the rubric from what makes it good.
- `user.define_outcome` event: description + rubric (inline or file) + `max_iterations` (default 3, max 20). Results per evaluation: `satisfied`, `needs_revision`, `max_iterations_reached` (one acknowledgement turn then idle), `failed` (rubric does not apply), `interrupted`. One outcome at a time; outcomes can be chained. Session retains history and can continue conversationally after.
- Pattern: worker -> independent grader with fixed rubric -> gap list -> worker revises, with an iteration cap. This is Anthropic's productised generator-verifier (see [[src-claudecom-multi-agent-coordination-patterns]]).
## Quotable
> "The grader uses a separate context window to avoid being influenced by the main agent's implementation choices."

## Used by
[[topic-anthropic-agent-guidance]], [[topic-context-engineering]]
