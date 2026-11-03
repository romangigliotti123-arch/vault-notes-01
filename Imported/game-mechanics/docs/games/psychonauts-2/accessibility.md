---
title: "Psychonauts 2: Accessibility as a design surface"
type: game
game: psychonauts-2
patterns:
  - assist-toggles-no-penalty
---

# Accessibility as a design surface

Psychonauts 2 is on this site partly because it is the clearest shipped example of treating the options menu as **a design surface rather than a compliance checklist.** The features cost the game nothing, changed who could finish it, and in at least one case handed a mechanical resource back to the player.

## What shipped

Grouped as Double Fine presented them:

**Gameplay assists**
- **Invincibility** toggle
- **Fall Damage** toggle
- **Narrative Combat** (Raz deals much more damage, so fights resolve fast and the story keeps moving)
- **Camera Shake Intensity** slider
- Colour-blindness options

**Movement and control**
- Fully remappable controls, with overlapping bindings allowed
- **Camera Assist** (steers the camera toward the intended path)
- **Use Triple Jump To Glide**
- **Levitation Ball Pulldown From Glide**
- Lock-on input mode (press versus hold)
- Radial Power Menu input type options
- Camera sensitivity, invert, vibration sliders

**Presentation**
- Font legibility toggle, larger subtitles, localised navigation signage in-world, brightness

## The decision that mattered: no penalty

Every one of these can be toggled at any time and **none of them disable achievements**. There is no "Easy" label to accept, no separate mode to select at the start, no progression locked behind playing a specific way.

> "We've always wanted as many people as possible to play our games. There are people who want to experience parts of the game but can't because of obstacles that we put in the way… there's no reason to exclude people because of that."
> — Tim Schafer, [TheGamer](https://www.thegamer.com/double-fine-interview-psychonauts-2/)

> "We have things that maybe you've seen before like being able to invert camera controls or remap controls... And then we have interesting gameplay assist features to sort of adjust the game according to the experience you want to have. There's a no fall damage toggle, there's an invincibility mode, and then there's narrative combat mode, which makes Raz do more damage."
> — Lauren Scott, senior systems designer, [TheGamer](https://www.thegamer.com/double-fine-interview-psychonauts-2/)

> "There is no 'intended' way to play Psychonauts 2. We encourage players to use these and other options to customize their experience to their personal preferences."
> — Double Fine, via [Can I Play That?](https://caniplaythat.com/2021/05/21/psychonauts-2-accessibility-assist-features-revealed/)

That last sentence is the design position, and it is the one worth arguing about. It is only defensible because of what the game *is*: the value proposition of Psychonauts 2 is seeing what is inside these people's heads, and combat difficulty is not part of the pitch. A game whose pitch *is* the challenge (Hollow Knight, Sekiro) makes this trade differently, and correctly. The lesson is not "always ship invincibility." It is **know what your game is selling, and don't gate it behind something you are not selling.**

## The accidental finding: assists changed exploration, not just fights

Reviewers noted something the design probably did not plan for. Turning on invincibility did not only make combat easier; it **made exploration better**, because collectible hunting in a level full of hazards is a fundamentally different activity from a combat encounter, and it was being taxed by the same damage rules.

That is a real and general observation: **a difficulty setting tuned for combat is silently also a difficulty setting for your exploration layer.** If your game has a collect-a-thon layer under a combat layer, they probably want different tuning, and a toggle is the cheapest way to let the player pick which one they are currently playing.

## The toggle that is secretly a build option

Covered in detail on the [PSI powers](./psi-powers.md#the-fix-double-fine-actually-shipped-in-the-accessibility-menu) page, but it belongs here too:

**Use Triple Jump To Glide** and **Levitation Ball Pulldown From Glide** let you glide and ball without binding Levitation to one of your four power slots. Switch them on and your loadout budget goes from four slots to effectively five.

An accessibility option that expands the build space is an unusual object. It suggests the four-slot budget was one slot too tight and the assist menu was where the fix could ship without re-balancing the game. Whatever the intent, it is a useful precedent: **assist options can carry design corrections that would be expensive to make globally.**

## The content warning

The game opens with a mental-health advisory noting that it contains "artistic interpretations of serious mental conditions." Double Fine's process behind that:

> "After we joined Xbox, we had more access to more research, more testing, and more mental health facilities since we're not actually professionally trained ourselves. They hooked us up with groups who helped us with testing, consulting, and identifying things in the game that were good representations."
> — Tim Schafer, [TheGamer](https://www.thegamer.com/double-fine-interview-psychonauts-2/)

> "Luckily there's a lot of stuff we got right in the first game just because of good intentions, but there was also a lot of stuff that we would do differently. So now with the second game, we're doing a lot more of it with actual intent… What we've always tried to do is approach characters from a point of view of humanity and empathy."
> — Tim Schafer, [TheGamer](https://www.thegamer.com/double-fine-interview-psychonauts-2/)

Worth recording as a process note rather than a mechanic: the sequel's subject matter is the same as the original's, and the difference in reception is largely a difference in *research*. "Good intentions" produced a beloved but occasionally careless 2005 game; consultation produced a 2021 game that won GDC's Best Narrative and is routinely cited as a high-water mark for mental-health representation in games.

## What to steal

1. **Ship assists as independent toggles, not difficulty tiers.** A player who wants no fall damage but full combat damage is a real player.
2. **Don't touch achievements.** The moment an assist costs progression, it becomes a confession rather than an option, and the people who need it most won't use it.
3. **Audit your assists against the exploration layer, not just combat.**
4. **If your subject matter is real people's lives, pay for consultation.** It is cheaper than the reputational cost of getting it wrong, and it demonstrably improved the writing here.
