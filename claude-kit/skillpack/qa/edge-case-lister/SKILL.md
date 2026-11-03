---
name: edge-case-lister
description: "List the edge cases a feature must survive by walking fixed axes (state, timing, count, identity, value, platform, failure) and turning each into a testable row with an expected outcome and an owner test. Use when specifying a feature, before writing its tests, or when a feature keeps breaking in odd ways."
category: qa
tags: edge cases, boundary, test cases, feature spec, failure modes, corner cases, qa, checklist, robustness, what if
kb: Roblox/roblox-kb/testing-debugging-and-qa.md, Roblox/roblox-kb/anti-exploit-and-security.md, Roblox/roblox-kb/data-persistence.md, Roblox/roblox-kb/client-server-and-remotes.md
related: remote-fuzzer, join-leave-race-tester, device-test-matrix, regression-checklist-builder, dupe-exploit-hunter, lune-unit-test-writer, multiplayer-test-planner
---

# edge-case-lister

Features usually work on the path the author tried. Edge cases are the paths nobody tried: zero of something, two at once, the player leaving, the value being huge or NaN, the data not loaded yet. This skill walks seven fixed axes over a feature and produces a short table where each row is testable, with the test that will own it. It does not invent facts about the game: it asks "what if" in a fixed order and records the answer the design wants.

## When to use
When a feature is specified or just written, before writing its tests, or after a bug that "should never happen". Not for: bad-argument attacks (`remote-fuzzer` generates values), race enumeration (`join-leave-race-tester`), or device coverage (`device-test-matrix`).

## Inputs (max 2)
1. The feature in two sentences with its inputs, state and outputs. 2. The risk to weight (default: lost progress or money first, then crashes, then cosmetics).

## Procedure
1. Write the feature as: trigger -> checks -> state change -> feedback. Stop when each part names concrete objects (the shop, the pet, the coin counter).
2. Walk the axes; for each ask the question and write a row only when it applies:
   - State: not loaded yet, just respawned, dead, in a menu, in a round vs lobby, already owns it, at max level, inventory full, no permission.
   - Timing: twice quickly (double click, double fire), during a yield (data load, purchase prompt), before the character exists, after the player left, at server shutdown, at the exact moment a timer ends.
   - Count: zero, one, max, max+1, negative, fractional; empty list; 1000 items.
   - Identity: another player's object, a destroyed object, a nil target, yourself, a friend, a banned or new account, two accounts on one device.
   - Value: NaN, inf, huge, empty string, very long string, unicode, a name that collides (see the corpus in `remote-fuzzer/scripts/Fuzz.luau`).
   - Platform: touch vs keyboard vs gamepad, smallest screen, slow network, low memory (pairs via `device-test-matrix/scripts/Pairwise.luau`).
   - Failure: DataStore errors, Marketplace call fails, HTTP times out, a dependency is missing, a script errors mid-way and leaves half a change.
3. For each row write the EXPECTED outcome the design wants: reject with a message, queue, ignore, roll back, retry, show a placeholder. "Do not crash" is not an outcome.
4. Assign the owner test: a Lune unit test for pure logic (`lune-unit-test-writer`), a fuzz rig (`remote-fuzzer`), a scenario suite, a bot step (`playtest-bot-writer`), or a manual row in `regression-checklist-builder`. A row with no owner is not covered.
5. Rank rows: S1 loses money/data or crashes, S2 blocks the loop, S3 odd but recoverable, S4 cosmetic; test S1 and S2 first.
6. Cut duplicates and rows the design explicitly accepts; keep the list under about 30 rows per feature, otherwise split the feature.
7. Re-read after the first bug: every bug found later that was not on the list adds a row and a question to the axis that missed it.

## Studio MCP path
`script_read` / `script_grep` for the feature's handlers and `get_studio_state` for the test place; `execute_luau` (Server) to set up each edge state (set data, kill the character, remove an item) and `get_console_output` to see the outcome for the row.

## Fallback
Pure thinking plus the table; run what can run under Lune. Rows that need a running game are `untested` until a bot or manual run records them.

## Evidence
`Roblox/roblox-kb/testing-debugging-and-qa.md`: stress-test loops, duplicates and persistence after each change; unit-test functions with known inputs including edge inputs; handle errors defensively (status codes, guards, catch blocks); try security as an exploiter in a test place (one-time codes twice, rejoin). `Roblox/roblox-kb/anti-exploit-and-security.md`: bound amounts, reject NaN, validate Instances. `Roblox/roblox-kb/data-persistence.md`: failures and shutdown. The seven axes are this skill's checklist, not a Roblox standard.

## Output
```
EDGE CASES <feature> <date>: rows N (S1 a, S2 b, S3 c)
| id | axis | what if | expected outcome | severity | owner test | status |
Excluded (accepted by design): <list>
```

## Acceptance checks
- [ ] Every axis was walked; skipped axes have a one-line reason.
- [ ] Every row has an observable expected outcome and an owner test; no row says "should work".
- [ ] All S1 and S2 rows have a runnable owner (test, bot, scenario or fuzz rig), run once, with result recorded or `untested`.
- [ ] The list is under about 30 rows or the feature was split.
- [ ] Rows found by later bugs were added back.

## Pitfalls
Listing cases without outcomes. Writing the happy path as an edge. Hundreds of rows nobody runs. Treating "client sends bad value" as the only edge (state and timing hurt more). Forgetting what happens to half-applied changes when an error hits mid-way.

## Related
`remote-fuzzer`, `join-leave-race-tester`, `device-test-matrix`, `regression-checklist-builder`, `dupe-exploit-hunter`, `multiplayer-test-planner`.
