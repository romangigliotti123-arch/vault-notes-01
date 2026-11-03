---
name: rewarded-ad-planner
description: "Plan rewarded video ad placements and rewards for a game: eligibility, natural-break placements, optional deterministic consumable rewards, and a check of the plan against the vault's reported targets with a daily-volume estimate. Use when considering rewarded ads; buying ads to promote a game is a different job (game-dev-ads)."
category: money
tags: rewarded video, rewarded ads, ads, placement, reward, opt-in, eligibility, dau, monetisation, non-payers
kb: Roblox/roblox-kb/monetisation-other.md, Roblox/roblox-kb/ads-and-sponsored-experiences.md, Roblox/roblox-kb/ads-stats-monetisation-playbook.md, Roblox/roblox-kb/analytics-metrics.md, Roblox/roblox-kb/_tools/CHECKLIST-monetization.md
related: offer-timing-planner, economy-balancer, pay-to-win-checker, shop-conversion-optimizer, game-dev-ads, premium-benefits-planner
---

# rewarded-ad-planner

One job: decide where a rewarded video fits and what it gives, without hurting the paid shop or the fun. Rewarded video is a beta-style platform feature with eligibility conditions (the vault reports roughly 100,000 DAU during the beta); everything below is Roblox Creator Docs 2026-10 and creator talks and must be live-checked. This skill plans USING ads inside your game; buying ads to promote it is `game-dev-ads` / `roblox-ad-campaign-planner`.

## When to use
A game with enough daily players wants a revenue source from non-payers. Not for: promoting the game (`game-dev-ads`), immersive ads or portals (read `ads-and-sponsored-experiences.md` first).

## Inputs (max 3)
1. DAU and platform mix (default: read the dashboard). 2. The game's natural breaks (lobby, death, results, between rounds) (default: ask). 3. Currencies and paid boosts the reward could overlap (default: read the shop).

## Procedure
1. Read the rules: `python -I ~/.claude/claude-kit/tools/kbq.py section monetisation-other rules --max-chars 5000` (rewarded video rule) and `section ads-and-sponsored-experiences rules --max-chars 4000`. Live-check eligibility and the forecast tools.
2. Pick placements at natural breaks only: lobby, death, results, between rounds. Never mid-fight or mid-run. Make the offer prominent, one or two clicks, with the exact reward stated (vault).
3. Choose rewards: optional, deterministic (no RNG), fixed, not tied to your top item, consumables rather than permanent upgrades. Vault ideas: double offline earnings, doubled post-match XP, trials, temporary auto-click, progressive rewards. Keep each reward below the value of the cheapest paid item that does the same thing, so ads do not cannibalise purchases; check with `economy-balancer`.
4. Plan the numbers and run the check: `python -I ~/.claude/claude-kit/skillpack/money/rewarded-ad-planner/scripts/ad_plan.py --dau <n> --optin <0-1> --views <per opted-in player per day> --reward-rate <0-1> --length <seconds> --placement lobby,death,results`. Targets reported by the vault: reward rate 90%+, opt-in 10%+, 3+ views per day, length 6-30 s, DAU near the beta floor. Exit 1 lists failures. These are targets to aim at, not guarantees.
5. Players who likely buy: the platform offers an option to exclude likely purchasers; use it only when players can choose between paying and watching (vault).
6. Never let the reward arrive without the ad completing: the grant happens on the server after the platform's completion signal (live-check the API); the client only asks.
7. Plan measurement: opt-in rate, views per day, reward rate, effect on purchases (`shop-conversion-optimizer`), effect on session length. The vault reports expected ad revenue shares of up to about 3% early and 5-10% long term (Driving Empire about 7%); treat as context only.
8. Write the owner checklist (enrol, enable, set placements, monitor). You never enrol or enable ads.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `multi_edit` for the offer button and server grant -> `start_stop_play` -> `get_console_output`. Ads do not serve in Studio and require enrolment on a published place: the real flow is `untested`.

## Fallback
Plan document plus `ad_plan.py` (headless). Everything platform-side stays `untested`.

## Evidence
`Roblox/roblox-kb/monetisation-other.md` ("Rewarded video: placement, rewards, eligibility": natural breaks, optional deterministic consumable rewards, targets, ideas, about 100k DAU beta, 3% early and 5-10% long term, Driving Empire about 7%), `Roblox/roblox-kb/ads-and-sponsored-experiences.md`, `Roblox/roblox-kb/ads-stats-monetisation-playbook.md`, `Roblox/roblox-kb/analytics-metrics.md`. Numbers are dated 2026-10 and platform-reported: live-check.

## Output
`design/rewarded-ads.md`: eligibility status, placement table, reward table with cannibalisation check, `ad_plan.py` output, measurement plan, owner checklist.

## Acceptance checks
- [ ] `ad_plan.py` output quoted; every FAIL has a plan or a reason.
- [ ] `python -I .../ad_plan.py --selftest` prints "4 checks ok".
- [ ] Every placement is a natural break; none are mid-action.
- [ ] Rewards are optional, deterministic and consumable; granted on the server only.
- [ ] Eligibility and targets are marked live-checked with a date or unverified.

## Pitfalls
Rewards bigger than what paying gets. Random rewards. Interrupting play. Promising uplift. Forgetting that eligibility may exclude small games. Granting on the client's say-so.

## Related
`offer-timing-planner`, `economy-balancer`, `pay-to-win-checker`, `shop-conversion-optimizer`, `game-dev-ads`.
