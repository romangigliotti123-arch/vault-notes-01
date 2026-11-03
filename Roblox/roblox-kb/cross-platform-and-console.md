---
title: Cross Platform And Console
topic: cross-platform-and-console
theme: Studio & Scripting
sources: 66 videos
creators: [Business of Creators, Deconstructor of Fun, Emancyphur, GamesBeat, GuideRealm, Last Level Studios, RoWatcher (tracker blog), Roblox, Roblox Creator Docs, Roblox DevForum, Roblox Investor Relations, Roblox Newsroom, Roblox public API, StudioKrew (agency blog, GGAID data), Suphi Kaner, VuukStudios, rasdev]
source_dates: 2019-10-11 to 2026-11-01
tags: [roblox, knowledge-base, cross-platform-and-console]
---

# Cross Platform And Console

_console, VR, mobile and cross-platform support, input handling, platform-specific design._

Evidence base: 132 extracted items from 66 videos by Business of Creators, Deconstructor of Fun, Emancyphur, GamesBeat, GuideRealm, Last Level Studios, RoWatcher (tracker blog), Roblox, Roblox Creator Docs, Roblox DevForum, Roblox Investor Relations, Roblox Newsroom, Roblox public API, StudioKrew (agency blog, GGAID data), Suphi Kaner, VuukStudios, rasdev (2019-10-11 to 2026-11-01). Roblox changes quickly: check the date on each source and see Date context below.

## Overview
Cross-platform Roblox work now centres on one codebase reaching PC, mobile, tablet and console, with cross-play needing no extra work (official, Sept 2026). Web Play adds a no-install entry point through the Experience Details Page or a direct link, Chrome first. Mobile-first design remains the consensus, and indie sources urge testing on low-end Android before launch. The newest official guidance (Nov 2026) favours supporting all platforms from launch, which supersedes staged rollouts. Verify capacity and per-platform input and UI as before. Existing input, VR, TV and console rules still apply; this update adds access and launch-scope guidance.

## Rules and findings
- **Treat touch as a first-class input** (multiple-creators): Rasdev and GuideRealm both say mobile and tablet must work because many players use phones (rasdev's player-share claim is self-reported and unverified). Check that buttons are easy to tap, UI is readable and performance is smooth on phones. Roblox official calls console and mobile optimization recommended, not required, so treat it as a strong default. Phones and tablets can always tap a prompt regardless of ClickablePrompt. Sources: [rasdev 2026-09 3:24](https://youtu.be/Df5ebFGEOXY?t=204), [GuideRealm 2026-10 7:38](https://youtu.be/ltbZzXRrDF8?t=458), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/creator-programs/standout-games), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/ui/proximity-prompts). Newest source 2026-10-28.
- **Test UI across device sizes before publishing** (one-creator-repeated): Use Studio Device Simulator to check a range of screen sizes and form factors so UI looks right everywhere. Custom device limits: width 1-7680 px, height 1-4320 px, pixel density 72-10,000 PPI (density drives physical-size scaling). On-screen keyboard coverage is 0-4320 px height per orientation. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/testing-modes), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/device-simulator), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/device-simulator), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/device-simulator). Newest source 2026-10-28.
- **Detect input type with PreferredInput and adapt UI** (one-creator-repeated): Read UserInputService.PreferredInput to adapt on-screen buttons and menus. Do not assume keyboard means desktop: a connected gamepad on PC can become the primary input. If PreferredInput is not sufficient, listen to GamepadConnected/GamepadDisconnected or check GamepadEnabled. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/input/gamepad), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/input/mouse-and-keyboard), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/input/gamepad). Newest source 2026-10-28.
- **Verify UI when input type changes mid-session** (one-creator-repeated): Test that UI updates when a player connects a Bluetooth controller or switches a trackpad to mouse during play. Do not assume the input type is fixed at join (inference from the guidance to verify mid-session switching). Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/performance-optimization/test-on-hardware), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/input/gamepad). Newest source 2026-10-28.
- **Bind gameplay actions with the Input Action System** (one-creator-repeated): Define actions such as jump, sprint and shoot as Input Action System actions, and bind multiple hardware inputs to each. Do not hardcode individual keys. This keeps one action working across keyboard, gamepad, touch and TV remote inputs. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/input/gamepad), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/input/mouse-and-keyboard). Newest source 2026-10-28.
- **Map every control per input type up front** (single-mention): Map all controls for keyboard/mouse, mobile and controller before building. A battle-royale sample project defines a separate mapping for each input type. Low-advice video; treat as a planning pattern rather than a requirement. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/resources/battle-royale/run-the-game). Newest source 2026-10-28.
- **Follow standard gamepad conventions** (single-mention): ButtonA for confirm/jump; ButtonB for cancel/dodge/sprint; Thumbstick1 for movement; Thumbstick2 for camera; R2/L2 for primary actions such as shooting. Players expect these mappings on controllers. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/input/gamepad). Newest source 2026-10-28.
- **Show the correct glyph per device** (single-mention): Set KeyboardKeyCode and GamepadKeyCode on prompts. Roblox shows the correct input glyph for each device type, so you do not need separate prompt art per platform. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/ui/proximity-prompts). Newest source 2026-10-28.
- **Hide default touch controls only when replacing them** (single-mention): Set GuiService.TouchControlsEnabled to false in a client script to hide the default virtual thumbstick and jump button on touch devices. Only do this if you supply your own touch controls, or touch players lose movement. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/ui/on-screen-containers). Newest source 2026-10-28.
- **Use Delta for mouse-locked input** (single-mention): While the mouse is locked, its position no longer changes. Read InputChanged with UserInputType MouseMovement and use the Delta property for movement or camera. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/input/mouse-and-keyboard). Newest source 2026-10-28.
- **Choose the camera type to fit gameplay** (single-mention): Detect user input to trigger actions and choose a camera type (first-person, side-scrolling or isometric) that suits the gameplay. Low-advice video. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/tutorials). Newest source 2026-10-28.
- **Override Roblox default controls sparingly** (single-mention): Only override default controls (movement, camera, reserved keys) in specific cases. Players already know the defaults, and overriding them can confuse them. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/input/input-action-system). Newest source 2026-10-28.
- **Pick drag style per input with BestForDevice** (single-mention): BestForDevice gives TranslatePlaneOrLine for mouse and gamepad, TranslatePlane for touch, and 6DOF for VR. Low-advice video; use it to get appropriate drag behaviour per device. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/ui/3D-drag-detectors). Newest source 2026-10-28.
- **Do not rely on grass motion for critical cues** (single-mention): Animated grass speed is reduced when players enable Reduce Motion. Do not rely on grass motion alone for gameplay-critical information; pair it with another cue. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/parts/terrain). Newest source 2026-10-28.
- **Design Android TV experiences for the D-pad** (one-creator-repeated): The Android TV pilot favours straightforward controls that adapt to a D-pad: 2D games, simple movement and menu-driven mechanics. Plan input mapping and UI optimization for D-pad navigation. Roblox offers hands-on technical help in the pilot. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/creator-programs/android-tv-pilot), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/creator-programs/android-tv-pilot). Newest source 2026-10-28.
- **Test TV remote input with simulation and hardware** (one-creator-repeated): Use TV Remote simulation in Studio plus hardware testing to validate input mapping before publishing. Test with a physical remote when possible. Without one, use the Studio Device Emulator Android TV viewport (1920x1080) with the Controller Emulator TV Remote. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/creator-programs/android-tv-pilot), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/input/micro-gamepad), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/input/micro-gamepad). Newest source 2026-10-28.
- **Detect TV remotes by micro-gamepad signature, not keycodes** (one-creator-repeated): Detect a micro gamepad by checking Gamepad1 is connected and supports neither Thumbstick1 nor Thumbstick2. Do not identify TV remotes by legacy keycodes alone, because full gamepads send the same codes; check ButtonCenter support on Gamepad1 too. Micro gamepads use slots Gamepad1-Gamepad8. Enum.PreferredInput.MicroGamepad is not yet set. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/input/micro-gamepad), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/input/micro-gamepad), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/input/micro-gamepad). Newest source 2026-10-28.
- **Map legacy TV remote keycodes to gamepad buttons** (single-mention): Bind TV remote buttons via legacy codes: ButtonCenter maps to ButtonA, ButtonBack maps to ButtonB, and D-pad keys map to DPad directions. This is the legacy route; for new work prefer the Input Action System. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/input/micro-gamepad), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/input/gamepad). Newest source 2026-10-28.
- **Separate navigation and gameplay input contexts** (single-mention): Use separate input contexts for navigation and gameplay, so one legacy button does not fire both actions at once (for example a remote's center button selecting a menu item and jumping). Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/input/micro-gamepad). Newest source 2026-10-28.
- **Check Enum.GamepadType branches against emulation** (single-mention): Check code that branches on Enum.GamepadType. The experience sees the emulated controller type as it would with the real device, so emulator tests exercise the same branches. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/controller-emulator), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/device-simulator). Newest source 2026-10-28.
- **Emulate hardware with Device Simulator and Controller Emulator** (one-creator-repeated): Use Device Simulator with Controller Emulator to preview touch, screen size, DPI, and gamepad, VR and TV remote input without owning the device. Use real hardware when possible. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/device-simulator), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/testing-modes), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/input/micro-gamepad). Newest source 2026-10-28.
- **Validate touch with emulator shortcuts** (single-mention): Use Alt+drag for pinch/rotate and Alt+Shift+drag for two-finger pan in Studio to validate that touch inputs land correctly before testing on a phone. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/device-simulator). Newest source 2026-10-28.
- **Use multi-input devices for combined touch and gamepad testing** (single-mention): Handheld gamepads with touchscreens and phones with USB-C gamepad adapters let you test touch and gamepad on one device. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/performance-optimization/test-on-hardware). Newest source 2026-10-28.
- **Configure OpenXR before launching Studio for VR** (one-creator-repeated): For VR testing on Windows, configure the OpenXR runtime before launching Studio. With multiple headsets, configure only the one you want to test with. Oculus VR needs at least an NVIDIA GeForce GTX 1060 or equivalent GPU. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/testing-modes), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/testing-modes). Newest source 2026-10-28.
- **Test VR interactions one hand at a time** (one-creator-repeated): Disable the headset and one controller to test each hand separately. Check reach, grab volumes, and whether interactions depend on gaze. Use Reset Positions during a playtest to recover from a VR pose you cannot recover by hand. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/controller-emulator), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/controller-emulator). Newest source 2026-10-28.
- **Tune VR and camera sensitivity constants** (single-mention): VR translation sensitivity ranges 1-10 and scales how far enabled VR parts travel per keypress. Camera rotation example: 1.5 radians per second at full input, set via a CAMERA_SENSITIVITY constant in the OnInput example. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/controller-emulator), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/input/input-action-system). Newest source 2026-10-28.
- **Keep depth-of-field at graphics quality 8 or higher on non-mobile** (single-mention): Depth-of-field requires graphics quality 8 or higher on non-mobile devices. Below this, players are prompted to raise graphics quality, so do not enable it unconditionally on low-end setups. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/resources/modules/selfie-mode). Newest source 2026-10-28.
- **Plan the Android TV pilot as a time-limited program** (one-creator-repeated): The Android TV pilot runs 90 days with a cohort of 25 creators. About 88% of Android TV users play exclusively with a TV remote, so remote-first design matters for that audience. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/creator-programs/android-tv-pilot), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/creator-programs/android-tv-pilot), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/creator-programs/android-tv-pilot). Newest source 2026-10-28.
- **Fix silent Toolbox audio on Windows** (single-mention): If Toolbox audio is silent on Windows, open Volume Mixer and make sure Microsoft Edge WebView2 is not muted. Low-advice video; a Studio troubleshooting step rather than a cross-platform design rule. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/projects/assets/toolbox). Newest source 2026-10-28.
- **Use non-R15 layered accessories guidance for custom characters** (single-mention): Custom non-Marketplace characters that use a unique cage or UV solution need the separate non-R15 layered accessories guidance. This is outside core platform input but affects custom-character cross-platform work. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/art/modeling/cage-meshes/apply-deformation). Newest source 2026-10-28.
- **Set a Scriptable camera with a reset CFrame for VR** (single-mention): Set Camera.CameraType to Scriptable and reset the camera CFrame to its position to avoid a wrongly angled VR view. Single indie source from 2021; verify against current VR docs. Sources: [Roblox DevForum 2021-05](https://devforum.roblox.com/t/creating-simple-vr-hands-from-scratch/1227966). Newest source 2021-05-15.
- **Disable default VR controller visuals before custom hands** (single-mention): Before replacing controllers with custom hand models, call SetCore VREnableControllerModels false and set VRLaserPointerMode to 0 so default models and the laser pointer do not conflict. Sources: [Roblox DevForum 2021-05](https://devforum.roblox.com/t/creating-simple-vr-hands-from-scratch/1227966). Newest source 2021-05-15.
- **Drive custom VR hands from UserCFrameChanged** (single-mention): Update hand positions in UserInputService.UserCFrameChanged, which fires before render, to avoid visible lag between controller and hand models. Multiply the move by camera.CFrame. Sources: [Roblox DevForum 2021-05](https://devforum.roblox.com/t/creating-simple-vr-hands-from-scratch/1227966). Newest source 2021-05-15.
- **Anchor HumanoidRootPart in VR** (single-mention): Anchor the HumanoidRootPart so the default character does not move or show while the player is in VR. Sources: [Roblox DevForum 2021-05](https://devforum.roblox.com/t/creating-simple-vr-hands-from-scratch/1227966). Newest source 2021-05-15.
- **Start VR from default player scripts before custom code** (single-mention): Official guidance says existing experiences using default player scripts usually run well in VR with little or no modification. Confirm this works before writing custom VR control code. Sources: [Roblox DevForum 2023-07](https://devforum.roblox.com/t/roblox-is-coming-to-meta-quest/2465291). Newest source 2023-07-12.
- **Set device availability per experience before publishing** (multiple-creators): Control VR, Desktop, Mobile, Tablet and Console availability on the Access page or in Studio Game Settings, and enable every target device in the Devices section at publish time. Keep the VR checkbox on to stay available on PC VR. Sources: [Roblox DevForum 2023-07](https://devforum.roblox.com/t/roblox-is-coming-to-meta-quest/2465291), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/tutorials/first-experience), [Roblox DevForum 2023-07](https://devforum.roblox.com/t/roblox-is-coming-to-meta-quest/2465291). Newest source 2026-10-28.
- **Isolate mobile controls in their own ScreenGui** (single-mention): Build mobile controls in a separate ScreenGui named 'Mobile Controls' in StarterGui, and enable it only when UserInputService.TouchEnabled is true. Sources: [VuukStudios 2023-09 0:37](https://youtu.be/dcJtZnan7i8?t=37). Newest source 2023-09-24.
- **Design mobile-first, then verify every supported platform** (multiple-creators): Most Roblox sessions are on mobile, so consider orientation and touch from the start. Then test PC and console too, since players switch devices and optimizing for one platform neglects others. Sources: [VuukStudios 2024-08 5:02](https://youtu.be/3J7Vp6NgYf4?t=302), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/input/mobile), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/ui/position-and-size), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/resources/battle-royale), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/input/mobile). Newest source 2026-10-28.
- **Read SteerFloat and ThrottleFloat for analog vehicle input** (single-mention): Read SteerFloat and ThrottleFloat rather than raw keys. They give finer control for mobile D-pad and gamepad input in driving experiences. Sources: [Suphi Kaner 2022-04 31:24](https://youtu.be/FVOowr2DXbM?t=1884). Newest source 2022-04-14.
- **Handle orientation changes at runtime** (one-creator-repeated): Change orientation via PlayerGui.ScreenOrientation and listen to PlayerGui:GetPropertyChangedSignal('ScreenOrientation'). Set emoteBarPosLandscape and emoteBarPosPortrait separately. Five orientation modes exist, two sensor-based and three locked. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/input/mobile), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/resources/modules/emote-bar), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/input/mobile). Newest source 2026-10-28.
- **Gate gestures and motion sensors on device support** (one-creator-repeated): Use TouchSwipe and TouchPinch, and accelerometer or gyroscope input, only where supported. Check AccelerometerEnabled and GyroscopeEnabled first. Mobile players can tilt to move, while desktop players click a button, so plan controls for both. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/input/mobile), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/education/build-it-play-it-island-of-move/save-and-publish), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/projects/cross-platform). Newest source 2026-10-28.
- **Test visuals at lowest and highest Editor Quality Level** (single-mention): Trail visual quality follows player graphics settings. Set Studio Editor Quality Level to both lowest and highest before finishing to catch visual differences. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/effects/trails). Newest source 2026-10-28.
- **Keep max players at 100 or fewer for Voice Chat** (one-creator-repeated): Voice Chat is only available in places with a maximum of 100 players. After lowering max players below 100, restart servers, because existing higher-capacity servers will not support Voice Chat. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/chat/voice-chat), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/chat/voice-chat), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/chat/voice-chat). Newest source 2026-10-28.
- **Plan fallback experiences for console and VR on the age check** (single-mention): Console and VR do not currently support the age check flow. Provide a fallback experience for those players rather than blocking them. Sources: [Roblox DevForum 2026-04](https://devforum.roblox.com/t/introducing-the-us-18-devex-rate-earn-42-more-on-spend-from-18-us-players/4607091). Newest source 2026-04-30.
- **Plan for client update lag on mobile and console** (single-mention): Mobile and console clients lag desktop updates by a few days and cannot connect until their client update lands. Avoid breaking server changes at release time on those platforms. Sources: [Roblox DevForum 2026-07](https://devforum.roblox.com/t/full-release-ship-fair-and-competitive-games-with-server-authority/4727993). Newest source 2026-07-09.
- **Do not hardcode default PC keybinds while bindings are in beta** (single-mention): Default bindings as of 2026-02: Strafe is Left Alt on PC and Left Option on Mac, Crouch is C, Sprint is Left Shift. Input bindings are still in beta and may change, so read bindings rather than assuming these keys. Sources: [Roblox DevForum 2026-02](https://devforum.roblox.com/t/studio-beta-avatarabilities-library-for-a-luau-based-character-controller/4403904). Newest source 2026-02-18.
- **Share the Details Page URL for web-start access when available** (single-mention): Players can start on web in Chrome with no install (announced for late 2026). Share the game's Details Page URL on YouTube, X or Discord to drive that start path. Sources: [Roblox DevForum 2026-09](https://devforum.roblox.com/t/rdc26-what-we-announced/4865880). Newest source 2026-09-11.
- **Use Activated-style button events, not mouse-only events** (multiple-creators): Wire GUI buttons to the generic Activated/MouseButton1Click-style event so mouse, touch and controller players can all trigger them. Prefer generic input activation over many keyboard- or mouse-specific actions, which eases porting to other platforms. Sources: [Emancyphur 2020-08 12:12](https://youtu.be/LjETISdUBp8?t=732), [Last Level Studios 2019-10 10:46](https://youtu.be/vY0om5O-Oh8?t=646). Newest source 2020-08-19.
- **Consider Xbox or mobile support around 10 concurrent players** (single-mention): Indie heuristic (self-reported): once a game reaches about 10 concurrent players, adding Xbox or mobile support is worth considering, since those audiences can be larger than PC. Example cited: a sniping game with about 80 PC players versus 4,800 console players. Sources: [Last Level Studios 2019-10 6:43](https://youtu.be/vY0om5O-Oh8?t=403), [Last Level Studios 2019-10 6:43](https://youtu.be/vY0om5O-Oh8?t=403), [Last Level Studios 2019-10 6:43](https://youtu.be/vY0om5O-Oh8?t=403). Newest source 2019-10-11.
- **Size VR investment against a small headset audience** (single-mention): Self-reported 2021 figure: VR was about 2-3% of the Steam hardware survey, so best case about 2% of the Roblox PC market. Treat VR as a niche platform and justify the build cost against that share before investing heavily. Sources: [Last Level Studios 2021-12 8:52](https://youtu.be/v_TGu45AD_g?t=532). Newest source 2021-12-09.
- **Use Web Play as a no-install entry point** (multiple-creators): Roblox Web Play (Chrome first, Sept 2026) lets players join via direct link or the Experience Details Page without installing. Make sure the entry flow and key UI work in the Chrome web player, and share the Details Page URL as the access point. Sources: [GamesBeat 2026-09](https://gamesbeat.com/roblox-hits-20-and-opens-rdc-2026-to-invite-the-world-to-play-and-make-games-dave-baszucki-keynote/), [Roblox Investor Relations 2026-09](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026068235/ex991-q32026earningsshar.htm). Newest source 2026-09-30.
- **Ship one codebase for cross-play** (single-mention): Roblox states the same codebase gives cross-play with no extra work. Do not fork separate console or mobile builds for cross-play; gate platform differences through input type detection and UI adaptation instead. Sources: [Roblox Investor Relations 2026-09](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026068235/ex991-q32026earningsshar.htm). Newest source 2026-09-30.
- **Test on a low-end Android phone before launch** (single-mention): StudioKrew reports that every top-10 game runs well on a budget phone and recommends testing on low-end Android before launch. Check frame rate, UI legibility and load time on a budget device, not just flagship hardware. Sources: [StudioKrew (agency blog, GGAID data) 2026-05](https://studiokrew.com/blog/top-roblox-games-may-2026/). Newest source 2026-05-00.
- **Plan PC, mobile, tablet and console support at launch** (single-mention): Official guidance (Nov 2026) recommends supporting PC, mobile, tablet and console from launch to widen the audience. Plan the per-platform input map and UI from the start, and verify each platform before release. Sources: [Roblox public API 2026-11](https://www.roblox.com/games/95168737547508/). Newest source 2026-11-01.
- **Treat cross-platform as a retention tool, not a revenue play** (single-mention): Per one indie developer (self-reported, low advice weight), cross-platform play is valued for keeping players engaged across devices rather than for extra revenue. The same source recommends shipping a pure-play build for mobile, or for PC/console, instead of one game spanning both. This conflicts with the existing 'Ship one codebase for cross-play' rule; weigh it against your audience data. Sources: [Deconstructor of Fun 2026-10 15:36](https://youtu.be/oU3oz6Ddz7g?t=936). Newest source 2026-10-22.
- **Use mobile ads to drive cross-platform installs** (single-mention): One indie developer (self-reported) used mobile ads to bring players into a cross-platform experience and reports that most of their users play on both mobile and PC. Treat the claim as anecdotal; verify with your own install and retention analytics before copying the approach. Sources: [Deconstructor of Fun 2026-10 21:12](https://youtu.be/NW4EShVGPYs?t=1272). Newest source 2026-10-26.

## Checklist
- [ ] Decide the target platforms up front: PC, mobile/tablet, console/gamepad, VR, Android TV.
- [ ] Make touch controls usable: buttons easy to tap, UI readable, performance smooth on a phone.
- [ ] Make every prompt tappable on touch regardless of ClickablePrompt.
- [ ] Run Device Simulator across screen sizes, custom dimensions and pixel density before publishing.
- [ ] Set KeyboardKeyCode and GamepadKeyCode on prompts so the correct glyph shows per device.
- [ ] Read UserInputService.PreferredInput to adapt on-screen buttons and menus.
- [ ] Add a GamepadConnected/GamepadDisconnected or GamepadEnabled fallback if PreferredInput is not enough.
- [ ] Bind jump, sprint, shoot and similar actions through the Input Action System with multiple bindings each.
- [ ] Apply gamepad conventions: ButtonA confirm/jump, ButtonB cancel/dodge/sprint, Thumbstick1 move, Thumbstick2 camera, R2/L2 primary action.
- [ ] Test UI when the player switches input mid-session (Bluetooth controller connect, trackpad to mouse).
- [ ] Use Controller Emulator (with Device Simulator) to test gamepad, VR and TV remote input without hardware, and check Enum.GamepadType branches against the emulated type.
- [ ] Validate touch with Alt+drag (pinch/rotate) and Alt+Shift+drag (two-finger pan).
- [ ] Set GuiService.TouchControlsEnabled to false only when you supply your own touch controls.
- [ ] Use Delta from InputChanged (MouseMovement) for mouse-locked movement.
- [ ] Choose the camera type (first-person, side-scrolling, isometric) to suit the gameplay.
- [ ] Override default controls (movement, camera, reserved keys) only when there is a specific reason.
- [ ] Do not make grass motion the only cue for gameplay-critical information.
- [ ] Android TV: design D-pad-friendly controls (2D, simple movement, menu-driven).
- [ ] Android TV: detect micro gamepads via Gamepad1 with no Thumbstick1/2, and check ButtonCenter, not keycodes alone.
- [ ] Android TV: map ButtonCenter to ButtonA, ButtonBack to ButtonB, D-pad keys to DPad directions; separate navigation and gameplay input contexts.
- [ ] Test TV remote on hardware when possible; otherwise use Android TV emulator at 1920x1080 with Controller Emulator TV Remote.
- [ ] VR: configure OpenXR before launching Studio; configure only the headset under test.
- [ ] VR: test each hand separately (disable headset and one controller); use Reset Positions when stuck.
- [ ] Use BestForDevice drag style: TranslatePlaneOrLine (mouse/gamepad), TranslatePlane (touch), 6DOF (VR).
- [ ] Keep depth-of-field at graphics quality 8 or higher on non-mobile; check VR translation sensitivity (1-10) and camera sensitivity when tuning movement.
- [ ] Choose camera configuration and supported input types (mouse, mobile, gamepad) early, since they affect accessibility and engagement.
- [ ] Enable every target device (phones, computers, tablets, consoles, VR) in the Devices section at publish time.
- [ ] Check the Access page or Studio Game Settings to confirm VR, Desktop, Mobile, Tablet and Console availability.
- [ ] Keep the VR checkbox enabled if you want PC VR availability.
- [ ] For VR, test default player scripts first before adding custom control code.
- [ ] For custom VR hands, disable controller models and laser pointer, then drive hands from UserCFrameChanged.
- [ ] Anchor HumanoidRootPart in VR experiences that should not show the default character.
- [ ] Put mobile controls in a 'Mobile Controls' ScreenGui and enable it only when TouchEnabled is true.
- [ ] Check AccelerometerEnabled and GyroscopeEnabled before using motion or gyro input.
- [ ] Check TouchSwipe and TouchPinch support before relying on gestures.
- [ ] Set emoteBarPosLandscape and emoteBarPosPortrait separately.
- [ ] Test visuals with Editor Quality Level set to both lowest and highest.
- [ ] Keep max players at 100 or fewer if you need Voice Chat, and restart servers after lowering the limit.
- [ ] Plan a fallback experience for console and VR players on the age check flow.
- [ ] Plan a release buffer for mobile and console client update lag.
- [ ] Replace mouse-only click handlers on GUI buttons with Activated-style events.
- [ ] Before a porting push, check your own concurrency and platform analytics rather than relying on the ~10-player heuristic.
- [ ] Confirm your experience's current platform split in analytics instead of using the 2021 ~70% mobile / ~30% PC+Xbox figure.
- [ ] Estimate VR audience size before committing VR-specific build time.
- [ ] Verify headset refresh rates in current device specs before tuning VR performance.
- [ ] Confirm the experience loads and plays through Web Play in Chrome via a direct link or Details Page URL.
- [ ] Check that the entry flow, onboarding and key menus work in the Chrome web player.
- [ ] Test the experience on at least one low-end Android phone before launch.
- [ ] Confirm cross-play works with the shared codebase; do not fork separate builds without a reason.
- [ ] Decide the launch platform list (PC, mobile, tablet, console) up front and map inputs for each.
- [ ] Verify UI and input per platform before publishing, not only on the primary platform.
- [ ] Before choosing between one cross-platform build and separate pure-play builds, check your own analytics for how many players use multiple devices.
- [ ] If you run mobile ads to drive cross-platform installs, track installs and retention per platform to confirm the effect.

## Numbers and benchmarks

| Metric | Value | Context | Sources |
|---|---|---|---|
| Android TV users who play exclusively with a TV remote | ~88% | Official Roblox Creator Docs; drives remote-first design for Android TV. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/creator-programs/android-tv-pilot) |
| Android TV pilot duration | 90 days | Official; the pilot is time-limited, so Android TV specifics may change after it ends. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/creator-programs/android-tv-pilot) |
| Android TV pilot cohort size | 25 creators | Official; pilot participants receive Roblox technical help. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/creator-programs/android-tv-pilot) |
| Custom device screen width (Device Simulator) | 1 to 7680 px | Upper bound for custom device dimensions in Device Simulator. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/device-simulator) |
| Custom device screen height (Device Simulator) | 1 to 4320 px | Upper bound for custom device dimensions in Device Simulator. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/device-simulator) |
| Custom device pixel density | 72 to 10,000 PPI | Drives physical-size scaling in the simulator. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/device-simulator) |
| On-screen keyboard height coverage | 0 to 4320 px per orientation | Portrait and landscape keyboard coverage for layout testing. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/device-simulator) |
| Graphics quality required for depth-of-field | 8 or higher on non-mobile | Below this, players are prompted to increase graphics quality. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/resources/modules/selfie-mode) |
| Android TV emulator viewport | 1920x1080 | Studio Device Emulator viewport when Android TV is selected. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/input/micro-gamepad) |
| Micro gamepad input slots | Gamepad1-Gamepad8 | Slots used by micro gamepads such as TV remotes. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/input/micro-gamepad) |
| Minimum GPU for Oculus VR | NVIDIA GeForce GTX 1060 or equivalent | Oculus drivers requirement, per official docs. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/testing-modes) |
| VR translation sensitivity range | 1 to 10 | Scales how far enabled VR parts travel per keypress. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/controller-emulator) |
| Camera rotation sensitivity example | 1.5 radians per second at full input | CAMERA_SENSITIVITY constant in the OnInput example script. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/input/input-action-system) |
| VR player count (unverified) | about 17 (unit unclear) | Rasdev, self-reported, 2026-06 (older). Wording says '17 people', likely meant as millions; treat as unverified and possibly stale. | [rasdev 2026-06 4:54](https://youtu.be/8lWfkv6dmpo?t=294) |
| Daily joins across Roblox | 66 million users join Roblox every day | Roblox-wide across mobile, desktop and Xbox; source dated 2023-07. | [Roblox DevForum 2023-07](https://devforum.roblox.com/t/roblox-is-coming-to-meta-quest/2465291) |
| Active experiences | 15 million by December 31, 2022 | Total active experiences on Roblox; figure is dated, check current stats. | [Roblox DevForum 2023-07](https://devforum.roblox.com/t/roblox-is-coming-to-meta-quest/2465291) |
| Minimum age for Roblox on Meta Quest | 13 and older | Age requirement on Quest; source dated 2023-07. | [Roblox DevForum 2023-07](https://devforum.roblox.com/t/roblox-is-coming-to-meta-quest/2465291) |
| Supported Quest devices in Open Beta | Meta Quest 2 and Meta Quest Pro | App Lab Open Beta device support as of 2023-07; likely outdated. | [Roblox DevForum 2023-07](https://devforum.roblox.com/t/roblox-is-coming-to-meta-quest/2465291), [Roblox DevForum 2023-07](https://devforum.roblox.com/t/roblox-is-coming-to-meta-quest/2465291) |
| Share of sessions on mobile | Majority | Roblox Creator Docs state most sessions are played on mobile devices (2026-10). | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/input/mobile) |
| Orientation modes | 5 (2 sensor-based, 3 locked) | No portrait-upside-down mode included. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/input/mobile) |
| PreferredInput enum values | Touch, Gamepad, KeyboardAndMouse | Values returned by UserInputService.PreferredInput. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/input) |
| Mobile with Bluetooth keyboard and mouse | PreferredInput switches to KeyboardAndMouse | Switches once the peripheral is connected and used. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/input) |
| Xbox/PlayStation with keyboard and mouse | PreferredInput = KeyboardAndMouse when most recently used | Depends on the most recently used device. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/input) |
| Max players for Voice Chat | 100 | Maximum Visitor Count must be 100 or fewer; restart servers after lowering. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/chat/voice-chat), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/chat/voice-chat) |
| Eligible users for Roblox (age gate) | 13+ and age-verified | Users outside supported countries need ID verification. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/chat/voice-chat) |
| Concurrent players before considering Xbox/mobile | ~10 | Indie suggested threshold, self-reported, 2019-10. | [Last Level Studios 2019-10 6:43](https://youtu.be/vY0om5O-Oh8?t=403), [Last Level Studios 2019-10 6:43](https://youtu.be/vY0om5O-Oh8?t=403) |
| Console vs PC player split (example game) | ~4,800 console vs ~80 PC players | Single indie example, self-reported, 2019-10. Shows console audiences can dwarf PC. | [Last Level Studios 2019-10 6:43](https://youtu.be/vY0om5O-Oh8?t=403) |
| VR share of Steam hardware survey | ~2-3% (best case ~2% of Roblox PC market) | Self-reported, 2021-12. Dated. | [Last Level Studios 2021-12 8:52](https://youtu.be/v_TGu45AD_g?t=532) |
| Roblox platform split | ~70% mobile, ~30% split between PC and Xbox | Self-reported, 2021-12. Dated; verify with current analytics. | [Last Level Studios 2021-12 8:12](https://youtu.be/v_TGu45AD_g?t=492) |
| Quest 2 refresh rate | 120 Hz | Hardware spec for Quest 2, 2021-12. Older headset. | [Last Level Studios 2021-12 33:44](https://youtu.be/v_TGu45AD_g?t=2024) |
| Web Play launch channel | Chrome first, no install | Sept 2026; other browsers not stated in sources. | [GamesBeat 2026-09](https://gamesbeat.com/roblox-hits-20-and-opens-rdc-2026-to-invite-the-world-to-play-and-make-games-dave-baszucki-keynote/), [Roblox Investor Relations 2026-09](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026068235/ex991-q32026earningsshar.htm) |
| Budget-phone performance claim | Every top-10 game runs well on a budget phone | StudioKrew, GGAID data, self-reported indie figure; no device spec given. | [StudioKrew (agency blog, GGAID data) 2026-05](https://studiokrew.com/blog/top-roblox-games-may-2026/) |
| Offline solo play target | By mid-2027 | Forward-looking GamesBeat report, not official confirmation. | [GamesBeat 2026-09](https://gamesbeat.com/roblox-hits-20-and-opens-rdc-2026-to-invite-the-world-to-play-and-make-games-dave-baszucki-keynote/) |
| Logins on mobile (share of Discord logins) | 56% | Self-reported by an indie developer; one data point from one community, not a platform-wide benchmark. Use it only as a rough reference. | [Deconstructor of Fun 2026-10 20:31](https://youtu.be/NW4EShVGPYs?t=1231) |
| Console install base referenced | about 150 million | Single indie creator, self-reported, low-advice. Treat as an unverified market-size reference, not platform ground truth; check against official platform disclosures before using it in planning. | [Deconstructor of Fun 2026-07 8:19](https://youtu.be/i6F_0YVzhz8?t=499) |
| Pre-order attach rate estimate (premium-skewed audience) | north of 50% to 60% | Speaker's own estimate during pre-order, self-reported, low-advice. Not a measured benchmark; do not use as a forecast for conversion or revenue without your own data. | [Deconstructor of Fun 2026-07 6:56](https://youtu.be/i6F_0YVzhz8?t=416) |

## Where creators agree
- Mobile and touch support matters: rasdev (T6774) and GuideRealm (T6868) both say to support or test on phones and tablets, and official docs note phone and tablet players can always tap prompts (T7399).
- Console and gamepad are important targets; official docs cover gamepad conventions and Controller Emulator testing (T7085, T7150), and rasdev lists console among supported platforms (T6774).
- Test UI across screen sizes: GuideRealm checks readability and tap targets (T6868), official docs recommend Device Simulator across form factors (T8247, T8291).
- Real hardware testing is preferred when available (T8204, T6936); emulators are the fallback when you do not own the device (T7150, T8291).
- Adapt to the detected input type rather than assuming a platform; official PreferredInput guidance (T7084, T7755) is consistent with rules that avoid hardcoded keys (T7087, T7754).
- Design for mobile first and for every supported platform rather than optimizing for one (VuukStudios, Roblox Creator Docs).
- Enable every target device at publish time so players can switch devices (Roblox Creator Docs, Roblox DevForum).
- Both Last Level Studios and Emancyphur advise avoiding mouse-only input so buttons and actions work for touch and controller players (T15725, T15812).
- Official Roblox sources (T17550, T17564) agree that multi-platform support, including cross-play, is a core goal.
- Indie sources (T17461, T17478) agree on mobile-first design, which reinforces the existing mobile-first rule.
- T17538 and T17550 agree that Web Play lets players join from a link with no install, Chrome first.

## Where creators disagree
- **Whether mobile and console support is mandatory**
  - rasdev (T6774, indie, self-reported): support mobile, tablet, console and desktop because most players use phones or tablets and missing mobile costs players.
  - Roblox Creator Docs (T9527, OFFICIAL): optimizing for console and mobile is recommended, not required, but improves consideration.
  - Resolution: prefer the official wording for requirement status; treat rasdev's player-share claim as unverified.
- **Emulator versus real device for mobile testing**
  - GuideRealm (T6868): test on mobile, checking tap targets, readability and performance on phones.
  - Roblox Creator Docs (T8291, T7150): emulate touch, screen size and gamepad/VR input in Studio without owning the device.
  - Not a true conflict: use real devices when available (T8204) and the emulator when they are not.
- **How much extra work VR publishing needs**
  - Roblox DevForum [OFFICIAL] (T11787): default player scripts usually run well in VR with little or no modification.
  - Roblox DevForum [indie] (T11007, T11008, T11010): custom VR needs controller-model removal, hand updates in UserCFrameChanged, and anchoring HumanoidRootPart to stop the default character.
- **Which input API to use for bindings**
  - Roblox Creator Docs [OFFICIAL] (T14237, T15110, T14347): use the Input Action System with multiple bindings per action.
  - Roblox Creator Docs [OFFICIAL] (T15345): ContextActionService with KeyCodes also covers keyboard and controller buttons. Treat this as older guidance and prefer the Input Action System for new work.
- **When to add console and tablet support**
  - T17564 (official, Nov 2026): support PC, mobile, tablet and console from launch.
  - Existing file rule: consider Xbox or mobile support around 10 concurrent players (staged approach).
- **Whether to ship one codebase for cross-play or separate pure-play builds**
  - Existing knowledge file rule 'Ship one codebase for cross-play' favors a single cross-play codebase.
  - Deconstructor of Fun (T17948) argues cross-platform is a retention tool, not a revenue play, and recommends pure-play builds per platform group (mobile vs PC/console).

## Date context (what may be outdated)
- All Roblox Creator Docs items are dated 2026-10 (most recent) and are treated as ground truth for platform mechanics.
- Older items: rasdev N2809 (VR player count, 2026-06) is the oldest and is self-reported and unverified. Rasdev T6774 (2026-09) and GuideRealm T6868 (2026-10) are indie advice.
- Android TV guidance comes from a limited pilot (90 days, 25 creators, N2982/N2983). Expect details to change after the pilot.
- T8198 says Enum.PreferredInput.MicroGamepad is 'not yet set'. Re-check this before relying on micro-gamepad detection, since it may change.
- Legacy TV-remote keycode mapping (T8200) is the older route. For new work, prefer the Input Action System (T7087, T7754) and PreferredInput (T7084). Legacy codes still matter for TV remote compatibility and for separating navigation and gameplay contexts (T8201).
- Hardcoded individual keys are the older pattern that later Roblox guidance (T7087, T7754) replaces with Input Action System bindings. No source explicitly labels anything as deprecated.
- Low-advice videos (T6990, T8247, T8331, T8395, T9500, N2809) are weaker evidence than the official docs.
- VR guidance T11006 to T11010 is from 2021-05, before the 2023 official VR Open Beta; verify SetCore and VR setting names against current docs.
- Quest device support (T11790, N4496) and the 66M/15M figures (N4493, N4494) are from 2023-07 and are likely outdated.
- Input bindings are in beta as of 2026-02 (T13209) and may change.
- Input Action System guidance (2026-10) supersedes ContextActionService-based binding (T15345) for new work.
- Console and VR age check gap (T13337, 2026-04) may close; re-check before relying on it.
- Client update lag for mobile and console (T13574, 2026-07) is a recent observation.
- Chrome web-start via Details Page URL (T13816) is announced for late 2026; confirm availability before promoting it.
- 2019-10 advice (Xbox/mobile at ~10 concurrent players, generic input activation) predates much current cross-platform tooling; re-verify before relying on it.
- 2020-08 Activated-event advice is still consistent with current GUI event practice but should be checked against current docs.
- 2021-12 platform split and VR share figures are about five years old as of 2026-10; treat as historical context, not current benchmarks.
- Quest 2 at 120 Hz is older hardware; newer headsets exist with different specs.
- Sept 2026: Web Play (Chrome first) lets players join via direct link or Details Page with no install (T17538, T17550). Earlier advice assumed install-only access; prefer the newer access path.
- Sept 2026: Roblox states cross-play needs no extra work on the same codebase (T17550).
- Nov 2026: official guidance favours launch-day support across PC, mobile, tablet and console (T17564). This is newer than the staged approach in the existing file; prefer it for launch planning but still verify capacity and per-platform UI.
- Offline solo play by mid-2027 (T17538) is a forecast from a news report, not a confirmed roadmap; do not build on it yet.
- T17674 (Roblox DevForum [OFFICIAL], 2026-09): offline solo play alongside a live multiplayer mode is planned for mid 2027. This is a roadmap item, not shipped, and it does not change any console, mobile, VR or input guidance.
- T17684 (Roblox Newsroom [OFFICIAL], 2026-09, low-advice): turn-based and asynchronous multiplayer is expanding. A turn notification system was slated for Studio Beta in October 2026 with full release by year end 2026. As of 2026-11-01 the Beta window has opened, so check whether the feature has reached full release before relying on it. It is not platform-specific and adds no cross-platform input rules.
- Deconstructor of Fun's items are dated 2026-10 and are self-reported indie figures; the 56% mobile login share (N7709) is from one Discord community and may not reflect the wider Roblox audience.
- Today is 2026-11-01. Re-check cross-platform analytics before acting on single-source claims.
- Figures are dated 2026-07 and may be stale by the current date (2026-11-01); re-check the console install base against current platform disclosures.

## Instructions for an agent using this file
- If the experience targets any non-PC platform, then ensure touch works: tappable prompts (T7399), readable UI and smooth performance on phones (T6868), and treat console and mobile optimization as recommended (T9527).
- If you define gameplay inputs, then use Input Action System actions with multiple bindings and do not hardcode keys (T7087, T7754).
- If the UI needs to adapt to input, then read PreferredInput (T7084, T7755); if it is insufficient, add GamepadConnected/GamepadDisconnected or GamepadEnabled checks (T7090).
- If the player can switch input mid-session, then test UI updates when a controller connects or a trackpad switches to mouse (T9701).
- If you build an Android TV experience, then design D-pad-friendly controls (T6935, T6937), test with TV Remote simulation and hardware (T6936), and use the 1920x1080 emulator with the TV Remote Controller Emulator if no hardware (T8204, N3371).
- If you detect a TV remote, then check Gamepad1 for no Thumbstick1/2 and ButtonCenter support, not keycodes alone (T8198, T8199); map ButtonCenter to ButtonA, ButtonBack to ButtonB, and D-pad keys to DPad (T8200).
- If nav and gameplay share a remote button, then use separate input contexts (T8201). If you hide default touch controls, then set GuiService.TouchControlsEnabled=false only when you supply your own (T8194).
- If the mouse is locked, then read InputChanged MouseMovement Delta instead of position (T7759).
- If you build VR, then configure OpenXR before launching Studio (T8292), test each hand separately (T8630), and use Reset Positions when stuck (T8631).
- If you override default controls or a gameplay cue relies on grass motion, then override only for specific needs (T9391) and add a non-motion cue for Reduce Motion players (T7259).
- If the target includes VR, first test whether default player scripts work, then add custom VR code only where needed.
- If building custom VR hands, disable controller models and the laser pointer first, then drive hand positions from UserCFrameChanged.
- If building VR, anchor HumanoidRootPart when the default character should not move or show.
- If building mobile UI, place controls in a 'Mobile Controls' ScreenGui and enable it only when TouchEnabled is true.
- If using gestures, gyro, or accelerometer input, check AccelerometerEnabled, GyroscopeEnabled, and gesture support first.
- If the UI depends on orientation, set separate emote bar positions and listen to ScreenOrientation changes.
- If the experience needs Voice Chat, keep max players at 100 or fewer and restart servers after lowering the limit.
- If the target includes console or VR, plan a fallback for the age check flow.
- If referencing default PC keybinds, mark them as beta and read bindings at runtime instead of hardcoding them.
- When writing new bindings, prefer the Input Action System over ContextActionService with KeyCodes.
- If code uses mouse-only click events for buttons and the project targets multiple platforms, switch to Activated-style events.
- If an experience is planning console or mobile support, check current concurrency and analytics first; do not treat the ~10-player threshold as official.
- If citing platform split or VR share numbers, state that they are self-reported and dated (2021), and prefer current data.
- Treat all indie figures in this set as self-reported, not [OFFICIAL] platform ground truth.
- If a user asks how players should join, recommend the Details Page URL or direct link and note Web Play is Chrome first.
- If a user is planning cross-platform release, use one codebase, confirm cross-play, and gate differences by input type.
- If a user asks about launch platforms, prefer the Nov 2026 official guidance (support all platforms at launch) and flag the staged-rollout advice in the existing file as older.
- If a user targets mobile, include low-end Android testing before launch.
- Do not state offline solo play as available or confirmed; cite it as a forecast only.
- Do not claim Web Play supports browsers other than Chrome; sources only cover Chrome.
- Do not plan console, mobile or VR launch scope around T17674 or T17684; both are general multiplayer or solo-mode roadmap items with no platform input changes.
- If a task depends on turn-based or async multiplayer notifications, verify current availability in Studio and the official Newsroom before building on it, since the schedule was announced as planned.
- If a request asks whether to ship one cross-play codebase or separate pure-play builds, note the disagreement (T17948 vs the existing cross-play rule) and ask for the target audience's device mix before recommending.
- If citing the 56% mobile login figure (N7709), label it as self-reported and from a single Discord community, not an official platform statistic.
- Do not treat single-mention indie claims (T17948, T17972) as established best practice.
- If a planning decision depends on the console install base or a pre-order attach rate, cite the figure as self-reported (N8159, N8160) and verify it independently before relying on it.
- Do not treat indie-creator market estimates as platform ground truth; [OFFICIAL] items take precedence.

## Not covered here (research elsewhere)
- No console-specific guidance on Xbox or PlayStation certification, platform store rules, controller vibration or button-hold behaviour.
- No mobile performance budgets (FPS targets, memory limits) or minimum tap-target sizes.
- No touch UI layout patterns beyond tap behaviour and TouchControlsEnabled.
- No VR comfort or locomotion guidance, and no verified VR player count (N2809 is unverified).
- No Android TV pilot application or eligibility details beyond the 90-day, 25-creator timeline.
- No code samples for Input Action System setup or PreferredInput handling.
- No compatibility matrix for Bluetooth controllers, Steam Deck or other handhelds.
- No per-platform revenue, CCU or visit data; the only such claim (rasdev) is unverified.
- T9233 (non-R15 layered accessories) and T9500 (Toolbox audio) are only loosely related to cross-platform input and should be researched separately.
- VR comfort, locomotion, and frame-rate targets are not covered.
- Current Quest and Open Beta device lists after 2023-07 are not covered.
- Console-specific button mappings beyond existing Enum.GamepadType notes are not covered.
- Haptics API details are not covered; only the existence of haptics on mobile and gamepad is noted (T15119).
- Input Action System API details (setting up actions and bindings in code) are not covered.
- Console certification and publishing requirements are not covered.
- Details of the late-2026 Chrome web start and how it interacts with device enablement are not covered.
- The age-check flow details for consoles and VR (what fallback is allowed) are not covered.
- No official Roblox data on current platform split, console versus PC audience size, or device share.
- No official guidance on the ~10-concurrent-player threshold for adding Xbox or mobile support.
- No verification of Activated event behavior across all input types, including gamepad selection and touch.
- No coverage of Xbox certification, console-specific input requirements or platform submission rules.
- No current VR headset data beyond Quest 2 (2021); no 2026 hardware or market figures.
- No detail on how to test the Activated pattern across the Device Simulator and Controller Emulator.
- Which features are unsupported or limited in Web Play, and any performance limits in the web player.
- Whether Web Play extends beyond Chrome to other browsers, and timelines for it.
- Cross-play details for VR, Android TV and console specifically, beyond the general one-codebase statement.
- Device specs defining low-end Android, and performance budgets for budget phones.
- Console certification or platform-approval requirements and timelines.
- Underlying GGAID data and methodology behind the StudioKrew top-10 claim.
- Confirmed date and scope for offline solo play.
- T17674 and T17684 contain no console, VR, mobile, TV or input-handling guidance, so this topic gains no new rules from them.
- No official or creator source here covers whether turn notifications or offline solo play will support gamepad, touch or VR prompts. Research platform-specific UI behavior for these features separately once they ship.
- No new Enum.GamepadType, PreferredInput, Device Simulator, OpenXR or Android TV information is included in these items.
- No official Roblox data on cross-platform retention or revenue; the new items are indie, self-reported claims.
- No evidence on how mobile ad campaigns affect cross-platform installs beyond one developer's anecdote.
- No platform-wide device-usage statistics in these sources to check the 56% mobile login figure against.
- No official source confirms the console install base figure (N8159); verify against platform publisher disclosures.
- The attach rate (N8160) is not defined in the source beyond a pre-order estimate; no method, sample, or product definition is given.
- No input-handling, UI, or platform-design guidance was included in these additions; the existing rule set covers those areas.

## Appendix: every extracted tip on this topic

- 2019-10-11 Last Level Studios [6:43](https://youtu.be/vY0om5O-Oh8?t=403): Add Xbox or mobile support once the game has about 10 concurrent players; these audiences can be larger than PC.
- 2019-10-11 Last Level Studios [10:46](https://youtu.be/vY0om5O-Oh8?t=646): Use generic default input activation rather than many keyboard- or mouse-specific actions to ease porting.
- 2020-08-19 Emancyphur [12:12](https://youtu.be/LjETISdUBp8?t=732): Use MouseButton1Click-style 'Activated' events instead of mouse-only events so mobile, touch and controller players can click buttons.
- 2021-05-15 Roblox DevForum [page](https://devforum.roblox.com/t/creating-simple-vr-hands-from-scratch/1227966): Set Camera.CameraType to Scriptable and reset camera CFrame to its position to avoid a wrongly angled VR view.
- 2021-05-15 Roblox DevForum [page](https://devforum.roblox.com/t/creating-simple-vr-hands-from-scratch/1227966): Disable VR controller models (SetCore VREnableControllerModels false) and laser pointer (VRLaserPointerMode 0) before replacing them with custom hand models.
- 2021-05-15 Roblox DevForum [page](https://devforum.roblox.com/t/creating-simple-vr-hands-from-scratch/1227966): Update hand positions in UserInputService.UserCFrameChanged, which fires before render, to avoid visible lag between controller and hand models; multiply move by camera.CFrame.
- 2021-05-15 Roblox DevForum [page](https://devforum.roblox.com/t/creating-simple-vr-hands-from-scratch/1227966): Anchor the HumanoidRootPart to stop the default character from moving or being visible while in VR.
- 2022-04-14 Suphi Kaner [31:24](https://youtu.be/FVOowr2DXbM?t=1884): Read SteerFloat and ThrottleFloat rather than raw keys: they give finer control for mobile D-pad and gamepad input.
- 2023-07-12 Roblox DevForum [page](https://devforum.roblox.com/t/roblox-is-coming-to-meta-quest/2465291): Existing experiences using default player scripts typically run well in VR without modifications, so publishing to VR may need little extra coding.
- 2023-07-12 Roblox DevForum [page](https://devforum.roblox.com/t/roblox-is-coming-to-meta-quest/2465291): Use the Access page (Creator Dashboard > Creations > select experience > Access) or Game Settings in Studio to control VR, Desktop, Mobile, Tablet and Console availability per experience.
- 2023-07-12 Roblox DevForum [page](https://devforum.roblox.com/t/roblox-is-coming-to-meta-quest/2465291): Note that the Open Beta supports only Meta Quest 2 and Meta Quest Pro; target those devices for early testing.
- 2023-07-12 Roblox DevForum [page](https://devforum.roblox.com/t/roblox-is-coming-to-meta-quest/2465291): If you publish only to 'Desktop', it stays available on PC VR for now, but in future only experiences with the 'VR' checkbox will be available on PC VR, with advance notice.
- 2023-09-24 VuukStudios [0:37](https://youtu.be/dcJtZnan7i8?t=37): Build mobile controls in a separate ScreenGui in StarterGui named 'Mobile Controls' and enable it only when UserInputService.TouchEnabled is true.
- 2024-08-30 VuukStudios [5:02](https://youtu.be/3J7Vp6NgYf4?t=302): Design and monetise for mobile users first, since most Roblox players are on mobile rather than PC or console.
- 2026-02-18 Roblox DevForum [page](https://devforum.roblox.com/t/studio-beta-avatarabilities-library-for-a-luau-based-character-controller/4403904): Strafe defaults to Left Alt on PC and Left Option on Mac; Crouch uses C; Sprint uses Left Shift. Input bindings are still in beta and may change.
- 2026-03-00 RoWatcher (tracker blog) [page](https://rowatcher.com/news/the-10-fastest-growing-roblox-games-in-march-2026): Design mobile-first and accessible; the fastest-climbing games favour approachability over complexity on a mobile-heavy audience.
- 2026-04-30 Roblox DevForum [page](https://devforum.roblox.com/t/introducing-the-us-18-devex-rate-earn-42-more-on-spend-from-18-us-players/4607091): Console and VR do not currently support the age check flow; plan fallback experiences for those players.
- 2026-05-00 StudioKrew (agency blog, GGAID data) [page](https://studiokrew.com/blog/top-roblox-games-may-2026/): Design mobile-first: every top-10 game runs well on a budget phone, so test on low-end Android before launch.
- 2026-06-15 Roblox DevForum [page](https://devforum.roblox.com/t/pilot-create-and-sell-animation-packs-and-emotes-on-marketplace/4684642): Animation Packs (R15) require 7 clips: Idle, Walk, Run, Jump, Fall, Climb, Swim.
- 2026-07-09 Roblox DevForum [page](https://devforum.roblox.com/t/full-release-ship-fair-and-competitive-games-with-server-authority/4727993): Mobile and console clients lag desktop updates by a few days and cannot connect until their client update lands.
- 2026-08-07 Roblox DevForum [page](https://devforum.roblox.com/t/weekly-recap-august-3-7-2026/4781555): Use InputActionLabel (Beta, File > Beta Features) to auto-display an InputAction's binding on-screen, using PreferredBinding, for cross-platform hotkey UI.
- 2026-08-21 Business of Creators [24:56](https://youtu.be/lpIzMycpiKo?t=1496): Roblox games need no extra work to run on phone, tablet, console, PC, VR and Fire Stick once published.
- 2026-09-10 GamesBeat [page](https://gamesbeat.com/roblox-hits-20-and-opens-rdc-2026-to-invite-the-world-to-play-and-make-games-dave-baszucki-keynote/): Web player lets players join from the Experience Details Page in Chrome with no install. Offline solo play alongside multiplayer arrives by mid-2027.
- 2026-09-11 Roblox DevForum [page](https://devforum.roblox.com/t/rdc26-what-we-announced/4865880): Share the game's Details Page URL on YouTube, X or Discord; players can start on web in Chrome with no install (late 2026).
- 2026-09-11 Roblox DevForum [page](https://devforum.roblox.com/t/rdc26-what-we-announced/4865880): Offline solo play alongside a live multiplayer mode is planned for mid 2027.
- 2026-09-11 Roblox Newsroom [page](https://about.roblox.com/newsroom/2026/09/rdc-2026-the-world-needs-more-play): Turn-based and asynchronous multiplayer is expanding; a turn notification system arrives in Studio Beta in October 2026 and full release by year end.
- 2026-09-13 rasdev [3:24](https://youtu.be/Df5ebFGEOXY?t=204): Support mobile, tablet, console and desktop, since most players use phones or tablets, and missing mobile costs players.
- 2026-09-17 Roblox [15:14](https://youtu.be/3a2RbLOAl4A?t=914): Games can mix online and offline modes; offline play syncs when reconnected, avoiding the disconnect dialog.
- 2026-09-17 Roblox [1:44:45](https://youtu.be/3a2RbLOAl4A?t=6285): All games will be playable in browser by year-end via WebAssembly; shared links work with or without the app.
- 2026-09-17 Roblox [1:52:17](https://youtu.be/3a2RbLOAl4A?t=6737): Standalone app builds of a single experience can ship through app stores while sharing the same cloud, services and safety stack.
- 2026-09-30 Roblox Investor Relations [page](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026068235/ex991-q32026earningsshar.htm): Web Play (Chrome first) lets players join via direct link with no install; same codebase gives cross-play with no extra work.
- 2026-10-17 GuideRealm [7:38](https://youtu.be/ltbZzXRrDF8?t=458): Test on mobile: check buttons are easy to tap, UI is readable, and performance is smooth, since many players use phones.
- 2026-10-22 Deconstructor of Fun [15:36](https://youtu.be/oU3oz6Ddz7g?t=936): Treat cross-platform as a retention tool, not a revenue play; build pure-play for mobile, or PC/console, rather than a single game spanning both.
- 2026-10-26 Deconstructor of Fun [21:12](https://youtu.be/NW4EShVGPYs?t=1272): Use mobile ads to drive cross-platform installs; claimed majority of users use both mobile and PC.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/creator-programs/android-tv-pilot): Android TV pilot favors experiences with straightforward controls that adapt to a D-pad: 2D games, simple movement, or menu-driven mechanics.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/creator-programs/android-tv-pilot): Use TV Remote simulation in Studio plus hardware testing to validate input mapping before publishing for TV remote play.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/creator-programs/android-tv-pilot): Plan input mapping and UI optimization for D-pad navigation; Roblox offers hands-on technical help for this in the pilot.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/tutorials): Detect user input to trigger actions and choose a camera type (first-person, side-scrolling, isometric) that suits the gameplay.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/input/gamepad): Detect the player's PreferredInput type and respond to it so on-screen buttons and menus adapt across devices; a PC player may connect a gamepad and want it as primary.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/input/gamepad): Use common gamepad conventions: ButtonA for confirm/jump, ButtonB for cancel/dodge/sprint, Thumbstick1 movement, Thumbstick2 camera, R2/L2 primary actions like shooting.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/input/gamepad): Define gameplay inputs as Input Action System actions with bindings for multiple hardware inputs rather than hardcoding individual keys.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/input/gamepad): Listen to GamepadConnected/GamepadDisconnected or check GamepadEnabled as alternative detection methods if PreferredInput is not sufficient.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/studio/device-simulator): Use Controller Emulator alongside Device Simulator to test gamepad, VR and TV remote input without owning the hardware.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/studio/device-simulator): Use the touch shortcuts (Alt+drag for pinch/rotate, Alt+Shift+drag for two-finger pan) to validate touch inputs land correctly.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/parts/terrain): Animated grass speed is reduced when players enable Reduce Motion, so don't rely on grass motion alone for gameplay-critical cues.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/tutorials/first-experience): Enable every device you want players to use (phones, computers, tablets, consoles, VR) in the Devices section at publish time.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/ui/proximity-prompts): Set KeyboardKeyCode and GamepadKeyCode; Roblox shows the correct input glyph per device type.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/ui/proximity-prompts): Phones and tablets can always tap a prompt, regardless of ClickablePrompt; plan touch input accordingly.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/input/mobile): Design for mobile first: the majority of Roblox sessions are played on mobile devices, so consider orientation and touch from the start.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/input/mobile): Use the Input Action System to define actions (jump, sprint, shoot) and bind multiple hardware inputs to each, rather than hardcoding per-device input.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/input/mobile): Check UserInputService.PreferredInput to decide which UI to show; switch to on-screen buttons only when touch is primary, and keep touch as a backup when a gamepad is connected.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/input/mobile): Change orientation at runtime via PlayerGui.ScreenOrientation and listen to PlayerGui:GetPropertyChangedSignal("ScreenOrientation") to respond to changes.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/input/mobile): Use touch gestures (TouchSwipe, TouchPinch) and accelerometer/gyroscope only where the device supports them, checking AccelerometerEnabled and GyroscopeEnabled first.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/effects/trails): Trail visual quality changes with player graphics settings; test in Studio by setting Editor Quality Level to both lowest and highest before finishing.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/input/mouse-and-keyboard): Use the Input Action System to define actions (jump, sprint, shoot) and bind multiple hardware inputs to each, instead of hardcoding keys.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/input/mouse-and-keyboard): Check UserInputService.PreferredInput to adapt on-screen buttons and menus; a connected gamepad can become the primary input even on PC.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/input/mouse-and-keyboard): While the mouse is locked, read InputChanged with UserInputType MouseMovement and use Delta for movement, since position no longer changes.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/input): Build controls with the Input Action System (actions plus multiple bindings) so one action works across touch, keyboard, gamepad and VR.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/ui/on-screen-containers): Set GuiService.TouchControlsEnabled to false in a client script to hide the default virtual thumbstick and jump button on touch devices.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/input/micro-gamepad): Detect micro gamepads by checking Gamepad1 is connected and supports neither Thumbstick1 nor Thumbstick2; Enum.PreferredInput.MicroGamepad is not yet set.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/input/micro-gamepad): Do not identify TV remotes by legacy keycodes alone; full gamepads send the same codes. Check ButtonCenter support on Gamepad1 as well.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/input/micro-gamepad): Bind TV remote buttons via legacy codes: ButtonCenter maps to ButtonA, ButtonBack maps to ButtonB, D-pad keys map to DPad directions.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/input/micro-gamepad): Use separate input contexts for navigation and gameplay so one legacy button does not fire both actions at once.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/input/micro-gamepad): Test with a physical TV remote when possible; otherwise use Studio Device Emulator (Android TV, 1920x1080) with the Controller Emulator TV Remote.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/studio): Use Studio device emulation to test a range of screen sizes and form factors before publishing, so the UI looks right on all devices.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/studio/testing-modes): Use Device Simulator with Controller Emulator to preview touch, screen size, DPI and gamepad/VR input without owning the device.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/studio/testing-modes): For VR testing on Windows, configure the OpenXR runtime before launching Studio; with multiple headsets, configure only the one you want to test with.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/resources/battle-royale/run-the-game): Map every control for keyboard/mouse, mobile, and controller up front; the battle-royale project defines separate mappings for each input type.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/ui/3D-drag-detectors): Use BestForDevice drag style to get appropriate behaviour per input: TranslatePlaneOrLine for mouse and gamepad, TranslatePlane for touch, 6DOF for VR.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/studio/controller-emulator): Test VR interactions one hand at a time by disabling the headset and one controller, to check reach, grab volumes and whether interactions depend on gaze.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/studio/controller-emulator): Use Reset Positions during a playtest to recover quickly from a VR pose you cannot recover by hand.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/studio/controller-emulator): Check code branching on Enum.GamepadType, since the experience sees the emulated controller type as it would with the real device.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/resources/modules/emote-bar): Emote bar position differs by orientation: set emoteBarPosLandscape and emoteBarPosPortrait separately; hotkeys cover only numeric keys 1-9.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/use-case-tutorial-overview): Design the camera configuration and supported input types (mouse, mobile, gamepad) early, since they affect accessibility and engagement.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/ui/position-and-size): Design for all platforms you support (mobile, PC, console) rather than optimizing for one and neglecting others, since players switch devices.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/art/modeling/cage-meshes/apply-deformation): Custom non-Marketplace characters using a unique cage or UV solution need the separate non-R15 layered accessories guidance.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/input/input-action-system): Only override Roblox default controls (movement, camera, reserved keys) in specific cases; players already know them.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/education/build-it-play-it-island-of-move/save-and-publish): Mobile players can move characters with device accelerometers; desktop players click a button to move. Plan controls for both.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/projects/assets/toolbox): If Toolbox audio is silent on Windows, open Volume Mixer and make sure Microsoft Edge WebView2 is not muted.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/creator-programs/standout-games): Recommended: optimize for both console and mobile devices. Not required but improves consideration.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/resources/battle-royale): Support mobile, Xbox and high-end PC from the start; the kit's systems are built to work across phones, consoles, controllers and screen sizes.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/projects/cross-platform): Use the Input Action System to define actions (jump, sprint, shoot) and bind multiple hardware inputs to each, instead of handling raw device inputs.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/projects/cross-platform): Respond to the primary input type (UserInputService.PreferredInput), not just device capability. Touch stays a backup when a gamepad is connected.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/projects/cross-platform): After the game is cross-platform, add haptics on mobile/gamepad, touch swipe/pinch gestures, and accelerometer/gyroscope where it fits.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/chat/voice-chat): Keep max players at 100 or fewer; Voice Chat is only available for places supporting a maximum of 100 players.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/chat/voice-chat): After lowering max players below 100, restart servers, since existing higher-capacity servers won't support Voice Chat.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/projects): Newly published games are only visible to the creator, Edit/Playtest users and qualifying group members until you release them to a wider audience.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/performance-optimization/test-on-hardware): Verify the UI responds correctly when players switch input type mid-session, such as connecting a Bluetooth controller or switching trackpad to mouse.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/performance-optimization/test-on-hardware): Multi-input devices (handheld gamepads with touchscreens, phones with USB-C gamepad adapters) cover touch and gamepad testing on one device.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/input-and-camera/detect-user-input): Use ContextActionService with KeyCodes rather than raw input checks; the same binding can cover keyboard and controller buttons.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/education/educator-onboarding/3-setting-up-a-roblox-classroom): For larger schools, create a batch installer deployable via USB drive or image; for small classes, install per computer from a browser.
- 2026-10-29 Roblox DevForum [page](https://devforum.roblox.com/t/creators-can-test-games-on-the-web/4964592): Design around unavailable web features: voice chat, party/friends chat, video playback/ads, moments capture, haptics, in-game avatar switching, remote MicroProfiler.
- 2026-10-30 Roblox DevForum [page](https://devforum.roblox.com/t/studio-beta-build-2d-isometric-and-top-down-games-with-orthographic-camera/4966772): Orthographic cameras are not supported in VR during beta; device support details are promised before full release.
- 2026-10-30 Roblox DevForum [page](https://devforum.roblox.com/t/weekly-recap-october-26-30-2026/4966810): Use the Input Action Manager (Window > Input) to build and audit cross-platform control mappings visually.
- 2026-11-01 Roblox public API [page](https://www.roblox.com/games/95168737547508/): Support PC, mobile, tablet and console from launch to widen the audience.

Index: [[README]] | Master: [[master-playbook]]
