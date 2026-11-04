--!nocheck
local t = require("../../_check/harness")
local Admin = require("../src/Admin")

local ranks = { [1] = 3, [2] = 1, [3] = 0, [4] = 3 }
local names = { alice = 1, bob = 2, carol = 3, dave = 4, bobby = 5 }

local function make(over)
	local env = { audit = {}, ran = {}, clock = 100 }
	local cfg = {
		commands = {
			kick = {
				minRank = 1,
				args = { { name = "target", kind = "player" }, { name = "reason", kind = "rest", optional = true } },
				run = function(actor, a)
					table.insert(env.ran, { "kick", actor, a.target, a.reason })
					return "kicked"
				end,
			},
			give = {
				minRank = 3,
				args = {
					{ name = "target", kind = "player", outranks = false },
					{ name = "amount", kind = "number", min = 1, max = 1000 },
				},
				run = function(actor, a)
					table.insert(env.ran, { "give", a.target, a.amount })
					return nil
				end,
			},
			boom = {
				minRank = 1,
				args = {},
				run = function()
					error("bug")
				end,
			},
		},
		getRank = function(uid)
			return ranks[uid] or 0
		end,
		findPlayers = function(q)
			q = string.lower(q)
			if names[q] then
				return { names[q] }
			end
			local out = {}
			for n, id in names do
				if string.sub(n, 1, #q) == q then
					table.insert(out, id)
				end
			end
			return out
		end,
		now = function()
			return env.clock
		end,
		audit = function(e)
			table.insert(env.audit, e)
		end,
	}
	for k, v in over or {} do
		cfg[k] = v
	end
	return Admin.new(cfg), env
end

print("Admin")

t.test("non-admins get no reply at all and nothing runs", function()
	local a, env = make()
	local r = a:Execute(3, "/kick bob")
	t.falsy(r.handled)
	t.eq(r.message, nil)
	t.eq(#env.ran, 0)
	t.eq(#env.audit, 0)
end)

t.test("text without the prefix is not a command", function()
	local a = make()
	t.falsy(a:Execute(1, "hello").handled)
	t.falsy(a:Execute(1, "kick bob").handled)
end)

t.test("rank gate: a mod cannot run an owner command", function()
	local a, env = make()
	local r = a:Execute(2, "/give carol 5")
	t.eq(r.message, "Unknown command.")
	t.eq(#env.ran, 0)
	t.falsy(env.audit[1].ok)
end)

t.test("owner kicks a lower-ranked player with a free-text reason", function()
	local a, env = make()
	local r = a:Execute(1, "/kick bob being rude")
	t.truthy(r.ok)
	t.eq(r.message, "kicked")
	t.eq(env.ran[1], { "kick", 1, 2, "being rude" })
	t.truthy(env.audit[1].ok)
end)

t.test("cannot target an equal or higher rank; can target self", function()
	local a, env = make()
	t.eq(a:Execute(1, "/kick dave").message, "you cannot target that player")
	t.eq(a:Execute(2, "/kick alice").message, "you cannot target that player")
	t.eq(#env.ran, 0)
	t.truthy(a:Execute(1, "/kick alice").ok)
end)

t.test("ambiguous and unknown player names are rejected", function()
	local a = make()
	t.truthy(string.find(a:Execute(1, "/kick bo").message, "several players"))
	t.truthy(string.find(a:Execute(1, "/kick zed").message, "no player matches"))
end)

t.test("number args: type, range and NaN/inf are validated", function()
	local a, env = make()
	t.eq(a:Execute(1, "/give carol abc").message, "amount must be a number")
	t.eq(a:Execute(1, "/give carol 0").message, "amount out of range")
	t.eq(a:Execute(1, "/give carol 5000").message, "amount out of range")
	t.eq(a:Execute(1, "/give carol nan").message, "amount must be a number")
	t.eq(a:Execute(1, "/give carol inf").message, "amount must be a number")
	t.eq(#env.ran, 0)
	t.truthy(a:Execute(1, "/give carol 25").ok)
	t.eq(env.ran[1], { "give", 3, 25 })
end)

t.test("missing required argument is reported", function()
	local a = make()
	t.eq(a:Execute(1, "/give carol").message, "amount is required")
	t.eq(a:Execute(1, "/kick").message, "target is required")
end)

t.test("a crashing command is contained and audited", function()
	local a, env = make()
	local r = a:Execute(1, "/boom")
	t.falsy(r.ok)
	t.eq(r.message, "Command failed.")
	t.truthy(string.find(env.audit[1].note, "error:"))
end)

t.test("rate limit: 10 per 10 s per actor, then allowed again", function()
	local a, env = make()
	local blocked = 0
	for _ = 1, 12 do
		if a:Execute(1, "/give carol 1").message == "Slow down." then
			blocked += 1
		end
	end
	t.eq(blocked, 2)
	env.clock += 11
	t.truthy(a:Execute(1, "/give carol 1").ok)
end)

t.test("oversized input is ignored", function()
	local a = make()
	t.falsy(a:Execute(1, "/kick " .. string.rep("a", 400)).handled)
end)

t.test("every attempt by an admin is audited, including refusals", function()
	local a, env = make()
	a:Execute(1, "/kick bob")
	a:Execute(1, "/kick dave")
	a:Execute(1, "/nope")
	t.eq(#env.audit, 3)
	t.eq({ env.audit[1].ok, env.audit[2].ok, env.audit[3].ok }, { true, false, false })
end)

t.done()
