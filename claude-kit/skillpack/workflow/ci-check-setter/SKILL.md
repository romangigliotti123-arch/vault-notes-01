---
name: ci-check-setter
description: "Set up the automatic Luau checks for a project: a git pre-commit hook that runs the kit's luau-check.sh (stylua, selene, luau-lsp) on staged files, blocks real failures, and prints UNCHECKED when tools are missing instead of passing. Use after the toolchain is pinned and before several authors or workers commit code."
category: workflow
tags: ci, check, hook, pre-commit, lint, stylua, selene, luau-lsp, quality gate
kb: Roblox/roblox-kb/version-control-and-tooling.md, Roblox/roblox-kb/testing-debugging-and-qa.md, Manager/topic-claude-code-features.md, Manager/topic-multi-agent-failure-modes.md, Manager/topic-managing-ai-agents-for-roblox-game-dev.md, Mentor/Combined-Brain.md
related: dependency-pinner, git-workflow-setter, code-style-guide-writer, roblox-rojo-project-setup, worker-verifier, regression-checklist-builder
---

# ci-check-setter

Computational checks first: the Manager KB's strongest rule for AI-written Luau is that verification must be a run of a tool, not "I re-read it". The kit already has `luau-check.sh`; this skill makes it run automatically at commit time. It is a local hook, not a hosted CI service (a GitHub Actions workflow needs the tools installed on a runner and the user's account, which is theirs to set up).

## When to use
Code is committed by more than one author or by workers, or "it passed on my machine" has happened. Not for: Lune unit-test suites (run those from the brief's DONE WHEN list), or runtime checks that need Studio.

## Inputs (max 2)
1. The project folder (must already be a git repo; see `git-workflow-setter`). 2. Path to `luau-check.sh` (default: the kit's `tools/roblox-project-template/luau-check.sh`, or the copy inside the project).

## Procedure
1. Confirm the checker works: run `bash <path>/luau-check.sh src/shared` on a known-good folder and read the last lines; note which tools it reports SKIPPED.
2. Generate the hook: `python ci-check-setter/scripts/hookgen.py gen <project> --check-script <path>`. It writes `.githooks/pre-commit` that checks only staged `.luau` files.
3. Verify the hook text: `python ci-check-setter/scripts/hookgen.py check <project>/.githooks/pre-commit` must print PASS (blocks on failure, prints UNCHECKED when no tool ran, no `--no-verify` advice).
4. Enable it for this clone: `git config core.hooksPath .githooks` (a repo-local setting; tell the user, it is not global).
5. Prove it works with one bad and one good file on a throwaway branch: stage a file with a style error and expect `BLOCKED` and exit 1; stage a clean file and expect exit 0. If tools are missing, the expected output is `UNCHECKED`, and that is reported as untested, never as a pass.
6. Add a line to `docs/GIT.md` and `CLAUDE.md`: workers must not use `--no-verify`; a blocked commit is fixed or reported.
7. Write `docs/CI.md` (headings Hook, Checks, Skipped; under 80 lines) with the exact commands and which tools were present when tested; check it.

## Studio MCP path
None. Studio playtests are a separate gate (`playtest-evidence-logger`).

## Fallback
Run `bash luau-check.sh src` by hand before each commit; the hook only automates it. On Windows use Git Bash for the hook.

## Evidence
`Roblox/roblox-kb/version-control-and-tooling.md` (match Studio's editor features outside it with selene, StyLua and the language server), `Roblox/roblox-kb/testing-debugging-and-qa.md`, `Manager/topic-managing-ai-agents-for-roblox-game-dev.md` (computational sensors first: selene, stylua, luau-lsp; a missing tool is reported as manual review, never as a pass), `Manager/topic-multi-agent-failure-modes.md` (structural controls beat prompt rules), `Manager/topic-claude-code-features.md` (hooks as enforcement).

## Output
`.githooks/pre-commit`, `docs/CI.md`, and the bad-file/good-file test output.

## Acceptance checks
- [ ] Executed: `python ci-check-setter/scripts/hookgen.py --selftest` prints `selftest ok`; `hookgen.py check .githooks/pre-commit` prints PASS.
- [ ] Executed: the throwaway-branch test shows `BLOCKED` for the bad file and exit 0 for the good one, or `UNCHECKED` is recorded as untested.
- [ ] Executed: `python project-kickoff/scripts/wfdoc.py docs/CI.md --kind ci` prints PASS.
- [ ] `git config core.hooksPath` prints `.githooks`.

## Pitfalls
A hook that exits 0 when tools are missing without saying so. Checking the whole tree on every commit (slow, so people bypass it). Setting `core.hooksPath` globally. Forgetting that hooks do not run for edits that never reach git (Studio-only changes).

## Related
`dependency-pinner`, `git-workflow-setter`, `code-style-guide-writer`, `worker-verifier`, `regression-checklist-builder`.
