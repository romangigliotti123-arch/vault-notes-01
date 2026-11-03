---
name: input-validation-auditor
description: "Check that every argument a client can send to a server handler is validated (type, nil, NaN/inf, range, length, Instance class and location) and that each handler has a cooldown, producing a per-argument table of unchecked leads. Use after writing or importing remote handlers, and before remote-fuzzer proves them."
category: qa
tags: validation, remote, argument, type check, nan, range, instance, rate limit, audit, input, security
kb: Roblox/roblox-kb/anti-exploit-and-security.md, Roblox/roblox-kb/client-server-and-remotes.md, Roblox/roblox-kb/scripting-and-performance.md, Mentor/Combined-Brain.md
related: remote-guard-builder, remote-fuzzer, exploit-audit, server-authority-checker, chat-filter-tester, lune-unit-test-writer
---

# input-validation-auditor

Every client argument is attacker-controlled: any type, nil, NaN, inf, huge, or a spoofed Instance. This skill lists every handler, every argument, and whether the handler tests it, using `scripts/ArgScan.luau` (a text scan that extracts `OnServerEvent`/`OnServerInvoke` handlers; tested in Lune). It is the cheap static pass; `remote-fuzzer` is the runtime proof and `remote-guard-builder` supplies the validators.

## When to use
After adding remotes, importing a model or module with remotes, or before a launch review. Not for: deciding who owns outcomes (`server-authority-checker`), text filtering (`chat-filter-tester`), or runtime attack (`remote-fuzzer`).

## Inputs (max 2)
1. Where the handlers are (default: all scripts in ServerScriptService and any script containing `OnServerEvent`). 2. Strictness (default: report all unchecked arguments; money/item/data handlers first).

## Procedure
1. Collect script sources (Studio MCP below, or the Rojo `src` folder) and run `ArgScan.extract(source)` on each. Stop when the handler count matches `grep -c "OnServerEvent\|OnServerInvoke"` per file; a mismatch means a handler style the scan does not see (read those by hand).
2. `ArgScan.audit(handlers)` returns leads: `unchecked` (argument used with no type/NaN/range test and no guard call in the handler), `unused` (read nowhere: remove or check), `no-args` (state, cooldown and range still needed), `no-rate-limit` (no cooldown/debounce/limiter visible).
3. Read each lead. For each argument decide the validator: number -> finite and range (`RemoteGuard.number(min, max)` or `integer`); string -> length and pattern or `oneOf` a known set; Instance -> `typeof`, class and location (`IsDescendantOf` a server-known folder); table -> avoid, send flat arguments; boolean -> `typeof == "boolean"`.
4. Apply with `remote-guard-builder` (`RemoteGuard.bind(remote, spec)`: validators plus a per-player limiter before the handler body) rather than ad-hoc ifs. NaN must be rejected explicitly because it fails every comparison and passes range checks.
5. Look beyond the signature: lookups like `Items[name]` must confirm the entry exists; amounts must be floored and `> 0`; client vectors must be clamped or unit-normalised; cooldowns keyed by UserId, not a client flag.
6. Re-run the scan; leads that remain must each have a written reason (validated in a helper the scan cannot see, etc.).
7. Hand the table to `remote-fuzzer` so every dismissed lead is attacked once at runtime.

## Studio MCP path
`list_roblox_studios` -> `script_grep` with `OnServerEvent|OnServerInvoke` to get the files -> `script_read` for each -> `execute_luau` (Edit) running `ArgScan` pasted inline over `Script.Source` of the listed scripts (Source reads need Edit mode) -> `multi_edit` for fixes.

## Fallback
Rojo files: run `lune run ../skillpack/qa/input-validation-auditor/scripts/tests/ArgScan.test.luau` from `claude-kit/systems` to see usage, then feed each file's text to `ArgScan.extract`. The scan reads formatted code (a handler ends at the first `end` at the same indentation); unformatted code needs `stylua` first. Handlers passed by name or built dynamically are `untested`.

## Evidence
`Roblox/roblox-kb/anti-exploit-and-security.md`: validate every client argument (type, nil, numeric range, string length, Instance exists and is the expected class and location); reject NaN and inf with `math.isfinite`; type-, existence- and NaN-check remote arguments; route client mutations through validated, size-capped commands; clamp client vectors and key cooldowns by UserId; rate-limit and debounce per player on the server. Heuristic scan, labelled.

## Output
```
INPUT VALIDATION <date>: handlers N, args M, leads K
| script:line | remote | arg | lead | validator to add |
Dismissed leads: <reason each>
Unchecked: <dynamic remotes, helper-validated handlers>
```

## Acceptance checks
- [ ] `lune run` of the ArgScan test prints "5 passed, 0 failed".
- [ ] Handler count from the scan equals the grep count per file (or the gap is explained).
- [ ] Every `unchecked` lead is fixed or dismissed with a reason; money/item/data handlers have zero open leads.
- [ ] NaN, inf, negative and fractional values are rejected explicitly where numbers are used.
- [ ] `remote-fuzzer` was run (or named untested) on the handlers that changed.

## Pitfalls
Trusting the scan's silence: a guard hidden in a helper looks unchecked, a weak `type(x) == "number"` test looks validated (it still passes NaN and -1). Validating only types. Accepting a table argument and walking it. Per-remote limits that a second remote bypasses. Adding a validator but leaving the old unguarded handler connected.

## Related
`remote-guard-builder`, `remote-fuzzer`, `exploit-audit`, `server-authority-checker`, `chat-filter-tester`.
