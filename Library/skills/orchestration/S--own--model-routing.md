---
id: "model-routing"
type: skill
category: "orchestration"
source: "own"
license: "first-party"
repo_path: "skills/orchestration/model-routing/SKILL.md"
description: "Decision rules for choosing haiku, sonnet or opus and the effort level for a delegated job."
orig_name: "model-routing"
tags: [lib/skill, cat/orchestration, src/own]
---

# model-routing

> Decision rules for choosing haiku, sonnet or opus and the effort level for a delegated job.

Type: skill | Category: [[categories/cat-orchestration|orchestration]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/orchestration/model-routing/SKILL.md` (extra files, if any, sit beside it in the repo)

---
# Model and effort routing

- haiku (effort low-medium): status checks, reading files/logs, simple lookups, small one-step commands, dependency inventories, relaying results.
- sonnet (effort high default): any real job - multi-step setup, debugging, scripting, research, remote-machine work, reviews, docs, tests. Default when unsure.
- opus (effort high; xhigh/max only for genuinely hard problems): building a whole app/game, large multi-file builds, hard architecture, or when sonnet already tried and failed. Never for installs, setup, lookups.

Effort: low/medium for repetitive or well-specified work (thinking longer wastes money); high default; xhigh/max rarely.

Escalation: partial/failed with a sound brief -> retry once with a sharper brief on the same tier, then move up one tier. If the failure is a missing fact, fix the brief, not the model.
Parallelism: independent jobs with disjoint files run concurrently, each on its own right-sized model.
Cost sense: a subagent costs more than it looks (briefing + report handoff). Do trivial checks inline.
