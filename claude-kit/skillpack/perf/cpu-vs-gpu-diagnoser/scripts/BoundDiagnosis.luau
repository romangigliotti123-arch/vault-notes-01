--!strict
-- BoundDiagnosis: classify a slow frame as GPU-bound, CPU-script/physics-bound or CPU render-prep-bound from MicroProfiler numbers. Pure logic, Lune-tested.
-- Rules from the vault optimization KB (creator guide, MicroProfiler colour reading) and Creator Docs performance-optimization/identify (official frame budget 16.67 ms):
--   orange bars (Jobs > Render): scripts, physics or animation;  blue bars (Render > Jobs): object density, movement or lighting;
--   red (GPU wait over 2.5 ms): scene complexity, texture size or VFX. "Act on colour only when the frame goal is missed."
-- Inputs are the numbers you read from a paused MicroProfiler frame (Ctrl+P): total frame ms, Jobs (main-thread/simulation) ms, Render prep ms, and the GPU wait ms.
local BoundDiagnosis = {}

export type Frame = { frameMs: number, jobsMs: number, renderMs: number, gpuWaitMs: number }
export type Diagnosis = { bound: string, colour: string, nextSkills: { string }, note: string }

BoundDiagnosis.GPU_WAIT_MS = 2.5

function BoundDiagnosis.diagnose(f: Frame, goalMs: number?): Diagnosis
	local goal = goalMs or 1000 / 60
	if f.frameMs <= goal then
		return {
			bound = "none",
			colour = "-",
			nextSkills = {},
			note = "frame is inside the goal; do not optimise this scene",
		}
	end
	if f.gpuWaitMs > BoundDiagnosis.GPU_WAIT_MS then
		return {
			bound = "gpu",
			colour = "red",
			nextSkills = { "render-cost-auditor", "texture-budget-checker", "effects-budget-setter" },
			note = "GPU wait over 2.5 ms: reduce shadows, overdraw, texture size, particles",
		}
	end
	if f.jobsMs > f.renderMs then
		return {
			bound = "cpu-simulation",
			colour = "orange",
			nextSkills = { "script-profiler", "physics-load-reducer", "animation-cost-reducer" },
			note = "Jobs exceed Render: scripts, physics or animation dominate",
		}
	end
	return {
		bound = "cpu-render-prep",
		colour = "blue",
		nextSkills = { "part-count-auditor", "render-cost-auditor" },
		note = "Render exceeds Jobs: too many objects in view, movement or lighting cost",
	}
end

-- Compare two frames of the same scenario after a fix: positive = faster. Needs the same goal.
function BoundDiagnosis.improvement(before: Frame, after: Frame): number
	if before.frameMs <= 0 then
		return 0
	end
	return (before.frameMs - after.frameMs) / before.frameMs * 100
end

return BoundDiagnosis
