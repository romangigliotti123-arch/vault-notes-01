---
tags: [moc]
---
# Source: agency-agents

License: MIT. 18 items. Back: [[_Home]]

## SOURCE.md

# SOURCE: agency-agents

- Origin: https://github.com/msitarzewski/agency-agents
- Commit: b37b5bb33b78f2c1d6567d98e25ca818e3259219
- License: MIT
- Imported: 2026-10-29 (batch B)
- Skills imported: 0 (quarantined: 0)
- Agents imported: 283 (quarantined: 0)
- Duplicates skipped (identical content hash to a file already imported in this batch, incl. mirrors): 0
- Skipped (not importable): 16

## What was copied
Only skill folders (SKILL.md plus beside-it assets; executable binaries and files over 5 MB excluded) and agent .md files. Upstream sub-structure preserved under skills/ and agents/ with the generic path components `skills`, `agents`, `plugins`, `.github`, `cli-tool`, `components` removed from the middle of paths. READMEs, docs, tests, commands, hooks, MCP config and mirror copies (.gemini, .codex, .agents, translations) were not copied.
Items whose scan hits were reviewed by hand and judged benign (documented prompt-injection examples, detection signatures, forensic paths, honeytoken/OOB tooling names, data blobs) were kept; test/ tests/ fixtures/ folders inside skills were not copied. Items with pipe-to-shell install instructions (curl|sh from vendor hosts) were quarantined per policy.

## Modifications
- Line endings normalised to LF in copied text files of types md/txt/py/sh/json/yaml/js/ts.
- added model: sonnet: 283 items
- description single-lined: 5 items
- clipped description: 2 items

## Quarantined (0)
Moved to `_quarantine/` (not indexed). See each QUARANTINE note.

## Skipped (16)
- agent strategy/EXECUTIVE-BRIEF.md : no frontmatter
- agent strategy/QUICKSTART.md : no frontmatter
- agent strategy/nexus-strategy.md : no frontmatter
- agent strategy/coordination/agent-activation-prompts.md : no frontmatter
- agent strategy/coordination/handoff-templates.md : no frontmatter
- agent strategy/playbooks/phase-0-discovery.md : no frontmatter
- agent strategy/playbooks/phase-1-strategy.md : no frontmatter
- agent strategy/playbooks/phase-2-foundation.md : no frontmatter
- agent strategy/playbooks/phase-3-build.md : no frontmatter
- agent strategy/playbooks/phase-4-hardening.md : no frontmatter
- agent strategy/playbooks/phase-5-launch.md : no frontmatter
- agent strategy/playbooks/phase-6-operate.md : no frontmatter
- agent strategy/runbooks/scenario-enterprise-feature.md : no frontmatter
- agent strategy/runbooks/scenario-incident-response.md : no frontmatter
- agent strategy/runbooks/scenario-marketing-campaign.md : no frontmatter
- agent strategy/runbooks/scenario-startup-mvp.md : no frontmatter

## Deduped against earlier imports in this batch (0)

## Second-pass scan (2026-10-29, tools\scan.ps1 -Source agency-agents)

1 items flagged by the rule set (inject/pipesh/b64/upload/creds/binary) and hand-reviewed: 1 kept (documentation of attacks or defences, detection signatures, placeholder/OOB hostnames, safety-guard flags, JSON-parsing pipes such as curl|python3 -m json.tool, genetic sequences or icon data matched as base64), 0 quara

## Items

- [[A--agency-agents--Blender-Add-on-Engineer|agency-agents/Blender Add-on Engineer]]
- [[A--agency-agents--Game-Audio-Engineer|agency-agents/Game Audio Engineer]]
- [[A--agency-agents--Godot-Gameplay-Scripter|agency-agents/Godot Gameplay Scripter]]
- [[A--agency-agents--Godot-Multiplayer-Engineer|agency-agents/Godot Multiplayer Engineer]]
- [[A--agency-agents--Godot-Shader-Developer|agency-agents/Godot Shader Developer]]
- [[A--agency-agents--Level-Designer|agency-agents/Level Designer]]
- [[A--agency-agents--Narrative-Designer|agency-agents/Narrative Designer]]
- [[A--agency-agents--Roblox-Avatar-Creator|agency-agents/Roblox Avatar Creator]]
- [[A--agency-agents--Roblox-Experience-Designer|agency-agents/Roblox Experience Designer]]
- [[A--agency-agents--Roblox-Systems-Scripter|agency-agents/Roblox Systems Scripter]]
- [[A--agency-agents--Unity-Architect|agency-agents/Unity Architect]]
- [[A--agency-agents--Unity-Editor-Tool-Developer|agency-agents/Unity Editor Tool Developer]]
- [[A--agency-agents--Unity-Multiplayer-Engineer|agency-agents/Unity Multiplayer Engineer]]
- [[A--agency-agents--Unity-Shader-Graph-Artist|agency-agents/Unity Shader Graph Artist]]
- [[A--agency-agents--Unreal-Multiplayer-Architect|agency-agents/Unreal Multiplayer Architect]]
- [[A--agency-agents--Unreal-Systems-Engineer|agency-agents/Unreal Systems Engineer]]
- [[A--agency-agents--Unreal-Technical-Artist|agency-agents/Unreal Technical Artist]]
- [[A--agency-agents--Unreal-World-Builder|agency-agents/Unreal World Builder]]
