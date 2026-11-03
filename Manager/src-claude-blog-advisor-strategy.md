---
tags: [manager-kb, source]
url: https://claude.com/blog/the-advisor-strategy
type: eng-blog
author: Anthropic
published: undated (benchmarks use Sonnet 4.6 / Haiku 4.5 / Opus 4.6)
accessed: 2026-10-29
reliability: med-high (vendor benchmarks, older models, footnoted prompt differences)
---
# The advisor strategy
## Key claims
- "pair Opus as an advisor with Sonnet or Haiku as an executor"; executor runs end-to-end, consults Opus when stuck; "The advisor never calls tools or produces user-facing output".
- SWE-bench Multilingual: Sonnet+Opus advisor "+2.7 percentage point" and "reducing cost per agentic task by 11.9%" vs Sonnet solo.
- BrowseComp: Haiku + Opus advisor 41.2% vs Haiku solo 19.7%. "Haiku with an Opus advisor trails Sonnet solo by 29% in score but costs 85% less per task."
- Advisor output is short: "typically 400-700 text tokens".
- "The advisor adds cost relative to Haiku alone." Recommended test: Sonnet solo vs Sonnet+Opus advisor vs Opus solo. Footnotes: prompt/thinking setup differed between runs (so treat deltas as indicative).
## Quotable
> "Haiku with an Opus advisor trails Sonnet solo by 29% in score but costs 85% less per task."

## Used by
[[topic-anthropic-agent-guidance]], [[topic-model-effort-routing-cost]]
