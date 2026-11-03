---
title: byteblox100 - How to make successful Roblox games
tags: [roblox, byteblox100, playbook]
videos: 25
generated: 2026-10-29
credibility: trusted
credibility_score: 8.1
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# byteblox100 - How to make successful Roblox games

Byteblox100's playbook: learn the client/server model and Luau basics first, then ship a simple loop (often an incremental buy-button or obby). Keep the server authoritative for economy and secrets, clean up what you spawn, and build UI with Scale and Activated so it works on mobile. Make death and progression meaningful, and add cheap first-interaction feedback for personality. Monetise without interrupting play: gamepasses and products, not popups or paywalled convenience. Add ads only once you have real players, and never use manipulative odds. Where advice conflicts, the later videos (late 2024 and 2025) take precedence.

**Style:** Opinionated and blunt, moving from beginner code tutorials to design and ethics critique. Strong on fast builds, player respect and monetisation skepticism. Best for beginners who want a practical base plus a conscience about monetisation. Some videos are satire or entertainment, and some plug paid courses.

## Playbook
1. **Start with a loop you can ship in days** [[game-ideas-and-genres]]: Incremental or tycoon buy-button loops are quick to build with basic UI and a few scripts. A simple loop built in about 15 minutes, using attributes and a per-second cash tick, is a valid first prototype (ekM2z9FMhZc).
2. **Make death and failure carry stakes** [[core-loops-and-game-design]]: Treat death as more than a health-zero reset: try a shared team health pool, ghost states that grant abilities, or death loops where knowledge carries over (_rksdF5JoHo). Harsh-but-fair death gives earlier risk-taking meaning. Always give dead players something to do. Refuse features that punish progress, like monetised popups, exponential difficulty and currency-locked walls (Nzrtg8SGOY0).
3. **Debug with breakpoints, not prints** [[testing-debugging-and-qa]]: Use breakpoints with conditions, log points and step over/into/out instead of print statements. Remove breakpoints on hit when debugging loops, and set trigger-at to client or server for shared ModuleScripts (9YwYDuIuih4).
4. **Use RemoteFunctions and RemoteEvents for the right job** [[client-server-and-remotes]]: Use RemoteFunctions when you need a server-calculated return; remember InvokeServer yields until the server returns (Q-xgfPRACcw). Use RemoteEvents for critical actions like firing a gun. Use UnreliableRemoteEvents only for cosmetic, non-critical effects (VitH_k_-AZU).
5. **Keep the server authoritative and secrets off the client** [[anti-exploit-and-security]]: Treat every client message as untrusted and validate movement, collisions and purchases on the server (KbW_p_83hgQ). Put passwords and economy checks on the server. Store sensitive instances in ServerStorage and server-only scripts in ServerScriptService, because anything in ReplicatedStorage is visible to clients (MmYAacyHaSw).
6. **Label instances with tags** [[code-architecture-and-frameworks]]: Use CollectionService tags to mark roles like weapon or collectible. Use GetTagged to fetch them and TagAdded/TagRemoved to react to changes. Tag names are global, so one tag can be shared by many instances, and giving instances a category tag plus a specific tag helps group them (j-yWdoJqV_c).
7. **Clean up everything you spawn** [[scripting-and-performance]]: Destroy created parts after use. In the leak demo, controlled spawns held about 130 to 150 parts, while leaking spawns grew to about 1,000 and made the game unplayable within minutes. Print instance counts to diagnose leaks (D6DwmHcmwwQ). Delete old effects on respawn.
8. **Build UI with Scale, Activated and LocalScripts** [[ui-ux-design]]: Use Scale rather than Offset so layouts hold across devices. Use Activated, not MouseButton1Click, and put button handlers in LocalScripts inside the GUI. Test on multiple device presets before release. Build a colour palette with a role for each colour, and use simple TweenService slide-ins (1KKQ6YrktTk, ZTzUHfMeYKA).
9. **Add cheap juice on first interaction** [[player-psychology-and-game-feel]]: Make feedback play once per part: a 0.2s Back-eased bounce, a highlight colour, and a particle aura whose transparency is 1 minus progress. Delay visual state changes about 0.1s so they land with the tween (Issrodr_wK8, player-feel notes). Cheap details add personality and make the game feel finished.
10. **Monetise with gamepasses and products, not nagging** [[monetisation-gamepasses]]: Use developer products for repeatable purchases and gamepasses for one-time unlocks. Keep shop buttons and pop-ups out of the player's path. Do not paywall basic convenience like auto-collect for 300 Robux while the core loop is tedious (Nzrtg8SGOY0). Where a product price affects cost, check the player's cash on the server before subtracting it.
11. **Price subscriptions and show local prices** [[pricing]]: Create the subscription in Creator Hub and activate it before prompting. Choose durable or consumable based on whether items should persist after cancelling. Show regional prices using GetSubscriptionProductInfoAsync from a LocalScript, and gate benefits with GetUserSubscriptionStatusAsync on the server (7NRp4BEYrsQ). The creator found the UI and perks lacking, so treat it as an optional tool.
12. **Add ads only after you have players** [[ads-and-sponsored-experiences]]: Use an Ad GUI on in-world surfaces like tycoon computer screens, with a fallback image. Roblox pays on impressions and clicks, but ads earn little without traffic. Avoid giant billboards and accidental clicks that send players away (okGvZjneq60). Later advice in this set says to wait for a real player base.
13. **Give grinds and first buyers new hooks** [[retention-d1-d7]]: Introduce a new currency, area or power-up at each grind stage so new players do not quit early. Give first-time buyers a boosted chance so their first reward feels exciting (o-8V99horro). Use these onboarding tweaks to lift day-1 retention before adding monetisation pressure.
14. **Keep event odds honest** [[events-and-seasonal-content]]: Do not quietly change odds at the end of limited events or cut chances after spending, and do not swap duplicate rewards with fallbacks of lower value. The creator calls these tactics manipulative and says players should recognise them (o-8V99horro). Publish odds, and use visible pity counters as a trust signal.

## Key numbers
- Rarity weights out of 100: common 50, rare 30, epic 19, legendary 1 (UUgj-hmX2LM)
- Leak demo: about 130 to 150 parts when destroyed, about 1,000 when leaking, lag in about 5 minutes (D6DwmHcmwwQ)
- Unreliable event test: 0.1s fire interval, about 2 slowdowns observed (VitH_k_-AZU)
- Passive income: awards owned amount times cash-per-second every 1 second (ekM2z9FMhZc)
- Walk speed penalty example: speed = 16 - 0.1 * cash, zero at 160 cash (4yIjd9Xn9sE)
- Mobile target: above about 40 FPS (1KKQ6YrktTk)
- Default offset button example: 82px tall, 354px wide, which breaks across devices (1KKQ6YrktTk)
- Shared health pool example: 100 HP per player, 200 total for two players (_rksdF5JoHo)
- Respawn cap example: 10 free respawns before a knockout loss (_rksdF5JoHo)
- Ghost state: Transparency 0.6 and WalkSpeed +30 (_rksdF5JoHo)
- Bounce tween: 0.2s, Back easing, size +2 studs X/Z (Issrodr_wK8)
- Auto-collect gamepass example: 300 Robux (Nzrtg8SGOY0)
- Pity demo: 30 opens, while real games use far higher thresholds (o-8V99horro)
- Spend before odds cut in demo: about 4,000 Robux; event-end window last 3 to 10 days (o-8V99horro)
- Hitbox lag simulation: 0.5s judged too much, 0.2s more realistic (3rxZj5-Qx30)

## Common mistakes
- Spawning parts or effects without destroying them, which inflates instance count and causes lag (D6DwmHcmwwQ)
- Running a while true loop without a yield, which exhausts execution time (s2XUzTyCdK4)
- Trusting client-reported state such as collidability or economy without server checks (KbW_p_83hgQ)
- Storing passwords or secrets in ReplicatedStorage where clients can read them (MmYAacyHaSw)
- Using Offset sizing, which breaks layouts across phones and tablets (1KKQ6YrktTk)
- Building for PC first and treating mobile as an afterthought (1KKQ6YrktTk)
- Using MouseButton1Click instead of Activated for touch input (1KKQ6YrktTk)
- Subtracting a percentage from small IntValues, where rounding does nothing below about 5 (4yIjd9Xn9sE)
- Placing giant billboard ads or spamming ads everywhere, which hurts retention (okGvZjneq60)
- Paywalling basic convenience while making the core loop tedious (Nzrtg8SGOY0)

## Launch checklist
- [ ] Validate every purchase, collision and economy change on the server
- [ ] Keep passwords and secrets in ServerStorage or ServerScriptService
- [ ] Check that spawned parts and effects are destroyed
- [ ] Test UI on several device presets, including phone sizes
- [ ] Use Scale sizing and Activated for all buttons
- [ ] Verify touch-friendly controls and check FPS on a mobile device
- [ ] Confirm subscriptions are activated in Creator Hub before prompting
- [ ] Show localized prices using GetSubscriptionProductInfoAsync
- [ ] Keep shop and gamepass buttons out of the main gameplay path
- [ ] Confirm no paywall blocks basic convenience
- [ ] Hold ads until you have a real player base
- [ ] Place any ads on in-world surfaces, not spawn billboards
- [ ] Use breakpoints to test edge cases before launch
- [ ] Check rarity or odds weights add up and are published

## How the advice changed over time
- Early videos (Oct 2023 to Apr 2024) are beginner code tutorials on remotes, raycasting, tags and Luau basics, with technical advice only.
- Feb 2024 ads advice says add Ad GUI and earn; later advice (2024 onward) says only add ads once the game has a real player base. Prefer the later stance.
- Jun 2024 incremental video jokes about microtransactions; Sep 2024 and later videos say never add monetised UI interruptions. Prefer the later stance.
- Apr 2024 subscription video calls the feature serious but criticises its UI and perks; treat it as optional rather than a required monetisation path.
- From Sep 2024 onward, content shifts to design and monetisation critique (death, currencies, mobile, Robux satire) rather than pure code.
- Feb 2025 and Mar 2025 videos expose manipulative odds and set the most recent stance: be transparent and avoid manipulative tactics.

## Theme notes
- [[byteblox100 - Retention|Retention]]
- [[byteblox100 - Monetisation|Monetisation]]
- [[byteblox100 - Discovery & Algorithm|Discovery & Algorithm]]
- [[byteblox100 - Game Ideas|Game Ideas]]
- [[byteblox100 - Studio & Scripting|Studio & Scripting]]
- [[byteblox100 - Mindset & Process|Mindset & Process]]
- [[byteblox100 - Games Mentioned]]
- [[byteblox100 - Numbers & Benchmarks]]
- [[byteblox100 - Tools & Resources]]
- Cross-creator knowledge base: [[README]]

## All videos (oldest first)
- [[2023-10-22 - Advanced Server-Client Communication|Advanced Server-Client Communication]] (23,491 views, 2023-10-22): RemoteFunctions: invoke from the client, handle with OnServerInvoke, and note invoking yields until the server returns.
- [[2023-12-16 - How Roblox Exploits Work (+ how to fix them)|How Roblox Exploits Work (+ how to fix them)]] (43,196 views, 2023-12-16): The server holds the truth; clients change only local state, so validate every client message on the server.
- [[2023-12-17 - Roblox Debugging (done efficiently)|Roblox Debugging (done efficiently)]] (13,576 views, 2023-12-17): Use breakpoints, conditions and log points instead of print statements to debug faster.
- [[2024-01-05 - Full Guide to Roblox Raycasting - 2024|Full Guide to Roblox Raycasting - 2024]] (48,977 views, 2024-01-05): Cast a client-side ray from camera through the mouse, excluding your character, since raycasts are cheap.
- [[2024-02-20 - Should Your Roblox Game Have Ads|Should Your Roblox Game Have Ads?]] (25,763 views, 2024-02-20): Ad GUIs pay on impressions; weave ads into in-world screens once you have real players, not billboards.
- [[2024-02-26 - All Use Cases for UnreliableRemoteEvents|All Use Cases for UnreliableRemoteEvents]] (4,807 views, 2024-02-26): Unreliable events suit cosmetic effects; critical actions like gun fire need RemoteEvents, and unreliable functions don't exist.
- [[2024-03-07 - How Are Big Roblox Games Organized|How Are Big Roblox Games Organized?]] (18,577 views, 2024-03-07): CollectionService tags organise instances across the game, with GetTagged, TagAdded and TagRemoved for changes.
- [[2024-04-05 - If you’re a new Roblox dev, watch this|If you’re a new Roblox dev, watch this]] (30,112 views, 2024-04-05): Beginner Luau fundamentals: task.spawn, enums, ModuleScripts, events, scaled GUI, services, TweenService and server versus client.
- [[2024-04-06 - Roblox Monetization Just Became Serious|Roblox Monetization Just Became Serious]] (25,754 views, 2024-04-06): Subscriptions are created in Creator Hub and checked server-side; the creator found the UI and perks lacking.
- [[2024-04-16 - How Unoptimized Can a Roblox Game Get|How Unoptimized Can a Roblox Game Get?]] (336,568 views, 2024-04-16): A comedic counter-example of terrible Luau: redundant variables and needless loops to avoid, with little real guidance.
- [[2024-05-10 - How One Memory Leak Can Kill Your Game|How One Memory Leak Can Kill Your Game]] (41,037 views, 2024-05-10): Parts spawned without Destroy inflate instance count to about 1,000 and lag; clean up and print counts.
- [[2024-05-11 - Programming Rarity is Harder Than You Think|Programming Rarity is Harder Than You Think]] (344,308 views, 2024-05-11): Build weighted rarity from a table summing to 100, with pet models in ReplicatedStorage and a random pick function.
- [[2024-06-07 - How “Impossible” Features Are Actually Coded|How “Impossible” Features Are Actually Coded]] (97,126 views, 2024-06-07): Perceived infinity comes from cloning room modules at attachment points, hidden with fog and lighting, since true infinity is impossible.
- [[2024-06-10 - Why Do Most Games Make Death Boring|Why Do Most Games Make Death Boring?]] (60,807 views, 2024-06-10): Make death meaningful with a shared health pool, ghost states, or death loops where knowledge carries over lives.
- [[2024-06-24 - How to Make a Game Addictive in 15 Minutes|How to Make a Game Addictive in 15 Minutes]] (31,559 views, 2024-06-24): Build a basic incremental buy-button game in about 15 minutes using attributes, a per-second loop and a cash display.
- [[2024-07-06 - Making Good UI is EASY, People Are Just Lazy|Making Good UI is EASY, People Are Just Lazy]] (174,474 views, 2024-07-06): Good UI comes from a palette with assigned roles, scaled sizing, custom image buttons and simple TweenService animations.
- [[2024-09-24 - Every Game is Soulless; And There's a Really Easy Fix|Every Game is Soulless; And There's a Really Easy ]] (393,575 views, 2024-09-24): Cheap feedback like bounce tweens, highlights, progress bars and growing auras makes a simple obby feel polished.
- [[2024-09-29 - 7 Things I'll Never Add as a Roblox Developer|7 Things I'll Never Add as a Roblox Developer]] (180,305 views, 2024-09-29): Refuse features that interrupt, punish or lock progress, such as monetised popups, exponential difficulty and currency walls.
- [[2024-10-12 - The Genius Way That Roblox Prevents Exploits|The Genius Way That Roblox Prevents Exploits]] (58,901 views, 2024-10-12): Clients can see ReplicatedStorage, so hide secrets in ServerStorage and keep passwords and economy checks server-side.
- [[2024-10-24 - How Do You Make Impossible Roblox Features|How Do You Make "Impossible" Roblox Features?]] (376,722 views, 2024-10-24): ViewportFrames can fake optical illusions like transparent parts and low-rate character clones; experimental, not business advice.
- [[2024-11-03 - Why I Hate Roblox Currencies|Why I Hate Roblox Currencies]] (20,734 views, 2024-11-03): Tie currency to walk speed, add inflation, and shift colour toward green as cash nears 1,000 for a design hook.
- [[2024-11-17 - Roblox Mobile Developers Are Insanely Lazy|Roblox Mobile Developers Are Insanely Lazy]] (428,331 views, 2024-11-17): Most mobile games are poor because they're built for PC; use Scale, Activated and device checks to cut effects.
- [[2024-11-20 - I Made Literally Everything Cost Robux|I Made Literally Everything Cost Robux]] (164,263 views, 2024-11-20): Satire: charging Robux for walking is a ToS-violating pitfall the creator deleted rather than shipping.
- [[2025-02-01 - Why Roblox Simulators Punish Players Who Spend Money|Why Roblox Simulators Punish Players Who Spend Mon]] (361,739 views, 2025-02-01): Simulators use pity, spend-based odds cuts and event-end boosts; players should recognise these manipulative tactics.
- [[2025-03-15 - Roblox Has Very Bad Hitboxes & It's Not Their Fault|Roblox Has Very Bad Hitboxes & It's Not Their Faul]] (478,050 views, 2025-03-15): Default hitboxes feel poor; use invisible enlarged hitboxes and account for client-server delay with lag compensation.
