--!strict
--[[
	Roblox glue for DailyRewards. Server only.

	local DailyRewardsService = require(script.Parent.DailyRewardsService)
	DailyRewardsService.Start({
		config = { rewardCount = 7, graceDays = 0 },
		getData = PlayerDataService.Get,           -- (Player) -> data table or nil; data.Daily is the state table
		apply = function(player, data, cycleDay, streak) data.coins += 100 * cycleDay end,
		saveNow = PlayerDataService.SaveNow,
	})
	Client: local r = ReplicatedStorage.DailyReward:InvokeServer("claim")   -- or "status"
]]
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local DailyRewards = require(script.Parent.DailyRewards)

export type StartOptions = {
	config: DailyRewards.Config,
	getData: (Player) -> { [any]: any }?,
	apply: (player: Player, data: { [any]: any }, cycleDay: number, streak: number) -> (),
	saveNow: ((Player) -> boolean)?,
}

local Service = {}

function Service.Start(opts: StartOptions)
	local remote = Instance.new("RemoteFunction")
	remote.Name = "DailyReward"
	remote.Parent = ReplicatedStorage
	local busy: { [Player]: boolean } = {}

	remote.OnServerInvoke = function(player: Player, action: unknown)
		local data = opts.getData(player)
		if data == nil then
			return { ok = false, reason = "notloaded" }
		end
		data.Daily = DailyRewards.sanitize(data.Daily)
		local state = data.Daily :: DailyRewards.State
		if action == "status" then
			return DailyRewards.Status(state, os.time(), opts.config)
		elseif action == "claim" then
			if busy[player] then
				return { ok = false, reason = "busy" }
			end
			busy[player] = true
			local result = DailyRewards.Claim(state, os.time(), opts.config)
			if result.ok then
				-- same synchronous step as Claim: no yield between marking the day claimed and paying out
				opts.apply(player, data, result.cycleDay, result.streak)
			end
			busy[player] = nil
			if result.ok and opts.saveNow then
				task.spawn(opts.saveNow, player)
			end
			return result
		end
		return { ok = false, reason = "badrequest" }
	end
end

return Service
