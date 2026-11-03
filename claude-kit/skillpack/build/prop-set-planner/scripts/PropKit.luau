--!strict
-- PropKit: size a reusable prop kit and cost the scene it dresses. Pure logic, unit-tested under Lune.
-- Vault (optimization KB, Creator Docs estimates): about 1 second of load per 10,000 instances sent to the client, about 500 bytes of
-- client memory per instance, aim for about 150,000 client instances or fewer with streaming on; cloned MeshParts that reuse a
-- MeshId keep memory roughly constant (reuse beats unique art). Densities below are inputs, not recommendations.
local PropKit = {}

export type Prop = {
	name: string,
	variants: number, -- distinct meshes/looks in the kit
	instancesPer: number, -- instances one placed copy adds (parts + attachments + decals + scripts...)
	per1000: number, -- placed copies per 1000 studs^2 of dressed area
}
export type Result = {
	placed: { [string]: number },
	instances: number,
	loadSeconds: number,
	clientMB: number,
	uniqueMeshes: number,
	issues: { string },
}

PropKit.INSTANCES_PER_SECOND = 10000
PropKit.BYTES_PER_INSTANCE = 500
PropKit.CLIENT_GUIDE = 150000

function PropKit.plan(areaStuds2: number, props: { Prop }, maxInstances: number?): Result
	local limit = maxInstances or PropKit.CLIENT_GUIDE
	local placed: { [string]: number } = {}
	local instances, meshes = 0, 0
	local issues: { string } = {}
	for _, p in props do
		local n = math.floor(areaStuds2 / 1000 * p.per1000 + 0.5)
		placed[p.name] = n
		instances += n * p.instancesPer
		meshes += p.variants
		if n > 0 and n < p.variants then
			table.insert(issues, `{p.name}: {p.variants} variants but only {n} placed, drop variants`)
		end
	end
	if instances > limit then
		table.insert(issues, `{instances} instances above the guide of {limit}: lower density, merge props, or stream`)
	end
	return {
		placed = placed,
		instances = instances,
		loadSeconds = instances / PropKit.INSTANCES_PER_SECOND,
		clientMB = instances * PropKit.BYTES_PER_INSTANCE / (1024 * 1024),
		uniqueMeshes = meshes,
		issues = issues,
	}
end

-- Reuse ratio: placed copies per unique mesh. Low ratios mean the kit is too varied to be cheap.
function PropKit.reuse(r: Result): number
	local copies = 0
	for _, n in r.placed do
		copies += n
	end
	return if r.uniqueMeshes > 0 then copies / r.uniqueMeshes else 0
end

return PropKit
