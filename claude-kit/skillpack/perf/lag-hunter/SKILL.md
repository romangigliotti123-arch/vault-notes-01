---
name: lag-hunter
description: "Find the cause of a specific lag symptom (rubber-banding, server freezes, stutter in one area, lag after N minutes, lag with many players) by splitting client vs server vs network, probing remote traffic and heartbeat time, and narrowing to a script, an area or a leak. Use when you have a symptom, not a number; game-optimizer is the broad pass."
category: perf
tags: lag, rubber banding, stutter, server lag, heartbeat, ping, remote spam, freeze, hitch, leak, slow
kb: Roblox/roblox-kb/optimization-and-streaming.md, Roblox/roblox-kb/scripting-and-performance.md, Roblox/roblox-kb/client-server-and-remotes.md, Roblox/roblox-kb/testing-debugging-and-qa.md
related: game-optimizer, script-profiler, network-traffic-auditor, heartbeat-loop-auditor, instance-leak-finder, server-tick-analyzer, physics-load-reducer, ping-sensitivity-tester
---

# lag-hunter

Symptom in, suspect out. Start by deciding WHERE the lag lives, because the fixes differ: client frame time (rendering/scripts), server heartbeat (physics/scripts/remotes), or network (latency, replication volume). Then confirm with a probe before touching code.

## When to use
"Players rubber-band", "the server freezes every minute", "lags only in the market", "gets laggier over time", "lags with 20 players". Not for: a blanket optimisation pass (`game-optimizer`).

## Inputs (max 3)
1. The symptom, exactly (who sees it: all players or some? where? when? how long after joining?). 2. Does it reproduce in a Studio playtest or only live? 3. Studio MCP connected? (default: detect).

## Procedure
1. Classify by symptom:
   - Everyone's world stutters and other players move jerkily at the same time -> SERVER (slow heartbeat).
   - Only your own screen stutters, others look smooth -> CLIENT frame time.
   - Your character rubber-bands, actions delay, others fine -> NETWORK/ownership/latency or a server handler blocking.
   - Gets worse over time -> a LEAK (instances, connections, tables).
   - Only with many players -> per-player cost scaling (loops over all players, replication volume).
   - Only in one area -> content density (parts, effects, NPCs) there.
2. Reproduce with the cheapest test: Studio playtest with the Server/Client toggle; add latency in Studio's network settings; spawn test dummies; or the live server with the Developer Console (F9) Server tab (script activity, memory, network).
3. Probe the server: `scripts/remote_probe.luau` on the Server datamodel for 20 s. It reports heartbeat average and worst frame and the client->server remote calls per second by remote and sender. Over about 10 calls/s per player from gameplay input, or one player dominating a remote, is a suspect (batch, throttle, rate-limit; may also be an exploiter).
4. Server heartbeat high with few remote calls: look at scripts (`script-profiler`: Script Profiler and MicroProfiler, `Heartbeat` loops over all parts/players, `GetDescendants` in loops, `FindFirstChild` storms, pathfinding, NPC AI), physics (unanchored parts, constraints, `Touched` spam: `physics-load-reducer`).
5. Client-side: MicroProfiler (Ctrl+Alt+F6) to see whether time is script, render, or physics; check effect counts and shadows in the area (`render-cost-auditor`), streaming settings (`streaming-enabler`).
6. Leaks: sample instance counts and memory over several minutes (`instance-leak-finder`): rising Instance count in Workspace or Debris-less effects; connections created per player/event and never disconnected; tables that only grow (caches keyed by player not cleaned on leave).
7. Network: unreliable remote use for high-frequency cosmetic data, send identifiers not tables, replicate less (StreamingEnabled), avoid `FireAllClients` in loops, set `NetworkOwnership` knowingly (`SetNetworkOwner(nil)` for server-run physics objects that jitter).
8. Fix ONE suspect, re-run the probe/scenario, keep the fix only if the number moves. Report with before/after.

## Studio MCP path
`list_roblox_studios` -> `start_stop_play` -> `execute_luau` (datamodel_type Server) with `scripts/remote_probe.luau` while a bot or `character_navigation` exercises the area -> `get_console_output` -> `search_game_tree` / `inspect_instance` on suspects -> fix via `multi_edit` -> re-run. The profiler windows are manual: ask the owner for readings or say untested.

## Fallback
Developer Console readings and MicroProfiler captures pasted by the owner; the probe script can be a Script in ServerScriptService of a test place. Without a repro, produce a ranked suspect list with the probe to run next.

## Evidence
`Roblox/roblox-kb/optimization-and-streaming.md` (measure first; MicroProfiler for spikes vs steady cost; Developer Console memory; real low-end client; collision and effects costs), `Roblox/roblox-kb/client-server-and-remotes.md` (minimal data; rate-limit per player; gatekeeper not relay), `Roblox/roblox-kb/scripting-and-performance.md`, `Roblox/roblox-kb/testing-debugging-and-qa.md`. The "10 calls per second" figure is this skill's triage heuristic, not a Roblox limit.

## Output
```
LAG HUNT <game> <symptom>
Class: SERVER|CLIENT|NETWORK|LEAK|SCALING   Evidence: <probe output lines>
Top suspects (ranked): 1. ... confirmed|unconfirmed
Fix applied: ... before -> after (heartbeat avg/worst ms, calls/s)
Not checked: ...
```

## Acceptance checks
- [ ] The class (server/client/network/leak/scaling) is stated with the observation that decided it.
- [ ] A probe or profiler reading backs the top suspect, or it is marked unconfirmed.
- [ ] Any fix has before/after numbers from the same scenario.
- [ ] `remote_probe.luau` passes luau-check (it is part of the pack's check run).
- [ ] No gameplay behaviour changed unnoticed (core loop playtested).

## Pitfalls
Fixing the loudest script instead of the biggest cost. Calling it "network" without a ping reading. Adding rate limits that break legit fast actions. Testing alone when the cost scales with players. Forgetting that Studio is not a real client.

## Related
`game-optimizer`, `script-profiler`, `network-traffic-auditor`, `heartbeat-loop-auditor`, `instance-leak-finder`, `physics-load-reducer`.
