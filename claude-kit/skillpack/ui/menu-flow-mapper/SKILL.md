---
name: menu-flow-mapper
description: "Map every screen, how it is opened and how it is left, then audit for unreachable screens, traps, broken links and paths deeper than a phone player will tolerate. Use when the UI has grown ad hoc or players get stuck in menus."
category: ui
tags: ui, menu, flow, navigation, screens, back button, stack, dead end, information architecture
kb: Roblox/roblox-kb/ui-ux-design.md, Roblox/roblox-kb/first-session-onboarding.md, Roblox/roblox-kb/cross-platform-and-console.md
related: hud-layout-planner, gamepad-ui-navigator, shop-ui-planner, mobile-ui-audit, settings-menu-builder, first-minute-designer
---

# menu-flow-mapper

Draw the UI as a graph before changing it. Nodes are screens, edges are "opens", and every non-root screen needs a way back. `scripts/MenuGraph.luau` audits the graph (Lune-tested).

## When to use
After several screens were added without a plan, a "stuck" bug report, or before adding controller support. Not for per-screen layout (`hud-layout-planner`) or visual polish.

## Inputs (max 2)
1. Screens source (default: every ScreenGui and the scripts that show them). 2. The entry points (default: HUD buttons and prompts).

## Procedure
1. Inventory screens: find ScreenGuis and the code that toggles them (search for `Enabled =` and `Visible =` on top-level frames). One row per screen: id, opened by, back target, closable.
2. Model as `{ id, entry, opens, back, closable }` and run `MenuGraph.audit(screens, maxDepth)`. Fix: `unreachable` (orphan screens), `trapped` (no way out), `brokenLinks`, `deep` (core screens more than about 3 taps away).
3. Apply menu rules: a menu is one stateful object with a stack; two dismissals (close button and tap-outside/back); only one modal at a time; toggling `Enabled` rather than destroying (vault). Define what Back does on each device (B on pad, Android back where available, close button always visible).
4. Reduce depth: merge rarely used screens, add shortcuts from the HUD for the two or three frequent ones, and use progressive disclosure (gate UI behind progression).
5. Document the final map as a table plus a list of entry bindings and keyboard/pad shortcuts; share with `gamepad-ui-navigator` for focus work.
6. Re-run the audit on the final map; stop at all-empty.

## Studio MCP path
`list_roblox_studios` -> `search_game_tree` (StarterGui) -> `script_grep` for `Enabled`/`Visible` toggles -> `inspect_instance` for each screen -> compose the graph -> `MenuGraph.audit`. A Client playtest (`start_stop_play`, `user_mouse_input`) walks the paths for the claims you make.

## Fallback
Work from a code read: the map is a static view; runtime-created screens are listed as `untested`.

## Evidence
`Roblox/roblox-kb/ui-ux-design.md` (structure menus as single stateful objects with two dismissals and a stack; toggle ScreenGuis instead of destroying them; keep the screen clear and design around user flows; layer with ZIndex and DisplayOrder). `Roblox/roblox-kb/first-session-onboarding.md` (clear goals and next steps; gate UI behind progression; reduce UI friction on mobile). `Roblox/roblox-kb/cross-platform-and-console.md` (map controls per input type). The 3-tap depth is a heuristic.

## Output
```
MENU MAP <game>   screens N   entries: ...
id | opened by | back | depth
audit: unreachable [] trapped [] broken [] deep []
```

## Acceptance checks
- [ ] Every screen row has an opener and a back/close path.
- [ ] `MenuGraph.audit` returns four empty lists (or each finding is justified).
- [ ] Runtime-created screens were found by code search, or listed as unchecked.
- [ ] Lune test passes (`MenuGraph.test.luau`, 5 tests).

## Pitfalls
Stacked modals with different close rules. A screen opened by a prompt but absent from the map. Closing by `Destroy()` (state lost). Treating the HUD as having a back target.

## Related
`hud-layout-planner`, `gamepad-ui-navigator`, `shop-ui-planner`, `mobile-ui-audit`, `settings-menu-builder`.
