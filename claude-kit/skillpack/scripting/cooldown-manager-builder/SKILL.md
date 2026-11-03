---
name: cooldown-manager-builder
description: "Install one server-side cooldown and debounce helper keyed by UserId and action, used by every remote, prompt and Touched handler, with early reset, per-player cleanup and a sweep for expired entries. Use when an action can be spammed or a Touched handler fires repeatedly."
category: scripting
tags: cooldown, debounce, rate limit, touched, spam, remote, ability, server, userid, throttle
kb: Roblox/roblox-kb/scripting-and-performance.md, Roblox/roblox-kb/anti-exploit-and-security.md, Roblox/roblox-kb/client-server-and-remotes.md
related: remote-guard-builder, proximity-prompt-wiring, exploit-audit, state-machine-builder, roblox-remote-security
---

# cooldown-manager-builder

A cooldown is a game rule (an ability may be used every 0.6 s); a rate limit is a safety net (no remote may be called 50 times a second). This skill is the rule. The safety net is `remote-guard-builder`, which has its own limiter; use both, they answer different questions.

## When to use
A power, tool, purchase, interaction or Touched handler must not run again within a time window. Not for: client-only visual debounce (a local bool is fine), or limiting call volume of remotes (use `remote-guard-builder`).

## Inputs (max 2)
1. The actions and their durations (default: the numbers in the design doc; ask if none). 2. Which can be reset early (respawn, potion).

## Procedure
1. List every server entry point that causes an effect: remote handlers, prompt `Triggered`, `Touched`, tool `Activated`. Each gets an action name and a duration.
2. Copy `scripts/Cooldowns.luau` to the server. Create one object per system: `local cooldowns = Cooldowns.new()` (clock defaults to `os.clock`; tests pass a fake).
3. Guard each entry point at its top, before any state change: `if not cooldowns:Try(player.UserId, "Swing", 0.6) then return end`. `Try` starts the cooldown only when it succeeds; a rejected call does not extend it.
4. Always key by `player.UserId`, never by name or by the Player object (names can change, objects pin memory and break across rejoin).
5. On `Players.PlayerRemoving` call `cooldowns:Clear(player.UserId)`. Run `cooldowns:Sweep()` on a slow timer (every 60 s) to drop expired entries.
6. Expose time left to the client for UI as a replicated attribute or a reply to a validated remote (`Remaining`): the client displays it, the server enforces it.
7. For `Touched`, the same helper replaces ad-hoc boolean flags: `cooldowns:Gate(userId, "Lava", 1, function() damage(player) end)`.
8. Test: `lune run ../skillpack/scripting/cooldown-manager-builder/scripts/tests/Cooldowns.test.luau` from the kit `systems` folder.

## Studio MCP path
`list_roblox_studios` -> `script_grep` for `debounce|cooldown|Touched:Connect|OnServerEvent` -> `multi_edit` to add the guards -> `start_stop_play` -> `execute_luau` (Client) firing the action twice quickly -> `get_console_output` (Server) shows one effect.

## Fallback
Files plus Lune; the double-fire check against a real remote is `untested` without a running place.

## Evidence
`Roblox/roblox-kb/scripting-and-performance.md`: debounce every Touched handler (it fires repeatedly from settling and from each body part) with a flag or attribute cooldown; clear per-player tables on leave. `Roblox/roblox-kb/anti-exploit-and-security.md`: rate-limit per player on the server, validate on the server, re-verify context. `Roblox/roblox-kb/client-server-and-remotes.md`: the client may predict, the server decides.

## Output
`Cooldowns.luau` in the project and a table: action, duration, entry point, early-reset rule. Test line quoted.

## Acceptance checks
- [ ] Executed: Lune test quoted (`7 passed, 0 failed`).
- [ ] Every effectful entry point calls `Try` or `Gate` before changing state.
- [ ] Keys are UserIds; `Clear` runs on PlayerRemoving.
- [ ] A rejected call does not extend the cooldown (tested).
- [ ] Durations come from the design numbers, not guesses.

## Pitfalls
Checking the cooldown after granting the reward. One shared cooldown for different actions. Using `tick()` or wall clock where `os.clock` suits (a clock that jumps breaks cooldowns). Letting the client report "my cooldown is over". Forgetting that a respawn or teleport may reset the player's state but not the table.

## Related
`remote-guard-builder`, `proximity-prompt-wiring`, `exploit-audit`, `roblox-remote-security`.
