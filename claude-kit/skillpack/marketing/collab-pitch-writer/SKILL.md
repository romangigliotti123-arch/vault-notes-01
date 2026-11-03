---
name: collab-pitch-writer
description: "Write a pitch to another developer, a larger game, a platform event or a brand for a cross-promotion or collaboration: what each side gets, the format (shared event, portal, creator swap, licensed IP request), a lightweight timeline, and a respectful message. Use when seeking cross-promotion; creator video deals are influencer-outreach-writer."
category: marketing
tags: collab, collaboration, cross promotion, partnership, portal, brand deal, license manager, event, pitch, developer
kb: Roblox/roblox-kb/community-and-discord.md, Roblox/roblox-kb/social-features-and-virality.md, Roblox/roblox-kb/brand-deals-and-ip-licensing.md, Roblox/roblox-kb/updates-live-ops.md
related: influencer-outreach-writer, press-kit-builder, event-planner, launch-day-planner, social-post-calendar, roblox-monetization-audit
---

# collab-pitch-writer

Vault: network by offering value (top developers rarely answer cold DMs or give free advice), cross-promotion via live collaboration events mixes player bases, a portal from a popular game sent most of one sequel's plays, and brand work only works when it fits the game and community. A pitch is a clear, small, mutual ask. Legal terms, revenue splits and licensing are the owner's decisions and may need a lawyer.

## When to use
You want a developer, a bigger game, a platform event or a brand/IP holder to promote with you. Not for: creators (`influencer-outreach-writer`), paid ads, selling the game.

## Inputs (max 3)
1. What you offer (audience, event, content, tooling, a good game) and the date range. 2. Partner type: peer developer, larger game, platform event, brand/IP. 3. Your numbers the owner is willing to share, with date (CCU, MAU), or none.

## Procedure
1. Qualify the partner: a similar audience age and genre fit, a game you have actually played, current activity. Play it first (vault: play their game first) and write one specific compliment based on it.
2. Pick the format by value to the partner: a timed shared event or collab content, a two-way portal or teleport link with a small reward, a mutual update-post swap, a creator swap, a small co-built mini-game, or an IP/brand licence via the platform's rights tool. Keep the first ask small and reversible.
3. Mutual value table: what they get (players, content, goodwill, a fix for a gap), what you get, effort for each side, risks (audience quality, brand fit, workload during their update crunch; vault says join collabs when spare time exists, not during crunch).
4. For brand or IP partners: the game must be public and eligible; pitch the vision, gameplay fit, timeline, and which passes and products will carry the IP; add mockups; check revenue share and content standards before applying; one IP per game; plan for expiry and removal (vault, official docs; live-check, terms change). The licence tool handles offers, not email negotiation.
5. Write the message: under about 150 words, who you are, the specific thing you like, the proposal in one sentence, what they get, what you need from them, the timeline, how to say no, a link to the press kit (`press-kit-builder`). No pressure, no figures you cannot back.
6. Follow-up plan: one follow-up after about a week; accept a no; keep the relationship (reply to their posts, send a bug report if you find one).
7. If yes: a half-page written agreement of dates, assets, who posts what, what happens if one side slips; the owner or a lawyer reviews anything involving money or IP.

## Studio MCP path
Not needed, except for building a portal or teleport link later: `list_roblox_studios`, `multi_edit`, `start_stop_play`; place ids come from the partner.

## Fallback
Text only. Everything is `untested` until a reply arrives.

## Evidence
`Roblox/roblox-kb/community-and-discord.md` (network by offering value; cross-promotion; choose promotion venues carefully), `Roblox/roblox-kb/social-features-and-virality.md` (live collaboration events with larger games mix player bases; one sequel got most plays from an in-game portal; creator-friendly tooling), `Roblox/roblox-kb/brand-deals-and-ip-licensing.md` (only brand deals that fit; vet partners; License Manager mechanics, single-IP limits, expiry and removal; Brand Link is invite-only and expects an established game), `Roblox/roblox-kb/updates-live-ops.md` (join cross-promotional events when there is spare time). Programme terms change: live-check.

## Output
`marketing/collab-<partner>.md`: partner notes, value table, format, message draft, follow-up date, agreement checklist.

## Acceptance checks
- [ ] `python -I ~/.claude/claude-kit/skillpack/marketing/influencer-outreach-writer/scripts/outreach_lint.py message.txt` prints no FAIL (link, concrete offer, no pressure, no placeholders left); output quoted.
- [ ] The message names one specific thing the writer actually played or read.
- [ ] The ask is small, dated and mutual; both sides' effort is written.
- [ ] Any shared numbers have a date and the owner's approval.
- [ ] Brand/IP rules were live-checked and dated, or the section is absent.
- [ ] Nothing was sent or signed by the skill.

## Pitfalls
Asking a top game for free promotion with nothing offered. Vague "let's collab". Pitching during their update crunch. Promising numbers you cannot show. Using an IP before a licence starts.

## Related
`influencer-outreach-writer`, `press-kit-builder`, `event-planner`, `launch-day-planner`, `social-post-calendar`.
