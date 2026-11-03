---
tags: [manager-kb, source]
url: https://docs.langchain.com/oss/python/langchain/multi-agent.md
type: official-doc
author: LangChain
published: undated (current docs, fetched 2026-10-29)
accessed: 2026-10-29
reliability: med-high (vendor docs; numbers are for a toy "buy coffee" / language-comparison example, illustrative not benchmarked)
---
# LangChain docs: Multi-agent patterns
## Key claims
- Patterns and fit table: Subagents (main agent coordinates subagents as tools; all routing passes through it; best for parallelisation + distributed development, poor for direct user interaction), Handoffs (state-driven agent switching; best for multi-hop + direct user interaction, no parallelism), Skills (single agent loads specialised prompts on demand), Router (classifier directs to specialists, results synthesised), Custom workflow (LangGraph). "You can mix patterns."
- One-shot request: Subagents 4 model calls vs 3 for Handoffs / Skills / Router - "results flow back through the main agent—this overhead provides centralized control."
- Repeat request (turn 2): stateful Handoffs and Skills need 2 calls (5 total) vs Subagents 4 (8 total): "Stateful patterns (Handoffs, Skills) save 40-50% of calls on repeat requests. Subagents maintain consistent cost per request".
- Multi-domain compare (3 languages x ~2000 tokens docs): Subagents 5 calls ~9K tokens, Router 5 calls ~9K, Handoffs 7+ calls ~14K+ (sequential), Skills 3 calls ~15K (accumulated context). "Subagents processes 67% fewer tokens overall due to context isolation."
- So the trade: subagents buy context isolation and parallelism at one extra hop per request; skills buy fewer calls but pay re-reading loaded context every turn.

## Used by
[[topic-multi-agent-frameworks]], [[topic-orchestration-patterns]]
