<!-- cold: rbx-luau/lifetimes-example.md | read when: read only to wire PlayerAdded/CharacterAdded/PlayerRemoving/BindToClose cleanup with the Cleaner above. -->

## From skills/rbx-luau/SKILL.md :: Player and character lifetimes with it:

Player and character lifetimes with it:
```lua
--!strict
local Players = game:GetService("Players")
local Cleaner = require(script.Parent.Cleaner)

local playerData: { [Player]: { coins: number } } = {}
local playerCleaners: { [Player]: Cleaner.Cleaner } = {}
local characterCleaners: { [Player]: Cleaner.Cleaner } = {}

local function onCharacterAdded(player: Player, character: Model)
	local cleaner = Cleaner.new()
	characterCleaners[player] = cleaner
	local humanoid = character:FindFirstChildOfClass("Humanoid")
	if humanoid then
		cleaner:add(humanoid.Died:Connect(function()
			print(player.Name, "died")
		end))
	end
end

local function onCharacterRemoving(player: Player)
	local cleaner = characterCleaners[player]
	if cleaner then
		characterCleaners[player] = nil
		cleaner:destroy()
	end
end

local function onPlayerAdded(player: Player)
	local cleaner = Cleaner.new()
	playerCleaners[player] = cleaner
	playerData[player] = { coins = 0 }
	cleaner:add(player.CharacterAdded:Connect(function(character)
		onCharacterAdded(player, character)
	end))
	cleaner:add(player.CharacterRemoving:Connect(function()
		onCharacterRemoving(player)
	end))
	if player.Character then
		onCharacterAdded(player, player.Character)
	end
end

local function onPlayerRemoving(player: Player)
	onCharacterRemoving(player)
	playerData[player] = nil
	local cleaner = playerCleaners[player]
	if cleaner then
		playerCleaners[player] = nil
		cleaner:destroy()
	end
end

Players.PlayerAdded:Connect(onPlayerAdded)
Players.PlayerRemoving:Connect(onPlayerRemoving)
for _, player in Players:GetPlayers() do
	task.spawn(onPlayerAdded, player)
end

game:BindToClose(function()
	for _, player in Players:GetPlayers() do
		onPlayerRemoving(player)
	end
end)
```
