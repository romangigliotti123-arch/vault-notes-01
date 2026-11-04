# rbx-graph

`/rbx-graph` opens a side pane titled "Vault graph" with the link graph of your Obsidian vault, read from the local markdown files and `[[wikilinks]]`. Read-only: it never writes to the vault, and the only network use is the "Open full graph" link, which opens the vault site in your browser when you click it.

## What it shows

```
links in 2 · links out 2 · notes 4821
Find [ note name ] [Go]
← links in
┌─ Delta
├─ Alpha
│
◉ README
│
├─ Alpha
└─ Beta
links out →
[Note] [Refresh] [Close] Open full graph
```

- The selected note is in the centre (the vault README by default). Notes it links to and notes that link to it are drawn around it with lines. Each is a button: press one and the graph re-centres on it.
- Find: type part of a note name and press Go (or Enter) to jump to the best match; up to 6 matches are listed as buttons.
- Note: shows the first 20 lines of the centre note; press the button again (it reads Graph) to go back.
- Refresh re-reads the vault. Close, the pane's own close mark and `/rbx-graph` again all close it.
- On a terminal too narrow to place the pane, a line above the prompt says "widen the window to see the graph".

## Where the vault is found

Same lookup as the kit's uninstall skill: `$CLAUDES_VAULT`, then `~/Obsidian/claudes-vault`, then a search of Downloads, Documents, Desktop, Obsidian and the home folder for a folder holding `Roblox/`, `Mentor/` and `claude-kit/`.

## Index

Built once and cached in the plugin store (names, links, backlinks only; previews are read on demand). It is rebuilt when the vault's file count or newest modification time changes, re-reading only changed notes, or in full with Refresh. A first build of a large vault (thousands of notes) takes a while; the pane shows progress meanwhile.

## Install and uninstall

INSTALL: `claude plugin install rbx-graph --marketplace <kit>/mods`

INSTALL (two steps): `claude plugin marketplace add <kit>/mods` then `claude plugin install rbx-graph@roblox-vault-kit-mods`

UNINSTALL: `claude plugin uninstall rbx-graph@roblox-vault-kit-mods`

Replace `<kit>` with the kit folder. Run `/reload-plugins` in an open session after installing.

## Limits

- Remote Control and mobile views cannot show panes; the mobile surface gets a one-line notice.
- "Open full graph" is a link element (the plugin API has no button that opens a URL); click it, or open it from the terminal's link handling.
- Links are `[[wikilinks]]` only (aliases and headings are stripped); plain markdown links are not counted. A name used by several notes resolves to the one with the shortest path.
