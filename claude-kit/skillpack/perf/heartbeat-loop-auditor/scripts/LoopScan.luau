--!strict
local LoopScan = {}

export type Finding = { line: number, kind: string, text: string }

local FRAME_EVENTS =
	{ "Heartbeat", "RenderStepped", "Stepped", "PreSimulation", "PostSimulation", "PreRender", "PreAnimation" }
local EXPENSIVE = {
	"GetDescendants",
	"GetChildren",
	"GetPlayers",
	"FindFirstChild",
	"WaitForChild",
	"Raycast",
	"GetPartBoundsInBox",
	"GetPartBoundsInRadius",
	"GetPartsInPart",
	"Instance.new",
	":Clone(",
	"FindPartsInRegion3",
}

local function indentOf(line: string): number
	local ws = string.match(line, "^([ \t]*)") or ""
	return #ws
end

local function frameEventOn(line: string): string?
	for _, e in FRAME_EVENTS do
		if string.find(line, e .. ":Connect", 1, true) or string.find(line, e .. ":Once", 1, true) then
			return e
		end
	end
	if string.find(line, "BindToRenderStep", 1, true) then
		return "BindToRenderStep"
	end
	return nil
end

local function waitSeconds(line: string): number?
	local arg = string.match(line, "task%.wait%(([^)]*)%)") or string.match(line, "[^%w_%.]wait%(([^)]*)%)")
	if arg == nil then
		return nil
	end
	arg = string.gsub(arg, "%s", "")
	if arg == "" then
		return 0
	end
	return tonumber(arg)
end

function LoopScan.scan(source: string): { Finding }
	local findings: { Finding } = {}
	local lines = string.split(source, "\n")
	local callbackIndent: number? = nil
	local callbackEvent = ""
	local loopIndent: number? = nil
	for i, line in lines do
		local trimmed = string.match(line, "^%s*(.-)%s*$") or ""
		local skip = trimmed == "" or string.sub(trimmed, 1, 2) == "--"
		if not skip then
			local ind = indentOf(line)
			if callbackIndent and ind <= callbackIndent then
				callbackIndent = nil
			end
			if loopIndent and ind <= loopIndent then
				loopIndent = nil
			end
			local ev = frameEventOn(line)
			if ev then
				table.insert(findings, { line = i, kind = "per-frame-callback", text = ev .. ": " .. trimmed })
				callbackIndent = ind
				callbackEvent = ev
			end
			if
				string.find(trimmed, "^while%s+true%s+do")
				or string.find(trimmed, "^while%s+task%.wait%(")
				or string.find(trimmed, "^while%s+wait%(")
			then
				loopIndent = ind
			end
			local ws = waitSeconds(line)
			if string.find(trimmed, "[^%w_%.]wait%(") or string.find(trimmed, "^wait%(") then
				table.insert(
					findings,
					{ line = i, kind = "legacy-wait", text = "wait() overshoots and is throttled; use task.wait" }
				)
			end
			if ws ~= nil and ws <= 0.05 and (loopIndent ~= nil or string.find(trimmed, "^while") ~= nil) then
				table.insert(findings, {
					line = i,
					kind = "tight-wait-loop",
					text = "loop waits " .. tostring(ws) .. " s: runs about every frame",
				})
			end
			if callbackIndent ~= nil and ind > callbackIndent then
				for _, call in EXPENSIVE do
					if string.find(line, call, 1, true) then
						table.insert(findings, {
							line = i,
							kind = "expensive-in-frame-loop",
							text = call .. " inside " .. callbackEvent .. " callback: cache it or move it out",
						})
						break
					end
				end
			elseif loopIndent ~= nil and ind > loopIndent then
				for _, call in EXPENSIVE do
					if string.find(line, call, 1, true) then
						table.insert(findings, {
							line = i,
							kind = "expensive-in-wait-loop",
							text = call .. " inside a repeating loop: cache it or move it out",
						})
						break
					end
				end
			end
		end
	end
	return findings
end

function LoopScan.summarise(findings: { Finding }): { [string]: number }
	local out: { [string]: number } = {}
	for _, f in findings do
		out[f.kind] = (out[f.kind] or 0) + 1
	end
	return out
end

return LoopScan
