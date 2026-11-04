---
id: "rbx-make"
type: skill
category: "roblox"
source: "own"
license: "first-party"
repo_path: "skills/roblox/rbx-make/SKILL.md"
description: "Use when the user says make/build/create me a Roblox game (with or without an idea) without being asked questions; delegates to the rbx-builder agent: vault research, scored GDD, Rojo/Luau project, checks, how to open it in Studio."
orig_name: "rbx-make"
tags: [lib/skill, cat/roblox, src/own]
---

# rbx-make

> Use when the user says make/build/create me a Roblox game (with or without an idea) without being asked questions; delegates to the rbx-builder agent: vault research, scored GDD, Rojo/Luau project, checks, how to open it in Studio.

Type: skill | Category: [[categories/cat-roblox|roblox]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/roblox/rbx-make/SKILL.md` (extra files, if any, sit beside it in the repo)

Related: [[A--own--rbx-builder]], [[S--own--rbx-ideas]], [[S--own--rbx-lighting]], [[S--own--rbx-placement]], [[S--own--rbx-visual]]

---
# rbx-make

Code comments: none by default (see rbx-luau, Comments).
Smallest complete change: see rbx-luau.

One sentence from the user is enough. Do not ask the user anything.

## What to do
1. Take the user's idea verbatim (it may be empty or vague; that is fine: the builder makes assumptions and writes them down).
2. If `~/.claude/claude-kit/vault-mode/.claude/agents/rbx-builder.md` does not exist, install the kit first (no questions): find the vault (`$CLAUDES_VAULT`, `~/Obsidian/claudes-vault`, `%USERPROFILE%\Obsidian\claudes-vault`; if absent clone `git clone http://[host]:8765/vault.git ~/Obsidian/claudes-vault`) and follow `claude-kit/INSTALL.md` in it.
3. Delegate: use the Agent tool with `subagent_type: rbx-builder`; prompt = the user's idea word for word plus the working folder to create the project in (default: the current directory). If you have no Agent tool (you are already a subagent), read `~/.claude/claude-kit/vault-mode/.claude/agents/rbx-builder.md` and follow it yourself, inline.
4. "Give me game ideas that would do well" (no build wanted): run only the rbx-ideas skill (it reads the vault first) and return the top three scored ideas, then offer in one line to build the winner.
5. Relay the builder's final report to the user as it is: what exists, where, how to open it in Roblox Studio (Rojo sync or paste), what is untested, the next three tasks. Do not claim the game works unless the report shows a command and its output. Never describe the result as done, complete or polished unless `rbx-visual` passed with screenshots; otherwise say `playable prototype, visuals not polished` and offer `/rbx-visual` as the next step. Placement is a separate gate: never call the result done unless `rbx-placement` printed `PLACEMENT GATE: PASS` (every model placed in the map checked, full-map scan); otherwise say `playable prototype, placement not verified` and offer `/rbx-placement`. Lighting is a third gate: set the genre's lighting preset first (`/rbx-lighting`) and never call the result done unless `LIGHTING GATE: PASS`; otherwise say `playable prototype, lighting not verified`.

## Sentences that trigger this
"make me a Roblox game: <idea>", "use the vault to build <idea>", "build me a pet obby for kids", "give me game ideas that would do well", "design and build a tycoon".

## Guardrails
Never publish to Roblox, spend Robux or money, or post anything. Never write into the vault. Never invent Roblox asset, pass or product ids.

## Learn

Verified something non-obvious? Record it with `/rbx-learn` (one finding per note). Hit a problem? Check `vault-find.py "<problem>" --type learned` first.
