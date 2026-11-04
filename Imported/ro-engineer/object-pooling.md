---
title: "ro-engineer reference - object-pooling"
source: https://github.com/excaldev/ro-engineer/blob/d86f0c04d902ddd7d1d600359940dcf7524ff604/references/object-pooling.md
source_repo: https://github.com/excaldev/ro-engineer
source_commit: d86f0c04d902ddd7d1d600359940dcf7524ff604
license: MIT
copyright: "Copyright (c) 2026 excaldev"
status: imported, reference only (third-party text, not verified by this vault, not loaded into sessions)
tags: [imported, reference-only, third-party]
---
> Imported, reference only. Third-party text by excaldev (MIT, see LICENSE and THIRD-PARTY-NOTICES.md in this folder), pinned commit `d86f0c04d9`. Modified: frontmatter added, unverified-tool references removed or marked unverified, vault notes added where marked "vault rule" or "vault note". Where this text and the vault's own skills differ, the skills win (roblox-luau-style, roblox-architecture-choice, roblox-code-rate, roblox-monetisation-setup). Links to files that were not imported (client-server-boundaries, game-loops, market-references, progression-economy, networking-remotes, performance) lead nowhere.

# Object pooling

Consider pooling when representative profiles show repeated creation/destruction
or allocation causes material spikes. Rare, long-lived, or costly-to-reset
objects may be cheaper to create normally. Reuse a suitable project pool.

## Lifecycle contract

- Acquire transfers temporary ownership; release accepts active leases only.
  Detect double release, foreign objects, and stale callbacks.
- End the active lifetime on release: disconnect hit handlers, cancel tweens
  and delayed work, stop/clear effects, and remove external references.
- Before reuse, restore transform, velocity, collision/query/touch flags,
  transparency, attributes, sounds, emitters, and children as applicable.
  Reset can be split across release/acquire, but idle objects must be inert.
  Generation ids can prevent old callbacks mutating a new lease.
- Define pool teardown, including active leases and retained objects. Generic
  pools need a disposal callback, not only Instance cleanup.

## Capacity and placement

Measure active peak and burst demand. Distinguish idle retention cap from
active limit; define whether exhaustion grows, rejects, or degrades cosmetic
work. Prewarm within loading/memory budgets and reclaim overflow.

Parking in Workspace can retain replication/physics cost; unparenting has
reparenting costs. Compare strategies. For parked parts, account for anchoring,
`CanCollide`, `CanTouch`, and `CanQuery`.

Local VFX can use client pools; gameplay authority stays on the server even
when clients render compact state. Cover hit, timeout, respawn, owner departure,
and shutdown. Compare peak frame time and retained memory/Instance counts;
remove complexity if it yields no useful benefit.