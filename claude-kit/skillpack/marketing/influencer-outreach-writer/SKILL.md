---
name: influencer-outreach-writer
description: "Write a respectful, self-contained pitch to a Roblox content creator: who to pick, what to offer, the message itself with playable link, trailer and screenshots, and a follow-up plan, linted by outreach_lint.py. Use when seeking YouTubers, TikTokers or streamers for a launch or update; never sends anything itself."
category: marketing
tags: influencer, youtuber, creator outreach, pitch, dm, email, early access, sponsorship, tracked link, affiliate
kb: Roblox/roblox-kb/influencer-and-creator-marketing.md, Roblox/roblox-kb/social-features-and-virality.md, Roblox/roblox-kb/community-and-discord.md, Roblox/roblox-kb/ads-stats-monetisation-playbook.md
related: codes-campaign-planner, short-video-planner, collab-pitch-writer, press-kit-builder, launch-day-planner, sponsored-ad-reviewer
---

# influencer-outreach-writer

Vault: a pickup by a YouTuber is, in Roblox staff's words, far and away the best way to get discovered (one case 200 to 4,000 CCU), but a bare "play my game" DM fails. The message must contain what the game is, a playable link and a concrete reason for the creator to play. Money, giveaway and affiliate programme rules are fast-moving and legal: the owner decides; this skill drafts.

## When to use
Launch, a big update or a revival, once the game is worth playing (vault: fix the game before building promotion). Not for: dev-to-dev cross-promotion (`collab-pitch-writer`), the code system (`codes-campaign-planner`).

## Inputs (max 3)
1. Game, genre, the clip-worthy moment (default: `GAME.md`). 2. Budget in Robux or money, possibly zero (default: no cash; offer access and items). 3. Target size range (default: smaller creators 1-10k subscribers with a matching audience).

## Procedure
1. Build a creator list of 10-20 whose audience matches the genre and age. Prefer creators already featuring similar games (look at their most-viewed videos). Record channel, size, last three videos, contact route.
2. Decide the offer ladder, cheapest first: early access to the next update (contact about 3 months before a big release per one source, 1-2 weeks before for a normal launch), an exclusive in-game item or pet, a personal tracked code, private server, admin tools, assets and thumbnail renders, a creator tournament. Payment is a last, separate step: small-creator offers have been called 8-12 times below their worth, so lowballing gets declined. Ask for reuse rights to cutdowns and short clips when paying.
3. Draft the message (under about 150 words, one screen on a phone): who you are in a line; one specific thing from their content (`<<video name>>`); what the game is in a sentence; the playable link; trailer and 3 screenshots link; the offer; zero pressure. Never request or promise views. Use the placeholder `AMOUNT` rather than inventing a price.
4. Run `python -I .rbx/claude-kit/skillpack/marketing/influencer-outreach-writer/scripts/outreach_lint.py message.txt` and fix every FAIL. All `<<...>>` placeholders must be filled before the owner sends.
5. Tracking: one tracked share link or unique code per creator (`codes-campaign-planner`); tag creator-acquired players in analytics and compare retention by source (vault: Deconstructor of Fun, self-reported). Judge on a window of at least 7 days; a late payer can arrive weeks later.
6. Follow-up: one polite follow-up after 5-7 days, then stop. Reply to and share their video after it posts.
7. Disclosure and programmes: if payment, codes or affiliate links are involved, the creator must disclose per the platform and consumer rules; Roblox's Creator Affiliate pilot has strict eligibility. Live-check Creator Docs before mentioning it.
8. The owner sends everything; you never contact anyone.

## Studio MCP path
Not needed.

## Fallback
Same; this is text. Nothing is `tested` until replies exist.

## Evidence
`Roblox/roblox-kb/influencer-and-creator-marketing.md` (reach out to creators already featuring the game; concrete reason to play; self-contained first pitch with trailer, screenshots, playable link; expect slow low-yield micro-payment outreach; budget realistically; permanent pillar; judge on long-tail; groups need 10+ videos and ~500k combined views; Creator Affiliate pilot terms are official and may change), `Roblox/roblox-kb/social-features-and-virality.md` (approach smaller creators first with a playable build; unique codes; early access; creator tournaments), `Roblox/roblox-kb/community-and-discord.md` (design for clippability), `Roblox/roblox-kb/ads-stats-monetisation-playbook.md` (no price list exists; anecdotal). Prices, programmes and disclosure rules change: live-check.

## Output
`marketing/outreach/<creator>.md` per message plus `marketing/outreach/creators.csv` (name, channel, size, fit, offer, tracked code, status, follow-up date).

## Acceptance checks
- [ ] `outreach_lint.py` printed no FAIL on each message (quote the last line).
- [ ] Each message names one specific thing from the creator's own content.
- [ ] Each has a playable link, a trailer/screenshots link and a concrete offer.
- [ ] No unfilled placeholders, no promised results, no pressure.
- [ ] Every creator has a tracked code or link row.

## Pitfalls
Mass-pasting one text. Asking for a video before the game is ready. Paying big names early. Cutting a creator after one weak video. Forgetting disclosure.

## Related
`codes-campaign-planner`, `short-video-planner`, `collab-pitch-writer`, `press-kit-builder`, `launch-day-planner`.
