---
tags: [moc]
---
# Source: awesome-copilot

License: MIT. 1 items. Back: [[_Home]]

## SOURCE.md

# SOURCE: awesome-copilot

- Origin: https://github.com/github/awesome-copilot
- Commit: 0fe6545b950671641b2b14b44eb56678fea6c6b4
- License: MIT
- Imported: 2026-10-29 (batch B)
- Skills imported: 462 (quarantined: 3)
- Agents imported: 221 (quarantined: 1)
- Duplicates skipped (identical content hash to a file already imported in this batch, incl. mirrors): 0
- Skipped (not importable): 0

## What was copied
Only skill folders (SKILL.md plus beside-it assets; executable binaries and files over 5 MB excluded) and agent .md files. Upstream sub-structure preserved under skills/ and agents/ with the generic path components `skills`, `agents`, `plugins`, `.github`, `cli-tool`, `components` removed from the middle of paths. READMEs, docs, tests, commands, hooks, MCP config and mirror copies (.gemini, .codex, .agents, translations) were not copied.
Items whose scan hits were reviewed by hand and judged benign (documented prompt-injection examples, detection signatures, forensic paths, honeytoken/OOB tooling names, data blobs) were kept; test/ tests/ fixtures/ folders inside skills were not copied. Items with pipe-to-shell install instructions (curl|sh from vendor hosts) were quarantined per policy.

## Modifications
- Line endings normalised to LF in copied text files of types md/txt/py/sh/json/yaml/js/ts.
- frontmatter converted to name/description/model (dropped tools etc.): 222 items
- description single-lined: 88 items
- model mapped: 81 items
- clipped description: 79 items
- derived description: 1 items

## Quarantined (4)
Moved to `_quarantine/` (not indexed). See each QUARANTINE note.
- skill skills/aspire : pipeshell
- skill skills/azure-container-registry-cli : pipeshell
- skill skills/azure-devops-cli : pipeshell
- agent agents/droid.md : pipeshell

## Skipped (0)

## Deduped against earlier imports in this batch (0)

## Second-pass scan (2026-10-29, tools\scan.ps1 -Source awesome-copilot)

7 items flagged by the rule set (inject/pipesh/b64/upload/creds/binary) and hand-reviewed: 6 kept (documentation of attacks or defences, detection signatures, placeholder/OOB hostnames, safety-guard flags, JSON-parsing pipes such as curl|python3 -m json.tool, genetic sequences or icon data matched as base64), 1 quarantined. Quarantined: skills/anti-ui-slop (vendor promo skill for a paid external MCP whose reference policy tells the agent to never tell the user when evidence was missing/rejected, i.e. instructs concealment from the user).


## Items

- [[S--awesome-copilot--game-engine|awesome-copilot/game-engine]]
