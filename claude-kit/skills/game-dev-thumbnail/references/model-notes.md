# Image-model naming: dated snapshot (HINT ONLY; do not use as truth)

Snapshot taken 2026-10-29 from Google's Gemini API docs (ai.google.dev, pages "Nano Banana" / "Image generation with Gemini"). Names and APIs change often, which is why `scripts/gen_image.py lookup` asks the user's own account for its current model list at run time, and why the skill live-checks the docs every run.

What the docs showed that day (nickname -> model id):
- Nano Banana 2.1 -> `gemini-nano-banana-2.1` (recommended for new projects)
- Nano Banana 2 Lite -> `gemini-3.1-flash-lite-image` (fastest, cheapest)
- Nano Banana 2 -> `gemini-3.1-flash-image` (previous generation)
- Nano Banana Pro -> `gemini-3-pro-image` (highest-complexity tasks, better text rendering)
- Nano Banana (original) -> `gemini-2.5-flash-image` (legacy)
Earlier pages that same day also showed `-preview` suffixed ids (`gemini-3.1-flash-image-preview`, `gemini-3-pro-image-preview`): preview ids come and go.

API shape that day: the docs' examples used the Interactions API (`POST /v1beta/interactions`, header `x-goog-api-key`, body `model`, `input` parts with `{"type":"image","mime_type","data"}`, `response_format` `{"type":"image","aspect_ratio","image_size"}` where sizes use an uppercase K such as 2K); earlier docs used `POST /v1beta/models/{model}:generateContent` with `generationConfig.responseModalities` and `imageConfig`. The script supports both and tries the documented one first. Up to 14 reference images; all outputs carry a SynthID watermark.

If a run finds something different, trust the run (live docs + the account's model list) and mention the difference in the report, so this snapshot can be refreshed when the vault is next updated.
