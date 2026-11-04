---
name: roblox-thumbnail-brief
description: "Sourced packaging brief for a Roblox experience: icon, 3-5 thumbnail concepts, title options, description draft, video shot list, A/B plan and sponsored-ad creative briefs from the knowledge base's CTR, PTR and discovery rules. Briefs only; no image generation."
---

# Roblox thumbnail brief

KB-grounded packaging for the experience page (icon, thumbnails, title, description, video) and for sponsored-ad creatives (section Ad creatives below).

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

## Ad creatives (sponsored experiences)

- Concept options: 3 distinct one-line scenes (action moment, reward moment, social moment); pick the one that reads clearest at phone thumbnail size. Keep key content in the centre so crops do not cut it.
- Ad formats and sizes differ by placement in Ads Manager: check the live requirements, do not trust memory.
- No fake counters, fake UI buttons, copied logos or "free Robux" text; all assets owned or original; all-ages safe.
- Test one variable at a time (icon first, it drives most impressions), fixed period or impressions chosen in advance, judge CTR and D1 of the visitors each variant brought, log the winner with its date.
- Paid ads: a small daily budget cap approved by the user (spending needs the user's yes); pause variants with the worst cost per retained visit. Budget plan: `roblox-ad-campaign-planner`.
- Deliverable: brief text, prompt/spec sheet per variant, test table (variant | dates | impressions | clicks | CTR | D1).
