--!nocheck
-- Run: lune run LoopScan.test.luau   (from the kit's systems folder, see check-scripts.sh)
local t = require("../../../../../systems/_check/harness")
local LoopScan = require("../LoopScan")

local function kinds(src)
	return LoopScan.summarise(LoopScan.scan(src))
end

t.test("a clean event-driven script has no findings", function()
	local src = [[
local Players = game:GetService("Players")
Players.PlayerAdded:Connect(function(p)
	print(p.Name)
end)
]]
	t.eq(next(kinds(src)), nil)
end)

t.test("Heartbeat callback is reported and expensive calls inside it are flagged", function()
	local src = [[
RunService.Heartbeat:Connect(function(dt)
	for _, p in workspace:GetDescendants() do
		p.Name = "x"
	end
end)
local x = workspace:GetChildren()
]]
	local k = kinds(src)
	t.eq(k["per-frame-callback"], 1)
	t.eq(k["expensive-in-frame-loop"], 1)
end)

t.test("code after the callback ends is not charged to it", function()
	local src = [[
RunService.RenderStepped:Connect(function()
	camera.CFrame = cf
end)
local list = workspace:GetDescendants()
]]
	t.eq(kinds(src)["expensive-in-frame-loop"], nil)
end)

t.test("tight wait loops and legacy wait are flagged, slow loops are not", function()
	local fast = kinds([[
while true do
	task.wait()
	update()
end
]])
	t.eq(fast["tight-wait-loop"], 1)
	local slow = kinds([[
while true do
	task.wait(5)
	update()
end
]])
	t.eq(slow["tight-wait-loop"], nil)
	local legacy = kinds([[
while true do
	wait(1)
end
]])
	t.eq(legacy["legacy-wait"], 1)
end)

t.test("expensive calls in a repeating loop are flagged", function()
	local src = [[
while true do
	task.wait(1)
	for _, v in workspace:GetDescendants() do
		v.Name = v.Name
	end
end
]]
	t.eq(kinds(src)["expensive-in-wait-loop"], 1)
end)

t.test("comments are ignored", function()
	t.eq(next(kinds("-- RunService.Heartbeat:Connect(function()\n")), nil)
end)

t.done()
