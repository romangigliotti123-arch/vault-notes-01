---
name: thumbnail-guideline-checker
description: "Check the icon, thumbnails and video thumbnails against the current Creator Docs rules (size, aspect, safe area, authentic gameplay, no price claims, number of active thumbnails) by running the pack's header-only image check with live-checked specs and reviewing content rules by eye. Use before upload and before a re-skin."
category: publish
tags: thumbnail, icon, image specs, video thumbnail, content guidelines, store page, moderation, aspect ratio, publish
kb: Roblox/roblox-kb/thumbnails-icons.md, Roblox/roblox-kb/titles-descriptions.md, Roblox/roblox-kb/trailers-and-video-marketing.md, Roblox/roblox-kb/age-ratings-moderation-and-tos.md
related: thumbnail-maker, experience-settings-configurator, experience-name-checker, copyright-checker, game-icon-maker, store-page-audit
---

# thumbnail-guideline-checker

One job: a pass/fail on the store images BEFORE upload, so a rejected thumbnail does not burn quota or delay launch. It does not make images (`thumbnail-maker`, `game-icon-maker`) and does not judge appeal (`store-page-audit`). It reuses `marketing/thumbnail-maker/scripts/image_specs.py`, which reads PNG/JPEG headers only and takes the spec numbers as arguments; the numbers come from the live Creator Docs pages (`live-check`: sizes and rules change), then the content rules are checked by eye against the same pages.

## When to use
Before uploading an icon or thumbnail, before a major update's new thumbnail set, and after a rejection. Not for: designing the image (`thumbnail-maker`), CTR testing (`ctr-ab-test-planner`), licence of the art (`copyright-checker`).

## Inputs (max 2)
1. The image files. 2. Which slot each is for: icon, image thumbnail or video thumbnail.

## Procedure
1. Open the live thumbnails and icons pages (Evidence). Write down the current sizes, aspect ratios and content rules with the date.
2. Thumbnails: `python -I .rbx/claude-kit/skillpack/marketing/thumbnail-maker/scripts/image_specs.py thumb1.png thumb2.png --expect <WxH> --aspect <A:B>` with the live numbers (the 2026-10-28 note says 16:9 at 1920x1080).
3. Icon: `python -I .../image_specs.py icon.png --aspect 1:1 --min-width <live minimum>` (the note says square, at least 512 px, previewed at about 150 px).
4. Content rules by eye (from the pages): authentic gameplay in video thumbnails; no misleading visuals, voiceover or promo claims such as "50% off"; essential text off the bottom edge (player-count metadata covers it); nothing ambiguous; no default auto-generated icon; no copied logos or characters.
5. Count: the page advises activating several thumbnails (2-5 in the note) so personalisation can work; record the planned number in the settings sheet (`experience-settings-configurator`).
6. Moderation: icons and thumbnails are moderated before they show to others, so upload early and keep the launch image set approved a day ahead.
7. After upload, compare the live store page to the files; judge results by qualified play-through rate per the page, not impressions.
8. Write `release/images.md`: file table (file, slot, size, script verdict), eye-check notes, page dates.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> no MCP tool uploads store images: thumbnails and icons are Creator Hub uploads by the owner. Studio's thumbnail tool may capture a viewport image (`start_stop_play` to frame it); the file then goes through the script.

## Fallback
Fully offline: the script and a human review. Moderation outcome and live rendering are `untested` until uploaded.

## Evidence
Official (live-check): `Roblox/docs/Videos/2026-10-28 - Docs production publishing thumbnails.md` (16:9 at 1920x1080; keep text off the bottom edge; authentic gameplay; no promo claims; 2-5 active; measure by qualified play-through rate), `... Docs production publishing experience-icons.md` (square, at least 512 px, check at about 150 px, avoid the default icon, moderation before display), `... Docs marketplace custom-thumbnails.md` (Marketplace items; separate rules). Pack: `Roblox/roblox-kb/thumbnails-icons.md`, `Roblox/roblox-kb/trailers-and-video-marketing.md`.

## Output
`release/images.md`.

## Acceptance checks
- [ ] `image_specs.py` ran with specs taken from the live page (quote its summary line).
- [ ] Each image has an eye-check note for every content rule.
- [ ] The number of active thumbnails is decided.
- [ ] The page date is recorded.
- [ ] `image_specs.py --selftest` prints `selftest ok`.

## Pitfalls
Using last year's size. Uploading a stretched non-16:9 image. Text in the bottom strip. A video thumbnail that shows something the game cannot do. Counting a rejected upload as free (the note says it still counts against the quota).

## Related
`thumbnail-maker`, `experience-settings-configurator`, `experience-name-checker`, `copyright-checker`, `game-icon-maker`, `store-page-audit`.
