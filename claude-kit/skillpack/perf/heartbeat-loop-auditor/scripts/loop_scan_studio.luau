--!strict
-- loop_scan_studio.luau: runs LoopScan (heartbeat-loop-auditor/scripts/LoopScan.luau) over every script in the open place. Command bar or MCP `execute_luau` (Edit datamodel).
-- Setup: LoopScan must exist as a ModuleScript named "LoopScan" in ServerStorage (Rojo: map scripts/LoopScan.luau there for the audit, then remove it; or create it from the file's text).
-- It reads Script.Source, so it needs plugin/command-bar security (works from execute_luau). Output: findings per script, worst scripts first, as TEXT CANDIDATES to review,
-- not measured cost: open the Script Profiler (script-profiler skill) to see which of them actually shows up.
local ServerStorage = game:GetService("ServerStorage")

local moduleScript = ServerStorage:FindFirstChild("LoopScan")
if moduleScript == nil or not moduleScript:IsA("ModuleScript") then
	return "loop_scan_studio: put LoopScan.luau in ServerStorage as a ModuleScript named LoopScan first"
end
local LoopScan = require(moduleScript :: ModuleScript) :: any

local results: { { path: string, count: number, text: string } } = {}
for _, inst in game:GetDescendants() do
	if inst:IsA("LuaSourceContainer") and inst ~= moduleScript then
		local ok, src = pcall(function()
			return (inst :: any).Source :: string
		end)
		if ok and src ~= "" then
			local findings = LoopScan.scan(src)
			if #findings > 0 then
				local parts = {}
				for _, f in findings do
					table.insert(parts, ("  L%d %s %s"):format(f.line, f.kind, f.text))
				end
				table.insert(
					results,
					{ path = inst:GetFullName(), count = #findings, text = table.concat(parts, "\n") }
				)
			end
		end
	end
end
table.sort(results, function(a, b)
	return a.count > b.count
end)

local lines = { ("%d scripts with candidates"):format(#results) }
for i = 1, math.min(15, #results) do
	table.insert(lines, results[i].path .. " (" .. results[i].count .. ")")
	table.insert(lines, results[i].text)
end
return table.concat(lines, "\n")
