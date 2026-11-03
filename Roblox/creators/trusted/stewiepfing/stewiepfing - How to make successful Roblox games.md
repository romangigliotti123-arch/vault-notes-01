---
title: stewiepfing - How to make successful Roblox games
tags: [roblox, stewiepfing, playbook]
videos: 5
generated: 2026-10-29
credibility: trusted
credibility_score: 7.7
creator_trust: TRUSTED
creator_score: 7.7
---

> [!note] Trust: TRUSTED (credibility audit score 7.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# stewiepfing - How to make successful Roblox games

Build a simulator with a simple, rewarding core and deeper systems left for players to discover. Pair frequent small goals with optional big ones, reward playtime, and anchor pricing with an expensive gamepass shown on join. Put satisfying feedback (orb pops, sounds, checkmarks, particles) on every achievement. Polish for mobile with viewport-scaled strokes, aspect-ratio constraints, haptics, and compact numbers. Prompt for favorites only after several minutes of play, never on join.

**Style:** Practical, tutorial-first Roblox Studio creator who mixes short design takeaways with code walkthroughs and downloadable models. Uses Pet Simulator X/99 and Adopt Me as reference points. Suits developers building simulators or clicker-style games who want copy-ready polish code and simple monetisation and retention ideas.

## Playbook
1. **Pick a simple core with hidden depth** [[core-loops-and-game-design]]: Keep the core loop easy for young players, and leave deeper mechanics for players to find and research, which signals investment. Plan replayability early: multiple worlds, many pets and currencies to unlock, and varied content like new opponents or multiple endings. (v8tFfBTr6M8)
2. **Layer small and big goals** [[core-loops-and-game-design]]: Pair short, frequent goals (next egg, currency threshold) with big optional goals (huge pet, leaderboard rank, completing the game). Frequent small wins keep sessions moving, and big goals give long-term reasons to return. (v8tFfBTr6M8)
3. **Add playtime rewards** [[retention-d1-d7]]: Offer a gift claimable every 5 minutes of play, growing in value over time, to give players a reason to stay longer in each session. The creator used this in his own gift-reward system. (v8tFfBTr6M8)
4. **Anchor pricing with an expensive gamepass** [[pricing]]: Show a very expensive gamepass (example: 900 Robux) as soon as players join. Cheaper items at 100-200 Robux then look like good deals by comparison. Adopt Me is the cited example. (v8tFfBTr6M8)
5. **Build popup orbs on the client** [[scripting-and-performance]]: Spawn currency orbs in a LocalScript so only the player sees them. Launch each with a LinearVelocity at random X/Z force, stagger spawns with task.wait(0.15), and run each orb in its own task.spawn. Destroy the force after about 2 seconds. (qMdRT1xf9GM)
6. **Make feedback loud on every win** [[core-loops-and-game-design]]: Pair each achievement with a sound, a checkmark, or a particle burst. The creator frames these small dopamine hits as the reason players keep playing. Apply the same rule to pickups and milestones. (v8tFfBTr6M8)
7. **Use custom art and proportional UI** [[building-art-and-assets]]: Make your own currency icon instead of default toolbox icons. Add UIAspectRatioConstraint to frames and images so shapes keep their proportions on phone, tablet, and PC. (e48wgHQll2Y, THpSS73tveg)
8. **Scale UI strokes to screen height** [[scripting-and-performance]]: Store stroke thickness at a 1080p baseline, then set thickness = viewportSize.Y × (originalThickness / 1080) so borders look the same on small and large screens. Use observe-pattern modules to update on resize. (e48wgHQll2Y)
9. **Add haptic rumble, using HapticEffect** [[playtesting-and-feedback]]: Use timed rumble (example: amount 2, duration 5 s) for fixed effects and start/stop rumble for open-ended systems. The 2025 video says HapticService is deprecated, so write new rumble code with HapticEffect. (e48wgHQll2Y)
10. **Format large numbers for display** [[scripting-and-performance]]: Compact numbers of 5,000 and above (e.g. 5k, 1k) into K/M/B or comma form. Format inside the display module, not before sending, because arithmetic on an already-formatted string fails. (THpSS73tveg)
11. **Store pet info as data with add-on fallbacks** [[building-art-and-assets]]: Keep pet data in a table with name, rarity, add-on, and generic keys. The hover frame checks for add-on keys and falls back to generic text. Pair with a click ripple tween on input for responsiveness. (THpSS73tveg, qMdRT1xf9GM)
12. **Delay the favorite prompt until after play** [[social-features-and-virality]]: Call AvatarEditorService:PromptSetFavorite from a LocalScript after a RunService timer. Use the place ID, not the universe ID. The creator's stated range is 2 to 5 minutes (300 s), shorter for weaker retention. (OLrTDcjYWGw)
13. **Tune prompt timing from retention data** [[analytics-metrics]]: Check your retention numbers before choosing the favorite prompt delay. The creator says to prompt sooner when retention is weaker, and to wait longer for stronger games. Recheck after each update. (OLrTDcjYWGw)
14. **Keep adding content after launch** [[updates-live-ops]]: Use live updates to add worlds, pets, currencies, and varied content, which the creator links to replayability. Avoid stacking more onto the core loop without new goals to pair with it. (v8tFfBTr6M8)

## Key numbers
- Playtime gift interval: every 5 minutes (v8tFfBTr6M8)
- Anchor gamepass shown on join: 900 Robux vs 100-200 Robux items (v8tFfBTr6M8)
- Orb stagger wait: 0.15 s between orbs (qMdRT1xf9GM)
- Force removal wait: about 2 s before destroying attachment/LinearVelocity (qMdRT1xf9GM)
- Random X/Z force: -10 to 10 final, -55 to 55 initial, LinearVelocity Max Force 250 (qMdRT1xf9GM)
- Orb test counts: 3 then 5 in 2024, with a crash warning for high counts (qMdRT1xf9GM)
- 2025 orb demo: 5 orbs at 0.5 s, then 15 orbs at 1 s (THpSS73tveg)
- Popup test: 5 pops of random 0-100 with 6 s wait, then reset (THpSS73tveg)
- Orb random offset range: -3 to 20 (THpSS73tveg)
- Favorite prompt delay: 2 to 5 minutes (300 s) stated; 5 to 10 minutes used as example (OLrTDcjYWGw)
- Compact number threshold: 5,000 and above (THpSS73tveg)
- Stroke scaling: thickness = viewport Y × (original / 1080) (e48wgHQll2Y)
- Haptic example: amount 2, duration 5 s; start/stop example at 3 s (e48wgHQll2Y)

## Common mistakes
- Prompting for favorites on join, before new players have seen the game (OLrTDcjYWGw)
- Using the universe ID instead of the place ID for favorite prompts (OLrTDcjYWGw)
- Spawning too many orbs at once, which can crash the game; stagger and keep counts modest (qMdRT1xf9GM)
- Leaving collected orbs collidable, so players can get stuck touching them (core notes)
- Formatting numbers before sending them, then doing arithmetic on the string (THpSS73tveg)
- Requiring modules in replicated scripts without WaitForChild, so code errors on load (core notes)
- Using default toolbox currency icons instead of custom art (core notes)
- Building gradients without a transparency sequence or without ending on the starting color (THpSS73tveg)
- Using HapticService in new code instead of HapticEffect (e48wgHQll2Y)
- Showing cheap gamepasses with no expensive anchor, so they don't look like deals (v8tFfBTr6M8)

## Launch checklist
- [ ] Confirm the place ID (not universe ID) for the favorite prompt, from Asset Manager or the creations URL (OLrTDcjYWGw)
- [ ] Remove any favorite prompt from the join flow; use a RunService timer instead (OLrTDcjYWGw)
- [ ] Set the favorite prompt delay in the 2-5 minute range, adjusted for retention (OLrTDcjYWGw)
- [ ] Replace default currency icons with a custom icon (core notes)
- [ ] Add UIAspectRatioConstraint to frames and images (e48wgHQll2Y)
- [ ] Test UI on phone, tablet, and PC resolutions (e48wgHQll2Y)
- [ ] Scale UI strokes to viewport height with the 1080p baseline formula (e48wgHQll2Y)
- [ ] Add haptic rumble for mobile and console players, using HapticEffect (e48wgHQll2Y)
- [ ] Add a click ripple tween on mouse, touch, and controller R2 (core notes)
- [ ] Format numbers from 5,000 upward inside the display module (THpSS73tveg)
- [ ] Set the playtime gift timer to 5 minutes and check the reward grows (v8tFfBTr6M8)
- [ ] Show the 900 Robux anchor gamepass on join (v8tFfBTr6M8)
- [ ] Make collected orbs non-collidable and anchored after they settle (core notes)
- [ ] Wrap replicated module requires in WaitForChild (core notes)
- [ ] Test orb counts on a low-end device before shipping (qMdRT1xf9GM)

## How the advice changed over time
- Orb effect style changed: the 2024 tutorial (qMdRT1xf9GM) used LinearVelocity physics bursts, while the 2025 video (THpSS73tveg) uses clamped-time bezier curves that fly orbs to the character. Prefer the bezier approach for new builds.
- Haptics: the 2025 video (e48wgHQll2Y) says HapticService is deprecated in favour of HapticEffect. Use HapticEffect for new code and treat older HapticService advice as outdated.
- Favorite prompt timing: the 2024 video's example used 5 to 10 minutes, but its stated suggested range is 2 to 5 minutes (300 s). The stated range is the more specific guidance.
- Orb count caution: the 2024 video warned that high counts may crash, yet the 2025 demo runs 15 orbs at 1 s. Treat the 2025 demo as a showcase, not a performance guarantee, and test on your own target devices.

## Theme notes
- [[stewiepfing - Retention|Retention]]
- [[stewiepfing - Monetisation|Monetisation]]
- [[stewiepfing - Discovery & Algorithm|Discovery & Algorithm]]
- [[stewiepfing - Game Ideas|Game Ideas]]
- [[stewiepfing - Studio & Scripting|Studio & Scripting]]
- [[stewiepfing - Mindset & Process|Mindset & Process]]
- [[stewiepfing - Games Mentioned]]
- [[stewiepfing - Numbers & Benchmarks]]
- [[stewiepfing - Tools & Resources]]
- Cross-creator knowledge base: [[README]]

## All videos (oldest first)
- [[2024-02-16 - The SECRET To Successful Simulators Roblox Studio|The SECRET To Successful Simulators | Roblox Studi]] (639 views, 2024-02-16): Six simulator ideas: playtime rewards, anchor pricing, discoverability, goal layering, feedback, and replayability.
- [[2024-04-23 - Making Your Game More Satisfying Roblox Studio|Making Your Game More Satisfying | Roblox Studio]] (5,830 views, 2024-04-23): Client-side currency orb popups using LinearVelocity bursts, staggered spawns, and tunable force ranges in Studio.
- [[2024-08-07 - Getting More Favorites On Your Roblox Game (Potentially) Roblox Studio|Getting More Favorites On Your Roblox Game (Potent]] (6,208 views, 2024-08-07): Prompt favorites mid-session with AvatarEditorService and a timer, using the place ID, not on join.
- [[2025-04-27 - Simple Things Mobile Players LOVE! Roblox Studio|Simple Things Mobile Players LOVE! | Roblox Studio]] (12,531 views, 2025-04-27): Mobile polish in Luau: viewport-scaled strokes, aspect ratio constraints, haptic rumble, and click ripples.
- [[2025-08-10 - Must-Have Features For YOUR Simulator Game! Roblox Studio|Must-Have Features For YOUR Simulator Game! | Robl]] (16,042 views, 2025-08-10): Simulator polish code: pet hover info, stacking popups, compact numbers, animated gradients, and bezier orb flights.
