<!-- cold: rbx-ui-mockup/manual.md | read when: the user asks about the manual Nano Banana 2.1 mode, its Gemini-website steps, limits or what the package contains. -->

# Manual mode (preference on): what the user does

`/rbx-mockup on` stores the preference; the next UI step builds `ui-mockup/` with `ui_mock.py package`: `prompts/00-style-sheet.md` then one prompt per screen (text placeholders `[TITLE]`, `[BUTTON]`, `[NUMBER]` only), `references/` (the user's own screenshots, the automatic design sheet frames as layout references), `INSTRUCTIONS.md` (numbered steps), `CHECKLIST.md`, `status.json`, an empty `results/`.

After the images arrive the user can say `prototype this mockup` (with the images in the game folder): `rbx-ui-prototype` reads them and writes one clickable HTML prototype in `ui/prototype/` (buttons, animations, screen navigation, fake coins, device switcher) plus a Roblox handoff for `rbx-ui`. It is a stand-in, never the game.

## What Google says (read 2026-11-05; state only this, never "free")
- Help page https://support.google.com/gemini/answer/14286560 : you must be signed in; on the web open the left sidebar and choose Images; Nano Banana 2 is used with the Flash and Pro Gemini models and accepts several reference images; Nano Banana Pro is for regenerating with more detail and needs a Google AI plan; downloads are 2K with a plan and 1K without one; personal accounts need age 13+ to generate (18+ to edit).
- Limits page https://support.google.com/gemini/answer/16275805 : usage limits are compute-based, depend on your plan, image requests use more of your limit, limits may change without notice; check your own under Gemini Settings > Usage Limits. The pages give no image counts. Say "limits depend on your Gemini plan".
- The help pages name the model Nano Banana 2; Google's API pricing page lists `gemini-nano-banana-2.1`. Tell the user to pick the newest Nano Banana the model picker offers (2.1 if shown).

## Why this mode never blocks
Layout, spec, build and compare come from the automatic design sheet, so the agent keeps working. Images only add style (colours, icon style, decoration). When the user drops `results/style-sheet.png` and `results/<screen>.png`, `ui_mock.py status .` reports them; read them with the Read tool next to the design frame, adjust Theme colours or icon choices, never layout or text. An image that disagrees with the spec rectangles is ignored for layout.

## Rules for the images
No real brand, character or other game's UI as a reference; every upload to Roblox still passes moderation; keep the prompt, model name and date next to the asset (ui_assets.py `source`); Google's terms apply to the user's own account (the user decides); Roblox's AI-disclosure form is about PLAYER-facing AI, not about how art was made.
