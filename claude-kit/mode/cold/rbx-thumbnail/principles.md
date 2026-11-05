<!-- cold: rbx-thumbnail/principles.md | read when: designing or judging a thumbnail or icon and you need the click-psychology reasons, their evidence grade or the genre cues. -->

# Click psychology for Roblox icons and thumbnails: principles with evidence grades

Researched 2026-11-05, own words. Grades: **A** = peer-reviewed work or large platform data (supports the MECHANISM; size of effect on a Roblox tile is still unmeasured), **B** = official Roblox guidance or creator/platform data, **C** = folklore, anecdote or convention. No peer-reviewed study of Roblox thumbnails was found, and most "thumbnail psychology" web content is vendor blogging without methods. A faces-lift percentage that circulates widely has no traceable original and is not used here. The vault learns the real effect from your own results (`tools/thumb_record.py`, [cold:rbx-thumbnail/protocol.md]); the rubric weights ([cold:rbx-thumbnail/rubric.md]) follow these grades and are assumptions until then.

## What the platform optimises (B, official)
- The built-in test is thumbnail personalization: 2 to 5 active thumbnails, shown to users, then more traffic to the leader per user group. It scores qualified play-through rate (qPTR = qualified plays per Home impression), not raw clicks, so an image that earns clicks and fast bounces is penalised by the metric itself. https://create.roblox.com/docs/production/publishing/thumbnails
- Thumbnails, titles or genres that do not truthfully show the experience lose Home and Charts exposure; near-copies of another experience's thumbnail are deprioritised. https://devforum.roblox.com/t/improving-user-experience-by-reducing-exposure-of-low-quality-content/3299107
- Staff tips: show real gameplay, avoid click-bait, keep the variants clearly different, keep colour and style consistent across icon and thumbnails. https://devforum.roblox.com/t/5-tips-from-roblox-staff-to-get-the-most-out-of-thumbnail-personalization/3471689 and https://devforum.roblox.com/t/get-your-thumbnails-ready-for-thumbnail-personalization/3226599

## Roblox facts used by the tools (official pages, read 2026-11-05; re-check, they move)
| Item | Fact | Source |
|---|---|---|
| Icon | square, at least 512x512; some surfaces show it near 150x150 | https://create.roblox.com/docs/production/publishing/experience-icons and https://create.roblox.com/docs/production/promotion/game-icons |
| Thumbnail | 16:9, ideally 1920x1080; non-16:9 is stretched; up to 10 images or videos per page | https://create.roblox.com/docs/production/publishing/thumbnails |
| Personalization upload | under 3 MB, 1920x1080 | same |
| Safe area | keep essential text and elements off the bottom edge: player-count metadata can cover it | https://create.roblox.com/docs/production/promotion/promotional-thumbnails |
| Not stated | icon file size and format limits: not checked by the tools | |

## The 13 mechanisms
| # | Mechanism | Prediction | Grade | Source | Apply to Roblox | Test as a variant pair |
|---|---|---|---|---|---|---|
| 1 | Bottom-up saliency and contrast | regions that differ in brightness, colour or orientation capture early attention; clutter dilutes it | A mechanism, C effect size | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6969943/ | the hero is the single highest-contrast region; value contrast first, hue second; squint test at 150 px | subject/background value contrast low vs high |
| 2 | Processing fluency | easy-to-process images are preferred and judged faster | A general effect (Alter and Oppenheimer 2009), not shown for thumbnails | https://in-mind.org/glossary/processing-fluency-theory | one subject, simple background, few value masses, no tiny detail | simple vs busy version of the same scene |
| 3 | Faces, gaze, emotion | eye direction shifts viewers' attention to the target; faces draw attention | A gaze cueing (Frischen, Bayliss, Tipper 2007); C that faces raise CTR, depends on niche | https://pmc.ncbi.nlm.nih.gov/articles/PMC1950440 and https://1of10.com/blog/should-you-use-your-face-in-your-youtube-thumbnails | big readable expression (surprise, fear, joy); aim eyes or pose at the key object; a pet or mechanic can be the hero instead | expressive character vs object-only; gaze at object vs at camera |
| 4 | Curiosity gap | curiosity needs a gap in knowledge plus some prior knowledge | A theory (Loewenstein 1994), C thumbnail effect | https://stafforini.com/works/loewenstein-1994-psychology-curiosity-review/ | show a recognisable situation with ONE unresolved element the game pays off in the first minute | mystery element vs explicit loop |
| 5 | Promise-payoff match | a click the game does not reward becomes a bounce; qPTR counts qualified plays | B official (metric and exposure policy), magnitudes unpublished | the two Roblox pages above | show only what appears in the first 60 seconds; check against a real first-minute screenshot | judge by qPTR and playtime per qualified play, not CTR |
| 6 | Colour in context | colour meaning depends on context; "red converts best" style claims are not universal | A that meaning is context dependent (Elliot and Maier 2014), C for conversion claims | https://www.frontiersin.org/articles/10.3389/fpsyg.2015.00368/pdf | pick colour for contrast against the hero and for genre mood (official: bright saturated for fantasy, muted for somber, heavy contrast for horror) | same scene, 2-3 palettes |
| 7 | Text overlay | text can disambiguate but adds load and dies at small size | C | creator consensus; https://support.google.com/youtube/answer/13861714 does not address text | icon: none or one short word or number; thumbnail: 0-3 big words, outline, not in the bottom edge; the title already carries words | text vs no text |
| 8 | Focal hierarchy | a clear reading order helps (hero, then threat or goal, then setting); the rule of thirds itself is convention | C | none solid | hero fills roughly a third to a half of the frame, one supporting element, quiet background | hero size variants |
| 9 | Number of elements | fewer competing elements helps fluency and saliency | A mechanism (1, 2), C for any numeric limit | as 1 and 2 | one hero plus at most one or two supporting elements | 1 vs 3 elements |
| 10 | Implied action | dynamic poses signal that something is happening | C | creator and design folklore | diagonal poses, mid-action frames; video thumbnails must show real gameplay | static vs action pose |
| 11 | Social proof | popularity cues raise perceived value | C | none solid | Roblox already overlays player counts on the tile, so never fake them; show a crowd only if it is real gameplay | solo vs group scene |
| 12 | Novelty vs familiarity | people must recognise the genre fast and still notice something different; near-copies are penalised | B official for the penalty; C that odd beats generic | the low-quality-content and staff-tips pages above | genre cues plus ONE ownable twist; compare beside 5-10 competitors | familiar-cue vs twist |
| 13 | Cross-surface consistency | recognition improves when icon, thumbnails and title share palette and character | B official recommendation | the get-ready post above | share palette and hero across icon and thumbnails | not testable alone; just apply |

## Genre cues (grade C: working hypotheses, verify against the live front page each time)
| Genre | Cue pattern | Risk |
|---|---|---|
| Obby / parkour | bold course silhouette, character mid-jump, bright primaries, height or danger read | crowded; add one distinctive hazard or theme |
| Tycoon | visible base or factory plus a growing structure, cheerful palette | easy to copy; differentiate the theme |
| Simulator / clicker | large cute character or pet, collectibles, saturated colour, a progress cue | very crowded; a rare or huge pet or a distinct world is the twist |
| Horror | dark, high contrast, one eerie figure or silhouette, restraint over gore | all-ages rules: no gore, nothing misleading for young players |
| Roleplay / social | warm scene, several characters, home or town context | the promise is hanging out; avoid fake action |
| Fighting / PvP / shooter | two opposed figures or a weapon pose, diagonal energy, rim light | no weapons aimed at people; stylise |
| Tower defence | towers against a boss or wave on a readable map | keep the map path readable |
| Fishing / collecting | a rare catch or creature with a glow in a calm vivid scene | glow is the contrast tool |
| Anime / action RPG | stylised hero pose, effects, clean logo | style copying is penalised; no IP |
| Fashion / dress-up | bright outfits on a clean backdrop (an exception to the plain-background warning) | test per game |

## Other cautions
- Creator-reported click benchmarks (about 1-1.5% weak, 2.5% average, 3.5%+ strong for ads) are self-reported, not platform norms. Some creator videos quote much larger early-test lifts from personalization; the official figure is an average +8.5% qPTR with some thumbnails at +50% (Roblox docs and launch post). Use the official one.
- One case where a hand-drawn style beat a 3D render does not generalise.
- A claim that 16:9 beats square icons in Sponsored Sort (up to 40% play-through) is grade B and unverified here.
