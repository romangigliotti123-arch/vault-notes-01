---
name: codes-campaign-planner
description: "Plan a redeem-code campaign for a Roblox game: reward tiers tied to milestones and creators, unguessable per-creator codes from codes.py, a server-side CodeBook (normalise, window, per-player and global limits) wired to the kit systems, and the measurement table. Use when giving creators or the community codes; the economy impact check is part of it."
category: marketing
tags: codes, redeem codes, promo codes, creator codes, milestones, attribution, rewards, datastore, anti abuse
kb: Roblox/roblox-kb/social-features-and-virality.md, Roblox/roblox-kb/influencer-and-creator-marketing.md, Roblox/roblox-kb/community-and-discord.md, Roblox/roblox-kb/data-persistence.md, Roblox/roblox-kb/anti-exploit-and-security.md
related: influencer-outreach-writer, social-post-calendar, price-ladder-planner, datastore-schema-builder, remote-guard-builder, event-planner, community-showcase-planner
---

# codes-campaign-planner

Vault: give each creator a unique in-game code so you can see which one performs, pay small creators in items, ranks or skins, and offer community-only codes and small rewards so followers feel special. The risk is a leaked, guessable or over-generous code that wrecks the economy. This skill designs the campaign and the safe redemption path; it never grants anything itself.

## When to use
A creator deal, a milestone celebration (X likes, a Discord member count, an update), or a community reward. Not for: purchases (`gamepass-maker`, `devproduct-handler`), daily rewards (kit DailyRewards system).

## Inputs (max 3)
1. Campaign goal: attribution per creator, community reward, or milestone. 2. Creators or milestones list. 3. Reward budget in game terms (default: items worth about one early-game session, no premium currency).

## Procedure
1. Reward design: tie rewards to a goal (creator code: a cosmetic or boost that does not skip core progress; milestone: a one-time item). Keep the reward small, one-time and non-premium; never pay out the paid currency (`price-ladder-planner` for relative value). Reward an action you want (join the group, play the update).
2. Window and limits per code: start, expiry, per-player once, optional global cap. Creator codes expire later than community codes; milestone codes expire quickly.
3. Generate: `python -I .rbx/claude-kit/skillpack/marketing/codes-campaign-planner/scripts/codes.py --campaign launch --creator ethan --creator mia --prefix EGG --length 8 --expires 2026-12-31 --max-uses 5000 --out codes.csv`. Codes are random, without look-alike characters or vowels, so they cannot be guessed or spell words. Keep `codes.csv` out of the repo and out of any client-visible place.
4. Server book: copy `scripts/CodeBook.luau` beside your server code and load the book from a server-only ModuleScript. Run `CodeBook.validateBook(book)` at server start and fail loudly on any problem. On redeem: get the text through a rate-limited remote (kit RemoteGuard), call `CodeBook.check(book, text, state, os.time())`, and on `ok` increment the global count with `DataStore:UpdateAsync` and record the code in the player's PlayerData profile in the same step; only then grant the reward through your own server code (kit Shop or PlayerData). Return the same message for unknown and not-yet-started codes.
5. Tests: `lune run ../skillpack/marketing/codes-campaign-planner/scripts/tests/CodeBook.test.luau` from `.rbx/claude-kit/systems`, plus `bash .rbx/claude-kit/tools/roblox-project-template/luau-check.sh scripts/CodeBook.luau`. Add your own test for the real grant path.
6. Measurement: a table `marketing/codes-results.csv`: code (creator), date range, redemptions, new players among them, D1 of redeemers vs organic, notes. Judge on at least 7 days; a late conversion may arrive weeks later (vault, indie). Retire codes that are leaked or farmed.
7. Announce: creator posts and `social-post-calendar` slots; never put a community code in an image only; say the expiry.
8. Policy: giveaways and promotions follow the platform's rules and the creator's disclosure duties; live-check Creator Docs. No real-money prizes or randomised paid rewards.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `multi_edit` to add `CodeBook.luau` and the server module -> `start_stop_play` -> `execute_luau` (Server) to call `CodeBook.check` with test codes and `get_console_output`. DataStore saves in Studio need API access enabled by the owner; otherwise `untested`.

## Fallback
Files plus Lune tests (headless). The real grant, DataStore count and the redeem UI are the owner's test with a published place.

## Evidence
`Roblox/roblox-kb/social-features-and-virality.md` (unique code per YouTuber to measure performance; pay small creators in items, ranks or skins; creator codes and tracked giveaways), `Roblox/roblox-kb/influencer-and-creator-marketing.md` (gate giveaways behind tracked links, let creators pick prizes; judge on long-tail; show creator-themed content only to link users), `Roblox/roblox-kb/community-and-discord.md` (codes, early access and previews as community-only perks), `Roblox/roblox-kb/data-persistence.md`, `Roblox/roblox-kb/anti-exploit-and-security.md` (server authority, validate remote input). The vault itself notes that creator-deal and promo-code mechanics are thinly covered: treat the design as a pattern, not a proven recipe.

## Output
`marketing/codes-plan.md` (goal, reward table, limits, rollout dates), `codes.csv` (private), server `CodeBook` module and test results, `codes-results.csv` template.

## Acceptance checks
- [ ] `codes.py --selftest` and the Lune test pass (quote "6 passed, 0 failed").
- [ ] `validateBook` returns no problems for the real book.
- [ ] No code or book is reachable from a LocalScript or ReplicatedStorage.
- [ ] Redemption is once per player and survives rejoin (stored in the profile).
- [ ] Rewards do not skip core progress and exclude premium currency.

## Pitfalls
Guessable codes ("EGG100"). Client-side checks. Counting redemptions only in server memory so two servers overshoot a cap. Codes that never expire. Posting a creator code publicly and losing attribution.

## Related
`influencer-outreach-writer`, `social-post-calendar`, `price-ladder-planner`, `datastore-schema-builder`, `remote-guard-builder`.
