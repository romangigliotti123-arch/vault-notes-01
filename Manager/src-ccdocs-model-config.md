---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/model-config.md
type: official-doc
author: Anthropic (Claude Code docs)
published: undated (covers Claude Code ~2.1.311, Opus/Sonnet/Haiku 5.5, Fable 5.1)
accessed: 2026-10-29
reliability: high (primary vendor docs, fetched raw .md)
---
# Claude Code docs: Model configuration (aliases, effort, fallback, auto-compact window)
## Key claims
- Aliases on Anthropic API: `opus`=Opus 5.5, `sonnet`=Sonnet 5.5, `haiku`=Haiku 5.5; `fable`/`best`; `opusplan` = opus in plan mode, sonnet for execution (each toggle is a model switch = cache miss).
- Effort levels (Opus 5.5, Sonnet 5.5, Haiku 5.5, Opus 5/4.8/4.7, Fable): low, medium, high, xhigh, max. **Default effort is `medium` for Opus 5.5, Sonnet 5.5, Haiku 5.5**; `high` on most older; Opus 4.7 `xhigh`. Resolution order: env `CLAUDE_CODE_EFFORT_LEVEL` / `--effort` / `/effort` > settings (`modelSettings.<model>.effortLevel`, `effortLevel`) > model default. Skill/subagent frontmatter `effort` overrides session level but NOT the env var. A top-level `effortLevel` in user settings does not count for Opus 5.5; use per-model `modelSettings`.
- Level guidance table: low = quick exchanges/small change; medium = day-to-day engineering with clear scope; high = verification matters/edge cases (bug fix in existing codebase); xhigh = deeper reasoning, higher token spend; max = "hard problems you want Claude to work through without you... `max` may show diminishing returns and is prone to overthinking, so test before adopting it broadly". "The effort scale is calibrated per model". "Opus 5.5 at medium matches or exceeds Opus 5 at high on coding and knowledge-work evaluations... start at medium rather than carrying over the level you used on Opus 5."
- `max` applies to the current session only unless set via env var. Phone/browser effort control through Remote Control applies to that session only.
- `ultrathink` keyword: one-turn deeper reasoning (raises turn to xhigh when typed in terminal, v2.1.311+). "think", "think hard" are NOT keywords. `ultracode` = workflow orchestration toggle, not an effort level.
- Thinking cannot be turned off on Opus 5.5/Sonnet 5.5/Haiku 5.5/Fable. Fable/Sonnet 5+/Haiku 5.5/Opus 4.7+ always adaptive.
- 1M context is native for Fable, Sonnet 5+, Haiku 5.5, Opus 4.7+. "Models running with a native 1M window compact before the window fills, at about 967K tokens by default." Set earlier with `/autocompact 500k`, `autoCompactWindow`, `modelSettings.<model>.autoCompactWindow`, `--autocompact`, env `CLAUDE_CODE_AUTO_COMPACT_WINDOW` (100k-1M). `CLAUDE_CODE_DISABLE_1M_CONTEXT=1` forces 200K.
- **Haiku 5.5**: 1M window; "A Haiku 5.5 request costs more per token when its prompt is longer than 100K tokens." Auto-compacts ~967K by default.
- **Fallback chains**: `--fallback-model sonnet,haiku` / `fallbackModel` array, max 3. Triggers: overloaded/unavailable/non-retryable server error. Does NOT trigger on auth, billing, rate-limit, request-size, transport errors. Switch lasts for the current turn only; also applies to subagents (v2.1.247+); compaction won't fall back to a smaller-context model. Separate safety-classifier "automatic model fallback" (Opus 5.5 -> Opus 4.8 for cyber etc.; `switchModelsOnFlag`).
- Org-level `maxEffortLevel` / effort caps exist.
## Quotable
> "`max` may show diminishing returns and is prone to overthinking, so test before adopting it broadly."
> "Models running with a native 1M window compact before the window fills, at about 967K tokens by default."

## Used by
[[topic-context-window-management]], [[topic-model-effort-routing-cost]]
