--!strict
-- terrain_audit.luau: read-only snapshot of the place's terrain and streaming settings, to compare against the plan from
-- scripts/TerrainPlan.luau. Paste into the Studio command bar or send through the Studio MCP `execute_luau` tool (Edit).
-- Reports: used extent in studs (voxels are 4 studs), water settings, decoration, whether instance streaming is on, and big
-- non-terrain parts that look like ground (a terrain-by-parts smell). Changes nothing.
local VOXEL = 4
local GROUND_PART_AREA = 4000 -- studs^2 for a flat part to count as "ground-sized"

local function read(inst: Instance, prop: string): string
	local ok, value = pcall(function()
		return (inst :: any)[prop]
	end)
	return if ok then tostring(value) else "n/a"
end

local function run(): string
	local terrain = workspace.Terrain
	local lines = { "TERRAIN AUDIT" }
	local ok, extents = pcall(function()
		return terrain.MaxExtents
	end)
	if ok then
		local lo, hi = extents.Min, extents.Max
		local w, h, d = (hi.X - lo.X + 1) * VOXEL, (hi.Y - lo.Y + 1) * VOXEL, (hi.Z - lo.Z + 1) * VOXEL
		local empty = hi.X < lo.X
		if empty or (w <= VOXEL and d <= VOXEL) then
			table.insert(lines, "extents: terrain is empty or a single voxel")
		else
			table.insert(
				lines,
				`extents: {w} x {h} x {d} studs (voxel grid {VOXEL}); heightmap equivalent {math.ceil(w / VOXEL)} x {math.ceil(
					d / VOXEL
				)} px`
			)
			if math.ceil(w / VOXEL) > 4096 or math.ceil(d / VOXEL) > 4096 then
				table.insert(lines, "extent is larger than one 4096 px heightmap (16384 studs): plan tiles")
			end
		end
	else
		table.insert(lines, "extents: not readable here")
	end
	for _, prop in { "WaterWaveSize", "WaterWaveSpeed", "WaterReflectance", "WaterTransparency", "Decoration" } do
		table.insert(lines, `{prop} = {read(terrain, prop)}`)
	end
	for _, prop in { "StreamingEnabled", "StreamingMinRadius", "StreamingTargetRadius", "StreamingIntegrityMode" } do
		table.insert(lines, `Workspace.{prop} = {read(workspace, prop)}`)
	end
	local groundish = 0
	local examples: { string } = {}
	for _, inst in workspace:GetDescendants() do
		if inst:IsA("BasePart") and not inst:IsA("Terrain") then
			local part = inst :: BasePart
			local s = part.Size
			if s.X * s.Z >= GROUND_PART_AREA and s.Y <= 8 then
				groundish += 1
				if #examples < 5 then
					table.insert(examples, part:GetFullName())
				end
			end
		end
	end
	if groundish > 0 then
		table.insert(
			lines,
			`[{groundish}] ground-sized flat parts (terrain may be cheaper and nicer): {table.concat(examples, ", ")}`
		)
	end
	table.insert(
		lines,
		"vault: hollow terrain with Subtract and delete hidden terrain; hollow alone can leave excess detail (3 MB voxels / 5 MB physics in one test)"
	)
	table.insert(lines, "read-only run: nothing changed")
	return table.concat(lines, "\n")
end

local report = run()
print(report)
return report
