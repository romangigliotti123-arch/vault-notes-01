---
title: "Reference Instances Directly with Attributes"
url: https://devforum.roblox.com/t/reference-instances-directly-with-attributes/4753441
creator: Roblox DevForum
official: false
advice_density: medium
date: 2026-07-23
views: 1198
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Reference Instances Directly with Attributes

[Open](https://devforum.roblox.com/t/reference-instances-directly-with-attributes/4753441) | Roblox DevForum | 1,198 views | 2026-07-23

## Summary
Roblox DevForum/docs announcement: InstanceHandle and Instance attributes are now available in production. Attributes can store Instance references directly (no ObjectValue needed). GetAttribute returns an InstanceHandle; Get() returns the Instance or nil, Wait(timeout) yields until it streams in. Handles also work over RemoteEvents.

## Tips
- [page](https://devforum.roblox.com/t/reference-instances-directly-with-attributes/4753441) **[[scripting-and-performance]]** Replace ObjectValue children with attributes that hold Instance references directly via SetAttribute(name, instance), removing extra instances to manage.
- [page](https://devforum.roblox.com/t/reference-instances-directly-with-attributes/4753441) **[[client-server-and-remotes]]** Use InstanceHandle when the server sends a reference to an Instance the client may not have streamed yet; the client calls handle:Wait() to receive it.
- [page](https://devforum.roblox.com/t/reference-instances-directly-with-attributes/4753441) **[[optimization-and-streaming]]** Use handle:Get() for a non-yielding check and handle:Wait(timeout) when the target may stream in; Get() returns nil once a target streams out.
- [page](https://devforum.roblox.com/t/reference-instances-directly-with-attributes/4753441) **[[common-mistakes]]** Don't treat a nil GetAttribute result as 'target missing': nil means the attribute doesn't exist; a handle whose Get() returns nil means the target isn't available locally.
- [page](https://devforum.roblox.com/t/reference-instances-directly-with-attributes/4753441) **[[common-mistakes]]** GetAttributeChangedSignal does not fire when the referenced Instance streams in/out or is destroyed; only when the attribute itself is set or deleted.

## Tools
InstanceHandle, Instance:SetAttribute, Instance:GetAttribute, Instance:GetAttributes, Instance:GetAttributeChangedSignal, RemoteEvent

## Topics
[[client-server-and-remotes]] [[common-mistakes]] [[optimization-and-streaming]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
