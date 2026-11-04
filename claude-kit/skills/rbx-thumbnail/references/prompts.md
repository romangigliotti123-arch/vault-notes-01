# Prompt templates for Nano Banana (Gemini image models)

Fill `{...}` from the game plan and the live spec check; put the `STYLE` block verbatim into every prompt of a set. Use plain descriptive sentences (scene, camera, light, composition), not keyword lists; one subject, one action, one background idea per image.

## Shared blocks
```
STYLE: {style words, e.g. bright cartoon 3D render, chunky shapes, soft rim light, saturated candy palette of {color1}, {color2}, {color3}, clean background, no text}
SAFE: friendly, all ages, no weapons aimed at people, no realistic violence, no real people or brands, no Roblox logos or other games' characters.
```
(Style words are placeholders; do not copy another game's look.)

## Character reference sheet (do this first; reuse it as a reference image afterwards)
```
Character design sheet of {character description}, front view, three-quarter view and side view on a plain light background, same proportions in all views, {key colors}, {signature feature}. {STYLE}. {SAFE}
```
Accept one sheet only after checking: same face, same colors, readable silhouette at small size. Save as `art/character-sheet.png` and pass `--ref art/character-sheet.png` in later prompts.

## Icon (square; use the live-checked size and ratio)
```
Square game icon. {Subject: one big character or object filling about two thirds of the frame}, {expression: excited / surprised}, looking at the viewer, {one key prop}. Simple {color} background with a soft glow behind the subject, strong contrast between subject and background, thick clean outline, readable when shrunk to a tiny thumbnail. No text. {STYLE}. {SAFE}
```
Reference images: the character sheet. Variants: expression, background color, prop (change ONE).

## Thumbnail (wide; use the live-checked aspect)
```
Wide key art for a Roblox game: {hero} {action verb} in {setting}, {one clear goal object} in the foreground, depth with a clear foreground, middle ground and background, bright rim light, space on the {left|right} third kept clean for a title added later. One focal point, high contrast, no clutter, readable on a phone screen. {STYLE}. {SAFE}
```
Concepts to produce (3-5, distinct): (1) the hero moment, (2) the reward/collection moment, (3) the social moment (friends together), (4) the "wow" scale shot, (5) mystery/teaser. Title text is better added afterwards in an editor than generated; if generated, keep to 1-3 short words and check spelling.

## Store screenshots (3-6, same look)
```
In-game style screenshot of {feature}: {what the player sees: HUD element, collectible, zone}, third-person camera slightly above and behind the character, {STYLE}, clean uncluttered UI mock with big readable icons and no small text, consistent lighting with the other screenshots in this set.
```
Prefer real, composed captures from the actual build over invented UI (newest vault notes); use generated images for key art and mood, and say which is which.

## Reference photos (what to give the model)
- Character sheet from the step above (best consistency).
- 1-3 screenshots of the real map or character from the build, clean (no HUD clutter, no Studio UI), good light.
- A style board of 2-4 images of the *owner's own* art (not other games') when a look must be matched.
- Up to the model's reference-image limit from the live docs; fewer, cleaner references beat many noisy ones. State what each is for ("image 1 is the character, keep face and colors; image 2 is the setting").

## Consistency tips

Character sheet first and reuse it as a reference, copy the STYLE block verbatim, edit by describing only the change, same aspect ratio per set, re-generate only the weakest image. [cold:rbx-thumbnail/consistency-tips.md] read only when a set of images drifts (different face, colours or style between images).

## A/B variant plan (write to art/ab-plan.md)
| id | what changed (ONE variable) | everything else | hypothesis (from vault note) | metric | winner rule |
Variables to test, one per round: subject (character vs reward), expression, background color, composition (close vs wide), text vs no text. Run with the platform's thumbnail testing as confirmed by the live check; read the per-asset play-through metric, not clicks alone; export results regularly (the platform keeps them a limited time; see the thumbnails-icons note).
