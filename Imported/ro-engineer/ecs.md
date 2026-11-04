---
title: "ro-engineer reference - ecs"
source: https://github.com/excaldev/ro-engineer/blob/d86f0c04d902ddd7d1d600359940dcf7524ff604/references/ecs.md
source_repo: https://github.com/excaldev/ro-engineer
source_commit: d86f0c04d902ddd7d1d600359940dcf7524ff604
license: MIT
copyright: "Copyright (c) 2026 excaldev"
status: imported, reference only (third-party text, not verified by this vault, not loaded into sessions)
tags: [imported, reference-only, third-party]
---
> Imported, reference only. Third-party text by excaldev (MIT, see LICENSE and THIRD-PARTY-NOTICES.md in this folder), pinned commit `d86f0c04d9`. Modified: frontmatter added, unverified-tool references removed or marked unverified, vault notes added where marked "vault rule" or "vault note". Where this text and the vault's own skills differ, the skills win (roblox-luau-style, roblox-architecture-choice, roblox-code-rate, roblox-monetisation-setup). Links to files that were not imported (client-server-boundaries, game-loops, market-references, progression-economy, networking-remotes, performance) lead nowhere.

# ECS decisions and integration

Check [pattern selection](pattern-selection.md) before introducing ECS. Existing
ECS architecture, repeated bulk queries, clear scheduling needs, or measured
hot-loop gains can justify it. Counts alone cannot. Include migration,
debugging, and team familiarity.

Use installed library docs and versions. Jecs and Matter are examples, not
guaranteed recommendations; verify APIs and maintenance before adoption. Avoid
building a new ECS engine as a side effect of gameplay work.

- Define ordering (input, AI, movement, damage, cleanup, instance sync) and
  appropriate RunService phases. Keep synchronous updates bounded; give slower
  AI a deliberate rate/budget.
- Follow query-mutation guarantees of the actual library. If mutation invalidates
  iteration, defer structural changes to a defined command-buffer boundary.
- Layout follows real access patterns. Archetypes and sparse sets have different
  query/mutation costs; neither is universally fastest.
- Own Instance links, ids, connections, and despawn paths. ECS data does not
  replicate itself. Use snapshots/changes for required state, or events for
  local cosmetics; gameplay remains server-authoritative.
- Batch Instance updates when measured benefit supports it (`BulkMoveTo` for
  suitable BaseParts). Pool render objects only when justified.

Benchmark equivalent behavior/counts/update rates, physics, rendering, and
replication on target hardware. Record frame-time distribution, memory, and
integration complexity; use MicroProfiler labels around systems. Do not credit
ECS for gains caused by reducing gameplay fidelity or removing physics.