---
name: economy-health-monitor
description: "Track a live game's currency sources, sinks and wallet balance over time and flag drift: sink ratio, daily net trend, top sources and sinks, using kit Analytics economy events and a drift script. Use weekly in live ops, after any reward or event change, or when prices feel off."
category: liveops
tags: economy, sources, sinks, inflation, drift, currency, wallet, analytics, economy events, live ops
kb: Roblox/roblox-kb/analytics-metrics.md, Roblox/roblox-kb/updates-live-ops.md, Roblox/roblox-kb/monetisation-other.md, Roblox/roblox-kb/events-and-seasonal-content.md, Roblox/roblox-kb/anti-exploit-and-security.md
related: economy-balancer, sink-source-mapper, event-planner, live-balance-tuner, metrics-snapshot-logger, dupe-exploit-hunter, rbx-weekly
---

# economy-health-monitor

`economy-balancer` models an economy before launch from assumed rates; `sink-source-mapper` lists the sources and sinks in code. This skill measures the LIVE economy. Vault rule: track every currency source, sink and purchase; a constantly growing currency means too few sinks; wallet spikes mean too few sink options.

## When to use
Weekly live ops, after an event or reward change, when players say prices are meaningless or the game feels starved. Not for: pre-launch design (`economy-balancer`), dupe hunting (`dupe-exploit-hunter`), or pricing real-money items (`price-ladder-planner`).

## Inputs (max 3)
1. Daily totals per currency by kind (source or sink) and reason, from Creator Hub economy analytics or your own counters. 2. Which currency (default: the soft currency). 3. Recent changes (events, new sinks, reward edits) with dates.

## Procedure
1. Make sure the data exists: the kit `Analytics` system logs `LogEconomyEvent` from the server on every grant and spend, with a reason (item or sink name) and low-cardinality fields. If not, add it first (server only, after success; `funnel-analyzer` step 2 rules apply).
2. Export or paste daily totals as `econ.csv`: `date,currency,kind,amount,reason`. Exclude known exploiters and players inactive for 15-30 days before counting if you can (vault).
3. Run `python -I ~/.claude/claude-kit/skillpack/liveops/economy-health-monitor/scripts/econ_drift.py --csv econ.csv --currency Coins --window 7`. It prints sink ratio (sinks over sources), the net-per-day trend, cumulative change, top sources and top sinks, and a verdict: INFLATING (ratio under 0.6), DRAINING (over 1.1), DRIFTING UP/DOWN (net trend over 5 percent of daily sources per day) or BALANCED. These thresholds are this skill's defaults; tune them against `economy-balancer`.
4. Explain the verdict with the top reasons. A single dominant source after an event is a rate to cut; a dominant sink may be one item everyone buys.
5. Cross-check for exploits: a source reason that grows far faster than players does (`exploit-audit`, `dupe-exploit-hunter`).
6. Pick one lever: add a sink, cap a resource or inventory, add a daily cap, scale conversion cost with level, or use a separate event currency (vault). Apply it through a bounded live change (`live-balance-tuner`) and re-run in a week.
7. Add the sink ratio to the weekly numbers (`metrics-snapshot-logger`), plus the share of players who can afford the next item (from your own data).
8. Never "fix" inflation by silently changing odds or prices near an event end; announce balance changes in the patch notes.

## Studio MCP path
`script_grep` for `Economy(` / `LogEconomyEvent` to list logged flows -> `script_read` the reward and shop modules -> `multi_edit` to add missing source/sink logs. Counts themselves come from Creator Hub, not Studio.

## Fallback
Paste daily totals into the CSV; Python 3 only. Without economy events logged, say so and treat the output as nothing.

## Evidence
`Roblox/roblox-kb/analytics-metrics.md`: track the economy (sources, sinks, wallet balance); build custom monetisation tracking; filter exploiters and long-inactive players; custom calculated metrics such as sources minus sinks. `updates-live-ops.md`: balance and economy changes (buff underused items instead of nerfing popular ones; act on economy-threatening features even if players object); events with separate currencies (`events-and-seasonal-content.md`). Kit `systems/Analytics/README.md` for the economy event shape.

## Output
```
ECONOMY <currency> last 7 days
sources N, sinks N, sink ratio x.xx, trend ..., verdict ...
Top sources / sinks (by reason)
Cause hypothesis, one lever, expected effect, re-check date
```

## Acceptance checks
- [ ] `econ_drift.py --selftest` prints "selftest ok (6 checks)".
- [ ] Verdict, window and thresholds are stated with the note that thresholds are defaults.
- [ ] At least 3 days of data; exploit suspects and inactive accounts addressed or flagged.
- [ ] One lever with a re-check date, not several.
- [ ] Any resulting number change goes through bounds and a patch-note line.

## Pitfalls
Reading a cumulative change as an absolute wallet. Counting one-off event grants as a baseline. Summing across currencies. Ignoring a source that is an exploit. Fixing the symptom (more sinks) while a dupe feeds sources.

## Related
`economy-balancer`, `sink-source-mapper`, `event-planner`, `live-balance-tuner`, `metrics-snapshot-logger`.
