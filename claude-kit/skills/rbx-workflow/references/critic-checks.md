# critic-checks: pass/fail checks the critic runs per factor

Read by `rbx-judge` only for the factors the stage scores. Each line is a check with a number or a gotcha; DR = `Roblox/roblox-kb/_tools/DECISION-RULES.md` (topic in brackets). Trust: official or mixed (official and creators agree) only. A failed check with no cited exception caps that factor at 5; a pass is evidence for 7+. Re-check fast-moving numbers with `kbq.py` before quoting. Patterns only, never copy a game.
Run a check only where the stage's evidence can show it. At the idea stage a detail the plan has not had to decide yet (pixel sizes, API names, texture caps) is a "to specify" note, not a cap; a plan that contradicts a check (a pay-to-win pass, paid randomness aimed at kids) is a fail. "Rescue from loss" = a loss the design engineers to sell the fix (spiked difficulty, pressure timer, lost-gear ransom); cheap optional revives in a fair game free players can finish are an F7 note, not a cap.

Order: spec compliance (each acceptance line met, with evidence) is judged before style or polish; style never lifts a failed spec check. [cold:rbx-workflow/rulings.md] read only for the review-order rationale.

## F1 first 30 seconds
- Time the first action from AFTER the age-check/ID step; that step is pre-play friction, not tutorial time (official 2026-01; DR first-session-onboarding).
- Start currency is about 10 coins and the first purchase is reachable inside the first session (official; DR first-session-onboarding).
- D1 under about 10 percent: audit the first 5 minutes, the tutorial funnel and performance before adding rewards (mixed; DR retention-d1-d7).

## F3 clarity
- Icons and visible consequences replace instruction text; dialogue is at most 3-4 taps (mixed; DR first-session-onboarding).

## F4 feel
- Background music loops at volume about 0.2 and starts on join; loud sources stay at volume 2 or below; the climax mix is checked on phone speakers and headphones (official; DR sound-and-music).

## F5 progression
- Something unlocks every few minutes, early XP stays low, and a goal is visible within 10-15 minutes (mixed; DR core-loops-and-game-design).

## F6 social
- Friends are never split into isolated servers; group play earns a bonus and solo players are never penalised (official; DR social-features-and-virality).
- Invites reward both inviter and invitee and read `ReferredByPlayerID` (official; DR retention-d1-d7).
- Notifications go only to opted-in 13+ users, at most 1 per user per day (official; DR retention-d1-d7).

## F7 monetisation
- The shop has a cheap entry tier (about 25-100 Robux; a benchmark, not a price floor for single products); offers aimed at players in their first 10-30 minutes are cheap or hidden (mixed; DR pricing).
- One server `ProcessReceipt` returns `PurchaseGranted` only after the grant; `PromptProductPurchaseFinished` never grants; prices come from MarketplaceService (official; DR monetisation-devproducts).
- Text players type and others see passes `TextService:FilterStringAsync` in a pcall (official; DR age-ratings-moderation-and-tos).

## F8 packaging
- Thumbnail 16:9 at 1920x1080 under 3 MB; icon a custom 512x512 square showing theme and genre, never auto-generated (official; DR thumbnails-icons).
- Title literal, a few words, no repeated words, at most 2 emojis or special characters; description's first ~160 characters hold genre, feature, objective and keywords, total under 1000, no hashtags or changelogs (mixed/official; DR titles-descriptions).
- Preview video is authentic in-engine footage: no CGI, overlays, voiceover or promo text (official; DR thumbnails-icons).

## F9 performance and stability
- Read FPS, memory and session time at P10 and P90, never averages alone; act at 70 percent of a DataStore or Memory Store quota (official; DR analytics-metrics).
- UI: Scale not Offset, interactive ScreenGuis on CoreUISafeInsets, `MinTextSize` 9 or higher, mobile buttons about 60 px from the sides (mixed/official; DR ui-ux-design).
- Custom 3D assets: at most 20,000 triangles per mesh (4,000 for accessories), one material per mesh, textures within their scope cap (`Roblox/blender/blender-cheat-sheet-claude-blender-roblox.md`, official).

## PLACEMENT (placement gate, stage prototype or later)
- Checks P1-P7 and tolerances: `rbx-placement/references/checks.md`. Pass = the critic's own full-map scan (scorer critic, newer than the newest Luau source and the last placement) has every model pass or waived with a reason, waivers/ignores under 10%, and `placement_gate.py recheck` agrees with the stored inputs. A missing, builder-made, stale or failing scan caps the verdict at NOT YET.

## LIGHTING (lighting gate, stage prototype or later)
- Checks L1-L12 and tolerances: `rbx-lighting/references/checks.md`. Pass = the critic's own scan (scorer critic, newer than the newest Luau source) recomputed by `lighting_gate.py` has every check pass or waived with a reason (at most 2 waivers), brightness judged from sampled surfaces or screenshots, the genre passed from GAME.md. A missing, builder-made, stale or failing scan caps the verdict at NOT YET.
## LOOKS (visual gate, stage prototype or later)
- Rubric V1-V7, hard fails and the screenshot set: `rbx-visual/references/rubric.md`. Pass = every item at least 7, no open hard fail, `ui_overlap` shows 0 findings at phone, tablet and desktop, at least 6 distinct screenshots (desktop and phone; spawn, action, effect) newer than the newest Luau source. Run by `visual_gate.py`; a missing gate caps the verdict at NOT YET.

## CODE GATES, BUG FIXES AND PLAN (stage prototype or later)
- `Games/<slug>/code-gates/run.json` exists with scorer critic and covers comment, scope and security; the one-line `CODE GATES:` result is in the report (not run = NOT YET, `playable prototype, code gates not run`). Findings are scored, never blocks.
- Each bug reported fixed has `Games/<slug>/bugfix/<id>.md` with a RED and a GREEN block; otherwise the fix is `untested`.
- A claim of balanced, tuned or optimised has a `tune/<run>/` ledger that `tune_check.py` accepts; otherwise a LOW unmeasured-claim finding.
- The plan's M1 is the core loop, serial, with its own acceptance test, and no parallel job starts before it passes (manager.md, Core loop first).

## Stage and growth checks

[cold:rbx-workflow/critic-checks-late.md] read only when the critic scores a playtest, launch, growth or live-ops stage.

## Where sources disagree

[cold:rbx-workflow/critic-checks-late.md] read only when two numbers in these checks conflict (rewarded-video opt-in, A/B length, texture caps).