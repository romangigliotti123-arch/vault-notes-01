--!strict
-- dump_parts.luau: read-only. Prints the parts under ROOT as Lua table lines for scripts/Cluster.luau, so the clustering
-- (which parts could become one exported mesh) runs offline under Lune. Paste into the Studio command bar or send through the
-- Studio MCP `execute_luau` tool (datamodel_type Edit). Output goes to the return value; paste it into a Lune file as
--   local parts = { <lines> }
--   local result = Cluster.find(parts, 64, 10)  -- then read result.groups, result.partsMerged, result.skipped
-- interactive = true when a part is unanchored, tagged, scripted, has a ClickDetector/ProximityPrompt, or sits in a model with scripts:
-- such parts must stay separate so scripts and physics keep working.
local ROOT: Instance? = nil -- nil = the current Selection, or Workspace when nothing is selected
local MAX_PARTS = 3000

local Selection = game:GetService("Selection")
local CollectionService = game:GetService("CollectionService")

local function interactive(part: BasePart): boolean
	if not part.Anchored then
		return true
	end
	if #CollectionService:GetTags(part) > 0 then
		return true
	end
	if part:FindFirstChildWhichIsA("ClickDetector") or part:FindFirstChildWhichIsA("ProximityPrompt") then
		return true
	end
	if part:FindFirstChildWhichIsA("LuaSourceContainer", true) then
		return true
	end
	local model = part:FindFirstAncestorOfClass("Model")
	return model ~= nil and model:FindFirstChildWhichIsA("LuaSourceContainer", true) ~= nil
end

local function run(): string
	local base = ROOT or Selection:Get()[1] or workspace
	local lines: { string } = {}
	local count = 0
	for _, inst in base:GetDescendants() do
		if inst:IsA("BasePart") and not inst:IsA("Terrain") then
			count += 1
			if count <= MAX_PARTS then
				local part = inst :: BasePart
				local p = part.Position
				local mesh = if part:IsA("MeshPart") then (part :: MeshPart).MeshId else ""
				table.insert(
					lines,
					string.format(
						"{ name = %q, x = %.1f, y = %.1f, z = %.1f, material = %q, color = %q, anchored = %s, interactive = %s, meshId = %q },",
						part.Name,
						p.X,
						p.Y,
						p.Z,
						part.Material.Name,
						part.Color:ToHex(),
						tostring(part.Anchored),
						tostring(interactive(part)),
						mesh
					)
				)
			end
		end
	end
	local header = `-- PARTS: {base:GetFullName()} total={count} dumped={math.min(count, MAX_PARTS)}`
	if count > MAX_PARTS then
		header ..= ` (raise MAX_PARTS or dump per model: the rest was not listed)`
	end
	return header .. "\n" .. table.concat(lines, "\n")
end

local report = run()
print(string.sub(report, 1, 200) .. " ...")
return report
