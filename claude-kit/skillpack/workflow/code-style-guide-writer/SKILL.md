---
name: code-style-guide-writer
description: "Write a project's one-page Luau style guide (naming, module shape, types, remotes, comments) on top of the kit's rbx-luau, and make it enforceable with stylua.toml, selene.toml and the luau-check script rather than prose. Use when a project has more than one author (human or AI) or reviews keep arguing about style."
category: workflow
tags: style, luau, naming, stylua, selene, convention, lint, module, guide
kb: Roblox/roblox-kb/luau-language-and-types.md, Roblox/roblox-kb/code-architecture-and-frameworks.md, Roblox/roblox-kb/scripting-and-performance.md, Roblox/roblox-kb/version-control-and-tooling.md, Manager/topic-brief-prompt-engineering.md, Mentor/Combined-Brain.md
related: rbx-luau, luau-type-annotator, ci-check-setter, tech-debt-lister, ai-brief-writer, folder-structure-planner, dependency-pinner
---

# code-style-guide-writer

`rbx-luau` already contains the kit's Luau style rules and `luau-type-annotator` adds types. This skill adds only the project-specific decisions that tools cannot guess and wires the rest to tools, so style is a command, not a conversation. It writes at most one page.

## When to use
A second contributor (human or AI worker) is joining, or review comments keep repeating. Not for: re-teaching Luau, or rewriting existing code to a new style in one go.

## Inputs (max 2)
1. The project folder. 2. Any existing conventions the user insists on (default: none; use the kit's).

## Procedure
1. Read `rbx-luau` and the template configs (`tools/roblox-project-template/stylua.toml`, `selene.toml`). Do not copy their rules into the guide; link them.
2. Decide only the open questions and write each as one line: module naming (PascalCase files for modules, `*.server.luau` / `*.client.luau` suffixes), where types are declared, how remotes are named and who owns the `Remotes` module, how config constants and asset ids are stored (a constants module; ids are `0` until set), error handling, comment policy (why, not what), test file naming (`*.spec.luau`).
3. Add the AI-specific rules that help workers: every public function has a type signature and a `---` doc line (`docs-writer-roblox` reads them); no `wait()`/`spawn()` (use `task.*`); no `loadstring`; server never trusts client values.
4. Map each rule to its enforcer: stylua for formatting, selene for lint, luau-lsp for types, a grep line for banned calls. A rule with no enforcer is marked `review-only`; keep those few.
5. Run the enforcers on the current code: `luau-check.sh src`. Report the count of existing violations as a baseline; do not mass-fix in this skill (`tech-debt-lister`).
6. Save `docs/STYLE.md` (headings Naming, Tools, Enforce; under 100 lines) and check it. Mention it in `CLAUDE.md`/the brief template so workers read it.

## Studio MCP path
None; style is a file-level concern. Optionally `script_grep` across the open place for banned calls to count violations.

## Fallback
Without stylua/selene/luau-lsp installed (`rokit install` is the user's decision), the enforcers are listed as `missing` and the rules fall back to `review-only`.

## Evidence
`Roblox/roblox-kb/luau-language-and-types.md` (strict types, typed signatures), `Roblox/roblox-kb/code-architecture-and-frameworks.md`, `Roblox/roblox-kb/scripting-and-performance.md` (task library over legacy wait), `Roblox/roblox-kb/version-control-and-tooling.md` (add selene, StyLua and the language server outside Studio to match editor features), `Manager/topic-brief-prompt-engineering.md` (fewer, better constraints beat long rule lists; enforce real rules with tools or hooks, not prose).

## Output
`docs/STYLE.md`, plus a baseline violation count line.

## Acceptance checks
- [ ] Executed: `python project-kickoff/scripts/wfdoc.py docs/STYLE.md --kind style` prints PASS.
- [ ] Executed: `luau-check.sh src` was run and its summary quoted (or `missing: <tool>`).
- [ ] Every rule names an enforcer or is tagged `review-only`.
- [ ] The guide is one page and links to `rbx-luau` instead of copying it.

## Pitfalls
A 300-line guide no one reads. Rules the formatter already enforces. Style rules that contradict StyLua's output. Changing every file at once, which buries real changes in diffs.

## Related
`rbx-luau`, `luau-type-annotator`, `ci-check-setter`, `tech-debt-lister`, `docs-writer-roblox`.
