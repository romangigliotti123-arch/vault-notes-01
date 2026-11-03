--!nocheck
-- Run from the kit's systems folder: lune run ../skillpack/qa/input-validation-auditor/scripts/tests/ArgScan.test.luau
local t = require("../../../../../systems/_check/harness")
local ArgScan = require("../ArgScan")

local SRC = [[
local Buy = game.ReplicatedStorage.Remotes.Buy
local Sell = game.ReplicatedStorage.Remotes.Sell
local Get = game.ReplicatedStorage.Remotes.Get

Buy.OnServerEvent:Connect(function(player, itemName, qty)
	local price = Prices[itemName] * qty
	Data[player].coins -= price
end)

Sell.OnServerEvent:Connect(function(player, itemName, qty)
	if typeof(itemName) ~= "string" or type(qty) ~= "number" or qty ~= qty then
		return
	end
	if os.clock() - last[player] < 0.5 then
		return
	end
	last[player] = os.clock()
	Data[player].coins += Prices[itemName] * math.floor(qty)
end)

Get.OnServerInvoke = function(player)
	return Data[player]
end
]]

print("ArgScan")

t.test("extracts events and functions with client params only", function()
	local hs = ArgScan.extract(SRC)
	t.eq(#hs, 3)
	t.eq(hs[1].remote, "Buy")
	t.eq(hs[1].params, { "itemName", "qty" })
	t.eq(hs[1].line, 5)
	t.eq(hs[3].kind, "function")
	t.eq(hs[3].params, {})
end)

t.test("handler bodies stop at the closing end", function()
	local hs = ArgScan.extract(SRC)
	t.truthy(string.find(hs[1].body, "coins -= price", 1, true))
	t.falsy(string.find(hs[1].body, "typeof", 1, true))
end)

t.test("the unvalidated handler gets unchecked and rate leads, the validated one gets none", function()
	local f = ArgScan.audit(ArgScan.extract(SRC))
	local by = {}
	for _, x in f do
		by[x.remote .. ":" .. x.param .. ":" .. x.kind] = true
	end
	t.truthy(by["Buy:itemName:unchecked"])
	t.truthy(by["Buy:qty:unchecked"])
	t.truthy(by["Buy:(rate):no-rate-limit"])
	for key in by do
		t.falsy(string.find(key, "^Sell"), key)
	end
	t.truthy(by["Get:(none):no-args"])
end)

t.test("a handler that calls a guard is not flagged for its arguments", function()
	local src = [[
Buy.OnServerEvent:Connect(function(player, item, qty)
	if not RemoteGuard.check(guards, item, qty) then
		return
	end
	grant(player, item, qty)
end)
]]
	local f = ArgScan.audit(ArgScan.extract(src))
	for _, x in f do
		t.truthy(x.kind ~= "unchecked", x.kind)
	end
end)

t.test("report counts leads", function()
	t.eq(ArgScan.report({}), "ARGSCAN: 0 leads")
	t.truthy(string.find(ArgScan.report(ArgScan.audit(ArgScan.extract(SRC))), "unchecked", 1, true))
end)

t.done()
