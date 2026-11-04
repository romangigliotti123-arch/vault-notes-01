---
name: rbx-monetize-audit
description: "Audits a Roblox game's monetisation (gamepasses, developer products, starter pack, prices, store UX, Premium, ProcessReceipt security, pay-to-win and RNG risks) against the knowledge-base checklist: scorecard, fixes, three price experiments."
---

# Roblox monetisation audit

Output: scorecard + fixes + experiments, each sourced. Full redesign: `rbx-money` agent.

## Procedure

1. Collect facts (assume and state): genre/loop, audience age, current offers with Robux price and type, how and where each is shown, metrics (payer conversion, ARPPU, transactions per 30 days, D1), whether prices are scripted via MarketplaceService, RNG items, Premium/subscription/rewarded-ads use.
2. Load the checklist: `<KB>/_tools/CHECKLIST-monetization.md` (read the `Must` lists), plus `PRICE-LADDER.md` (top sections).
3. Add targeted evidence:
   ```
   K="bash $HOME/.claude/claude-kit/tools/pyrun $HOME/.claude/claude-kit/tools/kbq.py"   # run `$K where` once to see VAULT/KB/ASSETS
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
Many Roblox players are children. Label every offer, prompt and retention hook the audit touches fair or pressure and fix `pressure` ones. Vault rules win on conflicts (marked V).
Hooks to label: random rewards (V: none sold for Robux; free earned rolls with honest odds only; paid rolls and hidden odds are pressure and this vault fails them), scarcity, loss and streaks, prompts, status, return hooks. [cold:rbx-monetize-audit/fair-or-pressure.md] read only when labelling a hook fair or pressure (random rewards, scarcity, loss and streaks, prompts, status, return hooks).
Questions per hook: what does the player get if they ignore it, does missing it punish, would you explain it to a parent. Credit: adapted from excaldev/ro-engineer `retention-psychology.md` and `player-incentives.md` (MIT, Copyright (c) 2026 excaldev); copies in Imported/ro-engineer.

## Rules

- Official stance beats indie: cosmetics and convenience yes; selling challenge removal in competitive play is an unverified counter-view, show it only as such.
- Prices are proposals to test; revenue is never promised; any forecast is ESTIMATE with arithmetic.
- No changes to the live game; audit only.
