---
tags: [manager-kb, source]
url: https://www.zivtech.com/blog/economics-of-claude-code-cost-driver-reference
type: practitioner-blog
author: Alex Urevick-Ackelsberg (Zivtech); co-written with Claude
published: 2026-04-22 (June 2026 update)
accessed: 2026-10-29
reliability: low-med (rules of thumb from list-price arithmetic, no measured dataset; Opus 4.6 prices)
---
# The Economics of Claude Code: Cost Driver Reference
## Key claims
- Ranked cost drivers: front-loaded context (system prompt, CLAUDE.md), cache lifespan (5-minute rule), context accumulation, message churn, agent spawning, model tier, clarifying questions, blocking tool calls, aborted responses, output length.
- "a cache miss costs 12.5x the cost of the same message with a warm cache" (Opus 4.6 list: write 1.25x vs read 0.1x).
- Author thresholds (judgment, not measured): cache hit rate "comfortably above 80%", below 40% on longer sessions is a red flag; output share >=20% of tokens on routine coding is a flag; Opus "usually less than a third of spend".
- "Consider a handoff past 30-40 turns or 100K+ tokens of accumulated context"; "For long gaps ... starting fresh is almost always the right call"; keep project instructions "in the low single-digit thousands of tokens"; "Three parallel agents mean four separate caches". June 2026 update: oversized tool output now auto-persists to a file, so that driver softened.
- Flag: the article itself states it reports no controlled experiments or session dataset.
## Quotable
> "For long gaps (lunch, meetings, end of day), starting fresh is almost always the right call."

## Used by
[[topic-context-window-management]], [[topic-model-effort-routing-cost]]
