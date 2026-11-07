local fs = require("@lune/fs")
local luau = require("@lune/luau")
local process = require("@lune/process")
local roblox = require("@lune/roblox")
local serde = require("@lune/serde")
local Instance = roblox.Instance
local Vector3 = roblox.Vector3
local CFrame = roblox.CFrame
local Color3 = roblox.Color3

local args = process.args
local runnerPath, outPath = args[1], args[2]
local variant, inject = "plain", false
local pre: { string } = {}
for i = 3, #args do
	if args[i] == "inject" then
		inject = true
	elseif string.sub(args[i], 1, 4) == "pre:" then
		table.insert(pre, string.sub(args[i], 5))
	else
		variant = args[i]
	end
end

local dm = Instance.new("DataModel")
dm.Name = "FixtureGame"
local ws = dm:GetService("Workspace")

local function folder(name: string, parent: any)
	local f = Instance.new("Folder")
	f.Name = name
	f.Parent = parent
	return f
end
local function part(name: string, parent: any, o: any?)
	o = o or {}
	local p = Instance.new(o.class or "Part")
	p.Name = name
	p.Anchored = if o.anchored == nil then true else o.anchored
	p.CanCollide = if o.cc == nil then true else o.cc
	p.CanTouch = if o.ct == nil then true else o.ct
	p.CanQuery = if o.cq == nil then true else o.cq
	p.Size = o.size or Vector3.new(2, 1, 2)
	p.Transparency = o.tr or 0
	p.Color = o.color or Color3.fromRGB(120, 140, 90)
	p.CFrame = CFrame.new(o.pos or Vector3.new(0, 0, 0))
	p.Parent = parent
	return p
end

local decor = folder("Scenery", ws)
for i = 1, 6 do
	part("Pebble" .. i, decor, { cc = false, pos = Vector3.new(i * 5, 1, 40) })
end
local fern = part("Fern", decor, { cc = false, pos = Vector3.new(0, 1, 50) })
local decal = Instance.new("Decal")
decal.Texture = "rbxassetid://1"
decal.Parent = fern
local lamp = part("LampGlow", decor, { cc = false, pos = Vector3.new(0, 4, 50) })
local light = Instance.new("PointLight")
light.Range = 14
light.Parent = lamp
local mass = folder("Masonry", ws)
part("Slab", mass, { size = Vector3.new(30, 30, 30), pos = Vector3.new(100, 15, 0) })
part("Core", mass, { size = Vector3.new(4, 4, 4), pos = Vector3.new(100, 15, 0) })
part("Edge", mass, { size = Vector3.new(4, 4, 4), pos = Vector3.new(113, 15, 0) })
local left = folder("Leftovers", ws)
part("Stray1", left, { tr = 1, cc = false, cq = false, ct = false })
part("Stray2", left, { tr = 1, cc = false })
part("InvisibleWall", left, { tr = 1, cc = true, size = Vector3.new(20, 20, 1), pos = Vector3.new(0, 10, -60) })
local dup = folder("Duplicates", ws)
for _ = 1, 3 do
	part("Plank", dup, { pos = Vector3.new(-30, 1, 0), size = Vector3.new(8, 0.5, 2) })
end
for _ = 1, 2 do
	part("Pane", dup, { pos = Vector3.new(-30, 6, 0), tr = 0.5, size = Vector3.new(8, 4, 0.2) })
end
local haz = folder("Hazards", ws)
part("KillBrick", haz, { cc = false, color = Color3.fromRGB(200, 0, 0), pos = Vector3.new(60, 1, 0) })
part("Lava", haz, { cc = false, pos = Vector3.new(70, 1, 0) })
part("Waypoint", haz, { cc = false, tr = 1, cq = false, ct = false, pos = Vector3.new(80, 1, 0) })
local truss = part("RopeRail", haz, { class = "TrussPart", cc = true, pos = Vector3.new(90, 5, 0) })
truss.Size = Vector3.new(2, 10, 2)
local car = Instance.new("Model")
car.Name = "Buggy"
car.Parent = ws
part("Hood", car, { cc = false, pos = Vector3.new(0, 3, 90) })
part("Chassis", car, { cc = true, anchored = false, pos = Vector3.new(0, 2, 90) })
local seat = Instance.new("VehicleSeat")
seat.Name = "Driver"
seat.Parent = car
local npc = Instance.new("Model")
npc.Name = "Guard"
npc.Parent = ws
part("Hand", npc, { cc = false, pos = Vector3.new(0, 3, 70) })
Instance.new("Humanoid").Parent = npc
local doorM = Instance.new("Model")
doorM.Name = "Entry"
doorM.Parent = ws
part("Leaf", doorM, { cc = false, pos = Vector3.new(0, 3, 30) })
local doorScript = Instance.new("Script")
doorScript.Name = "Swing"
doorScript.Parent = doorM
local coin = part("Gem", ws, { cc = false, pos = Vector3.new(0, 1, 20) })
coin:AddTag("Collectable")
local note = part("Beacon", ws, { cc = false, pos = Vector3.new(0, 1, 25) })
note:SetAttribute("Kind", "x")
local axle = part("Axle", ws, { cc = false, pos = Vector3.new(0, 1, 10) })
local wheel = part("Disc", ws, { cc = false, pos = Vector3.new(2, 1, 10) })
local weld = Instance.new("WeldConstraint")
weld.Part0 = axle
weld.Part1 = wheel
weld.Parent = axle
part("Wall", ws, { size = Vector3.new(30, 12, 1), pos = Vector3.new(0, 6, -20), color = Color3.fromRGB(200, 190, 170) })
part("Crate", ws, { anchored = false, pos = Vector3.new(0, 1, -10) })
local sss = dm:GetService("ServerScriptService")
local s = Instance.new("Script")
s.Name = "Game"
local src =
	"local k = workspace.Hazards.KillBrick\nk.Touched:Connect(function(hit) end)\nlocal w = workspace.Hazards:WaitForChild('Waypoint')\nlocal p = Instance.new('Part')\nif p:IsA('Part') then end\n"
if variant == "query" then
	src ..= "local r = workspace:Raycast(Vector3.zero, Vector3.new(0, -10, 0))\n"
elseif variant == "touch" then
	src ..= "for _, d in workspace:GetDescendants() do d.Touched:Connect(print) end\n"
end
s.Source = src
s.Parent = sss
local function printTo(buf: { string })
	return function(...)
		local parts = { ... }
		for i, v in parts do
			parts[i] = tostring(v)
		end
		table.insert(buf, table.concat(parts, " "))
	end
end

local sharedBuf: { string } = {}
local function install(): any
	local game = setmetatable({
		Name = "FixtureGame",
		PlaceId = 0,
		GetService = function(_, name: string): any
			if name == "HttpService" then
				return {
					JSONEncode = function(_, v: any)
						return serde.encode("json", v)
					end,
				}
			elseif name == "ChangeHistoryService" then
				return { SetWaypoint = function() end }
			elseif name == "Stats" then
				return {
					InstanceCount = #dm:GetDescendants(),
					GetTotalMemoryUsageMb = function()
						return 123.456
					end,
				}
			end
			return dm:GetService(name)
		end,
	}, {
		__index = function(_, k)
			local v = (dm :: any)[k]
			if type(v) == "function" then
				return function(_, ...)
					return v(dm, ...)
				end
			end
			return v
		end,
	})
	return game
end

local function runFile(path: string, patch: ((string) -> string)?)
	local code = fs.readFile(path)
	if patch then
		code = patch(code)
	end
	local env: any = {
		game = install(),
		workspace = ws,
		Instance = Instance,
		Enum = roblox.Enum,
		Vector3 = roblox.Vector3,
		CFrame = roblox.CFrame,
		Color3 = roblox.Color3,
		typeof = roblox.typeof or function(v: any)
			return typeof(v)
		end,
		print = printTo(sharedBuf),
	}
	local f = luau.load(code, { environment = env, debugName = path })
	f()
end

for _, p in pre do
	runFile(p, nil)
end
runFile(runnerPath, function(code)
	if inject then
		code = string.gsub(
			code,
			"afterApplyHook = nil,",
			"afterApplyHook = function(list) for _, d in list do if d.Name == 'Pebble2' then d.Color = Color3.fromRGB(255, 0, 0) end end end,"
		)
	end
	return code
end)
fs.writeFile(outPath, table.concat(sharedBuf, "\n") .. "\n")
