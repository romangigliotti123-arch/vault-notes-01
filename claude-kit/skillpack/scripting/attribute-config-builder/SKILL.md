---
name: attribute-config-builder
description: "Put a system's tunable numbers in typed, validated Attributes on one Instance so designers can tweak them live in the Properties panel and code reacts, with clamping, reverts for bad values and change hooks. Use for boss stats, spawn rates, event settings and anything balanced by playtest."
category: scripting
tags: attributes, config, tuning, balance, setattribute, getattributechangedsignal, live tweak, designer, configuration, luau
kb: Roblox/roblox-kb/scripting-and-performance.md, Roblox/roblox-kb/client-server-and-remotes.md, Roblox/roblox-kb/anti-exploit-and-security.md
related: datastore-schema-builder, event-bus-builder, collection-tag-wiring, price-ladder-planner, rbx-leaderboard
---

# attribute-config-builder

Balance numbers buried in code get changed by editing and republishing. Attributes on one Instance can be edited in Studio, read in code, and watched for changes. `scripts/AttributeConfig.luau` adds the part Roblox does not: types, ranges, defaults and a revert when a value is nonsense.

## When to use
A system has five to thirty tunables and the design is still moving (spawn interval, boss health, event length). Not for: secrets or anything the client must not see (attributes replicate), large data tables (use a ModuleScript or a data file), or values that must survive a server restart (that is saved data, see `datastore-schema-builder`).

## Inputs (max 2)
1. The tunables (name, type, default, min, max, allowed values). 2. Which Instance holds them (default a `Configuration` named after the system, in ServerStorage if clients should not read it, ReplicatedStorage if they should).

## Procedure
1. Write the schema: `{ Health = { kind = "number", default = 500, min = 1, max = 10000 }, Phase = { kind = "string", default = "one", allowed = { "one", "two" } } }`. Names in constants (a typo in `GetAttribute("Healht")` silently reads nil). Keep within the engine limits: the vault lists 64 replicated attributes per instance and 50 characters for names and string values.
2. `AttributeConfig.validateSchema(schema)` returns problems (unknown kind, min above max, a default that breaks its own rules). `bind` refuses a bad schema, so mistakes fail at startup.
3. `local cfg = AttributeConfig.bind(configInstance, schema, function(name, new, old) ... end)`. It writes defaults for missing attributes, repairs invalid starting values, and listens: an out-of-range edit is clamped, a wrong-type, NaN or disallowed edit is reverted to the last good value, and only valid changes call your hook.
4. Read through `cfg:Get("Health")` (the last accepted value), not by re-reading the attribute at every use. Change values in code with `cfg:Set(...)` so the same rules apply.
5. Authority: gameplay numbers are read and enforced on the server from the server's copy. A client can change its local copy of a replicated attribute and nothing else, so never base rewards or damage on a client-readable value the client can edit; keep the config in ServerStorage or read only on the server.
6. For live-ops, drive the same schema from a remote-config source (see the vault's ConfigService notes) on the server and `Set` the values; designers can still hand-edit in Studio during development.
7. On shutdown or when the system is destroyed call `cfg:Destroy()` to disconnect.
8. Test: `lune run ../skillpack/scripting/attribute-config-builder/scripts/tests/AttributeConfig.test.luau` from the kit `systems` folder (fake instance: defaults, clamp, revert, NaN, hooks).

## Studio MCP path
`list_roblox_studios` -> `inspect_instance` on the config object -> `multi_edit` to add the bind script -> `start_stop_play` -> `execute_luau` (Server) setting an attribute to an invalid value and reading it back -> `get_console_output`.

## Fallback
Files and the Lune test; engine replication behaviour is `untested` without a running place.

## Evidence
`Roblox/roblox-kb/scripting-and-performance.md`: use `GetAttribute`/`SetAttribute` (not properties); store names in constants because a typo creates a new attribute; setting nil deletes; react with `GetAttributeChangedSignal`; prefer few JSON-encoded attributes over hundreds for bulk data; official limits 64 replicated attributes, 50-character names and string values (Creator Docs); ConfigService is server-only, wrap in pcall with fallbacks. `Roblox/roblox-kb/anti-exploit-and-security.md`: the client is untrusted.

## Output
`AttributeConfig.luau`, the schema file for the system, the list of hooks, test result.

## Acceptance checks
- [ ] Executed: Lune test quoted (`8 passed, 0 failed`).
- [ ] Every tunable has a type, default and range; `validateSchema` is empty for the real schema.
- [ ] Server logic reads server-side values only.
- [ ] Attribute count and name/string lengths are within the limits.
- [ ] Hooks do not assume the value changed on the client.

## Pitfalls
Using attributes for large or secret data. Reading `GetAttribute` in a hot loop instead of caching. Forgetting that setting an attribute to the value it already has fires nothing. Letting designers set values the code cannot handle (hence the ranges). Storing Instances or tables (not supported types).

## Related
`datastore-schema-builder`, `event-bus-builder`, `collection-tag-wiring`, `rbx-leaderboard`.
