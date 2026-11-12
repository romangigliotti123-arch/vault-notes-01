---
id: "rbx-metrics"
type: skill
category: "roblox"
source: "own"
license: "first-party"
repo_path: "skills/roblox/rbx-metrics/SKILL.md"
description: "Sourced table of Roblox benchmark numbers (D1, D7, session length, PTR, CTR, payer conversion, ARPPU, join time, ad cost per play, FPS) with an official/indie flag per row and a comparison script. Use for 'what is a good D1/CTR/conversion'."
orig_name: "rbx-metrics"
tags: [lib/skill, cat/roblox, src/own]
---

# rbx-metrics

> Sourced table of Roblox benchmark numbers (D1, D7, session length, PTR, CTR, payer conversion, ARPPU, join time, ad cost per play, FPS) with an official/indie flag per row and a comparison script. Use for 'what is a good D1/CTR/conversion'.

Type: skill | Category: [[categories/cat-roblox|roblox]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/roblox/rbx-metrics/SKILL.md` (extra files, if any, sit beside it in the repo)

---
# Roblox metrics benchmarks

Two parts: `benchmarks.md` (the table, same folder) and `compare.py` (deterministic comparison). Full tables: `<KB>/_tools/BENCHMARKS.md` (headline numbers first, regenerated daily).

## Use

- Look up: read `benchmarks.md` (about 15 rows).
- Compare: `bash ".rbx/claude-kit/tools/pyrun" ".rbx/claude-kit/vault-mode/.claude/skills/rbx-metrics/compare.py" --d1 8 --d7 1.5 --session 3 --ptr 2.2 --conv 0.8` (keys: d1 d7 d30 session ptr ctr conv arppu join fs5 bounce cpp optin fps). Output: verdict per metric, flag, sources.
- More detail on one metric: `bash ".rbx/claude-kit/tools/pyrun" ".rbx/claude-kit/tools/kbq.py" num "<metric>"`.

## Rules for using the numbers

- Most numeric bands are indie and self-reported (flag shows it). The official method is to compare against your own Creator Hub Similar Experience Benchmarks (50th to 90th percentile for similar games); tell the user to open Analytics and read those first.
- Official definitions (2026): D1/D7/D30 = share of new players (by first-play date) who return the next day / after 1 week / after 1 month; RFY scores returns in windows D1, D2-7, D8-28; ranking signals are PTR, first-play bounce, playtime and play days (QPTR retired).
- Gaps (no KB numbers): D30, first-play bounce, ARPPU band. Say "KB gap".
- Genre, audience age and traffic source change every number; ad and external traffic has lower D1 than Home recommendations.

## Maintenance

`thresholds.json` is curated from the KB `_tools/BENCHMARKS.md`; re-check bands with `kbq.py num` when the KB changes.
