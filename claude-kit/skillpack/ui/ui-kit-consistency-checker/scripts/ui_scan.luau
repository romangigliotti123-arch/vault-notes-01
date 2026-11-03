--!strict
-- ui_scan.luau: read-only. Collects corner radius, stroke thickness, font family, text size and padding from every ScreenGui under
-- StarterGui (or PlayerGui in a Client playtest) and prints the dominant value per field plus the rare values with example paths.
-- Same rule as Consistency.luau (dominant >= 50% of records, outlier < 15%); kept inline so it runs from the command bar / MCP execute_luau.
local Players = game:GetService("Players")
local RunService = game:GetService("RunService")
local StarterGui = game:GetService("StarterGui")

local root: Instance = StarterGui
if RunService:IsClient() and Players.LocalPlayer then
	root = Players.LocalPlayer:WaitForChild("PlayerGui")
end

local fields = { "cornerRadius", "strokeThickness", "font", "textSize", "padding" }
local counts: { [string]: { [string]: number } } = {}
local examples: { [string]: { [string]: { string } } } = {}
local totals: { [string]: number } = {}
for _, f in fields do
	counts[f], examples[f], totals[f] = {}, {}, 0
end

local function record(field: string, value: any, inst: Instance)
	local key = tostring(value)
	counts[field][key] = (counts[field][key] or 0) + 1
	totals[field] += 1
	local list = examples[field][key]
	if not list then
		list = {}
		examples[field][key] = list
	end
	if #list < 3 then
		table.insert(list, inst:GetFullName())
	end
end

for _, d in root:GetDescendants() do
	if d:IsA("UICorner") then
		local c = d :: UICorner
		record("cornerRadius", `{c.CornerRadius.Scale}s/{c.CornerRadius.Offset}px`, d)
	elseif d:IsA("UIStroke") then
		record("strokeThickness", (d :: UIStroke).Thickness, d)
	elseif d:IsA("UIPadding") then
		record("padding", (d :: UIPadding).PaddingLeft.Offset, d)
	elseif d:IsA("TextLabel") or d:IsA("TextButton") or d:IsA("TextBox") then
		local t = d :: TextLabel
		record("font", t.FontFace.Family, d)
		if not t.TextScaled then
			record("textSize", t.TextSize, d)
		end
	end
end

for _, f in fields do
	local top, topN = nil, 0
	for k, n in counts[f] do
		if n > topN then
			top, topN = k, n
		end
	end
	local total = totals[f]
	if total == 0 then
		print(`{f}: none found`)
	else
		print(`{f}: dominant {top} ({math.floor(100 * topN / total)}% of {total})`)
		if topN / total >= 0.5 then
			for k, n in counts[f] do
				if k ~= top and n / total < 0.15 then
					print(`  outlier {k} x{n}: {table.concat(examples[f][k], ", ")}`)
				end
			end
		end
	end
end
