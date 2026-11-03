---
name: honeypot-remote-builder
description: "Add trap remotes that legitimate code never fires (a fake AddMoney) plus a suspicion score, escalation ladder and watch list, so exploiters reveal themselves with near-zero false positives and the response stays reversible. Use after the real remotes are guarded, as an early-warning layer; never as the only defence."
category: qa
tags: honeypot, trap remote, anti-cheat, suspicion score, watch list, ban api, exploit detection, logging, escalation
kb: Roblox/roblox-kb/anti-exploit-and-security.md, Roblox/roblox-kb/client-server-and-remotes.md, Roblox/roblox-kb/testing-debugging-and-qa.md, Mentor/Combined-Brain.md
related: exploit-audit, remote-guard-builder, speed-teleport-detector, remote-fuzzer, input-validation-auditor, roblox-remote-security
---

# honeypot-remote-builder

An exploiter who enumerates remotes and fires attractive-looking ones identifies themselves: no honest client ever calls a fake `AddMoney`. The honeypot is detection, not protection; the real remotes still need validation (`remote-guard-builder`). `scripts/Honeypot.luau` is the tested decision logic (score, decay, ladder, watch list); `scripts/HoneypotService.luau` is the Roblox glue that creates the traps.

## When to use
After `exploit-audit` fixes the CRITICAL/HIGH findings, to see who probes the game, or to feed a suspicion score from several weak signals (movement flags, rate-limit hits). Not for: replacing validation, client-side detection, or auto-banning on weak signals.

## Inputs (max 2)
1. Trap names and where they live (default: 3 attractive names that do not exist in the game, in the same folder as the real remotes). 2. The response policy (default: log, then mitigate, then restrict, then human review; no automatic permanent ban).

## Procedure
1. Pick names that look valuable but are unused: grep the project to confirm no real code uses them. Never reuse a real remote's name. Stop when each name returns zero hits.
2. Install `scripts/Honeypot.luau` and `scripts/HoneypotService.luau` in ServerScriptService; call `HoneypotService.Start(onAction)`. The traps are RemoteEvents with only a server listener that calls `Honeypot:Trip(userId, name)`.
3. Weights: a trap trip is the review weight (default 10); weak signals are 1 (movement/rate flag) to 3 (impossible request). Decay is 1 point per minute, so one lag spike a day never escalates.
4. Ladder: `log` -> `mitigate` (drop the request, reset position quietly) -> `restrict` (disable trading/shop for the session) -> `review` (put the UserId on the watch list for a human; use the Ban API by UserId with a duration and reason, not a bare Kick). Keep the watch list separate from bans, and log every action as JSON (UserId, reason, score, action).
5. Respond silently where possible: do not tell the client which check fired; for a trap, return nothing.
6. Test in a TEST place with a non-exempt account: fire each trap from `execute_luau` (Client) and read the server log; confirm a normal session produces zero trips. Dev/staff accounts can be exempt from anti-cheat; use `exempt` only for them and test with a normal one too.
7. Optional hardening: keep the trap names out of any script a client can read to find them by diffing; assume a determined exploiter can learn them eventually.

## Studio MCP path
`list_roblox_studios` -> `execute_luau` (Edit) to create the scripts -> `start_stop_play` -> `execute_luau` (Client) `game.ReplicatedStorage.Network.AddMoney:FireServer(1e9)` -> `get_console_output` for the JSON line -> `start_stop_play` (stop).

## Fallback
Without Studio: write both files, run `lune run ../skillpack/qa/honeypot-remote-builder/scripts/tests/Honeypot.test.luau` from `claude-kit/systems`, and give the owner the manual fire step. Glue behaviour in a running server is `untested`.

## Evidence
`Roblox/roblox-kb/anti-exploit-and-security.md`: deploy honeypot remotes for high-confidence detection; escalating consequence ladder with a suspicion score; prefer reversible actions for uncertain detections; use the Ban API by user ID instead of Kick; keep a watch list separate from bans and log every action; respond silently to suspected exploiters; never trust client detections that hooks can spoof. Trust: DevForum and creator reports (labelled); the weights are this skill's defaults, tune per game.

## Output
Two scripts in ServerScriptService, a table of trap names (not published), the ladder thresholds, and a JSON log format. A short test log: normal session 0 trips, forced trip -> `review`.

## Acceptance checks
- [ ] Honeypot Lune test prints "6 passed, 0 failed".
- [ ] Each trap name has zero other uses in the project (grep output quoted).
- [ ] Firing a trap from a non-exempt test client produced one JSON log line with action `review`; a normal session produced none.
- [ ] No code path permanently bans or kicks automatically; the top rung only flags for human review.
- [ ] The real remotes are guarded (`exploit-audit` shows no CRITICAL left).

## Pitfalls
Treating the honeypot as protection. Naming a trap like a real remote. Testing only with a dev account. Auto-banning on a single weak signal. Telling the exploiter what tripped. Forgetting that anyone can read a client-visible name list.

## Related
`exploit-audit`, `remote-guard-builder`, `speed-teleport-detector`, `remote-fuzzer`.
