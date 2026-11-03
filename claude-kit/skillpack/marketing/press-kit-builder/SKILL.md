---
name: press-kit-builder
description: "Assemble a one-page press kit for a Roblox game that creators, press and partners can use without asking questions: fact sheet, honest description, approved art and renders, trailer and screenshot links, play link, contact, and usage rules, with a fact-check list. Use before outreach, launch or a brand conversation."
category: marketing
tags: press kit, media kit, fact sheet, creator kit, assets, renders, logo, contact, brand deal, launch
kb: Roblox/roblox-kb/influencer-and-creator-marketing.md, Roblox/roblox-kb/brand-deals-and-ip-licensing.md, Roblox/roblox-kb/trailers-and-video-marketing.md, Roblox/roblox-kb/community-and-discord.md
related: influencer-outreach-writer, brand-kit-builder, launch-day-planner, collab-pitch-writer, screenshot-set-planner, tagline-writer
---

# press-kit-builder

Vault: give creators a concrete reason and a self-contained pitch; support them with assets, models and thumbnail renders; keep the Talent Hub profile complete when you want brand work. The press kit is the single link that makes all of that one click. It holds facts and permitted assets, not hype.

## When to use
Before sending outreach, at launch, for a major update, or when a brand or publisher asks "do you have a kit". Not for: the outreach message (`influencer-outreach-writer`), the store page (`store-page-audit`).

## Inputs (max 2)
1. Game name, links (play link, group, Discord) and launch date or update date. 2. Contact route the owner is comfortable with publicly (default: a studio or project email, never a personal one).

## Procedure
1. Fact sheet block, every line checked against the live game: name, genre, one-sentence pitch, platforms it runs on, age rating / maturity answers, launch date, current version or update, group name, owner. Numbers like CCU or visits only if the owner confirms them from Creator Hub and gives a date.
2. Boilerplate: a 50-word and a 150-word description in plain words, matching the store page (`game-description-writer`); no claims the game cannot prove.
3. Assets list with file paths and sizes: logo (light and dark backgrounds), icon, thumbnails, 6-10 screenshots without UI clutter, 3-5 character or item renders on transparent or plain background, a gameplay clip or trailer link (`trailer-script-writer`), colours and fonts if public (`brand-kit-builder`).
4. Usage rules in four lines: what creators may do (video, stream, monetise their coverage), what they may not (misrepresent features, use art as their own), credit wording, and a takedown contact. Do not invent legal terms; mark them "owner to confirm" and suggest a lawyer for anything beyond plain guidance.
5. Creator support block (vault): tracked code or link per creator (`codes-campaign-planner`), a way to ask for early access, whether a creator server or private servers exist, a streamer-friendly mode if the game has one.
6. Contact and response expectation (for example "reply within 2 working days") that the owner can keep.
7. Build the page: one markdown page plus an `assets/` folder; a public share link is the owner's decision. Never include credentials, private emails, unreleased features or internal revenue numbers.
8. Fact-check list: tick each line against the live game or owner confirmation, with the date. Refresh at each major update.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `screen_capture` for screenshots; renders of characters or props via staged scenes with `execute_luau` (Edit) only with permission and no save. Everything else is files.

## Fallback
Text kit with a "to capture" list for the owner; asset checks are `untested` until files exist.

## Evidence
`Roblox/roblox-kb/influencer-and-creator-marketing.md` (self-contained first pitch with screenshots, trailer and playable link; support creators with a server, models and thumbnail renders; complete Talent Hub profile is required for the Brand Developer Directory; Creator Affiliate terms are official and change), `Roblox/roblox-kb/brand-deals-and-ip-licensing.md` (brand work fits the game and community; pitch with visuals; programme eligibility is official and moves), `Roblox/roblox-kb/trailers-and-video-marketing.md` (real footage; Details Page URL in every promo post; a durable style guide), `Roblox/roblox-kb/community-and-discord.md` (be transparent; announce publicly). Programme rules and sizes: live-check.

## Output
`marketing/press-kit.md` plus `marketing/press-kit/assets/` listing: fact sheet, boilerplates, asset table (file, size, use), usage rules, creator support block, contact, fact-check table with dates.

## Acceptance checks
- [ ] Every fact line has a check mark and a date.
- [ ] Each asset listed exists at the stated path (`ls` the folder) or is marked "to capture".
- [ ] No credential, private email, unreleased feature or internal revenue figure appears.
- [ ] The play link and Details Page URL open the right game.
- [ ] Usage rules are marked "owner to confirm".

## Pitfalls
Old screenshots of a previous version. Hype adjectives instead of facts. Stat claims without a date. A kit that needs three emails to use. Putting unreleased content in a public file.

## Related
`influencer-outreach-writer`, `brand-kit-builder`, `launch-day-planner`, `collab-pitch-writer`, `screenshot-set-planner`.
