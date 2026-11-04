--!strict
local TARGET: Instance? = nil
local MAX_NODES = 400

local Selection = game:GetService("Selection")
local HttpService = game:GetService("HttpService")

local function round(n: number): number
	return math.floor(n * 100 + 0.5) / 100
end

local function vec(v: Vector3): { number }
	return { round(v.X), round(v.Y), round(v.Z) }
end

local function describe(inst: Instance, pivot: CFrame): { [string]: any }
	local node: { [string]: any } = { n = inst.Name, c = inst.ClassName }
	if inst:IsA("BasePart") then
		local part = inst :: BasePart
		local rel = pivot:ToObjectSpace(part.CFrame)
		node.s = vec(part.Size)
		node.p = vec(rel.Position)
		local rx, ry, rz = rel:ToOrientation()
		node.r = { round(math.deg(rx)), round(math.deg(ry)), round(math.deg(rz)) }
		node.m = part.Material.Name
		node.col = part:GetAttribute("OriginalColor") or part.Color:ToHex()
		if part.Transparency > 0 then
			node.t = round(part.Transparency)
		end
		node.a = part.Anchored
		node.cc = part.CanCollide
		if part:IsA("MeshPart") then
			node.mesh = (part :: MeshPart).MeshId
			node.tex = (part :: MeshPart).TextureID
			node.cf = (part :: MeshPart).CollisionFidelity.Name
		elseif part:IsA("UnionOperation") then
			node.cf = (part :: UnionOperation).CollisionFidelity.Name
		elseif part:IsA("Part") then
			node.shape = (part :: Part).Shape.Name
		end
	end
	return node
end

local function dump(root: Instance): string
	local pivot = if root:IsA("Model")
		then (root :: Model):GetPivot()
		elseif root:IsA("BasePart") then (root :: BasePart).CFrame
		else CFrame.new()
	local nodes = {}
	local total = 0
	for _, inst in root:GetDescendants() do
		total += 1
		if #nodes < MAX_NODES then
			local node = describe(inst, pivot)
			node.d = #inst:GetFullName() - #root:GetFullName()
			node.parent = if inst.Parent == root then "" else inst.Parent and inst.Parent.Name or ""
			table.insert(nodes, node)
		end
	end
	local result = {
		root = root.Name,
		class = root.ClassName,
		descendants = total,
		truncated = total > MAX_NODES,
		nodes = nodes,
	}
	return HttpService:JSONEncode(result)
end

local target = TARGET or Selection:Get()[1]
if not target then
	return "model-rebuild manifest: select a model or set TARGET"
end
local json = dump(target)
print(json)
return json
