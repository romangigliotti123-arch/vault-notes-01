# Claude Code mods in the kit

This folder is a local plugin marketplace (`.claude-plugin/marketplace.json`, name `roblox-vault-kit-mods`). Replace `<kit>` below with the kit folder.

| Mod | What it does |
|---|---|
| rbx-subagent-hud | Side pane: the master agent on top, its subagents below joined by flashing dotted lines (grey running, green done), `2/4 done` counter, `~N min left` estimate, click a subagent to see the prompt the master sent it. `/rbx-subagent-hud` toggles it. Replaces `rbx-subagent-hud`. |
| rbx-graph | `/rbx-graph` opens a side pane with the link graph of the vault: centre note, links in and out, search, preview. |

INSTALL rbx-subagent-hud: `claude plugin install rbx-subagent-hud --marketplace <kit>/mods`

INSTALL rbx-graph: `claude plugin install rbx-graph --marketplace <kit>/mods`

UNINSTALL rbx-subagent-hud: `claude plugin uninstall rbx-subagent-hud@roblox-vault-kit-mods`

UNINSTALL rbx-graph: `claude plugin uninstall rbx-graph@roblox-vault-kit-mods`

REMOVE the marketplace (after uninstalling both): `claude plugin marketplace remove roblox-vault-kit-mods`

Desktop app, where `/plugin` does not run: click + next to the prompt box, then Plugins, Add marketplace with the path `<kit>/mods`, then Add plugin. Run `/reload-plugins` in an open session after installing.

Panes and the line above the prompt are not shown in Remote Control or mobile views.
