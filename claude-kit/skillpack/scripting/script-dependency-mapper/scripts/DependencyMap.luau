--!strict
-- DependencyMap: which scripts touch which remotes, modules, CollectionService tags, attributes and services. Text only.
--   local RequireGraph = require(path.to.RequireGraph)   -- from require-cycle-finder/scripts, passed in so this file has no path requires
--   local map = DependencyMap.scan({ ["ServerScriptService/Shop"] = src1, ["StarterPlayerScripts/ShopUI"] = src2 }, RequireGraph)
--   map.remotes["BuyItem"]   -> { fires = { "StarterPlayerScripts/ShopUI" }, handles = { "ServerScriptService/Shop" } }
--   DependencyMap.orphans(map) -> remotes only fired or only handled (dead or unprotected endpoints)
-- Names are matched by the last identifier before the call, so rename-aliased remotes need a manual look.
local DependencyMap = {}

export type Scanner = { stripComments: (source: string) -> string, extractRequires: (source: string) -> { string } }
export type RemoteUse = { fires: { string }, handles: { string } }
export type Map = {
	remotes: { [string]: RemoteUse },
	requires: { [string]: { string } },
	tags: { [string]: { string } },
	attributes: { [string]: { string } },
	services: { [string]: { string } },
}

local FIRE = { "FireServer", "FireClient", "FireAllClients", "InvokeServer", "InvokeClient" }
local HANDLE = { "OnServerEvent", "OnClientEvent", "OnServerInvoke", "OnClientInvoke" }

local function addUnique(list: { string }, value: string)
	if not table.find(list, value) then
		table.insert(list, value)
		table.sort(list)
	end
end

local function bucket(map: { [string]: { string } }, key: string, script: string)
	local list = map[key]
	if list == nil then
		list = {}
		map[key] = list
	end
	addUnique(list :: { string }, script)
end

local function remote(map: Map, name: string): RemoteUse
	local r = map.remotes[name]
	if r == nil then
		r = { fires = {}, handles = {} }
		map.remotes[name] = r
	end
	return r :: RemoteUse
end

function DependencyMap.scan(sources: { [string]: string }, RequireGraph: Scanner): Map
	local map: Map = { remotes = {}, requires = {}, tags = {}, attributes = {}, services = {} }
	for script, raw in sources do
		local code = RequireGraph.stripComments(raw)
		for _, method in FIRE do
			for name in string.gmatch(code, "([%w_]+)%s*:%s*" .. method .. "%f[%W]") do
				addUnique(remote(map, name).fires, script)
			end
		end
		for _, event in HANDLE do
			for name in string.gmatch(code, "([%w_]+)%s*%.%s*" .. event .. "%f[%W]") do
				addUnique(remote(map, name).handles, script)
			end
		end
		for _, module in RequireGraph.extractRequires(code) do
			bucket(map.requires, module, script)
		end
		for _, call in
			{ "GetTagged", "AddTag", "RemoveTag", "HasTag", "GetInstanceAddedSignal", "GetInstanceRemovedSignal" }
		do
			for tag in string.gmatch(code, call .. "%s*%(%s*[^\"']*[\"']([^\"']+)[\"']") do
				bucket(map.tags, tag, script)
			end
		end
		for _, call in { "GetAttribute", "SetAttribute", "GetAttributeChangedSignal" } do
			for attribute in string.gmatch(code, call .. "%s*%(%s*[\"']([^\"']+)[\"']") do
				bucket(map.attributes, attribute, script)
			end
		end
		for service in string.gmatch(code, "GetService%s*%(%s*[\"']([%w_]+)[\"']") do
			bucket(map.services, service, script)
		end
	end
	return map
end

-- remotes with a caller but no handler (the call goes nowhere) or a handler but no caller (dead code or an attack surface)
function DependencyMap.orphans(map: Map): { onlyFired: { string }, onlyHandled: { string } }
	local onlyFired, onlyHandled = {}, {}
	for name, use in map.remotes do
		if #use.fires > 0 and #use.handles == 0 then
			table.insert(onlyFired, name)
		elseif #use.handles > 0 and #use.fires == 0 then
			table.insert(onlyHandled, name)
		end
	end
	table.sort(onlyFired)
	table.sort(onlyHandled)
	return { onlyFired = onlyFired, onlyHandled = onlyHandled }
end

-- markdown table of remotes for the project doc
function DependencyMap.remoteTable(map: Map): string
	local names = {}
	for name in map.remotes do
		table.insert(names, name)
	end
	table.sort(names)
	local rows = { "| remote | fired by | handled by |", "|---|---|---|" }
	for _, name in names do
		local use = map.remotes[name]
		table.insert(rows, `| {name} | {table.concat(use.fires, ", ")} | {table.concat(use.handles, ", ")} |`)
	end
	return table.concat(rows, "\n")
end

return DependencyMap
