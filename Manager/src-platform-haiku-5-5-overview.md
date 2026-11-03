---
tags: [manager-kb, source]
url: https://platform.claude.com/docs/en/models/haiku-5-5/overview.md
type: official-doc
author: Anthropic (Claude Platform docs)
published: 2026-10-07 (release date stated)
accessed: 2026-10-29
reliability: high (raw .md)
---
# Claude Haiku 5.5 overview
## Key claims
- "Released October 7, 2026." "built for high-volume, latency-sensitive work such as classification, routing, extraction, and subagent tasks"; 1M context, 128K max output, from $0.10 / $0.50 per MTok; fastest model; adaptive thinking, default effort `medium`.
- New tokenizer: "the same text counts as approximately 30 percent more tokens than on Claude Haiku 4.5."
- Comparison table: Fable 5.1 $10/$50 (default high), Opus 5.5 $4/$20 (default medium, moderate latency), Sonnet 5.5 $2/$10 (default high on API, fast), Haiku 5.5 from $0.10/$0.50 (default medium, fastest). Batch API is 50% off; cache reads 10% of base (5% on Opus 5.5 and Sonnet 5.5).
- Docs position Haiku as router/subagent/extractor, not as the long-horizon coordinator; the long-horizon manager role with Haiku is paired in Anthropic material with an Opus advisor ([[src-ccdocs-advisor]]).

## Used by
[[topic-model-effort-routing-cost]]
