---
name: launch-teaser-planner
description: "Plan the pre-launch run-up for a Roblox game or big update: about two months of devlogs, a Discord or group opened roughly a month before, a sign-up pad or waitlist, teasers that end with a date and time, early access for a few creators, and honest rules about what to show. Use 4-10 weeks before a launch or major update."
category: marketing
tags: pre launch, teaser, waitlist, sign up, devlog, hype, countdown, early access, announcement, playtest
kb: Roblox/roblox-kb/community-and-discord.md, Roblox/roblox-kb/ads-and-sponsored-experiences.md, Roblox/roblox-kb/events-and-seasonal-content.md, Roblox/roblox-kb/trailers-and-video-marketing.md, Roblox/roblox-kb/influencer-and-creator-marketing.md
related: social-post-calendar, launch-day-planner, short-video-planner, influencer-outreach-writer, trailer-script-writer, update-announcement-writer
---

# launch-teaser-planner

Vault: a big update launched to about three players because no marketing was done; pre-release hype gives the algorithm early engagement; start devlogs about two months before, a Discord or group about a month before, tease with images and hints, and end teasers with a date and time. The balance: build awareness early, go full speed only near release, and never show or promise what may not ship.

## When to use
A launch or major update is 4-10 weeks away. Not for: the launch day itself (`launch-day-planner`), the monthly grid (`social-post-calendar`).

## Inputs (max 3)
1. Launch date (firm or window) and the build's current state. 2. Existing audience (group, Discord, followers) and channels. 3. Hours per week available (default: 4).

## Procedure
1. Date discipline: announce a date only when the build can make it; pick a Friday where possible (`launch-day-planner`). If the date is a window, tease the window and say it is a window.
2. Phases, counting back from launch: T-8 to T-4 weeks, devlogs about one system on one platform (vault: about two months, indie; if the team cannot sustain it, hold unlisted devlogs until release) and an early public concept image; T-5 to T-4 weeks, open a Discord or group (about a month before, not much earlier) and invite friends and testers; T-4 to T-2 weeks, a small playtest with 8-10 core testers and fixes; T-3 to T-1 weeks, a sign-up pad or waitlist in the game or a form with a reminder promise (vault: a sign-up pad builds a player pool and boosts launch retention, small self-reported example); T-2 to T-1 weeks, early access for a few matching creators and the press kit (`influencer-outreach-writer`, `press-kit-builder`); T-10 days, first teaser; T-7 days, in-game countdown starts; T-2 days, final teaser with the exact date and time; T0, `launch-day-planner`.
3. Teaser rules: show real gameplay or true concept art; escalate gradually; use silhouettes, hints and short clips; end every teaser with the date, time and the Details Page URL; do not leak content you might cut; the page-video rules (no cinematic, promo text, voiceover) apply to the details-page video, not to posts, so keep that clip separate (`trailer-script-writer`).
4. Collect interest in one place: the sign-up list or group; every teaser links to it; tag sources with tracked links.
5. Ads before launch are optional and low priority: ads need the build to retain players first (ads playbook); if used, the owner funds them.
6. Measure weekly: sign-ups, group and Discord joins, devlog views to joins, tester feedback themes, bug counts; set a go/no-go review at T-2 weeks with a written criterion (for example no blocker bugs in the playtest).
7. Prepare the day-one asks: creators posting a week or two before launch (vault, indie), and the first post-launch bug-fix update.

## Studio MCP path
For the in-game sign-up pad: `list_roblox_studios` -> `get_studio_state` -> `multi_edit` to add a server-side sign-up record (stored in the kit PlayerData profile or a DataStore) -> `start_stop_play` -> `get_console_output`. Collecting contact data from minors has legal limits: no emails or personal data in-game; use platform channels only (live-check the platform rules).

## Fallback
The plan and a form-based or group-join waitlist run by the owner; the in-game pad stays `untested` without Studio.

## Evidence
`Roblox/roblox-kb/community-and-discord.md` (Discord or group about a month before release; devlogs for about two months on one platform; tease with images, silhouettes and hints; public announcements; core playtesters; measure by anticipation), `Roblox/roblox-kb/ads-and-sponsored-experiences.md` (official: teaser trailers ending with date/time; ads need retention first), `Roblox/roblox-kb/events-and-seasonal-content.md` (pre-launch sign-up pad; do not leak content you may not ship), `Roblox/roblox-kb/trailers-and-video-marketing.md` (start posting early; time creator videos 1-2 weeks before launch), `Roblox/roblox-kb/influencer-and-creator-marketing.md` (pre-launch hype; the 3-player launch example). Nearly all timing figures are indie: treat as defaults.

## Output
`marketing/teaser-plan.md`: the dated phase table with owner and channel, teaser rules, sign-up design, weekly measurement table, go/no-go criterion at T-2 weeks.

## Acceptance checks
- [ ] The dates are generated from the real launch date (`calendar_gen.py` month or by hand, shown).
- [ ] Every teaser ends with date, time and URL.
- [ ] A go/no-go criterion with a date exists.
- [ ] No teaser shows a feature that is not in the build.
- [ ] No personal data collection from players is designed outside platform tools.

## Pitfalls
Teasing for six months and burning interest. A date that slips twice. Hype with nothing playable. Collecting emails from minors. Leaving all promotion to launch week.

## Related
`social-post-calendar`, `launch-day-planner`, `short-video-planner`, `influencer-outreach-writer`, `update-announcement-writer`.
