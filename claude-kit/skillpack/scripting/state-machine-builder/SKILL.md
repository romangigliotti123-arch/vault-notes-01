---
name: state-machine-builder
description: "Build a reusable state machine for NPC behaviour, round phases or abilities: explicit states, an allowed-transition table, enter/exit/update hooks, queued transitions and a history, validated at startup and unit-tested. Use when behaviour has more than two modes or a bool-flag tangle."
category: scripting
tags: state machine, fsm, npc, ai, round, ability, transition, enter, exit, update, luau
kb: Roblox/roblox-kb/physics-pathfinding-and-npc-ai.md, Roblox/roblox-kb/code-architecture-and-frameworks.md, Roblox/roblox-kb/combat-and-gameplay-systems.md
related: rbx-npc, rbx-rounds, event-bus-builder, cooldown-manager-builder, lune-unit-test-writer
---

# state-machine-builder

Replaces `isChasing`, `isAttacking`, `isStunned` flag soup with one named current state and a table of legal moves. The kit skills `rbx-npc` and `rbx-rounds` supply the behaviours; this supplies the structure they plug into.

## When to use
An NPC, a match loop, a boss, a tool or an ability has three or more modes and bugs come from impossible combinations. Not for: two-state toggles, or animation blending (use Animation Graphs / the animator).

## Inputs (max 2)
1. The states and what each does. 2. Who is allowed to trigger which transition (default: any state may only move to the listed ones).

## Procedure
1. Draw the table first: rows are states, columns are legal next states (`Idle -> Chase`, `Chase -> Idle | Attack`, `Attack -> Chase`). Every row needs an exit; a state with none is a trap (flag it unless it is terminal, like `Dead`).
2. Copy `scripts/StateMachine.luau`. Build the machine with the table: `StateMachine.new({ initial = "Idle", states = {...} }, ctx)`. The constructor runs `validate` and throws on an undefined initial state or target, so typos fail at startup.
3. Hooks: `enter(ctx, from, ...)` sets up (start a pathfind, play a sound), `exit(ctx, to)` cleans up (cancel the path, disconnect), `update(ctx, dt)` is the per-step logic. Keep decisions (when to change state) in `update`; keep effects in `enter`/`exit`.
4. Request moves with `machine:Transition("Chase", target)`. It returns false for an illegal move (nothing changes). A transition requested from inside a hook is queued and runs after the hook, so enter/exit never re-enter.
5. Drive `update` from one place: a Heartbeat connection for many NPCs (one loop, not a loop each) or the round loop for phases. Authoritative machines (NPCs, rounds, damage states) run on the server; the client may run a copy for presentation driven by replicated attributes.
6. Observe with `onChange(from, to)` (feed analytics or an event bus signal) and `History()` when debugging.
7. Test: `lune run ../skillpack/scripting/state-machine-builder/scripts/tests/StateMachine.test.luau` from the kit `systems` folder; add one test per illegal transition you care about.

## Studio MCP path
`list_roblox_studios` -> `script_grep` for the flag names being replaced -> `multi_edit` -> `start_stop_play` -> `execute_luau` (Server) to read `machine:Current()` while the NPC acts and `get_console_output` for the transition log.

## Fallback
Files and Lune tests; real NPC behaviour (pathfinding, animation timing) is `untested` without a running place.

## Evidence
`Roblox/roblox-kb/code-architecture-and-frameworks.md`: modules with explicit init/start phases, signals for hooks, one-way dependencies. `Roblox/roblox-kb/physics-pathfinding-and-npc-ai.md` and `Roblox/roblox-kb/combat-and-gameplay-systems.md`: NPC and combat behaviours are server-run loops; budget per-frame work. `Roblox/roblox-kb/building-art-and-assets.md` notes engine Animation Graphs with state machines in beta (2026-10) for animation only; this module is for game logic.

## Output
`StateMachine.luau`, the transition table (as a diagram or table in the PR), the per-state hook list, test result line.

## Acceptance checks
- [ ] Executed: Lune test quoted (`7 passed, 0 failed`).
- [ ] Every state is reachable and (unless terminal) has an exit.
- [ ] `validate` returns no problems for the real definition.
- [ ] Hooks never call `Transition` expecting it to run immediately.
- [ ] One update loop drives all instances.

## Pitfalls
Putting game rules in `enter` (it only runs on change). Letting clients request server-state transitions directly (they request an action; the server decides). Per-NPC `while true` loops. Skipping `exit` cleanup so connections leak (use `Janitor` from `connection-leak-auditor`). A transition table of "everything to everything" (that is no machine at all).

## Related
`rbx-npc`, `rbx-rounds`, `event-bus-builder`, `connection-leak-auditor`.
