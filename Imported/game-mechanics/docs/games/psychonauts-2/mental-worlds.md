---
title: "Psychonauts 2: Mental worlds as level design"
type: game
game: psychonauts-2
patterns:
  - metaphor-as-level
  - one-shot-level-mechanic
  - restorative-level-goal
---

# Mental worlds as level design

The system that makes the game worth studying. A **mental world** is one named character's psychological state built as a playable space, where the art style, the geometry, the enemy mix, the collectibles, and one central mechanic all derive from the same psychological premise.

This is not "a level with a theme." A themed level takes an existing verb set and re-skins it. Psychonauts 2 works the other way: **the psychological concept is the brief, and the verb is derived from it.** That derivation is the whole design method, and it's the reason the game took six years.

## The pipeline: concept → collision → prototype → level

Double Fine's process, as described by Tim Schafer and shown at length in [PsychOdyssey](https://www.doublefine.com/dftv/psychodyssey), ran roughly:

1. **Write conditions on cards.** Candidate levels were psychological states, not places: Peter Pan syndrome, narcissism, performance anxiety, hoarding, addiction, repression.
2. **Collide two nouns.** The productive step is joining a psychological state to an incongruous setting.

   > "The fun part is when you get two concepts that don't really go together like hospital and casino, because they just create more weird things that you don't even think about when you initially have the idea."
   > — Tim Schafer, [NME](https://www.nme.com/features/gaming-features/tim-schafer-says-tolkeins-to-blame-for-psychonauts-2s-nightmarish-teeth-doors-3034961)

3. **Vote, then prototype for two weeks.** The team voted on ideas; winners got a two-week prototype. This is the studio's Amnesia Fortnight habit applied inside a shipping project, and at least one shipped level (Compton's Cookoff) began as an Amnesia Fortnight prototype by a first-time game developer, filmmaker Asif Siddiky.
4. **Improv rather than assembly line.** Art director Lisette Titre-Montgomery's [GDC 2022 talk](https://www.gdcvault.com/play/1027613/The-Art-Direction-of-Psychonauts) frames the key move as abandoning the AAA "siloed departmental assembly line" for hands-on **art-and-design improv**, where artists and designers prototype the metaphor together. The stated result: levels designed around a specific mental concept out-performed generic ones with players.

The cost of this pipeline is that **almost nothing is reusable**, which is exactly what [design tensions](./design-tensions.md) is about.

## The worlds

| Mental world | Whose mind | The condition | The bespoke mechanic |
|---|---|---|---|
| **Loboto's Labyrinth** | Caligosto Loboto, the dentist villain of the first game | A mind literally under interrogation; dental horror | Opening tutorial run: mouth-and-teeth geometry, neon 2D line-art drawn *on* 3D surfaces |
| **Hollis' Classroom** | Hollis Forsythe, second-in-command | Rigid discipline; a nurse's suppressed thrill-seeking | Anatomy-lecture space; Raz plants a suggestion via Mind Melding, which *rewrites the level* |
| **Hollis' Hot Streak** | Hollis again, after the suggestion lands | The suppressed impulse let loose: gambling | Hospital-as-casino. Betting odds, wagers, a "Cardiology Department" turned bookmaker's shop |
| **Compton's Cookoff** | Compton Boole | Performance anxiety and collapse under scrutiny | Timed multitasking across blender / stove / slicer stations, a countdown, and a panel of judges; commercial-break combat waves |
| **PSI King's Sensorium** | The PSI King (a brain in a jar) | Sensory deprivation, then synesthesia | Senses restored one at a time; colour-as-sound rainbow bridges (each stripe plays a note), light-prism puzzles |
| **Ford's Fractured Mind** (Ford's Follicles, Strike City, Cruller's Correspondence, Tomb of the Sharkophagus) | Ford Cruller | A mind deliberately shattered into personality fragments | Four sub-levels in four unrelated genres/styles, each a fragment; hairdryers reshape traversal in Follicles |
| **Cassie's Collection** | Cassie O'Pia | Hoarding, and identity fragmented across her own writing | A colossal library made of paper and printing gear; Raz shrinks into books |
| **Bob's Bottles** | Bob Zanotto | Alcoholism, grief, bottled-up memory | Memories in bottles thrown out to sea; a garden that regrows as memories are recovered |
| **Lucrecia's Lament** | Lucrecia "Lucy" Mux / Nona | Repressed identity and dissociation | A moonlit dreamscape of a drowned city; the level's premise is that its owner does not know who she is |
| **Fatherland Follies** | Gristol Malik | Nationalist self-mythology; a childhood rewritten as propaganda | A theme-park puppet theatre that narrates a *lie* while you play through it |
| **Collective Unconscious** | Everyone | The hub | Floating brain with doors orbiting it, reachable only by Mental Connection grapple |

![Loboto's Labyrinth: Raz running through a giant mouth of teeth and gums](/images/psychonauts-2/lobotos-labyrinth-teeth.jpg)
*Loboto's Labyrinth, the game's first level. The dentist's mind is dental: molar platforms, gum floors, and a mouth ringed with teeth as the level's arch. Schafer, asked about the teeth doors: "let's say it's a homage to Lord of the Rings and the Mouth of Sauron... I just want to shift some of the blame, so yeah, you know, it's Tolkien's fault."*

## Why the "one mechanic per level" rule matters

Almost every mental world introduces a verb, a rule, or a spatial system that the game then never reuses. Cooking stations, betting odds, sense restoration, book-shrinking, memory bottles, propaganda staging. This is the opposite of the standard 3D-platformer economy, where a small verb set (ground pound, wall jump, hover) is recombined across 40 levels.

The trade:

- **Upside:** every level is a genuine surprise, and the level *teaches the character* rather than the moveset. Because the mechanic only exists here, its design can be shaped purely by what the metaphor needs, with no obligation to generalise.
- **Downside:** content cost is close to linear in level count with no economies of scale, and a mechanic used once cannot be tuned across repetitions. Some of the bespoke systems (Cookoff's timer, the Follies' staging) are the least mechanically deep parts of the game precisely because they only get one iteration.

The generalisable version of this pattern for smaller projects: **keep a shared traversal core, and make only one system per level bespoke.** Psychonauts 2 does exactly that. The movement kit ([traversal](./traversal.md)) and PSI powers ([psi-powers](./psi-powers.md)) are global and consistent; the level-specific system sits *on top* of a stable base. It's not a game of 10 unrelated prototypes, it's one platformer with 10 guest mechanics.

## The restorative goal

The stated design constraint that separates Psychonauts 2 from most action games:

> Psychonauts 2 was deliberately designed so that Raz should leave every level in a better condition than when he entered it: the "complete opposite" of what happens in a shooter.
> — Tim Schafer, via [GamesRadar](https://www.gamesradar.com/games/action/psychonauts-2-was-designed-as-the-complete-opposite-of-an-fps-because-tim-schafer-wanted-players-to-leave-levels-in-a-better-condition-than-they-found-them/)

This is load-bearing, not flavour:

- **The win condition is repair.** Bob's garden regrows. The PSI King gets a body. Hollis' hospital is returned to a hospital. The exit state of the level is visibly better than the entry state.
- **It reframes the collectibles.** Reuniting Emotional Baggage with its tag stops a bag crying. Figments are loose thoughts being tidied. See [collectibles](./collectibles-and-rank.md).
- **It bounds the violence.** The things you fight are the person's negative mental processes, not the person. See [combat & enemies](./combat-and-enemies.md).

For the design read of what this does to the game's meaning, see the [ludonarrative reading](./ludonarrative-resonance.md).

## Adjacent reading on this site

- [`handcrafted-pcg-hybrid`](/concepts/handcrafted-pcg-hybrid) is the opposite trade: author units, randomise layout, get scale. Psychonauts 2 authors everything and gets meaning instead of scale.
- [Nier: Automata](/games/nier-automata/) makes the same "form mirrors theme" bet at the level of *structure* (routes, endings, the HUD) rather than at the level of *place*.
- [Mina the Hollower](/games/mina-the-hollower/) and [Hollow Knight](/games/hollow-knight/) are the counter-model: one deep, global verb set explored across many spaces.
