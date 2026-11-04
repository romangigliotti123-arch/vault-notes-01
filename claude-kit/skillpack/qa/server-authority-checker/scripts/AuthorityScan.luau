--!strict
local AuthorityScan = {}

export type Handler = { remote: string, kind: string, line: number, params: { string }, body: string }
export type Finding = { severity: string, where: string, detail: string }

local MONEY = {
	"price",
	"cost",
	"reward",
	"payout",
	"amount",
	"coins",
	"gold",
	"cash",
	"money",
	"gems",
	"robux",
	"total",
	"value",
}
local COMBAT = {
	"damage",
	"dmg",
	"health",
	"hp",
	"heal",
	"kills",
	"score",
	"xp",
	"exp",
	"level",
	"multiplier",
	"result",
	"won",
	"win",
}
local WORLD = {
	"position",
	"pos",
	"cframe",
	"speed",
	"walkspeed",
	"rank",
	"isadmin",
	"admin",
	"owned",
	"unlocked",
	"time",
	"distance",
}

local function inList(list: { string }, name: string): boolean
	local lower = string.lower(name)
	for _, w in list do
		if lower == w or string.find(lower, w, 1, true) then
			return true
		end
	end
	return false
end

local function written(body: string, p: string): boolean
	local patterns = {
		"[%+%-%*/]=%s*" .. p .. "%f[^%w_]",
		"=%s*" .. p .. "%f[^%w_]",
		"[%+%-%*/]%s*" .. p .. "%f[^%w_]",
		"%f[%w_]" .. p .. "%s*[%+%-%*/]",
		"SetAsync%b()",
		"Increment%b()",
	}
	for i, pat in patterns do
		local m = string.match(body, pat)
		if m and (i <= 4 or string.find(m, "%f[%w_]" .. p .. "%f[^%w_]")) then
			return true
		end
	end
	return false
end

function AuthorityScan.scanHandlers(handlers: { Handler }): { Finding }
	local out: { Finding } = {}
	for _, h in handlers do
		for _, p in h.params do
			local tier: string? = nil
			if inList(MONEY, p) then
				tier = "CRITICAL"
			elseif inList(COMBAT, p) or inList(WORLD, p) then
				tier = "HIGH"
			end
			if tier and written(h.body, p) then
				table.insert(out, {
					severity = tier,
					where = `{h.remote} L{h.line}`,
					detail = `client argument '{p}' looks like an outcome and is written/used in maths: compute it on the server from state`,
				})
			end
		end
	end
	return out
end

local CLIENT_VISIBLE =
	{ "ReplicatedStorage", "ReplicatedFirst", "StarterGui", "StarterPlayer", "StarterPack", "Workspace" }
local SERVER_API = {
	"DataStoreService",
	"ProcessReceipt",
	"MessagingService",
	"MemoryStoreService",
	"OpenCloud",
	"x%-api%-key",
	"BanAsync",
	"UpdateAsync",
	"SetAsync",
}

function AuthorityScan.scanContainer(path: string, source: string): { Finding }
	local out: { Finding } = {}
	local visible = false
	for _, c in CLIENT_VISIBLE do
		if string.find(path, c, 1, true) then
			visible = true
			break
		end
	end
	if not visible then
		return out
	end
	for _, api in SERVER_API do
		if string.find(source, api) then
			table.insert(out, {
				severity = "HIGH",
				where = path,
				detail = `server-only API '{string.gsub(api, "%%", "")}' in a client-readable container: move the script to ServerScriptService or ServerStorage`,
			})
		end
	end
	return out
end

function AuthorityScan.scanInteractions(source: string, path: string): { Finding }
	local out: { Finding } = {}
	for name in string.gmatch(source, "(%w+)%.Triggered:Connect") do
		if
			string.find(path, "Local", 1, true)
			or string.find(path, "StarterGui", 1, true)
			or string.find(path, "StarterPlayer", 1, true)
		then
			table.insert(out, {
				severity = "HIGH",
				where = `{path} ({name}.Triggered)`,
				detail = "prompt handled in a client script: the server must listen to Triggered and re-check distance, state and cost",
			})
		end
	end
	return out
end

function AuthorityScan.report(findings: { Finding }): string
	if #findings == 0 then
		return "AUTHORITY: 0 leads"
	end
	local lines = { `AUTHORITY: {#findings} leads (heuristic: read each one)` }
	for _, f in findings do
		table.insert(lines, `  {f.severity} {f.where}: {f.detail}`)
	end
	return table.concat(lines, "\n")
end

return AuthorityScan
