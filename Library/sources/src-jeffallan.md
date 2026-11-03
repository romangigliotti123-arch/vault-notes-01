---
tags: [moc]
---
# Source: jeffallan

License: MIT. 1 items. Back: [[_Home]]

## SOURCE.md

# SOURCE: jeffallan

- Origin: https://github.com/Jeffallan/claude-skills
- Commit: 190e05a380b624187f5770451e1f41b9187cb63c
- License: MIT
- Imported: 2026-10-29 (batch B)
- Skills imported: 66 (quarantined: 1)
- Agents imported: 0 (quarantined: 0)
- Duplicates skipped (identical content hash to a file already imported in this batch, incl. mirrors): 0
- Skipped (not importable): 0

## What was copied
Only skill folders (SKILL.md plus beside-it assets; executable binaries and files over 5 MB excluded) and agent .md files. Upstream sub-structure preserved under skills/ and agents/ with the generic path components `skills`, `agents`, `plugins`, `.github`, `cli-tool`, `components` removed from the middle of paths. READMEs, docs, tests, commands, hooks, MCP config and mirror copies (.gemini, .codex, .agents, translations) were not copied.
Items whose scan hits were reviewed by hand and judged benign (documented prompt-injection examples, detection signatures, forensic paths, honeytoken/OOB tooling names, data blobs) were kept; test/ tests/ fixtures/ folders inside skills were not copied. Items with pipe-to-shell install instructions (curl|sh from vendor hosts) were quarantined per policy.

## Modifications
- Line endings normalised to LF in copied text files of types md/txt/py/sh/json/yaml/js/ts.
- clipped description: 20 items
- description single-lined: 20 items

## Quarantined (1)
Moved to `_quarantine/` (not indexed). See each QUARANTINE note.
- skill skills/kubernetes-specialist : pipeshell

## Skipped (0)

## Deduped against earlier imports in this batch (0)

## Second-pass scan (2026-10-29, tools\scan.ps1 -Source jeffallan)

2 items flagged by the rule set (inject/pipesh/b64/upload/creds/binary) and hand-reviewed: 2 kept (documentation of attacks or defences, detection signatures, placeholder/OOB hostnames, safety-guard flags, JSON-parsing pipes such as curl|python3 -m json.tool, genetic sequences or icon data matched as base64), 0 quarantined.

## Items

- [[S--jeffallan--game-developer|jeffallan/game-developer]]
