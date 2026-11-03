---
name: art-bible-writer
description: "Write a short art bible a team can follow - palette with checked contrast, shape language, material and lighting rules, detail level, UI style, do and do-not examples - from the game's fantasy and its mobile-first constraints, and test the draft against the place. Use before art production or when several builders disagree on the look."
category: build
tags: art bible, style guide, palette, shape language, materials, silhouette, art direction, consistency
kb: Roblox/roblox-kb/building-art-and-assets.md, Roblox/roblox-kb/ui-ux-design.md, Roblox/roblox-kb/development-process-and-speed.md, Roblox/roblox-kb/thumbnails-icons.md
related: palette-picker, material-consistency-checker, lighting-preset-picker, world-theme-picker, graybox-builder
---

# art-bible-writer

A style guide is how several people (or an AI and a human) produce one game's worth of art. The vault is explicit: decide the style early, document shapes, colours, UI, fonts, padding and character design, and keep 4-5 things consistent. This writes that document from a few answers and then checks it against reality with two other skills' scripts.

## When to use
Before art production, when a team grows, when imported assets clash, or when a reviewer says "no cohesive look". Not for: choosing the setting (`world-theme-picker`), or auditing an existing place (`material-consistency-checker`).

## Inputs (max 2)
1. The game's fantasy in one sentence and the audience (mostly phones and younger players is the default). 2. Two or three reference images or games the style should feel like, and one it must not.

## Procedure
1. Gather: spend a short time on a mood board of real references (take the best parts of several), then sketch what locks the style. Note the art-budget reality: a solo builder reuses and recolours assets (vault: cadence updates are mostly art reskins of existing assets).
2. Decide the five unifying elements the bible will protect: lighting, materials, palette, detail level, silhouette. Everything else may vary on purpose.
3. Palette: choose 5-8 colours with roles (ground, structure, accent, hazard, UI background, UI text). Run them through `palette-picker` (`Palette.check`): text contrast at least 4.5, pairs distinct under colour-blind simulation and in monochrome. Record the hex values.
4. Shape language: one sentence plus three do and three do-not sketches or examples (chunky rounded shapes versus angular; thick outlines versus none). Chunky shapes read on small screens and keep detail low around avatars.
5. Materials: the allowed Material enums and any MaterialVariants; one rule for neon and glass (accents only); texture style (cartoon or realistic, baked lighting or not).
6. Lighting and sky: name a mood preset (`lighting-preset-picker`) and the time of day; the skybox must match the light direction.
7. UI: font choices readable at the smallest phone size, padding (about 15 px), corner radius (about 6 px) and a limited palette, as the vault describes.
8. Output the bible as one page (template below) and add a "how to check" line per rule. Then test it: run `material-consistency-checker` on the place and compare its top materials and colours with the bible; list conflicts.
9. Review with the team; version it (date at the top) and keep it next to the project.

Template: 1 Fantasy and audience | 2 References (is / is not) | 3 Palette with roles and hex | 4 Shape language and silhouette rules | 5 Materials and textures | 6 Lighting and sky | 7 Detail budget (triangles, parts per area) | 8 UI style | 9 Do / do not examples | 10 Checks.

## Studio MCP path
Optional: `list_roblox_studios` -> `execute_luau` (Edit) with the `material-consistency-checker` script to compare reality with the draft -> `screen_capture` of 3 representative areas for the do/do-not section.

## Fallback
Entirely doable without Studio from references and the palette module under Lune. Only the comparison against the real place is `untested`.

## Evidence
`Roblox/roblox-kb/building-art-and-assets.md` (write an art bible and style sheet and decide style early; keep 4-5 things consistent; check silhouettes and colour focus; mobile-first; design for colour accessibility: WCAG-based contrast, never colour alone, check in grayscale), `Roblox/roblox-kb/ui-ux-design.md`, `Roblox/roblox-kb/development-process-and-speed.md`. Padding and radius figures are the vault's example values, not rules.

## Output
One markdown page following the template, plus a "conflicts found in the current place" list and the palette check result (issue count from `Palette.check`).

## Acceptance checks
- [ ] Every palette pair that carries text passes contrast 4.5 (checked with the module, result quoted).
- [ ] Colour-blind and grayscale checks ran on the palette and any flagged pair has a fix (outline, icon, or hue shift).
- [ ] Each rule has a how-to-check line.
- [ ] The draft was compared with the real place and conflicts listed.
- [ ] The page fits one screen of reading; examples are patterns, not copied art.

## Pitfalls
A bible nobody checks. Copying a game's actual assets or palette rather than learning its principles. Too many rules (keep them to the five unifying elements). Realistic textures for a phone-first cartoon game. Colour as the only signal for teams or hazards.

## Related
`palette-picker`, `material-consistency-checker`, `lighting-preset-picker`, `world-theme-picker`, `graybox-builder`.
