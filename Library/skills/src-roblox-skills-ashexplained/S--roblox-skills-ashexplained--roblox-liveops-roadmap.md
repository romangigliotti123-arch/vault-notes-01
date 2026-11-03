---
id: "roblox-skills-ashexplained/roblox-liveops-roadmap"
type: skill
category: "src-roblox-skills-ashexplained"
source: "roblox-skills-ashexplained"
license: "MIT"
repo_path: "sources/roblox-skills-ashexplained/skills/roblox-liveops-roadmap/SKILL.md"
description: "Plan Roblox live ops, update cadence, event systems, retention milestones, roadmap checkboxes, approval gates, content pacing, Day-1/Day-3/Day-7 hooks, quests, rewards, and release-ready task sequencing."
orig_name: "roblox-liveops-roadmap"
tags: [lib/skill, cat/src-roblox-skills-ashexplained, src/roblox-skills-ashexplained]
---

# roblox-skills-ashexplained/roblox-liveops-roadmap

> Plan Roblox live ops, update cadence, event systems, retention milestones, roadmap checkboxes, approval gates, content pacing, Day-1/Day-3/Day-7 hooks, quests, rewards, and release-ready task sequencing.

Type: skill | Category: [[categories/cat-src-roblox-skills-ashexplained|src-roblox-skills-ashexplained]] | Source: [[sources/src-roblox-skills-ashexplained|roblox-skills-ashexplained]] | License: MIT
Repo file: `sources/roblox-skills-ashexplained/skills/roblox-liveops-roadmap/SKILL.md` (extra files, if any, sit beside it in the repo)

Related: [[S--roblox-skills-ashexplained--roblox-release-operations]], [[S--roblox-skills-ashexplained--roblox-to-issues]]

---
# Roblox Live Ops Roadmap

## Goal

Turn a Roblox idea into a shippable, updateable game plan that protects retention and avoids premature polish.

## Roadmap Discipline

- Read project roadmap and instruction files before choosing work.
- Resume from the first unchecked item unless the user redirects.
- Mark an item complete only after implementation, testing/playtesting, and explicit human approval.
- Use an awaiting-approval marker for work that is built and tested but not approved.
- Keep current-state notes in sync with what was actually shipped.

## First Week Design

- Day 1: immediate fun, clear loop, first reward, first goal.
- Day 2: daily streak, unfinished objective, or friend/social reason to return.
- Day 3: unlock meaningful new content around 2-3 hours of play.
- Days 4-6: visible medium-term goals, collection progress, social identity.
- Day 7: advertised reward or milestone visible from Day 1.

## Update Cadence

Plan updates around:

- New zones, modes, enemies, quests, pets, cosmetics, or upgrades.
- Limited events and seasonal items.
- Balance changes driven by funnel and retention data.
- Social goals that encourage friends to return together.

## Task Sequencing

Prioritize:

1. Core action and reward loop.
2. Progression signals and save/load.
3. Social and return hooks.
4. Mobile UX and performance.
5. Monetization that fits the loop.
6. Content expansion and live events.

## Output Format

For roadmap work, provide:

- Current phase.
- Next buildable milestone.
- Acceptance criteria.
- Playtest criteria.
- Approval gate.
- Risks to retention, monetization fairness, or mobile performance.

## Next

Break the roadmap into playtestable slices with `roblox-to-issues`, and ship each update through `roblox-release-operations`.
