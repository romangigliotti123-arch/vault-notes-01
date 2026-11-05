---
name: rbx-ad-plan
description: "Plans a Roblox sponsored-experience ad test: readiness gate, budget, day-by-day checkpoints, creative test matrix, stop rules, sourced from the knowledge base. Use to plan, budget or evaluate ads ('plan a $100 ad test', 'is my game ready for ads', 'when to stop'). Plans only; never runs or pays."
---

# Roblox ad campaign planner

Output: a campaign plan (gate, budget table, schedule, creatives, KPIs, stop rules) with sources. Never spends money or touches Ads Manager.

## Procedure

1. Inputs (assume and state): game, genre, budget cap (or total), launch date, current D1 / first-play bounce / PTR / session length, existing thumbnails, age of game (new vs lapsed).
2. Evidence:
   ```
   K="bash $HOME/.claude/claude-kit/tools/pyrun $HOME/.claude/claude-kit/tools/kbq.py"   # run `$K where` once to see VAULT/KB/ASSETS
   $K section ads-and-sponsored-experiences instructions
   $K section ads-and-sponsored-experiences disagree
   $K find "budget per day duration objective targeting" -t ads-and-sponsored-experiences -n 8
   $K find "stop ads organic recommendations sponsored impressions" -n 5
   $K find "creative thumbnail test CTR" -t thumbnails-icons,ads-and-sponsored-experiences -n 6
   ```
   Also grep `<KB>/_tools/AD-PLAYBOOK.md` for the section you need.
3. Gate first: run `bash "$HOME/.claude/claude-kit/tools/pyrun" "$HOME/.claude/claude-kit/vault-mode/.claude/skills/rbx-metrics/compare.py" --d1 <x> --session <x> ...`. If D1, first-session funnel or PTR are below band, the plan is "fix first, retest on <date>"; still produce the plan to run after the gate passes. Official stance in the KB: ads are retrieval and seed data; only organic Home recommendation plays train ranking, so ads cannot rescue a weak game.
4. Arithmetic: `bash "$HOME/.claude/claude-kit/tools/pyrun" "$HOME/.claude/claude-kit/vault-mode/.claude/skills/rbx-ad-plan/adcalc.py" --total <usd> --days <n> [--cost-per-play 0.01 --ctr 2.5 --d1 12 --payer 1.5 --arppu 300]`. Copy its scenario table and checkpoints; they are ESTIMATES.
5. Compose the plan and cite each rule.

## Output template

```
Gate: pass/fail per metric (yours | KB band | flag | source)
Plan: objective, daily vs lifetime budget (sources disagree: show both, pick one), $/day x days = total, targeting, devices/regions
Creatives: 3-5 variants, one variable at a time, equal budget, kill any below ~1% CTR; max active creatives per campaign per docs
Schedule: Day 0 prep, Day 1/3/5/7/10 checkpoints (go / no-go, from adcalc)
Stop rules: organic Home impressions exceed sponsored; no restart loops; pause if D1 of the ad cohort is far below band
Cost: total = ESTIMATE with arithmetic; scenarios good/base/poor
Off-platform add-ons (optional): short video, Discord, creators (cite)
Evidence table: claim | link | flag | date
```

## Rules

- Dollar figures from indie creators are self-reported; label them. Official docs and the live Ads Manager UI override.
- Roblox guidance in the KB: run at least 1-2 weeks, judge after 3-5 days minimum; do not run a 1-2 day test and judge it.
- Never present ROAS or play forecasts as promises.
