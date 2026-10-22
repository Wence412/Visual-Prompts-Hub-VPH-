# Engine adaptation guide

VPH stores creative direction separately from execution. Choose the tool and model you have access to, then map only supported controls.

## Read the YAML correctly

`chatgpt_image_2` is a legacy VPH key. It does not select a model. `style_preset` describes a photographic treatment, `ar` records an intended aspect ratio, and BMB `background` labels describe the set. `quality: hd` is historical planning metadata. None of these fields establishes an API contract.

OpenAI documents model-specific output controls in its [image generation guide](https://developers.openai.com/api/docs/guides/image-generation). Use that reference when setting size, quality, output format, or an API model ID. Do not infer pixel dimensions from words such as “4K” in a prompt.

## Adapt a prompt

1. Keep the subject, composition, reference constraints, and intended mood from APAE.
2. Copy the natural-language prompt. Include exclusions in the text if the interface has no separate negative control.
3. Select size and other execution controls in the tool itself.
4. If using an engine override, verify every flag against the selected engine version. Existing Midjourney, DALL-E 3, and SDXL blocks are historical examples, not a tested compatibility matrix.
5. Record the actual tool, model, settings, date, and output dimensions with the reviewed result.

There is no measured cross-engine ranking in this repository. Test the same brief before choosing a tool for a campaign. Reference images and repeated review can support continuity; exact identity or layout consistency is not guaranteed.
