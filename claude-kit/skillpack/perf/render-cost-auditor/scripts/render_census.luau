--!strict
local Workspace = game:GetService("Workspace")
local Lighting = game:GetService("Lighting")

local c = {
	parts = 0,
	castShadow = 0,
	partialTransparent = 0,
	neon = 0,
	glass = 0,
	pbr = 0,
	lightsShadowed = 0,
	lightsTotal = 0,
	emitters = 0,
	liveParticles = 0,
	beams = 0,
	trails = 0,
	highlights = 0,
	surfaceGuis = 0,
	billboardGuis = 0,
	decalsOnTransparent = 0,
}

for _, inst in Workspace:GetDescendants() do
	do
		if inst:IsA("BasePart") then
			local p = inst :: BasePart
			c.parts += 1
			if p.CastShadow then
				c.castShadow += 1
			end
			if p.Transparency > 0 and p.Transparency < 1 then
				c.partialTransparent += 1
			end
			if p.Material == Enum.Material.Neon then
				c.neon += 1
			elseif p.Material == Enum.Material.Glass then
				c.glass += 1
			end
		elseif inst:IsA("SurfaceAppearance") then
			c.pbr += 1
		elseif inst:IsA("Light") then
			local l = inst :: Light
			c.lightsTotal += 1
			if l.Shadows then
				c.lightsShadowed += 1
			end
		elseif inst:IsA("ParticleEmitter") then
			local e = inst :: ParticleEmitter
			c.emitters += 1
			if e.Enabled then
				c.liveParticles += e.Rate * (e.Lifetime.Min + e.Lifetime.Max) / 2
			end
		elseif inst:IsA("Beam") then
			c.beams += 1
		elseif inst:IsA("Trail") then
			c.trails += 1
		elseif inst:IsA("Highlight") then
			c.highlights += 1
		elseif inst:IsA("SurfaceGui") then
			c.surfaceGuis += 1
		elseif inst:IsA("BillboardGui") then
			c.billboardGuis += 1
		elseif inst:IsA("Decal") or inst:IsA("Texture") then
			local parent = inst.Parent
			if parent and parent:IsA("BasePart") and (parent :: BasePart).Transparency >= 1 then
				c.decalsOnTransparent += 1
			end
		end
	end
end

local lines = {
	"Lighting.Technology="
		.. tostring((Lighting :: any).Technology)
		.. " (ShadowMap is the recommended default; Future only when visuals need it)",
	("parts=%d castShadow=%d partialTransparent=%d neon=%d glass=%d surfaceAppearance=%d"):format(
		c.parts,
		c.castShadow,
		c.partialTransparent,
		c.neon,
		c.glass,
		c.pbr
	),
	("lights=%d shadowed=%d  emitters=%d estLiveParticles=%.0f beams=%d trails=%d"):format(
		c.lightsTotal,
		c.lightsShadowed,
		c.emitters,
		c.liveParticles,
		c.beams,
		c.trails
	),
	("highlights=%d (cap 255) surfaceGuis=%d billboardGuis=%d decalsOnFullyTransparentParts=%d"):format(
		c.highlights,
		c.surfaceGuis,
		c.billboardGuis,
		c.decalsOnTransparent
	),
}
local post = {}
for _, e in Lighting:GetChildren() do
	if e:IsA("PostEffect") or e:IsA("Atmosphere") or e:IsA("Clouds") then
		table.insert(post, e.ClassName)
	end
end
table.insert(lines, "Lighting children: " .. (#post > 0 and table.concat(post, ", ") or "none"))
return table.concat(lines, "\n")
