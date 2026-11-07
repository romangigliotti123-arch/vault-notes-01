---
name: brand-kit-builder
description: "Define a game's brand kit so every asset looks like one game: colour palette checked for contrast with contrast.py, logo lockup rules, character art notes, fonts, tone of voice and a one-page style guide. Use when thumbnails, icon, UI, posts and videos do not look like they belong together, or before commissioning art."
category: marketing
tags: brand, style guide, palette, logo, colours, fonts, tone, contrast, consistency, wcag
kb: Roblox/roblox-kb/thumbnails-icons.md, Roblox/roblox-kb/trailers-and-video-marketing.md, Roblox/roblox-kb/ui-ux-design.md, Roblox/roblox-kb/titles-descriptions.md
related: game-icon-maker, thumbnail-maker, screenshot-set-planner, press-kit-builder, roblox-group-setup, mobile-ui-audit
---

# brand-kit-builder

Vault: keep icon and thumbnails consistent so players recognise the game, keep title, colours and characters when redesigning, and build a durable style guide (logos, lockup, character art) that stays in use for years and is applied across trailers, thumbnails and Shorts. The kit is small on purpose: a palette that passes contrast, a logo rule, a character rule, a font choice and a voice.

## When to use
Before commissioning art, when assets drift, or when a rebrand is planned. Not for: making the thumbnail itself (`thumbnail-maker`) or in-game UI layout (`mobile-ui-audit`).

## Inputs (max 3)
1. Core fantasy and genre (default: `GAME.md`). 2. Existing art or the top 3 reference games' look (read for pattern, never copy). 3. Audience age (default: young, mobile-first).

## Procedure
1. Mood: pick one word each for emotion and energy (cosy, intense, mysterious). Vault colour mapping: bright saturated for fantasy or dreamy, muted for somber, high contrast for horror; bright colour for crucial text and buttons; horror avoids oversaturated brights.
2. Palette: 1 background, 1 text, 1 primary accent, 1 secondary accent, 1 warning. Put hex values in `brand/palette.json` (`{"bg": "#...", "text": "#...", "accent": "#..."}`).
3. Contrast: `python -I .rbx/claude-kit/skillpack/marketing/brand-kit-builder/scripts/contrast.py --palette brand/palette.json` and again with `--large` for big text and UI shapes. Every text/background pair must pass its level; fix the palette, not the check. Avoid the vault's named bad pairing, white on yellow.
4. Logo and title lockup: one wordmark, a light and a dark version, a minimum size at which it stays readable on a phone, clear space rule, no thin white strokes that vanish on bright backgrounds.
5. Characters and subjects: the hero's silhouette, one signature colour, the expressions allowed; match Roblox's platform visual style rather than something unrecognisable, unless realism fits the genre (vault).
6. Type: at most two fonts, one for display and one for body; mobile-readable sizes; text in thumbnails 0-3 words.
7. Voice: five rules for posts and updates (friendly, short, honest about changes, no hype adjectives, no reward promises) with two sample lines.
8. Assemble `brand/STYLE.md` (one page) and a `brand/assets/` folder list; use it in `game-icon-maker`, `thumbnail-maker`, `screenshot-set-planner`, `press-kit-builder`.
9. Review annually or at a rebrand; keep title, colours and characters stable through redesigns.

## Studio MCP path
Optional: `list_roblox_studios` -> `get_studio_state` -> `screen_capture` to check that the in-game UI palette matches `palette.json`. No changes are made.

## Fallback
Files and a style page. Visual checks on a phone are `untested` unless seen on a phone.

## Evidence
`Roblox/roblox-kb/thumbnails-icons.md` (consistent theme and recognisable style; map colour to mood and hierarchy; verify text and UI contrast against WCAG; avoid white on yellow; text and logos checked at mobile size; match platform visual style; originality over cloning), `Roblox/roblox-kb/trailers-and-video-marketing.md` (durable style guide for brand assets, Deconstructor of Fun, self-reported), `Roblox/roblox-kb/ui-ux-design.md`, `Roblox/roblox-kb/titles-descriptions.md` (anchor the brand to one niche theme, indie). Contrast levels are WCAG 2.x (4.5 and 3.0).

## Output
`brand/STYLE.md`, `brand/palette.json`, `brand/contrast-report.txt` (the tool's output), and an asset list.

## Acceptance checks
- [ ] `contrast.py` exit 0 for both runs, output saved to `brand/contrast-report.txt`.
- [ ] Palette has at most six colours, each with a named role.
- [ ] Logo minimum size and clear space written down.
- [ ] Only two fonts; all fonts are usable under their licence (owner confirms).
- [ ] Voice rules include "no reward promises".

## Pitfalls
A palette picked from a screenshot of a rival. Rebranding every update. Brand colours that fail contrast on phones in sunlight. Many fonts. Letting each asset invent its own look.

## Related
`game-icon-maker`, `thumbnail-maker`, `screenshot-set-planner`, `press-kit-builder`, `roblox-group-setup`.
