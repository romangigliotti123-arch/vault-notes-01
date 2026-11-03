---
title: "Psychonauts 2: PSI powers & the four-slot radial"
type: game
game: psychonauts-2
patterns:
  - loadout-as-budget
  - opportunity-cost-loadout
  - diegetic-ui
---

# PSI powers & the four-slot radial

Raz accumulates roughly nine psychic powers over the campaign. He can have **four bound at once**, on the two shoulders and two triggers, with melee always available. Everything else lives behind a pause-menu reassignment.

That single number, four, is the game's build system, its most-cited friction point, and a clean example of [`loadout-as-budget`](/concepts/loadout-as-budget) with an unusual property: **traversal and combat compete for the same slots.**

## The catalogue

| Power | Verb | Primarily |
|---|---|---|
| **Melee (Psi-Punch)** | Punch, dash-strike | Always bound, not a slot |
| **Telekinesis** | Grab, carry, throw objects and enemies | Combat + puzzle |
| **Pyrokinesis** | Ignite a target, damage over time | Combat (hard-counters Doubts) |
| **PSI Blast** | Ranged projectile | Combat (the only thing that hurts Regrets) |
| **Levitation** | Ball to roll on, glide, high jump | **Traversal** |
| **Mental Connection** | Grapple-zip between floating thought bubbles | **Traversal** + puzzle |
| **Time Bubble** | Slow objects and enemies in a radius | Puzzle + crowd control (counters Enablers) |
| **Clairvoyance** | See through another creature's eyes | Puzzle + secret-finding |
| **Projection** | Summon an Archetype cutout to distract and press things | Puzzle + combat support |
| **Mind Melding** | Enter a mind / plant a suggestion | Story, not a slot power |

![The PSI powers journal open on Pyrokinesis, showing its four upgrade ranks](/images/psychonauts-2/psi-powers-journal.jpg)
*The upgrade screen as a merit-badge scrapbook. Pyrokinesis has four tiers: I Base Power ("Conjure fire with your mind to inflict damage over time"), II Bonfire ("burns a larger area"), III Slow Cooker ("damage duration is increased"), IV locked behind "RANK 20: Très Bon Fire." Note the counter at the bottom left: "Intern Credit Available: 0."*

## The upgrade economy

Two currencies, two shops, one gate.

- **Intern Credits** buy power ranks. You earn **one credit per Intern Rank**, and rank comes from collectibles (see [collectibles & rank](./collectibles-and-rank.md)). Each power has four tiers.
- **Rank thresholds gate the top tier.** Tier IV upgrades carry a hard rank requirement ("RANK 20") on top of their credit cost, so the strongest version of a power is locked behind *exploration volume*, not just spending.
- **Psitanium** (the pink crystal currency) buys consumables, carrying-capacity upgrades, PSI Challenge Cores, and **Pins** at Otto-matic vending machines.

**Pins** are the second loadout layer: **three equipped at a time**, bought for roughly 100–750 Psitanium, giving passive modifiers (health regeneration, power tweaks) or pure cosmetics. Unlike rank upgrades, pins are non-permanent and swappable, so they're the low-stakes tuning knob sitting under the high-stakes power slots.

The whole progression therefore reads:

```
explore → collectibles → Rank ↑ → +1 Intern Credit → power tier (permanent)
                            └──→ unlocks better Pins in the shop
combat/props → Psitanium → Pins (3 slots, swappable) + capacity + Cores
                              └── Cores + PSI Challenge Markers → more Rank
```

Note the loop closing on itself: Psitanium buys Cores, Cores pair with found Markers to buy Rank, Rank buys Credits. Money converts into progression at a fixed exchange rate, which is why the wallet-capacity upgrade matters more than it looks.

## Why four slots is the interesting number

Most action-game loadout budgets partition *combat* options. Psychonauts 2 puts **movement in the same budget**. Levitation (your glide and ball) and Mental Connection (your grapple) are slot powers, so a full combat build costs you mobility, and a full traversal build costs you damage type.

That makes the trade sharper than it first appears:

| If you slot | You gain | You give up |
|---|---|---|
| Levitation + Mental Connection + 2 combat | Full mobility, comfortable exploration | One damage type, so some enemy mixes have no clean answer |
| 4 combat powers | Every enemy hard-counter available | Glide and grapple, so half the level is unreachable |
| Time Bubble + Clairvoyance + 2 | Puzzle and secret-hunting throughput | Sustained damage, so fights drag |

The intended play is **contextual re-equipping**: platforming loadout for traversal stretches, combat loadout for arenas. The game's own level design pushes you into it, because most levels alternate the two.

## Where the design breaks

This is the most consistently criticised system in the game, and the criticism is well-founded.

- **Swapping costs a pause.** Reassigning a power means opening the journal and rebinding, mid-level, sometimes mid-arena. There is no second loadout page, no quick-swap deck, no auto-swap on context.
- **The enemy design assumes you have the counter equipped.** Regrets can only be damaged with PSI Blast; Doubts are hard-countered by Pyrokinesis; Enablers want Time Bubble. Mixed waves therefore either require a pre-planned loadout or a mid-fight menu trip. See [combat & enemies](./combat-and-enemies.md).
- **Two of the slots are effectively pre-spent.** Most players keep Levitation and one grapple/damage staple bound permanently, so the real choice space is two slots, not four. When part of a budget is functionally mandatory, the budget is smaller than the UI implies.

Wikipedia's reception summary names it plainly: "the limitation of having a maximum four abilities equipped at once was a common complaint."

### The fix Double Fine actually shipped, in the accessibility menu

Buried in the options are two toggles that quietly **give a slot back**:

- **Use Triple Jump To Glide** activates the glide without Levitation bound to a button.
- **Levitation Ball Pulldown From Glide** drops you into the ball from a glide, likewise without binding Levitation.

Turn both on and you have freed one of four slots, permanently, by changing an accessibility setting. This is either a beautiful piece of design or an admission that the budget was one slot too tight, and it is probably both. It is also the clearest example on this site of an accessibility option that is *mechanically* a build-space expansion. See [accessibility](./accessibility.md).

## The lesson

The generalisable version, for anyone building a slot budget:

1. **Putting traversal in the combat budget makes the trade real**, because both halves of the game are now bidding for the same space. It is a strong design if and only if the swap is cheap.
2. **If swapping is expensive, the budget must be generous.** Psychonauts 2 chose an expensive swap *and* a tight budget, and reviewers felt it. [Nier: Automata](/games/nier-automata/chip-system) makes the opposite call: a similarly tight chip budget, but three saved loadout Sets you can flip between instantly.
3. **Watch for pre-spent slots.** If a slot is effectively mandatory, subtract it from the budget when you tune. A 4-slot budget with 2 mandatory slots is a 2-slot budget with extra UI.
