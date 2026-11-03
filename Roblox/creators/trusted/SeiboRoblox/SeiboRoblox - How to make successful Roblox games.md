---
title: SeiboRoblox - How to make successful Roblox games
tags: [roblox, seiboroblox, playbook]
videos: 4
generated: 2026-10-29
credibility: trusted
credibility_score: 7.8
creator_trust: TRUSTED
creator_score: 7.8
---

> [!note] Trust: TRUSTED (credibility audit score 7.8): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# SeiboRoblox - How to make successful Roblox games

Based on four analytics devlogs from one party/casual game (1v1 IQ Race), the creator's method is: pick a short-session genre, hook new players in the first session, fix click-through, use sponsored ads only as a bridge to organic discovery, then monetise through Robux prompts, gamepasses and Creator Rewards. He tracks a small metric set (first-session retention, D1/D7, CTR, conversion, CCU, age-checked share) and treats numbers as signals to act on. Latest position (NNcwnxblzQgxg, Oct 10): retention is climbing, monetisation is weak, so he is shipping a revenue-focused update. Evidence is self-reported and some figures conflict.

**Style:** Transparent, numbers-first solo developer sharing raw dashboards close to real time. Strong at diagnosing metrics and tapering ad spend; light on prescriptive fixes and few outcomes are confirmed. Suits developers with a short-session party or casual game who want a metric checklist to benchmark against.

## Playbook
1. **1. IDEA: Pick a short-session party/casual concept** [[game-ideas-and-genres]]: The example, 1v1 IQ Race, sits in party/casual with ~11-minute average sessions (NqW98hvXUhc). Check the concept's session length and retention against genre benchmarks before committing to a build. Creator gives no formal benchmark source.
2. **2. BUILD: Design the first session to hook new players** [[first-session-onboarding]]: New-user first-session retention was 71% over 3 days (NqW98hvXUhc). It rose to 71.5% from under 50% about a month earlier (Fh0Xku6NwOQ). The creator does not document which onboarding changes drove the gain.
3. **3. BUILD: Instrument the new-user funnel** [[analytics-metrics]]: Track new-user funnel conversion (6.1%), D1 and session time. D1 was 9.58% on Sep 26 (NqW98hvXUhc) but 8.23% on Oct 2 (Fh0Xku6NwOQ), which the creator calls improving. Confirm metric windows and definitions before drawing conclusions.
4. **4. LAUNCH: Fix thumbnail and title click-through first** [[thumbnails-icons]]: QBTR of 1.29% was called 'awful' (NqW98hvXUhc) and thumbnail CTR of 1.29% 'horrible' (Fh0Xku6NwOQ). Impression CTR was ~10%. Test thumbnail and title variants to lift QBTR; the creator asked viewers for help and shows no confirmed fix.
5. **5. LAUNCH: Verify the correct build before publishing** [[testing-debugging-and-qa]]: An accidental bugged release caused a sharp player drop that the creator had to fix (FmAD02FS_3k). Confirm the exact place version and test it in a private or staging place before pushing to live players.
6. **6. GROWTH: Use sponsored ads as a bridge, then taper** [[ads-and-sponsored-experiences]]: Credits per day ran 10-16 from Aug 26, 14 (Aug 28-Sep 3), 8-10 (Sep 3-11), then 3 (Sep 15-29), about 170 total (FmAD02FS_3k). He cut spend when organic home-recommendation players overtook ad-driven players; sponsored sessions reached zero by ~Oct 1 (Fh0Xku6NwOQ).
7. **7. GROWTH: Check audience age mix and age-check status** [[age-ratings-moderation-and-tos]]: 22% of players were not age-checked, which the creator calls bad (cwnxblzQgxg). He wants older, age-checked players, who he says spend more Robux. US share rose from ~2% to ~9% to 14.1% across the videos. Largest age group was 18-20 (Fh0Xku6NwOQ).
8. **8. GROWTH: Check Creator Rewards eligibility** [[monetisation-other]]: Creator Rewards alone brought 12K Robux in 28 days (NqW98hvXUhc) and 35k Robux by Oct 2 (Fh0Xku6NwOQ). The creator treats it as close to free revenue. Check whether your game qualifies, as it is a major revenue source for him.
9. **9. GROWTH: Lift the share of paying players toward 2%** [[monetisation-gamepasses]]: Monetisation was 0.6% of players paying against a 2% target (NqW98hvXUhc). The paying-user conversion rate was 0.32 and unchanged by Oct 10 (cwnxblzQgxg). Improve paywall placement and gamepass offers, then re-measure.
10. **10. GROWTH: Fix the Robux prompt funnel** [[monetisation-devproducts]]: About 7,000 players saw the Robux prompt and about 100 bought, roughly 1% (Fh0Xku6NwOQ). ARPDAU was 0.15, called horrible, with currency unstated. Investigate prompt placement and offer value before adding more traffic.
11. **11. LIVE OPS: Announce big updates publicly before release** [[updates-live-ops]]: 11.6k users showed interest in the upcoming ~10-hour update before release (cwnxblzQgxg). The creator expects this to lift peak CCU. Results were not yet shown at the time of the last video, so track CCU after release.
12. **12. LIVE OPS: Ship a revenue-focused update when monetisation lags** [[updates-live-ops]]: The creator says monetisation is weak and is building a ~10-hour revenue-focused update (cwnxblzQgxg, Oct 10, the latest video). Measure paying-user conversion (0.32) and ARPDAU after release to judge whether the update worked.
13. **13. LIVE OPS: Judge retention on D7 trend and CCU range** [[retention-d1-d7]]: Retention was described as stable and climbing again, while average playtime slowly fell to the 73rd percentile, which he is not worried about (cwnxblzQgxg). 7-day CCU swung from ~100 to ~1,200. Judge stickiness on several weeks of D7 data, not one reading.

## Key numbers
- NqW98hvXUhc: new-user first-session retention 71% (past 3 days); Gemini called it excellent, not verified against Roblox benchmarks
- NqW98hvXUhc: D1 9.58%; new-user funnel conversion 6.1%; QBTR 1.29%; impression CTR ~10%
- NqW98hvXUhc: CCU current 457, 7-day peak 592; average session ~11 minutes
- NqW98hvXUhc: monetisation 0.6% of players paying (target 2%); 10K Robux in 3 days; 12K Creator Rewards Robux in 28 days
- Fh0Xku6NwOQ: new-user session retention 71.5%, up from under 50% about one month earlier; D1 8.23%
- Fh0Xku6NwOQ: Robux prompt ~7,000 saw, ~100 bought (~1%); ARPDAU 0.15 (currency unstated); 35k Creator Rewards Robux
- Fh0Xku6NwOQ: CCU ~1,000 (stable 500-1,000); session 10-30 minutes; thumbnail CTR 1.29%
- FmAD02FS_3k: ad credits per day 10-16 (Aug 26), 14 (Aug 28-Sep 3), 8-10 (Sep 3-11), 3 (Sep 15-29); ~170 total on top campaign
- Fh0Xku6NwOQ: sponsored ad sessions fell from 18 to zero around Oct 1
- FmAD02FS_3k: CCU 897 recently, fluctuating; creator hopes to stabilise at 1K
- cwnxblzQgxg: CCU current 714; 7-day peak ~1,200 (range ~100-1,200)
- cwnxblzQgxg: 11.6k users interested in upcoming ~10-hour update
- cwnxblzQgxg: paying-user conversion 0.32; QPTR 1.76 and rising; average playtime 73rd percentile, slowly declining
- cwnxblzQgxg: not-age-checked players 22% (called bad); US player share 14.1%
- Fh0Xku6NwOQ: demographics US 12.7%, Thailand 12.9%; largest age group 18-20

## Common mistakes
- Publishing an unverified build: an accidental bugged release caused a sharp player drop (FmAD02FS_3k).
- Continuing ad spend after organic home-recommendation players overtook ad-driven players (FmAD02FS_3k).
- Ignoring low QBTR (1.29%) while focusing on retention and playtime (NqW98hvXUhc, Fh0Xku6NwOQ).
- Trusting an AI tool's benchmark (Gemini called 71% first-session retention excellent) without checking Roblox benchmarks (NqW98hvXUhc).
- Mixing monetisation metrics with different definitions: 0.6% paying, ~1% Robux prompt conversion, 0.32 conversion, and ARPDAU 0.15 with unstated currency (NqW98hvXUhc, Fh0Xku6NwOQ, cwnxblzQgxg).
- Leaving 22% of players not age-checked and missing older, higher-spending audiences (cwnxblzQgxg).
- Judging stickiness from a single D7 reading rather than several weeks of trend (Fh0Xku6NwOQ).
- Reading CCU from a single snapshot; 7-day CCU swung from ~100 to ~1,200 (cwnxblzQgxg).
- Accepting 0.6% paying players as acceptable when the creator's target is 2% (NqW98hvXUhc).

## Launch checklist
- [ ] Verify the exact build and place version before publishing (FmAD02FS_3k).
- [ ] Test thumbnail and title variants before launch; track QBTR against the creator's 1.29%, which he called awful (NqW98hvXUhc).
- [ ] Set up tracking for new-user first-session retention, D1, D7, funnel conversion and session time.
- [ ] Benchmark first-session retention against your genre using Roblox data, not AI estimates (NqW98hvXUhc).
- [ ] Confirm Creator Rewards eligibility before counting it as revenue (NqW98hvXUhc, Fh0Xku6NwOQ).
- [ ] Set a sponsored-ad budget with a planned taper, and a rule to cut spend when organic players overtake ad-driven players (FmAD02FS_3k).
- [ ] Plan age-check coverage; track the not-age-checked share, which was 22% (cwnxblzQgxg).
- [ ] Design paywall and gamepass placement tests aimed at lifting paying players from 0.6% toward 2% (NqW98hvXUhc).
- [ ] Test Robux prompt placement and offer value, since about 1% of prompt viewers bought (Fh0Xku6NwOQ).
- [ ] Define ARPDAU with its currency before reporting it (Fh0Xku6NwOQ).
- [ ] Announce any big update publicly before release to build interest (cwnxblzQgxg).
- [ ] Track CCU over 7-day windows, not single snapshots (cwnxblzQgxg).

## How the advice changed over time
- Sep 26 (NqW98hvXUhc) framed QBTR and monetisation as the main problems; Oct 2 (Fh0Xku6NwOQ) kept thumbnails and conversion as open asks for help, with no confirmed fix.
- Ad credits per day stepped down from 10-16 (Aug 26) to 3 (Sep 15-29) as organic players overtook ad players; sponsored sessions reached zero by ~Oct 1 (FmAD02FS_3k, Fh0Xku6NwOQ). Latest advice is to taper ads, not scale them.
- Monetisation focus moved from 0.6% paying players (NqW98hvXUhc) to ~1% Robux prompt conversion (Fh0Xku6NwOQ), then to a 0.32 conversion rate reported unchanged. Latest advice (cwnxblzQgxg, Oct 10) is a revenue-focused update.
- Retention framing shifted from a 71% first-session figure called excellent (NqW98hvXUhc) to tracking climbing retention and slowly falling playtime with no stated concern (cwnxblzQgxg).
- D1 figures conflict: 9.58% on Sep 26 (NqW98hvXUhc) versus 8.23% on Oct 2 described as improving (Fh0Xku6NwOQ). Treat as unreliable until windows are confirmed.

## Theme notes
- [[SeiboRoblox - Retention|Retention]]
- [[SeiboRoblox - Monetisation|Monetisation]]
- [[SeiboRoblox - Discovery & Algorithm|Discovery & Algorithm]]
- [[SeiboRoblox - Thumbnails & Icons|Thumbnails & Icons]]
- [[SeiboRoblox - Updates & Live Ops|Updates & Live Ops]]
- [[SeiboRoblox - Mindset & Process|Mindset & Process]]
- [[SeiboRoblox - Games Mentioned]]
- [[SeiboRoblox - Numbers & Benchmarks]]
- [[SeiboRoblox - Tools & Resources]]
- Cross-creator knowledge base: [[README]]

## All videos (oldest first)
- [[2026-09-26 - My FULL Roblox Game Analytics!!!|My FULL Roblox Game Analytics!!!]] (8,735 views, 2026-09-26): Full analytics for 1v1 IQ Race: 71% first-session retention, weak 1.29% QBTR, low monetisation.
- [[2026-10-02 - ROBLOX GAME FULL ANALYTICS (part 2)|ROBLOX GAME FULL ANALYTICS (part 2)]] (7,757 views, 2026-10-02): Part 2 at ~1,000 CCU: retention improving, Robux conversion 1%, thumbnail CTR flagged as horrible.
- [[2026-10-04 - how much I spent on ADS (Roblox Analytics)|how much I spent on ADS (Roblox Analytics)]] (7,296 views, 2026-10-04): Ad credits cut from 14 to 3 per day once organic home-recommendation players overtook ad players.
- [[2026-10-10 - My Roblox Game ANALYTICS (Part 3)|My Roblox Game ANALYTICS (Part 3)]] (4,028 views, 2026-10-10): Part 3: CCU swings 100 to 1,200, retention climbing, playtime slipping; 10-hour revenue update announced.
