--!nocheck
local t = require("../../../../../systems/_check/harness")
local Wallet = require("../../../currency-system-builder/scripts/Wallet")
local Rebirth = require("../Rebirth")

local wallet = Wallet.new({ currencies = { Coins = {}, Gems = {} } })
local function make(extra)
	local cfg = {
		wallet = wallet,
		currency = "Coins",
		baseCost = 1000,
		growth = 2,
		gainPerRebirth = 0.5,
		maxRebirths = 3,
		reset = function(d)
			d.Wallet.bal.Coins = 0
			d.Zone = 1
		end,
	}
	for k, v in extra or {} do
		cfg[k] = v
	end
	return Rebirth.new(cfg)
end

t.test("cost grows and multiplier is additive", function()
	local d, r = {}, make()
	t.eq(r:cost(0), 1000)
	t.eq(r:cost(3), 8000)
	t.eq(r:multiplier(d), 1)
	t.eq(r:nextMultiplier(d), 1.5)
end)

t.test("rebirth pays, resets, keeps what the reset leaves, raises the multiplier", function()
	local d, r = { Zone = 7 }, make()
	wallet:add(d, "Coins", 1500, "x")
	wallet:add(d, "Gems", 20, "x")
	t.truthy((r:attempt(d, 0)))
	t.eq(wallet:balance(d, "Coins"), 0)
	t.eq(wallet:balance(d, "Gems"), 20)
	t.eq(d.Zone, 1)
	t.eq(r:multiplier(d), 1.5)
end)

t.test("a replayed or double-clicked request is refused", function()
	local d, r = {}, make()
	wallet:add(d, "Coins", 5000, "x")
	t.truthy((r:attempt(d, 0)))
	wallet:add(d, "Coins", 5000, "x")
	local ok, why = r:attempt(d, 0)
	t.falsy(ok)
	t.eq(why, "stale request")
	t.eq(r:count(d), 1)
end)

t.test("cannot afford changes nothing", function()
	local d, r = { Zone = 4 }, make()
	wallet:add(d, "Coins", 999, "x")
	local ok, why = r:attempt(d, 0)
	t.falsy(ok)
	t.eq(why, "cannot afford")
	t.eq(d.Zone, 4)
	t.eq(wallet:balance(d, "Coins"), 999)
end)

t.test("max rebirths is enforced", function()
	local d, r = {}, make({ maxRebirths = 1 })
	wallet:add(d, "Coins", 100000, "x")
	t.truthy((r:attempt(d, 0)))
	wallet:add(d, "Coins", 100000, "x")
	local ok, why = r:attempt(d, 1)
	t.falsy(ok)
	t.eq(why, "max rebirths")
end)

t.test("a free or losing config is rejected", function()
	t.falsy(pcall(make, { growth = 0.5 }))
	t.falsy(pcall(make, { gainPerRebirth = 0 }))
	t.falsy(pcall(make, { baseCost = 0 }))
end)

t.done()
