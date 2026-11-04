--!nocheck
local t = require("../../../../../systems/_check/harness")
local SP = require("../SoundPlan")

t.test("small outdoor zone gets one spot and no volumetric", function()
	local l = SP.zone({ name = "yard", kind = "outdoor", area = 800 })
	t.eq(l.spots, 1)
	t.falsy(l.volumetric)
end)

t.test("spots scale with area and are capped", function()
	t.eq(SP.zone({ name = "a", kind = "outdoor", area = 4800 }).spots, 3)
	local big = SP.zone({ name = "b", kind = "outdoor", area = 90000 })
	t.truthy(big.volumetric)
	t.eq(big.spots, 4)
end)

t.test("indoor zones get reverb advice", function()
	local l = SP.zone({ name = "cabin", kind = "indoor", area = 400 })
	t.truthy(string.find(l.bed, "room tone", 1, true))
	t.eq(#l.notes, 1)
end)

t.test("plan totals spots and warns past the cap", function()
	local zones = {}
	for i = 1, 10 do
		table.insert(zones, { name = "z" .. i, kind = "outdoor", area = 6000 })
	end
	local p = SP.plan(zones, 20)
	t.truthy(p.totalSpots > 20)
	t.eq(#p.issues, 1)
	t.eq(#SP.plan({}).issues, 1)
end)

t.test("mix check flags loud music, low UI priority and a missing music bus", function()
	local issues =
		SP.checkMix({ { name = "music", volume = 0.6, priority = 2 }, { name = "ui", volume = 1, priority = 1 } })
	t.eq(#issues, 2)
	t.eq(#SP.checkMix({ { name = "ui", volume = 1, priority = 3 } }), 1)
	t.eq(#SP.checkMix({ { name = "music", volume = 0.2, priority = 1 }, { name = "ui", volume = 1, priority = 3 } }), 0)
end)

t.done()
