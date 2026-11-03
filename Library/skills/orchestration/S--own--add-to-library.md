---
id: "add-to-library"
type: skill
category: "orchestration"
source: "own"
license: "first-party"
repo_path: "skills/orchestration/add-to-library/SKILL.md"
description: "Step-by-step for adding or updating an agent preset or skill in claude-library, rebuilding the index and committing."
orig_name: "add-to-library"
tags: [lib/skill, cat/orchestration, src/own]
---

# add-to-library

> Step-by-step for adding or updating an agent preset or skill in claude-library, rebuilding the index and committing.

Type: skill | Category: [[categories/cat-orchestration|orchestration]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/orchestration/add-to-library/SKILL.md` (extra files, if any, sit beside it in the repo)

---
# Add an item to the library

Root: ~\claude-library (private repo romangigliotti123-arch/claude-library).

Skill: create `skills\<category>\<skill-name>\SKILL.md`
```
---
name: skill-name            # lowercase-hyphen, unique, equals the folder name
description: One line saying what it does and when to use it
---
# Title
Instructions...
```
Extra files (scripts, templates, references) go in the same folder and are referenced from SKILL.md.

Agent: create `agents\<category>\<agent-name>.md`
```
---
name: agent-name
description: One line use case
model: sonnet            # haiku | sonnet | opus
effort: high             # low | medium | high | xhigh
tools: Read, Grep, Bash  # optional; omit for all tools
---
System prompt / brief header...

(end with the standard RESULT/DONE/VERIFIED/PROBLEMS/NEEDS/NEXT/ARTIFACTS report format)
```

Rules:
- `description` must be ONE line (no line breaks). Quote it if it contains a colon.
- Category must be an existing folder under skills\ / agents\; create a new category only if 3+ items would live there.
- Names are unique across the library; run the build to check.
- No secrets, tokens, or personal data in any file.
- Third-party content goes under `sources\<name>\` with LICENSE + SOURCE.md instead (see README).

Then:
```
powershell -File ~\claude-library\tools\build-index.ps1     # must end with errors=0
powershell -File ~\claude-library\tools\find.ps1 "<name>"   # confirm it is found
git -C ~\claude-library add -A
git -C ~\claude-library commit -m "Add <name>" -m "Co-Authored-By: Claude Sonnet 5.5 <[email]>"
git -C ~\claude-library push
```
