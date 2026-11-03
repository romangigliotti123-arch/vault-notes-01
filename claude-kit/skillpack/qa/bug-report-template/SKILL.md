---
name: bug-report-template
description: "A bug report format that gets bugs fixed: title, expected vs actual, numbered repro steps, where it happens (server or client), build, frequency, device and evidence, with a lint that rejects reports a developer cannot act on. Use whenever a tester, player or agent files a bug, and as the output format of the QA skills."
category: qa
tags: bug report, template, expected actual, repro, issue, triage, qa, evidence, severity, ticket
kb: Roblox/roblox-kb/testing-debugging-and-qa.md, Roblox/roblox-kb/playtesting-and-feedback.md, Roblox/roblox-kb/scripting-and-performance.md, Mentor/Combined-Brain.md
related: repro-step-writer, output-error-triager, crash-log-reader, regression-checklist-builder, playtest-bot-writer, multiplayer-test-planner
---

# bug-report-template

A report is good when someone who has never seen the bug can reproduce it and know what "fixed" looks like. The format is short, fixed and lintable: `scripts/bug_report_lint.py` (self-tested) checks the required fields and exits 1 on a report that cannot be acted on. It does not judge whether the bug is real: reproduce first (`repro-step-writer`).

## When to use
Filing a bug from a playtest, a player message, an Output group (`output-error-triager`) or a crash read (`crash-log-reader`). Not for: feature requests, balance opinions, or vague "it feels bad" feedback (put those in `playtesting-and-feedback` notes).

## Inputs (max 2)
1. What you saw (default: the raw note or log line). 2. Build and device (default: ask once; if unknown write `unknown` and say what is missing).

## Procedure
1. Title: one line that names the system and the symptom ("Shop Buy button does nothing after respawn"), under 100 characters. Never "bug" or "broken".
2. Write the template below. Expected is the behaviour a player or the design promises; Actual is what happens, with the exact Output line if there is one, quoted.
3. Steps: numbered, each one action, starting from a known state (a fresh join is the best start); 2-10 steps; each under 200 characters. If you cannot reproduce it, say "seen once" in Frequency and attach everything you have.
4. Where: Server, Client or Both (Output colouring and the `- Server`/`- Client` suffix tell you; blue is client, green is server in Studio). Build: place version, date or commit. Frequency: always, N of M, intermittent, once. Device: platform, input, graphics, network.
5. Evidence: Output excerpt in a code block, a screenshot or short video file name, and the account type used (dev accounts can be exempt from checks).
6. Severity: S1 loses data or money or crashes; S2 blocks the core loop or a paid feature; S3 breaks a feature with a workaround; S4 cosmetic. State one line why.
7. Lint: `python scripts/bug_report_lint.py report.md`; fix every FAIL; WARN lines (device, evidence) are recommended. Exit 0 prints "ready to file".

```
# <System>: <symptom>
Severity: S2 (blocks the shop on phones)
## Expected
<what should happen>
## Actual
<what happens; Output line in a code block>
## Steps
1. Join the test place ...
2. ...
Where: Server | Client | Both     Build: place version 112     Frequency: 3 of 3
Device: Android phone, touch, low graphics, good network     Account: non-dev
Evidence: output.txt, shop-buy.png
```

## Studio MCP path
`get_console_output` for the exact Output lines and `screen_capture` for the picture while the bug is on screen; `get_studio_state` for the Studio/place state; attach nothing that contains secrets.

## Fallback
Plain Markdown in an issue tracker or `bugs/` folder; run `python scripts/bug_report_lint.py --selftest` to see a passing and a failing example. Without a build number or device, write `unknown`; the lint will flag it as unmet.

## Evidence
`Roblox/roblox-kb/testing-debugging-and-qa.md`: report bugs with expected vs actual behaviour or paste the Output, verify agent edits by playtest, use fresh-eyes testers and keep a folder of repros, search the exact error text first. `Roblox/roblox-kb/playtesting-and-feedback.md`: how to take structured feedback from testers. Severity levels are this skill's convention.

## Output
One Markdown file per bug (`bugs/<id>-<slug>.md`) following the template, plus the lint line `BUG REPORT: ready to file`.

## Acceptance checks
- [ ] `python scripts/bug_report_lint.py --selftest` prints "bug_report_lint selftest: ok".
- [ ] `python scripts/bug_report_lint.py report.md` exits 0 for the report (quoted).
- [ ] Expected and Actual are separate sections; Actual quotes the real Output line when one exists.
- [ ] Steps start from a known state and were followed once by someone (or the report says "not reproduced").
- [ ] No secret, key or personal data is in the report or attachments.

## Pitfalls
Mixing several bugs in one report. Writing the guessed cause as the Actual. "Sometimes" with no count. A screenshot with no steps. Testing on a dev account and not saying so. Pasting a whole 5,000-line log instead of the relevant group.

## Related
`repro-step-writer`, `output-error-triager`, `crash-log-reader`, `regression-checklist-builder`, `playtest-bot-writer`.
