--!nocheck
local t = require("../../../../../systems/_check/harness")
local SS = require("../StyleStats")

t.test("bucket merges near colours and clamps to 255", function()
	t.eq(SS.bucket(250, 250, 250), "#FFFFFF")
	t.eq(SS.bucket(10, 12, 0), "#000000")
	t.eq(SS.bucket(100, 100, 100), SS.bucket(105, 98, 110))
end)

t.test("rare materials are outliers once there is a dominant set", function()
	local r = SS.analyse({
		{ material = "SmoothPlastic", color = "#808080", count = 500 },
		{ material = "Wood", color = "#808080", count = 300 },
		{ material = "Grass", color = "#808080", count = 190 },
		{ material = "Brick", color = "#808080", count = 80 },
		{ material = "Neon", color = "#808080", count = 3 },
	})
	t.eq(r.total, 1073)
	t.eq(#r.materialOutliers, 1)
	t.eq(r.materialOutliers[1].key, "Neon")
	t.eq(r.distinctMaterials, 5)
end)

t.test("few distinct values give no outliers (nothing dominant to compare against)", function()
	local r = SS.analyse({
		{ material = "A", color = "#111111", count = 1000 },
		{ material = "B", color = "#222222", count = 1 },
	})
	t.eq(#r.materialOutliers, 0)
	t.eq(#r.colorOutliers, 0)
end)

t.test("too many materials or colours add notes", function()
	local s = {}
	for i = 1, 8 do
		table.insert(s, { material = "M" .. i, color = "#" .. string.format("%06X", i * 1000), count = 10 })
	end
	for i = 9, 14 do
		table.insert(s, { material = "M1", color = "#" .. string.format("%06X", i * 1000), count = 10 })
	end
	local r = SS.analyse(s)
	t.eq(#r.notes, 2)
end)

t.test("count defaults to one", function()
	t.eq(SS.analyse({ { material = "A", color = "#000000" }, { material = "A", color = "#000000" } }).total, 2)
end)

t.done()
