--!strict
-- LeakScan: heuristic text scan for code that never cleans up. It ranks files to read; it cannot prove a leak.
-- Works best on stylua-formatted code (it uses indentation to find the enclosing block).
--   local findings = LeakScan.scan(source)      -- { { line, rule, message }, ... }
-- Rules: busy-loop, unstored-connect, repeat-connect, player-state-not-cleared, instances-not-destroyed, unpaired-render-bind.
local LeakScan = {}

export type Finding = { line: number, rule: string, message: string }

local REPEATING = {
	"while ",
	"for ",
	"repeat",
	"PlayerAdded",
	"CharacterAdded",
	"ChildAdded",
	"Touched",
	"Triggered",
	"OnServerEvent",
}

local function indentOf(line: string): number
	local ws = string.match(line, "^([ \t]*)") or ""
	return #string.gsub(ws, "\t", "    ")
end

local function stripComment(line: string): string
	return (string.gsub(line, "%-%-.*$", ""))
end

-- nearest earlier line with smaller indentation (the block header)
local function enclosing(lines: { string }, i: number): string
	local base = indentOf(lines[i])
	for j = i - 1, 1, -1 do
		local l = stripComment(lines[j])
		if string.match(l, "%S") and indentOf(lines[j]) < base then
			return l
		end
	end
	return ""
end

local function isRepeating(header: string): boolean
	for _, key in REPEATING do
		if string.find(header, key, 1, true) then
			return true
		end
	end
	return false
end

function LeakScan.scan(source: string): { Finding }
	local lines: { string } = {}
	for line in string.gmatch(source .. "\n", "(.-)\n") do
		table.insert(lines, line)
	end
	local out: { Finding } = {}
	local function add(line: number, rule: string, message: string)
		table.insert(out, { line = line, rule = rule, message = message })
	end

	local hasPlayerAdded, hasPlayerRemoving, keyedByPlayer = false, false, false
	local createsInstances, destroysInstances = false, false
	local renderBinds, renderUnbinds = 0, 0

	for i, raw in lines do
		local code = stripComment(raw)
		if string.find(code, "PlayerAdded", 1, true) then
			hasPlayerAdded = true
		end
		if string.find(code, "PlayerRemoving", 1, true) then
			hasPlayerRemoving = true
		end
		if string.match(code, "%[%s*player%s*%]%s*=") or string.match(code, "%[%s*[%w_%.]*UserId%s*%]%s*=") then
			keyedByPlayer = true
		end
		if string.find(code, "Instance.new", 1, true) then
			createsInstances = true
		end
		if string.find(code, ":Destroy()", 1, true) or string.find(code, "Debris", 1, true) then
			destroysInstances = true
		end
		if string.find(code, ":BindToRenderStep", 1, true) then
			renderBinds += 1
		end
		if string.find(code, ":UnbindFromRenderStep", 1, true) then
			renderUnbinds += 1
		end

		-- a loop that never yields freezes the thread; one that yields only via spawn still needs a stop condition
		if string.match(code, "^%s*while%s+true%s+do") then
			local yields = false
			local base = indentOf(raw)
			for j = i + 1, #lines do
				local body = stripComment(lines[j])
				if string.match(body, "%S") and indentOf(lines[j]) <= base then
					break
				end
				if
					string.find(body, "wait", 1, true)
					or string.find(body, "Heartbeat", 1, true)
					or string.find(body, "RenderStepped", 1, true)
				then
					yields = true
					break
				end
			end
			if not yields then
				add(i, "busy-loop", "while true do with no wait or frame event in the body")
			end
		end

		if string.find(code, ":Connect(", 1, true) or string.find(code, ":Once(", 1, true) then
			local stored = string.match(code, "=%s*[%w_%.:%(%)]+:Connect%(") ~= nil
				or string.match(code, "[%w_]+%s*=%s*.-:Connect%(") ~= nil
				or string.match(code, "^%s*table%.insert") ~= nil
				or string.match(code, "^%s*return%s") ~= nil
			local header = enclosing(lines, i)
			if not stored and isRepeating(header) then
				add(
					i,
					"repeat-connect",
					"connection made inside a repeating scope is never stored: "
						.. (string.match(header, "^%s*(.-)%s*$") or "")
				)
			elseif
				not stored and string.find(code, "Heartbeat", 1, true)
				or not stored and string.find(code, "RenderStepped", 1, true)
			then
				add(i, "unstored-connect", "frame-event connection with no handle, it can never be disconnected")
			end
		end
	end

	if hasPlayerAdded and keyedByPlayer and not hasPlayerRemoving then
		add(1, "player-state-not-cleared", "state is keyed by player but there is no PlayerRemoving handler")
	end
	if createsInstances and not destroysInstances then
		add(1, "instances-not-destroyed", "Instance.new is used but nothing calls Destroy or Debris")
	end
	if renderBinds > renderUnbinds then
		add(1, "unpaired-render-bind", `{renderBinds} BindToRenderStep vs {renderUnbinds} UnbindFromRenderStep`)
	end
	return out
end

-- count per rule, for the report header
function LeakScan.summarize(findings: { Finding }): { [string]: number }
	local counts: { [string]: number } = {}
	for _, f in findings do
		counts[f.rule] = (counts[f.rule] or 0) + 1
	end
	return counts
end

return LeakScan
