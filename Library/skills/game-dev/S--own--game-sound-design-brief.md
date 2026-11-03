---
id: "game-sound-design-brief"
type: skill
category: "game-dev"
source: "own"
license: "first-party"
repo_path: "skills/game-dev/game-sound-design-brief/SKILL.md"
description: "Create a sound and music brief for a game: sound list by event, mix priorities, loop and file specs, licensing. Use when adding or auditing audio for a Roblox or indie game."
orig_name: "game-sound-design-brief"
tags: [lib/skill, cat/game-dev, src/own]
---

# game-sound-design-brief

> Create a sound and music brief for a game: sound list by event, mix priorities, loop and file specs, licensing. Use when adding or auditing audio for a Roblox or indie game.

Type: skill | Category: [[categories/cat-game-dev|game-dev]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/game-dev/game-sound-design-brief/SKILL.md` (extra files, if any, sit beside it in the repo)

---
# Game sound design brief

1. Event list: every player-facing event gets a row: event | sound character (short adjective set) | length | variations | priority. Cover UI (click, hover, error, purchase), movement, actions, hits, rewards, level-up, ambience per area, music states (menu, explore, tension, win/lose).
2. Mix: priority order = critical feedback (damage, warnings) > player actions > rewards > ambience > music. Music about 10-15 dB under effects; duck music under key cues; loudness consistent across files (normalise, leave headroom, no clipping).
3. Variation: at least 3 variations for frequent sounds, random pitch +/- a few percent, no identical repeats back-to-back.
4. Loops: seamless music loops (cut on beat, check at the loop point), ambience beds 30-60 s, crossfade between area tracks.
5. Specs: mono for positional effects, stereo for music; compressed formats as the engine requires; keep short effects small. For Roblox, audio goes through Creator Hub upload and moderation, uses asset ids, and Roblox licenses its own audio library; verify current upload rules.
6. Licensing: use only CC0, purchased-with-licence, or original audio; record the source and licence per file; no ripped game audio.
7. Accessibility: separate music/effects volume sliders, visual cue for critical audio-only signals.
8. QA: listen on phone speakers and headphones; a 10-minute play session without ear fatigue; check for missing or overlapping sounds in the capture.
