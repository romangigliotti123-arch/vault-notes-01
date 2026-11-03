---
tags: [manager-kb, source]
url: https://lilianweng.github.io/posts/2023-06-23-agent/
type: practitioner-blog (survey)
author: Lilian Weng
published: 2023-06-23
accessed: 2026-10-29
reliability: high for 2023-era diagnosis; dated for 2026 models
---
# LLM Powered Autonomous Agents (and why AutoGPT/BabyAGI-style loops stalled)
## Key claims
- Names AutoGPT, GPT-Engineer and BabyAGI as proof-of-concept demos of LLM-as-controller agents; decomposes agent = planning + memory + tool use.
- Three limits observed in these demos: (1) finite context length ("restricted context capacity limits the inclusion of historical information, detailed instructions, API call context, and responses"; vector retrieval is weaker than full attention); (2) long-term planning and decomposition: "LLMs struggle to adjust plans when faced with unexpected errors, making them less robust compared to humans who learn from trial and error"; (3) reliability of the natural-language interface: formatting errors and "rebellious behavior", so "much of the agent demo code focuses on parsing model output".
- Search-only context (unverified, secondary): AutoGPT-era failure stories centre on runaway loops and cost with no stop condition; fixes proposed by practitioners are loop limits, circuit breakers and human escalation. 2026 models fix much of (1)-(3) but the missing-budget/kill-switch problem persists (see OpenClaw cost reports).
## Quotable
> LLMs struggle to adjust plans when faced with unexpected errors, making them less robust compared to humans who learn from trial and error.

## Used by
[[topic-personal-assistant-agents]]
