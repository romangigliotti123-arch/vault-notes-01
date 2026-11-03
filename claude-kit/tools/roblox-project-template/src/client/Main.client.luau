--!strict
-- Client entry point. Replace with the game's bootstrap (controllers started in order).
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local Config = require(ReplicatedStorage:WaitForChild("Shared"):WaitForChild("Config"))
print(`[{Config.GameName}] client started`)
