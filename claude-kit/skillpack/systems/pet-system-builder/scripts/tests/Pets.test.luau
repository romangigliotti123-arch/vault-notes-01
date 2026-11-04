--!nocheck
local t = require("../../../../../systems/_check/harness")
local Inventory = require("../../../inventory-system-builder/scripts/Inventory")
local Pets = require("../Pets")

local n = 0
local inv = Inventory.new({
	capacity = 6,
	newUid = function()
		n += 1
		return "p" .. n
	end,
	items = { Dog = { stack = 1, tradable = true }, GoldDog = { stack = 1, tradable = true }, Wood = { stack = 9 } },
})
local pets = Pets.new({
	inventory = inv,
	equipLimit = 2,
	fuseCount = 3,
	defs = { Dog = { power = 10, next = "GoldDog" }, GoldDog = { power = 40 } },
})

t.test("equip respects the slot limit and ownership", function()
	local d = {}
	inv:add(d, "Dog", 3)
	local u = inv:uids(d)
	t.truthy((pets:equip(d, u[1])))
	t.truthy((pets:equip(d, u[2])))
	t.falsy((pets:equip(d, u[3])))
	t.falsy((pets:equip(d, "forged")))
	t.falsy((pets:equip(d, u[1])))
end)

t.test("power sums equipped pets times the server multiplier", function()
	local d = {}
	inv:add(d, "Dog", 1)
	inv:add(d, "GoldDog", 1)
	for _, u in inv:uids(d) do
		pets:equip(d, u)
	end
	t.eq(pets:power(d), 50)
	t.eq(pets:power(d, 2), 100)
end)

t.test("fuse needs N unequipped pets and is all or nothing", function()
	local d = {}
	inv:add(d, "Dog", 4)
	local u = inv:uids(d)
	pets:equip(d, u[1])
	t.truthy((pets:fuse(d, "Dog")))
	t.eq(inv:count(d, "Dog"), 1)
	t.eq(inv:count(d, "GoldDog"), 1)
	t.falsy((pets:fuse(d, "Dog")))
	t.eq(inv:count(d, "Dog"), 1)
	t.falsy((pets:fuse(d, "GoldDog")))
end)

t.test("equipped list prunes pets that no longer exist", function()
	local d = {}
	inv:add(d, "Dog", 1)
	local u = inv:uids(d)[1]
	pets:equip(d, u)
	inv:removeUid(d, u)
	t.eq(pets:power(d), 0)
	t.eq(#d.Pets.equipped, 0)
end)

t.test("locked hook is true only for equipped pets", function()
	local d = {}
	inv:add(d, "Dog", 2)
	local u = inv:uids(d)
	pets:equip(d, u[1])
	t.truthy(pets:locked(d, u[1]))
	t.falsy(pets:locked(d, u[2]))
end)

t.test("config errors are caught up front", function()
	t.falsy(pcall(Pets.new, { inventory = inv, equipLimit = 1, defs = { A = { power = 1, next = "Missing" } } }))
	t.falsy(pcall(Pets.new, { inventory = inv, equipLimit = 0, defs = {} }))
end)

t.done()
