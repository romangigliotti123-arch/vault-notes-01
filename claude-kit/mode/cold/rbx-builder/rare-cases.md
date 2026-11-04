<!-- cold: rbx-builder/rare-cases.md | read when: read only when VAULT is still empty after that order (clone commands, fallback URLs, failure handling). -->

## From agents/rbx-builder.md :: - VAULT order: env CLAUDES_VAULT, `~/Obsidian/claudes-vault`

- VAULT order: env CLAUDES_VAULT, `~/Obsidian/claudes-vault`, `%USERPROFILE%\Obsidian\claudes-vault`, then (empty VAULT) clone read-only: `git clone https://github.com/romangigliotti123-arch/vault-notes-01.git ~/Obsidian/claudes-vault`, then repeat the two lines. If the clone fails, continue with WebFetch of create.roblox.com docs, mark everything UNVERIFIED, and say so in the report.

## From agents/rbx-builder.md :: - If python is missing (`pyrun` exits 127 or `where` fails):

- If python is missing (`pyrun` exits 127 or `where` fails): set VAULT yourself from the order above (`ls -d` each candidate; KB=$VAULT/Roblox/roblox-kb, ASSETS likewise) and replace every kbq call by `rg`/`grep` over `$KB` (markdown; topic names in `$KB/README.md`; read `_tools/` sheets directly).
