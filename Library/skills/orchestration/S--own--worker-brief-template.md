---
id: "worker-brief-template"
type: skill
category: "orchestration"
source: "own"
license: "first-party"
repo_path: "skills/orchestration/worker-brief-template/SKILL.md"
description: "Template and rules for writing a self-contained AI-to-AI brief for a worker agent; use before delegating any job."
orig_name: "worker-brief-template"
tags: [lib/skill, cat/orchestration, src/own]
---

# worker-brief-template

> Template and rules for writing a self-contained AI-to-AI brief for a worker agent; use before delegating any job.

Type: skill | Category: [[categories/cat-orchestration|orchestration]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/orchestration/worker-brief-template/SKILL.md` (extra files, if any, sit beside it in the repo)

Related: [[S--own--worker-report-format]]

---
# Worker brief template

A worker knows nothing except the brief. Write it as AI to AI: literal, dense, no pleasantries.

```
ROLE: <library agent name or role, e.g. security-auditor>  (model: <haiku|sonnet|opus>, effort: <low|medium|high|xhigh>)
GOAL: <one sentence outcome>
CONTEXT: <exact hosts/IPs, absolute paths, versions, accounts, what is already done, what is ruled out, links to read first>
STEPS (optional): <only if order matters or you know the approach>
CONSTRAINTS: <what not to touch; confirm-first rules (no deleting non-temp data, no spending, no sending/posting as the user, no security/credential/firewall/remote-access changes, nothing published externally); commit message trailer; privacy defaults such as private repos>
DONE = <observable acceptance checks the worker must run and show>
REPORT BACK: RESULT / DONE / VERIFIED / PROBLEMS / NEEDS / NEXT / ARTIFACTS
```

Rules:
1. Include every fact the worker needs; point to files instead of pasting large text.
2. State the definition of done as checks, not intentions ("`find.ps1 review` prints 3+ hits", not "search works").
3. Say what is out of scope. Name files/directories the worker may modify.
4. Pick the cheapest model that fits: haiku = lookups/status; sonnet = default real work; opus = whole apps, hard architecture, or after a sonnet failure.
5. One brief = one job. Independent jobs go to parallel workers with disjoint files.
6. Paste the report format from the worker-report-format skill, or let the agent preset's footer carry it.
7. Never put secrets in the brief; say where the worker finds them (e.g. "gh is already authenticated").
8. After the report comes back, verify it (the `verifier` agent or your own commands) before telling the user it worked.
