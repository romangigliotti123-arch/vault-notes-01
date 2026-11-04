--!strict
local TARGET: Instance? = nil

local Selection = game:GetService("Selection")

local R15_PARTS = {
	"HumanoidRootPart",
	"Head",
	"UpperTorso",
	"LowerTorso",
	"LeftUpperArm",
	"LeftLowerArm",
	"LeftHand",
	"RightUpperArm",
	"RightLowerArm",
	"RightHand",
	"LeftUpperLeg",
	"LeftLowerLeg",
	"LeftFoot",
	"RightUpperLeg",
	"RightLowerLeg",
	"RightFoot",
}

local R15_MOTORS: { [string]: { string } } = {
	Root = { "HumanoidRootPart", "LowerTorso" },
	Waist = { "LowerTorso", "UpperTorso" },
	Neck = { "UpperTorso", "Head" },
	LeftShoulder = { "UpperTorso", "LeftUpperArm" },
	LeftElbow = { "LeftUpperArm", "LeftLowerArm" },
	LeftWrist = { "LeftLowerArm", "LeftHand" },
	RightShoulder = { "UpperTorso", "RightUpperArm" },
	RightElbow = { "RightUpperArm", "RightLowerArm" },
	RightWrist = { "RightLowerArm", "RightHand" },
	LeftHip = { "LowerTorso", "LeftUpperLeg" },
	LeftKnee = { "LeftUpperLeg", "LeftLowerLeg" },
	LeftAnkle = { "LeftLowerLeg", "LeftFoot" },
	RightHip = { "LowerTorso", "RightUpperLeg" },
	RightKnee = { "RightUpperLeg", "RightLowerLeg" },
	RightAnkle = { "RightLowerLeg", "RightFoot" },
}

local function check(model: Model): { string }
	local problems = {}
	local function bad(msg: string)
		table.insert(problems, msg)
	end
	local humanoid = model:FindFirstChildOfClass("Humanoid")
	if not humanoid then
		bad("no Humanoid")
	elseif humanoid.RigType ~= Enum.HumanoidRigType.R15 then
		bad(`Humanoid.RigType is {humanoid.RigType.Name}, expected R15`)
	end
	if humanoid and not humanoid:FindFirstChildOfClass("Animator") then
		bad("Humanoid has no Animator (animations will not replicate predictably; add one)")
	end
	local parts: { [string]: BasePart } = {}
	for _, name in R15_PARTS do
		local part = model:FindFirstChild(name)
		if part and part:IsA("BasePart") then
			parts[name] = part
		else
			bad(`missing part {name}`)
		end
	end
	for motorName, ends in R15_MOTORS do
		local holder = parts[ends[2]]
		if holder then
			local motor = holder:FindFirstChild(motorName)
			if not motor or not motor:IsA("Motor6D") then
				bad(`{ends[2]} has no Motor6D named {motorName}`)
			else
				local m = motor :: Motor6D
				if m.Part0 ~= parts[ends[1]] then
					bad(`{motorName}.Part0 should be {ends[1]}`)
				end
				if m.Part1 ~= holder then
					bad(`{motorName}.Part1 should be {ends[2]}`)
				end
			end
		end
	end
	if not model.PrimaryPart then
		bad("Model.PrimaryPart is nil (set HumanoidRootPart)")
	elseif model.PrimaryPart.Name ~= "HumanoidRootPart" then
		bad(`PrimaryPart is {model.PrimaryPart.Name}, expected HumanoidRootPart`)
	end
	local root = parts.HumanoidRootPart
	if root and root.Anchored then
		bad("HumanoidRootPart is anchored: the character cannot move (fine for a static display dummy)")
	end
	for _, d in model:GetDescendants() do
		if
			d:IsA("BasePart")
			and d.Name ~= "HumanoidRootPart"
			and d.Massless == false
			and d:FindFirstAncestorOfClass("Accessory")
		then
			bad(`accessory part {d.Name} is not Massless (changes character mass and jump)`)
		end
	end
	local names: { [string]: boolean } = {}
	for _, c in model:GetChildren() do
		if c:IsA("BasePart") then
			if names[c.Name] then
				bad(`duplicate part name {c.Name}`)
			end
			names[c.Name] = true
		end
	end
	return problems
end

local target = TARGET or Selection:Get()[1]
if not target or not target:IsA("Model") then
	return "rig-checker: select the rig Model or set TARGET"
end
local problems = check(target :: Model)
local report = if #problems == 0
	then `RIG OK: {target:GetFullName()} passes the R15 structure checks`
	else `RIG PROBLEMS ({#problems}) in {target:GetFullName()}:\n- {table.concat(problems, "\n- ")}`
print(report)
return report
