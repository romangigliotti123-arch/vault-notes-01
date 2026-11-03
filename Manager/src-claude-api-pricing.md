---
tags: [manager-kb, source]
url: https://platform.claude.com/docs/en/about-claude/pricing.md
type: official-doc
author: Anthropic (Claude Platform docs)
published: undated (lists Fable 5.1, Opus 5.5, Sonnet 5.5, Haiku 5.5)
accessed: 2026-10-29
reliability: high (official price table; API list prices, NOT subscription weights)
---
# Claude pricing (API list prices, raw .md)
## Key claims
- Per MTok (input / 5m write / 1h write / cache hit / output): Fable 5.1 $10 / 12.50 / 20 / 0.25 / $50; **Opus 5.5 $4 / 5 / 8 / 0.20 / $20**; **Sonnet 5.5 $2 / 2.50 / 4 / 0.10 / $10**; **Haiku 5.5 (prompt <=100k) $0.10 / 0.125 / 0.20 / 0.01 / $0.50; (prompt >100k) $0.50 / 0.625 / 1 / 0.05 / $2.50**; Opus 5/4.8/4.7/4.6 $5/6.25/10/0.50/$25; Haiku 4.5 $1/1.25/2/0.10/$5.
- Cache multipliers: 5-min write 1.25x, 1-hour write 2x, read 0.1x base (0.05x on Opus 5.5 and Sonnet 5.5; 0.025x on Fable 5.1). "caching pays off after one cache read for the 5-minute duration (1.25x write), or after two cache reads for the 1-hour duration (2x write)". Multipliers stack with Batch discount and data residency.
- Long context: Claude 4.6+ models (except Haiku 5.5) include full 1M at standard price. **Haiku 5.5 is priced by prompt length: a request over 100,000 prompt tokens pays higher prices (5x input, 5x output); prompt length counts cache reads and writes; a request over the threshold pays the higher price even when part of its prompt is a cache hit.**
- Derived (arithmetic from the table, not stated by Anthropic): Opus 5.5 is 2x Sonnet 5.5 and 40x Haiku 5.5 (<=100k) on input and output. Haiku 5.5 above 100k is still 4x cheaper than Sonnet 5.5 on input and 5x cheaper on output.
## Quotable
> "a request over the threshold pays the higher prices even when part of its prompt is a cache hit"

## Used by
[[topic-model-effort-routing-cost]]
