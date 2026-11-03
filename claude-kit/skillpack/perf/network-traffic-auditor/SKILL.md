---
name: network-traffic-auditor
description: "Measure remote-event and replication volume per client, rank the biggest senders, and cut them with batching, smaller data types, unreliable-style updates and client-side visuals, keeping each client under about 50 KB/s. Use when ping is high, humanoids teleport or rubber-band, or before adding a high-frequency remote."
category: perf
tags: network, remote events, replication, bandwidth, KB/s, batching, vector3int16, buffer, ping, networkownership
kb: Roblox/roblox-kb/optimization-and-streaming.md, Roblox/roblox-kb/client-server-and-remotes.md, Roblox/roblox-kb/scripting-and-performance.md, Roblox/roblox-kb/physics-pathfinding-and-npc-ai.md
related: lag-hunter, game-optimizer, ping-sensitivity-tester, heartbeat-loop-auditor, remote-guard-builder, npc-cost-reducer
---

# network-traffic-auditor

Find what the server sends and receives, in bytes per second, and cut the biggest items first. `lag-hunter` starts from a symptom; this skill starts from the traffic itself and ends with a budget per remote.

## When to use
High data ping versus network ping, characters or NPCs teleporting, many tweened server objects, a new feature that fires a remote every frame, or a pre-launch bandwidth check. Not for: validating what clients may send (`remote-guard-builder`) or server CPU (`server-tick-analyzer`).

## Inputs (max 2)
1. The scenario (player count, area, action) where traffic is high. 2. Whether you can run a playtest with the Server datamodel (default: yes via Studio).

## Procedure
1. Inventory remotes: `execute_luau` or `script_grep` for `RemoteEvent|RemoteFunction|UnreliableRemoteEvent|FireClient|FireAllClients|FireServer`. List each remote with payload fields and how often it fires.
2. Measure real traffic during the scenario: run `lag-hunter/scripts/remote_probe.luau` on the Server datamodel (counts client-to-server calls per remote and per player) and capture a MicroProfiler dump or Network Stats (Ctrl+F7) for incoming and outgoing volume. Network data appears only in MicroProfiler frame dumps from desktop or Studio, not the live overlay; use Low verbosity to capture more frames and High to see asset IDs; right-click a frame to open Network events.
3. Estimate the rest with `scripts/NetBudget.luau`: `NetBudget.audit({{name="Pos", fields={"cframe"}, hz=20}, ...}, players)` returns rows ranked by total server send and the worst-case per-client KB/s, and `NetBudget.status` gives ok, warn (over 60 percent of the figure) or over (above 50 KB/s).
4. Cut, biggest first:
   a. Replace per-frame or per-tween server updates with client-side visuals: spawn cosmetic effects and animate distant props on the client, replicate only the state (one test: 60 tweened server doors about 1,800 KB/s received, animation playback about 0 KB/s; indie).
   b. Send compact types: Vector3int16 (about 6 bytes) instead of CFrame (about 20), an i16 for Y rotation, Color3 as a short string, arrays instead of string-keyed tables, identifiers instead of whole tables; group small buffers so compression works.
   c. Batch many small events into one send and rate-limit high-frequency ones. Do not use reliable ordered remotes for fast-changing state: a lost packet stalls everything behind it; use an unreliable path for things like head rotation.
   d. Reduce replicated instances and server-owned moving assemblies; give network ownership to the driver where safe.
5. Re-measure the same scenario. Keep a change only if the figure fell and gameplay is unchanged.
6. Write the per-remote budget (bytes x Hz x receivers) so new features are checked against it.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `script_grep` (find remotes) -> `start_stop_play` -> `execute_luau` (Server) with `lag-hunter/scripts/remote_probe.luau` -> `get_console_output`. The profiler/Network Stats windows cannot be driven by MCP: ask the owner for the KB/s readings or mark them `untested`.

## Fallback
Command bar and a Studio server session for the probe; otherwise do the paper audit with `NetBudget` and mark measured values `untested`. Rojo: edit remotes as files; verification still needs a session.

## Evidence
`Roblox/roblox-kb/optimization-and-streaming.md`: keep per-client replication under about 50 KB/s (above roughly that throttle humanoids replicate slowly or teleport), compact data sizes, batching, reliable-remote stalls, moving humanoid bandwidth about 4 KB/s at 5 units to 160 KB/s at 500 (creator tests; indie). `Roblox/roblox-kb/scripting-and-performance.md`: about 1 KB per streamed part; server-owned moving assemblies about 1 KB/s each, keep to about 50. Official: `Roblox/docs/Videos/2026-10-28 - Docs performance-optimization microprofiler network.md`. Sizes in `NetBudget.SIZES` come from these figures; the real wire format may differ: measure.

## Output
```
NETWORK AUDIT <game> <scenario> <date>
Per client: 63 KB/s (limit ~50) status=over   [measured: Network Stats | estimated: NetBudget]
1. PlayerPos  20 Hz x 20 B x 30 receivers = 11.7 KB/s total ... -> Vector3int16: 6 B
Changes kept: ...   After: 31 KB/s
```

## Acceptance checks
- [ ] Each figure is labelled measured or estimated.
- [ ] The biggest three senders are named with bytes, rate and receivers.
- [ ] After-change traffic measured in the same scenario, or labelled `untested`.
- [ ] No server-validation was removed to save bytes (`remote-guard-builder` rules still hold).
- [ ] Executed check: `NetBudget.test.luau` passes under Lune; scripts pass luau-check.

## Pitfalls
Optimising from byte estimates alone. Sending Float64 numbers for values that fit an int16. Batching so aggressively that input feels laggy. Making a remote unreliable when ordering matters. Forgetting the received (incoming) side. Treating the 50 KB/s figure as a hard Roblox limit for every game type.

## Related
`lag-hunter`, `game-optimizer`, `ping-sensitivity-tester`, `remote-guard-builder`, `npc-cost-reducer`.
