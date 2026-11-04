---
name: Admin
type: system
what: Permission-checked admin commands (owners table and/or group ranks), typed argument parsing, rank hierarchy, rate limit, audit log; silent to non-admins.
tags: admin, moderation, commands, kick, permissions, group rank, audit
tested: unit-tested headless (Lune) + analyzed + linted; NOT tested in live Studio
---
# Admin

**What:** server-authoritative admin commands. The client only ever sends text; the server decides who may run what.
**Not tested in live Studio** (parsing, ranks, hierarchy, rate limit and audit are tested; the chat/remote glue is only type-checked).

## Files
`src/Admin.luau` (pure), `src/AdminService.luau` (remotes `AdminCommand` / `AdminReply`, TextChatService hook, built-ins `help`, `kick`, `announce`), `tests/Admin.test.luau`.

## Setup
```lua
AdminService.Start({
	owners = { [123456789] = 3 },
	group = { id = 1234567, rankToAdmin = { [255] = 3, [200] = 2 } },
	extraCommands = {
		give = { minRank = 3, args = { { name = "target", kind = "player" }, { name = "amount", kind = "number", min = 1, max = 100000 } },
			run = function(actor, a) return "Gave." end },
	},
})
```
`owners` maps your UserId to an admin rank (3 here); the optional `group` gives group rank >= each key that admin rank.
Type `/kick name reason` in chat (admins only; the message is hidden from others) or fire `ReplicatedStorage.AdminCommand` from your own panel; replies arrive on `AdminReply`.

## Design rules (each has a test)
- Rank 0 (everyone else) gets no reply, so commands are not discoverable and cannot be probed.
- `minRank` per command; a `player` argument must have a LOWER rank than the actor (you can always target yourself) unless `outranks = false`.
- Arguments: `player` (exact name beats prefix; several matches = error), `number` (finite, min/max), `string`, `rest` (length-limited). Input over 300 chars is ignored.
- 10 commands per 10 s per admin; a command that errors is contained and audited.
- Every attempt by an admin, allowed or refused, goes to `audit` (the glue prints `[AdminAudit] ...`; pipe it to a DataStore/webhook if you need history).

## Pitfalls
- Keep `owners` and group ids in server code. Never gate anything on a client-side `IsAdmin` flag.
- Group admins gain rank when they join; ranks are read once per join (restart/rejoin to refresh).
- Commands that change data must go through your data module (PlayerData), not directly on player objects, so they persist.
- Add commands only for things you will really use; each one is attack surface.
- `ShouldDeliverCallback` hides admin text from chat only on the default TextChatService setup. With a custom chat, call the `AdminCommand` remote instead.

## Tests (2026-11-01)
```
cd <claude-kit>/systems && python check.py Admin
  stylua ok | selene ok | analyze ok (0 errors, 0 warnings) | lune Admin.test.luau: 12 passed, 0 failed
```

## Sources
Roblox docs: TextChannel.ShouldDeliverCallback, GroupService:GetGroupsAsync, RemoteEvent security notes (create.roblox.com/docs/scripting/security/security-tactics); KB: `rbx-remote-sec` skill.
