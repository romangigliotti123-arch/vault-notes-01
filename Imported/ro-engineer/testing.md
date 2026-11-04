---
title: "ro-engineer reference - testing"
source: https://github.com/excaldev/ro-engineer/blob/d86f0c04d902ddd7d1d600359940dcf7524ff604/references/testing.md
source_repo: https://github.com/excaldev/ro-engineer
source_commit: d86f0c04d902ddd7d1d600359940dcf7524ff604
license: MIT
copyright: "Copyright (c) 2026 excaldev"
status: imported, reference only (third-party text, not verified by this vault, not loaded into sessions)
tags: [imported, reference-only, third-party]
---
> Imported, reference only. Third-party text by excaldev (MIT, see LICENSE and THIRD-PARTY-NOTICES.md in this folder), pinned commit `d86f0c04d9`. Modified: frontmatter added, unverified-tool references removed or marked unverified, vault notes added where marked "vault rule" or "vault note". Where this text and the vault's own skills differ, the skills win (roblox-luau-style, roblox-architecture-choice, roblox-code-rate, roblox-monetisation-setup). Links to files that were not imported (client-server-boundaries, game-loops, market-references, progression-economy, networking-remotes, performance) lead nowhere.

# Validation and testing

Match checks to changed behavior and risk. Use existing runners/configuration;
do not add a new framework for a small fix.

| Evidence | Establishes | Does not establish |
|---|---|---|
| Generated code / static review | Proposed logic and inspected constraints | Execution success |
| Type checking | Compatibility with configured definitions/checker | Runtime payload safety or engine behavior |
| Unit tests | Tested logic/edge cases | Real replication, physics, persistence |
| Studio integration / multiplayer playtest | Observed engine/client/server behavior | All production/device scenarios |
| Profiling | Measured cost in a recorded workload | Universal speedup |
| Security checks | Tested attack paths and boundary review | Absence of all exploits |

For substantial changes cover relevant cases: purchase with exact/insufficient
funds, invalid/negative/NaN/infinite values, concurrent spend, duplicate receipt
retries, save failure/session conflict, migration, respawn, join/leave,
late-join snapshots, and streaming. Use test data or mocks for persistence;
do not exercise destructive cases on production saves.

Reuse installed tooling. Primary references (checked 2026-11-01):
- [Jest Lua](https://github.com/jsdotlua/jest-lua): use the project's runner
  and JestGlobals setup; do not assume bare describe/it/expect globals exist.
- [TestEZ](https://github.com/Roblox/testez): a Roblox test runner; follow its
  spec/runner setup instead of mixing Jest and TestEZ conventions.
- [Lune](https://github.com/lune-org/lune): standalone Luau for compatible
  logic tests, not a complete Roblox engine or multiplayer simulator.
- [luau-lsp](https://github.com/JohnnyMorganz/luau-lsp): configure Roblox
  definitions and the project's sourcemap/module resolution for useful checks.
  A bare analyzer without engine definitions is not equivalent to Studio.
- [StyLua](https://github.com/JohnnyMorganz/StyLua) formats and
  [Selene](https://github.com/Kampfkarren/selene) lints; neither proves runtime
  correctness. [Rojo](https://rojo.space/docs/) syncs project files.

Use the Studio capabilities actually exposed in the session; verify execution context and read
results. If no runtime is available, report static checks separately and give
placement plus concrete manual tests. Performance claims need comparable
before/after workloads; leaks need repeated lifecycle cycles and trend data.