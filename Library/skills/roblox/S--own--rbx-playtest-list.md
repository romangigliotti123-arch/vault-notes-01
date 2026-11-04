---
id: "rbx-playtest-list"
type: skill
category: "roblox"
source: "own"
license: "first-party"
repo_path: "skills/roblox/rbx-playtest-list/SKILL.md"
description: "Checklist and bug-report format for playtesting a Roblox experience (first 30 seconds through multiplayer and exploits)."
orig_name: "rbx-playtest-list"
tags: [lib/skill, cat/roblox, src/own]
---

# rbx-playtest-list

> Checklist and bug-report format for playtesting a Roblox experience (first 30 seconds through multiplayer and exploits).

Type: skill | Category: [[categories/cat-roblox|roblox]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/roblox/rbx-playtest-list/SKILL.md` (extra files, if any, sit beside it in the repo)

---
# Roblox playtest checklist

Setup: build/version, test mode (Studio Play, Local Server with N players, or live client), device profile (phone/tablet/PC), Output window open.

1. First 30 seconds: spawn is safe and readable; goal obvious without reading; first reward within 30s; no blocking tutorial walls.
2. Core loop: do the action 10 times; is it fun and are numbers sane; time to first upgrade; no dead ends.
3. Economy/progression: currency in/out rates, price curve, sinks, caps; try to break by repeating the cheapest action.
4. UI: scales on a phone emulator, buttons reachable, text readable, no overlap with Roblox topbar/safe area.
5. Lifecycle: die/respawn, reset character, leave and rejoin (data saved?), teleport, server shutdown save.
6. Multiplayer: 2+ clients, replication, shared objects, latency (network simulation), late joiners.
7. Exploit probing: fire remotes with bad types/huge numbers/other players' ids; teleport/speed assumptions; client-side ownership of currency.
8. Performance: FPS and memory (MicroProfiler, Developer Console F9), script activity, part count/streaming.
9. Console: errors and warnings in Output on each scenario.

Bug format: `[S1-S4] title | build | steps | expected | actual | repro rate | log/screenshot path`.
