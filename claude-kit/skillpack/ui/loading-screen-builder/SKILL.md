---
name: loading-screen-builder
description: "Build a custom Roblox loading screen with honest weighted progress, a never-backwards bar that cannot hit 100% early, a stall message, rotating tips and a clean hand-off to gameplay. Use to cut perceived join time or when players think the game froze."
category: ui
tags: ui, loading screen, progress, preload, contentprovider, join time, tips, first impression, mobile
kb: Roblox/roblox-kb/first-session-onboarding.md, Roblox/roblox-kb/ui-ux-design.md, Roblox/roblox-kb/cross-platform-and-console.md
related: first-minute-designer, game-optimizer, replicated-loader-builder, tooltip-system-builder, mobile-ui-audit, hud-layout-planner
---

# loading-screen-builder

The first thing a player sees is waiting. A loading screen should shorten the wait where it can and make the rest honest. Progress maths is `scripts/LoadingProgress.luau` (Lune-tested).

## When to use
Adding a loading screen, long join times, or "stuck at loading" complaints. Not for reducing the load itself (`game-optimizer`, `replicated-loader-builder`).

## Inputs (max 2)
1. What must be ready before play (default: critical assets, player data, character spawned). 2. Tips available (default: 5-10 short gameplay tips).

## Procedure
1. Measure first: join time is a retention lever (vault: cut load and join time, minimise lobby time). Record the current time to playable; the screen is a patch, not the cure.
2. Remove the default loading UI deliberately (`ReplicatedFirst` script with `RemoveDefaultLoadingScreen()`), show your gui at once, and keep it light (no heavy images).
3. Define tasks with weights from measured durations: critical asset preload (`ContentProvider:PreloadAsync` on a bounded list, not the whole game), data received, character spawned. `LoadingProgress.new(tasks)`; `set(name, fraction, now)` as each advances, `done(name, now)` on completion.
4. Drive the bar from `update(dt)` each frame: it never goes backwards, is capped under 100% until `isComplete()`, and follows the raw value at a speed limit (no jumpy bars).
5. Stall handling: `stalled(now, 10)` flips the text to a helpful line ("Still loading, a slow connection can take a while") and a retry/skip only if safe. Log the stalled task name to analytics.
6. Tips: `nextTip(count, last, math.random())`, change every few seconds; tips teach the core loop in one sentence (vault: teach core first, show don't tell).
7. Hand-off: fade the gui with a `CanvasGroup`, enable controls only after fade start, then destroy the loading gui and stop its updates. Never block playable moments behind a fixed minimum timer.
8. Safe areas and sizes per `mobile-ui-audit`: the bar and text sit inside safe insets; logo scaled with constraints.

## Studio MCP path
`list_roblox_studios` -> `search_game_tree` (ReplicatedFirst) -> `multi_edit` to add the script and module -> `start_stop_play` -> `get_console_output` (task timings) -> `screen_capture`. Real join times differ on devices and networks: `untested` until measured on a phone.

## Fallback
Provide script and module with the Lune proof; the owner measures join time on a phone.

## Evidence
`Roblox/roblox-kb/first-session-onboarding.md` (cut load and join time; minimise lobby time; get players into fun within seconds; match the first minute to the promise). `Roblox/roblox-kb/ui-ux-design.md` (toggle ScreenGuis; fade groups with CanvasGroup). `Roblox/roblox-kb/cross-platform-and-console.md` (mobile-first; test on a low-end Android phone before launch - indie advice, single source). Stall timeout and speed limit are heuristics.

## Output
```
LOADING SCREEN <game>   tasks: name(weight) ...   stall: 10 s message
tips: N   measured join time before -> after
```

## Acceptance checks
- [ ] The bar is monotonic and < 100% until every task is done (tested).
- [ ] A stall produces a visible message and an analytics event.
- [ ] No fixed minimum display time; hand-off fades and destroys the gui.
- [ ] Join time measured before and after on a phone, or `untested` stated.
- [ ] Lune test passes (`LoadingProgress.test.luau`, 6 tests).

## Pitfalls
Fake progress that finishes before loading does. Preloading everything (slower join). Heavy loading art. Leaving the loading gui updating after hand-off.

## Related
`first-minute-designer`, `game-optimizer`, `replicated-loader-builder`, `tooltip-system-builder`, `mobile-ui-audit`.
