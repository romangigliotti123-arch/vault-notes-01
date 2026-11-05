<!-- cold: rbx-thumbnail/prompts.md | read when: writing the image-model prompt for a candidate icon or thumbnail, or choosing where candidate images come from. -->

# Image-model prompt template for click-aware candidates

Use with `scripts/gen_image.py generate --prompt-file F --aspect 16:9` (the only Gemini client; dry-run by default, needs the user's own key already in the environment), or paste into the Gemini website with the manual Nano Banana steps in [cold:rbx-ui-mockup/manual.md] (read when the user asks how). The basic style blocks, character sheet and reference-photo advice stay in `references/prompts.md`; this template adds the click-psychology slots.

## Candidate sources (every source ends in the same scoring step)
1. `gen_image.py` from this template (user's own key, spend confirmation).
2. Manual Nano Banana: the same prompt pasted by the user into the Gemini website; the user saves the images into `art/`.
3. Blender render (optional, free local install, no key): `scripts/blender_gfx.py detect|gen|check|run`, details and UNTESTED LIVE notes in [cold:rbx-thumbnail/blender.md]; without Blender say the `detect` line and use the other sources.
4. User-supplied images (their own art, an edited screenshot).
Whatever the source: `thumb_score.py inspect` for the file, then LOOK at it and score it (rubric.md). Provenance (source, model, prompt, date) goes next to the image.

## Template (fill every placeholder; no placeholder stays empty)
```
Roblox {asset: icon | thumbnail} for a {genre} game. Aspect {aspect: 1:1 | 16:9}.
Hero: {hero}, expression/emotion: {emotion}. Pose: {action pose and direction}.
Focal point: the hero fills about {35-50}% of the frame, placed in the {left|centre|right} third, eyes or pointing toward {focal: the key object}.
Supporting element (at most one): {second element}. Background: simple, {setting}, soft depth, no clutter.
Palette: {palette}; the subject is much lighter or much darker than the background (strong value contrast); rim light on the hero.
Style: stylised 3D Roblox-like render consistent with the real game ({style notes from the game}); not photorealistic.
Text: {text: none | "WORD" in bold with a thick outline and high contrast, upper or centre area, never in the bottom 15%}.
Keep the key content readable when reduced to 150 px.
Negative: {negative: no logos or characters from other games, no real people, no weapons aimed at anyone, no gore, no fake UI, no Robux or currency imagery, no tiny text, no extra fingers or limbs, no watermark, no clutter, no blur}
```
Placeholders: `{genre}` from the game plan; `{hero}` one noun phrase; `{emotion}` one word; `{palette}` 2-3 colours with the contrast roles; `{focal}` what the eyes or pose point at; `{text}` none or one word; `{aspect}` 16:9 for thumbnails (live-check the spec first), 1:1 for icons; `{negative}` the default list above plus anything the game must not show.

## Make variants that teach something
Generate 4 to 5 candidates that differ in ONE feature group from a control: emotion, hero size, palette, text or no text, action pose, twist. Keep the rest of the prompt verbatim (the STYLE block too). Record the changed feature with `--varies` when the results are logged (protocol.md). Compare each candidate with a real first-minute screenshot before keeping it (rubric gate G1), and with 5-10 competitors (gate G3).

## Do not
Ask the model for another game's look, a named character or a real person; put fake counters, ratings, events or Robux in the image; generate small text and trust it (check spelling at 100%); rely on text for the promise. The provider adds an invisible watermark; follow the live Roblox rules on AI-made images.
