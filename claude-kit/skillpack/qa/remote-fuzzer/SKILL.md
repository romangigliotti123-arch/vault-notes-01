---
name: remote-fuzzer
description: "Fuzz your own remote handlers in a test place with a bad-value corpus (NaN, inf, negatives, fractions, huge strings, wrong types, cyclic tables) and rapid bursts, and report which values changed state or crashed the handler. Use after remote-guard-builder to prove the guards work, and before launch."
category: qa
tags: fuzz, remote, bad input, nan, negative, rate limit, burst, exploit test, validation test, server
kb: Roblox/roblox-kb/anti-exploit-and-security.md, Roblox/roblox-kb/testing-debugging-and-qa.md, Roblox/roblox-kb/client-server-and-remotes.md
related: remote-guard-builder, exploit-audit, input-validation-auditor, server-authority-checker, honeypot-remote-builder, playtest-bot-writer
---

# remote-fuzzer

A guard you have not attacked is a guess. This skill sends every bad value an exploiter could send into each argument of each handler, one position at a time, and reports the ones the handler accepted (state changed) or crashed on. `scripts/Fuzz.luau` holds the corpus and runner and is tested against a naive handler and a `RemoteGuard`-guarded one. Only ever run it against YOUR OWN test place or a Lune fake.

## When to use
After adding or changing a remote handler or its guard, before launch, after `exploit-audit` fixes. Not for: the live game, other people's games, load testing (`load-test-planner`), or finding which remotes exist (`exploit-audit`).

## Inputs (max 2)
1. The handler(s) to fuzz (default: every remote touching currency, items, data, teleport, damage). 2. A valid baseline call per handler (default: the call the client UI makes).

## Procedure
1. For each handler write a rig: `call(args)` (invoke the handler body, or fire the real RemoteEvent from a Client `execute_luau` in the test place), `snapshot()` (the state it may change: coins, inventory, position, cooldown table), `reset()`, `baseline` args, and `kinds` per argument (`number`, `integer`, `string`, `table`, `instance`, `any`). Stop when the baseline call alone changes the snapshot.
2. Run `Fuzz.run(rig)`. It tries NaN, +/-inf, -1, 0, 0.5, 2^53, 1e308, empty/10k/NUL/unicode/markup strings, nil, booleans, empty/cyclic/deep/5000-element tables in each argument position. Each result is `accepted` (state changed with a non-baseline value) or `threw` (handler errored; handlers should reject, not crash).
3. Triage: any `accepted` on a currency/item/data path is CRITICAL (fix with `remote-guard-builder`: integer range, `oneOf`, finite number, class check). A `threw` is MEDIUM (missing guard, `nil` index). Then re-run until 0 findings.
4. Burst test: `Fuzz.burst(rig, 50)` fires 50 valid requests back to back; the count of accepted ones must not exceed the per-player limit you configured (`RemoteGuard.newLimiter`). A burst of 50 accepted means no effective rate limit.
5. Instance arguments (real engine only): send an Instance of the wrong class, one under the wrong parent, a destroyed one, and one belonging to another player; the handler must reject by class and location.
6. Keep the rigs under `tests/fuzz/` (not shipped); add each fixed finding as a permanent case.
7. Never test against the live place or live DataStore; the fuzz rig touches only fakes or a test place with a test store.

## Studio MCP path
`list_roblox_studios` -> `start_stop_play` -> `execute_luau` (Client) firing the real RemoteEvents with the corpus values (use `Fuzz.corpus(kind)` pasted inline) -> `execute_luau` (Server) to read the snapshot -> `get_console_output` for rejections and errors -> `start_stop_play` (stop).

## Fallback
Without Studio: extract the handler body into a function, build the rig, and run it under Lune (`lune run ../skillpack/qa/remote-fuzzer/scripts/tests/Fuzz.test.luau` from `claude-kit/systems` shows the pattern). Engine-only checks (Instance args, replication, real rate-limit timing) stay `untested`.

## Evidence
`Roblox/roblox-kb/anti-exploit-and-security.md`: validate every client argument (type, nil, range, length, Instance class/location); reject NaN and inf with `math.isfinite` because NaN fails every comparison and silently passes range checks; bound economy amounts and floor fractions, since negative or decimal trades create value; rate-limit per player on the server. `Roblox/roblox-kb/testing-debugging-and-qa.md`: test security as an exploiter in your own test place (one-time codes twice, rejoin), stress-test loops and duplicates after each change.

## Output
```
FUZZ remote <name>: findings N
  arg 2 (integer): -1 -> accepted   (CRITICAL: coins increased)
  arg 1 (string): nil -> threw      (MEDIUM)
BURST 50 -> accepted K (limit L)
```
Plus the fix per finding and the re-run result.

## Acceptance checks
- [ ] Fuzz test file prints "6 passed, 0 failed" (naive handler caught, guarded handler clean).
- [ ] Every money/item/data handler has a rig; the baseline call changed state (no vacuous run).
- [ ] After fixes the re-run reports `FUZZ: 0 findings` and the burst count is at or below the configured limit.
- [ ] No fuzzing was done outside a test place or fake.

## Pitfalls
A snapshot that misses the field the handler changes (everything looks rejected). Fuzzing the validator instead of the handler. Counting a handler that silently ignores the value as safe when it `threw` instead. Forgetting the second remote that reaches the same logic. Running against the live game.

## Related
`remote-guard-builder`, `exploit-audit`, `input-validation-auditor`, `server-authority-checker`, `honeypot-remote-builder`.
