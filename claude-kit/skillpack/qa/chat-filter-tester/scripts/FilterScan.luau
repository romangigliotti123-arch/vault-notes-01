--!strict
-- FilterScan: finds server handlers where player-typed text reaches other players or storage without the text filter in the same handler.
-- Pure string logic, unit-tested in Lune. HEURISTIC: filtering done in a helper function is not seen, so every finding is a lead to read.
-- Input handlers come from ArgScan.extract (input-validation-auditor/scripts/ArgScan.luau); paste both when running via execute_luau.
local FilterScan = {}

export type Handler = { remote: string, kind: string, line: number, params: { string }, body: string }
export type Finding = { where: string, param: string, sink: string }

local TEXT_NAMES = {
	"text",
	"msg",
	"message",
	"name",
	"title",
	"caption",
	"description",
	"desc",
	"chat",
	"input",
	"str",
	"label",
	"bio",
	"note",
	"petname",
	"nick",
}
local FILTER_CALLS = {
	"FilterStringAsync",
	"FilterTextAsync",
	"GetNonChatStringForBroadcastAsync",
	"GetChatForUserAsync",
	"FilterAsync",
	"Filter(",
}
-- places the text becomes visible to others or persistent: { kind, Lua pattern, label }. "assign" patterns get the parameter appended.
local SINKS = {
	{ "assign", "%.Text%s*=%s*", ".Text assignment" },
	{ "assign", "%.Name%s*=%s*", ".Name assignment" },
	{ "assign", "%.DisplayName%s*=%s*", "DisplayName assignment" },
	{ "call", "FireAllClients%b()", "FireAllClients" },
	{ "call", "FireClient%b()", "FireClient" },
	{ "call", "SetAsync%b()", "DataStore write" },
	{ "call", "UpdateAsync%b()", "DataStore write" },
	{ "call", "SetAttribute%b()", "SetAttribute" },
	{ "call", "table%.insert%b()", "table.insert" },
}

local function isTextName(name: string): boolean
	local lower = string.lower(name)
	for _, w in TEXT_NAMES do
		if lower == w or string.find(lower, w, 1, true) then
			return true
		end
	end
	return false
end

local function mentions(s: string, p: string): boolean
	return string.find(s, "%f[%w_]" .. p .. "%f[^%w_]") ~= nil
end

function FilterScan.scanHandlers(handlers: { Handler }): { Finding }
	local out: { Finding } = {}
	for _, h in handlers do
		local filtered = false
		for _, f in FILTER_CALLS do
			if string.find(h.body, f, 1, true) then
				filtered = true
				break
			end
		end
		if not filtered then
			for _, p in h.params do
				if isTextName(p) then
					for _, sink in SINKS do
						local hit = false
						if sink[1] == "assign" then
							hit = string.find(h.body, sink[2] .. p .. "%f[^%w_]") ~= nil
						else
							for call in string.gmatch(h.body, sink[2]) do
								if mentions(call, p) then
									hit = true
									break
								end
							end
						end
						if hit then
							table.insert(out, { where = `{h.remote} L{h.line}`, param = p, sink = sink[3] })
							break
						end
					end
				end
			end
		end
	end
	return out
end

-- a client script that shows another player's text straight from a remote, or TextBox text sent on with no server filter on the way
function FilterScan.scanClient(path: string, source: string): { Finding }
	local out: { Finding } = {}
	if
		string.find(source, "OnClientEvent", 1, true)
		and string.find(source, "%.Text%s*=")
		and not string.find(source, "TextChatService", 1, true)
	then
		table.insert(out, {
			where = path,
			param = "(OnClientEvent text)",
			sink = "client shows remote text: it is only safe if the SERVER filtered it for this recipient before sending",
		})
	end
	return out
end

function FilterScan.report(findings: { Finding }): string
	if #findings == 0 then
		return "FILTERSCAN: 0 leads"
	end
	local lines = { `FILTERSCAN: {#findings} leads (heuristic: read each handler)` }
	for _, f in findings do
		table.insert(lines, `  {f.where} {f.param} -> {f.sink}`)
	end
	return table.concat(lines, "\n")
end

return FilterScan
