---
name: shop-ui-planner
description: "Design a shop screen that converts without dark patterns: card layout, button states (buy / needs currency / owned), ordering, confirmation, close and phone-friendly sizes, with a tested dark-pattern lint. Use when building or reviewing any in-game store UI."
category: ui
tags: ui, shop, store, monetisation, conversion, dark patterns, mobile, button states, gamepass, developer product
kb: Roblox/roblox-kb/ui-ux-design.md, Roblox/roblox-kb/monetisation-gamepasses.md, Roblox/roblox-kb/monetisation-devproducts.md, Roblox/roblox-kb/first-session-onboarding.md, Roblox/roblox-kb/cross-platform-and-console.md
related: gamepass-maker, devproduct-handler, price-ladder-planner, button-feedback-designer, currency-display-designer, inventory-ui-planner, mobile-ui-audit
---

# shop-ui-planner

The screen where a player decides to spend. It must show what they get, what it costs, what they own, and let them leave without friction. Purchase logic belongs to `gamepass-maker`, `devproduct-handler` and the kit Shop system (server authority); this skill is the client-side presentation.

## When to use
Building a shop, reworking a low-converting one, or reviewing for manipulative patterns. Not for choosing prices (`price-ladder-planner`) or wiring purchases (`devproduct-handler`).

## Inputs (max 2)
1. The offers (id, price, one-time or repeatable, featured). Use `0` / `SET IN CREATOR HUB` for unknown ids and prices, never invent them. 2. Platforms (default phone first).

## Procedure
1. Layout: tabs or sections by intent (starter, boosts, cosmetics), a grid of cards, each card = icon, name, one-line benefit, price on the card before any tap (vault: clear, consistent UI). Use a layout object for positioning and scroll frames that scale (vault: layouts own positioning).
2. Order with `ShopLayout.order` (featured first, then cheaper first, stable). Stop condition: the cheapest useful starter is visible without scrolling.
3. Button states with `ShopLayout.buttonState`: `buy`, `needsCurrency` (shows a way to get currency, not a dead button), `owned` (hide or swap the buy button for one-time items - vault), `unavailable`. Drive visuals with `button-feedback-designer`.
4. Purchase flow: tap -> clear confirm for Robux spends -> server grants -> client refreshes from the server result. The client never grants. Show success feedback and update the balance via `currency-display-designer`.
5. Close and focus: a 44 px+ close target, back button support, controller navigation (`gamepad-ui-navigator`), and no unprompted popup on join (delay asks until the player has seen the game - vault).
6. Lint the spec with `ShopLayout.audit`: price visible, close target, no fake countdown, owned hides buy, Robux confirm, closable full-screen, no unprompted popups. Stop condition: empty list.

## Studio MCP path
`list_roblox_studios` -> `search_game_tree` (shop ScreenGui) -> `inspect_instance` (card template) -> `execute_luau` to clone a card per offer from a hidden template and set Scale sizes -> `start_stop_play` -> `screen_capture` per device size. Real purchase prompts only fire in a published place: `untested` in Studio.

## Fallback
Mock the card grid and states in a table; run the audit against the spec; owner tests purchases in a published test place.

## Evidence
`Roblox/roblox-kb/ui-ux-design.md` (hide or swap buy buttons once owned; primary and secondary buttons carry different weight; clone hidden templates per row). `Roblox/roblox-kb/first-session-onboarding.md` (make the first purchase easy; delay asks; give starter items). `Roblox/roblox-kb/monetisation-gamepasses.md` and `monetisation-devproducts.md` (what each product type does). `Roblox/roblox-kb/cross-platform-and-console.md` (mobile-first, most sessions on mobile; creators' player-share claims are self-reported). The 44 px close target is a touch heuristic.

## Output
```
SHOP UI <game>
sections: ...   cards: N (ordered)   states: buy/needsCurrency/owned/unavailable handled
audit: pass | failed rules: ...
```

## Acceptance checks
- [ ] `ShopLayout.audit(spec)` returns an empty list.
- [ ] Every offer has a button state for all four cases.
- [ ] Prices and ids are real or marked `SET IN CREATOR HUB`.
- [ ] The client only requests; the server grants (kit Shop / handlers).
- [ ] Lune test passes (`ShopLayout.test.luau`, 5 tests).

## Pitfalls
A fake "ends in 00:59" timer; a tiny close button; a buy button that stays after purchase; popping the shop on join; confirming nothing before a Robux spend; forgetting that phones need a scroll frame that scales.

## Related
`gamepass-maker`, `devproduct-handler`, `price-ladder-planner`, `button-feedback-designer`, `currency-display-designer`, `inventory-ui-planner`.
