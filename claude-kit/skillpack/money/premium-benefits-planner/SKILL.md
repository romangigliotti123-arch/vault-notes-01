---
name: premium-benefits-planner
description: "Plan how a game uses Roblox Premium and the Creator Rewards income without pressure: Premium-only perks that are cosmetic or convenient, the right use of the Premium purchase prompt, and what the payout programmes pay for. Use when adding Premium perks or when asked what Premium earns; paid perks sold for Robux are gamepass-maker."
category: money
tags: premium, premium payouts, creator rewards, engagement, perks, membership, daily reward, non-spenders, income
kb: Roblox/roblox-kb/monetisation-other.md, Roblox/roblox-kb/business-and-payouts.md, Roblox/roblox-kb/roblox-platform-changes.md, Roblox/roblox-kb/_tools/CHECKLIST-monetization.md, Roblox/roblox-kb/retention-d1-d7.md
related: gamepass-maker, vip-pass-designer, subscription-planner, devex-planner, pay-to-win-checker, kit-system-integrator
---

# premium-benefits-planner

One job: give Premium members something worth having and keep the game honest about what Premium earns. This is a planning skill with no new code: the perk check is one server line and the money rules change often. The vault's position: Premium time pays regardless of game size, is additive to passes and products, and means non-spenders still earn you money; the old engagement-based payout was replaced by Creator Rewards (July 2025), whose rates are launch values that may change.

## When to use
You want Premium-only perks, a Premium prompt, or an answer to "what does Premium pay us". Not for: perks sold for Robux (`gamepass-maker`, `vip-pass-designer`), recurring paid tiers (`subscription-planner`), cashing out (`devex-planner`).

## Inputs (max 2)
1. The existing perks and reward loops (default: read `design/` and the shop catalogue). 2. Whether the audience is mostly young or has many adults (default: assume mixed; affects pressure and regional notes).

## Procedure
1. Read the rules: `python -I ~/.claude/claude-kit/tools/kbq.py section monetisation-other rules --max-chars 5000` and `section business-and-payouts rules`. Write down the Premium payout, Creator Rewards and Premium-prompt rules with their dates.
2. Pick perks: exclusive cosmetics, a chat or lobby flair, a small daily bonus or a saved-slot convenience. The vault's rule: Premium perks should be exclusive merch, not tactical advantages. Run `pay-to-win-checker` on them.
3. Make the check server-side: the server reads the player's membership (live-check the current API; historically `Player.MembershipType == Enum.MembershipType.Premium`) when granting the perk, never a client flag. Cache with the join and refresh on membership change events.
4. Prompt rules: use the platform's Premium purchase prompt at a natural moment (profile, shop tab), do not use the modal as a paywall and do not promise Robux (vault). Pair it with `offer-timing-planner` limits.
5. Income model: Premium engagement and Creator Rewards are income lines, not a plan. The vault lists a Daily Engagement Reward and an Audience Expansion programme with launch values; treat the numbers as live-check and never plan the budget on them. Report them as a separate line in `devex-planner` records.
6. Do not rank free players below Premium in core gameplay; the perk list must not make the free path worse than it is today.
7. Write the checklist for the owner: perk list, where the prompt shows, what to read in the Creator Dashboard (Premium engagement and rewards pages) each month, what to re-check.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `multi_edit` for the server perk check -> `start_stop_play` -> `execute_luau` (Server) to log a test player's membership result -> `get_console_output`. Studio test players are not Premium members: the Premium branch stays `untested` until a real Premium account joins a published place.

## Fallback
Plan document and hand checklist. The perk code is one function; test it with a fake player table in a Lune test the owner writes (`lune-unit-test-writer`).

## Evidence
`Roblox/roblox-kb/monetisation-other.md` ("Use Premium payouts and Creator Rewards": Premium pays regardless of game size; additive; engagement-based payouts deprecated July 24, 2025; launch values for Daily Engagement Reward and Audience Expansion; self-reported examples; older doubts from 2020 creators), `Roblox/roblox-kb/business-and-payouts.md` (Creator Rewards as a real income line; payout timing), `Roblox/roblox-kb/roblox-platform-changes.md` (live-check changes). Rates in the vault are launch values dated 2025: say so.

## Output
`design/premium.md`: perks table (perk, why, risk flags), prompt placement, server check location, income lines with "live-check" dates, monthly review checklist.

## Acceptance checks
- [ ] Every perk is cosmetic or convenience and passes `pay-to-win-checker` (quote "0 block").
- [ ] The membership check runs on the server (name the file and function).
- [ ] No rate or percentage appears without a date and "live-check".
- [ ] `python -I ~/.claude/claude-kit/tools/kbq.py section monetisation-other rules --max-chars 1500` was run and its Premium rule quoted in the plan.
- [ ] The Premium branch is marked `untested` unless a real Premium account tested it.

## Pitfalls
Using the Premium prompt as a gate. Promising Robux for subscribing. Building the budget on payout rates. Treating Premium perks as a power advantage. Trusting a client-sent "isPremium".

## Related
`gamepass-maker`, `vip-pass-designer`, `subscription-planner`, `devex-planner`, `pay-to-win-checker`.
