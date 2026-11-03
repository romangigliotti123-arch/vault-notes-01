---
title: generalistprogrammer3233 - Studio & Scripting
creator: generalistprogrammer3233
tags: [roblox, generalistprogrammer3233, theme]
creator_trust: MIXED
creator_score: 7.1
---

> [!note] Trust: MIXED (credibility audit score 7.1): do not rely on this creator alone; confirm a recommendation with a second source. See [[creator-credibility]].

# generalistprogrammer3233: Studio & Scripting

All generalistprogrammer3233 tips on this theme, grouped by topic, oldest first. Cross-creator synthesis: see [[README]] in roblox-kb.

## [[scripting-and-performance]]
- 2026-07-04 [3:46](https://youtu.be/DirIakVx7eQ?t=226) Give every dropped cash part a lifespan with Debris:AddItem so uncollected drops are deleted and the world does not lag. ([[2026-07-04 - How to Make a Roblox Tycoon (Droppers, Buttons & Cash)|How to Make a Roblox Tycoon (Droppers, Buttons & C]])
- 2026-07-04 [6:41](https://youtu.be/DirIakVx7eQ?t=401) Debounce collector Touched events with an attribute on each part so a drop that fires Touched multiple times is only credited once. ([[2026-07-04 - How to Make a Roblox Tycoon (Droppers, Buttons & Cash)|How to Make a Roblox Tycoon (Droppers, Buttons & C]])
- 2026-07-04 [2:47](https://youtu.be/YMvezOFyl8o?t=167) Enable File > Game Settings > Security > 'Enable Studio Access to API Services' or DataStore saves appear to do nothing in Studio. ([[2026-07-04 - Roblox DataStore Tutorial (Save Player Data the Right Way)|Roblox DataStore Tutorial (Save Player Data the Ri]])
- 2026-07-04 [3:26](https://youtu.be/YMvezOFyl8o?t=206) Wrap every SetAsync/GetAsync in pcall; DataStore calls throw on network or service failures and will halt the script mid-save. ([[2026-07-04 - Roblox DataStore Tutorial (Save Player Data the Right Way)|Roblox DataStore Tutorial (Save Player Data the Ri]])
- 2026-07-04 [4:47](https://youtu.be/YMvezOFyl8o?t=287) Retry failed saves in a loop, about three attempts with a short wait between them; most transient failures clear on the second try. ([[2026-07-04 - Roblox DataStore Tutorial (Save Player Data the Right Way)|Roblox DataStore Tutorial (Save Player Data the Ri]])
- 2026-07-07 [2:42](https://youtu.be/Oj0nbY61qsY?t=162) In a server Script, ClickDetector.MouseClick already gives the player on the server, so earning doesn't need a RemoteEvent. ([[2026-07-07 - How to Make a Roblox Simulator Game (Pets & Rebirths)|How to Make a Roblox Simulator Game (Pets & Rebirt]])

## [[code-architecture-and-frameworks]]
- 2026-07-04 [2:25](https://youtu.be/DirIakVx7eQ?t=145) Run all tycoon logic (cash, purchases, saving) on the server in Script, never LocalScript, so clients cannot grant themselves money. ([[2026-07-04 - How to Make a Roblox Tycoon (Droppers, Buttons & Cash)|How to Make a Roblox Tycoon (Droppers, Buttons & C]])

## [[client-server-and-remotes]]
- 2026-07-04 [2:06](https://youtu.be/YMvezOFyl8o?t=126) Run all DataStore code in a server Script in ServerScriptService, never on the client, since clients cannot be trusted with save data. ([[2026-07-04 - Roblox DataStore Tutorial (Save Player Data the Right Way)|Roblox DataStore Tutorial (Save Player Data the Ri]])
- 2026-07-07 [1:32](https://youtu.be/Oj0nbY61qsY?t=92) Keep all coin changes on the server. Client-controlled currency lets players give themselves unlimited coins. ([[2026-07-07 - How to Make a Roblox Simulator Game (Pets & Rebirths)|How to Make a Roblox Simulator Game (Pets & Rebirt]])
- 2026-07-07 [3:41](https://youtu.be/Oj0nbY61qsY?t=221) Rebirth via RemoteEvent: client only fires the event; server checks the cost, zeroes coins, increments rebirths. ([[2026-07-07 - How to Make a Roblox Simulator Game (Pets & Rebirths)|How to Make a Roblox Simulator Game (Pets & Rebirt]])

## [[data-persistence]]
- 2026-07-04 [9:05](https://youtu.be/DirIakVx7eQ?t=545) Save coins and the list of purchased buttons to a DataStore keyed by UserId; replay purchases on load to rebuild the base. ([[2026-07-04 - How to Make a Roblox Tycoon (Droppers, Buttons & Cash)|How to Make a Roblox Tycoon (Droppers, Buttons & C]])
- 2026-07-04 [9:47](https://youtu.be/DirIakVx7eQ?t=587) Wrap DataStore calls in pcall because cloud calls can fail; an unprotected failure crashes the save. ([[2026-07-04 - How to Make a Roblox Tycoon (Droppers, Buttons & Cash)|How to Make a Roblox Tycoon (Droppers, Buttons & C]])
- 2026-07-04 [10:29](https://youtu.be/DirIakVx7eQ?t=629) Save on PlayerRemoving and also on an autosave timer (about every minute), since PlayerRemoving does not fire on crashes. ([[2026-07-04 - How to Make a Roblox Tycoon (Droppers, Buttons & Cash)|How to Make a Roblox Tycoon (Droppers, Buttons & C]])
- 2026-07-04 [10:41](https://youtu.be/DirIakVx7eQ?t=641) Save all players in BindToClose on server shutdown so players in a closing server do not lose their last minutes. ([[2026-07-04 - How to Make a Roblox Tycoon (Droppers, Buttons & Cash)|How to Make a Roblox Tycoon (Droppers, Buttons & C]])
- 2026-07-04 [5:43](https://youtu.be/YMvezOFyl8o?t=343) If a load fails, do not give the player default values. Kick them or block saving, otherwise the next save overwrites real data with zeros. ([[2026-07-04 - Roblox DataStore Tutorial (Save Player Data the Right Way)|Roblox DataStore Tutorial (Save Player Data the Ri]])
- 2026-07-04 [5:02](https://youtu.be/YMvezOFyl8o?t=302) Load on PlayerAdded using the same key built from UserId, so reads match what was written. ([[2026-07-04 - Roblox DataStore Tutorial (Save Player Data the Right Way)|Roblox DataStore Tutorial (Save Player Data the Ri]])
- 2026-07-04 [6:24](https://youtu.be/YMvezOFyl8o?t=384) Save on three triggers: PlayerRemoving, a task.spawn autosave loop every 60 seconds, and BindToClose. Missing any one leaves a data loss gap. ([[2026-07-04 - Roblox DataStore Tutorial (Save Player Data the Right Way)|Roblox DataStore Tutorial (Save Player Data the Ri]])
- 2026-07-04 [7:04](https://youtu.be/YMvezOFyl8o?t=424) In BindToClose, save all remaining players then task.wait about 3 seconds so the requests reach the cloud before the server shuts down. ([[2026-07-04 - Roblox DataStore Tutorial (Save Player Data the Right Way)|Roblox DataStore Tutorial (Save Player Data the Ri]])
- 2026-07-04 [7:46](https://youtu.be/YMvezOFyl8o?t=466) Respect rate limits (roughly 60 requests/min plus 10 per player). Save on a timer and only when data changed, never per frame or per coin pickup. ([[2026-07-04 - Roblox DataStore Tutorial (Save Player Data the Right Way)|Roblox DataStore Tutorial (Save Player Data the Ri]])
- 2026-07-04 [8:26](https://youtu.be/YMvezOFyl8o?t=506) If you see 'data store request was added to queue', you are saving too often. Reduce save frequency. ([[2026-07-04 - Roblox DataStore Tutorial (Save Player Data the Right Way)|Roblox DataStore Tutorial (Save Player Data the Ri]])
- 2026-07-04 [8:26](https://youtu.be/YMvezOFyl8o?t=506) Prefer UpdateAsync over SetAsync when the same player might be on two servers, since SetAsync blindly overwrites newer saves. ([[2026-07-04 - Roblox DataStore Tutorial (Save Player Data the Right Way)|Roblox DataStore Tutorial (Save Player Data the Ri]])
- 2026-07-04 [9:06](https://youtu.be/YMvezOFyl8o?t=546) Add session locking for a serious game so a second server cannot load a player's data until the first server releases it. UpdateAsync alone does not fully fix duplicate-server bugs. ([[2026-07-04 - Roblox DataStore Tutorial (Save Player Data the Right Way)|Roblox DataStore Tutorial (Save Player Data the Ri]])
- 2026-07-04 [0:43](https://youtu.be/YMvezOFyl8o?t=43) Use one DataStore per game with a key per player (the UserId string) holding a table of their state. Keep the store name permanent. ([[2026-07-04 - Roblox DataStore Tutorial (Save Player Data the Right Way)|Roblox DataStore Tutorial (Save Player Data the Ri]])
- 2026-07-07 [6:03](https://youtu.be/Oj0nbY61qsY?t=363) Save coins, rebirths and pets to a DataStore keyed by UserId on PlayerRemoving, wrapped in pcall, and load on join. ([[2026-07-07 - How to Make a Roblox Simulator Game (Pets & Rebirths)|How to Make a Roblox Simulator Game (Pets & Rebirt]])

## [[building-and-level-design]]
- 2026-07-04 [4:37](https://youtu.be/DirIakVx7eQ?t=277) Use an anchored conveyor part with AssemblyLinearVelocity set along the belt direction to move parts; make belts wider than drops or add lip walls. ([[2026-07-04 - How to Make a Roblox Tycoon (Droppers, Buttons & Cash)|How to Make a Roblox Tycoon (Droppers, Buttons & C]])

## [[ui-ux-design]]
- 2026-07-07 [0:59](https://youtu.be/BJea3LJJWww?t=59) Set ScreenGui ResetOnSpawn to false so the menu is not destroyed and rebuilt on every respawn, which would reset held state. ([[2026-07-07 - Roblox UI Tutorial Clean GUI Menu in Luau|Roblox UI Tutorial: Clean GUI Menu in Luau]])
- 2026-07-07 [2:05](https://youtu.be/BJea3LJJWww?t=125) Use UDim2 with scale for size/position so layouts adapt to phones, tablets and monitors; offset adds fixed pixels on top. ([[2026-07-07 - Roblox UI Tutorial Clean GUI Menu in Luau|Roblox UI Tutorial: Clean GUI Menu in Luau]])
- 2026-07-07 [2:47](https://youtu.be/BJea3LJJWww?t=167) Set AnchorPoint to 0.5,0.5 when centering a frame with position 0.5,0,0.5,0; otherwise the top-left corner lands at center. ([[2026-07-07 - Roblox UI Tutorial Clean GUI Menu in Luau|Roblox UI Tutorial: Clean GUI Menu in Luau]])
- 2026-07-07 [3:40](https://youtu.be/BJea3LJJWww?t=220) Add a UICorner child to frames and buttons (scale 0, offset ~12) to replace dated sharp 90-degree corners with one instance per element. ([[2026-07-07 - Roblox UI Tutorial Clean GUI Menu in Luau|Roblox UI Tutorial: Clean GUI Menu in Luau]])
- 2026-07-07 [4:37](https://youtu.be/BJea3LJJWww?t=277) Enable TextScaled on text labels and buttons so text resizes to its box instead of clipping on small screens. ([[2026-07-07 - Roblox UI Tutorial Clean GUI Menu in Luau|Roblox UI Tutorial: Clean GUI Menu in Luau]])
- 2026-07-07 [5:31](https://youtu.be/BJea3LJJWww?t=331) Connect TextButton.MouseButton1Click for clicks; it fires on both mouse click and phone tap with no extra code. ([[2026-07-07 - Roblox UI Tutorial Clean GUI Menu in Luau|Roblox UI Tutorial: Clean GUI Menu in Luau]])
- 2026-07-07 [6:37](https://youtu.be/BJea3LJJWww?t=397) Use UIListLayout (padding ~8px, horizontal center) instead of hand-placing elements so the column reflows when items are added or removed. ([[2026-07-07 - Roblox UI Tutorial Clean GUI Menu in Luau|Roblox UI Tutorial: Clean GUI Menu in Luau]])
- 2026-07-07 [7:20](https://youtu.be/BJea3LJJWww?t=440) Add UIPadding to keep content off the frame border; roughly 10px top padding gives breathing room. ([[2026-07-07 - Roblox UI Tutorial Clean GUI Menu in Luau|Roblox UI Tutorial: Clean GUI Menu in Luau]])

Up: [[generalistprogrammer3233 - How to make successful Roblox games]]
