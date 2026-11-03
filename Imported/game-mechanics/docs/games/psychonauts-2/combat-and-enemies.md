---
title: "Psychonauts 2: Combat & enemies as emotions"
type: game
game: psychonauts-2
patterns:
  - enemy-as-emotion
  - damage-type-matrix
  - diegetic-ui
---

# Combat & enemies as emotions

The bestiary is the best-designed part of the combat and the combat is the worst-reviewed part of the game. Both statements are true, and the gap between them is the interesting thing.

## The roster: every enemy is a named mental process

Nothing in a mental world is a monster. Every hostile entity is a specific negative cognition, given a shape, a behaviour, and a hard counter that matches what it is.

| Enemy | What it is | Behaviour | Counter |
|---|---|---|---|
| **Censor** | The mind's rejection of foreign thoughts | Swarms, stamps things with a "denied" stamp | Melee, generalist |
| **Doubt** | Nagging uncertainty | Sluggish sludge that slows and clings to you | **Pyrokinesis** (highly flammable) |
| **Regret** | A weight you carry about the past | Flies overhead, drops its burden on you | **PSI Blast** only; melee does nothing |
| **Bad Idea** | An intrusive impulse | Erratic, dangerous, hard to pin | Ranged / burst |
| **Panic Attack** | Exactly that | Chaotic, fast, uncontrolled movement | Crowd control |
| **Enabler** | Someone who makes a bad thing invulnerable | Fast, agile support unit that grants nearby enemies invincibility | **Time Bubble**, then kill it first |
| **Bad Mood** | A mood with a cause | Cannot be killed directly | Find and destroy the *source* |

Two of those deserve emphasis:

**The Enabler** is a support enemy whose entire function is to make other bad things invulnerable, and the correct response is to identify it and remove it before addressing anything else. That is a mechanically standard "kill the healer first" unit whose *name* turns it into a statement about how harmful behaviour is sustained. The design is doing double duty with no extra systems cost.

**The Bad Mood** cannot be attacked at all. You have to find what is causing it. A player who has ever tried to argue someone out of a mood recognises the rule immediately.

![A Censor enemy mid-attack with the notepad identification card: "fig. Censor. notes: Attacks thoughts that don't belong"](/images/psychonauts-2/enemy-censor-notecard.jpg)
*The bestiary is delivered as a torn notepad page that slides into frame on first encounter, in Raz's handwriting. Name, sketch, one line of behaviour. It's a tutorial pop-up, a joke, and characterisation in one element, and it never uses the word "tutorial." Coach: "That's just a Censor."*

## The damage-type matrix

Underneath the fiction is a conventional and fairly rigid rock-paper-scissors:

```
Regret        → PSI Blast only
Doubt         → Pyrokinesis (fast), anything else (slow)
Enabler       → Time Bubble, then burst
Censor        → melee/generalist
Bad Mood      → not damage; find the source
mixed wave    → needs 2–3 of the above simultaneously
```

Combined with the [four-slot power limit](./psi-powers.md), a mixed wave can present an enemy you literally cannot damage with your current loadout. The intended reading is "plan your loadout"; the felt experience is "pause and rebind mid-fight."

Schafer framed the enemy design as a deliberate correction to the first game, where players stopped using their powers in the back half: enemies were built to "play off of each other and play off of your powers in new and strategic ways," so different foes force different tools. The intent lands. The delivery has friction.

## Why it doesn't work as well as it reads

Reviewers were consistent, and their criticism is worth recording because it is a general trap:

- **Enemies are damage sponges.** Fights aren't hard; they're long. Health pickups are generous enough that dying is rare, so the tension is low while the duration is high. That combination is the specific recipe for tedium: **low stakes plus long duration**.
- **The early game is one enemy.** The first several hours are mostly Censor waves, which is precisely the generalist enemy with no interesting counter. The roster's best ideas arrive after the player has already formed an opinion about the combat.
- **The counter matrix punishes the loadout system.** A hard counter is only good design if switching to it is cheap. Here it costs a menu.
- **Boss fights repeat their patterns.** Bosses were cut for budget before the Microsoft acquisition and re-added after it, and they read as the least-iterated content in the game.

The underlying lesson: **an enemy roster with hard counters presumes a fast loadout swap.** Get one of those two wrong and the other becomes a liability. If your swap is expensive, prefer soft counters (this enemy is *harder* without the right tool) over hard ones (this enemy is *immune*).

## What it still gets right

- **Naming an enemy after what it does psychologically gets you behaviour design for free.** "Enabler" already tells you it should grant invulnerability to others. "Bad Mood" already tells you it should have a source. The fiction *is* the design document.
- **Non-violence where it counts.** You never fight the person whose mind you are in. You fight their processes, and clearing them is part of leaving the level better than you found it. The game's one significant exception, and its handling, is discussed in the [ludonarrative reading](./ludonarrative-resonance.md).
- **Comedy as a difficulty valve.** A Censor is genuinely funny, which lowers the emotional temperature of a game that is otherwise about trauma. That is deliberate tonal engineering, and it is why the heavy levels land instead of feeling like homework.
