---
title: Player Psychology And Game Feel
topic: player-psychology-and-game-feel
theme: Retention
sources: 124 videos
creators: [1Coal, AlvinBlox, ArTheDev, B Ricey, Bemmy, ByteBlox, CORSO, Cumin, Duckable, Emancyphur, Game Maker's Toolkit, GameMakers, GnomeCode, GosuGamers, JustDucksey, Last Level Studios, Lnor Roblox, MonarchDev, PineappleDev, Raul, RoDev, RoWatcher (tracker blog), Roblox, Roblox Creator Docs, Roblox DevForum, Roblox public API, Roox4, RoyalDev, StudioKrew (agency blog, GGAID data), Suphi Kaner, janisjanis01, rasdev, revolver agz]
source_dates: 2018-05-27 to 2026-11-01
tags: [roblox, knowledge-base, player-psychology-and-game-feel]
---

# Player Psychology And Game Feel

_player motivation, psychology, rewards, game feel and juice, difficulty, flow, behavioural design._

Evidence base: 201 extracted items from 124 videos by 1Coal, AlvinBlox, ArTheDev, B Ricey, Bemmy, ByteBlox, CORSO, Cumin, Duckable, Emancyphur, Game Maker's Toolkit, GameMakers, GnomeCode, GosuGamers, JustDucksey, Last Level Studios, Lnor Roblox, MonarchDev, PineappleDev, Raul, RoDev, RoWatcher (tracker blog), Roblox, Roblox Creator Docs, Roblox DevForum, Roblox public API, Roox4, RoyalDev, StudioKrew (agency blog, GGAID data), Suphi Kaner, janisjanis01, rasdev, revolver agz (2018-05-27 to 2026-11-01). Roblox changes quickly: check the date on each source and see Date context below.

## Overview
Creators teach player feel as layered, immediate feedback: visible and audible reactions, tweened HUD and camera motion kept at restrained amplitude, and haptic or colour-tint polish. Reward design centres on transparent randomness (visible pity counters, fixed published odds), currency that costs something to hold, and cosmetic milestones. Retention comes from reasons to return (teasers, mysteries, always something to do) and moderate punishment, where a leaver loses only the fight. Horror guidance adds controlled tension through isolation, sparse and varied jumpscares, readable lighting, safe rooms, and backstory told through the environment. Official Creator Docs (2026-10) are platform ground truth. Most numeric camera values are single-creator starting points from 2025 indie posts, and several tips are flagged low-advice.

## Rules and findings
- **Give every player action an immediate visible or audible reaction** (one-creator-repeated): Hits, checkpoints, level-ups, pickups and objective progress should each produce a response, or players think the game is broken. Use a second channel because sound-off and hearing-impaired players rely on visuals, while low-vision players rely on audio. Prioritise important feedback with louder volume (sample raised gumdrop-collect to Volume 3). Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/education/build-it-play-it-island-of-move/animations-and-feedback), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/education/build-it-play-it-mansion-of-wonder/using-particles-for-actions), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-2D-audio), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-2D-audio). Newest source 2026-10-28.
- **Sell combat impact with anticipation, a short contact hold and heavy recovery** (one-creator-repeated): Use a big wind-up, a fast strike, a brief hold on contact (around 3 frames), then a heavy recovery. Add motion lines, screen blur, sparks, enemy hurt reactions and crunchy sound. Heavy attacks had longer contact frames than light attacks in the Transformers Devastation example (36 vs 14). Sources: [Game Maker's Toolkit 2018-05 13:53](https://youtu.be/8X4fx-YncqA?t=833), [Game Maker's Toolkit 2018-05 2:43](https://youtu.be/8X4fx-YncqA?t=163), [Game Maker's Toolkit 2018-05 14:38](https://youtu.be/8X4fx-YncqA?t=878). Newest source 2018-05-27.
- **Add short camera moves to attacks and cinematic shots to cutscenes** (one-creator-repeated): A short camera move on attacks makes them feel more powerful, and cinematic shots suit cutscenes. A DevForum commenter noted that few games use camera animation despite its effect, so it is an underused lever. Sources: [Roblox DevForum 2021-04](https://devforum.roblox.com/t/camera-animations-for-cutscenes-and-gameplay/1181691), [Roblox DevForum 2021-04](https://devforum.roblox.com/t/camera-animations-for-cutscenes-and-gameplay/1181691). Newest source 2021-04-22.
- **Use spring-based recoil with decay, random sideways offset and screen shake** (one-creator-repeated): Use a spring module to shove recoil on each shot, then let it decay back down. Add a random sideways offset and screen shake for feel. Example firing settings from the tutorial were 700 rpm, magCapacity 30, velocity 1500 and range 5000. Sources: [Roblox DevForum 2021-05](https://devforum.roblox.com/t/designing-an-fps-framework-beginner%E2%80%99s-guide-part-2/1203507), [Roblox DevForum 2020-05](https://devforum.roblox.com/t/writing-an-fps-framework-part-2-2020/581791). Newest source 2021-05-04.
- **Show disabled or cooldown state clearly, with distinct easing per motion** (single-mention): Raise pickup transparency from 0.4 (enabled) to 0.9 (disabled) during cooldown, and dim PointLight brightness for impact on collection. Use Exponential easing for pickups shrinking on touch and Quad for button presses so motions feel distinct. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/intermediate-scripting/create-a-health-pickup), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/intermediate-scripting/create-a-health-pickup), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/intermediate-scripting/create-a-health-pickup), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/education/build-it-play-it-island-of-move/animating-parts). Newest source 2026-10-28.
- **Use high-contrast focal points to direct attention** (single-mention): Put glowing eyes or tentacle tips on a dark body so players look where the designer wants. Contrast works as a cheap attention-direction tool. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/resources/beyond-the-dark/custom-characters). Newest source 2026-10-28.
- **Set mood immediately on join with opening music** (single-mention): Choose opening music to set the intended mood right away. Swapping an upbeat track for a metal track changes the whole experience. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-2D-audio). Newest source 2026-10-28.
- **Give positive reinforcement on goal completion and specific feedback on struggle** (single-mention): On goal completion, use a burst of particle effects or playful object interaction. When students struggle, give specific improvement feedback rather than only a failure state. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/education/developer/planning-for-educational-settings). Newest source 2026-10-28.
- **Use immediate one-shot audio for score, health and level progress** (one-creator-repeated): Play an immediate one-shot sound when score, health or level progress changes. Players then understand the result of an action without relying on visuals alone. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-2D-audio). Newest source 2026-10-28.
- **Design challenge that is hard but not punishing by default** (multiple-creators): Official guidance: players should be challenged but not frustrated or punished. This conflicts with a Duckable view that frustrating competitive difficulty can drive re-engagement; use the frustrating-retry model only in opt-in competitive modes. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/education/edu-templates/edu-lesson-plan-template), [Duckable 2025-03 4:15](https://youtu.be/I9eyeEG6dpc?t=255). Newest source 2026-10-28.
- **Design wins to feel earned and losses to motivate another attempt** (one-creator-repeated): Competitive difficulty can drive re-engagement if wins feel earned and losses make players want to try again. Pair with clear loss feedback so a loss reads as a learning moment, not a glitch. Sources: [Duckable 2025-03 4:15](https://youtu.be/I9eyeEG6dpc?t=255), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/education/edu-templates/edu-lesson-plan-template). Newest source 2026-10-28.
- **Use randomised reward size, rarity and timing** (multiple-creators): Giving the same reward every time makes players quit. Randomise size, rarity and timing. Tune odds so good results still happen; too much variance feels like pure gambling. Show the odds to keep trust. Sources: [rasdev 2026-04 1:21](https://youtu.be/M-GCMK1Tryk?t=81), [RoDev 2025-05 11:32](https://youtu.be/Gw2FwndwnOg?t=692), [janisjanis01 2025-05 1:07](https://youtu.be/Shjq-Xd9Kmw?t=67). Newest source 2026-04-27.
- **Use variable rewards for each completion, with caution** (one-creator-repeated): Rewards that differ each time a player completes something drive the same compulsion as slot machines (rasdev). Treat this as a powerful, ethically sensitive lever: keep it transparent, and don't let it override fairness or age-appropriateness. Sources: [rasdev 2026-05 5:35](https://youtu.be/q0lIbkUC2r8?t=335), [rasdev 2026-10 5:55](https://youtu.be/53OBGXktIPY?t=355). Newest source 2026-10-20.
- **Build the moment of rare rolls with cutscenes or zoom** (one-creator-repeated): Add rare-roll cutscenes for top rarities to create dopamine spikes that RNG players expect. A janisjanis example: the screen zooms out just before rare results, then switches to a common result. Sources: [janisjanis01 2026-08 8:05](https://youtu.be/pjN_aBDHAfY?t=485), [janisjanis01 2025-05 5:02](https://youtu.be/Shjq-Xd9Kmw?t=302). Newest source 2026-08-30.
- **Frame limited items and daily rewards as losses if the player does not return** (multiple-creators): Players fight harder to avoid losing than to gain. Duckable shows losses on profiles and win-streak resets, and limited items add urgency. Frame daily rewards as something to lose, not just gain. Sources: [rasdev 2026-04 2:42](https://youtu.be/M-GCMK1Tryk?t=162), [Duckable 2025-03 7:19](https://youtu.be/I9eyeEG6dpc?t=439), [Duckable 2025-03 7:19](https://youtu.be/I9eyeEG6dpc?t=439). Newest source 2026-04-27.
- **Use drains to add risk to carried currency** (single-mention): Losing carried currency on death (Elden Ring example) makes exploring new areas feel dangerous as holdings grow. Drains work when the player can recover the loss, so make recovery clear. Sources: [Game Maker's Toolkit 2022-04 10:34](https://youtu.be/Zrf1cou_yVo?t=634). Newest source 2022-04-25.
- **Reward combos, variety and quick kills while penalising damage taken** (single-mention): A scoring system that rewards combos, variety and quick kills while penalising damage lets casual players mash and skilled players chase grades. Sources: [Game Maker's Toolkit 2018-05 12:53](https://youtu.be/8X4fx-YncqA?t=773). Newest source 2018-05-27.
- **Use badges, milestones and status items for replayability** (multiple-creators): Badges for achievements and milestones add replayability beyond the core loop. Give showable status items (rarest or most expensive) and mastery goals worth grinding for. For one-time rewards, allCollected fires only once per player, so pair it with a badge, area access or currency. Sources: [B Ricey 2022-05 1:05](https://youtu.be/T0xqkYODIl0?t=65), [rasdev 2026-04 3:23](https://youtu.be/M-GCMK1Tryk?t=203), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/resources/modules/scavenger-hunt). Newest source 2026-10-28.
- **Use stackable title bonuses and free timed rewards to pace progression** (single-mention): Stackable title bonuses let new slots progress faster, encouraging repeat investment. A free earn-once-every-30-minutes unit roll gives free-to-play players an outlet alongside paid crates. Sources: [revolver agz 2026-09 29:43](https://youtu.be/j3L0K1yZjms?t=1783), [Bemmy 2025-06 1:08](https://youtu.be/-Z0C5YJtnqY?t=68). Newest source 2026-09-18.
- **Let players leave a visible mark on the world** (single-mention): Players enjoy feeling part of constructing the space. Default quota is 2 pieces per player. Use this for shared-building games. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/resources/modules/surface-art). Newest source 2026-10-28.
- **Use a visible world-reaction hook to make areas memorable** (single-mention): Example: ships sail away when the player leaves an area. Small reactive world details make places feel alive and memorable. Sources: [janisjanis01 2024-06 10:35](https://youtu.be/e725ByFD8EI?t=635). Newest source 2024-06-23.
- **Add a live player-progress tracker for competition** (single-mention): Show other players' progress on the server to add competition, as Tower of Hell does. This is an indie self-report. Sources: [1Coal 2023-05 2:01](https://youtu.be/JzB8fpyofnw?t=121). Newest source 2023-05-07.
- **Apply the Xbox test before shipping** (one-creator-repeated): Ask whether a kid's friends would keep watching the gameplay rather than scrolling TikTok. If not, the game doesn't look fun enough. Make the game look and feel fun enough that friends won't reach for their phone. Sources: [1Coal 2023-08 1:04](https://youtu.be/YBSsksqfxo0?t=64), [1Coal 2023-08 1:04](https://youtu.be/YBSsksqfxo0?t=64). Newest source 2023-08-25.
- **Make gameplay match or beat the icon and title promise** (one-creator-repeated): Under-promise and over-deliver: gameplay should match or beat what the icon and title show. Under-promise and deliver is the advice. Sources: [rasdev 2026-09 7:27](https://youtu.be/0_dR_081Hq8?t=447), [rasdev 2026-09 7:27](https://youtu.be/0_dR_081Hq8?t=447). Newest source 2026-09-26.
- **Define target audience and design for multiple player types first** (multiple-creators): Define age range and motivations such as competition and visible progress before designing. Design for Bartle explorers, achievers and socializers so the game appeals broadly. Sources: [rasdev 2026-05 6:32](https://youtu.be/N3L63uyLyQ8?t=392), [Duckable 2025-02 1:43](https://youtu.be/OS-k2iOEfhM?t=103). Newest source 2026-05-18.
- **Keep anti-cheat unobtrusive and avoid hard rejection** (multiple-creators): Invasive checks that pester legit players hurt fun more than exploiters hurt the base game. Only reject at None as a last resort; prefer routing or feature gating, since rejection also hits legitimate players on old or unfixable devices. If rejection is unavoidable, write a custom message that points to a playable mode, since Roblox otherwise shows a generic default. Sources: [Roblox DevForum 2022-01](https://devforum.roblox.com/t/why-your-anti-exploit-sucks/1643298), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/scripting/security/device-trust), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/scripting/security/device-trust). Newest source 2026-10-28.
- **Apply damage with Humanoid:TakeDamage(), not Health** (single-mention): TakeDamage respects active ForceFields so they block damage. Setting Health directly bypasses them. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/detect-hits). Newest source 2026-10-28.
- **Use MaterialVariant with PhysicalProperties to change physics globally** (single-mention): Create a custom MaterialVariant from a base material and set custom PhysicalProperties (e.g., extremely slippery Ice variant) to change gameplay behaviour globally. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/parts/materials). Newest source 2026-10-28.
- **Tie chat bubble styling to events and limit speech-to-text voice broadcast** (single-mention): Use OnBubbleAdded for per-bubble customization, such as VIP styling or highlighting low health. To use speech-to-text without broadcasting voice, disable VoiceChatService.EnableDefaultVoice. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/chat/bubble-chat), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/audio/objects). Newest source 2026-10-28.
- **Keep camera bob and shake subtle** (multiple-creators): Bobbing should stay small; a 10-stud-scale swing can make players leave. Camera bob is the hardest effect to tune, so test with breaks, because over-attending to bob makes it seem stronger than it is. Sources: [Roblox DevForum 2020-06](https://devforum.roblox.com/t/creating-a-simple-realistic-camera-with-view-bobbing-dynamic-blur-sprinting/646943), [Roblox DevForum 2020-06](https://devforum.roblox.com/t/creating-a-simple-realistic-camera-with-view-bobbing-dynamic-blur-sprinting/646943), [Roblox DevForum 2020-06](https://devforum.roblox.com/t/creating-a-simple-realistic-camera-with-view-bobbing-dynamic-blur-sprinting/646943), [PineappleDev 2025-01 2:00](https://youtu.be/hHKQEohHqwU?t=120). Newest source 2025-01-10.
- **Drive camera feel from movement state** (one-creator-repeated): Set FOV from normalised velocity, clamped to a max speed, and lerp it so running widens the view and stopping zooms back in. Scale bob frequency and amplitude with walk state using a sine of tick() times speed. Tilt Z-angle with clamped turn rate, then smooth back to upright each frame. Sources: [PineappleDev 2025-01 5:29](https://youtu.be/hHKQEohHqwU?t=329), [PineappleDev 2025-01 8:14](https://youtu.be/hHKQEohHqwU?t=494), [PineappleDev 2025-01 11:40](https://youtu.be/hHKQEohHqwU?t=700), [PineappleDev 2025-01 2:43](https://youtu.be/hHKQEohHqwU?t=163), [PineappleDev 2025-01 3:24](https://youtu.be/hHKQEohHqwU?t=204). Newest source 2025-01-10.
- **Smooth the camera around 16 by default** (single-mention): Use camera smoothing of about 16 as a baseline. Raise it for a snappier camera and lower it for a floaty, cinematic feel, which suits horror. Tune unknown camera values by pushing one value to an extreme, play-testing, then settling. Sources: [PineappleDev 2025-01 4:07](https://youtu.be/hHKQEohHqwU?t=247), [PineappleDev 2025-01 3:24](https://youtu.be/hHKQEohHqwU?t=204), [PineappleDev 2025-01 4:07](https://youtu.be/hHKQEohHqwU?t=247). Newest source 2025-01-10.
- **Lerp picked-up objects toward screen centre** (single-mention): Move a picked-up object to screen centre with Vector3:Lerp(..., 0.2) each frame rather than teleporting it. The alpha of 0.2 gives a smooth, readable pickup motion. Sources: [Roblox DevForum 2020-05](https://devforum.roblox.com/t/perspective-object-dragging-like-superliminal/566200), [Roblox DevForum 2020-05](https://devforum.roblox.com/t/perspective-object-dragging-like-superliminal/566200). Newest source 2020-05-09.
- **Choose easing for the motion's feel** (multiple-creators): Use Exponential or Circular for fast-start, slow-stop motion; Linear reads as mechanical. Quint or Quart start more snappily than Quad or Cubic. Use Exponential Out for HUD changes. Advice is low-advice, so verify by feel. Sources: [Roblox DevForum 2020-12](https://devforum.roblox.com/t/understanding-easing-styles/937281), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-hud-meters), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-hud-meters). Newest source 2026-10-28.
- **Tween HUD bars instead of snapping** (single-mention): Tween health bar size and colour over about 0.5 s with Exponential Out. Keep one-shot audio immediate for health and score changes; the audio fires instantly while the visual tweens. Replace the default red screen-edge damage tint with a ColorCorrectionEffect if wanted. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-hud-meters), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-hud-meters), [ByteBlox 2024-09 26:42](https://youtu.be/Issrodr_wK8?t=1602). Newest source 2026-10-28.
- **Time and limit feedback effects** (one-creator-repeated): Delay a visual state change about 0.1 s so it lands with the tween rather than before it. Play per-part feedback such as bounce only on first interaction, so effects stay meaningful instead of repeating. Sources: [ByteBlox 2024-09 26:42](https://youtu.be/Issrodr_wK8?t=1602), [ByteBlox 2024-09 33:44](https://youtu.be/Issrodr_wK8?t=2024). Newest source 2024-09-24.
- **Pair menu open and close with a short UI sound** (single-mention): Add a brief UI sound to panel open and close transitions. Small audio on menu actions adds juice without blocking play. Low-advice, so test with players. Sources: [PineappleDev 2025-05 6:14](https://youtu.be/Iz2ljOdZRJI?t=374). Newest source 2025-05-08.
- **Give distinct victory and defeat feedback** (single-mention): On round end, show different UI text and audio for winners and losers so each outcome reads clearly. This complements earned wins and motivating losses by making the result itself unmistakable. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/add-rounds). Newest source 2026-10-28.
- **Add haptics for tactile feel** (single-mention): Use HapticEffect with types such as GameplayCollision, GameplayExplosion and UIClick to add touch feedback beyond visuals and audio. Support is on most modern iPhone, Pixel and Samsung Galaxy devices, so treat it as an enhancement, not the only cue. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/input/mobile). Newest source 2026-10-28.
- **Tint the screen to signal danger or fear** (multiple-creators): Use ColorCorrectionEffect TintColor to signal state, such as red when health is low. The same tint can darken or colour the screen as fear rises. Keep the environment itself readable. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/environment/post-processing-effects), [Roblox DevForum 2021-12](https://devforum.roblox.com/t/how-to-make-a-terrifying-horror-game/1583917), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-hud-meters). Newest source 2026-10-28.
- **Gate effects client-side by location and state** (single-mention): Only play visual and audio effects when the local player can perceive them, for example indoors or in the right game state. This stops hidden players receiving FX and saves client work. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/develop-a-moving-world). Newest source 2026-10-28.
- **Smooth position only on large divergence** (single-mention): Apply smoothing only when the simulated object jumps far from the rendered one, as Soccer does. Normal play then has no visual latency, and corrections are visible only when needed. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/projects/server-authority/techniques). Newest source 2026-10-28.
- **Animate ambient life in the world** (single-mention): Add swaying trees, falling leaves, NPC activity, birds, butterflies and a day/night script. Ambient motion brings a scene to life and makes the world feel reactive without gameplay cost. Sources: [Roblox DevForum 2020-08](https://devforum.roblox.com/t/map-design-and-scene-building-fantasy-medieval-and-nature-maps/709866). Newest source 2020-08-06.
- **Keep leaver punishment proportional** (multiple-creators): Treat a leaver as having lost the fight, not as having suffered a harsher penalty. Disconnects from crashes, network issues or misclicks are common, and harsh penalties drive players away. Sources: [Roblox DevForum 2020-08](https://devforum.roblox.com/t/how-to-catch-combat-logging/743912), [Roblox DevForum 2020-08](https://devforum.roblox.com/t/how-to-catch-combat-logging/743912). Newest source 2020-08-27.
- **Give players a reason to return** (multiple-creators): Show upcoming content and unresolved mysteries so players expect more. Keep something always available to do, since players should continuously have something to do. This sits beside, not instead of, loss-framed limited items. Sources: [Roblox DevForum 2021-03](https://devforum.roblox.com/t/how-to-make-your-game-have-replayability/1082534), [ByteBlox 2024-06 11:16](https://youtu.be/_rksdF5JoHo?t=676). Newest source 2024-06-10.
- **Show a visible pity counter for top rewards** (one-creator-repeated): Guarantee a top reward after N opens with a pity counter that resets on a legendary drop. Players trust visible pity systems more than hidden ones. Keep the counter on screen so the guarantee is verifiable. Sources: [ByteBlox 2025-02 13:37](https://youtu.be/o-8V99horro?t=817). Newest source 2025-02-01.
- **Keep drop odds fixed and published** (one-creator-repeated): Publish odds and keep them fair and simple, citing Brawl Stars as the model. Avoid one-in-a-billion odds for mass rewards. Changing legendary odds by outcome is manipulative, so avoid it or use only transparently. Sources: [ByteBlox 2025-02 25:43](https://youtu.be/o-8V99horro?t=1543), [ByteBlox 2025-02 22:15](https://youtu.be/o-8V99horro?t=1335). Newest source 2025-02-01.
- **Apply luck boosts as multipliers below one** (single-mention): Multiply the roll by a boost value under 1 (for example 0.1 gives 10x effective luck). This keeps boosts compatible with weighted tables and makes the effect easy to reason about. Sources: [PineappleDev 2025-07 1:33](https://youtu.be/QRkRk-FHN4s?t=93), [PineappleDev 2025-07 6:21](https://youtu.be/QRkRk-FHN4s?t=381). Newest source 2025-07-15.
- **Use a short perfect-block window with a stun** (single-mention): Open a perfect-block window of about 0.1 s after pressing block. On success stun the attacker; otherwise apply a normal block hit. The tight window rewards timing skill over button mashing. Sources: [ArTheDev 2025-07 29:32](https://youtu.be/Pi8rQ9gGTKE?t=1772), [ArTheDev 2025-07 29:32](https://youtu.be/Pi8rQ9gGTKE?t=1772). Newest source 2025-07-25.
- **Make enemy behaviour unpredictable** (single-mention): Mix random wandering with sudden attacks so players stay tense rather than learning a fixed pattern. Low-advice, so validate the frequency of surprise attacks in play-tests. Sources: [JustDucksey 2025-10 2:05](https://youtu.be/XZKHQPObHgw?t=125). Newest source 2025-10-09.
- **Make carried money costly and keep it flowing** (one-creator-repeated): Tie money to a gameplay effect, such as walk speed = 16 - 0.1 * cash (zero at 160 cash), so holding cash has a cost. Add a periodic percentage deduction (e.g. 10% per second) to keep money circulating. Roblox rounds integers, so small balances may not decrease. Sources: [ByteBlox 2024-11 14:30](https://youtu.be/4yIjd9Xn9sE?t=870), [ByteBlox 2024-11 15:54](https://youtu.be/4yIjd9Xn9sE?t=954), [ByteBlox 2024-11 19:32](https://youtu.be/4yIjd9Xn9sE?t=1172), [ByteBlox 2024-11 16:29](https://youtu.be/4yIjd9Xn9sE?t=989), [ByteBlox 2024-11 14:30](https://youtu.be/4yIjd9Xn9sE?t=870). Newest source 2024-11-03.
- **Reward milestones with cosmetics and an animated screen** (one-creator-repeated): Pair a milestone with a cosmetic unlock and a dedicated animated milestone screen so progress feels special. Cosmetics are a reliable reward that rarely fails to motivate. Sources: [PineappleDev 2025-03 4:47](https://youtu.be/IEAr0I_sUV4?t=287), [PineappleDev 2025-03 5:28](https://youtu.be/IEAr0I_sUV4?t=328). Newest source 2025-03-04.
- **Isolate the player and make them feel vulnerable** (one-creator-repeated): Minimise NPC and player interaction unless it serves the story, to isolate the player. Limit movement speed, disorient them and make combat risky as fear rises, so the player feels weak. Sources: [Roblox DevForum 2021-12](https://devforum.roblox.com/t/how-to-make-a-terrifying-horror-game/1583917), [Roblox DevForum 2021-12](https://devforum.roblox.com/t/how-to-make-a-terrifying-horror-game/1583917). Newest source 2021-12-10.
- **Make characters relatable and tell backstory through the world** (one-creator-repeated): Make characters likable so players bond and care about their impact on the story. Reveal the villain's backstory through clues, notes, corpses, decals and enemy placement rather than dialogue, and mix emotions such as sadness. Sources: [Roblox DevForum 2021-12](https://devforum.roblox.com/t/how-to-make-a-terrifying-horror-game/1583917), [Roblox DevForum 2021-12](https://devforum.roblox.com/t/how-to-make-a-terrifying-horror-game/1583917), [Roblox DevForum 2023-03](https://devforum.roblox.com/t/guide-to-making-better-horror-experiences/2212571). Newest source 2023-03-09.
- **Build tension with buildup, release and recovery** (one-creator-repeated): Alternate buildup and release, then give recovery time such as safe rooms or calm areas. Use quest or activity logs so distracted players can recover track of objectives. Avoid false safety unless you know what you are doing, since it can backfire. Sources: [Roblox DevForum 2023-03](https://devforum.roblox.com/t/guide-to-making-better-horror-experiences/2212571), [Roblox DevForum 2021-07](https://devforum.roblox.com/t/making-accessible-games-for-the-disability-aware-era-a-not-fully-comprehensive-guide-by-an-actual-disabled-developer/1375919), [Roblox DevForum 2021-12](https://devforum.roblox.com/t/how-to-make-a-terrifying-horror-game/1583917). Newest source 2023-03-09.
- **Use jumpscares sparingly and varied** (one-creator-repeated): Make jumpscares expected but not predictable, and never repeat the same scare every time. Frequent scares dull their effect. Sources: [Roblox DevForum 2023-03](https://devforum.roblox.com/t/guide-to-making-better-horror-experiences/2212571). Newest source 2023-03-09.
- **Break your own rules late for unease** (multiple-creators): Late in the game, break rules you established earlier, since uncertainty scares more than a known threat. Keep illusions consistent: if players are never given reason to doubt, the illusion holds regardless of objective truth. Sources: [Roblox DevForum 2023-03](https://devforum.roblox.com/t/guide-to-making-better-horror-experiences/2212571), [ByteBlox 2024-06 2:03](https://youtu.be/s2XUzTyCdK4?t=123), [ByteBlox 2024-06 2:03](https://youtu.be/s2XUzTyCdK4?t=123). Newest source 2024-06-07.
- **Keep horror scenes lit enough to be scary** (one-creator-repeated): Avoid overly dark or poorly lit scenes. Lamps should give sufficient light, otherwise progression becomes painful rather than scary. Sources: [Roblox DevForum 2021-12](https://devforum.roblox.com/t/how-to-make-a-terrifying-horror-game/1583917). Newest source 2021-12-10.
- **Punish players who ignore the environment** (one-creator-repeated): Let neglect have visible consequences, such as an unfed pet dying, to keep players attentive. This works as a subtle horror touch that rewards environmental awareness. Sources: [Roblox DevForum 2021-12](https://devforum.roblox.com/t/how-to-make-a-terrifying-horror-game/1583917). Newest source 2021-12-10.
- **Telegraph enemy and boss attacks visibly, then open a vulnerability window** (multiple-creators): Give each heavy attack a readable windup (e.g. lift leg, pause, stomp) so players can dodge or parry, then leave a clear window to punish afterwards. Creators say unreadable boss attacks make combat feel unfair and unsatisfying. Note the Roox4 source is low-advice. Sources: [Roox4 2024-07 9:40](https://youtu.be/OYfrdTxNdjA?t=580), [Cumin 2025-12 5:16](https://youtu.be/hQpC_UHxJDU?t=316). Newest source 2025-12-23.
- **Balance chasers with escape options** (single-mention): Pair any chasing enemy with escape tools such as vents, doors, freeze items or NPC help. This keeps the game co-operative and stops it being too hard for average players. Sources: [Emancyphur 2020-09 5:42](https://youtu.be/C0ybJ5ghSHk?t=342). Newest source 2020-09-17.
- **Replace QTEs with physical actions in VR** (single-mention): In VR, swap quick-time prompts for a physical gesture the player performs with their body (e.g. shaking a hand to break free). Creator reports players did it instinctively without being told. Sources: [Last Level Studios 2021-12 36:48](https://youtu.be/v_TGu45AD_g?t=2208). Newest source 2021-12-09.
- **Compose custom music for cutscenes and chapters** (single-mention): Use music written for the game to set tone for each cutscene and chapter, not only the opening screen on join. This extends the existing join-music rule to every story beat. Sources: [Emancyphur 2020-09 7:47](https://youtu.be/C0ybJ5ghSHk?t=467). Newest source 2020-09-17.
- **Show currency gain animations on screen** (single-mention): When money or currency is earned, play an on-screen gain animation so players can see exactly what they got. This is the most recent advice on reward feedback (2026-09). Sources: [Lnor Roblox 2026-09 2:56](https://youtu.be/gSFxStWqmgM?t=176). Newest source 2026-09-23.
- **Pace reward delivery instead of flooding the screen** (single-mention): Avoid stacking many numbers and loot-box style openings at once. Reviewer contrasts a slower reward pace favourably. Keep feedback brief and let each reward land. Low-advice source. Sources: [Cumin 2025-04 11:58](https://youtu.be/YmAwFbqUA0U?t=718). Newest source 2025-04-06.
- **Sell cosmetic trails as a status sink** (single-mention): Let players buy cosmetic trails with an in-game currency so progression currency has a use beyond unlocks. This gives a visible status purchase that drains earned currency. Sources: [Lnor Roblox 2026-09 7:47](https://youtu.be/gSFxStWqmgM?t=467). Newest source 2026-09-23.
- **Let companions be fed, upgraded and stay relevant** (single-mention): Let players feed or upgrade companions and keep them useful across zones so they feel like partners rather than disposable pets. Reviewer cites Bee Swarm over Pet Simulator. Low-advice source. Sources: [Cumin 2025-04 10:36](https://youtu.be/YmAwFbqUA0U?t=636). Newest source 2025-04-06.
- **Front-load fun; never rely on 'it gets better later'** (one-creator-repeated): Early movement and the core activity must already feel good. Forced long waits for seeds or crops made the creator lose interest within minutes. Do not ask players to endure a slow start for a later payoff. Sources: [Cumin 2025-06 12:34](https://youtu.be/Z1tj1OPOEZg?t=754), [Cumin 2025-05 7:43](https://youtu.be/E7bedfC8A10?t=463), [Cumin 2025-05 7:43](https://youtu.be/E7bedfC8A10?t=463). Newest source 2025-06-08.
- **Keep respawn timers short** (single-mention): Use a few seconds for shooters and about a minute at most for MOBAs. Long waits make the game boring and cut the time players have to learn. Sources: [Cumin 2025-07 4:57](https://youtu.be/jXogdTgtlXE?t=297). Newest source 2025-07-31.
- **Keep death penalties below losing some gold** (single-mention): Losing half the carried gold per death plus a long walk back frustrates players. Keep the penalty to a small loss of gold and avoid stacking travel time on top of it. Sources: [Cumin 2025-12 10:36](https://youtu.be/hQpC_UHxJDU?t=636). Newest source 2025-12-23.
- **Avoid power upgrades that split casual and tryhard tiers** (single-mention): Power upgrades that only serve one player tier make balancing nearly impossible. Design upgrades that work across skill levels. Low-advice source. Sources: [CORSO 2025-05 1:21](https://youtu.be/O2LZcQG5PPQ?t=81). Newest source 2025-05-29.
- **Make higher difficulty add variation, not just damage** (single-mention): Harder modes should change enemy behaviour, layout or mechanics. Raising only enemy damage gives replaying no engagement. Sources: [Cumin 2026-02 6:44](https://youtu.be/ROo_Xpms4ok?t=404). Newest source 2026-02-07.
- **Prefer hard-to-get rewards over pure RNG rarity** (single-mention): A creator says players would rather earn a reward through effort than receive a rare random drop. Use this to shape rare rewards, while keeping randomised timing where it adds surprise. Sources: [CORSO 2024-09 5:19](https://youtu.be/lFD1wKdwSUs?t=319). Newest source 2024-09-05.
- **Let progress accrue while the player is away** (multiple-creators): Idle mechanics support retention in fishing-style games (RoWatcher, self-reported). StudioKrew (GGAID-based, self-reported) advises that a game should not punish stepping away, since that supports daily-active play. Use offline or idle income, and avoid resets or penalties for absence. Sources: [RoWatcher (tracker blog) 2026-03](https://rowatcher.com/news/top-10-roblox-games-by-players-march-2026-data-breakdown), [StudioKrew (agency blog, GGAID data) 2026-05](https://studiokrew.com/blog/top-roblox-games-may-2026/). Newest source 2026-05-00.
- **Deepen gear progression with tradeable rare catches** (single-mention): RoWatcher (self-reported) cites deep rod- and lure-style progression plus trading of rare catches as retention drivers in fishing games. Give players layered gear tiers that change catch outcomes, and make rare catches scarce enough to be worth trading. Sources: [RoWatcher (tracker blog) 2026-03](https://rowatcher.com/news/top-10-roblox-games-by-players-march-2026-data-breakdown). Newest source 2026-03-00.
- **Use timed random spawns for scarcity** (single-mention): GosuGamers (self-reported) recommends limited-time random pet spawns across the map instead of a permanent egg shop. Scarcity and urgency come from the spawn window, which gives a reason to log in now. Pair with the fixed, published-odds rule for rare results. Sources: [GosuGamers 2026-06](https://www.gosugamers.net/entertainment/news/78614-grow-a-garden-2-has-launched-on-roblox-here-s-everything-new-added-in-this-sequel). Newest source 2026-06-12.
- **Make collectibles feed the core loop directly** (single-mention): Official Roblox API guidance: pets can act as speed multipliers, so riding a pet makes the player faster. Collection then changes how the core loop plays, not just how it looks. Check any speed multiplier against the rule on casual versus tryhard tier splits before shipping. Sources: [Roblox public API 2026-11](https://www.roblox.com/games/95168737547508/). Newest source 2026-11-01.
- **Make hits connect instantly and visibly** (single-mention): Hit registration should feel immediate: the player's input should produce a visible hit reaction without perceptible delay. Jujitsu Shenanigans is cited as connecting instantly and tying visible world reaction to each hit. Test input-to-visual latency directly rather than assuming it is fine. Sources: [Roblox 2026-09 49:05](https://youtu.be/HXZRH-2zurk?t=2945). Newest source 2026-09-17.
- **Playtest yourself and replay after every change** (single-mention): Do not treat AI-generated design as a finished judgement of fun. AI cannot assess whether a design is fun. Play the build yourself, change something, and replay the loop. AI output is only a starting point for iteration. Sources: [Roblox 2026-10 26:18](https://youtu.be/KB5iAzy86Fo?t=1578). Newest source 2026-10-12.
- **Give at least about 2 seconds of warning before instant death** (one-creator-repeated): A trigger timer that ends in instant death within about 2 seconds feels unfair. Show a visible countdown or wind-up cue first, so the player can read the threat and react before the lethal outcome. Sources: [Cumin 2026-08 12:37](https://youtu.be/rjPW4GeeyFg?t=757), [Cumin 2026-08 12:37](https://youtu.be/rjPW4GeeyFg?t=757). Newest source 2026-08-22.
- **Give stalker enemies readable cues and a persistent presence** (single-mention): Stalkers should have an audio or visual cue, plus a physical presence the player can track. This lets players read the enemy's position and react instead of being ambushed by something they cannot see. Sources: [Cumin 2026-08 13:37](https://youtu.be/rjPW4GeeyFg?t=817). Newest source 2026-08-22.
- **Do not chain threats back-to-back** (one-creator-repeated): Avoid starting a new chase or threat before the player has reached the next room or had a breather. Stacked threats remove recovery time and can make the experience feel exhausting rather than tense. Leave deliberate calm gaps between encounters. Sources: [Cumin 2026-08 12:37](https://youtu.be/rjPW4GeeyFg?t=757), [Cumin 2026-08 14:58](https://youtu.be/rjPW4GeeyFg?t=898), [Cumin 2026-08 12:37](https://youtu.be/rjPW4GeeyFg?t=757). Newest source 2026-08-22.
- **Balance AI-generated enemies before release** (single-mention): Enemies produced by AI generation can be badly tuned. One developer found generated wolves far too strong in testing. Playtest and adjust health, damage and speed for every generated enemy before shipping. Sources: [MonarchDev 2026-10 6:09](https://youtu.be/QwdZRB6xRKk?t=369). Newest source 2026-10-12.
- **Cap on-rails camera turn to a readable arc** (single-mention): In on-rails shooting segments, limit the camera's turn range to about 100 degrees. This keeps the aim range readable and stops the player from losing track of targets. Sources: [Cumin 2026-08 7:42](https://youtu.be/rjPW4GeeyFg?t=462). Newest source 2026-08-22.
- **Tune difficulty from real death and session data** (single-mention): Do not rely only on designer intent. Watch where players actually die and how sessions end, then adjust. Escalate threats in small steps so each new threat is learned before the next one arrives. Sources: [Roox4 2023-11 5:44](https://youtu.be/kKiPL7wc8Rc?t=344). Newest source 2023-11-26.
- **Lead players forward with ambient sound and light under doors** (single-mention): Use directional ambient sound cues and light glowing under doors or gaps to pull players toward the next area. This adds tension and guidance at almost no cost, without UI markers. Sources: [GnomeCode 2025-02 10:45](https://youtu.be/-oZIdFe8qHk?t=645). Newest source 2025-02-22.
- **Keep high challenge hard but not impossible, with something always happening** (single-mention): Hard sections should remain beatable. Keep other activity going during them (sounds, pickups, ambient events) so players stay engaged rather than stalling on a single obstacle. Refines the existing hard-but-not-punishing rule. Sources: [GnomeCode 2025-02 13:31](https://youtu.be/-oZIdFe8qHk?t=811). Newest source 2025-02-22.
- **Add hover and click sounds to every button, including runtime buttons** (single-mention): Connect hover and click audio to all buttons. Use DescendantAdded on the GUI container so buttons created at runtime (for example inventory items) also receive sounds, instead of wiring only buttons present at load. Sources: [PineappleDev 2025-03 1:21](https://youtu.be/2z4rebjBnQA?t=81). Newest source 2025-03-03.
- **Tune throw boost to control throw distance** (single-mention): When dropping or throwing, add a velocity boost on release and adjust its value to set throw distance. The creator's far-throw example used 20. Treat that as a starting point to playtest, not a fixed standard. Sources: [PineappleDev 2025-03 3:52](https://youtu.be/E6Bev4VCWeA?t=232). Newest source 2025-03-21.
- **Disguise a threat as harmless, then transform it** (single-mention): Let a scary enemy look harmless at first, then transform on a trigger such as nightfall. A visible transition animation adds tension and surprise. Works well alongside horror pacing that breaks expectations late. Sources: [JustDucksey 2025-07 6:59](https://youtu.be/s5nooZlK5Pc?t=419). Newest source 2025-07-27.
- **Make solo play viable or clearly label it unsupported** (single-mention): If the game advertises 3-4 players but solo players cannot find a party, they quit. Either make solo play genuinely fun or state clearly that it is unsupported. This is recent advice (June 2026). Sources: [Cumin 2026-06 16:53](https://youtu.be/2IdxQNOGoqA?t=1013). Newest source 2026-06-24.
- **Treat any paid gameplay advantage as pay-to-win** (single-mention): Any purchase that gives a gameplay advantage will be perceived as pay-to-win, regardless of designer intent. Judge paid items by how players will read them, not by how you meant them. This complements the existing rule on avoiding power upgrades that split casual and tryhard tiers. Sources: [GameMakers 2022-11 25:03](https://youtu.be/NaR3-VIg5-I?t=1503). Newest source 2022-11-24.
- **Keep monetization transparent so players do not feel manipulated** (one-creator-repeated): Players who feel manipulated drop off. Transparent monetization produces kinder participation and better retention. When players sense they are treated as a wallet, the battle is very hard to win; when they are having fun, they spend willingly. Sources: [GameMakers 2022-11 40:41](https://youtu.be/NaR3-VIg5-I?t=2441), [GameMakers 2022-11 40:41](https://youtu.be/NaR3-VIg5-I?t=2441), [GameMakers 2024-03 20:36](https://youtu.be/zvNQHk1hUYc?t=1236). Newest source 2024-03-08.
- **Read the player's emotional state and offer calm content when needed** (single-mention): Players may be anxious or stressed by outside events. A calm themed map or area during such periods can bring players back on its own; one example reported players returning just to see a calm themed map added during COVID-era anxiety. Sources: [GameMakers 2024-03 13:48](https://youtu.be/zvNQHk1hUYc?t=828). Newest source 2024-03-08.
- **Gate premium currency behind time or progress** (single-mention): Make currency available only after time or progress so spending feels earned. This is the velvet-rope model (as used in Club Penguin) and also underpins battle passes. Avoid giving instant access to currency that players can buy straight away. Sources: [GameMakers 2024-08 29:16](https://youtu.be/gp_hDijjC4U?t=1756). Newest source 2024-08-12.
- **Design cosmetics and status for four player types** (single-mention): Expect achievers chasing rare items, self-expressers changing outfits often, speculators treating items as assets, and competitors showing status. Offer rare, tradeable, and status-signalling items as well as frequent outfit changes so each type has a reason to spend. Sources: [GameMakers 2024-08 37:49](https://youtu.be/gp_hDijjC4U?t=2269). Newest source 2024-08-12.
- **Rotate difficulty spikes rather than keeping them on** (single-mention): Raising difficulty can produce revenue spikes, but overusing it hurts retention. Rotate harder phases in and out. Higher rewards, by contrast, drove retention and stickiness in the same report, so pair difficulty pushes with rewarding returns. Sources: [GameMakers 2025-02 4:32](https://youtu.be/qZRNpN5M8jA?t=272). Newest source 2025-02-04.
- **Stage area unlocks as a multi-sense event** (one-creator-repeated): When an area unlocks, combine a door-slide animation, a screen shake, smoke particles and a sound effect. The source says this makes the unlock feel rewarding. Egg opening and pad unlocks also need sound, since near-silent games feel flat. Sources: [janisjanis01 2024-12 2:31](https://youtu.be/Jc7yQTMFexk?t=151), [janisjanis01 2024-04 6:12](https://youtu.be/7z8XlhAtGpQ?t=372). Newest source 2024-12-01.
- **Celebrate shop purchases with confetti and sound** (single-mention): Add confetti and a sound effect when a player buys something in the shop. The source calls this cheap polish that makes buying feel more rewarding. Sources: [janisjanis01 2024-11 15:09](https://youtu.be/vJekPDaIT30?t=909). Newest source 2024-11-17.
- **Use streaks and leaderboard positions as loss-aversion hooks** (single-mention): Use win streaks, leaderboard positions and login streak rewards so players feel they will lose progress if they stay away. Frame return prompts around what the player stands to lose, not only what they gain. Sources: [rasdev 2026-04 2:01](https://youtu.be/yFKY2FlwHjE?t=121). Newest source 2026-04-30.

## Checklist
- [ ] Check every player action (hit, pickup, checkpoint, level-up, objective) produces a visible or audible reaction.
- [ ] Pair each important visual cue with a sound cue, and each audio cue with a visual, for accessibility.
- [ ] Raise volume on high-priority feedback (e.g., Volume 3 on collect) rather than on routine sounds like jumps.
- [ ] Add a short camera move on attacks; add a cinematic shot for cutscenes.
- [ ] Tune recoil with a spring module: shove, decay, random sideways offset, screen shake.
- [ ] Use a brief contact hold (~3 frames) and a heavy recovery for combat impact.
- [ ] Set pickup disabled state explicitly (transparency 0.4 enabled to 0.9 disabled; dim PointLight).
- [ ] Pick opening music that sets the intended mood on join.
- [ ] Write a scoring system that rewards combos and variety and penalises damage taken.
- [ ] Define target audience and motivations before building.
- [ ] Run the Xbox test on gameplay footage before publishing.
- [ ] Make the icon and title promise something the gameplay already delivers.
- [ ] Use badges and milestones for replayability.
- [ ] Use allCollected for a one-time reward per player.
- [ ] Use TakeDamage (not Health) so ForceFields work.
- [ ] Avoid hard rejection; gate features or route players, and write a custom message if rejection is unavoidable.
- [ ] Keep anti-cheat unobtrusive so legit players aren't pestered.
- [ ] If using randomised rewards, show odds and ensure good results still happen.
- [ ] Use rare-roll cutscenes for top rarities if you have a rarity system.
- [ ] Frame limited items and daily rewards as losses if the player does not return.
- [ ] Give a free earn-once timed reward alongside any paid crates.
- [ ] Offer a cheap first purchase to bring in new spenders (rasdev, 2026-10).
- [ ] Add a live progress tracker for competitive games.
- [ ] Use a world-reaction hook (e.g., ships sail away) to make areas memorable.
- [ ] Start camera at smoothing about 16 and FOV 60; change one value at a time to an extreme, play-test, then settle.
- [ ] Keep bob amplitude small and test it with breaks, since over-attention exaggerates bob.
- [ ] Drive FOV from clamped normalised velocity and lerp it; drive bob from walk state, not idle.
- [ ] Lerp picked-up objects toward screen centre (alpha about 0.2) instead of teleporting them.
- [ ] Tween HUD bars about 0.5 s with Exponential Out; keep one-shot health and score audio immediate.
- [ ] Delay visual state changes about 0.1 s so they land with the tween.
- [ ] Limit per-part feedback (such as bounce) to first interaction.
- [ ] Add a short UI sound to menu open and close.
- [ ] Play a chime on collectable touch and a particle effect when a task completes.
- [ ] Show distinct victory and defeat text plus audio on round end.
- [ ] Add HapticEffect for collisions, explosions and UI clicks, and check device support.
- [ ] Tint the screen with ColorCorrectionEffect for low health or rising fear.
- [ ] Gate FX client-side by player location and game state.
- [ ] Smooth position only when the simulated object diverges far from the rendered one.
- [ ] Animate ambient life such as swaying trees, leaves, birds, NPCs and day/night.
- [ ] Apply leaver penalties no harsher than losing the fight.
- [ ] Show upcoming content and unresolved mysteries to create reasons to return.
- [ ] Add a visible pity counter that guarantees a top reward after N opens.
- [ ] Publish drop odds and keep them fixed; do not shift odds by outcome.
- [ ] Apply luck boosts as multipliers below 1 (0.1 = 10x).
- [ ] Use a 0.1 s perfect-block window that stuns the attacker on success.
- [ ] Randomise enemy wandering with occasional sudden attacks.
- [ ] Tie carried cash to a speed penalty and add a periodic percentage deduction to keep money moving.
- [ ] Pair milestones with a cosmetic unlock and an animated milestone screen.
- [ ] For horror, keep scenes lit, limit jumpscares, add safe rooms, and tell backstory through the environment.
- [ ] Add a readable windup and a punish window to every heavy enemy and boss attack.
- [ ] Give every chasing enemy at least one escape tool (vent, door, freeze item or NPC help).
- [ ] Replace any VR quick-time prompt with a physical gesture.
- [ ] Write or commission music for each cutscene and chapter, not just the join screen.
- [ ] Show an on-screen gain animation for every currency earned.
- [ ] Stagger large reward reveals so one moment is not buried under many numbers.
- [ ] Let a sink item (cosmetic trails or similar) use progression currency.
- [ ] Make early core actions fun without forced waits for crops, seeds or similar.
- [ ] Set respawn timers to a few seconds for shooters and no more than about 60 seconds for MOBAs.
- [ ] Cap death losses to a small gold penalty and avoid long walk-backs on top.
- [ ] Test that upgrades serve casual and competitive players alike.
- [ ] Make higher difficulty change enemy behaviour or layout, not only damage.
- [ ] If the game has idle or offline income, confirm that absence causes no reset, decay or penalty.
- [ ] If the game has collectible pets or mounts, decide what each one changes in the core loop (speed, income, reach) before adding more.
- [ ] If a collectible is meant to be scarce, use a timed map-wide spawn window rather than a permanent shop.
- [ ] If pets give a speed multiplier, test it against the casual-versus-tryhard tier rule.
- [ ] If the game has gear tiers or rare catches, make sure tiers change outcomes and rare catches can be traded or shown off.
- [ ] Measure input-to-visual hit latency and confirm each hit shows an immediate reaction
- [ ] Pair each instant hit with a visible world reaction where the design allows it
- [ ] After every tuning change, play the loop yourself and replay it before moving on
- [ ] Treat any AI-generated mechanic, balance or feel values as a draft until playtested
- [ ] Before shipping a timed lethal trigger, confirm a visible warning of at least about 2 seconds exists before the kill.
- [ ] For any stalker or chaser enemy, add an audio or visual cue and keep it physically present in the scene so its position stays readable.
- [ ] Check the sequence of threats in each area and insert a calm gap or safe room between encounters so the player can recover.
- [ ] Playtest every AI-generated enemy's stats (health, damage, speed) before release and rebalance them.
- [ ] On on-rails or fixed-track shooting segments, limit camera turn range to roughly 100 degrees.
- [ ] Log deaths and session-end points in playtests and use them to adjust difficulty.
- [ ] Add hover and click sounds to all buttons, and connect runtime-created buttons with DescendantAdded.
- [ ] Expose throw boost as a tunable value and playtest throw distance with it.
- [ ] Check that solo players can find a match; if not, label the mode as unsupported in the store description.
- [ ] Place ambient sound and light cues to guide players toward the next objective.
- [ ] Before adding a paid item, check whether it gives any gameplay advantage; if it does, assume players will call it pay-to-win and reconsider or tier it.
- [ ] Publish clear rules on what each paid item does and does not change.
- [ ] Gate premium currency behind time or progress rather than selling instant access.
- [ ] Offer both rare, status-signalling items and frequent outfit-style items so achievers, self-expressers, speculators and competitors each have a reason to spend.
- [ ] Schedule difficulty spikes in rotation and track retention after each spike.
- [ ] Pair harder challenge with clear reward upgrades so difficulty does not drive players away.
- [ ] During periods of external stress, consider adding calm themed content or areas.
- [ ] Review monetization feedback from players for signs of feeling manipulated and adjust before retention drops.
- [ ] Add a sound effect to egg openings and pad unlocks.
- [ ] Add confetti and a sound effect to shop purchases.
- [ ] Add a door-slide, screen shake, smoke particles and a sound effect to area unlocks.
- [ ] Show win streaks and leaderboard positions clearly in the UI so losing them is visible.
- [ ] Frame login streak rewards around what the player loses by missing a day.

## Numbers and benchmarks

| Metric | Value | Context | Sources |
|---|---|---|---|
| Hold on contact (combat impact) | ~3 frames | Transformers Devastation hit-pause: two characters hold the same pose for 3 frames. GMT 2018 example. | [Game Maker's Toolkit 2018-05 13:53](https://youtu.be/8X4fx-YncqA?t=833), [Game Maker's Toolkit 2018-05 14:38](https://youtu.be/8X4fx-YncqA?t=878) |
| Light vs heavy attack contact frames | Light 14 frames; heavy 36 frames | Transformers Devastation example (GMT 2018). Heavy attacks have longer contact. | [Game Maker's Toolkit 2018-05 2:43](https://youtu.be/8X4fx-YncqA?t=163) |
| Pickup transparency enabled / disabled | 0.4 enabled; 0.9 disabled (cooldown) | Official Roblox docs visual states. Use for disabled feedback. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/intermediate-scripting/create-a-health-pickup), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/intermediate-scripting/create-a-health-pickup), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/intermediate-scripting/create-a-health-pickup) |
| Bridge countdown timer duration | 5 seconds | Default in official tutorial; configurable via timerDuration variable. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/tutorials/fundamentals/coding-4/create-a-timed-bridge) |
| Photo countdown length | countdownSeconds default 3 | Countdown before photo taken; tune with countdownSeconds, countdownBeepSound, countdownFlashSound. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/resources/modules/photo-booth) |
| Default quota for player-placed pieces | 2 pieces per player | Official docs default for leave-a-mark building feature. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/resources/modules/surface-art) |
| Gumdrop-collect sound volume | Volume 3 | Official sample: raised for priority feedback vs lower jump sound volume. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-2D-audio) |
| Free unit roll cadence | Earn once every 30 minutes | Bemmy 2025 example of free outlet alongside paid gacha crates. | [Bemmy 2025-06 1:08](https://youtu.be/-Z0C5YJtnqY?t=68) |
| Animation transition blend time | 0 = instant switch | Animation:Play blend length in seconds; 0 gives no blending (Black Magic 2, 2020). | [Roblox DevForum 2020-05](https://devforum.roblox.com/t/procedural-animation-what-it-is-and-how-to-do-it/564782) |
| Example firing settings | 700 rpm, magCapacity 30, velocity 1500, range 5000 | Tutorial example from 2020 DevForum; not a standard. | [Roblox DevForum 2020-05](https://devforum.roblox.com/t/writing-an-fps-framework-part-2-2020/581791) |
| Camera smoothing default | 16 | Raise for snappier camera, lower (e.g. horror) for floaty, cinematic feel. | [PineappleDev 2025-01 4:07](https://youtu.be/hHKQEohHqwU?t=247), [PineappleDev 2025-01 4:07](https://youtu.be/hHKQEohHqwU?t=247) |
| Default FOV / walk FOV change / max FOV velocity / FOV smooth | 60 / 8 / 10 / 3 | PineappleDev 2025-01 starting values for velocity-driven FOV. | [PineappleDev 2025-01 2:43](https://youtu.be/hHKQEohHqwU?t=163) |
| Camera bob settings | Bob speed 2, bob distance 2, walk bob multiplier 55, walk velocity threshold 9 | PineappleDev 2025-01 values; starting point, tune per game. | [PineappleDev 2025-01 2:00](https://youtu.be/hHKQEohHqwU?t=120) |
| Viewmodel bob and sway starting values | Bob speed 1.5, distance 0.1, walk multi 3, velocity threshold 9, sway speed 1.1, sway distance 0.7, sway multi 2, smoothing 50 | Starting values for a viewmodel bob and sway script. | [PineappleDev 2025-01 2:25](https://youtu.be/2HRX5AqBfNA?t=145) |
| Camera offset and lean | Y offset 2 studs, turn lean 320, turn lean smoothing 0.9, max vertical angle 80 degrees | Lean is clamped and smoothed back to upright each frame. | [PineappleDev 2025-01 3:24](https://youtu.be/hHKQEohHqwU?t=204) |
| Camera weight (lerp divisor) | WEIGHT 20 horizontal, 5 vertical example; 1 = no weight | Each tick moves subject 1/WEIGHT of remaining distance; lower vertical weight suits wide screens. | [Roblox DevForum 2021-07](https://devforum.roblox.com/t/how-to-add-weight-to-the-camera-camera-tutorial/1331996), [Roblox DevForum 2021-07](https://devforum.roblox.com/t/how-to-add-weight-to-the-camera-camera-tutorial/1331996) |
| Pickup lerp alpha | 0.2 per frame | Smooth centring of a picked-up object. | [Roblox DevForum 2020-05](https://devforum.roblox.com/t/perspective-object-dragging-like-superliminal/566200), [Roblox DevForum 2020-05](https://devforum.roblox.com/t/perspective-object-dragging-like-superliminal/566200) |
| HUD bar tween duration | 0.5 s (Exponential Out) | Health bar size and colour tween; OFFICIAL Creator Docs. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-hud-meters), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-hud-meters) |
| Visual state change delay | about 0.1 s | Delay so the change lands with the tween. | [ByteBlox 2024-09 26:42](https://youtu.be/Issrodr_wK8?t=1602) |
| Perfect block window | 0.1 s after pressing block | Successful perfect block stuns the attacker. | [ArTheDev 2025-07 29:32](https://youtu.be/Pi8rQ9gGTKE?t=1772), [ArTheDev 2025-07 29:32](https://youtu.be/Pi8rQ9gGTKE?t=1772) |
| Sprint double-tap threshold | 2 s between two W presses | ArTheDev 2025-10 sprint trigger. | [ArTheDev 2025-10 2:38](https://youtu.be/KaCj7Jld35Q?t=158) |
| Walk speed penalty from cash | Speed = 16 - 0.1 * cash; zero at 160 cash | ByteBlox 2024-11 example implementation. | [ByteBlox 2024-11 15:54](https://youtu.be/4yIjd9Xn9sE?t=954) |
| Character colour threshold from cash | grey (127,127,127) to green at 1,000 cash; clamped percentage = cash / 1000 | ByteBlox 2024-11 visual cue for money held. | [ByteBlox 2024-11 19:32](https://youtu.be/4yIjd9Xn9sE?t=1172) |
| Inflation deduction example | 10% per second | Periodic percentage deduction; Roblox rounds integers so small balances may not drop. | [ByteBlox 2024-11 16:29](https://youtu.be/4yIjd9Xn9sE?t=989) |
| Luck boost example | 0.1 multiplier = 10x effective luck | Lower boost multiplier means higher effective luck. | [PineappleDev 2025-07 6:21](https://youtu.be/QRkRk-FHN4s?t=381), [PineappleDev 2025-07 1:33](https://youtu.be/QRkRk-FHN4s?t=93) |
| Time to master one TF2 weapon | about 200 hours; plus 50 hours per new primary | Author's estimate, indie, 2021-03; a mastery benchmark rather than a fact. | [Roblox DevForum 2021-03](https://devforum.roblox.com/t/how-to-make-your-game-have-replayability/1082534) |
| Bobbing scale warning | a 10-stud difference cited as extreme | DevForum 2020; cited as enough to make players leave; units not comparable to bob settings. | [Roblox DevForum 2020-06](https://devforum.roblox.com/t/creating-a-simple-realistic-camera-with-view-bobbing-dynamic-blur-sprinting/646943), [Roblox DevForum 2020-06](https://devforum.roblox.com/t/creating-a-simple-realistic-camera-with-view-bobbing-dynamic-blur-sprinting/646943) |
| Respawn timer (shooters) | a few seconds | Creator's recommended maximum for shooter games; longer waits make the game boring. | [Cumin 2025-07 4:57](https://youtu.be/jXogdTgtlXE?t=297) |
| Respawn timer (MOBAs) | about 1 minute max | Creator's recommended maximum; longer waits cut learning time. | [Cumin 2025-07 4:57](https://youtu.be/jXogdTgtlXE?t=297) |
| Gold lost per death (anti-benchmark) | half of carried gold | Cited as too punishing when combined with a long walk back; keep losses to a small amount. | [Cumin 2025-12 10:36](https://youtu.be/hQpC_UHxJDU?t=636) |
| Player count for Jujitsu Shenanigans (cited as example of responsive hits) | 160k players | Official Roblox source, 2026-09. Point-in-time figure cited as evidence that instant hit feedback with world reaction can draw a large audience; not a benchmark for other games. | [Roblox 2026-09 49:05](https://youtu.be/HXZRH-2zurk?t=2945) |
| Lethal trigger timer warning (fair minimum heuristic) | about 2 seconds | Instant death ending a trigger timer within about 2 seconds of the trigger was described as unfair. Self-reported indie design guidance. | [Cumin 2026-08 12:37](https://youtu.be/rjPW4GeeyFg?t=757) |
| Clown transformation wind-up before kill mode near the player | about 2 seconds | Time between the clown's transformation starting and it reaching kill mode near the player. Self-reported indie example from a horror game. | [Cumin 2026-08 12:37](https://youtu.be/rjPW4GeeyFg?t=757) |
| Camera turn range on roller-coaster on-rails shooting | about 100 degrees | Limited aim range in the on-rails shooting segment. Self-reported indie example. | [Cumin 2026-08 7:42](https://youtu.be/rjPW4GeeyFg?t=462) |
| Blur effect tween (Teleport transition) | 0 to 24 over 1s, back to 0 after 10s | Blur tween in a local script for a teleport transition. Source is 2022, so treat the timings as a starting point. | [Suphi Kaner 2022-08 14:23](https://youtu.be/c4DymnlVuL0?t=863) |
| Throw boost velocity for far throw | 20 | Speaker's example value for a far throw. Unit and scale are not specified; tune by playtest. | [PineappleDev 2025-03 3:52](https://youtu.be/E6Bev4VCWeA?t=232) |

## Where creators agree
- Visible and audible feedback on every action is needed: T7126, T9574, T8217, T9573 (all official Roblox docs).
- Loss aversion and loss framing work: T6143, T6440, Q975 (Duckable and rasdev) and drains in T5677 (GMT).
- Randomised rewards drive engagement, but odds must be fair: T6437, T6194, Q982.
- Under-promise and deliver: T6813 and Q1095 (rasdev).
- Define audience first: T6527 (rasdev) and T6097 (Duckable, Bartle types).
- Impact juice relies on several channels combined: T4979 (GMT) and Roblox camera and recoil items T5462, T5476.
- Avoid hard rejection and invasive anti-cheat: T5626 (DevForum) and T8617 (official).
- Challenge should be hard but fair, not frustrating or punishing (T14432, T15245, plus existing rule on hard-but-not-punishing).
- Keep camera motion subtle; extreme bob drives players away (T10706, Q1155, T12519).
- Keep punishments proportional; a leaver loses the fight, not more (T10791, Q1162).
- Cosmetics and milestones are dependable motivators (T12594, Q1302).
- Visible, fair randomness builds trust (T12555, T12558).
- Immediate audio plus tweened visuals is the right split for HUD feedback (T15454, N6039, T12336).
- Enemy and boss attacks must be readable so players can dodge or parry, otherwise combat feels unfair (Roox4, Cumin).
- Early-game fun must not depend on long waits or a 'gets better later' promise (Cumin, supported by the Q1538 quote).
- RoWatcher (T17470) and StudioKrew (T17476) both treat tolerance of player absence and idle progress as a driver of return play, though neither gives a figure.

## Where creators disagree
- **Whether frustration drives retention**
  - Duckable (T6140): competitive difficulty that provokes frustration can drive re-engagement.
  - Roblox Creator Docs (T8754, official): design challenge so players are challenged but not frustrated or punished.
  - Resolution: the official line is the safer default; reserve frustration-driven retry loops for opt-in competitive modes.
- **How far to push randomised and variable rewards**
  - RoDev (T6194): too much variance feels like pure gambling; tune odds so good results still happen.
  - rasdev (T6479, T6878) and janisjanis (Q982): variable rewards drive slot-machine-like compulsion; use luck, rarity and timed events to keep players spinning.
  - Tension is ethical and commercial, not a mechanical contradiction. Keep odds visible and avoid manipulative framing aimed at minors.
- **Whether camera animation is commonly used or valuable**
  - Roblox DevForum (T5462): camera animation makes attacks feel more powerful; use it.
  - Roblox DevForum commenter (Q912): barely any games use camera animations, though a good camera adds power.
  - Not a true conflict: value is agreed, while the Q912 usage observation is dated (2021).
- **Darkness as a fear tool**
  - Roblox DevForum (T11201): darken the screen as fear rises to make players feel weak.
  - Roblox DevForum (T11209): avoid overly dark or poorly lit scenes; progression becomes painful rather than scary.
- **Rewarding high-skill play**
  - Existing rule: reward combos, variety and quick kills by default.
  - Roblox DevForum (T11216): decide deliberately; heavy skill rewards can make consistent execution second nature and unbalance play.
- **Adjusting odds by outcome**
  - ByteBlox (T12555): visible pity counters are trusted and effective.
  - ByteBlox (T12556): lowering or raising legendary odds after results is manipulative; use deliberately and fairly if at all.
- **On-screen reward feedback and pacing**
  - Cumin (2025-04, T16152) warns against flooding the screen with numbers and loot-box style openings and prefers slower pacing.
  - Lnor Roblox (2026-09, T16685) recommends on-screen money and currency gain animations so players see what they earned.
- **Random rarity versus hard-to-get rewards**
  - CORSO (2024-09, Q1530) says players would 100% prefer hard-to-get rewards over RNG rarity.
  - Existing rule 'Use randomised reward size, rarity and timing' favours randomness.
- **Whether absence should carry any cost**
  - Existing rule: frame limited items and daily rewards as losses if the player does not return.
  - StudioKrew (T17476, 2026-05): do not punish stepping away; absence should cost nothing.

## Date context (what may be outdated)
- Newest and most authoritative source: Roblox Creator Docs (2026-10, official). Prefer its platform mechanics (TakeDamage/ForceField T7907, rejection T8617/T8618, speech-to-text T7635, MaterialVariant T8116) over older community guidance.
- 2018-2022 GMT, DevForum and 1Coal items are older community advice. Frame counts, firing settings (N2301, 2020) and animation blend (N2299, 2020) are examples and may be out of date with current engine behaviour.
- The 2025-2026 monetisation items (rasdev, janisjanis, Bemmy, revolver agz, Duckable) reflect a more aggressive randomised-reward and loss-framing trend than the 2018 GMT and 2022 advice. Treat them as current practice, not endorsed standards, and check current Roblox policy on random item sales.
- Q912 (2021, camera animation rarely used) is a dated observation; usage may have changed.
- Indie claims about revenue, CCU or engagement are unverified self-reports; no such claims were verified here.
- Roblox Creator Docs (2026-10, OFFICIAL) items are the most current platform ground truth: distinct win/lose feedback, HapticEffect, client-side FX gating, smoothing only on divergence, ColorCorrectionEffect tints and the 0.5 s HUD tween. Prefer them for API facts.
- Indie camera values from PineappleDev (2025-01) are newer than 2020-2021 DevForum camera and tween advice (T10668, T10706, N4261), which are older starting points.
- Horror advice dates from 2021-12 and 2023-03; treat its specifics as older and validate against current play-tests.
- Items flagged low-advice (T10888, T12738, T12998, T13593, N5738-N5741) should be treated as lower confidence and verified in play.
- Economy and odds advice (ByteBlox 2024-11 to 2025-02) predates or may not reflect current regulations on randomised paid rewards; check current policy before shipping.
- Advice about camera bob was given in 2020 and 2025 at different magnitudes; the 2025 values are creator-specific, not universal.
- Sources span 2020-09 to 2026-09. Newest items (Lnor 2026-09, Cumin 2025-12 to 2026-02) take precedence where they conflict with older advice.
- Emancyphur (2020) and Last Level Studios (2021) advice is older; the VR QTE tip applies only to VR projects.
- Several items are tagged low-advice (Roox4, Cumin, CORSO); treat them as lower-confidence.
- All creator figures are self-reported indie experience, not platform data; no official Roblox guidance is included here.
- T17476 (2026-05) is newer than the existing loss-framing rule for non-return, whose date is not known. Where they conflict, prefer the no-punishment advice for absence in general. Use timed scarcity (T17496) for urgency rather than loss framing.
- T17563 is official platform guidance dated 2026-11. Confirm the pet speed-multiplier behaviour against current Roblox docs before relying on exact values.
- T17470, T17476 and T17496 are indie, self-reported, and dated 2026-03 to 2026-06. Treat them as anecdotal.
- T17692 (2026-09, official) and T17715 (2026-10, official) are the newest items. Neither contradicts existing rules; both add to existing responsiveness and iteration guidance.
- T17715 states AI output is only a starting point. Advice on AI-assisted design should be read with this caveat as of 2026-10.
- New items are dated 2026-08 (Cumin) and 2026-10 (MonarchDev). None of them supersede existing rules; they add new failure modes (unfair instant death, threat stacking, unbalanced AI-generated enemies).
- T17910 is flagged [low-advice] and is a single anecdote; treat it as a prompt to playtest rather than a firm benchmark.
- All figures in this batch are self-reported by indie developers, not official Roblox guidance.
- T18379 (2026-06) is the newest item and adds solo-play guidance on top of the older multiple-player-type rule.
- N7746 (2022-08) is the oldest item; its blur timings are a single example and may not match current Roblox effect practice.
- Items T18066, T18230 and T18277 are marked [low-advice] and should be treated as weaker guidance.
- New items span 2022-11 to 2025-02 (GameMakers, indie, self-reported). Monetization-perception advice is from 2022 onward and has not been contradicted by later items in this batch.
- Nothing here overrides existing rules; no conflicts with the most recent advice in the knowledge file.
- As of 2026-11, platform monetization policies and Roblox's own monetization tools may have changed since these 2022-2025 indie sources; check current platform rules before relying on specific monetization mechanics.
- janisjanis01 items (T18761, T18822, T18840) date from 2024-04 to 2024-12. rasdev items (T18934, T18935) date from 2026-04. None of the new items conflict with existing rules, so no recency override applies.
- janisjanis01 is marked low-advice; treat their polish tips as optional rather than required.

## Instructions for an agent using this file
- If the user asks for combat or attack feel, then combine anticipation, a short contact hold, heavy recovery, a camera nudge, recoil and layered audio rather than a single effect.
- If a player action has no visible or audible response, then add immediate feedback (sound, particle, state change) before adding anything else.
- If the user asks for randomised rewards or gacha, then show odds, guarantee that good results still happen, and flag the ethical and policy check before recommending compulsion-style tactics.
- If the user asks to make the game more frustrating for retention, then recommend challenge without punishment by default and only suggest frustration-driven retry loops for opt-in competitive modes.
- If the user asks about anti-cheat or kicking players, then prefer unobtrusive checks and feature gating over hard rejection; write a custom message if rejection is needed.
- If the question is about platform mechanics (damage, ForceField, physics, chat, rejection, speech), then answer from Roblox Creator Docs (2026-10) and override older community advice.
- If the user asks for numeric values (frame counts, transparency, blend time, firing settings), then quote them as examples from the named source, not as standards, and note their age.
- If the user cites revenue, CCU or engagement figures from these creators, then label them as unverified indie self-reports.
- If the user is starting a new game, then define target audience and motivation first, then design for multiple player types, then run the Xbox test on gameplay footage.
- If the icon or title promises a feature, then verify gameplay delivers it or exceeds it before publishing.
- If building camera feel from scratch, start with smoothing about 16 and FOV 60, then tune one value at a time.
- If a player-visible value changes, tween HUD visuals about 0.5 s and keep the one-shot audio immediate.
- If a random reward has a guarantee, show the pity counter and keep the published odds fixed.
- If a player leaves or disconnects, do not apply a penalty beyond losing the current fight.
- If designing horror, keep scenes readable, limit jumpscares, and place safe rooms after high-tension beats.
- If a combat timing window is added, use about 0.1 s and pair it with a stun on success.
- If choosing easing, prefer Exponential or Circular for fast-start, slow-stop motion; avoid Linear for feel.
- Prefer OFFICIAL Creator Docs (2026-10) over indie figures for APIs and platform behaviour; treat indie numbers as starting points.
- If a numeric value is cited from one creator, verify it in your own play-test before shipping.
- Do not change drop odds based on past outcomes; that pattern is labelled manipulative.
- If designing a boss or heavy enemy attack, then add a visible windup and a vulnerability window before finalising it.
- If a game has a chasing enemy, then add escape options before tuning its speed.
- If a reward is earned, then show an on-screen gain animation and avoid stacking several reveals at once.
- If core activity requires long waits early on, then redesign the early loop rather than relying on later payoff.
- If designing higher difficulty, then change behaviour or layout rather than only raising damage.
- If setting death penalties, then keep carried-currency loss small and avoid long walk-backs.
- If tuning respawn timers, then keep them at a few seconds for shooters and no more than about a minute for MOBAs.
- If a rule conflicts with the existing random-rarity rule, then weigh player preference for earned rewards and document the trade-off.
- If a source is tagged low-advice, then treat it as a hypothesis to test rather than a settled rule.
- If a design includes idle or offline income, do not add a penalty for absence (T17470, T17476).
- If a design uses scarce collectibles, prefer timed map-wide spawns over a permanent egg or shop (T17496).
- If a design uses pets or mounts as speed multipliers, treat that as official guidance (T17563) and check the tier-split rule.
- If a source is indie and self-reported (T17470, T17476, T17496), do not present its claims as measured benchmarks.
- If absence punishment and urgency conflict, use scarcity windows for urgency, not loss framing for non-return.
- If a player action produces a hit or impact, verify the reaction shows immediately before adding further juice.
- If the task involves AI-generated design, balance or feel values, label them as a draft and recommend a playtest-and-replay pass before shipping.
- Do not claim a design is fun based only on AI evaluation; recommend human playtesting.
- If a design includes an instant-death timer, add a visible warning of at least about 2 seconds before the lethal outcome.
- If a design includes a stalker or chaser enemy, add an audio or visual cue and keep the enemy physically visible or trackable.
- If a level sequence has several threats in a row, insert a calm gap or safe space before the next threat.
- If enemies are AI-generated, do not ship them without a balance pass on health, damage and speed.
- If the camera is locked to a rail or track, cap the turn range near 100 degrees so the player can keep aim readable.
- Treat self-reported figures (2 seconds, 100 degrees) as starting points and verify them in playtests.
- If a player-facing difficulty change is proposed, check it against real death and session data before accepting it as balanced.
- If a GUI has buttons created at runtime, connect hover and click sounds through DescendantAdded, not a one-time loop.
- If a threat is meant to escalate, add it in steps and avoid introducing several new threats at once.
- If the game is advertised for multiple players, verify solo matchmaking works or state clearly that it is unsupported.
- Use ambient sound and light cues to guide players before resorting to on-screen markers.
- If a proposed paid item gives any gameplay advantage, flag it as pay-to-win risk and recommend a cosmetic or time-gated alternative.
- If monetization changes are proposed, favour transparent, published rules over hidden mechanics, since players who feel manipulated drop off.
- If premium currency is being designed, gate it behind time or progress rather than making it instantly purchasable.
- If a difficulty spike is proposed for revenue, schedule it as a rotation and check retention impact rather than making it permanent.
- If external events are stressing players, consider adding calm content before pushing high-intensity challenge.
- When designing cosmetic or status items, cover achievers, self-expressers, speculators and competitors explicitly.
- Treat indie-sourced monetization figures and anecdotes as self-reported and unverified; corroborate with official platform data before committing to them.
- If a player action completes an unlock or purchase, add both a sound and a visual payoff (particles, confetti, shake or animation).
- If a return or login reward is designed, frame the message around what the player stands to lose by not returning.
- Treat loss-aversion hooks as optional polish that depends on the audience; do not add them where they would punish absence in a way that feels manipulative.

## Not covered here (research elsewhere)
- No retention, conversion or monetisation metrics are verified across these sources; the analysis relies on indie self-reports.
- No guidance on Roblox policy for random item odds disclosure, age restrictions or regulatory compliance for loot-box-style mechanics.
- No quantitative difficulty tuning method (e.g., target win rates, death counts) or playtest methodology.
- Limited accessibility detail beyond visual and audio redundancy (colour-blind palettes, reduced motion, input-specific UX for mobile and controller).
- No measurement guidance for juice or game feel (how to A/B test effects or camera shake).
- Little coverage of how loss-aversion and drain mechanics affect player trust or churn over time.
- No detail on engine-specific tuning values for spring modules or camera shake amplitude beyond the cited example.
- No official guidance on exact camera bob, FOV or motion-sickness and accessibility thresholds.
- No retention or engagement benchmarks; no A/B data on pity counters, reward ratios or punishment levels.
- Legal and platform-policy limits on randomised paid rewards (loot-box rules, Roblox policy) are not covered.
- Audio design specifics such as layering, mixing and ducking are not covered.
- Performance cost of ambient life, camera scripts and FX is not covered.
- Haptics: device support is summarised only; no code or testing guidance.
- Horror tuning numbers (jumpscare frequency, light levels, safe-room spacing) are not given.
- Economy sink and faucet tuning beyond the single 10%/s example is not covered.
- Psychology theory (flow, motivation models, self-determination) is not sourced; advice is practical, not research-backed.
- Combat timing values for genres other than the ArTheDev example are not covered.
- No playtest or retention data with sample sizes; all figures are self-reported.
- No quantitative telegraph windup or vulnerability window durations for bosses.
- No Roblox-specific implementation guidance for chase AI, VR input or UI gain animations.
- No data on how companion progression affects long-term retention.
- Narrative perspective-taking (Q1492) is not covered by this topic.
- No comparison data for on-screen reward pacing versus player retention.
- No retention or DAU figures are given for idle mechanics or absence tolerance.
- No tuning values for idle or offline income rates.
- No data on trading economies, including dupe or anti-cheat handling for traded rare catches.
- No official numbers for pet speed multipliers or how they stack.
- No guidance on spawn frequency, window length or how spawn scarcity affects player spend.
- No evidence beyond fishing games for the idle and trading advice.
- No detail on how Jujitsu Shenanigans implements its hit latency or world reaction (networking, client prediction, effects).
- No measurable latency targets (milliseconds) for instant hit feedback.
- No playtest method, session length, or fun metrics beyond 'play it yourself and replay'.
- No guidance on how to structure replay testing across different player types.
- No official Roblox documentation in this batch on reaction-time design, stalker AI, or AI-generated asset balancing.
- No data on how reaction time varies by platform, input method or player skill level.
- No playtest metrics showing how much threat stacking hurts retention or completion.
- No details on how the on-rails camera limit was tested or whether it varied by device.
- No guidance on how to balance AI-generated enemies beyond the single anecdote from T17910.
- No units or scale given for throw boost velocity (T18230).
- No guidance on hover and click sound volume, pitch or whether to debounce rapid hover events (T18206).
- No playtest sample sizes or thresholds for reading death and session data (T18066).
- No information on how to balance solo versus party matchmaking (T18379).
- No measured durations for ambient sound cues versus other guidance methods (T18197).
- No quantitative data: no conversion rates, retention figures, price points, or A/B results are given for any of these monetization or difficulty claims.
- No official Roblox guidance on player perception of pay-to-win, monetization policy, or DevEx rules is covered; research platform documentation separately.
- No method is given for measuring player perception of pay-to-win or manipulation (surveys, feedback signals, or retention proxies).
- The velvet-rope and battle-pass claims are not tied to any specific Roblox monetization mechanic, so implementation details must be researched separately.
- Evidence is from one indie creator (self-reported); cross-creator corroboration is missing.
- No guidance on how to rotate difficulty concretely (cadence, length of spikes, or how to detect over-use).
- No retention, conversion or engagement figures are given for confetti, sound, shake or unlock animations.
- No timing or duration guidance for confetti, screen shake or door-slide animations.
- No ethical limits are given for loss-aversion mechanics beyond the general monetisation-transparency rule.
- Sources are indie, self-reported and not verified against official Roblox documentation.

## Quotes (near-verbatim)
- "The bobbing shouldn't be a 10 stud difference; that can easily cause players to leave your game." ([Roblox DevForum 2020-06 ](https://devforum.roblox.com/t/creating-a-simple-realistic-camera-with-view-bobbing-dynamic-blur-sprinting/646943))
- "try not to punish too harshly - i.e. don't over-punish beyond what would happen if they lost the battle." ([Roblox DevForum 2020-08 ](https://devforum.roblox.com/t/how-to-catch-combat-logging/743912))
- "I want to teach a lesson that generally, in real life, arguments are usually made through not seeing through someone's perspective." ([Emancyphur 2020-09 10:36](https://youtu.be/C0ybJ5ghSHk?t=636))
- "To be honest, there are barely any games that use camera animations. Even though a good camera can make an attack feel much more powerful." ([Roblox DevForum 2021-04 ](https://devforum.roblox.com/t/camera-animations-for-cutscenes-and-gameplay/1181691))
- "the audience sort of recognizes that they're not being manipulated... they react a little more kindly to their participation in the game" ([GameMakers 2022-11 40:41](https://youtu.be/NaR3-VIg5-I?t=2441))
- "You need to make your game look and feel so fun that Albert's friends won't pull out their phone and scroll through TikTok." ([1Coal 2023-08 1:04](https://youtu.be/YBSsksqfxo0?t=64))
- "If the players are being treated like a wallet, it's a very hard battle to win; if they're having fun they'll happily spend money." ([GameMakers 2024-03 20:36](https://youtu.be/zvNQHk1hUYc?t=1236))
- "I think we're good on the 10% aspect however I think it's changing too slowly maybe 5 seconds is a little too long" ([ByteBlox 2024-03 8:52](https://youtu.be/lJ_ZwfNHkQU?t=532))
- "if you make the players believe that it is and you don't leave any room for doubt then it's a real optical illusion" ([ByteBlox 2024-06 2:03](https://youtu.be/s2XUzTyCdK4?t=123))
- "you want your game to be played 24/7 ... you want people to continuously have something to do" ([ByteBlox 2024-06 11:16](https://youtu.be/_rksdF5JoHo?t=676))
- "if it's like between RNG like being rare and being hard to get I definitely think people would 100% prefer hard to get" ([CORSO 2024-09 5:19](https://youtu.be/lFD1wKdwSUs?t=319))
- "A good economy always has money flowing; no one got rich from just saving their money." ([ByteBlox 2024-11 14:30](https://youtu.be/4yIjd9Xn9sE?t=870))
- "it's good to hint towards something scary... I'm not a big fan when games do that... I do like it when games slowly build up to something" ([ByteBlox 2025-01 4:37](https://youtu.be/K-KvVwt_Y4I?t=277))
- "Sometimes you just want to play the game by yourself right that's how it works" ([ByteBlox 2025-01 17:16](https://youtu.be/RkgxOf3iZfA?t=1036))
- "Cosmetics, the one thing that has never failed anyone ever." ([PineappleDev 2025-03 5:28](https://youtu.be/IEAr0I_sUV4?t=328))
- "People are more worried about losing than they are excited about winning." ([Duckable 2025-03 7:19](https://youtu.be/I9eyeEG6dpc?t=439))
- "The novelty of growing a garden kind of ran out fast when I found out that I have to wait to buy the freaking seeds." ([Cumin 2025-05 7:43](https://youtu.be/E7bedfC8A10?t=463))
- "The trick is that you don't always get what you want, but the chances are always visible." ([janisjanis01 2025-05 1:07](https://youtu.be/Shjq-Xd9Kmw?t=67))
- "When you're about to roll something really rare, your screen starts to zoom out... half a second later, it switches to garbage." ([janisjanis01 2025-05 5:02](https://youtu.be/Shjq-Xd9Kmw?t=302))
- "If your game requires effort before joy, then you're bleeding retention." ([AlvinBlox 2025-06 3:21](https://youtu.be/Y93DRfB-Deo?t=201))
- "at least that game had attempts at making me feel dopamine. Like, this one, I'm going to freaking die." ([Cumin 2025-08 8:28](https://youtu.be/wdf6cfH3rnA?t=508))
- "Kids are especially susceptible to this micro FOMO, as I'll call it." ([Cumin 2025-11 5:42](https://youtu.be/66n0P2NtBoQ?t=342))
- "When everything is rare, then nothing is. This game was basically only alive because of its economy." ([Cumin 2026-08 16:53](https://youtu.be/xtuuL-wRFho?t=1013))
- "You can't even get to the next room before the clown is already in chase mode." ([Cumin 2026-08 12:37](https://youtu.be/rjPW4GeeyFg?t=757))
- "There is no time to breathe in this game." ([Cumin 2026-08 14:58](https://youtu.be/rjPW4GeeyFg?t=898))
- "Under promise, and deliver." ([rasdev 2026-09 7:27](https://youtu.be/0_dR_081Hq8?t=447))
- "All, and I mean all LARP games require improvisation on the spot and context-dependent replies or commands." ([Roblox DevForum 2026-10 ](https://devforum.roblox.com/t/age-based-chat-restrictions-changes/4962382))

## Appendix: every extracted tip on this topic

- 2018-05-27 Game Maker's Toolkit [12:53](https://youtu.be/8X4fx-YncqA?t=773): Add a scoring system that rewards combos, variety and quick kills while penalising damage taken, so casual players can mash while skilled players chase grades.
- 2018-05-27 Game Maker's Toolkit [13:53](https://youtu.be/8X4fx-YncqA?t=833): Sell impact with animation: a big wind-up, a fast strike, a brief hold on contact (around 3 frames), then a heavy recovery, plus motion lines, screen blur, sparks, enemy hurt reactions and crunchy sound.
- 2020-05-09 Roblox DevForum [page](https://devforum.roblox.com/t/perspective-object-dragging-like-superliminal/566200): Tween a picked-up object toward screen centre with Vector3:Lerp(…, 0.2) per frame instead of teleporting it, for smoother feel.
- 2020-06-27 Roblox DevForum [page](https://devforum.roblox.com/t/creating-a-simple-realistic-camera-with-view-bobbing-dynamic-blur-sprinting/646943): Keep camera effects subtle; bobbing shouldn't be a 10-stud difference, as extreme motion can make players leave the game.
- 2020-06-27 Roblox DevForum [page](https://devforum.roblox.com/t/creating-a-simple-realistic-camera-with-view-bobbing-dynamic-blur-sprinting/646943): Camera bobbing is the hardest effect to tune; test with breaks, because over-attending to small bobbing makes it seem more noticeable.
- 2020-08-06 Roblox DevForum [page](https://devforum.roblox.com/t/map-design-and-scene-building-fantasy-medieval-and-nature-maps/709866): Animate ambient life (swaying trees, falling leaves, NPCs, birds, butterflies, day/night script) to bring a scene to life.
- 2020-08-27 Roblox DevForum [page](https://devforum.roblox.com/t/how-to-catch-combat-logging/743912): Keep punishment moderate: treat a leaver as having lost the fight, not harsher, since disconnects (crashes, net issues, misclicks) are common and harsh penalties drive players away.
- 2020-09-17 Emancyphur [5:42](https://youtu.be/C0ybJ5ghSHk?t=342): Balance the chaser with escape options (vents, doors, freeze tools, NPC help) so the game stays co-operative and not too hard for average players.
- 2020-09-17 Emancyphur [7:47](https://youtu.be/C0ybJ5ghSHk?t=467): Use custom music composed for the game to set tone in cutscenes and chapters.
- 2020-12-21 Roblox DevForum [page](https://devforum.roblox.com/t/understanding-easing-styles/937281): Use Exponential or Circular for fast-start, slow-stop motion; Linear feels mechanical. Quint/Quart start faster than Quad/Cubic for more snappy starts.
- 2021-03-03 Roblox DevForum [page](https://devforum.roblox.com/t/how-to-make-your-game-have-replayability/1082534): Let players feel they have a reason to return by showing upcoming content and unresolved mysteries.
- 2021-04-22 Roblox DevForum [page](https://devforum.roblox.com/t/camera-animations-for-cutscenes-and-gameplay/1181691): Camera animation can make attacks feel more powerful; use short camera moves on attacks and cinematic shots for cutscenes.
- 2021-05-04 Roblox DevForum [page](https://devforum.roblox.com/t/designing-an-fps-framework-beginner%E2%80%99s-guide-part-2/1203507): Use a spring module to shove recoil on each shot, then decay it back down, with random sideways offset and screen shake for feel.
- 2021-07-26 Roblox DevForum [page](https://devforum.roblox.com/t/weighted-chance-system/1373953): Higher chance values make a prize proportionally more likely to be rolled; weights are relative, so they need not sum to exactly 1.
- 2021-07-27 Roblox DevForum [page](https://devforum.roblox.com/t/making-accessible-games-for-the-disability-aware-era-a-not-fully-comprehensive-guide-by-an-actual-disabled-developer/1375919): Keep calm areas and quest/activity logs so overstimulated or distracted players can rest and recover track of objectives.
- 2021-12-09 Last Level Studios [36:48](https://youtu.be/v_TGu45AD_g?t=2208): Replace QTEs with a physical action in VR (shake hand to break free); players did it instinctively without being told.
- 2021-12-10 Roblox DevForum [page](https://devforum.roblox.com/t/how-to-make-a-terrifying-horror-game/1583917): Make players feel weak and vulnerable: limit movement speed, disorient them, darken the screen as fear rises, make combat risky.
- 2021-12-10 Roblox DevForum [page](https://devforum.roblox.com/t/how-to-make-a-terrifying-horror-game/1583917): Minimise player and NPC interactions to isolate the player, unless it damages the story.
- 2021-12-10 Roblox DevForum [page](https://devforum.roblox.com/t/how-to-make-a-terrifying-horror-game/1583917): Make characters relatable and likable so players feel bonded and care about their impact on the story.
- 2021-12-10 Roblox DevForum [page](https://devforum.roblox.com/t/how-to-make-a-terrifying-horror-game/1583917): Mix emotions beyond fear, such as sadness, by revealing the villain's backstory through clues.
- 2021-12-10 Roblox DevForum [page](https://devforum.roblox.com/t/how-to-make-a-terrifying-horror-game/1583917): Punish players for ignoring the environment (e.g., an unfed pet dies) to keep them attentive, as a subtle horror touch.
- 2021-12-10 Roblox DevForum [page](https://devforum.roblox.com/t/how-to-make-a-terrifying-horror-game/1583917): Avoid overly dark or poorly lit scenes; lamps should give sufficient light, or progression becomes painful rather than scary.
- 2021-12-10 Roblox DevForum [page](https://devforum.roblox.com/t/how-to-make-a-terrifying-horror-game/1583917): Create a false sense of safety before scares only when you know what you are doing; it can backfire.
- 2021-12-11 Roblox DevForum [page](https://devforum.roblox.com/t/a-guide-to-balance-the-pillars-of-balance/1585238): Decide deliberately whether high-skill actions should be rewarded more heavily. Rewards satisfy skilled play but can make consistent execution second nature and unbalanced.
- 2022-01-25 Roblox DevForum [page](https://devforum.roblox.com/t/why-your-anti-exploit-sucks/1643298): Keep anti-cheat unobtrusive; invasive checks that pester legit players hurt fun more than exploiters hurt the base game.
- 2022-04-25 Game Maker's Toolkit [10:34](https://youtu.be/Zrf1cou_yVo?t=634): Use drains to add risk: losing carried currency on death (Elden Ring) makes exploring new areas feel dangerous as holdings grow.
- 2022-05-28 B Ricey [1:05](https://youtu.be/T0xqkYODIl0?t=65): Use badges for achievements and milestones; they add replayability and give hunters something to collect beyond the core loop.
- 2022-11-24 GameMakers [25:03](https://youtu.be/NaR3-VIg5-I?t=1503): Any purchase that confers a gameplay advantage will be perceived as pay-to-win. Player perception matters more than intent.
- 2022-11-24 GameMakers [40:41](https://youtu.be/NaR3-VIg5-I?t=2441): Players who feel manipulated drop off. Transparent monetization tends to produce kinder participation and better retention.
- 2023-03-09 Roblox DevForum [page](https://devforum.roblox.com/t/guide-to-making-better-horror-experiences/2212571): Use environmental storytelling (notes, corpses, decals, enemy placement) to convey backstory without dialogue.
- 2023-03-09 Roblox DevForum [page](https://devforum.roblox.com/t/guide-to-making-better-horror-experiences/2212571): Build tension with buildup and release; give players recovery time, e.g. safe rooms.
- 2023-03-09 Roblox DevForum [page](https://devforum.roblox.com/t/guide-to-making-better-horror-experiences/2212571): Break your own established rules late in the game to create unease, since uncertainty scares more than known threats.
- 2023-03-09 Roblox DevForum [page](https://devforum.roblox.com/t/guide-to-making-better-horror-experiences/2212571): Use jumpscares sparingly; make them expected but not predictable, and avoid repeating the same jumpscare every time.
- 2023-05-07 1Coal [2:01](https://youtu.be/JzB8fpyofnw?t=121): Show a live player-progress tracker of other players on the server to add competition, as Tower of Hell does.
- 2023-08-25 1Coal [1:04](https://youtu.be/YBSsksqfxo0?t=64): Apply the 'Xbox test': would a kid's friends keep watching instead of scrolling TikTok? If not, the game doesn't look fun enough.
- 2023-11-26 Roox4 [5:44](https://youtu.be/kKiPL7wc8Rc?t=344): Tune difficulty by watching real deaths and session results, not only designer intent; escalate threats incrementally.
- 2024-03-08 GameMakers [13:48](https://youtu.be/zvNQHk1hUYc?t=828): Know your player's emotional state; Temple Run 2 pivoted to a calm themed map during COVID anxiety and players said they'd return just to see it.
- 2024-03-30 ByteBlox [8:52](https://youtu.be/lJ_ZwfNHkQU?t=532): Tune chaos by interval: he found a 5 second switch too slow and shortened it to 1 second for more tension.
- 2024-04-14 janisjanis01 [6:12](https://youtu.be/7z8XlhAtGpQ?t=372): Add sound effects to egg opening and pad unlocks; the game had almost no sound, which hurts game feel.
- 2024-06-07 ByteBlox [2:03](https://youtu.be/s2XUzTyCdK4?t=123): Illusions work if the player is never given reason to doubt them; consistency matters more than objective truth.
- 2024-06-23 janisjanis01 [10:35](https://youtu.be/e725ByFD8EI?t=635): Add a visible world-reaction hook, such as ships that sail away when you leave an area, to make areas memorable.
- 2024-07-25 Roox4 [9:40](https://youtu.be/OYfrdTxNdjA?t=580): Give a boss a telegraphed attack (lift leg, pause, stomp) so players can read and dodge it, with a vulnerability window.
- 2024-08-12 GameMakers [29:16](https://youtu.be/gp_hDijjC4U?t=1756): Gate currency behind time or progress so players feel earned spend (Club Penguin velvet-rope model, also used in battle passes).
- 2024-08-12 GameMakers [37:49](https://youtu.be/gp_hDijjC4U?t=2269): Expect distinct player types: achievers chasing rare items, self-expressers changing outfits often, speculators treating items as assets, and competitors showing status.
- 2024-09-24 ByteBlox [33:44](https://youtu.be/Issrodr_wK8?t=2024): Make feedback play only on first interaction (e.g. bounce once per part) so effects stay meaningful rather than repeating.
- 2024-09-24 ByteBlox [26:42](https://youtu.be/Issrodr_wK8?t=1602): Delay a visual state change slightly (about 0.1s) so it lands with the tween animation rather than before it.
- 2024-11-03 ByteBlox [14:30](https://youtu.be/4yIjd9Xn9sE?t=870): Tie a currency to a gameplay effect such as walk speed so holding money has a cost and encourages spending.
- 2024-11-03 ByteBlox [16:29](https://youtu.be/4yIjd9Xn9sE?t=989): Add a periodic percentage-based deduction (e.g. 10% per second) as inflation to keep money flowing; note Roblox rounds integers, so small balances may not decrease.
- 2024-11-17 janisjanis01 [15:09](https://youtu.be/vJekPDaIT30?t=909): Add confetti and a sound effect on shop purchases so buying feels more rewarding; cheap polish with little effort.
- 2024-12-01 janisjanis01 [2:31](https://youtu.be/Jc7yQTMFexk?t=151): Add door-slide animation, screen shake, smoke particles and a sound effect to area unlocks to make an unlock feel rewarding.
- 2025-01-05 ByteBlox [4:37](https://youtu.be/K-KvVwt_Y4I?t=277): Catch players off guard by cutting from a normal, upbeat state to a sudden change; unexpected shocks land harder than anticipated jump scares.
- 2025-01-10 PineappleDev [3:24](https://youtu.be/hHKQEohHqwU?t=204): When tuning unknown camera settings, bump one value to an extreme, play-test, and observe the effect before settling on a value.
- 2025-01-10 PineappleDev [4:07](https://youtu.be/hHKQEohHqwU?t=247): Camera smoothing around 16 is a good default; raise it for snappier camera, lower it for floaty, cinematic feel (useful for horror).
- 2025-01-10 PineappleDev [5:29](https://youtu.be/hHKQEohHqwU?t=329): Tilt the camera's Z-angle proportional to horizontal turn rate and clamp it, then smooth it back to upright each frame for an immersive lean.
- 2025-01-10 PineappleDev [8:14](https://youtu.be/hHKQEohHqwU?t=494): Drive FOV from normalized velocity (clamped to a max speed) and lerp it, so running widens the view and stopping zooms back in.
- 2025-01-10 PineappleDev [11:40](https://youtu.be/hHKQEohHqwU?t=700): Make the bob frequency and amplitude scale with walking state so walking bobs faster than idle, using a sine of tick() times speed.
- 2025-01-27 ByteBlox [8:43](https://youtu.be/RkgxOf3iZfA?t=523): Use a simple boost formula like 1 + level/10 so each level gives a clear, understandable bonus.
- 2025-01-27 ByteBlox [17:16](https://youtu.be/RkgxOf3iZfA?t=1036): Tune random probabilities (e.g. release/leash chances) during playtests so the pet-owner interaction feels fair and fun.
- 2025-02-01 ByteBlox [13:37](https://youtu.be/o-8V99horro?t=817): Use a pity counter that resets on a legendary drop to guarantee a top reward after N opens. Players trust visible pity systems.
- 2025-02-01 ByteBlox [22:15](https://youtu.be/o-8V99horro?t=1335): Adjust drop chances by outcome: lower legendary odds after rare hits, raise them after bad rolls. This is manipulative; use it deliberately and fairly if at all.
- 2025-02-01 ByteBlox [25:43](https://youtu.be/o-8V99horro?t=1543): Keep odds fair and transparent. The speaker says Brawl Stars is fair and simple, while one-in-a-billion pet odds are bad design.
- 2025-02-04 GameMakers [4:32](https://youtu.be/qZRNpN5M8jA?t=272): Higher rewards drove retention and stickiness. Raising difficulty drove revenue spikes but hurt retention if overused, so rotate it.
- 2025-02-07 Duckable [1:43](https://youtu.be/OS-k2iOEfhM?t=103): Design for multiple player types (Bartle: explorers, achievers, socializers) so the game appeals broadly.
- 2025-02-22 GnomeCode [10:45](https://youtu.be/-oZIdFe8qHk?t=645): Use ambient sound cues and light hints under doors to drive players forward; these add tension cheaply.
- 2025-02-22 GnomeCode [13:31](https://youtu.be/-oZIdFe8qHk?t=811): Balance challenge so it is hard but not impossible, with something always happening to keep players engaged.
- 2025-03-03 PineappleDev [1:21](https://youtu.be/2z4rebjBnQA?t=81): Add hover and click sounds to every button; use DescendantAdded so buttons created at runtime (e.g. inventory items) also get sounds.
- 2025-03-04 PineappleDev [4:47](https://youtu.be/IEAr0I_sUV4?t=287): Reward milestone completion with a cosmetic unlock (new fish/tray skin) plus a dedicated animated milestone screen to make progress feel special.
- 2025-03-15 Duckable [4:15](https://youtu.be/I9eyeEG6dpc?t=255): Competitive difficulty that provokes frustration can drive re-engagement; design wins to feel earned and losses to motivate another attempt.
- 2025-03-15 Duckable [7:19](https://youtu.be/I9eyeEG6dpc?t=439): Use loss aversion: show losses on profiles and win-streak resets so players fight for every casual match; limited items add urgency.
- 2025-03-21 PineappleDev [3:52](https://youtu.be/E6Bev4VCWeA?t=232): Adjust throw boost (velocity added on drop) to control throw distance; the speaker's example used 20 for a far throw.
- 2025-04-06 Cumin [10:36](https://youtu.be/YmAwFbqUA0U?t=636): Let players feed or upgrade companions and keep them relevant across zones; reviewer says Bee Swarm's bees feel more like companions than disposable Pet Simulator pets.
- 2025-04-06 Cumin [11:58](https://youtu.be/YmAwFbqUA0U?t=718): Pace reward delivery deliberately rather than flooding the screen with numbers and loot-box style openings; reviewer contrasts Bee Swarm's slower pacing favourably.
- 2025-05-02 Duckable [2:05](https://youtu.be/Wc8wjiy1oYk?t=125): Make failure states feel good: ragdoll/fling on hit gives the rage-fun reaction the speaker wanted, rather than a plain bonk.
- 2025-05-08 PineappleDev [6:14](https://youtu.be/Iz2ljOdZRJI?t=374): Pair the open/close transitions with a short UI sound to add juice to menu interactions.
- 2025-05-23 RoDev [11:32](https://youtu.be/Gw2FwndwnOg?t=692): Random size and rarity rolls create engagement, but too much variance can feel like pure gambling; tune the odds so good results still happen.
- 2025-05-24 Cumin [7:43](https://youtu.be/E7bedfC8A10?t=463): Early progression that forces long waits for seeds and crops made the creator lose interest fast; the novelty of the core activity wore off within minutes.
- 2025-05-29 CORSO [1:21](https://youtu.be/O2LZcQG5PPQ?t=81): Avoid power upgrades that split the player base into casual and tryhard tiers; balancing both sides becomes nearly impossible.
- 2025-06-07 AlvinBlox [3:21](https://youtu.be/Y93DRfB-Deo?t=201): Make every interaction give immediate feedback or reward (explosion, effect); don't gate fun behind grinding or pay-to-win.
- 2025-06-08 Cumin [12:34](https://youtu.be/Z1tj1OPOEZg?t=754): Don't rely on a 'it gets better later' promise; early movement must already feel good enough to keep players.
- 2025-06-28 Bemmy [1:08](https://youtu.be/-Z0C5YJtnqY?t=68): Free earn-once-every-30-minutes unit roll gives free-to-play players an outlet alongside paid gacha crates.
- 2025-07-15 PineappleDev [1:33](https://youtu.be/QRkRk-FHN4s?t=93): Apply luck boosts by multiplying the roll by a boost value below 1 (e.g. 0.1 gives 10x effective luck) so boosts stay compatible with weighted tables.
- 2025-07-25 ArTheDev [29:32](https://youtu.be/Pi8rQ9gGTKE?t=1772): Make perfect block a short window (about 0.1s) after pressing block, applying a stun to the attacker on success and a normal hit otherwise.
- 2025-07-27 JustDucksey [6:59](https://youtu.be/s5nooZlK5Pc?t=419): Make a scary enemy start as a harmless-looking version and transform at night; the transition animation adds tension.
- 2025-07-31 Cumin [4:57](https://youtu.be/jXogdTgtlXE?t=297): Keep respawn timers short (a few seconds in shooters, about a minute max in MOBAs); long waits make a game boring and cut learning time.
- 2025-10-09 JustDucksey [2:05](https://youtu.be/XZKHQPObHgw?t=125): Make enemy behaviour unpredictable (random wandering, then sudden attacks) so players stay tense rather than learning a pattern.
- 2025-12-23 Cumin [5:16](https://youtu.be/hQpC_UHxJDU?t=316): Telegraph enemy attacks visibly so players can dodge or parry. Unreadable boss attacks make combat feel unfair and unsatisfying.
- 2025-12-23 Cumin [10:36](https://youtu.be/hQpC_UHxJDU?t=636): Don't make death punishment exceed losing some gold. Losing half the gold per death plus a long walk back frustrates players.
- 2026-02-07 Cumin [6:44](https://youtu.be/ROo_Xpms4ok?t=404): Make higher difficulty add meaningful variation, not just higher enemy damage. Otherwise replaying it gives no engagement.
- 2026-03-00 RoWatcher (tracker blog) [page](https://rowatcher.com/news/top-10-roblox-games-by-players-march-2026-data-breakdown): Idle mechanics plus deep rod/lure-style progression and rare-catch trading are cited as drivers of retention in fishing games.
- 2026-04-27 rasdev [1:21](https://youtu.be/M-GCMK1Tryk?t=81): Randomize reward size, rarity and timing rather than giving the same reward every time, since predictable rewards lead to quitting.
- 2026-04-27 rasdev [2:42](https://youtu.be/M-GCMK1Tryk?t=162): Frame limited items and daily rewards as something players will lose if they don't return, not as something they gain.
- 2026-04-27 rasdev [3:23](https://youtu.be/M-GCMK1Tryk?t=203): Give players showable status items (rare or most expensive items) and mastery goals worth grinding for.
- 2026-04-30 rasdev [1:20](https://youtu.be/yFKY2FlwHjE?t=80): Use variable rewards (egg hatches, crate openings, rare drops) with unpredictable payout size so players keep playing for the next roll.
- 2026-04-30 rasdev [2:01](https://youtu.be/yFKY2FlwHjE?t=121): Use loss aversion: win streaks, leaderboard positions and login streak rewards. Frame returns around what players will lose if they stay away.
- 2026-05-00 StudioKrew (agency blog, GGAID data) [page](https://studiokrew.com/blog/top-roblox-games-may-2026/): Let players return without punishment for stepping away; a game that doesn't punish absence supports daily-active play.
- 2026-05-03 rasdev [5:35](https://youtu.be/q0lIbkUC2r8?t=335): Use variable rewards that differ each time a player completes something, which drives the same compulsion as slot machines.
- 2026-05-18 rasdev [6:32](https://youtu.be/N3L63uyLyQ8?t=392): Define a target audience (age range, motivations such as competition and visible progress) before designing the game.
- 2026-06-12 GosuGamers [page](https://www.gosugamers.net/entertainment/news/78614-grow-a-garden-2-has-launched-on-roblox-here-s-everything-new-added-in-this-sequel): Limited-time random pet spawns across the map create scarcity and urgency instead of a permanent egg shop.
- 2026-06-24 Cumin [16:53](https://youtu.be/2IdxQNOGoqA?t=1013): Make solo play viable or clearly unsupported. Advertising 3-4 players while solo is a slog frustrates players who can't find a party.
- 2026-07-16 Raul [1:05](https://youtu.be/CbAL1e8NgSU?t=65): Add satisfying sound effects and visual pop-ups to the first purchase action; game feel was a key reason the creator found the reference game fun.
- 2026-08-12 RoyalDev [2:45](https://youtu.be/LpqqLed1dBU?t=165): Add humor and a more human, reactive button character to make the interaction engaging while keeping it challenging but not impossible.
- 2026-08-22 Cumin [12:37](https://youtu.be/rjPW4GeeyFg?t=757): Give players time to react to threats. A trigger timer that ends in instant death within about 2 seconds feels unfair.
- 2026-08-22 Cumin [13:37](https://youtu.be/rjPW4GeeyFg?t=817): Give stalker enemies audio or visual cues and a persistent physical presence so players can read their position and react.
- 2026-08-30 janisjanis01 [8:05](https://youtu.be/pjN_aBDHAfY?t=485): Add rare-roll cutscenes for top rarities; they create dopamine spikes that RNG players expect.
- 2026-09-17 Roblox [49:05](https://youtu.be/HXZRH-2zurk?t=2945): Make hits feel responsive. Jujitsu Shenanigans connects instantly and ties visible world reaction to hits, drawing 160k players.
- 2026-09-18 revolver agz [29:43](https://youtu.be/j3L0K1yZjms?t=1783): Stackable title bonuses let new slots progress faster, encouraging repeat investment in progression.
- 2026-09-23 Lnor Roblox [2:56](https://youtu.be/gSFxStWqmgM?t=176): Show reward feedback on screen (money and currency gain animations) so players can see what they earned.
- 2026-09-23 Lnor Roblox [7:47](https://youtu.be/gSFxStWqmgM?t=467): Sell cosmetic trails for an in-game currency to create a status sink for progression currency.
- 2026-09-26 rasdev [7:27](https://youtu.be/0_dR_081Hq8?t=447): Under-promise and over-deliver: make sure gameplay matches or beats the promise shown in the icon and title.
- 2026-10-12 Roblox [26:18](https://youtu.be/KB5iAzy86Fo?t=1578): AI cannot judge whether design is fun; playtest yourself, change, and replay, since AI output is only a starting point.
- 2026-10-12 MonarchDev [6:09](https://youtu.be/QwdZRB6xRKk?t=369): Balance AI-generated enemies before release; generated wolves were far too strong in testing.
- 2026-10-20 rasdev [5:55](https://youtu.be/53OBGXktIPY?t=355): Use luck, rarity and timed events to keep players spinning; offer a cheap first purchase to get new players spending.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/education/build-it-play-it-island-of-move/animations-and-feedback): Give a visible reaction to every player action (e.g. hit, checkpoint, level-up) so players don't think the game is broken.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/add-rounds): Give distinct victory or defeat feedback (UI text plus audio) on round end so winners and losers each get clear, different outcomes.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/develop-a-moving-world): Gate visual/audio effects client-side by player location (indoors, game state) so hidden players don't get FX.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/input/mobile): Add haptic feedback (HapticEffect with types like GameplayCollision, GameplayExplosion, UIClick) to enhance feel beyond visuals and audio; supported on most modern iPhone, Pixel and Samsung Galaxy devices.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/audio/objects): To use speech-to-text without broadcasting voice, disable VoiceChatService.EnableDefaultVoice.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/chat/bubble-chat): Use per-bubble customization (OnBubbleAdded) for special effects tied to events, e.g. VIP styling or highlighting low health, to make chat more contextually meaningful.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/detect-hits): Apply damage with Humanoid:TakeDamage() rather than setting Health directly, so active ForceFields block damage.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/resources/beyond-the-dark/custom-characters): Use high-contrast focal points (glowing eyes and tentacle tips on a dark body) to direct player attention.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/education/lesson-plans/digital-citizenship/finishing-projects): Make the game challenging but fair: players should be challenged without being frustrated or punished.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/parts/materials): Create a custom MaterialVariant from a base material and set custom PhysicalProperties (e.g. extremely slippery Ice variant) to change gameplay behaviour globally.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/intermediate-scripting/create-a-health-pickup): Give pickups clear disabled feedback, e.g. raising transparency from 0.4 to 0.9 while on cooldown; dimming the PointLight brightness adds impact on collection.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/education/build-it-play-it-mansion-of-wonder/using-particles-for-actions): Give feedback through multiple forms (visual, sound) since players with sound off or hearing impairment rely on visual cues, and low-vision players rely on audio.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/in-game-sounds): Play a short chime on collectable touch as feedback so pickups feel rewarding.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/scripting/security/device-trust): Avoid hard rejection. Only reject at None as a last resort, and prefer routing or feature gating. Rejection also hits legitimate players on old or unfixable devices.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/scripting/security/device-trust): Write a custom rejection message that points players to a mode they can still play. Otherwise Roblox shows a generic default message.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/projects/assets/packages): Add scripts that read package attributes at runtime to implement configurations; attribute values set per copy survive updates, other attributes take new defaults.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/education/build-it-play-it-island-of-move/animating-parts): Use Exponential easing for pickups shrinking on touch and Quad for button presses to make motion feel distinct.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/education/edu-templates/edu-lesson-plan-template): Design challenge so players are challenged but not frustrated or punished.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/education/build-it-play-it-mansion-of-wonder/experienced-landing-page): Play a particle effect when a player completes a task to reward the action and mark progress.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/resources/modules/photo-booth): Use countdownSeconds, countdownBeepSound and countdownFlashSound to tune the photo ritual's pacing and feedback.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/resources/modules/surface-art): Let players leave a visible mark on the world; the docs note players enjoy feeling part of constructing the space. Default quota is 2 pieces per player.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/education/developer/planning-for-educational-settings): Give positive reinforcement on goal completion, e.g. a burst of particle effects or playful object interaction; give specific improvement feedback when students struggle.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-2D-audio): Choose opening music to set the intended mood immediately on join; swapping an upbeat track for a metal track changes the experience.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-2D-audio): Prioritise important feedback with louder volume: the sample raised gumdrop-collect sound to Volume 3 versus lower volume for jump sounds.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-2D-audio): Give immediate one-shot audio feedback on objectives (score, health, level progress) so players understand the result of actions without relying on visuals alone.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/projects/server-authority/techniques): Only smooth position when the simulated object jumps far from the rendered one, as Soccer does, so normal play has no visual latency.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/environment/post-processing-effects): Use ColorCorrectionEffect TintColor to give feedback, e.g. tint screen red when health is low.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/education/lesson-plans/roblox-developer/roblox-developer-5): Challenge should not frustrate or punish players; aim for challenging but fair design.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/resources/modules/scavenger-hunt): Reward allCollected once per player with a badge, new area access, or currency; the event fires only once per player.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-hud-meters): Tween HUD bar size and color (about 0.5s, Exponential Out) rather than snapping, and replace the default red screen-edge damage tint with a ColorCorrectionEffect if wanted.
- 2026-11-01 Roblox public API [page](https://www.roblox.com/games/95168737547508/): Use pets as speed multipliers (riding pets makes you faster) so collection directly feeds the core loop.

Index: [[README]] | Master: [[master-playbook]]
