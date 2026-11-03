---
id: "roblox-skills-ashexplained/roblox-combat-systems"
type: skill
category: "src-roblox-skills-ashexplained"
source: "roblox-skills-ashexplained"
license: "MIT"
repo_path: "sources/roblox-skills-ashexplained/skills/roblox-combat-systems/SKILL.md"
description: "Design, implement, and review Roblox combat systems. Use for melee, ranged, abilities, cooldowns, hit detection, damage validation, status effects, enemy AI hooks, combat UI, balance knobs, VFX/SFX, and exploit-resistant remotes."
orig_name: "roblox-combat-systems"
tags: [lib/skill, cat/src-roblox-skills-ashexplained, src/roblox-skills-ashexplained]
---

# roblox-skills-ashexplained/roblox-combat-systems

> Design, implement, and review Roblox combat systems. Use for melee, ranged, abilities, cooldowns, hit detection, damage validation, status effects, enemy AI hooks, combat UI, balance knobs, VFX/SFX, and exploit-resistant remotes.

Type: skill | Category: [[categories/cat-src-roblox-skills-ashexplained|src-roblox-skills-ashexplained]] | Source: [[sources/src-roblox-skills-ashexplained|roblox-skills-ashexplained]] | License: MIT
Repo file: `sources/roblox-skills-ashexplained/skills/roblox-combat-systems/SKILL.md` (extra files, if any, sit beside it in the repo)

Related: [[S--roblox-skills-ashexplained--roblox-animation-audio-feedback]], [[S--roblox-skills-ashexplained--roblox-mobile-playtest]], [[S--roblox-skills-ashexplained--roblox-playtest-qa]], [[S--roblox-skills-ashexplained--roblox-security-economy]]

---
# Roblox Combat Systems

## Goal

Make combat readable, responsive, and server-authoritative.

## Authority

- Let the client request intent, animation, aim direction, or target candidate.
- Let the server validate range, cooldown, line of sight, team, state, and damage.
- Never let the client decide final hit, damage, reward, kill credit, or loot.
- Rate-limit combat remotes.
- Use deterministic balance tables shared or mirrored carefully.

## Combat Loop

Design:

- Anticipation, action, impact, recovery.
- Clear cooldowns and ability availability.
- Strong feedback for hit, miss, crit, block, dodge, and death.
- Enemy tells and fair counterplay.
- Early encounters that teach through safe repetition.

## Implementation Areas

- Hitboxes and raycasts.
- Cooldown and stamina/energy systems.
- Damage types and modifiers.
- Status effects with duration, stacking, and cleanup.
- Enemy AI target selection and leash rules.
- Reward grants tied to server-confirmed contribution.

## MCP Workflow

1. Locate combat scripts with `script_search` and `script_grep`.
2. Read attack, damage, enemy, and reward scripts with `script_read`.
3. Inspect remotes and combat instances with `search_game_tree` and `inspect_instance`.
4. Edit with `multi_edit`.
5. Playtest attacks using `start_stop_play`, `user_keyboard_input`, `user_mouse_input`, and `screen_capture`.
6. Check `get_console_output`.

## Output

Return:

- Combat state flow.
- Server validations.
- Balance knobs.
- Feedback hooks.
- Exploit and regression tests.

## Next

Validate every combat remote and damage path with `roblox-security-economy`, add impact with `roblox-animation-audio-feedback`, and verify with `roblox-playtest-qa` and `roblox-mobile-playtest`.
