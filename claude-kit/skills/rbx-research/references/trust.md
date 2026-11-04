# Trust layer (verify stage)

Every key point, number and technique in the topic notes, and every playbook step, carries one label.

| Label | Meaning | How it is decided |
|---|---|---|
| OFFICIAL | matches official docs / manual / maintainers' repo that were actually read | the verifier cites official fact ids; code checks the ids exist and every number in the claim appears in the cited fact. A wrong number is rewritten to the official value ("corrected"), the original kept in the note JSON. All-official citations also count. |
| CORROBORATED | 2+ independent sources | different creators; a WEAK-rated creator is not the second source |
| SINGLE-SOURCE | one creator | stated plainly as unconfirmed; a sole WEAK source is flagged |
| CONTRADICTED | sources disagree, or an official fact says otherwise | both views shown, the better supported one named (theme `disagreements`, playbook "Where sources disagree") |
| OUTDATED-UNSURE | one creator and the newest item is over 12 months old, or a number/limit/setting/API name/version no official source covered | never shown as a plain fact |

Playbook steps take the WEAKEST label of the points they cite. `cheat-sheet.md` ("do this first") has only OFFICIAL or CORROBORATED steps. Hub `00-README.md` "How reliable is this": counts per label plus the 5 shakiest claims (contradicted or outdated first, sole-WEAK and numeric first among singles).

## What counts as official
Selected creators you mark with `trust.py mark-official --creator ID` (docs site, manual, the project's own repo or release notes); their extracted claims are the first fact pool, so nothing is re-fetched. Only when a claim needs more, fetch ONE official page: `trust.py official-fetch --out OUT --url URL` (robots.txt respected, cached under `.cache/official/`), or `official-add --file F --name N` for text already read. `trust.py needs` lists numeric/setting claims with no official coverage; after fetching, `trust.py verify --recheck` re-checks only those. Official beats creators whenever they differ.

## Cost control and limits
One model call per theme (haiku in Light, sonnet otherwise), reusing extracted claims; relevant facts picked by keyword retrieval in code (at most 110 per call); labelled items are skipped on rerun. A label is only as good as the official pages read: "unverified" means no fact in the pool covered it, not that it is wrong. Verification checks claims against text; it does not run code.
