---
title: "Roblox Weapons System - Add Creator Tags for Kills!"
url: https://youtu.be/_ANWj69QDms
creator: SimTek Game Development
official: false
advice_density: low
date: 2021-02-15
views: 15183
transcript: auto-captions
confidence: medium
tags: [roblox, simtekgamedevelopment, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.2
---

> [!note] Trust: TRUSTED (credibility audit score 8.2): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Roblox Weapons System - Add Creator Tags for Kills!

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/_ANWj69QDms) | SimTekGameDevelopment | 15,183 views | 2021-02-15

## Summary
Shows how to add a creator tag (ForceField-style "creator" ObjectValue) to a weapon system's damage callback so the last attacker gets kill credit, then wires a died-event script on zombies to increment a leaderstats Kills value. Includes a basic leaderboard setup and a debounce fix for multiple death events.

## Tips
- [1:25](https://youtu.be/_ANWj69QDms?t=85) **[[combat-and-gameplay-systems]]** In the damage callback, remove existing 'creator' tags from the humanoid, then add a new creator tag pointing to the shooter so last attacker gets kill credit.
- [4:57](https://youtu.be/_ANWj69QDms?t=297) **[[combat-and-gameplay-systems]]** On each enemy, attach a server script listening to Humanoid.Died; read the 'creator' child and increment the attacker's leaderstats Kills value.
- [8:21](https://youtu.be/_ANWj69QDms?t=501) **[[scripting-and-performance]]** Ensure the stat name in the zombie script (e.g. 'Kills') exactly matches the leaderstats value name; mismatches silently fail.
- [9:42](https://youtu.be/_ANWj69QDms?t=582) **[[testing-debugging-and-qa]]** If Humanoid.Died fires multiple times, guard with a boolean flag (canDie) so the kill is only counted once.

## Numbers
- [9:42](https://youtu.be/_ANWj69QDms?t=582) Test spawn count: **4 zombies used for testing** (Test setup; not a performance benchmark)

## Tools
Roblox Studio, Toolbox, Explorer, Ctrl+Shift+F find in files

## Topics
[[combat-and-gameplay-systems]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[SimTekGameDevelopment - How to make successful Roblox games]]
