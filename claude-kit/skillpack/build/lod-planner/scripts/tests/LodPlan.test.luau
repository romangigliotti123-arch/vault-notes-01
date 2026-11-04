--!nocheck
local t = require("../../../../../systems/_check/harness")
local LodPlan = require("../LodPlan")

t.test("essential models are Persistent and not SLIM", function()
	local d = LodPlan.classify({ name = "Spawn", parts = 50, essential = true })
	t.eq(d.streamingMode, "Persistent")
	t.falsy(d.slim)
end)

t.test("scripted models are Atomic", function()
	t.eq(LodPlan.classify({ name = "Door", parts = 5, scripted = true, dynamic = true }).streamingMode, "Atomic")
end)

t.test("static scenery is SLIM with the default mode", function()
	local d = LodPlan.classify({ name = "House", parts = 300 })
	t.eq(d.streamingMode, "Default")
	t.truthy(d.slim)
end)

t.test("dynamic models are not SLIM and say why", function()
	local d = LodPlan.classify({ name = "Elevator", parts = 20, dynamic = true })
	t.falsy(d.slim)
	t.eq(#d.notes, 1)
end)

t.test("large extent and part count add split notes", function()
	local d = LodPlan.classify({ name = "City", parts = 5000, extent = 900 })
	t.eq(#d.notes, 2)
end)

t.test("too many Persistent models raise a warning", function()
	local models = {}
	for i = 1, 10 do
		table.insert(models, { name = "M" .. i, parts = 1, essential = i <= 3 })
	end
	local s = LodPlan.plan(models)
	t.eq(s.persistent, 3)
	t.eq(#s.warnings, 1)
	t.eq(s.slim, 7)
end)

t.done()
