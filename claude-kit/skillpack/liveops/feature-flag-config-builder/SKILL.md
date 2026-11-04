---
name: feature-flag-config-builder
description: "Build live config and feature flags for a Roblox game: typed values with safe defaults and bounds, a kill switch, deterministic percent rollout, fallback on a bad push, and the glue to Creator Hub Configs or a DataStore document. Ships a tested FlagConfig module. Use to tune values or hide unfinished content without republishing."
category: liveops
tags: config, feature flag, kill switch, rollout, live tuning, creator hub configs, remote config, hotfix, defaults
kb: Roblox/roblox-kb/ab-testing-and-experiments.md, Roblox/roblox-kb/updates-live-ops.md, Roblox/roblox-kb/data-persistence.md, Roblox/roblox-kb/client-server-and-remotes.md
related: experiment-designer, live-balance-tuner, rollback-planner, event-planner, hotfix-playbook, datastore-schema-builder, remote-guard-builder, rbx-datastore
---

# feature-flag-config-builder

Vault: put enemy health, damage, prices and event toggles in configs so you can change them live, and deploy time-sensitive content early behind a config, then flip the value. The risk is a bad value that breaks the game. `FlagConfig` makes every value typed, bounded and defaulted, so a corrupt push falls back instead of sticking.

## When to use
Any value you may want to change without a publish, any unfinished or timed content (events, seasons), or any risky feature that needs a kill switch. Not for: player data (`datastore-schema-builder`), per-player secrets, or balancing logic itself (`live-balance-tuner`).

## Inputs (max 3)
1. The values and flags you want live-tunable, with their normal and safe values. 2. Config source: Creator Hub Configs (default), a DataStore document, or MessagingService push. 3. Which flags are percent rollouts.

## Procedure
1. List each key with kind (number, boolean, string, rollout), default, min/max or allowed set. The default must be the safe, shipped behaviour; defaults are validated at construction and a bad default asserts.
2. Copy `scripts/FlagConfig.luau` beside the server code and declare the definitions in one server-only ModuleScript. Do not replicate it; the client asks the server for the few values it needs through a validated remote (`remote-guard-builder`).
3. Fetch the raw table in the server glue (Configs API; live-check the current Roblox Configs documentation for the call and signal names, which this skill does not hard-code) inside `pcall`, then `flags:Apply(raw)`. Log every returned problem string to the console and a custom analytics event.
4. Poll or subscribe; the docs give about 5 minutes for a config change to deploy and publishing a draft is irreversible except by restoring a previous version, so GET the draft and check it before publishing. Use a gradual rollout (15 minutes) for gameplay values.
5. Gate unfinished content: `if flags:IsOn("newShop", player.UserId)`. Rollout is stable per player and only grows: raising 20 to 50 percent never switches anyone off.
6. Kill switch: `flags:Kill("eventActive")` forces the default until revived, even if the source is unreachable; wire it to a kit `Admin` command so on-call can use it from in game.
7. Test: `lune run ../skillpack/liveops/feature-flag-config-builder/scripts/tests/FlagConfig.test.luau` from `~/.claude/claude-kit/systems` (8 tests) and `bash ~/.claude/claude-kit/tools/roblox-project-template/luau-check.sh <FlagConfig.luau>`. Then a Play test: push a bad value, confirm the default is used and the problem is logged.
8. Record each flag in `decisions.md` with owner and removal date; delete flags once a feature is permanent.

## Studio MCP path
`list_roblox_studios` -> `script_read` the economy/config modules -> `multi_edit` to move hard-coded numbers behind `flags:Get` -> `start_stop_play` -> `execute_luau` (Server) calling `flags:Apply({bossHealth = -5})` and asserting `Get` equals the default -> `get_console_output`.

## Fallback
Rojo: add the module and the definitions file; run the Lune suite and luau-check without Studio. What stays `untested`: the real Configs fetch, deploy delay and Play-mode behaviour.

## Evidence
`Roblox/roblox-kb/ab-testing-and-experiments.md` (Roblox Creator Docs 2026-10): use configs for tunable values and feature flags; config deploys in about 5 minutes; publish with gradual rollout (15 minutes); verify the draft before publishing; conditional configs evaluate rules top to bottom, first match wins. `updates-live-ops.md`: use live configs instead of republishing; deploy early behind a config, then flip the value; publishing a place propagates in about 15 seconds to 1 minute.

## Output
`FlagConfig.luau` plus `Flags.luau` (definitions), the glue snippet, `liveops/flags.md` (key, kind, default, bounds, owner, remove-by date).

## Acceptance checks
- [ ] The Lune suite prints "8 passed, 0 failed".
- [ ] luau-check exit 0 on the module.
- [ ] A bad pushed value falls back to the default and is logged (Play test or marked untested).
- [ ] Every flag has an owner and a removal date; no flag reaches the client unvalidated.
- [ ] Draft config is read back and checked before publish; gameplay values use gradual rollout.

## Pitfalls
Last-good-value fallback that keeps a corrupt value alive (this module returns the default). Flags that never get removed. Secrets in configs. Trusting client-sent flag values. Treating the config source as instant: it takes minutes.

## Related
`experiment-designer`, `live-balance-tuner`, `rollback-planner`, `event-planner`, `hotfix-playbook`.
