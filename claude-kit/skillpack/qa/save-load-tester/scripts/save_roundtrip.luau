--!strict
local Players = game:GetService("Players")
local ServerScriptService = game:GetService("ServerScriptService")

local PHASE: string = "write"
local MODULE_NAME = "PlayerDataService"
local FIELD = "qaProbe"
local STAMP = "probe-1"

local function firstPlayer(): Player?
	local deadline = os.clock() + 15
	while os.clock() < deadline do
		local p = Players:GetPlayers()[1]
		if p then
			return p
		end
		task.wait(0.25)
	end
	return nil
end

local function run(): string
	local player = firstPlayer()
	if player == nil then
		return "FAIL no player joined within 15 s (start a playtest with Test, not Run)"
	end
	local moduleScript = ServerScriptService:FindFirstChild(MODULE_NAME)
	if moduleScript == nil or not moduleScript:IsA("ModuleScript") then
		return `FAIL {MODULE_NAME} ModuleScript not found in ServerScriptService`
	end
	local service = require(moduleScript) :: any
	local data = service.WaitFor(player, 20)
	if data == nil then
		return "FAIL player data did not load in 20 s (check Output for DataStore errors; is Studio API access on?)"
	end
	if PHASE == "write" then
		data[FIELD] = STAMP
		local saved = service.SaveNow(player)
		return if saved
			then `PASS wrote {FIELD}={STAMP} and the save returned true; stop the playtest and run phase "read"`
			else "FAIL SaveNow returned false"
	end
	local value = data[FIELD]
	if value == STAMP then
		return `PASS {FIELD} survived the round trip ({tostring(value)})`
	end
	return `FAIL {FIELD} expected {STAMP}, got {tostring(value)}`
end

return run()
