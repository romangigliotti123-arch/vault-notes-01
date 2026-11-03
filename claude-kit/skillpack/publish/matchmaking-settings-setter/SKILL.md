---
name: matchmaking-settings-setter
description: "Plan and validate the matchmaking configuration for an experience (attributes read from DataStores, signals, aggregations, weights) before it is entered in Creator Hub, so the first live config cannot silently do nothing or the wrong thing. Use when a game has skill, region, mode or party preferences for which server a player joins."
category: publish
tags: matchmaking, signals, attributes, aggregation, weights, servers, skill matching, creator hub, settings
kb: Roblox/roblox-kb/matchmaking-and-teleport.md, Roblox/roblox-kb/data-persistence.md, Roblox/roblox-kb/ab-testing-and-experiments.md, Roblox/roblox-kb/social-features-and-virality.md
related: private-server-settings-setter, experience-settings-configurator, datastore-schema-builder, ping-sensitivity-tester, post-launch-monitor, publish-readiness-gate
---

# matchmaking-settings-setter

One job: a matchmaking config that is consistent on paper before it reaches live places. The product (attribute sources, signal names, aggregations, preview tools) changes, so the live Creator Docs pages are read first and the script's rules can be overridden; the script only checks internal consistency: signals reference defined attributes, aggregation fits the attribute type, data-store attributes use the exact `{UserId}` token and a value path, weights are usable. Whether a config improves play is measured with the matchmaking analytics and an experiment, not by this check.

## When to use
When players should land with similar-skill, same-mode or same-language players, before publishing the first config, and when changing weights. Not for: private/reserved server rules (`private-server-settings-setter`), writing the skill-rating system itself (`datastore-schema-builder`, rating logic), latency tuning (`ping-sensitivity-tester`).

## Inputs (max 2)
1. What should be matched (skill, mode, language, party size; default: start with platform default signals only). 2. Where the attribute data lives (DataStore name and key shape).

## Procedure
1. Open the live matchmaking pages (Evidence): glossary, attributes and signals, scoring, customize, analytics. Copy the current names of aggregations and any limits into the notes with the date.
2. Start from the defaults: change only default signal weights first; add custom attributes and signals only for a stated problem (the vault says this is the simplest configuration and the first thing to try).
3. Write the config: `python -I ~/.claude/claude-kit/skillpack/publish/matchmaking-settings-setter/scripts/mm_config_check.py --template > release/matchmaking.json` and fill it. Attributes come before the signals that use them; data-store keys use the exact case-sensitive id token.
4. Choose the aggregation by intent: average/median to match the server's typical player, sum for a total, cluster to group the same categorical value (mode), diversify to mix values. If the live page names differ, set `aggregations` in the JSON.
5. Run `python -I .../mm_config_check.py release/matchmaking.json`; fix every FAIL (undefined attribute, wrong aggregation for the type, zero weights).
6. In Creator Hub, use Preview and Test (mock servers; hover signal scores to see the formula) before applying to live places. Record the winner of each test case. This stays `untested` here.
7. Plan the measurement: baseline from the matchmaking analytics page, one change at a time, a rollback config, and a check after 24-72 hours (`post-launch-monitor`).
8. Write `release/matchmaking.md` with the JSON, script output, test cases, rollback plan and page dates.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `script_grep` (`GetDataStore` key shapes for the attribute data) -> `execute_luau` (Server, test universe only) to confirm the key and value path return the expected JSON -> `get_console_output`. Matchmaking itself runs on live servers and cannot be exercised from a Studio session.

## Fallback
The consistency check and the plan need no Studio. Preview/Test results and live behaviour are `untested` until the owner runs them in Creator Hub.

## Evidence
Official (live-check): `Roblox/docs/Videos/2026-10-28 - Docs matchmaking customize-matchmaking.md` (start with default signals and weights, attributes before signals, Preview and Test, aggregation choices, DataStore attribute with `{UserId}` key template, value path, scope), `... Docs matchmaking attributes-and-signals.md`, `... Docs matchmaking scoring.md`, `... Docs matchmaking analytics.md`, `... Docs matchmaking glossary.md`. Pack: `Roblox/roblox-kb/matchmaking-and-teleport.md`.

## Output
`release/matchmaking.json`, `release/matchmaking.md`.

## Acceptance checks
- [ ] `mm_config_check.py release/matchmaking.json` exits 0 (quote the OK line).
- [ ] The first config changes defaults only, or the reason for each custom signal is written.
- [ ] A rollback config and a measurement plan exist.
- [ ] Preview/Test was run or is marked `untested`.
- [ ] `mm_config_check.py --selftest` prints `selftest ok`.

## Pitfalls
Many custom signals at once (impossible to attribute a result). Weights that all point at skill so servers never fill. Attribute data that is missing for new players (decide the default). Reading the config change as success without the analytics baseline.

## Related
`private-server-settings-setter`, `experience-settings-configurator`, `datastore-schema-builder`, `ping-sensitivity-tester`, `post-launch-monitor`.
