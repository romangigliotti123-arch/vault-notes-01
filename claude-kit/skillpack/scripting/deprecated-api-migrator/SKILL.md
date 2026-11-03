---
name: deprecated-api-migrator
description: "Scan scripts for deprecated or legacy Roblox API use, say what replaces each (with the vault's evidence labelled apart from general knowledge), check every replacement against the live docs, and migrate in small tested steps. Use before a release, after a platform update, or when old free models or tutorials crept in."
category: scripting
tags: deprecated, migration, wait, spawn, raycast, physicsservice, collision groups, bodyvelocity, linearvelocity, processreceipt, api
kb: Roblox/roblox-kb/roblox-platform-changes.md, Roblox/roblox-kb/luau-language-and-types.md, Roblox/roblox-kb/scripting-and-performance.md, Roblox/roblox-kb/building-art-and-assets.md, Roblox/roblox-kb/anti-exploit-and-security.md
related: strict-mode-migrator, raycast-recipes, collision-group-setup, exploit-audit, model-cleaner, roblox-code-rate
---

# deprecated-api-migrator

The platform changes faster than any list. This skill finds likely deprecated use with `scripts/DeprecatedScan.luau`, separates what the vault actually records from what is only general knowledge, and forces a live docs check before any edit.

## When to use
Pre-launch, after a release-notes read, when code came from old tutorials or free models, or when Studio shows deprecation warnings. Not for: style (use `roblox-luau-style`) or security review (use `exploit-audit`).

## Inputs (max 2)
1. Source root or place (default: all scripts). 2. Scope (default: everything; or only `confidence = vault` rules for a conservative pass).

## Procedure
1. Collect `{ name = source }` (Studio `script_read`, or `src/**/*.luau`).
2. `DeprecatedScan.scan(source)` per file returns hits with line, rule, replacement, `confidence` and a note. `confidence = "vault"` means the knowledge base states it, with source and date; `"general"` means widely known but not in the vault. Current rules cover: `wait`/`spawn`/`delay`/`ypcall`, the `FindPartOnRay` family, `FilterDescendantsInstances` (older but working), the purchase-finished events, the PhysicsService collision-group methods (official, 2026-09-03), `getfenv`/`setfenv`, the legacy Body movers, `SetPrimaryPartCFrame`, `Humanoid:LoadAnimation`, `unpack`, lowercase `connect`/`remove`.
3. `DeprecatedScan.summarize(hits)` gives counts per rule, vault-backed first.
4. Before touching code, verify each rule you will act on against the current API reference and release notes (live-check). Record the URL and date next to the rule. If the docs disagree with the table, the docs win and the table gets an edit (it is a Lua table at the top of the script).
5. Migrate one rule at a time, in this order: mechanical and safe (`wait` to `task.wait`, `unpack` to `table.unpack`, lowercase methods), then API swaps with small behaviour differences (raycasts, movers, `PivotTo`), then ones needing design (collision groups, purchase flow).
6. After each rule: analyzer (`luau-lsp analyze`), the Lune tests for pure modules, and a play test of the area. Commit per rule so a regression bisects cleanly.
7. Special cases: legacy movers do not map one to one (a `BodyVelocity` becomes a `LinearVelocity` with an `Attachment`, different force limits); purchase events must not grant items (use the receipt flow of the kit Shop system); collision groups move to a WorldRoot-based API (write the adapter from the current docs, see `collision-group-setup`).
8. Re-run the scan; vault-backed hits should be zero or each remaining one justified.

## Studio MCP path
`list_roblox_studios` -> `script_grep` with the rule names as a first pass -> `script_read` -> `execute_luau` to run the scanner on sources -> `multi_edit` per rule -> `start_stop_play` -> `get_console_output` (deprecation warnings appear there).

## Fallback
Rojo repo with Lune; docs check by hand. Anything not play-tested is `untested`.

## Evidence
`Roblox/roblox-kb/luau-language-and-types.md` (task library replaces wait/spawn/delay; `ypcall` deprecated; `getfenv`/`setfenv` disable optimisations), `Roblox/roblox-kb/scripting-and-performance.md` (Raycast replaces FindPartOnRay; ExcludeInstances/IncludeInstances), `Roblox/roblox-kb/building-art-and-assets.md` (PhysicsService collision methods deprecated, official 2026-09-03), `Roblox/roblox-kb/anti-exploit-and-security.md` (purchase-finished events; use ProcessReceipt). `Roblox/roblox-kb/roblox-platform-changes.md` for dated notices; its newest entries should be re-read each run. The `general` rules are not in the vault.

## Output
`deprecations.md`: hits table (file, line, rule, confidence), docs URLs checked, order of migration, per-rule commit list, final scan result.

## Acceptance checks
- [ ] Executed: scanner run on the real sources; counts quoted. Lune test passes (`8 passed, 0 failed`).
- [ ] Every migrated rule has a docs URL and date.
- [ ] `general` rules were verified in the docs before editing.
- [ ] Analyzer clean after each rule; behaviour tested in play or marked untested.
- [ ] No grant-on-purchase-event path remains.

## Pitfalls
Search and replace without reading (`wait(` inside a string, `spawn` as a user function). Replacing `wait()` with `task.wait()` in code that relied on the old throttled timing. Treating the table as complete. Migrating deprecated-but-working code in a hot release week.

## Related
`strict-mode-migrator`, `raycast-recipes`, `collision-group-setup`, `exploit-audit`, `model-cleaner`.
