# Click psychology: the mechanisms behind the MrBeast-style patterns

Complements `[cold:rbx-thumbnail/principles.md]` (13 graded mechanisms: saliency, fluency, faces and gaze, curiosity gap, promise-payoff, colour, text, hierarchy, element count, action, social proof, novelty, consistency, plus genre cues). Read that first; this file adds the mechanisms the study set leans on and ties each to a thing you can do. Grades as there: A = peer-reviewed mechanism (effect size on a Roblox tile unmeasured), B = official Roblox guidance or platform data, C = convention or anecdote. Nothing here is a promise of a CTR lift; the variant test decides.

| # | Mechanism | In plain words | Grade | Where it shows in the examples | Do this on Roblox |
|---|---|---|---|---|---|
| P1 | Pattern interrupt (isolation effect, von Restorff 1933; salience capture) | the item that differs from its neighbours is noticed and remembered first | A that distinct items are remembered better; C for thumbnails | #37 grey statue in a colour street, #28 button on white, #39 egg on white, #9 red figure on blue ice | the feed is full of bright 3D renders: be the one thing that differs (value, colour, scale or emptiness), but stay genre-readable |
| P2 | Curiosity gap (Loewenstein 1994) | curiosity peaks when you know enough to want the missing piece | A theory, C thumbnail effect | #24 half-covered face, #28 button, #32 circle with arrow, #5 many hazards, one face | show a real, recognisable situation and leave one thing the first minute answers (what is in the box, what is the button) |
| P3 | Scale and stakes | big contrasts of size or danger imply a story and cost | C | #9 tiny figure on iceberg, #17 planks over a valley, #14 sarcophagus with small people, #13 cheetah beside a calm driver | tiny hero on a giant tower or monster; the danger must be something the game really has |
| P4 | Faces, gaze and emotion | faces and the direction they look steer attention; strong emotion is read before text | A mechanism (gaze cueing), C that faces raise CTR in a niche | #6 terror, #15 snarl, #1 duel, #41 gaze sideways | a large Roblox character with one readable emotion, eyes toward the key object; closed-mouth vs open-mouth is audience dependent (mrbeast-process.md item 5) |
| P5 | Contrast in value, then hue | the eye reads brightness differences before colour | A | #25 red ring on green, #10 white car on dark, #24 red on teal | greyscale test at 100 px: the hero must still separate |
| P6 | Loss and challenge framing (Kahneman and Tversky: losses weigh more than equal gains) | "last to leave" and "survive" frame a possible loss, which feels more urgent than a plain gain | A for the effect, C for thumbnails | day counters (#3, #7, #9, #18, #19, #34), "keeps it" prize objects (#7, #36) | show a challenge, a streak, a rival or a rising threat; never a countdown aimed at children (see roblox-mapping.md) |
| P7 | Numbers and specificity | exact, large, odd numbers feel real and give the gap something to fill | C | "$456,000", "100 COPS", "#801", "100 SPEAKERS" | one number in the title or image that is true in the game (100 players, 1,000 coins, 50 levels) |
| P8 | Contrast pairs | two opposite things beside each other explain a claim without words | C | #20 and #21 ($1 vs $100M), #2 before/after, #12 robot vs man | starter vs maxed item, noob vs pro, day 1 vs day 100, same pose both sides |
| P9 | Novelty and the feed's baseline | what was new last year is now background; people look for new, but must recognise the genre | B (official: copies are penalised), C for the rest | the channel's titles become more extreme over time (thestory.au) | refresh the thumbnail with the update; one ownable twist on the genre cues |
| P10 | Familiar face and last-experience effect | clicks depend on how the last experience felt; a stable character builds recognition | P (Youshaei interview), A in general for mere exposure | the host is in the frame in nearly all modern examples | keep one mascot and palette across icon, thumbnails and updates; do not use a real person |
| P11 | Processing fluency / glanceability | what is easy to read is preferred | A | the team lead's 10-20 seconds rule (mrbeast-process.md item 10) | the one-sentence test: a stranger names the game's action in one second |
| P12 | Promise match | a click the game cannot honour becomes a bounce; Roblox filters and demotes mismatched packaging | B official | the team lead on trust (mrbeast-process.md item 9) | the first minute must contain everything the image shows (gate G1 in `thumb_score.py`) |

## How the mechanisms combine (each good thumbnail is usually 3 to 4 of them)
- Hook = P2 + P3: a situation people recognise, with a gap and a stake.
- Reading = P5 + P11: separated by value, readable in a second.
- Emotion = P4: one face feeling one thing.
- Proof = P7 + P8: a number or a contrast pair that makes the claim concrete.
- Differentiation = P1 + P9: different from the feed, same genre.

## Where the mechanisms mislead
- Contrast and curiosity beat clarity only up to the point where the genre stops being readable.
- Loss framing with children: avoid fear-of-missing-out pressure and fake urgency (`checklist.md` rule on pressure imagery).
- "It worked for that channel" is not evidence for your tile; the audience, the feed and the metric differ.
- Every effect in the table is unmeasured on Roblox: only your own variant test with qPTR counts.

Sources: Loewenstein, G. (1994) The psychology of curiosity, Psychological Bulletin 116(1), https://stafforini.com/works/loewenstein-1994-psychology-curiosity-review/ ; Frischen, Bayliss and Tipper (2007) gaze cueing, https://pmc.ncbi.nlm.nih.gov/articles/PMC1950440 ; Alter and Oppenheimer (2009) processing fluency, https://in-mind.org/glossary/processing-fluency-theory ; Kahneman and Tversky (1979) prospect theory (textbook); von Restorff (1933) isolation effect (textbook); channel statements in mrbeast-process.md.
