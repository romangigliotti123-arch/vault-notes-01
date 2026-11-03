# Code-walk: mental playthrough protocol

Work from the code and the plan. At each step write what the player sees, what the code does, and what could go wrong, with file:line. Keep it to about 12 files; read entry points first (`Main.server.luau`, `Main.client.luau`, the services they start).

## A. First 30 seconds (timeline table: t | player sees | code path | verdict)
1. Join: character spawn point, camera, loading screen/time, `PlayerAdded` order (data load before gameplay? kick-on-failure message present?).
2. 0-10 s: is there a visible goal without reading? First interactable within reach? First input works on touch (buttons >= 44 px, no keyboard-only)?
3. 10-30 s: first reward fired? Feedback (sound + particle + number)? Is the reward amount in Config the value the plan says?
4. Blockers: modal prompts, purchase prompts before the first win, text walls, forced tutorial waits, anything that needs a gamepass.
Verdict per row: OK / FRICTION / DEAD END. Compare the first-reward time with the plan's target and the vault note `first-session-onboarding` ("a win in the first 30 seconds").

## B. Core loop x10
Trace one full loop in code: trigger -> server validation -> state change -> reward -> UI update -> next goal. Then repeat mentally ten times with the numbers from Config: does the cost of the next upgrade stay reachable (no stall), does anything accumulate unbounded (inflation), does a state fail to reset (soft-lock), can the loop be skipped or repeated faster than intended (exploit), what happens at the first death/respawn, leave and rejoin (persisted?).

## C. Exploit review (every remote, every purchase, every save)
For each `OnServerEvent` / `OnServerInvoke`: arguments type-checked? numbers range-checked and finite? target instance verified (exists, correct class, near the player, owned)? rate limited? server decides outcome (client only requests)? For each currency/progress write: only server code writes it. Purchases: `ProcessReceipt` records `PurchaseId`, returns NotProcessedYet on failure, grants once; passes checked with `UserOwnsGamePassAsync` in pcall + cached. Data: load before use, session lock or ProfileStore, `Reconcile`, release on leave, `BindToClose` waits, no save on every tick, retry with backoff. Client scripts: nothing trusted by the server, no secrets, no `loadstring`. Teleport/speed/fly assumptions: server sanity checks or acceptable for the genre (state which).

## D. Onboarding and UX friction
Mobile layout (Scale sizes, UIAspectRatio/UISizeConstraint, safe area), text size, color contrast, button reach, clutter on small screens, language/reading level for the target age, sound defaults (not blasting), reward popups that block input.

## E. Feel and fluidity
Per core action: input latency (immediate local feedback before server confirm), animation/tween, sound, particle, camera shake or FOV nudge (subtle), hit-stop where relevant, UI counter tween. Movement speed vs map size (time to cross the map), jump height vs obstacles, checkpoint spacing for obbies. Performance smells: per-frame `GetDescendants`/`FindFirstChild` chains, unanchored part swarms, `RenderStepped` doing server-style work, uncapped particle emitters, many tweens created per frame, unbounded tables. Reference the vault notes `player-psychology-and-game-feel`, `vfx-and-particles`, `optimization-and-streaming`, `sound-and-music` for the current guidance (dates in the freshness line).

## F. Severity
S1 blocker: crash, data loss, exploit that grants currency/progress, soft-lock, cannot finish first loop. S2 major: broken feature, big friction in the first minute, unfair economy stall. S3 minor: polish, small UX, deprecated API. S4 note: idea or maintainability.
