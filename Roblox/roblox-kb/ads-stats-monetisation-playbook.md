---
title: Roblox ads, stats and monetisation playbook
tags: [roblox, knowledge-base, ads, analytics, monetisation, playbook]
built: 2026-11-01
---

# Ads, stats and monetisation playbook

Synthesis of this KB (see [[ads-and-sponsored-experiences]], [[analytics-metrics]], [[retention-d1-d7]], [[monetisation-gamepasses]], [[monetisation-devproducts]], [[monetisation-other]], [[pricing]], [[_tools/AD-PLAYBOOK]], [[_tools/BENCHMARKS]]) plus official pages re-fetched on 2026-11-01. Numbers are guides, not guarantees. Always re-check the live Ads Manager UI; the product changes often.

Trust labels: **OFFICIAL** (Roblox docs / staff post, fetched this session or cited in KB) | **CORROBORATED** (2+ independent creators, or creator + official-consistent) | **SINGLE-SOURCE** | **CONTRADICTED** | **OUTDATED-UNSURE**.

## 0. Rules that override everything
1. Ads are retrieval and seed, not a ranking hack. Ad-acquired users are excluded from Recommended-For-You signals. OFFICIAL (Creator Docs ads-manager; discovery-faq via KB).
2. Fix D1 and first-session before spending. Ads on a leaky game burn Robux (failed campaigns in KB: 369,000 spent vs 64,506 earned; 100,000 spent vs 60,000 28-day revenue). SINGLE-SOURCE each, but consistent direction: CORROBORATED.
3. Spend only Robux you can lose. Ad-credit conversion Robux -> credits is irreversible. OFFICIAL.

## 1. What each stat means and what to aim for

Targets come mostly from indie creators (TRUSTED tier in [[creator-credibility]]) because Roblox publishes definitions, not ranges. Official definitions: create.roblox.com/docs/production/analytics/get-started (fetched 2026-11-01).

| Stat | Meaning | Rough target (new/early game) | Label |
|---|---|---|---|
| D1 retention | % of new players who return the next day. Low = weak onboarding (official reading) | 10%+ ok, 12-15% "very good". Platform-wide anchor (GameAnalytics 2026, 500+ games over 1M MAU, Aug 2025-Jul 2026): median 10.3%, top 1% 22.2%; smaller games likely lower.  DevForum benchmark example: 50th-90th percentile 12.4-24.1% (2023, OUTDATED-UNSURE). Genre matters; check Roblox "similar experience" benchmarks in Analytics | CORROBORATED (VuukStudios, janisjanis01, MoseyTube) |
| D7 | Return after 7 days. Low = weak progression | 2-3% pretty good; D7 above expectation = strong daily habit. GameAnalytics 2026: median 1.6%, top 1% 9.1% | CORROBORATED (indie) + SINGLE-SOURCE third-party anchor |
| D30 | Return after a month. Low = no end-game or goals | GameAnalytics 2026 (secondary summary): median 0.5%, top 1% 4.7%, games over 1M MAU only. Official: low D30 = no end-game content/goals; no official number. Use your Similar Experience Benchmarks percentile | SINGLE-SOURCE (third-party), definition OFFICIAL. A genre table (obby D30 <5%, roleplay 8-15%) from rowatcher.com has no cited data or date: WEAK, not adopted; it also conflicts with the 0.5% median |
| Play-through rate / QPTR | % of impressions that become plays / qualified plays (stay past the bounce window, discovery metric) | PTR over 1% floor, 2-3% very good, 4% excellent; QPTR ~3% healthy. Roblox sample talk: QPTR 3.50% (2024) | CORROBORATED; one OFFICIAL sample |
| Thumbnail / ad CTR | clicks per impression | Ads: 1% bad, ~2% average, 2.5% day-one target, 3%+ good; tower/niche genres reported up to 4.5-8% | CORROBORATED (Raul, Yann, MoseyTube, janisjanis01); 2021 broad ad 0.019% = OUTDATED-UNSURE |
| Avg session length | start to logout | Roblox sample talk: 10.2 min; GameAnalytics 2026 median 9.8, top 5% 16.6, top 1% 21.1. Aim 10+ min; compare to your genre | CORROBORATED (official sample + third-party median) |
| Payer conversion | % of all users who ever spent. Roblox calls it among the most important | Sample talk 1.63%; indie healthy 2-3%; simulators 2-5%; pets 0.3-0.75% reported. GameAnalytics 2026: 3.80% of players spent (4.2% two years earlier) | CORROBORATED range, wide |
| ARPPU | spend per payer ("spend depth") | Sample talk 573 Robux. GameAnalytics 2026 per-game ARPPU in USD: median $0.70, top 10% $2.33, top 5% $4.80, top 1% $55.31 (the two units differ; do not compare directly). Low ARPPU + high conversion = one purchase and nothing after | SINGLE official sample |
| ARPDAU | Roblox: avg spend per DAU, overall health | Official docs (re-fetched 2026-11-01) give neither range nor unit; GameAnalytics 2026 does not report ARPDAU. Indie/DevForum anecdotes: 0.15 poor; 0.5-1.5 low; 0.5-2 typical; 3-5 decent; top games above 2, up to 8. Unit unknown, so use only your own Analytics benchmark percentile | UNRESOLVED: anecdotal, unit unknown |
| Official ARPU anchor | Earnings-objective beta games footnote: "ARPU 6 Robux or higher in H1 2026" | use as rough minimum monetisation before Earnings ads | OFFICIAL (DevForum 2026-10-02) |
| Likes ratio | likes / (likes+dislikes) | no official or corroborated range. One DevForum anecdote calls a stable 80.6% good feedback; ~80% warning line stays a heuristic | SINGLE-SOURCE anecdote (DevForum) |
| Favourites | long-term interest signal | no target found in docs (analytics pages re-fetched 2026-11-01) or searches; trend only | thin spot, confirmed none |
| CCU | concurrent players; useful for pacing ad bursts, not a goal alone | n/a | -- |
| Cost per play (CPP, Ads Manager) | spend / plays | OFFICIAL benchmarks (DevForum 2025-08-05): Maximize Plays $0.008, Drive Retention $0.007, Reactivate $0.011. Indie day-one target $0.008 or better; reports 0.006-0.02+ | OFFICIAL (upgrades prior indie-only label) |
| ROAS | USD value of attributed earnings / spend (official). 100% = broke even; earnings counted up to 30 days after click | Keep above 100% to scale; OFFICIAL case: 277% at $250/day | OFFICIAL |
| Payback | days to recover spend | no official number; Roblox ROAS counts earnings up to 30 days after click, so use 100% ROAS at 30 days as break-even. Yann's 28-day window failed at 0.6 ratio | OFFICIAL window; target = derived, not a published number |

Early-harm thresholds in Experiments (OFFICIAL): playtime -10%, ARPU -20%, payer conversion -20%, min 10,000 players in first 24h.

## 2. Ad products (what to use when)

| Product | Use | Facts | Label |
|---|---|---|---|
| Sponsored experiences (Ads Manager) | Get plays for a game | Home sort row now dynamic (2nd-10th); 16:9 thumbnails, up to 10 rotated; auto-bidding (you set budget + duration, Roblox sets the bid); daily or lifetime budget; reports lag up to 48h, plays and earnings finalise up to 30 days | OFFICIAL |
| Search ads | Capture intent | Max 10 keywords per Ad Set, winner pays second-highest bid + $0.01, Visits objective only, no audience targeting, relevance is scored; Roblox says search-acquired users beat sponsored-experience users (2024) | OFFICIAL |
| Sponsored items | Promote Marketplace/UGC items only (not games) | Bid auction, minimum 10 Robux/day, cycles 24h-28 days; example 50/100/300 Robux bids -> 1x/2x/6x display. Erthlord test: 3,400 Robux spent, no clear gain | OFFICIAL mechanics; result SINGLE-SOURCE |
| Rewarded video (earn) | Monetise players without Robux | Earn = EPM (per 1,000 impressions) x impressions; publisher 13+, 2FA, ID verified; game 2,000+ average monthly unique visitors; reward worth about 3-10 Robux; rewards must be dev products; ads 6-30 s; call GetAdAvailabilityNowAsync right before showing | OFFICIAL. Re-checked 2026-11-01: NO EPM value or earnings example published (docs or launch thread). Docs expect 85%+ completion; launch FAQ: up to 3% of earnings early, 5-10% growth from ads products long term. Launch rule 100K DAU (2025) was replaced by 2,000 monthly uniques. 2023 immersive-ad anecdote (EPM 140 then ~50 Robux) is not rewarded video and outdated |
| Billboards / Portals / Immersive ads | In-game ad units / cross-promo | listed on Creator Docs advertise-on-roblox | OFFICIAL (no numbers) |
| Influencer / creator deals | Off-platform traffic | see [[influencer-and-creator-marketing]]; no price list found in 2026-11-01 search; DevForum threads show Robux/perk pay negotiated by channel size; one commenter claims big YouTubers pull few players | anecdotal, UNRESOLVED |

Objectives (RESOLVED 2026-11-01, OFFICIAL Creator Docs ads-manager): current names are **Plays** (players likely to start a session), **Earnings (Limited)** (likely to spend Robux; success = ROAS; needs developed economy) and **Engagement** (age-checked highly engaged players; smaller audience, usually higher CPP; in beta, can overspend so pause manually). Audiences are a separate setting: All / New (never played or 180+ days) / Recent (last 30 days) / Lapsed (30-180 days). The 2025-08 DevForum list (Maximize Plays, Acquire New Users, Drive Retention, Reactivate) is the older scheme; its CPP benchmarks (Plays $0.008, Retention $0.007, Reactivate $0.011) were published under those names, so read them as the equivalent audience/objective setting. Confirm labels in the live dashboard.
- Mapping (inference, not official): Acquire New Users = Plays + New audience; Drive Retention = Plays + Recent; Reactivate = Plays + Lapsed. Earnings: reach likely spenders, success = ROAS.
- Audience size limits: Recent needs 10,000+ recent players; Lapsed 20,000+. OFFICIAL.
- Learning period: docs say first 24 h; staff (DevForum 2026-10-02) say 24-48 h and it restarts on each pause. CONTRADICTION resolved by planning for 48 h and not pausing/editing daily. OFFICIAL.

## 3. Ad-spend ladder

| Step | Gate to enter | Spend | Action | Exit / next |
|---|---|---|---|---|
| 0. Organic proof | D1 >=10% (ideally 12%+), tutorial bounce low, one working monetisation item | 0 | fix retention, ship 3+ thumbnails | go to 1 |
| 1. Creative test | Step 0 met | indie floor: $25 lifetime; typical $10/day x 7-11 days (~$100-200 total); Roblox says some popular games reached Home recs under $100. spend only what you can afford to lose | 2-4 thumbnails, broad audience, one change at a time; do not touch for first 24-48h | Keep thumbnails with CTR >=2.5%, CPP near $0.008 |
| 2. Quality read | after ~7 days (D1 cohort ready) | same | read D1/D7 of ad cohort vs organic, payer conversion, CPP | Ad cohort D1 near organic (heuristic, unsourced) -> go 3. Else fix game, stop |
| 3. Scale | ROAS/payback ok or retention holds | raise in modest steps (20-50% is an unsourced heuristic); official case doubled then tripled from $250/day while ROAS stayed above 100% | add Reactivate/Retention for updates; continuous campaign | repeat read each step |
| 4. Earnings / ROAS mode | monetisation thresholds; roughly ARPU 6+ Robux | reinvest up to 4% of daily earnings (OFFICIAL: ~2/3 of beta games doing that hit ROAS >100%) | use Estimated ROAS (early read, avoids 30-day wait) | stop if ROAS <100% two reads in a row |

Stop rules: ROAS under 100% after the attribution window, D1 of ad users collapsing, organic Home recs now exceed sponsored impressions (shrink), CPP double the benchmark with CTR fine (game page/thumbnail mismatch).
Official evidence ads are worth it: median 150% impression lift, 99% of 370 games saw lift (KB official); incrementality study 21 campaigns: median +14% incremental sessions, +10% D7 retained users (Plays objective). 71 of top 100 games use sponsored ads (2026). OFFICIAL. Treat the headline lift as an upper bound for small indie games.

## 4. Decision tree: if X is low, do Y
- **Impressions low** -> budget/bid too low or audience too narrow (check Audience Estimator); for organic, raise PTR first.
- **CTR low (<2%)** -> new thumbnail/icon (16:9, bright subject, readable at small size); see [[thumbnails-icons]].
- **CTR fine, plays/CPP bad** -> mismatch between thumbnail and game, or loading/join friction.
- **PTR/QPTR low after click** -> first 60-180 s bounce: shorten intro, immediate action, see [[first-session-onboarding]].
- **D1 low (<10%)** -> onboarding, first reward, clear next goal, return hook (daily reward, timed event). Do not run ads.
- **D1 ok, D7 low (<2%)** -> progression/mid-game gap, social features, content cadence; see [[updates-live-ops]].
- **D7 ok, D30 low** -> end-game goals, seasons, events.
- **Session short (below ~8 min, heuristic; sample talk 10.2)** -> add goals/pace; check crashes and load times.
- **Payer conversion low (<1-2%)** -> cheap starter offer (low-Robux entry price; see PRICE-LADDER for bands), show it after first win, A/B via Experiments; see [[pricing]].
- **Conversion ok, ARPPU low** -> add post-first-purchase content: tiers, repeat dev products, bundles.
- **ARPDAU low despite payers** -> add Robux sinks / whale tier; check item value ladder.
- **ROAS <100%** -> improve monetisation or retention before more spend; do not "scale out of it".
- **Likes ratio low** -> read comments; monetisation pop-ups, bugs, or paywalls are the usual cause.

## 5. Monetisation ladder (cheapest to build first)
1. Passes: permanent (2x, VIP, auto-collect). Highest value for simulators; ~76% of earnings in one ad test came from passes (SINGLE-SOURCE). OFFICIAL definition.
2. Developer products: consumable, repeatable (currency, boosts, revives, skip). Main revenue engine for loop games. OFFICIAL.
3. Starter pack / limited offer: Royal Egg starter pack (Adopt Me) +6% new-user ARPU and conversion, +2% D7, needed over a month for significance. OFFICIAL.
4. Subscriptions: recurring monthly benefits. OFFICIAL.
5. Rewarded video: add after economy is stable; 2,000 monthly uniques minimum. OFFICIAL.
6. Private servers, paid access, Roblox Plus incentives, price optimisation / managed pricing tools: situational. OFFICIAL list.
7. Creator Rewards: Premium engagement-based payouts programme is DEPRECATED (docs, 2025-07-24), replaced by Creator Rewards. Active Spender: $9.99 in 60 days; Daily Engagement Rewards need 10 minutes per active spender per day; "35% on first $100" is a DevForum figure (2026-02, SINGLE-SOURCE, verify). Top 15% of payers produce about 50% of revenue (OFFICIAL, analytics page).
Price points: see [[_tools/PRICE-LADDER]] and [[pricing]]. Cash-out: DevEx 0.0038 USD/Earned Robux, 0.0054 for qualifying 18+ US purchases, 30,000 minimum (OFFICIAL fetched 2026-11-01; resolves earlier indie "0.038" confusion, which was 10x off = CONTRADICTED). Pre-2025-09-05 balances 0.0035.

## 6. What to check weekly
Mon: D1 by day (cohort by first-play date), D7 of last week's cohort, session length, PTR/QPTR, CTR of each live thumbnail.
Mid-week: payer conversion, ARPPU, ARPDAU, top-selling offers, Robux sinks balance.
Ads: Spent, CPP vs $0.008, Estimated ROAS (Earnings), ad-cohort D1 vs organic, impressions/clicks real-time (plays and earnings lag up to 30 days).
Platform: likes ratio, crash rate, any Experiments result (harm thresholds), new DevForum ads announcements.
After each update: compare 7 days before/after for earnings, playtime, D1/D7.

## 7. Thin spots (updated 2026-11-01, chunk 2)
Resolved or improved:
- D30: third-party median 0.5% / top 1% 4.7% (GameAnalytics 2026, SINGLE-SOURCE, big games only); definition official. Still no official target.
- Objective names: resolved to Plays / Earnings (Limited) / Engagement with audiences (docs).
- Learning period contradiction (24 h vs 24-48 h): documented, plan 48 h.
- Platform medians for D1, D7, session, conversion, ARPPU added (GameAnalytics 2026).
- Payback: 30-day ROAS >=100% is the official-window break-even; no published payback days.
Still open:
- ARPDAU unit and genre ranges: no official or reliable source; only DevForum anecdotes.
- Likes-ratio and favourites targets: none official; one 80.6% anecdote.
- Rewarded-video EPM: not published by Roblox; only a 2023 immersive-ads anecdote.
- Influencer/creator deal pricing: no price list; anecdotal.
- Genre-specific CTR/retention/ARPDAU: only unsourced rowatcher tables (WEAK) and CTR hints; GameAnalytics summary had no genre split.
- YouTube extraction this chunk (haiku, 4 videos: Wulis 2025-07, ZeeZee 2023-04, med_v3 2025-03, FliedaDev 2026-09) yielded little: none of these creators is in the TRUSTED list, no new targets. Trusted creators' relevant videos were already in the KB.

## Sources fetched 2026-11-01
create.roblox.com/docs/production/promotion/ads-manager, /advertise-on-roblox, /rewarded-video-ads; /production/analytics/get-started; /production/monetization; /production/monetization/developer-exchange; /engagement-based-payouts; devforum.roblox.com/t/3862159 (2025-08-05, Ads Manager updates); devforum.roblox.com/t/4909790 (2026-10-02, Ads Manager RDC recap). Added in chunk 2 (2026-11-01): rewarded-video-ads docs and devforum.roblox.com/t/3838678 (2025-07/08, rewarded video launch); analytics-essentials docs (no numbers); gamedevreports.substack.com GameAnalytics 2026 Roblox report summary (third-party, secondary); rowatcher.com genre retention (unsourced, not adopted); YouTube Vi3Ck32SuiY, 7ZKZo0enAMU, DVUbZrF9cdw, 9AjRPKdinVw (extracted into data/research2). Everything else is from KB files above with their own timestamped links.
