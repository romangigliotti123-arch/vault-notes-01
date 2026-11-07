---
name: vip-pass-designer
description: "Design a VIP (or similar permanent premium) pass whose perks are cosmetic and convenience first, stack safely with other passes under a capped multiplier, and do not break the economy; then audit the combined perks offline. Use when planning or fixing a VIP tier; the Shop wiring is gamepass-maker."
category: money
tags: vip, premium pass, perks, multiplier, stacking, cap, permanent, tier, bundle, economy
kb: Roblox/roblox-kb/monetisation-gamepasses.md, Roblox/roblox-kb/monetisation-other.md, Roblox/roblox-kb/pricing.md, Roblox/roblox-kb/_tools/PRICE-LADDER.md, Roblox/roblox-kb/core-loops-and-game-design.md
related: gamepass-maker, economy-balancer, pay-to-win-checker, price-ladder-planner, pass-ownership-cache-builder, starter-pack-designer, premium-benefits-planner
---

# vip-pass-designer

One job: decide what a VIP pass gives and prove the perks cannot compound into an economy break or a pay-to-win advantage. `gamepass-maker` already decides the whole pass set and wires ownership through the kit Shop system (`systems/Shop`, NOT live-tested); this skill goes deep on one high-value pass and its stacking.

## When to use
A VIP or "supporter" tier is planned, or an existing one makes buyers far richer than everyone else. Not for: subscriptions (`subscription-planner`), Premium membership perks (`premium-benefits-planner`), one-off boosts (`devproduct-handler`).

## Inputs (max 2)
1. The other passes and boosts that exist or are planned, with the currencies they touch (default: none). 2. Competitive modes, if any (default: assume pvp exists and keep VIP out of it).

## Procedure
1. Read the rules: `python -I .rbx/claude-kit/tools/kbq.py section monetisation-gamepasses rules --max-chars 4000`. Note the flags (official vs indie) and the "free players must reach all core content" rule.
2. List candidate perks in three buckets: identity (chat tag, name colour, lobby area, cosmetic), convenience (extra storage, auto-collect, faster queue, saved loadouts), progression speed (a multiplier). Prefer the first two; the vault warns that single XP or coin boosters cap spend and that buyers who never need to spend again lower lifetime value.
3. If you include a multiplier, keep it small and let `scripts/PerkStack.luau` combine it with every other perk: bonuses ADD (2x and 1.5x give 2.5x) and clip to a cap you choose (default 3, a starting point). Run `PerkStack.audit` over every perk you plan to sell to see which targets would exceed the cap if one player owned all of them.
4. Check the share: `PerkStack.perkShare(multiplier)` shows what fraction of a buyer's income comes from the perk (2x means 0.5). If free players would earn under half of a buyer's rate in a shared mode, cut the multiplier or move the perk to cosmetics.
5. Run `pay-to-win-checker` on the final list: no perk may change damage, health or aim in competitive play or gate core progress.
6. Price with `price-ladder-planner` (core or higher rung; bundle logic: a bundle of all current and future passes at a modest discount is a creator-reported pattern, test it).
7. Wire: the pass goes in `Passes.luau` (`gamepass-maker`); perks read `ShopService.HasPass(player, "VIP")` on the server at the moment a reward is computed, then call `PerkStack.multiplier(activePerks, "coins", cap)`.
8. Test: `lune run ../skillpack/money/vip-pass-designer/scripts/tests/PerkStack.test.luau` from `.rbx/claude-kit/systems`.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `multi_edit` to add `PerkStack.luau` and the reward code -> `start_stop_play` -> `execute_luau` (Server) to compute a reward for a test player with and without the pass (`ShopService.HasPass`) -> `get_console_output`. Buying the real pass needs a published place and a test account: `untested` until the owner buys.

## Fallback
Files plus the Lune test; the stacking maths is fully testable headless. Perk feel and the purchase flow stay `untested`.

## Evidence
`Roblox/roblox-kb/monetisation-gamepasses.md` (never gate core progress; cosmetics and convenience over power; small valuable set; counter-views flagged indie), `Roblox/roblox-kb/monetisation-other.md` (pay-to-win rules; genre pricing; bundling passes at a discount, creator-reported), `Roblox/roblox-kb/pricing.md` (test prices; regional pricing), `Roblox/roblox-kb/core-loops-and-game-design.md` (sources and sinks). Multiplier caps are this skill's heuristic, not a vault number.

## Output
`design/vip.md`: perk table (perk, bucket, target, multiplier, risk flags), stacking audit output, price and rung, rejected perks with reasons, Creator Hub checklist, test steps; code `PerkStack.luau` and the reward hook.

## Acceptance checks
- [ ] `PerkStack.audit` over all planned perks lists no target above the cap, or the design says why.
- [ ] No perk gates core progress or changes pvp outcomes (`pay-to-win-checker`: 0 blocks).
- [ ] Perks are checked on the server at use time via Shop/`HasPass`, not from a client flag.
- [ ] `lune run` PerkStack tests pass (quote "6 passed, 0 failed") and luau-check is clean.
- [ ] Price came from the ladder with a "test this" note; ids are `0` placeholders.

## Pitfalls
Multiplicative stacking (2x times 2x times 2x). A permanent multiplier that makes every later purchase pointless. Giving VIP an advantage in the only competitive mode. Checking the pass once at join and never after a mid-session purchase.

## Related
`gamepass-maker`, `economy-balancer`, `pay-to-win-checker`, `price-ladder-planner`, `pass-ownership-cache-builder`, `premium-benefits-planner`.
