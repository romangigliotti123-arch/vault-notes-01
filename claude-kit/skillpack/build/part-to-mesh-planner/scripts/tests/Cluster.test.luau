--!nocheck
-- Run: lune run Cluster.test.luau   (from the kit's systems folder, see check-scripts.sh)
local t = require("../../../../../systems/_check/harness")
local Cluster = require("../Cluster")

local function part(i, x, material, color, extra)
	local p = { name = "P" .. i, x = x, y = 0, z = 0, material = material, color = color, anchored = true }
	for k, v in extra or {} do
		p[k] = v
	end
	return p
end

t.test("same material, colour and cell form one group", function()
	local parts = {}
	for i = 1, 12 do
		table.insert(parts, part(i, i, "Brick", "#aa0000"))
	end
	local r = Cluster.find(parts, 64, 10)
	t.eq(r.candidates, 1)
	t.eq(r.groups[1].count, 12)
	t.eq(r.partsMerged, 11)
end)

t.test("different material or colour splits the group", function()
	local parts = {}
	for i = 1, 12 do
		table.insert(parts, part(i, i, i % 2 == 0 and "Brick" or "Wood", "#aa0000"))
	end
	t.eq(Cluster.find(parts, 64, 10).candidates, 0)
	t.eq(Cluster.find(parts, 64, 5).candidates, 2)
end)

t.test("distant parts land in different cells", function()
	local parts = {}
	for i = 1, 10 do
		table.insert(parts, part(i, i * 100, "Brick", "#aa0000"))
	end
	t.eq(Cluster.find(parts, 64, 2).candidates, 0)
end)

t.test("unanchored and interactive parts are skipped and counted", function()
	local parts = {}
	for i = 1, 10 do
		table.insert(parts, part(i, i, "Brick", "#aa0000", { anchored = i > 2, interactive = i == 3 }))
	end
	local r = Cluster.find(parts, 64, 5)
	t.eq(r.skipped.unanchored, 2)
	t.eq(r.skipped.interactive, 1)
	t.eq(r.groups[1].count, 7)
end)

t.test("groups are sorted largest first", function()
	local parts = {}
	for i = 1, 6 do
		table.insert(parts, part(i, i, "Brick", "#aa0000"))
	end
	for i = 7, 16 do
		table.insert(parts, part(i, i, "Wood", "#aa0000"))
	end
	local r = Cluster.find(parts, 64, 5)
	t.eq(r.groups[1].count, 10)
end)

t.done()
