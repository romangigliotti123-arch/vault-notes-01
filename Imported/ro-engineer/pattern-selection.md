---
title: "ro-engineer reference - pattern-selection"
source: https://github.com/excaldev/ro-engineer/blob/d86f0c04d902ddd7d1d600359940dcf7524ff604/references/pattern-selection.md
source_repo: https://github.com/excaldev/ro-engineer
source_commit: d86f0c04d902ddd7d1d600359940dcf7524ff604
license: MIT
copyright: "Copyright (c) 2026 excaldev"
status: imported, reference only (third-party text, not verified by this vault, not loaded into sessions)
tags: [imported, reference-only, third-party]
---
> Imported, reference only. Third-party text by excaldev (MIT, see LICENSE and THIRD-PARTY-NOTICES.md in this folder), pinned commit `d86f0c04d9`. Modified: frontmatter added, unverified-tool references removed or marked unverified, vault notes added where marked "vault rule" or "vault note". Where this text and the vault's own skills differ, the skills win (roblox-luau-style, roblox-architecture-choice, roblox-code-rate, roblox-monetisation-setup). Links to files that were not imported (client-server-boundaries, game-loops, market-references, progression-economy, networking-remotes, performance) lead nowhere.

# Pattern selection

Start with current architecture, interfaces, team knowledge, and installed
libraries. Extend a working system before introducing a second one. Compare
functional needs, lifetimes, update rates, target-device budgets, maintenance,
migration, and tests for significant choices.

| Candidate | Evidence that favors it | Costs to check |
|---|---|---|
| Plain functions/module or typed data | Local logic with a clear owner | Avoid duplicating existing behavior |
| OOP | Independent stateful lifetimes tied to Models, vehicles, sessions | Metatable typing, cleanup, callback ownership |
| Composition | Repeated independent behavior combinations | Wiring and ownership; components need not be classes |
| ECS | Existing ECS project, bulk queries/scheduling needs, or representative benchmark supports migration | Structural changes, debugging, library APIs, replication, team cost |
| State store | Multiple consumers need coordinated updates/subscriptions | Notification cost, duplicate truth, snapshot/resync |
| Pooling | Profiling identifies material allocation/destruction cost | Reset correctness, retained memory, peak demand, exhaustion |

Choices can combine. Entity count is an input, not an adoption threshold.
ECS is not inherently faster than OOP; frequent spawning alone does not
justify a pool. An existing ECS project may reasonably keep ECS for a small
addition to avoid a second architecture.

For a substantial decision, give fit, key trade-offs, and why plausible
alternatives lose. Define migration boundaries and rollback for architectural
changes. A small fix simply preserves the existing pattern.