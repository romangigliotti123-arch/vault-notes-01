---
name: thumbnail-maker
description: "Produce a Roblox game's thumbnail set end to end: pick the concept from the core fantasy, capture a real in-game render, compose it (AI art only as a base layer), run the phone-size and spec checks, and output 3-5 one-variable-apart variants plus an upload and test plan. Use after the game has a playable loop and before the first ad or launch."
category: marketing
tags: thumbnail, icon, packaging, ctr, composition, variants, mobile, screenshot, nano banana
kb: Roblox/roblox-kb/thumbnails-icons.md, Roblox/roblox-kb/titles-descriptions.md, Roblox/roblox-kb/discovery-algorithm.md, Roblox/roblox-kb/ab-testing-and-experiments.md, Roblox/roblox-kb/case-studies-grow-a-garden.md
related: game-icon-maker, ctr-ab-test-planner, game-description-writer, game-dev-thumbnail, roblox-thumbnail-brief, roblox-ad-thumbnail-brief, thumbnail-guideline-checker
---

# thumbnail-maker

Packaging gates every other signal: a weak thumbnail means no clicks and no impressions, whatever the game quality (vault: thumbnails-icons, "Treat packaging as gating every other signal"). This skill finishes the job: concept, real render, composition, checks, variants. Image generation itself is `game-dev-thumbnail` (Gemini key, prompts, `gen_image.py`); the brief format is `roblox-thumbnail-brief`. This skill decides WHAT to make and verifies the result.

## When to use
- The game plays and needs its first thumbnail set, or CTR/PTR is low and the thumbnail is the suspect (confirm with `discovery-signal-reader` first).
- Not for: the square icon alone (`game-icon-maker`), ad creative (`roblox-ad-thumbnail-brief`), policy review (`thumbnail-guideline-checker`).

## Inputs (ask at most 3; default the rest)
1. Game name and one-sentence pitch (default: `Games/<slug>/GAME.md` pitch). 2. The hero: the character, pet, vehicle or moment the game is about (default: the most-repeated action of the core loop). 3. Tool access: Studio MCP connected? Gemini key present (`game-dev-thumbnail` checks)? Defaults: files only, prompts only.

## Procedure
1. Freshness: `bash ~/.claude/claude-kit/tools/pyrun ~/.claude/claude-kit/tools/freshness.py --pull thumbnails-icons titles-descriptions` and live-check the CURRENT Creator Hub thumbnail and icon requirements (dimensions, aspect, file size, content rules). Write the numbers you found into `art/thumbnail-plan.md` with the date; never use remembered numbers.
2. Concept (5 minutes of thinking, written down): core fantasy in one line; the single focal subject; the emotion (power, cute, danger, mystery); the implied challenge or unique mechanic; background colour that contrasts with the subject. Rule set from the vault: one clear focal point, 1-2 characters, clean background, high contrast, minimal text (0-3 words), show real gameplay honestly.
3. Capture the real thing. Studio MCP: `list_roblox_studios`, `get_studio_state`, stage the shot (hide UI, pose the hero, camera close and low for scale), `screen_capture`; several angles. Fallback: ask the owner for 3 clean full-screen captures with the HUD hidden (Studio screenshot or F12), or use the Studio camera and a plain background.
4. Make 3-5 distinct concepts (thumbnail personalization serves several active thumbnails and picks winners per audience; the vault says 3-5, retuned hourly, winners in about 48 hours). Each concept differs from the next in ONE variable: subject pose, background colour, emotion, camera distance, or text/no text.
5. Compose each: real render as the base; AI art (via `game-dev-thumbnail`) only for background or the hero when no render exists; add at most one short text; keep key content inside the centre (crops differ by surface).
6. Phone-size check: view each at about 160 px wide (resize with any viewer or a copy). Can you still say what the game is and spot the subject in under a second? If not, enlarge the subject or delete detail.
7. Spec check with the live numbers: `python -I ~/.claude/claude-kit/skillpack/marketing/thumbnail-maker/scripts/image_specs.py art/*.png --expect <WxH from step 1> --aspect <A:B> --max-mb <N>` (exit 1 = a file fails).
8. Write `art/thumbnail-plan.md` (Output below). The owner uploads; you never upload, publish or spend.
9. Hand off to `ctr-ab-test-planner` for the test plan, and set a reminder to refresh the set at major updates.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> stage with `execute_luau` (Edit) only if you need to move the camera or hide parts in the user's named place (ask first; never save the place) -> `screen_capture`. Optional: `insert_asset` / `search_asset` for props; `generate_mesh` for a hero prop. Outputs are files in the project `art/` folder.

## Fallback (no Studio, no image key)
Write `art/thumbnail-plan.md` with the concept table, a shot list for the owner (what to capture, from where), the composition spec and the checks. Mark every image check `untested` until real files exist.

## Evidence
- Official/creator packaging rules: `Roblox/roblox-kb/thumbnails-icons.md` (one focal point; simple composition; check at mobile size; thumbnail personalization with 2-5 active thumbnails; honest gameplay).
- Title and thumbnail work as a pair: `Roblox/roblox-kb/titles-descriptions.md`.
- Click-through gates discovery: `Roblox/roblox-kb/discovery-algorithm.md`; test mechanics: `Roblox/roblox-kb/ab-testing-and-experiments.md`.
- Pattern example (read the pattern, never copy art): `Roblox/roblox-kb/case-studies-grow-a-garden.md`.
- Conflicting views on AI-made icons exist in the vault; `kbq.py section thumbnails-icons disagree` shows both with dates. Raw screenshots and plain AI icons can hurt CTR; a composed final is the plan.

## Output
`art/thumbnail-plan.md`: (1) live specs with source and date, (2) concept table: id, focal subject, emotion, the one variable that differs, text, file, (3) check table per file (phone-size, spec, honesty, IP), (4) upload checklist for the owner, (5) test plan link/handoff. Images in `art/`.

## Acceptance checks (run on your own output)
- [ ] Specs in the plan carry a source URL/date from this run, not memory.
- [ ] Every thumbnail has ONE focal subject and 0-3 words of text.
- [ ] Phone-size look done for each; noted pass/fail.
- [ ] `image_specs.py` exit 0 for every final file (or marked untested if no files).
- [ ] Shown content matches real gameplay (the render came from the game).
- [ ] No real people, brand logos or other games' characters; all-ages.
- [ ] Variants differ by exactly one variable.

## Pitfalls
- Text and logos fine on desktop, unreadable on phones (vault: common mistake). Clutter, clouds and busy backgrounds hurt mobile readability.
- Clickbait that the game cannot deliver raises CTR and lowers retention.
- Changing three things at once makes the test unreadable.
- Do not hard-code Roblox sizes or AI model names in outputs; both change.

## Related
`game-icon-maker`, `ctr-ab-test-planner`, `game-description-writer`, `game-dev-thumbnail` (image generation), `roblox-thumbnail-brief`, `thumbnail-guideline-checker`.
