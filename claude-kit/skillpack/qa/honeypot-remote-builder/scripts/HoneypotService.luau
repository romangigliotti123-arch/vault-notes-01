--!strict
-- HoneypotService (Roblox glue, server only). Put in ServerScriptService next to Honeypot.luau.
-- Creates trap RemoteEvents that no legitimate script fires. Any firing is logged and scored; the action is applied by the callback.
-- Names are examples: choose names that look attractive but are not used by your game, and never reuse a real remote name.
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local HttpService = game:GetService("HttpService")
local Honeypot = require((script.Parent :: Instance):WaitForChild("Honeypot")) :: any

local Service = {}

local TRAPS = { "AddMoney", "GiveAllItems", "SetAdminLevel" }

function Service.Start(onAction: ((player: Player, action: string, reason: string) -> ())?): any
	local hp = Honeypot.new({ now = os.time })
	local folder = Instance.new("Folder")
	folder.Name = "Network"
	folder.Parent = ReplicatedStorage
	for _, name in TRAPS do
		local remote = Instance.new("RemoteEvent")
		remote.Name = name
		remote.Parent = folder
		remote.OnServerEvent:Connect(function(player: Player)
			local action = hp:Trip(player.UserId, name)
			-- log as JSON so it can be read with get_console_output or sent to the kit Analytics Custom event
			print(HttpService:JSONEncode({ honeypot = name, userId = player.UserId, action = action }))
			if onAction then
				onAction(player, action, "honeypot:" .. name)
			end
		end)
	end
	return hp
end

return Service
