--!nocheck
local t = require("../../../../../systems/_check/harness")
local DependencyMap = require("../DependencyMap")
local RequireGraph = require("../../../require-cycle-finder/scripts/RequireGraph")

local server = [==[
local Players = game:GetService("Players")
local CollectionService = game:GetService("CollectionService")
local Shop = require(script.Parent.ShopData)
BuyItem.OnServerEvent:Connect(function(player, id) end)
Ghost.OnServerEvent:Connect(function() end)
for _, part in CollectionService:GetTagged("Coin") do
	part:SetAttribute("Value", 5)
end
-- Commented:FireServer()
]==]
local client = [==[
local RS = game:GetService("ReplicatedStorage")
BuyItem:FireServer("sword")
Missing:FireServer()
print(part:GetAttribute("Value"))
]==]

t.test("maps remotes to the scripts that fire and handle them", function()
	local map = DependencyMap.scan({ Server = server, Client = client }, RequireGraph)
	t.eq(map.remotes.BuyItem, { fires = { "Client" }, handles = { "Server" } })
	t.eq(map.remotes.Commented, nil)
end)

t.test("orphans list fired-only and handled-only remotes", function()
	local o = DependencyMap.orphans(DependencyMap.scan({ Server = server, Client = client }, RequireGraph))
	t.eq(o.onlyFired, { "Missing" })
	t.eq(o.onlyHandled, { "Ghost" })
end)

t.test("collects modules, tags, attributes and services", function()
	local map = DependencyMap.scan({ Server = server, Client = client }, RequireGraph)
	t.eq(map.requires.ShopData, { "Server" })
	t.eq(map.tags.Coin, { "Server" })
	t.eq(map.attributes.Value, { "Client", "Server" })
	t.eq(map.services.Players, { "Server" })
	t.eq(map.services.ReplicatedStorage, { "Client" })
end)

t.test("remoteTable renders one row per remote, sorted", function()
	local text = DependencyMap.remoteTable(DependencyMap.scan({ Server = server, Client = client }, RequireGraph))
	t.truthy(string.find(text, "| BuyItem | Client | Server |", 1, true))
	t.truthy(string.find(text, "| Missing | Client |  |", 1, true))
end)

t.done()
