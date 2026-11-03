---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2506.08837
type: paper
author: Beurer-Kellner, Buesser, Cretu, Debenedetti, Dobos, Fabian, Fischer, Froelicher, Grosse, Naeff, Ozoani, Paverd, Tramer, Volhejn
published: 2025-06-10 (v1; v3 2025-06-27)
accessed: 2026-10-29
reliability: high (academic, multi-vendor authors)
---
# Design Patterns for Securing LLM Agents against Prompt Injections
## Key claims
- NOTE: the assignment brief cited arXiv 2506.08226; that ID is an unrelated PDE paper ("Mondrian"). The correct ID is 2506.08837.
- Proposes "principled design patterns for building AI agents with provable resistance to prompt injection" and analyses their utility/security trade-offs with case studies.
- Pattern names (from Willison's summary [[src-willison-design-patterns-post]]; the arXiv abstract page lists no names): Action-Selector, Plan-Then-Execute, LLM Map-Reduce, Dual LLM, Code-Then-Execute, Context-Minimization.
- Authors accept that restricting agents from arbitrary tasks is the price of provable safety; they doubt general-purpose agents can offer reliable guarantees with current models (per Willison).
- Only the abstract page was opened (not the full PDF).
## Quotable
> propose a set of principled design patterns for building AI agents with provable resistance to prompt injection

## Used by
[[topic-agent-security]]
