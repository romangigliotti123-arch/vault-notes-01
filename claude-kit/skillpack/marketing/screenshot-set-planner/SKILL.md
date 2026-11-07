---
name: screenshot-set-planner
description: "Plan the gallery of images and clips on a Roblox experience page so each one sells a different part of the loop: shot list, capture method, order, captions, and a spec and honesty check. Use when the page has no gallery, only menu screenshots, or after a big update changed what the game looks like."
category: marketing
tags: screenshots, gallery, images, details page, shot list, capture, freecam, loop, conversion
kb: Roblox/roblox-kb/thumbnails-icons.md, Roblox/roblox-kb/trailers-and-video-marketing.md, Roblox/roblox-kb/titles-descriptions.md, Roblox/roblox-kb/discovery-algorithm.md
related: thumbnail-maker, game-icon-maker, store-page-audit, trailer-script-writer, short-video-planner, brand-kit-builder
---

# screenshot-set-planner

The details page takes extra images and video (vault: up to 10 per the docs, live-check). Each slot should answer one question a hesitant player has: what do I do, what do I get, who do I play with, how does it look, what is new. This skill plans and checks the set. Thumbnail composition is `thumbnail-maker`.

## When to use
Filling or refreshing the gallery. Not for: the 16:9 thumbnails, the icon, or ads.

## Inputs (max 2)
1. Core loop and the 3 best moments (default: `GAME.md`). 2. Current gallery if any (default: none).

## Procedure
1. Live-check the current image count, size and format rules for the page and the rules for video (approval, monthly upload limits). Write them with the date. Vault: gameplay video uploads are reviewed and have a monthly quota, and rejected uploads still consume it, so pre-check footage.
2. Questions to answer, in this order (the first two images are seen most): (1) the core action in progress, (2) the reward moment, (3) the progression or collection screen with real numbers, (4) social: friends together, trading or a party, (5) the newest content, (6) the variety (maps, items, modes), (7) the monetisation view only if it is honest and not first. Fewer than 6 is fine; do not pad.
3. For each slot write: what is on screen, where the camera is, the one caption (0-6 words, optional), and the real feature it proves.
4. Capture plan: Studio freecam with UI hidden (vault freecam shortcuts), narrow field of view for scale, depth of field and bloom for polish; capture from the spawn point of view for authenticity; 16:9; high resolution. Keep the hero subject in the central area. No UI overlays, no off-platform art, no CGI.
5. Consistency: same time of day, same colour grade, the style guide from `brand-kit-builder` when it exists; the gallery should look like one game.
6. Check files with `python -I .rbx/claude-kit/skillpack/marketing/thumbnail-maker/scripts/image_specs.py gallery/*.png --expect <WxH from step 1> --aspect 16:9 --max-mb <N>`.
7. Honesty pass: every image shows what a new player can actually do or see today; remove anything that needs a paid item to appear without saying so.
8. Order, caption, and give the owner the upload checklist. Refresh at major updates.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> stage with `execute_luau` (Edit) only with permission (camera, lighting, hide UI; never save the place) -> `screen_capture` per shot. `insert_asset` for props if a scene is thin.

## Fallback
Without Studio: the shot list as a request to the owner (what to capture, where, with HUD hidden); mark all image checks `untested` until files exist.

## Evidence
`Roblox/roblox-kb/thumbnails-icons.md` (complete metadata and visuals on every surface; up to 10 images and videos on the details page; build thumbnails from a Studio scene with UI hidden; honest gameplay; video quota 3 per month, rejected uploads consume it), `Roblox/roblox-kb/trailers-and-video-marketing.md` (freecam capture settings; real current footage only; page videos feed discovery surfaces), `Roblox/roblox-kb/titles-descriptions.md` (store media), `Roblox/roblox-kb/discovery-algorithm.md` (video previews give context; directional test gains are Roblox figures, not guarantees). Counts and quotas change: live-check.

## Output
`art/gallery-plan.md`: live specs and date, slot table (order, question answered, scene, camera, caption, feature proved, file), check results, upload checklist.

## Acceptance checks
- [ ] Every slot answers a different question and names the feature that backs it.
- [ ] Specs are cited with a date from this run; `image_specs.py` exit 0 (or `untested`).
- [ ] No UI overlays, CGI or content the game cannot show today.
- [ ] The first two slots are the action and the reward.
- [ ] Nothing uploaded by the skill.

## Pitfalls
Eight menu screenshots. Captions that promise more than the game. Mixed art styles. Showing late-game content to new players as if it were the start. Uploading rejected footage and burning the quota.

## Related
`thumbnail-maker`, `game-icon-maker`, `store-page-audit`, `trailer-script-writer`, `brand-kit-builder`.
