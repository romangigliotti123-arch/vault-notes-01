--!nocheck
local t = require("../../../../../systems/_check/harness")
local ArgScan = require("../../../input-validation-auditor/scripts/ArgScan")
local AuthorityScan = require("../AuthorityScan")

print("AuthorityScan")

t.test("client-sent reward and damage are flagged, an item id is not", function()
	local src = [[
Claim.OnServerEvent:Connect(function(player, reward)
	Data[player].coins += reward
end)
Hit.OnServerEvent:Connect(function(player, target, damage)
	target.Humanoid.Health -= damage
end)
Equip.OnServerEvent:Connect(function(player, itemId)
	Data[player].equipped = lookup(itemId)
end)
]]
	local f = AuthorityScan.scanHandlers(ArgScan.extract(src))
	t.eq(#f, 2)
	t.eq(f[1].severity, "CRITICAL")
	t.truthy(string.find(f[1].where, "Claim", 1, true))
	t.eq(f[2].severity, "HIGH")
end)

t.test("a parameter that is read but only used as a lookup key is not flagged", function()
	local src = [[
Buy.OnServerEvent:Connect(function(player, itemName)
	local price = Prices[itemName]
	Data[player].coins -= price
end)
]]
	t.eq(#AuthorityScan.scanHandlers(ArgScan.extract(src)), 0)
end)

t.test("server-only APIs in replicated containers are HIGH, in ServerScriptService they are fine", function()
	local code = "local ds = game:GetService('DataStoreService')"
	t.eq(#AuthorityScan.scanContainer("ReplicatedStorage.Modules.Economy", code), 1)
	t.eq(#AuthorityScan.scanContainer("ServerScriptService.Economy", code), 0)
	t.eq(#AuthorityScan.scanContainer("Workspace.Shop.Script", "ProcessReceipt = function() end"), 1)
end)

t.test("prompt handled on the client is reported", function()
	local f = AuthorityScan.scanInteractions(
		"prompt.Triggered:Connect(function() end)",
		"StarterPlayer.StarterPlayerScripts.Shop"
	)
	t.eq(#f, 1)
	t.eq(#AuthorityScan.scanInteractions("prompt.Triggered:Connect(function() end)", "ServerScriptService.Shop"), 0)
end)

t.test("report", function()
	t.eq(AuthorityScan.report({}), "AUTHORITY: 0 leads")
end)

t.done()
