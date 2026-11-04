--!strict
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
			print(HttpService:JSONEncode({ honeypot = name, userId = player.UserId, action = action }))
			if onAction then
				onAction(player, action, "honeypot:" .. name)
			end
		end)
	end
	return hp
end

return Service
