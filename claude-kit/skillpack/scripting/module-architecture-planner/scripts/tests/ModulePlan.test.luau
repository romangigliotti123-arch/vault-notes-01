--!nocheck
-- Run: lune run ModulePlan.test.luau   (from the kit's systems folder, see check-scripts.sh)
local t = require("../../../../../systems/_check/harness")
local ModulePlan = require("../ModulePlan")
local RequireGraph = require("../../../require-cycle-finder/scripts/RequireGraph")

local sources = {
	ShopService = "local DataStoreService = game:GetService('DataStoreService')\nlocal Config = require(script.Parent.Config)\nBuy.OnServerEvent:Connect(f)",
	ShopUI = "local Players = game:GetService('Players')\nlocal gui = Players.LocalPlayer.PlayerGui\nlocal Config = require(script.Parent.Config)",
	Config = "local M = {}\nreturn M",
	Greedy = "local x = Players.LocalPlayer\nBuy.OnServerEvent:Connect(f)\nBuy:FireServer()",
	BadShared = "local S = require(script.Parent.ShopService)",
}

t.test("classifies side from the APIs a file uses", function()
	local plan = ModulePlan.analyse(sources, RequireGraph)
	t.eq(plan.modules.ShopService.side, "server")
	t.eq(plan.modules.ShopUI.side, "client")
	t.eq(plan.modules.Config.side, "shared")
	t.truthy(plan.modules.Greedy.mixed)
end)

t.test("layout lists modules per side, sorted", function()
	local plan = ModulePlan.analyse(sources, RequireGraph)
	t.eq(plan.layout.server, { "ShopService" })
	t.eq(plan.layout.client, { "ShopUI" })
	t.eq(plan.layout.shared, { "BadShared", "Config", "Greedy" })
end)

t.test("a shared module requiring server code is a violation", function()
	local plan = ModulePlan.analyse(sources, RequireGraph)
	t.eq(#plan.violations, 1)
	t.truthy(string.find(plan.violations[1], "BadShared (shared) requires ShopService (server)", 1, true))
end)

t.test("client requiring server and server requiring client are violations", function()
	local plan = ModulePlan.analyse({
		C = "local P = Players.LocalPlayer\nlocal S = require(script.Parent.S)",
		S = "local D = game:GetService('DataStoreService')\nlocal C = require(script.Parent.C)",
	}, RequireGraph)
	t.eq(#plan.violations, 2)
end)

t.test("big or mixed modules become split candidates, largest first", function()
	local big = {}
	for i = 1, 320 do
		big[i] = "local a" .. i .. " = 1"
	end
	local plan = ModulePlan.analyse(
		{ Big = table.concat(big, "\n"), Greedy = sources.Greedy, Small = "return {}" },
		RequireGraph
	)
	t.eq(ModulePlan.splitCandidates(plan), { "Big", "Greedy" })
end)

t.test("function count triggers a split reason", function()
	local fns = {}
	for i = 1, 21 do
		fns[i] = "function M.f" .. i .. "()\nend"
	end
	local plan = ModulePlan.analyse({ Many = table.concat(fns, "\n") }, RequireGraph)
	t.eq(#plan.modules.Many.splitReasons, 1)
end)

t.done()
