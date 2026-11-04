<!-- cold: rbx-builder/assets-import.md | read when: read only when you copy chosen asset files into the project (ASSET-IMPORT.md steps). -->

## From agents/rbx-builder.md :: 4. Assets: pick from `$ASSETS/3d-models`, `textures`, `audio

4. Assets: pick from `$ASSETS/3d-models`, `textures`, `audio`, `hdris` via the rbx-assets logic. Rojo cannot sync FBX/OBJ/audio: copy the chosen files (plus license text) to `PROJECT/assets/` and write `PROJECT/docs/ASSET-IMPORT.md` (file, license, attribution duty, Studio steps: Asset Manager > Bulk Import, then put the ids into `Config.AssetIds`). Code must run with ids missing (procedural Parts, no sound). Catalog/Creator Store ideas are suggestions only.
