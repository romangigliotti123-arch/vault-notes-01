---
name: lighting-preset-picker
description: "Pick a lighting, atmosphere, fog, bloom and colour-grading preset by mood and device budget (bright cartoon, warm sunset, night, spooky fog, overcast), preview the exact property changes as a dry run, and apply them in one undo step. Covers sky and atmosphere setting. Use when a map looks flat, mismatched or too heavy for phones."
category: build
tags: lighting, atmosphere, sky, fog, bloom, colorcorrection, mood, shadowmap, mobile, clocktime
kb: Roblox/roblox-kb/building-art-and-assets.md, Roblox/roblox-kb/building-and-level-design.md, Roblox/roblox-kb/optimization-and-streaming.md, Roblox/roblox-kb/vfx-and-particles.md
related: palette-picker, art-bible-writer, material-consistency-checker, particle-effect-planner, game-optimizer
---

# lighting-preset-picker

Lighting is foundation, not polish: the vault says to set light direction, intensity and the skybox together. This keeps five tested-for-validity presets, trims them for phones, and applies one with a diff you can read first. It replaces a separate sky-atmosphere skill: sky, fog, bloom and grading are all set here.

## When to use
Starting a map's look, a screenshot looks washed out, fog is wrong, or a mobile build needs fewer effects. Not for: deciding the whole art direction (`art-bible-writer`), or per-light placement (PointLights, SpotLights are set by hand).

## Inputs (max 2)
1. Mood: `bright_cartoon` (default), `warm_sunset`, `night`, `spooky_fog`, `overcast`. 2. Device: `pc` or `mobile` (default `mobile` if most players are on phones).

## Procedure
1. Connect (below). Take a screenshot of the current look at the player's camera (`screen_capture`).
2. Generate the preset: under Lune, `LightingPresets.pick(mood, device)` from `scripts/LightingPresets.luau` (validated ranges, mobile trims) and `LightingPresets.toLuau(...)` prints a Luau table. Mobile removes Haze, sun rays and blur and caps bloom (vault: turn off haze, keep post-processing small).
3. Paste the table over `PRESET` in `scripts/apply_lighting.luau` and run it with `APPLY = false`: it prints every property as `old -> new` and notes effects the preset does not mention.
4. Apply with `APPLY = true` (one undo step). Existing Atmosphere, Bloom, ColorCorrection, SunRays and Blur are updated in place; missing ones are created.
5. Set by hand what the script does not touch: `Lighting.Technology` (ShadowMap is the vault's default; Future only for demanding visuals), the Sky asset (the owner's skybox; match it to the light direction).
6. Screenshot again at the same camera, plus an interior and a night/dark corner if there is one. Compare. Tweak ClockTime, Brightness and Atmosphere density by eye; the numbers are starting points.
7. Check contrast of UI and key gameplay objects against the new look (`palette-picker`), and check frame time on a low-end device profile (`game-optimizer`).

## Studio MCP path
`list_roblox_studios` -> `screen_capture` -> `execute_luau` (Edit) with `scripts/apply_lighting.luau` (dry run, then apply) -> `screen_capture` -> `get_console_output`.

## Fallback
Set the printed values in the Lighting properties by hand. Without Studio the preset can still be validated under Lune (ranges, mobile trims); the look is `untested`.

## Evidence
`Roblox/roblox-kb/building-art-and-assets.md` (lighting and atmosphere are foundation; adjust direction, intensity and skybox together; an indie cartoon preset used Atmosphere density 0.269 and Blur 4, labelled indie), `Roblox/roblox-kb/building-and-level-design.md` (warm ambient tint 83,70,57 versus the default 70,70,70; Realistic lighting for local lights), `Roblox/roblox-kb/optimization-and-streaming.md` (ShadowMap by default; turn off Haze and dynamic clouds). Every other number is this skill's own starting point.

## Output
```
LIGHTING PRESET: warm_sunset (mobile)
  Lighting.ClockTime: 14 -> 17.8   Atmosphere.Density: 0.269 -> 0.35 ...
applied (one undo step). Before/after screenshots: 2. Untested: low-end device frame time
```

## Acceptance checks
- [ ] A dry run diff was read before applying.
- [ ] Before/after screenshots at the same camera are attached.
- [ ] Mobile trims are present when the device is mobile (no haze, sun rays, blur).
- [ ] Technology and the Sky asset were set by a person, not invented.
- [ ] The apply was one undo step; ranges validated by the module's tests.

## Pitfalls
Judging the preset in Studio's editor camera only. Bloom plus neon plus glass stacking into a blur. Night presets that make gameplay unreadable on dim phone screens. Haze left on for phones. Atmosphere colours that fight the palette. Applying a preset over hand-tuned work without a screenshot.

## Related
`palette-picker`, `art-bible-writer`, `material-consistency-checker`, `particle-effect-planner`, `game-optimizer`.
