---
name: make-roblox-game
description: "Use when the user says make/build/create me a Roblox game (with or without an idea), 'use the vault to build', 'give me game ideas that would do well', or wants a Roblox game designed and built from the vault, skills and assets without being asked questions; delegates to the roblox-game-builder agent, which researches the vault, writes a scored GDD and a Rojo/Luau project, checks it and reports how to open it in Studio."
---

# make-roblox-game

One sentence from the user is enough. Do not ask the user anything.

## What to do
1. Take the user's idea verbatim (it may be empty or vague; that is fine: the builder makes assumptions and writes them down).
2. If `~/.claude/claude-kit/vault-mode/.claude/agents/roblox-game-builder.md` does not exist, install the kit first (no questions): find the vault (`$CLAUDES_VAULT`, `~/Obsidian/claudes-vault`, `%USERPROFILE%\Obsidian\claudes-vault`; if absent clone `git clone https://github.com/romangigliotti123-arch/vault-notes-01.git ~/Obsidian/claudes-vault`) and follow `claude-kit/INSTALL.md` in it.
3. Delegate: use the Agent tool with `subagent_type: roblox-game-builder`; prompt = the user's idea word for word plus the working folder to create the project in (default: the current directory). If you have no Agent tool (you are already a subagent), read `~/.claude/claude-kit/vault-mode/.claude/agents/roblox-game-builder.md` and follow it yourself, inline.
4. "Give me game ideas that would do well" (no build wanted): run only the roblox-game-ideas skill (it reads the vault first) and return the top three scored ideas, then offer in one line to build the winner.
5. Relay the builder's final report to the user as it is: what exists, where, how to open it in Roblox Studio (Rojo sync or paste), what is untested, the next three tasks. Do not claim the game works unless the report shows a command and its output. Never describe the result as done, complete or polished unless `game-dev-visual-qa` passed with screenshots; otherwise say `playable prototype, visuals not polished` and offer `/game-dev-visual-qa` as the next step.

## Sentences that trigger this
"make me a Roblox game: <idea>", "use the vault to build <idea>", "build me a pet obby for kids", "give me game ideas that would do well", "design and build a tycoon".

## Guardrails
Never publish to Roblox, spend Robux or money, or post anything. Never write into the vault. Never invent Roblox asset, pass or product ids.

## Learn

When this run verifies something non-obvious (a fix, a gotcha, a corrected assumption, a technique that worked), record it with `/vault-learn` (`learn.py add`, one finding per note). Before researching a problem, check the curated `learned/` notes: `vault-find.py "<problem>" --type learned`.
