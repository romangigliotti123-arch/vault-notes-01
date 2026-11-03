---
tags: [manager-kb, source]
url: https://hamel.dev/blog/posts/field-guide/
type: practitioner-blog
author: Hamel Husain
published: 2025-03-24
accessed: 2026-10-29
reliability: med-high (widely cited practitioner; not benchmarked)
---
# A Field Guide to Rapidly Improving AI Products
## Key claims
- Error analysis of real traces is "the highest-ROI activity"; bottom-up: write open notes on bad behaviour, have an LLM group notes into a failure-mode taxonomy, label traces, count frequencies (his example: three issues > 60% of problems).
- Avoid generic top-down metrics (hallucination, toxicity score); they miss domain failures and give false confidence. Use binary pass/fail + written critique.
- Page says "dozens of conversations"; it does not give a ~100 trace rule or name open/axial coding.
## Quotable
> The more effective bottom-up approach forces you to look at actual data and let metrics naturally emerge.

## Used by
[[topic-long-running-always-on-agents]], [[topic-observability]]
