---
id: "roblox-brain/roblox-security"
type: skill
category: "src-roblox-brain"
source: "roblox-brain"
license: "MIT"
repo_path: "sources/roblox-brain/skills/core/roblox-security/SKILL.md"
description: "Use when auditing or hardening Roblox code against exploits: authority, remotes, economy, purchases, and DataStore flows."
orig_name: "roblox-security"
orig_when_to_use: "Also for security reviews, cheaters or exploiters, duplicated items or currency, trusting client values, admin commands, and pre-release audits."
orig_last_reviewed: "2026-10-14"
alternatives: ["roblox-skills-el4cteo: roblox-skills-el4cteo/roblox-security"]
tags: [lib/skill, cat/src-roblox-brain, src/roblox-brain]
---

# roblox-brain/roblox-security

> Use when auditing or hardening Roblox code against exploits: authority, remotes, economy, purchases, and DataStore flows.

Type: skill | Category: [[categories/cat-src-roblox-brain|src-roblox-brain]] | Source: [[sources/src-roblox-brain|roblox-brain]] | License: MIT
Repo file: `sources/roblox-brain/skills/core/roblox-security/SKILL.md` (extra files, if any, sit beside it in the repo)

---
# Roblox Security

## When to Load

Load for authority, remote abuse, economy, saves, bans, or sandboxing audits. Remote validation/rate limits: `roblox-networking`.

## Quick Reference

**Core:** Client is always compromised. The server remains the source of truth, but the implementation depends on the authority model.

### Authority Models

- **Classic replication:** validate client requests against server state. Never trust client damage, currency, inventory, permissions, or positions.
- **Server Authority:** `Workspace.AuthorityMode = Server`: the server owns core simulation while clients predict and recover from misprediction. Use `BindToSimulation()` (needs `UseFixedSimulation`), not blanket `Heartbeat` correction. Cheap for stock characters, rewrite-scale for authored simulation (full.md).
- **Both:** validate attacks, purchases, teleports, permissions, and custom remotes at the server boundary.

### Audit Checklist

**CRITICAL:** Server-authoritative state · Documented authority model · Validate all arg types · Rate limit remotes · Session-lock DataStore · No client currency mutations · ProcessReceipt verification · No secrets in client code

**HIGH:** Validate custom movement and action transitions · BindToClose protection · Atomic trading · Never trust client values · Use InputActions for simulation input in Server Authority projects · Validate ProximityPrompt/ClickDetector/DragDetector like remotes

**MEDIUM:** Server cooldowns · server-computed leaderboards · anti-AFK reward checks · TextService filtering · Script sandboxing for third-party code

### Enforcement

Enforcement is a product decision with appeal implications. `Players:BanAsync`/`UnbanAsync` are server-only and need `Players.BanningEnabled`; `pcall` them. Duration, reason limits and device blocks: full.md.

### Anti-Patterns

Don't obfuscate client code, use `_G` for security, kick without logging, over-validate movement, or rely on client anti-cheat.

See `references/full.md` for detailed examples.

---

## Alternatives (same name, not shown in this vault)

This note is the best of 2 items called `roblox-security`. The others stay in the claude-library repo (open the repo file if this one does not fit):

- `roblox-skills-el4cteo`: roblox-skills-el4cteo/roblox-security - Anti-exploit design - never trust the client, validate every remote argument (NaN, spoofed instances, strings), rate limiting, ProximityPro... (repo file `sources/roblox-skills-el4cteo/skills/roblox-security/SKILL.md`)

