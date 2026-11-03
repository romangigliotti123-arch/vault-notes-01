---
name: checkpoint-system-builder
description: "Build obby checkpoints decided by the server: touches accepted only for the next stage, skip detection, a minimum stage time with a suspicion counter, saved stage for respawn and a finish stamp. Use for obbies and stage runners; the tower/round flow is round-system-builder."
category: systems
tags: checkpoints, obby, stages, respawn, anti-skip, speedrun, progress, save stage
kb: Roblox/roblox-kb/anti-exploit-and-security.md, Roblox/roblox-kb/case-studies-tower-of-hell.md, Roblox/roblox-kb/case-studies-obby.md, Roblox/roblox-kb/data-persistence.md
related: round-system-builder, spawn-system-builder, achievement-badge-builder, exploit-audit, leaderboard-builder
---

# checkpoint-system-builder

One job: make stage progress something the server decides. A checkpoint touch is accepted only when it is the NEXT stage (or an already-passed one), a stage cleared faster than a human minimum is refused and counted, the saved stage drives respawn, and finishing stamps the time. `scripts/Checkpoints.luau` works on `data.Obby` in the player's saved data.

## When to use
Obbies, parkour, stage-based runs, any 'resume where you left' progress. Not for: round-based modes (`round-system-builder`), leaderboards of times (`leaderboard-builder`).

## Inputs (max 2)
1. Number of stages and expected fastest legitimate time per stage (default: from a playtest run; ask for it). 2. What a refused touch does (default: respawn at last stage, log, no kick).

## Procedure
1. Playtest the fastest legitimate stage time (use the fastest tester run, minus a margin) and set `minStageSeconds` below that. A value from a guess flags honest players: tune it from data.
2. Copy `Checkpoints.luau`; `Checkpoints.new({ stages, minStageSeconds, now = os.clock, maxFlags = 5 })`. Number checkpoint parts with a server-readable attribute (`Stage`), and connect `Touched` (or a ProximityPrompt) in a SERVER script; never accept a remote that says 'I reached stage N'.
3. On touch: resolve the player from the touching part, then `cp:touch(data, userId, stage)`. Results: `advanced` (update spawn + effects), `already` (ignore), `skipped` (teleport back to the last stage), `too fast` (teleport back, count). `cp:suspicious(userId)` becomes true after repeated refusals: log it and let your own policy act.
4. Respawn: set the player's `RespawnLocation` or teleport to `cp:respawnStage(data)`'s spawn on `CharacterAdded`. The stage lives in saved data, so rejoin resumes it.
5. Finish: stage == last records `finishedAt`; reward through the Wallet/badge systems and offer a reset (`cp:reset`) for a new run.
6. Add a physical check too: invisible kill-floor/anti-fly volumes on stage borders are cheap and do not replace the logical check.
7. Run `cd ~/.claude/claude-kit/systems && lune run ../skillpack/systems/checkpoint-system-builder/scripts/tests/Checkpoints.test.luau` (quote the "N passed, 0 failed" line).

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `multi_edit` (or edit the Rojo files) to add `Checkpoints.luau` and the touch-handler script -> `start_stop_play` -> `execute_luau` (Server) to simulate touches for stages 1, 3 and 2 in order with a fake clock and print `data.Obby` -> `get_console_output` to read the result. Real `Touched` reliability and respawn placement are Studio work: `untested` here.

## Fallback
Files + Lune tests only. Everything that needs a running Studio session (Touched events, respawn placement, real stage times) stays `untested` until the owner runs it; the Lune tests below are the headless proof for the pure logic.

## Evidence
`Roblox/roblox-kb/anti-exploit-and-security.md` (obbies: mandatory sequential checkpoints verified in order on the server before rewards; optionally flag stage times faster than humanly possible as an extra layer - Creator Docs defensive design), `Roblox/roblox-kb/case-studies-tower-of-hell.md` and `case-studies-obby.md`, `Roblox/roblox-kb/data-persistence.md`.

## Output
`Checkpoints.luau`, the touch handler, stage attribute convention, `design/obby.md` (stage count, min time basis, refusal policy).

## Acceptance checks
- [ ] Skipping ahead is refused and changes nothing (Checkpoints test 2).
- [ ] Too-fast clears are refused, counted and flagged after the limit (test 4).
- [ ] Bad stage values (0, negative, fractional, string, NaN) are refused (test 5).
- [ ] Finish records the time; reset clears progress (test 6).
- [ ] Checkpoints Lune tests pass: `cd ~/.claude/claude-kit/systems && lune run ../skillpack/systems/checkpoint-system-builder/scripts/tests/Checkpoints.test.luau` (quote the "N passed, 0 failed" line).

## Pitfalls
Trusting a remote for stage completion. A minimum time guessed rather than measured. Kicking on the first flag (lag causes false positives). Not saving the stage (rejoin restarts). Checkpoint parts that can be moved by the client (anchor them, keep them server-owned).

## Related
`round-system-builder`, `spawn-system-builder`, `achievement-badge-builder`, `exploit-audit`, `leaderboard-builder`.
