---
tags: [moc]
---
# Source: davila7

License: MIT. 13 items. Back: [[_Home]]

## SOURCE.md

# SOURCE: davila7

- Origin: https://github.com/davila7/claude-code-templates
- Commit: f57964ebda91cdfb31755661ecea9395f30020f1
- License: MIT
- Imported: 2026-10-29 (batch B)
- Skills imported: 892 (quarantined: 14)
- Agents imported: 419 (quarantined: 1)
- Duplicates skipped (identical content hash to a file already imported in this batch, incl. mirrors): 10
- Skipped (not importable): 2

## What was copied
Only skill folders (SKILL.md plus beside-it assets; executable binaries and files over 5 MB excluded) and agent .md files. Upstream sub-structure preserved under skills/ and agents/ with the generic path components `skills`, `agents`, `plugins`, `.github`, `cli-tool`, `components` removed from the middle of paths. READMEs, docs, tests, commands, hooks, MCP config and mirror copies (.gemini, .codex, .agents, translations) were not copied.
Items whose scan hits were reviewed by hand and judged benign (documented prompt-injection examples, detection signatures, forensic paths, honeytoken/OOB tooling names, data blobs) were kept; test/ tests/ fixtures/ folders inside skills were not copied. Items with pipe-to-shell install instructions (curl|sh from vendor hosts) were quarantined per policy.

## Modifications
- Line endings normalised to LF in copied text files of types md/txt/py/sh/json/yaml/js/ts.
- added model: sonnet: 337 items
- description single-lined: 250 items
- clipped description: 242 items
- model mapped: 6 items

## Quarantined (15)
Moved to `_quarantine/` (not indexed). See each QUARANTINE note.
- skill skills/ai-research/fine-tuning-axolotl : pipeshell
- skill skills/ai-research/fine-tuning-unsloth : pipeshell
- skill skills/ai-research/infrastructure-lambda-labs : pipeshell
- skill skills/database/using-neon : pipeshell
- skill skills/development/bun-development : pipeshell
- skill skills/development/cloudflare-deploy : pipeshell
- skill skills/development/environment-setup-guide : pipeshell
- skill skills/development/render-deploy : pipeshell
- skill skills/scientific/alphafold-database : pipeshell
- skill skills/scientific/clinvar-database : pipeshell
- skill skills/scientific/denario : pipeshell
- skill skills/security/cloud-penetration-testing : pipeshell
- skill skills/security/linux-privilege-escalation : pipeshell
- skill skills/workflow-automation/gitops-workflow : pipeshell
- agent agents/expert-advisors/droid.md : pipeshell

## Skipped (2)
- skill .claude-plugin/skills/owasp-security : outside cli-tool/components/skills/
- agent cli-tool/components/agents/deep-research-team/agent-overview.md : no frontmatter

## Deduped against earlier imports in this batch (10)
- cli-tool/components/skills/development/dispatching-parallel-agents == davila7:cli-tool/components/skills/ai-research/dispatching-parallel-agents
- cli-tool/components/skills/development/subagent-driven-development == davila7:cli-tool/components/skills/ai-research/subagent-driven-development
- cli-tool/components/skills/enterprise-communication/slack-gif-creat

## Items

- [[S--davila7--2d-games|davila7/2d-games]]
- [[A--davila7--3d-artist|davila7/3d-artist]]
- [[S--davila7--3d-games|davila7/3d-games]]
- [[S--davila7--develop-web-game|davila7/develop-web-game]]
- [[S--davila7--game-art|davila7/game-art]]
- [[S--davila7--game-audio|davila7/game-audio]]
- [[S--davila7--game-design|davila7/game-design]]
- [[S--davila7--mobile-games|davila7/mobile-games]]
- [[S--davila7--multiplayer|davila7/multiplayer]]
- [[S--davila7--pc-games|davila7/pc-games]]
- [[A--davila7--unity-game-developer|davila7/unity-game-developer]]
- [[A--davila7--unreal-engine-developer|davila7/unreal-engine-developer]]
- [[S--davila7--web-games|davila7/web-games]]
