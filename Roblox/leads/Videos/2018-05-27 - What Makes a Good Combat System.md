---
title: "What Makes a Good Combat System?"
url: https://youtu.be/8X4fx-YncqA
creator: Game Maker's Toolkit
official: false
advice_density: low
date: 2018-05-27
views: 2029262
transcript: manual-subs
confidence: high
tags: [roblox, leads, youtube-learn]
---

# What Makes a Good Combat System?

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/8X4fx-YncqA) | leads | 2,029,262 views | 2018-05-27

## Summary
Dante's breakdown of melee combat design: attack frame anatomy (anticipation/contact/recovery), animation cancelling, stickiness and range, tactical move niches, parry risk tuning, stun-lock prevention (poise/super armour), enemy design for readable telegraphs, scoring systems, and impact feel via animation, VFX and sound. Not Roblox-specific.

## Tips
- [2:43](https://youtu.be/8X4fx-YncqA?t=163) **[[combat-and-gameplay-systems]]** Split every attack into anticipation, contact and recovery frames; anticipation mostly sets attack speed, and it is when the player is most vulnerable.
- [3:28](https://youtu.be/8X4fx-YncqA?t=208) **[[combat-and-gameplay-systems]]** Decide whether attacks can be cancelled mid-animation; cancelling makes play free-flowing but enemies become more aggressive, while no cancelling makes play deliberate.
- [5:30](https://youtu.be/8X4fx-YncqA?t=330) **[[combat-and-gameplay-systems]]** Give each move a distinct niche with minimal overlap, and give every attack a disadvantage such as slowness, vulnerability, resource cost or cooldown.
- [6:19](https://youtu.be/8X4fx-YncqA?t=379) **[[combat-and-gameplay-systems]]** Get many moves from one attack button using hold for charge and directional input, rather than putting attacks on every button.

## Numbers
- [2:43](https://youtu.be/8X4fx-YncqA?t=163) Light vs heavy attack contact frames (Transformers Devastation): **Light 14 frames, heavy 36 frames**
- [3:28](https://youtu.be/8X4fx-YncqA?t=208) Black Knight Greatsword heavy attack anticipation (Dark Souls): **almost 2 seconds, plus 1-2 seconds recovery**
- [14:38](https://youtu.be/8X4fx-YncqA?t=878) Hit-pause on impact (Transformers): **two characters hold same pose for 3 frames**

## Games
- **Dark Souls** [3:28](https://youtu.be/8X4fx-YncqA?t=208): Heavy attacks have long anticipation and no animation cancelling, making play deliberate; block drains stamina, roll grants invincibility but costs stamina and recovery.
- **Bayonetta** [3:28](https://youtu.be/8X4fx-YncqA?t=208): Any animation can be cancelled into a dodge, giving free-flowing play; dodging at the last second triggers slow-mo Witch Time.
- **Arkham Asylum** [4:38](https://youtu.be/8X4fx-YncqA?t=278): Heavy snapping to enemies makes attack range largely irrelevant.

## Topics
[[combat-and-gameplay-systems]] [[player-psychology-and-game-feel]]

Back to [[leads - How to make successful Roblox games]]
