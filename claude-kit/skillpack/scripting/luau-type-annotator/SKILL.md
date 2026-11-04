---
name: luau-type-annotator
description: "Add strict-mode types to one untyped Luau module without changing what it does: rank the gaps with a scanner, annotate parameters, returns, tables and Instances, narrow nil and unknown properly, and prove the module still behaves. Use when a module is nonstrict or untyped; strict-mode-migrator orders a whole codebase."
category: scripting
tags: luau, types, strict, annotation, typecheck, any, unknown, narrowing, export type, luau-lsp
kb: Roblox/roblox-kb/luau-language-and-types.md, Roblox/roblox-kb/code-architecture-and-frameworks.md, Roblox/roblox-kb/scripting-and-performance.md
related: strict-mode-migrator, rbx-luau, rbx-code-rate, require-cycle-finder, lune-unit-test-writer
---

# luau-type-annotator

One module at a time. The aim is a module that passes `--!strict` with the fewest `any` casts and exactly the old behaviour. Choosing which module goes first across a codebase is `strict-mode-migrator`; the style rules for names and layout are the kit skill `rbx-luau`.

## When to use
A single ModuleScript or Script has no types, `--!nonstrict`, or many `any`. Not for: changing logic (this skill must not), whole-codebase ordering, or untyped code that is about to be deleted.

## Inputs (max 2)
1. The file (default: the one named; ask only if several match). 2. Target mode (default `--!strict`).

## Procedure
1. Baseline. Run `scripts/TypeScan.luau` on the source: `TypeScan.scan(source)` returns the mode, every function with untyped parameters or no return type, and the explicit `any` count. Record the numbers. Stop if the file already scores 0 and is strict.
2. Capture behaviour first: note exports and call sites (`script_grep` for the module name), and if there is pure logic write a quick Lune test (`lune-unit-test-writer`) so step 6 compares real results.
3. Put `--!strict` on line 1. Run `luau-lsp analyze` (or Studio Script Analysis) to get the real error list; the scanner only ranks, the analyzer decides.
4. Annotate in this order, re-analyzing after each group: exported types (`export type Config = { ... }`), function parameters and returns, `local` tables that start empty (`local items: { [string]: Item } = {}`), Instance variables (`local humanoid: Humanoid`), callbacks typed to the specific class.
5. Remove `any`, never hide it. Untrusted input (remote arguments, DataStore results, attributes) is `unknown` and narrowed with `type()` or `typeof()` before use. Where Luau does not narrow after a guard, make one new local with a cast (`local p = optional :: number`). If deep Instance traversal needs a cast, wrap it once in a helper, not at every call site.
6. Behaviour check: re-run the Lune test or the play test; compare outputs with step 2. Any diff means an annotation changed logic (usually a default value or a nil path); fix the annotation, not the test.
7. Re-scan: `TypeScan.score` should be 0 or each remaining `any` has a comment saying why.

## Studio MCP path
`list_roblox_studios` -> `script_read` the module -> run `TypeScan` through `execute_luau` (paste the module source into a long string) -> `multi_edit` the annotations -> `get_console_output` / Script Analysis for errors -> `start_stop_play` for the behaviour check.

## Fallback
Rojo file in `src/`: run the scanner under Lune, `luau-lsp analyze --definitions=<globalTypes> file.luau`. The play-test behaviour check is `untested` without Studio.

## Evidence
`Roblox/roblox-kb/luau-language-and-types.md`: `--!strict` first line or the Workspace type-check mode; annotate parameters and returns and Instance variables; avoid `any` or cast once; type untrusted input as `unknown` and narrow; optional `?` only when nil is meaningful; types have no runtime effect so runtime validation still matters (official Creator Docs 2026-10 plus indie guides, labelled in the file).

## Output
The annotated file, a before/after table (mode, untyped parameters, missing returns, `any` count), and the analyzer's final line quoted.

## Acceptance checks
- [ ] `--!strict` present and the analyzer reports no errors for the file.
- [ ] Executed: `TypeScan.score` run before and after, both numbers quoted.
- [ ] Every exported function has typed parameters and a return type.
- [ ] No new `any` without a comment; untrusted input is `unknown` and narrowed.
- [ ] Behaviour check output identical to the baseline, or marked untested.

## Pitfalls
Annotating a parameter as `any` to silence an error. Marking fields optional so a constructor compiles (initialise them instead). Typing a callback parameter as `Instance` when the event gives a specific class. Casting `:: any` on a require to dodge a cycle (fix the cycle with `require-cycle-finder`). Declaring a type on a later line (annotate at the declaration or it does not enforce).

## Related
`strict-mode-migrator`, `rbx-luau`, `rbx-code-rate`, `lune-unit-test-writer`, `require-cycle-finder`.
