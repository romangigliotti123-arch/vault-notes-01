--!strict
local Players = game:GetService("Players")
local TweenService = game:GetService("TweenService")

local Theme = require((script.Parent :: Instance):WaitForChild("Theme") :: ModuleScript) :: any

local UI = {}

local function corner(parent: Instance)
	local c = Instance.new("UICorner")
	c.CornerRadius = Theme.radius
	c.Parent = parent
end

local function stroke(parent: Instance, color: Color3?)
	local s = Instance.new("UIStroke")
	s.Thickness = Theme.strokeThickness
	s.Color = color or Theme.colors.stroke
	s.ApplyStrokeMode = Enum.ApplyStrokeMode.Border
	s.Parent = parent
end

local function padding(parent: Instance)
	local p = Instance.new("UIPadding")
	local d = UDim.new(0, Theme.padding)
	p.PaddingTop, p.PaddingBottom, p.PaddingLeft, p.PaddingRight = d, d, d, d
	p.Parent = parent
end

local function shade(parent: Instance)
	local g = Instance.new("UIGradient")
	g.Color = ColorSequence.new(Color3.new(1, 1, 1), Color3.fromRGB(205, 205, 215))
	g.Rotation = 90
	g.Parent = parent
end

function UI.root(name: string, layer: number): ScreenGui
	local gui = Instance.new("ScreenGui")
	gui.Name = name
	gui.ResetOnSpawn = false
	gui.ZIndexBehavior = Enum.ZIndexBehavior.Sibling
	gui.ScreenInsets = Enum.ScreenInsets.CoreUISafeInsets
	gui.DisplayOrder = layer
	gui.Parent = Players.LocalPlayer:WaitForChild("PlayerGui")
	return gui
end

export type PanelOpts = { name: string?, size: UDim2?, alt: boolean?, auto: boolean? }

function UI.panel(parent: Instance, opts: PanelOpts?): Frame
	local o: PanelOpts = opts or {}
	local f = Instance.new("Frame")
	f.Name = o.name or "Panel"
	f.BackgroundColor3 = if o.alt then Theme.colors.panelAlt else Theme.colors.panel
	f.BorderSizePixel = 0
	f.Size = o.size or UDim2.fromScale(1, 0)
	if o.auto ~= false then
		f.AutomaticSize = Enum.AutomaticSize.Y
	end
	corner(f)
	stroke(f)
	padding(f)
	shade(f)
	f.Parent = parent
	return f
end

export type LabelKind = "title" | "heading" | "body" | "small"

function UI.label(parent: Instance, text: string, kind: LabelKind?, color: Color3?): TextLabel
	local k: LabelKind = kind or "body"
	local l = Instance.new("TextLabel")
	l.Name = "Label"
	l.BackgroundTransparency = 1
	l.Size = UDim2.fromScale(1, 0)
	l.AutomaticSize = Enum.AutomaticSize.Y
	l.FontFace = if k == "body" or k == "small" then Theme.fontBody else Theme.font
	l.TextSize = Theme.text[k]
	l.TextColor3 = color or Theme.colors.text
	l.TextXAlignment = Enum.TextXAlignment.Left
	l.TextWrapped = true
	l.Text = text
	local ts = Instance.new("UIStroke")
	ts.Thickness = 1.5
	ts.Color = Theme.colors.stroke
	ts.Transparency = 0.3
	ts.Parent = l
	l.Parent = parent
	return l
end

function UI.button(parent: Instance, text: string, onActivated: () -> (), primary: boolean?): TextButton
	local b = Instance.new("TextButton")
	b.Name = "Button_" .. text
	b.AutoButtonColor = false
	b.BackgroundColor3 = if primary == false then Theme.colors.panelAlt else Theme.colors.accent
	b.TextColor3 = if primary == false then Theme.colors.text else Theme.colors.textOnAccent
	b.FontFace = Theme.font
	b.TextSize = Theme.text.body
	b.Text = text
	b.Size = UDim2.new(1, 0, 0, 48)
	corner(b)
	stroke(b)
	shade(b)
	local scale = Instance.new("UIScale")
	scale.Parent = b
	b.MouseEnter:Connect(function()
		TweenService:Create(scale, Theme.tween.fast, { Scale = 1.05 }):Play()
	end)
	b.MouseLeave:Connect(function()
		TweenService:Create(scale, Theme.tween.fast, { Scale = 1 }):Play()
	end)
	b.Activated:Connect(function()
		TweenService:Create(scale, TweenInfo.new(0.08), { Scale = 0.94 }):Play()
		task.delay(0.08, function()
			TweenService:Create(scale, Theme.tween.pop, { Scale = 1 }):Play()
		end)
		onActivated()
	end)
	b.Parent = parent
	return b
end

function UI.stat(parent: Instance, name: string, value: string): { panel: Frame, set: (string) -> () }
	local p = UI.panel(parent, { name = "Stat_" .. name })
	local row = Instance.new("UIListLayout")
	row.FillDirection = Enum.FillDirection.Horizontal
	row.VerticalAlignment = Enum.VerticalAlignment.Center
	row.Padding = UDim.new(0, Theme.gap)
	row.Parent = p
	local n = UI.label(p, name, "small", Theme.colors.textDim)
	n.Size = UDim2.fromScale(0.5, 0)
	local v = UI.label(p, value, "heading", Theme.colors.accent)
	v.Size = UDim2.fromScale(0.5, 0)
	v.TextXAlignment = Enum.TextXAlignment.Right
	local scale = Instance.new("UIScale")
	scale.Parent = v
	return {
		panel = p,
		set = function(text: string)
			v.Text = text
			scale.Scale = 1.25
			TweenService:Create(scale, Theme.tween.pop, { Scale = 1 }):Play()
		end,
	}
end

function UI.bar(parent: Instance, color: Color3?): { frame: Frame, set: (number) -> () }
	local track = UI.panel(parent, { name = "Bar", size = UDim2.new(1, 0, 0, 22), alt = true, auto = false })
	for _, child in track:GetChildren() do
		if child:IsA("UIPadding") or child:IsA("UIGradient") then
			child:Destroy()
		end
	end
	track.ClipsDescendants = true
	local fill = Instance.new("Frame")
	fill.Name = "Fill"
	fill.BackgroundColor3 = color or Theme.colors.accent2
	fill.BorderSizePixel = 0
	fill.Size = UDim2.fromScale(0, 1)
	corner(fill)
	fill.Parent = track
	return {
		frame = track,
		set = function(ratio: number)
			TweenService:Create(fill, Theme.tween.slide, { Size = UDim2.fromScale(math.clamp(ratio, 0, 1), 1) }):Play()
		end,
	}
end

export type Hud = { TopLeft: Frame, TopCenter: Frame, TopRight: Frame, BottomCenter: Frame }
local hudRef: Hud? = nil

function UI.hud(): Hud
	local gui = UI.root("HUD", Theme.layer.hud)
	local function slot(name: string, anchor: Vector2, pos: UDim2, widthScale: number): Frame
		local f = Instance.new("Frame")
		f.Name = name
		f.BackgroundTransparency = 1
		f.AnchorPoint = anchor
		f.Position = pos
		f.Size = UDim2.fromScale(widthScale, 0)
		f.AutomaticSize = Enum.AutomaticSize.Y
		local cap = Instance.new("UISizeConstraint")
		cap.MaxSize = Vector2.new(320, math.huge)
		cap.Parent = f
		local list = Instance.new("UIListLayout")
		list.Padding = UDim.new(0, Theme.gap)
		list.SortOrder = Enum.SortOrder.LayoutOrder
		list.VerticalAlignment = if anchor.Y == 1 then Enum.VerticalAlignment.Bottom else Enum.VerticalAlignment.Top
		list.Parent = f
		f.Parent = gui
		return f
	end
	local hud: Hud = {
		TopLeft = slot("TopLeft", Vector2.new(0, 0), UDim2.fromOffset(12, 12), 0.28),
		TopCenter = slot("TopCenter", Vector2.new(0.5, 0), UDim2.new(0.5, 0, 0, 12), 0.3),
		TopRight = slot("TopRight", Vector2.new(1, 0), UDim2.new(1, -12, 0, 12), 0.28),
		BottomCenter = slot("BottomCenter", Vector2.new(0.5, 1), UDim2.new(0.5, 0, 1, -12), 0.4),
	}
	hudRef = hud
	return hud
end

local popupGui: ScreenGui? = nil
local popupQueue: { { title: string, body: string, seconds: number } } = {}
local popupBusy = false

local function showNext()
	local nextItem = table.remove(popupQueue, 1)
	if not nextItem then
		popupBusy = false
		return
	end
	popupBusy = true
	if not popupGui then
		popupGui = UI.root("Popups", Theme.layer.popup)
	end
	local group = Instance.new("CanvasGroup")
	group.Name = "Popup"
	group.AnchorPoint = Vector2.new(0.5, 0.5)
	group.Position = UDim2.fromScale(0.5, 0.55)
	group.Size = UDim2.fromScale(0.4, 0)
	group.AutomaticSize = Enum.AutomaticSize.Y
	group.BackgroundTransparency = 1
	group.GroupTransparency = 1
	local cap = Instance.new("UISizeConstraint")
	cap.MaxSize = Vector2.new(420, math.huge)
	cap.Parent = group
	local list = Instance.new("UIListLayout")
	list.Parent = group
	local panel = UI.panel(group, { name = "PopupPanel" })
	local inner = Instance.new("UIListLayout")
	inner.Padding = UDim.new(0, Theme.gap)
	inner.Parent = panel
	local t = UI.label(panel, nextItem.title, "title", Theme.colors.accent)
	t.TextXAlignment = Enum.TextXAlignment.Center
	if nextItem.body ~= "" then
		local b = UI.label(panel, nextItem.body, "body")
		b.TextXAlignment = Enum.TextXAlignment.Center
	end
	local scale = Instance.new("UIScale")
	scale.Scale = 0.7
	scale.Parent = group
	group.Parent = popupGui
	TweenService:Create(group, Theme.tween.fade, { GroupTransparency = 0 }):Play()
	TweenService:Create(scale, Theme.tween.pop, { Scale = 1 }):Play()
	task.delay(nextItem.seconds, function()
		local out = TweenService:Create(group, Theme.tween.fade, { GroupTransparency = 1 })
		out.Completed:Connect(function()
			group:Destroy()
			showNext()
		end)
		out:Play()
	end)
end

function UI.popup(title: string, body: string?, seconds: number?)
	table.insert(popupQueue, { title = title, body = body or "", seconds = seconds or 2.2 })
	if not popupBusy then
		showNext()
	end
end

local toastLabel: TextLabel? = nil
function UI.toast(text: string)
	if not toastLabel then
		local host: Instance = if hudRef then hudRef.TopCenter else UI.root("Toasts", Theme.layer.toast)
		local p = UI.panel(host, { name = "Toast" })
		p.LayoutOrder = 99
		p.Visible = false
		local made = UI.label(p, "", "body")
		made.TextXAlignment = Enum.TextXAlignment.Center
		toastLabel = made
	end
	local l = toastLabel :: TextLabel
	local p = l.Parent :: Frame
	l.Text = text
	p.Visible = true
	local id = os.clock()
	p:SetAttribute("ToastId", id)
	task.delay(1.8, function()
		if p:GetAttribute("ToastId") == id then
			p.Visible = false
		end
	end)
end

return UI
