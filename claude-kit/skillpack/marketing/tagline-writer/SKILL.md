---
name: tagline-writer
description: "Write short taglines and hook lines for a Roblox game's ads, posts and page opener: 3-7 words that state the action and the payoff, each checked with title_screen.py and against the game's real features. Use when a trailer, ad, short-form caption or page needs a one-line hook; titles are title-generator."
category: marketing
tags: tagline, hook, slogan, caption, ad copy, one liner, call to action, short form
kb: Roblox/roblox-kb/titles-descriptions.md, Roblox/roblox-kb/trailers-and-video-marketing.md, Roblox/roblox-kb/ads-and-sponsored-experiences.md, Roblox/roblox-kb/thumbnails-icons.md
related: title-generator, game-description-writer, short-video-planner, trailer-script-writer, sponsored-ad-reviewer, update-announcement-writer
---

# tagline-writer

A tagline is the line that sits next to a thumbnail or opens a clip. It has one job: make the first two seconds clear. Hooks in the first seconds are the vault's repeated advice for short-form (trailers-and-video-marketing); a hook that the game cannot deliver is the same clickbait the discovery system now penalises through first-play bounce.

## When to use
You need a line for an ad, a caption, a post header, a store opener or a thumbnail word. Not for: the title (`title-generator`), the full description (`game-description-writer`), update posts (`update-announcement-writer`).

## Inputs (max 2)
1. The core loop and its single best moment (default: `GAME.md`, `design/core-loop.md`). 2. Surface and length limit (default: caption or ad line, unknown limit: live-check the surface).

## Procedure
1. Find the moment worth a line: the action a stranger repeats, the surprise, or the payoff number. Use real, current features only (vault: show what players will actually do).
2. Write 12 candidates in four shapes: action ("Steal eggs. Do not get caught."), question the game answers, contrast ("Noob to boss in one hour" only if true), number plus setting ("99 nights, one forest"). 3-7 words each, plain words, no emoji chains.
3. Put the candidates in `taglines.txt` and run `python -I ~/.claude/claude-kit/skillpack/marketing/title-generator/scripts/title_screen.py --file taglines.txt --min-words 3 --max-words 7 --max-emoji 1`. Drop FAIL rows (repeats, reward promises, random caps).
4. Truth check each survivor against a real feature or clip; delete any line that promises a reward, rank, drop rate or feature that the game does not have today.
5. Surface fit: for on-platform video there is no promo text allowed (see `trailer-script-writer`), so the line lives in the caption or page, not on the footage; for ad creatives text stays minimal (0-3 words on the image); for short-form put the exact game name in the caption so viewers can search it.
6. Pick 3: one for ads, one for short-form hook (spoken or subtitled in the first 2 s), one for the page opener. Pair with the matching thumbnail; test one line at a time (`ctr-ab-test-planner`).

## Studio MCP path
Not needed.

## Fallback
Same; this is text. Everything is `untested` until a surface shows it and numbers come back.

## Evidence
`Roblox/roblox-kb/trailers-and-video-marketing.md` (hook in the first seconds; first 2 seconds for Shorts; game name in captions; polished ad creative vs lo-fi organic), `Roblox/roblox-kb/titles-descriptions.md` (do not lead with money rewards; keep metadata true; keyword-style verb statements; front-load about 160 characters), `Roblox/roblox-kb/ads-and-sponsored-experiences.md` (simple creatives can beat expensive art; test one element), `Roblox/roblox-kb/thumbnails-icons.md` (minimal text, 0-3 words). Surface rules for text and video change: live-check.

## Output
`marketing/taglines.md`: table (line, shape, surface, the real feature that backs it, screen result), the 3 picks, what was cut and why.

## Acceptance checks
- [ ] `title_screen.py` output quoted; every pick is PASS.
- [ ] Each pick names the feature or clip that proves it.
- [ ] 3-7 words; no reward promise; no third-party names.
- [ ] Game name appears in the caption version.
- [ ] Surface text rules were live-checked and dated.

## Pitfalls
Promising drops or prizes. Long lines that wrap off a phone. Wordplay that needs context. Using the same line on every surface. Overlaying promo text on on-platform gameplay video, which the guidelines forbid.

## Related
`title-generator`, `game-description-writer`, `short-video-planner`, `trailer-script-writer`, `sponsored-ad-reviewer`.
