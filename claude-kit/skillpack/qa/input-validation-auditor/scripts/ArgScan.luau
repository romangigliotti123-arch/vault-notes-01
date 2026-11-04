--!strict
local ArgScan = {}

export type Handler = {
	remote: string,
	kind: "event" | "function",
	line: number,
	params: { string },
	body: string,
}
export type Finding = { line: number, remote: string, param: string, kind: string, detail: string }

local function splitParams(list: string): { string }
	local out = {}
	for name in string.gmatch(list, "[%w_]+") do
		table.insert(out, name)
	end
	if #out > 0 then
		table.remove(out, 1)
	end
	return out
end

local function lineOf(src: string, pos: number): number
	local _, n = string.gsub(string.sub(src, 1, pos), "\n", "")
	return n + 1
end

local function bodyAfter(src: string, from: number, indent: string): string
	local closer = "\n" .. indent .. "end"
	local s, e = string.find(src, closer, from, true)
	if s == nil then
		return string.sub(src, from)
	end
	return string.sub(src, from, e)
end

function ArgScan.extract(src: string): { Handler }
	local out: { Handler } = {}
	local init = 1
	while true do
		local s, e, remote, params =
			string.find(src, "([%w_%.%[%]\"']+)%.OnServerEvent:Connect%(function%(([^)]*)%)", init)
		if s == nil or e == nil or remote == nil or params == nil then
			break
		end
		local ls = string.find(string.sub(src, 1, s), "[^\n]*$") or 1
		local indent = string.match(string.sub(src, ls, s), "^(%s*)") or ""
		table.insert(out, {
			remote = remote,
			kind = "event",
			line = lineOf(src, s),
			params = splitParams(params),
			body = bodyAfter(src, e + 1, indent),
		})
		init = e + 1
	end
	init = 1
	while true do
		local s, e, remote, params =
			string.find(src, "([%w_%.%[%]\"']+)%.OnServerInvoke%s*=%s*function%(([^)]*)%)", init)
		if s == nil or e == nil or remote == nil or params == nil then
			break
		end
		local ls = string.find(string.sub(src, 1, s), "[^\n]*$") or 1
		local indent = string.match(string.sub(src, ls, s), "^(%s*)") or ""
		table.insert(out, {
			remote = remote,
			kind = "function",
			line = lineOf(src, s),
			params = splitParams(params),
			body = bodyAfter(src, e + 1, indent),
		})
		init = e + 1
	end
	table.sort(out, function(a, b)
		return a.line < b.line
	end)
	return out
end

local function validated(body: string, p: string): boolean
	local patterns = {
		"typeof%(" .. p .. "%)",
		"type%(" .. p .. "%)",
		"isfinite%(" .. p .. "%)",
		p .. "%s*~=%s*" .. p,
		"math%.clamp%(" .. p,
		"math%.floor%(" .. p .. "%)",
		"IsA%(",
	}
	for _, pat in patterns do
		if string.find(body, pat) then
			return pat ~= "IsA%(" or string.find(body, p .. ":IsA%(") ~= nil
		end
	end
	return false
end

local function usedIn(body: string, p: string): boolean
	return string.find(body, "%f[%w_]" .. p .. "%f[^%w_]") ~= nil
end

local GUARD_WORDS = { "RemoteGuard", "Guard.check", "Validate", "validate", "Validator" }

function ArgScan.audit(handlers: { Handler }): { Finding }
	local out: { Finding } = {}
	for _, h in handlers do
		local guarded = false
		for _, w in GUARD_WORDS do
			if string.find(h.body, w, 1, true) then
				guarded = true
				break
			end
		end
		if #h.params == 0 then
			table.insert(out, {
				line = h.line,
				remote = h.remote,
				param = "(none)",
				kind = "no-args",
				detail = "no client arguments: still needs state, cooldown and range checks",
			})
		end
		for _, p in h.params do
			if not usedIn(h.body, p) then
				table.insert(out, {
					line = h.line,
					remote = h.remote,
					param = p,
					kind = "unused",
					detail = "argument is never read: remove it or check it",
				})
			elseif not guarded and not validated(h.body, p) then
				table.insert(out, {
					line = h.line,
					remote = h.remote,
					param = p,
					kind = "unchecked",
					detail = "argument is used with no type/NaN/range test and no guard call in the handler",
				})
			end
		end
		if
			not guarded
			and not string.find(h.body, "os%.clock%(%)")
			and not string.find(h.body, "os%.time%(%)")
			and not string.find(h.body, "tick%(%)")
			and not string.find(h.body, "[Cc]ooldown")
			and not string.find(h.body, "[Dd]ebounce")
			and not string.find(h.body, "[Ll]imit")
		then
			table.insert(out, {
				line = h.line,
				remote = h.remote,
				param = "(rate)",
				kind = "no-rate-limit",
				detail = "no cooldown, debounce or rate limiter visible in the handler",
			})
		end
	end
	return out
end

function ArgScan.report(findings: { Finding }): string
	if #findings == 0 then
		return "ARGSCAN: 0 leads"
	end
	local lines = { `ARGSCAN: {#findings} leads (heuristic: read each handler)` }
	for _, f in findings do
		table.insert(lines, `  L{f.line} {f.remote} {f.param}: {f.kind} - {f.detail}`)
	end
	return table.concat(lines, "\n")
end

return ArgScan
