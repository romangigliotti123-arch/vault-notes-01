---
name: rbx-monetize-audit
description: "Audits a Roblox game's monetisation (gamepasses, developer products, starter pack, prices, store UX, Premium, ProcessReceipt security, pay-to-win and RNG risks) against the knowledge-base checklist: scorecard, fixes, three price experiments. Use to check what you sell and how it is priced."
---

# Roblox monetisation audit

Output: scorecard + fixes + experiments, each sourced. For a full redesign use the `rbx-money` agent.

## Procedure

1. Collect facts (assume and state): genre/loop, audience age, list of current offers with Robux prices and type, how and where each is shown, metrics (payer conversion, ARPPU, transactions per 30 days, D1), whether prices are scripted via MarketplaceService, RNG items, Premium/subscription/rewarded-ads use.
2. Load the checklist: `<KB>/_tools/CHECKLIST-monetization.md` (read the `Must` lists), plus `PRICE-LADDER.md` (top sections).
3. Add targeted evidence:
   ```
   K="bash .rbx/claude-kit/tools/pyrun .rbx/claude-kit/tools/kbq.py"   # run `$K where` once to see VAULT/KB/ASSETS
   $K section monetisation-devproducts instructions
   $K section monetisation-gamepasses instructions
   $K section pricing instructions
   $K find "<genre> best selling offers" -n 6
   $K find "pay to win" -n 5
   $K docs "ProcessReceipt purchase handling" -n 4
   $K num "payer conversion ARPPU"
   ```
4. Score each Must item pass / fail / unknown with evidence. Key checks: repeatables are developer products, permanent perks are passes (about 2-6); very cheap entry offer and a spread of tiers; starter pack after the tutorial or first milestone; offers shown at moments of need; nothing sells challenge removal or gates core progress; paid random items disclosed or avoided; ProcessReceipt idempotent and persists before granting; prices scripted (needed for Price Optimization, regional pricing, Plus discounts); sales are genuine and time-bound.
5. Price tests: Price Optimization needs about 60k transactions per 30 days and scripted prices; below that run manual A/B, one change at a time.

## Output template

```
Verdict (3 lines)
Scorecard: item | pass/fail/unknown | evidence or fix | source+flag | fair/pressure
Fix list: ranked, effort S/M/L, expected effect (KB example, flagged)
Experiments (3): change | metric | duration | success threshold | stop rule
Risks: pay-to-win, RNG disclosure, child safety, economy inflation
Benchmarks: metric | yours | KB band | flag (use compare.py in rbx-metrics)
```

## Fair or pressure column
Many Roblox players are children. For every offer, prompt and retention hook the audit touches, label the version in use and fix `pressure` ones. Vault rules win on conflicts (marked V).
| Hook | Fair | Pressure |
|---|---|---|
| Random rewards | V: none sold for Robux (eggs, spins, crates, luck boosts). Free rolls earned by play, honest odds, a guaranteed minimum | Paid rolls, hidden odds, faked near-misses. Roblox allows paid random items only with every outcome and its odds shown and `PolicyService` `ArePaidRandomItemsRestricted` honoured; this vault still fails them |
| Scarcity | Restock rushes of minutes during play | Purchase countdowns, "never coming back", fake sales |
| Loss and streaks | Protection earned by play, grace days | Losses only a purchase prevents, streak wiped by one missed day |
| Prompts | After a win or at a need, dismissible, a one-line benefit | During intense play, timed to an emotional peak, confusing currency conversion hiding the Robux cost |
| Status | Cosmetics others see, co-op bonuses | Status for sale, shaming non-payers |
| Return hooks | Daily reward that costs nothing to skip | Absence destroys progress |
Questions per hook: what does the player get if they ignore it, does missing it punish, would you explain it to a parent. Credit: adapted from excaldev/ro-engineer `retention-psychology.md` and `player-incentives.md` (MIT, Copyright (c) 2026 excaldev), reference copies in Imported/ro-engineer.

## Rules

- Official stance beats indie: cosmetics and convenience yes; selling challenge removal in competitive play is an unverified counter-view, show it only as such.
- Prices are proposals to test; revenue is never promised; any forecast is ESTIMATE with arithmetic.
- No changes to the live game; audit only.
