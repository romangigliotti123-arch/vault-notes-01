--!nocheck
-- Run from the kit's systems folder: lune run ../skillpack/systems/tool-weapon-system-builder/scripts/tests/Weapons.test.luau
local t = require("../../../../../systems/_check/harness")
local Weapons = require("../Weapons")

local clock = 100
local function make()
	return Weapons.new({
		now = function()
			return clock
		end,
		defs = { Pistol = { cooldown = 0.5, damage = 12, mag = 2, reload = 1 }, Sword = { cooldown = 1, damage = 20 } },
	})
end
local holding = function(name)
	return { equipped = name, alive = true }
end

t.test("damage comes from the table and cooldown is enforced", function()
	local w = make()
	t.eq({ w:activate(1, "Sword", holding("Sword")) }, { true, "ok", 20 })
	clock += 0.2
	t.eq({ w:activate(1, "Sword", holding("Sword")) }, { false, "cooldown" })
	clock += 0.8
	t.eq((w:activate(1, "Sword", holding("Sword"))), true)
end)

t.test("not equipped, dead, unknown and non-string names are refused", function()
	local w = make()
	t.eq({ w:activate(1, "Sword", holding("Pistol")) }, { false, "not equipped" })
	t.eq({ w:activate(1, "Sword", { equipped = "Sword", alive = false }) }, { false, "dead" })
	t.eq({ w:activate(1, "Laser", holding("Laser")) }, { false, "unknown weapon" })
	t.eq({ w:activate(1, {}, holding("Sword")) }, { false, "unknown weapon" })
end)

t.test("ammo runs out, reload refills after the reload time", function()
	clock = 200
	local w = make()
	w:activate(1, "Pistol", holding("Pistol"))
	clock += 0.5
	w:activate(1, "Pistol", holding("Pistol"))
	clock += 0.5
	t.eq({ w:activate(1, "Pistol", holding("Pistol")) }, { false, "empty" })
	t.eq({ w:reload(1, "Pistol") }, { true, "ok" })
	t.eq({ w:activate(1, "Pistol", holding("Pistol")) }, { false, "reloading" })
	clock += 1
	t.eq((w:activate(1, "Pistol", holding("Pistol"))), true)
	t.eq(w:ammo(1, "Pistol"), 1)
end)

t.test("players are independent and melee has no ammo or reload", function()
	clock = 300
	local w = make()
	w:activate(1, "Sword", holding("Sword"))
	t.eq((w:activate(2, "Sword", holding("Sword"))), true)
	t.eq({ w:reload(1, "Sword") }, { false, "cannot reload" })
end)

t.test("a mag without a reload time is a config error", function()
	t.falsy(pcall(Weapons.new, { now = os.clock, defs = { X = { cooldown = 1, damage = 1, mag = 3 } } }))
end)

t.done()
