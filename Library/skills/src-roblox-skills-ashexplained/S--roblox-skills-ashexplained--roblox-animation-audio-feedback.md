---
id: "roblox-skills-ashexplained/roblox-animation-audio-feedback"
type: skill
category: "src-roblox-skills-ashexplained"
source: "roblox-skills-ashexplained"
license: "MIT"
repo_path: "sources/roblox-skills-ashexplained/skills/roblox-animation-audio-feedback/SKILL.md"
description: "Improve Roblox feel through animation, audio, VFX, haptics-like feedback, reward juice, movement feel, combat feedback, UI transitions, emotes, and satisfying loop feedback without hurting mobile performance."
orig_name: "roblox-animation-audio-feedback"
tags: [lib/skill, cat/src-roblox-skills-ashexplained, src/roblox-skills-ashexplained]
---

# roblox-skills-ashexplained/roblox-animation-audio-feedback

> Improve Roblox feel through animation, audio, VFX, haptics-like feedback, reward juice, movement feel, combat feedback, UI transitions, emotes, and satisfying loop feedback without hurting mobile performance.

Type: skill | Category: [[categories/cat-src-roblox-skills-ashexplained|src-roblox-skills-ashexplained]] | Source: [[sources/src-roblox-skills-ashexplained|roblox-skills-ashexplained]] | License: MIT
Repo file: `sources/roblox-skills-ashexplained/skills/roblox-animation-audio-feedback/SKILL.md` (extra files, if any, sit beside it in the repo)

Related: [[S--roblox-skills-ashexplained--roblox-mobile-playtest]], [[S--roblox-skills-ashexplained--roblox-performance-optimization]]

---
# Roblox Animation Audio Feedback

## Goal

Make every core action feel satisfying and understandable.

## Feedback Stack

Use layered feedback:

- Animation: anticipation, impact, recovery.
- Sound: action, hit, reward, failure, purchase, unlock.
- VFX: particles, highlights, trails, popups, camera-safe effects.
- UI: counters tick, bars fill, buttons press, reward deltas appear.
- World response: object changes, enemy reaction, collectible burst.

## Rules

- Feedback must clarify state, not obscure it.
- Keep first-session effects readable and quick.
- Budget particles, transparency, lights, and looping sounds for mobile.
- Use consistent audio language for success, danger, rarity, and progression.
- Make rare rewards feel distinct without requiring long animations.

## MCP Workflow

1. Search scripts and assets for animation, sound, reward, and effect hooks.
2. Inspect relevant instances with `search_game_tree` and `inspect_instance`.
3. Use `search_asset` for audio/visual assets before generating new ones.
4. Patch trigger code with `multi_edit` or use `execute_luau` for instance setup.
5. Playtest and capture with `screen_capture`.
6. Check `get_console_output`.

## Output

Return:

- Feedback moments.
- Asset or effect choices.
- Trigger ownership.
- Mobile performance risks.
- Verification notes.

## Next

Confirm the added juice does not hurt mobile frame rate with `roblox-performance-optimization` and `roblox-mobile-playtest`.
