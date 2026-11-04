---
tags: [moc]
---
# About this vault section

`Library/` is a generated, read-only view of the private git repo `claude-library` (single source of truth). Edits here are overwritten.
This vault is the Roblox Dev Mastery Vault; it holds the Roblox, game-dev, orchestration (manager) and research items plus everything the claude-kit uses. All other skills and agents are in the companion AI Library Vault.

- Start with the mentor: `/rbx-mentor` (claude-kit) reads `CAPABILITIES.md` and `Mentor/Combined-Brain.md`, works alongside you and suggests the right item at each step. By hand: scan `CAPABILITIES.md`, search with `vault-find.py "<what you need>"`, read the one note you chose.
- Each note holds the full text of one skill or agent. Frontmatter: `id`, `type`, `category`, `source`, `license`, `repo_path`, `description`, original keys as `orig_*`.
- Note names: `S--<source>--<name>` for skills, `A--<source>--<name>` for agents.
- Same-name items (for example several `code-reviewer`) show only the best one; the others are listed as `alternatives` in its frontmatter and in an Alternatives section at its end. A few stubs and off-target items are left out of this view. Both lists, with reasons, are in `claude-library/tools/vault-exclude.json`; the repo itself keeps every item.
- `Related:` links come from item names mentioned in the text; Category and Source notes group items.
- Tags: `lib/skill`, `lib/agent`, `cat/<category>`, `src/<source>`. Graph colours: agents orange, own skills green, imported skills blue.
- Regenerate: `powershell -File ~\claude-library\tools\sync-vault.ps1`
- Query the graph: `graphify query "<task>" --graph ~\claude-host\vault-graph\catalog\graphify-out\graph.json --budget 800`
- Assets beside a SKILL.md (scripts, references) stay in the repo, see `repo_path`.
