# Fix loop (reproduce first)

A bug is fixed when a check that was red is green. Without a red check you are guessing.

## Phase 1: build the red check (before any edit)
Pick the cheapest rung that can fail for the real reason:
1. Pure logic in a ModuleScript: a Lune test (`lune run`), the way the kit's own `tests/` folders do it.
2. Behaviour in a running place: Studio MCP scripted playtest (`start_stop_play`, `execute_luau`), assert on state read back after the action or on tagged Output lines.
3. A scanner that already knows the class: `Placement.verify`, `LightingKit.scan`, a `static_scan.py` rule, `luau-check`.
4. A captured Output log or stack trace replayed against the suspect module.
5. Races and "sometimes" bugs: run the trigger N times in one script, seed `math.random`, replace sleeps by explicit waits, add a second client or a rejoin, until it fails every time.
6. Last resort: ask the user for the exact steps on their phone. Say what you tried first.

Then tighten the check: faster, a sharper symptom (the exact wrong number or message), deterministic. If you cannot make any check go red, stop and report "not reproduced", with what you tried. Do not edit code on a guess.

## Phase 2: hypotheses
Write at most 3, ranked, each with the evidence that would kill it. Test with temporary logs tagged `[FIXDBG]` (remove them after; `rg FIXDBG` must find nothing). After two failed fixes that share an assumption (for example "the event fires once"), attack the premise: write it down and test it directly before a third fix.

## Phase 3: fix
Fix the cause, not the symptom: grep all callers and sibling code with the same pattern. Keep the red check as the regression check (project `tests/` for Lune tests, otherwise `Games/<slug>/bugfix/<id>/`). Show it green. Re-run `static_scan.py`, and for map bugs the placement verify, so the fix did not move the problem.

## Phase 4: ledger
`Games/<slug>/bugfix/<id>.md` from `templates/bugfix.md`: symptom, `## RED` (command and output excerpt), cause with file:line, fix, `## GREEN` (same command, passing output). `code_gates.py` check FL1 scores the share of ledgers that have both blocks (1 of 2 complete = 5.0, below the 7.0 pass mark; scored, not blocking). A fix without a ledger is `untested` in the report. A non-obvious cause also goes to `/rbx-learn`.

## Scanner leads
A scanner hit (`static_scan.py`, `--triggers`, `scope_scan.py`) is a lead. Before it enters a fix loop give it a TRUE-POSITIVE or FALSE-POSITIVE verdict with one evidence line (the failing line or the guard, quoted); no evidence = open and unverified, not fixed on a guess. Fix true leads in tier order: exploits and data loss, crashes, leaks, performance. [cold:rbx-playtest/fp-verdict.md] read only for the line format or the optional mutation-testing one-off (not a standing rule).

## Exemptions and limits
- Trivial one-line fixes that luau-check or selene flagged: say so, no ledger.
- No Studio MCP: use rungs 1, 3 and 4 and mark play-only checks `untested`.
- Tools stay read-only for the repro: the red check never changes game data or publishes.

## Sources
Phase structure re-written in our own words from the "diagnosing bugs" skill in Matt Pocock's skills repository (MIT) and the repro-first and attack-the-premise ideas of pstack / Poteto mode by Lauren Tan (MIT, cursor/plugins); no text copied.
