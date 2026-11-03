---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/costs.md
type: official-doc
author: Anthropic (Claude Code docs)
published: undated (references Claude Code v2.1.305-ish, Opus/Sonnet/Haiku 5.5)
accessed: 2026-10-29
reliability: high (primary vendor docs, fetched raw .md)
---
# Claude Code docs: Manage costs effectively
## Key claims
- Enterprise average "around $13 per developer per active day and $150-250 per developer per month", <$30/day for 90% of users (API-billing context; Roman is on a subscription).
- `/usage` on Pro/Max shows plan usage bars plus an **attribution** breakdown (skills, subagents, plugins, MCP servers as % of recent usage) and **recommendations** (rows with >=10% share, e.g. "Compact before you step away", "Switch from max to high effort", "Trim CLAUDE.md . 49k tokens per request"). Press `d`/`w` for 24h/7d. Figures are local-only (this machine). Press `f` to apply fixes, but NOT while Remote Control is connected ("Nothing was sent. Turn off Remote Control to use fixes.").
- `Prompt cache (main)` line in `/usage` (v2.1.251+): requests, % tokens from cache, misses, expected rebuilds, warm/cold + TTL. Statusline gets `prompt_cache` object. Main conversation only, not subagents.
- Subscription windows: "per-seat allowance that resets on a rolling five-hour window and a weekly window... shared with Claude chat and Cowork". "You've hit your session/weekly limit" is shared across all models: switching /model does not help (only model-family-specific "Opus limit"/"Sonnet limit" messages can be dodged by switching family).
- `autoContinueAtUsageLimit` (v2.1.234+) waits and continues after reset.
- "Why usage climbs in a long session": full conversation is sent with every request, re-read at cached rate ("a one-line question in a session that has been open all day still draws usage for the whole conversation"); cache misses after idle > TTL; **scheduled tasks fire while idle with full context**; **cross-session messages delivered as a new turn when idle (full context each time); set `crossSessionInbound` to `hold`**; goal check-ins (max 3 idle per goal; `CLAUDE_CODE_GOAL_CHECKIN_MINUTES=0` turns off); every subagent/workflow agent sends its own requests; teammates keep consuming; `/compact` reads the whole conversation (large request) while `/clear` costs nothing.
- Agent teams "approximately 7x more tokens than standard sessions" in plan mode.
- Reduce usage: `/clear` between tasks; custom compaction instructions via `/compact <focus>` or a "# Compact instructions" section in CLAUDE.md; Sonnet for most work, Opus only for complex architecture/multi-step reasoning, `model: haiku` for simple subagents; prefer CLI (`gh`) over MCP; hooks to pre-filter verbose output; move workflow-specific CLAUDE.md content into skills; "Aim to keep CLAUDE.md under 200 lines"; delegate verbose ops to subagents ("The subagent's own requests still draw on your usage").
- Thinking: tokens billed as output; cannot turn thinking off on Opus 5.5, Sonnet 5.5, Haiku 5.5, Fable; use effort. `MAX_THINKING_TOKENS` ignored by adaptive models.
- Background token use: summarization for --resume, /usage requests, prompt suggestions (reuse cache, skipped near limit) - "typically under $0.04 per session".
## Quotable
> "Claude Code sends your full conversation with every request... a one-line question in a session that has been open all day still draws usage for the whole conversation."
> "Aim to keep CLAUDE.md under 200 lines by including only essentials."

## Used by
[[topic-context-engineering]], [[topic-context-window-management]], [[topic-model-effort-routing-cost]]
