---
name: proximity-prompt-wiring
description: "Wire ProximityPrompts so the server re-validates every trigger (distance, alive, cooldown, state, ownership) before acting, handled centrally instead of one script per prompt. Use for shops, doors, pickups, levers and any interaction; exploiters can fire a prompt from anywhere."
category: scripting
tags: proximityprompt, interaction, prompt, triggered, distance, server validation, exploit, shop, door, pickup
kb: Roblox/roblox-kb/scripting-and-performance.md, Roblox/roblox-kb/anti-exploit-and-security.md, Roblox/roblox-kb/client-server-and-remotes.md
related: remote-guard-builder, cooldown-manager-builder, collection-tag-wiring, exploit-audit, roblox-remote-security
---

# proximity-prompt-wiring

A ProximityPrompt looks like UI but its `Triggered` event reaches the server like a remote. The vault is explicit: an exploiter can fire a prompt from any distance and ignore `Enabled` and `MaxActivationDistance`. So the server decides again. `scripts/PromptGuard.luau` is that second decision.

## When to use
Any interaction done through a prompt: open shop, take item, pull lever, enter door. Not for: continuous input (use the input map) or interactions that spend money (those also go through the Shop system's receipt flow).

## Inputs (max 2)
1. The prompts (what each does, who may use it, range). 2. State rules (ownership, price, one-use, cooldown).

## Procedure
1. Inventory every prompt (`script_grep` for `ProximityPrompt|Triggered`; also `ClickDetector` and `DragDetector`, which have the same weakness). Give each an action name.
2. Central wiring: connect `Triggered` once per prompt through one script, ideally tag-driven (`collection-tag-wiring`: tag `"ShopPrompt"`, one binder, behaviour looked up by tag or attribute) instead of a script inside each prompt.
3. Bind with the guard: `PromptGuard.bind(prompt, { cooldowns = cooldowns, action = "OpenShop", duration = 1, slack = 4, canUse = function(player) ... end, handler = function(player) ... end, onReject = log })`. Before the handler runs it checks: the player has a character and root part, is alive, is within `MaxActivationDistance` plus slack of the prompt's position (part, attachment or model pivot), is outside the cooldown, and passes your `canUse` (owns the key, has the currency, the door is closed).
4. The slack default is 3 studs to absorb latency and character size; raise it only with a reason. `PromptGuard.evaluate` is the pure function behind it, tested offline.
5. Inside `handler`, change state last, after every check, and never trust anything the client sent (a prompt sends nothing; keep it that way: do not add a remote that carries an item id for the same action).
6. Prices and rewards come from the server's data (Shop system), never from attributes on the prompt that a client could edit locally.
7. Log rejects with the reason; a burst of "too far" from one player is an exploit signal (see `exploit-audit`).
8. Test: `lune run ../skillpack/scripting/proximity-prompt-wiring/scripts/tests/PromptGuard.test.luau` from the kit `systems` folder; then in play, fire the prompt from the far side of the map with `execute_luau` (Client) and confirm a reject.

## Studio MCP path
`list_roblox_studios` -> `script_grep` for `ProximityPrompt|Triggered|ClickDetector` -> `multi_edit` -> `start_stop_play` -> `execute_luau` (Server) to move the test character far from the prompt and call the connected handler path (a client exploit firing the prompt remotely cannot be reproduced faithfully from the command bar) -> `get_console_output` (Server) for the reject reason.

## Fallback
Offline: the distance/alive/cooldown logic is unit-tested. `bind` needs a running place; marked `untested` until played.

## Evidence
`Roblox/roblox-kb/anti-exploit-and-security.md`: treat ProximityPrompt, ClickDetector and DragDetector as remotes; validate arguments, ownership, distance and state on the server; rate-limit per player. `Roblox/roblox-kb/scripting-and-performance.md`: handle ProximityPrompts centrally (listen once, not in every prompt); debounce.

## Output
`PromptGuard.luau` plus the binder script, a table of prompts (action, range, checks, handler), test line.

## Acceptance checks
- [ ] Executed: Lune test quoted (`6 passed, 0 failed`).
- [ ] Every prompt, ClickDetector and DragDetector is bound through the guard or removed.
- [ ] Each handler re-checks ownership/state/currency server-side before acting.
- [ ] Rejections are logged with reasons.
- [ ] A far-away trigger is rejected in play, or marked untested.

## Pitfalls
Distance measured to the wrong point (a huge model's pivot). Checking `prompt.Enabled` as security. Per-prompt scripts that drift apart. Letting the prompt carry its own price. Not clearing cooldown entries on PlayerRemoving.

## Related
`remote-guard-builder`, `cooldown-manager-builder`, `collection-tag-wiring`, `exploit-audit`.
