---
id: "roblox-brain/roblox-performance"
type: skill
category: "src-roblox-brain"
source: "roblox-brain"
license: "MIT"
repo_path: "sources/roblox-brain/skills/core/roblox-performance/SKILL.md"
description: "Use when profiling or fixing Roblox performance: low FPS, lag, memory, network load, slow phones, hot paths."
orig_name: "roblox-performance"
orig_when_to_use: "Also when the game stutters, phones overheat or crash, server heartbeat drops, before adding many parts/effects/UI, and when auditing performance before release."
orig_last_reviewed: "2026-10-02"
alternatives: ["roblox-skills-el4cteo: roblox-skills-el4cteo/roblox-performance"]
tags: [lib/skill, cat/src-roblox-brain, src/roblox-brain]
---

# roblox-brain/roblox-performance

> Use when profiling or fixing Roblox performance: low FPS, lag, memory, network load, slow phones, hot paths.

Type: skill | Category: [[categories/cat-src-roblox-brain|src-roblox-brain]] | Source: [[sources/src-roblox-brain|roblox-brain]] | License: MIT
Repo file: `sources/roblox-brain/skills/core/roblox-performance/SKILL.md` (extra files, if any, sit beside it in the repo)

Related: [[S--roblox-brain--roblox-luau-patterns]]

---
# Roblox Performance

## When to Load

Use for profiling and performance budgets. Pooling and lifecycle patterns: `roblox-luau-patterns`.

## Quick Reference

### Profiling Tools
- **MicroProfiler (Ctrl+F6)**: Frame breakdown of scripts, physics, rendering.
- **Developer Console (F9)**: Memory, network, rendering, and server stats.
- **Script Profiler (Ctrl+Alt+F5)**: Per-script CPU and heap.
- **Labels**: `debug.profilebegin`/`debug.profileend` mark regions; `debug.setmemorycategory` labels memory. Gate instrumentation behind a flag.

### Performance Targets
| Metric | Starting target | Investigate at |
|--------|-----------------|----------------|
| Server heartbeat | < 16ms | > 33ms |
| Client FPS (desktop) | 60 | < 30 |
| Client FPS (mobile) | 45 | < 30 |
| Memory | device-specific | sustained growth |

Optimize measured hot paths, not folklore. Throttle from measurements; re-profile after shipping.

### Parallel Luau
- Use Actors only after profiling identifies isolatable CPU work.
- Workers compute; synchronize before restricted DataModel writes.
- Do not rely on shared module state across Actors. `SendMessage` copies data; SharedTable supports shared state and atomic updates.

### Hot-loop cost model
- Luau optimizes global imports; avoid folklore function hoisting/unrolling. Environment impurity can disable optimizations. Profile allocations as well as CPU; GC cost may occur later.

### Object Pooling
Pre-clone and reuse. Canonical pool code (token-lease ownership): `roblox-luau-patterns`.

### StreamingEnabled Essentials
- **On by default**. Container-scoped: only Workspace descendants stream. `ModelStreamingBehavior = Improved` streams non-BasePart descendants with their parent Model; Legacy streams only BaseParts.
- **Streamed-out = parented to nil**, not destroyed. Luau refs persist if it streams back.
- **Config (Studio)**: target defaults 1024, min 64; set `StreamingIntegrityMode`; tune from data.
- **Gotcha**: `FindFirstChild("DistantPart")` returns nil if streamed out. Use WaitForChild with timeout.

### Mobile
- Profile geometry, textures, particles, UI, shadows on low-end devices.

> Full reference with code examples and API tables: [references/full.md](references/full.md)

---

## Alternatives (same name, not shown in this vault)

This note is the best of 2 items called `roblox-performance`. The others stay in the claude-library repo (open the repo file if this one does not fit):

- `roblox-skills-el4cteo`: roblox-skills-el4cteo/roblox-performance - Performance diagnosis and optimization - MicroProfiler, Script Profiler, Developer Console, Scene Analysis, Luau heap and memory categories... (repo file `sources/roblox-skills-el4cteo/skills/roblox-performance/SKILL.md`)

