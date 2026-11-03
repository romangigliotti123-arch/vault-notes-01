---
title: 1_Bruce - How to make successful Roblox games
tags: [roblox, 1_bruce, playbook]
videos: 4
generated: 2026-10-29
credibility: mixed
credibility_score: 7.2
creator_trust: MIXED
creator_score: 7.2
---

> [!note] Trust: MIXED (credibility audit score 7.2): do not rely on this creator alone; confirm a recommendation with a second source. See [[creator-credibility]].

# 1_Bruce - How to make successful Roblox games

Bruce's playbook: pick a high-revenue genre (incremental, FPS, anime TD, bandit beaters, training sims) and avoid brain rot, flop obbys, puzzle games and plain RPGs. Build a simple stat-multiplier loop that is easy to update, monetised with consumables priced to Robux bundles. Launch without paid ads, seeding a Discord community that every release feeds. Read overview stats (D1, D7, payer conversion, QPTR, playtime) against same-genre games. If stats stay weak, treat the game as a dud and apply the lessons to a new one. Evidence is mostly one promo kit, one case study and an opinion tier list.

**Style:** Community- and data-oriented creator who favours cheap-to-build incremental and simulator genres, benchmarks stats per genre, and rejects paid ads early on. Suits solo or small teams targeting 18+ audiences who want a simple, updatable stat loop. Many claims are opinion; the tier list has little data.

## Playbook
1. **Choose a high-revenue genre** [[game-ideas-and-genres]]: Start with incremental or stat-multiplier games, which he rates easy to build, best demographics and high revenue. Other top tiers: FPS, anime TD, bandit beaters, training sims. Avoid brain rot, flop obbys, puzzle games. The tier list is opinion-based.
2. **Check audience fit before building** [[analytics-metrics]]: Target 18+ players in high-income countries. He credits this demographic for high spending. Young or low-income audiences convert poorly, so price very low or avoid them.
3. **Play several genre games first** [[core-loops-and-game-design]]: Study multiple games in the genre before building one. You need to understand how incremental and stat-multiplier loops work before designing your own.
4. **Design compounding multipliers** [[core-loops-and-game-design]]: Make each stat multiply the previous one, e.g. rebirth doubles the multiplier. Tiered levels can scale predictably, such as x2, x4, x6 per level. Keep the formula simple so upgrades visibly compound.
5. **Add weighted rarity and a secondary currency** [[core-loops-and-game-design]]: Use weighted rarity tables from common to mythical with configurable chances and luck modifiers. Add tokens (about 1 in 50 per button press) to gate higher-tier rooms and purchases.
6. **Use scalable scripting patterns** [[scripting-and-performance]]: Store large values as strings with a Big Num library to get past Lua's number limit. Use math rather than loops for bulk opens. Use a data service update helper, plus tags and components for modular logic.
7. **Centralise gamepass multipliers** [[monetisation-gamepasses]]: Put gamepass multipliers in the central formula script so they apply to any stat with one line. Keep scripting clean so later updates stay feasible.
8. **Lead monetisation with consumables** [[monetisation-devproducts]]: Developer products, especially bundled consumables such as a potion bundle, drove most Robux revenue in his case study. Prioritise consumables over other monetisation. FPS games can add skin cases.
9. **Price to Robux bundles** [[pricing]]: Match top gamepass prices to Robux bundles, e.g. 1,800 Robux equals what a $20 Robux purchase yields. He says this worked very efficiently. Price low for young or low-income audiences to keep conversion up.
10. **Seed a Discord audience before launch** [[community-and-discord]]: Advertise to interested players on Discord before paying for Roblox sponsors. He had no ad budget and grew this way. Build as many developer connections as possible for feedback and help.
11. **Funnel every game into Discord** [[community-and-discord]]: Send players from every game into one Discord server. Each new release then starts from a larger base and performs better. His games are community-oriented and lean on the community to boost them.
12. **Benchmark overview stats per genre** [[analytics-metrics]]: Track average playtime, D1, D7, payer conversion and QPTR (clicked thumbnail and played ~5 minutes). Compare against same-genre games, not absolute numbers. Adult-targeted games run lower QPTR than kids' games.
13. **Keep D7 and D30 up with updates and community** [[retention-d1-d7]]: Update regularly and build a strong community to hold D7. Newer advice: his $25M-Robux game kept D30 surprisingly high despite infrequent updates, so updates are not the only lever.
14. **Abandon duds and reapply lessons** [[mindset-and-strategy]]: If stats stay weak against genre peers, treat the game as a dud. Do not endlessly patch it. Apply the lessons to a new game. Expect sustained discipline; vibe-coding alone will not reliably make a game blow up.

## Key numbers
- Day-1 retention target roughly 10-15%; a community-driven game reached the 20s (i3RQXxZeVYc)
- Typical revenue per DAU about 0.5 to 2-3 at max (i3RQXxZeVYc)
- Brain rot and kids games earn about 20x less revenue than his genre (i3RQXxZeVYc)
- QPTR defined as clicked thumbnail and played about 5 minutes (i3RQXxZeVYc)
- Paid button-simulator starter kit about $5 (9ZoyhYqBkcI)
- Token drop about 1 in 50 per button press (9ZoyhYqBkcI)
- Stat multiplier scaling example: x2, x4, x6 per level; money x5, x10, x15 (9ZoyhYqBkcI)
- Rune example: 5 mythical rooms gives money 5x, multiplier 2.5x, rebirth 0.5x (9ZoyhYqBkcI)
- About 23-24M Robux earned in roughly one month, Jan-Feb; title says 25M (zgq6L4ZzCHs)
- Peak daily active users about 54,000 (zgq6L4ZzCHs)
- Peak single-day Robux revenue about 1.3 million (zgq6L4ZzCHs)
- Home recommendation impressions over 3 million, the largest traffic source (zgq6L4ZzCHs)
- Search impressions 2.5 million, the second-largest source (zgq6L4ZzCHs)
- Retention around release low 20s to high teens percent (zgq6L4ZzCHs)
- Gamepass bundle 1,800 Robux equals a $20 Robux package; about 600-700 Robux per paying user (zgq6L4ZzCHs)

## Common mistakes
- Patching a weak game endlessly instead of treating it as a dud and starting a new one (i3RQXxZeVYc)
- Making brain rot, flop obbys or puzzle games, which he says earn little and hurt platform reputation (i3RQXxZeVYc, iGng-GC_xFk)
- Building plain RPGs unless going MMO; he says they are hard to build and rarely monetise well (iGng-GC_xFk)
- Judging stats by absolute numbers rather than same-genre benchmarks (i3RQXxZeVYc)
- Paying for sponsors or ads before building an audience through Discord (i3RQXxZeVYc)
- Expecting vibe-coding alone to make a game blow up (i3RQXxZeVYc)
- Pricing high for young or low-income audiences, which hurts payer conversion (i3RQXxZeVYc)
- Using hard-to-update scripting that slows update cadence (9ZoyhYqBkcI)
- Using for loops for bulk opens, which can crash or lag the server (9ZoyhYqBkcI)
- Storing large incremental values as plain numbers and hitting Lua's number limit (9ZoyhYqBkcI)

## Launch checklist
- [ ] Pick an incremental, FPS, anime TD, bandit beater or training-sim genre; avoid brain rot and puzzle games
- [ ] Confirm the target is 18+ and high-income countries
- [ ] Play several same-genre games before starting the build
- [ ] Set compounding multipliers (e.g. rebirth doubles) and a simple formula
- [ ] Add weighted rarity tables with luck modifiers
- [ ] Add a secondary currency (about 1 in 50 drop) to gate high-tier content
- [ ] Store large values as strings and use Big Num
- [ ] Use math, not loops, for bulk opens
- [ ] Put gamepass multipliers in the central formula script
- [ ] Make consumables the lead developer product
- [ ] Price top gamepasses to match Robux bundles (e.g. 1,800 Robux = $20 bundle)
- [ ] Price low if the audience is young or low-income
- [ ] Set up a Discord server before launch and seed it without paid ads
- [ ] Add a Discord funnel from inside the game
- [ ] Build developer connections for feedback
- [ ] Set D1 target of 10-15% and benchmark vs same-genre games
- [ ] Track QPTR (clicked thumbnail, played about 5 minutes)
- [ ] Plan a regular update cadence and keep the scripting clean for updates

## How the advice changed over time
- Latest (Apr 2026 tier list) ranks genres by opinion: incremental, FPS, anime TD, bandit beaters and training sims on top. Earlier notes called anime sims dying; the tier list instead ranks anime TD high, so the two claims cover different sub-genres.
- Mar 2026 case study says D30 stayed high despite infrequent updates, which softens the earlier 'update regularly' advice. Prefer the newer evidence, but treat it as one game's experience.
- Feb 2026 talk stressed Discord-first growth and stat benchmarking. Mar 2026 added Robux-bundle pricing and traffic-source data, which give concrete numbers for the earlier advice.

## Theme notes
- [[1_Bruce - Retention|Retention]]
- [[1_Bruce - Monetisation|Monetisation]]
- [[1_Bruce - Game Ideas|Game Ideas]]
- [[1_Bruce - Studio & Scripting|Studio & Scripting]]
- [[1_Bruce - Mindset & Process|Mindset & Process]]
- [[1_Bruce - Games Mentioned]]
- [[1_Bruce - Numbers & Benchmarks]]
- [[1_Bruce - Tools & Resources]]
- Cross-creator knowledge base: [[README]]

## All videos (oldest first)
- [[2026-02-20 - why YOU are failing as a Roblox Developer (and how to fix it)|why YOU are failing as a Roblox Developer (and how]] (13,688 views, 2026-02-20): Weak overview stats mean a weak game: grow via Discord and start a new one, not patch.
- [[2026-03-02 - I made my first $1,000,000 ROBUX off this genre!|I made my first $1,000,000 ROBUX off this genre!]] (10,064 views, 2026-03-02): Promo walkthrough of a ~$5 button-simulator kit: runes, tokens, Big Num and component OOP.
- [[2026-03-15 - This Roblox game earned $25,000,000 robux in a month|This Roblox game earned $25,000,000 robux in a mon]] (23,191 views, 2026-03-15): Incremental game earned ~24M Robux in a month; breakdown of retention, traffic and bundle pricing.
- [[2026-04-17 - The BEST Roblox genres to develop Tier List|The BEST Roblox genres to develop Tier List]] (7,241 views, 2026-04-17): Opinion tier list of 20 genres: incremental, FPS, anime TD and bandit beaters rank top.
