# rbx-perf-models: the exact rules

Facts used (read 2026-11): vault KB optimization-and-streaming and physics topics (kbq); create.roblox.com/docs/performance-optimization/improve (CanCollide, CanTouch and CanQuery off for parts that need no collision; collision geometry stays in memory even when collisions are off, Box has the lowest overhead, "generally safe to set any small anchored part's collision fidelity to Box"; CastShadow off on small parts "might result in visual artifacts"; RenderFidelity Automatic or Performance); reference/engine/classes/Stats (InstanceCount and PrimitivesCount deprecated, MovingPrimitivesCount, ContactsCount, GetTotalMemoryUsageMb). The BasePart reference page gave no semantics, so behaviour claims about CanQuery come from the KB and the page above. Low confidence: that default camera occlusion ignores CanCollide-off parts (S2 requires CanCollide off for that reason).

## Decorative part (D1-D8): all must hold, else the part is "kept as is"
- D1 class is Part, MeshPart, UnionOperation, NegateOperation, WedgePart or CornerWedgePart (never Seat, VehicleSeat, SpawnLocation, TrussPart, Terrain).
- D2 children only from: Decal, Texture, SurfaceAppearance, SpecialMesh, BlockMesh, CylinderMesh, FileMesh, PointLight, SpotLight, SurfaceLight, ParticleEmitter, Fire, Smoke, Sparkles, Sound. Anything else (Attachment, welds, ClickDetector, ProximityPrompt, scripts, Humanoid, SurfaceGui) = not decorative.
- D3 no tags, no attributes. D4 not the target of a weld, constraint (through its Attachment), Model.PrimaryPart, ObjectValue, Adornee, Beam or Trail.
- D5 not inside (or being) a container that has a script child, a Humanoid, is a Tool/Accessory, is tagged or has attributes, or holds a Seat/VehicleSeat/SpawnLocation/TrussPart (that container's whole subtree is excluded).
- D6 neither its name nor any parent's name is used by any script in the game (word match on identifiers and string literals; `Name1`/`Name2` families by base name; class names inside Instance.new, IsA and FindFirstChildOfClass are ignored).
- D7 no interactive word in its name or any parent's name (kill, lava, damage, spawn, checkpoint, trigger, zone, door, gate, ladder, seat, vehicle, button, lever, pickup, coin, portal, teleport, goal, hitbox, sensor, platform, elevator, barrier, npc, enemy, shop, click and similar).
- D8 every script in the game was readable and the scan was not capped.

## SAFE rules (the only things applied without per-id approval)
- S2 CanQuery true -> false: decorative, anchored, CanCollide already false (or turned off by S4), and no script uses raycasts or spatial queries (Raycast, Spherecast, Blockcast, GetPartBoundsIn*, GetPartsInPart, FindPartOnRay*, FindPartsInRegion3*, ViewportPointToRay, ScreenPointToRay, Mouse.Target).
- S3 CanTouch true -> false: decorative, anchored, and no script both listens to touches (Touched, TouchEnded, GetTouchingParts) and iterates broadly or watches the character (GetDescendants, GetChildren, GetTagged, HumanoidRootPart, feet, Character, Torso, Head).
- S4 CanCollide true -> false: decorative, anchored, and every corner of its bounding box lies at least 0.01 stud inside a bigger anchored, collidable, decorative Block part that stays collidable. Nobody can reach it, so collision there is unchanged (edge case: a player placed inside the block).
- S5 move to ServerStorage.PerfPass_Removed: decorative, no children at all, Transparency 1, CanCollide false, not queried (or no query scripts), not touched (or no broad touch scripts).
- S6 move to ServerStorage.PerfPass_Removed: decorative, anchored, no children, Transparency 0, and identical in class, shape, size, position and rotation (3 decimals), material, variant, color, reflectance, shadow, anchored, collision flags, fidelity and mesh/texture ids to a kept twin (the lowest id of the group stays).
- S7 CollisionFidelity -> Box: decorative, anchored MeshPart/Union whose CanCollide, CanQuery and CanTouch are all off after S2-S4 (collision geometry is still stored in memory).
SAFE properties written: CanQuery, CanTouch, CanCollide, CollisionFidelity, and the move of S5/S6. Nothing else; the runner refuses any other property, and visual properties without an approval.

## REVIEW (reported with estimated gain and risk; applied only per approved id)
RV-SHADOW (CastShadow off, parts up to 2 studs), RV-ANCHOR (unanchored parts without joints or scripts), RV-COLLIDE (CanCollide off on small anchored decorative parts), RV-FIDELITY-BOX / RV-FIDELITY-HULL (collision shape), RV-RENDER (RenderFidelity Precise -> Automatic), RV-QUERY / RV-TOUCH (SAFE-like changes blocked by a script that queries or listens broadly). Report only, no automatic action: RV-TEXTURES, RV-LIGHTS, RV-PARTICLES, RV-STREAMING, RV-MERGE (clusters of 50+ identical small anchored parts), RV-TRANSPARENT.

## Appearance diff (what must be identical)
class, name, parent, Transparency, Reflectance, Material, MaterialVariant, Color, Shape, Size, CFrame, RenderFidelity, MeshId, TextureID, CastShadow, child classes and a hash of every Decal/Texture/SurfaceAppearance/mesh/light/emitter property, tags, attributes. Behaviour fields (Anchored, CanCollide, CanQuery, CanTouch, Massless, CollisionFidelity) may differ only exactly as planned. Removed parts must be Transparency 1 or have an identical opaque twin at the same place.

## Cannot be improved without a visible change
High-poly meshes (triangle counts are not readable from Luau), unions, lights, particles, large textures, partly transparent parts, unique materials. They are listed in the report and never touched.
