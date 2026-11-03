---
title: "Psychonauts 2: Traversal & movement feel"
type: game
game: psychonauts-2
patterns:
  - forgiving-platforming-assists
  - one-shot-level-mechanic
---

# Traversal & movement feel

The single most-praised part of the game, and the one that gets written about least, because when platforming feels good nobody can say why.

The short answer for Psychonauts 2: **the moveset is small and the forgiveness layer is large.** Double Fine spent its inventiveness on the levels and its tuning budget on making sure the player never blames the controls for what the level is doing to them.

## The kit

| Verb | Input | Note |
|---|---|---|
| Double jump | Jump ×2 | Baseline |
| Glide | Jump ×3, or Levitation from air | Long, floaty, very controllable descent |
| Levitation ball | Levitation on ground | Ride a psychic ball like a circus balance act; fast, momentum-carrying |
| High jump | Levitation charged | Vertical gain |
| Wall run / ledge grab | Automatic on contact | Heavily magnetised |
| Rail / rope grind | Automatic on contact | Same |
| Mental Connection | Aim at a floating thought bubble, zip | Grapple, but only at authored points |
| Swim, wall-climb, level-specific rigs | Contextual | Per-level, see below |

That is a *small* set for a 2021 3D platformer. There is no wall jump chain, no dash-cancel, no air dash, no combo movement tech. The ceiling is deliberately low.

## The forgiveness layer

What makes it feel good is everything the game does *for* you:

- **Interaction magnetism.** Ledge grabs, rope swings, and rail attachments snap toward you rather than requiring a precise contact. Reviewers consistently note that "you'll very rarely miss your landing."
- **Generous glide.** A double jump plus a long hover means most gaps have a bail-out. The glide is slow enough to be a correction tool, not just a traversal tool.
- **Camera Assist.** An option that steers the camera toward the intended path. It ships as an accessibility feature but functions as a level-readability tool for everyone.
- **Fall damage is a toggle.** Off by default for anyone who wants it off, with no achievement penalty. Falling costs you time, not progress.
- **Death is nearly free.** You respawn immediately, near where you were, with no run loss. Reviewers noted you rarely die at all, and when you do the game barely notices.

The design position here is coherent: **the platforming is a delivery mechanism for the levels, not a test.** If you are here to see what is inside Bob Zanotto's head, the game will not make failing a jump the reason you stop.

Compare this against a movement system built as its own mastery ladder, such as [Mina the Hollower](/games/mina-the-hollower/) where the dodge is also the traversal and the combat, or [Hollow Knight](/games/hollow-knight/), where precision is the point. Psychonauts 2 is on the other end of that axis on purpose.

## Mental Connection: a grapple that is a metaphor

The one genuinely new traversal verb, and it is worth its own note because of *where* it can be used.

Mental Connection zips Raz between floating thought bubbles. It is not a free grapple: the anchor points are authored, visible, and thematically loaded. They are ideas, and connecting them is the act of following a train of thought. In puzzle contexts the same power is used to link concepts in the right order, so the traversal verb and the puzzle verb are literally the same action.

It also structures the hub: the Collective Unconscious is a floating brain with doors orbiting it, reachable only by chaining Mental Connections. Your route through the game's level select is a sequence of thought-jumps.

This is the cleanest small example of the game's whole method: **take a standard genre verb (grapple), and pick the anchor fiction so that using it means something.**

## Per-level movement rigs

On top of the global kit, most mental worlds add one movement system used only there:

- **Ford's Follicles**: hairdryers redirect airflow, and airflow reshapes what is traversable, so the level's geometry is partly a wind puzzle.
- **Loboto's Labyrinth**: dental and mouth geometry, sliding on gums, molar platforms.
- **PSI King's Sensorium**: rainbow bridges that only exist when the right prism is lit.
- **Cassie's Collection**: shrinking into books, so the same shelf is two different spaces at two scales.
- **Bob's Bottles**: bottled memory interiors, entered and exited as discrete pockets.

The pattern holds from [mental worlds](./mental-worlds.md): a stable global movement core, one guest system per level. The guest systems are shallow because they only get one iteration each, but they are never the thing you are fighting, because the core underneath them is reliable.

## What to steal

1. **Decide whether movement is the test or the delivery.** Both are valid. Trouble comes from games that are ambiguous about which, and end up with fiddly platforming *and* forgiving checkpoints.
2. **Magnetism is cheap and enormous.** Snapping ledge grabs and rail attachments cost a few lines and remove most of the "the controls did that, not me" complaints.
3. **Ship the assists as options, not as difficulty modes.** Fall damage off, triple-jump-to-glide, camera assist. Individually toggleable, no achievement penalty, no "Easy" label anyone has to accept about themselves. See [accessibility](./accessibility.md).
4. **Choose your grapple's anchor fiction carefully.** The mechanical difference between a grappling hook and Mental Connection is nearly zero. The narrative difference is the entire game.
