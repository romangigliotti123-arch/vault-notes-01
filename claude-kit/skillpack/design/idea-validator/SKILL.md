---
name: idea-validator
description: "Fast go / fix / kill gate for a Roblox game idea before any build time: seven pass/fail tests from the vault (one-sentence, proven loop, core fantasy, young-mobile fit, first-minute fun, scope, packaging) with evidence from comparable games, ending in a verdict and the single cheapest fix. Use before rbx-rate and the plan; it is the 10-minute filter, not the full rating."
category: design
tags: idea, validate, validation, kill, go no-go, concept, pitch, genre, saturated, test
kb: Roblox/roblox-kb/game-ideas-and-genres.md, Roblox/roblox-kb/trend-research-and-validation.md, Roblox/roblox-kb/core-loops-and-game-design.md, Roblox/roblox-kb/_tools/DECISION-RULES.md, Roblox/roblox-kb/mindset-and-strategy.md
related: rbx-rate, rbx-ideas, rbx-trends, one-sentence-pitch, genre-twist-finder, scope-cutter, competitor-teardown, game-reviewer
---

# idea-validator

`rbx-ideas` generates ideas, `rbx-rate` scores a chosen one on 12 weighted criteria. This sits between: seven binary tests that kill weak ideas in minutes. It never builds anything.

## When to use
The user has an idea (or three) and wants to know whether it is worth building. Not for: generating ideas (`rbx-ideas`), market research (`rbx-trends`), or the full rating (`rbx-rate`).

## Inputs (max 2)
1. The idea in a few sentences. 2. Team and time (default: solo, 4 weeks to a first playable, AI-assisted).

## Procedure
1. Restate the idea as ONE sentence a 12-year-old could repeat (see `one-sentence-pitch`). If you cannot, fail test 1 and stop at the fix.
2. Run the seven tests. Each is PASS / FAIL / UNSURE with an evidence line. Pull rules with `python -I ~/.claude/claude-kit/tools/kbq.py section game-ideas-and-genres rules --max-chars 3500` and `section core-loops-and-game-design rules`; find comparables with `python -I ~/.claude/claude-kit/tools/kbq.py case "<genre>" -n 3`.
   1. One sentence: repeatable in 10-15 seconds, understood from a thumbnail.
   2. Proven loop: starts from a working formula with a 10-20 percent twist (vault: change at least about 20 percent of the reference; keep 80-90 percent familiar), not a new genre. Name the 1-2 reference games and the twist.
   3. Core fantasy: a role or feeling the player wants (builder, hatcher, survivor, racer), not a bare mechanic.
   4. Audience fit: Roblox skews young and mobile; works with touch, no long text, no heavy skill gate.
   5. First-minute fun: the first action and first reward can happen within the first minute (vault: fun within seconds, 5 minutes at most).
   6. Scope: a playable core loop can exist in the stated time; list what must be cut (`scope-cutter`).
   7. Packaging: a clear thumbnail concept and literal title are possible (title carries the fantasy).
3. Saturation check (live data is the exception, so label it): `rbx-trends` for what leads now, or the vault cases. Saturated is fine if the twist is real; unsaturated and unproven is the risky case.
4. Verdict: GO = 6-7 pass and no FAIL on 1, 3 or 5; FIX = at most two fails that one change repairs; KILL = a fail on 1, 3 or 5 that no cheap change repairs, or three or more fails. Say the single cheapest fix for FIX.
5. Next step: GO -> `/rbx-rate` then `/rbx-plan`; FIX -> apply the fix, re-run only the failed tests once; KILL -> offer 2 alternative directions from the same fantasy.

## Studio MCP path
Not needed. Optionally `http_get` (Roblox docs only) for platform facts.

## Fallback
Same procedure from the vault only. Mark live saturation as `untested` when no web access.

## Evidence
`Roblox/roblox-kb/game-ideas-and-genres.md` (proven loop; 20 percent twist; one-sentence test; core fantasy; mass appeal and young players), `Roblox/roblox-kb/trend-research-and-validation.md`, `Roblox/roblox-kb/core-loops-and-game-design.md`, `Roblox/roblox-kb/_tools/DECISION-RULES.md`. Most creator advice is indie-flagged: say so when a test rests on it.

## Output
```
IDEA CHECK: "<one sentence>"
1 One sentence PASS - ...   2 Proven loop PASS - ref: <game>, twist: <...>   (7 rows, one line each)
Verdict: GO | FIX | KILL   Cheapest fix: ...   Next: /rbx-rate
Assumptions: ...   Not checked: ...
```
Under 30 lines.

## Acceptance checks
- [ ] Exactly seven tests, each with an evidence line.
- [ ] The reference game(s) and the twist are named for test 2.
- [ ] Verdict follows the stated rule (recount the passes).
- [ ] KILL and FIX include something actionable.
- [ ] Live market claims are labelled live-checked or untested.

## Pitfalls
Passing everything out of politeness. Treating "no one has made this" as a plus. Confusing a feature list with a fantasy. Skipping the time-boxed scope test (most solo projects die there).

## Related
`rbx-rate`, `rbx-ideas`, `one-sentence-pitch`, `genre-twist-finder`, `scope-cutter`, `competitor-teardown`.
