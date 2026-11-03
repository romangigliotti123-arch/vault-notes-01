---
name: memory-budget-planner
description: "Set client memory budgets per device tier and a server memory budget from the player cap, read the Developer Console memory categories against them, and name the biggest categories to cut. Use before a content update, when phones crash with out-of-memory, or when the Performance dashboard shows rising crashes."
category: perf
tags: memory, budget, out of memory, OOM, crash, 2gb, developer console, server memory, ClientMemoryUsagePercentage, devices
kb: Roblox/roblox-kb/optimization-and-streaming.md, Roblox/roblox-kb/scripting-and-performance.md, Roblox/roblox-kb/analytics-metrics.md, Roblox/roblox-kb/testing-debugging-and-qa.md
related: game-optimizer, texture-budget-checker, streaming-enabler, instance-leak-finder, mobile-perf-tester, server-tick-analyzer
---

# memory-budget-planner

Mobile crashes are mostly memory problems, so memory comes before frame rate. This skill turns "how much is too much" into numbers per device tier, reads where memory actually goes, and sets a regression guard so a content update cannot silently blow the budget.

## When to use
A crash rate above about 2-3 percent, out-of-memory exits on phones, a big asset drop coming, or a first launch. Not for: a number that grows over time (`instance-leak-finder`), shrinking textures or meshes (`texture-budget-checker`), or frame time (`mobile-perf-tester`).

## Inputs (max 2)
1. Lowest device you promise to support (default: a 2 GB Android phone). 2. Max players per server (default: the place's MaxPlayers).

## Procedure
1. Pick the tiers. The Creator Docs say about 65 percent of a typical game's players are on Android and most Android devices have 2-4 GB. Run `MemoryBudget.clientTier(ramGB)` (scripts/MemoryBudget.luau) for each tier you support: it returns the ejection ceiling (66 percent of RAM, about 1.3 GB on a 2 GB phone) and a target (450 MB for the 2 GB tier, from the vault's 400-500 MB whole-game consensus; larger tiers scale as a labelled heuristic).
2. Read real usage on a physical device, not Studio (Studio runs server and client together, so its memory is significantly higher): Developer Console F9 > Memory tab. Record PlaceMemory, PlaceScriptMemory, and in the client categories GraphicsMeshParts, GraphicsTexture, Sounds. Stop if you only have Studio numbers: mark everything `untested`.
3. Rank the categories with `MemoryBudget.breakdown({PlaceMemory=..., Sounds=..., ...})` and assess with `MemoryBudget.assessClient(usedMB, tier)`: ok, over-target, risk, ejection-zone.
4. Server side: `MemoryBudget.serverTotalMB(maxPlayers)` is 6.25 GiB + 100 MiB per player (30 players about 9.18 GiB); keep use below 50 percent (the analytics docs also say under 3 GB). Server memory does not shrink when players leave, so plan on the peak. `assessServer` returns ok, warn (over 40 percent) or over.
5. Cut the largest category first: textures and meshes (`texture-budget-checker`), sounds stored in SoundService (create at runtime and destroy), unused animation and audio references (destroy so they unload), content in ReplicatedStorage that clients do not need (move to ServerStorage), streaming off (`streaming-enabler`).
6. Set the regression guard: the tier table, the target per category, and the check to run on every release (Developer Console on the baseline device, plus the dashboard's ClientMemoryUsagePercentageP90 per place version).
7. Alert: in the Performance dashboard watch ClientMemoryUsagePercentage and OomUnexpectedExits per platform (see `server-tick-analyzer` for the server side).

## Studio MCP path
Studio MCP cannot read a device's memory. `execute_luau` can read `game:GetService("Stats"):GetTotalMemoryUsageMb()` in a Play session for a Studio-only relative comparison (label it Studio, not device). Use `execute_luau` with `game:GetService("Workspace")` queries from `part-count-auditor` for content counts if needed.

## Fallback
Pure paper: run `MemoryBudget` under Lune with numbers the owner reads from the device's Developer Console; the dashboard supplies crash and memory percentiles. Everything about a specific device stays `untested` without a reading.

## Evidence
`Roblox/roblox-kb/optimization-and-streaming.md` (full-game memory about 400-500 MB; Studio memory is not device memory; investigate crash rates past 2-3 percent; server memory formula; sounds created at runtime instead of SoundService dropped one game from about 500 MB to 58 MB, indie-reported). `Roblox/roblox-kb/scripting-and-performance.md` (ejections rise near 66 percent of memory, about 1.3 GB, crash about 1.4 GB on a 2 GB device; creator reports). Official: `Roblox/docs/Videos/2026-10-28 - Docs performance-optimization identify.md`, `Roblox/docs/Videos/2026-10-28 - Docs performance-optimization test-on-hardware.md` (device mix), `Roblox/docs/Videos/2026-10-28 - Docs studio optimization memory-usage.md` (Memory tool categories), `Roblox/docs/Videos/2026-10-28 - Docs production analytics performance.md`. Device mix and thresholds change: live-check.

## Output
```
MEMORY BUDGET <game> <date>
Tier 2 GB: ceiling 1351 MB, target 450 MB | Tier 4 GB: ceiling ..., target ... (heuristic)
Measured (device, build): PlaceMemory 380 | GraphicsTexture 210 | Sounds 60 ... -> status over-target
Server: MaxPlayers 30 -> total 9.18 GiB, budget 4.6 GiB, measured ... -> ok
Cuts (largest first): ... Guard: re-check on <device> each release; alert at ...
```

## Acceptance checks
- [ ] Each number is labelled device, Studio, or dashboard; Studio memory never stands in for a device.
- [ ] Targets for tiers above 2 GB are marked heuristic; the 2 GB figures cite the vault.
- [ ] Server budget uses the player cap and the 50 percent rule.
- [ ] A cut list is ordered by measured share.
- [ ] Executed check: `MemoryBudget.test.luau` passes under Lune; scripts pass luau-check.

## Pitfalls
Judging memory in Studio or the device emulator. Optimising frame rate while the real problem is out-of-memory. Forgetting that server memory only grows. Budgeting for the dev PC. Treating the heuristic tier targets as facts.

## Related
`game-optimizer`, `texture-budget-checker`, `streaming-enabler`, `instance-leak-finder`, `mobile-perf-tester`.
