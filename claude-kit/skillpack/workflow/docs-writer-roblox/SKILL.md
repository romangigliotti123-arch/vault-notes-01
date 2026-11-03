---
name: docs-writer-roblox
description: "Draft API documentation for Luau ModuleScripts from their source: types, public function signatures and doc comments extracted with moddoc.py, a purpose line and a real usage example written by hand, and a list of undocumented functions. Use when a module is used by several systems or by AI workers that need its contract."
category: workflow
tags: docs, documentation, api, module, luau, signature, comments, readme, contract
kb: Roblox/roblox-kb/luau-language-and-types.md, Roblox/roblox-kb/code-architecture-and-frameworks.md, Roblox/roblox-kb/development-process-and-speed.md, Manager/topic-context-engineering.md, Manager/topic-brief-prompt-engineering.md, Mentor/Combined-Brain.md
related: code-style-guide-writer, luau-type-annotator, onboarding-new-dev, ai-brief-writer, folder-structure-planner, session-handoff
---

# docs-writer-roblox

Documentation for code that other code (or a worker with no chat history) must call correctly. The tool extracts signatures and doc comments mechanically so nothing is invented; a human or worker writes only the purpose and the example. System-level docs (GDD, kickoff) are other skills; this is per-module API reference.

## When to use
A module has callers in more than one system, a worker is about to depend on a module it did not write, or onboarding needs a map of the shared code. Not for: describing game design, or documenting private helpers.

## Inputs (max 2)
1. The module file or folder (default: `src/shared`). 2. Output folder (default: `docs/api/`).

## Procedure
1. For each module run `python docs-writer-roblox/scripts/moddoc.py src/shared/Util.luau > docs/api/Util.md`. It lists `export type` lines, public functions (`function M.f(...)`, `function M:f(...)`, `M.f = function(...)`) with signatures, and the `---` doc comment above each; undocumented functions are marked.
2. Fill **Purpose** with one sentence taken from the code (what it owns, what it never does). Do not guess at behaviour the code does not show; if unclear, write `unclear: ask the owner`.
3. For every function marked `(undocumented)`, add the `---` comment in the source (one line: what it returns, what it assumes) and regenerate; do not describe it only in the Markdown.
4. Write one **Example** per module from a real caller found with `grep -rn "require(.*Util" src` (3-5 lines). If there is no caller, say so.
5. Record side effects and trust: server-only or shared, whether it touches DataStores or remotes, and which arguments come from the client and must be validated.
6. Write `docs/api/INDEX.md` linking each module with its one-line purpose; regenerate when a module's signatures change (a signature diff in review is the cue).
7. Run the check on each page and `moddoc.py <file> --fail-undocumented` to confirm the source has no undocumented public function left.

## Studio MCP path
Optional: `script_read` to read a module that is not yet in the repo, `script_grep` to find callers. The generated Markdown goes in the repo, not the place.

## Fallback
Reading the `.luau` files directly; the extractor needs only Python and is regex based, so unusual syntax (metatable class declarations) may be missed: check the function count against `grep -c "function "`.

## Evidence
`Roblox/roblox-kb/luau-language-and-types.md` (typed signatures and `export type` make contracts explicit), `Roblox/roblox-kb/code-architecture-and-frameworks.md` (modules and single responsibilities), `Manager/topic-context-engineering.md` and `Manager/topic-brief-prompt-engineering.md` (a worker needs paths and contracts, not whole files pasted), `Roblox/roblox-kb/development-process-and-speed.md` (keep clear specs when people leave).

## Output
`docs/api/<Module>.md` per module and `docs/api/INDEX.md`.

## Acceptance checks
- [ ] Executed: `python docs-writer-roblox/scripts/moddoc.py --selftest` prints `selftest ok`.
- [ ] Executed: `python docs-writer-roblox/scripts/moddoc.py <module> --fail-undocumented` exits 0 after step 3.
- [ ] Executed: `python project-kickoff/scripts/wfdoc.py docs/api/<Module>.md --kind docs` prints PASS.
- [ ] Function count in the page equals `grep -c` of public function definitions in the source.

## Pitfalls
Docs that restate the code. Inventing behaviour for a function the author never explained. Letting the Markdown drift from the source (regenerate on change). Documenting private functions.

## Related
`code-style-guide-writer`, `luau-type-annotator`, `onboarding-new-dev`, `ai-brief-writer`, `session-handoff`.
