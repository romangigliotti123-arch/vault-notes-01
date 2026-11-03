---
name: creator-collab-planner
description: "Plan an ongoing working relationship with content creators (YouTubers, TikTokers, streamers) for a Roblox game: tiers by size, what each gets (early access, unique items, codes), how it is tracked, how to treat minors and sponsorship disclosure, and how to engage after the content. Use once a game is playable and you want creators to actually feature it; the first pitch itself is a separate skill."
category: community
tags: creators, youtubers, streamers, collab, program, codes, early-access, influencer, disclosure, tracking
kb: Roblox/roblox-kb/influencer-and-creator-marketing.md, Roblox/roblox-kb/community-and-discord.md, Roblox/roblox-kb/social-features-and-virality.md
related: collab-pitch-writer, influencer-outreach-writer, streamer-kit-builder, codes-campaign-planner, sponsored-ad-reviewer, social-proof-collector, ambassador-program-planner
---

# creator-collab-planner

This is the program, not the pitch. `collab-pitch-writer` and `influencer-outreach-writer` write the messages; this decides tiers, perks, tracking, safety and follow-up so a handful of creators become a repeatable channel. The vault: start with smaller creators whose audience matches your genre, offer real value and early access, give each a unique code to measure performance, and engage after the content.

## When to use
The game is playable and you want sustained creator coverage, or you already got a few creators and need structure. Not for: writing the outreach email (`influencer-outreach-writer`), the in-game streaming tools (`streamer-kit-builder`), or paid ad reviews (`sponsored-ad-reviewer`).

## Inputs (max 2)
1. Genre, stage and budget (default: playable build, no cash budget, items and access only). 2. Target creator sizes (default: small, 1-10k subscribers, free playthroughs, then bigger).

## Procedure
1. Define three tiers by audience size: Starter (small creators: playable build, an item, a code), Partner (mid: early access about three months before a big release, unique pet or item, planning input), Spotlight (large: business-email pitch, bespoke event). Tier by audience match to your genre first, size second.
2. Perks list per tier, all cosmetic or access, nothing that makes the game pay-to-win; creator-inspired features should be available to everyone. Never promise Robux for views; any paid sponsorship follows the platform's and the country's disclosure rules (live-check Roblox sponsorship policy and local advertising rules).
3. Tracking: one unique in-game code per creator via `codes-campaign-planner` (and a Share Link where useful) so performance is measurable; the log lives in `creators/tracker.csv` (creator, platform, tier, code, date sent, video date, notes).
4. Safety and age: many creators and viewers are minors. Contact via business email or public channels, never DM minors; do not ask a young creator to sign contracts; for under-18 creators involve a parent or guardian before any exchange of value; live-check platform rules for minors and payments.
5. Content fit: ask what moments a creator would film, then check they exist in the core loop (design for clippability); provide a press kit and the streamer kit.
6. After the content: reply to and share their videos, thank them, tally results (code redemptions, visits during the window), and decide per creator: continue, upgrade, pause. Judge holistically, not just direct installs (vault).
7. Cadence: a monthly creator update with news, upcoming events and a new code; a yearly review of the program.
8. Lint every outbound template: `python welcome-message-writer/scripts/text_lint.py creators/templates.txt`.

## Studio MCP path
Only for code or attribution plumbing: `list_roblox_studios` -> `get_studio_state` -> `script_grep` for existing redeem code handling, then `multi_edit` per `codes-campaign-planner`; `start_stop_play` and `get_console_output` to verify.

## Fallback
Plan, tracker CSV and templates in text. Sending anything is the owner's action; the skill never contacts a creator.

## Evidence
`Roblox/roblox-kb/influencer-and-creator-marketing.md` (approach smaller creators first with a playable build; offer early access and unique items; unique cash codes per creator; tournaments and brackets; creator-friendly tooling; engage creators after the content; judge spend on holistic effects). `Roblox/roblox-kb/community-and-discord.md` (design for clippability; build an influencer program; nurture a recognised community creator). `Roblox/roblox-kb/social-features-and-virality.md`.

## Output
`creators/PROGRAM.md` (tiers, perks, rules, cadence), `creators/tracker.csv` header and first rows, template list. Under 80 lines.

## Acceptance checks
- [ ] Every tier has a perk list with no pay-to-win items and no promise of Robux for views.
- [ ] Each creator has one tracking code or link in the tracker.
- [ ] The plan states disclosure and minors rules with a live-check note.
- [ ] `text_lint.py` exits 0 on the templates.
- [ ] A post-content engagement step and a results review exist.

## Pitfalls
Chasing the biggest names first. No tracking, so no learning. Perks that unbalance the game. Contacting young creators privately. Undisclosed sponsorship. Forgetting to thank creators after the video.

## Related
`collab-pitch-writer`, `influencer-outreach-writer`, `streamer-kit-builder`, `codes-campaign-planner`, `ambassador-program-planner`.
