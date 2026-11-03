---
id: "game-feel-checklist"
type: skill
category: "game-dev"
source: "own"
license: "first-party"
repo_path: "skills/game-dev/game-feel-checklist/SKILL.md"
description: "Checklist to improve game feel and juice (input response, feedback, animation, audio, camera, hit reactions) for any engine. Use when a game works but feels flat or when polishing the core action."
orig_name: "game-feel-checklist"
tags: [lib/skill, cat/game-dev, src/own]
---

# game-feel-checklist

> Checklist to improve game feel and juice (input response, feedback, animation, audio, camera, hit reactions) for any engine. Use when a game works but feels flat or when polishing the core action.

Type: skill | Category: [[categories/cat-game-dev|game-dev]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/game-dev/game-feel-checklist/SKILL.md` (extra files, if any, sit beside it in the repo)

---
# Game feel checklist

Pick the one core action (jump, shoot, collect, swing, place). Improve it in this order and re-test after each step.

1. Input: response under about 100 ms from press to visible change; input buffering and coyote time for platforming; consistent controls on touch, mouse/keyboard and gamepad.
2. Immediate feedback on every action: sound within the same frame, a visual change (scale pop, flash, particles), a number or UI reaction. Missing feedback is the top cause of "flat".
3. Animation: anticipation, action, follow-through; ease curves instead of linear; short durations (80-250 ms for most feedback).
4. Impact: hit-stop (very short freeze), camera shake scaled to power, knock-back, damage numbers, distinct sounds per material/weapon.
5. Rewards: collection feels escalating (pitch up per combo, bigger pop for rarer item), progress bars animate, level-up is a moment.
6. Camera: smoothing, look-ahead, FOV kicks for speed, never nauseating; offer a reduce-motion/shake option.
7. Audio: layered, varied (3+ variations to avoid repetition), ducking so key cues are heard, volume mix, no clipping.
8. Restraint: effects must not hide gameplay information or hurt low-end device frame rate; test on the weakest target device.
9. Accessibility: no flashing above safe rates, colour-blind-safe cues, settings for shake, volume, and vibration.

Report: action tested | what was missing | change | before/after notes from a recorded play session.
