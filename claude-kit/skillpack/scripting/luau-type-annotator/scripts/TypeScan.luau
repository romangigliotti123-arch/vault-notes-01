--!strict
local TypeScan = {}

export type FunctionGap = { line: number, name: string, untyped: { string }, missingReturn: boolean }
export type Report = { mode: string, functions: { FunctionGap }, anyCount: number, totalFunctions: number }

function TypeScan.mode(source: string): string
	for line in string.gmatch(source, "[^\n]+") do
		local directive = string.match(line, "^%s*%-%-!(%a+)")
		if directive == "strict" or directive == "nonstrict" or directive == "nocheck" then
			return directive
		end
		if not string.match(line, "^%s*%-%-") then
			break
		end
	end
	return "none"
end

local function splitParams(list: string): { string }
	local out: { string } = {}
	local depth, current = 0, ""
	for ch in string.gmatch(list, ".") do
		if ch == "{" or ch == "(" or ch == "<" then
			depth += 1
		elseif ch == "}" or ch == ")" or ch == ">" then
			depth -= 1
		end
		if ch == "," and depth == 0 then
			table.insert(out, current)
			current = ""
		else
			current ..= ch
		end
	end
	if string.match(current, "%S") then
		table.insert(out, current)
	end
	return out
end

local function trim(s: string): string
	return (string.gsub(s, "^%s+", "")):match("^(.-)%s*$") :: string
end

local function declaration(line: string): (string?, string?, string?)
	local name, params, rest = string.match(line, "function%s+([%w_%.:]+)%s*(%b())%s*(.*)$")
	if name then
		return name, params, rest
	end
	local var, anon, tail = string.match(line, "([%w_%.]+)%s*=%s*function%s*(%b())%s*(.*)$")
	if var then
		return var, anon, tail
	end
	local _, inlineParams, inlineRest = string.match(line, "(function)%s*(%b())%s*(.*)$")
	if inlineParams then
		return "<anonymous>", inlineParams, inlineRest
	end
	return nil, nil, nil
end

function TypeScan.scan(source: string): Report
	local gaps: { FunctionGap } = {}
	local total, anyCount = 0, 0
	local n = 0
	for line in string.gmatch(source .. "\n", "(.-)\n") do
		n += 1
		local code = string.gsub(line, "%-%-.*$", "")
		anyCount += select(2, string.gsub(code, "[:%s]any%f[%W]", ""))
		local name, params, rest = declaration(code)
		if name and params and rest then
			total += 1
			local untyped: { string } = {}
			for _, p in splitParams(string.sub(params, 2, -2)) do
				local param = trim(p)
				if param ~= "self" and param ~= "..." and not string.find(param, ":", 1, true) then
					table.insert(untyped, param)
				end
			end
			local missingReturn = string.sub(rest, 1, 1) ~= ":"
			if #untyped > 0 or missingReturn then
				table.insert(gaps, { line = n, name = name, untyped = untyped, missingReturn = missingReturn })
			end
		end
	end
	return { mode = TypeScan.mode(source), functions = gaps, anyCount = anyCount, totalFunctions = total }
end

function TypeScan.score(report: Report): number
	local s = report.anyCount
	for _, g in report.functions do
		s += #g.untyped + (if g.missingReturn then 1 else 0)
	end
	return s
end

return TypeScan
