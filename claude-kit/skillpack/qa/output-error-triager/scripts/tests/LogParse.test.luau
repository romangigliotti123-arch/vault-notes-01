--!nocheck
local t = require("../../../../../systems/_check/harness")
local LogParse = require("../LogParse")

local LOG = [[
12:00:01.100  Loading shop  -  Server - Shop:4
12:00:02.200  ServerScriptService.Shop:31: attempt to index nil with 'coins'  -  Server - Shop:31
12:00:02.201  Stack Begin
12:00:02.201  Script 'ServerScriptService.Shop', Line 31
12:00:02.201  Stack End
12:00:03.000  Infinite yield possible on 'Workspace.Map:WaitForChild("Spawn")'  -  Client - Loader:8
12:00:04.000  Players.Bob.PlayerGui.Hud:9: attempt to index nil with 'Text'  -  Client - Hud:9
12:00:05.000  ServerScriptService.Shop:31: attempt to index nil with 'coins'  -  Server - Shop:31
12:00:06.000  ServerScriptService.Shop:31: attempt to index nil with 'coins'  -  Server - Shop:31
12:00:07.000  fetch failed for 8412 retrying  -  Server - Http:3
]]

print("LogParse")

t.test("classify finds kind and side", function()
	local e = LogParse.classify("12:00:02.200  Shop:31: attempt to index nil with 'coins'  -  Server - Shop:31")
	t.eq(e.kind, "error")
	t.eq(e.side, "server")
	t.eq(LogParse.classify("12:00:03.000  Infinite yield possible on 'x'  -  Client - Loader:8").kind, "warn")
	t.eq(LogParse.classify("12:00:01.100  hello  -  Server - A:1").kind, "info")
end)

t.test("repeated server error ranks first with its count; stack lines fold into it", function()
	local g = LogParse.rank(LogParse.parse(LOG))
	t.eq(g[1].count, 3)
	t.eq(g[1].side, "server")
	t.truthy(string.find(g[1].example, "attempt to index nil with 'coins'", 1, true))
	for _, x in g do
		t.falsy(string.find(x.example, "Stack Begin", 1, true))
		t.falsy(string.find(x.example, "Line 31", 1, true))
	end
end)

t.test("client error and warning rank below it; info lines are ignored", function()
	local g = LogParse.rank(LogParse.parse(LOG))
	t.eq(#g, 4)
	t.truthy(g[1].score > g[2].score)
	for _, x in g do
		t.truthy(x.kind ~= "info")
	end
end)

t.test("ids and numbers are normalised so retries group together", function()
	t.eq(LogParse.normalise("fetch failed for 8412 retrying"), LogParse.normalise("fetch failed for 9977 retrying"))
end)

t.test("spam threshold is reported", function()
	local many = {}
	for _ = 1, 60 do
		table.insert(many, "12:00:00.000  Hud:9: attempt to index nil with 'Text'  -  Client - Hud:9")
	end
	local g = LogParse.rank(LogParse.parse(table.concat(many, "\n")))
	t.eq(g[1].count, 60)
	t.truthy(g[1].spam)
	t.truthy(string.find(LogParse.report(g), "SPAM", 1, true))
end)

t.test("report lists distinct problems and truncates", function()
	local r = LogParse.report(LogParse.rank(LogParse.parse(LOG)), 2)
	t.truthy(string.find(r, "4 distinct problems", 1, true))
	t.truthy(string.find(r, "... 2 more", 1, true))
end)

t.done()
