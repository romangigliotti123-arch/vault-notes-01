---
name: world-theme-picker
description: "Choose a setting and art direction that matches the core fantasy, reads at phone size and is cheap to build: score 3-5 candidate themes on fit, readability, cost and thumbnail strength, and record a palette and style rule set. Use after the fantasy is defined, before assets are bought or made."
category: design
tags: theme, setting, art direction, style, palette, low poly, mobile, readability, thumbnail, cost
kb: Roblox/roblox-kb/building-art-and-assets.md, Roblox/roblox-kb/game-ideas-and-genres.md, Roblox/roblox-kb/ui-ux-design.md, Roblox/roblox-kb/thumbnails-icons.md, Roblox/roblox-kb/cross-platform-and-console.md
related: core-fantasy-definer, one-sentence-pitch, level-flow-planner, lighting-preset-picker, thumbnail-maker, ui-kit-consistency-checker
---

# world-theme-picker

Vault: pick simple, culturally neutral concepts for ages 9-14; mobile can be 70-80 percent of players, so readability on a small screen decides; kids forgive mid builds if the game is playable (fun beats graphics). This skill picks the theme with cost and readability in mind, not taste alone.

## When to use
After `core-fantasy-definer`, before building or buying assets. Not for: lighting (`lighting-preset-picker`), UI kits (`ui-kit-consistency-checker`), thumbnail art (`thumbnail-maker`).

## Inputs (max 3)
1. Core fantasy and genre (default: `design/fantasy.md`). 2. Art budget: hours or money, and who builds (default: solo, low). 3. Asset policy (default: own parts, free Creator Store assets with licences checked).

## Procedure
1. Generate 3-5 candidate themes that fit the fantasy (setting plus visual style, e.g. cosy farm, neon arcade, spooky mansion).
2. Score each 0-5 on: Fantasy fit (does it make the role obvious in 5 seconds), Mobile readability (silhouettes, contrast, not dark or noisy at phone size), Build cost (parts, textures, unique assets; modular kits cheap), Thumbnail strength (a clear subject on a simple background), Reuse (assets can serve future updates and seasons), Differentiation (not a copy of the reference's look). Sum and rank; the score is a conversation, not a law.
3. Check the top theme against pitfalls: dark tones that fail on dim phones, busy ground textures that hide pickups, too many unique props. Test by taking a 100 px screenshot of a greybox with the proposed palette; the player, pickups and goal must still stand out.
4. Record the style rules: palette of 5-7 colours (reward = brightest, danger = one colour), shape language (round for friendly, angular for threat), material limit, prop density, font, one signature element that makes the theme recognisable.
5. Cost plan: list the 10 assets the first area needs, mark build or reuse or buy; keep under the art budget; plan modular tiles.
6. Seasonal reuse: note two re-themes (holiday, event) the style supports.
7. Save `design/theme.md`; run the doc check.

## Studio MCP path
Design only. After a greybox: `screen_capture` at phone resolution to run the 100 px readability test; `execute_luau` (Server) to count parts per area for the cost line.

## Fallback
Pure document and a mood board of descriptions (never copy another game's art).

## Evidence
`building-art-and-assets` (style consistency, modular kits), `game-ideas-and-genres` (simple neutral concepts for young players; niche can still win per official guidance), `ui-ux-design` (mobile-first readability), `thumbnails-icons` (readable at small size), `cross-platform-and-console`.

## Output
`design/theme.md`: candidate score table, chosen theme, style rules (palette, shapes, materials, font), first-area asset plan with build/reuse/buy, seasonal reuse.

## Acceptance checks
- [ ] At least 3 candidates scored with the same criteria.
- [ ] A 100 px mobile readability check result is recorded (or marked `untested`).
- [ ] Asset plan stays under the stated budget.
- [ ] Executed: `python gdd-one-pager/scripts/docheck.py design/theme.md --kind theme` prints PASS.

## Pitfalls
Picking for personal taste. Realism that costs months. Dark mood with no readable pickups. Mixing five art styles from free assets.

## Related
`core-fantasy-definer`, `one-sentence-pitch`, `level-flow-planner`, `lighting-preset-picker`, `thumbnail-maker`.
