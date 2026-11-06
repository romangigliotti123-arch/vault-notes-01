# Roblox Dev Mastery Vault

A Roblox game-development knowledge base plus a manager toolkit that runs AI agents to design, build, rate, market and update Roblox games. (Folder and repo name: `claudes-vault`.)

Built and maintained by Roman (GitHub: romangigliotti123-arch)

## Install

Paste this to Claude: Set up the Roblox Dev Mastery Vault on my computer: fetch https://raw.githubusercontent.com/romangigliotti123-arch/vault-kit-01/main/SETUP-FOR-CLAUDE.md with curl and follow it exactly. The agent follows SETUP-FOR-CLAUDE.md: clone this repository, install the Claude kit (https://github.com/romangigliotti123-arch/vault-kit-01), assets, light mode. Update later with /rbx-update. Website (viewer): https://vault-hhmi60uo.netlify.app

## Start here: making a game

Start a Claude session in the vault folder (for example `~/Obsidian/claudes-vault`; that folder is loaded automatically and the vault kit is OFF in every other Claude session), then run `/rbx-workflow`. To see it end to end first, read `Guides/Worked-Example-Idea-To-Live-Ops.md` (also at `claude-kit/examples/worked-example/README.md`): one game from idea to live-ops, with what you type, what Claude does, the critic's verdicts and the files created at each stage.

## For agents: start at CAPABILITIES.md

- `CAPABILITIES.md` (vault root) is a job router: "I need to review code / rate something 1-10 / research a topic / run agents ..." -> the item to use, its type and path (kit commands, Roblox knowledge base, Manager research, library picks).
- **Entry point: the vault mentor.** `/rbx-mentor` (or the agent `rbx-coach`) works alongside you on any job and suggests the right skill, agent, note or creator method at each step. It reads `CAPABILITIES.md` and `Mentor/Combined-Brain.md` first: the principles, methods and disagreements of every creator in both vaults, by job, with trust labels (creators weighted by the credibility audit; weak or unaudited creators never count as authorities). Optional hook that suggests vault matches on every prompt: `bash claude-kit/install.sh --with-hooks` / `install.ps1 -WithHooks`.
- Search both vaults by words: `bash ~/.claude/claude-kit/tools/pyrun ~/.claude/claude-kit/tools/vault-find.py "<what you need>"` (skills `rbx-use`, `rbx-ailib`). Read the one note you chose and follow it.

## What it is

The Roblox Dev Mastery Vault is an Obsidian vault built only for Roblox: one place where you learn what makes Roblox games succeed, and where AI agents use that knowledge to make games for you. It has two halves:

1. A Roblox knowledge base (about 4,550 notes) built from official Roblox docs and from the transcripts of about 100 Roblox creators: playbooks, decision rules, benchmark numbers, 90 case studies of real games, ads, monetisation, retention, thumbnails, security and Luau.
2. A manager toolkit (the `claude-kit/`, installed into `~/.claude/claude-kit`; only the vault folder itself is loaded, so every other Claude session stays clean): a flagship `/rbx-workflow`, side skills, 25 Roblox skills and 13 Roblox agents that design, build, rate, market, playtest and update a game, with you acting as the manager.

Who it is for: someone who wants to make or run Roblox games and manage the work with AI, with or without writing Luau themselves. Apart from the setup, nothing in it is general-purpose.

## What is inside

| Part | Where | What it is |
|---|---|---|
| Roblox knowledge base | `Roblox/roblox-kb/` (about 215 curated topic notes, tool sheets with `-TLDR` indexes and about 120 case studies; the Blender notes are separate, below) | Curated playbooks by topic (core loops, onboarding, retention, monetisation, pricing, ads, discovery, analytics, anti-exploit, updates and live ops, and more), `_tools` sheets (BENCHMARKS, DECISION-RULES, PRICE-LADDER, AD-PLAYBOOK, launch and monetisation checklists), 90+ `case-studies-*` notes. Start at `Roblox/roblox-kb/README.md` and `master-playbook.md`. |
| Creator and official sources | `Roblox/` (about 4,500 notes in total; about 87 creator folders grouped by trust in `creators/` (trusted, mixed, unaudited), plus `docs/`, `devforum/`, `RobloxCreators/`, `must-watch/`) | The source notes behind the playbooks: video notes with timestamps, Roblox Creator Docs and DevForum pages. |
| Creator credibility | `Roblox/roblox-kb/creator-credibility.md` | Which creators and claims to trust and why. Indie revenue and CCU figures are self-reported; prefer official sources for platform mechanics. |
| Blender for Roblox | `Roblox/blender/` (about 1,250 notes; hidden in light mode) | Research on modelling, rigging, animation and exporting from Blender to Roblox. |
| The manager method | `Manager/` (about 475 notes) | Research on how to manage AI agents: delegation, model choice, verification, cost control. It powers `/rbx-manager` and the head-manager step of the workflow. |
| Supporting material | `Library/` (about 850 notes), `Imported/` (about 1,700 notes) | `Library/` is one note per Roblox, game-dev, manager or research skill or agent (plus everything the kit uses) collected from open-source projects; `Imported/` holds other people's vaults and guides about Roblox and game dev (Roblox Creator Docs copy, Luau, game mechanics, awesome lists), licensed as listed under Licence. They are supporting reference, not the core. The general (non-Roblox) library is the companion AI Library Vault. |
| Assets | `Assets/` (about 2.7 GB, not in git) | Models, audio, textures, HDRIs and code libraries for Roblox, synced from the host PC's Tailscale share. |

Light mode (the default) hides the big supporting folders (`Library/`, `Imported/`, `Assets/`) from Obsidian so it opens fast, leaving the Roblox knowledge base and the Manager notes visible. The files stay on disk and Claude still searches them. See `LIGHT-MODE.md`; `/rbx-light-off` shows everything.

## How it works

1. Start Claude in the vault folder (the loaded folder), then run `/rbx-workflow` with your idea (or none).
2. Claude elaborates the idea from the vault: core loop, first 30 seconds, progression, monetisation, social hooks, each fact tied to a vault note.
3. It rates the idea 1.00-10.00 on 12 weighted criteria and checks what is hot now.
4. It plans the build with agents, models and a budget (`game-plan.md`).
5. It asks one question, "Ready to build?". On yes, a head manager runs the Roblox agents, builds a Rojo/Luau project, checks it and ends with a playtest report.
6. Side skills work alone at any point: `/rbx-ads`, `/rbx-game-update`, `/rbx-playtest`, `/rbx-thumbnail`, `/rbx-rate`, `/rbx-plan`, `/rbx-art`, `/rbx-visual` (the visual gate), plus `/rbx-research`, `/rbx-manager` and the vault commands `/rbx-update`, `/rbx-clean`, `/rbx-light-on`, `/rbx-light-off`.

Limits: it does not publish to Roblox or spend Robux; Studio playtests run only when the Roblox Studio MCP is connected, otherwise results are files marked untested. The notes are AI-compiled research from public sources: check numbers against the linked sources.

After setup, the AI ends with a summary block: see STEP 6 below.

## Installation

The step-by-step installation (vault clone, Claude kit, assets, light mode) is in SETUP-FOR-CLAUDE.md in this folder, the same text as https://raw.githubusercontent.com/romangigliotti123-arch/vault-kit-01/main/SETUP-FOR-CLAUDE.md.
