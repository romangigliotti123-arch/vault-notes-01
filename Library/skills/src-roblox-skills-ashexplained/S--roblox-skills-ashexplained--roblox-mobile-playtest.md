---
id: "roblox-skills-ashexplained/roblox-mobile-playtest"
type: skill
category: "src-roblox-skills-ashexplained"
source: "roblox-skills-ashexplained"
license: "MIT"
repo_path: "sources/roblox-skills-ashexplained/skills/roblox-mobile-playtest/SKILL.md"
description: "Playtest and QA Roblox experiences for mobile and tablet. Use for device simulator checks, touch controls, safe areas, thumb zones, text readability, orientation, HUD overlap, first-action friction, and mobile performance verification through Studio MCP."
orig_name: "roblox-mobile-playtest"
tags: [lib/skill, cat/src-roblox-skills-ashexplained, src/roblox-skills-ashexplained]
---

# roblox-skills-ashexplained/roblox-mobile-playtest

> Playtest and QA Roblox experiences for mobile and tablet. Use for device simulator checks, touch controls, safe areas, thumb zones, text readability, orientation, HUD overlap, first-action friction, and mobile performance verification through Studio MCP.

Type: skill | Category: [[categories/cat-src-roblox-skills-ashexplained|src-roblox-skills-ashexplained]] | Source: [[sources/src-roblox-skills-ashexplained|roblox-skills-ashexplained]] | License: MIT
Repo file: `sources/roblox-skills-ashexplained/skills/roblox-mobile-playtest/SKILL.md` (extra files, if any, sit beside it in the repo)

Related: [[S--roblox-skills-ashexplained--roblox-debugging-bugfix]], [[S--roblox-skills-ashexplained--roblox-playtest-qa]]

---
# Roblox Mobile Playtest

## Goal

Verify that the Roblox experience works and feels good for phone-first players.

## Use Device Simulator

When available, invoke `rbx-device-simulator-lua` before device-specific UI checks. Use it to test phone and tablet form factors, orientation, and layout behavior.

## MCP Workflow

1. Confirm Studio state with `get_studio_state`.
2. Start play mode with `start_stop_play`.
3. Use device simulation when relevant.
4. Exercise controls with `user_mouse_input`, `user_keyboard_input`, and direct character movement through `character_navigation`.
5. Capture evidence with `screen_capture`.
6. Check `get_console_output`.

## Mobile Checks

- First core action is reachable in 10-30 seconds.
- Tap targets are large and spaced apart.
- Important buttons avoid thumb conflict and system gesture zones.
- HUD does not block movement, combat, collection, or objectives.
- Text is readable on phone and tablet sizes.
- Objective markers and reward feedback are visible without opening menus.
- No keyboard-only requirement exists for core play.
- Menus scroll cleanly and do not hide primary actions.
- Performance remains smooth in the first playable area.

## Report Format

Return:

- Devices or simulated form factors checked.
- First-action time.
- Control and HUD issues.
- Readability issues.
- Console or performance risks.
- Highest-impact fixes before launch.

## Next

Run the full first-session pass with `roblox-playtest-qa`, and send any defect to `roblox-debugging-bugfix`.
