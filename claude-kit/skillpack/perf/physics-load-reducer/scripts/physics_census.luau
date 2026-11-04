--!strict
local TOP = 8

local Workspace = game:GetService("Workspace")

local c = {
	parts = 0,
	unanchored = 0,
	assemblies = 0,
	moving = 0,
	canTouch = 0,
	canQuery = 0,
	canCollide = 0,
	constraints = 0,
	welds = 0,
	motor6d = 0,
}
local seenRoots: { [BasePart]: boolean } = {}
local biggest: { [string]: number } = {}

for _, inst in Workspace:GetDescendants() do
	if inst:IsA("BasePart") and not inst:IsA("Terrain") then
		local part = inst :: BasePart
		c.parts += 1
		if part.CanTouch then
			c.canTouch += 1
		end
		if part.CanQuery then
			c.canQuery += 1
		end
		if part.CanCollide then
			c.canCollide += 1
		end
		if not part.Anchored then
			c.unanchored += 1
			local root = part.AssemblyRootPart
			if root and not seenRoots[root] then
				seenRoots[root] = true
				c.assemblies += 1
				local m = root.AssemblyLinearVelocity.Magnitude
				if m > 0.33 then
					c.moving += 1
				end
				local owner = root:GetFullName()
				biggest[owner] = #root:GetConnectedParts(true)
			end
		end
	elseif inst:IsA("Constraint") then
		c.constraints += 1
	elseif inst:IsA("WeldConstraint") or inst:IsA("Weld") then
		c.welds += 1
	elseif inst:IsA("Motor6D") then
		c.motor6d += 1
	end
end

local ranked: { { name: string, parts: number } } = {}
for name, n in biggest do
	table.insert(ranked, { name = name, parts = n })
end
table.sort(ranked, function(a, b)
	return a.parts > b.parts
end)

local lines = {
	("parts=%d unanchored=%d (%.1f%%) assemblies=%d moving-now=%d"):format(
		c.parts,
		c.unanchored,
		c.parts > 0 and c.unanchored / c.parts * 100 or 0,
		c.assemblies,
		c.moving
	),
	("CanTouch=%d CanQuery=%d CanCollide=%d constraints=%d welds=%d motor6d=%d"):format(
		c.canTouch,
		c.canQuery,
		c.canCollide,
		c.constraints,
		c.welds,
		c.motor6d
	),
	"PhysicsSteppingMethod="
		.. tostring((Workspace :: any).PhysicsSteppingMethod)
		.. " (docs: Adaptive recommended in most cases)",
	"Largest unanchored assemblies (parts connected):",
}
for i = 1, math.min(TOP, #ranked) do
	table.insert(lines, ("  %4d  %s"):format(ranked[i].parts, ranked[i].name))
end
table.insert(
	lines,
	"Next: anchor static props, CanTouch/CanQuery off on scenery, fewer constraints per contraption, Debris-clean fragments, then re-measure physics time."
)
return table.concat(lines, "\n")
