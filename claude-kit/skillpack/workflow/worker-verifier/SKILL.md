---
name: worker-verifier
description: "Verify an AI worker's report with cheap real checks before accepting it: well-formedness triage with reportcheck.py, then one re-run command per load-bearing claim (file exists, hash, lint, test), and a verdict of accept, spot-check or reject. Use on every worker or subagent report before you relay success or start dependent work."
category: workflow
tags: verify, report, claims, false success, spot check, evidence, worker, review, trust
kb: Manager/topic-report-formats-and-verification.md, Manager/topic-llm-judge-and-adversarial-verification.md, Manager/topic-multi-agent-failure-modes.md, Manager/src-advani-false-success.md, Roblox/roblox-kb/testing-debugging-and-qa.md, Mentor/Combined-Brain.md
related: ai-brief-writer, milestone-reviewer, playtest-evidence-logger, rbx-verifier, rbx-critic, regression-checklist-builder
---

# worker-verifier

A worker's report is a set of claims; this skill checks state, not narration. The kit agent `rbx-verifier` and the `rbx-critic` give an independent LLM verdict at stage gates; this is the cheap first layer you run yourself on every report, mostly with commands. It does not judge game quality (`rbx-critic`) or run milestone sign-off (`milestone-reviewer`).

## When to use
A worker returned `RESULT: done|partial`, or you are about to say "fixed" to the user. Not for: reports you wrote yourself with command output pasted in the same turn.

## Inputs (max 2)
1. The report text or file. 2. The brief it answered (default: `briefs/<job-id>.md`).

## Procedure
1. Save the report as `reports/<job-id>.md` and run `python worker-verifier/scripts/reportcheck.py reports/<job-id>.md --brief briefs/<job-id>.md --root <project>`. A REJECT line (met without evidence, criteria count not equal to DONE WHEN count, hash mismatch) ends here: re-brief or send it back with the exact gap.
2. Read the first sentence. A report that does not start with RESULT, or buries a failure, is a warning, not a verdict.
3. Run the printed CHECK lines yourself, one per load-bearing claim: the worker's own command, `git diff --stat` against the claimed CHANGES, `ls`/`sha256sum` on artifacts. Scale effort with irreversibility: deterministic checks on everything, expensive ones only for risky or unobservable work (a remote machine, a GUI, a long unattended run).
4. Compare the CHANGES list with `git status --short`: any file changed that is outside OWNS is a fence breach; any claimed file that does not exist is a false claim.
5. For `[untested]` items, decide whether you can run them (Studio MCP playtest) or leave them visible to the user; never promote them to met.
6. Write the verdict: ACCEPT (all re-runs matched), SPOT-CHECK-OK with the list not run, or REJECT with the mismatch. Log a mismatch as one line in `docs/worker-incidents.md` ("brief lacked X", "claimed Y, state showed Z").
7. Never use a second model reading the same narration as the check; if you need an LLM judge, give it the requirements and artifacts, fresh context, read-only, binary criteria; trust its FAIL more than its PASS.

## Studio MCP path
For Luau claims that need a run: `start_stop_play`, then `get_console_output` and quote the Output; `list_roblox_studios` first. Only one MCP job at a time.

## Fallback
`luau-check.sh`, `lune run`, `rojo build`, `git diff`, `sha256sum`. Claims that need Studio stay `untested` and are reported as such.

## Evidence
`Manager/topic-report-formats-and-verification.md` (claims need command and output; false success is common and sounds confident; mandatory not-checked field; check the diff before relaying), `Manager/topic-llm-judge-and-adversarial-verification.md` (verify state not narration; judges fail open; fresh-context read-only verifier), `Manager/topic-multi-agent-failure-modes.md` (done claims are the weakest link), `Manager/src-advani-false-success.md` (published false-success rates on benchmark agents), `Roblox/roblox-kb/testing-debugging-and-qa.md`.

## Output
`reports/<job-id>.verdict.md`: verdict, commands run with output excerpts, mismatches, items left unverified.

## Acceptance checks
- [ ] Executed: `python worker-verifier/scripts/reportcheck.py --selftest` prints `selftest ok`; the real report run prints a VERDICT line.
- [ ] At least one re-run command per [met] line that is irreversible or load-bearing was actually executed and its output quoted.
- [ ] `git status --short` compared with CHANGES.
- [ ] Verdict and any mismatch recorded.

## Pitfalls
Trusting tone. Checking only the files the worker mentions. A passing selftest or lint on code that was never run in the engine (say `checked, not run`). Letting the worker's own subagent count as independent.

## Related
`ai-brief-writer`, `milestone-reviewer`, `playtest-evidence-logger`, `rbx-critic`, `regression-checklist-builder`.
