--!nocheck
local t = require("../../../../../systems/_check/harness")
local Inventory = require("../../../inventory-system-builder/scripts/Inventory")
local Crafting = require("../Crafting")

local clock = 1000
local inv = Inventory.new({
	capacity = 3,
	newUid = function()
		return "x"
	end,
	items = {
		Wood = { stack = 10 },
		Plank = { stack = 10 },
		Nail = { stack = 10 },
		Box = { stack = 10 },
		Junk1 = { stack = 1 },
		Junk2 = { stack = 1 },
	},
})
local function make()
	return Crafting.new({
		inventory = inv,
		queueLimit = 2,
		now = function()
			return clock
		end,
		recipes = {
			Plank = { inputs = { Wood = 2 }, output = { id = "Plank", qty = 1 }, seconds = 30 },
			Box = { inputs = { Plank = 2, Nail = 4 }, output = { id = "Box", qty = 1 }, seconds = 0 },
		},
	})
end

t.test("start consumes inputs immediately and queues", function()
	local d, c = {}, make()
	inv:add(d, "Wood", 5)
	t.truthy((c:start(d, "Plank")))
	t.eq(inv:count(d, "Wood"), 3)
	t.eq(#d.Crafting.queue, 1)
end)

t.test("missing ingredients, unknown recipe and full queue are refused without changes", function()
	local d, c = {}, make()
	inv:add(d, "Wood", 4)
	local ok, why = c:start(d, "Box")
	t.falsy(ok)
	t.eq(string.sub(why, 1, 7), "missing")
	t.falsy((c:start(d, "Nope")))
	c:start(d, "Plank")
	c:start(d, "Plank")
	local full, fwhy = c:start(d, "Plank")
	t.falsy(full)
	t.eq(fwhy, "queue full")
	t.eq(inv:count(d, "Wood"), 0)
end)

t.test("collect delivers only finished crafts, in order, once", function()
	local d, c = {}, make()
	inv:add(d, "Wood", 4)
	c:start(d, "Plank")
	c:start(d, "Plank")
	clock += 29
	t.eq(#c:collect(d), 0)
	clock += 1
	t.eq(#c:collect(d), 1)
	t.eq(#c:collect(d), 0)
	clock += 30
	t.eq(#c:collect(d), 1)
	t.eq(inv:count(d, "Plank"), 2)
end)

t.test("an output that does not fit stays queued, nothing lost", function()
	local d, c = {}, make()
	inv:add(d, "Wood", 2)
	c:start(d, "Plank")
	inv:add(d, "Junk1", 1)
	inv:add(d, "Junk2", 1)
	inv:add(d, "Nail", 1)
	clock += 100
	t.eq(#c:collect(d), 0)
	t.eq(#d.Crafting.queue, 1)
	inv:remove(d, "Nail", 1)
	t.eq(#c:collect(d), 1)
	t.eq(inv:count(d, "Plank"), 1)
end)

t.test("bad recipes are rejected at construction", function()
	local base = { inventory = inv, queueLimit = 1, now = os.time }
	local function with(r)
		return pcall(Crafting.new, { inventory = base.inventory, queueLimit = 1, now = os.time, recipes = { R = r } })
	end
	t.falsy((with({ inputs = {}, output = { id = "Plank", qty = 1 }, seconds = 1 })))
	t.falsy((with({ inputs = { Wood = 1.5 }, output = { id = "Plank", qty = 1 }, seconds = 1 })))
	t.falsy((with({ inputs = { Plank = 1 }, output = { id = "Plank", qty = 1 }, seconds = 1 })))
	t.falsy((with({ inputs = { Wood = 1 }, output = { id = "Plank", qty = 0 }, seconds = 1 })))
end)

t.done()
