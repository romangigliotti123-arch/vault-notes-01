---
tags: [manager-kb, source]
url: file:///~/.claude/projects/C--Windows-system32/78968f1c-7f98-4d3e-a2f7-b4e068a165e5.jsonl (+ subagents/ folder)
type: repo (local measurement of our own master transcript)
author: D1 worker (parsed `message.usage` with a short Python script, read-only; de-duplicated by message id)
published: measured 2026-10-29 ~08:25 AEDT; covers 2026-10-28 23:16 AEDT onward (master transcript 6.6 MB, 31 subagent transcripts, still growing as other research workers run)
accessed: 2026-10-29
reliability: high for token counts (API-reported usage, one record kept per message id); costs are API LIST-PRICE equivalents (5-minute cache-write rate), NOT what the subscription meters
---
# Measured usage of the current master session and its workers
Method note: the transcript writes one JSON record per content block of an assistant message, each repeating the same `usage`; summing records over-counts (about 1.8x for the master, 2.3x for subagents). All numbers below keep ONE record per `message.id`.
## Key claims
- Master (main thread, 128 unique assistant messages): Opus 5.5 88 msgs, Sonnet 5.5 24, Haiku 5.5 16. Cache read 18.5M, cache write 0.82M, output 0.12M (of which thinking ~40k). List-equivalent cost about $7.7 (Opus $6.8, Sonnet $0.9, Haiku $0.05).
- Subagents (31 workers, all `sonnet-worker`, Sonnet 5.5, 1,707 messages): cache read 325.6M, cache write 15.1M, output 1.94M (thinking 0.56M = 29%). List-equivalent about $89.7 (read $32.6, write $37.7, output $19.4). **Workers = 95% of all tokens and ~11.6x the master's list cost.** The Opus master is not the cost problem; worker turns x worker context is.
- Per worker: turns p50 42, p75 81, p90 105, max 171 (mean 55). Median first-turn context 52,332 tokens (min 26k, max 54k): the fixed baseline is ~26% of all worker cache-read volume. Peak context median 186k, max 574k. Cost per worker: median $1.92; top worker $23.5 (171 turns, 383k context) and the top 5 = $43 (48% of subagent cost): a heavy tail.
- Cache hit share (read / (read + write)): master 95.8%, workers 95.6%. Workers' cache WRITES cost more than their reads at list rates ($37.7 vs $32.6) because each added token is written once at 1.25x and re-read every later turn.
- Master context: first turn after (re)boot 70,320 tokens (fixed overhead ~68-70k even though the transcript is long). Grew to 247-260k in ~3 h, then **auto compaction at 2026-10-28T16:14Z: preTokens 260,474 -> postTokens 21,920, durationMs 67,734** (trigger "auto" although window is 700k-967k: consistent with idle compaction: >=200k tokens and ~1 h idle on the 1 h TTL). Back to ~147k by 21:03Z.
- 6 model switches in the first 40 minutes (haiku<->sonnet<->opus): cache writes of 75,119 / 49,105 / 68 / 9,773 / 109,465 / 155,314 tokens at the switches. Two idle gaps (174 min, 88 min) each forced a 52,483 / 69,184-token cache re-write on the next turn.
- Where master context comes from (chars/4 token estimate): tool results ~40k tokens total (PowerShell 25.7k, Agent 7.5k, Read 4.6k, SendMessage 1k); worker completion notices: 16 plain `<task-notification>` (~27k tokens) + 16 wrapped in a `[SYSTEM NOTIFICATION]` reminder (~29k) = 32 separate reports; CLAUDE.md injected three times (31,234 + 27,861 + 27,293 chars); the compaction summary message 24,220 chars; tool_use inputs (briefs, commands) ~218k chars.
- `claude auth status`: subscriptionType `max`.
- boot-claude.ps1 starts the master with `--model haiku`; the transcript shows the session driven by Opus 5.5 after manual switches.

## Used by
[[topic-context-window-management]], [[topic-model-effort-routing-cost]], [[topic-personal-assistant-agents]]
