--!strict
-- ui_audit.luau: read-only static scan of every ScreenGui under StarterGui (or the local PlayerGui when run in a client playtest).
-- Flags layout choices that usually break on phones. Static: it cannot see runtime-created UI or real device aspect ratios, so it
-- supplements, never replaces, a screenshot pass at several resolutions. Studio command bar or MCP `execute_luau` (Edit or Client).
local MIN_TOUCH_PX = 44 -- industry touch-target heuristic (Apple HIG 44pt); Roblox publishes no single number, so treat as a guide
local MIN_TEXT_PX = 14
local MAX_FIXED_WIDTH = 300 -- an Offset-only width above this is wider than many phones leave free
local MAX_LIST = 6

local Players = game:GetService("Players")
local StarterGui = game:GetService("StarterGui")
local RunService = game:GetService("RunService")

local root: Instance = StarterGui
if RunService:IsClient() and Players.LocalPlayer then
	root = Players.LocalPlayer:WaitForChild("PlayerGui")
end

local issues: { [string]: { string } } = {}
local counts: { [string]: number } = {}
local function flag(kind: string, inst: Instance)
	counts[kind] = (counts[kind] or 0) + 1
	local list = issues[kind]
	if not list then
		list = {}
		issues[kind] = list
	end
	if #list < MAX_LIST then
		table.insert(list, inst:GetFullName())
	end
end

local guis = 0
for _, gui in root:GetDescendants() do
	if gui:IsA("ScreenGui") then
		guis += 1
		local sg = gui :: ScreenGui
		if sg.ScreenInsets == Enum.ScreenInsets.None and sg.IgnoreGuiInset then
			-- fine for full-bleed art, risky for buttons near the notch: reported once per gui so the human can look
			flag("ScreenInsets=None (content can sit under notch/home bar)", sg)
		end
	elseif gui:IsA("GuiObject") then
		local obj = gui :: GuiObject
		local size = obj.Size
		if size.X.Scale == 0 and size.Y.Scale == 0 and size.X.Offset > 0 then
			flag("Offset-only size (does not scale with the screen)", obj)
		end
		if size.X.Scale == 0 and size.X.Offset > MAX_FIXED_WIDTH then
			flag(`fixed width over {MAX_FIXED_WIDTH}px`, obj)
		end
		if obj:IsA("TextButton") or obj:IsA("ImageButton") then
			local w = if obj.AbsoluteSize.X > 0 then obj.AbsoluteSize.X else size.X.Offset
			local h = if obj.AbsoluteSize.Y > 0 then obj.AbsoluteSize.Y else size.Y.Offset
			if w > 0 and h > 0 and (w < MIN_TOUCH_PX or h < MIN_TOUCH_PX) then
				flag(`touch target under {MIN_TOUCH_PX}px at the current viewport`, obj)
			end
		end
		if obj:IsA("TextLabel") or obj:IsA("TextButton") or obj:IsA("TextBox") then
			local t = obj :: TextLabel
			if not t.TextScaled and t.TextSize < MIN_TEXT_PX then
				flag(`TextSize under {MIN_TEXT_PX}`, obj)
			end
			if t.TextScaled and not t:FindFirstChildOfClass("UITextSizeConstraint") then
				flag("TextScaled without UITextSizeConstraint (huge or tiny text on extreme screens)", obj)
			end
		end
		if obj:IsA("ImageLabel") or obj:IsA("ImageButton") then
			if size.X.Scale > 0 and size.Y.Scale > 0 and not obj:FindFirstChildOfClass("UIAspectRatioConstraint") then
				flag("scaled image without UIAspectRatioConstraint (stretches on other aspect ratios)", obj)
			end
		end
		if obj:IsA("ScrollingFrame") then
			local sf = obj :: ScrollingFrame
			if sf.AutomaticCanvasSize == Enum.AutomaticSize.None and sf:FindFirstChildWhichIsA("UIListLayout") then
				flag("ScrollingFrame with a layout but fixed CanvasSize (use AutomaticCanvasSize)", sf)
			end
		end
	end
end

local lines = { `MOBILE UI AUDIT (static): {guis} ScreenGuis under {root:GetFullName()}` }
local any = false
for kind, n in counts do
	any = true
	table.insert(lines, `[{n}] {kind}`)
	table.insert(lines, `    e.g. {table.concat(issues[kind], ", ")}`)
end
if not any then
	table.insert(
		lines,
		"no static issues found; still check screenshots at phone portrait, phone landscape, tablet and 16:9"
	)
end
local report = table.concat(lines, "\n")
print(report)
return report
