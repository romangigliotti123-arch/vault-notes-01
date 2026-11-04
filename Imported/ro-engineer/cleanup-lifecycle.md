---
title: "ro-engineer reference - cleanup-lifecycle"
source: https://github.com/excaldev/ro-engineer/blob/d86f0c04d902ddd7d1d600359940dcf7524ff604/references/cleanup-lifecycle.md
source_repo: https://github.com/excaldev/ro-engineer
source_commit: d86f0c04d902ddd7d1d600359940dcf7524ff604
license: MIT
copyright: "Copyright (c) 2026 excaldev"
status: imported, reference only (third-party text, not verified by this vault, not loaded into sessions)
tags: [imported, reference-only, third-party]
---
> Imported, reference only. Third-party text by excaldev (MIT, see LICENSE and THIRD-PARTY-NOTICES.md in this folder), pinned commit `d86f0c04d9`. Modified: frontmatter added, unverified-tool references removed or marked unverified, vault notes added where marked "vault rule" or "vault note". Where this text and the vault's own skills differ, the skills win (rbx-luau, rbx-arch, rbx-code-rate, rbx-monetize). Links to files that were not imported (client-server-boundaries, game-loops, market-references, progression-economy, networking-remotes, performance) lead nowhere.

# Cleanup and lifecycle

Most Roblox memory leaks are connections, threads and tables keyed by
objects that are gone.

## What must be cleaned up

| Thing | How |
|---|---|
| `RBXScriptConnection` | `:Disconnect()` |
| Custom signal connections | their disconnect method |
| Threads from `task.spawn`/`task.delay` | Cancel pending work when safe; guard callbacks already running |
| Tweens | `:Cancel()` then drop references |
| Instances you created | `:Destroy()` or return to pool |
| Objects with `Destroy` | call it |
| Per-player tables (`data[player]`) | `nil` on `PlayerRemoving` |
| Subscriptions to stores | call the unsubscribe function |
| `RunService:BindToRenderStep` | `UnbindFromRenderStep(name)` |

## Use a cleanup helper

Reuse the project's cleanup helper where present. Trove (Sleitnick), Maid
(Quenty) or Janitor (howmanysmall) collect cleanup
tasks and run them all at once. Current versions are (unverified by this vault).

```lua
local trove = Trove.new()
trove:Connect(humanoid.Died, onDied)
trove:Add(task.delay(10, expire)) -- thread: cancelled on cleanup
trove:Add(effectPart)             -- instance: destroyed on cleanup
-- later
trove:Destroy()
```

One trove per lifetime: per object, per character, per round, per UI screen.

## Lifetimes to think about

- **Player:** `PlayerAdded` to `PlayerRemoving`. Also handle players already
  in game when your script starts (`for _, p in Players:GetPlayers()`).
- **Character:** `CharacterAdded` to the next `CharacterAdded` or
  `CharacterRemoving`. Connections to the old character must go.
- **Round/match:** start to end; everything spawned for the round is in one
  trove.
- **Instance:** use `instance.Destroying` to tie an object's cleanup to the
  instance's life.
- **Server:** `game:BindToClose` for final saves (limited time window).

## Destroy semantics

- `Destroy()` sets `Parent` to nil, locks it, disconnects connections *on
  that instance and its descendants*. It does not disconnect connections you
  made to *other* instances' events from code that referenced it.
- `Debris:AddItem` is acceptable for fire-and-forget cleanup but cannot be
  cancelled; `task.delay` + `Destroy` gives you control.
- Holding a Lua reference to a destroyed instance keeps the Lua object alive.
  Drop references.

## Weak tables

For caches keyed by objects you do not own, use weak keys:

```lua
local cache = setmetatable({}, { __mode = "k" })
```

Do not rely on weak tables for Instances you control; clean up explicitly.

## Finding leaks

- Developer Console > Memory: watch `LuaHeap` and `Instances` over a long
  session with players joining and leaving.
- Play a loop (spawn and die 50 times, join and leave) and check counts
  return to baseline.
- With Studio execution, instrument owned connections/subscriptions and
  per-player tables after departure. Roblox does not expose a general API
  to enumerate all event connections.

## Checklist for every new object or system

- [ ] Connections cannot outlive their owner. Instance destruction cleans its
  own signals; external subscriptions need explicit lifetime cleanup.
- [ ] Every spawned thread cancellable or bounded.
- [ ] Every created instance destroyed or pooled.
- [ ] Per-player data cleared on leave.
- [ ] `Destroy` is idempotent.
