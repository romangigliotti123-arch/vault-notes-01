<!-- cold: rbx-thumbnail/rubric.md | read when: scoring a candidate icon or thumbnail with thumb_score.py, or when you need the 0/1/2 anchors of a check. -->

# THUMBNAIL SCORE RUBRIC: 3 gates and 13 weighted checks (max 46, pass 32)

How to use: look at the image at full size, then again reduced to about 150 px (icon) or 320 px wide (thumbnail). Decide the three gates (pass or fail), score the 13 checks 0, 1 or 2 from the anchors below, put them in a scores file (`thumb_score.py template`), run `thumb_score.py score S.json --write Games/<slug>`. The tool does the arithmetic, the ranking of 2-5 variants, the file checks and the gate record. Never score an image you have not looked at.

ASSUMPTION label: the weights (3/2/1 from the evidence grade), the pass bar of 32 (70% of 46) and every threshold are the vault's judgement, not fitted to data and not Roblox rules. The result ledger (`tools/thumb_record.py summary`, [cold:rbx-thumbnail/protocol.md]) exists to replace them with measured ones once 20 or more decided variants per genre exist. Evidence for each check: [cold:rbx-thumbnail/principles.md].

Weight = 3 for a mechanism with grade A evidence, 2 for official guidance (grade B), 1 for convention (grade C). Max = (3+3+3+2+2+2+2+1+1+1+1+1+1) x 2 = 46. Ship = no failed gate AND total at least 32 AND the file checks pass. Otherwise fix the three checks that lose the most points and score again (cap 3 rounds).

## Gates (any fail = not shippable, whatever the total)
| ID | Gate | How to check by looking |
|---|---|---|
| G1 | Promise is real | List every element shown (mechanic, UI, reward, creature, setting) and mark in game yes/no against the first-minute screenshot or GAME.md. Anything absent, or enhanced beyond what players see = fail. |
| G2 | Rule-safe | Run the Roblox section of `references/checklist.md`: no free-Robux or reward hint, no real people or brands, no copied art, no gore or weapons aimed at people, no fake UI, ratings or event badges. |
| G3 | Original vs competitors | Put it beside 5-10 current genre competitors (live front page). A near-copy of another experience's key art, title look or composition = fail. |

## Checks (score 0 / 1 / 2)
| ID | Check | Weight | Grade | 0 | 1 | 2 | How to check |
|---|---|---|---|---|---|---|---|
| 1 | One clear focal subject | x3 | A | none, or several compete | a hero exists but the frame is cluttered | one obvious hero | blur or squint; name the hero in one noun |
| 2 | Subject/background value contrast | x3 | A | hero merges with background | moderate separation | hero separates clearly in greyscale | view in greyscale (or imagine it); does the hero still pop |
| 3 | Small-size legibility | x3 | B | unreadable at 150 px | partly readable | fully readable | downscale and look again |
| 4 | Element count | x2 | A | four or more competing items | three | one or two | count distinct focal items |
| 5 | Genre legibility | x2 | B | genre unclear | guessable | read in one second | cover the title and ask what genre it is |
| 6 | Emotion or stakes cue | x2 | A mechanism, C size | none | weak | clear expression, threat or reward | describe the feeling in one word |
| 7 | Curiosity the game answers | x2 | A theory, C size | none | vague | one clear gap paid off in the first minute | name the question the image raises and where the game answers it |
| 8 | Text discipline | x1 | B+C | tiny or long text, or text in the bottom 15% | acceptable | none, or 1-3 big high-contrast words | read at small size; check the bottom edge |
| 9 | Colour fit | x1 | B+C | clashing or muddy, mood mismatch | ok | palette fits the genre mood and supports contrast | compare with the mood guidance in principles.md |
| 10 | Action or implied motion | x1 | C | static and flat | some | clear pose or direction | is there a diagonal or pose implying action |
| 11 | Novelty twist | x1 | C | generic | small | one distinct ownable element | state the one thing only this game has |
| 12 | Cross-asset consistency | x1 | B | icon and thumbnails unrelated | partly | shared palette and character | compare with the icon and the other thumbnails (score 1 when there is only one asset) |
| 13 | Artifact check | x1 | quality | broken hands, garbled text, extra limbs | minor | clean | zoom to 100% |

## Objective file checks (done by `thumb_score.py inspect`, header only, no libraries)
Thumbnail: file exists and is not empty; PNG/JPEG/GIF/BMP header size read; aspect 16:9 (else Roblox stretches it: fail); 1920x1080 recommended (smaller 16:9 = warning); under 3 MB for personalization (read as 3,000,000 bytes: ASSUMPTION, stricter than needed); bottom-edge note (check 8 by eye). Icon: square, at least 512x512; file size not stated by Roblox, so not checked; legibility at about 150 px is check 3. A failed file check blocks PASS but not the ranking.

## Reading the result
- Table columns: total of 46, gates, file checks, PASS or FAIL, difference to the control variant. One variant scored = fine for polishing, but the platform test needs 2 to 5 active thumbnails; more than 5 candidates: pick the top 5.
- Variants for a test should differ by ONE feature group each from a control, so a later win or loss means something (protocol.md).
- The gate record is advisory: it is shown in the verdict and the scorecard and never blocks. A final record that failed counts as a failing gate record for the hiccup check, like any other gate.
