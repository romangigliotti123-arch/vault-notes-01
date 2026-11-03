--!strict
-- audit_model.luau: read-only audit of one model (and optional safe fixes). Paste into the Studio command bar,
-- or send through the Studio MCP `execute_luau` tool (datamodel_type Edit). Returns/prints a compact text report.
-- Set TARGET to an Instance, or leave nil to use the first selected object.
local TARGET: Instance? = nil
local APPLY_SAFE_FIXES = false -- true: set PrimaryPart when missing, CastShadow=false on tiny parts, then record one undo step
local EXPECT_STATIC = true -- true: unanchored parts are reported as problems (set false for ragdolls, vehicles, physics props)
local MAX_LIST = 12

local Selection = game:GetService("Selection")
local ChangeHistoryService = game:GetService("ChangeHistoryService")

local DEFAULT_NAMES = {
	Part = true,
	MeshPart = true,
	UnionOperation = true,
	Model = true,
	Folder = true,
	WedgePart = true,
	SpawnLocation = true,
}

local function isDefaultName(name: string): boolean
	local base = string.gsub(name, "%d+$", "")
	return DEFAULT_NAMES[base] == true
end

local function pathOf(inst: Instance, root: Instance): string
	local parts = {}
	local cur: Instance? = inst
	while cur and cur ~= root.Parent do
		table.insert(parts, 1, cur.Name)
		cur = cur.Parent
	end
	return table.concat(parts, "/")
end

local function audit(root: Instance): string
	local counts = {
		parts = 0,
		meshParts = 0,
		unions = 0,
		unanchored = 0,
		defaultNames = 0,
		preciseFidelity = 0,
		tinyParts = 0,
		zeroSize = 0,
		invisibleCollide = 0,
		scripts = 0,
		emptyContainers = 0,
		noMeshId = 0,
		plasticDefault = 0,
		decals = 0,
		welds = 0,
	}
	local samples: { [string]: { string } } = {}
	local function note(key: string, inst: Instance)
		local list = samples[key]
		if not list then
			list = {}
			samples[key] = list
		end
		if #list < MAX_LIST then
			table.insert(list, pathOf(inst, root))
		end
	end

	local siblingNames: { [Instance]: { [string]: number } } = {}
	local dupes = 0
	local largest: BasePart? = nil
	local largestVol = 0
	local all = root:GetDescendants()
	table.insert(all, 1, root)
	for _, inst in all do
		if inst:IsA("BasePart") then
			counts.parts += 1
			local part = inst :: BasePart
			local vol = part.Size.X * part.Size.Y * part.Size.Z
			if vol > largestVol then
				largestVol = vol
				largest = part
			end
			if part:IsA("MeshPart") then
				counts.meshParts += 1
				if (part :: MeshPart).MeshId == "" then
					counts.noMeshId += 1
					note("MeshPart without MeshId", part)
				end
				if (part :: MeshPart).CollisionFidelity == Enum.CollisionFidelity.PreciseConvexDecomposition then
					counts.preciseFidelity += 1
					note("PreciseConvexDecomposition collision", part)
				end
			elseif part:IsA("UnionOperation") then
				counts.unions += 1
				if (part :: UnionOperation).CollisionFidelity == Enum.CollisionFidelity.PreciseConvexDecomposition then
					counts.preciseFidelity += 1
					note("PreciseConvexDecomposition collision", part)
				end
			end
			if EXPECT_STATIC and not part.Anchored then
				counts.unanchored += 1
				note("unanchored", part)
			end
			if isDefaultName(part.Name) then
				counts.defaultNames += 1
				note("default name", part)
			end
			if part.Size.X < 0.05 or part.Size.Y < 0.05 or part.Size.Z < 0.05 then
				counts.zeroSize += 1
				note("near-zero size", part)
			end
			if part.Size.Magnitude < 0.5 then
				counts.tinyParts += 1
			end
			if part.Transparency >= 1 and part.CanCollide then
				counts.invisibleCollide += 1
				note("invisible but collidable", part)
			end
			if part.Material == Enum.Material.Plastic and not part:IsA("MeshPart") then
				counts.plasticDefault += 1
			end
		elseif inst:IsA("LuaSourceContainer") then
			counts.scripts += 1
			note("script inside model", inst)
		elseif inst:IsA("Decal") or inst:IsA("Texture") then
			counts.decals += 1
		elseif inst:IsA("WeldConstraint") or inst:IsA("Weld") then
			counts.welds += 1
		elseif (inst:IsA("Model") or inst:IsA("Folder")) and #inst:GetChildren() == 0 then
			counts.emptyContainers += 1
			note("empty container", inst)
		end
		local parent = inst.Parent
		if parent and inst ~= root then
			local names = siblingNames[parent]
			if not names then
				names = {}
				siblingNames[parent] = names
			end
			local n = (names[inst.Name] or 0) + 1
			names[inst.Name] = n
			if n == 2 then
				dupes += 1
			end
		end
	end

	local lines = {}
	table.insert(lines, `MODEL AUDIT: {root:GetFullName()} ({root.ClassName})`)
	table.insert(
		lines,
		`parts={counts.parts} meshParts={counts.meshParts} unions={counts.unions} scripts={counts.scripts} decals/textures={counts.decals} welds={counts.welds}`
	)
	local function row(label: string, n: number, hint: string)
		if n > 0 then
			table.insert(lines, `[{n}] {label} -> {hint}`)
		end
	end
	row("unanchored parts", counts.unanchored, "anchor static scenery; keep only parts that must move")
	row("default part names", counts.defaultNames, "name by purpose (Wall_North, Door_Frame)")
	row("duplicate sibling names", dupes, "unique names make FindFirstChild and Rojo predictable")
	row(
		"PreciseConvexDecomposition collision",
		counts.preciseFidelity,
		"use Box or Hull unless exact collision is needed"
	)
	row("unions", counts.unions, "prefer parts/meshes; unions cost memory and can fail to replicate on streaming")
	row("near-zero sized parts", counts.zeroSize, "delete or enlarge; usually leftovers")
	row("invisible but collidable parts", counts.invisibleCollide, "intended walls only; otherwise CanCollide=false")
	row("MeshParts without MeshId", counts.noMeshId, "broken import; re-import the mesh")
	row("scripts inside the model", counts.scripts, "move logic to server/client containers or tag the model")
	row("empty Folders/Models", counts.emptyContainers, "delete")
	row("default Plastic parts", counts.plasticDefault, "set a deliberate Material for the art style")
	row("tiny parts (<0.5 studs)", counts.tinyParts, "CastShadow=false is safe; consider merging")
	if root:IsA("Model") and not (root :: Model).PrimaryPart then
		table.insert(lines, "[1] no PrimaryPart -> set one (largest part is suggested) so PivotTo/placement behave")
	end
	for key, list in samples do
		table.insert(lines, `  e.g. {key}: {table.concat(list, ", ")}`)
	end

	if APPLY_SAFE_FIXES then
		local recording = ChangeHistoryService:TryBeginRecording("model-cleaner safe fixes")
		local fixed = 0
		if root:IsA("Model") and not (root :: Model).PrimaryPart and largest then
			(root :: Model).PrimaryPart = largest
			fixed += 1
		end
		for _, inst in all do
			if inst:IsA("BasePart") and (inst :: BasePart).Size.Magnitude < 0.5 and (inst :: BasePart).CastShadow then
				(inst :: BasePart).CastShadow = false
				fixed += 1
			end
		end
		if recording then
			ChangeHistoryService:FinishRecording(recording, Enum.FinishRecordingOperation.Commit)
		end
		table.insert(lines, `safe fixes applied: {fixed} (one undo step)`)
	else
		table.insert(lines, "read-only run: nothing changed")
	end
	return table.concat(lines, "\n")
end

local target = TARGET or Selection:Get()[1]
if not target then
	return "model-cleaner: select a model or set TARGET"
end
local report = audit(target)
print(report)
return report
