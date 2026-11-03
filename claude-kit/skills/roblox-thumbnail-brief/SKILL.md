---
name: roblox-thumbnail-brief
description: "Writes a sourced packaging brief for a Roblox experience: icon, 3-5 thumbnail concepts, title options, description draft, gameplay-video shot list and an A/B test plan, using the knowledge base's CTR, PTR, specs and discovery rules. Use when the user wants thumbnails, an icon, a title or description for a Roblox game, to raise CTR, or to refresh packaging after an update. Briefs only; does not generate or upload images."
---

# Roblox thumbnail brief

Related skill `roblox-ad-thumbnail-brief` covers ad creatives; this one is KB-grounded packaging for the experience page (icon, thumbnails, title, description, video).

## Procedure

1. Inputs (assume and state): game name, genre, core fantasy in one line, hook, current CTR/PTR/bounce if known, existing assets, audience, update to promote (if any).
2. Evidence:
   ```
   K="bash $HOME/.claude/claude-kit/tools/pyrun $HOME/.claude/claude-kit/tools/kbq.py"   # run `$K where` once to see VAULT/KB/ASSETS
   $K section thumbnails-icons instructions
   $K section titles-descriptions instructions
   $K find "thumbnail personalization active thumbnails specs" -t thumbnails-icons -n 6
   $K find "clickbait mismatch bounce accurate" -t thumbnails-icons,discovery-algorithm -n 5
   $K case "<genre>" -n 2
   $K docs "thumbnail requirements icon video" -n 5
   ```
3. Check the diagnosis first: if CTR is near 0.5% treat it as a packaging problem (repackage before changing gameplay); target 2.5-3%+ (indie, self-reported); if first-play bounce is high, the cause may be a mismatch between packaging and gameplay.
4. Write the brief; cite specs from `docs` output (do not rely on memory for sizes, counts or quotas).

## Output template

```
Diagnosis: <packaging vs gameplay problem, with numbers and flags>
Icon: concept, composition, text/no text, must read at ~150 px, size per docs
Thumbnails (3-5 concepts): subject / focal point, composition, colours and contrast, text (large, away from the bottom edge), what to A/B, size per docs
Title options (5): literal, core fantasy first, no clickbait; one recommended
Description draft: genre + objective + keywords in the first ~160 chars; limit per docs
Video: shot list of real in-engine footage only (no voiceover, CGI, promo text)
Test plan: change one element, equal exposure, promote the winner, refresh when performance declines, refresh with updates (max about once a week, revert on dip), event thumbnails distinct
Image-generation prompts (optional)
Evidence table: claim | link | flag | date
```

## Rules

- One focal subject, high contrast, readable at phone size, authentic gameplay. Misleading packaging causes bounces that hurt recommendations (official).
- Indie CTR numbers are self-reported. Official docs override on specs.
- No uploading, posting or spending.
