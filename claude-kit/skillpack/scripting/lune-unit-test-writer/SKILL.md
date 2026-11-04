---
name: lune-unit-test-writer
description: "Write Lune unit tests for pure game logic using the kit's tiny harness and a set of mocks (fake clock, spy, signal, remote, player, DataStore with failure injection), and keep the Roblox-only parts out of the tested core. Use when logic can break silently: economy maths, cooldowns, state rules, parsers, schedulers."
category: scripting
tags: lune, unit test, testing, mock, harness, ci, pure logic, tdd, luau, regression
kb: Roblox/roblox-kb/testing-debugging-and-qa.md, Roblox/roblox-kb/version-control-and-tooling.md, Roblox/roblox-kb/code-architecture-and-frameworks.md
related: state-machine-builder, cooldown-manager-builder, datastore-schema-builder, retry-wrapper-builder, kit-system-integrator, rbx-playtest-list
---

# lune-unit-test-writer

Tests catch the bugs that only show up as angry reviews three weeks later. Lune runs Luau outside Roblox, so it can test any module that does not need the engine. The kit already ships the harness (`systems/_check/harness.luau`) and five tested systems (PlayerData, Shop, DailyRewards, Analytics, Admin); this skill writes tests the same way and supplies the fakes.

## When to use
A module with rules that can be wrong: money, odds, cooldowns, rewards, state transitions, parsing, scheduling. Not for: anything that is mostly engine calls (physics, rendering, replication): those are play tests, and are reported `untested`, not faked.

## Inputs (max 2)
1. The module to test (default: pure logic first). 2. The cases that matter (default: normal, boundary, invalid, failure).

## Procedure
1. Make the module testable: pass in anything environmental (a clock function, a store, a random function, the service) instead of reaching for globals. `Cooldowns.new(clock)`, `Retry.run(fn, { wait, random })` are the pattern. If a module calls `game:GetService` at top level, split the pure core out and test that.
2. Write `scripts/tests/<Module>.test.luau` beside the module with `--!nocheck`, requiring the harness (`../../../../../systems/_check/harness`) and the module by relative path. One `t.test("sentence describing behaviour", function() ... end)` per behaviour; end with `t.done()` (exits 1 on any failure so CI notices).
3. Use `scripts/Mocks.luau`: `Mocks.clock()` (advance time by hand), `Mocks.spy(fn)` (calls and count), `Mocks.signal()`, `Mocks.remote()` (call `FireFromClient(player, ...)` as the exploiter, read `sent`), `Mocks.player(userId, name)`, `Mocks.store()` (DataStore-like, `failNext(n)` injects throttling). The kit systems have their own store fake; reuse theirs when testing them.
4. Case list per module: the happy path; each boundary (0, 1, max, max+1, negative, NaN); invalid types (the exploit inputs); each failure mode (store throws, signal handler throws, player leaves mid-operation); idempotency (the same receipt twice); ordering (two events in both orders).
5. Test through the public API, not private fields. Assert on outcomes (balance, state, calls made), not on how many internal steps ran.
6. Run: from the kit `systems` folder `lune run ../skillpack/scripting/<skill>/scripts/tests/<Name>.test.luau`; all packs: `bash skillpack/check-scripts.sh` (runs stylua, selene, luau-lsp and every test; exit 0 means all green).
7. Wire CI: the vault recommends gating merges on StyLua `--check` and Selene; add the test command next to them.
8. After a bug is found in play, add the failing test first, then fix it.

## Studio MCP path
Not applicable to the tests themselves (they run outside Studio). Use `start_stop_play` + `get_console_output` only to check the engine-bound parts the tests cannot cover, and say which those are.

## Fallback
This is the fallback: Lune, `stylua`, `selene`, `luau-lsp` from Rokit (see `tools/roblox-project-template/README.md`).

## Evidence
`Roblox/roblox-kb/testing-debugging-and-qa.md`: print inputs per step for logic bugs, defensive error handling with status codes; the same file states the vault has no coverage of unit-test frameworks, so Lune and this harness come from the kit, not from the KB. `Roblox/roblox-kb/version-control-and-tooling.md`: gate merges with StyLua `--check` and Selene in CI; linters outside Studio.

## Output
Test files, the command used, the result line (`N passed, 0 failed`), and a list of what is not covered (engine-bound behaviour).

## Acceptance checks
- [ ] Executed: `lune run ../skillpack/scripting/lune-unit-test-writer/scripts/tests/Mocks.test.luau` quoted (`7 passed, 0 failed`) and the new module's tests quoted.
- [ ] Each test name states a behaviour; each module has boundary and invalid-input cases.
- [ ] A deliberately broken copy of the module fails at least one test (mutation check, executed once).
- [ ] No test touches the network, the real clock or random without injection.
- [ ] Not-covered list written.

## Pitfalls
Mocking so much that the test checks the mock. Asserting implementation details. Time-based tests with `task.wait` (use the fake clock). Random without a seed or injection. Testing only the happy path. A green suite read as "the game works" (engine behaviour is separate).

## Related
`state-machine-builder`, `cooldown-manager-builder`, `retry-wrapper-builder`, `kit-system-integrator`, `rbx-playtest-list`.
