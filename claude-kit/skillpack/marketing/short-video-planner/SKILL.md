---
name: short-video-planner
description: "Plan a month of short vertical clips (TikTok, YouTube Shorts, Reels) for a Roblox game: clip ideas that show the hook in 2 seconds, a repeatable format, caption rules, cadence, and a tracker that finds the over-1,000-view pattern. Use when starting short-form promotion or when clips get views but no plays."
category: marketing
tags: tiktok, shorts, reels, short form, clips, hook, caption, cadence, devlog, organic, vertical
kb: Roblox/roblox-kb/trailers-and-video-marketing.md, Roblox/roblox-kb/social-features-and-virality.md, Roblox/roblox-kb/influencer-and-creator-marketing.md, Roblox/roblox-kb/titles-descriptions.md
related: trailer-script-writer, social-post-calendar, tagline-writer, influencer-outreach-writer, community-showcase-planner, launch-teaser-planner
---

# short-video-planner

Short-form is the vault's cheapest acquisition channel but a noisy one: most clips spike and die and a single flop is not a verdict. The plan is a format you can repeat, a hook in the first 2 seconds, the game name in every caption, and a tracker that tells you which format to repeat. The 60-90 second trailer is `trailer-script-writer`.

## When to use
Starting or restarting short-form, or when clips earn views and no plays. Not for: page video, paid ads, creator deals (`influencer-outreach-writer`).

## Inputs (max 3)
1. Core loop and clippable moments (default: `GAME.md`; ask what a creator would film). 2. Platform and time per week the owner can spend (default: TikTok first, 3 hours). 3. Language of the core audience (default: English; the vault's example matched content language to where players are).

## Procedure
1. Pick one platform to do well first (vault: do not be everywhere). Others get cross-posts.
2. Build 3 repeatable formats from real game moments: (a) the satisfying loop beat (collect, steal, upgrade) in 10-20 seconds, (b) the surprise or fail (clippable chaos), (c) a one-system devlog ("how the egg trading works") for dev audiences. Cutting long footage into 10-20 second clips works (indie).
3. Hook rules: the first 2 seconds show the payoff or the problem, with a bold claim or on-screen subtitles; looped endings; real footage, not a promise the game cannot keep.
4. Caption rules: the exact game name, the Details Page URL where the platform allows links (bio otherwise), a one-line `tagline-writer` hook; trending audio is unproven, treat it as optional.
5. Cadence: a floor of 2-3 clips a week, daily short plus one weekly long video if sustainable; judge only after 30-60 days. Quality over raw volume; budget 40-60 minutes per short (one creator).
6. Tracker `marketing/shorts-log.csv`: date, format, hook, views at 24 h and 7 days, plays attributed (see tracked links in `codes-campaign-planner`), notes. Benchmark each clip against your own channel average. Mark any clip over 1,000 views and write the common element; repeat that element. Read it with `python -I ~/.claude/claude-kit/skillpack/marketing/short-video-planner/scripts/shorts_report.py marketing/shorts-log.csv`: channel average, hit clips, and per-format average views, hit rate and plays per 1,000 views (formats rank only after 3 posts; under 10 clips it says the sample is too small).
7. Early start: begin during development, not at launch (vault: even rough footage builds awareness; keep trailers earlier than other promo and go full speed near release).
8. Design for clips: ask `core-loop-designer`-style questions about which moments a creator would film, and add streamer-friendly tools (HUD hide, clean camera) in the game when cheap.
9. Do not post as the owner without the owner's go-ahead; this skill prepares.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `screen_capture` for stills and shot checks. Recording is done by the owner (Roblox recorder or screen capture with freecam).

## Fallback
Plan and tracker only. Everything stays `untested` until posts exist and the tracker has numbers.

## Evidence
`Roblox/roblox-kb/trailers-and-video-marketing.md` (hook in the first 2 seconds; 10-20 second cuts; post early and consistently; quality over volume; most shorts spike then die; find the over-1,000-view pattern; benchmark against channel average; 40-60 minutes per short; game name in captions via titles-descriptions), `Roblox/roblox-kb/social-features-and-virality.md` (clippable, chaotic moments; creator-friendly tooling; quick TikToks), `Roblox/roblox-kb/influencer-and-creator-marketing.md` (cadence 3-4 videos a week judged after 30-60 days; keep a dev channel on a narrow topic), `Roblox/roblox-kb/titles-descriptions.md`. Nearly all numbers are indie, self-reported: treat them as examples, not targets. Platform rules change: live-check.

## Output
`marketing/short-form-plan.md`: platform, 3 formats with 8 clip ideas each tied to real moments, hook and caption templates, weekly cadence, and the tracker file path with columns.

## Acceptance checks
- [ ] Every clip idea names the real game moment it shows.
- [ ] Each hook shows payoff or problem within 2 seconds.
- [ ] The caption template contains the exact game name.
- [ ] The tracker exists with the stated columns, `shorts_report.py` runs on it without error (output quoted), and a 30-60 day review date is set.
- [ ] No promise of views or growth is made.

## Pitfalls
Judging after three clips. Posting "play my game" with no hook. Chasing trending audio over the loop. Burning out on daily posts. Ignoring that 95% of short viewers do not subscribe (one case): measure plays, not followers.

## Related
`trailer-script-writer`, `social-post-calendar`, `tagline-writer`, `influencer-outreach-writer`, `community-showcase-planner`.
