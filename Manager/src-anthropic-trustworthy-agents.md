---
tags: [manager-kb, source]
url: https://www.anthropic.com/research/trustworthy-agents
type: eng-blog
author: Anthropic Frontier Red Team
published: 2026-04-09
accessed: 2026-10-29
reliability: high (primary policy/safety framing; light on numbers)
---
# Trustworthy agents in practice
## Key claims
- Four layers: model, harness (instructions/guardrails), tools, environment; safety depends on all four; each is both capability and an oversight point.
- Human control: per-tool/per-action permissions (allow, ask, block); Plan Mode (show the whole plan up front, user edits/approves, oversight moves from steps to strategy). Subagents complicate visibility; Anthropic "exploring new coordination patterns".
- Knowing when to ask: models trained to pause on ambiguity; cited result: check-in rate on complex tasks roughly doubled while user interruptions rose only slightly.
- Prompt injection: malicious instructions hidden in content the agent processes; layered defences, no single one sufficient; scrutinise which tools/data/permissions/environments an agent gets.
- Five principles: humans in control, aligned with human values, secure interactions, transparency, privacy.
## Quotable
> "Agents act with less human oversight, so there is more room for them to misread users' intent"
> "each one is both a source of capability and a potential point of oversight"

## Used by
[[topic-agent-security]], [[topic-anthropic-agent-guidance]], [[topic-llm-judge-and-adversarial-verification]], [[topic-multi-agent-failure-modes]]
