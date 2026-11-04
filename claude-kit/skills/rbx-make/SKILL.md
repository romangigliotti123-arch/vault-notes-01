---
name: rbx-make
description: "Use when the user says make/build/create me a Roblox game (with or without an idea) without being asked questions; delegates to the rbx-builder agent: vault research, scored GDD, Rojo/Luau project, checks, how to open it in Studio."
---

# rbx-make

Code comments: none by default (see rbx-luau, Comments).
Smallest complete change: see rbx-luau.

One sentence from the user is enough. Do not ask the user anything.

## What to do
1. Take the user's idea verbatim (empty or vague is fine: the builder writes down its assumptions).
2. If `~/.claude/claude-kit/vault-mode/.claude/agents/rbx-builder.md` does not exist, install the kit first (no questions): find the vault (`$CLAUDES_VAULT`, `~/Obsidian/claudes-vault`, `%USERPROFILE%\Obsidian\claudes-vault`; if absent `git clone https://github.com/romangigliotti123-arch/vault-notes-01.git ~/Obsidian/claudes-vault`) and follow `claude-kit/INSTALL.md` in it.
3. Delegate: Agent tool with `subagent_type: rbx-builder`; prompt = the user's idea word for word plus the working folder for the project (default: current directory). No Agent tool (you are already a subagent): read `~/.claude/claude-kit/vault-mode/.claude/agents/rbx-builder.md` and follow it inline.
4. "Give me game ideas that would do well" (no build wanted): run only the rbx-ideas skill (it reads the vault first) and return the top three scored ideas, then offer in one line to build the winner.
5. Relay the builder's final report as it is: what exists, where, how to open it in Roblox Studio (Rojo sync or paste), what is untested, the next three tasks. Do not claim the game works unless the report shows a command and its output. Never call the result done, complete or polished unless `rbx-visual` passed with screenshots; otherwise say `playable prototype, visuals not polished` and offer `/rbx-visual`. Placement is a separate gate: never call it done unless `rbx-placement` printed `PLACEMENT GATE: PASS` (every placed model checked, full-map scan); otherwise say `playable prototype, placement not verified` and offer `/rbx-placement`. Lighting is a third gate: set the genre's lighting preset first (`/rbx-lighting`) and never call it done unless `LIGHTING GATE: PASS`; otherwise say `playable prototype, lighting not verified`.

## Sentences that trigger this
"make me a Roblox game: <idea>", "use the vault to build <idea>", "build me a pet obby for kids", "give me game ideas that would do well", "design and build a tycoon".

## Guardrails
Never publish to Roblox, spend Robux or money, or post anything. Never write into the vault. Never invent Roblox asset, pass or product ids.

## Learn

Verified something non-obvious? Record it with `/rbx-learn` (one finding per note). Hit a problem? Check `vault-find.py "<problem>" --type learned` first.
