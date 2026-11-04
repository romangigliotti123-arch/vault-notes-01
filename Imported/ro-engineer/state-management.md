---
title: "ro-engineer reference - state-management"
source: https://github.com/excaldev/ro-engineer/blob/d86f0c04d902ddd7d1d600359940dcf7524ff604/references/state-management.md
source_repo: https://github.com/excaldev/ro-engineer
source_commit: d86f0c04d902ddd7d1d600359940dcf7524ff604
license: MIT
copyright: "Copyright (c) 2026 excaldev"
status: imported, reference only (third-party text, not verified by this vault, not loaded into sessions)
tags: [imported, reference-only, third-party]
---
> Imported, reference only. Third-party text by excaldev (MIT, see LICENSE and THIRD-PARTY-NOTICES.md in this folder), pinned commit `d86f0c04d9`. Modified: frontmatter added, unverified-tool references removed or marked unverified, vault notes added where marked "vault rule" or "vault note". Where this text and the vault's own skills differ, the skills win (rbx-luau, rbx-arch, rbx-code-rate, rbx-monetize). Links to files that were not imported (client-server-boundaries, game-loops, market-references, progression-economy, networking-remotes, performance) lead nowhere.

# State management

Use a state manager when many unrelated systems or UI read the same changing
data. If one module owns and reads its own state, a local table is enough.

## Principles

- **Single source of truth.** Each piece of state has one owner. Others read
  or subscribe; they never hold their own copy that drifts.
- **Server-owned for gameplay.** Currency, inventory, progression and match
  state live on the server. Clients receive a replica for display.
- **Changes go through actions/functions**, not direct writes from anywhere,
  so you can log, validate and replicate in one place.

## Minimal API

```lua
--!strict
export type Store<S> = {
	get: (self: Store<S>) -> S,
	set: (self: Store<S>, update: (S) -> S) -> (),
	subscribe: (self: Store<S>, fn: (new: S, old: S) -> ()) -> () -> (),
}
```

- `get` returns the current state.
- `set` takes an updater that returns a new state.
- `subscribe` returns an unsubscribe function; call it in cleanup.

## Immutable updates vs mutation

| Immutable (new table per change) | Mutation in place |
|---|---|
| Cheap change detection (`old ~= new`) | No allocation per change |
| Easy undo/history, safer subscribers | Must notify manually and carefully |
| Allocates; fine for UI-rate changes | Better for per-frame data |

Default to immutable for gameplay/UI state that changes a few times per
second or less. Use mutation plus explicit change signals for high-frequency
data, or keep that data out of the store.

Freeze state in development (`table.freeze`) to catch accidental mutation.

## Selectors

Subscribers should depend on the slice they need:

```lua
local function selectCoins(state: PlayerState): number
	return state.coins
end
```

Wrap subscriptions so they only fire when the selected value changes.

## Replication to clients

- Per-player state: server sends the initial snapshot when the client is
  ready, then diffs or action events.
- Global state (round timer, scores): broadcast changes; let late joiners
  request a snapshot.
- Use a version/sequence number so clients can detect missed updates and
  resync.
- Never accept state from the client. Clients send *requests*; the server
  validates and changes state (`client-server-boundaries.md`).
- Attributes and `ValueBase` objects are a simple built-in replication path
  for small per-instance values.

## Libraries

Current status is (unverified by this vault). Options include Charm (atom-based, has a sync
add-on), Reflex (producer/selector model), and Rodux (older Redux port).
ReplicaService-style libraries handle server-to-client replication. A small
hand-written store is often enough.

## Pitfalls

- Subscribing every frame or creating subscriptions in render loops.
- Forgetting to unsubscribe when UI or an object is destroyed.
- Storing Instances in state that gets serialized or replicated.
- One huge store where every change notifies every subscriber.
- Deriving values and storing them too (they drift). Compute in selectors.
