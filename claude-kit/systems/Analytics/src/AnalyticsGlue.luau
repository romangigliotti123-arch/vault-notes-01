--!strict
--[[
	Roblox glue for Analytics: builds the wrapper from AnalyticsService and the real enums. Server only.

	local Analytics = require(script.Parent.AnalyticsGlue).Create()
	Analytics:Onboarding(player, 1, "Spawned")
	Analytics:Economy(player, "Sink", "Coins", 100, newBalance, "Shop", "sword_basic")
	Analytics:Funnel(player, "FirstPurchase", HttpService:GenerateGUID(false), 1, "OpenedShop")
]]
local AnalyticsService = game:GetService("AnalyticsService")
local Players = game:GetService("Players")

local Analytics = require(script.Parent.Analytics)

local Glue = {}

function Glue.Create(): Analytics.Analytics
	local a = Analytics.new({
		service = AnalyticsService,
		flowTypes = {
			Source = Enum.AnalyticsEconomyFlowType.Source,
			Sink = Enum.AnalyticsEconomyFlowType.Sink,
		},
		progressionTypes = {
			Start = Enum.AnalyticsProgressionType.Start,
			Complete = Enum.AnalyticsProgressionType.Complete,
			Fail = Enum.AnalyticsProgressionType.Fail,
		},
		now = os.time,
		customFieldKeys = {
			Enum.AnalyticsCustomFieldKeys.CustomField01,
			Enum.AnalyticsCustomFieldKeys.CustomField02,
			Enum.AnalyticsCustomFieldKeys.CustomField03,
		},
		log = function(m)
			warn(m)
		end,
	})
	Players.PlayerRemoving:Connect(function(p)
		a:ClearPlayer(p)
	end)
	return a
end

return Glue
