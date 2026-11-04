--!nocheck
local t = require("../../../../../systems/_check/harness")
local Inventory = require("../Inventory")

local n = 0
local function make(capacity)
	return Inventory.new({
		capacity = capacity or 4,
		newUid = function()
			n += 1
			return "u" .. n
		end,
		items = { Wood = { stack = 10 }, Sword = { stack = 1, tradable = true }, Gem = { stack = 5 } },
	})
end

t.test("stacks fill existing slots before opening new ones", function()
	local d, inv = {}, make()
	t.truthy((inv:add(d, "Wood", 7)))
	t.truthy((inv:add(d, "Wood", 8)))
	t.eq(inv:count(d, "Wood"), 15)
	t.eq(inv:freeSlots(d), 2)
end)

t.test("add that does not fit changes nothing", function()
	local d, inv = {}, make(2)
	inv:add(d, "Wood", 10)
	inv:add(d, "Gem", 3)
	local ok, why = inv:add(d, "Wood", 11)
	t.falsy(ok)
	t.eq(why, "no room")
	t.eq(inv:count(d, "Wood"), 10)
	t.eq(inv:count(d, "Gem"), 3)
end)

t.test("rejects bad quantities and unknown items", function()
	local d, inv = {}, make()
	for _, bad in { 0, -1, 1.5, 0 / 0, 1e9 } do
		t.falsy((inv:add(d, "Wood", bad)), "add " .. tostring(bad))
		t.falsy((inv:remove(d, "Wood", bad)), "remove " .. tostring(bad))
	end
	t.falsy((inv:add(d, "Nope", 1)))
	t.eq(inv:count(d, "Wood"), 0)
end)

t.test("remove is all or nothing and drops emptied slots", function()
	local d, inv = {}, make()
	inv:add(d, "Wood", 15)
	local ok = inv:remove(d, "Wood", 16)
	t.falsy(ok)
	t.eq(inv:count(d, "Wood"), 15)
	t.truthy((inv:remove(d, "Wood", 15)))
	t.eq(inv:freeSlots(d), 4)
end)

t.test("unique items get distinct uids and remove by uid", function()
	local d, inv = {}, make()
	inv:add(d, "Sword", 2)
	local uids = inv:uids(d)
	t.eq(#uids, 2)
	t.truthy(uids[1] ~= uids[2])
	t.truthy((inv:removeUid(d, uids[1])))
	t.falsy((inv:removeUid(d, uids[1])))
	t.eq(inv:count(d, "Sword"), 1)
end)

t.test("validate catches corruption", function()
	local d, inv = {}, make()
	inv:add(d, "Wood", 3)
	t.eq(#inv:validate(d), 0)
	d.Inventory.slots[2] = { id = "Wood", qty = 999 }
	d.Inventory.slots[3] = { id = "Ghost", qty = 1 }
	d.Inventory.slots[4] = { id = "Sword", qty = 1 }
	t.eq(#inv:validate(d), 3)
end)

t.test("room counts partial stacks and free slots", function()
	local d, inv = {}, make()
	inv:add(d, "Wood", 4)
	t.eq(inv:room(d, "Wood"), 6 + 3 * 10)
	t.eq(inv:room(d, "Sword"), 3)
end)

t.done()
