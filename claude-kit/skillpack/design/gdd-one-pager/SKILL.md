---
name: gdd-one-pager
description: "Write a one-page game design doc an AI or a teammate can build from: pitch, core loop, progression, systems, monetisation, scope and acceptance tests, in plain sections that the game-dev critic can score. Also ships docheck.py, the structure checker the design skills use. Use once the loop, fantasy and scope exist."
category: design
tags: gdd, design doc, one pager, spec, documentation, handoff, requirements, acceptance
kb: Roblox/roblox-kb/development-process-and-speed.md, Roblox/roblox-kb/game-ideas-and-genres.md, Roblox/roblox-kb/core-loops-and-game-design.md, Roblox/roblox-kb/monetisation-gamepasses.md, Roblox/roblox-kb/trend-research-and-validation.md
related: idea-validator, one-sentence-pitch, core-loop-designer, scope-cutter, mvp-definer, rbx-critic, rbx-workflow
---

# gdd-one-pager

Vault: write a game design doc (genre, concept, references, features, modes, monetisation, controls, UI, needed roles and assets) and turn it into a task board; write detail up front because gaps found in week one beat gaps found in month three. One page keeps it readable by an AI with a small context.

## When to use
After the idea passes `idea-validator` and the loop is designed, or when a teammate or AI must build from it. Not for: a long bible, the loop design itself, or store copy.

## Inputs (max 2)
1. The design files already written (`design/pitch.md`, `core-loop.md`, `fantasy.md`, `scope.md`, `mvp.md`). Default: summarise those; ask only for what is missing. 2. Audience (default: ages 9-14, mobile-first).

## Procedure
1. Pull, do not rewrite: copy each section's conclusion from the existing design files with a link. Missing section = call the matching skill first (pitch: `one-sentence-pitch`; loop: `core-loop-designer`; scope: `scope-cutter`).
2. Write these sections, one short paragraph or table each: Pitch (sentence plus references), Core loop (verb sentence plus three layers with cycle times), Progression (goals by horizon, first unlock time), Systems (list; for each: build or reuse from the kit's PlayerData, Shop, DailyRewards, Analytics), Monetisation (what is sold, what stays free, nothing core behind a paywall), Scope (MVP, deferred, cut), Acceptance (pass/fail tests from `mvp-definer`), Open questions (what is unknown, labelled `judgment`).
3. Keep it to one page: about 60-100 non-empty lines. A line over a limit is cut or linked.
4. Check consistency: every system appears under a loop layer; every monetisation item is optional or cosmetic or convenience (`monetisation-gamepasses`); every acceptance test maps to a section. Stop at the first mismatch and fix it.
5. Run the structure check: `python gdd-one-pager/scripts/docheck.py design/gdd.md --kind gdd`.
6. Hand to `rbx-critic` at the idea stage: the doc should let it score factors 2, 5, 7 and 10 of the quality model from text alone; if it cannot, add the missing facts.
7. Save `design/gdd.md`; add its path to the plan.

## Studio MCP path
Design only.

## Fallback
Pure document.

## Evidence
`development-process-and-speed` (write a game design doc and turn it into a task board; detail up front), `game-ideas-and-genres` (references, one-sentence test), `core-loops-and-game-design` (three-part loop; tie systems to the loop), `monetisation-gamepasses` (never gate core progress), `trend-research-and-validation`.

## Output
`design/gdd.md` (one page) with headings Pitch, Core loop, Progression, Systems, Monetisation, Scope, Acceptance, Open questions. Script: `scripts/docheck.py` (also used by the other design skills; `--kind` picks the required headings).

## Acceptance checks
- [ ] Executed: `python gdd-one-pager/scripts/docheck.py --selftest` prints `selftest ok (6 checks)`.
- [ ] Executed: `python gdd-one-pager/scripts/docheck.py design/gdd.md --kind gdd` prints PASS.
- [ ] Every section either links a source file or is marked `judgment`.
- [ ] No placeholder text (TODO, TBD) and no invented ids or prices (use `0` / `SET IN CREATOR HUB`).

## Pitfalls
A GDD that is a wish list. Rewriting sections rather than linking them (drift). Detail on features that are deferred. Skipping Open questions so unknowns look like decisions.

## Related
`idea-validator`, `core-loop-designer`, `scope-cutter`, `mvp-definer`, `rbx-critic`.
