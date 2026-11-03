---
name: tween-helper-builder
description: "Add a small tween utility that cancels conflicting tweens, chains steps with a cancellable handle, reports completion once and cleans up after itself. Use when several scripts tween the same objects, sequences are nested Completed callbacks, or a menu glitches when opened and closed fast."
category: scripting
tags: tween, tweenservice, animation, ui, chain, cancel, easing, sequence, completed, luau
kb: Roblox/roblox-kb/ui-ux-design.md, Roblox/roblox-kb/scripting-and-performance.md, Roblox/roblox-kb/luau-language-and-types.md
related: roblox-ui-responsive, mobile-ui-audit, connection-leak-auditor, event-bus-builder, input-handler-builder
---

# tween-helper-builder

TweenService is fine; the trouble is what grows around it: two tweens fighting over one property, nested `Completed` callbacks, a half-played sequence when the player closes the menu. `scripts/TweenKit.luau` fixes those three and nothing else.

## When to use
UI or world visuals that tween and can be interrupted, or sequences of three or more steps. Not for: a one-off tween that nothing interrupts, gameplay movement (physics or server-owned motion), or skeletal animation (Animator).

## Inputs (max 2)
1. The tweens (instance, properties, time, easing). 2. Where it runs (default client; server only for state other systems read).

## Procedure
1. Create a kit once per system: `local kit = TweenKit.new(game:GetService("TweenService") :: any)`. The service is injected so the logic is testable; the single `:: any` cast is the boundary.
2. Replace direct `TweenService:Create(...):Play()` with `kit:Play(instance, TweenInfo.new(0.25), { Position = pos }, onDone)`. If a running tween already animates any of the same properties on that instance, it is cancelled first (its `onDone(false)` fires) so two tweens never write the same property.
3. Sequences: `kit:Chain({ { frame, info, goalA }, { frame, info2, goalB } }, onDone)`. `onDone(true)` after the last step; `handle:Cancel()` stops the step in flight, skips the rest and calls `onDone(false)` once.
4. Interrupt-friendly UI: open and close call `kit:Cancel(frame)` before starting the opposite tween, or just play the new one (conflicts cancel automatically). Use a 0-duration `TweenInfo` for instant changes.
5. Create tween goals from the current state at call time, never from stale captured positions.
6. Cleanup: call `kit:Destroy()` when the owner goes away (menu closed for good, character removed) so nothing keeps playing.
7. Fade a group by tweening one `CanvasGroup.GroupTransparency` rather than every child, and avoid per-frame text stroke tweens.
8. Test: `lune run ../skillpack/scripting/tween-helper-builder/scripts/tests/TweenKit.test.luau` from the kit `systems` folder (fake service: conflicts, chain, cancel, destroy).

## Studio MCP path
`list_roblox_studios` -> `script_grep` for `TweenService|:Create(` -> `multi_edit` -> `start_stop_play` -> `execute_luau` (Client) to open and close the menu rapidly -> `screen_capture` to see the final state; `get_console_output` for errors.

## Fallback
Files and the Lune test. Real easing curves and frame timing are `untested` without Studio.

## Evidence
`Roblox/roblox-kb/ui-ux-design.md`: tween with 0-duration TweenInfo for instant changes, cancel running tweens before starting a new state, reuse tweens per state, chain by calling the next Play from the previous Completed, fade groups with a CanvasGroup (official Creator Docs 2026-10). `Roblox/roblox-kb/scripting-and-performance.md`: avoid per-frame work where an event or one tween will do.

## Output
`TweenKit.luau`, the replaced call sites, test line quoted.

## Acceptance checks
- [ ] Executed: Lune test quoted (`6 passed, 0 failed`).
- [ ] No two live tweens target the same property of one instance (tested by the conflict case).
- [ ] Every sequence has a cancel path and a single completion callback.
- [ ] Rapid open/close in play ends in the correct final state, or marked untested.
- [ ] `Destroy` is called by each owner.

## Pitfalls
Cancelling a tween mid-way leaves the property at an in-between value (set the target state explicitly if that matters). Tweening a property that something else sets every frame. Tweening server-owned parts on the client and expecting the server to see it. Chain callbacks that capture instances that were destroyed.

## Related
`roblox-ui-responsive`, `mobile-ui-audit`, `connection-leak-auditor`, `input-handler-builder`.
