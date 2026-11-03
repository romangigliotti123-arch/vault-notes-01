---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2508.21433
type: paper
author: JetBrains Research / TUM (Lindenbauer et al.)
published: 2025-08-29 (v3 NeurIPS 2025 workshop)
accessed: 2026-10-29
reliability: med-high (abstract read via arXiv API; SWE-agent on SWE-bench Verified only; blog post not opened)
---
# The Complexity Trap: Simple Observation Masking Is as Efficient as LLM Summarization for Agent Context Management
## Key claims
- Compared LLM summarisation vs simply omitting old observations (tool outputs) in SWE-agent on SWE-bench Verified, five model configs, initial generalisation to OpenHands: "a simple environment observation masking strategy halves cost relative to the raw agent while matching, and sometimes slightly exceeding, the solve rate of LLM summarization."
- Hybrid (masking + summarisation) cuts cost a further 7% vs masking alone and 11% vs summarisation alone.
- "Our findings raise concerns regarding the trend towards pure LLM summarization."
- Reading for us: the cheapest, safest context reduction is dropping old tool RESULTS (keep the actions/decisions); this is what a manager gets for free by delegating tool-heavy work to subagents. Summaries add their own cost and drift.
## Quotable
> "a simple environment observation masking strategy halves cost relative to the raw agent while matching, and sometimes slightly exceeding, the solve rate of LLM summarization"

## Used by
[[topic-context-window-management]]
