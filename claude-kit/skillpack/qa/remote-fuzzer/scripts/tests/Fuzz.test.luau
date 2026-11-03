--!nocheck
-- Run from the kit's systems folder: lune run ../skillpack/qa/remote-fuzzer/scripts/tests/Fuzz.test.luau
local t = require("../../../../../systems/_check/harness")
local Fuzz = require("../Fuzz")
local RemoteGuard = require("../../../../scripting/remote-guard-builder/scripts/RemoteGuard")

-- A shop handler with state: buy(item, qty) spends coins
local function world(handler)
	local s = { coins = 1000, items = {} }
	local prices = { sword = 100 }
	return {
		call = function(args)
			handler(s, prices, args[1], args[2])
		end,
		snapshot = function()
			return { coins = s.coins, items = s.items }
		end,
		reset = function()
			s.coins, s.items = 1000, {}
		end,
		baseline = { "sword", 2 },
		kinds = { "string", "integer" },
	}
end

local function naive(s, prices, item, qty)
	s.coins -= prices[item] * qty -- trusts everything
	s.items[item] = (s.items[item] or 0) + qty
end

local guards = { RemoteGuard.oneOf({ "sword" }), RemoteGuard.integer(1, 10) }
local function guarded(s, prices, item, qty)
	if not RemoteGuard.check(guards, item, qty) then
		return
	end
	local cost = prices[item] * qty
	if cost > s.coins then
		return
	end
	s.coins -= cost
	s.items[item] = (s.items[item] or 0) + qty
end

print("Fuzz")

t.test("naive handler is accepted for negative, NaN and fractional quantities", function()
	local f = Fuzz.run(world(naive))
	local seen = {}
	for _, x in f do
		seen[x.arg .. ":" .. x.label] = x.outcome
	end
	t.eq(seen["2:-1"], "accepted") -- negative qty pays the player
	t.eq(seen["2:0.5"], "accepted")
	t.truthy(seen["2:NaN"] ~= nil)
	t.truthy(#f > 5)
end)

t.test("guarded handler has no findings", function()
	local f = Fuzz.run(world(guarded))
	t.eq(#f, 0, Fuzz.report(f, { "string", "integer" }))
end)

t.test("errors inside the handler are reported unless skipped", function()
	local w = world(function(s, prices, item, qty)
		s.coins -= prices[item] * qty -- indexes nil for unknown item names
		s.items[item] = qty
	end)
	local threw = 0
	for _, x in Fuzz.run(w) do
		if x.outcome == "threw" then
			threw += 1
		end
	end
	t.truthy(threw > 0)
	w.skipThrew = true
	for _, x in Fuzz.run(w) do
		t.truthy(x.outcome ~= "threw")
	end
end)

t.test("a baseline that changes nothing is refused", function()
	local ok = pcall(Fuzz.run, world(function() end))
	t.falsy(ok)
end)

t.test("burst counts how many identical requests were honoured", function()
	local limiter = RemoteGuard.newLimiter(3, 1, function()
		return 0
	end)
	local limited = world(function(s, prices, item, qty)
		if limiter:allow(1) then
			guarded(s, prices, item, qty)
		end
	end)
	t.eq(Fuzz.burst(limited, 20), 3)
	t.eq(Fuzz.burst(world(guarded), 5), 5)
end)

t.test("report is readable", function()
	local f = Fuzz.run(world(naive))
	t.truthy(string.find(Fuzz.report(f, { "string", "integer" }), "arg 2 (integer)", 1, true))
	t.eq(Fuzz.report({}, {}), "FUZZ: 0 findings")
end)

t.done()
