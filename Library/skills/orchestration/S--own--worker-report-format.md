---
id: "worker-report-format"
type: skill
category: "orchestration"
source: "own"
license: "first-party"
repo_path: "skills/orchestration/worker-report-format/SKILL.md"
description: "The standard final-report format every worker returns (RESULT/DONE/VERIFIED/PROBLEMS/NEEDS/NEXT/ARTIFACTS) and how to read one."
orig_name: "worker-report-format"
tags: [lib/skill, cat/orchestration, src/own]
---

# worker-report-format

> The standard final-report format every worker returns (RESULT/DONE/VERIFIED/PROBLEMS/NEEDS/NEXT/ARTIFACTS) and how to read one.

Type: skill | Category: [[categories/cat-orchestration|orchestration]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/orchestration/worker-report-format/SKILL.md` (extra files, if any, sit beside it in the repo)

---
# Worker report format

Workers end with exactly this, nothing else after it:

```
RESULT: success | partial | failed
DONE: concrete actions in order, with exact paths, commands, versions, ports, IPs
VERIFIED: how it was confirmed, with the evidence (command + trimmed output)
PROBLEMS: errors, surprises, anything undone or blocked (or "none")
NEEDS: anything the user must do or approve (or "none")
NEXT: sensible follow-up steps
ARTIFACTS: absolute paths / URLs / IDs of everything produced, with counts (or "none")
```

Definitions:
- success = all of DONE criteria met and verified. partial = useful result but something is missing or unverified. failed = goal not achieved.
- VERIFIED must contain evidence from the worker's own checks. "Should work" is not verification.
- NEEDS lists blocked confirm-first actions and exactly which approval is required.

Reading a report as the manager: check RESULT, then spot-verify one or two VERIFIED claims yourself, then relay a short outcome to the user in your own words, naming which model did the work. Retry once with a better brief or escalate one model tier if partial/failed.
