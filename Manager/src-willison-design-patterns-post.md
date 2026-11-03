---
tags: [manager-kb, source]
url: https://simonwillison.net/2025/Jun/13/prompt-injection-design-patterns/
type: practitioner-blog
author: Simon Willison
published: 2025-06-13
accessed: 2026-10-29
reliability: high
---
# Willison on "Design Patterns for Securing LLM Agents" (the six patterns)
## Key claims
- Action-Selector: agent triggers tools but never sees their output, so results cannot steer it.
- Plan-Then-Execute: the sequence of tool calls is fixed up front; injected content can change data passed along but not which actions run.
- LLM Map-Reduce: sub-agents each process one untrusted item and return a narrow answer (e.g. boolean), combined afterwards.
- Dual LLM: privileged model directs a quarantined model that reads untrusted text and returns symbolic variables, not raw content.
- Code-Then-Execute: privileged model writes code in a sandboxed DSL that specifies tool calls and data flow so taint can be tracked.
- Context-Minimization: drop unneeded content (e.g. the original user prompt) once no longer required. Willison admits being "slightly confused" by this one.
- Trade-off: patterns cut utility (e.g. SWE case study sees only formal API descriptions). Any exposure to malicious input taints the whole output.
## Quotable
> We don’t have a magic solution to prompt injection

## Used by
[[topic-agent-security]]
