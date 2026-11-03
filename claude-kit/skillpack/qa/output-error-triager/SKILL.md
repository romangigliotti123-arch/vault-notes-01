---
name: output-error-triager
description: "Read a pasted Output or Developer Console log and rank the errors and warnings by impact: group repeats, separate server from client, fold stack traces, call out spam, and name the first thing to fix. Use after any playtest, bug report or live error spike, before reading the log line by line."
category: qa
tags: output, error log, triage, stack trace, console, warnings, spam, developer console, debugging, rank errors
kb: Roblox/roblox-kb/testing-debugging-and-qa.md, Roblox/roblox-kb/scripting-and-performance.md, Roblox/roblox-kb/data-persistence.md, Roblox/roblox-kb/client-server-and-remotes.md
related: crash-log-reader, error-logger-builder, lag-hunter, playtest-bot-writer, bug-report-template, repro-step-writer
---

# output-error-triager

A playtest log has hundreds of lines and a handful of problems. `scripts/LogParse.luau` (tested) classifies each line as error, warning or info, notes server or client, folds stack-trace lines into the error above, groups repeats after normalising ids and counts, and ranks groups by a transparent score: weight (server error 3, client error 2, warning 0.5-0.75) times (1 + log2 of the count); groups seen 50+ times are marked SPAM. It reads text; it cannot say why something fails.

## When to use
After a playtest, a bug report with Output pasted, or a spike in live errors; before reading logs by hand. Not for: crashes and disconnects (`crash-log-reader`), building a logger (`error-logger-builder`), or performance (`lag-hunter`).

## Inputs (max 2)
1. The log text (paste or `get_console_output`), with client and server lines if possible. 2. What you were doing (default: unknown; the first group still ranks).

## Procedure
1. Collect: Studio MCP `get_console_output` after a full scenario (not mid-way), or paste from the Output window / Developer Console (F9 in a live session). Note blue client vs green server colouring is lost in text; the `- Server`/`- Client` suffix carries it. Stop if the log is empty and say how to capture it.
2. `LogParse.rank(LogParse.parse(log))` then `LogParse.report(groups, 10)`; read the top groups first. Errors with the same normalised text group together even when ids differ.
3. For each top group read its example: a script path and line (`Shop:31`), the message, and the side. Classify the cause: nil index (`attempt to index nil with ...`: missing `WaitForChild`, load order, or data not loaded), `not a valid member` (name or path typo, object missing), `Infinite yield possible` (path never resolves; check spelling and that the object replicates), require errors (cycle or error inside the module), DataStore throttle lines (saving too often), HTTP errors.
4. Fix top-down: one group at a time, replay the same scenario, re-run the triage and compare counts. Do not fix warnings before server errors.
5. Handle spam: a group with a high count is usually one bug in a loop; fix the cause, not the print. Throttle noisy logging with `error-logger-builder`.
6. File what you cannot fix now using `bug-report-template` with the group's example line as the Actual and `repro-step-writer` for steps.
7. Report the before/after table and any groups skipped, with reasons.

## Studio MCP path
`list_roblox_studios` -> `start_stop_play` -> run the scenario (`playtest-bot-writer` bot or `character_navigation`) -> `get_console_output` -> feed the text to `LogParse` via `execute_luau` (Edit) with the module pasted inline -> `script_read` the top script lines -> `multi_edit` -> repeat -> `start_stop_play` (stop).

## Fallback
Paste the log: `lune run ../skillpack/qa/output-error-triager/scripts/tests/LogParse.test.luau` from `claude-kit/systems` shows the parser; run `LogParse` over a saved text file in a scratch Lune script. Without a log, nothing can be ranked: ask for one.

## Evidence
`Roblox/roblox-kb/testing-debugging-and-qa.md`: keep Output open and click errors to jump to the line; read errors as path, line and message; "attempt to index nil" usually needs `WaitForChild` or a load-order fix; "Infinite yield possible" and "not a valid member" mean checking the require or object path and spelling; use print and warn deliberately and filter Output; open the Developer Console with F9 in a playtest; search the exact error text before asking. `Roblox/roblox-kb/data-persistence.md`: "request was added to queue" means saving too often. The score weights are this skill's heuristic.

## Output
```
LOG TRIAGE: N distinct problems
  1. [error server] xK score S (first at line L): <example>
fix order + cause class per group; before/after counts
```

## Acceptance checks
- [ ] `lune run` of the LogParse test prints "6 passed, 0 failed".
- [ ] The top group's example line and count are quoted from the real log.
- [ ] After a fix the same scenario was replayed and the group's count dropped to 0 (or the fix is marked untested).
- [ ] Server and client groups were not merged.
- [ ] Spam groups have a root-cause note, not just a silenced print.

## Pitfalls
Fixing the loudest line instead of the highest impact. Missing that a client error is the visible symptom of a server error. Stack lines treated as separate errors. Clearing the log between steps and losing the first error. Judging after a mid-scenario capture.

## Related
`crash-log-reader`, `error-logger-builder`, `lag-hunter`, `bug-report-template`, `repro-step-writer`.
