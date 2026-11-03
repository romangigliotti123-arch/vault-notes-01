---
id: "roblox-skills-ashexplained/setup-roblox-skills"
type: skill
category: "src-roblox-skills-ashexplained"
source: "roblox-skills-ashexplained"
license: "MIT"
repo_path: "sources/roblox-skills-ashexplained/skills/setup-roblox-skills/SKILL.md"
description: "Bootstrap the Roblox skill pack in a game project by injecting a `## Roblox Skills` block into CLAUDE.md — the full game-development lifecycle map, every skill's purpose, use case, and trigger words, and the next-skill routing so each skill ends by telling the user what to run next. Also records the project's tracker (GitHub issues or local roadmap), triage labels, and UI design artifact layout. Run once when setting up a Roblox project, or if the skills seem to be missing lifecycle, tracker, label, or routing context."
orig_name: "setup-roblox-skills"
orig_disable_model_invocation: "true"
tags: [lib/skill, cat/src-roblox-skills-ashexplained, src/roblox-skills-ashexplained]
---

# roblox-skills-ashexplained/setup-roblox-skills

> Bootstrap the Roblox skill pack in a game project by injecting a `## Roblox Skills` block into CLAUDE.md — the full game-development lifecycle map, every skill's purpose, use case, and trigger words, and the next-skill routing so each skill ends by telling the user what to run next. Also records the project's tracker (GitHub issues or local roadmap), triage labels, and UI design artifact layout. Run once when setting up a Roblox project, or if the skills seem to be missing lifecycle, tracker, label, or routing context.

Type: skill | Category: [[categories/cat-src-roblox-skills-ashexplained|src-roblox-skills-ashexplained]] | Source: [[sources/src-roblox-skills-ashexplained|roblox-skills-ashexplained]] | License: MIT
Repo file: `sources/roblox-skills-ashexplained/skills/setup-roblox-skills/SKILL.md` (extra files, if any, sit beside it in the repo)

Related: [[S--roblox-skills-ashexplained--roblox-game-development-lifecycle]], [[S--roblox-skills-ashexplained--roblox-game-ux]], [[S--roblox-skills-ashexplained--roblox-to-issues]], [[S--roblox-skills-ashexplained--roblox-triage]]

---
# Setup Roblox Skills

Wire the Roblox skill pack into a specific game project so every skill knows the lifecycle, its neighbors, and where this project tracks work — and so **each skill ends by suggesting what to run next.**

This is a prompt-driven skill, not a script. Explore, ask a few short questions, confirm, then write.

**The tracker is for planning, not code.** The game's Luau code and instances live in the Roblox cloud experience and are edited through Studio MCP (`roblox-studio-workflow`) — never committed to Git. Git / the tracker holds only planning artifacts: `ROADMAP.md`, PRDs, slices, and UI design briefs. Make this explicit when setting up.

## What it writes

1. A **`## Roblox Skills`** block in the project's `CLAUDE.md`, containing:
   - the game-development **lifecycle map** (phases → which skills run in each),
   - the **skill catalog** — every skill's one-line purpose, *use when*, and *trigger words*,
   - the **next-skill routing** convention: at the end of any skill, tell the user which skill to run next.
   The canonical block is [claude-block.md](claude-block.md) — inject it verbatim (trimming any skill folders this project doesn't have installed).
2. `docs/agents/` config files: the tracker, the triage labels, and the UI design artifact layout.

## Process

### 1. Explore

Read what already exists — don't assume:

- `git remote -v` — is this game project a GitHub repo?
- `CLAUDE.md` at the root — does it exist? Is there already a `## Roblox Skills` block?
- `ROADMAP.md`, `roadmap/`, `.roblox/` — is a local roadmap/tracker convention already in use?
- `docs/agents/` — did a prior run already write config?
- `design/` — do any UI design briefs already exist?

### 2. Ask (one at a time)

Assume the user may be new to this. Give a one-line explainer, then the choices and the default.

**A — Where is work tracked?** Slices from `roblox-to-issues` and bugs from `roblox-triage` need a home.

- **Local roadmap (default, Studio-first)** — `ROADMAP.md` as the index plus markdown files under `roadmap/<feature-slug>/`. Best for solo devs working in Studio without a Git remote. Seed from [tracker-local.md](tracker-local.md).
- **GitHub issues** — issues live in the project's GitHub repo via the `gh` CLI. Propose this if a GitHub remote exists. Seed from [tracker-github.md](tracker-github.md).
- **Other** (Trello, Notion, etc.) — the user describes it in a sentence; record as prose.

**B — Triage labels.** The five canonical states (`needs-triage`, `needs-info`, `ready-to-build`, `needs-human`, `wontfix`) plus categories (`bug`, `enhancement`). Defaults equal their names; ask only if the user already uses different strings. Seed from [triage-labels.md](triage-labels.md).

**C — UI design artifacts.** UI slices can't be built until an approved design brief exists (see `roblox-game-ux`). Confirm the layout (default: markdown briefs under `design/features/<feature-slug>/`, optionally with reference images/screenshots — Roblox UI is built in Studio, so these are specs, not HTML stylekits). Seed from [design-artifacts.md](design-artifacts.md).

### 3. Confirm

Show the user a draft of the `## Roblox Skills` block and the `docs/agents/*.md` files. Let them edit before writing.

### 4. Write

- If `CLAUDE.md` exists, edit it; if not, ask before creating one (don't also create `AGENTS.md` if the user prefers that — edit whichever they choose).
- If a `## Roblox Skills` block already exists, **update it in place** — don't append a duplicate, and don't clobber surrounding sections.
- Inject the block from [claude-block.md](claude-block.md). Omit any skill whose folder isn't installed here rather than inventing it.
- Write `docs/agents/tracker.md`, `docs/agents/triage-labels.md`, and `docs/agents/design.md` from the chosen seed files.

### 5. Done

Tell the user setup is complete, that every Roblox skill will now read this block for lifecycle and routing, and that they can edit `docs/agents/*.md` later without re-running this skill.

## Next

Start (or resume) the game with **`roblox-game-development-lifecycle`**, which reads this block to find the current phase and route to the right specialist. For a brand-new game, go to **`roblox-game-ideas`**.
