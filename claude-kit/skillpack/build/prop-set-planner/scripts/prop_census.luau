--!strict
local ROOT: Instance? = nil
local TOP = 8

local function run(): string
	local root = ROOT or workspace
	local total, parts, meshParts = 0, 0, 0
	local byMesh: { [string]: number } = {}
	local perModel: { [Instance]: number } = {}
	for _, inst in root:GetDescendants() do
		total += 1
		local model = inst:FindFirstAncestorOfClass("Model")
		local top: Instance? = model
		while top and top.Parent and top.Parent:IsA("Model") do
			top = top.Parent
		end
		if top then
			perModel[top] = (perModel[top] or 0) + 1
		end
		if inst:IsA("BasePart") then
			parts += 1
		end
		if inst:IsA("MeshPart") then
			meshParts += 1
			local id = (inst :: MeshPart).MeshId
			if id ~= "" then
				byMesh[id] = (byMesh[id] or 0) + 1
			end
		end
	end
	local uniqueMeshes = 0
	local ids: { string } = {}
	for id in byMesh do
		uniqueMeshes += 1
		table.insert(ids, id)
	end
	table.sort(ids, function(a, b)
		return byMesh[a] > byMesh[b]
	end)
	local models: { Instance } = {}
	for m in perModel do
		table.insert(models, m)
	end
	table.sort(models, function(a, b)
		return perModel[a] > perModel[b]
	end)
	local reuse = if uniqueMeshes > 0 then meshParts / uniqueMeshes else 0
	local lines = {
		`PROP CENSUS: {root:GetFullName()} instances={total} parts={parts} meshParts={meshParts} uniqueMeshes={uniqueMeshes} reuse={string.format(
			"%.1f",
			reuse
		)} copies/mesh`,
		`estimate (vault figures): load ~{string.format("%.1f", total / 10000)} s, client memory ~{string.format(
			"%.1f",
			total * 500 / 1048576
		)} MB for these instances`,
	}
	if total > 150000 then
		table.insert(lines, "over the ~150,000 instance guide: lower density, merge, or stream")
	end
	table.insert(lines, "most reused meshes:")
	for i = 1, math.min(TOP, #ids) do
		table.insert(lines, `  {byMesh[ids[i]]}x {ids[i]}`)
	end
	table.insert(lines, "heaviest top-level models (instances):")
	for i = 1, math.min(TOP, #models) do
		table.insert(lines, `  {perModel[models[i]]} {models[i]:GetFullName()}`)
	end
	if reuse > 0 and reuse < 3 then
		table.insert(lines, "reuse under 3 copies per mesh: the kit is too varied to be cheap, plan fewer variants")
	end
	table.insert(lines, "read-only run: nothing changed")
	return table.concat(lines, "\n")
end

local report = run()
print(report)
return report
