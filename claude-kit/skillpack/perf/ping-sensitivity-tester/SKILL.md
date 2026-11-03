---
name: ping-sensitivity-tester
description: "Test how gameplay behaves under added latency: step Studio's incoming replication lag through a short matrix, run a fixed checklist of actions at each step, record what breaks (rubber-banding, missed hits, desynced UI, double purchases), and confirm on a real constrained network. Use before shipping netcode-sensitive features or when players with high ping report bugs."
category: perf
tags: ping, latency, lag simulation, packet loss, rubber banding, desync, netcode, replication lag, cellular, test
kb: Roblox/roblox-kb/optimization-and-streaming.md, Roblox/roblox-kb/testing-debugging-and-qa.md, Roblox/roblox-kb/client-server-and-remotes.md, Roblox/roblox-kb/scripting-and-performance.md
related: lag-hunter, network-traffic-auditor, playtest-bot-writer, mobile-perf-tester, remote-guard-builder, game-optimizer
---

# ping-sensitivity-tester

Developers test at near-zero latency; many players do not have it. This skill adds latency in Studio on purpose, runs the same action checklist at each step, and writes down exactly where the experience falls apart, so netcode fixes target real failures.

## When to use
A fast-action or competitive feature (combat, parkour, vehicles), a purchase or reward flow that could double-fire, reports of "works for me", or before a launch. Not for: bandwidth volume (`network-traffic-auditor`) or finding the source of lag from a symptom (`lag-hunter`).

## Inputs (max 2)
1. The features to test (default: movement, one combat action, one purchase/reward, one UI that depends on server state). 2. The latency matrix (default: 0, 100, 200, 300 ms; a heuristic: widen from your players' ping in the dashboard).

## Procedure
1. Write the checklist first (5-8 actions with a pass condition each), for example: walk across the map and stop (no snap back); fire the main ability and see hit feedback within the expected time; buy a developer product (one grant, one receipt); open a shop UI while the server updates stock; teleport; pick up an item twice quickly. Stop if you cannot state a pass condition for an action.
2. Baseline at 0 ms (run `scripts/set_lag.luau` with `LAG_MS = 0`, play, run the checklist). Record results.
3. For each step in the matrix: set `LAG_MS` in `scripts/set_lag.luau` and run it (Edit mode, before Play; it sets `settings().Network.IncomingReplicationLag`), play the checklist, record pass/fail and what you saw. Always reset to 0 at the end.
4. Classify each failure: rubber-banding (server correction of client prediction), missed or late hits (hit authority, see the hit-detection notes), double actions (missing debounce on remotes or on UI), UI that shows stale state, animation or sound out of sync, remote spam while waiting.
5. Fixes by class: client prediction with server reconciliation for movement-like actions; debounce on the client and idempotency on the server (processing receipts exactly once); show a pending state until the server confirms; server-side tolerance windows for hits; send inputs not results; keep remotes small (`network-traffic-auditor`).
6. Real network: Studio's simulation is coarse (incoming replication only, no jitter or packet loss). Repeat the key actions on a phone over cellular or constrained Wi-Fi and a throttled connection; report loss/jitter results separately as `untested` if not done.
7. Re-run the matrix after fixes; keep the results table with the build id.

## Studio MCP path
`list_roblox_studios` -> `execute_luau` (Edit) `scripts/set_lag.luau` with the chosen value -> `start_stop_play` -> drive actions with `playtest-bot-writer` scripts where possible -> `get_console_output` -> `screen_capture` for UI state -> `execute_luau` (Edit) `LAG_MS = 0` to reset. Feel (rubber-banding) needs a human; mark bot-only checks as partial.

## Fallback
If the setting is unavailable (permission, Studio version), run the test on a throttled network (OS or router level) and say so. Hand steps: Studio settings > Network > Incoming Replication Lag. Packet loss and jitter stay `untested` unless done on a real network.

## Evidence
Official: `Roblox/docs/Videos/2026-10-28 - Docs performance-optimization test-on-hardware.md` (confirm network behaviour over cellular or constrained Wi-Fi; Studio simulation is only for quick iteration), `Roblox/docs/Videos/2026-10-28 - Docs studio device-simulator.md` (emulation limits). `Roblox/roblox-kb/optimization-and-streaming.md`: remotes are reliable and ordered, so a lost packet stalls traffic and causes ping spikes; physics replication roughly 20 Hz interpolated at 60 Hz; data ping much higher than network ping points at replication queueing. `Roblox/roblox-kb/scripting-and-performance.md`: choose hit-detection authority by game type; server authority for characters; validate everything on the server. The matrix values are heuristics.

## Output
```
PING MATRIX <build> <date>
Action            0 ms   100    200    300
Walk & stop       ok     ok     snap   snap+stuck
Ability hit       ok     ok     late   missed (server rejects)
Buy product       ok     ok     ok     double prompt (BUG: no pending state)
Fixes: pending state on purchase button; hit window +80 ms server side. Re-run: all ok to 200, snap at 300 accepted.
Not tested: packet loss, jitter (no real-network run)
```

## Acceptance checks
- [ ] Each checklist action has a stated pass condition and a result per latency step.
- [ ] Latency was reset to 0 afterwards (verify by reading the property).
- [ ] Each failure is classed and either fixed with a re-run or listed as accepted with the reason.
- [ ] Real-network run done, or loss/jitter listed as `untested`.
- [ ] Executed check: `set_lag.luau` passes the pack's luau-check run (stylua, selene, luau-lsp).

## Pitfalls
Forgetting to reset the lag and then debugging a "slow Studio". Treating the simulation as real-world ping. Testing only walking. Fixing double-purchases only on the client. Making hit detection fully client-trusted to hide lag (exploit risk).

## Related
`lag-hunter`, `network-traffic-auditor`, `playtest-bot-writer`, `mobile-perf-tester`, `remote-guard-builder`.
