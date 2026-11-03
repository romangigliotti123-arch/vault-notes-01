---
name: render-cost-auditor
description: "Find what makes frames expensive to draw: shadow-casting lights and parts, partial transparency and overdraw, Neon and glass, particle and beam load, Highlights, SurfaceGuis, PBR textures and the Lighting technology; rank the offenders and fix them one at a time with GPU-wait evidence. Use when the MicroProfiler shows GPU wait or Render bars, or phones overheat."
category: perf
tags: rendering, shadows, overdraw, transparency, lights, neon, highlights, gpu, fill rate, lighting technology, draw calls
kb: Roblox/roblox-kb/optimization-and-streaming.md, Roblox/roblox-kb/scripting-and-performance.md, Roblox/roblox-kb/building-art-and-assets.md
related: game-optimizer, cpu-vs-gpu-diagnoser, effects-budget-setter, part-count-auditor, texture-budget-checker, lighting-preset-picker
---

# render-cost-auditor

Rendering cost hides in lights, transparency and effects rather than in raw part count. This skill takes a census of the usual drivers, orders the fixes by likely payoff, and insists on a GPU-side measurement for each.

## When to use
GPU wait (red MicroProfiler bars over 2.5 ms), a frame rate that falls with graphics quality up, overheating phones, or a scene with lots of lights, glass and VFX. Not for: deciding CPU vs GPU (`cpu-vs-gpu-diagnoser`), particle caps themselves (`effects-budget-setter`), or the look of the lighting (`lighting-preset-picker`).

## Inputs (max 2)
1. The scene or area and device where it is slow. 2. The visual non-negotiables (what must not change).

## Procedure
1. Confirm it is render-side: `cpu-vs-gpu-diagnoser` (red bars, GPU wait over 2.5 ms, or blue Render-over-Jobs). If the frame is inside its goal, stop.
2. Census: `scripts/render_census.luau` (read-only; Workspace only). Save it. It reports Lighting.Technology, shadow-casting parts, partially transparent parts, Neon and glass, SurfaceAppearance parts, lights and how many cast shadows, particle emitters with an estimated live-particle count, beams, trails, Highlights, SurfaceGuis, BillboardGuis, and decals on fully transparent parts.
3. Fix in this order, re-measuring (GPU wait and Render stats) after each:
   a. Shadows: disable `CastShadow` on tiny, hidden or in-shadow parts; `Light.Shadows` off where not needed; limit range/angle; merge small nearby point lights. Shadows are not computed below graphics quality 4, so the cost exists only for players at quality 4+.
   b. Transparency: use 0 or 1; avoid stacked partial-transparency layers over large screen areas (merge into one union), and no decals or textures on fully transparent parts.
   c. Materials: SmoothPlastic instead of Neon/Glass on large counts; built-in materials before custom textures.
   d. Effects: cap emitters, reduce size of big particles (fill rate), distance-fade; Highlights: toggle Enabled instead of adding/removing, delete unused ones (cap 255). Hand the numbers to `effects-budget-setter`.
   e. Lighting.Technology: ShadowMap is the recommended default; Future only when visuals need it. Turn off Haze and dynamic clouds if unneeded; keep post-processing inside Lighting.
   f. Textures: drop or shrink PBR maps (`texture-budget-checker`); SurfaceGuis: lower counts and set MaxDistance.
4. Provide a client-only low-graphics mode if the audience is phones: SmoothPlastic, CastShadow off, cheaper lighting, heavy particles stripped client-side. Keep the PC look unchanged.
5. Compare before/after screenshots (`screen_capture`) to prove the visual is acceptable, and the GPU numbers to prove the gain. Revert changes with no measurable gain.

## Studio MCP path
`list_roblox_studios` -> `execute_luau` (Edit) `scripts/render_census.luau` -> `script_read` of Lighting/QualityLevel scripts if any -> `execute_luau` property edits (record old values) -> `screen_capture` before and after (same camera) -> `start_stop_play`. GPU timing is read manually from the MicroProfiler; MCP cannot drive it: `untested` otherwise.

## Fallback
Command bar: paste `render_census.luau`. Without a profiler, report the census and ranked suspects and label every gain `untested`. Rojo: scripts only; lights and materials live in place data, so list property changes for the owner.

## Evidence
`Roblox/roblox-kb/optimization-and-streaming.md`: shadow and light cost (shadows disabled below quality 4), overdraw from transparency, SmoothPlastic over Neon, Highlight rebuild and 255 cap, ShadowMap default, MicroProfiler colour reading (red GPU wait over 2.5 ms: complexity, texture size, VFX); tester ratings for clouds, Neon, glass and haze are indie. Official: `Roblox/docs/Videos/2026-10-28 - Docs performance-optimization design.md` (avoid partial transparency; reuse assets), `Roblox/docs/Videos/2026-10-28 - Docs performance-optimization improve.md` (shadow cutoff at quality 4), `Roblox/docs/Videos/2026-10-28 - Docs performance-optimization scene-analysis.md`. Gains per item are not published: measure.

## Output
```
RENDER AUDIT <scene> <device> <date>
GPU wait before 5.8 ms (red) | shadowed lights 64 | partial-transparent parts 3,200 | emitters 410 (~9,000 live)
Fixes kept (in order): 1. 51 lights Shadows off: -1.9 ms | 2. merged glass panes ...
After: GPU wait 2.1 ms. Visual diff: accepted/rejected (screenshots).
```

## Acceptance checks
- [ ] Render-bound confirmed before work began (or stated assumption).
- [ ] Each kept fix has before/after GPU or frame numbers, or is labelled `untested`.
- [ ] Before/after screenshots from the same camera attached.
- [ ] Nothing the owner called non-negotiable changed.
- [ ] Executed check: `render_census.luau` passes the pack's luau-check run (stylua, selene, luau-lsp).

## Pitfalls
Fixing lights when the bound is CPU. Disabling all shadows and ruining the look instead of targeting tiny parts. Counting parts when the problem is overdraw. Adding and removing Highlights at runtime. Trusting a PC GPU reading for a phone.

## Related
`game-optimizer`, `cpu-vs-gpu-diagnoser`, `effects-budget-setter`, `part-count-auditor`, `texture-budget-checker`, `lighting-preset-picker`.
