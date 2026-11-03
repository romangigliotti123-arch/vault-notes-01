---
id: "roblox-skills-ashexplained/roblox-code-maintenance-refactor"
type: skill
category: "src-roblox-skills-ashexplained"
source: "roblox-skills-ashexplained"
license: "MIT"
repo_path: "sources/roblox-skills-ashexplained/skills/roblox-code-maintenance-refactor/SKILL.md"
description: "Maintain and refactor Roblox Luau code safely. Use for technical debt, dead code removal, module boundaries, naming cleanup, duplicate logic, dependency review, regression prevention, and long-term codebase health."
orig_name: "roblox-code-maintenance-refactor"
tags: [lib/skill, cat/src-roblox-skills-ashexplained, src/roblox-skills-ashexplained]
---

# roblox-skills-ashexplained/roblox-code-maintenance-refactor

> Maintain and refactor Roblox Luau code safely. Use for technical debt, dead code removal, module boundaries, naming cleanup, duplicate logic, dependency review, regression prevention, and long-term codebase health.

Type: skill | Category: [[categories/cat-src-roblox-skills-ashexplained|src-roblox-skills-ashexplained]] | Source: [[sources/src-roblox-skills-ashexplained|roblox-skills-ashexplained]] | License: MIT
Repo file: `sources/roblox-skills-ashexplained/skills/roblox-code-maintenance-refactor/SKILL.md` (extra files, if any, sit beside it in the repo)

Related: [[S--roblox-skills-ashexplained--roblox-luau-architecture]], [[S--roblox-skills-ashexplained--roblox-playtest-qa]], [[S--roblox-skills-ashexplained--roblox-to-issues]]

---
# Roblox Code Maintenance Refactor

## Goal

Improve code health without changing player-facing behavior accidentally.

## Refactor Rules

- Read before editing.
- Keep changes scoped.
- Preserve remote contracts unless intentionally migrating.
- Avoid mixing behavior changes with cleanup.
- Playtest after meaningful refactors.
- Check console output.

## Targets

- Duplicated constants and reward formulas.
- Large scripts with mixed responsibilities.
- Client/server boundary confusion.
- Dead remotes, stale UI paths, unused modules.
- Repeated event connection patterns.
- Unclear names around valuable state.
- Magic numbers that should be balance tables.

## Finding Deepening Opportunities

Beyond obvious cleanup, hunt for **shallow modules** to deepen — where the interface is nearly as complex as the implementation, so callers carry complexity that should be hidden.

- Where does understanding one concept require bouncing between many tiny scripts?
- Where were pure helpers extracted only for tidiness, but the real bugs live in how they're called (no locality)?
- Where do client and server share a responsibility that leaks across the remote boundary?

Apply the **deletion test** to anything you suspect is shallow: if deleting it just moves complexity around, inline it; if deleting it would scatter the same complexity across many call sites, keep it and give it a small, stable interface named from the game's vocabulary. Present each opportunity as: files involved · the friction today · the proposed change · the benefit (locality + testability). Don't propose new indirection for a single implementation. See `roblox-luau-architecture` for the deep-module model.

## MCP Workflow

1. Use `script_grep` to find duplication, old names, or call sites.
2. Read all affected scripts with `script_read`.
3. Make small edits with `multi_edit`.
4. Use `start_stop_play` to verify the relevant loop.
5. Check `get_console_output`.

## Output

Return:

- Refactor goal.
- Behavior preserved.
- Scripts changed.
- Verification performed.
- Follow-up debt items.

## Next

Verify no behavior changed with `roblox-playtest-qa`. For larger structural changes, design them in `roblox-luau-architecture` and slice them with `roblox-to-issues` so they land one safe step at a time.
