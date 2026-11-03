---
title: waveshinedev - How to make successful Roblox games
tags: [roblox, waveshinedev, playbook]
videos: 2
generated: 2026-10-29
credibility: insufficient
credibility_score: n/a
creator_trust: INSUFFICIENT
---

> [!note] Trust: UNAUDITED (fewer than 4 checkable claims verified): credibility unknown, treat as unverified, not as bad; confirm before relying. See [[creator-credibility]].

# waveshinedev - How to make successful Roblox games

Roblox success comes from shipping repeatedly and building for retention, not from one hit. Make a game you would open on a boring afternoon, with progression, RNG, leaderboards, enemies and something to grind for, and give new players a win within 30 seconds. Build small systems first, avoid saturated clones, and test on live servers. Treat flops as tuition: read feedback, fix what you can, and don't let daily player counts set your mood. The platform now ranks games on returning players, so design for next week's session, not today's spike.

**Style:** Motivational, mindset-first devlogs from a young developer with self-reported earnings and results. Strong on resilience, retention and taking responsibility for flops; light on hard data and metrics. Suits beginners who need perspective on early failure and small-system building. Less suited to analytics-driven optimisation.

## Playbook
1. **Pick a genre you would play yourself** [[game-ideas-and-genres]]: Avoid saturated, tutorial-clone genres (e.g. Grow a Garden-style games). Make the game you would want to open on a boring afternoon. Source: hQ1, xnlaYLnCtFc.
2. **Design the core retention loop first** [[core-loops-and-game-design]]: Prioritise meaningful progression, RNG, leaderboards, enemies and a grind target over clean code. Players care about fun. Rarity Rumble gained traction on this basis. Source: xnlaYLnCtFc.
3. **Build small standalone systems, then stack them** [[development-process-and-speed]]: Start with a shop button, notifications, leaderboard, inventory or save system. Use tutorials only for basics, try first, then search your exact error. Pass the change test: reprice an item without breaking things. Source: hQ1.
4. **Give a win in the first 30 seconds** [[first-session-onboarding]]: Assume players have zero context. Deliver a win or reward almost immediately. Test whether a new player ever wonders what to do next and fix every such moment.
5. **Test under live-server conditions before publishing** [[scripting-and-performance]]: Expect hours of debugging for issues that work in Studio but break on live servers. Plan for failures such as data store errors (cited 1% rate). Use AI as a tutor for explanations, not to generate systems you don't understand. Source: hQ1.
6. **Design for the second session** [[retention-d1-d7]]: Build a loop that itches: a small feelable reward, a number going up and a one-more-run hook. Players return for that loop. Source: xnlaYLnCtFc.
7. **Playtest and treat feedback as fuel** [[playtesting-and-feedback]]: Early messages and feature requests are fuel. Once players give feedback, build with the community rather than for yourself. Diagnose departures by reading feedback and running experiments. Source: xnlaYLnCtFc.
8. **Ship, accept flops, keep releasing** [[mindset-and-strategy]]: Expect the first few games to flop and a hit often comes after several releases. Treat scrapped projects as tuition (speaker cites 100+ scrapped files). Consistent shipping beats any single launch. Source: hQ1, xnlaYLnCtFc.
9. **Design for returning players, not launch hype** [[discovery-algorithm]]: Roblox now ranks games on day-over-day and monthly return, not one-session hype. Measure return rates rather than peak counts. Source: hQ1 (newer than xnlaYLnCtFc).
10. **Optionally buy early visibility with ads** [[ads-and-sponsored-experiences]]: Speaker claims a good game can be pushed with about $100 in ads to kick-start the algorithm. This is an unverified single claim with no reported results. Source: hQ1.
11. **Track retention, not daily counts** [[analytics-metrics]]: Use return-based metrics to decide what to fix. Do not let daily player counts set your mood or decisions, since obsessing over stats erodes self-worth. Source: xnlaYLnCtFc.
12. **Update live content around retention drivers** [[updates-live-ops]]: Post-launch, iterate on progression, RNG, leaderboards and enemies that keep players returning. Separate ego from the game and ask what you can fix. Source: xnlaYLnCtFc.
13. **Keep shipping and budget for years of learning** [[team-and-budget]]: Plan for weeks to years, not a quick win. Success requires marketing, design, retention, monetisation and balancing skills. Most early projects will be scrapped. Source: hQ1, xnlaYLnCtFc.

## Key numbers
- xnlaYLnCtFc: ~6,000 total visits on early open-source-based games before main account loss (2022)
- xnlaYLnCtFc: ~100,000 Robux of progress lost when main account was terminated
- xnlaYLnCtFc: Steel Time, first game on new account, got 163 visits
- xnlaYLnCtFc: Rarity Rumble got thousands of visits in its first week
- xnlaYLnCtFc: about 100 hours invested with no results (effort example)
- hQ1lrFLEF1c: speaker claims over 100 million daily Roblox players walking the platform
- hQ1lrFLEF1c: speaker claims about $100 ad spend can kick-start a good game
- hQ1lrFLEF1c: speaker, age 17, claims around $30,000 earned from Roblox games (still rising)
- hQ1lrFLEF1c: speaker claims over 100 million combined visits across shipped games
- hQ1lrFLEF1c: data store failure rate of 1% cited as hard-to-debug example
- hQ1lrFLEF1c: over 100 scrapped game files in speaker's graveyard of abandoned projects
- All speaker figures in hQ1lrFLEF1c are self-reported with no supporting data; the 100,000-subscriber goal is promotional and excluded.

## Common mistakes
- Blaming players or the algorithm for a flop instead of taking responsibility, which removes your control over the outcome (xnlaYLnCtFc).
- Tying your mood and decisions to daily player counts; momentum is fragile (xnlaYLnCtFc).
- Relying on a single account; termination can wipe out all progress, as with ~100,000 Robux lost (xnlaYLnCtFc).
- Building on copied open-source projects as a base (xnlaYLnCtFc).
- Polishing code while neglecting meaningful progression and retention drivers (xnlaYLnCtFc).
- Entering saturated genres already dominated by tutorial clones (hQ1lrFLEF1c).
- Learning via tutorials only, instead of building small systems and testing (hQ1lrFLEF1c).
- Shipping only for a day-one spike rather than designing for returning players (hQ1lrFLEF1c).
- Assuming Studio behaviour matches live servers (hQ1lrFLEF1c).

## Launch checklist
- [ ] Test the game on live-server conditions, not only in Studio.
- [ ] Confirm a new player gets a win or reward within the first 30 seconds.
- [ ] Check that no moment leaves a new player asking 'what do I do now?'
- [ ] Verify progression, RNG, a leaderboard, enemies and a grind target are present.
- [ ] Confirm there is a clear reason to return next session (feelable reward, number going up, one-more-run hook).
- [ ] Pass the change test: reprice an item or add a currency without breaking systems.
- [ ] Handle data store failures gracefully (1% failure rate cited).
- [ ] Keep source code and game files backed up.
- [ ] Do not rely on a single account for everything you have built.
- [ ] Avoid building on copied open-source projects.
- [ ] Set up a channel to collect early player feedback.
- [ ] Decide which return-based metrics you will track (day-over-day, monthly return).
- [ ] Do not judge the launch by day-one player counts.
- [ ] Use AI only to explain errors and code, not to generate systems you don't understand.
- [ ] Pick a saturated-genre check before you start building.
- [ ] Plan the next game in case this one flops.
- [ ] Set a review cadence that is about fixes, not daily stats.
- [ ] Decide in advance whether ad spend is part of the plan and treat the $100 claim as unverified.

## How the advice changed over time
- Newer advice (hQ1lrFLEF1c, 2026-07-27) says the Roblox home page and discovery now reward retention over short-term hype; the older video (xnlaYLnCtFc, 2025-08-04) emphasised core retention in design but did not discuss discovery. Prefer the newer framing for discovery.
- Newer video adds the advice to build small systems instead of following tutorials, and to avoid saturated genres. The older video did not cover these.
- Newer video adds an ad-spend claim ($100 kick-start) not present in the older video; it is unverified.
- Older account-safety lesson (2022 account loss) is historical and has not been updated, but remains the same advice: do not depend on a single account.

## Theme notes
- [[waveshinedev - Retention|Retention]]
- [[waveshinedev - Discovery & Algorithm|Discovery & Algorithm]]
- [[waveshinedev - Game Ideas|Game Ideas]]
- [[waveshinedev - Studio & Scripting|Studio & Scripting]]
- [[waveshinedev - Mindset & Process|Mindset & Process]]
- [[waveshinedev - Games Mentioned]]
- [[waveshinedev - Numbers & Benchmarks]]
- [[waveshinedev - Tools & Resources]]
- Cross-creator knowledge base: [[README]]

## All videos (oldest first)
- [[2025-08-04 - Watch this before making ROBLOX Games|Watch this before making ROBLOX Games]] (546,172 views, 2025-08-04): Expect early flops; take responsibility, build the retention loop, and never let player counts decide your mood.
- [[2026-07-27 - There's so much money to be made from Roblox|There's so much money to be made from Roblox]] (28,612 views, 2026-07-27): Build small systems, avoid saturated genres, and design for returning players; the home page now rewards retention.
