--!nocheck
-- Run from the kit's systems folder: lune run ../skillpack/liveops/feature-flag-config-builder/scripts/tests/FlagConfig.test.luau
local t = require("../../../../../systems/_check/harness")
local FlagConfig = require("../FlagConfig")

local function make()
	return FlagConfig.new({
		bossHealth = { kind = "number", default = 1000, min = 100, max = 5000 },
		eventActive = { kind = "boolean", default = false },
		mode = { kind = "string", default = "normal", allowed = { "normal", "hard" } },
		newShop = { kind = "rollout", default = 0 },
	})
end

t.test("defaults apply before any config arrives", function()
	local f = make()
	t.eq(f:Get("bossHealth"), 1000)
	t.eq(f:IsOn("eventActive", 1), false)
end)

t.test("valid values are taken, invalid ones fall back to the default and are reported", function()
	local f = make()
	local p = f:Apply({ bossHealth = 2500, eventActive = true, mode = "impossible", extra = 1 })
	t.eq(f:Get("bossHealth"), 2500)
	t.eq(f:IsOn("eventActive", 1), true)
	t.eq(f:Get("mode"), "normal")
	t.eq(#p, 2)
	t.truthy(string.find(p[1], "extra"))
end)

t.test("out of range, NaN and wrong types never stick: the default is used, not the last value", function()
	local f = make()
	f:Apply({ bossHealth = 2500 })
	f:Apply({ bossHealth = 99999 })
	t.eq(f:Get("bossHealth"), 1000)
	f:Apply({ bossHealth = 0 / 0 })
	t.eq(f:Get("bossHealth"), 1000)
	f:Apply({ bossHealth = "3000" })
	t.eq(f:Get("bossHealth"), 1000)
end)

t.test("a key missing from a push returns to its default", function()
	local f = make()
	f:Apply({ eventActive = true })
	f:Apply({})
	t.eq(f:Get("eventActive"), false)
end)

t.test("kill switch forces the default until revived", function()
	local f = make()
	f:Apply({ eventActive = true, bossHealth = 3000 })
	f:Kill("eventActive")
	t.eq(f:IsOn("eventActive", 5), false)
	t.eq(f:Get("bossHealth"), 3000)
	f:Revive("eventActive")
	t.eq(f:IsOn("eventActive", 5), true)
end)

t.test("rollout is stable per player and roughly matches the percentage", function()
	local f = make()
	f:Apply({ newShop = 30 })
	local on = 0
	for id = 1, 5000 do
		local a = f:IsOn("newShop", id)
		t.eq(a, f:IsOn("newShop", id))
		if a then
			on += 1
		end
	end
	t.truthy(on > 1200 and on < 1800)
	f:Apply({ newShop = 0 })
	t.eq(f:IsOn("newShop", 77), false)
	f:Apply({ newShop = 100 })
	t.eq(f:IsOn("newShop", 77), true)
end)

t.test("raising the percentage never switches an enabled player off", function()
	local f = make()
	f:Apply({ newShop = 20 })
	local early = {}
	for id = 1, 2000 do
		if f:IsOn("newShop", id) then
			early[id] = true
		end
	end
	f:Apply({ newShop = 50 })
	for id in early do
		t.eq(f:IsOn("newShop", id), true)
	end
end)

t.test("a bad default or unknown flag is a programmer error", function()
	t.falsy(pcall(FlagConfig.new, { x = { kind = "number", default = 5, min = 10 } }))
	t.falsy(pcall(function()
		make():Get("nope")
	end))
	t.falsy(pcall(function()
		make():IsOn("bossHealth", 1)
	end))
end)

t.done()
