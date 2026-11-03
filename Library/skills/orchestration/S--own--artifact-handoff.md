---
id: "artifact-handoff"
type: skill
category: "orchestration"
source: "own"
license: "first-party"
repo_path: "skills/orchestration/artifact-handoff/SKILL.md"
description: "Deliver long or visual results to Roman by publishing a private Artifact page or a file and sending only a short summary plus link."
orig_name: "artifact-handoff"
tags: [lib/skill, cat/orchestration, src/own]
---

# artifact-handoff

> Deliver long or visual results to Roman by publishing a private Artifact page or a file and sending only a short summary plus link.

Type: skill | Category: [[categories/cat-orchestration|orchestration]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/orchestration/artifact-handoff/SKILL.md` (extra files, if any, sit beside it in the repo)

---
# Artifact / file handoff

Roman reads on a phone. Long output does not go in chat.

- Text report, table, plan: write to a file (absolute path) and reply with a 3-line summary + the path. If it is meant to be shared or reviewed by others, publish it as a private Artifact (HTML, load the artifact-design skill first; the page is private by default) and give the link.
- Visual/interactive result (dashboard, prototype, explainer): publish as an Artifact with `capabilities` only if needed.
- Screenshots: save to the host's temp screenshot folder only; keep one via `save-screenshot.ps1 -Reason` if it is genuine evidence.
- Never publish pages containing secrets, credentials or Roman's private data; never make a repo or page public without approval.
- In the final worker report, put the paths/URLs in ARTIFACTS so the manager can relay them.
