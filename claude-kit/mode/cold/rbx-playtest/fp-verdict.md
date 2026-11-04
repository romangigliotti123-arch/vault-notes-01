<!-- cold: rbx-playtest/fp-verdict.md | read when: a scanner (static_scan, triggers, scope_scan, comment_scan) reports leads before a fix loop, or you consider mutation-testing the Systems tests once. -->

# Verdict before fix (research round 2; the idea comes from the Trail of Bits false-positive-check skill, licensed CC-BY-SA so idea only, wording ours)

A scanner hit is a lead, not a bug. The fix loop (`references/fix-loop.md`) only acts on a lead that has a verdict.

## Format, one line per lead (in the playtest report or `bugfix/<id>.md`)
`<path:line> | <check id> | TRUE-POSITIVE or FALSE-POSITIVE | evidence: <what you opened or ran, with the exact line or output>`
- TRUE-POSITIVE needs the failing path shown: the unguarded handler line, the missing `BindToClose`, or a red check that fails because of it.
- FALSE-POSITIVE needs the guard that makes it safe, quoted with its line (the rate limit in the wrapper, the cleanup in the parent module, the deliberate cast).
- No evidence line = the lead stays open and is reported as unverified; do not fix it on a guess and do not dismiss it on a guess.
- Fix TRUE-POSITIVEs in tier order: exploits and data loss, crashes, leaks, performance.

## Mutation testing, optional one-off (NOT a standing rule)
Purpose: learn whether a Systems test suite would notice a real defect. Only on our own repo, never on a game under review, no scripts shipped.
1. Pick one system (for example PlayerData or Shop) and confirm its Lune tests pass.
2. Make ONE small change in a scratch copy: flip a comparison, drop a clamp, skip a `PlayerRemoving` cleanup, return early before the save.
3. Run the tests. A failing test means the mutant was killed; passing means a test gap: note it and add a test.
4. Revert the copy, repeat for 5-10 mutants, record the survivors in the notes. Stop there.
