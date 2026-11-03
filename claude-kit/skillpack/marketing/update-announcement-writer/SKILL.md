---
name: update-announcement-writer
description: "Write the update announcement for a Roblox game in three forms from one change list: the in-game/group post, the Discord post and a short X or video caption, each leading with what players get, honest about changes, with the release time and Details Page URL. Use when an update, event or fix is about to ship or just shipped."
category: marketing
tags: update post, patch notes, changelog, announcement, discord, group shout, release notes, event post, devforum
kb: Roblox/roblox-kb/updates-live-ops.md, Roblox/roblox-kb/community-and-discord.md, Roblox/roblox-kb/titles-descriptions.md, Roblox/roblox-kb/events-and-seasonal-content.md
related: social-post-calendar, launch-day-planner, tagline-writer, event-planner, game-description-writer, short-video-planner
---

# update-announcement-writer

Players read an update post in seconds. Vault: announce in several places at once, say why something changed (especially money and removals), tell players about experiments, keep a predictable rhythm, and use title or description to surface "brand new update" for returning players. One change list, three forms, no spin.

## When to use
An update, event or hotfix is ready to describe. Not for: the full store description (`game-description-writer`), teasers before the date is firm (`launch-teaser-planner`).

## Inputs (max 3)
1. The change list: what was added, changed, fixed, removed (default: ask for the git log or notes). 2. Release time with time zone (default: ask; vault prefers a fixed time). 3. Audience (default: players of all ages; keep language simple).

## Procedure
1. Sort the changes into player value: new things to do, better things, fixes, removals or nerfs. Order by what the average player cares about, not by what was hardest to build.
2. Headline: what the player gets in 6-10 words, naming the update theme (vault: themed releases are easier to market). Never lead with a money reward or a promise; do not exaggerate.
3. Body (group / in-game post, under about 120 words): 3-5 bullets of concrete changes, one line on what is next, the release time in UTC and one local example, the Details Page URL. Removals and nerfs come with the reason in one sentence (vault: be transparent, explain why). If odds or prices changed, say so plainly; show odds where relevant.
4. Discord post: same facts plus a thanks to testers, a link to the feedback channel, and where to report bugs. Pin it.
5. Short caption (X, video): hook line (`tagline-writer`), one visual from the update, game name, URL. Do not add promo text over on-platform video.
6. Truth check: every bullet maps to a thing that exists in the released build (play it or check the diff). Delete anything you cannot confirm. Mention only experiments that are really running.
7. Safety: all-ages language, no third-party brands, no real names, no claims about rewards that are not guaranteed.
8. Schedule: post at the release time, repost a short reminder at the event end; the owner posts, never this skill.
9. Keep a changelog entry with the date in `docs/CHANGELOG.md` so the page, group and Discord agree.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` to confirm the place and version match the notes; nothing else.

## Fallback
Same; text only. If the build cannot be played, mark bullets as `unconfirmed` and tell the owner.

## Evidence
`Roblox/roblox-kb/updates-live-ops.md` (theme each release; countdowns and cross-channel announcements; predictable schedule; first post-launch update is bug fixes; release Friday; surface updates via title and description), `Roblox/roblox-kb/community-and-discord.md` (tease and announce publicly; be transparent about changes and money; explain why features are removed; tell players about experiments), `Roblox/roblox-kb/titles-descriptions.md` (surface updates via metadata; one freshness tag such as [NEW] used temporarily; description limits), `Roblox/roblox-kb/events-and-seasonal-content.md` (do not announce content you may not ship; fixed launch time). Platform posting features change: live-check.

## Output
`docs/updates/<version>.md` with three blocks: GROUP/IN-GAME POST, DISCORD POST, SHORT CAPTION, plus a truth-check table (bullet, where it exists in the build) and the changelog line.

## Acceptance checks
- [ ] Every bullet maps to something confirmed in the build (table filled).
- [ ] Release time has a time zone and the URL is the Details Page URL.
- [ ] Removals and nerfs include the reason.
- [ ] Headline passes `python -I ~/.claude/claude-kit/skillpack/marketing/title-generator/scripts/title_screen.py --min-words 3 --max-words 10 "<headline>"`.
- [ ] No reward promise, brand name or real person; all-ages language.

## Pitfalls
Burying the thing players want in line 9. Announcing before the build is ready. Hiding a nerf. Different facts in group and Discord. Over-hyping a small fix.

## Related
`social-post-calendar`, `launch-day-planner`, `tagline-writer`, `event-planner`, `launch-teaser-planner`.
