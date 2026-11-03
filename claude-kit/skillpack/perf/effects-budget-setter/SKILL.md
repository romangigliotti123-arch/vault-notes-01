---
name: effects-budget-setter
description: "Set explicit particle, beam, trail and Highlight budgets per scene and device tier, compute live particles from emitter rate and lifetime, scale rates down to the cap, and add a low-graphics mode for phones. Use when a scene is full of VFX, GPU fill rate is high, or before adding new effects to an existing area."
category: perf
tags: particles, effects, vfx, beams, trails, highlights, budget, emitter, fill rate, low graphics mode
kb: Roblox/roblox-kb/optimization-and-streaming.md, Roblox/roblox-kb/vfx-and-particles.md, Roblox/roblox-kb/scripting-and-performance.md
related: render-cost-auditor, cpu-vs-gpu-diagnoser, game-optimizer, texture-budget-checker, mobile-perf-tester, lighting-preset-picker
---

# effects-budget-setter

Effects get added one at a time and nobody owns the total. This skill makes the total a number: live particles per scene, a cap per device tier, a plan that scales every emitter proportionally to fit, and a client-only low-graphics mode so phones do not pay for PC visuals.

## When to use
A scene with many emitters, a new VFX pass, GPU wait in effect-heavy areas, or a phone-vs-PC visual split. Not for: finding all render costs (`render-cost-auditor` first), or art direction of the effects (the VFX skills).

## Inputs (max 2)
1. Target tiers (default: low = phone, mid, high = PC). 2. Which effects are gameplay-critical (hit confirms, telegraphs) and must not be cut.

## Procedure
1. Collect emitters per scene: `render-cost-auditor/scripts/render_census.luau` gives a quick estimate; for a per-emitter list use `execute_luau` to list ParticleEmitter name, Rate, Lifetime min/max, Enabled, size, texture. Stop if a scene has no emitters, beams or trails.
2. Compute with `scripts/EffectsBudget.luau`: `EffectsBudget.plan(emitters, "low")` returns rows ranked by live particles (Rate times average lifetime), the scene total, the cap, and a suggested rate that scales every emitter so the total fits. Caps are heuristic defaults (low 300, mid 800, high 2000 live particles); the vault gives no live-particle numbers, so tune the caps by profiling the target device and write the chosen values down.
3. Apply cuts, in this order: lower Rate before lifetime; shrink very large particles (fill rate is the real cost, so a few big particles can cost more than many small ones); reduce overlapping transparent layers; flipbook textures to smaller sizes (flipbooks are disabled by clients under low memory); trails/beams: fewer segments, shorter lifetime, cull by distance; Highlights: toggle Enabled instead of creating and destroying (changes rebuild geometry), delete unused ones, nesting avoided; stay under the 255 cap (`EffectsBudget.highlightStatus`), mobile Highlights can cost up to 1 ms GPU and scale with screen coverage.
4. Distance and visibility: enable emitters only when the player is near (distance fade), pool one-shot bursts, stop emitters in unseen rooms. Never spawn purely visual effects from the server; spawn them on the client.
5. Low-graphics mode (client-only): detect the tier (UserGameSettings saved quality and a player toggle), apply `suggestedRate` for the tier, switch heavy materials to SmoothPlastic, drop CastShadow on small parts; PC stays unchanged.
6. Verify: compare GPU wait or frame time before/after on a device (`cpu-vs-gpu-diagnoser`) and screenshots; keep gameplay-critical effects identical. Revert changes without a measured gain.
7. Publish the budget table (scene, tier, cap, current total) so every new effect is checked against it.

## Studio MCP path
`list_roblox_studios` -> `execute_luau` (Edit) listing emitters per scene folder -> compute the plan (Lune or `execute_luau` with the module pasted) -> `execute_luau` property edits (log old Rate values) -> `screen_capture` before/after -> `start_stop_play`. Frame-time effects are read manually from the profiler: otherwise `untested`.

## Fallback
Rojo/paper: owner supplies the emitter table; the plan and rates come from `EffectsBudget` under Lune; applying values is a manual or command-bar step. The cap values remain heuristics until profiled.

## Evidence
`Roblox/roblox-kb/optimization-and-streaming.md`: large particles cost fill rate; overdraw from overlapping transparency; Highlights (add/remove rebuilds geometry, disabled ones still count to 255, extras ignored, up to 1 ms GPU on mobile); client-only low-graphics mode (SmoothPlastic, no CastShadow, cheaper lighting, strip heavy mobile particles); flipbooks disabled under low memory. Official: `Roblox/docs/Videos/2026-10-28 - Docs performance-optimization design.md` (avoid partial transparency), `Roblox/docs/Videos/2026-10-28 - Docs performance-optimization scene-analysis.md` (an illustrative 25,000 emitters found in Instance Composition). Live-particle caps in the script are this skill's heuristic defaults, not vault figures.

## Output
```
EFFECTS BUDGET <scene> <tier> <date>   cap 300 live particles (heuristic)
Total 1,000 live -> scale 0.30: Smoke 400/s -> 120/s, Sparks 200/s -> 60/s ...
Highlights: 37 (cap 255) ok | Beams 12 -> 6 | Trails 20 -> 8
Result (device): GPU wait 4.1 ms -> 2.3 ms; screenshots accepted. Gameplay-critical effects unchanged.
```

## Acceptance checks
- [ ] Every scene has a total and a cap for each target tier, with the cap source stated (heuristic or measured).
- [ ] Gameplay-critical effects are listed and unchanged.
- [ ] A measured before/after (GPU wait or frame) or `untested`; screenshots from the same camera.
- [ ] No server-spawned cosmetic effects remain in the changed scene.
- [ ] Executed check: `EffectsBudget.test.luau` passes under Lune; scripts pass luau-check.

## Pitfalls
Cutting lifetime when rate is the cost, or the reverse. Counting only emitter numbers, not particle size. Leaving Highlights toggled by creating/destroying. Removing telegraph effects players need. Presenting the heuristic caps as engine limits.

## Related
`render-cost-auditor`, `cpu-vs-gpu-diagnoser`, `game-optimizer`, `texture-budget-checker`, `mobile-perf-tester`.
