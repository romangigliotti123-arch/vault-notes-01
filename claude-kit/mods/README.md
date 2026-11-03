# Claude Code mods in the kit

This folder is a local plugin marketplace (`.claude-plugin/marketplace.json`, name `roblox-vault-kit-mods`). Replace `<kit>` below with the kit folder.

| Mod | What it does |
|---|---|
| hud-rbxdev-vault | Side pane for the game dev workflow: tree of the master agent and its agents with status and elapsed time, plus a progress bar. `/hud-rbxdev-vault` toggles it. |
| graph-rbxdev-vault | `/graph-rbxdev-vault` opens a side pane with the link graph of the vault: centre note, links in and out, search, preview. |

INSTALL hud-rbxdev-vault: `claude plugin install hud-rbxdev-vault --marketplace <kit>/mods`

INSTALL graph-rbxdev-vault: `claude plugin install graph-rbxdev-vault --marketplace <kit>/mods`

UNINSTALL hud-rbxdev-vault: `claude plugin uninstall hud-rbxdev-vault@roblox-vault-kit-mods`

UNINSTALL graph-rbxdev-vault: `claude plugin uninstall graph-rbxdev-vault@roblox-vault-kit-mods`

REMOVE the marketplace (after uninstalling both): `claude plugin marketplace remove roblox-vault-kit-mods`

Desktop app, where `/plugin` does not run: click + next to the prompt box, then Plugins, Add marketplace with the path `<kit>/mods`, then Add plugin. Run `/reload-plugins` in an open session after installing.

Panes and the line above the prompt are not shown in Remote Control or mobile views.
