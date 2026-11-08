# From MrBeast-style principles to a Roblox icon and thumbnail

Evidence base: the vault KB (`$K section thumbnails-icons instructions`, `$K section thumbnails-icons disagree`, `$K num "thumbnail size"`; file `thumbnails-icons.md`, 194 videos, newest 2026-10-30) plus the official Creator Hub pages it cites. Specs move: run the live check in SKILL.md step 1 and let it override anything below. Principles: mrbeast-process.md, psychology.md, `[cold:rbx-thumbnail/principles.md]`.

## Two different jobs
| | Icon | Thumbnail (and video thumbnail) |
|---|---|---|
| Shape | square, upload 512x512 (KB: confirm it stays sharp at about 150x150, where some surfaces show it) | 16:9, create at 1920x1080, under 3 MB; non-16:9 is stretched or auto-resized |
| Where | Home recommendations, search, lists, the returning player's first look | the experience page, Home tile, personalization set, ads |
| Reader | a returning or scrolling player in a fast list | a player choosing between games, often a new one |
| Job | recognition and one idea: the theme and genre in half a second | the hook, the action and the reward; more room, still readable at phone width |
| Content | one subject filling the square, no text or one very short word/number | hero + one prize/threat + quiet background; 0-3 words |
| Test | separately; a strong thumbnail with a weak icon loses returning players (KB, Roblox 2024-09) | 2 to 5 active thumbnails (personalization, official), 10+ in an ad test |

Keep the essentials off the bottom edge of the thumbnail: player-count metadata can cover it (Creator Docs 2026-10). Mobile is about 60% of minutes (KB, Roblox 2026-10): judge at phone width.

## Principle to Roblox move
| Principle (source in the study) | Roblox move |
|---|---|
| One dominant subject (every modern example) | one Roblox character, pet or object fills one third to one half of the frame; the KB says Swordburst 3 saw a big CTR/recommendation uplift from one clear focus, and "if the subject is not identifiable in a second at phone size it is too busy" |
| Face and emotion (#6, #15, #26) | a character close-up from the game's own avatar with an exaggerated, readable face; eyes aimed at the prize or threat. A render of the character is the common choice (AlvinBlox 2025), but an official 2025 test had a hand-drawn style beat a 3D render for Tower Defense Simulator, so test styles |
| Scale (#9, #14, #17) | tiny avatar on a giant tower, boss, map or pile of currency; the scale must exist in the game |
| One action or reward (#25 circle, #28 button) | show the verb or the prize, not the menu: a jump over lava, a pet hatching, a big win. KB: Adopt Me's best thumbnail was a vibrant pet-collection shot matching the core fantasy (about 1.7x the average) and beat the minigame action shot |
| Colour and contrast (#25, #10, #24) | bright, saturated colour for fantasy and cartoon games, muted for somber, heavy contrast for horror (official); a complementary pair for subject and background; check greyscale |
| Minimal text (#3 day counter, #6 "100 COPS") | 0 to 3 big words, white with a thick dark outline, upper area, never the bottom edge; the title already carries words. Many young players avoid reading (official design-for-Roblox page) |
| Counter or number (#3, #18, #33) | a real in-game number (Level 100, 1,000 coins, Day 6) in a corner; never a fake count |
| Contrast pair (#2, #20) | before/after pet, starter/maxed base, noob/pro, same pose twice |
| Curiosity gap (#24, #28) | one unresolved but honest element the first minute answers |
| Test everything (the team's own method) | personalization with 2-5 thumbnails; ad test with 10+ creatives, one change at a time, judge by qualified play-through (qPTR), not clicks |
| Re-package when the content is good (outlier idea) | re-do the icon and thumbnails with each major update, at most about once a week, keep the palette and character, add a marker, revert on a dip (KB) |

## What top Roblox packaging does (KB, with dates)
- Big focal subject and clean background; 1-2 characters; bright colours; minimal text (Tizzy 2026-06, Roblox 2024-09, AlvinBlox 2025-04).
- Shows the core fantasy and the unique mechanic, especially in a sequel (Tizzy 2026-06).
- Several thumbnail concepts in play and rotated: winners decay as impressions grow (Roblox Creators 2024-11, Tizzy 2026-06).
- The newest guidance (2026) says a raw screenshot or a plain AI icon can hurt CTR: compose the final (clean, large subject, outline, mobile check). That is what `thumb_compose.py` is for.
- Disagreements to keep in mind (KB "Where creators disagree"): match the platform style vs be original; hire an artist vs make your own; 3D render vs hand-drawn. Use the variant test.

## What not to copy
- **Real people.** Do not use a real person's face, an influencer, or this channel's host or look-alike; do not imitate his likeness, outfit, logo, merch or the channel's branding. Study the composition, then draw your own Roblox character.
- **Brands, other games, IP.** No real logos, no other game's characters, art or UI, no licensed film or toy characters (see entries marked "Do not copy" in the library, e.g. the Wonka-style costume and the celebrity charity photo).
- **Misrepresentation.** The image must show what the game really offers in its first minute: no fake rewards, fake Robux, fake ratings, fake UI or counters, or scenes that are not in the game. The KB: clickbait lowers qualified play-through and mismatched content is detected and filtered; a 2024-06 creator reported 1.5% with a clickbait icon; the 2025 guidance rejects brainrot-style clickbait that does not match the game.
- **"FREE" or reward claims** (#35 style): no "free Robux", no off-platform links or handles.
- **Fear and pressure for children.** No graphic or scary imagery that would mislead a young audience, no weapon pointed at the viewer or at a person (#42), no countdown-FOMO or loot-box visuals presented as paid randomness. Horror games: use mood and mystery, not gore.
- **Fake platform UI.** No fake LIVE badges, player counts, like buttons or "official" marks (#55).
- **Raw screenshots with HUD or watermark** (#51, #52): compose them.
- **Clutter and long text** (#44, #49): two or more of these in the same image fail the legibility test.
- **Copying another experience's key art.** Near-copies are deprioritised (official); gate G3 in `thumb_score.py`.

The full rule list to run before delivery is `references/checklist.md`; if it and a live official page differ, the live page wins.
