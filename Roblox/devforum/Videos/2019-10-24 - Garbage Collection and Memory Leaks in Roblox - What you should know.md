---
title: "Garbage Collection and Memory Leaks in Roblox - What you should know"
url: https://devforum.roblox.com/t/garbage-collection-and-memory-leaks-in-roblox-what-you-should-know/374954
creator: Roblox DevForum
official: false
advice_density: medium
date: 2019-10-24
views: 492
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Garbage Collection and Memory Leaks in Roblox - What you should know

[Open](https://devforum.roblox.com/t/garbage-collection-and-memory-leaks-in-roblox-what-you-should-know/374954) | Roblox DevForum | 492 views | 2019-10-24

## Summary
Hexcede's guide to Roblox Luau garbage collection and memory leaks. Covers GC being uncontrollable (no forced collect, collectgarbage("count") works), weak tables via __mode, closures holding strong references to upvalues, connections and callbacks as leak sources, do-blocks for scoping, and how to test for leaks with weak references.

## Tips
- [page](https://devforum.roblox.com/t/garbage-collection-and-memory-leaks-in-roblox-what-you-should-know/374954) **[[scripting-and-performance]]** Disconnect event connections and destroy instances when done; a connected function keeps every upvalue it references alive indefinitely.
- [page](https://devforum.roblox.com/t/garbage-collection-and-memory-leaks-in-roblox-what-you-should-know/374954) **[[scripting-and-performance]]** Set local variables to nil when finished with them; a referenced table is never collected while any strong reference remains.
- [page](https://devforum.roblox.com/t/garbage-collection-and-memory-leaks-in-roblox-what-you-should-know/374954) **[[scripting-and-performance]]** Wrap temporary values in do blocks so they go out of scope and become collectable without waiting for the thread to end.
- [page](https://devforum.roblox.com/t/garbage-collection-and-memory-leaks-in-roblox-what-you-should-know/374954) **[[scripting-and-performance]]** Use setmetatable with __mode set to "k", "v", or "kv" for caches so entries can be garbage collected automatically.
- [page](https://devforum.roblox.com/t/garbage-collection-and-memory-leaks-in-roblox-what-you-should-know/374954) **[[scripting-and-performance]]** Clear or weak-reference tables you still hold but no longer use; a table keeps its values alive until the table itself is collected.
- [page](https://devforum.roblox.com/t/garbage-collection-and-memory-leaks-in-roblox-what-you-should-know/374954) **[[scripting-and-performance]]** Clean up callbacks like Bindable/RemoteFunction OnInvoke handlers, since they hold references to captured variables just like connections.
- [page](https://devforum.roblox.com/t/garbage-collection-and-memory-leaks-in-roblox-what-you-should-know/374954) **[[scripting-and-performance]]** Clean up never-ending threads (e.g. coroutine.yield loops) by scoping temporaries in do blocks or clearing them, because such threads never collect their root values.
- [page](https://devforum.roblox.com/t/garbage-collection-and-memory-leaks-in-roblox-what-you-should-know/374954) **[[testing-debugging-and-qa]]** Detect leaks by storing a value in a weak table (setmetatable({v}, {__mode="v"})) and checking whether ref[1] becomes nil after collection.
- [page](https://devforum.roblox.com/t/garbage-collection-and-memory-leaks-in-roblox-what-you-should-know/374954) **[[optimization-and-streaming]]** Use collectgarbage("count") to read Luau memory in KB (multiply by 1024 for bytes); forced collection is not available on Roblox.
- [page](https://devforum.roblox.com/t/garbage-collection-and-memory-leaks-in-roblox-what-you-should-know/374954) **[[common-mistakes]]** Do not call collectgarbage("collect") in Roblox; it errors, and GC timing is unpredictable and undocumented, so memory cannot be freed on demand.
- [page](https://devforum.roblox.com/t/garbage-collection-and-memory-leaks-in-roblox-what-you-should-know/374954) **[[common-mistakes]]** Do not assume a root script environment will be collected; the author could not force it, though it collects when all threads referencing it are yielding or dead with no references to yielding threads.
- [page](https://devforum.roblox.com/t/garbage-collection-and-memory-leaks-in-roblox-what-you-should-know/374954) **[[common-mistakes]]** Remember numbers are never garbage collected and strings in your script keep their copies alive; these are not reliable leak sources to chase.

## Numbers
- [page](https://devforum.roblox.com/t/garbage-collection-and-memory-leaks-in-roblox-what-you-should-know/374954) Memory unit: **collectgarbage("count") returns KB; multiply by 1024 for bytes** (Only memory-reporting call usable in Roblox Lua)
- [page](https://devforum.roblox.com/t/garbage-collection-and-memory-leaks-in-roblox-what-you-should-know/374954) Test delay: **delay(1.5) used to allow GC to run in weak-table example** (Author's example wait before checking weak references)

## Tools
collectgarbage (count only), setmetatable with __mode, do blocks for scoping

## Quotes
- [page](https://devforum.roblox.com/t/garbage-collection-and-memory-leaks-in-roblox-what-you-should-know/374954) "Unlike in vanilla lua, it is impossible to force a garbage collection."
- [page](https://devforum.roblox.com/t/garbage-collection-and-memory-leaks-in-roblox-what-you-should-know/374954) "When a function references a variable from an outside scope it holds a strong reference to that value!"

## Topics
[[common-mistakes]] [[optimization-and-streaming]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
