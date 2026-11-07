---
name: dependency-pinner
description: "Pin Rojo, StyLua, Selene, luau-lsp, Lune and Wally package versions exactly in rokit.toml and wally.toml, detect drift against the kit template with pincheck.py, and write an upgrade routine that tests before accepting. Use when a project has unpinned tools, mismatched versions between machines, or before upgrading anything."
category: workflow
tags: pin, version, rokit, wally, rojo, stylua, selene, lune, dependency, upgrade, toolchain
kb: Roblox/roblox-kb/version-control-and-tooling.md, Roblox/roblox-kb/tools-and-resources.md, Roblox/roblox-kb/development-process-and-speed.md, Manager/topic-claude-code-features.md, Mentor/Combined-Brain.md
related: rbx-rojo, ci-check-setter, git-workflow-setter, project-kickoff, folder-structure-planner, code-style-guide-writer
---

# dependency-pinner

Same toolchain on every machine and for every worker, upgraded on purpose. The kit template ships a pinned `rokit.toml`; `rbx-rojo` installs the managers. This skill keeps pins exact, notices drift, and defines the upgrade routine. Installing software is the user's decision: this skill reads and edits pin files, it does not download tools.

## When to use
A new project copies the template, two machines give different lint results, or a tool update is being considered. Not for: choosing which libraries to adopt, or auditing a model's licence (`asset-license-checker`).

## Inputs (max 2)
1. The project folder (default: current; files `rokit.toml` or `aftman.toml`, `wally.toml`). 2. The template to compare against (default: `tools/roblox-project-template/rokit.toml`).

## Procedure
1. Run `python dependency-pinner/scripts/pincheck.py rokit.toml [wally.toml] --against .rbx/claude-kit/tools/roblox-project-template/rokit.toml`. FAIL lines are unpinned entries (`@latest`, ranges, no version); WARN lines are drift from the template.
2. Fix FAIL by writing the exact `x.y.z` the project is actually using: take it from the tool itself (`rojo --version`, `stylua --version`, `selene --version`, `lune --version`), not from memory. A missing tool stays `missing`.
3. Decide drift case by case: align the project to the template, or keep the difference and write a `docs/decisions.md` entry (`decision-log-writer`) saying why.
4. Upgrade routine, one tool at a time on a branch: read the tool's release notes (live check: versions and notes change), change the pin, run `luau-check.sh src`, `rojo build -o build.rbxl`, and the Lune suites; accept only if the output is unchanged or the changes are understood. Commit the pin change alone.
5. Never pipe an install script into a shell; use `rokit install` from the pinned file or the official release binary, after the user agrees.
6. Write `docs/TOOLCHAIN.md` (headings Tool, Version, Upgrade; under 70 lines) listing each pin, its purpose and the last verified date; check it.

## Studio MCP path
None. Studio and Rojo plugin versions are separate: note the plugin version shown in Studio's plugin manager as a manual item.

## Fallback
Edit the TOML by hand; the script needs only Python. Wally resolution (`wally install`) needs the tool and network: `untested` without it.

## Evidence
`Roblox/roblox-kb/version-control-and-tooling.md` (pin tool versions with Rokit and upgrade cautiously; example pins Rojo 7.6.1, Wally 0.3.2, Lune 0.10.4 are dated examples, the template pins newer ones; prefer official 2026 tooling over 2021 indie tooling), `Roblox/roblox-kb/tools-and-resources.md`, `Roblox/roblox-kb/development-process-and-speed.md` (Roblox tooling advice is version-dependent; verify against current docs), `Manager/topic-claude-code-features.md`.

## Output
Corrected `rokit.toml`/`wally.toml`, `docs/TOOLCHAIN.md`, the pincheck output.

## Acceptance checks
- [ ] Executed: `python dependency-pinner/scripts/pincheck.py --selftest` prints `selftest ok`; `pincheck.py rokit.toml` prints PASS.
- [ ] Executed: `python project-kickoff/scripts/wfdoc.py docs/TOOLCHAIN.md --kind pins` prints PASS.
- [ ] Each pin was read from the tool's own `--version` output or marked `missing`.
- [ ] An upgrade, if made, was verified by `luau-check.sh` and `rojo build` before commit.

## Pitfalls
Pinning to what the docs say rather than what is installed. Upgrading three tools in one commit. Treating a newer version as automatically better. `@latest` in a team repo.

## Related
`rbx-rojo`, `ci-check-setter`, `git-workflow-setter`, `project-kickoff`, `code-style-guide-writer`.
