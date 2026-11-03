---
name: ui-animation-planner
description: "Plan tweened UI motion for open, close, feedback and rewards with duration ceilings, a concurrent-loop budget and a reduced-motion variant; lints the plan and implements it with CanvasGroup fades. Use when adding or reviewing UI animation."
category: ui
tags: ui, animation, tween, motion, canvasgroup, reduced motion, performance, polish, juice
kb: Roblox/roblox-kb/ui-ux-design.md, Roblox/roblox-kb/first-session-onboarding.md
related: button-feedback-designer, tween-helper-builder, accessibility-checker, notification-system-planner, damage-number-builder, settings-menu-builder
---

# ui-animation-planner

Motion explains what changed and rewards what the player did. Too slow or too many loops makes the UI feel laggy and costs frames on low-end phones. This skill sets the plan; `scripts/UiMotion.luau` lints it and builds the reduced-motion version. Execution uses `tween-helper-builder` (TweenKit) or TweenService.

## When to use
New screens, reward moments, or a UI that feels sluggish or noisy. Not for per-button hover/press states (`button-feedback-designer`) or world effects.

## Inputs (max 2)
1. The screens/events to animate (default: open, close, button press, purchase success, reward). 2. A frame budget concern, if any (default: low-end phone).

## Procedure
1. Table every animation as a step: name, role (`feedback`, `transition`, `reward`, `ambient`), duration, properties tweened, loops. Heuristic ceilings: feedback 0.2 s, transition 0.35 s, reward 1.2 s, ambient 3 s.
2. Prefer fades on a `CanvasGroup` (`GroupTransparency`) over tweening many children; never tween text stroke per frame (vault).
3. Open: fade + small scale/position from the trigger. Close: faster than open (~60%). Tween rules: handle 0-duration, cancel the previous tween before starting a new one, reuse `TweenInfo` (vault).
4. Run `UiMotion.validate(plan)`; fix every finding. Stop condition: empty list.
5. Generate `UiMotion.reduced(plan)`: no loops, no movement/scale, short fades only. Wire it to a Reduced Motion setting from `settings-menu-builder`.
6. Implement and test on a phone-class budget: count simultaneous tweens, stop loops when a screen is hidden (toggle ScreenGuis instead of destroying them).

## Studio MCP path
`list_roblox_studios` -> `search_game_tree` -> `execute_luau` (Edit) to add `CanvasGroup` wrappers -> `multi_edit` on the controller script -> `start_stop_play` -> `get_console_output` for errors -> `screen_capture` mid-state is unreliable; timing feel is `untested` without a human.

## Fallback
Deliver the plan table plus the TweenService snippet; owner judges feel.

## Evidence
`Roblox/roblox-kb/ui-ux-design.md` (tween with 0-duration, cancellation and reuse rules; fade groups with CanvasGroup and avoid tweening text strokes per frame; give hover and press feedback with short tweens and sound; ship accessibility toggles for motion and flashing). `Roblox/roblox-kb/first-session-onboarding.md` (immediate feedback for every action; early reward/wow moment). The duration ceilings are heuristics, not Roblox limits.

## Output
```
UI MOTION PLAN <game>
step | role | dur | props | loops
validate: ok | findings   reduced variant: N steps
```

## Acceptance checks
- [ ] `UiMotion.validate` empty for the normal and reduced plans.
- [ ] Every looping tween is stoppable and at most 3 run at once.
- [ ] A reduced-motion path exists and is tied to a setting.
- [ ] Previous tweens are cancelled before replacement.
- [ ] Lune test passes (`UiMotion.test.luau`, 5 tests).

## Pitfalls
Opening animations that block input. Tweening Position of dozens of children. Looping glows left running on hidden screens. Flashing effects (see `accessibility-checker`).

## Related
`button-feedback-designer`, `tween-helper-builder`, `accessibility-checker`, `notification-system-planner`, `damage-number-builder`.
