--!strict
-- ModulePlan: read a set of scripts and propose where each belongs (server service, client controller, shared) and which ones
-- should be split. Text only; a starting proposal for the human, never an automatic refactor.
--   local plan = ModulePlan.analyse(sources, RequireGraph)        -- RequireGraph from require-cycle-finder/scripts, passed in
--   plan.modules[name] = { lines, functions, side, mixed, splitReasons, requires }
--   plan.violations    = shared modules that require server/client code, client modules that require server code
-- "side" comes from the services and APIs a file uses (listed below); it is a hint. Server-only logic must never live in a
-- container clients can read (ReplicatedStorage): the vault's security notes say exploiters read everything replicated.
local ModulePlan = {}

export type Graph = {
	build: (modules: { [string]: string }) -> { edges: { [string]: { string } }, unknown: { [string]: { string } } },
	stripComments: (source: string) -> string,
}
export type Module = {
	lines: number,
	functions: number,
	side: string, -- "server" | "client" | "shared"
	mixed: boolean,
	splitReasons: { string },
	requires: { string },
}
export type Plan = {
	modules: { [string]: Module },
	violations: { string },
	layout: { server: { string }, client: { string }, shared: { string } },
}

local SERVER_MARKERS = {
	"DataStoreService",
	"MemoryStoreService",
	"OnServerEvent",
	"OnServerInvoke",
	"ServerStorage",
	"ServerScriptService",
	"ProcessReceipt",
	"MessagingService",
	"FireClient",
	"FireAllClients",
	"Players.PlayerAdded",
	"PlayerRemoving",
}
local CLIENT_MARKERS = {
	"LocalPlayer",
	"PlayerGui",
	"UserInputService",
	"ContextActionService",
	"RenderStepped",
	"CurrentCamera",
	"FireServer",
	"OnClientEvent",
	"StarterGui",
	"GuiService",
}

local function countAny(code: string, markers: { string }): number
	local n = 0
	for _, m in markers do
		if string.find(code, m, 1, true) then
			n += 1
		end
	end
	return n
end

-- why a dependency from a `from`-side module on a `to`-side module is not allowed, or nil
local FORBIDDEN: { [string]: { [string]: string } } = {
	shared = {
		server = "shared code must not depend on one side",
		client = "shared code must not depend on one side",
	},
	client = { server = "a client cannot load server code" },
	server = { client = "the server cannot load client code" },
}

function ModulePlan.violation(from: string, to: string): string?
	local row = FORBIDDEN[from]
	return if row then row[to] else nil
end

function ModulePlan.analyse(sources: { [string]: string }, graph: Graph): Plan
	local built = graph.build(sources)
	local modules: { [string]: Module } = {}
	local layout =
		{ server = {}, client = {}, shared = {} } :: { server: { string }, client: { string }, shared: { string } }
	for name, source in sources do
		local code = graph.stripComments(source)
		local lines = select(2, string.gsub(source, "\n", "\n")) + 1
		local functions = select(2, string.gsub(code, "function[%s%(]", ""))
		local serverHits = countAny(code, SERVER_MARKERS)
		local clientHits = countAny(code, CLIENT_MARKERS)
		local side = if serverHits > 0 and clientHits == 0
			then "server"
			elseif clientHits > 0 and serverHits == 0 then "client"
			else "shared"
		local mixed = serverHits > 0 and clientHits > 0
		local reasons: { string } = {}
		if lines > 300 then
			table.insert(reasons, `{lines} lines (over 300)`)
		end
		if functions > 20 then
			table.insert(reasons, `{functions} functions (over 20)`)
		end
		if mixed then
			table.insert(reasons, "uses both server and client APIs: split by side")
		end
		modules[name] = {
			lines = lines,
			functions = functions,
			side = side,
			mixed = mixed,
			splitReasons = reasons,
			requires = built.edges[name],
		}
		table.insert(layout[side :: "server"], name)
	end
	for _, list in { layout.server, layout.client, layout.shared } do
		table.sort(list)
	end

	local violations: { string } = {}
	for name, m in modules do
		for _, dep in m.requires do
			local ds: string = modules[dep].side
			local ms: string = m.side
			local why = ModulePlan.violation(ms, ds)
			if why then
				table.insert(violations, `{name} ({ms}) requires {dep} ({ds}): {why}`)
			end
		end
	end
	table.sort(violations)
	return { modules = modules, violations = violations, layout = layout }
end

-- modules worth splitting, biggest first
function ModulePlan.splitCandidates(plan: Plan): { string }
	local names = {}
	for name, m in plan.modules do
		if #m.splitReasons > 0 then
			table.insert(names, name)
		end
	end
	table.sort(names, function(a, b)
		local la, lb = plan.modules[a].lines, plan.modules[b].lines
		if la ~= lb then
			return la > lb
		end
		return a < b
	end)
	return names
end

return ModulePlan
