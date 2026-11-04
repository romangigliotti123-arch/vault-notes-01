--!strict
local Theme = {}

Theme.colors = {
	bg = Color3.fromRGB(24, 32, 56),
	panel = Color3.fromRGB(44, 62, 108),
	panelAlt = Color3.fromRGB(62, 84, 140),
	accent = Color3.fromRGB(255, 196, 61),
	accent2 = Color3.fromRGB(64, 200, 190),
	good = Color3.fromRGB(96, 214, 110),
	bad = Color3.fromRGB(240, 92, 92),
	text = Color3.fromRGB(255, 255, 255),
	textDim = Color3.fromRGB(200, 212, 240),
	textOnAccent = Color3.fromRGB(40, 28, 8),
	stroke = Color3.fromRGB(14, 20, 40),
}

Theme.font = Font.fromEnum(Enum.Font.FredokaOne)
Theme.fontBody = Font.fromEnum(Enum.Font.GothamMedium)

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

Theme.layer = { hud = 1, popup = 10, toast = 20, fullscreen = 30 }

Theme.sounds = {
	click = "rbxassetid://0",
	collect = "rbxassetid://0",
	reward = "rbxassetid://0",
	error = "rbxassetid://0",
	popup = "rbxassetid://0",
}

return Theme
