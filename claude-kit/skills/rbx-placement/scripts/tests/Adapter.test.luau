--!nocheck
local roblox = require("@lune/roblox")
local serde = require("@lune/serde")
local t = require("../../../../systems/_check/harness")
local Placement = require("../Placement")

local Instance, CFrame, Vector3 = roblox.Instance, roblox.CFrame, roblox.Vector3

local root = Instance.new("Folder")
root.Name = "Workspace"

local function allParts(inst)
	local out = {}
	for _, d in inst:GetDescendants() do
		if d:IsA("BasePart") then
			table.insert(out, d)
		end
	end
	if inst:IsA("BasePart") then
		table.insert(out, inst)
	end
	return out
end

local function inside(inst, ignore)
	for _, ig in ignore do
		if inst == ig or inst:IsDescendantOf(ig) then
			return true
		end
	end
	return false
end

local function modelParts(m)
	local out = {}
	for _, d in m:GetDescendants() do
		if d:IsA("BasePart") then
			table.insert(out, d)
		end
	end
	return out
end

local world = {
	root = function()
		return root
	end,
	resolve = function(path)
		local segs = string.split(path, ".")
		local cur = root
		for i = 2, #segs do
			cur = cur and cur:FindFirstChild(segs[i])
		end
		return cur
	end,
	pivot = function(inst)
		if inst:IsA("Model") then
			local pp = inst.PrimaryPart
			if pp then
				return pp.CFrame
			end
			return modelParts(inst)[1].CFrame
		end
		return inst.CFrame
	end,
	pivotTo = function(inst, cf)
		if inst:IsA("Model") then
			local pp = inst.PrimaryPart or modelParts(inst)[1]
			local delta = cf * pp.CFrame:Inverse()
			for _, p in modelParts(inst) do
				p.CFrame = delta * p.CFrame
			end
		else
			inst.CFrame = cf
		end
	end,
	position = function(inst)
		local p = (inst:IsA("Model") and inst.PrimaryPart or inst).CFrame.Position
		return { p.X, p.Y, p.Z }
	end,
	assemblyAnchored = function(part)
		return part.Anchored
	end,
	raycast = function(ox, oy, oz, length, ignore)
		local best
		for _, p in allParts(root) do
			if not inside(p, ignore) then
				local c, s = p.CFrame.Position, p.Size
				local top = c.Y + s.Y / 2
				if
					math.abs(ox - c.X) <= s.X / 2
					and math.abs(oz - c.Z) <= s.Z / 2
					and top <= oy
					and oy - top <= length
				then
					if not best or top > best.y then
						best = { y = top, n = { 0, 1, 0 }, path = p:GetFullName() }
					end
				end
			end
		end
		return best
	end,
	partsInBox = function(center, size, ignore)
		local out = {}
		for _, p in allParts(root) do
			if not inside(p, ignore) then
				local c, s = p.CFrame.Position, p.Size
				local r = (s.X + s.Y + s.Z) / 2
				if
					math.abs(c.X - center[1]) <= size[1] / 2 + r
					and math.abs(c.Y - center[2]) <= size[2] / 2 + r
					and math.abs(c.Z - center[3]) <= size[3] / 2 + r
				then
					table.insert(out, p)
				end
			end
		end
		return out
	end,
	terrainFill = function()
		return nil
	end,
	isCharacter = function()
		return false
	end,
	translated = function(cf, d)
		return cf + Vector3.new(d[1], d[2], d[3])
	end,
	rotatedY = function(cf, deg)
		return CFrame.new(cf.Position) * CFrame.Angles(0, math.rad(deg), 0) * (CFrame.new(-cf.Position) * cf)
	end,
	upright = function(cf)
		local look = cf.LookVector
		local flat = Vector3.new(look.X, 0, look.Z)
		if flat.Magnitude < 0.1 then
			flat = Vector3.new(0, 0, -1)
		end
		return CFrame.lookAt(cf.Position, cf.Position + flat.Unit)
	end,
	moveTo = function(cf, pos)
		return CFrame.new(Vector3.new(pos[1], pos[2], pos[3])) * (CFrame.new(-cf.Position) * cf)
	end,
	jsonEncode = function(v)
		return serde.encode("json", v)
	end,
	jsonDecode = function(s)
		return serde.decode("json", s)
	end,
	plain = function(v)
		return v
	end,
	now = function()
		return "2026-01-01T00:00:00Z"
	end,
	datamodel = function()
		return "Edit"
	end,
}
Placement.world = world
Placement.config.emit = false

local map = Instance.new("Folder")
map.Name = "Map"
map.Parent = root

local function newPart(parent, name, pos, size, yaw, anchored)
	local p = Instance.new("Part")
	p.Name = name
	p.Size = Vector3.new(size[1], size[2], size[3])
	p.CFrame = CFrame.new(pos[1], pos[2], pos[3]) * CFrame.Angles(0, math.rad(yaw or 0), 0)
	p.Anchored = anchored ~= false
	p.CanCollide = true
	p.Parent = parent
	return p
end

local function newModel(name, parts)
	local m = Instance.new("Model")
	m.Name = name
	local first
	for _, spec in parts do
		local p = newPart(m, spec.name, spec.pos, spec.size, spec.yaw, spec.anchored)
		first = first or p
	end
	m.PrimaryPart = first
	return m
end

local floor = newPart(map, "Floor", { 0, -0.5, 0 }, { 200, 1, 200 }, 0, true)
local function y(m)
	return Placement.world.pivot(m).Position.Y
end

t.test("snapshot reads parts, pivot and flags into plain data", function()
	local m = newModel("Crate1", { { name = "Box", pos = { 5, 1.5, 5 }, size = { 3, 3, 3 } } })
	m.Parent = map
	local snap = Placement.snapshot(m)
	t.eq(snap.path, "Workspace.Map.Crate1")
	t.eq(snap.class, "Model")
	t.eq(#snap.parts, 1)
	t.eq(snap.parts[1].name, "Box")
	t.eq(snap.parts[1].size, { 3, 3, 3 })
	t.eq(snap.hasPrimaryPart, true)
	t.eq(snap.pivot.p, { 5, 1.5, 5 })
	t.eq(snap.parts[1].anchored, true)
end)

t.test("verify passes a model that rests on the floor", function()
	local m = newModel("Crate2", { { name = "Box", pos = { 10, 1.5, 5 }, size = { 3, 3, 3 } } })
	m.Parent = map
	local rep = Placement.verify(m, { kind = "crate", surfacePath = "Workspace.Map.Floor" })
	t.eq(rep.status, "pass")
	t.eq(rep.checks.P2.measured.gap, 0)
	t.eq(rep.checks.P2.measured.restsOn, "Workspace.Map.Floor")
end)

t.test("place: a floating, off-grid, unanchored crate is fixed and re-verified", function()
	local m =
		newModel("Crate3", { { name = "Box", pos = { 20, 6, 5 }, size = { 3, 3, 3 }, yaw = 22, anchored = false } })
	local rep = Placement.place(m, { kind = "crate" }, { parent = map })
	t.eq(rep.status, "pass", table.concat(rep.failed, ",") .. " " .. serde.encode("json", rep.checks))
	t.truthy(#rep.fixesApplied >= 2, "applied fixes")
	t.eq(y(m), 1.5)
	t.eq(m:FindFirstChild("Box").Anchored, true)
	t.truthy(rep.passes >= 2)
end)

t.test("place: NPC is turned to face the player area and snapped down", function()
	local m = newModel("Guide", { { name = "Root", pos = { -10, 4, 0 }, size = { 2, 6, 1 }, yaw = 0 } })
	local rep = Placement.place(m, { kind = "npc", face = { target = { -10, 3, 30 } } }, { parent = map })
	t.eq(rep.status, "pass", serde.encode("json", rep.checks.P4))
	t.truthy(rep.checks.P4.measured.facingOffDeg < 1)
	t.eq(y(m), 3)
end)

t.test("place: a pitched crate is stood upright", function()
	local m = newModel("Crate4", { { name = "Box", pos = { 30, 2, 5 }, size = { 3, 3, 3 } } })
	m.Parent = map
	local p = m:FindFirstChild("Box")
	p.CFrame = CFrame.new(30, 2, 5) * CFrame.Angles(0, 0, math.rad(25))
	local before = Placement.verify(m, { kind = "crate" })
	t.eq(before.checks.P3.status, "fail")
	local rep = Placement.place(m, { kind = "crate" })
	t.eq(rep.status, "pass", serde.encode("json", rep.failed))
end)

t.test("place: a crate cutting into a wall is nudged out of it", function()
	local wall = newModel("WallA", { { name = "W", pos = { 100, 4, 5 }, size = { 1, 8, 8 } } })
	wall.Parent = map
	local m = newModel("CrateB", { { name = "Box", pos = { 99.5, 1.5, 5 }, size = { 3, 3, 3 } } })
	m.Parent = map
	local before = Placement.verify(m, { kind = "crate" })
	t.eq(before.checks.P5.status, "fail")
	t.eq(before.checks.P5.measured.overlaps[1].depth, 1.5)
	local rep = Placement.place(m, { kind = "crate" })
	t.eq(rep.checks.P5.status, "pass", serde.encode("json", rep.checks.P5))
	t.eq(Placement.world.pivot(m).Position.X, 98)
end)

t.test("an unfixable intent stops after the passes and stays failed", function()
	local m = newModel("Crate5", { { name = "Box", pos = { 50, 1.5, 5 }, size = { 3, 3, 3 } } })
	local rep = Placement.place(m, { kind = "crate", expectedSize = { 9, 9, 9 } }, { parent = map })
	t.eq(rep.status, "fail")
	t.eq(rep.failed[1], "P1")
	t.truthy(rep.passes <= Placement.config.maxPasses + 1)
end)

t.test("the intent is stored on the model and used when verify gets none", function()
	local m = newModel("Door1", { { name = "Panel", pos = { 60, 3.5, 5 }, size = { 4, 7, 0.5 } } })
	Placement.place(m, { kind = "door", face = { target = { 60, 3.5, -20 } } }, { parent = map })
	t.truthy(m:GetAttribute("PlacementIntent"))
	local rep = Placement.verify(m)
	t.eq(rep.status, "pass", serde.encode("json", rep.failed))
	t.eq(rep.intentSource, "attribute PlacementIntent")
end)

t.test("without an intent the kind is inferred from the name and a door must declare its facing", function()
	local m = newModel("Door2", { { name = "Panel", pos = { 70, 3.5, 5 }, size = { 4, 7, 0.5 } } })
	m.Parent = map
	local rep = Placement.verify(m)
	t.eq(rep.kind, "door")
	t.eq(rep.checks.P4.status, "fail")
	t.eq(rep.intentSource, "inferred from the name")
end)

t.test("connections and mirrored pairs resolve other instances", function()
	local s1 = newModel("StairsA", { { name = "S", pos = { 80, 4, 5 }, size = { 4, 8, 8 } } })
	s1.Parent = map
	local s2 = newModel("StairsB", { { name = "S", pos = { 80, 4, -3.4 }, size = { 4, 8, 8 } } })
	s2.Parent = map
	local rep = Placement.verify(
		s1,
		{ kind = "stairs", connect = { { at = "front", to = "Workspace.Map.StairsB", toAt = "back" } } }
	)
	t.eq(rep.checks.P7.status, "fail")
	t.eq(rep.checks.P7.measured.connections[1].dist, 0.4)
	local fix = rep.checks.P7.fixes[1]
	t.eq(fix.action, "moveBy")
end)

t.test("siblings with the same base name form a group", function()
	for i = 1, 3 do
		local m = newModel("Post " .. i, { { name = "P", pos = { 90 + i * 6, 3, 5 }, size = { 1, 6, 1 } } })
		m.Parent = map
	end
	local odd = newModel("Post 4", { { name = "P", pos = { 90 + 24, 4, 5 }, size = { 1, 8, 1 } } })
	odd.Parent = map
	local rep = Placement.verify(odd, { kind = "prop", group = {} })
	t.eq(rep.checks.P7.status, "fail")
	local ok = Placement.verify(map:FindFirstChild("Post 2"), { kind = "prop", group = {} })
	t.eq(ok.checks.P7.status, "pass", serde.encode("json", ok.checks.P7))
end)

t.test("scan visits every object, skips the ignored ones with a reason, and counts pass and fail", function()
	local extra = Instance.new("Folder")
	extra.Name = "Extras"
	extra.Parent = map
	local bad = newModel("Rock1", { { name = "R", pos = { 0, 9, 40 }, size = { 3, 3, 3 } } })
	bad.Parent = extra
	local hidden = newModel("Secret", { { name = "S", pos = { 0, 9, 50 }, size = { 3, 3, 3 } } })
	hidden:SetAttribute("PlacementIgnore", true)
	hidden.Parent = extra
	local scan = Placement.scan(root, { game = "test", scorer = "critic", emit = false })
	t.eq(scan.kind, "placement-scan")
	t.eq(scan.game, "test")
	t.eq(scan.scorer, "critic")
	t.truthy(scan.models_total >= 12, "models " .. scan.models_total)
	t.eq(scan.models_total, #scan.models)
	t.eq(scan.summary.pass + scan.summary.fail, scan.models_total)
	local paths = {}
	for _, m in scan.models do
		paths[m.path] = m.status
	end
	t.eq(paths["Workspace.Map.Extras.Rock1"], "fail")
	t.eq(paths["Workspace.Map.Extras.Secret"], nil)
	local sk
	for _, s in scan.skipped do
		if s.path == "Workspace.Map.Extras.Secret" then
			sk = s.reason
		end
	end
	t.truthy(sk and string.find(sk, "NO REASON GIVEN"), "ignore without reason is flagged: " .. tostring(sk))
	t.truthy(paths["Workspace.Map.Floor"], "the floor part is scanned too")
	t.eq(string.len(scan.fingerprint), 8)
	local again = Placement.scan(root, { emit = false })
	t.eq(again.fingerprint, scan.fingerprint)
end)

t.test("the Floor part is a ground kind: not asked to rest on anything", function()
	local rep = Placement.verify(floor)
	t.eq(rep.kind, "ground")
	t.eq(rep.checks.P2.status, "skip")
end)

t.done()
