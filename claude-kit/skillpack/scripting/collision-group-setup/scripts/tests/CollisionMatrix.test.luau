--!nocheck
local t = require("../../../../../systems/_check/harness")
local CollisionMatrix = require("../CollisionMatrix")

local spec = {
	groups = { "Players", "Enemies", "Pickups" },
	collide = { { "Players", "Enemies" } },
	noCollide = { { "Players", "Players" }, { "Enemies", "Enemies" }, { "Pickups", "Players" } },
}

t.test("plan registers groups and lists only the pairs that must stop colliding", function()
	local plan = CollisionMatrix.plan(spec)
	t.eq(plan.problems, {})
	t.eq(plan.register, { "Players", "Enemies", "Pickups" })
	t.eq(#plan.pairs, 3)
	t.eq(plan.pairs[1], { a = "Enemies", b = "Enemies", collidable = false })
end)

t.test("a pair in both lists is a problem and unknown groups are reported", function()
	local plan = CollisionMatrix.plan({
		groups = { "A" },
		collide = { { "A", "A" } },
		noCollide = { { "A", "A" }, { "A", "Ghost" } },
	})
	t.eq(#plan.problems, 2)
end)

t.test("duplicate, Default and badly named groups are problems", function()
	t.eq(#CollisionMatrix.plan({ groups = { "A", "A" } }).problems, 1)
	t.eq(#CollisionMatrix.plan({ groups = { "Default" } }).problems, 1)
	t.eq(#CollisionMatrix.plan({ groups = { "bad;name" } }).problems, 1)
end)

t.test("the group budget counts Default", function()
	local groups = {}
	for i = 1, 32 do
		groups[i] = "G" .. i
	end
	t.eq(#CollisionMatrix.plan({ groups = groups }).problems, 1)
	table.remove(groups)
	t.eq(#CollisionMatrix.plan({ groups = groups }).problems, 0)
end)

t.test("apply drives the adapter, and refuses a plan with problems", function()
	local log = {}
	local adapter = {
		register = function(n)
			table.insert(log, "reg " .. n)
		end,
		setCollidable = function(a, b, on)
			table.insert(log, a .. "/" .. b .. "=" .. tostring(on))
		end,
	}
	t.truthy(CollisionMatrix.apply(CollisionMatrix.plan(spec), adapter))
	t.eq(log[1], "reg Players")
	t.eq(#log, 6)
	local before = #log
	t.falsy(CollisionMatrix.apply(CollisionMatrix.plan({ groups = { "A", "A" } }), adapter))
	t.eq(#log, before)
end)

t.test("matrix draws X for colliding and . for ignoring pairs", function()
	local text = CollisionMatrix.matrix(spec)
	t.truthy(string.find(text, "Players", 1, true))
	t.truthy(string.find(text, ".", 1, true))
end)

t.done()
