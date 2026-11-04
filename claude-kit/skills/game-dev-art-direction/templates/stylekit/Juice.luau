--!strict
local Debris = game:GetService("Debris")
local TweenService = game:GetService("TweenService")

local Theme = require((script.Parent :: Instance):WaitForChild("Theme") :: ModuleScript) :: any

local Juice = {}

local PRESETS: { [string]: { count: number, speed: number, size: number, life: number, color: Color3 } } = {
	collect = { count = 10, speed = 14, size = 0.5, life = 0.6, color = Color3.fromRGB(255, 220, 90) },
	reward = { count = 24, speed = 22, size = 0.7, life = 0.9, color = Color3.fromRGB(255, 196, 61) },
	hit = { count = 14, speed = 26, size = 0.4, life = 0.4, color = Color3.fromRGB(255, 255, 255) },
	splash = { count = 18, speed = 16, size = 0.6, life = 0.8, color = Color3.fromRGB(150, 220, 255) },
}

function Juice.burst(at: BasePart, preset: string)
	local p = PRESETS[preset] or PRESETS.collect
	local e = Instance.new("ParticleEmitter")
	e.Enabled = false
	e.Color = ColorSequence.new(p.color)
	e.LightEmission = 0.6
	e.LightInfluence = 0
	e.Lifetime = NumberRange.new(p.life * 0.7, p.life)
	e.Speed = NumberRange.new(p.speed * 0.6, p.speed)
	e.SpreadAngle = Vector2.new(180, 180)
	e.Size = NumberSequence.new({ NumberSequenceKeypoint.new(0, p.size), NumberSequenceKeypoint.new(1, 0) })
	e.Transparency = NumberSequence.new({ NumberSequenceKeypoint.new(0, 0), NumberSequenceKeypoint.new(1, 1) })
	e.Parent = at
	e:Emit(p.count)
	Debris:AddItem(e, p.life + 0.2)
end

function Juice.floatText(at: BasePart, text: string, color: Color3?)
	local bb = Instance.new("BillboardGui")
	bb.Size = UDim2.fromOffset(120, 40)
	bb.StudsOffset = Vector3.new(0, 3, 0)
	bb.AlwaysOnTop = true
	local l = Instance.new("TextLabel")
	l.Size = UDim2.fromScale(1, 1)
	l.BackgroundTransparency = 1
	l.FontFace = Theme.font
	l.TextSize = Theme.text.heading
	l.TextColor3 = color or Theme.colors.accent
	l.Text = text
	local s = Instance.new("UIStroke")
	s.Thickness = 2
	s.Color = Theme.colors.stroke
	s.Parent = l
	l.Parent = bb
	bb.Parent = at
	TweenService:Create(bb, Theme.tween.slide, { StudsOffset = Vector3.new(0, 6, 0) }):Play()
	TweenService:Create(l, Theme.tween.fade, { TextTransparency = 1 }):Play()
	TweenService:Create(s, Theme.tween.fade, { Transparency = 1 }):Play()
	Debris:AddItem(bb, 0.8)
end

function Juice.squash(part: BasePart, amount: number?)
	local a = amount or 0.25
	local original = part.Size
	part.Size = original * Vector3.new(1 + a, 1 - a, 1 + a)
	TweenService:Create(part, Theme.tween.pop, { Size = original }):Play()
end

function Juice.sound(name: string, at: Instance?)
	local id = Theme.sounds[name]
	if not id or id == "rbxassetid://0" then
		return
	end
	local snd = Instance.new("Sound")
	snd.SoundId = id
	snd.Volume = 0.5
	snd.Parent = at or workspace
	snd:Play()
	Debris:AddItem(snd, 3)
end

return Juice
