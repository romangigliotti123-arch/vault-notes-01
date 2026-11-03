---
name: ugc-item-planner
description: "Plan UGC and avatar items that fit a game and the creator's situation: check Marketplace eligibility and costs first, choose item types and the in-experience sales route, and sequence the first releases. Use when considering selling avatar items or in-experience creations; building the meshes is outside this skill."
category: money
tags: ugc, avatar items, accessories, marketplace, limited, creation tokens, commission, eligibility, bundles, cosmetics
kb: Roblox/roblox-kb/ugc-and-avatar-economy.md, Roblox/roblox-kb/monetisation-other.md, Roblox/roblox-kb/business-and-payouts.md, Roblox/roblox-kb/brand-deals-and-ip-licensing.md, Roblox/roblox-kb/age-ratings-moderation-and-tos.md
related: gamepass-maker, pay-to-win-checker, regional-pricing-checker, devex-planner, asset-license-checker, premium-benefits-planner
---

# ugc-item-planner

One job: decide whether and how to sell avatar items, and plan the first few, before any mesh work. The vault separates three routes: Marketplace items you upload (eligibility, fees, an advance, moderation delay), items sold inside your own game for the owner commission, and in-experience creations through Creation Tokens. Rules and fees are Roblox Creator Docs 2026-10 facts that change: every number below is "live-check".

## When to use
Planning avatar items, deciding between Marketplace and in-game sale, or checking if the creator can sell at all. Not for: modelling or rigging (`3d-modeling-rigging-and-animation` in the KB), game passes (`gamepass-maker`), licensing checks of assets you did not make (`asset-license-checker`).

## Inputs (max 3)
1. Who owns the account and its status (ID verified? Roblox Plus or Premium? age?) (default: ask). 2. The game's theme and what players already wear or ask for (default: read community posts). 3. Budget for upload fees and the publishing advance (default: unknown, ask).

## Procedure
1. Read the rules: `python -I ~/.claude/claude-kit/tools/kbq.py section ugc-and-avatar-economy rules --max-chars 5000`. List: eligibility, fees, advance, one-per-day limits for some item types, availability choices, moderation delay.
2. Eligibility gate first. The vault reports ID verification, a Roblox Plus or Premium tier, compliance with Community Standards and Marketplace Policies, an upload fee per submission and a publishing advance. If any is missing, stop and put it in the report; do not plan sales on an ineligible account.
3. Pick the route per item: (a) Marketplace upload for items sold anywhere, (b) sell avatar items in your own game for the game-owner commission (the vault reports 40% on in-game purchases; live-check), (c) in-experience creation with an Avatar Creation Token (items are not listed on the Marketplace and cannot be resold).
4. Pick item types by effort and fit: classic clothing is the lowest-cost entry; accessories need cages and validation; emotes and animation packs have their own fees and specs; bundles need a body part. Prefer items players already ask for in this game. Timed rentals can add a cheaper tier (vault: some clothing types).
5. Availability: limited versus resellable is a one-way choice at publish; Limited items have per-day limits and anti-bot gates. Do not promise scarcity you cannot control.
6. Sequence: 1 low-cost item to learn the pipeline, then 2-3 themed items, then a bundle that shows value (set the displayed value of each included item so the saving is real).
7. Money: record fees, the advance and expected payout timing as a P&L row (`devex-planner`); the vault says to budget for the advance before uploading.
8. Risk: IP and polycount checks before upload, copies and takedowns refund and earn nothing durable (vault), and moderation delay before sale. Never copy another creator's item.

## Studio MCP path
Not needed for planning. For checks on assets already in a place: `list_roblox_studios` -> `get_studio_state` -> `execute_luau` (Edit) to read accessory attachment names and counts -> `get_console_output`. Publishing and fees are the owner's actions.

## Fallback
Plan document and hand checklist. Anything about the live Marketplace, current fees or the upload tool stays `untested`.

## Evidence
`Roblox/roblox-kb/ugc-and-avatar-economy.md` (eligibility, publish path, Limited one per day, Creation Tokens, rentals, takedowns refund, bundles need a body), `Roblox/roblox-kb/monetisation-other.md` (UGC / avatar items economics; sell avatar items in your own game for the owner commission; bundle value display; regionalised avatar pricing reported +26% in emerging markets), `Roblox/roblox-kb/business-and-payouts.md` (escrow and payout timing), `Roblox/roblox-kb/brand-deals-and-ip-licensing.md` (IP), `Roblox/roblox-kb/age-ratings-moderation-and-tos.md`. Indie trading and inventory tactics are unverified (vault says so).

## Output
`design/ugc-plan.md`: eligibility result (pass/fail per requirement), route per item, item list with effort and expected cost, release sequence, P&L rows, risks, a checklist for the owner. Under about 120 lines.

## Acceptance checks
- [ ] Every eligibility requirement has a stated status (yes, no, unknown) and a source line.
- [ ] No fee, commission or percentage appears without "live-check".
- [ ] `python -I ~/.claude/claude-kit/tools/kbq.py section ugc-and-avatar-economy rules --max-chars 1500` was run and quoted.
- [ ] No item copies another creator's work; IP check listed per item.
- [ ] Budget (fees plus advance) is in the plan before the release order.

## Pitfalls
Planning sales before checking eligibility. Treating in-experience creations as Marketplace items. Choosing Limited availability without understanding the anti-bot gate. Ignoring moderation delay in a launch date. Pricing without regional review.

## Related
`gamepass-maker`, `pay-to-win-checker`, `regional-pricing-checker`, `devex-planner`, `asset-license-checker`.
