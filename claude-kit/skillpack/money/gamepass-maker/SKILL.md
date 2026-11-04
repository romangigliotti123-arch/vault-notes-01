---
name: gamepass-maker
description: "Design a game's gamepass set (what each pass gives, price tier, when it is offered) from the vault's sourced rules, reject passes that gate core progress, then wire it into the kit's Shop system for server-verified ownership and generate the Creator Hub setup checklist. Use when planning or adding gamepasses; repeatable purchases are devproduct-handler."
category: money
tags: gamepass, monetisation, vip, 2x, permanent perk, robux, price, ownership, shop, catalogue
kb: Roblox/roblox-kb/monetisation-gamepasses.md, Roblox/roblox-kb/pricing.md, Roblox/roblox-kb/_tools/PRICE-LADDER.md, Roblox/roblox-kb/monetisation-devproducts.md, Roblox/roblox-kb/_tools/CHECKLIST-monetization.md
related: devproduct-handler, price-ladder-planner, pay-to-win-checker, starter-pack-designer, vip-pass-designer, pass-ownership-cache-builder, rbx-monetize-audit, rbx-monetize
---

# gamepass-maker

One job: decide the gamepass catalogue and make it work correctly on the server. Ownership checks, caching, retries and the "never trust the client or `wasPurchased`" rule already exist in the kit system `Shop` (`~/.claude/claude-kit/systems/Shop`; 13 Lune tests; NOT live-tested in Studio), so this skill designs the set and feeds Shop. Whole-game review is `rbx-monetize-audit`; consumables and currency packs are `devproduct-handler`.

## When to use
Adding the first passes, adding one, or fixing passes that do not apply perks. Not for: repeatable purchases, subscriptions, UGC items.

## Inputs (max 3)
1. Game pitch and core loop (default: `GAME.md`, `design/core-loop.md`). 2. Audience and genre (default: all ages, mobile-first, no pay-to-win). 3. Existing passes with ids (default: none; ids are `0` = SET IN CREATOR HUB).

## Procedure
1. Read the rules: `python -I ~/.claude/claude-kit/tools/kbq.py section monetisation-gamepasses rules --max-chars 4000` and `section pricing rules`. Note each rule's flag (official vs indie).
2. Find the pain points the loop already creates (grinding, waiting, clutter, missing out, losing progress). Vault: best sellers solve a real pain; do not sell items that remove the challenge or fix a loss.
3. Draft 2-6 passes (vault: keep the set small and valuable; about six at most, 2-5 permanent is a common range). For each: name, one-line benefit, the moment a player wants it, price tier, type (cosmetic, convenience, progression-skip). Mark as REJECTED anything that gates core progress or required skill (the top vault rule: free players must reach all core content), anything pay-to-win in competitive modes, and any pass so strong that buyers never need to spend again (low lifetime value).
4. Passes are for permanent one-time perks (VIP, bundles, restricted areas, permanent convenience such as extra storage or auto-collect, avatar items). Rebuyable things belong to developer products. Avoid single XP/coin boosters as passes (they cap spend).
5. Prices: `price-ladder-planner` and `_tools/PRICE-LADDER.md`; entry rung for impulse items, core rung for boosts and convenience, higher rungs for bundles. Every price is a starting test.
6. Timing: show a pass at the moment of need (full inventory -> storage pass), never in the first 30 seconds; bundle-style offers after the first milestone.
7. Wire it: install the Shop system if missing (`python ~/.claude/claude-kit/tools/games.py system add Shop --project <project>`), copy `scripts/PassCatalogue.luau` beside `ShopService`, create `Passes.luau` returning entries `{ name, id, benefit, onOwned? }` (`coreProgress = true` makes `build` refuse the entry). Then
   ```lua
   local passes, notes = PassCatalogue.build(require(script.Parent.Passes))
   ShopService.Start({ products = products, passes = passes, getData = ..., saveNow = ... })
   ```
   Perks that live in the world check `ShopService.HasPass(player, "VIP")` on the server at the time of use; `onOwned` runs once per join and right after buying. The client prompts by NAME through Shop's rate-limited remote; it never sends an id or price.
8. Tests: `lune run ../skillpack/money/gamepass-maker/scripts/tests/PassCatalogue.test.luau` from `~/.claude/claude-kit/systems` (pattern for your own `tests/Passes.test.luau`: build the real list, assert no duplicates, run through `Shop.new` with a fake `ownsPass`, assert a spoofed `wasPurchased` does not grant). Static: `bash ~/.claude/claude-kit/tools/roblox-project-template/luau-check.sh <files>`.
9. Write the Creator Hub checklist for the owner (create each pass, name, description, icon, price, regional pricing, copy the id into `Passes.luau`). You never create, price or publish passes.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `multi_edit` to add `PassCatalogue.luau` and `Passes.luau` (Rojo owners edit files) -> `start_stop_play` -> `execute_luau` (Server) to call `ShopService.HasPass` for the test player and `get_console_output` for the id-0 notes. Real purchase prompts need a published place: `untested` until the owner buys with a test account.

## Fallback
Files + Lune tests (headless). The purchase path is the owner's test.

## Evidence
`Roblox/roblox-kb/monetisation-gamepasses.md` (never gate core progress; cosmetics and convenience over pay-to-win, counter-views are flagged indie; small valuable set; passes for one-time perks), `Roblox/roblox-kb/pricing.md` (no formula; test live; regional pricing), `Roblox/roblox-kb/_tools/PRICE-LADDER.md` (price points are creator-reported), `Roblox/roblox-kb/monetisation-devproducts.md` (passes vs products), `Roblox/roblox-kb/_tools/CHECKLIST-monetization.md`. Shop guarantees: `systems/Shop/README.md`.

## Output
`design/gamepasses.md`: table (name, benefit, pain it solves, type, tier/price, shown when, risk flags), rejected ideas with reasons, Creator Hub checklist, test steps; code `Passes.luau` + `PassCatalogue.luau` + `tests/Passes.test.luau`.

## Acceptance checks
- [ ] No pass gates core progress or required skill (`coreProgress` never true; the design doc says why).
- [ ] Every pass has a named pain point and a moment to show it.
- [ ] Ownership is verified only through Shop (server, with Roblox asked), never from client input.
- [ ] Ids are `0` placeholders unless the owner supplied them.
- [ ] `lune run` PassCatalogue tests pass (quote "4 passed, 0 failed") and luau-check is clean.
- [ ] Prices came from the ladder with a "test this" note.

## Pitfalls
Selling XP/coin boosters as passes. Overlapping passes that confuse the shop. Prompting before the player understands the game. Checking perks once at join and never again after a mid-session purchase (use `HasPass` at use time). Setting a second `ProcessReceipt`/pass handler outside Shop.

## Related
`devproduct-handler`, `price-ladder-planner`, `pay-to-win-checker`, `vip-pass-designer`, `starter-pack-designer`, `rbx-monetize-audit`.
