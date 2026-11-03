---
type: research-recall
topic: "Blender 3D for Roblox Studio: using Claude with Blender (blender-mcp, bpy scripting) and the Blender-to-Roblox asset pipeline"
date: 2026-11-01
---
# Recall check: Blender 3D for Roblox Studio: using Claude with Blender (blender-mcp, bpy scripting) and the Blender-to-Roblox asset pipeline

Ten questions drawn from the sources. Answer from memory first, then open the answer.

1. **Q:** What does deleting the 'Roblox Package ID' custom property do on the next plugin upload?
   <details><summary>Answer</summary>It makes the next upload a new asset ID instead of updating the existing package. [[sources/off-gh-roblox-blender-plugin-README|off-gh-roblox-blender-plugin-README]]</details>
2. **Q:** What is the Open Cloud Assets API size limit per call, and how do you get the assetId?
   <details><summary>Answer</summary>20 MB per asset per call. Poll the returned operation for the assetId and moderation result. [[sources/off-cloud_guides_usage-assets|off-cloud_guides_usage-assets]] [[sources/web-57279f4b4c|web-57279f4b4c]]</details>
3. **Q:** Which Blender FBX export settings does Roblox recommend?
   <details><summary>Answer</summary>Apply Scalings = FBX Unit Scale, Path Mode Copy with Embed Textures, Add Leaf Bones off, selected objects only, modifiers applied or removed. [[sources/off-art_accessories_creating_exporting|off-art_accessories_creating_exporting]] [[sources/off-art_blender|off-art_blender]] [[sources/off-art_modeling_export-requirements|off-art_modeling_export-requirements]] [[sources/off-art_characters_creating_blender-configurations|off-art_characters_creating_blender-configurations]]</details>
4. **Q:** How did importer unit conversion change on June 16, 2026?
   <details><summary>Answer</summary>Non-Stud units moved from 20 studs/m to 25:7 studs/m. A Scale Factor field was added, and 5.6 preserves the old behavior. [[sources/off-dev_4644371|off-dev_4644371]]</details>
5. **Q:** What is the Reimport shortcut, and what is the naming pitfall?
   <details><summary>Answer</summary>Alt+Shift+R. It matches meshes by name, so renaming a mesh in Blender creates a new MeshPart and leaves the old one. [[sources/off-dev_4068650|off-dev_4068650]] [[sources/off-dev_4112031|off-dev_4112031]]</details>
6. **Q:** What are the triangle limits for a single mesh and a rigid accessory?
   <details><summary>Answer</summary>A single mesh is at most 20,000 triangles. A rigid accessory is one mesh at most 4,000 triangles. [[sources/web-7195087017|web-7195087017]] [[sources/off-dev_3958222|off-dev_3958222]] [[sources/off-avatar_layered-accessories_specifications|off-avatar_layered-accessories_specifications]] [[sources/web-04cef4e0ee|web-04cef4e0ee]]</details>
7. **Q:** What are the cage names for layered accessories?
   <details><summary>Answer</summary><Mesh>_InnerCage and <Mesh>_OuterCage. Never delete cage vertices or alter cage UVs. [[sources/off-art_modeling_specifications|off-art_modeling_specifications]] [[sources/off-avatar_layered-accessories_specifications|off-avatar_layered-accessories_specifications]] [[sources/web-04cef4e0ee|web-04cef4e0ee]] [[sources/web-96978ac98f|web-96978ac98f]]</details>
8. **Q:** What does a character body require?
   <details><summary>Answer</summary>15 *_Geo meshes, 15 outer cages parented to one empty, and 19 attachments in an armature. [[sources/off-avatar_character-bodies_export|off-avatar_character-bodies_export]] [[sources/off-avatar_character-bodies_specifications|off-avatar_character-bodies_specifications]] [[sources/web-2a50b96cb8|web-2a50b96cb8]] [[sources/web-6e2b07b559|web-6e2b07b559]]</details>
9. **Q:** What are Roblox's skinning limits?
   <details><summary>Answer</summary>At most 4 bone influences per vertex. No influences on Root or HumanoidRootNode. Bones frozen at scale 1 and rotation 0, with the root at 0,0,0. [[sources/off-art_modeling_skin-a-humanoid-model|off-art_modeling_skin-a-humanoid-model]] [[sources/off-art_modeling_specifications|off-art_modeling_specifications]] [[sources/off-studio_importer|off-studio_importer]] [[sources/off-avatar_character-bodies_specifications|off-avatar_character-bodies_specifications]]</details>
10. **Q:** What is the PBR accessory map size cap?
   <details><summary>Answer</summary>Normal, Roughness and Metalness are capped at 256x256, and ColorMap at 1024x1024. [[sources/off-dev_3816937|off-dev_3816937]]</details>
