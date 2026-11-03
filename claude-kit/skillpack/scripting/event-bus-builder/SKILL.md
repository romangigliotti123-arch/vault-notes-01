---
name: event-bus-builder
description: "Add a typed Signal and, when needed, a named event bus so systems talk without requiring each other: ordered handlers, safe disconnect during fire, Once, Wait, Destroy that drops everything. Use to break a require cycle or to let a new feature react to an old one without editing it."
category: scripting
tags: signal, event, bus, decoupling, observer, publish subscribe, bindable, disconnect, leak, luau
kb: Roblox/roblox-kb/code-architecture-and-frameworks.md, Roblox/roblox-kb/luau-language-and-types.md, Roblox/roblox-kb/scripting-and-performance.md
related: require-cycle-finder, connection-leak-auditor, state-machine-builder, module-architecture-planner, kit-system-integrator
---

# event-bus-builder

Gives modules a way to announce things (`PlayerDied`, `RoundEnded`, `LevelChanged`) without knowing who listens. Use it for in-process coordination only. Anything crossing the server/client line is a remote, validated by `remote-guard-builder`, never a signal.

## When to use
Two modules need each other only for notifications, a new feature must hook an existing one, or a require cycle exists. Not for: a single listener (a plain callback is simpler), request/response (call the function), or client-to-server messages.

## Inputs (max 2)
1. The events (name, arguments). 2. Where they live (default: one `Events` module per system, not one global bus).

## Procedure
1. List the events as a table of name to argument types. Prefer one `Signal` per event, exposed as a field (`Health.Died`), over a string-keyed global bus: the types are checked and a typo is an error, not a silent no-op. Use a named bus only when listeners are loaded dynamically.
2. Copy `scripts/Signal.luau` into the project (shared if both sides use it). Create typed signals: `local died = Signal.new() :: Signal.Signal<Player, string>`.
3. Fire after the state change is complete (`died:Fire(player, cause)`), never in the middle of an update. Handlers run in connection order; a handler that yields runs in its own thread (`task.spawn`), so it cannot block the others or the firing code.
4. Own your connections: every `Connect` result goes into a cleanup object (`connection-leak-auditor` ships `Janitor`). A system that is destroyed calls `Destroy()` on its signals; the signal then drops every handler so nothing keeps a module alive.
5. Use `Once` for one-shot reactions and `Wait` to resume a thread on the next fire; do not poll a flag in a loop.
6. For a bus of named events build a small table `{ [string]: Signal }` created on first use; keep the names in constants so a typo fails loudly.
7. Test it: `lune run ../skillpack/scripting/event-bus-builder/scripts/tests/Signal.test.luau` from the kit `systems` folder (order, disconnect during fire, Once, Wait, Destroy, error isolation).

## Studio MCP path
`list_roblox_studios` -> `script_grep` for `BindableEvent|Event:Connect` to find ad-hoc buses -> `multi_edit` to add the module and replace them -> `start_stop_play` -> `get_console_output` to confirm handlers fire once. Deferred versus immediate engine signal behaviour changes ordering; set `Workspace.SignalBehavior` deliberately and test with it (live-check the current default).

## Fallback
Files plus the Lune tests. Behaviour inside a running place (handler ordering against engine signals) is `untested` without Studio.

## Evidence
`Roblox/roblox-kb/code-architecture-and-frameworks.md`: signals break cycles and expose hook events, emit custom change signals from your classes (fire after updating state, disconnect every connection before the owner's lifetime ends), one-way dependency direction. `Roblox/roblox-kb/luau-language-and-types.md`: fire a Destroying-style signal before clearing a custom object; yielding inside a handler pauses only that thread; `Once` replaces connect-then-disconnect. `Roblox/roblox-kb/scripting-and-performance.md`: official 2026 docs recommend setting `SignalBehavior` explicitly (live-check).

## Output
`Signal.luau` in the project, the event list with types, the places that fire and listen, and the test result line.

## Acceptance checks
- [ ] Executed: the Lune test quoted (`7 passed, 0 failed`).
- [ ] Every `Connect` has an owner that disconnects it.
- [ ] No event crosses client/server; those are remotes.
- [ ] Events are fired after state is consistent, with typed arguments.
- [ ] No handler relies on firing order beyond connection order.

## Pitfalls
A global bus that becomes a hidden dependency graph. Firing inside a loop over the same listener list (the snapshot makes it safe, but double-firing is still a logic bug). Passing mutable tables that handlers change. Using a BindableEvent for this: it copies arguments and costs more than a Luau signal. Forgetting `Destroy`, the classic leak.

## Related
`require-cycle-finder`, `connection-leak-auditor`, `state-machine-builder`, `module-architecture-planner`.
