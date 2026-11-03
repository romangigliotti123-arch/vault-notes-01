--!strict
-- scan_place.luau: read-only census of a place for performance triage. Counts what usually costs memory, CPU or bandwidth and
-- prints a ranked hot list. Studio command bar or MCP `execute_luau` (Edit). Numbers are counts, not frame times: always confirm
-- with the profiler (MicroProfiler / Performance Summary) before and after a fix.
local TOP_MODELS = 8

local Workspace = game:GetService("Workspace")

local c = {
	parts = 0,
	meshParts = 0,
	unions = 0,
	unanchored = 0,
	canTouch = 0,
	canQuery = 0,
	preciseCollision = 0,
	transparent = 0,
	castShadowParts = 0,
	lights = 0,
	shadowLights = 0,
	emitters = 0,
	beamsTrails = 0,
	decals = 0,
	surfaceGuis = 0,
	billboardGuis = 0,
	sounds = 0,
	humanoids = 0,
	scripts = 0,
	constraints = 0,
	instances = 0,
}
local modelParts: { [Model]: number } = {}

for _, inst in Workspace:GetDescendants() do
	c.instances += 1
	if inst:IsA("BasePart") then
		local part = inst :: BasePart
		c.parts += 1
		if part:IsA("MeshPart") then
			c.meshParts += 1
			if (part :: MeshPart).CollisionFidelity == Enum.CollisionFidelity.PreciseConvexDecomposition then
				c.preciseCollision += 1
			end
		elseif part:IsA("UnionOperation") then
			c.unions += 1
			if (part :: UnionOperation).CollisionFidelity == Enum.CollisionFidelity.PreciseConvexDecomposition then
				c.preciseCollision += 1
			end
		end
		if not part.Anchored then
			c.unanchored += 1
		end
		if part.CanTouch then
			c.canTouch += 1
		end
		if part.CanQuery then
			c.canQuery += 1
		end
		if part.Transparency > 0 then
			c.transparent += 1
		end
		if part.CastShadow then
			c.castShadowParts += 1
		end
		local model = part:FindFirstAncestorOfClass("Model")
		if model then
			modelParts[model] = (modelParts[model] or 0) + 1
		end
	elseif inst:IsA("Light") then
		c.lights += 1
		if (inst :: Light).Shadows then
			c.shadowLights += 1
		end
	elseif inst:IsA("ParticleEmitter") then
		c.emitters += 1
	elseif inst:IsA("Beam") or inst:IsA("Trail") then
		c.beamsTrails += 1
	elseif inst:IsA("Decal") or inst:IsA("Texture") then
		c.decals += 1
	elseif inst:IsA("SurfaceGui") then
		c.surfaceGuis += 1
	elseif inst:IsA("BillboardGui") then
		c.billboardGuis += 1
	elseif inst:IsA("Sound") then
		c.sounds += 1
	elseif inst:IsA("Humanoid") then
		c.humanoids += 1
	elseif inst:IsA("LuaSourceContainer") then
		c.scripts += 1
	elseif inst:IsA("Constraint") then
		c.constraints += 1
	end
end

local ranked = {}
for model, n in modelParts do
	table.insert(ranked, { model = model, n = n })
end
table.sort(ranked, function(a, b)
	return a.n > b.n
end)

local lines = {}
table.insert(lines, `PLACE SCAN (Workspace descendants: {c.instances})`)
table.insert(
	lines,
	`StreamingEnabled={tostring(Workspace.StreamingEnabled)} (a big map with it off is the first thing to fix)`
)
table.insert(
	lines,
	`parts={c.parts} meshParts={c.meshParts} unions={c.unions} unanchored={c.unanchored} constraints={c.constraints}`
)
table.insert(
	lines,
	`CanTouch parts={c.canTouch} CanQuery parts={c.canQuery} (turn off on scenery that never needs events or raycast hits)`
)
table.insert(lines, `PreciseConvexDecomposition={c.preciseCollision} (costliest collision; Box/Hull where possible)`)
table.insert(
	lines,
	`transparent parts={c.transparent} shadow-casting parts={c.castShadowParts} lights={c.lights} (with shadows: {c.shadowLights})`
)
table.insert(
	lines,
	`particle emitters={c.emitters} beams/trails={c.beamsTrails} decals/textures={c.decals} SurfaceGuis={c.surfaceGuis} BillboardGuis={c.billboardGuis}`
)
table.insert(lines, `sounds={c.sounds} humanoids={c.humanoids} scripts={c.scripts}`)
table.insert(lines, `largest models by part count:`)
for i = 1, math.min(TOP_MODELS, #ranked) do
	table.insert(lines, `  {ranked[i].n} parts: {ranked[i].model:GetFullName()}`)
end
local report = table.concat(lines, "\n")
print(report)
return report
