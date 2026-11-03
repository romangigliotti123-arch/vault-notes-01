---
name: contribute-rbxdev-vault
description: "Optional, on request only: packages one of your reusable items (Games/_Reusable/<name>/) into a zip so you can offer it to the vault owner for the shared host vault. Nothing is uploaded or published by this skill. Use only when the user says contribute this to the vault, share this reusable item, send it to the host, or /contribute-rbxdev-vault."
argument-hint: "<reusable item name>"
---

# contribute-rbxdev-vault

Your `Games/_Reusable/` items stay yours and local. Contributing is a manual, opt-in hand-over to the vault owner, who reviews it before it can reach the shared vault.

## Do this (only when the user asked)
1. List the items: `python ~/.claude/claude-kit/tools/games.py reusable list`. Pick the one the user named. If its README says `tested: n` or `rating: unrated`, say so and suggest testing first (the owner will not take untested code).
2. Check it is shareable: no secrets, no personal paths, no ids that belong to your game, no code copied from another game, licences of anything third-party noted in the README.
3. Bundle: `python ~/.claude/claude-kit/tools/games.py contribute <name>`. It writes `~/contribute-rbxdev-vault/<name>-<date>.zip` and prints the path. It does not upload anything.
4. Tell the user how to hand it over: send the zip to the vault owner (copy it to the drop location the owner gives you, for example with scp or a file share) and tell them the name and one-line purpose. If the user does not know the drop location, say "ask the vault owner"; do not guess an address or a path.
5. Never push to the vault repository or edit the vault clone; it is pull-only.
