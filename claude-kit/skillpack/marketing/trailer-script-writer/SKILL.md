---
name: trailer-script-writer
description: "Script a Roblox game video in the right mode: the strict on-platform gameplay preview (real footage, no cinematic, promo text, voiceover or lyrics) or an external 60-90 second trailer (hook, features, title card, call to play). Outputs a shot-by-shot list with timings, capture notes and a rules check. Use when planning a page video, trailer or video ad."
category: marketing
tags: trailer, video, gameplay preview, script, shot list, hook, freecam, call to action, video ad, moments
kb: Roblox/roblox-kb/trailers-and-video-marketing.md, Roblox/roblox-kb/thumbnails-icons.md, Roblox/roblox-kb/discovery-algorithm.md, Roblox/roblox-kb/ads-and-sponsored-experiences.md
related: short-video-planner, screenshot-set-planner, tagline-writer, thumbnail-maker, launch-teaser-planner, store-page-audit
---

# trailer-script-writer

Two different products share the word "trailer". The vault's key finding: on-platform page videos must show real, current gameplay and forbid cinematic trailers, dramatised gameplay, promo text, real-life footage, voiceover, narration and lyric music; external trailers (YouTube, X, paid social) may use a hook / features / title card / call to action structure. Mixing the two gets the upload rejected, and a rejected upload still uses the monthly quota. Choose the mode first. Short vertical clips are `short-video-planner`.

## When to use
You need a page video, a trailer or a video ad script. Not for: gallery stills (`screenshot-set-planner`), 10-20 second Shorts (`short-video-planner`).

## Inputs (max 3)
1. Mode: page (on-platform), external trailer, or paid ad. 2. Core loop and the three best moments (default: `GAME.md`). 3. Features that exist today, in a list (default: ask; never script an unbuilt feature).

## Procedure
1. Live-check the current rules and limits for page videos (format, length, review, monthly upload quota, forbidden content) and any ad video rules. Write them with the date. The vault's September 2026 note says YouTube embeds were removed from game pages on 2026-09-30, so page video means an uploaded file; confirm live.
2. Page mode: an authentic play-through of the core loop from the player's point of view, shown in the first seconds; pick clips with a story arc and pacing shifts (calm to action); camera work, minor post-processing and a logo overlay are allowed only if they show real mechanics; no promo text or voiceover. Keep it short enough to loop; the first seconds carry the hook.
3. External mode (vault, rasdev, indie): 60-90 s total; 5-10 s high-action hook; 15-20 s core features and the map; then combat and other features; end with title card and call to play; cut to the beat. Use real in-game footage over heavy animation; a trailer cannot save a weak game.
4. Ad mode: lead with the thumbnail's promise, keep text minimal, polished loops are fine for paid social while lo-fi suits organic short form (Deconstructor of Fun, self-reported). Include the Details Page URL where links are allowed.
5. Write the shot list: time range, what is on screen, camera, the feature it proves, sound note (no lyrics for page mode). Mark each shot "exists in game today: yes/no"; remove every no.
6. Capture plan: Studio freecam with hidden UI, narrow FOV for scale, depth of field, bloom, colour correction, Player Lock to follow the hero; or `screen_capture` stills as a fallback.
7. Put the shot table in `shots.csv` (columns `start,end,scene,in_game,text_overlay,voiceover`) and run `python -I ~/.claude/claude-kit/skillpack/marketing/trailer-script-writer/scripts/shot_check.py shots.csv --mode <external|page|ad>` with the live limits if they differ from the 60-90 s and 10 s defaults. It checks existence in the game, order and gaps, total length, hook length and, in page mode, overlay and voiceover; cinematic style, lyrics and real-life footage stay human checks. Then rules check against step 1 (list each rule, tick or fix). Estimate production time honestly (the vault reports 40-60 minutes per short; trailers take longer).
8. The owner uploads; you never upload.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `screen_capture` for stills and shot checks; footage itself is recorded in Studio or the Roblox client by the owner. `execute_luau` (Edit) only for camera staging, with permission.

## Fallback
The script and shot list as a document; the owner records. Every shot stays `untested` until footage exists and passes review.

## Evidence
`Roblox/roblox-kb/trailers-and-video-marketing.md` (upload as a file; show real current footage; forbidden elements; 60-90 s external structure; hook window; freecam capture; Roblox's reported play-time gain from real gameplay video is second-hand; Moments and hover previews use page video), `Roblox/roblox-kb/thumbnails-icons.md` (video thumbnail quota; limit edits to real mechanics; a gameplay-video test showed plays up 47% in a Standout Games test, not guaranteed), `Roblox/roblox-kb/discovery-algorithm.md` (video previews: directional test gains from Roblox in 2026), `Roblox/roblox-kb/ads-and-sponsored-experiences.md`. Rules and quotas change: live-check.

## Output
`marketing/video-script-<mode>.md`: mode, live rules with date, shot table (time, scene, camera, feature proved, exists today), capture plan, rules-check list, time estimate, upload checklist.

## Acceptance checks
- [ ] The mode is stated and the script obeys that mode's rules (no promo text or voiceover in page mode).
- [ ] `shot_check.py` exit 0 on `shots.csv` (output quoted); every shot is marked as existing in the game today.
- [ ] Rules cited with a source and date from this run.
- [ ] External mode totals 60-90 s with a 5-10 s hook, or the deviation is explained.
- [ ] Nothing was uploaded or published.

## Pitfalls
Using the external structure for a page video. Showing an unreleased feature. Music with lyrics. Over-polished footage that no longer looks like the game. Spending the monthly quota on an unchecked upload.

## Related
`short-video-planner`, `screenshot-set-planner`, `tagline-writer`, `launch-teaser-planner`, `store-page-audit`.
