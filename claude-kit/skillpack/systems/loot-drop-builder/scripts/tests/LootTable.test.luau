--!nocheck
local t = require("../../../../../systems/_check/harness")
local LootTable = require("../LootTable")

local function seq(values)
	local i = 0
	return function()
		i += 1
		return values[(i - 1) % #values + 1]
	end
end

local entries = {
	{ id = "Dog", weight = 70, rarity = "common" },
	{ id = "Fox", weight = 25, rarity = "rare" },
	{ id = "Dragon", weight = 5, rarity = "legendary" },
}
local function make(rng, pity, log)
	return LootTable.new({ name = "Egg", entries = entries, rng = rng, pity = pity, log = log })
end

t.test("odds sum to 100 and match the weights", function()
	local o = make(seq({ 0 })):odds()
	local sum = 0
	for _, e in o do
		sum += e.percent
	end
	t.truthy(math.abs(sum - 100) < 1e-9)
	t.eq(o[3].percent, 5)
end)

t.test("roll walks the cumulative weights", function()
	local d = {}
	local loot = make(seq({ 0, 0.69, 0.70, 0.94, 0.95, 0.999 }))
	local got = {}
	for _ = 1, 6 do
		table.insert(got, loot:roll(d))
	end
	t.eq(got, { "Dog", "Dog", "Fox", "Fox", "Dragon", "Dragon" })
end)

t.test("pity forces the top rarity on the Nth roll and resets", function()
	local d = {}
	local loot = make(seq({ 0 }), { rarity = "legendary", every = 4 })
	t.eq(loot:roll(d), "Dog")
	t.eq(loot:roll(d), "Dog")
	t.eq(loot:roll(d), "Dog")
	t.eq(loot:roll(d), "Dragon")
	t.eq(loot:sinceRare(d), 0)
	t.eq(loot:roll(d), "Dog")
end)

t.test("a natural legendary resets the pity counter", function()
	local d = {}
	local loot = make(seq({ 0, 0, 0.99 }), { rarity = "legendary", every = 10 })
	loot:roll(d)
	loot:roll(d)
	t.eq(loot:sinceRare(d), 2)
	t.eq(loot:roll(d), "Dragon")
	t.eq(loot:sinceRare(d), 0)
end)

t.test("luck boosts non-base weights only and is bounded", function()
	local d = {}
	t.eq(make(seq({ 0.55 })):roll(d, 2), "Fox")
	t.eq(make(seq({ 0.55 })):roll(d, 1), "Dog")
	t.falsy(pcall(function()
		return make(seq({ 0 })):roll(d, 0.5)
	end))
	t.falsy(pcall(function()
		return make(seq({ 0 })):roll(d, 1000)
	end))
end)

t.test("rng outside [0,1) is refused", function()
	t.falsy(pcall(function()
		return make(seq({ 1 })):roll({})
	end))
end)

t.test("the log gets one entry per roll", function()
	local logs = {}
	local loot = make(seq({ 0 }), nil, function(e)
		table.insert(logs, e)
	end)
	loot:roll({})
	t.eq(#logs, 1)
	t.eq(logs[1].id, "Dog")
end)

t.test("empirical rates over 20000 seeded rolls are near the stated odds", function()
	local state = 12345
	local function lcg()
		state = (state * 1103515245 + 12345) % 2147483648
		return state / 2147483648
	end
	local d, counts = {}, { Dog = 0, Fox = 0, Dragon = 0 }
	local loot = make(lcg)
	for _ = 1, 20000 do
		local id = loot:roll(d)
		counts[id] += 1
	end
	t.truthy(math.abs(counts.Dog / 200 - 70) < 2, "Dog " .. counts.Dog)
	t.truthy(math.abs(counts.Dragon / 200 - 5) < 1, "Dragon " .. counts.Dragon)
end)

t.test("bad tables are rejected", function()
	t.falsy(pcall(LootTable.new, { name = "x", entries = {}, rng = seq({ 0 }) }))
	t.falsy(
		pcall(LootTable.new, { name = "x", entries = { { id = "a", weight = 0, rarity = "c" } }, rng = seq({ 0 }) })
	)
	t.falsy(
		pcall(
			LootTable.new,
			{ name = "x", entries = entries, rng = seq({ 0 }), pity = { rarity = "mythic", every = 5 } }
		)
	)
end)

t.done()
