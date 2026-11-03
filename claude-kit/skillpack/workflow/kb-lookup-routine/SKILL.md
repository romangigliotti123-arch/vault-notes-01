---
name: kb-lookup-routine
description: "Find the right vault evidence fast and cheaply for a question: route the job with vault-find, query the Roblox KB with kbq, read only the cited section, and record a source list with trust labels. Use whenever a decision, brief or skill needs vault evidence, and to prepare KB paths for a worker's brief."
category: workflow
tags: vault, kb, lookup, search, evidence, kbq, vault-find, mentor, sources, trust, citation
kb: Manager/topic-knowledge-management-rag.md, Manager/topic-skill-library-retrieval.md, Mentor/Combined-Brain.md, Roblox/roblox-kb/master-playbook.md, Roblox/roblox-kb/creator-credibility.md, Manager/topic-context-window-management.md
related: mentor-rbxdev-vault, use-rbxdev-vault, roblox-kb-answer, decision-log-writer, ai-brief-writer, use-ai-library-rbxdev-vault, game-dev-workflow
---

# kb-lookup-routine

The vault is large (the Roblox KB topic files run 50-450 KB each); loading one whole is the common mistake. `mentor-rbxdev-vault` is the interactive co-pilot that suggests things as you work and `roblox-kb-answer` answers a question from the KB; this routine is the repeatable lookup procedure behind them, used when you need citations for a decision log, a brief or another skill.

## When to use
You need evidence for a design, tooling or process choice; a worker needs KB paths in its brief; you must check a claim against the vault before stating it. Not for: general chat, or facts that are live-check items (prices, limits, menu paths), which need the current official docs.

## Inputs (max 2)
1. The question in one sentence. 2. Domain (default: guess from words: Roblox game/dev vs Manager/agent practice).

## Procedure
1. Route first: `python ~/.claude/claude-kit/tools/vault-find.py "<question>" -n 8` (add `--type kb|manager|skillpack|brain`). Read the titles and one-line descriptions, not the notes.
2. For Roblox facts query the KB: `python ~/.claude/claude-kit/tools/kbq.py find "<query>" -n 8 --official` first (official flags win on numbers), then `kbq.py section <topic> rules --max-chars 1500` for one topic section. For API or limit facts use `kbq.py docs "<query>"`. Never open a whole topic file.
3. For agent and process questions open the matching `Manager/topic-*.md` TL;DR section only, then follow one cited `src-*.md` note if the claim is load-bearing. `Mentor/Combined-Brain.md` has trust-weighted job sections and creator cards.
4. Apply the trust order: official docs and staff, then TRUSTED creators, then MIXED (needs a second source), then indie single-mention. Label every claim you carry forward: `official`, `TRUSTED`, `indie`, `opinion`. Where sources disagree, report both sides, not a blend.
5. Check freshness: the note's newest date; for fast-moving topics (monetisation rules, platform changes, tool versions) write `live-check` instead of a number.
6. Write the source list: claim, vault path, label, date. Limit to the five most load-bearing sources; more is noise.
7. If the vault has nothing, say "vault has no evidence" and mark the answer `opinion`; do not fill the gap with a plausible number.
8. Save to `docs/evidence/<topic>.md` (headings Question, Sources, Trust; under 60 lines) and check it.

## Studio MCP path
None.

## Fallback
If the scripts or Python are missing, use `rg -n -m 5 "<term>" "<vault>/Roblox/roblox-kb" --glob "*.md"` and open the matching section by line number. If the vault is absent, say so in one line; do not answer vault questions from memory.

## Evidence
`Manager/topic-knowledge-management-rag.md` (corpus this size: agentic search over small well-named files with an index; must-happen knowledge in always-loaded text, not behind an optional lookup; provenance on every note), `Manager/topic-skill-library-retrieval.md` (route before reading; measure on your own queries), `Manager/topic-context-window-management.md` (keep tool output small), `Mentor/Combined-Brain.md` (trust weighting and creator cards), `Roblox/roblox-kb/creator-credibility.md` (how sources are rated).

## Output
`docs/evidence/<topic>.md`: question, up to five labelled sources with paths and dates, the conclusion, and any live-check items.

## Acceptance checks
- [ ] Executed: `python ~/.claude/claude-kit/tools/vault-find.py "<question>" -n 3` returned hits (paste the first line) or `no vault` is stated.
- [ ] Executed: `python project-kickoff/scripts/wfdoc.py docs/evidence/<topic>.md --kind kblookup` prints PASS.
- [ ] Every cited path exists (`test -f` on each).
- [ ] Every claim carries a trust label; fast-moving facts say live-check.

## Pitfalls
Quoting one indie creator as a benchmark. Reading a whole topic file for one fact. Treating a search hit's snippet as the source. Citing a path from memory without opening it.

## Related
`mentor-rbxdev-vault`, `use-rbxdev-vault`, `roblox-kb-answer`, `decision-log-writer`, `ai-brief-writer`.
