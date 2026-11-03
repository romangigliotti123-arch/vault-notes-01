---
id: "roblox-kb-answer"
type: skill
category: "roblox"
source: "own"
license: "first-party"
repo_path: "skills/roblox/roblox-kb-answer/SKILL.md"
description: "Cheap, cited answers to Roblox game-making questions from the local Roblox knowledge base (516 sources: official docs/sessions plus 25 creators), without spawning agents or reading big files. Use proactively for any factual or \"what do the best creators/Roblox say about X\" question about Roblox ideas, retention, monetisation, pricing, ads, thumbnails, live ops, scripting limits, DevEx/tax, platform changes, benchmarks. Not for building a full plan (use the Roblox specialist agents) or live market data (roblox-trend-research)."
orig_name: "roblox-kb-answer"
tags: [lib/skill, cat/roblox, src/own]
---

# roblox-kb-answer

> Cheap, cited answers to Roblox game-making questions from the local Roblox knowledge base (516 sources: official docs/sessions plus 25 creators), without spawning agents or reading big files. Use proactively for any factual or "what do the best creators/Roblox say about X" question about Roblox ideas, retention, monetisation, pricing, ads, thumbnails, live ops, scripting limits, DevEx/tax, platform changes, benchmarks. Not for building a full plan (use the Roblox specialist agents) or live market data (roblox-trend-research).

Type: skill | Category: [[categories/cat-roblox|roblox]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/roblox/roblox-kb-answer/SKILL.md` (extra files, if any, sit beside it in the repo)

Related: [[A--own--roblox-game-designer]], [[A--own--roblox-game-doctor]], [[A--own--roblox-launch-marketing-manager]], [[A--own--roblox-liveops-planner]], [[A--own--roblox-luau-engineer]], [[A--own--roblox-monetization-consultant]], [[A--own--roblox-studio-lead]], [[S--own--youtube-learn]]

---
# Roblox KB answer

Answer from the KB, with timestamped citations and an official/indie flag, in as few tokens as possible. Do the work yourself; no subagents.

## Procedure

Each Bash call is a fresh shell, so set `K` every time:

```
K="python ~/claude-library/tools/roblox-kb/kbq.py"
$K route "<question in plain words>"                       # 1 call: which topic files + coverage warning
$K find "<question keywords>" -n 8                         # cited rules, numbers, checklist, if-then items across topics
$K find "<keywords>" -t <topic1,topic2> -n 8               # narrow to the topics route suggested
$K num "<metric>"                                          # benchmark rows only
$K section <topic> disagree                                # only if sources might conflict
$K docs "<api, limit or feature>"                          # official Creator Docs facts (limits, rates, requirements)
$K case "<genre or game>"                                  # case studies
```

Stop as soon as you can answer: normally 2 to 4 calls. Quick references that are cheaper than topic files: `~/claude-host/youtube-learn/out/roblox-kb/_tools/` (BENCHMARKS.md, DECISION-RULES.md, PRICE-LADDER.md, AD-PLAYBOOK.md, CHECKLIST-*.md); Grep them for a keyword.

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
- If the question needs a plan, audit, diagnosis or code, say which Roblox specialist handles it (roblox-game-designer, roblox-monetization-consultant, roblox-launch-marketing-manager, roblox-game-doctor, roblox-liveops-planner, roblox-luau-engineer) or hand to roblox-studio-lead.

## Self-check

- [ ] Answer first, then evidence; under about 200 words.
- [ ] Every number cites a source link and flag.
- [ ] Conflicts and age (over 12 months) surfaced.
- [ ] No more than about 4 kbq calls unless the question is broad.
