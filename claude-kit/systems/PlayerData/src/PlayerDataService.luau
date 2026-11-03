--!strict
--[[
	Roblox glue for PlayerData: wires Players.PlayerAdded / PlayerRemoving, autosave and BindToClose.
	Server only. Put PlayerData.luau and this file side by side in ServerScriptService (or ServerStorage).

	local PlayerDataService = require(script.Parent.PlayerDataService)
	PlayerDataService.Start({ storeName = "PlayerData_v1", template = { coins = 0 } })
	local data = PlayerDataService.Get(player)   -- nil until loaded or after the player left
	data.coins += 10                             -- saved by autosave / on leave / on shutdown
]]
local DataStoreService = game:GetService("DataStoreService")
local Players = game:GetService("Players")
local RunService = game:GetService("RunService")

local PlayerData = require(script.Parent.PlayerData)

export type StartOptions = {
	storeName: string,
	template: PlayerData.Data,
	version: number?,
	migrations: { [number]: (PlayerData.Data) -> PlayerData.Data }?,
	autosaveInterval: number?,
	lockTimeout: number?,
}

local Service = {}

local core: PlayerData.PlayerData? = nil
local loaded = Instance.new("BindableEvent") -- fires (player, data) when a profile finished loading
Service.Loaded = loaded.Event

local function keyOf(player: Player): string
	return "Player_" .. player.UserId
end

-- Studio without API access (or an unpublished place) has no DataStore: fall back to an in-memory store so
-- development still works. Nothing is saved in that case.
local function memoryStore(): PlayerData.StoreLike
	local rows: { [string]: any } = {}
	return {
		UpdateAsync = function(_, key: string, transform: (any) -> any)
			local new = transform(rows[key])
			if new ~= nil then
				rows[key] = new
			end
			return new
		end,
	}
end

function Service.Start(opts: StartOptions)
	assert(core == nil, "PlayerDataService.Start called twice")
	local store: PlayerData.StoreLike
	local okStore, ds = pcall(function()
		return DataStoreService:GetDataStore(opts.storeName)
	end)
	if okStore and not (RunService:IsStudio() and game.GameId == 0) then
		store = ds :: any
	else
		warn("[PlayerData] no DataStore available: using in-memory store, NOTHING IS SAVED")
		store = memoryStore()
	end

	local pd = PlayerData.new({
		store = store,
		jobId = game.JobId ~= "" and game.JobId or "studio-" .. tostring(os.clock()),
		template = opts.template,
		version = opts.version,
		migrations = opts.migrations,
		autosaveInterval = opts.autosaveInterval,
		lockTimeout = opts.lockTimeout,
		now = os.time,
		wait = task.wait,
		spawn = function(fn)
			task.spawn(fn)
		end,
		log = function(msg)
			warn("[PlayerData] " .. msg)
		end,
		onLost = function(session, why)
			local uid = tonumber(string.match(session.Key, "%d+$"))
			local player = uid and Players:GetPlayerByUserId(uid)
			if player then
				player:Kick("Your data session ended (" .. why .. "). Please rejoin.")
			end
		end,
	})
	core = pd

	local function onAdded(player: Player)
		local session, err = pd:LoadAsync(keyOf(player), function()
			return player.Parent ~= Players
		end)
		if session == nil then
			if err ~= "cancelled" then
				player:Kick("Could not load your data (" .. tostring(err) .. "). Please rejoin in a minute.")
			end
			return
		end
		loaded:Fire(player, session.Data)
	end
	Players.PlayerAdded:Connect(onAdded)
	for _, p in Players:GetPlayers() do
		task.spawn(onAdded, p)
	end

	Players.PlayerRemoving:Connect(function(player)
		local session = pd:GetSession(keyOf(player))
		if session then
			pd:ReleaseAsync(session)
		end
	end)

	task.spawn(function()
		while true do
			task.wait(10)
			pd:AutosaveDue()
		end
	end)

	game:BindToClose(function()
		pd:ReleaseAll(25)
	end)
end

-- The live data table of a loaded player, or nil.
function Service.Get(player: Player): PlayerData.Data?
	local c = core
	if c == nil then
		return nil
	end
	local s = c:GetSession(keyOf(player))
	return if s and s.State == "active" then s.Data else nil
end

-- Yields until the player's data is loaded; nil if they left or the load failed.
function Service.WaitFor(player: Player, timeout: number?): PlayerData.Data?
	local deadline = os.clock() + (timeout or 60)
	while player.Parent == Players and os.clock() < deadline do
		local d = Service.Get(player)
		if d then
			return d
		end
		task.wait(0.2)
	end
	return nil
end

-- Save now (e.g. right after a purchase). Returns true when written.
function Service.SaveNow(player: Player): boolean
	local c = core
	local s = c and c:GetSession(keyOf(player))
	if c and s then
		return c:SaveAsync(s)
	end
	return false
end

return Service
