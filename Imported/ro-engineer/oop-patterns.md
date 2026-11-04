---
title: "ro-engineer reference - oop-patterns"
source: https://github.com/excaldev/ro-engineer/blob/d86f0c04d902ddd7d1d600359940dcf7524ff604/references/oop-patterns.md
source_repo: https://github.com/excaldev/ro-engineer
source_commit: d86f0c04d902ddd7d1d600359940dcf7524ff604
license: MIT
copyright: "Copyright (c) 2026 excaldev"
status: imported, reference only (third-party text, not verified by this vault, not loaded into sessions)
tags: [imported, reference-only, third-party]
---
> Imported, reference only. Third-party text by excaldev (MIT, see LICENSE and THIRD-PARTY-NOTICES.md in this folder), pinned commit `d86f0c04d9`. Modified: frontmatter added, unverified-tool references removed or marked unverified, vault notes added where marked "vault rule" or "vault note". Where this text and the vault's own skills differ, the skills win (roblox-luau-style, roblox-architecture-choice, roblox-code-rate, roblox-monetisation-setup). Links to files that were not imported (client-server-boundaries, game-loops, market-references, progression-economy, networking-remotes, performance) lead nowhere.

# OOP in Roblox projects

Use objects when independent identity, state, and lifetime fit the project.
A utility or server-lifetime service does not need a class. Preserve existing
constructors, naming, and caller contracts.

- Metatable objects commonly use `Class.__index = Class`. Type instance data
  and methods using the configured checker; explicit self annotations can help
  inference but are not a universal style requirement.
- Field prefixes are conventions, not access control. Define who mutates state.
- Document yielding construction; avoid yielding require cycles or exposing
  partly initialized objects to callbacks.
- Resource-owning objects need a teardown contract compatible with existing
  cleanup helpers. Make repeated cleanup safe, end subscriptions/delayed work,
  and guard late callbacks. Do not destroy caller-owned Models without an
  explicit ownership transfer.
- Prefer components when behavior combinations cause duplicated overrides or
  irrelevant base fields. Do not replace working inheritance solely for depth.

See [composition](composition.md) for tag/streaming and hybrid boundaries,
and [cleanup](cleanup-lifecycle.md) for resource semantics. Reuse the project's
signal implementation; a replacement needs an API, lifecycle, or measured benefit.