---
id: "library-search"
type: skill
category: "orchestration"
source: "own"
license: "first-party"
repo_path: "skills/orchestration/library-search/SKILL.md"
description: "How to browse the claude-library cheaply (names, then descriptions, then the file) and use a found agent or skill."
orig_name: "library-search"
tags: [lib/skill, cat/orchestration, src/own]
---

# library-search

> How to browse the claude-library cheaply (names, then descriptions, then the file) and use a found agent or skill.

Type: skill | Category: [[categories/cat-orchestration|orchestration]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/orchestration/library-search/SKILL.md` (extra files, if any, sit beside it in the repo)

Related: [[A--own--opus-builder]], [[A--own--sonnet-worker]], [[S--own--add-to-library]], [[S--own--worker-brief-template]]

---
# Using the library (progressive disclosure)

Root: ~\claude-library

1. Names first (cheapest): read `NAMES.txt` (names only), or run
   `powershell -File ~\claude-library\tools\find.ps1 "<words>" [-Type skill|agent] [-Top 6]`
   which prints a few `type | category | name | description` lines plus the file path.
2. Descriptions: `INDEX.md` has one line per item grouped by category (grep it: `Select-String -Path ...\INDEX.md -Pattern 'roblox'`).
3. Only then read the one or two files you actually need.

Using a skill: read its `SKILL.md` and follow it (extra files sit beside it). Using an agent preset: read the file; its body is the system prompt / brief header for a worker. Spawn the worker with the Agent tool (sonnet-worker or opus-builder, or a general agent), paste the preset body at the top of the brief, then add the job-specific brief (see worker-brief-template). Honor the preset's `model` and `effort`. Restricted `tools:` lines are advice for scoping.

Do not load many items "just in case"; each file read costs context. If nothing fits, use the closest preset or add one (add-to-library skill).
