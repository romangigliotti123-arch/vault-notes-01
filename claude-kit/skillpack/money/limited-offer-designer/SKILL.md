---
name: limited-offer-designer
description: "Design limited-time offers and event shops that create honest urgency: one shared window, stated end date, permanent ownership of non-consumables, a separate event currency, no stock races or restarting timers. Includes the server-side window check. Use for seasonal items, event bundles or sales; per-player first-purchase windows are starter-pack-designer."
category: money
tags: limited time, event shop, seasonal, urgency, dark pattern, event currency, window, scarcity, ownership
kb: Roblox/roblox-kb/monetisation-other.md, Roblox/roblox-kb/events-and-seasonal-content.md, Roblox/roblox-kb/updates-live-ops.md, Roblox/roblox-kb/player-psychology-and-game-feel.md, Roblox/roblox-kb/common-mistakes.md
related: starter-pack-designer, battle-pass-designer, event-planner, offer-timing-planner, pay-to-win-checker, economy-balancer, devproduct-handler
---

# limited-offer-designer

One job: seasonal and event offers that sell without tricking anyone. The vault's rules: limited-time seasonal items create demand; stock caps frustrate players who lose the race (one creator disagrees, self-reported); keep non-consumable limited items permanently owned afterwards; launch a separate event currency so hoarders cannot buy out event content on day one and track wallets to keep the sink-back healthy; never use appointment timers. `scripts/LimitedWindow.luau` checks the window on the server and lints the design.

## When to use
A holiday item, an event shop, a one-week bundle, a sale. Not for: a new player's first-purchase offer (`starter-pack-designer`), a season track (`battle-pass-designer`), choosing when to show offers (`offer-timing-planner`).

## Inputs (max 2)
1. The event or season, its dates and the content calendar (default: ask for start and end as UTC times). 2. What sells: cosmetics, boosts, bundles (default: a cosmetic plus a bundle).

## Procedure
1. Read the rules: `python -I .rbx/claude-kit/tools/kbq.py section monetisation-other rules --max-chars 4000` and `section events-and-seasonal-content rules --max-chars 3000`.
2. Define each offer as `{ id, startsAt, endsAt, consumable, keepOwned, ... }` with ONE window for everyone, in server time. A countdown that restarts per player or per join is fake urgency and is rejected by `LimitedWindow.lint`.
3. Non-consumables (skins, pets): `keepOwned = true`; buyers keep it after the window. Consumables may expire.
4. Prefer limited time over limited stock. If you choose a stock cap anyway (the dissent), say why and test it; `lint` will warn.
5. Event currency: a separate currency earned through event play, with a daily earn cap and sinks inside the event shop, so day-one hoarders cannot buy everything (`economy-balancer` for the numbers).
6. Server check at purchase: `LimitedWindow.canBuy(offer, os.time(), alreadyOwned)`; the product grant (`devproduct-handler`) refuses outside the window or when a permanent item is already owned. The client only shows a countdown computed from the server's end time.
7. No pay-to-win: run `pay-to-win-checker` (event power items are still power).
8. After the event: remove the offer from sale, keep ownership, record sales vs the plan, and write the next event's calendar entry (`event-planner`).
9. Test: `lune run ../skillpack/money/limited-offer-designer/scripts/tests/LimitedWindow.test.luau` from `.rbx/claude-kit/systems`.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `multi_edit` to add `LimitedWindow.luau` and the purchase guard -> `start_stop_play` -> `execute_luau` (Server) to evaluate `status` and `canBuy` at a time before, inside and after the window -> `get_console_output`. A live purchase and real event timing need a published place: `untested`.

## Fallback
Files plus the Lune test (headless). Real timezone behaviour and purchases stay `untested`; always store times as Unix seconds.

## Evidence
`Roblox/roblox-kb/monetisation-other.md` ("Use limited-time items and event currency; avoid limited stock (one dissent)", "Never make paid items pay-to-win, force spending, or use appointment timers"), `Roblox/roblox-kb/events-and-seasonal-content.md` (event cadence), `Roblox/roblox-kb/updates-live-ops.md`, `Roblox/roblox-kb/player-psychology-and-game-feel.md`, `Roblox/roblox-kb/common-mistakes.md`. UGC "limiteds" on the platform Marketplace are a separate product with their own rules (vault): not covered here.

## Output
`design/limited-offers.md`: offer table (id, window UTC, items, price, keepOwned, currency), event-currency plan, lint output, post-event checklist; code `LimitedWindow.luau` and the purchase guard.

## Acceptance checks
- [ ] `LimitedWindow.lint` returns an empty list for every offer (quote it), or each issue has a reason.
- [ ] The purchase guard refuses before start, after end and for an owned permanent item (Lune tests).
- [ ] `lune run` LimitedWindow tests pass (quote "5 passed, 0 failed") and luau-check is clean.
- [ ] Times are server-side Unix seconds; the client never decides.
- [ ] `pay-to-win-checker` reports 0 blocks.

## Pitfalls
Per-player countdowns. Taking items away at the end. A stock race on mobile-heavy audiences. Event currency sold directly with no sinks. Forgetting daylight-saving confusion (use UTC).

## Related
`starter-pack-designer`, `battle-pass-designer`, `event-planner`, `offer-timing-planner`, `pay-to-win-checker`, `economy-balancer`.
