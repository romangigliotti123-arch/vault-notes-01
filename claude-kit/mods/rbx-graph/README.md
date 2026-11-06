# rbx-graph

`/rbx-graph` replies with one line, the link to the vault graph site, ready to click:

```
https://vault-hhmi60uo.netlify.app/#graph
```

No pane, no panel and nothing stored; it never reads or writes the vault and makes no network request (your browser opens the site when you click the link).

## Install and uninstall

INSTALL: `claude plugin install rbx-graph --marketplace <kit>/mods`

INSTALL (two steps): `claude plugin marketplace add <kit>/mods` then `claude plugin install rbx-graph@roblox-vault-kit-mods`

UNINSTALL: `claude plugin uninstall rbx-graph@roblox-vault-kit-mods`

Replace `<kit>` with the kit folder. Run `/reload-plugins` in an open session after installing.

## Updates

`install.sh` / `install.ps1` (the mods are installed by default; `--no-mods` / `-NoMods` skips them) re-copy the mods from the kit: an installed rbx-graph older than the kit's (version 0.2.0 is the link-only one) is updated in place.
