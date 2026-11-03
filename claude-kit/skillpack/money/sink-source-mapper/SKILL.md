---
name: sink-source-mapper
description: "Map every currency source and sink in a game's code, log them through one server-side ledger, and read the report for inflation, a dominating source, or missing sinks. Use when you suspect inflation or after launch to compare real flows with the model; building the model is economy-balancer."
category: money
tags: economy, ledger, sources, sinks, inflation, currency flow, audit, analytics events, source sink map
kb: Roblox/roblox-kb/core-loops-and-game-design.md, Roblox/roblox-kb/analytics-metrics.md, Roblox/roblox-kb/monetisation-other.md, Roblox/roblox-kb/anti-exploit-and-security.md, Roblox/roblox-kb/data-persistence.md
related: economy-balancer, devproduct-handler, exploit-audit, datastore-schema-builder, shop-conversion-optimizer, retention-diagnoser
---

# sink-source-mapper

One job: find every place the currency changes and show the totals. Two parts: a one-time code map (search the project for each balance change) and a running `Ledger` (`scripts/Ledger.luau`) that records source and sink amounts with a name. Its report flags a low sink/source ratio, one source dominating income, no sinks at all, and sinks that exceed sources. The kit `Analytics` system already sends economy events with Source/Sink flows to the dashboard; the ledger gives you the same totals inside your own tools and tests.

## When to use
Suspected inflation or deflation, after adding a source, before an economy patch, or an audit after exploit reports. Not for: building the target numbers (`economy-balancer`), exploit hunting in remotes (`exploit-audit`).

## Inputs (max 2)
1. The currency names in the game (default: read the PlayerData template and shop). 2. A window of logged data if it exists (default: none; run the map and ledger first).

## Procedure
1. Read the rules: `python -I ~/.claude/claude-kit/tools/kbq.py section core-loops-and-game-design rules --max-chars 4000` ("Balance the economy with sources, sinks and caps").
2. Map in code: search every write to a balance (`coins +=`, `Currency:Add`, `Shop` grants, quest rewards, daily rewards, offline earnings, refunds, admin commands) and every spend. Write a table: name, kind (source/sink), file and function, capped (yes/no), server-only (must be yes).
3. Route all changes through ONE function per currency (`Grant(player, name, amount)` and `Spend(player, name, amount)`) that updates the balance, calls `Ledger.record(ledger, "source"|"sink", name, amount)` and, with the Analytics system, `Analytics:Economy(...)`. If a change bypasses it, that is a finding.
4. Keep names stable and few (the Analytics system caps transaction types and SKUs per experience; see its README): `quest_reward`, not `quest_reward_<id>`.
5. Run the report over a play session or a log: `Ledger.report(ledger)`; read `flags`. A ratio under 0.6 or a source above 60% of income are the defaults (tunable); both are heuristics, not platform rules.
6. Compare with the model from `economy-balancer`: where reality differs by more than the model's uncertainty, fix the assumption or the code.
7. Check refunds: a source that grants after a purchase is reversed (or a sink that refunds) must be recorded as its own named flow, otherwise totals drift.
8. Save the map in `design/economy-map.md`. Test: `lune run ../skillpack/money/sink-source-mapper/scripts/tests/Ledger.test.luau` from `~/.claude/claude-kit/systems`.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `multi_edit` to install the Grant/Spend wrappers -> `start_stop_play` -> `execute_luau` (Server) to simulate a session of grants and spends and print `Ledger.report` -> `get_console_output`. Live economy data from real players needs a published place and the dashboard: `untested`.

## Fallback
Files plus Lune and search commands (headless). Real-player totals stay `untested` until data exists.

## Evidence
`Roblox/roblox-kb/core-loops-and-game-design.md` (sources, sinks, caps), `Roblox/roblox-kb/analytics-metrics.md` (source/sink flow events; consistent names), `Roblox/roblox-kb/monetisation-other.md` (event currency; track wallets for sink-back), `Roblox/roblox-kb/anti-exploit-and-security.md` (server authority for grants), `Roblox/roblox-kb/data-persistence.md` (session locking prevents duplication). The report thresholds are this skill's defaults.

## Output
`design/economy-map.md`: the source and sink table, a ledger report from a real or simulated session, findings with fixes.

## Acceptance checks
- [ ] Every balance write found by search appears in the table (list the search commands used).
- [ ] No balance change happens outside Grant/Spend (search returns none).
- [ ] `Ledger.report` output is quoted, including `flags`.
- [ ] `lune run` Ledger tests pass (quote "5 passed, 0 failed") and luau-check is clean.
- [ ] Names are stable (no per-id names).

## Pitfalls
Recording only sources. Per-item names that blow the analytics cap. Forgetting offline earnings, refunds and admin grants. Logging on the client. Reading a one-hour session as the economy.

## Related
`economy-balancer`, `devproduct-handler`, `exploit-audit`, `datastore-schema-builder`, `shop-conversion-optimizer`.
