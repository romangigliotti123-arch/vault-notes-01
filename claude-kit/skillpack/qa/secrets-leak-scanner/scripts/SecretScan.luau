--!strict
-- SecretScan: finds secrets and server-only data in project text that could ship to clients or into a repo. Pure string logic,
-- unit-tested in Lune. Matches are REDACTED in findings (first 3 characters + length): never print or log a real secret.
-- Heuristics only: a clean scan is not proof. Rotate anything real that was ever committed or published.
local SecretScan = {}

export type Finding = { severity: string, rule: string, path: string, line: number, preview: string }

local function redact(s: string): string
	if #s <= 6 then
		return "***"
	end
	return string.sub(s, 1, 3) .. "*** (" .. #s .. " chars)"
end

-- rules: { id, severity, Lua pattern, capture index to redact, note }. Patterns match one line.
local RULES: { { string } } = {
	{ "discord-webhook", "CRITICAL", "discord[%w]*%.com/api/webhooks/%d+/([%w_%-]+)" },
	{ "bearer-token", "CRITICAL", "[Bb]earer%s+([%w_%-%.]%w[%w_%-%.]+)" },
	{ "private-key-block", "CRITICAL", "(%-%-%-%-%-BEGIN [%w ]*PRIV​ATE KEY%-%-%-%-%-)" },
	{ "api-key-header", "CRITICAL", "[xX]%-[aA]pi%-[kK]ey[\"']?%]?%s*[=:,]%s*[\"']([^\"']+)[\"']" },
	{ "key-in-url", "HIGH", "[?&][Kk]ey=([%w_%-]+)" },
	{ "secret-assignment", "HIGH", "[%w_]*[Ss]ecret[%w_]*%s*=%s*[\"']([^\"']+)[\"']" },
	{ "token-assignment", "HIGH", "[%w_]*[Tt]oken[%w_]*%s*=%s*[\"']([^\"']+)[\"']" },
	{ "apikey-assignment", "HIGH", "[%w_]*[Aa]pi[_]?[Kk]ey[%w_]*%s*=%s*[\"']([^\"']+)[\"']" },
	{ "password-assignment", "HIGH", "[%w_]*[Pp]ass[Ww]or[Dd][%w_]*%s*=%s*[\"']([^\"']+)[\"']" },
	{ "secure-teleportdata", "MEDIUM", "SetTeleportData%b()" },
}

local PLACEHOLDER =
	{ "xxx", "your", "changeme", "example", "todo", "placeholder", "<", "${", "env", "secret_here", "set in" }

local function looksReal(value: string): boolean
	if #value < 8 then
		return false
	end
	local lower = string.lower(value)
	for _, p in PLACEHOLDER do
		if string.find(lower, p, 1, true) then
			return false
		end
	end
	return true
end

-- scan one file's text. `path` is only used to label findings (and for the client-visible rule).
function SecretScan.scanText(path: string, text: string): { Finding }
	local out: { Finding } = {}
	local n = 0
	for line in string.gmatch(text .. "\n", "([^\n]*)\n") do
		n += 1
		if not string.match(line, "^%s*%-%-") or string.find(line, "BEGIN", 1, true) then
			for _, rule in RULES do
				local id: string, sev: string, pat: string = rule[1], rule[2], rule[3]
				local ruleName: string = id
				local whole = string.match(line, pat)
				if whole then
					if id == "secure-teleportdata" then
						local lower = string.lower(whole)
						if
							string.find(lower, "secret", 1, true)
							or string.find(lower, "token", 1, true)
							or string.find(lower, "key", 1, true)
							or string.find(lower, "password", 1, true)
						then
							table.insert(out, {
								severity = sev,
								rule = ruleName,
								path = path,
								line = n,
								preview = "TeleportData is visible to clients and unencrypted",
							})
						end
					elseif id == "private-key-block" or id == "discord-webhook" or looksReal(whole) then
						table.insert(
							out,
							{ severity = sev, rule = ruleName, path = path, line = n, preview = redact(whole) }
						)
					end
				end
			end
		end
	end
	return out
end

-- paths whose contents the client can read: admin lists and server tables there are public
local CLIENT_VISIBLE = {
	"ReplicatedStorage",
	"ReplicatedFirst",
	"StarterGui",
	"StarterPlayer",
	"StarterPack",
	"Workspace",
	"src/shared",
	"src/client",
}

function SecretScan.scanClientVisible(path: string, text: string): { Finding }
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
	local n = 0
	for line in string.gmatch(text .. "\n", "([^\n]*)\n") do
		n += 1
		local l = string.lower(line)
		if
			(string.find(l, "admin", 1, true) or string.find(l, "owner", 1, true) or string.find(l, "banned", 1, true))
			and string.find(line, "%d%d%d%d%d%d+")
		then
			table.insert(out, {
				severity = "MEDIUM",
				rule = "userid-list-client-visible",
				path = path,
				line = n,
				preview = "UserId list in a client-readable script: move to a server-only module",
			})
		end
	end
	return out
end

function SecretScan.report(findings: { Finding }): string
	if #findings == 0 then
		return "SECRETS: 0 findings (heuristic: not proof)"
	end
	local lines = { `SECRETS: {#findings} findings (values redacted)` }
	for _, f in findings do
		table.insert(lines, `  {f.severity} {f.rule} {f.path}:{f.line} {f.preview}`)
	end
	return table.concat(lines, "\n")
end

return SecretScan
