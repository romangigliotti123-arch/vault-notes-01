---
tags: [manager-kb, source]
url: https://www.anthropic.com/research/april-23-postmortem
type: eng-blog
author: Anthropic
published: 2026-04-23
accessed: 2026-10-29
reliability: high (primary postmortem)
---
# An update on recent Claude Code quality reports
## Key claims
- Three product-layer changes (not the model) degraded Claude Code/Agent SDK/Cowork: (1) default effort `high` -> `medium` (Mar 4-Apr 7; "the wrong tradeoff"); (2) a context-clearing bug meant to clear stale reasoning once after an hour idle instead cleared it every turn (Mar 26-Apr 10): agent seemed forgetful and repetitive, cache misses drained limits; (3) a verbosity word-limit system prompt (Apr 16-20) cost ~3% on coding evals for Opus 4.6/4.7 in a later ablation.
- Detection failed because each change hit a different traffic slice; internal evals and dogfooding (pre-release builds) did not reproduce; code review missed the bug. Fixes: more staff on public build, per-model evals + line-by-line ablation of every system prompt change, model-specific changes gated to the target model, soak periods and gradual rollout for anything that could trade off intelligence.
- Implication for any harness owner: harness/prompt edits (effort defaults, context trimming, brevity limits) silently change quality; ablate and soak them.
## Quotable
> "For any change that could trade off against intelligence, we'll add soak periods."

## Used by
[[topic-anthropic-agent-guidance]], [[topic-context-engineering]]
