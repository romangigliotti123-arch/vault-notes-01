---
id: "roblox-metrics-benchmarks"
type: skill
category: "roblox"
source: "own"
license: "first-party"
repo_path: "skills/roblox/roblox-metrics-benchmarks/SKILL.md"
description: "One sourced table of Roblox benchmark numbers (D1, D7, session length, PTR, CTR, payer conversion, ARPPU, join time, ad cost per play, FPS) with an official/indie flag per row, plus a script that compares a game's numbers to those bands. Use for 'what is a good D1/CTR/conversion' and for benchmark targets."
orig_name: "roblox-metrics-benchmarks"
tags: [lib/skill, cat/roblox, src/own]
---

# roblox-metrics-benchmarks

> One sourced table of Roblox benchmark numbers (D1, D7, session length, PTR, CTR, payer conversion, ARPPU, join time, ad cost per play, FPS) with an official/indie flag per row, plus a script that compares a game's numbers to those bands. Use for 'what is a good D1/CTR/conversion' and for benchmark targets.

Type: skill | Category: [[categories/cat-roblox|roblox]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/roblox/roblox-metrics-benchmarks/SKILL.md` (extra files, if any, sit beside it in the repo)

Related: [[S--own--youtube-learn]]

---
# Roblox metrics benchmarks

Two parts: `benchmarks.md` (the table, same folder) and `compare.py` (deterministic comparison). Full tables: `~/claude-host/youtube-learn/out/roblox-kb/_tools/BENCHMARKS.md` (headline numbers first, regenerated daily).

## Use

- Look up: read `benchmarks.md` (about 15 rows).
- Compare: `python ~/claude-library/skills/roblox/roblox-metrics-benchmarks/compare.py --d1 8 --d7 1.5 --session 3 --ptr 2.2 --conv 0.8` (keys: d1 d7 d30 session ptr ctr conv arppu join fs5 bounce cpp optin fps). Output: verdict per metric, flag, sources.
- More detail on one metric: `python ~/claude-library/tools/roblox-kb/kbq.py num "<metric>"`.

## Rules for using the numbers

- Most numeric bands are indie and self-reported (flag shows it). The official method is to compare against your own Creator Hub Similar Experience Benchmarks (50th to 90th percentile for similar games); tell the user to open Analytics and read those first.
- Official definitions (2026): D1/D7/D30 = share of new players (by first-play date) who return the next day / after 1 week / after 1 month; RFY scores returns in windows D1, D2-7, D8-28; ranking signals are PTR, first-play bounce, playtime and play days (QPTR retired).
- Gaps (no KB numbers): D30, first-play bounce, ARPPU band. Say "KB gap".
- Genre, audience age and traffic source change every number; ad and external traffic has lower D1 than Home recommendations.

## Maintenance

`thresholds.json` is curated from the KB; when `_tools/BENCHMARKS.md` changes materially, re-check bands with `kbq.py num` and update the JSON, then run `python ~/claude-library/tools/roblox-kb/build_tools.py` (rewrites `benchmarks.md`).


## Triggers (moved out of the description)

Use when the user asks what a good D1/D7/session/conversion/CTR is, how their numbers compare, or wants benchmark targets for a Roblox game.
