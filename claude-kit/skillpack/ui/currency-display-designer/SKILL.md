---
name: currency-display-designer
description: "Design currency counters: abbreviated formatting that never rounds up a unit, a bounded count-up on gains, instant drops on spending, a plus button to the shop, and server-truth snapping. Use when adding or fixing any coin, gem or Robux-adjacent balance display."
category: ui
tags: ui, currency, coins, counter, count up, abbreviation, formatting, shop button, balance, hud
kb: Roblox/roblox-kb/ui-ux-design.md, Roblox/roblox-kb/first-session-onboarding.md, Roblox/roblox-kb/monetisation-other.md
related: shop-ui-planner, hud-layout-planner, notification-system-planner, ui-animation-planner, button-feedback-designer
---

# currency-display-designer

The balance is the most-read number in the game. It must be legible at a glance on a phone, feel alive when it grows, and never disagree with the server. Logic is in `scripts/CurrencyCounter.luau` (Lune-tested).

## When to use
First currency HUD, a balance that jumps or shows `1000K`, or a missing path from "not enough" to the shop. Not for the store itself (`shop-ui-planner`) or price tuning (`price-ladder-planner`).

## Inputs (max 2)
1. The currencies (default: soft currency plus one premium). 2. Their scale range (default up to billions, so abbreviations are required).

## Procedure
1. One widget per currency: icon, number, and a plus button on currencies the shop sells. Place per `hud-layout-planner`; the widget uses Scale size, `AutomaticSize` on the number's width, and a text constraint so large numbers shrink instead of clipping.
2. Format with `CurrencyCounter.format`: under 1000 exact, then K/M/B/T with two decimals, always floored (999999 shows 999.99K, never 1000K).
3. Animate with `CurrencyCounter.new(initial, { duration = 0.6 })`: `set(target)` on a gain, `update(dt)` each frame while unsettled, stop updating when `isSettled()` (no per-frame work at rest). Decreases are instant by default so spending feels immediate; set `instantOnDecrease = false` only for a deliberate drain effect.
4. Feedback: on a gain, a small scale pulse (feedback role, <= 0.2 s) and optional `+N` float via `notification-system-planner` or `damage-number-builder`; merge rapid gains into one number.
5. The plus button opens the relevant shop tab (`shop-ui-planner`); when currency is short, purchase buttons show "need N" and link to the same place. Do not auto-open the shop.
6. Truth: the server owns the balance (kit PlayerData). The client display subscribes to server updates; if the received value differs from the animated target after settling, call `snap(value)`.

## Studio MCP path
`list_roblox_studios` -> `search_game_tree` (HUD) -> `multi_edit` to add the CurrencyCounter module and a binder script -> `start_stop_play` -> `execute_luau` (Server) to change a test player's balance -> `screen_capture` -> `get_console_output`.

## Fallback
Provide the module and widget spec; the owner verifies the feel on a phone. Mark visuals `untested`.

## Evidence
`Roblox/roblox-kb/ui-ux-design.md` (drive bars/values with clamped ratios; AutomaticSize and constraints for variable text; keep text legible). `Roblox/roblox-kb/first-session-onboarding.md` (give starter currency; make the first purchase easy; immediate feedback). `Roblox/roblox-kb/monetisation-other.md` (premium currency is sold through developer products; ids from Creator Hub).

## Output
```
CURRENCY WIDGET <currency>  format: floor, K/M/B/T   count-up: 0.6 s   decrease: instant
plus button -> <shop tab>   server sync: snap on mismatch
```

## Acceptance checks
- [ ] `format` never produces a unit overflow (`1000K`).
- [ ] Count-up never overshoots; updates stop at rest.
- [ ] A spend shows immediately; a server mismatch snaps.
- [ ] The plus button reaches the shop in one tap.
- [ ] Lune test passes (`CurrencyCounter.test.luau`, 5 tests).

## Pitfalls
Animating from the previous visual value after a snap. Counting up for seconds on huge jumps. Client-side balances treated as truth. Number clipping in German/Russian-style long formats (use constraints).

## Related
`shop-ui-planner`, `hud-layout-planner`, `notification-system-planner`, `ui-animation-planner`, `button-feedback-designer`.
