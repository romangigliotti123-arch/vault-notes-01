---
title: "How Top Studios Use Analytics and Experimentation to Grow | RDC 2025"
url: https://youtu.be/j6OPA95-1O0
creator: Roblox
official: true
advice_density: high
date: 2025-09-26
views: 7089
transcript: auto-captions
confidence: high
tags: [roblox, mustwatch, youtube-learn]
---

# How Top Studios Use Analytics and Experimentation to Grow | RDC 2025

[Watch](https://youtu.be/j6OPA95-1O0) | MustWatch | 7,089 views | 2025-09-26

## Summary
Roblox RDC 2025 panel (Roblox + Brookhaven, Adopt Me, Tower Defense Simulator) on configs/feature flags and A/B experimentation. Covers stat-sig basics, not peeking early, segmenting data, and case studies on avatar editor, trade restriction, matchmaking, contextual upsells, starter packs, and thumbnails.

## Tips
- [2:11](https://youtu.be/j6OPA95-1O0?t=131) **[[development-process-and-speed]]** Ship risky features behind runtime config feature flags so you can instantly disable them without hotfix or server restart.
- [6:13](https://youtu.be/j6OPA95-1O0?t=373) **[[analytics-metrics]]** Only call a result when the confidence interval excludes zero; more sample size shrinks intervals and makes results precise.
- [8:22](https://youtu.be/j6OPA95-1O0?t=502) **[[analytics-metrics]]** Run experiments longer and at larger rollout to detect small lifts (e.g. 1% D1 retention) instead of only 5%+.
- [9:03](https://youtu.be/j6OPA95-1O0?t=543) **[[analytics-metrics]]** Don't act on day-one results; wait until metrics are static (ideally ~2 weeks) to avoid novelty effects.
- [9:45](https://youtu.be/j6OPA95-1O0?t=585) **[[analytics-metrics]]** When metrics trade off, decide by the dominant gain; ramp to 100% only once the key metric is clearly and statistically up.
- [12:06](https://youtu.be/j6OPA95-1O0?t=726) **[[playtesting-and-feedback]]** Playtest major features with players before experimenting; Brookhaven caught confusing 3D clothing categories this way.
- [11:24](https://youtu.be/j6OPA95-1O0?t=684) **[[community-and-discord]]** Tell players in Discord or update logs that you run experiments, since many are surprised to see different experiences from friends.
- [13:29](https://youtu.be/j6OPA95-1O0?t=809) **[[development-process-and-speed]]** Start high-risk features at small group sizes (10% in Brookhaven's avatar editor case) and ramp after confidence builds.
- [14:09](https://youtu.be/j6OPA95-1O0?t=849) **[[analytics-metrics]]** Let tests run until stat-sig, including long-horizon metrics like D7 retention; Brookhaven ran 28 testing days total with two public playtests.
- [16:07](https://youtu.be/j6OPA95-1O0?t=967) **[[common-mistakes]]** Consider segmenting data (new vs veteran, player types); Adopt Me's trade-delay test looked negative only because bots/alts were concentrated in control.
- [20:10](https://youtu.be/j6OPA95-1O0?t=1210) **[[analytics-metrics]]** If results don't make sense, investigate or run another test rather than trusting the surprising number.
- [24:11](https://youtu.be/j6OPA95-1O0?t=1451) **[[monetisation-gamepasses]]** Add contextual upsells when players click locked content; Brookhaven saw +10% ARPD and +18% payer conversion with no playtime or retention loss.
- [25:32](https://youtu.be/j6OPA95-1O0?t=1532) **[[common-mistakes]]** Test even obvious changes: popups on locked items can drive new players away, so measure retention alongside revenue.
- [27:07](https://youtu.be/j6OPA95-1O0?t=1627) **[[monetisation-devproducts]]** Test starter pack variables: product type, price, presentation art, prompt timing, and offer duration (FOMO timer vs longer window).
- [28:29](https://youtu.be/j6OPA95-1O0?t=1709) **[[monetisation-devproducts]]** Use recognizable value language like 'guaranteed uncommon or better' and a relevant icon; Adopt Me's royal egg beat the cracked egg by +6% new-user conversion.
- [29:51](https://youtu.be/j6OPA95-1O0?t=1791) **[[analytics-metrics]]** Starter-pack tests on new-user spenders can take over a month to reach stat-sig; don't react to day-1 or day-2 swings.
- [31:02](https://youtu.be/j6OPA95-1O0?t=1862) **[[thumbnails-icons]]** A/B test thumbnails and follow recent art trends; hand-drawn, cleaner style gave Tower Defense Simulator 2x QPTR over 3D render.
- [33:46](https://youtu.be/j6OPA95-1O0?t=2026) **[[thumbnails-icons]]** Make thumbnails for new players seeing homepage recs: show what the game is about, stay relevant, avoid clickbait that hurts other stats.
- [32:23](https://youtu.be/j6OPA95-1O0?t=1943) **[[thumbnails-icons]]** Keep 3-5 thumbnails running at once; Adopt Me's minigame action shot lost to its dog-walk thumbnail by 5%.
- [35:07](https://youtu.be/j6OPA95-1O0?t=2107) **[[thumbnails-icons]]** Adopt Me's best thumbnail was a vibrant pet-collection shot matching core fantasy, performing ~1.7x average.
- [21:42](https://youtu.be/j6OPA95-1O0?t=1302) **[[core-loops-and-game-design]]** Simplify matchmaking tickets: TDS removing difficulty from the menu gave +14% play time and +4% D1 but +40% disconnects, so they kept control.
- [17:42](https://youtu.be/j6OPA95-1O0?t=1062) **[[core-loops-and-game-design]]** Add a short trade delay for new accounts to cut scam reports; Adopt Me saw scam reports down 5.5%, playtime up 1%, revenue up ~2%.

## Numbers
- [9:03](https://youtu.be/j6OPA95-1O0?t=543) D1 retention lift (demo experiment): **+37%, session time -2%** (Hypothetical dungeon RPG onboarding test; decision to ramp)
- [15:32](https://youtu.be/j6OPA95-1O0?t=932) New user play time / D0-D7 retention (Brookhaven avatar editor): **+14% playtime; +8.5% D0-D7 retention; ARPD dropped** (28 testing days, 10% then 50% then 100% rollout)
- [17:42](https://youtu.be/j6OPA95-1O0?t=1062) Scam reports (Adopt Me trade delay): **-5.5%; playtime +1%; revenue +~2%** (New-account trade delay of first couple hours)
- [23:05](https://youtu.be/j6OPA95-1O0?t=1385) Matchmaking test (TDS): **Disconnects +40%; play time +14%; D1 retention +4%** (Control 60% / variant 40%; variant rejected)
- [26:13](https://youtu.be/j6OPA95-1O0?t=1573) Contextual upsell (Brookhaven): **ARPD +10%; payer conversion +18%; playtime and retention unchanged** (Popup when clicking locked hoverboard)
- [29:10](https://youtu.be/j6OPA95-1O0?t=1750) Starter pack Royal Egg (Adopt Me): **New-user ARPU +6%; new-user conversion +6%; D7 retention +2%** (Replaced cracked egg; took just over a month to reach stat-sig)
- [31:02](https://youtu.be/j6OPA95-1O0?t=1862) QPTR (TDS hand-drawn thumbnail): **2x vs 3D render control; later variants 1.2x, 1.5x, 2x** (PVP update, July)
- [33:04](https://youtu.be/j6OPA95-1O0?t=1984) Adopt Me spring thumbnail test: **Control beat action-shot variant by 5%** (Kai Jr. minigame action shot lost to dog walk)
- [35:07](https://youtu.be/j6OPA95-1O0?t=2107) Adopt Me top thumbnail: **~1.7x average thumbnail performance** (Pet collection thumbnail)
- [10:43](https://youtu.be/j6OPA95-1O0?t=643) Avatar editor daily usage (Brookhaven): **over 70% of daily users** (Core feature used daily)

## Games
- **Brookhaven**: Avatar editor A/B test over 28 days lifted playtime 14% and D0-D7 retention 8.5%; contextual upsells lifted ARPD 10%.
- **Adopt Me**: Trade delay for new accounts cut scam reports 5.5%; royal egg starter pack beat cracked egg; dog-walk thumbnail beat action shot.
- **Tower Defense Simulator**: Simplified matchmaking raised play time 14% but disconnects rose 40%, so the team kept the control; hand-drawn thumbnail doubled QPTR.

## Tools
Roblox Experiments (in development), Roblox Configs / feature flags (in development), Creator Hub, Roblox Studio

## He points to
- RDC 2025 funnel analysis talk (prior year)

## Quotes
- [6:13](https://youtu.be/j6OPA95-1O0?t=373) "If the range spans 0%, it's not stat sig."
- [9:03](https://youtu.be/j6OPA95-1O0?t=543) "You definitely want to wait until your numbers are static or ideally at least wait two weeks."
- [16:07](https://youtu.be/j6OPA95-1O0?t=967) "Consider segmenting it; new players versus veteran players or different player types."
- [33:46](https://youtu.be/j6OPA95-1O0?t=2026) "Remember your audience. Thumbnail tests are typically shown on home recommendations to new players."

## On screen
Contact sheet shows Experimentation 101 coin-flip confidence-interval chart, the Experiments dashboard with 'Decision needed' status, D1 retention +37% and session time -2% stat-sig results, Adopt Me trade-restriction mockup (CookieCutterYT trade window), Adopt Me data analysis chart segmented by cohort, and thumbnail A/B cards (Dog Walk control vs Kaijunior Stomp variant).

## Topics
[[analytics-metrics]] [[common-mistakes]] [[community-and-discord]] [[core-loops-and-game-design]] [[development-process-and-speed]] [[monetisation-devproducts]] [[monetisation-gamepasses]] [[playtesting-and-feedback]] [[thumbnails-icons]]

Back to [[MustWatch - How to make successful Roblox games]]
