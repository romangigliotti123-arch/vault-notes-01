--!strict
-- Theme: the ONE place for the game's look. Every panel, button, label and popup reads these tokens (UI.luau) so the UI cannot drift.
-- Copy into ReplicatedStorage.Shared.StyleKit and replace the values with the ones in art-direction.md. Never hard-code a colour, font,
-- radius, stroke or text size anywhere else.
local Theme = {}

Theme.colors = {
	bg = Color3.fromRGB(24, 32, 56), -- screen-dimmer / deep background
	panel = Color3.fromRGB(44, 62, 108), -- default panel fill
	panelAlt = Color3.fromRGB(62, 84, 140), -- inner rows, inactive buttons
	accent = Color3.fromRGB(255, 196, 61), -- primary action, focal numbers
	accent2 = Color3.fromRGB(64, 200, 190), -- secondary highlight
	good = Color3.fromRGB(96, 214, 110),
	bad = Color3.fromRGB(240, 92, 92),
	text = Color3.fromRGB(255, 255, 255),
	textDim = Color3.fromRGB(200, 212, 240),
	textOnAccent = Color3.fromRGB(40, 28, 8),
	stroke = Color3.fromRGB(14, 20, 40),
}

Theme.font = Font.fromEnum(Enum.Font.FredokaOne) -- display text; replace with the font chosen in art-direction.md
Theme.fontBody = Font.fromEnum(Enum.Font.GothamMedium)

-- type scale in pixels at 1x (phone-readable minimum is 14)
Theme.text = { title = 32, heading = 24, body = 18, small = 14 }

Theme.radius = UDim.new(0, 12)
Theme.strokeThickness = 2
Theme.padding = 10
Theme.gap = 8
Theme.shadowOffset = UDim2.fromOffset(0, 4)
Theme.shadowTransparency = 0.6

Theme.tween = {
	fast = TweenInfo.new(0.12, Enum.EasingStyle.Quad, Enum.EasingDirection.Out),
	pop = TweenInfo.new(0.28, Enum.EasingStyle.Back, Enum.EasingDirection.Out),
	slide = TweenInfo.new(0.3, Enum.EasingStyle.Quint, Enum.EasingDirection.Out),
	fade = TweenInfo.new(0.25, Enum.EasingStyle.Sine, Enum.EasingDirection.InOut),
}

-- DisplayOrder per layer: HUD under popups under toasts. Never invent another number elsewhere.
Theme.layer = { hud = 1, popup = 10, toast = 20, fullscreen = 30 }

-- Sound registry: name -> rbxassetid. Fill ONLY with ids from search_asset/insert_asset results or the user's own assets. 0 = silent (a V6 gap to report).
Theme.sounds = {
	click = "rbxassetid://0",
	collect = "rbxassetid://0",
	reward = "rbxassetid://0",
	error = "rbxassetid://0",
	popup = "rbxassetid://0",
}

return Theme
