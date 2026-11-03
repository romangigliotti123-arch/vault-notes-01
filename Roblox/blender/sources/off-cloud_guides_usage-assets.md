---
type: research-source
id: off-cloud_guides_usage-assets
title: "Roblox Creator Docs: cloud_guides_usage-assets"
source_type: "web"
creator: "create.roblox.com"
url: "https://create.roblox.com/docs/cloud/guides/usage-assets"
published: "2026-10-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0027
relevance: 3
density: high
tags: ["research-source", "web", "automation-and-creator-workflows", "blender-roblox-export-import", "mesh-texture-limits", "other"]
---
# off-cloud_guides_usage-assets

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox Open Cloud Assets API guide: upload and update assets via single HTTP requests (Create Asset / Update Asset / Get Operation). Lists per-type formats, content types, and limits (20 MB per call, Animation/Audio/Decal/Video/Model rules). Covers API key and OAuth2 scopes (asset:read/asset:write), operation polling, and using uploaded assets in Studio via rbxassetid. Only .fbx content updates are supported.

## Claims
- c1: Create Asset and Update Asset endpoints allow one asset per call with file size up to 20 MB. *(doc, high; automation-and-creator-workflows)*
- c2: Model uploads accept .fbx, .gltf, .glb, .rbxm, .rbxmx and are imported as a Model containing MeshPart objects, uploaded as packages. *(doc, high; blender-roblox-export-import)*
- c3: Currently only .fbx asset content can be updated via Update Asset; each update creates a new version. *(doc, high; automation-and-creator-workflows)*
- c4: Docs recommend using the Studio Importer instead of the API for custom 3D models, since Importer offers 3D preview, error checks, and import settings. *(doc, high; automation-and-creator-workflows)*
- c5: Decal/Image uploads accept png, jpeg, bmp, tga and must be smaller than 8000x8000 pixels; not updatable. *(doc, high; mesh-texture-limits)*
- c6: Audio up to 7 minutes; 100 uploads/month if ID-verified, 10/month if not; not updatable. *(doc, high; automation-and-creator-workflows)*
- c7: Video uploads: mp4/mov up to 5 minutes, up to 4096x2160, up to 3.75 GB, 20 uploads/day for ID-verified 13+ users; not updatable. *(doc, high; automation-and-creator-workflows)*
- c8: Mesh type is Roblox-only: only content downloaded from the Asset Delivery API is accepted; otherwise use Importer. *(doc, high; automation-and-creator-workflows)*
- c9: Creating an API key requires the assets access permission plus Read/Write on the game per endpoint scope; all endpoints need x-api-key header. *(doc, high; automation-and-creator-workflows)*
- c10: Upload returns an operation path; poll Get Operation until done is true to get the assetId and moderationResult. *(doc, high; automation-and-creator-workflows)*
- c11: Uploaded assets are used in Studio via rbxassetid://<assetId>, or Datatype.Content.fromAssetId() for Content properties. *(doc, high; automation-and-creator-workflows)*
- c12: Metadata-only updates (displayName, description via updateMask) are not subject to the content upload limits. *(doc, medium; automation-and-creator-workflows)*
- c13: Source does not cover Blender, blender-mcp, bpy scripting, or Claude integration; relevance to the Blender pipeline is indirect. *(doc, high; other)*

## Numbers
- n1: **max file size per Create/Update call**: 20 MB 
- n2: **max decal/image dimensions**: smaller than 8000x8000 px 
- n3: **audio max duration**: 7 minutes 
- n4: **audio uploads per month**: 100 if ID-verified; 10 if not 
- n5: **video max duration / resolution / size**: 5 min, 4096x2160, 3.75 GB 
- n6: **video uploads per day**: 20 (ID-verified, 13+) 

## Techniques
- t1: **Upload FBX via Open Cloud**: POST multipart to apis.roblox.com/assets/v1/assets with request JSON (assetType Model, displayName, description, creationContext.creator.userId or groupId) and fileContent typed model/fbx. Poll operations/{id}.
- t2: **Versioned FBX update**: PATCH /assets/v1/assets/{assetId} with assetType, assetId, optional fileContent; add updateMask query for metadata changes. Creates new version; only .fbx supported.

### Code: Create a Model asset from an FBX file via Open Cloud
```bash
curl --location 'https://apis.roblox.com/assets/v1/assets' \
--header 'x-api-key: ${ApiKey}' \
--form 'request="{
  \"assetType\": \"Model\",
  \"displayName\": \"Name\",
  \"description\": \"This is a description\",
  \"creationContext\": {
    \"creator\": {
      \"userId\": \"${userId}\"
    }
  }
}"' \
--form 'fileContent=@"/filepath/model.fbx";type=model/fbx'
```

## Quotes (brief, for attribution)
> Currently, you can only update the asset content for .fbx files. The update creates a new version.  (create.roblox.com)
> Depending on your use-case, consider uploading custom 3D models manually using the Importer.  (create.roblox.com)

## Points to
- https://create.roblox.com/docs/cloud/reference/cloud/assets/v1.json
- https://create.roblox.com/docs/cloud/auth/api-keys
- https://create.roblox.com/docs/cloud/auth/oauth2-overview
- https://create.roblox.com/docs/studio/importer
- https://create.roblox.com/docs/projects/assets/packages
- https://create.roblox.com/docs/cloud/reference/domains/assetdelivery
