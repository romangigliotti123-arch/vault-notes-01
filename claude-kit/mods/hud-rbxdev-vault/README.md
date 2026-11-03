# hud-rbxdev-vault

A side pane for the game dev workflow. While the master agent works, the pane shows which agents it started, whether each is working, and how far through the current plan the turn is. It makes no notifications, plays no sounds, uses no network and writes no files (state lives in the session's `$.state` only).

## What it shows

```
● Master working 3m12s
├─ ● Build terrain working 3m12s
│  └─ ● Place trees working 3m12s
├─ ● Write shop UI working 3m12s
└─ ● Audit scripts done 1m00s

██████████░░░░░░░░░░ 50%
2/3 tasks 1/3 workers
Doing step 3
```

- The master agent is the top node. Each agent it spawned is a child; agents spawned by an agent are drawn under that agent (tree lines).
- Each node shows a short name (the agent description), a coloured status (working, waiting, done, failed, killed) and elapsed time. A finished node shows its total time.
- The bar is done/total of the task list (TaskCreate/TaskUpdate), TodoWrite and the workers of the current batch. A new batch starts when an agent is spawned while none are working, so old finished agents do not count. Half the plan items and workers done reads 50%.

## When it opens

It opens by itself on the first of these:

1. the Skill tool called with a skill whose name contains `game-dev`,
2. a prompt that starts with `/game-dev`,
3. the first Agent spawn while a `GAME.md` exists in the working folder.

`/hud-rbxdev-vault` toggles it by hand. If you close the pane yourself it stays closed until you run `/hud-rbxdev-vault`.

On a terminal too narrow for a docked pane (under about 144 columns for an automatic open), a one-line fallback above the prompt shows a short bar and "N agents working". `/hud-rbxdev-vault` opens the pane at any width.

## Install and uninstall

The `mods` folder of the kit is a local plugin marketplace (`mods/.claude-plugin/marketplace.json`, name `roblox-vault-kit-mods`).

INSTALL: `claude plugin install hud-rbxdev-vault --marketplace <kit>/mods`

INSTALL (two steps): `claude plugin marketplace add <kit>/mods` then `claude plugin install hud-rbxdev-vault@roblox-vault-kit-mods`

INSTALL (inside a terminal session): `/plugin install hud-rbxdev-vault --marketplace <kit>/mods`

INSTALL (desktop app, where `/plugin` does not run): click + next to the prompt box, then Plugins, Add marketplace with the path `<kit>/mods`, then Add plugin.

UNINSTALL: `claude plugin uninstall hud-rbxdev-vault@roblox-vault-kit-mods`

UNINSTALL (also drop the marketplace): `claude plugin marketplace remove roblox-vault-kit-mods`

Replace `<kit>` with the folder the kit is installed in. Run `/reload-plugins` in an open session after installing.

## Limits

- Remote Control and mobile views cannot show it. Panes and the above-prompt line are drawn only on the local terminal, desktop app and VS Code; a phone or remote client gets the normal transcript only.
- The engine reports an agent only as spawned or ended; elapsed time is measured from the first time the HUD sees the agent (about one second resolution), so an agent that started before the mod loaded shows time from load.
- Agents the engine drops from its list seconds after they end stay in the tree (with their total time) until a new batch starts or 60 agents are kept.
