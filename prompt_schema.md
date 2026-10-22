# VPH file contract

The eight example files use the APAE v1 structure. Four files ending in `_template.yaml` are starter forms and may contain placeholders.

| Field | Complete example requirement |
|---|---|
| `title`, `version`, `category`, `engine_primary` | Nonempty strings; version uses major.minor.patch |
| `apae` | Nonempty `appearance`, `place`, `action`, and `emotion` strings |
| Primary engine block | A mapping with a nonempty `prompt` string matching `engine_primary` |
| `negatives` | At least three distinct strings, chosen for the brief |
| `variants` | At least two entries with unique `id`, nonempty `label`, and `change` |
| `license` | `MIT` |

Allowed categories: products, fashion, portraits, architecture, abstract, branding.

Templates use one of four shapes: a single prompt, `batch`, `brand_pack`, or `campaign`. Their placeholders are intentional. The validator checks the relevant shape and required sections without presenting them as completed examples.

`chatgpt_image_2`, `style_preset`, BMB `background`, `ar`, and `quality` are VPH planning metadata. Consult [engine adaptation](engine_comparison.md) before using an API.

No generated images or run records establish output quality in this repository. A valid file still requires a human review of its generated result.
