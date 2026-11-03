---
title: "How to save parts, and the idea of Serialization"
url: https://devforum.roblox.com/t/how-to-save-parts-and-the-idea-of-serialization/524311
creator: Roblox DevForum
official: false
advice_density: medium
date: 2020-04-14
views: 591
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# How to save parts, and the idea of Serialization

[Open](https://devforum.roblox.com/t/how-to-save-parts-and-the-idea-of-serialization/524311) | Roblox DevForum | 591 views | 2020-04-14

## Summary
Tutorial on saving Roblox instances with DataStore by serializing them into dictionaries/tables. Covers serializing properties (BrickColor, CFrame, Vector3, Color3, Enums), recursive handling of Children, the Encode/Decode module, deserializing via property names, and a tip to store only Vector3 positions for grid-based building games.

## Tips
- [page](https://devforum.roblox.com/t/how-to-save-parts-and-the-idea-of-serialization/524311) **[[data-persistence]]** DataStore cannot save Instances or userdata (Vector3, CFrame, Color3, BrickColor, Enum). Convert them to plain tables/strings/numbers before SetAsync.
- [page](https://devforum.roblox.com/t/how-to-save-parts-and-the-idea-of-serialization/524311) **[[data-persistence]]** Serialize instances as dictionaries keyed by property name, grouped by ClassName, with a Children key for nested descendants.
- [page](https://devforum.roblox.com/t/how-to-save-parts-and-the-idea-of-serialization/524311) **[[data-persistence]]** Keep a per-class whitelist of properties to save rather than dumping all properties; the list is editable for each class you need.
- [page](https://devforum.roblox.com/t/how-to-save-parts-and-the-idea-of-serialization/524311) **[[data-persistence]]** Do not manually JSONEncode before saving; DataStore encodes to JSON internally, and pre-encoding causes objects to be saved as null.
- [page](https://devforum.roblox.com/t/how-to-save-parts-and-the-idea-of-serialization/524311) **[[data-persistence]]** Deserialize by property name, not value type, since a string value could be a BrickColor, Enum part, or plain Name.
- [page](https://devforum.roblox.com/t/how-to-save-parts-and-the-idea-of-serialization/524311) **[[data-persistence]]** For building games with few repeated block types, save a table per block name containing only Vector3 positions and :Clone() preset parts from ServerStorage/ReplicatedStorage on load; this is lighter than full property saves.
- [page](https://devforum.roblox.com/t/how-to-save-parts-and-the-idea-of-serialization/524311) **[[client-server-and-remotes]]** Instances cannot be sent over RemoteEvents either; serialize them into tables before network transfer.
- [page](https://devforum.roblox.com/t/how-to-save-parts-and-the-idea-of-serialization/524311) **[[luau-language-and-types]]** Use Color3:ToHSV() and Color3.fromHSV(unpack(t)) for compact Color3 serialization; CFrame:GetComponents() with CFrame.new(unpack(t)) is a shorter CFrame alternative.

## Tools
DataStoreService, HttpService:JSONEncode, Roblox Studio

## He points to
- Crazyman32 serializer module (linked by author)
- serializer_place.rbxl demo place (author attachment)

## Topics
[[client-server-and-remotes]] [[data-persistence]] [[luau-language-and-types]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
