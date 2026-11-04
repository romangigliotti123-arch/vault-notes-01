--!strict
local process = require("@lune/process")

local passed, failed = 0, 0
local M = {}

local function show(v: any): string
	if type(v) == "table" then
		local parts = {}
		for k, x in v do
			table.insert(parts, tostring(k) .. "=" .. show(x))
		end
		table.sort(parts)
		return "{" .. table.concat(parts, ",") .. "}"
	end
	return tostring(v)
end

function M.eq(a: any, b: any, msg: string?)
	if show(a) ~= show(b) then
		error((msg or "eq") .. ": expected " .. show(b) .. ", got " .. show(a), 2)
	end
end

function M.truthy(v: any, msg: string?)
	if not v then
		error((msg or "truthy") .. ": got " .. show(v), 2)
	end
end

function M.falsy(v: any, msg: string?)
	if v then
		error((msg or "falsy") .. ": got " .. show(v), 2)
	end
end

function M.test(name: string, fn: () -> ())
	local ok, err = pcall(fn)
	if ok then
		passed += 1
		print("  ok   " .. name)
	else
		failed += 1
		print("  FAIL " .. name .. " -> " .. tostring(err))
	end
end

function M.done()
	print(string.format("%d passed, %d failed", passed, failed))
	if failed > 0 then
		process.exit(1)
	end
end

return M
