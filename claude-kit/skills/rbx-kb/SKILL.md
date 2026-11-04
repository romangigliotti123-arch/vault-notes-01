---
name: rbx-kb
description: "Cheap, cited answers to Roblox game-making questions from the local knowledge base (516 sources: official docs, 25 creators), no agents, no big files. Use proactively for any factual or 'what do the best creators say about X' question (retention, thumbnails, live ops, benchmarks). Not for plans, pricing or audits of your own game, or live market data."
---

# Roblox KB answer

Answer from the KB with timestamped citations and an official/indie flag, in few tokens. Do the work yourself; no subagents.

## Procedure
Each Bash call is a fresh shell, so set `K` every time:

```
K="bash $HOME/.claude/claude-kit/tools/pyrun $HOME/.claude/claude-kit/tools/kbq.py"   # run `$K where` once to see VAULT/KB/ASSETS
$K route "<question in plain words>"                       # 1 call: which topic files + coverage warning
$K find "<question keywords>" -n 8                         # cited rules, numbers, checklist, if-then items across topics
$K find "<keywords>" -t <topic1,topic2> -n 8               # narrow to the topics route suggested
$K num "<metric>"                                          # benchmark rows only
$K section <topic> disagree                                # only if sources might conflict
$K docs "<api, limit or feature>"                          # official Creator Docs facts (limits, rates, requirements)
$K case "<genre or game>"                                  # case studies
```

Stop as soon as you can answer: normally 2 to 4 calls. Quick references that are cheaper than topic files: `<KB>/_tools/` (BENCHMARKS.md, DECISION-RULES.md, PRICE-LADDER.md, AD-PLAYBOOK.md, CHECKLIST-*.md); Grep them for a keyword.

## Answer format (phone-sized)

```
<Direct answer in 1-3 sentences.>
- <supporting point or number> [flag, date] ([source label](url))
- <supporting point> ...
Conflict: <only if sources disagree: side A vs side B, which to trust and why>
Caveat: <outdated (>12 months), thin KB coverage, or indie self-reported>
```

At most 8 bullets. Every number or rule has a link and a flag (official | indie | mixed | devforum).

## Rules

- Official 2026 Creator Docs override older or indie advice on mechanics, metrics, payouts and limits. Say so when you choose between them.
- Indie CCU, revenue and conversion figures are self-reported: report them as "creators report", never as targets.
- If `route` or `find` shows thin or no coverage, or returns nothing relevant, write "KB gap", try `$K docs`, then a WebFetch of the relevant create.roblox.com page, and mark those facts UNVERIFIED.
- Never invent a number, link or timestamp; copy links exactly from the tool output.
- If the question needs a plan, audit, diagnosis or code, say which Roblox specialist handles it (rbx-designer, rbx-money, rbx-marketer, rbx-doctor, rbx-liveops, rbx-engineer) or hand to rbx-lead.

Self-check: answer first, then evidence, under about 200 words; every number cites a link and flag; conflicts and age (over 12 months) surfaced; about 4 kbq calls at most unless the question is broad.

## Learn
`/rbx-learn` for a verified non-obvious finding (one note each); on a problem run `vault-find.py "<problem>" --type learned` first.
