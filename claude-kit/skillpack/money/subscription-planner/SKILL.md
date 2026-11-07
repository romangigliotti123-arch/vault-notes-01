---
name: subscription-planner
description: "Decide whether an experience should offer subscriptions, design distinct tiers that follow the platform's rules, estimate net income and lifetime value against a one-time pass, and list the Creator Hub steps. Use when considering auto-renewing monthly tiers or Roblox Plus perks; one-time perks are gamepass-maker."
category: money
tags: subscription, monthly tier, recurring, roblox plus, ltv, local currency, robux, benefits, renewal
kb: Roblox/roblox-kb/monetisation-other.md, Roblox/roblox-kb/business-and-payouts.md, Roblox/roblox-kb/pricing.md, Roblox/roblox-kb/_tools/CHECKLIST-monetization.md, Roblox/roblox-kb/roblox-platform-changes.md
related: gamepass-maker, vip-pass-designer, battle-pass-designer, premium-benefits-planner, devex-planner, regional-pricing-checker
---

# subscription-planner

One job: decide if subscriptions fit this game and plan tiers that obey the rules. Subscriptions are fast-moving platform features: the vault's facts are Roblox Creator Docs 2026-10 and creator talks, so every rule below is something to live-check on the day you build. The kit has no subscription system; delivery logic here is a plan, not shipped code.

## When to use
A game with a strong retained audience and recurring value to give (daily rewards, ongoing content). Not for: permanent one-time perks (`gamepass-maker`), seasonal progression (`battle-pass-designer`), Premium-based engagement rewards (`premium-benefits-planner`).

## Inputs (max 3)
1. What recurring value the game can deliver every month (default: ask; none means do not subscribe). 2. Retention data (default: unknown; the LTV model uses 4 months as an assumption to replace). 3. An existing pass that tiers would replace (default: none).

## Procedure
1. Read the rules: `python -I .rbx/claude-kit/tools/kbq.py section monetisation-other rules --max-chars 5000`. Find the subscription rule and write down: tier limit, platform share, term rules, cross-platform rule, what you may not do.
2. Decide go or no-go: subscribe only when the game gives something every month that you will keep shipping (the vault warns benefits must be honoured for the full term and delivered on time). If you cannot, stop and report "use passes".
3. Draft 1-3 tiers as JSON with name, price, benefits (cosmetic, convenience, a monthly currency drip, never core progress or pvp power), and `platformExclusive` and `extraTasks` set to false.
4. Validate: `python -I .rbx/claude-kit/skillpack/money/subscription-planner/scripts/subplan.py tiers.json --share 0.7 --months 4 --pass-price <price of the equivalent pass>`. It fails on duplicate or identical tiers, tiers over the limit, platform-exclusive or task-gated benefits, and prints net per month, lifetime value and months until a subscription beats a one-time pass. Replace the 4-month assumption with your own retention.
5. If replacing a pass, keep honouring existing owners (vault note); do not strip a pass's perks.
6. Currencies: the vault reports Robux and local-currency subscriptions as separate subscriptions with different payout timing (see `devex-planner` for cash flow). Plan both or say why only one.
7. Verification in code: subscription status is checked on the server through the platform API, never from the client (live-check the current API names; the vault names `GetSubscriptionProductInfoAsync` for display prices and a `HasRobloxSubscription` style check for Roblox Plus perks). Do not ship an API call before the feature is live for users (vault).
8. Write the Creator Hub checklist (create each subscription, description, price, regional review, benefits delivery plan, support plan). You never create or publish it.

## Studio MCP path
Mostly planning. If a perk check is added: `list_roblox_studios` -> `get_studio_state` -> `multi_edit` for the server check -> `start_stop_play` -> `get_console_output`. Real subscription state needs a published place and a test account: `untested`.

## Fallback
Hand steps and the checker script (headless). Everything platform-side stays `untested`.

## Evidence
`Roblox/roblox-kb/monetisation-other.md` (experience subscriptions and Roblox Plus: up to 50 tiers per game, 70% creator share on Robux subscriptions, rules on benefits, two-currency note, claimed 2x lifetime value for retained subscribers; one game gets 5-7% of revenue, self-reported), `Roblox/roblox-kb/business-and-payouts.md` (payout timing: local-currency subscriptions pay 70% in month one and 100% after, Robux ones 70% every month), `Roblox/roblox-kb/roblox-platform-changes.md` (live-check changes). Older "no auto-renew" claims are outdated per the vault.

## Output
`design/subscriptions.md`: go/no-go reason, tier table, `subplan.py` output, comparison with a pass, delivery and support plan, Creator Hub checklist, risks.

## Acceptance checks
- [ ] `subplan.py tiers.json` exits 0 (quote "0 error(s)").
- [ ] `python -I .../subplan.py --selftest` prints "5 checks ok".
- [ ] Every benefit can be delivered every month for the whole term (the plan names who and how).
- [ ] No benefit is platform-exclusive, task-gated, core progress or pvp power.
- [ ] Every platform rule used has a "live-checked on <date>" line, or is marked unverified.

## Pitfalls
Promising benefits you cannot keep shipping. Identical tiers. Treating the 70% share and tier limit as permanent. Deleting an active subscription (take it off sale and cancel renewals instead, per the vault payout note). Mixing currencies in one tier.

## Related
`gamepass-maker`, `vip-pass-designer`, `battle-pass-designer`, `premium-benefits-planner`, `devex-planner`.
