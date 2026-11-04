--!strict
local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local ContentProvider = game:GetService("ContentProvider")

local t0 = os.clock()
local marks: { { name: string, t: number } } = {}

local function mark(name: string)
	local t = os.clock() - t0
	table.insert(marks, { name = name, t = t })
	print(("[join] %6.2fs  %s"):format(t, name))
end

mark("client script started")

task.spawn(function()
	if not game:IsLoaded() then
		game.Loaded:Wait()
	end
	mark("game loaded")
end)

local player = Players.LocalPlayer
task.spawn(function()
	local character = player.Character or player.CharacterAdded:Wait()
	mark("character spawned")
	if character:FindFirstChild("HumanoidRootPart") == nil then
		character:WaitForChild("HumanoidRootPart")
	end
	mark("character root ready")
end)

task.spawn(function()
	local gui = player:WaitForChild("PlayerGui")
	mark("PlayerGui ready")
	local first: Instance? = gui:FindFirstChildWhichIsA("ScreenGui")
	if first == nil then
		first = gui.ChildAdded:Wait()
	end
	mark("first ScreenGui: " .. (first :: Instance).Name)
end)

local bindable = ReplicatedStorage:FindFirstChild("JoinMark")
if bindable and bindable:IsA("BindableEvent") then
	(bindable :: BindableEvent).Event:Connect(function(name: string)
		mark(name)
	end)
end

task.delay(60, function()
	print("[join] MARKS (paste into JoinTimeline.phases):")
	local parts = {}
	for _, m in marks do
		table.insert(parts, ('{ name = "%s", t = %.3f }'):format(m.name, m.t))
	end
	print("{ " .. table.concat(parts, ", ") .. " }")
	print("[join] in-flight content requests at 60 s: " .. tostring(ContentProvider.RequestQueueSize))
end)
