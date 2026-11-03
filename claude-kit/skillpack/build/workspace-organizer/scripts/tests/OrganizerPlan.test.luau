--!nocheck
-- Run: lune run OrganizerPlan.test.luau   (from the kit's systems folder, see check-scripts.sh)
local t = require("../../../../../systems/_check/harness")
local OP = require("../OrganizerPlan")

t.test("engine and organising classes are kept in place", function()
	for _, c in { "Terrain", "Camera", "Folder", "Script" } do
		local f = OP.folderFor({ name = "x", class = c })
		t.eq(f, nil)
	end
end)

t.test("classes map to folders", function()
	t.eq((OP.folderFor({ name = "Start", class = "SpawnLocation" })), "Spawns")
	t.eq((OP.folderFor({ name = "Wind", class = "Sound" })), "Audio")
	t.eq((OP.folderFor({ name = "L", class = "PointLight" })), "Lights")
end)

t.test("names decide zone, prop, interactive and map", function()
	t.eq((OP.folderFor({ name = "KillBrick1", class = "Part" })), "Zones")
	t.eq((OP.folderFor({ name = "OakTree", class = "Model" })), "Props")
	t.eq((OP.folderFor({ name = "Elevator", class = "Model", hasScripts = true })), "Interactive")
	t.eq((OP.folderFor({ name = "Castle", class = "Model" })), "Map")
	t.eq((OP.folderFor({ name = "Wall", class = "UnionOperation" })), "Map")
end)

t.test("unknown classes go to Misc", function()
	t.eq((OP.folderFor({ name = "B", class = "BindableEvent" })), "Misc")
end)

t.test("plan lists moves, kept names and sorted unique folders", function()
	local p = OP.plan({
		{ name = "Terrain", class = "Terrain" },
		{ name = "Castle", class = "Model" },
		{ name = "Hill", class = "Model" },
		{ name = "Pine tree", class = "Model" },
	})
	t.eq(p.keep, { "Terrain" })
	t.eq(#p.moves, 3)
	t.eq(p.folders, { "Map", "Props" })
end)

t.done()
