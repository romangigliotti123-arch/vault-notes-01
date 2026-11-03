---
name: notification-system-planner
description: "Plan an in-game toast and alert system with priorities, a visible cap, per-key spam limits and merged repeats, backed by a tested queue; decides what deserves a toast versus a banner, a chat line or nothing. Use when notifications flood the screen or important ones get missed."
category: ui
tags: ui, notification, toast, alert, queue, priority, spam, rate limit, feedback, mobile
kb: Roblox/roblox-kb/ui-ux-design.md, Roblox/roblox-kb/first-session-onboarding.md, Roblox/roblox-kb/cross-platform-and-console.md
related: ui-animation-planner, currency-display-designer, hud-layout-planner, settings-menu-builder, accessibility-checker, damage-number-builder
---

# notification-system-planner

Every event wants attention; the screen has room for three things. This skill sets a notification policy and the queue behind it (`scripts/ToastQueue.luau`, Lune-tested; time is injected, so it works from any clock).

## When to use
Adding the first toast system, or fixing floods ("+1 coin" x50), or missed critical messages (kicked, purchase failed). Not for floating damage numbers (`damage-number-builder`) or tutorial prompts (`first-minute-designer`).

## Inputs (max 2)
1. The event list that currently notifies or should. 2. Max simultaneous toasts on a phone (default 3).

## Procedure
1. Classify each event: critical (errors, purchase result, disconnect warnings), important (level up, quest done), routine (pickups), none (do not notify; update a counter instead). Assign numeric priorities; critical is 100+.
2. Choose the channel by class: critical = modal/banner that needs an acknowledgement or lasts longer; important = toast with icon; routine = merged count on the HUD item (`+50` ticking on the currency widget) instead of its own toast.
3. Configure the queue: `maxVisible` 3, `maxQueued` about 12, `keyCooldown` 2 s per key, `defaultTtl` 3 s (heuristics; tune by playtest). Repeats of a visible key merge (`x3`) instead of stacking.
4. Placement: top-centre or a side stack, inside safe insets and away from the control zones (`hud-layout-planner`, `safe-area-checker`); never over the main action.
5. Server-to-client: the server fires a RemoteEvent with a key and numbers, never raw text from other players unfiltered; client formats and localises. Rate-limit the remote on the server.
6. Reduced motion and sound: honour the motion setting (`ui-animation-planner`); give a mute option (`settings-menu-builder`).
7. Prove the queue: run the Lune test, then simulate a burst of 100 pickups in a playtest and confirm at most `maxVisible` frames exist.

## Studio MCP path
`list_roblox_studios` -> `search_game_tree` (where notifications are created) -> `multi_edit` to add the ToastQueue module and a renderer -> `start_stop_play` -> `execute_luau` (Client) to fire a burst -> `get_console_output` -> `screen_capture`. Timing feel is `untested` without a human.

## Fallback
Deliver the policy table plus the module; run the Lune file for logic proof.

## Evidence
`Roblox/roblox-kb/ui-ux-design.md` (keep the screen clear; layer UI deliberately with ZIndex/DisplayOrder; toggle ScreenGuis instead of destroying them). `Roblox/roblox-kb/first-session-onboarding.md` (provide immediate feedback for every action; delay asks until players have seen the game). `Roblox/roblox-kb/cross-platform-and-console.md` (mobile-first). Numeric limits are heuristics.

## Output
```
NOTIFICATION POLICY <game>
event | class | priority | channel
queue: maxVisible N, cooldown S, ttl T      burst test: 100 events -> max visible N
```

## Acceptance checks
- [ ] Every event has a class, priority and channel; routine events do not each get a toast.
- [ ] Burst test attached (visible frames never exceed the cap).
- [ ] Critical messages cannot be dropped by cooldown.
- [ ] Remote is server-rate-limited; client does not display unfiltered user text.
- [ ] Lune test passes (`ToastQueue.test.luau`, 6 tests).
- [ ] Experience notifications go only to opted-in users aged 13+, at most 1 per user per day, only for meaningful events (official; Roblox/roblox-kb/_tools/DECISION-RULES.md, retention-d1-d7, social-features-and-virality).

## Pitfalls
One toast per pickup. Toasts over the jump button. Queue growing without a cap. Critical errors hidden behind routine spam.

## Related
`ui-animation-planner`, `currency-display-designer`, `hud-layout-planner`, `settings-menu-builder`, `accessibility-checker`.
