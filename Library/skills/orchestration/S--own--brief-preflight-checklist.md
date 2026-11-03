---
id: "brief-preflight-checklist"
type: skill
category: "orchestration"
source: "own"
license: "first-party"
repo_path: "skills/orchestration/brief-preflight-checklist/SKILL.md"
description: "Use before every Agent/worker spawn or remote claude -p run: the 6-block brief template (context, task, scope, done-when, budget, report) plus a 12-item pre-send checklist; catches the gaps that cause partial or fabricated worker results."
orig_name: "brief-preflight-checklist"
tags: [lib/skill, cat/orchestration, src/own]
---

# brief-preflight-checklist

> Use before every Agent/worker spawn or remote claude -p run: the 6-block brief template (context, task, scope, done-when, budget, report) plus a 12-item pre-send checklist; catches the gaps that cause partial or fabricated worker results.

Type: skill | Category: [[categories/cat-orchestration|orchestration]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/orchestration/brief-preflight-checklist/SKILL.md` (extra files, if any, sit beside it in the repo)

Related: [[A--own--haiku-scout]], [[A--own--opus-builder]], [[A--own--sonnet-worker]], [[S--own--model-routing]], [[S--own--worker-report-format-v2]]

---
# Brief pre-flight (manager side)

A worker knows only the brief. A brief a smart new colleague could not act on without asking will fail. Dense, not terse. Evidence base: manager-kb `topic-brief-prompt-engineering`, `topic-multi-agent-failure-modes`, `topic-anthropic-agent-guidance`.

## Template (AI to AI, no pleasantries, no SHOUTING; give the reason instead)
```
CONTEXT: goal in one sentence; why / for whom; what is done or ruled out (label guesses HYPOTHESIS);
         hosts, absolute paths to read (never paste long content), versions, who else is changing what.
TASK:    one core objective. Type: research | build | diagnose | verify | operate.
         Investigations: the question. Lookups: the exact command.
SCOPE:   may touch: ... | must not touch: ... | confirm-first list (quote it) | subagents: not allowed unless stated
         If blocked or impossible: finish everything else and say exactly what you left out. Never fill a gap with a guess.
DONE WHEN: observable criteria, each with the check that proves it (command + expected output). Hand over the whole task with a finish line: "continue until every item passes; do not stop at a progress report". A loop's stop is a metric ("until X equals Y"), never "until satisfied", plus a max-iteration cap (manager-kb takeaways 23, 46, 48: Nate Herk, RoboNuggets; Anthropic Opus 5.5 prompting guide).
BUDGET:  expected size; stop rule: same error twice, or 2x the estimate -> stop and report PARTIAL.
         Jobs over ~20 min: write progress to ~\claude-host\jobs\<slug>\progress.md after each phase.
REPORT:  the report format in the agent file (or worker-report-format-v2); <= 350 words; bulky output in files, absolute paths listed.
TRUST:   which of {untrusted input, host secrets, external actions} this worker may touch (never all three at once).
```
Pick model/effort per job (see `model-routing`): haiku-scout for read-only lookups; sonnet-worker medium for clear-spec work, high for verification-critical work; opus-builder only for hard builds or after sonnet failed with a correct brief.

## Pre-send checklist (answer silently; fix any "no")
1. Could a colleague with zero context do this from the brief alone?
2. Is the goal one objective, with the reason stated?
3. Did I synthesize first? (No "based on your findings, fix it": give file:line and the cause.)
4. Is everything already known or ruled out stated, so nothing is rediscovered?
5. Are paths/hosts/versions exact and absolute?
6. Is every DONE WHEN item checkable, with the check named, and does any loop in the brief have a metric stop and an iteration cap?
7. Is scope fenced (touch / do not touch / no unrequested extras, list suggestions instead)?
8. Is there an honest exit (blocked => say so, finish the rest)?
9. Is there a stop rule and a size/time estimate?
10. Is the confirm-first list quoted, with the TRUST line set?
11. Is the library lookup done (PICKS/find.ps1) and the chosen preset named, or "none fits"?
12. Is it the right model/effort, and is another worker already writing the same files?

High-stakes, remote, destructive or Opus-builder jobs: write the checklist answers in two lines each before sending. Routine jobs: skip the write-up, keep the habit.

## After the report
If the job came back partial/failed: add one line to `~\claude-host\brief-lessons.md` (`[job type] symptom -> what the brief lacked -> new rule`, newest first, max 30 lines) and fold repeated lessons into this template.
