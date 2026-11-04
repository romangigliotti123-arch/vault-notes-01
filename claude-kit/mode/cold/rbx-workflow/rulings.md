<!-- cold: rbx-workflow/rulings.md | read when: the manager writes a brief or hits an ambiguity, or the critic orders spec compliance against style. -->

# Rulings, DONE WHEN and review order (research round 2; ideas adapted from the MIT-licensed Superpowers subagent-driven-development skill and a public goal-prompt pattern, wording ours)

## Ruling ledger (decide, log, move on)
When a brief or a spec is ambiguous, the manager decides instead of asking and writes one line in `decisions.md` (or the job row): `Ruling: <what was decided> - <why> - <cost if wrong>`. Example: `Ruling: coins cap at 99,999 - the UI fits 5 digits - raising it later needs a UI pass`. Ask the user only for anything irreversible, security or data loss, spending, publishing, or a plan that cannot work. A ruling can be overturned in one line; a stalled worker cannot.

## DONE WHEN is one checkable line
Each brief carries ONE first DONE WHEN line that a command can prove, plus "print the evidence command output in CRITERIA". Shape: `<command>` prints `<expected text or exit code>`. Why: a long run is judged from what is printed in its transcript, so a done condition that is only a feeling cannot end correctly. More checks may follow as extra numbered lines, but the first line decides done. Example: `lune run tests/Shop.test.luau` prints `ALL PASS` and exits 0. A vague line ("shop works well") is rewritten before the brief is sent.

## Review order
Fresh worker per task with a brief built for it (no inherited history). The critic judges SPEC COMPLIANCE first: every acceptance line met, with evidence. Only then style, naming and polish. Style never lifts a failed spec check, and a style finding never blocks a spec pass.
