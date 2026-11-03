---
name: server-authority-checker
description: "Check that the server owns every outcome: price, reward, damage, position, rank, ownership and cooldowns are computed server-side from state, not sent by the client, and server logic does not live in client-readable containers. Returns ranked leads with a fix each. Use as the first design check of any feature that touches money, items, progression or combat."
category: qa
tags: server authority, client trust, outcome, reward, damage, price, replicated storage, prompt, security audit, authority
kb: Roblox/roblox-kb/anti-exploit-and-security.md, Roblox/roblox-kb/client-server-and-remotes.md, Roblox/roblox-kb/scripting-and-performance.md, Mentor/Combined-Brain.md
related: exploit-audit, input-validation-auditor, remote-guard-builder, remote-fuzzer, honeypot-remote-builder, dupe-exploit-hunter
---

# server-authority-checker

The rule is simple: the client may REQUEST an action; the server decides what it costs, whether it is allowed now, and what it yields. `exploit-audit` is the full pre-launch audit; this skill is the focused authority pass that runs while a feature is being designed, using `scripts/AuthorityScan.luau` (heuristic scan, tested) on top of `input-validation-auditor/scripts/ArgScan.luau`'s handler extraction. It never weakens a check: fixes only move decisions to the server.

## When to use
When a feature is specified or just written: shops, rewards, quests, combat, trading, movement-based progress, admin tools, seats/vehicles. Not for: argument validation depth (`input-validation-auditor`), full launch audit (`exploit-audit`), or movement cheats (`speed-teleport-detector`).

## Inputs (max 2)
1. The feature or folder to check (default: all server and shared scripts). 2. The outcomes that matter most (default: currency, items, progression, damage).

## Procedure
1. For each action in the feature write one line: client REQUEST -> server DECISION -> server RESULT. If the request contains the result (a price, a reward, a damage number, a position the server will trust, an `isAdmin`/`rank` flag), that is a finding.
2. Run `ArgScan.extract(source)` per script to list the handlers, then `AuthorityScan.scanHandlers(handlers)`: a client argument with an outcome-like name (price, reward, amount, damage, health, xp, level, position, speed, rank, owned...) that is written or used in arithmetic is CRITICAL (money) or HIGH. Read each one: a name match is a lead, not proof.
3. `AuthorityScan.scanContainer(path, source)` on every script path: server-only APIs (`DataStoreService`, `ProcessReceipt`, `UpdateAsync`, Open Cloud key header) in `ReplicatedStorage`, `ReplicatedFirst`, `StarterGui`, `StarterPlayer`, `Workspace` are HIGH; move the script to `ServerScriptService` or `ServerStorage`, which never replicate.
4. `AuthorityScan.scanInteractions(source, path)`: prompts, click detectors and drag detectors are remotes; a `Triggered` handler in a client script means the server never checked distance, state or cost. Re-check on the server: distance AND line of sight, alive, owns/affords, off cooldown.
5. For every finding apply the standard fix: the client sends an id or intent only (`"buy", itemId`); the server looks up the price/reward/damage in a server table, re-verifies context, and updates state; prices and rewards in client-readable config are display only. Hits: the client requests an attack; the server validates target, range, cooldown, expiry and line of sight, then applies damage.
6. Also check: player-owned physics (set network ownership of NPCs, coins and pushed items to the server), health only changed server-side, admin actions gated by a server-side UserId/role check on every call, and client-visible lists (admin ids) removed.
7. Re-run steps 2-4 after fixes; list what a scan cannot see (dynamic remotes, helper-function validation, third-party modules) as unchecked.

## Studio MCP path
`list_roblox_studios` -> `execute_luau` (Edit) iterating `GetDescendants()` of the services above to collect `Script.Source` and paths, then run the scanner modules pasted inline -> `script_read` for each lead -> `multi_edit` for fixes -> `start_stop_play` + `execute_luau` (Client) to fire a request with a forged price/reward and `get_console_output` to confirm the server ignored it.

## Fallback
With a Rojo folder: run the scanners under Lune over the files (see `lune run ../skillpack/qa/server-authority-checker/scripts/tests/AuthorityScan.test.luau` from `claude-kit/systems` for usage) or `grep -rn OnServerEvent src`. Runtime forging of values stays `untested` without a test place.

## Evidence
`Roblox/roblox-kb/anti-exploit-and-security.md`: re-verify context and economy on the server before granting rewards (distance, ownership, alive, cooldown); keep authoritative logic in server-only containers; treat ProximityPrompt/ClickDetector/DragDetector as remotes; keep health and Humanoid state server-authoritative; validate hit requests (target, expiry, duplicates, distance, walls); verify events, leaderboards and rewards on the server; Server Authority mirrors scripted movement where used (live-check). `Roblox/roblox-kb/client-server-and-remotes.md`: the client requests, the server decides.

## Output
```
AUTHORITY CHECK <feature> <date>: handlers N, leads M
CRITICAL/HIGH/MEDIUM table: where | what the client decides | fix
Containers: clean | hits
Unchecked: <dynamic remotes, helper validation, third-party modules>
```

## Acceptance checks
- [ ] `lune run` of the AuthorityScan test prints "5 passed, 0 failed".
- [ ] Every action has a request -> decision -> result line and no result is client-supplied.
- [ ] Every scan lead was read and marked confirmed or dismissed with a reason.
- [ ] A forged value test (or `untested`) shows the server ignoring a client-sent price/reward/damage.
- [ ] No fix relaxes a server-side check; client-side hints are display only.

## Pitfalls
Name matching misses odd names (`n`, `v`) and flags harmless ones: read the code. Trusting a client "isAdmin" or "owned" flag. Putting prices in a client-readable module and also trusting what the client sends. Fixing one remote while a ProximityPrompt reaches the same logic. Hiding scripts in `ReplicatedStorage` with vague names and calling it secure (obfuscation is friction only).

## Related
`exploit-audit`, `input-validation-auditor`, `remote-guard-builder`, `remote-fuzzer`, `honeypot-remote-builder`.
