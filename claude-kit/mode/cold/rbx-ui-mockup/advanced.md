<!-- cold: rbx-ui-mockup/advanced.md | read when: the user explicitly asks for generated UI images through the API (never offer it yourself). -->

# Advanced: automatic image generation (quiet path)

Only when `GEMINI_API_KEY` (or `GOOGLE_API_KEY`) is ALREADY in the user's environment; never ask for, store, print or pass a key. `python -I scripts/ui_mock.py gen --project .` builds `ui-mockup/prompts.json` and runs `rbx-thumbnail/scripts/gen_image.py batch` (the only Gemini client in the vault) as a DRY RUN. A real run needs `--go --yes` after you told the user how many images it creates and that the price depends on their plan or API pricing (no price is stored in the vault: check the provider page); if there is no estimate, ask anyway. Results land in `ui-mockup/results/` under the expected names; use them as style hints exactly like manually made images. No local image generation anywhere.
