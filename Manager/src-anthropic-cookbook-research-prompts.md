---
tags: [manager-kb, source]
url: https://github.com/anthropics/claude-cookbooks/tree/main/patterns/agents/prompts (research_lead_agent.md, research_subagent.md)
type: repo
author: Anthropic (claude-cookbooks)
published: undated (accompanies the 2025 multi-agent research system post)
accessed: 2026-10-29
reliability: high (first-party prompt text, read in full; designed for a web-research harness)
---
# Anthropic cookbook: research lead and research subagent prompts
Raw files fetched from raw.githubusercontent.com. They are the closest thing to an Anthropic-published reference brief pair (lead -> subagent).
## Key claims
- Lead prompt classifies the query first: depth-first (many perspectives on one issue), breadth-first (independent sub-questions), or straightforward; then plans accordingly. Default 3 subagents; guideline bands: simple 1, standard 2-3, medium 3-5, high 5-10 (max 20): "Prefer fewer, more capable subagents over many overly narrow ones. More subagents = more overhead."
- Delegation checklist (what every subagent brief must contain "as appropriate"): "Specific research objectives, ideally just 1 core objective per subagent"; "Expected output format"; "Relevant background context"; "Key questions to answer"; "Suggested starting points and sources... define what constitutes reliable information... and list any unreliable sources to avoid"; "Specific tools that the subagent should use"; "precise scope boundaries to prevent research drift". Good brief example is one dense paragraph naming sources, focus areas and the output ("compile your findings into a dense report of the facts... with specific timelines and quantitative data").
- Test for a plan: "Make sure that IF all the subagents followed their instructions very well, the results in aggregate would allow you to give an EXCELLENT answer".
- "Avoid overlap between subagents - every subagent should have distinct, clearly separate tasks." "In communicating with subagents, maintain extremely high information density while being concise."
- Lead keeps synthesis: "NEVER create a subagent to generate the final report - YOU write and craft this final research report yourself"; stop research at diminishing returns; adjust depth to time constraints.
- Lead does not do trivial work through subagents ("simple calculations, basic formatting, small web searches").
- Subagent prompt: pick a "research budget" (tool-call count) by difficulty (<5 simple, ~5 medium, ~10 hard, up to 15 very hard; hard cap 20 tool calls / ~100 sources); OODA loop; start with short broad queries (<5 words) then narrow; "NEVER repeatedly use the exact same queries"; return findings that are "detailed, condensed, complete, accurate".
- Source-quality discipline in the subagent: flag speculation ("could", "may"), aggregators, marketing language; "If unable to reconcile facts, include the conflicting information in your final task report for the lead researcher to resolve"; "flag these issues when returning your report ... rather than blindly presenting all results as established facts."
## Quotable
> "Make sure that IF all the subagents followed their instructions very well, the results in aggregate would allow you to give an EXCELLENT answer to the user's question"

## Used by
[[topic-brief-prompt-engineering]], [[topic-report-formats-and-verification]]
