---
type: game-systems
game: {{slug}}
---
# {{slug}} - systems
Back to [[{{slug}}/GAME|GAME]] | [[{{slug}}/design|design]]

## Rule: reuse before building
For every system this game needs (data saving, shop and passes, daily rewards, analytics events, admin tools, UI kits, round loop ...) look in this order:
1. `Games/_Reusable/` (your own tested blocks): `python .rbx/claude-kit/tools/vault-find.py "<system>" --type reusable`, or [[Games/README|Games hub]].
2. The kit's tested drop-in systems (`python .rbx/claude-kit/tools/games.py system list`; `vault-find.py "<system>" --type system`; add with `games.py system add <Name> --game {{slug}}`: PlayerData, Shop, DailyRewards, Analytics, Admin) and the vault skills (`rbx-datastore`, `rbx-monetize`, `rbx-leaderboard` ...).
3. Only then write it, and when it works and is tested, harvest it (`rbx-harvest`) so the next game gets it for free.

## Systems in this game
| System | Source (reusable / library / built here) | Tested? | Link |
|---|---|---|---|
| - | - | - | - |

## Harvested from this game (links to Games/_Reusable)
