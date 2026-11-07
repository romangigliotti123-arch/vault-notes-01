---
name: game-icon-maker
description: "Design and check a Roblox game's square icon so it reads at phone size and stands out against its neighbours on the feed: concept, composed art from a real render, glance test, spec check, and 2-3 icon variants one variable apart. Use when the icon is the default art, a raw screenshot, or weak next to competitors; the 16:9 thumbnails are thumbnail-maker."
category: marketing
tags: icon, game icon, square, 512, glance test, feed, neighbours, face, contrast, ctr
kb: Roblox/roblox-kb/thumbnails-icons.md, Roblox/roblox-kb/discovery-algorithm.md, Roblox/roblox-kb/ab-testing-and-experiments.md, Roblox/roblox-kb/titles-descriptions.md
related: thumbnail-maker, ctr-ab-test-planner, title-generator, brand-kit-builder, rbx-thumbnail, thumbnail-guideline-checker, store-page-audit
---

# game-icon-maker

The icon is shown on the Home feed beside many other icons, so it is judged against its neighbours, not alone (vault: thumbnails-icons, "Design the icon to differ from its grid neighbours"). One job: decide what the icon shows, build it from a real render, and prove it survives shrinking. The wide thumbnails are `thumbnail-maker`; the test design is `ctr-ab-test-planner`.

## When to use
The icon is the auto-generated default, a raw screenshot or plain AI art, or looks the same as the genre's other icons. Not for: 16:9 thumbnails, ad creatives (`rbx-thumb-brief`), badge/pass icons.

## Inputs (max 3)
1. Game name, genre and core fantasy (default: `GAME.md`). 2. The hero subject: character, pet, vehicle (default: the most repeated thing in the loop). 3. Three or four genre-neighbour icons to compare with (default: top charts for the genre, looked at live).

## Procedure
1. Live-check the current icon requirements on Creator Docs (size, format, file size, content rules). Vault says a 512x512 square stays sharp and scales to about 150x150 in places; write what you find with the date into `art/icon-plan.md`, never from memory.
2. Read the rules: `python -I .rbx/claude-kit/tools/kbq.py section thumbnails-icons rules --max-chars 4000`. Note the flags: raw screenshots and plain AI icons are called the worst options in the newest indie guidance; the vault also holds older conflicting views (`section thumbnails-icons disagree`).
3. Concept: one subject filling the frame, a large readable expression (grin, fear, shock) if it has a face, blue or green backdrop with a red or vivid subject for instant read (indie, multiple creators), one progression cue only if true (for example a growth number). Horror: mood and shadow, not oversaturated brights.
4. Neighbour pass: put the 3-4 neighbour icons beside a mock of yours. Ask: what colour and shape do they share, and what can I do that is different and still honest. Write the answer in one line.
5. Build 2-3 variants one variable apart (expression, backdrop colour, subject crop). Base is a real render (`thumbnail-maker` step 3); AI art only for background. No text unless one short word survives step 6.
6. Glance test: shrink to about 150x150, look away, look back. If you cannot say the game and its feel in one sentence, redesign (vault: half-second rule).
7. Check specs with the live numbers: `python -I .rbx/claude-kit/skillpack/marketing/thumbnail-maker/scripts/image_specs.py art/icon*.png --expect <WxH> --aspect 1:1 --max-mb <N>`.
8. Consistency: icon, thumbnails and title share colours, character and tone (vault: keep a consistent recognisable style; `brand-kit-builder`).
9. Hand the variants to `ctr-ab-test-planner`. The owner uploads; you never upload.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> stage the hero close-up (UI hidden) -> `screen_capture`. Optional `execute_luau` (Edit) to set camera and lighting in the user's named place, ask first, never save the place. Files go in `art/`.

## Fallback
No Studio: write `art/icon-plan.md` with the shot list for the owner (hero, angle, expression), the neighbour comparison table and the checks; mark every image check `untested` until files exist.

## Evidence
`Roblox/roblox-kb/thumbnails-icons.md` (512x512 square; theme and genre in the icon; one icon per locale; neighbours; large emotive face; raw screenshots and AI icons labelled worst by one 2026 creator; test icon and thumbnail separately), `Roblox/roblox-kb/discovery-algorithm.md` (custom thumbnail required for Home recommendations; icon judged against front-page competition, unverified pickup anecdote), `Roblox/roblox-kb/ab-testing-and-experiments.md` (test title and thumbnail as pairs). Sizes and limits change: live-check.

## Output
`art/icon-plan.md`: live specs with date, concept line, neighbour table, variant table (id, the one variable, file), check table per file (glance, spec, honesty), upload checklist. Images in `art/`.

## Acceptance checks
- [ ] Specs carry a source and date from this run.
- [ ] Each icon passed the 150 px glance test, noted pass/fail.
- [ ] `image_specs.py` exit 0 on every final file (or `untested` if no files).
- [ ] The icon was compared beside neighbours and the difference is written down.
- [ ] Variants differ by exactly one variable.
- [ ] No third-party characters, logos or real people; content matches the game.

## Pitfalls
Detail that disappears at 150 px. Copying the top icon's layout and colours so it blends in. Text that is unreadable on a phone. Clickbait that raises clicks and early leaves. Changing icon and thumbnail together so the test cannot be read.

## Related
`thumbnail-maker`, `ctr-ab-test-planner`, `title-generator`, `brand-kit-builder`, `store-page-audit`.
