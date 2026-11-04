--!nocheck
local t = require("../../../../../systems/_check/harness")
local ArgScan = require("../../../input-validation-auditor/scripts/ArgScan")
local FilterScan = require("../FilterScan")

print("FilterScan")

t.test("unfiltered pet name broadcast and label text are flagged", function()
	local src = [[
Rename.OnServerEvent:Connect(function(player, petName)
	pet.Name = petName
end)
Say.OnServerEvent:Connect(function(player, message)
	Remotes.Chat:FireAllClients(player.Name, message)
end)
]]
	local f = FilterScan.scanHandlers(ArgScan.extract(src))
	t.eq(#f, 2)
	t.eq(f[1].sink, ".Name assignment")
	t.eq(f[2].sink, "FireAllClients")
end)

t.test("a handler that filters is clean", function()
	local src = [[
Rename.OnServerEvent:Connect(function(player, petName)
	local ok, result = pcall(function()
		return TextService:FilterStringAsync(petName, player.UserId)
	end)
	if ok then
		pet.Name = result:GetNonChatStringForBroadcastAsync()
	end
end)
]]
	t.eq(#FilterScan.scanHandlers(ArgScan.extract(src)), 0)
end)

t.test("non-text parameters are ignored", function()
	local src = [[
Buy.OnServerEvent:Connect(function(player, itemId, qty)
	table.insert(Data[player].items, itemId)
end)
]]
	t.eq(#FilterScan.scanHandlers(ArgScan.extract(src)), 0)
end)

t.test("a client script that displays remote text is a lead, TextChatService users are not", function()
	local code = "Remote.OnClientEvent:Connect(function(msg)\n\tlabel.Text = msg\nend)"
	t.eq(#FilterScan.scanClient("StarterGui.Chat", code), 1)
	t.eq(#FilterScan.scanClient("StarterGui.Chat", code .. "\nTextChatService"), 0)
end)

t.test("report", function()
	t.eq(FilterScan.report({}), "FILTERSCAN: 0 leads")
end)

t.done()
