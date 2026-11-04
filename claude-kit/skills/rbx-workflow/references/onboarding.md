# onboarding: first run only

Run once per user and vault. `G profile` (G = `python ~/.claude/claude-kit/tools/games.py`) prints the stored answers in `Games/_profile.json` (protected, survives updates). If it prints a JSON with `level` and `type`, skip this file entirely.

## Ask (one AskUserQuestion with two questions; headless: take the defaults and say so)
1. "How much Roblox / Luau experience do you have?" options: New to Roblox development | Some (made a few things) | Experienced.
2. "What kind of game do you want to make?" options: Obby / parkour | Tycoon / simulator | Round-based / PvP | Surprise me (best-scoring small one); free text allowed.

Store: `G profile --level new|some|experienced --type "<answer>"`.

## What the answers change (nothing else is asked later)
| level | Behaviour |
|---|---|
| new | Explain each stage in one plain sentence when it starts; define terms the first time (CCU, D1, PTR); keep scope tiny (one loop, one map); prefer Studio MCP / Rojo steps written out; critic report adds a "what this means" line; offer to show where the file lives in Studio. |
| some | Short explanations only for new terms; normal scope; show commands. |
| experienced | Terse; show only evidence and decisions; allow bigger scope but still flag scope risk (F10). |
The game type feeds Stage 1 (`rbx-ideas` seed) and picks the genre playbook to read (`game-ideas-and-genres`, `genre-mechanics`, `Roblox/docs` genre playbooks).

## Rules
Never re-ask. To change: user says "change my level" and you run `G profile --level ...`; `G profile --reset` forgets everything. Do not store anything else about the person (no name, email, secrets).
