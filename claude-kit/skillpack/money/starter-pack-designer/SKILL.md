---
name: starter-pack-designer
description: "Design the first-purchase offer (a starter pack: currency plus a permanent item plus a small convenience), pick the moment it appears and an honest purchase window, then wire it into the kit's Shop system with a tested eligibility rule. Use when a game has no entry-level purchase or its first purchase converts poorly; the full pass set is gamepass-maker."
category: money
tags: starter pack, first purchase, bundle, new player offer, entry price, impulse, conversion, singleUse, window, shop
kb: Roblox/roblox-kb/monetisation-other.md, Roblox/roblox-kb/pricing.md, Roblox/roblox-kb/first-session-onboarding.md, Roblox/roblox-kb/_tools/PRICE-LADDER.md, Roblox/roblox-kb/monetisation-devproducts.md
related: devproduct-handler, gamepass-maker, price-ladder-planner, offer-timing-planner, pay-to-win-checker, limited-offer-designer, first-minute-designer
---

# starter-pack-designer

One job: the first thing a new player can buy. The vault calls the first purchase "pivotal" and calls a template with only a currency and a starter pack minimal monetisation, so this is the first offer to get right. Delivery, idempotent receipts and duplicate protection already exist in the kit Shop system (`.rbx/claude-kit/systems/Shop`; NOT live-tested in Studio) through `devproduct-handler`; this skill decides what is in the pack, when it appears, and whether a player is still eligible.

## When to use
No entry-level purchase exists, the first purchase converts poorly, or a launch needs a "welcome" offer. Not for: the permanent pass set (`gamepass-maker`), repeatable currency packs (`devproduct-handler`), event offers (`limited-offer-designer`).

## Inputs (max 2)
1. Core loop and the first milestone a player reaches (default: `GAME.md`, `design/core-loop.md`; if none, ask what the player does in minute five). 2. Currency in the game (default: one soft currency; the vault says keep an in-game currency so spend does not feel like real money).

## Procedure
1. Read the rules: `python -I .rbx/claude-kit/tools/kbq.py section monetisation-other rules --max-chars 4000` and note the starter-bundle rules (singleUse, 15-minute example window, value display) and the "Sell cosmetics and make the first purchase satisfying" rule. Stop when you can state them in your own words.
2. Choose the anchor moment: after the first milestone, never on join (vault: do not show sales on join; new players rarely spend in the first 10-30 minutes). Record it as `StarterOffer.markMilestone`.
3. Fill the pack with three things, in this order: a currency amount that makes the next goal reachable, one permanent cosmetic or pet that shows off, one small convenience. Reject anything that gates core progress or gives pvp power (run `pay-to-win-checker` on the list).
4. Price it from `price-ladder-planner` (entry rung; the vault reports most spenders sit in the smallest spend bucket, 1-800 Robux). State the value honestly: set the displayed value of each included item so the saving is visible and true.
5. Window: optional. The bundle docs example is `durationInSeconds = 900` with `singleUse = true`; treat as an example and live-check. A window must be anchored to the milestone and never restart (`StarterOffer.lint` flags restarting windows and windows under five minutes).
6. Wire it: copy `scripts/StarterOffer.luau` beside the shop code; the pack is a developer product in `Catalogue` (`devproduct-handler`) whose `grant` also sets `data.starterBought = true` in the SAME saved data as the receipt. Before showing it, the server calls `StarterOffer.eligible(cfg, state, os.time())`; the client only asks to open the offer by name.
7. Decide where it shows with `offer-timing-planner` (a moment of need, one modal, never mid-action).
8. Test: `lune run ../skillpack/money/starter-pack-designer/scripts/tests/StarterOffer.test.luau` from `.rbx/claude-kit/systems`; then `receipt-flow-tester` against the real catalogue.
9. Write the Creator Hub checklist (create the product, name, icon, price, regional pricing review, copy the id into the catalogue). You never create, price or publish products.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `multi_edit` to add `StarterOffer.luau` and the catalogue entry (Rojo owners edit files) -> `start_stop_play` -> `execute_luau` (Server) to call `StarterOffer.eligible` for the test player before and after the milestone -> `get_console_output`. A real purchase needs a published place and a test account: `untested` until the owner buys.

## Fallback
Files plus the Lune test (headless). Without Studio the purchase and the UI stay `untested`.

## Evidence
`Roblox/roblox-kb/monetisation-other.md` (first purchase is pivotal; currency plus starter pack as the minimum; singleUse bundles with a 15-minute window; OneTime bundles at moments of need; bundle value display; tourists vs veterans), `Roblox/roblox-kb/pricing.md` (test prices live), `Roblox/roblox-kb/first-session-onboarding.md` (do not sell before the player understands the game), `Roblox/roblox-kb/_tools/PRICE-LADDER.md` (creator-reported price points). Bundle limits and durations are Roblox Creator Docs 2026-10 facts: live-check.

## Output
`design/starter-pack.md`: contents table (item, why, value), anchor moment, price and rung, window and why, rejected ideas, Creator Hub checklist, test steps; code `StarterOffer.luau` plus the catalogue entry.

## Acceptance checks
- [ ] The pack never contains core progress or pvp power (`pay-to-win-checker` run, 0 blocks).
- [ ] The offer cannot appear before the milestone (the Lune test "not eligible before the first milestone" passes).
- [ ] `lune run` StarterOffer tests pass (quote "6 passed, 0 failed") and luau-check is clean.
- [ ] Any window is shared, anchored and single-use (`StarterOffer.lint` returns no issues).
- [ ] Ids are `0` placeholders unless the owner supplied them; the price came from the ladder with a "test this" note.

## Pitfalls
Showing it on join. A timer that restarts on rejoin. Granting from the client or from `PromptProductPurchaseFinished` (only the Shop receipt handler grants). Listing a "value" that is not the real sum. Making the pack so strong that buyers never need to spend again.

## Related
`devproduct-handler`, `gamepass-maker`, `price-ladder-planner`, `offer-timing-planner`, `pay-to-win-checker`, `limited-offer-designer`.
