---
name: roblox-monetization-audit
description: Audits a Roblox game's monetisation (gamepasses, developer products, starter pack, prices, store UX, Premium/subscriptions, ProcessReceipt security, pay-to-win and RNG risks) against the merged knowledge-base checklist and returns a pass/fail scorecard, fixes and three price experiments. Use when the user asks to audit, review, fix or price their Roblox game's monetisation, passes or products.
---

# Roblox monetisation audit

Output: scorecard + fixes + experiments, each sourced. For a full redesign use the `roblox-monetization-consultant` agent.

## Procedure

1. Collect facts (assume and state): genre/loop, audience age, list of current offers with Robux prices and type, how and where each is shown, metrics (payer conversion, ARPPU, transactions per 30 days, D1), whether prices are scripted via MarketplaceService, RNG items, Premium/subscription/rewarded-ads use.
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
Scorecard: item | pass/fail/unknown | evidence or fix | source+flag
Fix list: ranked, effort S/M/L, expected effect (KB example, flagged)
Experiments (3): change | metric | duration | success threshold | stop rule
Risks: pay-to-win, RNG disclosure, child safety, economy inflation
Benchmarks: metric | yours | KB band | flag (use compare.py in roblox-metrics-benchmarks)
```

## Rules

- Official stance beats indie: cosmetics and convenience yes; selling challenge removal in competitive play is an unverified counter-view, show it only as such.
- Prices are proposals to test; revenue is never promised; any forecast is ESTIMATE with arithmetic.
- No changes to the live game; audit only.
