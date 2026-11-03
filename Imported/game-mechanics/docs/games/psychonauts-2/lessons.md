---
title: "Psychonauts 2: Lessons"
type: game
game: psychonauts-2
---

# What I'd steal (and what I'd avoid)

Opinionated takeaways for my own (Godot) projects.

## Steal

### 1. Write the level brief as a psychology, not a place

The single most transferable idea in the game. Instead of "ice level, lava level, sewer level," the brief is "performance anxiety," "hoarding," "repressed identity." A place brief tells you what the level looks like. A psychology brief tells you what the level *does to the player*, which is the part you actually have to design.

Concretely: before laying out geometry, write one sentence about the person whose space this is and what is wrong with them. Then ask what mechanic would make the player feel that. Compton crumbles under pressure, therefore a timer, competing stations, and a panel of judges. The mechanic is derived, not decorated.

### 2. Collide two nouns that don't belong together

Hospital + casino. Dentist + labyrinth. Nationalist rally + puppet theatre. This is a five-minute exercise, it costs nothing, and it reliably produces things you would not have thought of from either noun alone. Schafer's own warning applies: the method generates more good ideas than you can afford, so **the discipline is refusing them, not having them.**

### 3. One guest mechanic per level, on a stable core

The structure that makes the bespoke-everything approach survivable: a global movement kit and power set that never changes, with exactly one level-specific system layered on top. The player always knows how to move and fight; the surprise is always additive. For a small project this is affordable in a way that "ten unrelated prototypes" is not.

### 4. Two-part collectibles

Emotional Baggage: a crying bag in one part of the level, its luggage tag in another. Neither does anything alone. You cannot complete it without covering two separate areas, and the reward is characterisation rather than a stat.

This is strictly better than "find 40 identical things" for the same authoring cost, and it is trivially portable. Any pair of objects with a shared identity works: a key and a lock, a letter and a recipient, a photograph and the place it was taken.

### 5. Funnel every collectible into one fungible number

Six collectible types, all converting into Intern Rank at published exchange rates. Result: no collectible type is mandatory, no play style is punished, and the completionist and the tourist are on the same progression curve at different speeds. Compare a checklist economy, where missing one category blocks a reward entirely.

### 6. Ship the assists as toggles, not as difficulty tiers, and don't touch achievements

Invincibility, fall damage off, Narrative Combat, camera assist. Individually switchable at any time, no penalty, no label anyone has to accept about themselves. The moment an assist costs progression it becomes a confession, and the players who need it most stop using it.

The corollary I hadn't considered before this game: **a difficulty setting tuned for combat is silently also a difficulty setting for your exploration layer.** Reviewers found invincibility improved collectible hunting more than it improved fights. If your game has both layers, they probably want separate dials.

### 7. Put the UI in the fiction's handwriting

A molar-shaped completion jigsaw is no harder to build than a progress bar. A merit-badge upgrade page is no harder than a skill grid. A torn notepad that slides in with an enemy's name and one behaviour line is a tutorial pop-up that nobody experiences as a tutorial pop-up. This is the cheapest characterisation available and Psychonauts 2 takes all of it.

### 8. Give the player a restorative goal

"Leave the level better than you found it" changes the meaning of every verb without changing any of them. It costs a design rule and some exit-state art. It is available to almost any game and almost nobody uses it.

### 9. When the style breaks readability, add a diegetic contrast element and give it a job

The Sensorium's green-on-green palette and 2D shaders destroyed depth perception. The fix was light prisms and rainbow bridges, high-contrast objects that carry the wayfinding load, which then became a mechanic (each stripe plays a note). The general form: **don't soften the style, add a legible object and make it earn its place.**

### 10. If your subject matter is real people's lives, pay for consultation

The difference between the 2005 game (good intentions, occasionally careless) and the 2021 game (GDC Best Narrative) is largely research. Double Fine got access to mental-health consultants after joining Xbox and used them for testing, representation review, and language. This is a line item, not a virtue.

## Handle with care

### 11. Hard counters presume a cheap loadout swap

Regrets take damage only from PSI Blast. If PSI Blast is not in your four slots, you pause the game. The enemy design and the loadout design were built to different assumptions, and reviewers felt the gap for the whole campaign.

Rule I'm taking away: **hard counters and expensive swapping cannot coexist.** Pick one. Either make swapping instant (Nier: Automata's three saved chip Sets), or make counters soft, where the wrong tool is slower rather than useless.

### 12. Subtract your mandatory slots before you tune the budget

Most players permanently bound Levitation and one staple, so the advertised four-slot budget was a two-slot budget wearing four slots of UI. When auditing any loadout system: count how many slots a competent player will never change, and treat the rest as the real budget.

### 13. Low stakes plus long duration is the recipe for tedium

Psychonauts 2's fights are not hard (health is generous, death is nearly free) but enemies are damage sponges, so encounters are long. That combination is worse than either difficult-and-short or easy-and-short. If you are going to be generous with failure, **be aggressive about pacing**, because you have removed the tension that was covering for the length.

### 14. Audit your inherited systems against your theme

The collectible economy came from a 2005 platformer. The subject matter came from a 2021 conversation about mental health. They contradict each other exactly once, at Cassie's Collection, a level about hoarding sitting inside a 1,300-figment collect-a-thon.

Dissonance almost never comes from a bad new decision. It comes from a decision that was correct in the genre you inherited and is no longer correct in the game you are actually making. **New systems get scrutinised; inherited ones don't. Inherited ones are where the problem is.**

### 15. Bespoke everything is a schedule commitment, not just a budget one

Six years, an estimated $10–13.5M, boss fights cut for money and only restored because a platform holder bought the studio mid-development, all to ship a ~15 hour game with no reusable level content. It won Best Narrative and it is Double Fine's best-selling game, and the studio's subsequent direction has been toward smaller projects.

For a solo or small-team project the honest version of this lesson is: **you can afford the method at a smaller N.** Three bespoke levels built this way will outperform twelve generic ones, and three is a number you can actually finish. The method scales down better than it scales up.

## Watch the documentary

[PsychOdyssey](https://www.doublefine.com/dftv/psychodyssey), 32 episodes, ~22 hours, free. It is the most detailed record of medium-scale game development that exists: prototypes that don't work, features cut and re-added, morale, money, and an episode called "Villains of Crunch Mode." Nothing else on this site comes with primary-source video of the decisions being made.
