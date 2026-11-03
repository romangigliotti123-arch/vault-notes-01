---
tags: [manager-kb, source]
url: https://blog.langchain.com/how-and-when-to-build-multi-agent-systems/
type: eng-blog
author: Harrison Chase (LangChain)
published: 2025-06-16
accessed: 2026-10-29
reliability: med (framework vendor with an agenda, but a fair synthesis; opened in full)
---
# How and when to build multi-agent systems
## Key claims
- Written days after Cognition "Don't Build Multi-Agents" (2025-06-12) and Anthropic's research-system post (2025-06-13); argues the two "have a lot in common": context engineering is the crux.
- "Multi-agent systems that primarily 'read' are easier than those that 'write'": reads parallelise; parallel writes need context passing plus coherent merging, and "conflicting write actions typically produce far worse outcomes than conflicting read actions".
- Anthropic's Research keeps the final report write in one agent, one call: the multi-agent part is the reading half.
- Reliability needs durable execution (resume, do not restart), tracing and evals; these apply to any long-running agent, not only multi-agent ones.
- Pitches LangGraph as "no hidden prompts, no enforced cognitive architectures" so the developer controls exactly what context each LLM call sees.
## Quotable
> Multi-agent systems designed primarily for "reading" tasks tend to be more manageable than those focused on "writing" tasks.

## Used by
[[topic-multi-agent-frameworks]], [[topic-orchestration-patterns]]
