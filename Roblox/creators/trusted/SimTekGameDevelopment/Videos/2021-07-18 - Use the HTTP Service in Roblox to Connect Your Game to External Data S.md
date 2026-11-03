---
title: "Use the HTTP Service in Roblox to Connect Your Game to External Data Sources"
url: https://youtu.be/NsnoDX2dEY8
creator: SimTek Game Development
official: false
advice_density: low
date: 2021-07-18
views: 11575
transcript: auto-captions
confidence: high
tags: [roblox, simtekgamedevelopment, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.2
---

> [!note] Trust: TRUSTED (credibility audit score 8.2): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Use the HTTP Service in Roblox to Connect Your Game to External Data Sources

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/NsnoDX2dEY8) | SimTekGameDevelopment | 11,575 views | 2021-07-18

## Summary
Tutorial on making HTTP requests from a Roblox game to an external API (free cat-fact API) using HttpService. Covers enabling HTTP requests in game security, a server script calling GetAsync and JSONDecode, a RemoteEvent to pass the fact to a client LocalScript, and displaying it in a TextLabel.

## Tips
- [0:49](https://youtu.be/NsnoDX2dEY8?t=49) **[[scripting-and-performance]]** Make HTTP calls from a server Script, not a LocalScript; HttpService requests only run on the server, so pass results to clients via a RemoteEvent.
- [0:18](https://youtu.be/NsnoDX2dEY8?t=18) **[[scripting-and-performance]]** Enable 'Allow HTTP Requests' under game Settings > Security before using HttpService, or requests will fail.
- [6:11](https://youtu.be/NsnoDX2dEY8?t=371) **[[client-server-and-remotes]]** Use a RemoteEvent in ReplicatedStorage as the doorway between server and client; match the name exactly to avoid infinite yield errors on WaitForChild.
- [6:46](https://youtu.be/NsnoDX2dEY8?t=406) **[[scripting-and-performance]]** Print the decoded HTTP response and inspect it before parsing; API payloads often nest fields (e.g. fact and length) you must index explicitly.

## Numbers
- [6:46](https://youtu.be/NsnoDX2dEY8?t=406) Response payload: **JSON with fact string and length field** (Cat fact API response shape observed in the print output)

## Tools
HttpService, RemoteEvent, TextLabel, LocalScript

## Topics
[[client-server-and-remotes]] [[scripting-and-performance]]

Back to [[SimTekGameDevelopment - How to make successful Roblox games]]
