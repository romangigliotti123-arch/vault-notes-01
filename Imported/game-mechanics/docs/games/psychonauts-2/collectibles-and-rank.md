---
title: "Psychonauts 2: Collectibles & the rank economy"
type: game
game: psychonauts-2
patterns:
  - collectible-as-repair
  - diegetic-ui
  - metaphor-as-level
---

# Collectibles & the rank economy

Psychonauts 2 has a lot of collectibles. What separates it from every other collect-a-thon is that **each collectible type is a different psychological object**, and picking it up means something different as a result.

## The six types

| Collectible | What it is, in fiction | What it does, mechanically |
|---|---|---|
| **Figments** | Loose fragments of imagination, drawn as animated 2D scribbles | Every **100 = +1 Rank**. ~1,300 in the game, so ~13 ranks total |
| **Emotional Baggage** | A crying suitcase, plus its lost luggage tag hidden elsewhere in the level | Reunite bag + tag; every **5 reunions = +1 Rank**, and unlocks a "Primal Memories" concept-art reel |
| **Memory Vaults** | A locked, spinning vault containing a repressed memory | Smash it open, watch a memory film reel; **+1 Rank** each. The level's backstory lives here |
| **Half-A-Minds** | Half of a brain. Find its other half | Two halves = **+1 max health pip** |
| **Nuggets of Wisdom** | Advice from an NPC with a golden marker over them | **+1 Rank** each; 29 in the game |
| **PSI Challenge Markers** | Hidden markers in the real world; pair with a **Core** bought for 25 Psitanium | **+1 Rank** per pairing |

Plus **Psitanium**, the pink crystal currency, which is not a rank source but buys Cores, Pins, consumables, and wallet capacity.

![Raz on a rooftop with three glowing blue bird figments and a green plaid steamer trunk of Emotional Baggage](/images/psychonauts-2/figments-and-baggage.jpg)
*Two collectible types in one frame. The blue birds are Figments, drawn as flat 2D scribbles floating in 3D space, and note that **figments take the shape of something specific to whose mind you are in**: birds here, other motifs elsewhere. The green plaid steamer trunk behind them is Emotional Baggage, waiting for its tag. HUD: Psitanium 181/1,000 (capacity, upgradeable), figments 17/42 for this level, and the small green bar showing "3 to next" rank.*

## Rank: one number, several sources, hard ceiling

Everything above converges on a single stat, **Intern Rank**, and every rank grants exactly one **Intern Credit** to spend on [PSI power upgrades](./psi-powers.md).

```
100 Figments        ─┐
5 Baggage reunions  ─┤
1 Memory Vault      ─┼──→ +1 Intern Rank ──→ +1 Intern Credit ──→ power tier
1 Nugget of Wisdom  ─┤                  └──→ unlocks better Pins in Otto-matic stock
Marker + Core       ─┤
optional missions   ─┘

max Rank = 102, reachable only at 100% completion
```

Two properties worth copying:

1. **Every collectible feeds the same number.** A player who ignores baggage but hoovers figments, and a player who does the opposite, both progress. The economy is *fungible across activities*, so no single collectible type is mandatory. This is the opposite of a checklist.
2. **The ceiling is honest.** Rank 102 requires literally everything. The game does not pretend otherwise, and it puts the per-level totals in the journal so you know exactly what you're signing up for.

![The collectibles journal page for Loboto's Labyrinth: a tooth-shaped jigsaw completion meter with per-type counters](/images/psychonauts-2/collectibles-journal-loboto.jpg)
*The completion tracker as a scrapbook page. The jigsaw is shaped like a molar because this is a dentist's mind, and it fills in as you collect. Figments 80/80, Nuggets of Wisdom 0/2, Half-A-Minds 0/0, five Emotional Baggage slots along the bottom, two Memory Vaults on the right, one already found (glowing). Every counter is legible at a glance and the whole screen is in the fiction's handwriting.*

## Why Emotional Baggage is the good one

If you take one idea from this page, take this one.

An Emotional Baggage collectible is **a pair**: a bag that sits somewhere in the level *audibly crying*, and a luggage tag hidden somewhere else entirely. Neither half does anything alone. Bring the tag to the bag and the bag stops crying, opens, and gives you a reel of that person's memories.

![Five pieces of Emotional Baggage: a pink suitcase, a blue duffel, a green plaid trunk, a yellow hatbox, and a small green purse, all with sad faces](/images/psychonauts-2/emotional-baggage-lineup.png)
*The full set that appears in every mental world: suitcase, duffel, steamer trunk, hatbox, purse. Each has a face. Each is miserable until you find its tag. Five per world, nine worlds.*

![Raz reaching a glowing hatbox tag inside a padded interior, with four PSI power icons bound to LB/LT/RB/RT](/images/psychonauts-2/baggage-tag-and-power-hud.jpg)
*A tag pickup, tucked in a dead-end pocket of the level. The four corner icons are the entire power loadout: LB, LT, RB, RT. Psitanium 701/5,000 after wallet upgrades; 10/47 figments in this level.*

What makes it a good design rather than a cute one:

- **It's a two-part fetch, so it forces coverage.** You cannot complete a bag by finding one thing; you have to have walked two separate parts of the level.
- **The reward is characterisation, not stats.** The payoff is a look at who this person was. The rank contribution is real but secondary.
- **The verb matches the theme.** The literal English idiom "emotional baggage" is rendered as an object that is heavy, that follows the person around, that cries, and that becomes bearable when the thing it belongs to is identified. That is a metaphor doing mechanical work, which is the whole game in miniature.
- **It restates the level's goal.** Every reunion makes the level a slightly happier place, which is the [restorative goal](./mental-worlds.md#the-restorative-goal) at collectible scale.

## The honest criticism

The most common critical note on the game, and the sharpest:

> The omnipresence of collectibles is questionable in a game that has a whole mission dedicated to the problems that can result from compulsive behaviour.

There are around 1,300 figments. **Cassie's Collection is a level about hoarding.** The game asks you to compulsively vacuum up a person's every stray thought and then, in a different level, asks you to think about compulsive accumulation. Nobody at Double Fine appears to have connected the two.

![The in-game explainer popup: "FIGMENTS! FIGMENTS of the imagination are littered all over mental worlds. Your RANK will increase for every 100 you collect!"](/images/psychonauts-2/figments-explainer.jpg)
*The game's own framing. Note the verb: figments are "littered" over mental worlds, and the reward for tidying is rank. The tidying reading is generous; the hoovering reading is the one most completionists actually experience.*

This is the game's one loud ludonarrative seam and it's covered in full in the [resonance reading](./ludonarrative-resonance.md). The design takeaway is not "have fewer collectibles." It is: **if your game says something about a behaviour, check whether your reward loop asks the player to perform it.**

## What to steal

1. **Make each collectible type mean something different.** Six types with six fictions costs no more systemically than six types with one fiction, and it makes the world legible.
2. **Two-part collectibles force coverage without gating.** Bag plus tag beats "find 40 identical things" for the same authoring effort.
3. **Funnel everything into one number.** A single Rank stat fed by every activity means no collectible is mandatory and no play style is punished.
4. **Pay in characterisation where you can.** Memory Vaults and Baggage reels reward exploration with story. It's the cheapest content to author (a slideshow) attached to the most expensive behaviour to motivate (exhaustive search).
5. **Put the counters in the fiction.** A molar-shaped jigsaw completion meter is not harder to build than a progress bar.
