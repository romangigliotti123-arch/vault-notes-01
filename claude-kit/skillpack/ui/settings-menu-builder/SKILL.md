---
name: settings-menu-builder
description: "Build a settings menu from a single schema: toggles, sliders and choices with defaults, server-side sanitising, diff-only saves into the player profile and versioned migrations, plus the standard accessibility and performance options. Use when adding or fixing player preferences."
category: ui
tags: ui, settings, options, preferences, volume, graphics, accessibility, save, schema, mobile
kb: Roblox/roblox-kb/ui-ux-design.md, Roblox/roblox-kb/cross-platform-and-console.md, Roblox/roblox-kb/anti-exploit-and-security.md
related: accessibility-checker, ui-animation-planner, datastore-schema-builder, remote-guard-builder, gamepad-ui-navigator, notification-system-planner
---

# settings-menu-builder

Settings are player-owned data entering the server from an untrusted client. A schema drives both the controls and the validation (`scripts/Settings.luau`, Lune-tested), so what the menu offers and what the server accepts cannot drift apart. Persist through the kit PlayerData system; do not write a second save path.

## When to use
First settings menu, adding an option, or fixing "my settings reset". Not for gameplay rebinding details (`input-handler-builder`) or the accessibility audit (`accessibility-checker`).

## Inputs (max 2)
1. The options wanted (default set below). 2. Which are client-only (applied locally, saved) versus server-relevant (e.g. privacy of trade requests).

## Procedure
1. Default option set: music and effects volume (sliders), screen shake and flashing effects (toggles), reduced motion (toggle), text size (choice: normal, large), colour-blind-friendly indicators (toggle), graphics quality (choice: auto, low, high), tap-vs-hold interactions where relevant. Ship the motion/flashing/display toggles (vault).
2. Write the schema: `{ key, kind, default, min, max, step, options }`. Share the module via ReplicatedStorage; the menu builds its rows from it with one row template cloned per setting.
3. Apply locally at once (volume, quality) so changes feel immediate; debounce saves. Send only `Settings.diff(old, new)` to the server through a RemoteEvent guarded per `remote-guard-builder` (rate limit, type check).
4. Server: `Settings.sanitize(SCHEMA, payload)` then store into the profile (PlayerData). Unknown keys dropped, wrong types and NaN replaced by defaults, numbers clamped.
5. Versioning: save a `settingsVersion`; on load run `Settings.migrate(saved, version, MIGRATIONS)` so new options get defaults without wiping choices.
6. Layout: scrolling list with sections, 44 px+ controls, sliders usable by thumb and by pad; "Reset to defaults" with confirm; the menu is reachable from the pause/HUD menu (`menu-flow-mapper`).
7. Apply settings consumers: reduced motion -> `ui-animation-planner` reduced plan; shake/flash -> camera and effects code read the setting.

## Studio MCP path
`list_roblox_studios` -> `search_game_tree` -> `multi_edit` (schema module, menu script, server handler) -> `start_stop_play` -> `execute_luau` (Server) with a hostile payload `{music=1e308, quality="x", cheat=1}` -> `get_console_output` to confirm sanitised values. Saving across sessions needs a published place with API access: `untested` in Studio.

## Fallback
Provide the schema module and handler; run the Lune test for validation logic.

## Evidence
`Roblox/roblox-kb/ui-ux-design.md` (ship accessibility toggles for motion, flashing and display; keep reserved and default inputs out of rebinds). `Roblox/roblox-kb/cross-platform-and-console.md` (gate by input type; touch first-class). `Roblox/roblox-kb/anti-exploit-and-security.md` (never trust client input; validate remotes server-side).

## Output
```
SETTINGS <game>  schema v N: key kind default range
save path: diff -> remote(guarded) -> sanitize -> PlayerData      migrations: n
hostile payload test: sanitised to defaults
```

## Acceptance checks
- [ ] Server sanitises every payload with the shared schema (hostile test shown).
- [ ] Only changed keys travel; remote is rate-limited.
- [ ] Old saves gain new options without losing existing ones.
- [ ] Reduced motion and flashing options exist and are consumed.
- [ ] Lune test passes (`Settings.test.luau`, 6 tests).

## Pitfalls
Saving on every slider tick. Trusting the client's numbers. Options that do nothing. A separate DataStore key per setting. Resetting everyone when the schema grows.

## Related
`accessibility-checker`, `ui-animation-planner`, `datastore-schema-builder`, `remote-guard-builder`, `gamepad-ui-navigator`.
