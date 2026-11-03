---
name: material-consistency-checker
description: "Census the materials and colours in a place, report how many distinct ones there are, and list the rare ones as candidate style outliers with example paths, so an art lead can decide which are deliberate. Read-only. Use when a map looks like several games glued together."
category: build
tags: material, colour, color, consistency, style, art direction, outlier, neon, glass, palette
kb: Roblox/roblox-kb/building-art-and-assets.md, Roblox/roblox-kb/building-and-level-design.md, Roblox/roblox-kb/optimization-and-streaming.md
related: palette-picker, art-bible-writer, model-cleaner, texture-budget-checker, lighting-preset-picker
---

# material-consistency-checker

Style consistency is cheap to measure and expensive to ignore. The vault says to keep 4-5 things consistent (lighting, materials, palette, detail level, silhouette) and break rules only on purpose. This counts what is actually in the place and shows what does not belong. It never edits.

## When to use
After importing Toolbox assets, before a trailer or release, when a reviewer says "this looks off". Not for: choosing the palette (`palette-picker`), writing the style rules (`art-bible-writer`), or fixing (a human decision).

## Inputs (max 2)
1. Scope (Workspace default, or an area). 2. The art bible or palette if one exists (else the audit's top materials and colours become the working definition of the style).

## Procedure
1. Connect (below).
2. Run `scripts/style_audit.luau`. It counts visible parts (Transparency below 1) by Material and by colour bucket (32-step per channel, so near-identical shades merge). The statistics are `scripts/StyleStats.luau` (Lune-tested): outliers appear only when there is a dominant set to be outside of (more than 3 materials, more than 5 colour buckets) and are parts under 2 percent of the total.
3. Read: the top five materials and colours with their share, the distinct counts, neon/glass counts, and the outlier list with up to six example paths each.
4. Compare to the style definition. A single gold chest or a red hazard colour is intended; a Brick wall in a SmoothPlastic world is not. Mark each outlier keep or fix with a one-line reason.
5. If there are more than about six materials or twelve colour buckets, propose consolidation targets (map several near colours to the palette's nearest entry). Use `palette-picker` to choose them; do the recolouring as a separate, reviewed change.
6. Screenshot two outlier examples and one representative area (`screen_capture`) so the decision is visual, not numeric.
7. Re-run after fixes and report the new distinct counts.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `execute_luau` (Edit) with `scripts/style_audit.luau` -> `inspect_instance` on example paths -> `screen_capture` -> re-run after edits.

## Fallback
Command bar. Offline, dump Material and Color per part and feed `StyleStats.analyse` under Lune; screenshots are `untested`.

## Evidence
`Roblox/roblox-kb/building-art-and-assets.md` (keep a few unifying elements consistent; check silhouettes and colour focus; art bible), `Roblox/roblox-kb/building-and-level-design.md` (distinct materials for indoor/outdoor and team zones on purpose), `Roblox/roblox-kb/optimization-and-streaming.md` (one tester's ratings: Neon 3/5 and glass 3/5 lag, indie, single source). The 2 percent threshold and bucket size are this skill's defaults.

## Output
```
STYLE AUDIT: Workspace visible parts=8120 materials=9 colour-buckets=31 neon=44 glass=12
top material: SmoothPlastic 52%, Wood 21% ...   candidate outliers: Neon 44, Brick 17, CorrodedMetal 3
Decisions: keep Neon (signs), fix Brick (3 builds), CorrodedMetal (1 asset, re-skin)
```

## Acceptance checks
- [ ] The audit ran and the report copies its counts.
- [ ] Every outlier has a keep/fix decision with a reason.
- [ ] Terrain and fully transparent parts were not counted (the script skips them).
- [ ] No instance was changed by this skill (read-only run).
- [ ] At least one screenshot backs the decisions.

## Pitfalls
Treating rarity as wrongness. Counting parts instead of visible area: a few huge parts dominate what players see, so also look at the picture. Colour buckets merge shades but cannot tell paint from lighting. SurfaceAppearance/MaterialVariant overrides change how a Material looks without changing the enum: a "Plastic" part may be styled. Terrain materials are not in this count.

## Related
`palette-picker`, `art-bible-writer`, `model-cleaner`, `texture-budget-checker`, `lighting-preset-picker`.
