---
title: "Designing for Accessibility with BitwiseAndrea, WooleyWool, and ControlCoreAngel"
url: https://youtu.be/K1pEI6LVJJA
creator: Roblox Creators
official: true
advice_density: high
date: 2023-05-18
views: 1121
transcript: manual-subs
confidence: high
tags: [roblox, robloxcreators, youtube-learn]
---

# Designing for Accessibility with BitwiseAndrea, WooleyWool, and ControlCoreAngel

[Watch](https://youtu.be/K1pEI6LVJJA) | RobloxCreators | 1,121 views | 2023-05-18

## Summary
Roundtable on designing accessible Roblox games with Roblox accessibility engineer BitwiseAndrea and developers WooleyWool and ControlCoreAngel. Covers goals of accessibility, visual (contrast, colorblind-safe design, don't rely on color alone), auditory (captions, separate volume controls via sound groups), motor (rebindable keys, WASD plus arrows, larger buttons, no simultaneous key combos), epilepsy/migraine warnings, tutorials for learning disabilities, and inclusive community/playtesting.

## Tips
- [1:00](https://youtu.be/K1pEI6LVJJA?t=60) **[[playtesting-and-feedback]]** Recruit disabled players and varied testers to try your game; their feedback is what confirms whether controls and UI actually work for all players.
- [26:10](https://youtu.be/K1pEI6LVJJA?t=1570) **[[thumbnails-icons]]** Check UI and text color contrast against WCAG guidelines or a contrast calculator; large text can use lower contrast, but avoid combos like white on yellow.
- [28:53](https://youtu.be/K1pEI6LVJJA?t=1733) **[[building-art-and-assets]]** Keep your palette but add outlines or tweak brightness to make key elements stand out for colorblind players rather than abandoning the look.
- [29:34](https://youtu.be/K1pEI6LVJJA?t=1774) **[[building-art-and-assets]]** Test colorblind legibility by viewing your UI in monochrome; if elements blend in grayscale, they will likely blend for colorblind players.
- [32:59](https://youtu.be/K1pEI6LVJJA?t=1979) **[[building-art-and-assets]]** Don't convey meaning by color alone; add symbols or icons, e.g. team markers, as Super Doomspire does.
- [34:36](https://youtu.be/K1pEI6LVJJA?t=2076) **[[building-art-and-assets]]** Provide visual alternatives for sound cues, such as captions or on-screen indicators for a ringing phone.
- [35:56](https://youtu.be/K1pEI6LVJJA?t=2156) **[[building-art-and-assets]]** Give players separate volume controls for music, effects and speech; use Roblox sound groups to make this easy to implement.
- [36:37](https://youtu.be/K1pEI6LVJJA?t=2197) **[[core-loops-and-game-design]]** Offer options to lower or disable background music and sound effects; many players with cognitive disabilities find overlapping sounds overwhelming.
- [41:43](https://youtu.be/K1pEI6LVJJA?t=2503) **[[core-loops-and-game-design]]** Make keybinds fully customizable rather than one fixed scheme, since disability needs vary and abled players also have preferences.
- [43:45](https://youtu.be/K1pEI6LVJJA?t=2625) **[[core-loops-and-game-design]]** Support both WASD and arrow keys for movement, and avoid requiring simultaneous key presses or hard-to-reach keys like F-keys.
- [39:39](https://youtu.be/K1pEI6LVJJA?t=2379) **[[core-loops-and-game-design]]** Avoid designs requiring simultaneous move and shoot or fast precise inputs; test with abled and disabled players because a build system can work for one and fail for the other.
- [44:26](https://youtu.be/K1pEI6LVJJA?t=2666) **[[core-loops-and-game-design]]** Enable keyboard UI navigation and test it; ensure every modal has a clear close action and menu actions have keybinds.
- [40:21](https://youtu.be/K1pEI6LVJJA?t=2421) **[[core-loops-and-game-design]]** Make buttons larger and controls simple so players with motor or precision difficulties can play at their own pace without feeling rushed.
- [46:13](https://youtu.be/K1pEI6LVJJA?t=2773) **[[first-session-onboarding]]** Put a warning for flashing lights or fast motion in the game description and before any triggering section, so players can step away.
- [49:37](https://youtu.be/K1pEI6LVJJA?t=2977) **[[common-mistakes]]** Avoid flashing lights, especially red, and large screen-filling flashes; avoid autoplay trailers with fast flashing content that users cannot turn off.
- [52:23](https://youtu.be/K1pEI6LVJJA?t=3143) **[[core-loops-and-game-design]]** Limit camera shake and provide a disable option or intensity slider, since strong shake makes the game hard to see for everyone.
- [55:19](https://youtu.be/K1pEI6LVJJA?t=3319) **[[first-session-onboarding]]** Add repeatable tutorials and on-screen markers (e.g. arrows) for first-time players; they help learning-disabled players practice in a safe space.
- [58:42](https://youtu.be/K1pEI6LVJJA?t=3522) **[[first-session-onboarding]]** Even in hard games like roguelikes, include a small tutorial explaining controls and items; offer skippable tutorials for players who prefer to learn alone.
- [1:00:04](https://youtu.be/K1pEI6LVJJA?t=3604) **[[ai-and-tools]]** Use Roblox DevForum to request or upvote accessibility features like a color contrast checker and text-to-speech API.
- [1:00:56](https://youtu.be/K1pEI6LVJJA?t=3656) **[[community-and-discord]]** Listen to disabled players when they report issues and avoid dismissing their feedback as skill issues; respond constructively.
- [38:00](https://youtu.be/K1pEI6LVJJA?t=2280) **[[building-art-and-assets]]** Include in-game settings for volume, camera shake and controls; the Split game by EgoMoose and Minecraft accessibility settings are examples.
- [21:52](https://youtu.be/K1pEI6LVJJA?t=1312) **[[building-art-and-assets]]** Make visual and audio options customizable across the board, as Minecraft does, to inspire your own accessibility settings.
- [1:02:17](https://youtu.be/K1pEI6LVJJA?t=3737) **[[community-and-discord]]** Acknowledge accessibility mistakes openly and keep improving; accessibility is an ongoing process rather than a one-time checklist.

## Numbers
- [14:00](https://youtu.be/K1pEI6LVJJA?t=840) Accessibility goal: **Make games usable by everyone; accessibility features help all players, not only disabled ones** (Andrea's framing, comparing to curb ramps)
- [26:50](https://youtu.be/K1pEI6LVJJA?t=1610) WCAG contrast guidance: **Contrast ratio values depend on font size; larger/bolder text allows lower contrast** (Based on WCAG web guidelines applied to game UI)
- [23:57](https://youtu.be/K1pEI6LVJJA?t=1437) Dyslexia-friendly fonts: **Comic Sans and OpenDyslexic cited; serif fonts harder for some** (Panelist opinion, not formal research)

## Games
- **Angel Sensory Room** [10:45](https://youtu.be/K1pEI6LVJJA?t=645): Uses a visible epilepsy/flashing-light warning in the game description so players can decide before entering.
- **Holiday Frenzy** [5:16](https://youtu.be/K1pEI6LVJJA?t=316): Uses sound groups with volume sliders, keybind settings, depth-of-field toggle and on-screen arrow markers for first-time players.
- **Super Doomspire** [32:59](https://youtu.be/K1pEI6LVJJA?t=1979): Adds team symbols so team identity is not conveyed by color alone.
- **Split (EgoMoose)** [38:00](https://youtu.be/K1pEI6LVJJA?t=2280): Puzzle game cited for solid accessibility settings.
- **3008** [52:23](https://youtu.be/K1pEI6LVJJA?t=3143): Allows camera shake to be disabled.
- **Minecraft** [21:11](https://youtu.be/K1pEI6LVJJA?t=1271): Highly customizable accessibility settings and light-on-dark text style.
- **Overwatch** [33:42](https://youtu.be/K1pEI6LVJJA?t=2022): Colorblind mode swaps one color for another so enemy outlines stay visible.
- **Splatoon** [20:28](https://youtu.be/K1pEI6LVJJA?t=1228): Color lock option for colorblind players.

## Tools
Roblox Sound Groups, Roblox controller/keyboard UI navigation keybind, Game Accessibility Guidelines website, Adobe Color contrast picker, WCAG guidelines

## He points to
- Game Accessibility Guidelines (gameaccessibilityguidelines.com)
- Adobe Color contrast picker
- WCAG web accessibility guidelines
- Roblox DevForum accessibility feature requests
- Roblox Accessibility & Localization Bootcamp

## Quotes
- [1:00:04](https://youtu.be/K1pEI6LVJJA?t=3604) "Please use the DevForum to either show your support for feature requests related to accessibility or make those requests directly."
- [29:34](https://youtu.be/K1pEI6LVJJA?t=1774) "If you set everything to a grayscale... if you can't tell the difference from the monochrome, a colorblind person can't."
- [41:43](https://youtu.be/K1pEI6LVJJA?t=2503) "Open it up, allow people to customize it because everyone comes in with whatever disability they have."

## Topics
[[ai-and-tools]] [[building-art-and-assets]] [[common-mistakes]] [[community-and-discord]] [[core-loops-and-game-design]] [[first-session-onboarding]] [[playtesting-and-feedback]] [[thumbnails-icons]]

Back to [[RobloxCreators - How to make successful Roblox games]]
