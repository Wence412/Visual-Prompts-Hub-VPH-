# Visual Prompts Hub (VPH)

By WenceStudio by SmartDesign.

Eight visual prompt examples and four planning templates for product photography, fashion, portraits, architecture, abstract textures, and brand imagery.

[![License: WenceStudio Library License](https://img.shields.io/badge/License-All%20rights%20reserved-lightgrey.svg)](LICENSE)
[![Validate prompts](https://github.com/Wence412/Visual-Prompts-Hub-VPH-/actions/workflows/validate-prompts.yml/badge.svg)](https://github.com/Wence412/Visual-Prompts-Hub-VPH-/actions/workflows/validate-prompts.yml)

## Start here

1. Open a prompt from the table below, or copy [prompt_template.yaml](prompt_template.yaml).
2. Describe Appearance, Place, Action, and Emotion (APAE). Add your references, framing, and lighting.
3. Copy the prompt text into your image tool. Translate the planning fields into controls supported by that tool.
4. Review the result against the brief before publishing. Change one variable at a time when comparing variants.

These are editable examples. [View the tested visuals and review notes](tested/README.md). They are not verified production outputs. This repository does not run image generation, enforce brand safety, or guarantee matching results across engines. Structural validation checks files, not images.

## Choose an example

| Example | Category | File |
|---|---|---|
| Premium studio watch | Products | [Watch](watch_dark_studio_premium.yaml) |
| Sculptural gold jewelry | Products | [Jewelry](jewelry_gold_editorial.yaml) |
| Minimal luxury shoe | Fashion | [Shoe](shoe_luxury_minimal.yaml) |
| Contrast jacket editorial | Fashion | [Jacket](jacket_editorial_contrast.yaml) |
| Dark editorial character | Portraits | [Character](editorial_character_dark.yaml) |
| Brutalist facade at dusk | Architecture | [Facade](facade_brutalist_dusk.yaml) |
| Charcoal and gold texture | Abstract | [Texture](texture_charcoal_gold.yaml) |
| Tech product hero | Branding | [Tech hero](hero_shot_tech_product.yaml) |

## Build a brief

| APAE field | What to specify |
|---|---|
| Appearance | Subject, materials, color, finish, and details that must remain consistent |
| Place | Environment, backdrop, surfaces, and light sources |
| Action | Pose, arrangement, viewpoint, and framing |
| Emotion | Intended mood and visual tone |

The BMB background labels describe sets: `practical`, `gradient`, `clean`, `cinematic`, `environment`, and `practical_with_props`. They are planning labels, not API values.

## Templates and guides

- [Single prompt](prompt_template.yaml), [batch](batch_template.yaml), [brand pack](brand_pack_template.yaml), and [campaign](campaign_template.yaml)
- [Getting started](getting_started.md) and [annotated watch example](wearable_hero_example.md)
- [Schema and field meanings](prompt_schema.md)
- [Engine adaptation](engine_comparison.md) and [prompt-writing notes](engine_notes.md)
- [Variant strategies](variant_strategies.md) and [brand review](brand_safe_guidelines.md)

The YAML key `chatgpt_image_2` is retained for compatibility with existing imports. It is a VPH label, not an API model ID. Fields such as `style_preset`, `ar`, and `quality: hd` express creative intent. Do not send this YAML directly to an API. Check the selected model and interface before mapping settings.

For a searchable collection, open [Prompt Packs Library](https://wence412.github.io/Prompt-Packs-library/image/). VPH source edits do not automatically update its imported copy.

## Validate and contribute

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_prompts.py
```

The validator checks all root YAML files, requires eight or more complete examples, and checks APAE fields, engine prompt blocks, variant IDs, and the license field. The four intentionally incomplete templates receive structural checks separately. It does not call image services.

Read [CONTRIBUTING.md](CONTRIBUTING.md), then open a pull request. Report problems through [Issues](https://github.com/Wence412/Visual-Prompts-Hub-VPH-/issues).

## License

[WenceStudio Visual Prompts Hub License](LICENSE) © 2026 WenceStudio by SmartDesign. Free to use in your own work, including client work. Do not republish, resell, mirror, or bulk-collect the prompts. Copies obtained before 23 October 2026 were released under the MIT License, and that earlier grant is not revoked. Review rights to any supplied references, trademarks, likenesses, and generated assets separately. Questions: hello@wencestudio.com.
