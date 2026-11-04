---
id: "contribute-rbxdev-vault"
type: skill
category: "game-dev"
source: "own"
license: "first-party"
repo_path: "skills/game-dev/contribute-rbxdev-vault/SKILL.md"
description: "Optional, on request only: packages one of your reusable items (Games/_Reusable/<name>/) into a zip so you can offer it to the vault owner for the shared host vault. Nothing is uploaded or published by this skill. Use only when the user says contribute this to the vault, share this reusable item, send it to the host, or /contribute-rbxdev-vault."
orig_name: "contribute-rbxdev-vault"
orig_argument_hint: "<reusable item name>"
tags: [lib/skill, cat/game-dev, src/own]
---

# contribute-rbxdev-vault

> Optional, on request only: packages one of your reusable items (Games/_Reusable/<name>/) into a zip so you can offer it to the vault owner for the shared host vault. Nothing is uploaded or published by this skill. Use only when the user says contribute this to the vault, share this reusable item, send it to the host, or /contribute-rbxdev-vault.

Type: skill | Category: [[categories/cat-game-dev|game-dev]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/game-dev/contribute-rbxdev-vault/SKILL.md` (extra files, if any, sit beside it in the repo)

---
# contribute-rbxdev-vault

Your `Games/_Reusable/` items stay yours and local. Contributing is a manual, opt-in hand-over to the vault owner, who reviews it before it can reach the shared vault.

## Do this (only when the user asked)
1. List the items: `python ~/.claude/claude-kit/tools/games.py reusable list`. Pick the one the user named. If its README says `tested: n` or `rating: unrated`, say so and suggest testing first (the owner will not take untested code).
2. Check it is shareable: no secrets, no personal paths, no ids that belong to your game, no code copied from another game, licences of anything third-party noted in the README.
3. Bundle: `python ~/.claude/claude-kit/tools/games.py contribute <name>`. It writes `~/contribute-rbxdev-vault/<name>-<date>.zip` and prints the path. It does not upload anything.
4. Tell the user how to hand it over: the vault owner's host is reached over Tailscale (the same network the vault clone uses). Send the zip to the owner (copy it to the drop location the owner gives you, for example with scp or a Tailscale file share) and tell them the name and one-line purpose. If the user does not know the drop location, say "ask the vault owner"; do not guess an address or a path.
5. Never push to the vault repository or edit the vault clone; it is pull-only.
