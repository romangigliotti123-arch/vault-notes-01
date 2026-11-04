--!strict
local ROOT: Instance? = nil
local MODE: "bottomCenter" | "center" = "bottomCenter"
local APPLY = false
local TOLERANCE = 0.05
local DEPTH = 2
local MAX_LIST = 20

local Selection = game:GetService("Selection")
local ChangeHistoryService = game:GetService("ChangeHistoryService")

local function collect(inst: Instance, depth: number, out: { Model })
	for _, child in inst:GetChildren() do
		if
			child:IsA("Model")
			and not child:FindFirstChildOfClass("Humanoid")
			and child:GetAttribute("PivotLocked") ~= true
		then
			table.insert(out, child)
		elseif (child:IsA("Folder") or child:IsA("Model")) and depth > 1 then
			collect(child, depth - 1, out)
		end
	end
end

local function wanted(model: Model): CFrame
	local bbCF, size = model:GetBoundingBox()
	local pivot = model:GetPivot()
	local local_ = if MODE == "center" then Vector3.zero else Vector3.new(0, -size.Y / 2, 0)
	return CFrame.new((bbCF * CFrame.new(local_)).Position) * pivot.Rotation
end

local function run(): string
	local base = ROOT or Selection:Get()[1] or workspace
	local models: { Model } = {}
	if base:IsA("Model") then
		table.insert(models, base)
	else
		collect(base, DEPTH, models)
	end
	local off: { { model: Model, dist: number, target: CFrame } } = {}
	for _, m in models do
		local want = wanted(m)
		local dist = (want.Position - m:GetPivot().Position).Magnitude
		if dist > TOLERANCE then
			table.insert(off, { model = m, dist = dist, target = want })
		end
	end
	table.sort(off, function(a, b)
		return a.dist > b.dist
	end)
	local lines = { `PIVOT AUDIT: {base:GetFullName()} models={#models} off-pivot={#off} mode={MODE}` }
	for i = 1, math.min(MAX_LIST, #off) do
		table.insert(
			lines,
			`  {off[i].model:GetFullName()} pivot is {string.format("%.2f", off[i].dist)} studs from {MODE}`
		)
	end
	if APPLY and #off > 0 then
		local recording = ChangeHistoryService:TryBeginRecording("pivot-fixer set pivots")
		for _, o in off do
			local primary = o.model.PrimaryPart
			if primary then
				primary.PivotOffset = primary.CFrame:ToObjectSpace(o.target)
			else
				o.model.WorldPivot = o.target
			end
		end
		if recording then
			ChangeHistoryService:FinishRecording(recording, Enum.FinishRecordingOperation.Commit)
		end
		table.insert(lines, `moved the pivot of {#off} models (parts untouched, one undo step)`)
	else
		table.insert(lines, "read-only run: nothing changed")
	end
	return table.concat(lines, "\n")
end

local report = run()
print(report)
return report
