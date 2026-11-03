--!strict
-- count_regions.luau: READ-ONLY. Buckets Workspace parts into square grid cells and prints counts per cell plus the 3x3 neighbourhood sum
-- (what a player standing in the cell can roughly see), worst first. Studio command bar or MCP `execute_luau` (Edit datamodel).
-- Output lines are "cell x,z  parts  neighbourhood  meshparts  unions  transparent" and can be pasted into PartBudget.evaluate (see SKILL.md).
-- Counts are INSTANCES, not draw calls or triangles: confirm those in Studio's Render/Summary stats (Ctrl+Shift+F2 draw count) before and after.
local CELL = 256 -- studs; heuristic cell size, larger than the usual first-person view but within the 1024 default streaming radius
local TOP = 12

local Workspace = game:GetService("Workspace")

type Cell = { x: number, z: number, parts: number, meshParts: number, unions: number, transparent: number }
local cells: { [string]: Cell } = {}

for _, inst in Workspace:GetDescendants() do
	if inst:IsA("BasePart") and not inst:IsA("Terrain") then
		local part = inst :: BasePart
		local cx = math.floor(part.Position.X / CELL)
		local cz = math.floor(part.Position.Z / CELL)
		local key = cx .. "," .. cz
		local c = cells[key]
		if not c then
			c = { x = cx, z = cz, parts = 0, meshParts = 0, unions = 0, transparent = 0 }
			cells[key] = c
		end
		c.parts += 1
		if part:IsA("MeshPart") then
			c.meshParts += 1
		elseif part:IsA("UnionOperation") then
			c.unions += 1
		end
		if part.Transparency > 0 and part.Transparency < 1 then
			c.transparent += 1 -- partial transparency causes overdraw (Creator Docs performance-optimization/design)
		end
	end
end

local rows: { { cell: Cell, hood: number } } = {}
for _, c in cells do
	local hood = 0
	for dx = -1, 1 do
		for dz = -1, 1 do
			local n = cells[(c.x + dx) .. "," .. (c.z + dz)]
			if n then
				hood += n.parts
			end
		end
	end
	table.insert(rows, { cell = c, hood = hood })
end
table.sort(rows, function(a, b)
	return a.hood > b.hood
end)

local lines = { ("cell size %d studs; %d non-empty cells"):format(CELL, #rows) }
for i = 1, math.min(TOP, #rows) do
	local r = rows[i]
	table.insert(
		lines,
		("cell %d,%d  parts=%d  neighbourhood=%d  mesh=%d  union=%d  partial-transparent=%d"):format(
			r.cell.x,
			r.cell.z,
			r.cell.parts,
			r.hood,
			r.cell.meshParts,
			r.cell.unions,
			r.cell.transparent
		)
	)
end
return table.concat(lines, "\n")
