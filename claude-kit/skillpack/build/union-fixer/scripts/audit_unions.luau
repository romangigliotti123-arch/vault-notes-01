--!strict
local ROOT: Instance? = nil
local APPLY_FIDELITY = false
local FIDELITY_TARGET = Enum.CollisionFidelity.Hull
local MAX_LIST = 15
local TINY = 1

local ChangeHistoryService = game:GetService("ChangeHistoryService")

local function run(): string
	local root = ROOT or workspace
	local unions: { UnionOperation } = {}
	local precise: { UnionOperation } = {}
	local tiny: { UnionOperation } = {}
	local negative = 0
	local totalParts = 0
	for _, inst in root:GetDescendants() do
		if inst:IsA("BasePart") then
			totalParts += 1
		end
		if inst:IsA("UnionOperation") then
			local u = inst :: UnionOperation
			table.insert(unions, u)
			if u.CollisionFidelity == Enum.CollisionFidelity.PreciseConvexDecomposition then
				table.insert(precise, u)
			end
			if math.max(u.Size.X, u.Size.Y, u.Size.Z) < TINY then
				table.insert(tiny, u)
			end
		elseif inst:IsA("NegateOperation") then
			negative += 1
		end
	end
	table.sort(unions, function(a, b)
		return a.Size.X * a.Size.Y * a.Size.Z > b.Size.X * b.Size.Y * b.Size.Z
	end)
	local lines = {
		`UNION AUDIT: {root:GetFullName()} unions={#unions} of {totalParts} parts, leftover negative parts={negative}`,
		`[{#precise}] PreciseConvexDecomposition unions -> APPLY_FIDELITY drops them to {FIDELITY_TARGET.Name}`,
		`[{#tiny}] tiny unions (every side under {TINY} stud) -> replace with a Part by hand`,
		"Replace by shape: box/wedge/cylinder-like -> plain Part(s); carved or curved -> export a mesh (part-to-mesh-planner); keep a union only if neither works.",
	}
	table.insert(lines, "largest unions (replace these first):")
	for i = 1, math.min(MAX_LIST, #unions) do
		local u = unions[i]
		table.insert(
			lines,
			`  {u:GetFullName()} size {string.format("%.1f x %.1f x %.1f", u.Size.X, u.Size.Y, u.Size.Z)} {u.CollisionFidelity.Name}`
		)
	end
	if APPLY_FIDELITY and #precise > 0 then
		local recording = ChangeHistoryService:TryBeginRecording("union-fixer collision fidelity")
		for _, u in precise do
			u.CollisionFidelity = FIDELITY_TARGET
		end
		if recording then
			ChangeHistoryService:FinishRecording(recording, Enum.FinishRecordingOperation.Commit)
		end
		table.insert(lines, `set {#precise} unions to {FIDELITY_TARGET.Name} (one undo step)`)
	else
		table.insert(lines, "read-only run: nothing changed")
	end
	return table.concat(lines, "\n")
end

local report = run()
print(report)
return report
