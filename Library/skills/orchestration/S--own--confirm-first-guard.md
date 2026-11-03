---
id: "confirm-first-guard"
type: skill
category: "orchestration"
source: "own"
license: "first-party"
repo_path: "skills/orchestration/confirm-first-guard/SKILL.md"
description: "PreToolUse guard hook that makes the 'Always confirm first' list mechanical (publish, send-as-user, security/firewall, destructive deletes, credential reads, self-modification of manager config); includes a tested PowerShell script and the settings snippet. Not installed until Roman approves."
orig_name: "confirm-first-guard"
tags: [lib/skill, cat/orchestration, src/own]
---

# confirm-first-guard

> PreToolUse guard hook that makes the 'Always confirm first' list mechanical (publish, send-as-user, security/firewall, destructive deletes, credential reads, self-modification of manager config); includes a tested PowerShell script and the settings snippet. Not installed until Roman approves.

Type: skill | Category: [[categories/cat-orchestration|orchestration]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/orchestration/confirm-first-guard/SKILL.md` (extra files, if any, sit beside it in the repo)

---
# Confirm-first guard (mechanical version of CLAUDE.md's "Always confirm first")

Prose rules are advisory and are lost at compaction; hooks and deny/ask rules bind the main agent AND subagents even under `bypassPermissions`. Tested 2026-10-29 on Claude Code 2.1.312 (haiku-5-5, `-p`): `permissions.ask` and `permissions.deny` rules and a `PreToolUse` hook exiting 2 each stopped the tool call directly and via a subagent; hook stderr reached the model. NOT tested: whether a hook `ask` decision renders as a phone prompt over Remote Control. Evidence base: manager-kb `topic-agent-security`.

Honest limits: pattern guards are speed bumps, not walls (`git -C . push`, `sh -c`, LOLBAS tricks); the real boundaries are credential isolation, egress control and not mixing untrusted input with powerful tools in one session (Rule of Two). Native Windows has no Claude Code sandbox.

## Files
`scripts/confirm-first-guard.ps1` (tested with sample inputs: push/delete/netsh/secrets => ask JSON; writes to the manager config => exit 2; harmless commands and unparseable input => exit 0, fail-open).

## Settings snippet (user `~/.claude/settings.json`; propose to Roman, then test in a scratch session with `claude -p --settings <file>` first)
```json
"hooks": { "PreToolUse": [ { "matcher": "Bash|PowerShell|Write|Edit|NotebookEdit",
  "hooks": [ { "type": "command", "shell": "powershell",
    "command": "powershell -NoProfile -ExecutionPolicy Bypass -File ~/claude-host/tools/confirm-first-guard.ps1" } ] } ] }
```
Add `"onFailure": "block"` only after the script has run cleanly for a while (a crashed hook would then block every tool call). Complement with `permissions.deny` for config files and `permissions.ask` for `git push`/`gh repo`/`gh release` (simple patterns need no code).

## Behaviour contract for workers
An `ask` in a headless worker is refused: the worker must stop that step and report it under NEEDS with the exact action. Roman's approval is passed in the next brief by quoting his words and the literal command; do not forward approval by SendMessage.

Changing hooks or permissions is a security-settings change: confirm with Roman before installing.
