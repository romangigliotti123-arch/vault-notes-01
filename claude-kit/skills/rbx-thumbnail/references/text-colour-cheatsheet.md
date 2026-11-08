# Text, colour and size cheat sheet

Numbers marked (A) are assumptions chosen from the study and the legibility strip; they are starting points, not Roblox rules. Official specs and rules: roblox-mapping.md and the live check in SKILL.md.

## Text
| Item | Rule |
|---|---|
| Words | thumbnail: 0 to 3 (the study set uses a counter or number far more than a phrase); icon: none, or one word or number (A) |
| Content | a number, a counter (DAY 6, LEVEL 100), a 1-2 word label of the twist. Never a claim the game cannot honour; never "free Robux", never handles or links |
| Height | at 1920x1080 a big word is 160 to 260 px tall (15-24% of the frame height) (A); after the 400/200/100 px downscale the letters must still be readable, which `thumb_compose.py check` measures as `text_px_at_100` (WARN under 8 px, A) |
| Font | heavy sans-serif or rounded display face, caps, tight spacing; no thin or script faces; not more than one font |
| Edge | white fill with a thick dark outline (about 6-8% of the cap height), or yellow fill with a dark outline; optional soft shadow; the study set shows white with black outline in nearly every case |
| Position | top right corner or top centre; left or right third if the hero is on the other side; never the bottom 15% (player-count area) and not on the hero's face |
| Contrast | text against its local background at least 3:1 (large text, A); the compose check prints the measured ratio. White on yellow fails; use a dark outline |
| Spelling | read it twice; image models garble text, so add words in the composer, not in the generator |

## Colour
| Item | Rule |
|---|---|
| Palette | hero + background + one accent: 3 colours, not 6; limit the number of saturated hues in the frame to two |
| Pairs | warm subject on cool field (orange on blue, red on teal), or dark subject on a light flat field; complementary pairs in the study: red/green (#25), red/teal (#24), yellow/dark (#36), red/blue ice (#9) |
| Value first | squint or greyscale: the hero must be clearly lighter or darker than its surroundings; colour alone fails at 100 px |
| Saturation | high saturation is the Roblox norm for bright games (official: bright saturated colour for fantasy and dreamy tones); muted for somber; strong contrast for horror. Moderate moving or glowing elements so they do not overwhelm (official) |
| Glow and outline | a 2-4% outline in black or a dark shade around the hero, a coloured glow behind the head, a rim light: these separate the hero from the feed |
| Background | blurred, simple or one flat colour; reduce detail behind the hero |
| Consistency | keep the same hero, palette and style across icon, thumbnails and updates (official recommendation) |

## Size and safe zones (Roblox)
| Item | Value |
|---|---|
| Thumbnail | 16:9, create at 1920x1080, under 3 MB; mobile-size judge at about 200-400 px wide |
| Icon | 512x512 square; check at 150x150; no important detail within about 8% of the edge (A: icons are shown with rounded corners) |
| Bottom | keep text and the face out of the bottom 15% of the thumbnail (A for the exact number; the platform's overlay can cover it) |
| Margins | at least 4% of the frame between the text and any edge |

## Mobile-size legibility checks (what `thumb_compose.py strip` renders)
- Widths 100, 200 and 400 px for the thumbnail, and 64, 100 and 150 px for the icon, shown at true pixel size, in colour and in greyscale.
- At 100 px: can you name the subject (one noun), the emotion (one word) and read any text? If not, enlarge, simplify or recolour.
- Greyscale row: if the hero disappears, the value contrast is too low.
