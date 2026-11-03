--!nocheck
-- Run from the kit's systems folder: lune run ../skillpack/systems/quest-system-builder/scripts/tests/Quests.test.luau
local t = require("../../../../../systems/_check/harness")
local Wallet = require("../../../currency-system-builder/scripts/Wallet")
local Quests = require("../Quests")

local wallet = Wallet.new({ currencies = { Coins = {} } })
local function make()
	return Quests.new({
		defs = {
			wood = {
				goal = { event = "collect", target = "Wood", amount = 10 },
				reward = function(d)
					return (wallet:add(d, "Coins", 50, "quest:wood", "quest:wood"))
				end,
			},
			boss = {
				goal = { event = "kill", amount = 1 },
				requires = "wood",
				reward = function()
					return true
				end,
			},
			broken = {
				goal = { event = "x", amount = 1 },
				reward = function()
					return false
				end,
			},
		},
	})
end

t.test("progress counts matching events only and caps at the goal", function()
	local d, q = {}, make()
	q:progress(d, "collect", "Stone", 5)
	q:progress(d, "kill", nil, 1)
	t.eq(q:value(d, "wood"), 0)
	t.eq(q:progress(d, "collect", "Wood", 4), {})
	t.eq(q:progress(d, "collect", "Wood", 99), { "wood" })
	t.eq(q:value(d, "wood"), 10)
	t.eq(q:progress(d, "collect", "Wood", 1), {})
end)

t.test("bad event amounts are ignored", function()
	local d, q = {}, make()
	for _, bad in { -3, 0, 1.5, 0 / 0, 1e9 } do
		q:progress(d, "collect", "Wood", bad)
	end
	t.eq(q:value(d, "wood"), 0)
end)

t.test("claim works once and pays once", function()
	local d, q = {}, make()
	t.falsy((q:claim(d, "wood")))
	q:progress(d, "collect", "Wood", 10)
	t.truthy((q:claim(d, "wood")))
	local ok, why = q:claim(d, "wood")
	t.falsy(ok)
	t.eq(why, "already claimed")
	t.eq(wallet:balance(d, "Coins"), 50)
end)

t.test("chained quest stays locked and collects no progress until the prerequisite is claimed", function()
	local d, q = {}, make()
	q:progress(d, "kill", nil, 1)
	t.eq(q:value(d, "boss"), 0)
	q:progress(d, "collect", "Wood", 10)
	q:claim(d, "wood")
	q:progress(d, "kill", nil, 1)
	t.truthy(q:isComplete(d, "boss"))
end)

t.test("a refused reward leaves the quest claimable", function()
	local d, q = {}, make()
	q:progress(d, "x", nil, 1)
	local ok, why = q:claim(d, "broken")
	t.falsy(ok)
	t.eq(why, "reward refused")
	t.falsy(d.Quests.claimed.broken)
end)

t.test("construction rejects unknown or looping prerequisites", function()
	local function r()
		return true
	end
	t.falsy(pcall(Quests.new, { defs = { a = { goal = { event = "e", amount = 1 }, requires = "zzz", reward = r } } }))
	t.falsy(pcall(Quests.new, {
		defs = {
			a = { goal = { event = "e", amount = 1 }, requires = "b", reward = r },
			b = { goal = { event = "e", amount = 1 }, requires = "a", reward = r },
		},
	}))
end)

t.done()
