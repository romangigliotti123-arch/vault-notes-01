# Content-rules and quality checklist (run on every prompt before generating and every image after)

Source of truth for the rules: the live Roblox Community Standards and Creator Hub thumbnail/icon requirements found in the live check, plus `Roblox/roblox-kb/age-ratings-moderation-and-tos.md` and `thumbnails-icons.md` in the vault. If this list and a live official page differ, the live page wins; say so.

## Roblox rules (all must pass)
- [ ] All ages: no gore, realistic violence, weapons pointed at people, sexual or suggestive content, drugs, hate symbols, self-harm, scary imagery that would mislead a young audience.
- [ ] No real people, celebrities, brands, logos, or trademarked characters; no other game's characters, art or UI; no Roblox logo misuse.
- [ ] No misleading content: the image shows what the game really offers (the vault: thumbnail must match the first minute); no fake Robux/rewards, fake ratings, "official" claims, or fake UI that is not in the game.
- [ ] No pressure or gambling imagery aimed at kids (countdown FOMO, loot-box/spin visuals presented as paid randomness).
- [ ] No text claims that break the rules (no "free Robux", no off-platform links, no social handles unless the live rules allow).
- [ ] Right size, ratio, file type and file size as per the live spec (write the numbers from the live check here: ______ ).
- [ ] AI-image disclosure and watermark: the provider adds an invisible watermark; follow any Roblox rule on AI-generated content found in the live check (write result: ______ ).

## Quality (from the vault's thumbnail notes; check dates in the note)
- [ ] One focal point, 1-2 characters, simple background, strong contrast.
- [ ] Large emotive face or clear hero object filling the frame.
- [ ] Readable at phone size (shrink the image to about icon size and look).
- [ ] Text: none, or 1-3 short words, big, high contrast, spelled right.
- [ ] Matches the first 30 seconds of the game (no bait and switch).
- [ ] Not a raw screenshot and not an unedited AI image if the newest vault note still advises against it (state the note date); composed final reviewed by the owner.
- [ ] Hands, faces, extra limbs, garbled text: no artifacts.
- [ ] Set consistency: same character, palette and style across the set.

Result per image: PASS / FIX (what) / REJECT (why). Never mark PASS without looking at the image.

## Score and test (click psychology)
Candidate prompt template with the click slots: [cold:rbx-thumbnail/prompts.md] read when writing any icon or thumbnail prompt.
1. File: `python -I ~/.claude/claude-kit/vault-mode/.claude/skills/rbx-thumbnail/scripts/thumb_score.py inspect <image> [--kind icon]` (size, 16:9 or square, under 3 MB, bottom-edge note).
2. Look at the image at full size and at about 150 px, then `thumb_score.py template` and fill gates G1-G3 (pass/fail) and checks 1-13 (0/1/2): [cold:rbx-thumbnail/rubric.md] read before scoring (anchors, weights, ASSUMPTION labels).
3. `thumb_score.py score S.json --write Games/<slug>` ranks 2-5 variants and writes `thumb-score/gate.json`. Pass = no failed gate and 32 of 46 (assumption); fix the 3 lowest checks, cap 3 rounds. No game folder: omit `--write`.
4. Report `thumbnail: scored <score>/<max> (variants N)`, or `thumb_score.py skip --reason "<why>" --write Games/<slug>` for `thumbnail: skipped: <reason>` (hotfix, no store page yet, user declined). Advisory: it never blocks.
5. Why a check matters, with evidence grades A/B/C: [cold:rbx-thumbnail/principles.md] read when explaining a score or choosing what to vary. An idea that bends the truth: [cold:rbx-thumbnail/fair.md] read first.
6. After the user runs a Roblox thumbnail personalization test: [cold:rbx-thumbnail/protocol.md] read for the steps, then `python -I ~/.claude/claude-kit/tools/thumb_record.py add|decide|summary` (local ledger in `claude-kit/state/thumbnails/`; sharing is opt-in via `thumb_record.py share on`).
7. A hiccup in this work (tool error, bad file, repeat fix round): `python -I ~/.claude/claude-kit/tools/learn.py hiccup add ...` per `rbx-learn`.
